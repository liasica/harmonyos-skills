---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-dlpantipeep-api
title: DlpAntiPeep（防窥保护）
breadcrumb: API参考 > 系统 > 安全 > Device Security Kit（设备安全服务） > ArkTS API > DlpAntiPeep（防窥保护）
category: harmonyos-references
scraped_at: 2026-04-28T08:07:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:469914ebfc9387f25adfd4f9093beeda4b33205042f986c61de1c4bf8ae6c6ff
---

本模块提供窥视状态相关接口，应用根据窥视状态保护用户隐私，如拉起系统级蒙层遮盖窗口，非机主状态（即有非机主以外的人在注视屏幕）下不进行个性化推荐、隐藏浏览记录、支付记录、收藏记录等敏感信息。

**起始版本：** 6.0.0(20)

## 导入模块

Phone

```
1. import { dlpAntiPeep } from '@kit.DeviceSecurityKit';
```

## DlpAntiPeepStatus

Phone

表示窥视状态的枚举。

**系统能力**：SystemCapability.Security.DlpAntiPeep

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PASS | 0 | 表示当前设备屏幕无人在窥视。 |
| HIDE | 1 | 表示有除机主以外的人在窥视设备屏幕。 |

## isDlpAntiPeepSwitchOn

Phone

isDlpAntiPeepSwitchOn(): Promise<boolean>

检查当前应用是否开启防窥保护。使用Promise异步回调。

**需要权限：** ohos.permission.DLP\_GET\_HIDE\_STATUS

**系统能力：** SystemCapability.Security.DlpAntiPeep

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回当前应用是否开启了防窥保护，true代表开启，false代表未开启，默认值为false。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-dlpantipeep.md) **。**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. Function isDlpAntiPeepSwitchOn can not work correctly due to limited device capabilities. |
| 1020600001 | Internal error. |

**示例：**

```
1. import { dlpAntiPeep } from '@kit.DeviceSecurityKit';

3. try {
4. let result = await dlpAntiPeep.isDlpAntiPeepSwitchOn();
5. console.info('Succeeded in getting switch status.');
6. } catch (error) {
7. console.error(`Failed to get switch status. Code: ${error.code}, message: ${error.message}`);
8. }
```

## on("dlpAntiPeep")

Phone

on(type: 'dlpAntiPeep', callback: Callback<DlpAntiPeepStatus>): void

订阅防窥保护通知。使用callback方式异步返回结果。

注意

