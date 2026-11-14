---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-member-scene-view
title: 查看会员卡
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 会员卡 > 开发场景 > 查看会员卡
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:34+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:835fb296bd94b17a8b4a44cac5c73376e178d675005150f4e5274a8d1aded22d
---

查询已开通会员卡的状态并展示，用户可以点击跳转钱包会员卡详情页，查看和使用更多功能。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/11IfyxjSTJew3o1ISXcPJg/zh-cn_image_0000002817507803.png?HW-CC-KV=V1&HW-CC-Date=20261114T004834Z&HW-CC-Expire=31536000000&HW-CC-Sign=653CF92016DB03BEBD24F2681341D4EF091809F0E86A012415C9E71F3DED1E9D)

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
