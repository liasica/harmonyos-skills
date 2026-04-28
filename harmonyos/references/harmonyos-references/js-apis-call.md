---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-call
title: @ohos.telephony.call (拨打电话)
breadcrumb: API参考 > 系统 > 网络 > Telephony Kit（蜂窝通信服务） > ArkTS API > @ohos.telephony.call (拨打电话)
category: harmonyos-references
scraped_at: 2026-04-28T08:09:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:683f2c7be4a1c74a9937950ed35ea599b31c52a90820ebb5a0931a8b7f491d3a
---

该模块提供呼叫管理功能，包括拨打电话、跳转到拨号界面、获取通话状态、格式化电话号码等。

如需订阅通话状态请使用[observer.on('callStateChange')](js-apis-observer.md#observeroncallstatechange)。

说明

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { call } from '@kit.TelephonyKit';
```

## call.dial(deprecated)

PhoneTabletWearable

dial(phoneNumber: string, callback: AsyncCallback<boolean>): void

拨打电话。使用callback异步回调。

说明

从API version 6 开始支持，从API version 9 开始废弃。替代接口能力仅对系统应用开放。

**需要权限**：ohos.permission.PLACE\_CALL（该权限仅系统应用可申请）

**系统能力**：SystemCapability.Telephony.CallManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| phoneNumber | string | 是 | 电话号码。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数，返回true为成功，false为失败。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. call.dial("138xxxxxxxx", (err: BusinessError, data: boolean) => {
4. console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
5. });
```

## call.dial(deprecated)

PhoneTabletWearable

dial(phoneNumber: string, options: DialOptions, callback: AsyncCallback<boolean>): void

拨打电话，可设置通话参数。使用callback异步回调。

说明

从API version 6 开始支持，从API version 9 开始废弃。替代接口能力仅对系统应用开放。

**需要权限**：ohos.permission.PLACE\_CALL（该权限仅系统应用可申请）

**系统能力**：SystemCapability.Telephony.CallManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| phoneNumber | string | 是 | 电话号码。 |
| options | [DialOptions](js-apis-call.md#dialoptions) | 是 | 通话参数，选择为语音通话还是视频通话。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数，返回true为成功，false为失败。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let dialOptions: call.DialOptions = {
4. extras: false
5. }
6. call.dial("138xxxxxxxx", dialOptions, (err: BusinessError, data: boolean) => {
7. console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
8. });
```

## call.dial(deprecated)

PhoneTabletWearable

dial(phoneNumber: string, options?: DialOptions): Promise<boolean>

拨打电话，可设置通话参数。使用Promise异步回调。

说明

从API version 6 开始支持，从API version 9 开始废弃。替代接口能力仅对系统应用开放。

**需要权限**：ohos.permission.PLACE\_CALL（该权限仅系统应用可申请）

**系统能力**：SystemCapability.Telephony.CallManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| phoneNumber | string | 是 | 电话号码。 |
| options | [DialOptions](js-apis-call.md#dialoptions) | 否 | 通话参数，选择为语音通话还是视频通话。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | 以Promise形式返回拨打电话的结果，返回true为成功，false为失败。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let dialOptions: call.DialOptions = {
4. extras: false
5. }
6. call.dial("138xxxxxxxx", dialOptions).then((data: boolean) => {
7. console.info(`dial success, promise: data->${JSON.stringify(data)}`);
8. }).catch((err: BusinessError) => {
9. console.error(`dial fail, promise: err->${JSON.stringify(err)}`);
10. });
```

## call.makeCall7+

PhonePC/2in1TabletWearable

makeCall(phoneNumber: string, callback: AsyncCallback<void>): void

跳转到拨号界面，并显示待拨出的号码。使用callback异步回调。只支持在UIAbility中调用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.Contacts

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| phoneNumber | string | 是 | 电话号码。 |
| callback | AsyncCallback<void> | 是 | 以callback形式异步返回跳转拨号界面的结果。 |

**错误码：**

以下错误码的详细介绍请参见[电话子系统错误码](errorcode-telephony.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Unknown error code. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // 从API15开始支持tel格式电话号码，如："tel:13xxxx"
3. call.makeCall("138xxxxxxxx", (err: BusinessError) => {
4. if (err) {
5. console.error(`makeCall fail, err->${JSON.stringify(err)}`);
6. } else {
7. console.info(`makeCall success`);
8. }
9. });
```

## call.makeCall7+

PhonePC/2in1TabletWearable

makeCall(phoneNumber: string): Promise<void>

跳转到拨号界面，并显示待拨出的号码。使用Promise异步回调。只支持在UIAbility中调用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.Contacts

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| phoneNumber | string | 是 | 电话号码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 以Promise形式异步返回拨号的结果。 |

**错误码：**

以下错误码的详细介绍请参见[电话子系统错误码](errorcode-telephony.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Unknown error code. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // 从API15开始支持tel格式电话号码，如："tel:13xxxx"
3. call.makeCall("138xxxxxxxx").then(() => {
4. console.info(`makeCall success`);
5. }).catch((err: BusinessError) => {
6. console.error(`makeCall fail, promise: err->${JSON.stringify(err)}`);
7. });
```

## call.makeCall12+

PhonePC/2in1TabletWearable

makeCall(context: Context, phoneNumber: string): Promise<void>

跳转到拨号界面，并显示待拨出的号码。使用Promise异步回调。后台调用需要申请ohos.permission.START\_ABILITIES\_FROM\_BACKGROUND权限。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.Contacts

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context。 |
| phoneNumber | string | 是 | 电话号码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 以Promise形式异步返回拨号的结果。 |

**错误码：**

以下错误码的详细介绍请参见[电话子系统错误码](errorcode-telephony.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // 获取context
3. let context = this.getUIContext().getHostContext() as Context;
4. // 从API15开始支持tel格式电话号码，如："tel:13xxxx"
5. call.makeCall(context, "138xxxxxxxx").then(() => {
6. console.info(`makeCall success`);
7. }).catch((err: BusinessError) => {
8. console.error(`makeCall fail, promise: err->${JSON.stringify(err)}`);
9. });
```

## call.hasCall

PhoneTabletWearable

hasCall(callback: AsyncCallback<boolean>): void

判断是否存在通话。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CallManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示当前存在通话，false表示当前不存在通话。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. call.hasCall((err: BusinessError, data: boolean) => {
4. if (err) {
5. console.error(`hasCall fail, err->${JSON.stringify(err)}`);
6. } else {
7. console.info(`hasCall success, data->${JSON.stringify(data)}`);
8. }
9. });
```

## call.hasCall

PhoneTabletWearable

hasCall(): Promise<boolean>

判断是否存在通话。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CallManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | 以Promise形式异步返回判断是否存在通话。返回true表示当前存在通话，false表示当前不存在通话。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. call.hasCall().then(() => {
4. console.info(`hasCall success`);
5. }).catch((err: BusinessError) => {
6. console.error(`hasCall fail, promise: err->${JSON.stringify(err)}`);
7. });
```

## call.hasCallSync10+

PhoneTabletWearable

hasCallSync(): boolean

判断是否存在通话。

**系统能力**：SystemCapability.Telephony.CallManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回判断是否存在通话。返回true表示当前存在通话，false表示当前不存在通话。 |

**示例：**

```
1. let hasCall: boolean = call.hasCallSync();
2. console.info(`hasCallSync success, has call is ` + hasCall);
```

## call.getCallState

PhoneTabletWearable

getCallState(callback: AsyncCallback<CallState>): void

获取当前通话状态。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CallManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[CallState](js-apis-call.md#callstate)> | 是 | 回调函数，异步返回获取到的通话状态。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. call.getCallState((err: BusinessError, data: call.CallState) => {
4. if (err) {
5. console.error(`getCallState fail, err->${JSON.stringify(err)}`);
6. } else {
7. console.info(`getCallState success, data->${JSON.stringify(data)}`);
8. }
9. });
```

## call.getCallState

PhoneTabletWearable

getCallState(): Promise<CallState>

获取当前通话状态。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CallManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[CallState](js-apis-call.md#callstate)> | 以Promise形式异步返回获取到的通话状态。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. call.getCallState().then((data: call.CallState) => {
4. console.info(`getCallState success, promise: data->${JSON.stringify(data)}`);
5. }).catch((err: BusinessError) => {
6. console.error(`getCallState fail, promise: err->${JSON.stringify(err)}`);
7. });
```

## call.getCallStateSync10+

PhoneTabletWearable

getCallStateSync(): CallState

获取当前通话状态。

**系统能力**：SystemCapability.Telephony.CallManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CallState](js-apis-call.md#callstate) | 返回获取到的通话状态。 |

**示例：**

```
1. let callState: call.CallState = call.getCallStateSync();
2. console.info(`the call state is:` + callState);
```

## call.hasVoiceCapability7+

PhoneTabletWearable

hasVoiceCapability(): boolean

检查当前设备是否具备语音通话能力。

**系统能力**：SystemCapability.Telephony.CallManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示设备具备语音通话能力，返回false表示设备不具备语音通话能力。 |

```
1. let result: boolean = call.hasVoiceCapability();
2. console.info(`hasVoiceCapability: ${JSON.stringify(result)}`);
```

## call.isEmergencyPhoneNumber7+

PhoneTabletWearable

isEmergencyPhoneNumber(phoneNumber: string, callback: AsyncCallback<boolean>): void

判断是否是紧急电话号码。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CallManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| phoneNumber | string | 是 | 电话号码。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示是紧急电话号码，返回false表示不是紧急电话号码。 |

**错误码：**

以下错误码的详细介绍请参见[电话子系统错误码](errorcode-telephony.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Unknown error code. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. call.isEmergencyPhoneNumber("138xxxxxxxx", (err: BusinessError, data: boolean) => {
4. if (err) {
5. console.error(`isEmergencyPhoneNumber fail, err->${JSON.stringify(err)}`);
6. } else {
7. console.info(`isEmergencyPhoneNumber success, data->${JSON.stringify(data)}`);
8. }
9. });
```

## call.isEmergencyPhoneNumber7+

PhoneTabletWearable

isEmergencyPhoneNumber(phoneNumber: string, options: EmergencyNumberOptions, callback: AsyncCallback<boolean>): void

根据电话号码参数，判断是否是紧急电话号码。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CallManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| phoneNumber | string | 是 | 电话号码。 |
| options | [EmergencyNumberOptions](js-apis-call.md#emergencynumberoptions7) | 是 | 电话号码参数。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示是紧急电话号码，返回false表示不是紧急电话号码。 |

**错误码：**

以下错误码的详细介绍请参见[电话子系统错误码](errorcode-telephony.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Unknown error code. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let options: call.EmergencyNumberOptions = {slotId: 1}
4. call.isEmergencyPhoneNumber("112", options, (err: BusinessError, data: boolean) => {
5. if (err) {
6. console.error(`isEmergencyPhoneNumber fail, err->${JSON.stringify(err)}`);
7. } else {
8. console.info(`isEmergencyPhoneNumber success, data->${JSON.stringify(data)}`);
9. }
10. });
```

## call.isEmergencyPhoneNumber7+

PhoneTabletWearable

isEmergencyPhoneNumber(phoneNumber: string, options?: EmergencyNumberOptions): Promise<boolean>

根据电话号码参数，判断是否是紧急电话号码。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CallManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| phoneNumber | string | 是 | 电话号码。 |
| options | [EmergencyNumberOptions](js-apis-call.md#emergencynumberoptions7) | 否 | 电话号码参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | 以Promise形式异步返回判断是否是紧急电话号码的结果。返回true表示是紧急电话号码，返回false表示不是紧急电话号码。 |

**错误码：**

以下错误码的详细介绍请参见[电话子系统错误码](errorcode-telephony.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Unknown error code. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let options: call.EmergencyNumberOptions = {slotId: 1}
4. call.isEmergencyPhoneNumber("138xxxxxxxx", options).then((data: boolean) => {
5. console.info(`isEmergencyPhoneNumber success, promise: data->${JSON.stringify(data)}`);
6. }).catch((err: BusinessError) => {
7. console.error(`isEmergencyPhoneNumber fail, promise: err->${JSON.stringify(err)}`);
8. });
```

## call.formatPhoneNumber7+

PhoneTabletWearable

formatPhoneNumber(phoneNumber: string, callback: AsyncCallback<string>): void

格式化电话号码。使用callback异步回调。

电话号码格式化后为标准数字字符串，例如：“138 xxxx xxxx”、“0755 xxxx xxxx”。

**系统能力**：SystemCapability.Telephony.CallManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| phoneNumber | string | 是 | 电话号码。 |
| callback | AsyncCallback<string> | 是 | 回调函数，返回格式化电话号码的结果。 |

**错误码：**

以下错误码的详细介绍请参见[电话子系统错误码](errorcode-telephony.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Unknown error code. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. call.formatPhoneNumber("138xxxxxxxx", (err: BusinessError, data: string) => {
4. if (err) {
5. console.error(`formatPhoneNumber fail, err->${JSON.stringify(err)}`);
6. } else {
7. console.info(`formatPhoneNumber success, data->${JSON.stringify(data)}`);
8. }
9. });
```

## call.formatPhoneNumber7+

PhoneTabletWearable

formatPhoneNumber(phoneNumber: string, options: NumberFormatOptions, callback: AsyncCallback<string>): void

格式化电话号码，可设置格式化参数。使用callback异步回调。

电话号码格式化后为标准数字字符串，例如：“138 xxxx xxxx”、“0755 xxxx xxxx”。

**系统能力**：SystemCapability.Telephony.CallManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| phoneNumber | string | 是 | 电话号码。 |
| options | [NumberFormatOptions](js-apis-call.md#numberformatoptions7) | 是 | 格式化参数，如国家码。 |
| callback | AsyncCallback<string> | 是 | 回调函数，返回格式化电话号码的结果。 |

**错误码：**

以下错误码的详细介绍请参见[电话子系统错误码](errorcode-telephony.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Unknown error code. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let options: call.NumberFormatOptions = {
4. countryCode: "CN"
5. }
6. call.formatPhoneNumber("138xxxxxxxx", options, (err: BusinessError, data: string) => {
7. if (err) {
8. console.error(`formatPhoneNumber fail, err->${JSON.stringify(err)}`);
9. } else {
10. console.info(`formatPhoneNumber success, data->${JSON.stringify(data)}`);
11. }
12. });
```

## call.formatPhoneNumber7+

PhoneTabletWearable

formatPhoneNumber(phoneNumber: string, options?: NumberFormatOptions): Promise<string>

格式化电话号码，可设置格式化参数。使用Promise异步回调。

电话号码格式化后为标准数字字符串，例如：“138 xxxx xxxx”、“0755 xxxx xxxx”。

**系统能力**：SystemCapability.Telephony.CallManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| phoneNumber | string | 是 | 电话号码。 |
| options | [NumberFormatOptions](js-apis-call.md#numberformatoptions7) | 否 | 格式化参数，如国家码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | 以Promise形式异步返回格式化电话号码的结果。 |

**错误码：**

以下错误码的详细介绍请参见[电话子系统错误码](errorcode-telephony.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Unknown error code. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let options: call.NumberFormatOptions = {
4. countryCode: "CN"
5. }
6. call.formatPhoneNumber("138xxxxxxxx", options).then((data: string) => {
7. console.info(`formatPhoneNumber success, promise: data->${JSON.stringify(data)}`);
8. }).catch((err: BusinessError) => {
9. console.error(`formatPhoneNumber fail, promise: err->${JSON.stringify(err)}`);
10. });
```

## call.formatPhoneNumberToE1647+

PhoneTabletWearable

formatPhoneNumberToE164(phoneNumber: string, countryCode: string, callback: AsyncCallback<string>): void

将电话号码格式化为E.164表示形式，使用callback异步回调。

待格式化的电话号码需要与传入的国家码相匹配，如中国电话号码需要传入国家码CN，否则格式化后的电话号码为null。

**系统能力**：SystemCapability.Telephony.CallManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| phoneNumber | string | 是 | 电话号码。 |
| countryCode | string | 是 | 国家码，支持所有国家码，如：中国（CN）。 |
| callback | AsyncCallback<string> | 是 | 回调函数，返回将电话号码格式化为E.164表示形式的结果。 |

**错误码：**

以下错误码的详细介绍请参见[电话子系统错误码](errorcode-telephony.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Unknown error code. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. call.formatPhoneNumberToE164("138xxxxxxxx", "CN", (err: BusinessError, data: string) => {
4. if (err) {
5. console.error(`formatPhoneNumberToE164 fail, err->${JSON.stringify(err)}`);
6. } else {
7. console.info(`formatPhoneNumberToE164 success, data->${JSON.stringify(data)}`);
8. }
9. });
```

## call.formatPhoneNumberToE1647+

PhoneTabletWearable

formatPhoneNumberToE164(phoneNumber: string, countryCode: string): Promise<string>

将电话号码格式化为E.164表示形式，使用Promise异步回调。

待格式化的电话号码需要与传入的国家码相匹配，如中国电话号码需要传入国家码CN，否则格式化后的电话号码为null。

支持所有国家码。

**系统能力**：SystemCapability.Telephony.CallManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| phoneNumber | string | 是 | 电话号码。 |
| countryCode | string | 是 | 国家码，支持所有国家码，如：中国（CN）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | 以Promise形式异步返回将电话号码格式化为E.164表示形式的结果。 |

**错误码：**

以下错误码的详细介绍请参见[电话子系统错误码](errorcode-telephony.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Unknown error code. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. call.formatPhoneNumberToE164("138xxxxxxxx", "CN").then((data: string) => {
4. console.info(`formatPhoneNumberToE164 success, promise: data->${JSON.stringify(data)}`);
5. }).catch((err: BusinessError) => {
6. console.error(`formatPhoneNumberToE164 fail, promise: err->${JSON.stringify(err)}`);
7. });
```

## call.answerCall23+

PhoneTabletWearable

answerCall(callback: AsyncCallback<void>): void

接听来电。使用callback异步回调。

**需要权限**：ohos.permission.ANSWER\_CALL 或 ohos.permission.MANAGE\_CALL\_FOR\_DEVICES

* ohos.permission.ANSWER\_CALL权限仅系统应用可申请。

**系统能力**：SystemCapability.Telephony.CallManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。返回接听电话成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[电话子系统错误码](errorcode-telephony.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Unknown error code. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. call.answerCall((err: BusinessError) => {
4. if (err) {
5. console.error(`answerCall fail, err->${JSON.stringify(err)}`);
6. } else {
7. console.info(`answerCall success.`);
8. }
9. });
```

## call.hangUpCall23+

PhoneTabletWearable

hangUpCall(callback: AsyncCallback<void>): void

挂断电话。使用callback异步回调。

**需要权限**：ohos.permission.ANSWER\_CALL 或 ohos.permission.SET\_TELEPHONY\_STATE 或 ohos.permission.MANAGE\_CALL\_FOR\_DEVICES

* ohos.permission.ANSWER\_CALL、ohos.permission.SET\_TELEPHONY\_STATE权限仅系统应用可申请。

**系统能力**：SystemCapability.Telephony.CallManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当挂断电话成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[电话子系统错误码](errorcode-telephony.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Unknown error code. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. call.hangUpCall((err: BusinessError) => {
4. if (err) {
5. console.error(`hangUpCall fail, err->${JSON.stringify(err)}`);
6. } else {
7. console.info(`hangUpCall success.`);
8. }
9. });
```

## call.rejectCall23+

PhoneTabletWearable

rejectCall(callback: AsyncCallback<void>): void

拒绝来电。使用callback异步回调。

**需要权限**：ohos.permission.ANSWER\_CALL 或 ohos.permission.MANAGE\_CALL\_FOR\_DEVICES

* ohos.permission.ANSWER\_CALL权限仅系统应用可申请。

**系统能力**：SystemCapability.Telephony.CallManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当拒接来电成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[电话子系统错误码](errorcode-telephony.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Unknown error code. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. call.rejectCall((err: BusinessError) => {
4. if (err) {
5. console.error(`rejectCall fail, err->${JSON.stringify(err)}`);
6. } else {
7. console.info(`rejectCall success.`);
8. }
9. });
```

## DialOptions

PhoneTabletWearable

拨打电话的可选参数。

**系统能力**：SystemCapability.Telephony.CallManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| extras | boolean | 否 | 是 | 根据extras的值判断是否为视频通话，默认为语音通话。  - true：视频通话。  - false：语音通话。 |

## CallState

PhoneTabletWearable

通话状态码。

**系统能力**：SystemCapability.Telephony.CallManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CALL\_STATE\_UNKNOWN | -1 | 无效状态，当获取呼叫状态失败时返回。 |
| CALL\_STATE\_IDLE | 0 | 表示没有正在进行的呼叫。 |
| CALL\_STATE\_RINGING | 1 | 表示来电正在振铃或等待。 |
| CALL\_STATE\_OFFHOOK | 2 | 表示至少有一个呼叫处于拨号、通话中或呼叫保持状态，并且没有新的来电振铃或等待。 |
| CALL\_STATE\_ANSWERED11+ | 3 | 表示来电已经接听。 |

## TelCallState21+

PhoneTabletWearable

通话状态码。

**系统能力**：SystemCapability.Telephony.CallManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TEL\_CALL\_STATE\_UNKNOWN | -1 | 无效状态，当获取呼叫状态失败时返回。 |
| TEL\_CALL\_STATE\_IDLE | 0 | 表示没有正在进行的呼叫。 |
| TEL\_CALL\_STATE\_RINGING | 1 | 表示来电正在振铃或等待。 |
| TEL\_CALL\_STATE\_OFFHOOK | 2 | 表示至少有一个呼叫处于拨号，并且没有新的来电振铃或等待。 |
| TEL\_CALL\_STATE\_ANSWERED | 3 | 表示来电已经接听。 |
| TEL\_CALL\_STATE\_CONNECTED | 4 | 表示电话已经接通中或呼叫保持。 |

## CCallState23+

PhoneTabletWearable

运营商通话状态码。

**系统能力**：SystemCapability.Telephony.CallManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CCALL\_STATE\_UNKNOWN | -1 | 无效状态，当获取呼叫状态失败时返回。 |
| CCALL\_STATE\_ACTIVE | 0 | 表示当前通话已经接通成功。 |
| CCALL\_STATE\_HOLDING | 1 | 表示当前通话处于保持状态。 |
| CCALL\_STATE\_DIALING | 2 | 表示去电处于拨号过程中，对端还没有收到振铃期间。 |
| CCALL\_STATE\_ALERTING | 3 | 表示去电处于振铃过程中，对端处于响铃阶段。 |
| CCALL\_STATE\_INCOMING | 4 | 表示收到来电。 |
| CCALL\_STATE\_WAITING | 5 | 同一个卡槽上已经存在一路通话的情况下，又收到一路来电。 |
| CCALL\_STATE\_DISCONNECTED | 6 | 表示通话已经释放完成。 |
| CCALL\_STATE\_DISCONNECTING | 7 | 表示通话正在释放中，还没有释放完成。 |
| CCALL\_STATE\_IDLE | 8 | 表示没有正在进行的呼叫。 |
| CCALL\_STATE\_ANSWERED | 9 | 表示来电已经接听。 |

## EmergencyNumberOptions7+

PhoneTabletWearable

判断是否是紧急电话号码的可选参数。

**系统能力**：SystemCapability.Telephony.CallManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| slotId | number | 否 | 是 | 卡槽ID：  - 卡槽1：0。  - 卡槽2：1。 |

## NumberFormatOptions7+

PhoneTabletWearable

格式化号码的可选参数。

**系统能力**：SystemCapability.Telephony.CallManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| countryCode | string | 否 | 是 | 国家码，支持所有国家的国家码，如：CN（中国）。默认为：CN。 |
