---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-resource-management-overview
title: 资源管理介绍及规格
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 外部密钥管理扩展 > 资源管理 > 资源管理介绍及规格
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:32+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:d0f35b66f9325cb6fba28f7ee37a422fdcd3e5744c9b2d41746764d792b854aa
---

约定外部密钥管理扩展（例如UKey）中使用resourceId唯一标识资源。该resourceId目前支持以下两种获取方式：

* **证书管理服务获取**：通过[openAuthorizeDialog](../harmonyos-references/js-apis-certmanagerdialog.md#certificatemanagerdialogopenauthorizedialog22)返回。每个证书链对应1个resourceId。适用于浏览器双向SSL认证等需要证书选择的场景。
* **getResourceId接口获取**：从API版本26.0.0开始，可通过[getResourceId](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptogetresourceid)接口获取。适用于密钥生成、密钥导入等不需要证书选择的场景。

应用拿到resourceId后，需要[打开资源](huks-open-close-resource-arkts.md#打开资源)，然后才可以进行后续密钥操作。操作完成后需要[关闭资源](huks-open-close-resource-arkts.md#关闭资源)。该接口会回调[onClearUkeyPinAuthState](../harmonyos-references/js-apis-cryptoextensionability.md#onclearukeypinauthstate)清理该资源关联的PIN认证状态，以及会回调[onFinishSession](../harmonyos-references/js-apis-cryptoextensionability.md#onfinishsession)清理该资源关联的会话handle。

**说明** 

1. 操作密钥之前，必须先打开资源。如果涉及私钥签名等高权限操作，需要验证完PIN码后，才能继续执行，否则会导致资源状态异常。
2. 用户操作之后，必须手动关闭资源，避免资源泄漏。
