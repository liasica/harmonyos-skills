---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-audit-subscribe-arkts-filterevent
title: 订阅通知类事件
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 安全审计 > 多客户端订阅场景 > 订阅通知类事件
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:22+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:efe98a5d7dfd8ce3050837fb7cce1926c23918d7dce16294eefe6983c7f2f4cd
---

## 场景介绍

从6.0.0(20)开始，新增提供统一的安全审计数据多客户端订阅/取消订阅与添加/删除过滤条件接口，应用可以获取设备上的安全审计数据（详见[API参考](../harmonyos-references/devicesecurity-securityaudit-api.md#notifyevent)），并按需进行过滤，以支撑审计相关业务。

## 约束与限制

1. 当前能力仅支持PC/2in1设备。
2. 一个进程最大只允许创建2个客户端实例，当前设备最多只允许创建16个客户端实例。
3. 一个客户端实例最大只允许设置256个Filter，每个Filter限制10条过滤value。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/KgqBOGB-SEiWNeIS9S3f3Q/zh-cn_image_0000002742123453.png)

**流程说明：**

1. 开发者创建审计通知类事件(以下统称为事件)订阅客户端实例，需要提供CallBack。
2. 开发者使用1中创建的实例订阅事件，需要提供想要订阅的事件id。
3. 开发者使用1中创建的实例设置事件过滤条件，需要提供事件id和过滤条件信息。
4. 当事件发生时，审计服务先根据事件过滤条件过滤事件，当事件满足过滤条件时，触发回调通知订阅当前事件的客户端。
5. 开发者根据审计数据处理业务。
6. 当开发者应用不需要过滤/使用该审计数据时，开发者可以使用1中创建的实例解除过滤条件，取消对应的订阅事件。
7. 当开发者应用不需要使用当前实例时，开发者可以删除实例。

   **说明** 

   支持先设置过滤条件再订阅事件。

   删除实例后，被删除的实例所有的订阅以及过滤条件将被全部解除。

## 接口说明

更多接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-securityaudit-api.md#newclient)。

| 接口名 | 描述 |
| --- | --- |
| newClient(callback: Callback<AuditEvent>): Client | 创建审计通知类事件管理对象Client，Client提供订阅、解订阅、增加事件过滤、移除事件过滤功能。 |
| deleteClient(client:Client): void | 删除审计通知类事件管理对象。 |
| subscribe(events: NotifyEvent[]): void | 订阅审计通知类事件。 |
| unsubscribe(events: NotifyEvent[]): void | 解订阅审计通知类事件。 |
| addFilter(event: NotifyEvent, filter: Filter): void | 添加审计通知类事件过滤条件。 |
| removeFilter(event: NotifyEvent, filter: Filter): void | 移除审计通知类事件过滤条件。 |

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
2. 创建审计通知类事件客户端实例。

   ```typescript
   let client: securityAudit.Client | undefined = undefined;
   const TAG = 'SecurityAuditJsTest';
   const callback = (event: securityAudit.AuditEvent): void => {
     hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func eventId= ' + event.eventId);
     hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func version= ' + event.version);
     hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func content= ' + event.content);
     hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func timestamp= ' + event.timestamp);
     hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func userId= ' + event.userId);
     hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func deviceId= ' + event.deviceId);
   };
   try {
     client = securityAudit.newClient(callback);
   } catch (err) {
     let e: BusinessError = err as BusinessError;
     hilog.error(0x0000, TAG, 'newClient failed: %{public}d %{public}s', e.code, e.message);
   }
   ```
3. 订阅审计通知类事件。

   ```typescript
   try {
     hilog.info(0x0000, TAG, 'subscribe begin.');
     client?.subscribe([0x02D000000]);
     hilog.info(0x0000, TAG, 'Succeeded in subscribe.');
   } catch (err) {
     let e: BusinessError = err as BusinessError;
     hilog.error(0x0000, TAG, 'subscribe failed: %{public}d %{public}s', e.code, e.message);
   }
   ```
4. 设置审计通知类事件过滤条件。

   ```typescript
   let filter : securityAudit.Filter = {
     type: 0x00000200,
     isInclude: true,
     values : ['2']
   };
   try {
     hilog.info(0x0000, TAG, 'addFilter begin.');
     client?.addFilter(0x02D000000, filter);
     hilog.info(0x0000, TAG, 'Succeeded in addFilter.');
   } catch (err) {
     let e: BusinessError = err as BusinessError;
     hilog.error(0x0000, TAG, 'addFilter failed: %{public}d %{public}s', e.code, e.message);
   }
   ```
5. 解除审计通知类事件订阅。

   ```typescript
   try {
     hilog.info(0x0000, TAG, 'unsubscribe begin.');
     client?.unsubscribe([0x02D000000]);
     hilog.info(0x0000, TAG, 'Succeeded in unsubscribe.');
   } catch (err) {
     let e: BusinessError = err as BusinessError;
     hilog.error(0x0000, TAG, 'unsubscribe failed: %{public}d %{public}s', e.code, e.message);
   }
   ```
6. 解除审计通知类事件过滤条件。

   ```typescript
   try {
     hilog.info(0x0000, TAG, 'removeFilter begin.');
     client?.removeFilter(0x02D000000, filter);
     hilog.info(0x0000, TAG, 'Succeeded in removeFilter.');
   } catch (err) {
     let e: BusinessError = err as BusinessError;
     hilog.error(0x0000, TAG, 'removeFilter failed: %{public}d %{public}s', e.code, e.message);
   }
   ```
7. 删除审计通知类事件客户端实例。

   ```typescript
   try {
     securityAudit.deleteClient(client);
   } catch (err) {
     let e: BusinessError = err as BusinessError;
     hilog.error(0x0000, TAG, 'deleteClient failed: %{public}d %{public}s', e.code, e.message);
   }
   ```
