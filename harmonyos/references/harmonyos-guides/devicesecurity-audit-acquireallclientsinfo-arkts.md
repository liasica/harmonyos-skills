---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-audit-acquireallclientsinfo-arkts
title: 通知类客户端信息查询场景
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 安全审计 > 通知类客户端信息查询场景
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:22+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:cb9bec7cc56b2d65507ef5c299d06346ad4b2122c4e7606e03cceb957214af37
---

从26.0.0开始，支持开发者应用获取设备上全量的安全审计通知类客户端信息。

## 场景介绍

开发者应用调用[acquireAllClientsInfo](../harmonyos-references/devicesecurity-securityaudit-api.md#acquireallclientsinfo)接口可以获取设备上订阅了安全审计通知类事件的所有客户端信息，用于查看当前已被创建的客户端数量以及每个客户端创建者的进程名、进程ID和用户ID。

## 约束和限制

1. 当前能力仅支持PC/2in1设备。
2. 当前支持查询全量安全审计通知类客户端信息，最多存在16个客户端。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/wjuinleNSkW-ntPEQXu_jg/zh-cn_image_0000002742123455.png)

**流程说明：**

1. 开发者应用调用查询通知类客户端信息接口[acquireAllClientsInfo](../harmonyos-references/devicesecurity-securityaudit-api.md#acquireallclientsinfo)获取全量通知类客户端信息。
2. [acquireAllClientsInfo](../harmonyos-references/devicesecurity-securityaudit-api.md#acquireallclientsinfo)接口同步返回通知类客户端信息给开发者应用，开发者应用根据返回的通知类客户端信息进行业务处理。

## 接口说明

接口如下表，更多接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-securityaudit-api.md#acquireallclientsinfo)。

| 接口名 | 描述 |
| --- | --- |
| [acquireAllClientsInfo](../harmonyos-references/devicesecurity-securityaudit-api.md#acquireallclientsinfo)(): string | 获取所有的安全审计通知类客户端信息。 |

## 开发步骤

**说明** 

在开发准备过程中，需要申请权限：ohos.permission.QUERY\_AUDIT\_EVENT。只允许清单内的企业类应用申请该权限，申请方式请参考：[企业类应用可用权限](permissions-for-enterprise-apps.md)。

1. 导入Device Security Kit模块及相关公共模块。

   ```typescript
   import { securityAudit } from '@kit.DeviceSecurityKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 开发者应用调用查询通知类客户端信息接口[acquireAllClientsInfo](../harmonyos-references/devicesecurity-securityaudit-api.md#acquireallclientsinfo)，获取所有的通知类客户端信息。

   ```typescript
   const TAG = 'SecurityAuditJsTest';
   try {
     hilog.info(0x0000, TAG, 'acquireAllClientsInfo begin.');
     const result = securityAudit.acquireAllClientsInfo();
     hilog.info(0x0000, TAG, 'Succeeded in acquireAllClientsInfo.');
     // ...
   } catch (err) {
     let e: BusinessError = err as BusinessError;
     hilog.error(0x0000, TAG, 'acquireAllClientsInfo failed: %{public}d %{public}s', e.code, e.message);
     // ...
   }
   ```
