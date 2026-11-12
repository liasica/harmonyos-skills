---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/dataguard-preparations
title: 开发准备
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 开发准备
category: harmonyos-guides
scraped_at: 2026-11-12T09:51:38+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:8ded79d180953cc256a90d8655eb781997b7354fbcbc0e8f36a18a5f16695652
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

| 应用能力 | 使用场景 | 需要权限 |
| --- | --- | --- |
| 文件分级管控 | 企业应用进行公共目录扫描及设置文件扩展属性。 | ohos.permission.FILE\_GUARD\_MANAGER |
| 文件分级管控 | 企业应用下发文件管控策略。 | ohos.permission.SET\_FILE\_GUARD\_POLICY |
| 文件分级管控 | 企业应用可以获取指定文件的写权限，并修改文件。 | ohos.permission.FILE\_GUARD\_FILE\_WRITE |
| 企业恢复密钥 | 企业应用管理企业级恢复密钥。 | ohos.permission.ENTERPRISE\_RECOVERY\_KEY |
| 加密U盘管理 | 企业应用挂载或卸载加密U盘的加密区与交换区。 | ohos.permission.ENTERPRISE\_ENCRYPT\_BLOCK\_DEVICE |

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
    "name": "ohos.permission.FILE_GUARD_FILE_WRITE"
  },
  {
    "name": "ohos.permission.ENTERPRISE_RECOVERY_KEY"
  },
  {
    "name": "ohos.permission.ENTERPRISE_ENCRYPT_BLOCK_DEVICE"
  }
]
```
