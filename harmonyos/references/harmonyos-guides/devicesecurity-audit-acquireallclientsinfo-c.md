---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-audit-acquireallclientsinfo-c
title: 通知类客户端信息查询场景（C/C++）
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 安全审计 > 通知类客户端信息查询场景（C/C++）
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:22+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:b87963f7c271a11750353747e315f507c534a6301a2c5c85a38f7e28b7d973b2
---

从26.0.0开始，支持三方安全应用获取设备上全量的安全审计通知类客户端信息。

## 场景介绍

开发者应用调用[HMS\_SecurityAudit\_AcquireAllClientsInfo](../harmonyos-references/devicesecurity-capi-securityaudit.md#hms_securityaudit_acquireallclientsinfo)接口可以获取设备上订阅了安全审计通知类事件的所有客户端信息，用于查看当前已被创建的客户端数量以及每个客户端创建者的进程名、进程ID和用户ID。

## 约束和限制

1. 当前能力仅支持PC/2in1设备。
2. 当前支持查询全量安全审计通知类客户端信息，最多存在16个客户端。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/mvMbMhCmQUKSB4_LaK7HOg/zh-cn_image_0000002742123455.png)

**流程说明：**

1. 开发者应用调用查询通知类客户端信息接口[HMS\_SecurityAudit\_AcquireAllClientsInfo](../harmonyos-references/devicesecurity-capi-securityaudit.md#hms_securityaudit_acquireallclientsinfo)获取全量安全审计通知类客户端信息。
2. [HMS\_SecurityAudit\_AcquireAllClientsInfo](../harmonyos-references/devicesecurity-capi-securityaudit.md#hms_securityaudit_acquireallclientsinfo)接口同步返回通知类客户端信息给开发者应用，开发者应用根据返回的通知类客户端信息进行业务处理。

## 接口说明

接口如下表，更多接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-capi-securityaudit.md#hms_securityaudit_acquireallclientsinfo)。

| 接口名 | 描述 |
| --- | --- |
| int32\_t [HMS\_SecurityAudit\_AcquireAllClientsInfo](../harmonyos-references/devicesecurity-capi-securityaudit.md#hms_securityaudit_acquireallclientsinfo)(char\*\* outOwnedResult) | 获取全量安全审计通知类客户端信息。 |

## 开发步骤

**说明** 

在开发准备过程中，需要申请权限：ohos.permission.QUERY\_AUDIT\_EVENT。只允许清单内的企业类应用申请该权限，申请方式请参考：[企业类应用可用权限](permissions-for-enterprise-apps.md)。

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
3. 开发者应用调用[HMS\_SecurityAudit\_AcquireAllClientsInfo](../harmonyos-references/devicesecurity-capi-securityaudit.md#hms_securityaudit_acquireallclientsinfo)接口，获取全量安全审计通知类客户端信息。

   **说明** 

   开发者应用根据通知类客户端信息进行业务处理后，需要释放查询接口出入参的内存。

   ```
   char *outOwnedResult = nullptr;
   int32_t ret = HMS_SecurityAudit_AcquireAllClientsInfo(&outOwnedResult);
   if (ret == 0 && outOwnedResult != nullptr) {
       printf("HMS_SecurityAudit_AcquireAllClientsInfo outOwnedResult: %s\n", outOwnedResult);
   } else {
        printf("HMS_SecurityAudit_AcquireAllClientsInfo failed with error: %d\n", ret);
   }
   // ...
   if (outOwnedResult != nullptr) {
       delete[] outOwnedResult;
       outOwnedResult = nullptr;
   }
   ```
