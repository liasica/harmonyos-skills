---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-generalcard-scene-view
title: 查看通用凭证
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 通用凭证 > 开发场景 > 查看通用凭证
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:42+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:d2046009bd2a062dc3f27f365c5e9131bcb8dadcb524a5e20906212797445285
---

查询已开通通用凭证的状态并展示，用户可以点击跳转钱包通用凭证详情页，查看和使用更多功能。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/qRgTgroPTReChUc6_QXjYw/zh-cn_image_0000002821838261.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=A88A30DA8B1CBDFA124065F2B013628B567471049154509272628722A988F761)

## 客户端开发

调用[queryPass](../harmonyos-references/wallet-walletpass.md#querypass)接口查询通用凭证信息。如果已经开通过该卡片，展示“去查看”按钮，点击后调用[viewPass](../harmonyos-references/wallet-walletpass.md#viewpass)接口跳转钱包通用凭证详情页。

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
