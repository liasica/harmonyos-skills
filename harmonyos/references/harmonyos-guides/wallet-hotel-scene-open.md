---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-hotel-scene-open
title: 开通酒店房卡
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 酒店房卡 > 开发场景 > 开通酒店房卡
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:33+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:4d9554644fea489fe1f315881ff09521e3687f5f8087f1e24f6ccf50babccfef
---

用户线上预定酒店后，可以将房卡添加至钱包，在钱包中方便查看房号、入住有效期等信息，刷手机轻碰门锁即可通行电梯、房门。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/vT-9rVwjTT-aBkkM3iH26Q/zh-cn_image_0000002706675320.png)

## 开发流程

| 序号 | 步骤 | 说明 |
| --- | --- | --- |
| 1 | 预置酒店房卡模板 | 服务端开发步骤1 |
| 2 | 检查是否满足开通条件 | 客户端开发步骤1 |
| 3 | 查询账号设备标识 | 客户端开发步骤3 |
| 4 | 推送酒店房卡实例 | 客户端开发步骤4、服务端开发步骤2 |
| 5 | 客户端开卡 | 客户端开发步骤5 |
| 6 | 开发者服务端与钱包服务端交互 | 服务端开发步骤3 |
| 7 | NFC相关事件回调通知接口（可选） | 服务端开发步骤4 |
| 8 | 酒店房卡更新 | 服务端开发步骤5 |

## 服务端开发

1. 开发者服务器调用钱包服务器进行[预置模板](../harmonyos-references/wallet-rest-api-hotel.md#预置模板)，将一些公共信息写入模板用于后面关联酒店房卡实例。
2. 收到开发者端侧的申请请求之后，由开发者服务器[申请酒店房卡](../harmonyos-references/wallet-rest-api-hotel.md#申请酒店房卡)，然后将生成的酒店房卡JWE数据返回开发者端侧。
3. 激活酒店房卡过程中，开发者服务器收到钱包App（经过钱包服务器代理）的[获取酒店个人化数据](../harmonyos-references/wallet-rest-api-hotel.md#获取酒店个人化数据)请求，返回结果给钱包App。
4. 当酒店房卡开通成功之后，开发者服务器通过[NFC相关事件回调通知接口](../harmonyos-references/wallet-rest-api-public.md#nfc相关事件回调通知接口)接收到开通成功回调通知（eventType：RECEIVE\_CARD）。
5. 当用户已开通的酒店房卡数据变更（如更换新的房间号），开发者服务器需要通知钱包服务器进行[酒店房卡数据更新](../harmonyos-references/wallet-rest-api-hotel.md#酒店房卡数据更新)。钱包端侧需要申请最新酒店房卡数据，钱包服务器会向开发者服务器重新触发[获取酒店个人化数据](../harmonyos-references/wallet-rest-api-hotel.md#获取酒店个人化数据)请求，获取结果后将激活和更新数据写入安全芯片。

## 客户端开发

1. 用户进入开发者提供的管理页面时，通过[canAddPass](../harmonyos-references/wallet-walletpass.md#canaddpass)接口检测当前设备是否支持开通酒店房卡，具体如下：

   ```typescript
   async canAddPass(): Promise<boolean> {
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
         console.error(`Failed to check, code:${err.code}, message:${err.message}`);
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
2. 检测到当前设备支持开通酒店房卡后，展示开通按钮，引导用户开通酒店房卡到钱包。
3. 调用[queryPassDeviceInfo](../harmonyos-references/wallet-walletpass.md#querypassdeviceinfo)接口，查询当前设备的设备类型、账号+设备标识等信息。

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
         this.passDeviceId = queryPassDeviceInfoResult.passDeviceId;
      } catch (err) {
         console.error(`Failed to query passDeviceInfo, code:${err.code} message:${err.message}`);
      }
   }
   ```
4. 开发者客户端携带设备信息请求开发者服务器，由开发者服务器申请酒店房卡，然后将生成的JWE数据返回客户端。
5. 开发者客户端携带JWE数据，调用[addPass](../harmonyos-references/wallet-walletpass.md#addpass)跳转钱包进行开卡。涉及芯片数据写入，需要完成安全芯片初始化等动作，预计开卡时间30秒左右，开通完成后钱包内可以看到对应的卡片。

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
