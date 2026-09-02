---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-securityaudit-api
title: SecurityAudit（安全审计）
breadcrumb: API参考 > 系统 > 安全 > Device Security Kit（设备安全服务） > ArkTS API > SecurityAudit（安全审计）
category: harmonyos-references
scraped_at: 2026-09-02T15:01:43+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:016e98c86c0aa25283f598c755f9bf906df18b32289a9f61f92d655fdc5ae190
---

提供统一的安全审计数据订阅与取消订阅接口，应用可以获取设备上的安全审计数据，以支撑审计业务。

**起始版本：** 5.0.0(12)

## 导入模块

```typescript
import { securityAudit } from '@kit.DeviceSecurityKit';
```

## AuditEventInfo

用于订阅或取消订阅接口的请求参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| eventId | number | 否 | 否 | 审计事件ID，用于指定需要获取的安全审计数据。例如：0x810800800  审计事件ID的取值范围是[0, 0xFFFFFFFFF]。 |

## AuditEvent

安全审计数据。

**模型约束：** 此接口仅可在Stage模型下使用。

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

通知类事件枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PASTEBOARD | 0x27000000 | 剪贴板复制粘贴事件。 |
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
| CS\_VERIFY\_NULL | 0x12001081 | 应用代码未签名。  **起始版本：** 6.1.1(24) |
| CS\_VERIFY\_ABNORMAL | 0x12001082 | 应用代码验签异常。  **起始版本：** 6.1.1(24) |
| FS\_MOUNT\_ABNORMAL | 0x1C001102 | 系统目录异常挂载。  **起始版本：** 6.1.1(24) |
| DRIVER\_CS\_ABNORMAL | 0x1C001200 | 驱动代码验签异常。  **起始版本：** 6.1.1(24) |
| DRIVER\_MMAP\_ABNORMAL | 0x1C001201 | 驱动非法映射内核内存。  **起始版本：** 6.1.1(24) |
| KERNEL\_MEMORY\_ABNORMAL | 0x1C001300 | 内核内存异常使用。  **起始版本：** 6.1.1(24) |
| PROCESS\_DEBUG\_ABNORMAL | 0x1C001401 | 进程异常调试。  **起始版本：** 6.1.1(24) |
| PROCESS\_CRASH\_ABNORMAL | 0x1C001402 | 进程异常崩溃。  **起始版本：** 6.1.1(24) |
| PROCESS\_PRIVILEGE\_ESCALATION | 0x1C001403 | 进程提权。  **起始版本：** 6.1.1(24) |
| FILE\_SHARE | 0x0F000002 | 文件分享事件。  **起始版本：** 26.0.0 |
| DATA\_DRAG | 0x0F000003 | 数据拖拽事件。  **起始版本：** 26.0.0 |
| DLP\_FILE\_ACCESS | 0x0F000006 | DLP文件访问。  **起始版本：** 26.0.0 |
| FILE\_CREATE | 0x1C001104 | 文件创建事件。  **起始版本：** 26.0.0 |
| FILE\_OPEN | 0x1C001105 | 文件打开事件。  **起始版本：** 26.0.0 |
| FILE\_CLOSE | 0x1C001106 | 文件关闭事件。  **起始版本：** 26.0.0 |
| FILE\_DELETE | 0x1C001107 | 文件删除事件。  **起始版本：** 26.0.0 |
| FILE\_RENAME | 0x1C001108 | 文件重命名事件。  **起始版本：** 26.0.0 |
| FILE\_COPY | 0x1C001109 | 文件复制事件。  **起始版本：** 26.0.0 |
| FILE\_SETOWNER | 0x1C00110A | 文件修改所有者事件。  **起始版本：** 26.0.0 |
| FILE\_SETMODE | 0x1C00110B | 文件修改mode事件。  **起始版本：** 26.0.0 |
| FILE\_SETEXTATTR | 0x1C00110C | 文件设置扩展属性事件。  **起始版本：** 26.0.0 |
| FILE\_DELETEEXTATTR | 0x1C00110D | 文件删除扩展属性事件。  **起始版本：** 26.0.0 |
| FILE\_WRITE | 0x1C00110E | 文件写事件。  **起始版本：** 26.0.0 |
| BLUETOOTH\_INTERCEPTED | 0x03000200 | 蓝牙拦截事件。  **起始版本：** 26.0.0 |
| DISC\_BURNING | 0x0F000004 | 光盘刻录事件。  **起始版本：** 26.0.0 |
| MEDIA\_FILE\_ACCESS | 0x0F000005 | 媒体文件访问事件。  **起始版本：** 26.0.0 |
| ACCOUNT\_MANAGEMENT | 0x10000103 | 账户管理事件。  **起始版本：** 26.0.0 |
| DEVICE\_POWER\_ON | 0x16000001 | 设备开机事件。  **起始版本：** 26.0.0 |
| DEVICE\_POWER\_OFF | 0x16000002 | 设备关机事件。  **起始版本：** 26.0.0 |
| AUDIO\_INTERFACE\_ACCESS | 0x1A000001 | 音频接口访问事件。  **起始版本：** 26.0.0 |
| VIDEO\_INTERFACE\_ACCESS | 0x1A000002 | 视频接口访问事件。  **起始版本：** 26.0.0 |
| SERIAL\_PORT\_INTERCEPTED | 0x30000101 | 串口拦截事件。  **起始版本：** 26.0.0 |

