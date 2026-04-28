---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-antifraudpicker-api
title: AntifraudPicker（反诈选择器）
breadcrumb: API参考 > 系统 > 安全 > Device Security Kit（设备安全服务） > ArkTS API > AntifraudPicker（反诈选择器）
category: harmonyos-references
scraped_at: 2026-04-28T08:07:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:75bccd864cfb805bfca8452a7d11cd5a38b8bf73ad5f26cccc0a7ca4fa8d17b0
---

本模块提供获取诈骗消息、诈骗通话记录的接口，应用可以获取选择的消息或通话记录数据，以支撑反诈业务。

**起始版本：** 5.0.3(15)

## 导入模块

PhoneTablet

```
1. import {antifraudPicker} from '@kit.DeviceSecurityKit';
```

## AntifraudMessageOptions

PhoneTablet

获取诈骗消息的请求参数。

**系统能力：** SystemCapability.Security.Antifraud

**起始版本：** 5.0.3(15)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| maxSelectNumber | number | 否 | 是 | 最大可选项数。如果不传，则默认为50。取值范围为1~50。 |

## SingleAntifraudMessageInfo

PhoneTablet

单条诈骗消息信息。

**系统能力：** SystemCapability.Security.Antifraud

**起始版本：** 5.0.3(15)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| senderNumber | string | 否 | 否 | 消息发送方号码。 |
| receivingTime | number | 否 | 否 | 消息接收时间戳，单位：毫秒。 |
| messageContent | string | 否 | 否 | 消息内容，最长17152个字符。 |
| senderName | string | 否 | 否 | 发送方名称。 |
| senderPlace | string | 否 | 否 | 消息发送方号码归属地。 |
| messageType | string | 否 | 否 | 消息类型。'0' ：短信，'1'：彩信。 |
| mmsSubject | string | 否 | 是 | 彩信主题。该字段仅当消息类型为彩信时生效。 |
| mmsAttachments | [MmsAttachmentInfo](devicesecurity-antifraudpicker-api.md#mmsattachmentinfo)[] | 否 | 是 | 彩信附件信息列表。该字段仅当消息类型为彩信时生效。 |

## MmsAttachmentInfo

PhoneTablet

彩信附件信息。

**系统能力：** SystemCapability.Security.Antifraud

**起始版本：** 5.0.3(15)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| attachmentType | number | 否 | 否 | 彩信附件类型。  -1：彩信未下载；  0：smil文件；  1：图片；  2：视频；  3：音频；  4：联系人卡片；  5：主题；  6：幻灯片；  7：文本；  8：位置。 |
| uri | string | 否 | 否 | 附件URI。 |

## AntifraudMessageResult

PhoneTablet

诈骗消息结果。

**系统能力：** SystemCapability.Security.Antifraud

**起始版本：** 5.0.3(15)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| messageInfo | [SingleAntifraudMessageInfo](devicesecurity-antifraudpicker-api.md#singleantifraudmessageinfo)[] | 否 | 否 | 诈骗消息结果列表。 |

## SingleAntifraudCallLogInfo

PhoneTablet

单条诈骗通话记录信息。

**系统能力：** SystemCapability.Security.Antifraud

**起始版本：** 5.0.3(15)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| callerNumber | string | 否 | 否 | 来电方号码。 |
| receivingTime | number | 否 | 否 | 接听通话的时间戳，单位：毫秒。 |
| callLogType | number | 否 | 否 | 通话记录类型。0：来电，1：拨出。 |
| callerName | string | 否 | 否 | 来电方名称。 |
| callDuration | number | 否 | 否 | 通话时长，单位：毫秒。 |

## AntifraudCallLogResult

PhoneTablet

诈骗通话记录结果。

**系统能力：** SystemCapability.Security.Antifraud

**起始版本：** 5.0.3(15)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| callLogInfo | [SingleAntifraudCallLogInfo](devicesecurity-antifraudpicker-api.md#singleantifraudcallloginfo)[] | 否 | 否 | 诈骗通话记录列表。 |

## AntifraudCallLogOptions

PhoneTablet

获取诈骗通话记录的请求参数。

**系统能力：** SystemCapability.Security.Antifraud

**起始版本：** 5.0.3(15)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| maxSelectNumber | number | 否 | 是 | 最大可选项数。如果不传，则默认为50。取值范围为1~50。 |

## selectFraudMessage

PhoneTablet

selectFraudMessage(context: common.Context, options?: [AntifraudMessageOptions](devicesecurity-antifraudpicker-api.md#antifraudmessageoptions)): Promise<[AntifraudMessageResult](devicesecurity-antifraudpicker-api.md#antifraudmessageresult)>

拉起诈骗消息选择器，并获取用户选择的诈骗消息信息。使用Promise异步回调。

**需要权限：** ohos.permission.USE\_FRAUD\_MESSAGES\_PICKER

**系统能力：** SystemCapability.Security.Antifraud

**起始版本：** 5.0.3(15)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md) | 是 | 应用上下文。 |
| options | [AntifraudMessageOptions](devicesecurity-antifraudpicker-api.md#antifraudmessageoptions) | 否 | 请求参数。如果不传，则最大可选项数默认为50。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AntifraudMessageResult](devicesecurity-antifraudpicker-api.md#antifraudmessageresult)> | Promise对象，返回诈骗消息结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-antifraudpicker.md) **。**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. Interface caller does not have permission "ohos.permission.USE\_FRAUD\_MESSAGES\_PICKER". |
| 401 | Input parameter error.  Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 1017100001 | Unknown error. |
| 1017100002 | The device type is not supported. |

**示例：**

```
1. import { antifraudPicker} from '@kit.DeviceSecurityKit';
2. import { BusinessError} from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { common} from '@kit.AbilityKit';

6. const TAG = "AntifraudPickerJsTest";

8. // 请求获取诈骗消息信息，并进行业务处理
9. let options: antifraudPicker.AntifraudMessageOptions = {
10. maxSelectNumber: 5
11. };
12. try {
13. hilog.info(0x0000, TAG, 'SelectFraudMessage begin.');
14. let context = this.getUIContext().getHostContext();
15. const result: antifraudPicker.AntifraudMessageResult = await antifraudPicker.selectFraudMessage(context, options);
16. } catch (err) {
17. let e: BusinessError = err as BusinessError;
18. hilog.error(0x0000, TAG, 'SelectFraudMessage failed: %{public}d %{public}s', e.code, e.message);
19. }
```

## selectFraudCallLog

PhoneTablet

selectFraudCallLog(context: common.Context, options?: [AntifraudCallLogOptions](devicesecurity-antifraudpicker-api.md#antifraudcalllogoptions)): Promise<[AntifraudCallLogResult](devicesecurity-antifraudpicker-api.md#antifraudcalllogresult)>

拉起诈骗通话记录选择器，并获取用户选择的诈骗通话记录信息。使用Promise异步回调。

**需要权限：** ohos.permission.USE\_FRAUD\_CALL\_LOG\_PICKER

**系统能力：** SystemCapability.Security.Antifraud

**起始版本：** 5.0.3(15)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md) | 是 | 应用上下文。 |
| options | [AntifraudCallLogOptions](devicesecurity-antifraudpicker-api.md#antifraudcalllogoptions) | 否 | 请求参数。如果不传，则最大可选项数默认为50。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AntifraudCallLogResult](devicesecurity-antifraudpicker-api.md#antifraudcalllogresult)> | Promise对象，返回诈骗通话记录结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-antifraudpicker.md) **。**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. Interface caller does not have permission "ohos.permission.USE\_FRAUD\_CALL\_LOG\_PICKER". |
| 401 | Input parameter error.  Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 1017100001 | Unknown error. |
| 1017100002 | The device type is not supported. |

**示例：**

```
1. import { antifraudPicker} from '@kit.DeviceSecurityKit';
2. import { BusinessError} from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { common} from '@kit.AbilityKit';

6. const TAG = "AntifraudPickerJsTest";

8. // 请求获取诈骗通话记录信息，并进行业务处理
9. let options: antifraudPicker.AntifraudCallLogOptions = {
10. maxSelectNumber: 5
11. };
12. try {
13. hilog.info(0x0000, TAG, 'SelectFraudCallLog begin.');
14. let context = this.getUIContext().getHostContext();
15. const result: antifraudPicker.AntifraudCallLogResult = await antifraudPicker.selectFraudCallLog(context, options);
16. } catch (err) {
17. let e: BusinessError = err as BusinessError;
18. hilog.error(0x0000, TAG, 'SelectFraudCallLog failed: %{public}d %{public}s', e.code, e.message);
19. }
```

## AntifraudAppOptions

PhoneTablet

获取诈骗应用的请求参数。

**系统能力：** SystemCapability.Security.Antifraud

**起始版本：** 5.1.1(19)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| maxSelectNumber | number | 否 | 是 | 最大可选项数。如果不传，则默认为50。取值范围为1~50。 |

## AntifraudAppResult

PhoneTablet

诈骗应用结果。

**系统能力：** SystemCapability.Security.Antifraud

**起始版本：** 5.1.1(19)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| appInfo | [SingleAntifraudAppInfo](devicesecurity-antifraudpicker-api.md#singleantifraudappinfo)[] | 否 | 否 | 诈骗应用列表。 |

## SingleAntifraudAppInfo

PhoneTablet

单条诈骗应用信息。

**系统能力：** SystemCapability.Security.Antifraud

**起始版本：** 5.1.1(19)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| applicationName | string | 否 | 否 | 应用程序的名称。 |
| bundleName | string | 否 | 否 | APP包名。 |
| versionCode | number | 否 | 否 | 应用版本编码。 |
| versionName | string | 否 | 否 | 应用版本名称。 |
| installTime | number | 否 | 否 | 应用安装时间戳，单位：毫秒。 |
| appId | string | 否 | 否 | 应用ID。 |
| label | string | 否 | 否 | 应用名称，为用户视角的应用名称，如”时钟”。 |
| installSource | string | 否 | 否 | 应用程序的安装来源，支持的取值如下：  - pre-installed表示应用为第一次开机时安装的预置应用。  - ota表示应用为系统升级时新增的预置应用。  - recovery表示卸载后再恢复的预置应用。  - 安装来源的格式为包名表示应用由此包名对应的应用安装。  - unknown表示应用安装来源未知 |

## selectFraudApp

PhoneTablet

selectFraudApp(context: common.Context, options?: [AntifraudAppOptions](devicesecurity-antifraudpicker-api.md#antifraudappoptions)): Promise<[AntifraudAppResult](devicesecurity-antifraudpicker-api.md#antifraudappresult)>

拉起诈骗应用选择器，并获取用户选择的诈骗应用信息。使用Promise异步回调。

**需要权限：** ohos.permission.USE\_FRAUD\_APP\_PICKER

**系统能力：** SystemCapability.Security.Antifraud

**起始版本：** 5.1.1(19)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md) | 是 | 应用上下文。 |
| options | [AntifraudAppOptions](devicesecurity-antifraudpicker-api.md#antifraudappoptions) | 否 | 请求参数。如果不传，则最大可选项数默认为50。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AntifraudAppResult](devicesecurity-antifraudpicker-api.md#antifraudappresult)> | Promise对象，返回诈骗应用结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-antifraudpicker.md) **。**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. Interface caller does not have permission "ohos.permission.USE\_FRAUD\_APP\_PICKER". |
| 1017600001 | Unknown error. |
| 1017600002 | The device type is not supported. |
| 1017600003 | Parameter verification failed. |

**示例：**

```
1. import { antifraudPicker} from '@kit.DeviceSecurityKit';
2. import { BusinessError} from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { common} from '@kit.AbilityKit';

6. const TAG = "AntifraudPickerJsTest";

8. // 请求获取诈骗应用信息，并进行业务处理
9. let options: antifraudPicker.AntifraudAppOptions = {
10. maxSelectNumber: 5
11. };
12. try {
13. hilog.info(0x0000, TAG, 'SelectFraudApp begin.');
14. let context = this.getUIContext().getHostContext();
15. const result: antifraudPicker.AntifraudAppResult = await antifraudPicker.selectFraudApp(context, options);
16. } catch (err) {
17. let e: BusinessError = err as BusinessError;
18. hilog.error(0x0000, TAG, 'SelectFraudApp failed: %{public}d %{public}s', e.code, e.message);
19. }
```
