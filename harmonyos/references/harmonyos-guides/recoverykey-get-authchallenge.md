---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/recoverykey-get-authchallenge
title: 获取挑战值
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 企业恢复密钥 > 获取挑战值
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:02+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:d1dcc0de076cfdbe01de883ff47742d3c7ef05665701d71393b924d3cefc6cd5
---

## 场景介绍

请求获取挑战值，在发起更新企业公钥证书、删除已有企业恢复密钥流程前，需要获取挑战值，并进行签名，以确认企业身份。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/dataguard-recoverykey.md)。

| 接口名 | 描述 |
| --- | --- |
| [getAuthChallenge](../harmonyos-references/dataguard-recoverykey.md#recoverykeygetauthchallenge)(): Promise<Uint8Array> | 使用Promise方式获取挑战值。 |

## 开发步骤

1. 导入模块。

   ```typescript
   import { buffer } from '@kit.ArkTS';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { recoveryKey } from '@kit.EnterpriseDataGuardKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 调用接口[getAuthChallenge](../harmonyos-references/dataguard-recoverykey.md#recoverykeygetauthchallenge)，获取挑战值。

   ```typescript
   const TAG: string = 'EnterpriseRecoveryKey_GetChallenge';
   const DOMAIN: number = 0x0000;

   /**
    * 获取挑战值。使用Promise异步回调。
    */
   function getAuthChallenge() {
     recoveryKey.getAuthChallenge().then((challenge: Uint8Array) => {
       hilog.info(DOMAIN, TAG, `Succeeded in getting challenge. challenge is: ${buffer.from(challenge).toString('hex')}`);
     }).catch((error: BusinessError) => {
       hilog.error(DOMAIN, TAG, `Failed to get challenge. Code: ${error.code}, message: ${error.message}`);
     });
   }
   ```
