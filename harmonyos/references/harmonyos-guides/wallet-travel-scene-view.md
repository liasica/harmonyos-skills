---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-travel-scene-view
title: 查看出行凭证
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 出行凭证 > 开发场景 > 查看出行凭证
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:22+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:73596a4ae4d17f6ae2d2f337ee1cdb15f123d0ed3e227305f91b4877f3033691
---

查询已开通出行凭证的状态并展示，用户可以点击跳转钱包出行凭证详情页，查看和使用更多功能。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/IxgMxYJARxq45AbMBq36AA/zh-cn_image_0000002742004441.png)

## 客户端开发

调用[queryPass](../harmonyos-references/wallet-walletpass.md#querypass)接口查询出行凭证信息。如果已经开通过该卡片，展示“去查看”按钮，点击后调用[viewPass](../harmonyos-references/wallet-walletpass.md#viewpass)接口跳转钱包出行凭证详情页。

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
      // 该卡片当前状态已激活，开发者可以展示“去查看”按钮，点击后调用this.viewPass()跳转钱包卡片详情页。
      } else {
      // 无卡片或者卡片状态失效，展示“去开通”按钮，点击后进入卡片开通流程。
      }
   } catch (err) {
      console.error(`Failed to query pass, code:${err.code}, message:${err.message}`);
   }
}

async viewPass(): Promise<void> {
   const passStr = JSON.stringify({
      passType: this.passType,
      serialNumber: this.serialNumber
   });
   try {
      await this.walletPassClient.viewPass(passStr);
   } catch (err) {
      console.error(`Failed to view pass, code:${err.code}, message:${err.message}`);
   }
}
```
