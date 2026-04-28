---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-audit-subscribe-arkts-filterevent
title: 订阅通知类事件
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 安全审计 > 多客户端订阅场景 > 订阅通知类事件
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8be5e1939156c4825a31f11bb45560cda423409e5b701a7c12f56e0c803ca8a0
---

## 场景介绍

从6.0.0(20)开始，新增提供统一的安全审计数据多客户端订阅/取消订阅与添加/删除过滤条件接口，应用可以获取设备上的安全审计数据（如下表），并按需进行过滤，以支撑审计相关业务。

| 审计事件ID | 说明 |
| --- | --- |
| 0x027000000 | 剪切板复制粘贴事件 |
| 0x010000100 | 账号登录登出事件 |
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
| 0x01C000012 | KIA文件读事件 |
| 0x01C00000E | 网络流量事件 |
| 0x01C00000F | 网络连接事件 |
| 0x00B000000 | 应用权限变更事件 |
| 0x003000001 | DNS审计事件 |
| 0x01C001100 | 文件拦截事件 |
| 0x018000100 | app安装拦截事件 |
| 0x018000101 | app卸载拦截事件 |
| 0x018000102 | app更新拦截事件 |
| 0x018000103 | app恢复拦截事件 |
| 0x018000104 | app启动拦截事件 |
| 0x030000000 | USB访问拦截事件 |
| 0x0F000001 | SMB(Samba)外发事件  **起始版本：** 6.1.0(23) |
| 0x1C000014 | KIA文件秒开事件  **起始版本：** 6.1.0(23) |
| 0x27000100 | HDC(HarmonyOS Device Connector)调测文件事件  **起始版本：** 6.1.0(23) |
| 0x27000101 | HDC(HarmonyOS Device Connector)调测拦截事件  **起始版本：** 6.1.0(23) |
| 0x2F000000 | 多用户空间数据互传事件  **起始版本：** 6.1.0(23) |
| 0x2F000001 | 多用户空间互换审核策略事件  **起始版本：** 6.1.0(23) |
| 0x30000100 | 串口访问审计事件  **起始版本：** 6.1.0(23) |
| 0x03000002 | 网络拦截事件  **起始版本：** 6.1.0(23) |
| 0x03000100 | WI-FI拦截事件  **起始版本：** 6.1.0(23) |
| 0x2E000001 | 打印拦截事件  **起始版本：** 6.1.0(23) |

## 约束与限制

1. 当前能力仅支持2in1设备。
2. 一个进程最大只允许创建2个客户端实例，当前设备最多只允许创建16个客户端实例。
3. 一个客户端实例最大只允许设置256个Filter，每个Filter限制10条过滤value。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/2YAU5DVFQ768Mfo4FKdu2Q/zh-cn_image_0000002583478399.png?HW-CC-KV=V1&HW-CC-Date=20260427T234257Z&HW-CC-Expire=86400&HW-CC-Sign=3EDD9D66FBD9D1347617FDE2B60FAF32D1937440AD3524CFB878571680527A50)

**流程说明：**

1. 开发者创建审计通知类事件(以下统称为事件)订阅客户端实例，需要提供CallBack。
2. 开发者使用1中创建的实例订阅事件，需要提供想要订阅的事件id。
3. 开发者使用1中创建的实例设置事件过滤条件，需要提供事件id和过滤条件信息。
4. 当事件发生时，审计服务先根据事件过滤条件过滤事件，当事件满足过滤条件时，触发回调通知订阅当前事件的客户端。
5. 开发者根据审计数据处理业务。
6. 当开发者应用不需要过滤/使用该审计数据时，开发者可以使用1中创建的实例解除过滤条件，取消对应的订阅事件。
7. 当开发者应用不需要使用当前实例时，开发者可以删除实例。

   说明

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

说明

* 在开发准备过程中，需要申请权限：ohos.permission.QUERY\_AUDIT\_EVENT。
* 只允许清单内的企业类应用申请该权限，申请方式请参考：[申请使用企业类应用可用权限](permissions-for-enterprise-apps.md)。

1. 导入Device Security Kit模块及相关公共模块。

   ```
   1. import { securityAudit } from '@kit.DeviceSecurityKit';
   2. import { BusinessError} from '@kit.BasicServicesKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 创建审计通知类事件客户端实例。

   ```
   1. let client: securityAudit.Client | undefined = undefined;
   2. const TAG = "SecurityAuditJsTest";
   3. const callback = (event: securityAudit.AuditEvent) => {
   4. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func eventId= ' + event.eventId);
   5. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func version= ' + event.version);
   6. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func content= ' + event.content);
   7. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func timestamp= ' + event.timestamp);
   8. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func userId= ' + event.userId);
   9. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func deviceId= ' + event.deviceId);
   10. };
   11. try {
   12. client = securityAudit.newClient(callback);
   13. } catch (err) {
   14. let e: BusinessError = err as BusinessError;
   15. hilog.error(0x0000, TAG, 'newClient failed: %{public}d %{public}s', e.code, e.message);
   16. }
   ```
3. 订阅审计通知类事件。

   ```
   1. try {
   2. hilog.info(0x0000, TAG, 'subscribe begin.');
   3. client?.subscribe([0x02D000000]);
   4. hilog.info(0x0000, TAG, 'Succeeded in subscribe.');
   5. } catch (err) {
   6. let e: BusinessError = err as BusinessError;
   7. hilog.error(0x0000, TAG, 'subscribe failed: %{public}d %{public}s', e.code, e.message);
   8. }
   ```
4. 设置审计通知类事件过滤条件。

   ```
   1. let filter : securityAudit.Filter = {
   2. type: 0x00000200,
   3. isInclude: true,
   4. values : ["2"]
   5. };
   6. try {
   7. hilog.info(0x0000, TAG, 'addFilter begin.');
   8. client?.addFilter(0x02D000000, filter);
   9. hilog.info(0x0000, TAG, 'Succeeded in addFilter.');
   10. } catch (err) {
   11. let e: BusinessError = err as BusinessError;
   12. hilog.error(0x0000, TAG, 'addFilter failed: %{public}d %{public}s', e.code, e.message);
   13. }
   ```
5. 解除审计通知类事件订阅。

   ```
   1. try {
   2. hilog.info(0x0000, TAG, 'unsubscribe begin.');
   3. client?.unsubscribe([0x2E000000]);
   4. hilog.info(0x0000, TAG, 'Succeeded in unsubscribe.');
   5. } catch (err) {
   6. let e: BusinessError = err as BusinessError;
   7. hilog.error(0x0000, TAG, 'unsubscribe failed: %{public}d %{public}s', e.code, e.message);
   8. }
   ```
6. 解除审计通知类事件过滤条件。

   ```
   1. try {
   2. hilog.info(0x0000, TAG, 'removeFilter begin.');
   3. client?.removeFilter(0x02D000000, filter);
   4. hilog.info(0x0000, TAG, 'Succeeded in removeFilter.');
   5. } catch (err) {
   6. let e: BusinessError = err as BusinessError;
   7. hilog.error(0x0000, TAG, 'removeFilter failed: %{public}d %{public}s', e.code, e.message);
   8. }
   ```
7. 删除审计通知类事件客户端实例。

   ```
   1. try {
   2. securityAudit.deleteClient(client);
   3. } catch (err) {
   4. let e: BusinessError = err as BusinessError;
   5. hilog.error(0x0000, TAG, 'deleteClient failed: %{public}d %{public}s', e.code, e.message);
   6. }
   ```
