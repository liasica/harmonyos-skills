---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-audit-subscribe-arkts-suevent
title: 单客户端订阅场景
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 安全审计 > 单客户端订阅场景
category: harmonyos-guides
scraped_at: 2026-04-29T13:31:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:84f3811430fa3deceace764971b753a99b0f4e0437995aa0e82f0749b35b9ef6
---

## 场景介绍

提供统一的安全审计数据单客户端订阅与取消订阅接口，应用可以获取设备上的安全审计数据（如下表），以支撑审计相关业务。

| 审计事件ID | 说明 |
| --- | --- |
| 0x027000000 | 剪切板复制粘贴事件 |
| 0x810800800 | 账号登录登出事件 |
| 0x007000000 | 窗口截屏录屏投屏事件 |
| 0x00F000000 | 移动存储插拔事件，如U盘、存储卡等具有存储功能的外设插拔事件 |
| 0x02E000000 | 打印机事件 |
| 0x01C000007 | 文件事件 |
| 0x01C000008 | 进程创建退出事件 |
| 0x01C000009 | 网络事件 |
| 0x01C00000A | KIA文件拦截事件 |
| 0x02D000000 | 相机事件 |
| 0x010000000 | 应用事件 |
| 0x011000000 | edm事件 |
| 0x012003000 | 证书操作事件 |
| 0x01C00000B | KIA文件新增事件 |
| 0x01C00000C | KIA文件变种事件 |
| 0x01C00000E | 网络流量事件 |
| 0x01C00000F | 网络连接事件 |
| 0x00B000000 | 应用权限变更事件 |
| 0x003000001 | DNS审计事件 |

## 约束与限制

当前能力仅支持2in1设备。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/NkcyBzkJR2a5JTB_4bLlCw/zh-cn_image_0000002589324765.png?HW-CC-KV=V1&HW-CC-Date=20260429T053134Z&HW-CC-Expire=86400&HW-CC-Sign=1F4ADC55CEF4B1DCE7DD8675877A8043511845E18A900712BC2AE9FC0F5BC3BE)

**流程说明：**

1. 开发者应用订阅安全审计数据。
2. Device Security Kit调用回调函数通知开发者应用，开发者应用根据审计数据进行业务处理。
3. 当开发者应用不需要使用该审计数据时，取消订阅安全审计数据。

## 接口说明

以下是安全审计数据订阅与取消订阅接口，更多接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-securityaudit-api.md#onauditeventoccur)。

| 接口名 | 描述 |
| --- | --- |
| on(type: 'auditEventOccur', auditEventInfo: AuditEventInfo, callback: Callback<AuditEvent>): void | 订阅安全审计数据 |
| off(type: 'auditEventOccur', auditEventInfo: AuditEventInfo, callback?: Callback<AuditEvent>): void | 取消订阅安全审计数据 |

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
2. 订阅安全审计事件。

   ```
   1. const TAG = "SecurityAuditJsTest";
   2. const callback = (event: securityAudit.AuditEvent) => {
   3. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func eventId= ' + event.eventId);
   4. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func version= ' + event.version);
   5. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func content= ' + event.content);
   6. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func timestamp= ' + event.timestamp);
   7. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func userId= ' + event.userId);
   8. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func deviceId= ' + event.deviceId);
   9. };
   10. let auditEventInfo: securityAudit.AuditEventInfo = {
   11. eventId: 0x810800800
   12. };

   14. try {
   15. hilog.info(0x0000, TAG, 'on begin.');
   16. securityAudit.on('auditEventOccur', auditEventInfo, callback);
   17. hilog.info(0x0000, TAG, 'Succeeded in on.');
   18. } catch (err) {
   19. let e: BusinessError = err as BusinessError;
   20. hilog.error(0x0000, TAG, 'on failed: %{public}d %{public}s', e.code, e.message);
   21. }
   ```
3. 取消订阅安全审计事件。

   ```
   1. try {
   2. hilog.info(0x0000, TAG, 'off begin.');
   3. securityAudit.off('auditEventOccur', auditEventInfo, callback);
   4. hilog.info(0x0000, TAG, 'Succeeded in off.');
   5. } catch (err) {
   6. let e: BusinessError = err as BusinessError;
   7. hilog.error(0x0000, TAG, 'off failed: %{public}d %{public}s', e.code, e.message);
   8. }
   ```
