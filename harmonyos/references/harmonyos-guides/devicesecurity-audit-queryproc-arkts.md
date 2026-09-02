---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-audit-queryproc-arkts
title: 进程信息查询场景
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 安全审计 > 进程信息查询场景
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:30+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:3fd05e7761eb2533a20e0e8872d06d8ba313c2d0637759f204db395cd7bafd52
---

## 场景介绍

从6.0.0(20) 开始，新增提供应用进程信息查询接口，可以获取设备上已启动的应用进程信息。进程信息包括进程ID、指令命令行、父进程PID、用户ID、用户组ID、进程启动时间、进程所有者ID类型、进程所有者ID等相关信息。

## 约束和限制

1. 当前能力仅支持PC/2in1设备。
2. 支持单次输入要查询的进程数最大限制为16个。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/FLbDAZGmRfqcQMwthENJzw/zh-cn_image_0000002736313409.png)

**流程说明：**

1. 开发者应用调用查询接口获取应用进程信息。
2. Device Security Kit接口同步返回应用进程信息给开发者应用，开发者应用根据返回的应用进程信息进行业务处理。

## 接口说明

接口如下表，更多接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-securityaudit-api.md#queryallprocesses)。

| 接口名 | 描述 |
| --- | --- |
| queryAllProcesses(): string | 获取所有的应用进程信息。 |
| queryProcesses(pids: number[]): string | 获取输入的pid的应用进程信息。 |

## 开发步骤

**说明** 

* 在开发准备过程中，需要申请权限：ohos.permission.QUERY\_AUDIT\_EVENT。
* 只允许清单内的企业类应用申请该权限，申请方式请参考：[企业类应用可用权限](permissions-for-enterprise-apps.md)。

1. 导入Device Security Kit模块及相关公共模块。

   ```typescript
   import { securityAudit } from '@kit.DeviceSecurityKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 开发者根据实际场景，获取单个或所有应用进程信息。

   * 获取单个应用进程信息。

   ```typescript
   const TAG: string = 'SecurityAuditJsTest';
   let pids: number[] = [3622];
   try {
     hilog.info(0x0000, TAG, 'queryProcesses begin.');
     const result = securityAudit.queryProcesses(pids);
     hilog.info(0x0000, TAG, 'Succeeded in queryProcesses.');
     // ...
   } catch (err) {
     let e: BusinessError = err as BusinessError;
     hilog.error(0x0000, TAG, 'queryProcesses failed: %{public}d %{public}s', e.code, e.message);
     // ...
   }
   ```

   * 获取所有的应用进程信息。

   ```typescript
   const TAG: string = 'SecurityAuditJsTest';
   try {
     hilog.info(0x0000, TAG, 'queryAllProcesses begin.');
     const result = securityAudit.queryAllProcesses();
     hilog.info(0x0000, TAG, 'Succeeded in queryAllProcesses.');
     // ...
   } catch (err) {
     let e: BusinessError = err as BusinessError;
     hilog.error(0x0000, TAG, 'queryAllProcesses failed: %{public}d %{public}s', e.code, e.message);
     // ...
   }
   ```
