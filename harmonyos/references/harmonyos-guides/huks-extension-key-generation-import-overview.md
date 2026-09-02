---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-extension-key-generation-import-overview
title: 密钥生成与导入导出介绍
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 外部密钥管理扩展 > 密钥管理 > 密钥生成与导入导出介绍
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:32+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:b0a1b59668106e92b62c7c3723f7fca59474599c3eaad198429101cd64f962e2
---

从API版本26.0.0开始，HUKS提供密钥生成与导入导出能力，支持在外部密钥管理扩展场景下，在扩展设备内生成密钥对、导入加密封装的密钥对或导出公钥。

## 功能概述

在外部密钥管理扩展场景下，密钥生成与导入导出能力由[CryptoExtensionAbility](../harmonyos-references/js-apis-cryptoextensionability.md)提供，驱动厂商需继承CryptoExtensionAbility并实现相关接口。

### 密钥生成

密钥生成指在扩展设备内生成非对称密钥对（如RSA、ECC密钥对）。生成的密钥存储在扩展设备中，私钥不会离开扩展设备，公钥可通过导出接口获取。

应用通过调用HUKS的[generateKeyItem](../harmonyos-references/js-apis-huks.md#huksgeneratekeyitem9)接口发起密钥生成请求，请求被转发到CryptoExtensionAbility的[onGenerateKeyItem](../harmonyos-references/js-apis-cryptoextensionability.md#ongeneratekeyitem)接口完成密钥生成。

### 密钥安全导入

密钥安全导入指将加密封装的密钥对导入到扩展设备中。加密封装的密钥对通常由安全协商密钥加密，确保密钥在传输过程中不被泄露。

应用通过调用HUKS的[importWrappedKeyItem](../harmonyos-references/js-apis-huks.md#huksimportwrappedkeyitem9)接口发起密钥安全导入请求，请求被转发到CryptoExtensionAbility的[onImportWrappedKeyItem](../harmonyos-references/js-apis-cryptoextensionability.md#onimportwrappedkeyitem)接口完成密钥安全导入。

### 公钥导出

公钥导出指从扩展设备中导出指定密钥的公钥。导出的公钥可用于证书申请、密钥协商等场景。

应用通过调用HUKS的[exportKeyItem](../harmonyos-references/js-apis-huks.md#huksexportkeyitem9)接口发起公钥导出请求，请求被转发到CryptoExtensionAbility的[onExportKeyItem](../harmonyos-references/js-apis-cryptoextensionability.md#onexportkeyitem)接口完成公钥导出。

## 规格差异说明

以上接口复用HUKS原有接口定义。在外部密钥管理扩展场景下，params中的参数为可选参数，由Extension厂商定义支持范围。如未传入相应参数，厂商需设置默认行为。

* **密钥生成（generateKeyItem）**：推荐传入算法类型（HUKS\_TAG\_ALGORITHM）、密钥长度（HUKS\_TAG\_KEY\_SIZE）、密钥用途（HUKS\_TAG\_PURPOSE）等参数。如未传入，厂商需设置默认值。keyAlias需传入有效的资源ID。
* **密钥安全导入（importWrappedKeyItem）**：推荐传入算法类型、密钥长度、密钥用途等参数。keyAlias和wrappingKeyAlias需传入有效的资源ID。wrappedKey为封装密钥数据，格式由Extension厂商定义。
* **公钥导出（exportKeyItem）**：推荐传入密钥用途（HUKS\_TAG\_PURPOSE）参数，以便导出指定用途的公钥。如未传入，厂商需设置默认值（推荐默认签名用途）。keyAlias需传入有效的资源ID。

**说明** 

在外部密钥管理扩展场景下，keyAlias传入的是资源ID（resourceId），而非传统的密钥别名。keyAlias和wrappingKeyAlias需要保证其是有效的资源ID，即已通过[openResource](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptoopenresource)打开的资源，同时需要保证keyAlias和wrappingKeyAlias中包含的提供者名称（providerName）、外部扩展名称（abilityName）和应用包名（bundleName）内容一致。
