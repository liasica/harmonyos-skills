---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-audit-queryproc-c
title: 进程信息查询场景（C/C++）
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 安全审计 > 进程信息查询场景（C/C++）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:30+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:1863636515cceece53d69649571ff11d4086c33e96c8768ccebbb06e437a8786
---

## 场景介绍

从6.0.0(20) 开始，新增提供应用进程信息查询接口，可以获取设备上已启动的应用进程信息。进程信息包括进程ID、指令命令行、父进程PID、用户ID、用户组ID、进程启动时间、进程所有者ID类型、进程所有者ID等相关信息。

## 约束和限制

1. 当前能力仅支持PC/2in1设备。
2. 支持单次输入要查询的进程数最大限制为16个。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/Hy_NVQ4STI-jSMW5jXDhDA/zh-cn_image_0000002736313409.png)

**流程说明：**

1. 开发者应用调用查询接口获取应用进程信息。
2. Device Security Kit接口同步返回应用进程信息给开发者应用，开发者应用根据返回的应用进程信息进行业务处理。

## 接口说明

接口如下表，更多接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-capi-securityaudit.md#hms_securityaudit_queryallprocesses)。

| 接口名 | 描述 |
| --- | --- |
| int32\_t HMS\_SecurityAudit\_QueryAllProcesses(char\*\* result) | 获取所有的应用进程信息。 |
| int32\_t HMS\_SecurityAudit\_QueryProcesses(uint64\_t\* pids, uint64\_t count, char\*\* result) | 获取输入的pid的应用进程信息。 |

## 开发步骤

**说明** 

* 在开发准备过程中，需要申请权限：ohos.permission.QUERY\_AUDIT\_EVENT。
* 只允许清单内的企业类应用申请该权限，申请方式请参考：[企业类应用可用权限](permissions-for-enterprise-apps.md)。

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
3. 开发者根据实际场景，获取单个或所有应用进程信息。

   **说明** 

   开发者应用根据应用进程信息进行业务处理后，需要释放查询接口出入参的内存。

   * 调用HMS\_SecurityAudit\_QueryProcesses接口，获取单个应用进程信息。

   ```
   char* result = nullptr;
   uint64_t pids[] = {3266};
   int32_t ret = HMS_SecurityAudit_QueryProcesses(pids, sizeof(pids)/sizeof(pids[0]), &result);
   if (ret == 0 && result != nullptr) {
       printf("HMS_SecurityAudit_QueryProcesses result: %s\n", result);
   } else {
       printf("HMS_SecurityAudit_QueryProcesses failed with error: %d\n", ret);
   }
       
   // ...
   if (result != nullptr) {
       delete[] result;
       result = nullptr;
   }
   ```

   * 调用HMS\_SecurityAudit\_QueryAllProcesses接口，获取所有的应用进程信息。

   ```
   char* result = nullptr;
   int32_t ret = HMS_SecurityAudit_QueryAllProcesses(&result);
   if (ret == 0 && result != nullptr) {
   printf("HMS_SecurityAudit_QueryAllProcesses result: %s\n", result);
   } else {
       printf("HMS_SecurityAudit_QueryAllProcesses failed with error: %d\n", ret);
   }
   // ...
   if (result != nullptr) {
       delete[] result;
       result = nullptr;
   }
   ```
