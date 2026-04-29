---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-floatingball
title: @ohos.window.floatingBall (闪控球窗口)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > 窗口管理 > @ohos.window.floatingBall (闪控球窗口)
category: harmonyos-references
scraped_at: 2026-04-29T13:50:55+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:9e041da87343027dba08196258f7359f749a35ba9b41725b152ca9b99862a471
---

该模块提供闪控球的基础功能，包括判断设备是否支持闪控球功能，以及创建闪控球控制器来启动、更新或停止闪控球。适用于跨应用的题目搜索、账单记录、商品比价、抢单、翻译场景，以及金融类应用的实时盯盘场景，以小窗模式呈现内容。闪控球以悬浮小组件形式显示在其他应用之上，即时呈现应用的关键信息。

说明

* 本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 针对系统能力SystemCapability.Window.SessionManager，请先使用[canIUse()](js-apis-syscap.md#caniuse)接口判断当前设备是否支持此syscap及对应接口。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { floatingBall } from '@kit.ArkUI';
```

## floatingBall.isFloatingBallEnabled

PhonePC/2in1TabletTVWearable

isFloatingBallEnabled(): boolean

判断当前设备是否支持闪控球功能。

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 当前设备是否支持闪控球功能。true表示支持，false则表示不支持。 |

**示例：**

```
1. let enable: boolean = floatingBall.isFloatingBallEnabled();
2. console.info('Floating ball enabled is: ' + enable);
```

## floatingBall.create

PhonePC/2in1TabletTVWearable

create(config: FloatingBallConfiguration): Promise<FloatingBallController>

创建闪控球控制器，使用Promise异步回调。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在Tablet设备的非电脑模式、Phone设备下可正常调用，在其他设备、Tablet设备的电脑模式下调用返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [FloatingBallConfiguration](js-apis-floatingball.md#floatingballconfiguration) | 是 | 创建闪控球控制器的参数。该参数不能为空，并且构造该参数的context不能为空。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[FloatingBallController](js-apis-floatingball.md#floatingballcontroller)> | Promise对象。返回当前创建的闪控球控制器。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.Failed to call the API due to limited device capabilities. |
| 1300019 | Wrong parameters for operating the floating ball. |
| 1300023 | Floating ball internal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. let floatingBallController: floatingBall.FloatingBallController | undefined = undefined;
5. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回的结果为UIAbilityContext
6. let ctx = this.getUIContext().getHostContext() as common.UIAbilityContext;
7. let config: floatingBall.FloatingBallConfiguration = {
8. context: ctx,
9. };
10. try {
11. floatingBall.create(config).then((data: floatingBall.FloatingBallController) => {
12. floatingBallController = data;
13. console.info(`Succeeded in creating floating ball controller. Data: ${data}`);
14. }).catch((err: BusinessError) => {
15. console.error(`Failed to create floating ball controller. Cause:${err.code}, message:${err.message}`);
16. });
17. } catch(e) {
18. console.error(`Failed to create floating ball controller. Cause:${e.code}, message:${e.message}`);
19. }
```

## FloatingBallConfiguration

PhonePC/2in1TabletTVWearable

创建闪控球控制器时需要提供的参数配置。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [BaseContext](js-apis-inner-application-basecontext.md) | 否 | 否 | 表示上下文环境。 |

## FloatingBallController

PhonePC/2in1TabletTVWearable

闪控球控制器实例，用于启动、更新、停止闪控球以及注册回调等操作。

下列API示例中都需先使用[floatingBall.create()](js-apis-floatingball.md#floatingballcreate)方法获取到闪控球控制器实例（即floatingBallController），再通过此实例调用对应方法。

**系统能力：** SystemCapability.Window.SessionManager

### startFloatingBall

PhonePC/2in1TabletTVWearable

startFloatingBall(params: FloatingBallParams): Promise<void>

启动闪控球，使用Promise异步回调。

**需要权限：** ohos.permission.USE\_FLOAT\_BALL

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [FloatingBallParams](js-apis-floatingball.md#floatingballparams) | 是 | 启动闪控球的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed, usually returned by VerifyAccessToken. |
| 1300019 | Wrong parameters for operating the floating ball. |
| 1300020 | Failed to create the floating ball window. |
| 1300021 | Failed to start multiple floating ball windows. |
| 1300022 | Repeated floating ball operation. |
| 1300023 | Floating ball internal error. |
| 1300024 | The floating ball window state is abnormal. |
| 1300025 | The floating ball state does not support this operation. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let startParams: floatingBall.FloatingBallParams = {
4. template: floatingBall.FloatingBallTemplate.EMPHATIC,
5. title: 'title',
6. content: 'content'
7. };
8. try {
9. floatingBallController.startFloatingBall(startParams).then(() => {
10. console.info('Succeeded in starting floating ball.');
11. }).catch((err: BusinessError) => {
12. console.error(`Failed to start floating ball. Cause:${err.code}, message:${err.message}`);
13. });
14. } catch(e) {
15. console.error(`Failed to start floating ball. Cause:${e.code}, message:${e.message}`);
16. }
```

### updateFloatingBall

PhonePC/2in1TabletTVWearable

updateFloatingBall(params: FloatingBallParams): Promise<void>

更新闪控球，使用Promise异步回调。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [FloatingBallParams](js-apis-floatingball.md#floatingballparams) | 是 | 更新闪控球的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |
| 1300019 | Wrong parameters for operating the floating ball. |
| 1300023 | Floating ball internal error. |
| 1300024 | The floating ball window state is abnormal. |
| 1300025 | The floating ball state does not support this operation. |
| 1300027 | When updating the floating ball, the template type cannot be changed. |
| 1300028 | Updating static template-based floating balls is not supported. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let updateParams: floatingBall.FloatingBallParams = {
4. template: floatingBall.FloatingBallTemplate.EMPHATIC,
5. title: 'title2',
6. content: 'content2'
7. };
8. try {
9. floatingBallController.updateFloatingBall(updateParams).then(() => {
10. console.info('Succeeded in updating floating ball.');
11. }).catch((err: BusinessError) => {
12. console.error(`Failed to update floating ball. Cause:${err.code}, message:${err.message}`);
13. });
14. } catch(e) {
15. console.error(`Failed to update floating ball. Cause:${e.code}, message:${e.message}`);
16. }
```

### stopFloatingBall

PhonePC/2in1TabletTVWearable

stopFloatingBall(): Promise<void>

停止闪控球，使用Promise异步回调。

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300022 | Repeated floating ball operation. |
| 1300023 | Floating ball internal error. |
| 1300024 | The floating ball window state is abnormal. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. floatingBallController.stopFloatingBall().then(() => {
4. console.info('Succeeded in stopping floating ball.');
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to stop floating ball. Cause:${err.code}, message:${err.message}`);
7. });
```

### on('stateChange')

PhonePC/2in1TabletTVWearable

on(type: 'stateChange', callback: Callback<FloatingBallState>): void

注册闪控球生命周期状态变化的监听事件。不再使用时，取消监听以避免内存泄漏。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'stateChange'，即闪控球生命周期状态变化事件。 |
| callback | Callback<[FloatingBallState](js-apis-floatingball.md#floatingballstate)> | 是 | 回调函数。返回当前的闪控球生命周期状态。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300019 | Wrong parameters for operating the floating ball. |
| 1300022 | Repeated floating ball operation. |
| 1300023 | Floating ball internal error. |
| 1300024 | The floating ball window state is abnormal. |

**示例：**

```
1. let onStateChange = (state: floatingBall.FloatingBallState) => {
2. console.info('Floating ball stateChange: ' + state);
3. };
4. try {
5. floatingBallController.on('stateChange', onStateChange);
6. } catch(e) {
7. console.error(`Failed to on stateChange floating ball. Cause:${e.code}, message:${e.message}`);
8. }
```

### off('stateChange')

PhonePC/2in1TabletTVWearable

off(type: 'stateChange', callback?: Callback<FloatingBallState>): void

取消闪控球生命周期状态变化的监听事件。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'stateChange'，即闪控球生命周期状态变化事件。 |
| callback | Callback<[FloatingBallState](js-apis-floatingball.md#floatingballstate)> | 否 | 回调函数。返回当前的闪控球生命周期状态。若传入参数，则停止该监听。若未传入参数，则停止所有闪控球生命周期状态变化的监听。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300019 | Wrong parameters for operating the floating ball. |
| 1300023 | Floating ball internal error. |
| 1300024 | The floating ball window state is abnormal. |

**示例：**

```
1. let onStateChange = (state: floatingBall.FloatingBallState) => {
2. console.info('Floating ball stateChange: ' + state);
3. };
4. try {
5. floatingBallController.off('stateChange', onStateChange);
6. } catch(e) {
7. console.error(`Failed to off stateChange floating ball. Cause:${e.code}, message:${e.message}`);
8. }
```

### on('click')

PhonePC/2in1TabletTVWearable

on(type: 'click', callback: Callback<void>): void

注册闪控球的点击监听事件，不使用时，取消监听以避免内存泄漏。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'click'，即闪控球点击事件。 |
| callback | Callback<void> | 是 | 回调函数。当点击闪控球事件发生时的回调。该回调函数不返回任何参数。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300019 | Wrong parameters for operating the floating ball. |
| 1300022 | Repeated floating ball operation. |
| 1300023 | Floating ball internal error. |
| 1300024 | The floating ball window state is abnormal. |

**示例：**

```
1. let onClick = () => {
2. console.info('Floating ball onClick');
3. };
4. try {
5. floatingBallController.on('click', onClick);
6. } catch(e) {
7. console.error(`Failed to on click floating ball. Cause:${e.code}, message:${e.message}`);
8. }
```

### off('click')

PhonePC/2in1TabletTVWearable

off(type: 'click', callback?: Callback<void>): void

取消闪控球点击的监听事件。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'click'，即闪控球点击事件。 |
| callback | Callback<void> | 否 | 回调函数。当点击闪控球事件发生时的回调。该回调函数不返回任何参数。若传入参数，则关闭特定的监听。若未传入参数，则关闭所有闪控球点击的监听。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300019 | Wrong parameters for operating the floating ball. |
| 1300023 | Floating ball internal error. |
| 1300024 | The floating ball window state is abnormal. |

**示例：**

```
1. let onClick = () => {
2. console.info('Floating ball onClick');
3. };
4. try {
5. floatingBallController.off('click', onClick);
6. } catch(e) {
7. console.error(`Failed to off click floating ball. Cause:${e.code}, message:${e.message}`);
8. }
```

### getFloatingBallWindowInfo

PhonePC/2in1TabletTVWearable

getFloatingBallWindowInfo(): Promise<FloatingBallWindowInfo>

获得闪控球窗口信息，使用Promise异步回调。

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[FloatingBallWindowInfo](js-apis-floatingball.md#floatingballwindowinfo)> | Promise对象，返回闪控球窗口信息。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |
| 1300023 | Floating ball internal error. |
| 1300024 | The floating ball window state is abnormal. |
| 1300025 | The floating ball state does not support this operation. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. floatingBallController.getFloatingBallWindowInfo().then((data: floatingBall.FloatingBallWindowInfo) => {
4. console.info('Succeeded in getting floating ball window info. Info: ' + JSON.stringify(data));
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to get floating ball window info. Cause code: ${err.code}, message: ${err.message}`);
7. });
```

### restoreMainWindow

PhonePC/2in1TabletTVWearable

restoreMainWindow(want: Want): Promise<void>

恢复应用主窗口并加载指定页面。仅支持在点击闪控球后调用，使用Promise异步回调。

**需要权限：** ohos.permission.USE\_FLOAT\_BALL

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 加载指定页面的Want。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed, usually returned by VerifyAccessToken. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |
| 1300019 | Wrong parameters for operating the floating ball. |
| 1300023 | Floating ball internal error. |
| 1300024 | The floating ball window state is abnormal. |
| 1300025 | The floating ball state does not support this operation. |
| 1300026 | Failed to restore the main window. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { Want } from '@kit.AbilityKit';

4. let want: Want = {
5. bundleName: 'xxx.xxx.xxx',
6. abilityName: 'EntryAbility'
7. };
8. try {
9. floatingBallController.restoreMainWindow(want).then(() => {
10. console.info('Succeeded in restoring floating ball main window.');
11. }).catch((err: BusinessError) => {
12. console.error(`Failed to restore floating ball main window. Cause code: ${err.code}, message: ${err.message}`);
13. });
14. } catch(e) {
15. console.error(`Failed to create floating ball controller. Cause:${e.code}, message:${e.message}`);
16. }
```

## FloatingBallParams

PhonePC/2in1TabletTVWearable

启动和更新闪控球的配置参数。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| template | [FloatingBallTemplate](js-apis-floatingball.md#floatingballtemplate) | 否 | 否 | 闪控球模板。 |
| title | string | 否 | 否 | 闪控球标题，不可为空字符串，大小不超过64字节。 |
| content | string | 否 | 是 | 闪控球内容，大小不超过64字节。不传入时默认为空字符串，不显示闪控球内容。 |
| backgroundColor | string | 否 | 是 | 闪控球背景颜色，为不带透明度的十六进制颜色格式（例如'#008EF5'或'#FF008EF5'），不传入时闪控球跟随系统深浅色模式的默认背景色。 |
| icon | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | 是 | 闪控球图标，图标像素的总字节数不超过192KB（图标像素的总字节数通过[getPixelBytesNumber](arkts-apis-image-pixelmap.md#getpixelbytesnumber7)获取）。建议图标像素宽高为128px\*128px。实际显示效果依赖于设备能力和闪控球UI样式。 |

## FloatingBallState

PhonePC/2in1TabletTVWearable

闪控球生命周期状态的枚举。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STARTED | 1 | 表示闪控球启动。 |
| STOPPED | 2 | 表示闪控球停止。 |

## FloatingBallTemplate

PhonePC/2in1TabletTVWearable

闪控球模板类型的枚举。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STATIC | 1 | 静态布局，支持标题和图标。使用此模板时，FloatingBallParams中的title参数和icon参数必传。 |
| NORMAL | 2 | 普通文本布局，支持标题和内容。使用此模板时，FloatingBallParams中的title参数必传。 |
| EMPHATIC | 3 | 强调文本布局，支持图标、标题和内容。使用此模板时，FloatingBallParams中的title参数必传。 |
| SIMPLE | 4 | 纯文本布局，只支持标题。使用此模板时，FloatingBallParams中的title参数必传。 |

## FloatingBallWindowInfo

PhonePC/2in1TabletTVWearable

闪控球窗口信息。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| windowId | number | 是 | 否 | 闪控球窗口ID。 |
