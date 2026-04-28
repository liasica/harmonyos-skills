---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-avcastpickerhelper
title: Class (AVCastPickerHelper)
breadcrumb: API参考 > 媒体 > AVSession Kit（音视频播控服务） > ArkTS API > @ohos.multimedia.avsession (媒体会话管理) > Class (AVCastPickerHelper)
category: harmonyos-references
scraped_at: 2026-04-28T08:12:15+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:f8c3a89b26ab13c59cc6b7d7cba2624365e301bc83a61cc1d62b763015a54f21
---

投播半模态对象，可拉起半模态窗口，选择投播设备。在使用前，需要创建AVCastPickerHelper实例。

说明

* 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Class首批接口从API version 14开始支持。
* AVCastPickerHelper样式显示为半模态，实际会绑定[全模态页面（bindContentCover）](ts-universal-attributes-modal-transition.md#bindcontentcover)。

## 导入模块

PhonePC/2in1TabletTV

```
1. import { avSession } from '@kit.AVSessionKit';
```

## constructor14+

PhonePC/2in1TabletTV

constructor(context: Context)

创建AVCastPickerHelper对象，获取context参考[getHostContext](arkts-apis-uicontext-uicontext.md#gethostcontext12)。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文（仅支持[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)）。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |

**示例：**

```
1. import { avSession } from '@kit.AVSessionKit';

3. @Entry
4. @Component
5. struct Index {
6. @State message: string = 'hello world';

8. build() {
9. Row() {
10. Column() {
11. Text(this.message)
12. .fontSize(40)
13. .fontWeight(FontWeight.Bold)
14. .onClick(() => {
15. let context = this.getUIContext().getHostContext() as Context;
16. let avCastPicker = new avSession.AVCastPickerHelper(context);
17. })
18. }
19. .width('100%')
20. }
21. .height('100%')
22. }
23. }
```

## select14+

PhonePC/2in1TabletTV

select(options?: AVCastPickerOptions): Promise<void>

通过选择模式拉起AVCastPicker界面，用户可以选择投播设备。接口采用Promise异步返回形式，传入可选参数AVCastPickerOptions对象，无返回值。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [AVCastPickerOptions](arkts-apis-avsession-i.md#avcastpickeroptions14) | 否 | AVCastPicker选择选项。无此参数时，以AVCastPickerOptions默认值拉起。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。当命令发送成功，无返回结果，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { avSession } from '@kit.AVSessionKit';

4. class MyPage {
5. private avCastPicker: avSession.AVCastPickerHelper;

7. constructor(context: common.Context) {
8. this.avCastPicker = new avSession.AVCastPickerHelper(context);
9. }

11. async selectCastDevice() {
12. const avCastPickerOptions: avSession.AVCastPickerOptions = {
13. sessionType: 'video',
14. };

16. this.avCastPicker.select(avCastPickerOptions).then(() => {
17. console.info('Succeeded in selecting.');
18. });
19. }
20. }
```

## resetCommunicationDevice21+

PhonePC/2in1TabletTV

resetCommunicationDevice(): Promise<void>

将应用通话设备恢复至默认设备。比如在语音通话场景下，手机设备的通话装置将恢复成听筒。使用Promise异步回调。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { avSession } from '@kit.AVSessionKit';

4. async function avCastPicker(context: common.Context) {
5. let avCastPicker = new avSession.AVCastPickerHelper(context);
6. avCastPicker.resetCommunicationDevice().then(() => {
7. console.info('Succeeded in resetting communication device.');
8. });
9. }
```

## on('pickerStateChange')14+

PhonePC/2in1TabletTV

on(type: 'pickerStateChange', callback: Callback<AVCastPickerState>) : void

设置半模态窗口变化的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'pickerStateChange'：当半模态窗口变化时，触发该事件。 |
| callback | Callback<[AVCastPickerState](js-apis-avcastpickerparam.md#avcastpickerstate)> | 是 | 回调函数，参数state是变化后的半模态窗口状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { AVCastPickerState } from '@kit.AVSessionKit';
3. import { avSession } from '@kit.AVSessionKit';

5. async function onPickerStateChange(context: common.Context) {
6. let avCastPicker = new avSession.AVCastPickerHelper(context);
7. avCastPicker.on('pickerStateChange', (state: AVCastPickerState) => {
8. console.info(`picker state change : ${state}`);
9. });
10. }
```

## off('pickerStateChange')14+

PhonePC/2in1TabletTV

off(type: 'pickerStateChange', callback?: Callback<AVCastPickerState>) : void

取消半模态窗口变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'pickerStateChange'。 |
| callback | Callback<[AVCastPickerState](js-apis-avcastpickerparam.md#avcastpickerstate)> | 否 | 回调函数，参数state是变化后的半模态窗口状态。  当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { avSession } from '@kit.AVSessionKit';

4. async function onPickerStateChange(context: common.Context) {
5. let avCastPicker = new avSession.AVCastPickerHelper(context);
6. avCastPicker.off('pickerStateChange');
7. }
```
