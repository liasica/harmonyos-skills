---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-hotel-scene-view
title: 查看酒店房卡
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 酒店房卡 > 开发场景 > 查看酒店房卡
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:41+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:3450ee64f387ebf9afabae97bd65f5a405f2f1d59c1e78e4e1613ca41a79f69d
---

查询已开通酒店房卡的状态并展示，用户可以点击跳转钱包酒店房卡详情页，查看和使用更多功能。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/sIpEhdnAT8uPNbGf4GQIFQ/zh-cn_image_0000002793038332.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=8295432615632F57135F2F8BEDCD62662AB8635E1C75E2995DEE046DB5E0A34F)

## 客户端开发

调用[queryPass](../harmonyos-references/wallet-walletpass.md#querypass)接口查询酒店房卡信息。如果已经开通过该卡片，展示“去查看”按钮，点击后调用[viewPass](../harmonyos-references/wallet-walletpass.md#viewpass)接口跳转钱包酒店房卡详情页。

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
