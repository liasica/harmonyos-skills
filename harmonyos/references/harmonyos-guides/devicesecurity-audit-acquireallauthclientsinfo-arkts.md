---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-audit-acquireallauthclientsinfo-arkts
title: 阻断类客户端信息查询场景
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 安全审计 > 阻断类客户端信息查询场景
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:30+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:f10264e873a9442258a9ce0bdd36a88a348e17104a0e13e667d8827ec26f5e32
---

从API版本26.0.0开始，新增阻断类客户端信息查询功能，支持应用获取设备上订阅了阻断类事件的所有客户端信息。其中，阻断类信息是指被系统拦截并阻止执行的安全审计事件记录。

## 场景介绍

应用通过调用[acquireAllAuthClientsInfo](../harmonyos-references/devicesecurity-securityaudit-api.md#acquireallauthclientsinfo)接口获取设备上订阅了阻断类事件的所有客户端信息，包括当前已被创建的客户端数量，以及每个客户端创建者的进程名、进程ID和用户ID。该接口常用于在应用创建阻断类客户端失败时，获取设备上已被创建的客户端信息。

## 约束和限制

1. 当前能力仅支持PC/2in1设备。
2. 当前支持查询全量安全审计阻断类客户端信息，最多存在16个客户端。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/RFXT8ak4RVSuymoRIajzgA/zh-cn_image_0000002706834302.png)

**流程说明：**

1. 应用调用查询阻断类客户端信息接口[acquireAllAuthClientsInfo](../harmonyos-references/devicesecurity-securityaudit-api.md#acquireallauthclientsinfo)获取全量阻断类客户端信息。
2. [acquireAllAuthClientsInfo](../harmonyos-references/devicesecurity-securityaudit-api.md#acquireallauthclientsinfo)接口同步返回阻断类客户端信息给应用，应用根据返回的阻断类客户端信息信息进行业务处理。

## 接口说明

接口如下表，更多接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-securityaudit-api.md#acquireallauthclientsinfo)。

| 接口名 | 描述 |
| --- | --- |
| [acquireAllAuthClientsInfo](../harmonyos-references/devicesecurity-securityaudit-api.md#acquireallauthclientsinfo)(): string | 获取所有的安全审计阻断类客户端信息。 |

## 开发步骤

**说明** 

在开发准备过程中，需要申请权限：ohos.permission.kernel.AUTH\_AUDIT\_EVENT。只允许清单内的企业类应用申请该权限，申请方式请参考：[企业类应用可用权限](permissions-for-enterprise-apps.md)。

1. 导入Device Security Kit模块及相关公共模块。

   ```typescript
   import { securityAudit } from '@kit.DeviceSecurityKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 应用调用查询阻断类客户端信息接口[acquireAllAuthClientsInfo](../harmonyos-references/devicesecurity-securityaudit-api.md#acquireallauthclientsinfo)，获取所有的阻断类客户端信息。

   ```typescript
   const TAG = 'SecurityAuditJsTest';
   try {
     hilog.info(0x0000, TAG, 'acquireAllAuthClientsInfo begin.');
     const result = securityAudit.acquireAllAuthClientsInfo();
     hilog.info(0x0000, TAG, 'Succeeded in acquireAllAuthClientsInfo.');
     // ...
   } catch (err) {
     let e: BusinessError = err as BusinessError;
     hilog.error(0x0000, TAG, 'acquireAllAuthClientsInfo failed: %{public}d %{public}s', e.code, e.message);
     // ...
   }
   ```