## FilterType

事件过滤类型枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EVENT\_TYPE\_EQUAL | 0x00000100 | 事件类型的过滤器类型。 |
| EVENT\_SUBTYPE\_EQUAL | 0x00000200 | 事件子类型的过滤器类型。 |
| FILE\_PATH\_EQUAL | 0x00010000 | 文件路径类型的过滤器类型。 |
| FILE\_PATH\_PREFIX | 0x00010001 | 文件路径前缀类型的过滤器类型。 |
| FILE\_PATH\_SUFFIX | 0x00010002 | 文件路径后缀类型的过滤器类型。 |
| FILE\_PATH\_REGULAR | 0x00010003 | 文件路径正则表达式的过滤类型。  **起始版本：** 26.0.0 |
| PROCESS\_UID\_EQUAL | 0x00020000 | 过滤进程的UID类型。 |
| PROCESS\_PID\_EQUAL | 0x00020100 | 过滤进程ID类型。 |
| PROCESS\_NAME\_EQUAL | 0x00020200 | 筛选进程名称类型。 |
| PROCESS\_NAME\_PREFIX | 0x00020201 | 进程名称前缀的过滤类型。 |
| PROCESS\_NAME\_SUFFIX | 0x00020202 | 进程名称后缀的过滤类型。 |

## AuthEvent

阻断类事件枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

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
| FILE\_READ\_END | 0x1C801106 | 文件读结束阻断事件。  **起始版本：** 26.0.0 |
| PROCESS\_EXEC | 0x1C801400 | 进程执行的阻断事件。  **起始版本：** 26.0.0 |

## AuthResult

阻断结果的枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ALLOW | 0 | 对阻断事件放行操作。 |
| DENY | 1 | 对阻断事件拒绝操作。 |

## on('auditEventOccur')

