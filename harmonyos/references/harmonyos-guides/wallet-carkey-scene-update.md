---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-carkey-scene-update
title: 更新车钥匙
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 数字车钥匙 > 开发场景 > 更新车钥匙
category: harmonyos-guides
scraped_at: 2026-09-24T06:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d31b3c7da5d3e05d937403ef14a03ebe23f552da6a8c4a3cc60701359de32c2b
---

当车钥匙信息发生变化时，车主App通知钱包更新实例数据，完成移动端数字车钥匙更新。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/ZXVVC5DARQunv3GEyXzt0w/zh-cn_image_0000002769331663.png)

## 服务端开发

收到车主App或者DK服务器管理台的更新请求之后，由DK服务器调用车钥匙更新到钱包服务器完成[更新车钥匙](../harmonyos-references/wallet-rest-api-carkey.md#车钥匙数据更新)。然后钱包服务器会推送更新请求给钱包App完成移动端的更新。

## 客户端开发（可选）

DK服务器调用钱包服务器接口[更新车钥匙](wallet-carkey-scene-update.md#服务端开发)为异步流程，可能存在延迟。车主App可以调用[updatePass](../harmonyos-references/wallet-walletpass.md#updatepass)接口，立刻触发钱包端云对账，及时更新车钥匙。

```typescript
async updatePass(): Promise<void> {
  const passStr = JSON.stringify({
    passType: this.passType,
  });
  try {
    const result = await this.walletPassClient.updatePass(passStr);
    const updatePassResult = JSON.parse(result) as UpdatePassResult;
    if (updatePassResult.result === '0') {
      console.info('Succeeded in updating pass');
    }
  } catch (err) {
    console.error(`Failed to update pass, code:${err.code} message:${err.message}`);
  }
}
```
