---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-park-scene-view
title: 查看园区卡
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 园区卡 > 开发场景 > 查看园区卡
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:33+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:37b15585cbae912e6145d2d4413d100d13abd230ea27bc5c36ff338778882636
---

查询已开通园区卡的状态并展示，用户可以点击跳转钱包园区卡详情页，查看和使用更多功能。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/WfnKa_E3R_SAlHMZznpF5Q/zh-cn_image_0000002817427727.png?HW-CC-KV=V1&HW-CC-Date=20261114T004649Z&HW-CC-Expire=31536000000&HW-CC-Sign=7758DE2AB3BB5AEB6D57FC6E72335B389C24C99412FC054CFF176910EDE3EF0E)

## 客户端开发

调用[queryPass](../harmonyos-references/wallet-walletpass.md#querypass)接口查询园区卡信息。如果已经开通过该卡片，展示“去查看”按钮，点击后调用[viewPass](../harmonyos-references/wallet-walletpass.md#viewpass)接口跳转钱包园区卡详情页。

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
