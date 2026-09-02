---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-preparations
title: 开发准备
breadcrumb: 指南 > 应用服务 > Enterprise Space Kit（企业数字空间服务） > 开发准备
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6e200c08759057f64638129b69ac57d607e38f5c5b9d893bf0ced6ef7a44c19d
---

## 环境准备

* HarmonyOS系统：HarmonyOS 6.0.0 Release及以上。
* DevEco Studio版本：DevEco Studio 6.0.0 Release及以上。
* HarmonyOS SDK版本：HarmonyOS 6.0.0 Release SDK及以上。

## 申请资质

在开发应用前，需要在AppGallery Connect中配置项目和应用信息。包括：

* [注册账号](../start/registration-and-verification-0000001053628148.md)和[企业开发者实名认证](../start/edrna-0000001062678489.md)。
* [创建项目](../app/agc-help-create-project-0000002242804048.md)和[创建HarmonyOS应用](../app/agc-help-create-app-0000002247955506.md)。
* [申请企业MDM应用发布证书](../app/agc-help-enterprise-mdm-cert-0000002283256801.md)和[申请企业MDM应用发布Profile](../app/agc-help-enterprise-mdm-profile-0000002248341094.md)。

## 申请接口所需权限

在申请权限前，请保证符合[权限使用的基本原则](app-permission-mgmt-overview.md#权限使用的基本原则)。并且在工程模块对应的[module.json5配置文件](module-configuration-file.md)中"requestPermissions"标签下声明所需的权限。

**表1** 权限说明

| 应用能力 | 使用场景 | 需要权限 |
| --- | --- | --- |
| 空间互传 | 使用空间互传API设置、获取审批信息。 | ohos.permission.ENTERPRISE\_FILE\_TRANSFER\_AUDIT\_POLICY\_MANAGEMENT |
| 空间管理 | 下发空间生命周期策略需要申请该权限。 | ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES |
| 空间管理 | 查询空间信息需要申请该权限。 | ohos.permission.QUERY\_LOCAL\_WORKSPACES |
| 空间管理 | 企业应用订阅企业数字空间相关事件需要申请该权限。 | ohos.permission.ENTERPRISE\_WORKSPACES\_EVENT\_SUBSCRIBE |

示例：

```typescript
"requestPermissions": [
  {
    "name": "ohos.permission.ENTERPRISE_FILE_TRANSFER_AUDIT_POLICY_MANAGEMENT"
  },
  {
    "name": "ohos.permission.ENTERPRISE_MANAGE_LOCAL_PUBLICSPACES"
  },
  {
    "name": "ohos.permission.QUERY_LOCAL_WORKSPACES"
  },
  {
    "name": "ohos.permission.ENTERPRISE_WORKSPACES_EVENT_SUBSCRIBE"
  }
]
```