on(type: 'auditEventOccur', auditEventInfo: [AuditEventInfo](devicesecurity-securityaudit-api.md#auditeventinfo), callback: Callback<[AuditEvent](devicesecurity-securityaudit-api.md#auditevent)>): void

订阅安全审计数据。

**模型约束：** 此接口仅可在Stage模型下使用。

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

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[安全审计错误码](errorcode-devicesecurity-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |

**示例：**

```typescript
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'SecurityAuditAuditJsTest';
const callback = (event: securityAudit.AuditEvent) => {
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

## off('auditEventOccur')

off(type: 'auditEventOccur', auditEventInfo: [AuditEventInfo](devicesecurity-securityaudit-api.md#auditeventinfo), callback?: Callback<[AuditEvent](devicesecurity-securityaudit-api.md#auditevent)>): void

取消订阅安全审计数据。

**模型约束：** 此接口仅可在Stage模型下使用。

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

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[安全审计错误码](errorcode-devicesecurity-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |

**示例：**

```typescript
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'SecurityAuditAuditJsTest';
let auditEventInfo: securityAudit.AuditEventInfo = {
   eventId: 0x810800800
};

try {
  hilog.info(0x0000, TAG, 'off begin.');
  securityAudit.off('auditEventOccur', auditEventInfo);
  hilog.info(0x0000, TAG, 'Succeeded in off.');
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'off failed: %{public}d %{public}s', e.code, e.message);
}
```

## Filter

用户提供的过滤条件信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isInclude | boolean | 否 | 否 | 过滤标签，决定符合条件的事件是否返回给订阅者。  **true**：设置反过滤，符合过滤条件的事件将返回给订阅者。  **false**：设置过滤，符合过滤条件的事件将不会返回给订阅者。 |
| type | [FilterType](devicesecurity-securityaudit-api.md#filtertype) | 否 | 否 | 过滤类型。 |
| values | string[] | 否 | 否 | 过滤条件的值的数组。 |

## Client

为通知客户端提供条件。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 6.0.0(20)

**说明** 

需要通过[newClient](devicesecurity-securityaudit-api.md#newclient)构造实例。

### subscribe

subscribe(events: NotifyEvent[]): void

订阅通知事件。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限**：ohos.permission.QUERY\_AUDIT\_EVENT

**系统能力**：SystemCapability.Security.SecurityAudit

**起始版本**：6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| events | [NotifyEvent](devicesecurity-securityaudit-api.md#notifyevent)[] | 是 | 需要订阅的通知事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[安全审计错误码](errorcode-devicesecurity-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |
| 1012000001 | Internal error.Possible causes: 1. IPC cross-process invoking fails. 2. System service process is faulty. |

**示例：**

```typescript
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let client: securityAudit.Client | undefined = undefined;
const TAG = 'SecurityAuditJsTest';
const callback = (event: securityAudit.AuditEvent) => {
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func eventId= ' + event.eventId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func version= ' + event.version);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func content= ' + event.content);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func timestamp= ' + event.timestamp);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func userId= ' + event.userId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func deviceId= ' + event.deviceId);
};
try {
  client = securityAudit.newClient(callback);
  client?.subscribe([0x02D000000]);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'subscribe failed: %{public}d %{public}s', e.code, e.message);
}
```

### unsubscribe

unsubscribe(events: NotifyEvent[]): void

取消订阅通知事件。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限**：ohos.permission.QUERY\_AUDIT\_EVENT

**系统能力**：SystemCapability.Security.SecurityAudit

**起始版本**：6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| events | [NotifyEvent](devicesecurity-securityaudit-api.md#notifyevent)[] | 是 | 已订阅的通知事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[安全审计错误码](errorcode-devicesecurity-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |
| 1012000001 | Internal error.Possible causes: 1. IPC cross-process invoking fails. 2. System service process is faulty. |

**示例：**

```typescript
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let client: securityAudit.Client | undefined = undefined;
const TAG = 'SecurityAuditJsTest';
const callback = (event: securityAudit.AuditEvent) => {
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func eventId= ' + event.eventId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func version= ' + event.version);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func content= ' + event.content);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func timestamp= ' + event.timestamp);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func userId= ' + event.userId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func deviceId= ' + event.deviceId);
};
try {
  client = securityAudit.newClient(callback);
  client?.unsubscribe([0x02D000000]);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'unsubscribe failed: %{public}d %{public}s', e.code, e.message);
}
```

### addFilter

addFilter(event: NotifyEvent, filter: Filter): void

为通知事件添加过滤条件，符合过滤条件的事件将根据过滤器中的过滤标签决定是否返回给用户。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限**：ohos.permission.QUERY\_AUDIT\_EVENT

**系统能力**：SystemCapability.Security.SecurityAudit

**起始版本**：6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [NotifyEvent](devicesecurity-securityaudit-api.md#notifyevent) | 是 | 通知事件ID。 |
| filter | [Filter](devicesecurity-securityaudit-api.md#filter) | 是 | 通知事件的过滤器。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[安全审计错误码](errorcode-devicesecurity-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |
| 1012000001 | Internal error.Possible causes: 1. IPC cross-process invoking fails. 2. System service process is faulty. |
| 1012000004 | The number of filters exceeds the upper limit. |
| 1012000005 | The event does not support the filter condition. |

**示例：**

```typescript
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let client: securityAudit.Client | undefined = undefined;
const TAG = 'SecurityAuditJsTest';
const callback = (event: securityAudit.AuditEvent) => {
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func eventId= ' + event.eventId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func version= ' + event.version);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func content= ' + event.content);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func timestamp= ' + event.timestamp);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func userId= ' + event.userId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func deviceId= ' + event.deviceId);
};
let filter : securityAudit.Filter = {
  type: 0x00000200,
  isInclude: true,
  values : ["2"]
};
try {
  client = securityAudit.newClient(callback);
  client?.addFilter(0x02D000000, filter);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'addFilter failed: %{public}d %{public}s', e.code, e.message);
}
```

### removeFilter

removeFilter(event: NotifyEvent, filter: Filter): void

删除通知事件的过滤条件，满足该过滤条件的事件将不会再根据过滤器中的过滤标签进行处理。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限**：ohos.permission.QUERY\_AUDIT\_EVENT

**系统能力**：SystemCapability.Security.SecurityAudit

**起始版本**：6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [NotifyEvent](devicesecurity-securityaudit-api.md#notifyevent) | 是 | 通知事件ID 。 |
| filter | [Filter](devicesecurity-securityaudit-api.md#filter) | 是 | 通知事件的过滤器。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[安全审计错误码](errorcode-devicesecurity-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |
| 1012000001 | Internal error.Possible causes: 1. IPC cross-process invoking fails. 2. System service process is faulty. |
| 1012000005 | The event does not support the filter condition. |

**示例：**

```typescript
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let client: securityAudit.Client | undefined = undefined;
const TAG = 'SecurityAuditJsTest';
const callback = (event: securityAudit.AuditEvent) => {
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func eventId= ' + event.eventId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func version= ' + event.version);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func content= ' + event.content);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func timestamp= ' + event.timestamp);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func userId= ' + event.userId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func deviceId= ' + event.deviceId);
};
let filter : securityAudit.Filter = {
  type: 0x00000200,
  isInclude: true,
  values : ["2"]
};
try {
  client = securityAudit.newClient(callback);
  client?.removeFilter(0x02D000000, filter);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'removeFilter failed: %{public}d %{public}s', e.code, e.message);
}
```

## newClient

newClient(callback: Callback<[AuditEvent](devicesecurity-securityaudit-api.md#auditevent)>): Client

创建一个新的通知客户端，该客户端提供的方法可以实现通知类事件的订阅、过滤功能。

**模型约束：** 此接口仅可在Stage模型下使用。

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

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[安全审计错误码](errorcode-devicesecurity-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |
| 1012000001 | Internal error.Possible causes: 1. IPC cross-process invoking fails. 2. System service process is faulty. |
| 1012000002 | The number of clients exceeds the global upper limit. |
| 1012000003 | The number of clients exceeds the current process upper limit. |

**示例：**

```typescript
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let client: securityAudit.Client | undefined = undefined;
const TAG = 'SecurityAuditJsTest';
const callback = (event: securityAudit.AuditEvent) => {
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

## deleteClient

deleteClient(client: Client): void

删除通知客户端，用户将无法使用该客户端提供的方法，并会清空客户端记录的订阅与过滤信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.QUERY\_AUDIT\_EVENT

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| client | [Client](devicesecurity-securityaudit-api.md#client) | 是 | 通知客户端信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[安全审计错误码](errorcode-devicesecurity-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |
| 1012000001 | Internal error.Possible causes: 1. IPC cross-process invoking fails. 2. System service process is faulty. |

**示例：**

```typescript
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let client: securityAudit.Client | undefined = undefined;
const TAG = 'SecurityAuditJsTest';
const callback = (event: securityAudit.AuditEvent) => {
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func eventId= ' + event.eventId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func version= ' + event.version);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func content= ' + event.content);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func timestamp= ' + event.timestamp);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func userId= ' + event.userId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func deviceId= ' + event.deviceId);
};
try {
  client = securityAudit.newClient(callback);
  securityAudit.deleteClient(client);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'deleteClient failed: %{public}d %{public}s', e.code, e.message);
}
```

## AuthClient

为阻断类事件客户端提供条件。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 6.0.0(20)

**说明** 

需要通过[newAuthClient](devicesecurity-securityaudit-api.md#newauthclient)构造实例。

### subscribe

subscribe(events: AuthEvent[]): void

订阅阻断事件。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限**：ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**系统能力**：SystemCapability.Security.SecurityAudit

**起始版本**：6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| events | [AuthEvent](devicesecurity-securityaudit-api.md#authevent)[] | 是 | 要订阅的阻断事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[安全审计错误码](errorcode-devicesecurity-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |
| 1012000001 | Internal error.Possible causes: 1. IPC cross-process invoking fails. 2. System service process is faulty. |

**示例：**

```typescript
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'SecurityAuditAuthJsTest';
let authClient: securityAudit.AuthClient | undefined = undefined;
const callback = (event: securityAudit.AuditEvent) => {
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func eventId= ' + event.eventId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func content= ' + event.content);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func metadata= ' + event.metadata);
};
try {
  authClient = securityAudit.newAuthClient(callback);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'newAuthClient failed: %{public}d %{public}s', e.code, e.message);
}
try {
  authClient?.subscribe([securityAudit.AuthEvent.FILE_CREATE]);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'subscribe failed: %{public}d %{public}s', e.code, e.message);
}
```

### unsubscribe

unsubscribe(events: AuthEvent[]): void

取消订阅阻断事件。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限**：ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**系统能力**：SystemCapability.Security.SecurityAudit

**起始版本**：6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| events | [AuthEvent](devicesecurity-securityaudit-api.md#authevent)[] | 是 | 已订阅的阻断事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[安全审计错误码](errorcode-devicesecurity-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |
| 1012000001 | Internal error.Possible causes: 1. IPC cross-process invoking fails. 2. System service process is faulty. |

**示例：**

```typescript
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'SecurityAuditAuthJsTest';
let authClient: securityAudit.AuthClient | undefined = undefined;
const callback = (event: securityAudit.AuditEvent) => {
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func eventId= ' + event.eventId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func content= ' + event.content);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func metadata= ' + event.metadata);
};
try {
  authClient = securityAudit.newAuthClient(callback);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'newAuthClient failed: %{public}d %{public}s', e.code, e.message);
}
try {
  authClient?.subscribe([securityAudit.AuthEvent.FILE_CREATE]);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'subscribe failed: %{public}d %{public}s', e.code, e.message);
}
try {
  authClient?.unsubscribe([securityAudit.AuthEvent.FILE_CREATE]);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'unsubscribe failed: %{public}d %{public}s', e.code, e.message);
}
```

### addFilter

addFilter(event: AuthEvent, filter: Filter): void

为阻断事件添加过滤条件，符合过滤条件的事件将根据过滤器中的过滤标签决定是否返回给用户。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限**：ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**系统能力**：SystemCapability.Security.SecurityAudit

**起始版本**：6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [AuthEvent](devicesecurity-securityaudit-api.md#authevent) | 是 | 阻断事件ID。 |
| filter | [Filter](devicesecurity-securityaudit-api.md#filter) | 是 | 阻断事件的过滤器。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[安全审计错误码](errorcode-devicesecurity-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |
| 1012000001 | Internal error.Possible causes: 1. IPC cross-process invoking fails. 2. System service process is faulty. |
| 1012000004 | The number of filters exceeds the upper limit. |
| 1012000005 | The event does not support the filter condition. |

**示例：**

```typescript
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'SecurityAuditAuthJsTest';
let authClient: securityAudit.AuthClient | undefined = undefined;
const callback = (event: securityAudit.AuditEvent) => {
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func eventId= ' + event.eventId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func content= ' + event.content);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func metadata= ' + event.metadata);
};
try {
  authClient = securityAudit.newAuthClient(callback);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'newAuthClient failed: %{public}d %{public}s', e.code, e.message);
}
let filter : securityAudit.Filter = {
  type: securityAudit.FilterType.PROCESS_PID_EQUAL,
  isInclude: true,
  values : ["2"]
};
try {
  authClient?.addFilter(securityAudit.AuthEvent.FILE_CREATE, filter);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'addFilter failed: %{public}d %{public}s', e.code, e.message);
}
```

### removeFilter

removeFilter(event: AuthEvent, filter: Filter): void

删除阻断事件的过滤条件，满足该过滤条件的事件将不会再根据过滤器中的过滤标签进行处理。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限**：ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**系统能力**：SystemCapability.Security.SecurityAudit

**起始版本**：6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [AuthEvent](devicesecurity-securityaudit-api.md#authevent) | 是 | 阻断事件ID 。 |
| filter | [Filter](devicesecurity-securityaudit-api.md#filter) | 是 | 阻断事件的过滤器。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[安全审计错误码](errorcode-devicesecurity-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |
| 1012000001 | Internal error.Possible causes: 1. IPC cross-process invoking fails. 2. System service process is faulty. |
| 1012000005 | The event does not support the filter condition. |

**示例：**

```typescript
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'SecurityAuditAuthJsTest';
let authClient: securityAudit.AuthClient | undefined = undefined;
const callback = (event: securityAudit.AuditEvent) => {
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func eventId= ' + event.eventId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func content= ' + event.content);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func metadata= ' + event.metadata);
};
try {
  authClient = securityAudit.newAuthClient(callback);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'newAuthClient failed: %{public}d %{public}s', e.code, e.message);
}
let filter : securityAudit.Filter = {
  type: securityAudit.FilterType.PROCESS_PID_EQUAL,
  isInclude: true,
  values : ["2"]
};
try {
  authClient?.addFilter(securityAudit.AuthEvent.FILE_CREATE, filter);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'addFilter failed: %{public}d %{public}s', e.code, e.message);
}
try {
  authClient?.removeFilter(securityAudit.AuthEvent.FILE_CREATE, filter);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'removeFilter failed: %{public}d %{public}s', e.code, e.message);
}
```

### auth

auth(auditEvent: AuditEvent, authResult: AuthResult): void

设置阻断事件的阻断结果，审计模块会根据阻断结果对事件进行放行或拒绝的处理。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限**：ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**系统能力**：SystemCapability.Security.SecurityAudit

**起始版本**：6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| auditEvent | [AuditEvent](devicesecurity-securityaudit-api.md#auditevent) | 是 | 阻断事件信息 。 |
| authResult | [AuthResult](devicesecurity-securityaudit-api.md#authresult) | 是 | 阻断结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[安全审计错误码](errorcode-devicesecurity-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |
| 1012000001 | Internal error.Possible causes: 1. IPC cross-process invoking fails. 2. System service process is faulty. |
| 1012000007 | The auth event cannot be found. |

**示例：**

```typescript
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'SecurityAuditAuthJsTest';
let authClient: securityAudit.AuthClient | undefined = undefined;
const allowEventCallback = (event: securityAudit.AuditEvent) => {
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
try {
  authClient = securityAudit.newAuthClient(allowEventCallback);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'newAuthClient failed: %{public}d %{public}s', e.code, e.message);
}
```

## newAuthClient

newAuthClient(callback: Callback<[AuditEvent](devicesecurity-securityaudit-api.md#auditevent)>): AuthClient

创建一个新的阻断客户端，该客户端提供的方法可以实现阻断类事件的订阅、过滤和阻断功能。

**模型约束：** 此接口仅可在Stage模型下使用。

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
| [AuthClient](devicesecurity-securityaudit-api.md#authclient) | 阻断类客户端实例对象，一个进程最大只允许创建2个客户端实例对象，当前设备最多只允许创建16个客户端实例对象。一个客户端实例最大只允许设置256条正过滤的过滤value和256条反过滤的过滤value。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[安全审计错误码](errorcode-devicesecurity-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |
| 1012000001 | Internal error.Possible causes: 1. IPC cross-process invoking fails. 2. System service process is faulty. |
| 1012000002 | The number of clients exceeds the global upper limit. |
| 1012000003 | The number of clients exceeds the current process upper limit. |

**示例：**

```typescript
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'SecurityAuditAuthJsTest';
let authClient: securityAudit.AuthClient | undefined = undefined;
const callback = (event: securityAudit.AuditEvent) => {
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func eventId= ' + event.eventId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func content= ' + event.content);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func metadata= ' + event.metadata);
};
try {
  authClient = securityAudit.newAuthClient(callback);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'newAuthClient failed: %{public}d %{public}s', e.code, e.message);
}
```

## deleteAuthClient

deleteAuthClient(client: AuthClient): void

删除阻断客户端，用户将无法使用该客户端提供的方法，并会清空客户端记录的订阅与过滤信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| client | [AuthClient](devicesecurity-securityaudit-api.md#authclient) | 是 | 阻断客户端信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[安全审计错误码](errorcode-devicesecurity-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |
| 1012000001 | Internal error.Possible causes: 1. IPC cross-process invoking fails. 2. System service process is faulty. |

**示例：**

```typescript
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'SecurityAuditAuthJsTest';
let authClient: securityAudit.AuthClient | undefined = undefined;
const callback = (event: securityAudit.AuditEvent) => {
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func eventId= ' + event.eventId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func content= ' + event.content);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func metadata= ' + event.metadata);
};
try {
  authClient = securityAudit.newAuthClient(callback);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'newAuthClient failed: %{public}d %{public}s', e.code, e.message);
}
try {
  securityAudit.deleteAuthClient(authClient);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'deleteAuthClient failed: %{public}d %{public}s', e.code, e.message);
}
```

## AuthClientConfiguration

阻断类事件客户端配置项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| timeoutAuthResult | [AuthResult](devicesecurity-securityaudit-api.md#authresult) | 否 | 否 | 设置授权事件响应超时时的默认授权结果。  - ALLOW：超时放行  - DENY：超时阻断 |

## newAuthClient

newAuthClient(callback: Callback<[AuditEvent](devicesecurity-securityaudit-api.md#auditevent)>, configuration: [AuthClientConfiguration](devicesecurity-securityaudit-api.md#authclientconfiguration)): AuthClient

创建一个新的阻断客户端（可配置超时默认阻断策略），该客户端提供的方法可以实现阻断类事件的订阅、过滤和阻断功能。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[AuditEvent](devicesecurity-securityaudit-api.md#auditevent)> | 是 | 用于接收审计数据的回调函数。 |
| configuration | [AuthClientConfiguration](devicesecurity-securityaudit-api.md#authclientconfiguration) | 是 | 阻断客户端配置项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AuthClient](devicesecurity-securityaudit-api.md#authclient) | 阻断类客户端实例对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[安全审计错误码](errorcode-devicesecurity-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |
| 1012000001 | Internal error.Possible causes: 1. IPC cross-process invoking fails. 2. System service process is faulty. |
| 1012000002 | The number of clients exceeds the global upper limit. |
| 1012000003 | The number of clients exceeds the current process upper limit. |

**示例：**

```typescript
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'SecurityAuditAuthJsTest';
let authClient: securityAudit.AuthClient | undefined = undefined;
const callback = (event: securityAudit.AuditEvent) => {
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func eventId= ' + event.eventId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func content= ' + event.content);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func metadata= ' + event.metadata);
};

// 配置超时后阻断
let config: securityAudit.AuthClientConfiguration = {
  timeoutAuthResult: securityAudit.AuthResult.DENY
};

try {
  authClient = securityAudit.newAuthClient(callback, config);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'newAuthClient failed: %{public}d %{public}s', e.code, e.message);
}
```

## queryAllProcesses

queryAllProcesses(): string

查询获取所有的应用进程信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.QUERY\_AUDIT\_EVENT

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 应用进程信息内容，内容为json格式字符串。例如：{"1": {}}。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[安全审计错误码](errorcode-devicesecurity-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |
| 1012000001 | Internal error.Possible causes: 1. IPC cross-process invoking fails. 2. System service process is faulty. |

**示例：**

```typescript
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'SecurityAuditJsTest';
try {
  hilog.info(0x0000, TAG, 'queryAllProcesses begin.');
  const result = securityAudit.queryAllProcesses();
  hilog.info(0x0000, TAG, 'Succeeded in queryAllProcesses.');
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'queryAllProcesses failed: %{public}d %{public}s', e.code, e.message);
}
```

## queryProcesses

queryProcesses(pids: number[]): string

查询获取输入的PID的应用进程信息。

**模型约束：** 此接口仅可在Stage模型下使用。

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

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[安全审计错误码](errorcode-devicesecurity-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |
| 1012000001 | Internal error.Possible causes: 1. IPC cross-process invoking fails. 2. System service process is faulty. |
| 1012000006 | The number of queried processes exceeds the threshold. |

**示例：**

```typescript
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'SecurityAuditJsTest';
let pids: number[] = [1, 2];
try {
  hilog.info(0x0000, TAG, 'queryProcesses begin.');
  const result = securityAudit.queryProcesses(pids);
  hilog.info(0x0000, TAG, 'Succeeded in queryProcesses.');
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'queryProcesses failed: %{public}d %{public}s', e.code, e.message);
}
```

## acquireCodeSign

acquireCodeSign(path: string): string

获取输入的文件路径的代码签名信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.QUERY\_AUDIT\_EVENT

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 6.1.1(24)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待查询的应用文件路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 代码签名内容，内容为json格式字符串。例如：{"1": {}}。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[安全审计错误码](errorcode-devicesecurity-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |
| 1012000001 | Internal error.Possible causes: 1. IPC cross-process invoking fails. 2. System service process is faulty. |
| 1012000008 | The file cannot be found. |

**示例：**

```typescript
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
 
const TAG = 'SecurityAuditJsTest';
let path = 'test';
try {
  hilog.info(0x0000, TAG, 'acquireCodeSign begin.');
  const result = securityAudit.acquireCodeSign(path);
  hilog.info(0x0000, TAG, 'Succeeded in acquireCodeSign.');
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'acquireCodeSign failed: %{public}d %{public}s', e.code, e.message);
}
```

## acquireAllClientsInfo

acquireAllClientsInfo(): string

查询获取全量审计事件通知类客户端信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.QUERY\_AUDIT\_EVENT

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 26.0.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 安全审计通知类客户端信息，内容为json格式字符串。例如： [{"procName": vps, "uid": 1000, "pid": 1000}]。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[安全审计错误码](errorcode-devicesecurity-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |
| 1012000001 | Internal error.Possible causes: 1. IPC cross-process invoking fails. 2. System service process is faulty. |

**示例：**

```typescript
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'SecurityAuditJsTest';
try {
  hilog.info(0x0000, TAG, 'acquireAllClientsInfo begin.');
  const result = securityAudit.acquireAllClientsInfo();
  hilog.info(0x0000, TAG, 'Succeeded in acquireAllClientsInfo.');
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'acquireAllClientsInfo failed: %{public}d %{public}s', e.code, e.message);
}
```

## acquireAllAuthClientsInfo

acquireAllAuthClientsInfo(): string

查询获取全量审计事件阻断类客户端信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 26.0.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 安全审计阻断类客户端信息，内容为json格式字符串。例如： [{"procName": vps, "uid": 1000, "pid": 1000}]。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[安全审计错误码](errorcode-devicesecurity-securityaudit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission fail. |
| 1012000001 | Internal error.Possible causes: 1. IPC cross-process invoking fails. 2. System service process is faulty. |

**示例：**

```typescript
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
 
const TAG = 'SecurityAuditJsTest';
try {
  hilog.info(0x0000, TAG, 'acquireAllAuthClientsInfo begin.');
  const result = securityAudit.acquireAllAuthClientsInfo();
  hilog.info(0x0000, TAG, 'Succeeded in acquireAllAuthClientsInfo.');
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'acquireAllAuthClientsInfo failed: %{public}d %{public}s', e.code, e.message);
}
```
