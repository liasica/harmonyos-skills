---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-securityaudit-api
title: SecurityAudit（安全审计）
breadcrumb: API参考 > 系统 > 安全 > Device Security Kit（设备安全服务） > ArkTS API > SecurityAudit（安全审计）
category: harmonyos-references
scraped_at: 2026-04-28T08:07:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:adb487d86aebd13b1c11c80104e9632c348ec6f8c0e0db18878e58bc523890d4
---

提供统一的安全审计数据订阅与取消订阅接口，应用可以获取设备上的安全审计数据，以支撑审计业务。

**起始版本：** 5.0.0(12)

## 导入模块

PC/2in1

```
1. import { securityAudit } from '@kit.DeviceSecurityKit';
```

## AuditEventInfo

PC/2in1

用于订阅或取消订阅接口的请求参数。

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| eventId | number | 否 | 否 | 审计事件ID，用于指定需要获取的安全审计数据。例如：0x810800800  审计事件ID的取值范围是[0, 0xFFFFFFFFF]。 |

## AuditEvent

PC/2in1

安全审计数据。

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| eventId | number | 否 | 否 | 审计事件ID，与请求参数中的审计事件ID相同。 |
| version | string | 否 | 是 | 审计事件版本号。 |
| timestamp | string | 否 | 是 | 审计事件发生时间。格式为： YYYYMMDDHHMMSS |
| content | string | 否 | 是 | 审计事件内容。不同审计事件具备不同的内容，内容为json格式字符串。例如：{"type": 1} |
| userId | number | 否 | 是 | 发生审计事件时，登录的用户ID。 |
| deviceId | string | 否 | 是 | 审计事件发生的设备ID。 |
| metadata | string | 否 | 是 | 审计事件元数据。包含事件版本号、事件接收时间、设备ID和用户ID。  **起始版本：** 6.0.0(20) |

## NotifyEvent

PC/2in1

通知类事件枚举。

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PASTEBOARD | 0x27000000 | 剪切板复制粘贴事件。 |
| FILE | 0x1C000007 | 文件事件。 |
| FILE\_INTERCEPTED | 0x1C001100 | 文件访问规则违规事件。 |
| ACCOUNT | 0x10000100 | 账户登录或注销事件。 |
| WINDOW | 0x07000000 | 屏幕截图、屏幕录制或屏幕投影事件。 |
| VOLUME | 0x0F000000 | 可移动存储设备的插入或移除事件。 |
| PRINTER | 0x2E000000 | 打印机事件。 |
| PROCESS | 0x1C000008 | 进程创建或退出事件。 |
| NETWORK\_TRAFFIC | 0x1C00000E | 网络流量事件。 |
| NETWORK\_CONN | 0x1C00000F | 网络连接事件。 |
| CAMERA | 0x2D000000 | 相机事件。 |
| APP | 0x10000000 | 应用程序事件。 |
| EDM | 0x11000000 | 企业设备管理事件。 |
| CERT | 0x12003000 | 证书操作事件。 |
| KIA\_CREATE | 0x1C00000B | KIA文件创建事件。 |
| KIA\_READ | 0x1C000012 | KIA文件读取事件。 |
| KIA\_VARIANT | 0x1C00000C | 关键信息资产（KIA）文件变化事件。 |
| KIA\_INTERCEPT | 0x1C00000A | KIA文件拦截事件。 |
| PERMISSION | 0x0B000000 | 应用程序权限更改事件。 |
| DNS | 0x03000001 | DNS审计事件。 |
| APP\_INSTALL\_INTERCEPTED | 0x18000100 | 应用程序安装拦截事件。 |
| APP\_UNINSTALL\_INTERCEPTED | 0x18000101 | 应用程序卸载拦截事件。 |
| APP\_UPDATE\_INTERCEPTED | 0x18000102 | 应用程序更新拦截事件。 |
| APP\_RECOVER\_INTERCEPTED | 0x18000103 | 应用程序恢复拦截事件。 |
| APP\_START\_INTERCEPTED | 0x18000104 | 应用程序启动拦截事件。 |
| USB\_ACCESS\_INTERCEPTED | 0x30000000 | USB访问拦截事件。 |
| SMB\_FILE\_SEND | 0x0F000001 | SMB(Samba)外发事件。  **起始版本：** 6.1.0(23) |
| KIA\_PRE\_OPEN | 0x1C000014 | KIA文件秒开事件。  **起始版本：** 6.1.0(23) |
| HDC\_DEBUG | 0x27000100 | HDC(HarmonyOS Device Connector)调测文件事件。  **起始版本：** 6.1.0(23) |
| HDC\_DEBUG\_INTERCEPTED | 0x27000101 | HDC(HarmonyOS Device Connector)调测拦截事件。  **起始版本：** 6.1.0(23) |
| USER\_SPACE\_DATA\_TRANSFER | 0x2F000000 | 多用户空间数据互传事件。  **起始版本：** 6.1.0(23) |
| USER\_SPACE\_DATA\_TRANSFER\_POLICY | 0x2F000001 | 多用户空间互换审核策略事件。  **起始版本：** 6.1.0(23) |
| SERIAL\_PORT\_ACCESS | 0x30000100 | 串口访问审计事件。  **起始版本：** 6.1.0(23) |
| NETWORK\_INTERCEPTED | 0x03000002 | 网络拦截事件。  **起始版本：** 6.1.0(23) |
| WIFI\_INTERCEPTED | 0x03000100 | Wi-Fi拦截事件。  **起始版本：** 6.1.0(23) |
| PRINT\_INTERCEPTED | 0x2E000001 | 打印拦截事件。  **起始版本：** 6.1.0(23) |

