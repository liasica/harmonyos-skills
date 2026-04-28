---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/recoverykey-get-authchallenge
title: 获取挑战值
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 企业恢复密钥 > 获取挑战值
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3683b5667517e5a5f98c68bd4b8b4d5fa411386bf5edddf9001ba9a9e1511284
---

## 场景介绍

请求获取挑战值，在发起更新企业公钥证书、删除已有企业恢复密钥流程前，需要获取挑战值，并进行签名，以确认企业身份。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/dataguard-recoverykey.md)。

| 接口名 | 描述 |
| --- | --- |
| [getAuthChallenge](../harmonyos-references/dataguard-recoverykey.md#getauthchallenge)(): Promise<Uint8Array> | 使用Promise方式获取挑战值。 |

## 开发步骤

1. 导入模块。

   ```
   1. import { recoveryKey } from '@kit.EnterpriseDataGuardKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用接口[getAuthChallenge](../harmonyos-references/dataguard-recoverykey.md#getauthchallenge)，获取挑战值。

   ```
   1. function testGetAuthChallenge() {
   2. recoveryKey.getAuthChallenge().then((challenge: Uint8Array) => {
   3. console.info(`Succeeded in getting challenge.`);
   4. }).catch((error: BusinessError) => {
   5. console.error(`Failed to get challenge. Code: ${error.code}, message: ${error.message}`);
   6. });
   7. }
   ```
