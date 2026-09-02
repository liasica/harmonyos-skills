---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-carkey-scene-view
title: 查看车钥匙
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 数字车钥匙 > 开发场景 > 查看车钥匙
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:33+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:18e1bb4d3a12315985c6156bd38531f3551977b3cfc90cf2a3d3a163c427eddb
---

查询已开通车钥匙的状态并展示，用户可以点击跳转钱包车钥匙详情页，查看和使用更多功能。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/i2-qkmZdRyOzaELJEzmVlQ/zh-cn_image_0000002736434381.png)

## 客户端开发

1. 车主App携带当前车辆信息和用户信息请求DK服务器查询车钥匙信息，获取到车钥匙唯一标识（organizationPassId）和账号+设备的唯一标识（pushToken的sha256签名值）。
2. 车主App调用[queryPassDeviceInfo](../harmonyos-references/wallet-walletpass.md#querypassdeviceinfo)接口，查询当前设备的设备类型、账号+设备标识等信息。与云侧获取的数据进行比对，端云一致则说明车钥匙开通在当前设备。

   ```typescript
   async queryPassDeviceInfo(): Promise<void> {
      const passStr = JSON.stringify({
         passType: this.passType,
         targetDeviceType: this.targetDeviceType
      });
      try {
         const result = await this.walletPassClient.queryPassDeviceInfo(passStr);
         const queryPassDeviceInfoResult = JSON.parse(result) as QueryPassDeviceInfoResult;
         this.passDeviceId = queryPassDeviceInfoResult.passDeviceId;
      } catch (err) {
         console.error(`Failed to query passDeviceInfo, code:${err.code} message:${err.message}`);
      }
   }
   ```
3. 车主App携带车钥匙唯一标识organizationPassId作为serialNumber，调用[queryPass](../harmonyos-references/wallet-walletpass.md#querypass)接口查询车钥匙是否可用，确认车钥匙当前状态是否为已激活。

   ```typescript
   async queryPass(): Promise<void> {
      const passStr = JSON.stringify({
         passType: this.passType,
         serialNumber: this.serialNumber
      });
      try {
         const result = await this.walletPassClient.queryPass(passStr);
         const queryPassResult = JSON.parse(result) as QueryPassResult[];
         if (queryPassResult.length > 0 && queryPassResult[0].cardStatus === '0') {
            // 该车钥匙当前状态已激活，开发者可以展示“去查看”按钮，点击后调用this.viewPass()跳转钱包车钥匙详情页。
         } else {
            // 无车钥匙或者车钥匙状态失效，展示“去开通”按钮，点击后进入车钥匙开通流程。
         }
      } catch (err) {
         console.error(`Failed to query pass, code:${err.code} message:${err.message}`);
      }
   }
   ```
4. 如果车钥匙在当前设备上已激活，展示“去查看”UI。用户点击之后，车主App调用[viewPass](../harmonyos-references/wallet-walletpass.md#viewpass)跳转钱包App车钥匙详情页。如果车钥匙未在设备上开通，需要展示“去开通”UI，点击进入开通流程。

   ```typescript
   async viewPass(): Promise<void> {
      const passStr = JSON.stringify({
         passType: this.passType,
         serialNumber: this.serialNumber
      });
      try {
         await this.walletPassClient.viewPass(passStr);
      } catch (err) {
         console.error(`Failed to view pass, code:${err.code} message:${err.message}`);
      }
   }
   ```
