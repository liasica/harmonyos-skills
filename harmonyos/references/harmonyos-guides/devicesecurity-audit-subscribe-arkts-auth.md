---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-audit-subscribe-arkts-auth
title: 订阅阻断类事件
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 安全审计 > 多客户端订阅场景 > 订阅阻断类事件
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:30+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:1357924db4cf07ec84589605afeb9be62d4d21bdd6caaace8a0c5c77ae077c10
---

## 场景介绍

从6.0.0(20) 开始，新增提供统一的安全审计数据多客户端订阅/取消订阅、添加/删除过滤条件、阻断接口，应用可以获取设备上的安全审计数据（如下表），并按需进行订阅、过滤与阻断，以支撑审计相关业务。

| 审计事件ID | 说明 |
| --- | --- |
| 0x1C801100 | 文件创建阻断事件。 |
| 0x1C801101 | 文件打开阻断事件。 |
| 0x1C801102 | 文件重命名阻断事件。 |
| 0x1C801103 | 文件删除阻断事件。 |
| 0x1C801104 | 文件设置扩展属性的阻断事件。 |
| 0x1C801105 | 文件删除扩展属性的阻断事件。 |
| 0x1C801106 | 文件读结束阻断事件。  **起始版本：** 26.0.0 |
| 0x1C801400 | 进程执行的阻断事件。  **起始版本：** 26.0.0 |

## 约束与限制

1. 当前能力仅支持PC/2in1设备。
2. 一个进程最大只允许创建2个客户端实例，当前设备最多只允许创建16个客户端实例。
3. 一个客户端实例最大只允许设置256条正过滤的过滤value和256条反过滤的过滤value。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/l3O3tAQnT_6byH17uGYzzA/zh-cn_image_0000002706834300.png)

**流程说明：**

1. 开发者创建审计阻断类事件（以下统称为事件）订阅客户端实例，需要提供CallBack。
2. 开发者使用步骤1中创建的实例订阅事件，需要提供想要订阅的事件id。
3. 开发者使用步骤1中创建的实例设置事件过滤条件，需要提供事件id和过滤条件信息。
4. 当事件发生时，审计服务先根据事件过滤条件过滤事件，当事件满足过滤条件时，触发回调通知订阅当前事件的客户端。
5. 开发者根据审计数据制定阻断策略。
6. 使用步骤1中创建的实例设置接收到的事件的阻断策略。
7. 当业务结束时，开发者可以使用步骤1中创建的实例解除过滤条件，取消订阅事件。
8. 当业务结束时，开发者可以删除步骤1中创建的实例。

   **说明** 

   支持先设置过滤条件再订阅事件。

   删除实例后，被删除的实例所有的订阅以及过滤条件将被全部解除。

## 接口说明

更多接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-securityaudit-api.md#newauthclient)。

| 接口名 | 描述 |
| --- | --- |
| newAuthClient(callback: Callback<AuditEvent>): AuthClient; | 创建审计阻断类事件管理对象AuthClient，AuthClient提供订阅、解订阅、增加事件过滤、移除事件过滤、阻断功能（超时默认放行）。 |
| newAuthClient(callback: Callback<AuditEvent>, configuration: AuthClientConfiguration): AuthClient; | 创建审计阻断类事件管理对象AuthClient（可配置超时默认阻断策略），AuthClient提供订阅、解订阅、增加事件过滤、移除事件过滤、阻断功能。 |
| deleteAuthClient(client: AuthClient): void; | 删除审计阻断类事件管理对象。 |
| interface AuthClient {  subscribe(events: AuthEvent[]): void;  } | 订阅审计阻断类事件。 |
| interface AuthClient {  unsubscribe(events: AuthEvent[]): void;  } | 解订阅审计阻断类事件。 |
| interface AuthClient {  addFilter(event: AuthEvent, filter: Filter): void；  } | 添加审计阻断类事件过滤条件。 |
| interface AuthClient {  removeFilter(event: AuthEvent, filter: Filter): void;  } | 移除审计阻断类事件过滤条件。 |
| interface AuthClient {  auth(auditEvent: AuditEvent, authResult: AuthResult): void;  } | 设置审计阻断类事件的阻断结果。 |

## 开发步骤

**说明** 

* 在开发准备过程中，需要申请权限：ohos.permission.kernel.AUTH\_AUDIT\_EVENT。
* 只允许清单内的企业类应用申请该权限，申请方式请参考：[企业类应用可用权限](permissions-for-enterprise-apps.md)。

