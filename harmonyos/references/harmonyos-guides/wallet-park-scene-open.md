---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-park-scene-open
title: 开通园区卡
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 园区卡 > 开发场景 > 开通园区卡
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:33+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:1ea9239ff06e9c04d0647aa40bca5a744a5e0b7f7eb21c48dcd965979439e4cc
---

用户可以将园区卡添加至钱包，在钱包中方便查看卡片信息，亮证核验快速通行与消费，实现数字化便捷通行。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/nwrl3KQKQF6iQV-1jRrLNA/zh-cn_image_0000002706675306.png)

## 开发流程

| 序号 | 步骤 | 说明 |
| --- | --- | --- |
| 1 | 预置园区卡模板 | 服务端开发步骤1 |
| 2 | 检查是否满足开通条件 | 客户端开发步骤1 |
| 3 | 查询账号设备标识 | 客户端开发步骤3 |
| 4 | 推送园区卡实例 | 客户端开发步骤4、服务端开发步骤3 |
| 5 | 客户端开卡 | 客户端开发步骤5 |
| 6 | 开发者服务端与钱包服务端交互 | 服务端开发步骤5 |
| 7 | NFC相关事件回调通知接口（可选） | 服务端开发步骤6 |

## 服务端开发

1. 开发者服务器首先调用[预置模板](../harmonyos-references/wallet-rest-api-park.md#预置模板)接口向Wallet Kit服务器推送样式数据，如底图、商户LOGO，背景色等。样式数据预置后，开发者可以在实例数据中指定模板标识，即可使用模板指定的样式数据在手机端进行园区卡展示。当展示使用的模板数据更新后，已开通的卡片均会展示最新样式。
2. 用户点击开通园区卡时，开发者端侧向开发者云侧服务请求开卡，此部分属于开发者内部实现，注意携带端侧通过queryPassDeviceInfo接口获取的passDeviceId，用于生成JWE，其他实现符合自身的端云鉴权要求即可。
3. 开发者服务器收到端侧请求后，调用[申请园区卡](../harmonyos-references/wallet-rest-api-park.md#申请园区卡)接口推送用户园区卡数据给Wallet Kit服务器，数据中需要指定选用的模板标识作为样式数据进行展示。
4. 推送成功后获取实例标识，组装一次性开卡凭证JWE后，作为前述端侧请求的结果返回给端侧。
5. 端侧跳转钱包后，钱包会通过服务器接口依次调用开发者服务器提供的[设备认证](../harmonyos-references/wallet-rest-api-public.md#设备认证)、[获取个人化数据token](../harmonyos-references/wallet-rest-api-public.md#获取个人化数据token)、[获取个人化数据](../harmonyos-references/wallet-rest-api-public.md#获取个人化数据)接口，获取园区卡的密钥数据及卡面的个性化数据，写入安全芯片后完成开卡。
6. 如需获取园区卡的开通结果，开发者可实现[NFC相关事件回调通知接口](../harmonyos-references/wallet-rest-api-public.md#nfc相关事件回调通知接口)（可选）。

## 客户端开发

1. 用户进入开发者提供的管理页面时，通过[canAddPass](../harmonyos-references/wallet-walletpass.md#canaddpass)接口检测当前设备是否支持开通园区卡，具体如下：

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
2. 检测到当前设备支持开通园区卡后，展示开通按钮，引导用户开通园区卡到钱包。
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
4. 开发者客户端携带设备信息请求开发者服务器，由开发者服务器申请园区卡，然后将生成的JWE数据返回客户端。
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
