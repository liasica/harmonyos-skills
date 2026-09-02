---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisethreatprotection-prepare
title: 开发准备
breadcrumb: 指南 > 系统 > 安全 > Enterprise Threat Protection Kit（企业威胁防护服务） > 开发准备
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:02+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:73bc436b1643baf07997f997d6aa4e5d966f66ea19d58be6adfd00768bd0711f
---

## 申请资质

在开发应用前，需要在AppGallery Connect中配置项目和应用信息。包括：

* [注册账号](../start/registration-and-verification-0000001053628148.md)和[企业开发者实名认证](../start/edrna-0000001062678489.md)。
* [创建项目](../app/agc-help-create-project-0000002242804048.md)和[创建HarmonyOS应用](../app/agc-help-create-app-0000002247955506.md)。
* [申请企业应用发布证书](../app/agc-help-enterprise-cert-0000002248177978.md)和[申请企业应用发布Profile](../app/agc-help-enterprise-profile-0000002248181282.md)。

## 申请权限

在申请权限前，请保证符合[权限使用的基本原则](app-permission-mgmt-overview.md#权限使用的基本原则)。随后在工程模块对应的[module.json5配置文件](module-configuration-file.md)中"requestPermissions"标签下声明实际所需的开发权限。使用病毒检测与处置能力，则应申请[ohos.permission.SCAN\_REMEDIATE\_VIRUS](permissions-for-enterprise-apps.md#ohospermissionscan_remediate_virus)权限，此权限仅面向企业杀毒软件开放申请。权限申请代码示例如下：

```json
"requestPermissions": [
  {
    "name": "ohos.permission.SCAN_REMEDIATE_VIRUS"
  }
]
```
