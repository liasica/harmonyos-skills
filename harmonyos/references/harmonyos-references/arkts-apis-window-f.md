---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-f
title: Functions
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > 窗口管理 > @ohos.window (窗口) > Functions
category: harmonyos-references
scraped_at: 2026-04-28T08:00:43+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:8e1021d7acae2e3faed3d033740e504a5d94633aca5fd44fbea91e804ac3eef0
---

说明

* 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 针对系统能力SystemCapability.Window.SessionManager，请先使用[canIUse()](js-apis-syscap.md#caniuse)接口判断当前设备是否支持此syscap及对应接口。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { window } from '@kit.ArkUI';
```

## window.createWindow9+

PhonePC/2in1TabletTVWearable

createWindow(config: Configuration, callback: AsyncCallback<Window>): void

创建子窗口或者系统窗口，使用callback异步回调。

非[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态下，子窗口创建后默认是[沉浸式布局](../harmonyos-guides/window-terminology.md#沉浸式布局)。

自由窗口状态下，子窗口参数[decorEnabled](arkts-apis-window-i.md#configuration9)为false时，子窗口创建后为沉浸式布局；子窗口参数decorEnabled为true，子窗口创建后为非沉浸式布局。

**需要权限：** ohos.permission.SYSTEM\_FLOAT\_WINDOW（仅当创建窗口类型为window.WindowType.TYPE\_FLOAT时需要申请）

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [Configuration](arkts-apis-window-i.md#configuration9) | 是 | 创建窗口时的参数。 |
| callback | AsyncCallback<[Window](arkts-apis-window-window.md)> | 是 | 回调函数。返回当前创建的窗口对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. createWindow can not work correctly due to limited device capabilities. |
| 1300001 | Repeated operation. Possible cause: The window has been created and can not be created again. |
| 1300002 | This window state is abnormal. Possible cause: Invalid parent window type, parent window cannot be a subWindow. |
| 1300004 | Unauthorized operation. Possible cause: The window type in the configuration is invalid. |
| 1300006 | This window context is abnormal. |
| 1300009 | The parent window is invalid. |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class EntryAbility extends UIAbility {
6. onWindowStageCreate(windowStage: window.WindowStage): void {
7. let windowClass: window.Window | undefined = undefined;
8. let config: window.Configuration = {
9. name: "test",
10. windowType: window.WindowType.TYPE_DIALOG,
11. ctx: this.context
12. };
13. try {
14. window.createWindow(config, (err: BusinessError, data) => {
15. const errCode: number = err.code;
16. if (errCode) {
17. console.error(`Failed to create the window. Cause code: ${err.code}, message: ${err.message}`);
18. return;
19. }
20. windowClass = data;
21. console.info('Succeeded in creating the window. Data: ' + JSON.stringify(data));
22. windowClass.resize(500, 1000);
23. });
24. } catch (exception) {
25. console.error(`Failed to create the window. Cause code: ${exception.code}, message: ${exception.message}`);
26. }
27. }
28. }
```

## window.createWindow9+

PhonePC/2in1TabletTVWearable

createWindow(config: Configuration): Promise<Window>

创建子窗口或者系统窗口，使用Promise异步回调。

非[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态下，子窗口创建后默认是[沉浸式布局](../harmonyos-guides/window-terminology.md#沉浸式布局)。

自由窗口状态下，子窗口参数[decorEnabled](arkts-apis-window-i.md#configuration9)为false时，子窗口创建后为沉浸式布局；子窗口参数decorEnabled为true，子窗口创建后为非沉浸式布局。

**需要权限：** ohos.permission.SYSTEM\_FLOAT\_WINDOW（仅当创建窗口类型为window.WindowType.TYPE\_FLOAT时需要申请）

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [Configuration](arkts-apis-window-i.md#configuration9) | 是 | 创建窗口时的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Window](arkts-apis-window-window.md)> | Promise对象。返回当前创建的窗口对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. createWindow can not work correctly due to limited device capabilities. |
| 1300001 | Repeated operation. Possible cause: The window has been created and can not be created again. |
| 1300002 | This window state is abnormal. Possible cause: Invalid parent window type, parent window cannot be a subWindow. |
| 1300004 | Unauthorized operation. Possible cause: The window type in the configuration is invalid. |
| 1300006 | This window context is abnormal. |
| 1300009 | The parent window is invalid. |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class EntryAbility extends UIAbility {
6. onWindowStageCreate(windowStage: window.WindowStage): void {
7. let windowClass: window.Window | undefined = undefined;
8. let config: window.Configuration = {
9. name: "test",
10. windowType: window.WindowType.TYPE_DIALOG,
11. ctx: this.context
12. };
13. try {
14. window.createWindow(config).then((value:window.Window) => {
15. console.info('Succeeded in creating the window. Data: ' + JSON.stringify(value));
16. windowClass = value;
17. windowClass.resize(500, 1000);
18. }).catch((err:BusinessError)=> {
19. console.error(`Failed to create the window. Cause code: ${err.code}, message: ${err.message}`);
20. });
21. } catch (exception) {
22. console.error(`Failed to create the window. Cause code: ${exception.code}, message: ${exception.message}`);
23. }
24. }
25. }
```

## window.findWindow9+

PhonePC/2in1TabletTVWearable

findWindow(name: string): Window

查找指定名称对应的窗口。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 窗口名称。查找子窗口或系统窗口时使用[Configuration](arkts-apis-window-i.md#configuration9)中的窗口名称；查找主窗口时使用[getWindowName](arkts-apis-uicontext-uicontext.md#getwindowname12)获取当前实例的窗口名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Window](arkts-apis-window-window.md) | 当前查找的窗口对象。如果查找指定名称对应的窗口不存在，则返回对象为空。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```
1. let windowClass: window.Window | undefined = undefined;
2. try {
3. windowClass = window.findWindow('test');
4. } catch (exception) {
5. console.error(`Failed to find the Window. Cause code: ${exception.code}, message: ${exception.message}`);
6. }
```

## window.getLastWindow9+

PhonePC/2in1TabletTVWearable

getLastWindow(ctx: BaseContext, callback: AsyncCallback<Window>): void

获取当前应用内层级最高的子窗口，使用callback异步回调。

若无应用子窗口或子窗口未调用[showWindow()](arkts-apis-window-window.md#showwindow9)进行显示，则返回应用主窗口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ctx | [BaseContext](js-apis-inner-application-basecontext.md) | 是 | 当前应用上下文信息。 |
| callback | AsyncCallback<[Window](arkts-apis-window-window.md)> | 是 | 回调函数。返回当前应用内层级最高的窗口对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. Possible cause: 1. Top window or main window is null or destroyed; 2. This window context is abnormal. |
| 1300006 | This window context is abnormal. |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class EntryAbility extends UIAbility {
6. // ...
7. onWindowStageCreate(windowStage: window.WindowStage): void {
8. console.info('onWindowStageCreate');
9. let windowClass: window.Window | undefined = undefined;
10. windowStage.loadContent('pages/Index', (err: BusinessError) => {
11. if (err.code) {
12. console.error(`Failed to load content for main window. Cause code: ${err.code}, message: ${err.message}`);
13. }
14. windowStage.createSubWindow('TestSubWindow').then((subWindow) => {
15. let storage: LocalStorage = new LocalStorage();
16. subWindow.loadContent('pages/Index', storage, (err: BusinessError) => {
17. if (err.code) {
18. console.error(`Failed to load content for sub window. Cause code: ${err.code}, message: ${err.message}`);
19. }
20. subWindow.showWindow().then(() => {
21. try {
22. window.getLastWindow(this.context, (err: BusinessError, data) => {
23. const errCode: number = err.code;
24. if (errCode) {
25. console.error(`Failed to obtain the top window. Cause code: ${err.code}, message: ${err.message}`);
26. return;
27. }
28. windowClass = data;
29. console.info(`Succeeded in obtaining the top window. Window id: ${windowClass.getWindowProperties().id}`);
30. });
31. } catch (exception) {
32. console.error(`Failed to obtain the top window. Cause code: ${exception.code}, message: ${exception.message}`);
33. }
34. });
35. });
36. });
37. });
38. }
39. // ...
40. }
```

## window.getLastWindow9+

PhonePC/2in1TabletTVWearable

getLastWindow(ctx: BaseContext): Promise<Window>

获取当前应用内层级最高的子窗口，使用Promise异步回调。

若无应用子窗口或子窗口未调用[showWindow()](arkts-apis-window-window.md#showwindow9)进行显示，则返回应用主窗口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ctx | [BaseContext](js-apis-inner-application-basecontext.md) | 是 | 当前应用上下文信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Window](arkts-apis-window-window.md)> | Promise对象。返回当前应用内层级最高的窗口对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. Possible cause: 1. Top window or main window is null or destroyed; 2. This window context is abnormal. |
| 1300006 | This window context is abnormal. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { window } from '@kit.ArkUI';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. export default class EntryAbility extends UIAbility {
7. // ...
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. console.info('onWindowStageCreate');
10. let windowClass: window.Window | undefined = undefined;
11. windowStage.loadContent('pages/Index', (err: BusinessError) => {
12. if (err.code) {
13. console.error(`Failed to load content for main window. Cause code: ${err.code}, message: ${err.message}`);
14. }
15. windowStage.createSubWindow('TestSubWindow').then((subWindow) => {
16. let storage: LocalStorage = new LocalStorage();
17. subWindow.loadContent('pages/Index', storage, (err: BusinessError) => {
18. if (err.code) {
19. console.error(`Failed to load content for sub window. Cause code: ${err.code}, message: ${err.message}`);
20. }
21. subWindow.showWindow().then(() => {
22. try {
23. window.getLastWindow(this.context).then((topWindow) => {
24. windowClass = topWindow;
25. console.info(`Succeeded in obtaining the top window. Window id: ${topWindow.getWindowProperties().id}`);
26. }).catch((err: BusinessError) => {
27. console.error(`Failed to obtain the top window. Cause code: ${err.code}, message: ${err.message}`);
28. });
29. } catch (exception) {
30. console.error(`Failed to obtain the top window. Cause code: ${exception.code}, message: ${exception.message}`);
31. }
32. });
33. });
34. });
35. });
36. }
37. // ...
38. }
```

## window.shiftAppWindowFocus11+

PhonePC/2in1TabletTVWearable

shiftAppWindowFocus(sourceWindowId: number, targetWindowId: number): Promise<void>

在同应用内将窗口焦点从源窗口转移到目标窗口，仅支持应用主窗、子窗范围内的焦点转移。使用Promise异步回调。

目标窗口需确保具有获得焦点的能力（可通过[setWindowFocusable()](arkts-apis-window-window.md#setwindowfocusable9)设置），并确保调用[showWindow()](arkts-apis-window-window.md#showwindow9)成功且执行完毕。

说明

在调用shiftAppWindowFocus()前，建议确保目标窗口已调用[loadContent()](arkts-apis-window-window.md#loadcontent9)或[setUIContent()](arkts-apis-window-window.md#setuicontent9)并生效，否则可能会导致不可见窗口获取焦点，造成功能异常或影响用户体验。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sourceWindowId | number | 是 | 源窗口id，必须是获焦状态。推荐使用[getWindowProperties()](arkts-apis-window-window.md#getwindowproperties9)方法获取窗口id属性。 |
| targetWindowId | number | 是 | 目标窗口id。推荐使用[getWindowProperties()](arkts-apis-window-window.md#getwindowproperties9)方法获取窗口id属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. Possible cause: 1. Invalid window type. Only main windows and subwindows are supported. 2. The two windows are not from the same process. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { window } from '@kit.ArkUI';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. export default class EntryAbility extends UIAbility {
7. onWindowStageCreate(windowStage: window.WindowStage) {
8. // ...
9. console.info('onWindowStageCreate');
10. let mainWindow: window.Window | undefined = undefined;
11. let subWindow: window.Window | undefined = undefined;
12. let mainWindowId: number = -1;
13. let subWindowId: number = -1;

15. try {
16. windowStage.loadContent('pages/Index', (err) => {
17. if (err.code) {
18. console.error(`Failed to load content for main window. Cause code: ${err.code}, message: ${err.message}`);
19. }
20. // 获取应用主窗及ID
21. windowStage.getMainWindow().then((data) => {
22. if (data == null) {
23. console.error('Failed to obtain the main window. Cause: The data is empty');
24. return;
25. }
26. mainWindow = data;
27. mainWindowId = mainWindow.getWindowProperties().id;
28. console.info('Succeeded in obtaining the main window');
29. }).catch((err: BusinessError) => {
30. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
31. });

33. // 创建或获取子窗及ID，此时子窗口获焦
34. windowStage.createSubWindow('testSubWindow').then((data) => {
35. if (data == null) {
36. console.error('Failed to obtain the sub window. Cause: The data is empty');
37. return;
38. }
39. subWindow = data;
40. subWindowId = subWindow.getWindowProperties().id;
41. subWindow.resize(500, 500);
42. subWindow.setUIContent('pages/Index');
43. subWindow.showWindow();

45. // 监听Window状态，确保已经就绪
46. subWindow.on("windowEvent", (windowEvent) => {
47. if (windowEvent == window.WindowEventType.WINDOW_ACTIVE) {
48. // 切换焦点
49. window.shiftAppWindowFocus(subWindowId, mainWindowId).then(() => {
50. console.info('Succeeded in shifting app window focus');
51. }).catch((err: BusinessError) => {
52. console.error(`Failed to shift app window focus. Cause code: ${err.code}, message: ${err.message}`);
53. });
54. }
55. });
56. });
57. });
58. } catch (exception) {
59. console.error(`Failed to shift app focus. Cause code: ${exception.code}, message: ${exception.message}`);
60. }
61. }
62. }
```

## window.shiftAppWindowPointerEvent15+

PhonePC/2in1TabletTVWearable

shiftAppWindowPointerEvent(sourceWindowId: number, targetWindowId: number): Promise<void>

主窗口和子窗口可正常调用，用于将鼠标输入事件从源窗口转移到目标窗口。使用Promise异步回调。

源窗口仅在[onTouch](ts-universal-events-touch.md#ontouch)事件（事件类型必须为TouchType.Down）的回调方法中调用此接口才会有鼠标输入事件转移效果，成功调用此接口后，系统会向源窗口补发鼠标按键抬起（TouchType.Up）事件，并且向目标窗口补发鼠标按键按下（TouchType.Down）事件。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备及不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上调用返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sourceWindowId | number | 是 | 源窗口id。推荐使用[getWindowProperties()](arkts-apis-window-window.md#getwindowproperties9)方法获取窗口id属性。 |
| targetWindowId | number | 是 | 目标窗口id。推荐使用[getWindowProperties()](arkts-apis-window-window.md#getwindowproperties9)方法获取窗口id属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Failed to convert parameter to sourceWindowId; 3. Failed to convert parameter to targetWindowId; 4. Invalid sourceWindowId or targetWindowId. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. SourceWindow cannot find: not created or not belong to current process; 2. TargetWindow cannot find: not created or not belong to current process; 3. Internal task error. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. Possible cause: 1. Invalid window type. Only main windows and subwindows are supported; 2. The two windows are not from the same process. |

**示例：**

```
1. // ets/pages/Index.ets
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. struct Index {
7. build() {
8. Row() {
9. Column() {
10. Blank('160')
11. .color(Color.Blue)
12. .onTouch((event: TouchEvent) => {
13. if (event.type === TouchType.Down) {
14. try {
15. let sourceWindowId = 1;
16. let targetWindowId = 2;
17. let promise = window.shiftAppWindowPointerEvent(sourceWindowId, targetWindowId);
18. promise.then(() => {
19. console.info('Succeeded in shifting app window pointer event');
20. }).catch((err: BusinessError) => {
21. console.error(`Failed to shift app window pointer event. Cause code: ${err.code}, message: ${err.message}`);
22. });
23. } catch (exception) {
24. console.error(`Failed to shift app pointer event. Cause code: ${exception.code}, message: ${exception.message}`);
25. }
26. }
27. })
28. }.width('100%')
29. }.height('100%').width('100%')
30. }
31. }
```

## window.shiftAppWindowTouchEvent20+

PhonePC/2in1TabletTVWearable

shiftAppWindowTouchEvent(sourceWindowId: number, targetWindowId: number, fingerId: number): Promise<void>

主窗口和子窗口可正常调用，用于将触屏输入事件从源窗口转移到目标窗口。使用Promise异步回调。

源窗口仅在[onTouch](ts-universal-events-touch.md#ontouch)事件（事件类型必须为TouchType.Down）的回调方法中调用此接口才会有触屏输入事件转移效果，成功调用此接口后，系统会向源窗口补发触屏抬起（TouchType.Up）事件，并且向目标窗口补发触屏按下（TouchType.Down）事件。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备及不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上调用返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sourceWindowId | number | 是 | 源窗口id。推荐使用[getWindowProperties()](arkts-apis-window-window.md#getwindowproperties9)方法获取窗口id属性。该参数应为大于0的整数，小于等于0时会返回错误码1300016。 |
| targetWindowId | number | 是 | 目标窗口id。推荐使用[getWindowProperties()](arkts-apis-window-window.md#getwindowproperties9)方法获取窗口id属性。该参数应为大于0的整数，小于等于0时会返回错误码1300016。 |
| fingerId | number | 是 | 触屏事件的手指唯一标识符。推荐使用[TouchEvent](ts-universal-events-touch.md#touchevent对象说明)对象中touches属性获取id。该参数应为大于等于0的整数，小于0时会返回错误码1300016。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function shiftAppWindowTouchEvent can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. SourceWindow cannot find: not created or not belong to current process; 2. TargetWindow cannot find: not created or not belong to current process; 3. Internal task error. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. Possible cause: 1. Invalid window type. Only main windows and subwindows are supported; 2. The two windows are not from the same process. |
| 1300016 | Parameter error. Possible cause: 1. Invalid parameter range. |

**示例：**

```
1. // ets/pages/Index.ets
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. struct Index {
7. build() {
8. Row() {
9. Column() {
10. Blank('160')
11. .color(Color.Blue)
12. .onTouch((event: TouchEvent) => {
13. // 源窗口触屏事件类型必须为TouchType.Down
14. if (event.type === TouchType.Down) {
15. try {
16. let sourceWindowId = 1;
17. let targetWindowId = 2;
18. let promise = window.shiftAppWindowTouchEvent(sourceWindowId, targetWindowId, event.touches[0].id);
19. promise.then(() => {
20. console.info(`Succeeded in shifting app window touch event`);
21. }).catch((err: BusinessError) => {
22. console.error(`Failed to shift app window touch event. Cause code: ${err.code}, message: ${err.message}`);
23. });
24. } catch (exception) {
25. console.error(`Failed to shift app touch event. Cause code: ${exception.code}, message: ${exception.message}`);
26. }
27. }
28. })
29. }.width('100%')
30. }.height('100%').width('100%')
31. }
32. }
```

## window.getWindowsByCoordinate14+

PhonePC/2in1TabletTVWearable

getWindowsByCoordinate(displayId: number, windowNumber?: number, x?: number, y?: number): Promise<Array<Window>>

查询本应用指定坐标下的可见窗口（可通过[on('windowVisibilityChange')](arkts-apis-window-window.md#onwindowvisibilitychange11)接口监听）数组，按当前窗口层级排列，层级最高的窗口对应数组下标为0，使用Promise异步回调。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| displayId | number | 是 | 查询窗口所在的displayId，该参数应为整数，传入非整数会忽略掉小数部分，可以在窗口属性[WindowProperties](arkts-apis-window-i.md#windowproperties)中获取。 |
| windowNumber | number | 否 | 查询的窗口数量，该参数应为大于0的整数，传入非整数会忽略掉小数部分，未设置或小于等于0返回所有满足条件的窗口。 |
| x | number | 否 | 查询的x坐标，以屏幕左上角为原点，该参数应为非负整数，传入非整数会忽略掉小数部分，未设置或小于0返回所有可见窗口。 |
| y | number | 否 | 查询的y坐标，以屏幕左上角为原点，该参数应为非负整数，传入非整数会忽略掉小数部分，未设置或小于0返回所有可见窗口。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[Window](arkts-apis-window-window.md)>> | Promise对象。返回获取到的窗口对象数组。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300003 | This window manager service works abnormally. Possible cause: Internal task error. |

```
1. import { window } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { UIAbility } from '@kit.AbilityKit';

5. export default class EntryAbility extends UIAbility {
6. onWindowStageCreate(windowStage: window.WindowStage): void {
7. let windowClass: window.Window | undefined = undefined;
8. try {
9. let displayId = 0;
10. window.getWindowsByCoordinate(displayId, 2, 500, 500).then((data) => {
11. console.info(`Succeeded in getting windows. Data: ${data}`);
12. for (let windowObject of data) {
13. // do something with window
14. windowClass = windowObject;
15. }
16. }).catch((err: BusinessError) => {
17. console.error(`Failed to get window from point. Cause code: ${err.code}, message: ${err.message}`);
18. });
19. } catch (exception) {
20. console.error(`Failed to get window from point. Cause code: ${exception.code}, message: ${exception.message}`);
21. }
22. }
23. }
```

## window.getAllWindowLayoutInfo15+

PhonePC/2in1TabletTVWearable

getAllWindowLayoutInfo(displayId: number): Promise<Array<WindowLayoutInfo>>

获取指定屏幕上可见的窗口布局信息数组，其中返回的每个Rect的宽、高是已经过缩放计算后的值，按当前窗口层级排列，层级最高的对应数组index为0，使用Promise异步回调。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| displayId | number | 是 | 需要获取窗口布局信息的displayId，该参数应为整数，且为当前实际存在屏幕的displayId，可以通过窗口属性[WindowProperties](arkts-apis-window-i.md#windowproperties)获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[WindowLayoutInfo](arkts-apis-window-i.md#windowlayoutinfo15)>> | Promise对象。返回获取到的窗口布局信息对象数组。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. function getAllWindowLayoutInfo can not work correctly due to limited device capabilities. |
| 1300003 | This window manager service works abnormally. Possible cause: Internal task error. |

```
1. import { window } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let displayId = 0;
6. let promise = window.getAllWindowLayoutInfo(displayId);
7. promise.then((data) => {
8. console.info('Succeeded in obtaining all window layout info. Data: ' + JSON.stringify(data));
9. }).catch((err: BusinessError) => {
10. console.error(`Failed to obtain all window layout info. Cause code: ${err.code}, message: ${err.message}`);
11. });
12. } catch (exception) {
13. console.error(`Failed to obtain all window layout info. Cause code: ${exception.code}, message: ${exception.message}`);
14. }
```

## window.getVisibleWindowInfo18+

PhonePC/2in1TabletTVWearable

getVisibleWindowInfo(): Promise<Array<WindowInfo>>

获取当前屏幕的可见主窗口（未退至后台的主窗口）信息。使用Promise异步回调。

**系统能力：** SystemCapability.Window.SessionManager

**需要权限：** ohos.permission.VISIBLE\_WINDOW\_INFO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[WindowInfo](arkts-apis-window-i.md#windowinfo18)>> | Promise对象，返回当前可见窗口的相关信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. Possible cause: Need ohos.permission.VISIBLE\_WINDOW\_INFO permission. |
| 801 | Capability not supported. Function getVisibleWindowInfo can not work correctly due to limited device capabilities. |
| 1300003 | This window manager service works abnormally. Possible cause: Internal task error. |

**示例：**

```
1. import { window } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let promise = window.getVisibleWindowInfo();
6. promise.then((data) => {
7. data.forEach(windowInfo=>{
8. console.info(`left:${windowInfo.rect.left}`);
9. console.info(`top:${windowInfo.rect.top}`);
10. console.info(`width:${windowInfo.rect.width}`);
11. console.info(`height:${windowInfo.rect.height}`);
12. console.info(`windowId:${windowInfo.windowId}`);
13. console.info(`windowStatusType:${windowInfo.windowStatusType}`);
14. console.info(`abilityName:${windowInfo.abilityName}`);
15. console.info(`bundleName:${windowInfo.bundleName}`);
16. console.info(`isFocused:${windowInfo.isFocused}`);
17. })
18. }).catch((err: BusinessError) => {
19. console.error('Failed to getWindowInfo. Cause: ' + JSON.stringify(err));
20. });
21. } catch (exception) {
22. console.error(`Failed to get visible window info. Cause code: ${exception.code}, message: ${exception.message}`);
23. }
```

## window.getGlobalWindowMode20+

PhonePC/2in1TabletTVWearable

getGlobalWindowMode(displayId?: number): Promise<number>

获取指定屏幕上生命周期位于前台的窗口对应的窗口模式，使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| displayId | number | 否 | 可选的屏幕ID，用于获取对应屏幕上的窗口模式信息。该参数应为大于等于0的整数，小于0时会返回错误码1300016，不传或传值为null以及undefined则代表查询所有屏幕，传入非整数会忽略掉小数部分。如果指定的屏幕不存在，返回值为0，推荐使用[getWindowProperties()](arkts-apis-window-window.md#getwindowproperties9)方法获取窗口所在屏幕ID属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回获取到的窗口模式。每一个二进制位代表一种窗口模式，当前支持的窗口模式见[GlobalWindowMode](arkts-apis-window-e.md#globalwindowmode20)，返回值为对应窗口模式值按位进行或运算的结果。比如，当前屏幕上存在全屏窗口、悬浮窗和画中画三种窗口，则返回值为0b1|0b100|0b1000 = 13。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. function getGlobalWindowMode can not work correctly due to limited device capabilities. |
| 1300003 | This window manager service works abnormally. Possible cause: Internal task error. |
| 1300016 | Parameter error. Possible cause: 1. Invalid parameter range; 2. The parameter format is incorrect. |

**示例：**

```
1. import { window } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let displayId = 0;
6. let promise = window.getGlobalWindowMode(displayId);
7. promise.then((data) => {
8. console.info(`Succeeded in obtaining global window mode. Data: ${data}`);
9. }).catch((err: BusinessError) => {
10. console.error(`Failed to obtain global window mode. Cause code: ${err.code}, message: ${err.message}`);
11. });
12. } catch (exception) {
13. console.error(`Failed to obtain global window mode. Cause code: ${exception.code}, message: ${exception.message}`);
14. }
```

## window.setWatermarkImageForAppWindows21+

PhonePC/2in1TabletTVWearable

setWatermarkImageForAppWindows(pixelMap: image.PixelMap | undefined): Promise<void>

设置或取消本应用进程下窗口的水印图片，使用Promise异步回调。该接口需要在[loadContent()](arkts-apis-window-window.md#loadcontent9)或[setUIContent()](arkts-apis-window-window.md#setuicontent9)调用生效后使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pixelMap | [image.PixelMap](arkts-apis-image-pixelmap.md) | undefined | 是 | 传入image.PixelMap表示设置水印图片，传入undefined表示取消水印显示。  如果图片尺寸的宽和高同时超过窗口尺寸以及屏幕尺寸的宽和高，返回错误码1300016。  如果图片尺寸的宽或高超过窗口尺寸的宽或高，超出窗口宽或高的部分会被裁剪。  如果图片尺寸的宽或高小于窗口尺寸的宽或高，小于的部分会自动重复补充。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码 ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function setWatermarkImageForAppWindows can not to work correctly due to limited device capabilities. |
| 1300003 | This window manager service works abnormally. |
| 1300016 | Parameter error. Possible cause: 1. Invalid parameter range. |

**示例：**

```
1. import { image } from "@kit.ImageKit";
2. import { BusinessError } from "@kit.BasicServicesKit";

4. let color: ArrayBuffer = new ArrayBuffer(96);
5. let initializationOptions: image.InitializationOptions = {
6. editable: true,
7. pixelFormat: image.PixelMapFormat.RGBA_8888,
8. size: {
9. height: 4,
10. width: 6,
11. },
12. };
13. image.createPixelMap(color, initializationOptions).then((pixelMap: image.PixelMap) => {
14. console.info("Succeeded in creating pixelmap.");
15. try {
16. let promise = window.setWatermarkImageForAppWindows(pixelMap);
17. promise.then(() => {
18. console.info("Succeeded in setting watermark image.");
19. }).catch((err: BusinessError) => {
20. console.error(`Failed to set watermark image. Cause code: ${err.code}, message: ${err.message}`);
21. });
22. } catch (exception) {
23. console.error(`Failed to set watermark image. Exception code: ${exception.code}, message: ${exception.message}`);
24. }
25. }).catch((err: BusinessError) => {
26. console.error(`Failed to create PixelMap. Cause code: ${err.code}, message: ${err.message}`);
27. });
```

## window.setStartWindowBackgroundColor20+

PhonePC/2in1TabletTVWearable

setStartWindowBackgroundColor(moduleName: string, abilityName: string, color: ColorMetrics): Promise<void>

设置同一应用包名下指定moduleName、abilityName对应UIAbility的启动页背景色，使用Promise异步回调。

该接口对同一应用包名下的所有进程生效，例如多实例或应用分身场景。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleName | string | 是 | 需要设置的UIAbility所属模块名，moduleName的长度范围为0-200字节，仅支持设置当前同一应用包名内的模块。模块名由开发者在[module.json5配置文件](../harmonyos-guides/module-configuration-file.md#配置文件标签)中的name字段指定。 |
| abilityName | string | 是 | 需要设置的UIAbility名字，abilityName的长度范围为0-200字节，仅支持设置当前同一应用包名内的abilityName。UIAbility名由开发者在[module.json5配置文件abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)的name字段指定。 |
| color | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 是 | 设置的启动页背景色。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function setStartWindowBackgroundColor can not to work correctly due to limited device capabilities. |
| 1300003 | This window manager service works abnormally. Possible cause: Internal task error. |
| 1300016 | Parameter error. Possible cause: Parameter exceeds the allowed length. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { ColorMetrics, window } from '@kit.ArkUI';

4. try {
5. let promise = window.setStartWindowBackgroundColor("entry", "EntryAbility", ColorMetrics.numeric(0xff000000));
6. promise.then(() => {
7. console.info('Succeeded in setting the starting window color.');
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to set the starting window color. Cause code: ${err.code}, message: ${err.message}`);
10. });
11. } catch (exception) {
12. console.error(`Failed to set the starting window color. Cause code: ${exception.code}, message: ${exception.message}`);
13. }
```

## window.getAllMainWindowInfo21+

PhonePC/2in1TabletTVWearable

getAllMainWindowInfo(): Promise<Array<MainWindowInfo>>

获取全部主窗口信息，使用Promise异步回调。

**需要权限：** ohos.permission.CUSTOM\_SCREEN\_CAPTURE

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在2in1设备中可正常调用，在其他设备中返回801错误码。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[MainWindowInfo](arkts-apis-window-i.md#mainwindowinfo21)>> | Promise对象。返回主窗口信息列表。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { abilityAccessCtrl, UIAbility, common, Permissions } from '@kit.AbilityKit';

4. export default class EntryAbility extends UIAbility {
5. onWindowStageCreate(windowStage: window.WindowStage): void {
6. console.info('Ability onWindowStageCreate');
7. windowStage.loadContent('pages/Index', (err) => {
8. if (err.code) {
9. console.error(`Failed to load the content. Cause: ${JSON.stringify(err)}`);
10. }
11. reqPermissionsFromUser(permissions, this.context);
12. console.info('Succeeded in loading the content');
13. });
14. try {
15. let windowInfoPromise = window.getAllMainWindowInfo();
16. windowInfoPromise.then((list: Array<window.MainWindowInfo>) => {
17. console.info('Get all main window info success.');
18. }).catch((err: BusinessError) => {
19. console.error(`Get all main window info failed. Error info: ${JSON.stringify(err)}`);
20. });
21. } catch (err) {
22. console.error(`Get all main window info failed. Cause info: ${JSON.stringify(err)}`);
23. }
24. }
25. }

27. const permissions: Array<Permissions> = ['ohos.permission.CUSTOM_SCREEN_CAPTURE'];
28. function reqPermissionsFromUser(permissions: Array<Permissions>, context: common.UIAbilityContext): void {
29. let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
30. atManager.requestPermissionsFromUser(context, permissions).then((data) => {
31. console.info('requestPermissionsFromUser');
32. let grantStatus: Array<number> = data.authResults;
33. let length: number = grantStatus.length;
34. for (let i = 0; i < length; i++) {
35. if (grantStatus[i] === 0) {
36. // 用户授权
37. } else {
38. // 用户拒绝授权
39. return;
40. }
41. }
42. }).catch((err: BusinessError) => {
43. console.error(`Failed to request permission from user. Code is ${err.code}, message is ${err.message}`);
44. })
45. }
```

## window.getMainWindowSnapshot21+

PhonePC/2in1TabletTVWearable

getMainWindowSnapshot(windowId: Array<number>, config: WindowSnapshotConfiguration): Promise<Array<image.PixelMap | undefined>>

获取一个或多个指定windowId的主窗口截图，使用Promise异步回调。

**需要权限：** ohos.permission.CUSTOM\_SCREEN\_CAPTURE

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在2in1设备中可正常调用，在其他设备中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| windowId | Array<number> | 是 | 需要获取截图的主窗口ID列表。可通过[window.getAllMainWindowInfo()](arkts-apis-window-f.md#windowgetallmainwindowinfo21)获取到主窗口windowId。当windowId为null、undefined、小于0、存在重复值或数量超过512个时，返回错误码401；当windowId大于0但不存在对应窗口时，返回undefined。 |
| config | [WindowSnapshotConfiguration](arkts-apis-window-i.md#windowsnapshotconfiguration21) | 是 | 获取窗口截图时的配置信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[image.PixelMap](arkts-apis-image-pixelmap.md) | undefined>> | Promise对象。截图的PixelMap列表，按传入的窗口ID数组的顺序排列。当窗口ID合法但无法找到对应的主窗口时，返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { abilityAccessCtrl, UIAbility, common, Permissions } from '@kit.AbilityKit';
3. import { image } from '@kit.ImageKit';

5. export default class EntryAbility extends UIAbility {
6. onWindowStageCreate(windowStage: window.WindowStage): void {
7. console.info('Ability onWindowStageCreate');
8. windowStage.loadContent('pages/Index', (err) => {
9. if (err.code) {
10. console.error(`Failed to load the content. Cause: JSON.stringify(err)`);
11. }
12. reqPermissionsFromUser(permissions, this.context);
13. console.info('Success in loading the content');
14. });
15. try {
16. let windowIds: number[] = [];
17. let configs: window.WindowSnapshotConfiguration = {
18. useCache: false
19. }
20. let windowInfoPromise = window.getAllMainWindowInfo();
21. windowInfoPromise.then((mainWindowInfoList: Array<window.MainWindowInfo>) => {
22. for (let i = 0; i < mainWindowInfoList.length; i++) {
23. windowIds[i] = mainWindowInfoList[i].windowId;
24. }
25. let promise = window.getMainWindowSnapshot(windowIds, configs);
26. promise.then((list: Array<image.PixelMap | undefined>) => {
27. for (let i = 0; i < list.length; i++) {
28. console.info(`Get main window snapshot, getBytesNumberPerRow: ${list[i]?.getBytesNumberPerRow()}`);
29. }
30. }).catch((err: BusinessError) => {
31. console.error(`Get main window snapshot failed. Error info: ${JSON.stringify(err)}`);
32. });
33. }).catch((err: BusinessError) => {
34. console.error(`Get all main window info failed. Error info: ${JSON.stringify(err)}`);
35. });
36. } catch (err) {
37. console.error(`Get all main window info failed. Cause info: ${JSON.stringify(err)}`);
38. }
39. }
40. }

42. const permissions: Array<Permissions> = ['ohos.permission.CUSTOM_SCREEN_CAPTURE'];
43. function reqPermissionsFromUser(permissions: Array<Permissions>, context: common.UIAbilityContext): void {
44. let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
45. atManager.requestPermissionsFromUser(context, permissions).then((data) => {
46. console.info('requestPermissionsFromUser');
47. let grantStatus: Array<number> = data.authResults;
48. let length: number = grantStatus.length;
49. for (let i = 0; i < length; i++) {
50. if (grantStatus[i] === 0) {
51. // 用户授权
52. } else {
53. // 用户拒绝授权
54. return;
55. }
56. }
57. }).catch((err: BusinessError) => {
58. console.error(`Failed to request permission from user. Code is ${err.code}, message is ${err.message}`);
59. })
60. }
```

## window.create(deprecated)

PhonePC/2in1TabletTVWearable

create(id: string, type: WindowType, callback: AsyncCallback<Window>): void

创建子窗口，使用callback异步回调。

子窗口创建后默认是[沉浸式布局](../harmonyos-guides/window-terminology.md#沉浸式布局)。

说明

从API version 7开始支持，从API version 9开始废弃，参数id传入null或undefined时，可能会导致callback无法得到执行，建议使用[createWindow()](arkts-apis-window-f.md#windowcreatewindow9)替代。

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 窗口名字，即[Configuration](arkts-apis-window-i.md#configuration9)中的name。 |
| type | [WindowType](arkts-apis-window-e.md#windowtype7) | 是 | 窗口类型。 |
| callback | AsyncCallback<[Window](arkts-apis-window-window.md)> | 是 | 回调函数。返回当前创建的子窗口对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let windowClass: window.Window | undefined = undefined;
4. window.create('test', window.WindowType.TYPE_APP, (err: BusinessError, data) => {
5. const errCode: number = err.code;
6. if (errCode) {
7. console.error(`Failed to create the subWindow. Cause code: ${err.code}, message: ${err.message}`);
8. return;
9. }
10. windowClass = data;
11. console.info('Succeeded in creating the subWindow. Data: ' + JSON.stringify(data));
12. });
```

## window.create(deprecated)

PhonePC/2in1TabletTVWearable

create(id: string, type: WindowType): Promise<Window>

创建子窗口，使用Promise异步回调。

子窗口创建后默认是[沉浸式布局](../harmonyos-guides/window-terminology.md#沉浸式布局)。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[createWindow()](arkts-apis-window-f.md#windowcreatewindow9-1)替代。

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 窗口名字，即[Configuration](arkts-apis-window-i.md#configuration9)中的name。 |
| type | [WindowType](arkts-apis-window-e.md#windowtype7) | 是 | 窗口类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Window](arkts-apis-window-window.md)> | Promise对象。返回当前创建的子窗口对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let windowClass: window.Window | undefined = undefined;
4. let promise = window.create('test', window.WindowType.TYPE_APP);
5. promise.then((data) => {
6. windowClass = data;
7. console.info('Succeeded in creating the subWindow. Data: ' + JSON.stringify(data));
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to create the subWindow. Cause code: ${err.code}, message: ${err.message}`);
10. });
```

## window.create(deprecated)

PhonePC/2in1TabletTVWearable

create(ctx: BaseContext, id: string, type: WindowType, callback: AsyncCallback<Window>): void

创建系统窗口，使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[createWindow()](arkts-apis-window-f.md#windowcreatewindow9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ctx | [BaseContext](js-apis-inner-application-basecontext.md) | 是 | 当前应用上下文信息。 |
| id | string | 是 | 窗口名字，即[Configuration](arkts-apis-window-i.md#configuration9)中的name。 |
| type | [WindowType](arkts-apis-window-e.md#windowtype7) | 是 | 窗口类型。 |
| callback | AsyncCallback<[Window](arkts-apis-window-window.md)> | 是 | 回调函数。返回当前创建的子窗口对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let windowClass: window.Window | undefined = undefined;
4. window.create(globalThis.getContext(), 'test', window.WindowType.TYPE_SYSTEM_ALERT, (err: BusinessError, data) => {
5. const errCode: number = err.code;
6. if (errCode) {
7. console.error(`Failed to create the window. Cause code: ${err.code}, message: ${err.message}`);
8. return;
9. }
10. windowClass = data;
11. console.info('Succeeded in creating the window. Data: ' + JSON.stringify(data));
12. windowClass.resetSize(500, 1000);
13. });
```

## window.create(deprecated)

PhonePC/2in1TabletTVWearable

create(ctx: BaseContext, id: string, type: WindowType): Promise<Window>

创建系统窗口，使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[createWindow()](arkts-apis-window-f.md#windowcreatewindow9-1)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ctx | [BaseContext](js-apis-inner-application-basecontext.md) | 是 | 当前应用上下文信息。 |
| id | string | 是 | 窗口名字，即[Configuration](arkts-apis-window-i.md#configuration9)中的name。 |
| type | [WindowType](arkts-apis-window-e.md#windowtype7) | 是 | 窗口类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Window](arkts-apis-window-window.md)> | Promise对象。返回当前创建的子窗口对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let windowClass: window.Window | undefined = undefined;
4. let promise = window.create(globalThis.getContext(), 'test', window.WindowType.TYPE_SYSTEM_ALERT);
5. promise.then((data) => {
6. windowClass = data;
7. console.info('Succeeded in creating the window. Data:' + JSON.stringify(data));
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to create the Window. Cause code: ${err.code}, message: ${err.message}`);
10. });
```

## window.find(deprecated)

PhonePC/2in1TabletTVWearable

find(id: string, callback: AsyncCallback<Window>): void

查找id所对应的窗口，使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[findWindow()](arkts-apis-window-f.md#windowfindwindow9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 窗口名字，即[Configuration](arkts-apis-window-i.md#configuration9)中的name。 |
| callback | AsyncCallback<[Window](arkts-apis-window-window.md)> | 是 | 回调函数。返回当前查找到的窗口对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let windowClass: window.Window | undefined = undefined;
4. window.find('test', (err: BusinessError, data) => {
5. const errCode: number = err.code;
6. if (errCode) {
7. console.error(`Failed to find the Window. Cause code: ${err.code}, message: ${err.message}`);
8. return;
9. }
10. windowClass = data;
11. console.info('Succeeded in finding the window. Data: ' + JSON.stringify(data));
12. });
```

## window.find(deprecated)

PhonePC/2in1TabletTVWearable

find(id: string): Promise<Window>

查找id所对应的窗口，使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[findWindow()](arkts-apis-window-f.md#windowfindwindow9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 窗口名字，即[Configuration](arkts-apis-window-i.md#configuration9)中的name。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Window](arkts-apis-window-window.md)> | Promise对象。返回当前查找的窗口对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let windowClass: window.Window | undefined = undefined;
4. let promise = window.find('test');
5. promise.then((data) => {
6. windowClass = data;
7. console.info('Succeeded in finding the window. Data: ' + JSON.stringify(data));
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to find the Window. Cause code: ${err.code}, message: ${err.message}`);
10. });
```

## window.getTopWindow(deprecated)

PhonePC/2in1TabletTVWearable

getTopWindow(callback: AsyncCallback<Window>): void

获取当前应用内最后显示的窗口，使用callback异步回调。

说明

从API version 6开始支持，从API version 9开始废弃，建议使用[getLastWindow()](arkts-apis-window-f.md#windowgetlastwindow9)替代。

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[Window](arkts-apis-window-window.md)> | 是 | 回调函数。返回当前应用内最后显示的窗口对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let windowClass: window.Window | undefined = undefined;
4. window.getTopWindow((err: BusinessError, data) => {
5. const errCode: number = err.code;
6. if (errCode) {
7. console.error(`Failed to obtain the top window. Cause code: ${err.code}, message: ${err.message}`);
8. return;
9. }
10. windowClass = data;
11. console.info('Succeeded in obtaining the top window. Data: ' + JSON.stringify(data));
12. });
```

## window.getTopWindow(deprecated)

PhonePC/2in1TabletTVWearable

getTopWindow(): Promise<Window>

获取当前应用内最后显示的窗口，使用Promise异步回调。

说明

从API version 6开始支持，从API version 9开始废弃，建议使用[getLastWindow()](arkts-apis-window-f.md#windowgetlastwindow9-1)替代。

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Window](arkts-apis-window-window.md)> | Promise对象。返回当前应用内最后显示的窗口对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let windowClass: window.Window | undefined = undefined;
4. let promise = window.getTopWindow();
5. promise.then((data)=> {
6. windowClass = data;
7. console.info('Succeeded in obtaining the top window. Data: ' + JSON.stringify(data));
8. }).catch((err: BusinessError)=>{
9. console.error(`Failed to obtain the top window. Cause code: ${err.code}, message: ${err.message}`);
10. });
```

## window.getTopWindow(deprecated)

PhonePC/2in1TabletTVWearable

getTopWindow(ctx: BaseContext, callback: AsyncCallback<Window>): void

获取当前应用内最后显示的窗口，使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，参数ctx传入null或undefined时，可能会导致callback无法得到执行，建议使用[getLastWindow()](arkts-apis-window-f.md#windowgetlastwindow9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ctx | [BaseContext](js-apis-inner-application-basecontext.md) | 是 | 当前应用上下文信息。 |
| callback | AsyncCallback<[Window](arkts-apis-window-window.md)> | 是 | 回调函数。返回当前应用内最后显示的窗口对象。 |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class EntryAbility extends UIAbility {
6. onWindowStageCreate(windowStage:window.WindowStage){
7. console.info('onWindowStageCreate');
8. let windowClass: window.Window | undefined = undefined;
9. try {
10. window.getTopWindow(this.context, (err: BusinessError, data) => {
11. const errCode: number = err.code;
12. if(errCode){
13. console.error(`Failed to obtain the top window. Cause code: ${err.code}, message: ${err.message}`);
14. return ;
15. }
16. windowClass = data;
17. console.info('Succeeded in obtaining the top window. Data: ' + JSON.stringify(data));
18. });
19. } catch(error){
20. console.error(`Failed to obtain the top window. Cause code: ${error.code}, message: ${error.message}`);
21. }
22. }
23. }
```

## window.getTopWindow(deprecated)

PhonePC/2in1TabletTVWearable

getTopWindow(ctx: BaseContext): Promise<Window>

获取当前应用内最后显示的窗口，使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[getLastWindow()](arkts-apis-window-f.md#windowgetlastwindow9-1)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ctx | [BaseContext](js-apis-inner-application-basecontext.md) | 是 | 当前应用上下文信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Window](arkts-apis-window-window.md)> | Promise对象。返回当前应用内最后显示的窗口对象。 |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class EntryAbility extends UIAbility {
6. onWindowStageCreate(windowStage:window.WindowStage) {
7. console.info('onWindowStageCreate');
8. let windowClass: window.Window | undefined = undefined;
9. let promise = window.getTopWindow(this.context);
10. promise.then((data) => {
11. windowClass = data;
12. console.info('Succeeded in obtaining the top window. Data: ' + JSON.stringify(data));
13. }).catch((error: BusinessError) => {
14. console.error(`Failed to obtain the top window. Cause code: ${error.code}, message: ${error.message}`);
15. });
16. }
17. }
```
