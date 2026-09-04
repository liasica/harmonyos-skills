---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-member-scene-view
title: 查看会员卡
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 会员卡 > 开发场景 > 查看会员卡
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:22+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:83b57793d20ca66e7019278ac33a3eca76baccd43f862a7d95367d6f05686a62
---

查询已开通会员卡的状态并展示，用户可以点击跳转钱包会员卡详情页，查看和使用更多功能。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/dMjivAbuRx-56ZZNML5q_g/zh-cn_image_0000002742004441.png)

## 客户端开发

调用[queryPass](../harmonyos-references/wallet-walletpass.md#querypass)接口查询会员卡信息。如果已经开通过该卡片，展示“去查看”按钮，点击后调用[viewPass](../harmonyos-references/wallet-walletpass.md#viewpass)接口跳转钱包会员卡详情页。

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