1. 导入Device Security Kit模块及相关公共模块。

   ```typescript
   import { securityAudit } from '@kit.DeviceSecurityKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 定义携带阻断策略的回调函数。

   ```typescript
   const TAG = 'SecurityAuditAuthJsTest';
   let authClient: securityAudit.AuthClient | undefined = undefined;
   const allowEventCallback = (event: securityAudit.AuditEvent):void => {
     hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func eventId= ' + event.eventId);
     hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func content= ' + event.content);
     hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func metadata= ' + event.metadata);
     try {
       authClient?.auth(event, securityAudit.AuthResult.ALLOW);
     } catch (error) {
       let e: BusinessError = error as BusinessError;
       hilog.error(0x0000, TAG, 'allowEventCallback', 'auth error:' + e.code);
     }
   };
   ```
3. 使用携带阻断策略的回调函数创建审计阻断类事件客户端实例。

   ```typescript
   try {
     authClient = securityAudit.newAuthClient(allowEventCallback);
   } catch (err) {
     let e: BusinessError = err as BusinessError;
     hilog.error(0x0000, TAG, 'newAuthClient failed: %{public}d %{public}s', e.code, e.message);
   }
   ```
4. （可选）使用配置项创建可配置超时默认阻断策略的审计阻断类事件客户端实例。

   ```typescript
   // 配置超时后阻断
   let config: securityAudit.AuthClientConfiguration = {
     timeoutAuthResult: securityAudit.AuthResult.DENY
   };
   try {
     authClient = securityAudit.newAuthClient(allowEventCallback, config);
   } catch (err) {
     let e: BusinessError = err as BusinessError;
     hilog.error(0x0000, TAG, 'newAuthClient failed: %{public}d %{public}s', e.code, e.message);
   }
   ```

   **说明** 

   此方式为创建客户端的另一种方式，与步骤2二选一执行。配置项可指定事件响应超时后的默认授权结果，若不配置默认超时放行。起始版本：26.0.0。
5. 订阅审计阻断类事件。

   ```typescript
   try {
     hilog.info(0x0000, TAG, 'subscribe begin.');
     authClient?.subscribe([securityAudit.AuthEvent.FILE_CREATE]);
     hilog.info(0x0000, TAG, 'Succeeded in subscribe.');
   } catch (err) {
     let e: BusinessError = err as BusinessError;
     hilog.error(0x0000, TAG, 'subscribe failed: %{public}d %{public}s', e.code, e.message);
   }
   ```
6. 设置审计阻断类事件过滤条件。

   ```typescript
   let filter : securityAudit.Filter = {
     type: securityAudit.FilterType.PROCESS_PID_EQUAL,
     isInclude: true,
     values : ['2']
   };
   try {
     hilog.info(0x0000, TAG, 'addFilter begin.');
     authClient?.addFilter(securityAudit.AuthEvent.FILE_CREATE, filter);
     hilog.info(0x0000, TAG, 'Succeeded in addFilter.');
   } catch (err) {
     let e: BusinessError = err as BusinessError;
     hilog.error(0x0000, TAG, 'addFilter failed: %{public}d %{public}s', e.code, e.message);
   }
   ```
7. 解除审计阻断类事件订阅。

   ```typescript
   try {
     hilog.info(0x0000, TAG, 'unsubscribe begin.');
     authClient?.unsubscribe([securityAudit.AuthEvent.FILE_CREATE]);
     hilog.info(0x0000, TAG, 'Succeeded in unsubscribe.');
   } catch (err) {
     let e: BusinessError = err as BusinessError;
     hilog.error(0x0000, TAG, 'unsubscribe failed: %{public}d %{public}s', e.code, e.message);
   }
   ```
8. 解除审计阻断类事件过滤条件。

   ```typescript
   try {
     hilog.info(0x0000, TAG, 'removeFilter begin.');
     authClient?.removeFilter(securityAudit.AuthEvent.FILE_CREATE, filter);
     hilog.info(0x0000, TAG, 'Succeeded in removeFilter.');
   } catch (err) {
     let e: BusinessError = err as BusinessError;
     hilog.error(0x0000, TAG, 'removeFilter failed: %{public}d %{public}s', e.code, e.message);
   }
   ```
9. 删除审计阻断类事件客户端实例。

   ```typescript
   try {
     securityAudit.deleteAuthClient(authClient);
   } catch (err) {
     let e: BusinessError = err as BusinessError;
     hilog.error(0x0000, TAG, 'deleteAuthClient failed: %{public}d %{public}s', e.code, e.message);
   }
   ```
