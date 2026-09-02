---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-ukey-pin-authentication-management-overview
title: UKey PIN码认证介绍及规格
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 外部密钥管理扩展 > UKeyPIN码认证管理 > UKey PIN码认证介绍及规格
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:32+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:2871ad12afe8c2beb775cad0df86f594f948df7f350d630750da528c1d318b89
---

PIN（Personal Identification Number）码是UKey设备的安全访问凭证，采用“硬件设备+PIN码”的双因子认证模式。用户必须同时拥有物理UKey设备和正确的PIN码才能访问设备内的密钥材料。

PIN码作用如下：

1. 防暴力破解：连续错误输入达到一定次数（与驱动应用实现的外部密钥管理扩展能力相关）后自动锁定。
2. 硬件级安全：PIN码验证在UKey硬件内完成，敏感信息不出硬件。

UKey使用resourceId标识UKey资源，生态应用打开资源之后，如需要操作resourceId对应的私钥执行签名操作，则需要先验证PIN码。

## PIN码认证状态管理

HUKS提供以下PIN码认证状态管理能力：

* **查询认证状态**：通过[getUkeyPinAuthState](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptogetukeypinauthstate)查询当前PIN码认证状态。
* **清除认证状态**：从API版本26.0.0开始，可通过[clearUkeyPinAuthState](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptoclearukeypinauthstate)清除指定资源的PIN码认证状态。

### 清除认证状态使用场景

以下场景可能需要清除PIN码认证状态：

* 密钥操作完成后，主动清除认证状态，避免认证状态残留。
* 应用退出或切换用户时，清除认证状态。
* 认证状态异常时，重置认证状态。

具体开发示例请参考[清除UKey PIN码认证状态(ArkTS)](huks-clear-pin-auth-state-arkts.md)。

**说明** 

HUKS提供PIN码认证能力和认证状态查询能力。应用PIN码认证之前，可以先查询认证状态。如果需要PIN码认证，则需要拉起[证书管理应用](certmanager-overview.md)，完成PIN码认证。