## FilterType

PC/2in1

事件过滤类型枚举。

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EVENT\_TYPE\_EQUAL | 0x00000100 | 事件类型的过滤器类型。 |
| EVENT\_SUBTYPE\_EQUAL | 0x00000200 | 事件子类型的过滤器类型。 |
| FILE\_PATH\_EQUAL | 0x00010000 | 文件路径类型的过滤器类型。 |
| FILE\_PATH\_PREFIX | 0x00010001 | 文件路径前缀类型的过滤器类型。 |
| FILE\_PATH\_SUFFIX | 0x00010002 | 文件路径后缀类型的过滤器类型。 |
| PROCESS\_UID\_EQUAL | 0x00020000 | 过滤进程的UID类型。 |
| PROCESS\_PID\_EQUAL | 0x00020100 | 过滤进程ID类型。 |
| PROCESS\_NAME\_EQUAL | 0x00020200 | 筛选进程名称类型。 |
| PROCESS\_NAME\_PREFIX | 0x00020201 | 进程名称前缀的过滤类型。 |
| PROCESS\_NAME\_SUFFIX | 0x00020202 | 进程名称后缀的过滤类型。 |

## AuthEvent

PC/2in1

阻断类事件枚举。

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FILE\_CREATE | 0x1C801100 | 文件创建阻断事件。 |
| FILE\_OPEN | 0x1C801101 | 文件打开阻断事件。 |
| FILE\_RENAME | 0x1C801102 | 文件重命名阻断事件。 |
| FILE\_DELETE | 0x1C801103 | 文件删除阻断事件。 |
| FILE\_SETEXTATTR | 0x1C801104 | 文件设置扩展属性的阻断事件。 |
| FILE\_DELETEEXTATTR | 0x1C801105 | 文件删除扩展属性的阻断事件。 |

## AuthResult

PC/2in1

阻断结果的枚举。

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ALLOW | 0 | 对阻断事件放行操作。 |
| DENY | 1 | 对阻断事件拒绝操作。 |

## on('auditEventOccur')

PC/2in1

