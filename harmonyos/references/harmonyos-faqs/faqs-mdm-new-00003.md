---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-mdm-new-00003
title: 安装企业重签名证书接口certificateAlias参数的使用说明
breadcrumb: FAQ > 系统开发 > 基础功能 > 企业设备管理（MDM） > 安装企业重签名证书接口certificateAlias参数的使用说明
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-07-22
content_hash: sha256:7f88174b1fcc1466ef1895031b5708a3c359de7900fb91d8ad814152716ad523
---

## 问题现象

调用[securityManager.installEnterpriseReSignatureCertificate](../harmonyos-references/js-apis-enterprise-securitymanager.md#securitymanagerinstallenterpriseresignaturecertificate24)接口安装企业重签名证书时，参数certificateAlias是指申请证书时设置的证书别名，还是可以使用一个新的名称？另外，传入该参数时是否需要添加“.cer”后缀？

## 解决方案

参数certificateAlias用于在系统证书存储区中唯一标识该证书，后续卸载或查询时通过此别名定位。它与在AGC上申请证书时填写的“证书名称”是两个独立的概念，无需保持一致，可以使用一个新的名称。建议遵循以下命名规范：

* 使用具有业务含义的名称，便于后续管理和维护。
* 确保同一设备上不重复，避免安装时覆盖已有证书。
* 长度不超过100个字符。

无需添加后缀：不需要在别名后添加“.cer”后缀。别名本身是字符串标识，而非文件路径或文件名。例如，申请证书时设置的别名为qax\_123，则调用接口时直接传入qax\_123即可，不应写成qax\_123.cer。
