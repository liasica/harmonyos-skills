---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-carkey-scene-open
title: 开通车钥匙
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 数字车钥匙 > 开发场景 > 开通车钥匙
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:21+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:0bec02a76e45bdf452a6c0b1d9a56acc0baf08582e47a262bfe2f74b133d98d2
---

用户可将车钥匙添加至钱包，实现刷卡开车门、无感解闭锁、远程车控等便捷能力。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/_kKxYNkaSB2Hk3nwNZijUg/zh-cn_image_0000002712405432.png)

## 开发流程

| 序号 | 步骤 | 说明 |
| --- | --- | --- |
| 1 | 预置车钥匙模板 | 服务端调用预置模板接口，将公共信息写入模板用于关联车钥匙实例。 |
| 2 | 检查是否满足开通条件 | 开通前，客户端需要检查设备是否支持开通车钥匙。 |
| 3 | 查询账号设备标识 | 客户端获取账号设备标识。 |
| 4 | 推送车钥匙实例 | 客户端携带设备信息请求服务器，服务端申请钥匙并返回JWE数据给客户端。 |
| 5 | 客户端开卡 | 客户端携带JWE拉起钱包完成车钥匙开通。 |
| 6 | DK服务端与钱包服务端交互 | 服务端依次处理设备认证、获取个人化数据token、获取个人化数据请求。 |
| 7 | NFC相关事件回调通知接口 | 车钥匙开通成功后，钱包通过回调通知DK服务器。 |

## 服务端开发

1. DK服务器调用钱包服务器进行[预置模板](../harmonyos-references/wallet-rest-api-carkey.md#预置模板)，将一些公共信息写入模板用于后面关联车钥匙实例。
2. 收到车主App的申请请求之后，由DK服务器[申请ICCE钥匙](../harmonyos-references/wallet-rest-api-carkey.md#申请icce钥匙)，然后将生成的车钥匙JWE数据返回车主App。
3. 激活车钥匙过程中，DK服务器依次收到钱包App（经过钱包服务器代理）的[设备认证](../harmonyos-references/wallet-rest-api-public.md#设备认证)、[获取个人化数据token](../harmonyos-references/wallet-rest-api-public.md#获取个人化数据token)、[获取个人化数据](../harmonyos-references/wallet-rest-api-public.md#获取个人化数据)请求，返回结果给钱包App。
4. 当车钥匙开通成功之后，DK服务器通过[NFC相关事件回调通知接口](../harmonyos-references/wallet-rest-api-public.md#nfc相关事件回调通知接口)接收到开通成功回调通知，请求体中包含账号+设备的唯一标识pushToken（此为原值，非sha256签名值）。DK服务器需要记录车钥匙唯一标识organizationPassId和账号+设备唯一标识pushToken的sha256签名值之间的关联关系，用于后续车主App端云对账展示车钥匙。

## 客户端开发

完整示例请参考[客户端示例代码](https://gitcode.com/HarmonyOS_Samples/wallet-kit-for-harmony-os_demo)。

1. 车主App调用[canAddPass](../harmonyos-references/wallet-walletpass.md#canaddpass)接口检查当前是否可以开通车钥匙，如果不满足开通条件，请按照返回结果及错误码进行引导处理。

   ```typescript
   async canAddPass(): Promise<boolean> {
      // 不支持nfc的设备，不支持开通。
      if (!canIUse('SystemCapability.Communication.NFC.Core')) {
         return false;
      }
      // 检查钱包环境是否支持开通。
      const passStr = JSON.stringify({
         passType: this.passType,
         targetDeviceType: this.targetDeviceType
      });
      try {
         const result = await this.walletPassClient.canAddPass(passStr);
         const canAddPassResult = JSON.parse(result) as CanAddPassResult[];
         // 如果targetDeviceType只传了phone或者wear，则取数组首项判断，如果传了all，第一项为手机，第二项为穿戴，此处按实际情况进行判断。
         if (canAddPassResult[0].result === '0') {
            return true;
         } else {
            // 根据结果码对应提示用户升级系统版本或者钱包版本。
            return false;
         }
      } catch (err) {
         console.error(`Failed to check, code:${err.code} message:${err.message}`);
         if (err.code === 1010200003) {
            // 钱包App环境未准备好，需要执行初始化环境，需要避免重复调用接口反复拉起钱包App的情况。
            await this.walletPassClient.initWalletEnvironment(JSON.stringify({ targetDeviceType: this.targetDeviceType }));
            return false;
         }
         // 其他错误码，请按照对应场景，友好引导或提示用户进行下一步操作。
         return false;
      }
   }
   ```
2. 车主App调用[queryPassDeviceInfo](../harmonyos-references/wallet-walletpass.md#querypassdeviceinfo)接口，查询当前设备的设备类型、账号+设备标识等信息。

   ```typescript
   async queryPassDeviceInfo(): Promise<void> {
      const passStr = JSON.stringify({
         passType: this.passType,
         targetDeviceType: this.targetDeviceType
      });
      try {
         const result = await this.walletPassClient.queryPassDeviceInfo(passStr);
         const queryPassDeviceInfoResult = JSON.parse(result) as QueryPassDeviceInfoResult;
         // 获取到passDeviceId之后，携带此参数调用开发者服务器接口申请开卡，获取返回的一次性开卡凭证JWE，然后进行开卡。
         // 该值格式为"A|B"，其中A为标识账号+设备的唯一标识（pushToken的sha256签名值），由钱包服务器生成。B为设备udid+接口入参中传入的passType（sha256签名值），由钱包端侧生成。
         this.passDeviceId = queryPassDeviceInfoResult.passDeviceId;
         // 开发者对于车钥匙支持能力的显示，需要结合该值的返回值。
         // 如果车端支持UWB，但当前设备不支持UWB，则车主APP不应显示UWB相关内容。
         // 如果车端支持SLE，但当前设备不支持SLE，则车主APP不应显示SLE相关内容。
         this.deviceCapabilities = queryPassDeviceInfoResult.deviceCapabilities;
      } catch (err) {
         console.error(`Failed to query passDeviceInfo, code:${err.code} message:${err.message}`);
      }
   }
   ```
3. 车主App携带设备信息请求DK服务器，由DK服务器申请ICCE钥匙，然后将生成的车钥匙JWE数据返回车主App。
4. 车主App携带车钥匙JWE数据调用[addPass](../harmonyos-references/wallet-walletpass.md#addpass)接口跳转钱包开卡预览页，点击“立即添加”后进入激活车钥匙过程并完成车钥匙开通，车主App可以通过addPass接口的返回值接收开通结果。

   ```typescript
   async addPass(): Promise<void> {
      const passStr = JSON.stringify({
         jweContent: this.jweContent
      });
      try {
         const result = await this.walletPassClient.addPass(passStr);
         const addPassResult = JSON.parse(result) as AddPassResult;
         // 开卡成功，获取到卡片数据，进行页面刷新。
         console.info(`Successed in adding pass, serialNumber:${addPassResult.serialNumber}, passDeviceId:${addPassResult.passDeviceId}`);
      } catch (err) {
         console.error(`Failed to add pass, code:${err.code} message:${err.message}`);
      }
   }
   ```
