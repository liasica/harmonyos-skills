---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/dataguard-preparations
title: 开发准备
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 开发准备
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:396f731e25eb37235e7bbb021e28c06c65835bc331349b881299bcdaf4bfcb2c
---

## 环境准备

* HarmonyOS系统：HarmonyOS NEXT Developer Beta1及以上。
* DevEco Studio版本：DevEco Studio NEXT Developer Beta1及以上。
* HarmonyOS SDK版本：HarmonyOS NEXT Developer Beta1 SDK及以上。

## 申请资质

在开发应用前，需要在AppGallery Connect中配置项目和应用信息。包括：

* [注册账号](../start/registration-and-verification-0000001053628148.md)和[企业开发者实名认证](../start/edrna-0000001062678489.md)。
* [创建项目](../app/agc-help-create-project-0000002242804048.md)和[创建HarmonyOS应用](../app/agc-help-create-app-0000002247955506.md)。
* [申请企业MDM应用发布证书](../app/agc-help-enterprise-mdm-cert-0000002283256801.md)和[申请企业MDM应用发布Profile](../app/agc-help-enterprise-mdm-profile-0000002248341094.md)。

## 申请权限

在申请权限前，请确保符合[权限使用的基本原则](app-permission-mgmt-overview.md#权限使用的基本原则)。然后在工程模块对应的[module.json5配置文件](module-configuration-file.md)中"requestPermissions"标签下申请实际所需的开发权限。

| 应用能力 | 需要权限 |
| --- | --- |
| 文件分级管控 | ohos.permission.FILE\_GUARD\_MANAGER  ohos.permission.SET\_FILE\_GUARD\_POLICY |
| 企业恢复密钥 | ohos.permission.ENTERPRISE\_RECOVERY\_KEY |

例如：

```typescript
"requestPermissions": [
  {
    "name": "ohos.permission.FILE_GUARD_MANAGER"
  },
  {
    "name": "ohos.permission.SET_FILE_GUARD_POLICY"
  },
  {
    "name": "ohos.permission.ENTERPRISE_RECOVERY_KEY"
  }
]
```
