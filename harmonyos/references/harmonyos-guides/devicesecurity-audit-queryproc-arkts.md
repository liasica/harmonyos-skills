---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-audit-queryproc-arkts
title: 进程信息查询场景
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 安全审计 > 进程信息查询场景
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bc8b3cc53ff3bd9d7b44552942fffe5cfdf44213f3cf3deee19711e7982f6954
---

## 场景介绍

从6.0.0(20) 开始，新增提供应用进程信息查询接口，可以获取设备上已启动的应用进程信息。进程信息包括进程ID、指令命令行、父进程PID、用户ID、用户组ID、进程启动时间、进程所有者ID类型、进程所有者ID等相关信息。

## 约束和限制

1. 当前能力仅支持2in1设备。
2. 支持单次输入要查询的进程数最大限制为16个。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/3gc3ACVyQZSZAoFGqarttw/zh-cn_image_0000002583438445.png?HW-CC-KV=V1&HW-CC-Date=20260427T234258Z&HW-CC-Expire=86400&HW-CC-Sign=02C053833AF355CF82F7580EA88C6896A7F18495B62B9104FB902892998CC6EF)

**流程说明：**

1. 用户在hap应用上调用查询接口获取应用进程信息。
2. Device Security Kit接口同步返回应用进程信息给hap应用，hap应用根据返回的应用进程信息进行业务处理。

## 接口说明

接口如下表，更多接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-securityaudit-api.md#queryallprocesses)。

| 接口名 | 描述 |
| --- | --- |
| queryAllProcesses(): string | 获取所有的应用进程信息。 |
| queryProcesses(pids: number[]): string | 获取输入的pid的应用进程信息。 |

## 开发步骤

说明

* 在开发准备过程中，需要申请权限：ohos.permission.QUERY\_AUDIT\_EVENT。
* 只允许清单内的企业类应用申请该权限，申请方式请参考：[申请使用企业类应用可用权限](permissions-for-enterprise-apps.md)。

1. 导入Device Security Kit模块及相关公共模块。

   ```
   1. import { securityAudit } from '@kit.DeviceSecurityKit';
   2. import { BusinessError} from '@kit.BasicServicesKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 开发者根据实际场景，获取单个或所有应用进程信息。

   * 获取单个应用进程信息。

     ```
     1. const TAG = "SecurityAuditJsTest";
     2. let pids: number[] = [3622];
     3. try {
     4. hilog.info(0x0000, TAG, 'queryProcesses begin.');
     5. const result = securityAudit.queryProcesses(pids);
     6. hilog.info(0x0000, TAG, 'Succeeded in queryProcesses.');
     7. } catch (err) {
     8. let e: BusinessError = err as BusinessError;
     9. hilog.error(0x0000, TAG, 'queryProcesses failed: %{public}d %{public}s', e.code, e.message);
     10. }
     ```
   * 获取所有的应用进程信息。

     ```
     1. const TAG = "SecurityAuditJsTest";
     2. try {
     3. hilog.info(0x0000, TAG, 'queryAllProcesses begin.');
     4. const result = securityAudit.queryAllProcesses();
     5. hilog.info(0x0000, TAG, 'Succeeded in queryAllProcesses.');
     6. } catch (err) {
     7. let e: BusinessError = err as BusinessError;
     8. hilog.error(0x0000, TAG, 'queryAllProcesses failed: %{public}d %{public}s', e.code, e.message);
     9. }
     ```
