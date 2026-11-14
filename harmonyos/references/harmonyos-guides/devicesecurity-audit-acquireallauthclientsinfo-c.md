---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-audit-acquireallauthclientsinfo-c
title: 阻断类客户端信息查询场景（C/C++）
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 安全审计 > 阻断类客户端信息查询场景（C/C++）
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:28+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:89f91246c5ba255b609fa8d47269be965a20c778553f2982d8a289b087b92a9e
---

从API版本26.0.0开始，新增阻断类客户端信息查询功能，支持应用获取设备上订阅了阻断类事件的所有客户端信息。其中，阻断类信息是指被系统拦截并阻止执行的安全审计事件记录。

## 场景介绍

应用调用[HMS\_SecurityAudit\_AcquireAllAuthClientsInfo](../harmonyos-references/devicesecurity-capi-securityaudit.md#hms_securityaudit_acquireallauthclientsinfo)接口获取设备上订阅了阻断类事件的所有客户端信息，包括当前已被创建的客户端数量，以及每个客户端创建者的进程名、进程ID和用户ID。该接口常用于在应用创建阻断类客户端失败时，获取设备上已被创建的客户端信息。

## 约束和限制

1. 当前能力仅支持PC/2in1设备。
2. 当前支持查询全量安全审计阻断类客户端信息，最多存在16个客户端。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/uxcvYue8TVWpUfiwRxrCww/zh-cn_image_0000002817426777.png?HW-CC-KV=V1&HW-CC-Date=20261114T004549Z&HW-CC-Expire=31536000000&HW-CC-Sign=DF5651EF55D04C34655F814190225F5A19512FA71F1B1D2462ECEFAB7B0970C0)

**流程说明：**

1. 应用调用查询阻断类客户端信息接口[HMS\_SecurityAudit\_AcquireAllAuthClientsInfo](../harmonyos-references/devicesecurity-capi-securityaudit.md#hms_securityaudit_acquireallauthclientsinfo)获取全量安全审计阻断类客户端信息。
2. [HMS\_SecurityAudit\_AcquireAllAuthClientsInfo](../harmonyos-references/devicesecurity-capi-securityaudit.md#hms_securityaudit_acquireallauthclientsinfo)接口同步返回阻断类客户端信息给应用，应用根据返回的阻断类客户端信息进行业务处理。

## 接口说明

接口如下表，更多接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-capi-securityaudit.md#hms_securityaudit_acquireallauthclientsinfo)。

| 接口名 | 描述 |
| --- | --- |
| int32\_t [HMS\_SecurityAudit\_AcquireAllAuthClientsInfo](../harmonyos-references/devicesecurity-capi-securityaudit.md#hms_securityaudit_acquireallauthclientsinfo)(char\*\* outOwnedResult) | 获取全量安全审计阻断类客户端信息。 |

## 开发步骤

**说明** 

在开发准备过程中，需要申请权限：ohos.permission.kernel.AUTH\_AUDIT\_EVENT。只允许清单内的企业类应用申请该权限，申请方式请参考：[企业类应用可用权限](permissions-for-enterprise-apps.md)。

1. 在CMakeLists.txt中导入安全审计共享库，并链接该库。

   ```cmake
   find_library(dsm-lib libsecurityaudit_ndk.z.so)
   target_link_libraries(entry PUBLIC libace_napi.z.so ${dsm-lib})
   ```
2. 导入安全审计的头文件。

   ```
   #include <cstdio>
   #include "DeviceSecurityKit/security_audit.h"
   ```
3. 应用调用[HMS\_SecurityAudit\_AcquireAllAuthClientsInfo](../harmonyos-references/devicesecurity-capi-securityaudit.md#hms_securityaudit_acquireallauthclientsinfo)接口，获取全量安全审计阻断类客户端信息。

   **说明** 

   应用在根据阻断类客户端信息进行业务处理后，需要释放查询接口出入参的内存。

   ```
   char *outOwnedResult = nullptr;
   int32_t ret = HMS_SecurityAudit_AcquireAllAuthClientsInfo(&outOwnedResult);
   if (ret == 0 && outOwnedResult != nullptr) {
       printf("HMS_SecurityAudit_AcquireAllAuthClientsInfo outOwnedResult: %s\n", outOwnedResult);
   } else {
        printf("HMS_SecurityAudit_AcquireAllAuthClientsInfo failed with error: %d\n", ret);
   }
   // ...
   if (outOwnedResult != nullptr) {
       delete[] outOwnedResult;
       outOwnedResult = nullptr;
   }
   ```