on(type: 'auditEventOccur', auditEventInfo: [AuditEventInfo](devicesecurity-securityaudit-api.md#auditeventinfo), callback: Callback<[AuditEvent](devicesecurity-securityaudit-api.md#auditevent)>): void

订阅安全审计数据。

**需要权限：** ohos.permission.QUERY\_AUDIT\_EVENT

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型名称，固定值 'auditEventOccur'，表示审计事件。 |
| auditEventInfo | [AuditEventInfo](devicesecurity-securityaudit-api.md#auditeventinfo) | 是 | 订阅的审计数据信息。 |
| callback | Callback<[AuditEvent](devicesecurity-securityaudit-api.md#auditevent)> | 是 | 用于接收审计事件的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |

**示例：**

```
1. import { securityAudit } from '@kit.DeviceSecurityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "SecurityAuditAuditJsTest";
6. const callback = (event: securityAudit.AuditEvent) => {
7. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func eventId= ' + event.eventId);
8. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func version= ' + event.version);
9. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func content= ' + event.content);
10. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func timestamp= ' + event.timestamp);
11. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func userId= ' + event.userId);
12. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func deviceId= ' + event.deviceId);
13. };
14. let auditEventInfo: securityAudit.AuditEventInfo = {
15. eventId: 0x810800800
16. };

18. try {
19. hilog.info(0x0000, TAG, 'on begin.');
20. securityAudit.on('auditEventOccur', auditEventInfo, callback);
21. hilog.info(0x0000, TAG, 'Succeeded in on.');
22. } catch (err) {
23. let e: BusinessError = err as BusinessError;
24. hilog.error(0x0000, TAG, 'on failed: %{public}d %{public}s', e.code, e.message);
25. }
```

## off('auditEventOccur')

PC/2in1

off(type: 'auditEventOccur', auditEventInfo: [AuditEventInfo](devicesecurity-securityaudit-api.md#auditeventinfo), callback?: Callback<[AuditEvent](devicesecurity-securityaudit-api.md#auditevent)>): void

取消订阅安全审计数据。

**需要权限：** ohos.permission.QUERY\_AUDIT\_EVENT

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件类型名称，固定值 ‘auditEventOccur’，表示审计事件。 |
| auditEventInfo | [AuditEventInfo](devicesecurity-securityaudit-api.md#auditeventinfo) | 是 | 取消订阅的审计数据信息。 |
| callback | Callback<[AuditEvent](devicesecurity-securityaudit-api.md#auditevent)> | 否 | 用于接收审计数据的回调函数。如果传入了callback，则取消该callback的订阅，否则取消所有callback的订阅。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |

**示例：**

```
1. import { securityAudit } from '@kit.DeviceSecurityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "SecurityAuditAuditJsTest";
6. let auditEventInfo: securityAudit.AuditEventInfo = {
7. eventId: 0x810800800
8. };

10. try {
11. hilog.info(0x0000, TAG, 'off begin.');
12. securityAudit.off('auditEventOccur', auditEventInfo);
13. hilog.info(0x0000, TAG, 'Succeeded in off.');
14. } catch (err) {
15. let e: BusinessError = err as BusinessError;
16. hilog.error(0x0000, TAG, 'off failed: %{public}d %{public}s', e.code, e.message);
17. }
```

## Filter

PC/2in1

用户提供的过滤条件信息。

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isInclude | boolean | 否 | 否 | 过滤标签，决定符合条件的事件是否返回给订阅者。  **true**：设置反过滤，符合过滤条件的事件将返回给订阅者。  **false**：设置过滤，符合过滤条件的事件将不会返回给订阅者。 |
| type | [FilterType](devicesecurity-securityaudit-api.md#filtertype) | 否 | 否 | 过滤类型。 |
| values | string[] | 否 | 否 | 过滤条件的值的数组。 |

## Client

PC/2in1

为通知客户端提供条件。

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 6.0.0(20)

说明

需要通过[newClient](devicesecurity-securityaudit-api.md#newclient)构造实例。

### subscribe

PC/2in1

subscribe(events: NotifyEvent[]): void

订阅通知事件。

**需要权限**：ohos.permission.QUERY\_AUDIT\_EVENT

**系统能力**：SystemCapability.Security.SecurityAudit

**起始版本**：6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| events | [NotifyEvent](devicesecurity-securityaudit-api.md#notifyevent)[] | 是 | 需要订阅的通知事件。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |
| 1012000001 | Internal error. |

**示例：**

```
1. import { securityAudit } from '@kit.DeviceSecurityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let client: securityAudit.Client | undefined = undefined;
6. const TAG = "SecurityAuditJsTest";
7. const callback = (event: securityAudit.AuditEvent) => {
8. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func eventId= ' + event.eventId);
9. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func version= ' + event.version);
10. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func content= ' + event.content);
11. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func timestamp= ' + event.timestamp);
12. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func userId= ' + event.userId);
13. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func deviceId= ' + event.deviceId);
14. };
15. try {
16. client = securityAudit.newClient(callback);
17. client?.subscribe([0x02D000000]);
18. } catch (err) {
19. let e: BusinessError = err as BusinessError;
20. hilog.error(0x0000, TAG, 'subscribe failed: %{public}d %{public}s', e.code, e.message);
21. }
```

### unsubscribe

PC/2in1

unsubscribe(events: NotifyEvent[]): void

取消订阅通知事件。

**需要权限**：ohos.permission.QUERY\_AUDIT\_EVENT

**系统能力**：SystemCapability.Security.SecurityAudit

**起始版本**：6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| events | [NotifyEvent](devicesecurity-securityaudit-api.md#notifyevent)[] | 是 | 已订阅的通知事件。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |
| 1012000001 | Internal error. |

**示例：**

```
1. import { securityAudit } from '@kit.DeviceSecurityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let client: securityAudit.Client | undefined = undefined;
6. const TAG = "SecurityAuditJsTest";
7. const callback = (event: securityAudit.AuditEvent) => {
8. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func eventId= ' + event.eventId);
9. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func version= ' + event.version);
10. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func content= ' + event.content);
11. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func timestamp= ' + event.timestamp);
12. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func userId= ' + event.userId);
13. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func deviceId= ' + event.deviceId);
14. };
15. try {
16. client = securityAudit.newClient(callback);
17. client?.unsubscribe([0x02D000000]);
18. } catch (err) {
19. let e: BusinessError = err as BusinessError;
20. hilog.error(0x0000, TAG, 'unsubscribe failed: %{public}d %{public}s', e.code, e.message);
21. }
```

### addFilter

PC/2in1

addFilter(event: NotifyEvent, filter: Filter): void

为通知事件添加过滤条件，符合过滤条件的事件将根据过滤器中的过滤标签决定是否返回给用户。

**需要权限**：ohos.permission.QUERY\_AUDIT\_EVENT

**系统能力**：SystemCapability.Security.SecurityAudit

**起始版本**：6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [NotifyEvent](devicesecurity-securityaudit-api.md#notifyevent) | 是 | 通知事件ID。 |
| filter | [Filter](devicesecurity-securityaudit-api.md#filter) | 是 | 通知事件的过滤器。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |
| 1012000001 | Internal error. |
| 1012000004 | The number of filters exceeds the upper limit. |
| 1012000005 | The event does not support the filter condition. |

**示例：**

```
1. import { securityAudit } from '@kit.DeviceSecurityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let client: securityAudit.Client | undefined = undefined;
6. const TAG = "SecurityAuditJsTest";
7. const callback = (event: securityAudit.AuditEvent) => {
8. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func eventId= ' + event.eventId);
9. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func version= ' + event.version);
10. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func content= ' + event.content);
11. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func timestamp= ' + event.timestamp);
12. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func userId= ' + event.userId);
13. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func deviceId= ' + event.deviceId);
14. };
15. let filter : securityAudit.Filter = {
16. type: 0x00000200,
17. isInclude: true,
18. values : ["2"]
19. };
20. try {
21. client = securityAudit.newClient(callback);
22. client?.addFilter(0x02D000000, filter);
23. } catch (err) {
24. let e: BusinessError = err as BusinessError;
25. hilog.error(0x0000, TAG, 'addFilter failed: %{public}d %{public}s', e.code, e.message);
26. }
```

### removeFilter

PC/2in1

removeFilter(event: NotifyEvent, filter: Filter): void

删除通知事件的过滤条件，满足该过滤条件的事件将不会再根据过滤器中的过滤标签进行处理。

**需要权限**：ohos.permission.QUERY\_AUDIT\_EVENT

**系统能力**：SystemCapability.Security.SecurityAudit

**起始版本**：6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [NotifyEvent](devicesecurity-securityaudit-api.md#notifyevent) | 是 | 通知事件ID 。 |
| filter | [Filter](devicesecurity-securityaudit-api.md#filter) | 是 | 通知事件的过滤器。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |
| 1012000001 | Internal error. |
| 1012000005 | The event does not support the filter condition. |

**示例：**

```
1. import { securityAudit } from '@kit.DeviceSecurityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let client: securityAudit.Client | undefined = undefined;
6. const TAG = "SecurityAuditJsTest";
7. const callback = (event: securityAudit.AuditEvent) => {
8. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func eventId= ' + event.eventId);
9. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func version= ' + event.version);
10. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func content= ' + event.content);
11. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func timestamp= ' + event.timestamp);
12. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func userId= ' + event.userId);
13. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func deviceId= ' + event.deviceId);
14. };
15. let filter : securityAudit.Filter = {
16. type: 0x00000200,
17. isInclude: true,
18. values : ["2"]
19. };
20. try {
21. client = securityAudit.newClient(callback);
22. client?.removeFilter(0x02D000000, filter);
23. } catch (err) {
24. let e: BusinessError = err as BusinessError;
25. hilog.error(0x0000, TAG, 'removeFilter failed: %{public}d %{public}s', e.code, e.message);
26. }
```

## newClient

PC/2in1

newClient(callback: Callback<[AuditEvent](devicesecurity-securityaudit-api.md#auditevent)>): Client

创建一个新的通知客户端，该客户端提供的方法可以实现通知类事件的订阅、过滤功能。

**需要权限：** ohos.permission.QUERY\_AUDIT\_EVENT

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[AuditEvent](devicesecurity-securityaudit-api.md#auditevent)> | 是 | 用于接收审计数据的回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Client](devicesecurity-securityaudit-api.md#client) | 通知类客户端实例对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |
| 1012000001 | Internal error. |
| 1012000002 | The number of clients exceeds the global upper limit. |
| 1012000003 | The number of clients exceeds the current process upper limit. |

**示例：**

```
1. import { securityAudit } from '@kit.DeviceSecurityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let client: securityAudit.Client | undefined = undefined;
6. const TAG = "SecurityAuditJsTest";
7. const callback = (event: securityAudit.AuditEvent) => {
8. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func eventId= ' + event.eventId);
9. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func version= ' + event.version);
10. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func content= ' + event.content);
11. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func timestamp= ' + event.timestamp);
12. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func userId= ' + event.userId);
13. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func deviceId= ' + event.deviceId);
14. };
15. try {
16. client = securityAudit.newClient(callback);
17. } catch (err) {
18. let e: BusinessError = err as BusinessError;
19. hilog.error(0x0000, TAG, 'newClient failed: %{public}d %{public}s', e.code, e.message);
20. }
```

## deleteClient

PC/2in1

deleteClient(client: Client): void

删除通知客户端，用户将无法使用该客户端提供的方法，并会清空客户端记录的订阅与过滤信息。

**需要权限：** ohos.permission.QUERY\_AUDIT\_EVENT

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| client | [Client](devicesecurity-securityaudit-api.md#client) | 是 | 通知客户端信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |
| 1012000001 | Internal error. |

**示例：**

```
1. import { securityAudit } from '@kit.DeviceSecurityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let client: securityAudit.Client | undefined = undefined;
6. const TAG = "SecurityAuditJsTest";
7. const callback = (event: securityAudit.AuditEvent) => {
8. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func eventId= ' + event.eventId);
9. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func version= ' + event.version);
10. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func content= ' + event.content);
11. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func timestamp= ' + event.timestamp);
12. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func userId= ' + event.userId);
13. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func deviceId= ' + event.deviceId);
14. };
15. try {
16. client = securityAudit.newClient(callback);
17. securityAudit.deleteClient(client);
18. } catch (err) {
19. let e: BusinessError = err as BusinessError;
20. hilog.error(0x0000, TAG, 'deleteClient failed: %{public}d %{public}s', e.code, e.message);
21. }
```

## AuthClient

PC/2in1

为阻断类事件客户端提供条件。

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 6.0.0(20)

说明

需要通过[newAuthClient](devicesecurity-securityaudit-api.md#newauthclient)构造实例。

### subscribe

PC/2in1

subscribe(events: AuthEvent[]): void

订阅阻断事件。

**需要权限**：ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**系统能力**：SystemCapability.Security.SecurityAudit

**起始版本**：6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| events | [AuthEvent](devicesecurity-securityaudit-api.md#authevent)[] | 是 | 要订阅的阻断事件。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |
| 1012000001 | Internal error. |

**示例：**

```
1. import { securityAudit } from '@kit.DeviceSecurityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "SecurityAuditAuthJsTest";
6. let authClient: securityAudit.AuthClient | undefined = undefined;
7. const callback = (event: securityAudit.AuditEvent) => {
8. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func eventId= ' + event.eventId);
9. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func content= ' + event.content);
10. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func metadata= ' + event.metadata);
11. };
12. try {
13. authClient = securityAudit.newAuthClient(callback);
14. } catch (err) {
15. let e: BusinessError = err as BusinessError;
16. hilog.error(0x0000, TAG, 'newAuthClient failed: %{public}d %{public}s', e.code, e.message);
17. }
18. try {
19. authClient?.subscribe([securityAudit.AuthEvent.FILE_CREATE]);
20. } catch (err) {
21. let e: BusinessError = err as BusinessError;
22. hilog.error(0x0000, TAG, 'subscribe failed: %{public}d %{public}s', e.code, e.message);
23. }
```

### unsubscribe

PC/2in1

unsubscribe(events: AuthEvent[]): void

取消订阅阻断事件。

**需要权限**：ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**系统能力**：SystemCapability.Security.SecurityAudit

**起始版本**：6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| events | [AuthEvent](devicesecurity-securityaudit-api.md#authevent)[] | 是 | 已订阅的阻断事件。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |
| 1012000001 | Internal error. |

**示例：**

```
1. import { securityAudit } from '@kit.DeviceSecurityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "SecurityAuditAuthJsTest";
6. let authClient: securityAudit.AuthClient | undefined = undefined;
7. const callback = (event: securityAudit.AuditEvent) => {
8. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func eventId= ' + event.eventId);
9. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func content= ' + event.content);
10. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func metadata= ' + event.metadata);
11. };
12. try {
13. authClient = securityAudit.newAuthClient(callback);
14. } catch (err) {
15. let e: BusinessError = err as BusinessError;
16. hilog.error(0x0000, TAG, 'newAuthClient failed: %{public}d %{public}s', e.code, e.message);
17. }
18. try {
19. authClient?.subscribe([securityAudit.AuthEvent.FILE_CREATE]);
20. } catch (err) {
21. let e: BusinessError = err as BusinessError;
22. hilog.error(0x0000, TAG, 'subscribe failed: %{public}d %{public}s', e.code, e.message);
23. }
24. try {
25. authClient?.unsubscribe([securityAudit.AuthEvent.FILE_CREATE]);
26. } catch (err) {
27. let e: BusinessError = err as BusinessError;
28. hilog.error(0x0000, TAG, 'unsubscribe failed: %{public}d %{public}s', e.code, e.message);
29. }
```

### addFilter

PC/2in1

addFilter(event: AuthEvent, filter: Filter): void

为阻断事件添加过滤条件，符合过滤条件的事件将根据过滤器中的过滤标签决定是否返回给用户。

**需要权限**：ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**系统能力**：SystemCapability.Security.SecurityAudit

**起始版本**：6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [AuthEvent](devicesecurity-securityaudit-api.md#authevent) | 是 | 阻断事件ID。 |
| filter | [Filter](devicesecurity-securityaudit-api.md#filter) | 是 | 阻断事件的过滤器。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |
| 1012000001 | Internal error. |
| 1012000004 | The number of filters exceeds the upper limit. |
| 1012000005 | The event does not support the filter condition. |

**示例：**

```
1. import { securityAudit } from '@kit.DeviceSecurityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "SecurityAuditAuthJsTest";
6. let authClient: securityAudit.AuthClient | undefined = undefined;
7. const callback = (event: securityAudit.AuditEvent) => {
8. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func eventId= ' + event.eventId);
9. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func content= ' + event.content);
10. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func metadata= ' + event.metadata);
11. };
12. try {
13. authClient = securityAudit.newAuthClient(callback);
14. } catch (err) {
15. let e: BusinessError = err as BusinessError;
16. hilog.error(0x0000, TAG, 'newAuthClient failed: %{public}d %{public}s', e.code, e.message);
17. }
18. let filter : securityAudit.Filter = {
19. type: securityAudit.FilterType.PROCESS_PID_EQUAL,
20. isInclude: true,
21. values : ["2"]
22. };
23. try {
24. authClient?.addFilter(securityAudit.AuthEvent.FILE_CREATE, filter);
25. } catch (err) {
26. let e: BusinessError = err as BusinessError;
27. hilog.error(0x0000, TAG, 'addFilter failed: %{public}d %{public}s', e.code, e.message);
28. }
```

### removeFilter

PC/2in1

removeFilter(event: AuthEvent, filter: Filter): void

删除阻断事件的过滤条件，满足该过滤条件的事件将不会再根据过滤器中的过滤标签进行处理。

**需要权限**：ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**系统能力**：SystemCapability.Security.SecurityAudit

**起始版本**：6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [AuthEvent](devicesecurity-securityaudit-api.md#authevent) | 是 | 阻断事件ID 。 |
| filter | [Filter](devicesecurity-securityaudit-api.md#filter) | 是 | 阻断事件的过滤器。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |
| 1012000001 | Internal error. |
| 1012000005 | The event does not support the filter condition. |

**示例：**

```
1. import { securityAudit } from '@kit.DeviceSecurityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "SecurityAuditAuthJsTest";
6. let authClient: securityAudit.AuthClient | undefined = undefined;
7. const callback = (event: securityAudit.AuditEvent) => {
8. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func eventId= ' + event.eventId);
9. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func content= ' + event.content);
10. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func metadata= ' + event.metadata);
11. };
12. try {
13. authClient = securityAudit.newAuthClient(callback);
14. } catch (err) {
15. let e: BusinessError = err as BusinessError;
16. hilog.error(0x0000, TAG, 'newAuthClient failed: %{public}d %{public}s', e.code, e.message);
17. }
18. let filter : securityAudit.Filter = {
19. type: securityAudit.FilterType.PROCESS_PID_EQUAL,
20. isInclude: true,
21. values : ["2"]
22. };
23. try {
24. authClient?.addFilter(securityAudit.AuthEvent.FILE_CREATE, filter);
25. } catch (err) {
26. let e: BusinessError = err as BusinessError;
27. hilog.error(0x0000, TAG, 'addFilter failed: %{public}d %{public}s', e.code, e.message);
28. }
29. try {
30. authClient?.removeFilter(securityAudit.AuthEvent.FILE_CREATE, filter);
31. } catch (err) {
32. let e: BusinessError = err as BusinessError;
33. hilog.error(0x0000, TAG, 'removeFilter failed: %{public}d %{public}s', e.code, e.message);
34. }
```

### auth

PC/2in1

auth(auditEvent: AuditEvent, authResult: AuthResult): void

设置阻断事件的阻断结果，审计模块会根据阻断结果对事件进行放行或拒绝的处理。

**需要权限**：ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**系统能力**：SystemCapability.Security.SecurityAudit

**起始版本**：6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| auditEvent | [AuditEvent](devicesecurity-securityaudit-api.md#auditevent) | 是 | 阻断事件信息 。 |
| authResult | [AuthResult](devicesecurity-securityaudit-api.md#authresult) | 是 | 阻断结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |
| 1012000001 | Internal error. |
| 1012000007 | The auth event cannot be found. |

**示例：**

```
1. import { securityAudit } from '@kit.DeviceSecurityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "SecurityAuditAuthJsTest";
6. let authClient: securityAudit.AuthClient | undefined = undefined;
7. const allowEventCallback = (event: securityAudit.AuditEvent) => {
8. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func eventId= ' + event.eventId);
9. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func content= ' + event.content);
10. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func metadata= ' + event.metadata);
11. try {
12. authClient?.auth(event, securityAudit.AuthResult.ALLOW);
13. } catch (error) {
14. let e: BusinessError = error as BusinessError;
15. hilog.error(0x0000, TAG, 'allowEventCallback', 'auth error:' + e.code);
16. }
17. };
18. try {
19. authClient = securityAudit.newAuthClient(allowEventCallback);
20. } catch (err) {
21. let e: BusinessError = err as BusinessError;
22. hilog.error(0x0000, TAG, 'newAuthClient failed: %{public}d %{public}s', e.code, e.message);
23. }
```

## newAuthClient

PC/2in1

newAuthClient(callback: Callback<[AuditEvent](devicesecurity-securityaudit-api.md#auditevent)>): AuthClient

创建一个新的阻断客户端，该客户端提供的方法可以实现阻断类事件的订阅、过滤和阻断功能。

**需要权限：** ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[AuditEvent](devicesecurity-securityaudit-api.md#auditevent)> | 是 | 用于接收审计数据的回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AuthClient](devicesecurity-securityaudit-api.md#authclient) | 阻断类客户端实例对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |
| 1012000001 | Internal error. |
| 1012000002 | The number of clients exceeds the global upper limit. |
| 1012000003 | The number of clients exceeds the current process upper limit. |

**示例：**

```
1. import { securityAudit } from '@kit.DeviceSecurityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "SecurityAuditAuthJsTest";
6. let authClient: securityAudit.AuthClient | undefined = undefined;
7. const callback = (event: securityAudit.AuditEvent) => {
8. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func eventId= ' + event.eventId);
9. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func content= ' + event.content);
10. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func metadata= ' + event.metadata);
11. };
12. try {
13. authClient = securityAudit.newAuthClient(callback);
14. } catch (err) {
15. let e: BusinessError = err as BusinessError;
16. hilog.error(0x0000, TAG, 'newAuthClient failed: %{public}d %{public}s', e.code, e.message);
17. }
```

## deleteAuthClient

PC/2in1

deleteAuthClient(client: AuthClient): void

删除阻断客户端，用户将无法使用该客户端提供的方法，并会清空客户端记录的订阅与过滤信息。

**需要权限：** ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| client | [AuthClient](devicesecurity-securityaudit-api.md#authclient) | 是 | 阻断客户端信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |
| 1012000001 | Internal error. |

**示例：**

```
1. import { securityAudit } from '@kit.DeviceSecurityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "SecurityAuditAuthJsTest";
6. let authClient: securityAudit.AuthClient | undefined = undefined;
7. const callback = (event: securityAudit.AuditEvent) => {
8. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func eventId= ' + event.eventId);
9. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func content= ' + event.content);
10. hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func metadata= ' + event.metadata);
11. };
12. try {
13. authClient = securityAudit.newAuthClient(callback);
14. } catch (err) {
15. let e: BusinessError = err as BusinessError;
16. hilog.error(0x0000, TAG, 'newAuthClient failed: %{public}d %{public}s', e.code, e.message);
17. }
18. try {
19. securityAudit.deleteAuthClient(authClient);
20. } catch (err) {
21. let e: BusinessError = err as BusinessError;
22. hilog.error(0x0000, TAG, 'deleteAuthClient failed: %{public}d %{public}s', e.code, e.message);
23. }
```

## queryAllProcesses

PC/2in1

queryAllProcesses(): string;

查询获取所有的应用进程信息。

**需要权限：** ohos.permission.QUERY\_AUDIT\_EVENT

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 应用进程信息内容，内容为json格式字符串。例如：{"1": {}}。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |
| 1012000001 | Internal error. |

**示例：**

```
1. import { securityAudit } from '@kit.DeviceSecurityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "SecurityAuditJsTest";
6. try {
7. hilog.info(0x0000, TAG, 'queryAllProcesses begin.');
8. const result = securityAudit.queryAllProcesses();
9. hilog.info(0x0000, TAG, 'Succeeded in queryAllProcesses.');
10. } catch (err) {
11. let e: BusinessError = err as BusinessError;
12. hilog.error(0x0000, TAG, 'queryAllProcesses failed: %{public}d %{public}s', e.code, e.message);
13. }
```

## queryProcesses

PC/2in1

queryProcesses(pids: number[]): string;

查询获取输入的PID的应用进程信息。

**需要权限：** ohos.permission.QUERY\_AUDIT\_EVENT

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pids | number[] | 是 | 要查询的进程ID组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 应用进程信息内容，内容为json格式字符串。例如：{"1": {}}。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |
| 1012000001 | Internal error. |
| 1012000006 | The number of queried processes exceeds the threshold. |

**示例：**

```
1. import { securityAudit } from '@kit.DeviceSecurityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "SecurityAuditJsTest";
6. let pids: number[] = [1, 2];
7. try {
8. hilog.info(0x0000, TAG, 'queryProcesses begin.');
9. const result = securityAudit.queryProcesses(pids);
10. hilog.info(0x0000, TAG, 'Succeeded in queryProcesses.');
11. } catch (err) {
12. let e: BusinessError = err as BusinessError;
13. hilog.error(0x0000, TAG, 'queryProcesses failed: %{public}d %{public}s', e.code, e.message);
14. }
```