请在满足[开发前置条件](../harmonyos-guides/devicesecurity-dlpantipeep.md#开发前置条件)后再调用此接口，避免无法触发防窥回调。调用接口成功后，并且应用在前台可见时才会收到防窥回调。

**需要权限：** ohos.permission.DLP\_GET\_HIDE\_STATUS

**系统能力：** SystemCapability.Security.DlpAntiPeep

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 表示需要订阅的事件'dlpAntiPeep'，取值为固定字符串'dlpAntiPeep'。 |
| callback | Callback<[DlpAntiPeepStatus](devicesecurity-dlpantipeep-api.md#dlpantipeepstatus)> | 是 | 回调函数，返回调用结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-dlpantipeep.md) **。**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 1020600001 | Internal error. |

**示例：**

```
1. import { dlpAntiPeep } from '@kit.DeviceSecurityKit';

3. try {
4. dlpAntiPeep.on('dlpAntiPeep', (dlpAntiPeepStatus: dlpAntiPeep.DlpAntiPeepStatus) => {
5. console.info('Succeeded in subscribing dlpAntiPeep.');
6. });
7. } catch (error) {
8. console.error(`Failed to subscribe dlpAntiPeep. Code: ${error.code}, message: ${error.message}`);
9. }
```

## off("dlpAntiPeep")

Phone

off(type: 'dlpAntiPeep', callback?: Callback<DlpAntiPeepStatus>): void

解订阅防窥保护通知。使用callback方式异步返回结果。

**需要权限：** ohos.permission.DLP\_GET\_HIDE\_STATUS

**系统能力：** SystemCapability.Security.DlpAntiPeep

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 表示需要解订阅的事件'dlpAntiPeep'，取值为固定字符串'dlpAntiPeep'。 |
| callback | Callback<[DlpAntiPeepStatus](devicesecurity-dlpantipeep-api.md#dlpantipeepstatus)> | 否 | 用于接收防窥保护通知的回调函数。如果传入了callback，则取消callback的订阅，否则取消所有callback的订阅。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-dlpantipeep.md) **。**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 1020600001 | Internal error. |

**示例：**

```
1. import { dlpAntiPeep } from '@kit.DeviceSecurityKit';

3. try {
4. dlpAntiPeep.off('dlpAntiPeep', (dlpAntiPeepStatus: dlpAntiPeep.DlpAntiPeepStatus) => {
5. console.info('Succeeded in unsubscribing dlpAntiPeep.');
6. });
7. } catch (error) {
8. console.error(`Failed to unsubscribe dlpAntiPeep. Code: ${error.code}, message: ${error.message}`);
9. }
```

## getDlpAntiPeepInfo

Phone

getDlpAntiPeepInfo(): DlpAntiPeepStatus

获取当前应用的窥视状态。

**需要权限：** ohos.permission.DLP\_GET\_HIDE\_STATUS

**系统能力：** SystemCapability.Security.DlpAntiPeep

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DlpAntiPeepStatus](devicesecurity-dlpantipeep-api.md#dlpantipeepstatus) | 表示窥视状态。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-dlpantipeep.md) **。**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. Function getDlpAntiPeepInfo can not work correctly due to limited device capabilities. |
| 1020600001 | Internal error. |

**示例：**

```
1. import { dlpAntiPeep } from '@kit.DeviceSecurityKit';

3. try {
4. let dlpAntiPeepStatus = dlpAntiPeep.getDlpAntiPeepInfo();
5. console.info('Succeeded in getting DlpAntiPeepStatus.');
6. } catch (error) {
7. console.error(`Failed to get DlpAntiPeepStatus. Code: ${error.code}, message: ${error.message}`);
8. }
```

## passDlpAntiPeepInfo

Phone

passDlpAntiPeepInfo(): void

设置当前应用窥视状态为非窥视，后续[on("dlpAntiPeep")](devicesecurity-dlpantipeep-api.md#ondlpantipeep)接口回调函数返回的窥视状态、[getDlpAntiPeepInfo](devicesecurity-dlpantipeep-api.md#getdlpantipeepinfo)接口直接获取的窥视状态均为无人窥视屏幕。

若应用在生命周期内不再需要接受窥视状态，可直接调用[off("dlpAntiPeep")](devicesecurity-dlpantipeep-api.md#offdlpantipeep)接口解注册，若仍想接受放通后的非窥视状态，则可以调用该接口。

注意

请在满足[开发前置条件](../harmonyos-guides/devicesecurity-dlpantipeep.md#开发前置条件)并调用[on("dlpAntiPeep")](devicesecurity-dlpantipeep-api.md#ondlpantipeep)接口注册后再调用该接口，可用于在应用注册的生命周期内将回调状态变更为非防窥状态，直到应用退出或设备锁屏。

**需要权限：** ohos.permission.DLP\_GET\_HIDE\_STATUS

**系统能力：** SystemCapability.Security.DlpAntiPeep

**起始版本：** 6.0.0(20)

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-dlpantipeep.md) **。**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. Function passDlpAntiPeepInfo can not work correctly due to limited device capabilities. |
| 1020600001 | Internal error. |

**示例：**

```
1. import { dlpAntiPeep } from '@kit.DeviceSecurityKit';

3. try {
4. dlpAntiPeep.passDlpAntiPeepInfo();
5. console.info('Succeeded in calling passDlpAntiPeepInfo.');
6. } catch (error) {
7. console.error(`Failed to call passDlpAntiPeepInfo. Code: ${error.code}, message: ${error.message}`);
8. }
```

## setAntiPeepMaskLayer

Phone

setAntiPeepMaskLayer(windowId: number): Promise<void>

对指定窗口设置系统级蒙层，使用Promise异步回调。

注意

该接口调用后会拉起蒙层，覆盖应用窗口，建议开发者在检测到窥视状态后调用一次即可，频繁调用可能对用户体验造成影响。

**需要权限：** ohos.permission.DLP\_GET\_HIDE\_STATUS

**系统能力：** SystemCapability.Security.DlpAntiPeep

**起始版本：** 6.0.1(21)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| windowId | number | 是 | 应用需要覆盖保护的窗口ID，该参数取值范围为大于0的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-dlpantipeep.md) **。**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. Function setAntiPeepMaskLayer can not work correctly due to limited device capabilities. |
| 1020600001 | Internal error. |
| 1020600002 | The antipeep function is not enabled. |
| 1020600003 | The protected application is not displayed on the screen. |

**示例：**

```
1. import { dlpAntiPeep } from '@kit.DeviceSecurityKit';
2. import { common } from '@kit.AbilityKit';
3. import { window } from '@kit.ArkUI';

5. try {
6. const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
7. const win: window.Window = await window.getLastWindow(context);
8. const windowId: number = win.getWindowProperties().id;
9. await dlpAntiPeep.setAntiPeepMaskLayer(windowId);
10. console.info('Succeeded in setting AntiPeep MaskLayer.');
11. } catch (error) {
12. console.error(`Failed to set AntiPeep MaskLayer. Code: ${error.code}, message: ${error.message}`);
13. }
```

## requestAntiPeepOptions

Phone

requestAntiPeepOptions(context: Context): Promise<AntiPeepOptionsResult>

用于UIAbility/UIExtensionAbility拉起设置弹框，请求用户打开防窥保护开关。使用Promise异步回调。

**需要权限：** ohos.permission.DLP\_GET\_HIDE\_STATUS

**系统能力：** SystemCapability.Security.DlpAntiPeep

**起始版本：** 6.1.0(23)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 请求权限的UIAbility/UIExtensionAbility的Context。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AntiPeepOptionsResult](devicesecurity-dlpantipeep-api.md#antipeepoptionsresult)> | Promise对象，返回防窥保护开关设置的结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-dlpantipeep.md) **。**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. Function requestAntiPeepOptions can not work correctly due to limited device capabilities. |
| 1020600001 | Internal error. |
| 1020600004 | Facial recognition is not set. |

**示例：**

```
1. import { dlpAntiPeep } from '@kit.DeviceSecurityKit';
2. import { common } from '@kit.AbilityKit';

4. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
5. dlpAntiPeep.requestAntiPeepOptions(context).then((data: dlpAntiPeep.AntiPeepOptionsResult) => {
6. console.info(`Succeeded in calling requestAntiPeepOptions, result: ${data}.`);
7. }).catch((error: BusinessError) => {
8. console.error(`Failed to call requestAntiPeepOptions. Code: ${error.code}, message: ${error.message}`);
9. })
```

## AntiPeepOptionsResult

Phone

表示弹框设置结果的枚举。

**系统能力：** SystemCapability.Security.DlpAntiPeep

**起始版本：** 6.1.0(23)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUCCESS | 0 | 表示防窥保护开关开启成功。 |
| FAIL | 1 | 表示防窥保护开关开启失败。 |
| ALREADY\_ON | 2 | 表示防窥保护开关已处于开启状态。 |

## publishAntiPeepInformation

Phone

publishAntiPeepInformation(): Promise<void>

发布防窥保护提示信息。使用Promise异步回调。

当设备持续处于窥屏风险状态时，系统只会主动发送一次时长5秒的实况窗提醒，再次提醒需要通过本接口主动触发。

**需要权限：** ohos.permission.DLP\_GET\_HIDE\_STATUS

**系统能力：** SystemCapability.Security.DlpAntiPeep

**起始版本：** 6.1.0(23)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-dlpantipeep.md) **。**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. Function publishAntiPeepInformation can not work correctly due to limited device capabilities. |
| 1020600001 | Internal error. |
| 1020600002 | The anti-peep function is not enabled. |
| 1020600003 | The protected application is not displayed on the screen. |
| 1020600005 | The anti-peep information has been published. |
| 1020600006 | No peeping risk detected. |

**示例：**

```
1. import { dlpAntiPeep } from '@kit.DeviceSecurityKit';

3. dlpAntiPeep.publishAntiPeepInformation().then(() => {
4. console.info(`Succeeded in calling publishAntiPeepInformation, result: ${data}.`);
5. }).catch((error: BusinessError) => {
6. console.error(`Failed to call publishAntiPeepInformation. Code: ${error.code}, message: ${error.message}`);
7. })
```
