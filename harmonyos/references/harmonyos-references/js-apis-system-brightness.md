---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-brightness
title: @system.brightness (屏幕亮度)
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 已停止维护的接口 > @system.brightness (屏幕亮度)
category: harmonyos-references
scraped_at: 2026-04-28T08:09:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8f3cce8d0a75521565436858577dcc008d9d113503e53223c51608901d35d7fb
---

该模块提供屏幕亮度和模式的查询、调节接口。

说明

* 模块维护策略：

  - 对于Lite Wearable设备类型，该模块长期维护，正常使用。

  - 对于支持该模块的其他设备类型，该模块从API Version 7 开始不再维护，替代接口能力仅对系统应用开放。
* 本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

WearableLite Wearable

```
1. import brightness, { BrightnessModeResponse, BrightnessResponse } from '@system.brightness';
```

## brightness.getValue(deprecated)

WearableLite Wearable

getValue(options?: GetBrightnessOptions): void

获得设备当前的屏幕亮度值。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [GetBrightnessOptions](js-apis-system-brightness.md#getbrightnessoptionsdeprecated) | 否 | 获取屏幕亮度的参数对象。可选，默认为空。 |

**示例：**

```
1. brightness.getValue({
2. success: (data: BrightnessResponse) => {
3. console.log('success get brightness value:' + data.value);
4. },
5. fail: (data: string, code: number) => {
6. console.error('get brightness fail, code: ' + code + ', data: ' + data);
7. }
8. });
```

## brightness.setValue(deprecated)

WearableLite Wearable

setValue(options?: SetBrightnessOptions): void

设置设备当前的屏幕亮度值。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SetBrightnessOptions](js-apis-system-brightness.md#setbrightnessoptionsdeprecated) | 否 | 设置屏幕亮度的参数对象。可选，默认为空。 |

**示例：**

```
1. brightness.setValue({
2. value: 100,
3. success: () => {
4. console.log('handling set brightness success.');
5. },
6. fail: (data: string, code: number) => {
7. console.error('handling set brightness value fail, code:' + code + ', data: ' + data);
8. }
9. });
```

## brightness.getMode(deprecated)

WearableLite Wearable

getMode(options?: GetBrightnessModeOptions): void

获得当前屏幕亮度模式。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [GetBrightnessModeOptions](js-apis-system-brightness.md#getbrightnessmodeoptionsdeprecated) | 否 | 获取屏幕亮度模式的参数对象。可选，默认为空。 |

**示例：**

```
1. brightness.getMode({
2. success: (data: BrightnessModeResponse) => {
3. console.log('success get mode:' + data.mode);
4. },
5. fail: (data: string, code: number) => {
6. console.error('handling get mode fail, code:' + code + ', data: ' + data);
7. }
8. });
```

## brightness.setMode(deprecated)

WearableLite Wearable

setMode(options?: SetBrightnessModeOptions): void

设置设备当前的屏幕亮度模式。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SetBrightnessModeOptions](js-apis-system-brightness.md#setbrightnessmodeoptionsdeprecated) | 否 | 设置屏幕亮度模式的参数对象。可选，默认为空。 |

**示例：**

```
1. brightness.setMode({
2. mode: 1,
3. success: () => {
4. console.log('handling set mode success.');
5. },
6. fail: (data: string, code: number) => {
7. console.error('handling set mode fail, code:' + code + ', data: ' + data);
8. }
9. });
```

## brightness.setKeepScreenOn(deprecated)

WearableLite Wearable

setKeepScreenOn(options?: SetKeepScreenOnOptions): void

除Lite Wearable外，从API version 7开始不再维护，建议使用[window.setWindowKeepScreenOn()](arkts-apis-window-window.md#setwindowkeepscreenon9)替代。

设置屏幕是否保持常亮状态，开启常亮模式推荐在onShow()阶段调用。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SetKeepScreenOnOptions](js-apis-system-brightness.md#setkeepscreenonoptionsdeprecated) | 否 | 设置屏幕常亮的参数对象。可选，默认为空。 |

**示例：**

```
1. brightness.setKeepScreenOn({
2. keepScreenOn: true,
3. success: () => {
4. console.log('handling set keep screen on success.');
5. },
6. fail: (data: string, code: number) => {
7. console.error('handling set keep screen on fail, code:' + code + ', data: ' + data);
8. }
9. });
```

## GetBrightnessOptions(deprecated)

WearableLite Wearable

获取屏幕亮度的参数对象。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | (data: [BrightnessResponse](js-apis-system-brightness.md#brightnessresponsedeprecated)) => void | 否 | 接口调用成功的回调函数。data为[BrightnessResponse](js-apis-system-brightness.md#brightnessresponsedeprecated)类型的返回值。 |
| fail | (data: string, code: number) => void | 否 | 接口调用失败的回调函数。data为错误信息，code为错误码。 |
| complete | () => void | 否 | 接口调用结束的回调函数。 |

## SetBrightnessOptions(deprecated)

WearableLite Wearable

设置屏幕亮度的参数对象。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 屏幕亮度，值为1-255之间的整数。  - 如果值小于等于0，系统按1处理。  - 如果值大于255，系统按255处理。  - 如果值为小数，系统将处理为整数。例如设置为8.1，系统按8处理。 |
| success | () => void | 否 | 接口调用成功的回调函数。 |
| fail | (data: string, code: number) => void | 否 | 接口调用失败的回调函数。data为错误信息，code为错误码。 |
| complete | () => void | 否 | 接口调用结束的回调函数。 |

## BrightnessResponse(deprecated)

WearableLite Wearable

包含屏幕亮度的对象。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite

| 名称 | 类型 | 可读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| value | number | 是 | 否 | 屏幕亮度，范围：1到255。 |

## GetBrightnessModeOptions(deprecated)

WearableLite Wearable

获取屏幕亮度模式的参数对象。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | (data: [BrightnessModeResponse](js-apis-system-brightness.md#brightnessmoderesponsedeprecated)) => void | 否 | 接口调用成功的回调函数。data为[BrightnessModeResponse](js-apis-system-brightness.md#brightnessmoderesponsedeprecated)类型的返回值。 |
| fail | (data: string, code: number) => void | 否 | 接口调用失败的回调函数。data为错误信息，code为错误码。 |
| complete | () => void | 否 | 接口调用结束的回调函数。 |

## SetBrightnessModeOptions(deprecated)

WearableLite Wearable

设置屏幕亮度模式的参数对象。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | number | 是 | 0表示手动调节屏幕亮度模式，1表示自动调节屏幕亮度模式。 |
| success | () => void | 否 | 接口调用成功的回调函数。 |
| fail | (data: string, code: number) => void | 否 | 接口调用失败的回调函数。data为错误信息，code为错误码。 |
| complete | () => void | 否 | 接口调用结束的回调函数。 |

## BrightnessModeResponse(deprecated)

WearableLite Wearable

包含屏幕亮度模式的对象。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite

| 名称 | 类型 | 可读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| mode | number | 是 | 否 | 0表示手动调节屏幕亮度模式，1表示自动调节屏幕亮度模式。 |

## SetKeepScreenOnOptions(deprecated)

WearableLite Wearable

设置屏幕常亮的参数对象。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keepScreenOn | boolean | 是 | true表示保持屏幕常亮，false表示取消屏幕常亮。 |
| success | () => void | 否 | 接口调用成功的回调函数。 |
| fail | (data: string, code: number) => void | 否 | 接口调用失败的回调函数。data为错误信息，code为错误码。 |
| complete | () => void | 否 | 接口调用结束的回调函数。 |
