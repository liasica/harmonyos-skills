---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-carkey-scene-delete
title: 删除车钥匙
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 数字车钥匙 > 开发场景 > 删除车钥匙
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:21+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:aa7cb4b1eeaab7e2138590e1c78c589dcbf37554eada99f97131a2328e80c782
---

用户手动或系统自动删除车钥匙，从设备安全芯片中移除车钥匙数据。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/AL0Q1ye4Rt21vFwcpj8BRg/zh-cn_image_0000002742124383.png)

## 服务端开发

### 删除车钥匙

删除车钥匙的场景主要包括：用户手动触发删除、DK服务器管理台触发删除、车钥匙使用权限到期后的系统自动触发删除以及用户在钱包App执行车钥匙迁移成功之后触发删除。

其中用户在钱包App执行车钥匙迁移成功之后触发删除的具体实现，请参照[迁移车钥匙](wallet-carkey-scene-migration.md)章节。

其他删除场景的服务端开发参考[更新车钥匙](../harmonyos-references/wallet-rest-api-carkey.md#车钥匙数据更新)，采用PATCH方式进行局部更新，请求体如下：

```json
{
  "fields": {
    "status": {
      "state": "expired"
    }
  }
}
```

### 删除成功回调

当车钥匙删除成功之后，钱包App携带删除成功回调请求钱包服务器，钱包服务器通过[NFC相关事件回调通知接口](../harmonyos-references/wallet-rest-api-public.md#nfc相关事件回调通知接口)通知DK服务器，请求体中包含账号+设备的唯一值标识pushToken（pushToken需要使用原值，非sha256签名值）。

DK服务器需要对原有的车钥匙唯一标识organizationPassId和账号+设备的唯一标识pushToken（pushToken需要使用sha256签名值）的关联关系进行删除。

## 客户端开发（可选）

DK服务器调用钱包服务器接口[删除车钥匙](wallet-carkey-scene-delete.md#服务端开发)为异步流程，可能存在延迟。车主App可以调用[deletePass](../harmonyos-references/wallet-walletpass.md#deletepass)接口，立刻触发钱包端云对账，及时删除车钥匙。

```typescript
async deletePass(): Promise<void> {
  const passStr = JSON.stringify({
    passType: this.passType,
  });
  try {
    const result = await this.walletPassClient.deletePass(passStr);
    const deletePassResult = JSON.parse(result) as DeletePassResult;
    if (deletePassResult.result === '0') {
      console.info('Succeeded in deleting pass');
    }
  } catch (err) {
    console.error(`Failed to delete pass, code:${err.code} message:${err.message}`);
  }
}
```
