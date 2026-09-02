---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-audit-subscribe-arkts-suevent
title: 单客户端订阅场景
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 安全审计 > 单客户端订阅场景
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:30+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a78fa3a904b93cb1a8546f7f96328314914c86bcab301506bd2cc8f57864be56
---

## 场景介绍

从5.0.0(12)开始，新增提供统一的安全审计数据单客户端订阅与取消订阅接口，应用可以获取设备上的安全审计数据（详见[API参考](../harmonyos-references/devicesecurity-securityaudit-api.md#notifyevent)），以支撑审计相关业务。

## 约束与限制

当前能力仅支持PC/2in1设备。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/uSWLTd32QxmARUX2cegWqA/zh-cn_image_0000002706674366.png)

**流程说明：**

1. 应用订阅安全审计数据。
2. Device Security Kit调用回调函数通知应用。
3. 应用根据审计数据进行业务处理。
4. 当应用不需要使用该审计数据时，取消订阅安全审计数据。

## 接口说明

以下是安全审计数据订阅与取消订阅接口，更多接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-securityaudit-api.md#onauditeventoccur)。

| 接口名 | 描述 |
| --- | --- |
| on(type: 'auditEventOccur', auditEventInfo: AuditEventInfo, callback: Callback<AuditEvent>): void | 订阅安全审计数据。 |
| off(type: 'auditEventOccur', auditEventInfo: AuditEventInfo, callback?: Callback<AuditEvent>): void | 取消订阅安全审计数据。 |

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
2. 订阅安全审计事件。

   ```typescript
   const TAG: string = 'SecurityAuditJsTest';
   const callback = (event: securityAudit.AuditEvent): void => {
     hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func eventId= ' + event.eventId);
     hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func version= ' + event.version);
     hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func content= ' + event.content);
     hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func timestamp= ' + event.timestamp);
     hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func userId= ' + event.userId);
     hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func deviceId= ' + event.deviceId);
   };
   let auditEventInfo: securityAudit.AuditEventInfo = {
     eventId: 0x810800800
   };

   try {
     hilog.info(0x0000, TAG, 'on begin.');
     securityAudit.on('auditEventOccur', auditEventInfo, callback);
     hilog.info(0x0000, TAG, 'Succeeded in on.');
   } catch (err) {
     let e: BusinessError = err as BusinessError;
     hilog.error(0x0000, TAG, 'on failed: %{public}d %{public}s', e.code, e.message);
   }
   ```
3. 取消订阅安全审计事件。

   ```typescript
   try {
     hilog.info(0x0000, TAG, 'off begin.');
     securityAudit.off('auditEventOccur', auditEventInfo, callback);
     hilog.info(0x0000, TAG, 'Succeeded in off.');
   } catch (err) {
     let e: BusinessError = err as BusinessError;
     hilog.error(0x0000, TAG, 'off failed: %{public}d %{public}s', e.code, e.message);
   }
   ```
