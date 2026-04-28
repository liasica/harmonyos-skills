---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-uiextension
title: @ohos.arkui.uiExtension (uiExtension)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.uiExtension (uiExtension)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a268a92dcda9206ab3e128aaaf05b70cf33d5262a5461b16b0349a74bf3d6ec8
---

用于[EmbeddedUIExtensionAbility](../harmonyos-guides/embeddeduiextensionability.md)（或[UIExtensionAbility](js-apis-app-ability-uiextensionability.md#uiextensionability)）中获取宿主应用的窗口信息或对应的[EmbeddedComponent](ts-container-embedded-component.md)组件的信息。

说明

从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { uiExtension } from '@kit.ArkUI';
```

## WindowProxy

PhonePC/2in1TabletTVWearable

UIExtension宿主窗代理。

### 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 14开始，该接口支持在元服务中使用

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| properties14+ | [WindowProxyProperties](js-apis-arkui-uiextension.md#windowproxyproperties14) | 否 | 否 | 组件（EmbeddedComponent或UIExtensionComponent）的信息。  **约束：** 由于架构约束，不建议在[onSessionCreate](js-apis-app-ability-uiextensionability.md#onsessioncreate)阶段同步获取该值，建议在收到[on('windowSizeChange')](js-apis-arkui-uiextension.md#onwindowsizechange)回调之后获取。 |

### getWindowAvoidArea

PhonePC/2in1TabletTVWearable

getWindowAvoidArea(type: window.AvoidAreaType): window.AvoidArea

获取宿主应用窗口内容规避的区域；如系统栏区域、刘海屏区域、手势区域、软键盘区域等与宿主窗口内容重叠时，需要宿主窗口内容避让的区域。

**系统能力**：SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [window.AvoidAreaType](arkts-apis-window-e.md#avoidareatype7) | 是 | 表示避让区类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [window.AvoidArea](arkts-apis-window-i.md#avoidarea7) | 宿主窗口内容避让区域。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```
1. // ExtensionProvider.ts
2. import { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
3. import { window } from '@kit.ArkUI';

5. export default class EntryAbility extends EmbeddedUIExtensionAbility {
6. onSessionCreate(want: Want, session: UIExtensionContentSession) {
7. const extensionWindow = session.getUIExtensionWindowProxy();
8. // 获取宿主应用窗口的避让信息
9. let avoidArea: window.AvoidArea | undefined = extensionWindow?.getWindowAvoidArea(window.AvoidAreaType.TYPE_SYSTEM);
10. console.info(`avoidArea: ${JSON.stringify(avoidArea)}`);
11. }
12. }
```

### on('avoidAreaChange')

PhonePC/2in1TabletTVWearable

on(type: 'avoidAreaChange', callback: Callback<AvoidAreaInfo>): void

注册系统避让区变化的监听。

**系统能力**：SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，固定为'avoidAreaChange'，即系统避让区变化事件。 |
| callback | [Callback](js-apis-base.md#callback)<[AvoidAreaInfo](js-apis-arkui-uiextension.md#avoidareainfo)> | 是 | 回调函数：入参用于接收当前避让区的信息。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```
1. // ExtensionProvider.ts
2. import { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
3. import { uiExtension } from '@kit.ArkUI';

5. export default class EntryAbility extends EmbeddedUIExtensionAbility {
6. onSessionCreate(want: Want, session: UIExtensionContentSession) {
7. const extensionWindow = session.getUIExtensionWindowProxy();
8. // 注册避让区变化的监听
9. extensionWindow.on('avoidAreaChange', (info: uiExtension.AvoidAreaInfo) => {
10. console.info(`The avoid area of the host window is: ${JSON.stringify(info.area)}.`);
11. });
12. }
13. }
```

### off('avoidAreaChange')

PhonePC/2in1TabletTVWearable

off(type: 'avoidAreaChange', callback?: Callback<AvoidAreaInfo>): void

注销系统避让区变化的监听。

**系统能力**：SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 注销的事件类型，固定为'avoidAreaChange'，即系统避让区变化事件。 |
| callback | [Callback](js-apis-base.md#callback)<[AvoidAreaInfo](js-apis-arkui-uiextension.md#avoidareainfo)> | 否 | 回调函数：如果传入该参数，则关闭该监听。如果未传入参数，则关闭所有系统避让区变化的监听。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```
1. // ExtensionProvider.ts
2. import { EmbeddedUIExtensionAbility, UIExtensionContentSession } from '@kit.AbilityKit';

4. export default class EntryAbility extends EmbeddedUIExtensionAbility {
5. onSessionDestroy(session: UIExtensionContentSession) {
6. const extensionWindow = session.getUIExtensionWindowProxy();
7. // 注销所有避让区变化的监听
8. extensionWindow.off('avoidAreaChange');
9. }
10. }
```

### on('windowSizeChange')

PhonePC/2in1TabletTVWearable

on(type: 'windowSizeChange', callback: Callback<window.Size>): void

注册组件（EmbeddedComponent或UIExtensionComponent）尺寸变化的监听。

**系统能力**：SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，固定为'windowSizeChange'，即组件（EmbeddedComponent或UIExtensionComponent）尺寸变化事件。 |
| callback | [Callback](js-apis-base.md#callback)<[window.Size](arkts-apis-window-i.md#size7)> | 是 | 回调函数：入参用于接收当前组件（EmbeddedComponent或UIExtensionComponent）的尺寸。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```
1. // ExtensionProvider.ts
2. import { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
3. import { window } from '@kit.ArkUI';

5. export default class EntryAbility extends EmbeddedUIExtensionAbility {
6. onSessionCreate(want: Want, session: UIExtensionContentSession) {
7. const extensionWindow = session.getUIExtensionWindowProxy();
8. // 注册组件（EmbeddedComponent或UIExtensionComponent）大小变化的监听
9. extensionWindow.on('windowSizeChange', (size: window.Size) => {
10. console.info(`The avoid area of the host window is: ${JSON.stringify(size)}.`);
11. });
12. }
13. }
```

### off('windowSizeChange')

PhonePC/2in1TabletTVWearable

off(type: 'windowSizeChange', callback?: Callback<window.Size>): void

注销组件（EmbeddedComponent或UIExtensionComponent）尺寸变化的监听。

**系统能力**：SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 注销的事件类型，固定值：'windowSizeChange'，即组件（EmbeddedComponent或UIExtensionComponent）尺寸变化事件。 |
| callback | [Callback](js-apis-base.md#callback)<[window.Size](arkts-apis-window-i.md#size7)> | 否 | 回调函数。返回当前的组件（EmbeddedComponent或UIExtensionComponent）尺寸。如果传入该参数，则关闭该监听。如果未传入参数，则关闭组件（EmbeddedComponent或UIExtensionComponent）尺寸变化的监听。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```
1. // ExtensionProvider.ts
2. import { EmbeddedUIExtensionAbility, UIExtensionContentSession } from '@kit.AbilityKit';

4. export default class EntryAbility extends EmbeddedUIExtensionAbility {
5. onSessionDestroy(session: UIExtensionContentSession) {
6. const extensionWindow = session.getUIExtensionWindowProxy();
7. // 注销组件（EmbeddedComponent或UIExtensionComponent）大小变化的监听
8. extensionWindow.off('windowSizeChange');
9. }
10. }
```

### on('rectChange')14+

PhonePC/2in1TabletTVWearable

on(type: 'rectChange', reasons: number, callback: Callback<RectChangeOptions>): void

注册组件（EmbeddedComponent或UIExtensionComponent）位置及尺寸变化的监听。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**设备行为差异：** 该接口在2in1设备中可正常调用，在其他设备中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'rectChange'，即组件（EmbeddedComponent或UIExtensionComponent）矩形变化事件。 |
| reasons | number | 是 | 触发组件（EmbeddedComponent或UIExtensionComponent）位置及尺寸变化的原因，具体取值可参考[RectChangeReason](js-apis-arkui-uiextension.md#rectchangereason14)枚举值。 |
| callback | [Callback](js-apis-base.md#callback)<[RectChangeOptions](js-apis-arkui-uiextension.md#rectchangeoptions14)> | 是 | 回调函数。返回当前组件（EmbeddedComponent或UIExtensionComponent）矩形变化值及变化原因。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. // ExtensionProvider.ts
2. import { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
3. import { uiExtension } from '@kit.ArkUI';

5. export default class EntryAbility extends EmbeddedUIExtensionAbility {
6. onSessionCreate(want: Want, session: UIExtensionContentSession) {
7. const extensionWindow = session.getUIExtensionWindowProxy();
8. // 注册组件（EmbeddedComponent或UIExtensionComponent）位置及尺寸变化的监听
9. extensionWindow.on('rectChange', uiExtension.RectChangeReason.HOST_WINDOW_RECT_CHANGE, (data: uiExtension.RectChangeOptions) => {
10. console.info('Succeeded window rect changes. Data: ' + JSON.stringify(data));
11. });
12. }
13. }
```

### off('rectChange')14+

PhonePC/2in1TabletTVWearable

off(type: 'rectChange', callback?: Callback<RectChangeOptions>): void

注销组件（EmbeddedComponent或UIExtensionComponent）位置及尺寸变化的监听。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**设备行为差异：** 该接口在2in1设备中可正常调用，在其他设备中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'rectChange'，即组件（EmbeddedComponent或UIExtensionComponent）矩形变化事件。 |
| callback | [Callback](js-apis-base.md#callback)<[RectChangeOptions](js-apis-arkui-uiextension.md#rectchangeoptions14)> | 否 | 回调函数。返回当前组件（EmbeddedComponent或UIExtensionComponent）矩形变化值及变化原因。如果传入参数，则关闭该监听。如果未传入参数，则关闭所有组件（EmbeddedComponent或UIExtensionComponent）矩形变化的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. // ExtensionProvider.ts
2. import { EmbeddedUIExtensionAbility, UIExtensionContentSession } from '@kit.AbilityKit';

4. export default class EntryAbility extends EmbeddedUIExtensionAbility {
5. onSessionDestroy(session: UIExtensionContentSession) {
6. const extensionWindow = session.getUIExtensionWindowProxy();
7. // 注销组件（EmbeddedComponent或UIExtensionComponent）位置及尺寸变化的监听
8. extensionWindow.off('rectChange');
9. }
10. }
```

### createSubWindowWithOptions

PhonePC/2in1TabletTVWearable

createSubWindowWithOptions(name: string, subWindowOptions: window.SubWindowOptions): Promise<window.Window>

创建该WindowProxy实例下的子窗口，使用Promise异步回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**设备行为差异：** 当[subWindowOptions](arkts-apis-window-i.md#subwindowoptions11)中isModal为true且[modalityType](arkts-apis-window-e.md#modalitytype14)为APPLICATION\_MODALITY时，该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备及不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上调用返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 子窗口的名字。 |
| subWindowOptions | [window.SubWindowOptions](arkts-apis-window-i.md#subwindowoptions11) | 是 | 子窗口参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[window.Window](arkts-apis-window-window.md)> | Promise对象。返回当前WindowProxy下创建的子窗口对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible causes: 1. The window is not created or destroyed. 2. Internal task error. |

**示例：**

```
1. // ExtensionProvider.ts
2. import { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
3. import { window } from '@kit.ArkUI';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. export default class EntryAbility extends EmbeddedUIExtensionAbility {
7. onSessionCreate(want: Want, session: UIExtensionContentSession) {
8. const extensionWindow = session.getUIExtensionWindowProxy();
9. const subWindowOpts: window.SubWindowOptions = {
10. title: 'This is a subwindow',
11. decorEnabled: true
12. };
13. // 创建子窗口
14. extensionWindow.createSubWindowWithOptions('subWindowForHost', subWindowOpts)
15. .then((subWindow: window.Window) => {
16. subWindow.setUIContent('pages/Index', (err, data) => {
17. if (err && err.code != 0) {
18. return;
19. }
20. subWindow?.resize(300, 300, (err, data) => {
21. if (err && err.code != 0) {
22. return;
23. }
24. subWindow?.moveWindowTo(100, 100, (err, data) => {
25. if (err && err.code != 0) {
26. return;
27. }
28. subWindow?.showWindow((err, data) => {
29. if (err && err.code == 0) {
30. console.info(`The subwindow has been shown!`);
31. } else {
32. console.error(`Failed to show the subwindow!`);
33. }
34. });
35. });
36. });
37. });
38. }).catch((error: BusinessError) => {
39. console.error(`Create subwindow failed. Cause code: ${error.code}, message: ${error.message}`);
40. })
41. }
42. }
```

### createSubWindowWithOptions23+

PhonePC/2in1TabletTVWearable

createSubWindowWithOptions(name: string, subWindowConfig: window.SubWindowOptions, followCreatorLifecycle: boolean): Promise<window.Window>

创建该WindowProxy实例下的子窗口，可通过设置followCreatorLifecycle，决定子窗是否跟随组件（EmbeddedComponent或UIExtensionComponent）的生命周期，使用Promise异步回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**设备行为差异：** 当[subWindowOptions](arkts-apis-window-i.md#subwindowoptions11)中isModal为true且[modalityType](arkts-apis-window-e.md#modalitytype14)为APPLICATION\_MODALITY时，该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备及不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上调用返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 子窗口的名字。 |
| subWindowConfig | [window.SubWindowOptions](arkts-apis-window-i.md#subwindowoptions11) | 是 | 子窗口参数。 |
| followCreatorLifecycle | boolean | 是 | 子窗生命周期是否跟组件（EmbeddedComponent或UIExtensionComponent）保持同步。true表示该组件隐藏时，子窗隐藏，该组件显示时子窗显示，false表示子窗的显隐不跟随该组件变化。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[window.Window](arkts-apis-window-window.md)> | Promise对象。返回当前WindowProxy下创建的子窗口对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |

**示例：**

```
1. // ExtensionProvider.ts
2. import { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
3. import { window } from '@kit.ArkUI';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. export default class EntryAbility extends EmbeddedUIExtensionAbility {
7. onSessionCreate(want: Want, session: UIExtensionContentSession) {
8. const extensionWindow = session.getUIExtensionWindowProxy();
9. const subWindowConfig: window.SubWindowOptions = {
10. title: 'This is a subwindow',
11. decorEnabled: true
12. };
13. // 创建子窗口
14. extensionWindow.createSubWindowWithOptions('subWindowForHost', subWindowConfig, true)
15. .then((subWindow: window.Window) => {
16. subWindow.setUIContent('pages/Index', (err, data) => {
17. if (err && err.code != 0) {
18. return;
19. }
20. subWindow?.resize(300, 300, (err, data) => {
21. if (err && err.code != 0) {
22. return;
23. }
24. subWindow?.moveWindowTo(100, 100, (err, data) => {
25. if (err && err.code != 0) {
26. return;
27. }
28. subWindow?.showWindow((err, data) => {
29. if (err && err.code == 0) {
30. console.info(`The subwindow has been shown!`);
31. } else {
32. console.error(`Failed to show the subwindow!`);
33. }
34. });
35. });
36. });
37. });
38. }).catch((error: BusinessError) => {
39. console.error(`Create subwindow failed. Cause code: ${error.code}, message: ${error.message}`);
40. })
41. }
42. }
```

### occupyEvents18+

PhonePC/2in1TabletTVWearable

occupyEvents(eventFlags: number): Promise<void>

设置组件（EmbeddedComponent或UIExtensionComponent）占用事件，宿主将不响应组件区域内被占用的事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventFlags | number | 是 | 占用的事件类型，具体取值可见[EventFlag](js-apis-arkui-uiextension.md#eventflag18)枚举值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed. 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. // ExtensionProvider.ts
2. import { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
3. import { uiExtension } from '@kit.ArkUI';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. export default class EntryAbility extends EmbeddedUIExtensionAbility {
7. onSessionCreate(want: Want, session: UIExtensionContentSession) {
8. const extensionWindow = session.getUIExtensionWindowProxy();
9. // 占用事件
10. setTimeout(() => {
11. try {
12. let promise =
13. extensionWindow.occupyEvents(uiExtension.EventFlag.EVENT_CLICK | uiExtension.EventFlag.EVENT_LONG_PRESS);
14. promise.then(() => {
15. console.info(`Succeeded in occupying events`);
16. }).catch((err: BusinessError) => {
17. console.error(`Failed to occupy events. Cause code: ${err.code}, message: ${err.message}`);
18. });
19. } catch (e) {
20. console.error(`Occupy events got exception code: ${e.code}, message: ${e.message}`);
21. }
22. }, 500);
23. }
24. }
```

## EventFlag18+

PhonePC/2in1TabletTVWearable

事件类型枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EVENT\_NONE | 0x00000000 | 无事件。 |
| EVENT\_PAN\_GESTURE\_LEFT | 0x00000001 | 左滑事件。 |
| EVENT\_PAN\_GESTURE\_RIGHT | 0x00000002 | 右滑事件。 |
| EVENT\_PAN\_GESTURE\_UP | 0x00000004 | 上滑事件。 |
| EVENT\_PAN\_GESTURE\_DOWN | 0x00000008 | 下滑事件。 |
| EVENT\_CLICK | 0x00000100 | 点击事件。 |
| EVENT\_LONG\_PRESS | 0x00000200 | 长按事件。 |

## AvoidAreaInfo

PhonePC/2in1TabletTVWearable

用于表示窗口避让区的信息。

**系统能力**：SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [window.AvoidAreaType](arkts-apis-window-e.md#avoidareatype7) | 否 | 否 | 窗口避让区类型。 |
| area | [window.AvoidArea](arkts-apis-window-i.md#avoidarea7) | 否 | 否 | 窗口内容避让区域。 |

## WindowProxyProperties14+

PhonePC/2in1TabletTVWearable

用于表示组件的相关信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uiExtensionHostWindowProxyRect | [window.Rect](arkts-apis-window-i.md#rect7) | 否 | 否 | 组件（EmbeddedComponent或UIExtensionComponent）的位置和宽高。 |

## RectChangeReason14+

PhonePC/2in1TabletTVWearable

组件（EmbeddedComponent或UIExtensionComponent）矩形（位置及尺寸）变化的原因。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| HOST\_WINDOW\_RECT\_CHANGE | 0x0001 | 组件所在的宿主窗口矩形变化。 |

## RectChangeOptions14+

PhonePC/2in1TabletTVWearable

组件（EmbeddedComponent或UIExtensionComponent）矩形（位置及尺寸）变化返回的值及变化原因。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| rect | [window.Rect](arkts-apis-window-i.md#rect7) | 否 | 否 | 组件矩形变化后的值。 |
| reason | [RectChangeReason](js-apis-arkui-uiextension.md#rectchangereason14) | 否 | 否 | 组件矩形变化的原因。 |

## 完整示例

PhonePC/2in1TabletTVWearable

本示例展示文档中所有API在[EmbeddedUIExtensionAbility](../harmonyos-guides/embeddeduiextensionability.md)中的基础使用方式，示例应用的bundleName为"com.example.embeddeddemo"，被拉起的EmbeddedUIExtensionAbility为"ExampleEmbeddedAbility"。

* 示例应用中的EntryAbility(UIAbility)加载首页文件：pages/Index.ets，其中内容如下：

```
1. // pages/Index.ets -- UIAbility启动时加载此页面
2. import { Want } from '@kit.AbilityKit';

4. @Entry
5. @Component
6. struct Index {
7. @State message: string = 'Message: ';
8. private want: Want = {
9. bundleName: "com.example.embeddeddemo",
10. abilityName: "ExampleEmbeddedAbility",
11. }

13. build() {
14. Row() {
15. Column() {
16. Text(this.message).fontSize(30)
17. EmbeddedComponent(this.want, EmbeddedType.EMBEDDED_UI_EXTENSION)
18. .width('100%')
19. .height('90%')
20. .onTerminated((info) => {
21. this.message = 'Termination: code = ' + info.code + ', want = ' + JSON.stringify(info.want);
22. })
23. .onError((error) => {
24. this.message = 'Error: code = ' + error.code;
25. })
26. }
27. .width('100%')
28. }
29. .height('100%')
30. }
31. }
```

* EmbeddedComponent拉起的EmbeddedUIExtensionAbility在ets/extensionAbility/ExampleEmbeddedAbility文件中实现，内容如下：

```
1. import { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';

3. const TAG: string = '[ExampleEmbeddedAbility]';

5. export default class ExampleEmbeddedAbility extends EmbeddedUIExtensionAbility {
6. onCreate() {
7. console.info(TAG, `onCreate`);
8. }

10. onForeground() {
11. console.info(TAG, `onForeground`);
12. }

14. onBackground() {
15. console.info(TAG, `onBackground`);
16. }

18. onDestroy() {
19. console.info(TAG, `onDestroy`);
20. }

22. onSessionCreate(want: Want, session: UIExtensionContentSession) {
23. console.info(TAG, `onSessionCreate, want: ${JSON.stringify(want)}`);
24. let param: Record<string, UIExtensionContentSession> = {
25. 'session': session
26. };
27. let storage: LocalStorage = new LocalStorage(param);
28. session.loadContent('pages/extension', storage);
29. }
30. }
```

* EmbeddedUIExtensionAbility的入口页面文件pages/extension.ets内容如下：

```
1. import { UIExtensionContentSession } from '@kit.AbilityKit';
2. import { uiExtension, window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry()
6. @Component
7. struct Extension {
8. @State message: string = 'EmbeddedUIExtensionAbility Index';
9. private storage: LocalStorage | undefined = this.getUIContext()?.getSharedLocalStorage();
10. private session: UIExtensionContentSession | undefined = this.storage?.get<UIExtensionContentSession>('session');
11. private extensionWindow: uiExtension.WindowProxy | undefined = this.session?.getUIExtensionWindowProxy();
12. private subWindow: window.Window | undefined = undefined;

14. aboutToAppear(): void {
15. this.extensionWindow?.on('windowSizeChange', (size: window.Size) => {
16. console.info(`size = ${JSON.stringify(size)}`);
17. });
18. this.extensionWindow?.on('rectChange', uiExtension.RectChangeReason.HOST_WINDOW_RECT_CHANGE,
19. (data: uiExtension.RectChangeOptions) => {
20. console.info('Succeeded window rect changes. Data: ' + JSON.stringify(data));
21. });
22. this.extensionWindow?.on('avoidAreaChange', (info: uiExtension.AvoidAreaInfo) => {
23. console.info(`type = ${JSON.stringify(info.type)}, area = ${JSON.stringify(info.area)}`);
24. });
25. }

27. aboutToDisappear(): void {
28. this.extensionWindow?.off('windowSizeChange');
29. this.extensionWindow?.off('rectChange');
30. this.extensionWindow?.off('avoidAreaChange');
31. }

33. build() {
34. Column() {
35. Text(this.message)
36. .fontSize(20)
37. .fontWeight(FontWeight.Bold)
38. Button("获取组件大小").width('90%').margin({ top: 5, bottom: 5 }).fontSize(16).onClick(() => {
39. let rect = this.extensionWindow?.properties.uiExtensionHostWindowProxyRect;
40. console.info(`EmbeddedComponent的位置和尺寸信息: ${JSON.stringify(rect)}`);
41. })
42. Button("获取系统避让区信息").width('90%').margin({ top: 5, bottom: 5 }).fontSize(16).onClick(() => {
43. let avoidArea: window.AvoidArea | undefined =
44. this.extensionWindow?.getWindowAvoidArea(window.AvoidAreaType.TYPE_SYSTEM);
45. console.info(`系统避让区: ${JSON.stringify(avoidArea)}`);
46. })
47. Button("创建子窗口").width('90%').margin({ top: 5, bottom: 5 }).fontSize(16).onClick(() => {
48. let subWindowOpts: window.SubWindowOptions = {
49. 'title': 'This is a subwindow',
50. decorEnabled: true
51. };
52. this.extensionWindow?.createSubWindowWithOptions('subWindowForHost', subWindowOpts)
53. .then((subWindow: window.Window) => {
54. this.subWindow = subWindow;
55. this.subWindow.loadContent('pages/Index', this.storage, (err, data) => {
56. if (err && err.code != 0) {
57. return;
58. }
59. this.subWindow?.resize(300, 300, (err, data) => {
60. if (err && err.code != 0) {
61. return;
62. }
63. this.subWindow?.moveWindowTo(100, 100, (err, data) => {
64. if (err && err.code != 0) {
65. return;
66. }
67. this.subWindow?.showWindow((err, data) => {
68. if (err && err.code == 0) {
69. console.info(`The subwindow has been shown!`);
70. } else {
71. console.error(`Failed to show the subwindow!`);
72. }
73. });
74. });
75. });
76. });
77. }).catch((error: BusinessError) => {
78. console.error(`Create subwindow failed. Cause code: ${error.code}, message: ${error.message}`);
79. })
80. })
81. }.width('100%').height('100%')
82. }
83. }
```

* 最后，示例应用的module.json5中的"extensionAbilities"中需要增加一项，具体内容如下：

  ```
  1. {
  2. "name": "ExampleEmbeddedAbility",
  3. "srcEntry": "./ets/extensionAbility/ExampleEmbeddedAbility.ets",
  4. "type": "embeddedUI"
  5. }
  ```
