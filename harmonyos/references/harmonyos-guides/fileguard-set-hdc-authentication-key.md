---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-set-hdc-authentication-key
title: 设置HDC认证密钥
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 文件分级管控 > 设置HDC认证密钥
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:02+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:07104e855f5720d2759b131655179d4db68d56b6ba6e2dbdad0bab0e4ee126f3
---

从6.1.1(24)版本开始，新增设置[HDC](hdc.md)认证密钥接口，支持用户在企业设备上开展安全调试，进一步强化设备安全性。

## 场景介绍

该接口可为上位机和下位机配置HDC认证密钥，确保仅在双方均为企业设备的特定场景下才允许连接和调试，从而有效保障企业资产不被篡改和泄露。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/dataguard-fileguard.md)。

| 接口名 | 描述 |
| --- | --- |
| [setHdcAuthenticationKey](../harmonyos-references/dataguard-fileguard.md#sethdcauthenticationkey)(devType: AuthenticateDeviceType, keyType: AuthenticateKeyType, key: Uint8Array): Promise<void> | 使用Promise方式设置上下位机间的HDC认证密钥。 |

## 开发步骤

1. 应用需要通过OpenSSL在本地生成一个3072位的RSA密钥对。

   通过OpenSSL生成私钥：

   ```bash
   openssl genpkey -algorithm RSA -out private_key_3072.pem -pkeyopt rsa_keygen_bits:3072
   ```

   根据私钥提取公钥：

   ```bash
   openssl rsa -in private_key_3072.pem -pubout -out public_key_3072.pem
   ```
2. 导入模块。

   ```typescript
   import { BusinessError } from '@kit.BasicServicesKit';
   import { fileGuard } from '@kit.EnterpriseDataGuardKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
3. 初始化[FileGuard](../harmonyos-references/dataguard-fileguard.md#fileguard)对象guard，调用接口[setHdcAuthenticationKey](../harmonyos-references/dataguard-fileguard.md#sethdcauthenticationkey)，设置上下位机之间的HDC认证密钥。上位机需要下发私钥，下位机下发公钥，从而实现上位机对下位机的安全调试。

   ```typescript
   const TAG: string = 'FileGuard_HDCAuthenticationKey';
   const DOMAIN: number = 0x0000;

   /**
    * 设置上下位机间的HDC认证密钥。使用Promise异步回调。
    * 示例仅供参考，调用时需要分别设置上位机的私钥以及下位机的公钥，才能进行HDC安全调试。
    */
   function testSetHdcAuthenticationKey() {
     let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
     let devType: fileGuard.AuthenticateDeviceType = fileGuard.AuthenticateDeviceType.UPPER;
     let keyType: fileGuard.AuthenticateKeyType = fileGuard.AuthenticateKeyType.PRIVATE_KEY;
     // 将对应的密钥转为Uint8Array类型
     let key: Uint8Array = new Uint8Array([0]);

     guard.setHdcAuthenticationKey(devType, keyType, key).then(() => {
       hilog.info(DOMAIN, TAG, `Succeeded in setting the HDC authentication key.`);
     }).catch((error: BusinessError) => {
       hilog.error(DOMAIN, TAG,
         `Failed to set the HDC authentication key. Code: ${error.code}, message: ${error.message}.`);
     })
   }
   ```
