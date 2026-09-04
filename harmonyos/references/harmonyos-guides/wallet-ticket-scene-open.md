---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-ticket-scene-open
title: 开通活动/景点门票
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 活动/景点门票 > 开发场景 > 开通活动/景点门票
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:22+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:472f9aa8841bf6a9dd7dec366eebc92f6e52cf9c4cf536b0025b4c64d356994e
---

用户购买门票后，可以将电子门票添加至钱包，刷手机快速验票入场，提升验票体验和运营效率。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/Z4LnafagQ9aJKQGL0fhAHg/zh-cn_image_0000002712245492.png)

## 开发流程

| 序号 | 步骤 | 说明 |
| --- | --- | --- |
| 1 | 预置活动/景点门票模板 | 服务端开发步骤1 |
| 2 | 检查是否满足开通条件 | 客户端开发步骤1 |
| 3 | 查询账号设备标识 | 客户端开发步骤3 |
| 4 | 推送活动/景点门票实例 | 客户端开发步骤4、服务端开发步骤3 |
| 5 | 客户端开卡 | 客户端开发步骤5 |
| 6 | 开发者服务端与钱包服务端交互 | 服务端开发步骤5 |
| 7 | NFC相关事件回调通知接口（可选） | 服务端开发步骤6 |

## 服务端开发

1. 开发者服务器首先调用[预置模板](../harmonyos-references/wallet-rest-api-generalcard.md#预置模板)接口向Wallet Kit服务器推送样式数据，如底图、商户LOGO，背景色等。样式数据预置后，开发者可以在实例数据中指定模板标识，即可使用模板指定的样式数据在手机端进行门票展示。当展示使用的模板数据更新后，已开通的卡片均会展示最新样式。
2. 用户点击开通活动/景点门票时，开发者端侧向开发者云侧服务请求开卡，该请求需要携带queryPassDeviceInfo接口获取到的passDeviceId，用于生成JWE，其他实现符合自身的端云鉴权要求即可。
3. 开发者服务器收到端侧请求后，调用[申请活动/景点门票](../harmonyos-references/wallet-rest-api-ticket.md#申请门票)接口推送用户活动/景点门票数据给Wallet Kit服务器，数据中需要指定选用的模板标识作为样式数据进行展示。如需支持自动推送卡券，开发者服务器需留存用户授权结果，并生成spOpenId用于关联用户在开发者侧的账号。
4. 开发者服务器推送门票数据成功后，需获取Wallet Kit服务器返回的实例标识，并组装一次性开卡凭证JWE返回给端侧。

   如需支持自动推送卡券，还需将spOpenId一并返回。
5. 端侧跳转钱包后，钱包会通过服务器接口依次调用开发者服务器提供的[设备认证](../harmonyos-references/wallet-rest-api-public.md#设备认证)、[获取个人化数据token](../harmonyos-references/wallet-rest-api-public.md#获取个人化数据token)、[获取个人化数据](../harmonyos-references/wallet-rest-api-public.md#获取个人化数据)接口，获取活动/景点门票的密钥数据及卡面的个性化数据，写入安全芯片后完成开卡。

   如需支持自动推送卡券，开发者服务器还需实现[账号关联](../harmonyos-references/wallet-rest-api-public.md#账号关联)能力。
6. 如需获取活动/景点门票的开通结果，开发者可实现[NFC相关事件回调通知接口](../harmonyos-references/wallet-rest-api-public.md#nfc相关事件回调通知接口)（可选）。

## 客户端开发

1. 用户进入开发者提供的管理页面时，通过[canAddPass](../harmonyos-references/wallet-walletpass.md#canaddpass)接口检测当前设备是否支持开通活动/景点门票，具体如下：

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
2. 检测到当前设备支持开通活动/景点门票后，展示开通按钮，引导用户开通活动/景点门票到钱包。如需支持自动推送卡券，在用户点击开通时需要弹出授权提醒，记录授权结果并在后续请求中携带。
3. 调用[queryPassDeviceInfo](../harmonyos-references/wallet-walletpass.md#querypassdeviceinfo)接口，查询当前设备的设备类型、账号+设备标识等信息。如需支持自动推送卡券，需要携带autoPushPassFlag参数并设置为“1”，同时获取openId用于后续账号关联。
4. 开发者客户端携带设备信息请求开发者服务器，由开发者服务器申请活动/景点门票，然后将生成的JWE数据返回客户端。如需支持自动推送卡券，需同时携带用户授权结果，开发者服务器返回JWE和spOpenId给客户端。
5. 开发者客户端携带JWE数据，调用[addPass](../harmonyos-references/wallet-walletpass.md#addpass)跳转钱包进行开卡。如需支持自动推送卡券，需要同时携带autoPushPassFlag和spOpenId参数。
