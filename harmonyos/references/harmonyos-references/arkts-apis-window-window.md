---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window
title: Interface (Window)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > 窗口管理 > @ohos.window (窗口) > Interface (Window)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:47+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:42642be1cb8397e58c2918bfbcaa973cf2c8058716cf0c63d5b9d3a21142892b
---

当前窗口实例，窗口管理器管理的基本单元。

下列API示例中都需先使用[getLastWindow()](arkts-apis-window-f.md#windowgetlastwindow9)、[createWindow()](arkts-apis-window-f.md#windowcreatewindow9)、[findWindow()](arkts-apis-window-f.md#windowfindwindow9)中的任一方法获取到Window实例（windowClass），再通过此实例调用对应方法。

说明

* 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 针对系统能力SystemCapability.Window.SessionManager，请先使用[canIUse()](js-apis-syscap.md#caniuse)接口判断当前设备是否支持此syscap及对应接口。
* 本模块接口被调用时，若出现参数校验失败、权限校验失败、系统状态异常等情况，会抛出错误。建议调用本模块接口时在最外层通过try-catch捕获错误，避免调用失败导致应用崩溃。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { window } from '@kit.ArkUI';
```

## showWindow9+

PhonePC/2in1TabletTVWearable

showWindow(callback: AsyncCallback<void>): void

显示当前窗口，使用callback异步回调，支持系统窗口、应用子窗口、模态窗和全局悬浮窗，或将已显示的应用主窗口层级提升至顶部。

说明

调用该接口前，建议先通过[loadContent](arkts-apis-window-windowstage.md#loadcontent9)方法或者[setUIContent](arkts-apis-window-window.md#setuicontent9-1)方法完成页面加载。如果应用主窗口没有完成页面加载，直接调用该接口，界面会一直显示启动界面；如果系统窗口、应用子窗口、模态窗和全局悬浮窗没有完成页面加载，直接调用该接口，窗口会处于前台，但不可见。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. onWindowStageCreate(windowStage: window.WindowStage): void {
8. console.info('onWindowStageCreate');
9. windowStage.loadContent('pages/Index', (err) => {
10. if (err.code) {
11. console.error('Failed to load the content. Cause: %{public}s', JSON.stringify(err));
12. return;
13. }
14. console.info('Succeeded in loading the content.');
15. try {
16. // 创建子窗
17. windowStage.createSubWindow("testSubWindow").then((subWindow) => {
18. if (subWindow == null) {
19. console.error('Failed to create the subWindow. Cause: The data is empty');
20. return;
21. }
22. subWindow.setUIContent('pages/Index', (err) => {
23. if (err.code) {
24. console.error('Failed to load the subWindow content. Cause: %{public}s', JSON.stringify(err));
25. return;
26. }
27. console.info('Succeeded in loading the subWindow content.');
28. try {
29. subWindow.showWindow((err: BusinessError) => {
30. const errCode: number = err.code;
31. if (errCode) {
32. console.error(`Failed to show the window. Error code: ${err.code}, message: ${err.message}`);
33. return;
34. }
35. console.info('Succeeded in showing the window.');
36. });
37. } catch (exception) {
38. console.error(`Failed to show the window. Cause code: ${exception.code}, message: ${exception.message}`);
39. }
40. })
41. });
42. } catch (exception) {
43. console.error(`Failed to create the sub window. Cause code: ${exception.code}, message: ${exception.message}`);
44. }
45. });
46. }
47. }
```

## showWindow9+

PhonePC/2in1TabletTVWearable

showWindow(): Promise<void>

显示当前窗口，使用Promise异步回调，支持系统窗口、应用子窗口、模态窗和全局悬浮窗，或将已显示的应用主窗口层级提升至顶部。

说明

调用该接口前，建议优先通过[loadContent](arkts-apis-window-windowstage.md#loadcontent9)方法或者[setUIContent](arkts-apis-window-window.md#setuicontent9-1)方法完成页面加载。如果应用主窗口没有完成页面加载，直接调用该接口，界面会一直显示启动界面；如果系统窗口、应用子窗口、模态窗和全局悬浮窗没有完成页面加载，直接调用该接口，窗口会处于前台，但不可见。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. |

**示例：**

```
1. // EntryAbility.ets

3. import { UIAbility } from '@kit.AbilityKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { window } from '@kit.ArkUI';

7. export default class EntryAbility extends UIAbility {
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. console.info('onWindowStageCreate');
10. windowStage.loadContent('pages/Index', (err) => {
11. if (err.code) {
12. console.error('Failed to load the content. Cause: %{public}s', JSON.stringify(err));
13. return;
14. }
15. console.info('Succeeded in loading the content.');
16. try {
17. // 创建子窗
18. windowStage.createSubWindow("testSubWindow").then((subWindow) => {
19. if (subWindow == null) {
20. console.error('Failed to create the subWindow. Cause: The data is empty');
21. return;
22. }
23. subWindow.setUIContent('pages/Index', (err) => {
24. if (err.code) {
25. console.error('Failed to load the subWindow content. Cause: %{public}s', JSON.stringify(err));
26. return;
27. }
28. console.info('Succeeded in loading the subWindow content.');
29. try {
30. let promise = subWindow.showWindow();
31. promise.then(() => {
32. console.info('Succeeded in showing the window.');
33. }).catch((err: BusinessError) => {
34. console.error(`Failed to show the window. Error code: ${err.code}, message: ${err.message}`);
35. });
36. } catch (exception) {
37. console.error(`Failed to show window. Cause code: ${exception.code}, message: ${exception.message}`);
38. }
39. });
40. });
41. } catch (exception) {
42. console.error(`Failed to create the sub window. Cause code: ${exception.code}, message: ${exception.message}`);
43. }
44. });
45. }
46. }
```

## showWindow20+

PhonePC/2in1TabletTVWearable

showWindow(options: ShowWindowOptions): Promise<void>

显示当前窗口或将已显示的应用主窗口的层级提升至顶部，支持传入参数来控制窗口显示的行为，使用Promise异步回调。

仅支持除TYPE\_DIALOG类型的窗口和模态子窗口（即使用setSubWindowModal启用了子窗的模态属性）之外的应用子窗口、应用主窗、全局悬浮窗以及系统窗口。

说明

调用该接口前，建议优先通过[loadContent](arkts-apis-window-windowstage.md#loadcontent9)方法或者[setUIContent](arkts-apis-window-window.md#setuicontent9-1)方法完成页面加载。如果应用主窗口没有完成页面加载，直接调用该接口，界面会一直显示启动界面；如果系统窗口、应用子窗口和全局悬浮窗没有完成页面加载，直接调用该接口，窗口会处于前台，但不可见。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ShowWindowOptions](arkts-apis-window-i.md#showwindowoptions20) | 是 | 显示子窗口或系统窗口时的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function showWindow can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Modal subwindow and dialog window can not set focusOnShow. |
| 1300016 | Parameter validation error. Possible cause: 1. The value of the parameter is out of the allowed range; 2. The length of the parameter exceeds the allowed length; 3. The parameter format is incorrect. |

**示例：**

```
1. // EntryAbility.ets
2. import { window } from '@kit.ArkUI';
3. import { UIAbility } from '@kit.AbilityKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. export default class EntryAbility extends UIAbility {
7. onWindowStageCreate(windowStage: window.WindowStage): void {
8. console.info('onWindowStageCreate');
9. windowStage.loadContent('pages/Index', (err) => {
10. if (err.code) {
11. console.error('Failed to load the content. Cause: %{public}s', JSON.stringify(err));
12. return;
13. }
14. console.info('Succeeded in loading the content.');
15. // 创建子窗
16. try {
17. windowStage.createSubWindow('subWindow').then((data) => {
18. if (data == null) {
19. console.error('Failed to create the subWindow. Cause: The data is empty');
20. return;
21. }
22. data.setUIContent('pages/Index', (err) => {
23. if (err.code) {
24. console.error('Failed to load the subWindow content. Cause: %{public}s', JSON.stringify(err));
25. return;
26. }
27. console.info('Succeeded in loading the subWindow content.');
28. let options: window.ShowWindowOptions = {
29. focusOnShow: false
30. };
31. try {
32. data.showWindow(options).then(() => {
33. console.info('Succeeded in showing window');
34. }).catch((err: BusinessError) => {
35. console.error(`Failed to show window. Error code: ${err.code}, message: ${err.message}`);
36. });
37. } catch (exception) {
38. console.error(`Failed to show window. Cause code: ${exception.code}, message: ${exception.message}`);
39. }
40. });
41. });
42. } catch (exception) {
43. console.error(`Failed to create the sub window. Cause code: ${exception.code}, message: ${exception.message}`);
44. }
45. });
46. }
47. }
```

## destroyWindow9+

PhonePC/2in1TabletTVWearable

destroyWindow(callback: AsyncCallback<void>): void

销毁当前窗口，使用callback异步回调，支持系统窗口及应用子窗口，全局悬浮窗和模态窗。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. windowClass.destroyWindow((err) => {
4. const errCode: number = err.code;
5. if (errCode) {
6. console.error(`Failed to destroy the window. Cause code: ${err.code}, message: ${err.message}`);
7. return;
8. }
9. console.info('Succeeded in destroying the window.');
10. });
```

## destroyWindow9+

PhonePC/2in1TabletTVWearable

destroyWindow(): Promise<void>

销毁当前窗口，使用Promise异步回调，支持系统窗口及应用子窗口，全局悬浮窗和模态窗。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let promise = windowClass.destroyWindow();
4. promise.then(() => {
5. console.info('Succeeded in destroying the window.');
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to destroy the window. Cause code: ${err.code}, message: ${err.message}`);
8. });
```

## moveWindowTo9+

PhonePC/2in1TabletTVWearable

moveWindowTo(x: number, y: number, callback: AsyncCallback<void>): void

移动窗口位置，使用callback异步回调。调用成功即返回，但返回后无法立即获取最终生效结果。如需立即获取，请使用[moveWindowToAsync()](arkts-apis-window-window.md#movewindowtoasync12)。

说明

* 不建议在除自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING，WindowStatusType可通过[getWindowStatus()](arkts-apis-window-window.md#getwindowstatus12)获取）外的其他窗口模式下使用。
* 在[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态下，窗口相对于屏幕左上顶点移动；在非自由窗口状态下，窗口相对于父窗口左上顶点移动。
* 若需在非自由窗口状态下实现相对于屏幕左上顶点的移动，请使用[moveWindowToGlobal()](arkts-apis-window-window.md#movewindowtoglobal15)。
* 该方法对非自由窗口状态下的主窗口无效。
* [自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态下，若主窗口或子窗口的标题栏移出屏幕可视区域，系统将自动回弹窗口，确保标题栏保持可见。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 窗口在x轴方向移动到的坐标位置，单位为px，值为正表示在原点右侧，值为负表示在原点左侧。该参数仅支持整数输入，浮点数输入将向下取整。 |
| y | number | 是 | 窗口在y轴方向移动到的坐标位置，单位为px，值为正表示在原点下方，值为负表示在原点上方。该参数仅支持整数输入，浮点数输入将向下取整。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. windowClass.moveWindowTo(300, 300, (err: BusinessError) => {
5. const errCode: number = err.code;
6. if (errCode) {
7. console.error(`Failed to move the window. Cause code: ${err.code}, message: ${err.message}`);
8. return;
9. }
10. console.info('Succeeded in moving the window.');
11. });
12. } catch (exception) {
13. console.error(`Failed to move the window. Cause code: ${exception.code}, message: ${exception.message}`);
14. }
```

## moveWindowTo9+

PhonePC/2in1TabletTVWearable

moveWindowTo(x: number, y: number): Promise<void>

移动窗口位置，使用Promise异步回调。调用成功即返回，但返回后无法立即获取最终生效结果。如需立即获取，请使用[moveWindowToAsync()](arkts-apis-window-window.md#movewindowtoasync12)。

说明

* 不建议在除自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING，WindowStatusType可通过[getWindowStatus()](arkts-apis-window-window.md#getwindowstatus12)获取）外的其他窗口模式下使用。
* 在[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态下，窗口相对于屏幕左上顶点移动；在非自由窗口状态下，窗口相对于父窗口左上顶点移动。
* 若需在非自由窗口状态下实现相对于屏幕左上顶点的移动，请使用[moveWindowToGlobal()](arkts-apis-window-window.md#movewindowtoglobal15)。
* 该方法对非自由窗口状态下的主窗口无效。
* [自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态下，若主窗口或子窗口的标题栏移出屏幕可视区域，系统将自动回弹窗口，确保标题栏保持可见。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 窗口在x轴方向移动到的坐标位置，单位为px，值为正表示在原点右侧，值为负表示在原点左侧。该参数仅支持整数输入，浮点数输入将向下取整。 |
| y | number | 是 | 窗口在y轴方向移动到的坐标位置，单位为px，值为正表示在原点下方，值为负表示在原点上方。该参数仅支持整数输入，浮点数输入将向下取整。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let promise = windowClass.moveWindowTo(300, 300);
5. promise.then(() => {
6. console.info('Succeeded in moving the window.');
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to move the window. Cause code: ${err.code}, message: ${err.message}`);
9. });
10. } catch (exception) {
11. console.error(`Failed to move the window. Cause code: ${exception.code}, message: ${exception.message}`);
12. }
```

## moveWindowToAsync12+

PhonePC/2in1TabletTVWearable

moveWindowToAsync(x: number, y: number): Promise<void>

移动窗口位置，使用Promise异步回调。调用生效后返回，回调中可使用[getWindowProperties()](arkts-apis-window-window.md#getwindowproperties9)（见示例）立即获取最终生效结果。

该接口仅在窗口为自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING，窗口模式可通过[getWindowStatus()](arkts-apis-window-window.md#getwindowstatus12)获取）时调用生效，在其他窗口模式下调用返回错误码1300010错误码。

在自由悬浮窗口模式下，不同类型窗口的移动行为如下：

| 窗口类型 | [自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态 | 非自由窗口状态 |
| --- | --- | --- |
| 主窗口 | 相对于屏幕移动 | 调用不生效不报错 |
| 应用子窗口/模态窗 | 相对于屏幕移动 | 相对于主窗口移动 |
| 系统窗口/全局悬浮窗 | 相对于屏幕移动 | 相对于屏幕移动 |

说明

* [自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态下，若主窗口或子窗口的标题栏移出屏幕可视区域，系统将自动回弹窗口，确保标题栏保持可见。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 窗口在x轴方向移动到的坐标位置，单位为px，值为正表示位置在x轴右侧；值为负表示位置在x轴左侧；值为0表示位置在x轴坐标原点。该参数仅支持整数输入，浮点数输入将向下取整。 |
| y | number | 是 | 窗口在y轴方向移动到的坐标位置，单位为px，值为正表示位置在y轴下侧；值为负表示位置在y轴上侧；值为0表示位置在y轴坐标原点。该参数仅支持整数输入，浮点数输入将向下取整。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed. 2. The window type is not supported for this operation. |
| 1300003 | This window manager service works abnormally. |
| 1300010 | The operation in the current window status is invalid. Possible cause: The window status is not FLOATING. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let promise = windowClass.moveWindowToAsync(300, 300);
5. promise.then(() => {
6. console.info('Succeeded in moving the window.');
7. let rect = windowClass?.getWindowProperties().windowRect;
8. console.info(`Get window rect: ` + JSON.stringify(rect));
9. }).catch((err: BusinessError) => {
10. console.error(`Failed to move the window. Cause code: ${err.code}, message: ${err.message}`);
11. });
12. } catch (exception) {
13. console.error(`Failed to move the window. Cause code: ${exception.code}, message: ${exception.message}`);
14. }
```

## moveWindowToAsync15+

PhonePC/2in1TabletTVWearable

moveWindowToAsync(x: number, y: number, moveConfiguration?: MoveConfiguration): Promise<void>

移动窗口位置，支持配置moveConfiguration参数指定窗口移动的目标屏幕ID，使用Promise异步回调。调用生效后返回，回调中可使用[getWindowProperties()](arkts-apis-window-window.md#getwindowproperties9)（见示例）立即获取最终生效结果。

该接口仅在窗口为自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING，窗口模式可通过[getWindowStatus()](arkts-apis-window-window.md#getwindowstatus12)获取）时调用生效，在其他窗口模式下调用返回错误码1300010错误码。

在自由悬浮窗口模式下，不同类型窗口的移动行为如下：

| 窗口类型 | [自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态 | 非自由窗口状态 |
| --- | --- | --- |
| 主窗口 | 相对于屏幕移动 | 调用不生效不报错 |
| 应用子窗口/模态窗 | 相对于屏幕移动 | 相对于主窗口移动 |
| 系统窗口/全局悬浮窗 | 相对于屏幕移动 | 相对于屏幕移动 |

说明

* [自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态下，若主窗口或子窗口的标题栏移出屏幕可视区域，系统将自动回弹窗口，确保标题栏保持可见。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 窗口在x轴方向移动的值，值为正表示右移，单位为px，该参数应该为整数，非整数输入将向下取整。 |
| y | number | 是 | 窗口在y轴方向移动的值，值为正表示下移，单位为px，该参数应该为整数，非整数输入将向下取整。 |
| moveConfiguration | [MoveConfiguration](arkts-apis-window-i.md#moveconfiguration15) | 否 | 窗口移动选项，未设置将默认保持为当前屏幕。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed. 2. The window type is not supported for this operation. |
| 1300003 | This window manager service works abnormally. |
| 1300010 | The operation in the current window status is invalid. Possible cause: The window status is not FLOATING. |

**示例：**

```
1. import { window } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let moveConfiguration: window.MoveConfiguration = {
6. displayId: 0
7. };
8. let promise = windowClass.moveWindowToAsync(300, 300, moveConfiguration);
9. promise.then(() => {
10. console.info('Succeeded in moving the window.');
11. let rect = windowClass?.getWindowProperties().windowRect;
12. console.info(`Get window rect: ` + JSON.stringify(rect));
13. }).catch((err: BusinessError) => {
14. console.error(`Failed to move the window. Cause code: ${err.code}, message: ${err.message}`);
15. });
16. } catch (exception) {
17. console.error(`Failed to move the window. Cause code: ${exception.code}, message: ${exception.message}`);
18. }
```

## moveWindowToGlobal13+

PhonePC/2in1TabletTVWearable

moveWindowToGlobal(x: number, y: number): Promise<void>

基于屏幕坐标移动窗口位置，使用Promise异步回调。调用生效后返回，回调中可使用[getWindowProperties()](arkts-apis-window-window.md#getwindowproperties9)（见示例）立即获取最终生效结果。

该接口仅在窗口为自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING，窗口模式可通过[getWindowStatus()](arkts-apis-window-window.md#getwindowstatus12)获取）时调用生效，在其他窗口模式下调用返回错误码1300010错误码。

说明

* 主窗处于自由悬浮窗口模式时，在非[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态下调用不生效不报错。
* [自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态下，若主窗口或子窗口的标题栏移出屏幕可视区域，系统将自动回弹窗口，确保标题栏保持可见。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 表示以屏幕左上角为起点，窗口在x轴方向移动的值，单位为px。值为正表示右移，值为负表示左移。该参数仅支持整数输入，浮点数输入将向下取整。 |
| y | number | 是 | 表示以屏幕左上角为起点，窗口在y轴方向移动的值，单位为px。值为正表示下移，值为负表示上移。该参数仅支持整数输入，浮点数输入将向下取整。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed. 2. The window type is not supported for this operation. |
| 1300003 | This window manager service works abnormally. |
| 1300010 | The operation in the current window status is invalid. Possible cause: The window status is not FLOATING. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let promise = windowClass.moveWindowToGlobal(300, 300);
5. promise.then(() => {
6. console.info('Succeeded in moving the window.');
7. let rect = windowClass?.getWindowProperties().windowRect;
8. console.info(`Get window rect: ` + JSON.stringify(rect));
9. }).catch((err: BusinessError) => {
10. console.error(`Failed to move the window. Cause code: ${err.code}, message: ${err.message}`);
11. });
12. } catch (exception) {
13. console.error(`Failed to move the window. Cause code: ${exception.code}, message: ${exception.message}`);
14. }
```

## moveWindowToGlobal15+

PhonePC/2in1TabletTVWearable

moveWindowToGlobal(x: number, y: number, moveConfiguration?: MoveConfiguration): Promise<void>

基于屏幕坐标移动窗口位置，支持配置moveConfiguration参数指定窗口移动的目标屏幕ID，使用Promise异步回调。调用生效后返回，回调中可使用[getWindowProperties()](arkts-apis-window-window.md#getwindowproperties9)（见示例）立即获取最终生效结果。

该接口仅在窗口为自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING，窗口模式可通过[getWindowStatus()](arkts-apis-window-window.md#getwindowstatus12)获取）时调用生效，在其他窗口模式下调用返回错误码1300010错误码。

说明

* 主窗处于自由悬浮窗口模式时，在非[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态下调用不生效不报错。
* [自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态下，若主窗口或子窗口的标题栏移出屏幕可视区域，系统将自动回弹窗口，确保标题栏保持可见。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 表示以目标屏幕左上角为起点，窗口在x轴方向移动的值，单位为px。值为正表示右移，值为负表示左移。该参数应该为整数，非整数输入将向下取整。 |
| y | number | 是 | 表示以目标屏幕左上角为起点，窗口在y轴方向移动的值，单位为px。值为正表示下移，值为负表示上移。该参数应该为整数，非整数输入将向下取整。 |
| moveConfiguration | [MoveConfiguration](arkts-apis-window-i.md#moveconfiguration15) | 否 | 窗口移动选项，未设置将默认保持为当前屏幕。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed. 2. The window type is not supported for this operation. |
| 1300003 | This window manager service works abnormally. |
| 1300010 | The operation in the current window status is invalid. Possible cause: The window status is not FLOATING. |

**示例：**

```
1. import { window } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let moveConfiguration: window.MoveConfiguration = {
6. displayId: 0
7. };
8. let promise = windowClass.moveWindowToGlobal(300, 300, moveConfiguration);
9. promise.then(() => {
10. console.info('Succeeded in moving the window.');
11. let rect = windowClass?.getWindowProperties().windowRect;
12. console.info(`Get window rect: ` + JSON.stringify(rect));
13. }).catch((err: BusinessError) => {
14. console.error(`Failed to move the window. Cause code: ${err.code}, message: ${err.message}`);
15. });
16. } catch (exception) {
17. console.error(`Failed to move the window. Cause code: ${exception.code}, message: ${exception.message}`);
18. }
```

## moveWindowToGlobalDisplay20+

PhonePC/2in1TabletTVWearable

moveWindowToGlobalDisplay(x: number, y: number): Promise<void>

基于[全局坐标系](../harmonyos-guides/window-terminology.md#全局坐标系)移动窗口位置，使用Promise异步回调。

该接口仅在窗口为自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING，窗口模式可通过[getWindowStatus()](arkts-apis-window-window.md#getwindowstatus12)获取）时调用生效，在其他窗口模式下调用返回错误码1300010错误码。

说明

* 主窗处于自由悬浮窗口模式时，在非[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态下调用不生效不报错。
* 窗口移动后，如果窗口跨越多个屏幕，窗口将归属于与其重叠面积最大的屏幕。
* [自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态下，若主窗口或子窗口的标题栏移出屏幕可视区域，系统将自动回弹窗口，确保标题栏保持可见。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 表示以主屏幕左上角为起点，窗口在x轴方向移动的值，单位为px。值为正表示右移，值为负表示左移。该参数应该为整数，非整数输入将向下取整。 |
| y | number | 是 | 表示以主屏幕左上角为起点，窗口在y轴方向移动的值，单位为px。值为正表示下移，值为负表示上移。该参数应该为整数，非整数输入将向下取整。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed. 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |
| 1300010 | The operation in the current window status is invalid. Possible cause: The window status is not FLOATING. |
| 1300016 | Parameter error. Possible cause: 1. Invalid parameter range. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let promise = windowClass.moveWindowToGlobalDisplay(300, 300);
5. promise.then(() => {
6. console.info('Succeeded in moving the window in global display.');
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to move the window in global display. Cause code: ${err.code}, message: ${err.message}`);
9. });
10. } catch (exception) {
11. console.error(`Failed to move the window in global display. Cause code: ${exception.code}, message: ${exception.message}`);
12. }
```

## clientToGlobalDisplay20+

PhonePC/2in1TabletTVWearable

clientToGlobalDisplay(winX: number, winY: number): Position

将相对于当前窗口左上角的坐标转换为相对于主屏幕左上角的全局坐标。

不支持在经过显示缩放的窗口中调用，例如手机或平板设备在非自由多窗模式下的悬浮窗场景。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| winX | number | 是 | 表示以当前窗口左上角为原点的x轴方向偏移量，单位为px。值为正表示在原点右侧，值为负表示在原点左侧。该参数应为整数，非整数输入将向下取整。 |
| winY | number | 是 | 表示以当前窗口左上角为原点的y轴方向偏移量，单位为px。值为正表示在原点下方，值为负表示在原点上方。该参数应为整数，非整数输入将向下取整。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Position](arkts-apis-window-i.md#position20) | 返回转换后的坐标。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300010 | The operation in the current window status is invalid. |
| 1300016 | Parameter error. Possible cause: 1. Invalid parameter range. |

**示例：**

```
1. try {
2. let position = windowClass.clientToGlobalDisplay(100, 100);
3. console.info(`Succeeded in converting the position in the current window to the position in global display. Position: ` + JSON.stringify(position));
4. } catch (exception) {
5. console.error(`Failed to convert the position. Cause code: ${exception.code}, message: ${exception.message}`);
6. }
```

## globalDisplayToClient20+

PhonePC/2in1TabletTVWearable

globalDisplayToClient(globalDisplayX: number, globalDisplayY: number): Position

将相对于主屏幕左上角的全局坐标转换为相对于当前窗口左上角的坐标。

不支持在经过显示缩放的窗口中调用，例如手机或平板设备在非自由多窗模式下的悬浮窗场景。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| globalDisplayX | number | 是 | 表示以当前窗口左上角为原点的x轴方向偏移量，单位为px。值为正表示在原点右侧，值为负表示在原点左侧。该参数应为整数，非整数输入将向下取整。 |
| globalDisplayY | number | 是 | 表示以当前窗口左上角为原点的y轴方向偏移量，单位为px。值为正表示在原点下方，值为负表示在原点上方。该参数应为整数，非整数输入将向下取整。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Position](arkts-apis-window-i.md#position20) | 返回转换后的坐标。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300010 | The operation in the current window status is invalid. |
| 1300016 | Parameter error. Possible cause: 1. Invalid parameter range. |

**示例：**

```
1. try {
2. let position = windowClass.globalDisplayToClient(100, 100);
3. console.info(`Succeeded in converting in the position in global display to the position in the current window. Position: ` + JSON.stringify(position));
4. } catch (exception) {
5. console.error(`Failed to convert the position. Cause code: ${exception.code}, message: ${exception.message}`);
6. }
```

## resize9+

PhonePC/2in1TabletTVWearable

resize(width: number, height: number, callback: AsyncCallback<void>): void

基于窗口左上角顶点改变当前窗口大小，使用callback异步回调。

调用成功即返回，该接口返回后无法立即获取最终生效结果，如需立即获取，建议使用接口[resizeAsync()](arkts-apis-window-window.md#resizeasync12)。

窗口存在大小限制[WindowLimits](arkts-apis-window-i.md#windowlimits11)，具体尺寸限制范围可以通过[getWindowLimits](arkts-apis-window-window.md#getwindowlimits11)接口进行查询。

调用该接口设置的宽度与高度受到此限制约束，规则：

若所设置的窗口宽/高尺寸小于窗口最小宽/高限制值，则窗口最小宽/高限制值生效，系统窗口和全局悬浮窗设置最小值不受窗口最小宽/高限制值限制；

若所设置的窗口宽/高尺寸大于窗口最大宽/高限制值，则窗口最大宽/高限制值生效。

该接口仅在窗口为自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING，窗口模式可通过[getWindowStatus()](arkts-apis-window-window.md#getwindowstatus12)获取）时调用生效，在其他窗口模式下调用返回1300002错误码。

说明

* 主窗口处于自由悬浮窗口模式时，在非[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态下调用不报错不生效。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 当前窗口的目标宽度，单位为px，该参数仅支持整数输入，浮点数输入将向下取整，负值为非法参数（抛出错误码401）。 |
| height | number | 是 | 当前窗口的目标高度，单位为px，该参数仅支持整数输入，浮点数输入将向下取整，负值为非法参数（抛出错误码401）。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. windowClass.resize(500, 1000, (err: BusinessError) => {
5. const errCode: number = err.code;
6. if (errCode) {
7. console.error(`Failed to change the window size. Cause code: ${err.code}, message: ${err.message}`);
8. return;
9. }
10. console.info('Succeeded in changing the window size.');
11. });
12. } catch (exception) {
13. console.error(`Failed to change the window size. Cause code: ${exception.code}, message: ${exception.message}`);
14. }
```

## resize9+

PhonePC/2in1TabletTVWearable

resize(width: number, height: number): Promise<void>

基于窗口左上角顶点改变当前窗口大小，使用Promise异步回调。

调用成功即返回，该接口返回后无法立即获取最终生效结果，如需立即获取，建议使用接口[resizeAsync()](arkts-apis-window-window.md#resizeasync12)。

窗口存在大小限制[WindowLimits](arkts-apis-window-i.md#windowlimits11)，具体尺寸限制范围可以通过[getWindowLimits](arkts-apis-window-window.md#getwindowlimits11)接口进行查询。

调用该接口设置的宽度与高度受到此限制约束，规则：

若所设置的窗口宽/高尺寸小于窗口最小宽/高限制值，则窗口最小宽/高限制值生效，系统窗口和全局悬浮窗设置最小值不受窗口最小宽/高限制值限制；

若所设置的窗口宽/高尺寸大于窗口最大宽/高限制值，则窗口最大宽/高限制值生效。

该接口仅在窗口为自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING，窗口模式可通过[getWindowStatus()](arkts-apis-window-window.md#getwindowstatus12)获取）时调用生效，在其他窗口模式下调用返回1300002错误码。

说明

* 主窗口处于自由悬浮窗口模式时，在非[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态下调用不报错不生效。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 当前窗口的目标宽度，单位为px，该参数仅支持整数输入，浮点数输入将向下取整，负值为非法参数（抛出错误码401）。 |
| height | number | 是 | 当前窗口的目标高度，单位为px，该参数仅支持整数输入，浮点数输入将向下取整，负值为非法参数（抛出错误码401）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let promise = windowClass.resize(500, 1000);
5. promise.then(() => {
6. console.info('Succeeded in changing the window size.');
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to change the window size. Cause code: ${err.code}, message: ${err.message}`);
9. });
10. } catch (exception) {
11. console.error(`Failed to change the window size. Cause code: ${exception.code}, message: ${exception.message}`);
12. }
```

## resizeAsync12+

PhonePC/2in1TabletTVWearable

resizeAsync(width: number, height: number): Promise<void>

基于窗口左上角顶点改变当前窗口大小，使用Promise异步回调。

调用生效后返回，回调中可使用[getWindowProperties()](arkts-apis-window-window.md#getwindowproperties9)（见示例）立即获取最终生效结果。

窗口存在大小限制[WindowLimits](arkts-apis-window-i.md#windowlimits11)，具体尺寸限制范围可以通过[getWindowLimits](arkts-apis-window-window.md#getwindowlimits11)接口进行查询。

调用该接口设置的宽度与高度受到此限制约束，规则：

若所设置的窗口宽/高尺寸小于窗口最小宽/高限制值，则窗口最小宽/高限制值生效，系统窗口和全局悬浮窗设置最小值不受窗口最小宽/高限制值限制；

若所设置的窗口宽/高尺寸大于窗口最大宽/高限制值，则窗口最大宽/高限制值生效。

该接口仅在窗口为自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING，窗口模式可通过[getWindowStatus()](arkts-apis-window-window.md#getwindowstatus12)获取）时调用生效，否则抛出错误码1300010。

说明

* 在非[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态下，主窗口调用不生效。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 当前窗口的目标宽度，单位为px，该参数仅支持整数输入，浮点数输入将向下取整，负值为非法参数（抛出错误码401）。 |
| height | number | 是 | 当前窗口的目标高度，单位为px，该参数仅支持整数输入，浮点数输入将向下取整，负值为非法参数（抛出错误码401）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: Invalid parameter range. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed. 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |
| 1300010 | The operation in the current window status is invalid. Possible cause: The window status is not FLOATING. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let promise = windowClass.resizeAsync(500, 1000);
5. promise.then(() => {
6. console.info('Succeeded in changing the window size.');
7. let rect = windowClass?.getWindowProperties().windowRect;
8. console.info(`Get window rect: ` + JSON.stringify(rect));
9. }).catch((err: BusinessError) => {
10. console.error(`Failed to change the window size. Cause code: ${err.code}, message: ${err.message}`);
11. });
12. } catch (exception) {
13. console.error(`Failed to change the window size. Cause code: ${exception.code}, message: ${exception.message}`);
14. }
```

## getWindowProperties9+

PhonePC/2in1TabletTVWearable

getWindowProperties(): WindowProperties

获取当前窗口的属性。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WindowProperties](arkts-apis-window-i.md#windowproperties) | 当前窗口属性。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |

**示例：**

```
1. try {
2. let properties = windowClass.getWindowProperties();
3. } catch (exception) {
4. console.error(`Failed to obtain the window properties. Cause code: ${exception.code}, message: ${exception.message}`);
5. }
```

## getWindowDensityInfo15+

PhonePC/2in1TabletTVWearable

getWindowDensityInfo(): WindowDensityInfo

获取当前窗口所在屏幕的系统显示大小缩放系数、系统默认显示大小缩放系数和自定义显示大小缩放系数信息。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WindowDensityInfo](arkts-apis-window-i.md#windowdensityinfo15) | 当前窗口的显示大小缩放系数信息。当返回值为[-1, -1, -1]时，表示当前设备不支持使用该接口。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |

**示例：**

```
1. try {
2. let densityInfo = windowClass.getWindowDensityInfo();
3. } catch (exception) {
4. console.error(`Failed to obtain the window densityInfo. Cause code: ${exception.code}, message: ${exception.message}`);
5. }
```

## setWindowContainerColor20+

PhonePC/2in1TabletTVWearable

setWindowContainerColor(activeColor: string, inactiveColor: string): void

设置主窗口容器在焦点态和非焦点态时的背景色。在Stage模型下，该接口需在调用[loadContent()](arkts-apis-window-window.md#loadcontent9)或[setUIContent()](arkts-apis-window-window.md#setuicontent9)后使用。

窗口容器背景色覆盖整个窗口区域，包括标题栏和内容区域。当同时使用该接口和[setWindowBackgroundColor()](arkts-apis-window-window.md#setwindowbackgroundcolor9)设置背景色时，内容区域显示窗口背景色，标题栏显示窗口容器背景色。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 在HarmonyOS 6.1.0之前，该接口在2in1设备中可正常调用，在其他设备中返回801错误码；从HarmonyOS 6.1.0开始，该接口在2in1和Tablet设备中可正常调用，在其他设备中返回801错误码。

**需要权限：** ohos.permission.SET\_WINDOW\_TRANSPARENT

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| activeColor | string | 是 | 窗口容器处于焦点态时的背景色，为十六进制RGB或ARGB颜色，不区分大小写，例如'#00FF00'或'#FF00FF00'。 |
| inactiveColor | string | 是 | 窗口容器处于非焦点态时的背景色，为十六进制RGB颜色或ARGB颜色（透明度固定为'FF'），不区分大小写，例如'#00FF00'或'#FF00FF00'。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300004 | Unauthorized operation. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. onWindowStageCreate(windowStage: window.WindowStage) {
8. windowStage.loadContent("pages/page2", (err: BusinessError) => {
9. let errCode: number = err.code;
10. if (errCode) {
11. console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
12. return;
13. }
14. console.info('Succeeded in loading the content.');
15. // 获取应用主窗口。
16. let windowClass: window.Window | undefined = undefined;
17. windowStage.getMainWindow((err: BusinessError, data) => {
18. let errCode: number = err.code;
19. if (errCode) {
20. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
21. return;
22. }
23. windowClass = data;
24. let activeColor: string = '#00000000';
25. let inactiveColor: string = '#FF000000';
26. try {
27. windowClass.setWindowContainerColor(activeColor, inactiveColor);
28. console.info('Succeeded in setting window container color.');
29. } catch (exception) {
30. console.error(`Failed to set the window container color. Cause code: ${exception.code}, message: ${exception.message}`);
31. };
32. });
33. });
34. }
35. }
```

## getGlobalRect13+

PhonePC/2in1TabletTVWearable

getGlobalRect(): Rect

获取窗口在其所在物理屏幕上的真实显示区域，同步接口。

在某些设备上，窗口显示时可能经过了缩放，此接口可以获取缩放后窗口在屏幕上的真实位置和大小。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Rect](arkts-apis-window-i.md#rect7) | 四元组分别表示距离屏幕左上角的x坐标、距离屏幕左上角的y坐标、缩放后的窗口宽度和缩放后的窗口高度。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed. 2. Failed to convert result into JS value object. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. try {
2. let rect = windowClass.getGlobalRect();
3. console.info(`Succeeded in getting window rect: ` + JSON.stringify(rect));
4. } catch (exception) {
5. console.error(`Failed to get window rect. Cause code: ${exception.code}, message: ${exception.message}`);
6. }
```

## getWindowAvoidArea9+

PhonePC/2in1TabletTVWearable

getWindowAvoidArea(type: AvoidAreaType): AvoidArea

获取当前窗口避让区域。

主窗口/子窗口：

* [自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的自由悬浮窗口模式（即窗口模式为[window.WindowStatusType.FLOATING](arkts-apis-window-e.md#windowstatustype11)）下，仅存在固定态软键盘（[AvoidAreaType](arkts-apis-window-e.md#avoidareatype7)为TYPE\_KEYBOARD）类型的避让区域。
* 主窗口在非自由窗口状态的自由悬浮窗口模式下，仅存在系统栏（[AvoidAreaType](arkts-apis-window-e.md#avoidareatype7)为TYPE\_SYSTEM）类型的避让区域。
* 主窗口在其余场景下，仅当在非自由悬浮窗口模式下或设备类型为Phone和Tablet，才能通过此接口获取计算后的避让区域，否则获取的避让区域为空。
* 子窗口在非自由窗口状态或非自由悬浮窗口模式下，仅当窗口的位置和大小与主窗口一致时，才能通过此接口获取计算后的避让区域，否则获取的避让区域为空。

全局悬浮窗、模态窗或系统窗口：

* 仅在调用[setSystemAvoidAreaEnabled](arkts-apis-window-window.md#setsystemavoidareaenabled18)方法使能后，才能通过此接口获取避让区域，否则获取的避让区域为空。

该接口一般适用于两种场景：

* 在[onWindowStageCreate()](js-apis-app-ability-uiability.md#onwindowstagecreate)方法中，获取应用启动时的初始布局避让区域时可调用该接口。
* 当应用内子窗需要临时显示，对显示内容做布局避让时可调用该接口。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [AvoidAreaType](arkts-apis-window-e.md#avoidareatype7) | 是 | 表示避让区域类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AvoidArea](arkts-apis-window-i.md#avoidarea7) | 窗口内容避让区域。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Convert avoid area failed. |

**示例：**

```
1. let type = window.AvoidAreaType.TYPE_SYSTEM;
2. try {
3. let avoidArea = windowClass.getWindowAvoidArea(type);
4. } catch (exception) {
5. console.error(`Failed to obtain the area. Cause code: ${exception.code}, message: ${exception.message}`);
6. }
```

## getWindowAvoidAreaIgnoringVisibility22+

PhonePC/2in1TabletTVWearable

getWindowAvoidAreaIgnoringVisibility(type: AvoidAreaType): AvoidArea

获取当前应用窗口的避让区域，即使避让区域当前处于不可见状态。

主窗口/子窗口：

* 主窗口在非[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的自由悬浮窗口模式（即窗口模式为[window.WindowStatusType.FLOATING](arkts-apis-window-e.md#windowstatustype11)）下，仅存在系统栏（[AvoidAreaType](arkts-apis-window-e.md#avoidareatype7)为TYPE\_SYSTEM）类型的避让区域。
* 主窗口在其余场景下，仅当在非自由悬浮窗口模式下或设备类型为Phone和Tablet，才能通过此接口获取计算后的避让区域，否则获取的避让区域为空。
* 子窗口在非自由窗口状态或非自由悬浮窗口模式下，仅当窗口的位置和大小与主窗口一致时，才能通过此接口获取计算后的避让区域，否则获取的避让区域为空。

全局悬浮窗、模态窗或系统窗口：

* 仅在调用[setSystemAvoidAreaEnabled](arkts-apis-window-window.md#setsystemavoidareaenabled18)方法使能后，才能通过此接口获取计算后的避让区域，否则获取的避让区域为空。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [AvoidAreaType](arkts-apis-window-e.md#avoidareatype7) | 是 | 表示避让区域类型。不支持获取软键盘类型的避让区域，传入TYPE\_KEYBOARD时，返回1300016错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AvoidArea](arkts-apis-window-i.md#avoidarea7) | 窗口内容避让区域。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Convert avoid area failed. |
| 1300003 | This window manager service works abnormally. |
| 1300016 | Parameter error. |

**示例：**

```
1. let type = window.AvoidAreaType.TYPE_SYSTEM;
2. try {
3. let avoidArea = windowClass.getWindowAvoidAreaIgnoringVisibility(type);
4. } catch (exception) {
5. console.error(`Failed to obtain the area. Cause code: ${exception.code}, message: ${exception.message}`);
6. }
```

## setSystemAvoidAreaEnabled18+

PhonePC/2in1TabletTVWearable

setSystemAvoidAreaEnabled(enabled: boolean): Promise<void>

创建全局悬浮窗、模态窗或WindowType窗口类型为系统窗口时，调用该接口使能后才可以通过[getWindowAvoidArea()](arkts-apis-window-window.md#getwindowavoidarea9)获取窗口避让区信息或通过[on('avoidAreaChange')](arkts-apis-window-window.md#onavoidareachange9)监听窗口避让区变化。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 是否可以获取到避让区。  true表示可以获取避让区；false表示不可以获取避让区。默认值是false。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only global floating windows, dialog windows, or Window Type as system windows are supported. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. // ...
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. console.info('onWindowStageCreate');
10. windowStage.loadContent('pages/Index', (err) => {
11. if (err.code) {
12. console.error('Failed to load the content. Cause: %{public}s', JSON.stringify(err));
13. return;
14. }
15. console.info('Succeeded in loading the content.');
16. let windowClass: window.Window | undefined = undefined;
17. let config: window.Configuration = {
18. name: "test",
19. windowType: window.WindowType.TYPE_DIALOG,
20. decorEnabled: true,
21. ctx: this.context
22. };
23. try {
24. window.createWindow(config, (err: BusinessError, data) => {
25. const errCode: number = err.code;
26. if (errCode) {
27. console.error(`Failed to create the system window. Cause code: ${err.code}, message: ${err.message}`);
28. return;
29. }
30. windowClass = data;
31. windowClass.setUIContent("pages/Test");
32. let enabled = true;
33. let promise = windowClass.setSystemAvoidAreaEnabled(enabled);
34. promise.then(() => {
35. let type = window.AvoidAreaType.TYPE_SYSTEM;
36. let avoidArea = windowClass?.getWindowAvoidArea(type);
37. }).catch((err: BusinessError) => {
38. console.error(`Failed to obtain the system window avoid area. Cause code: ${err.code}, message: ${err.message}`);
39. });
40. });
41. } catch (exception) {
42. console.error(`Failed to create the system window. Cause code: ${exception.code}, message: ${exception.message}`);
43. }
44. });
45. }
46. }
```

## isSystemAvoidAreaEnabled18+

PhonePC/2in1TabletTVWearable

isSystemAvoidAreaEnabled(): boolean

获取悬浮窗、模态窗或WindowType为系统类型的窗口是否可以获取窗口内容的避让区[AvoidArea](arkts-apis-window-i.md#avoidarea7)。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否可以获取窗口内容的避让区。  true表示可以获取避让区；false表示不可以获取避让区。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Create js value failed. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. // ...
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. console.info('onWindowStageCreate');
10. windowStage.loadContent('pages/Index', (err) => {
11. if (err.code) {
12. console.error('Failed to load the content. Cause: %{public}s', JSON.stringify(err));
13. return;
14. }
15. console.info('Succeeded in loading the content.');
16. let windowClass: window.Window | undefined = undefined;
17. let config: window.Configuration = {
18. name: "test",
19. windowType: window.WindowType.TYPE_DIALOG,
20. decorEnabled: true,
21. ctx: this.context
22. };
23. try {
24. window.createWindow(config, (err: BusinessError, data) => {
25. const errCode: number = err.code;
26. if (errCode) {
27. console.error(`Failed to create the system window. Cause code: ${err.code}, message: ${err.message}`);
28. return;
29. }
30. windowClass = data;
31. windowClass.setUIContent("pages/Test");
32. let promise = windowClass.setSystemAvoidAreaEnabled(true);
33. promise.then(() => {
34. let enabled = windowClass?.isSystemAvoidAreaEnabled();
35. }).catch((err: BusinessError) => {
36. console.error(`Failed to obtain the system window avoid area enable. Cause code: ${err.code}, message: ${err.message}`);
37. });
38. });
39. } catch (exception) {
40. console.error(`Failed to create the system window. Cause code: ${exception.code}, message: ${exception.message}`);
41. }
42. });
43. }
44. }
```

## setTitleAndDockHoverShown14+

PhonePC/2in1TabletTVWearable

setTitleAndDockHoverShown(isTitleHoverShown?: boolean, isDockHoverShown?: boolean): Promise<void>

设置主窗口进入全屏模式时鼠标Hover到热区上是否显示窗口标题栏和dock栏，使用Promise异步回调。

**系统能力**：SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备及不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上调用返回801错误码。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isTitleHoverShown | boolean | 否 | 是否显示窗口标题栏。  true表示显示窗口标题栏；false表示不显示窗口标题栏。默认值是true。 |
| isDockHoverShown | boolean | 否 | 是否显示dock栏。  true表示显示dock栏；false表示不显示dock栏。默认值是true。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300004 | Unauthorized operation. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. // ...
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. // 加载主窗口对应的页面。
10. windowStage.loadContent('pages/Index', (err) => {
11. let mainWindow: window.Window | undefined = undefined;
12. // 获取应用主窗口。
13. windowStage.getMainWindow().then(
14. data => {
15. if (!data) {
16. console.error('Failed to get main window. Cause: The data is undefined.');
17. return;
18. }
19. mainWindow = data;
20. console.info(`Succeeded in obtaining the main window. Data: ${JSON.stringify(data)}`);
21. // 调用maximize接口，设置窗口进入全屏模式。
22. mainWindow.maximize(window.MaximizePresentation.ENTER_IMMERSIVE);
23. // 调用setTitleAndDockHoverShown接口，隐藏标题栏和dock栏。
24. mainWindow.setTitleAndDockHoverShown(false, false);
25. }
26. ).catch((err: BusinessError) => {
27. if(err.code){
28. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
29. }
30. });
31. });
32. }
33. }
```

## setWindowLayoutFullScreen9+

PhonePC/2in1TabletTVWearable

setWindowLayoutFullScreen(isLayoutFullScreen: boolean): Promise<void>

设置应用主窗口或应用子窗口的布局是否为沉浸式布局，使用Promise异步回调。其余窗口调用不生效也不报错。

沉浸式布局生效时，布局不避让状态栏与底部导航区域，组件可能产生与其重叠的情况。

非沉浸式布局生效时，布局避让状态栏与底部导航区域，组件不会与其重叠。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**设备行为差异：**

在HarmonyOS 5.0.2之前，该接口在所有设备中可正常调用。

从HarmonyOS 5.0.2开始，该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上调用不生效也不报错，切换到非[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态时生效；在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备及不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isLayoutFullScreen | boolean | 是 | 窗口的布局是否为沉浸式布局（该沉浸式布局状态栏、底部导航区域仍然显示）。true表示沉浸式布局；false表示非沉浸式布局。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. // ...
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. console.info('onWindowStageCreate');
10. let windowClass: window.Window | undefined = undefined;
11. windowStage.getMainWindow((err: BusinessError, data) => {
12. const errCode: number = err.code;
13. if (errCode) {
14. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
15. return;
16. }
17. windowClass = data;
18. let isLayoutFullScreen = true;
19. try {
20. let promise = windowClass.setWindowLayoutFullScreen(isLayoutFullScreen);
21. promise.then(() => {
22. console.info('Succeeded in setting the window layout to full-screen mode.');
23. }).catch((err: BusinessError) => {
24. console.error(`Failed to set the window layout to full-screen mode. Cause code: ${err.code}, message: ${err.message}`);
25. });
26. } catch (exception) {
27. console.error(`Failed to set the window layout to full-screen mode. Cause code: ${exception.code}, message: ${exception.message}`);
28. }
29. });
30. }
31. }
```

## setImmersiveModeEnabledState12+

PhonePC/2in1TabletTVWearable

setImmersiveModeEnabledState(enabled: boolean): void

设置当前窗口是否开启沉浸式布局，该调用不会改变窗口模式和窗口大小。仅主窗口和子窗口可调用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**设备行为差异：**

在HarmonyOS 5.0.2之前，该接口在所有设备中可正常调用。

从HarmonyOS 5.0.2开始，该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上调用不生效也不报错；在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备及不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 是否开启沉浸式布局。  true表示开启，false表示关闭。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. Possible cause: Internal IPC error. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only main windows and subwindows are supported. |

**示例：**

```
1. try {
2. let enabled = false;
3. windowClass.setImmersiveModeEnabledState(enabled);
4. } catch (exception) {
5. console.error(`Failed to set the window immersive mode enabled status. Cause code: ${exception.code}, message: ${exception.message}`);
6. }
```

## getImmersiveModeEnabledState12+

PhonePC/2in1TabletTVWearable

getImmersiveModeEnabledState(): boolean

查询当前窗口是否开启沉浸式布局。

仅支持主窗和子窗调用。

返回值与[setImmersiveModeEnabledState()](arkts-apis-window-window.md#setimmersivemodeenabledstate12)以及[setWindowLayoutFullScreen()](arkts-apis-window-window.md#setwindowlayoutfullscreen9)设置结果一致，若未调用上述两个接口则默认返回false。

**系统能力**：SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否设置开启沉浸式布局。  true表示开启沉浸式布局，false表示关闭沉浸式布局。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only main windows and subwindows are supported. |

**示例：**

```
1. try {
2. let isEnabled = windowClass.getImmersiveModeEnabledState();
3. } catch (exception) {
4. console.error(`Failed to get the window immersive mode enabled status. Cause code: ${exception.code}, message: ${exception.message}`);
5. }
```

## isImmersiveLayout20+

PhonePC/2in1TabletTVWearable

isImmersiveLayout(): boolean

查询当前窗口是否处于沉浸式布局状态。

**系统能力**：SystemCapability.Window.SessionManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否处于沉浸式布局状态。true表示处于沉浸式布局状态，false表示不处于沉浸式布局状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```
1. try {
2. let isEnabled = windowClass.isImmersiveLayout();
3. } catch (exception) {
4. console.error(`Failed to check if the window layout is in immersive mode. Cause code: ${exception.code}, message: ${exception.message}`);
5. }
```

## setWindowDelayRaiseOnDrag19+

PhonePC/2in1TabletTVWearable

setWindowDelayRaiseOnDrag(isEnabled: boolean): void

设置窗口是否使能延迟抬升，仅主窗和子窗可设置。

不调用此接口或传入false，主窗和子窗在鼠标左键按下时，默认立即抬升。

调用此接口使能延迟抬升后，在跨窗拖拽场景，可拖拽组件所在窗口在鼠标左键按下时不会立即抬升，直到鼠标左键抬起。

**系统能力**：SystemCapability.Window.SessionManager

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**设备行为差异：** 该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用； 在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备及不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上调用返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isEnabled | boolean | 是 | 是否使能延迟抬升。  true表示使能窗口延迟抬升；false表示不使能窗口延迟抬升。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function setWindowDelayRaiseOnDrag can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```
1. try {
2. windowClass.setWindowDelayRaiseOnDrag(true);
3. } catch (exception) {
4. console.error(`Failed to set window delay raise. Cause code: ${exception.code}, message: ${exception.message}`);
5. }
```

## setDragKeyFramePolicy20+

PhonePC/2in1TabletTVWearable

setDragKeyFramePolicy(keyFramePolicy: KeyFramePolicy): Promise<KeyFramePolicy>

设置主窗口拖拽的关键帧策略，并使用Promise处理异步回调。

非主窗口调用时，返回1300004错误码。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 在HarmonyOS 6.1.0之前，该接口在2in1设备可正常调用，在其他设备中返回801错误码。

从HarmonyOS 6.1.0开始，该接口在2in1设备、其他设备的电脑模式中可正常调用；在其他设备和其他模式中不生效不报错。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyFramePolicy | [KeyFramePolicy](arkts-apis-window-i.md#keyframepolicy20) | 是 | 用于设置拖拽的关键帧策略。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[KeyFramePolicy](arkts-apis-window-i.md#keyframepolicy20)> | Promise对象，返回实际生效的关键帧策略。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |
| 1300016 | Parameter error. Possible cause: 1. Invalid parameter range; 2. The parameter format is incorrect. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. // ...
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. console.info('onWindowStageCreate');
10. let windowClass: window.Window | undefined = undefined;
11. windowStage.getMainWindow((err: BusinessError, data) => {
12. const errCode: number = err.code;
13. if (errCode) {
14. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
15. return;
16. }
17. windowClass = data;
18. let keyFramePolicy: window.KeyFramePolicy = {
19. enable: true
20. }
21. try {
22. let promise = windowClass.setDragKeyFramePolicy(keyFramePolicy);
23. promise.then((ret: window.KeyFramePolicy) => {
24. console.info(`Succeeded in setting key frame: ${JSON.stringify(ret)}`);
25. }).catch((err: BusinessError) => {
26. console.error(`Failed to set key frame. Cause code: ${err.code}, message: ${err.message}`);
27. });
28. } catch (exception) {
29. console.error(`Failed to set key frame. Cause code: ${exception.code}, message: ${exception.message}`);
30. }
31. });
32. }
33. }
```

## setWindowSystemBarEnable9+

PhonePC/2in1TabletTVWearable

setWindowSystemBarEnable(names: Array<'status' | 'navigation'>): Promise<void>

设置主窗口状态栏、底部导航（根据用户设置，可表现为导航条或三键导航栏）的可见模式，状态栏和底部导航通过status控制、navigation参数无效果，使用Promise异步回调。

调用生效后返回并不表示状态栏和底部导航区域的显示或隐藏已完成。主窗口在非全屏/最大化模式（悬浮窗、分屏等场景）下配置不生效，进入全屏/最大化模式后配置生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**设备行为差异：**

在HarmonyOS 5.0.0之前，该接口在所有设备中可正常调用。

从HarmonyOS 5.0.0开始，该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上调用不生效也不报错；在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备及不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| names | Array<'status'|'navigation'> | 是 | 设置窗口全屏/最大化模式时状态栏、底部导航区域是否显示。  例如，需全部显示，该参数设置为['status', 'navigation']；设置为[]，则不显示。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. // 此处以状态栏等均不显示为例
2. // EntryAbility.ets
3. import { UIAbility } from '@kit.AbilityKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { window } from '@kit.ArkUI';

7. export default class EntryAbility extends UIAbility {
8. // ...
9. onWindowStageCreate(windowStage: window.WindowStage): void {
10. console.info('onWindowStageCreate');
11. let windowClass: window.Window | undefined = undefined;
12. windowStage.getMainWindow((err: BusinessError, data) => {
13. const errCode: number = err.code;
14. if (errCode) {
15. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
16. return;
17. }
18. windowClass = data;
19. let names: Array<'status' | 'navigation'> = [];
20. try {
21. let promise = windowClass.setWindowSystemBarEnable(names);
22. promise.then(() => {
23. console.info('Succeeded in setting the system bar to be invisible.');
24. }).catch((err: BusinessError) => {
25. console.error(`Failed to set the system bar to be invisible. Cause code: ${err.code}, message: ${err.message}`);
26. });
27. } catch (exception) {
28. console.error(`Failed to set the system bar to be invisible. Cause code: ${exception.code}, message: ${exception.message}`);
29. }
30. });
31. }
32. }
```

## setSpecificSystemBarEnabled11+

PhonePC/2in1TabletTVWearable

setSpecificSystemBarEnabled(name: SpecificSystemBar, enable: boolean, enableAnimation?: boolean): Promise<void>

设置主窗口状态栏、底部导航区域的显示或隐藏，使用Promise异步回调。

调用生效后返回并不表示状态栏和底部导航区域的显示或隐藏已完成。子窗口调用后不生效。主窗口在非全屏/最大化模式（悬浮窗、分屏等场景）下配置不生效，进入全屏/最大化模式后配置生效。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**设备行为差异：**

在HarmonyOS 5.0.0之前，该接口在所有设备中可正常调用。

从HarmonyOS 5.0.0开始，该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上调用不生效也不报错；在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备及不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | [SpecificSystemBar](arkts-apis-window-t.md#specificsystembar11) | 是 | 设置窗口全屏模式时，显示或隐藏的系统栏类型。 |
| enable | boolean | 是 | 设置窗口全屏模式时状态栏或底部导航区域是否显示，true表示显示， false表示隐藏。 |
| enableAnimation12+ | boolean | 否 | 设置状态栏或底部导航区域显示状态变化时是否使用动画，true表示使用， false表示不使用，默认值为false。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. // 此处以隐藏状态栏为例
2. // EntryAbility.ets
3. import { UIAbility } from '@kit.AbilityKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { window } from '@kit.ArkUI';

8. export default class EntryAbility extends UIAbility {
9. // ...
10. onWindowStageCreate(windowStage: window.WindowStage): void {
11. console.info('onWindowStageCreate');
12. let windowClass: window.Window | undefined = undefined;
13. windowStage.getMainWindow((err: BusinessError, data) => {
14. const errCode: number = err.code;
15. if (errCode) {
16. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
17. return;
18. }
19. windowClass = data;
20. try {
21. let promise = windowClass.setSpecificSystemBarEnabled('status', false);
22. promise.then(() => {
23. console.info('Succeeded in setting the system bar to be invisible.');
24. }).catch((err: BusinessError) => {
25. console.error(`Failed to set the system bar to be invisible. Cause code: ${err.code}, message: ${err.message}`);
26. });
27. } catch (exception) {
28. console.error(`Failed to set the system bar to be invisible. Cause code: ${exception.code}, message: ${exception.message}`);
29. }
30. });
31. }
32. }
```

## setWindowSystemBarProperties9+

PhonePC/2in1TabletTVWearable

setWindowSystemBarProperties(systemBarProperties: SystemBarProperties): Promise<void>

设置主窗口状态栏的属性，使用Promise异步回调。

子窗口调用后不生效。主窗口在非全屏/最大化模式（悬浮窗、分屏等场景）下配置不生效，进入全屏/最大化模式后配置生效。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**设备行为差异：** 该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上调用不生效也不报错；在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备及不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| systemBarProperties | [SystemBarProperties](arkts-apis-window-i.md#systembarproperties) | 是 | 状态栏的属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. // ...
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. console.info('onWindowStageCreate');
10. let windowClass: window.Window | undefined = undefined;
11. windowStage.getMainWindow((err: BusinessError, data) => {
12. const errCode: number = err.code;
13. if (errCode) {
14. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
15. return;
16. }
17. windowClass = data;
18. let SystemBarProperties: window.SystemBarProperties = {
19. statusBarColor: '#ff00ff',
20. navigationBarColor: '#00ff00',
21. // 以下两个属性从API Version8开始支持
22. statusBarContentColor: '#ffffff',
23. navigationBarContentColor: '#00ffff'
24. };
25. try {
26. let promise = windowClass.setWindowSystemBarProperties(SystemBarProperties);
27. promise.then(() => {
28. console.info('Succeeded in setting the system bar properties.');
29. }).catch((err: BusinessError) => {
30. console.error(`Failed to set the system bar properties. Cause code: ${err.code}, message: ${err.message}`);
31. });
32. } catch (exception) {
33. console.error(`Failed to set the system bar properties. Cause code: ${exception.code}, message: ${exception.message}`);
34. }
35. });
36. }
37. }
```

## getWindowSystemBarProperties12+

PhonePC/2in1TabletTVWearable

getWindowSystemBarProperties(): SystemBarProperties

获取主窗口状态栏的属性。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SystemBarProperties](arkts-apis-window-i.md#systembarproperties) | 当前状态栏属性。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. Possible cause: Create js object failed. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only main windows are supported. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. // ...

9. onWindowStageCreate(windowStage: window.WindowStage) {
10. let windowClass: window.Window | undefined = undefined;
11. windowStage.getMainWindow((err: BusinessError, data) => {
12. const errCode: number = err.code;
13. if (errCode) {
14. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
15. return;
16. }
17. windowClass = data;
18. try {
19. let systemBarProperty = windowClass.getWindowSystemBarProperties();
20. console.info('Success in obtaining system bar properties. Property: ' + JSON.stringify(systemBarProperty));
21. } catch (err) {
22. console.error(`Failed to get system bar properties. Code: ${err.code}, message: ${err.message}`);
23. }
24. });
25. }
26. };
```

## setStatusBarColor18+

PhonePC/2in1TabletTVWearable

setStatusBarColor(color: ColorMetrics): Promise<void>

设置主窗口状态栏的文字颜色，使用Promise异步回调。

子窗口不支持设置状态栏文字颜色，调用无效果。主窗口在非全屏/最大化模式（悬浮窗、分屏等场景）下配置不生效，进入全屏/最大化模式后配置生效。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**设备行为差异：** 该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上调用不生效也不报错；在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备及不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 是 | 要设置的状态栏颜色值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported on this device. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. Possible cause: Internal task error. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { ColorMetrics, window } from '@kit.ArkUI';
5. import { window } from '@kit.ArkUI';

7. export default class EntryAbility extends UIAbility {
8. // ...
9. onWindowStageCreate(windowStage: window.WindowStage): void {
10. console.info('onWindowStageCreate');
11. let windowClass: window.Window | undefined = undefined;
12. windowStage.getMainWindow((err: BusinessError, data) => {
13. const errCode: number = err.code;
14. if (errCode) {
15. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
16. return;
17. }
18. windowClass = data;
19. try {
20. let promise = windowClass.setStatusBarColor(ColorMetrics.numeric(0x112233));
21. promise.then(() => {
22. console.info('Succeeded in setting the status bar color.');
23. }).catch((err: BusinessError) => {
24. console.error(`Set the status bar color failed. Cause code: ${err.code}, message: ${err.message}`);
25. });
26. } catch (exception) {
27. console.error(`Failed to set the status bar color. Cause code: ${exception.code}, message: ${exception.message}`);
28. }
29. });
30. }
31. }
```

## getStatusBarProperty18+

PhonePC/2in1TabletTVWearable

getStatusBarProperty(): StatusBarProperty

获取主窗口状态栏的属性，如状态栏文字颜色。

子窗口不支持查询，调用会返回错误码1300004。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [StatusBarProperty](arkts-apis-window-i.md#statusbarproperty18) | 当前状态栏属性，如状态栏颜色。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only main windows are supported. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. // ...
8. onWindowStageCreate(windowStage: window.WindowStage) {
9. let windowClass: window.Window | undefined = undefined;
10. windowStage.getMainWindow((err: BusinessError, data) => {
11. const errCode: number = err.code;
12. if (errCode) {
13. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
14. return;
15. }
16. windowClass = data;
17. try {
18. let statusBarProperty = windowClass.getStatusBarProperty();
19. console.info('Succeeded in obtaining system bar properties. Property: ' + JSON.stringify(statusBarProperty));
20. } catch (err) {
21. console.error(`Failed to get system bar properties. Code: ${err.code}, message: ${err.message}`);
22. }
23. });
24. }
25. };
```

## setPreferredOrientation9+

PhonePC/2in1TabletTVWearable

setPreferredOrientation(orientation: Orientation, callback: AsyncCallback<void>): void

设置主窗口的显示方向属性，使用callback异步回调。相关横竖屏开发实践查询[横竖屏切换](../best-practices/bpta-landscape-and-portrait-development.md)。非主窗口调用后不生效不报错。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**设备行为差异：**

* 设备支持sensor旋转且未处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态：立即生效。
* 设备支持sensor旋转且处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态：调用不生效不报错，切换到非[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态后生效。
* 其他情况：不生效不报错。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| orientation | [Orientation](arkts-apis-window-e.md#orientation9) | 是 | 窗口显示方向的属性。 |
| callback | AsyncCallback<void> | 是 | 回调函数。该回调函数返回调用结果是否成功，非应用旋转动效结束。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: Invalid parameter value range. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. // ...
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. console.info('onWindowStageCreate');
10. let windowClass: window.Window | undefined = undefined;
11. windowStage.getMainWindow((err: BusinessError, data) => {
12. const errCode: number = err.code;
13. if (errCode) {
14. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
15. return;
16. }
17. windowClass = data;
18. let orientation = window.Orientation.AUTO_ROTATION;
19. try {
20. windowClass.setPreferredOrientation(orientation, (err: BusinessError) => {
21. const errCode: number = err.code;
22. if (errCode) {
23. console.error(`Failed to set window orientation. Cause code: ${err.code}, message: ${err.message}`);
24. return;
25. }
26. console.info('Succeeded in setting window orientation.');
27. });
28. } catch (exception) {
29. console.error(`Failed to set window orientation. Cause code: ${exception.code}, message: ${exception.message}`);
30. }
31. });
32. }
33. }
```

## setPreferredOrientation9+

PhonePC/2in1TabletTVWearable

setPreferredOrientation(orientation: Orientation): Promise<void>

设置主窗口的显示方向属性，使用Promise异步回调。非主窗口调用后不生效不报错。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**设备行为差异：**

* 设备支持sensor旋转且未处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态：立即生效。
* 设备支持sensor旋转且处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态：调用不生效不报错，切换到非[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态后生效。
* 其他情况：不生效不报错。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| orientation | [Orientation](arkts-apis-window-e.md#orientation9) | 是 | 窗口显示方向的属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: Invalid parameter value range. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. // ...
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. console.info('onWindowStageCreate');
10. let windowClass: window.Window | undefined = undefined;
11. windowStage.getMainWindow((err: BusinessError, data) => {
12. const errCode: number = err.code;
13. if (errCode) {
14. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
15. return;
16. }
17. windowClass = data;
18. let orientation = window.Orientation.AUTO_ROTATION;
19. try {
20. let promise = windowClass.setPreferredOrientation(orientation);
21. promise.then(() => {
22. console.info('Succeeded in setting the window orientation.');
23. }).catch((err: BusinessError) => {
24. console.error(`Failed to set the window orientation. Cause code: ${err.code}, message: ${err.message}`);
25. });
26. } catch (exception) {
27. console.error(`Failed to set window orientation. Cause code: ${exception.code}, message: ${exception.message}`);
28. }
29. });
30. }
31. }
```

## getPreferredOrientation12+

PhonePC/2in1TabletTVWearable

getPreferredOrientation(): Orientation

获取窗口的显示方向属性。未指定方向时，返回window.Orientation.UNSPECIFIED。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Orientation](arkts-apis-window-e.md#orientation9) | 窗口显示方向的属性。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. // ...

9. onWindowStageCreate(windowStage: window.WindowStage) {
10. console.info('onWindowStageCreate');
11. let windowClass: window.Window | undefined = undefined;
12. windowStage.getMainWindow((err: BusinessError, data) => {
13. const errCode: number = err.code;
14. if (errCode) {
15. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
16. return;
17. }
18. windowClass = data;
19. try {
20. let orientation = windowClass.getPreferredOrientation();
21. } catch (exception) {
22. console.error(`Failed to get window orientation. Cause code: ${exception.code}, message: ${exception.message}`);
23. }
24. });
25. }
26. };
```

## getUIContext10+

PhonePC/2in1TabletTVWearable

getUIContext(): UIContext

获取UIContext实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [UIContext](arkts-apis-uicontext-uicontext.md) | 返回UIContext实例对象。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { window, UIContext } from '@kit.ArkUI';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. export default class EntryAbility extends UIAbility {
7. onWindowStageCreate(windowStage: window.WindowStage) {
8. // 为主窗口加载对应的目标页面。
9. windowStage.loadContent("pages/page2", (err: BusinessError) => {
10. let errCode: number = err.code;
11. if (errCode) {
12. console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
13. return;
14. }
15. console.info('Succeeded in loading the content.');
16. // 获取应用主窗口。
17. let windowClass: window.Window | undefined = undefined;
18. windowStage.getMainWindow((err: BusinessError, data) => {
19. let errCode: number = err.code;
20. if (errCode) {
21. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
22. return;
23. }
24. windowClass = data;
25. console.info('Succeeded in obtaining the main window. Data: ' + JSON.stringify(data));
26. // 获取UIContext实例。
27. let uiContext: UIContext | null = null;
28. uiContext = windowClass.getUIContext();
29. });
30. });
31. }
32. };
```

## setUIContent9+

PhonePC/2in1TabletTVWearable

setUIContent(path: string, callback: AsyncCallback<void>): void

根据当前工程中指定的某个页面路径为窗口加载具体页面内容，使用callback异步回调。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 要加载到窗口中的页面内容的路径，Stage模型下该路径需添加到工程的main\_pages.json文件中，FA模型下该路径需添加到工程的config.json文件中。不支持相对路径写法，需与main\_pages.json或config.json中的src取值保持一致。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. windowClass.setUIContent('pages/page2/page3', (err: BusinessError) => {
5. const errCode: number = err.code;
6. if (errCode) {
7. console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
8. return;
9. }
10. console.info('Succeeded in loading the content.');
11. });
12. } catch (exception) {
13. console.error(`Failed to load the content. Cause code: ${exception.code}, message: ${exception.message}`);
14. }
```

## setUIContent9+

PhonePC/2in1TabletTVWearable

setUIContent(path: string): Promise<void>

根据当前工程中指定的某个页面路径为窗口加载具体页面内容，使用Promise异步回调。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 要加载到窗口中的页面内容的路径，Stage模型下该路径需添加到工程的main\_pages.json文件中，FA模型下该路径需添加到工程的config.json文件中。不支持相对路径写法，需与main\_pages.json或config.json中的src取值保持一致。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let promise = windowClass.setUIContent('pages/page2/page3');
5. promise.then(() => {
6. console.info('Succeeded in loading the content.');
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
9. });
10. } catch (exception) {
11. console.error(`Failed to load the content. Cause code: ${exception.code}, message: ${exception.message}`);
12. }
```

## loadContent9+

PhonePC/2in1TabletTVWearable

loadContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void

根据当前工程中指定的页面路径为窗口加载具体页面内容，通过LocalStorage传递状态属性给加载的页面，使用callback异步回调。

建议在UIAbility启动过程中使用该接口，重复调用将先销毁旧的页面内容（即UIContent）再加载新的页面内容，请谨慎使用。

当前UI的执行上下文可能不明确，所以不建议在本接口的回调函数中做UI相关的操作。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 要加载到窗口中的页面内容的路径，该路径需添加到工程的main\_pages.json文件中。不支持相对路径写法，需与main\_pages.json中的src取值保持一致。 |
| storage | [LocalStorage](../harmonyos-guides/arkts-localstorage.md) | 是 | 页面级UI状态存储单元，这里用于为加载到窗口的页面内容传递状态属性。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Invalid path parameter. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let storage: LocalStorage = new LocalStorage();
4. storage.setOrCreate('storageSimpleProp', 121);
5. windowClass.loadContent('pages/page2', storage, (err: BusinessError) => {
6. const errCode: number = err.code;
7. if (errCode) {
8. console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
9. return;
10. }
11. console.info('Succeeded in loading the content.');
12. });
```

## loadContent9+

PhonePC/2in1TabletTVWearable

loadContent(path: string, storage: LocalStorage): Promise<void>

根据当前工程中指定的页面路径为窗口加载具体页面内容，通过LocalStorage传递状态属性给加载的页面，使用Promise异步回调。

建议在UIAbility启动过程中使用该接口，重复调用将先销毁旧的页面内容（即UIContent）再加载新的页面内容，请谨慎使用。

当前UI的执行上下文可能不明确，所以不建议在本接口的回调函数中做UI相关的操作。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 要加载到窗口中的页面内容的路径，该路径需添加到工程的main\_pages.json文件中。不支持相对路径写法，需与main\_pages.json中的src取值保持一致。 |
| storage | [LocalStorage](../harmonyos-guides/arkts-localstorage.md) | 是 | 页面级UI状态存储单元，这里用于为加载到窗口的页面内容传递状态属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Invalid path parameter. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let storage: LocalStorage = new LocalStorage();
4. storage.setOrCreate('storageSimpleProp', 121);
5. let promise = windowClass.loadContent('pages/page2', storage);
6. promise.then(() => {
7. console.info('Succeeded in loading the content.');
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
10. });
```

## loadContentByName11+

PhonePC/2in1TabletTVWearable

loadContentByName(name: string, storage: LocalStorage, callback: AsyncCallback<void>): void

根据指定路由页面名称为当前窗口加载[命名路由](../harmonyos-guides/arkts-routing.md#命名路由)页面，通过LocalStorage传递状态属性至加载页面，使用callback异步回调。

建议在UIAbility启动过程中使用该接口，重复调用该接口将先销毁旧的页面内容（即UIContent）再加载新的页面内容，请谨慎使用。

当前UI的执行上下文可能不明确，所以不建议在本接口的回调函数中做UI相关的操作。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 命名路由页面的名称。 |
| storage | [LocalStorage](../harmonyos-guides/arkts-localstorage.md) | 是 | 页面级UI状态存储单元，这里用于为加载到窗口的页面内容传递状态属性。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. // EntryAbility.ets

3. import { window } from '@kit.ArkUI';
4. import { UIAbility } from '@kit.AbilityKit';
5. import { BusinessError } from '@kit.BasicServicesKit';
6. import * as Index from '../pages/Index'; // 导入命名路由页面

8. export default class EntryAbility extends UIAbility {
9. onWindowStageCreate(windowStage: window.WindowStage) {
10. console.info('onWindowStageCreate');
11. let storage: LocalStorage = new LocalStorage();
12. let newValue: Number = 121;
13. storage.setOrCreate('storageSimpleProp', newValue);
14. try {
15. let windowClass: window.Window = windowStage.getMainWindowSync();
16. if (!windowClass) {
17. console.error('Failed to get main window.');
18. return;
19. }
20. windowClass.loadContentByName(Index.entryName, storage, (err: BusinessError) => {
21. const errCode: number = err?.code;
22. if (errCode) {
23. console.error(`Failed to load the content. Cause code: ${err?.code}, message: ${err?.message}`);
24. return;
25. }
26. console.info('Succeeded in loading the content.');
27. });
28. } catch (exception) {
29. console.error(`Failed to load the content. Cause code: ${exception.code}, message: ${exception.message}`);
30. }
31. }
32. }
```

```
1. // ets/pages/Index.ets
2. export const entryName : string = 'Index';
3. @Entry({routeName: entryName, useSharedStorage: true})
4. @Component
5. export struct Index {
6. @State message: string = 'Hello World'
7. @LocalStorageLink('storageSimpleProp') storageSimpleProp: number = 1;
8. build() {
9. Row() {
10. Column() {
11. Text(this.message)
12. .fontSize(50)
13. .fontWeight(FontWeight.Bold)
14. }
15. .width('100%')
16. }
17. .height('100%')
18. }
19. }
```

## loadContentByName11+

PhonePC/2in1TabletTVWearable

loadContentByName(name: string, callback: AsyncCallback<void>): void

根据指定路由页面名称为当前窗口加载[命名路由](../harmonyos-guides/arkts-routing.md#命名路由)页面，使用callback异步回调。

建议在UIAbility启动过程中使用该接口，重复调用该接口将先销毁旧的页面内容（即UIContent）再加载新的页面内容，请谨慎使用。

当前UI的执行上下文可能不明确，所以不建议在本接口的回调函数中做UI相关的操作。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 命名路由页面的名称。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import * as Index from '../pages/Index'; // 导入命名路由页面

4. try {
5. (windowClass as window.Window).loadContentByName(Index.entryName, (err: BusinessError) => {
6. const errCode: number = err.code;
7. if (errCode) {
8. console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
9. return;
10. }
11. console.info('Succeeded in loading the content.');
12. });
13. } catch (exception) {
14. console.error(`Failed to load the content. Cause code: ${exception.code}, message: ${exception.message}`);
15. }
```

```
1. // ets/pages/Index.ets
2. export const entryName : string = 'Index';
3. @Entry({routeName: entryName})
4. @Component
5. export struct Index {
6. @State message: string = 'Hello World'
7. build() {
8. Row() {
9. Column() {
10. Text(this.message)
11. .fontSize(50)
12. .fontWeight(FontWeight.Bold)
13. }
14. .width('100%')
15. }
16. .height('100%')
17. }
18. }
```

## loadContentByName11+

PhonePC/2in1TabletTVWearable

loadContentByName(name: string, storage?: LocalStorage): Promise<void>

根据指定路由页面名称为当前窗口加载[命名路由](../harmonyos-guides/arkts-routing.md#命名路由)页面，通过LocalStorage传递状态属性至加载页面，使用Promise异步回调。

建议在UIAbility启动过程中使用该接口，重复调用该接口将先销毁旧的页面内容（即UIContent）再加载新的页面内容，请谨慎使用。

当前UI的执行上下文可能不明确，所以不建议在本接口的回调函数中做UI相关的操作。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 命名路由页面的名称。 |
| storage | [LocalStorage](../harmonyos-guides/arkts-localstorage.md) | 否 | 页面级UI状态存储单元，这里用于为加载到窗口的页面内容传递状态属性，默认值为空。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import * as Index from '../pages/Index'; // 导入命名路由页面

4. let storage: LocalStorage = new LocalStorage();
5. storage.setOrCreate('storageSimpleProp', 121);
6. try {
7. let promise = (windowClass as window.Window).loadContentByName(Index.entryName, storage);
8. promise.then(() => {
9. console.info('Succeeded in loading the content.');
10. }).catch((err: BusinessError) => {
11. console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
12. });
13. } catch (exception) {
14. console.error(`Failed to load the content. Cause code: ${exception.code}, message: ${exception.message}`);
15. }
```

```
1. // ets/pages/Index.ets
2. export const entryName : string = 'Index';
3. @Entry({routeName: entryName, useSharedStorage: true})
4. @Component
5. export struct Index {
6. @State message: string = 'Hello World'
7. @LocalStorageLink('storageSimpleProp') storageSimpleProp: number = 1;
8. build() {
9. Row() {
10. Column() {
11. Text(this.message)
12. .fontSize(50)
13. .fontWeight(FontWeight.Bold)
14. }
15. .width('100%')
16. }
17. .height('100%')
18. }
19. }
```

## isWindowShowing9+

PhonePC/2in1TabletTVWearable

isWindowShowing(): boolean

判断当前窗口是否已显示。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 当前窗口是否已显示。true表示当前窗口已显示，false则表示当前窗口未显示。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```
1. try {
2. let data = windowClass.isWindowShowing();
3. console.info('Succeeded in checking whether the window is showing. Data: ' + JSON.stringify(data));
4. } catch (exception) {
5. console.error(`Failed to check whether the window is showing. Cause code: ${exception.code}, message: ${exception.message}`);
6. }
```

## on('windowSizeChange')7+

PhonePC/2in1TabletTVWearable

on(type: 'windowSizeChange', callback: Callback<Size>): void

开启窗口尺寸变化的监听。仅在主线程调用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowSizeChange'，即窗口尺寸变化事件。 |
| callback | Callback<[Size](arkts-apis-window-i.md#size7)> | 是 | 回调函数。返回当前的窗口尺寸。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. try {
2. windowClass.on('windowSizeChange', (data) => {
3. console.info('Succeeded in enabling the listener for window size changes. Data: ' + JSON.stringify(data));
4. });
5. } catch (exception) {
6. console.error(`Failed to enable the listener for window size changes. Cause code: ${exception.code}, message: ${exception.message}`);
7. }
```

## off('windowSizeChange')7+

PhonePC/2in1TabletTVWearable

off(type: 'windowSizeChange', callback?: Callback<Size>): void

关闭窗口尺寸变化的监听。仅在主线程调用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowSizeChange'，即窗口尺寸变化事件。 |
| callback | Callback<[Size](arkts-apis-window-i.md#size7)> | 否 | 回调函数。返回当前的窗口尺寸。如果传入参数，则关闭该监听。如果未传入参数，则关闭窗口尺寸变化的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```
1. const callback = (size: window.Size) => {
2. // ...
3. }
4. try {
5. // 通过on接口开启监听
6. windowClass.on('windowSizeChange', callback);
7. // 关闭指定callback的监听
8. windowClass.off('windowSizeChange', callback);
9. // 如果通过on开启多个callback进行监听，同时关闭所有监听：
10. windowClass.off('windowSizeChange');
11. } catch (exception) {
12. console.error(`Failed to disable the listener for window size changes. Cause code: ${exception.code}, message: ${exception.message}`);
13. }
```

## on('avoidAreaChange')9+

PhonePC/2in1TabletTVWearable

on(type: 'avoidAreaChange', callback: Callback<AvoidAreaOptions>): void

开启当前应用窗口系统避让区域变化的监听。

主窗口/子窗口：

* [自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的自由悬浮窗口模式（即窗口模式为[window.WindowStatusType.FLOATING](arkts-apis-window-e.md#windowstatustype11)）下触发回调时，仅存在固定态软键盘（[AvoidAreaType](arkts-apis-window-e.md#avoidareatype7)为TYPE\_KEYBOARD）类型的避让区域。
* 主窗口在非自由窗口状态的自由悬浮窗口模式下触发回调时，仅存在系统栏（[AvoidAreaType](arkts-apis-window-e.md#avoidareatype7)为TYPE\_SYSTEM）类型的避让区域。
* 主窗口在其余场景下触发回调时，仅当在非自由悬浮窗口模式下或设备类型为Phone和Tablet，才能返回计算后的避让区域，否则直接返回空的避让区域。
* 子窗口在非自由窗口状态或非自由悬浮窗口模式下触发回调时，仅当子窗口的位置和大小与主窗口一致时，才能返回计算后的子窗口避让区域，否则直接返回空的避让区域。

全局悬浮窗、模态窗或系统窗口：

* 仅在调用[setSystemAvoidAreaEnabled](arkts-apis-window-window.md#setsystemavoidareaenabled18)方法使能后，触发回调时才能返回计算后的避让区域，否则直接返回空的避让区域。

常见的触发避让区回调的场景如下：应用窗口在全屏模式、悬浮模式、分屏模式之间的切换；应用窗口旋转；可折叠设备在屏幕折叠状态发生变化；应用窗口在多设备之间的流转。实现沉浸式布局可参考[开发应用沉浸式效果](../harmonyos-guides/arkts-develop-apply-immersive-effects.md)。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'avoidAreaChange'，即系统避让区变化事件。 |
| callback | Callback<[AvoidAreaOptions](arkts-apis-window-i.md#avoidareaoptions12)> | 是 | 回调函数。返回当前避让区以及避让区类型。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. try {
2. windowClass.on('avoidAreaChange', (data) => {
3. console.info('Succeeded in enabling the listener for system avoid area changes. type:' +
4. JSON.stringify(data.type) + ', area: ' + JSON.stringify(data.area));
5. });
6. } catch (exception) {
7. console.error(`Failed to enable the listener for system avoid area changes. Cause code: ${exception.code}, message: ${exception.message}`);
8. }
```

## off('avoidAreaChange')9+

PhonePC/2in1TabletTVWearable

off(type: 'avoidAreaChange', callback?: Callback<AvoidAreaOptions>): void

关闭当前窗口系统避让区变化的监听。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'avoidAreaChange'，即系统避让区变化事件。 |
| callback | Callback<[AvoidAreaOptions](arkts-apis-window-i.md#avoidareaoptions12)> | 否 | 回调函数。返回当前避让区以及避让区类型。如果传入参数，则关闭该监听。如果未传入参数，则关闭所有系统避让区变化的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```
1. interface Param {
2. type: window.AvoidAreaType,
3. area: window.AvoidArea
4. }
5. const callback = (data: Param) => {
6. // ...
7. }
8. try {
9. windowClass.on('avoidAreaChange', callback);

11. windowClass.off('avoidAreaChange', callback);
12. // 如果通过on开启多个callback进行监听，同时关闭所有监听：
13. windowClass.off('avoidAreaChange');
14. } catch (exception) {
15. console.error(`Failed to enable or disable the listener for system avoid area changes. Cause code: ${exception.code}, message: ${exception.message}`);
16. }
```

## on('keyboardHeightChange')7+

PhonePC/2in1TabletTVWearable

on(type: 'keyboardHeightChange', callback: Callback<number>): void

开启固定态软键盘高度变化的监听。当软键盘从本窗口唤出且与窗口有重叠区域时，通知键盘高度变化。从API version 10开始，有关将软键盘设置为固定态或悬浮态的方法，请参见[输入法服务](js-apis-inputmethodengine.md#changeflag10)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'keyboardHeightChange'，即键盘高度变化事件。 |
| callback | Callback<number> | 是 | 回调函数。返回当前的键盘高度。返回值为整数，单位为px。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. windowClass.on('keyboardHeightChange', (data) => {
5. console.info('Succeeded in enabling the listener for keyboard height changes. Data: ' + JSON.stringify(data));
6. });
7. } catch (exception) {
8. console.error(`Failed to enable the listener for keyboard height changes. Cause code: ${exception.code}, message: ${exception.message}`);
9. }
```

## off('keyboardHeightChange')7+

PhonePC/2in1TabletTVWearable

off(type: 'keyboardHeightChange', callback?: Callback<number>): void

关闭固定态软键盘高度变化的监听，使应用程序不再接收键盘高度变化的通知。从API version 10开始，有关将软键盘设置为固定态或悬浮态的方法，请参见[输入法服务](js-apis-inputmethodengine.md#changeflag10)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'keyboardHeightChange'，即键盘高度变化事件。 |
| callback | Callback<number> | 否 | 回调函数。返回当前的键盘高度，返回值为整数，单位为px。若传入参数，则关闭该监听；未传入参数，则关闭所有固定态软键盘高度变化的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const callback = (height: number) => {
4. // ...
5. }
6. try {
7. windowClass.on('keyboardHeightChange', callback);

9. windowClass.off('keyboardHeightChange', callback);
10. // 如果通过on开启多个callback进行监听，同时关闭所有监听：
11. windowClass.off('keyboardHeightChange');
12. } catch (exception) {
13. console.error(`Failed to disable the listener for keyboard height changes. Cause code: ${exception.code}, message: ${exception.message}`);
14. }
```

## on('keyboardWillShow')20+

PhonePC/2in1TabletTVWearable

on(type: 'keyboardWillShow', callback: Callback<KeyboardInfo>): void

开启固定态软键盘即将开始显示的监听。此监听在固定态软键盘即将开始显示或软键盘由悬浮态切换为固定态时触发，此监听仅对当前拉起或隐藏固定态软键盘的应用窗口生效。对于虚拟屏上应用拉起输入法键盘到主屏上，输入法键盘显隐通知只会给主屏上获焦窗口，而不是虚拟屏上应用窗口。

改变软键盘为固定态或者悬浮态方法详细介绍请参见[输入法服务](js-apis-inputmethodengine.md#changeflag10)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'keyboardWillShow'，即固定态软键盘即将开始显示的事件。 |
| callback | Callback<[KeyboardInfo](arkts-apis-window-i.md#keyboardinfo18)> | 是 | 回调函数。返回软键盘窗口信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function keyboardWillShow can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const callback = (keyboardInfo: window.KeyboardInfo) => {
4. console.info(`Keyboard will show animation. keyboardInfo: ` + JSON.stringify(keyboardInfo));
5. }
6. try {
7. windowClass.on('keyboardWillShow', callback);
8. console.info(`Register keyboard will show animation success`);
9. } catch (exception) {
10. console.error(`Failed to register or unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
11. }
```

## off('keyboardWillShow')20+

PhonePC/2in1TabletTVWearable

off(type: 'keyboardWillShow', callback?: Callback<KeyboardInfo>): void

关闭固定态软键盘即将开始显示的监听。改变输入法窗口为固定态或者悬浮态方法详细介绍请参见[输入法服务](js-apis-inputmethodengine.md#changeflag10)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'keyboardWillShow'，即固定态软键盘即将开始显示的事件。 |
| callback | Callback<[KeyboardInfo](arkts-apis-window-i.md#keyboardinfo18)> | 否 | 回调函数。返回软键盘窗口信息。若传入参数，则关闭该监听。如果未传入参数，则关闭所有固定态软键盘即将开始显示的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function keyboardWillShow can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const callback = (keyboardInfo: window.KeyboardInfo) => {
4. console.info(`Keyboard will show animation. keyboardInfo: ` + JSON.stringify(keyboardInfo));
5. }
6. try {
7. windowClass.on('keyboardWillShow', callback);
8. windowClass.off('keyboardWillShow', callback);
9. // 如果通过on开启多个callback进行监听，同时关闭所有监听：
10. windowClass.off('keyboardWillShow');
11. console.info(`Unregister keyboard will show animation success`);
12. } catch (exception) {
13. console.error(`Failed to register or unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
14. }
```

## on('keyboardWillHide')20+

PhonePC/2in1TabletTVWearable

on(type: 'keyboardWillHide', callback: Callback<KeyboardInfo>): void

开启固定态软键盘即将开始隐藏的监听。此监听在固定态软键盘即将开始隐藏或软键盘由固定态切换为悬浮态时触发，此监听仅对当前拉起或隐藏固定态软键盘的应用窗口生效。对于虚拟屏上应用拉起输入法键盘到主屏上，输入法键盘显隐通知只会给主屏上获焦窗口，而不是虚拟屏上应用窗口。

改变软键盘为固定态或者悬浮态方法详细介绍请参见[输入法服务](js-apis-inputmethodengine.md#changeflag10)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'keyboardWillHide'，即固定态软键盘即将开始隐藏的事件。 |
| callback | Callback<[KeyboardInfo](arkts-apis-window-i.md#keyboardinfo18)> | 是 | 回调函数。返回软键盘窗口信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function keyboardWillHide can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const callback = (keyboardInfo: window.KeyboardInfo) => {
4. console.info(`Keyboard will hide animation. keyboardInfo: ` + JSON.stringify(keyboardInfo));
5. }
6. try {
7. windowClass.on('keyboardWillHide', callback);
8. console.info(`Register keyboard will hide animation success`);
9. } catch (exception) {
10. console.error(`Failed to register or unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
11. }
```

## off('keyboardWillHide')20+

PhonePC/2in1TabletTVWearable

off(type: 'keyboardWillHide', callback?: Callback<KeyboardInfo>): void

关闭固定态软键盘即将开始隐藏的监听。改变输入法窗口为固定态切换至悬浮态方法详细介绍请参见[输入法服务](js-apis-inputmethodengine.md#changeflag10)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'keyboardWillHide'，即固定态软键盘即将开始隐藏的事件。 |
| callback | Callback<[KeyboardInfo](arkts-apis-window-i.md#keyboardinfo18)> | 否 | 回调函数。返回软键盘窗口信息。若传入参数，则关闭该监听。如果未传入参数，则关闭所有固定态软键盘即将开始隐藏的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function keyboardWillHide can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const callback = (keyboardInfo: window.KeyboardInfo) => {
4. console.info(`Keyboard will hide animation. keyboardInfo: ` + JSON.stringify(keyboardInfo));
5. }
6. try {
7. windowClass.on('keyboardWillHide', callback);
8. windowClass.off('keyboardWillHide', callback);
9. // 如果通过on开启多个callback进行监听，同时关闭所有监听：
10. windowClass.off('keyboardWillHide');
11. console.info(`Unregister keyboard will hide animation success`);
12. } catch (exception) {
13. console.error(`Failed to register or unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
14. }
```

## on('keyboardDidShow')18+

PhonePC/2in1TabletTVWearable

on(type: 'keyboardDidShow', callback: Callback<KeyboardInfo>): void

开启固定态软键盘显示动画完成的监听。此监听在固定态软键盘显示动画完成或软键盘由悬浮态切换至固定态时触发，此监听仅对当前拉起或隐藏固定态软键盘的应用窗口生效。对于虚拟屏上应用拉起输入法键盘到主屏上，输入法键盘显隐通知只会给主屏上获焦窗口，而不是虚拟屏上应用窗口。

改变软键盘为固定态或者悬浮态方法详细介绍请参见[输入法服务](js-apis-inputmethodengine.md#changeflag10)。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'keyboardDidShow'，即固定态软键盘显示动画完成事件。 |
| callback | Callback<[KeyboardInfo](arkts-apis-window-i.md#keyboardinfo18)> | 是 | 回调函数。返回软键盘窗口信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function keyboardDidShow can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. windowClass.on('keyboardDidShow', (keyboardInfo) => {
5. console.info('keyboard show animation completion. keyboardInfo: ' + JSON.stringify(keyboardInfo));
6. });
7. } catch (exception) {
8. console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
9. }
```

## off('keyboardDidShow')18+

PhonePC/2in1TabletTVWearable

off(type: 'keyboardDidShow', callback?: Callback<KeyboardInfo>): void

关闭固定态软键盘显示动画完成的监听。改变输入法窗口为固定态或者悬浮态方法详细介绍请参见[输入法服务](js-apis-inputmethodengine.md#changeflag10)。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'keyboardDidShow'，即固定态软键盘显示动画完成事件。 |
| callback | Callback<[KeyboardInfo](arkts-apis-window-i.md#keyboardinfo18)> | 否 | 回调函数。返回软键盘窗口信息。若传入参数，则关闭该监听。如果未传入参数，则关闭所有固定态软键盘显示动画完成的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function keyboardDidShow can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const callback = (keyboardInfo: window.KeyboardInfo) => {
4. // ...
5. }
6. try {
7. windowClass.on('keyboardDidShow', callback);
8. windowClass.off('keyboardDidShow', callback);
9. // 如果通过on开启多个callback进行监听，同时关闭所有监听：
10. windowClass.off('keyboardDidShow');
11. } catch (exception) {
12. console.error(`Failed to register or unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
13. }
```

## on('keyboardDidHide')18+

PhonePC/2in1TabletTVWearable

on(type: 'keyboardDidHide', callback: Callback<KeyboardInfo>): void

开启固定态软键盘隐藏动画完成的监听。此监听在固定态软键盘隐藏动画完成或软键盘由固定态切换至悬浮态时触发，此监听仅对当前拉起或隐藏固定态软键盘的应用窗口生效。对于虚拟屏上应用拉起输入法键盘到主屏上，输入法键盘显隐通知只会给主屏上获焦窗口，而不是虚拟屏上应用窗口。

改变软键盘为固定态或者悬浮态方法详细介绍请参见[输入法服务](js-apis-inputmethodengine.md#changeflag10)。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'keyboardDidHide'，即固定态软键盘隐藏动画完成事件。 |
| callback | Callback<[KeyboardInfo](arkts-apis-window-i.md#keyboardinfo18)> | 是 | 回调函数。返回软键盘窗口信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function keyboardDidHide can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. windowClass.on('keyboardDidHide', (keyboardInfo) => {
5. console.info('keyboard hide animation completion. keyboardInfo: ' + JSON.stringify(keyboardInfo));
6. });
7. } catch (exception) {
8. console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
9. }
```

## off('keyboardDidHide')18+

PhonePC/2in1TabletTVWearable

off(type: 'keyboardDidHide', callback?: Callback<KeyboardInfo>): void

关闭固定态软键盘隐藏动画完成的监听。改变输入法窗口为固定态切换至悬浮态方法详细介绍请参见[输入法服务](js-apis-inputmethodengine.md#changeflag10)。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'keyboardDidHide'，即固定态软键盘隐藏动画完成事件。 |
| callback | Callback<[KeyboardInfo](arkts-apis-window-i.md#keyboardinfo18)> | 否 | 回调函数。返回软键盘窗口信息。若传入参数，则关闭该监听。如果未传入参数，则关闭所有固定态软键盘隐藏动画完成的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function keyboardDidHide can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const callback = (keyboardInfo: window.KeyboardInfo) => {
4. // ...
5. }
6. try {
7. windowClass.on('keyboardDidHide', callback);
8. windowClass.off('keyboardDidHide', callback);
9. // 如果通过on开启多个callback进行监听，同时关闭所有监听：
10. windowClass.off('keyboardDidHide');
11. } catch (exception) {
12. console.error(`Failed to register or unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
13. }
```

## on('touchOutside')11+

PhonePC/2in1TabletTVWearable

on(type: 'touchOutside', callback: Callback<void>): void

开启本窗口区域范围外的点击事件的监听。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'touchOutside'，即本窗口范围外的点击事件。 |
| callback | Callback<void> | 是 | 回调函数。当点击事件发生在本窗口范围之外的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. try {
2. windowClass.on('touchOutside', () => {
3. console.info('touch outside');
4. });
5. } catch (exception) {
6. console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
7. }
```

## off('touchOutside')11+

PhonePC/2in1TabletTVWearable

off(type: 'touchOutside', callback?: Callback<void>): void

关闭本窗口区域范围外的点击事件的监听。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'touchOutside'，即本窗口范围外的点击事件。 |
| callback | Callback<void> | 否 | 回调函数。当点击事件发生在本窗口范围之外的回调。如果传入参数，则关闭该监听。如果未传入参数，则关闭所有本窗口区域范围外的点击事件的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```
1. const callback = () => {
2. // ...
3. }
4. try {
5. windowClass.on('touchOutside', callback);
6. windowClass.off('touchOutside', callback);
7. // 如果通过on开启多个callback进行监听，同时关闭所有监听：
8. windowClass.off('touchOutside');
9. } catch (exception) {
10. console.error(`Failed to register or unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
11. }
```

## on('screenshot')9+

PhonePC/2in1TabletTVWearable

on(type: 'screenshot', callback: Callback<void>): void

开启截屏事件的监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'screenshot'，即截屏事件，对控制中心截屏、hdc命令截屏、整屏截屏接口生效。 |
| callback | Callback<void> | 是 | 回调函数。发生截屏事件时的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. try {
2. windowClass.on('screenshot', () => {
3. console.info('screenshot happened');
4. });
5. } catch (exception) {
6. console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
7. }
```

## off('screenshot')9+

PhonePC/2in1TabletTVWearable

off(type: 'screenshot', callback?: Callback<void>): void

关闭截屏事件的监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'screenshot'，即截屏事件。 |
| callback | Callback<void> | 否 | 回调函数。发生截屏事件时的回调。若传入参数，则关闭该监听。若未传入参数，则关闭所有截屏事件的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```
1. let callback = () => {
2. console.info('screenshot happened');
3. };
4. try {
5. windowClass.on('screenshot', callback);
6. windowClass.off('screenshot', callback);
7. // 如果通过on开启多个callback进行监听，同时关闭所有监听：
8. windowClass.off('screenshot');
9. } catch (exception) {
10. console.error(`Failed to register or unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
11. }
```

## on('screenshotAppEvent')20+

PhonePC/2in1TabletTVWearable

on(type: 'screenshotAppEvent', callback: Callback<ScreenshotEventType>): void

开启屏幕截屏事件类型的监听。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'screenshotAppEvent'，即屏幕截屏的事件类型，对控制中心截屏、快捷键截屏以及滚动截屏生效。 |
| callback | Callback<[ScreenshotEventType](arkts-apis-window-e.md#screenshoteventtype20)> | 是 | 回调函数。返回触发的截屏事件类型。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. const callback = (eventType: window.ScreenshotEventType) => {
2. console.info(`screenshotAppEvent happened. Event: ${eventType}`);
3. }
4. try {
5. windowClass.on('screenshotAppEvent', callback);
6. } catch (exception) {
7. console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
8. }
```

## off('screenshotAppEvent')20+

PhonePC/2in1TabletTVWearable

off(type: 'screenshotAppEvent', callback?: Callback<ScreenshotEventType>): void

关闭屏幕截屏事件类型的监听。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'screenshotAppEvent'，即屏幕截屏的事件类型。 |
| callback | Callback<[ScreenshotEventType](arkts-apis-window-e.md#screenshoteventtype20)> | 否 | 回调函数。返回触发的截屏事件类型。若传入参数，则关闭该监听。若未传入参数，则关闭所有窗口截图事件的监听。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. const callback = (eventType: window.ScreenshotEventType) => {
2. // ...
3. }
4. try {
5. // 通过on接口开启监听
6. windowClass.on('screenshotAppEvent', callback);
7. // 关闭指定callback的监听
8. windowClass.off('screenshotAppEvent', callback);
9. // 如果通过on开启多个callback进行监听，同时关闭所有监听：
10. windowClass.off('screenshotAppEvent');
11. } catch (exception) {
12. console.error(`Failed to unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
13. }
```

## on('dialogTargetTouch')10+

PhonePC/2in1TabletTVWearable

on(type: 'dialogTargetTouch', callback: Callback<void>): void

开启模态窗口所遮盖窗口的点击或触摸事件的监听，除模态窗口以外其他窗口调用此接口不生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'dialogTargetTouch'，即模态窗口所遮盖窗口的点击或触摸事件。 |
| callback | Callback<void> | 是 | 回调函数。当点击或触摸事件发生在模态窗口所遮盖窗口的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. try {
2. windowClass.on('dialogTargetTouch', () => {
3. console.info('touch dialog target');
4. });
5. } catch (exception) {
6. console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
7. }
```

## off('dialogTargetTouch')10+

PhonePC/2in1TabletTVWearable

off(type: 'dialogTargetTouch', callback?: Callback<void>): void

关闭模态窗口目标窗口的点击事件的监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'dialogTargetTouch'，即模态窗口目标窗口的点击事件。 |
| callback | Callback<void> | 否 | 回调函数。当点击事件发生在模态窗口目标窗口的回调。若传入参数，则关闭该监听。若未传入参数，则关闭所有模态窗口目标窗口的点击事件的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```
1. const callback = () => {
2. // ...
3. }
4. try {
5. windowClass.on('dialogTargetTouch', callback);
6. windowClass.off('dialogTargetTouch', callback);
7. // 如果通过on开启多个callback进行监听，同时关闭所有监听：
8. windowClass.off('dialogTargetTouch');
9. } catch (exception) {
10. console.error(`Failed to register or unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
11. }
```

## on('windowEvent')10+

PhonePC/2in1TabletTVWearable

on(type: 'windowEvent', callback: Callback<WindowEventType>): void

开启窗口生命周期变化的监听。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowEvent'，即窗口生命周期变化事件。 |
| callback | Callback<[WindowEventType](arkts-apis-window-e.md#windoweventtype10)> | 是 | 回调函数。返回当前的窗口生命周期状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. try {
2. windowClass.on('windowEvent', (data) => {
3. console.info('Window event happened. Event:' + JSON.stringify(data));
4. });
5. } catch (exception) {
6. console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
7. }
```

## off('windowEvent')10+

PhonePC/2in1TabletTVWearable

off(type: 'windowEvent', callback?: Callback<WindowEventType>): void

关闭窗口生命周期变化的监听。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowEvent'，即窗口生命周期变化事件。 |
| callback | Callback<[WindowEventType](arkts-apis-window-e.md#windoweventtype10)> | 否 | 回调函数。返回当前的窗口生命周期状态。若传入参数，则关闭该监听。若未传入参数，则关闭所有窗口生命周期变化的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```
1. const callback = (windowEventType: window.WindowEventType) => {
2. // ...
3. }
4. try {
5. // 通过on接口开启监听
6. windowClass.on('windowEvent', callback);
7. // 关闭指定callback的监听
8. windowClass.off('windowEvent', callback);
9. // 如果通过on开启多个callback进行监听，同时关闭所有监听：
10. windowClass.off('windowEvent');
11. } catch (exception) {
12. console.error(`Failed to unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
13. }
```

## on('displayIdChange')14+

PhonePC/2in1TabletTVWearable

on(type: 'displayIdChange', callback: Callback<number>): void

开启本窗口所处屏幕变化事件的监听。比如，当前窗口移动到其他屏幕时，可以从此接口监听到这个行为。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'displayIdChange'，即本窗口所处屏幕变化的事件。 |
| callback | Callback<number> | 是 | 回调函数。当本窗口所处屏幕发生变化后的回调。回调函数返回number类型参数，表示窗口所处屏幕的displayId。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```
1. try {
2. windowClass.on('displayIdChange', (data) => {
3. console.info('Window displayId changed, displayId=' + JSON.stringify(data));
4. });
5. } catch (exception) {
6. console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
7. }
```

## off('displayIdChange')14+

PhonePC/2in1TabletTVWearable

off(type: 'displayIdChange', callback?: Callback<number>): void

关闭本窗口所处屏幕变化事件的监听。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'displayIdChange'，即本窗口所处屏幕变化的事件。 |
| callback | Callback<number> | 否 | 回调函数。当本窗口所处屏幕发生变化时的回调。如果传入参数，则关闭该监听。如果未传入参数，则关闭所有本窗口所处屏幕变化事件的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```
1. const callback = (displayId: number) => {
2. // ...
3. }
4. try {
5. // 通过on接口开启监听
6. windowClass.on('displayIdChange', callback);
7. // 关闭指定callback的监听
8. windowClass.off('displayIdChange', callback);
9. // 如果通过on开启多个callback进行监听，同时关闭所有监听：
10. windowClass.off('displayIdChange');
11. } catch (exception) {
12. console.error(`Failed to unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
13. }
```

## on('windowVisibilityChange')11+

PhonePC/2in1TabletTVWearable

on(type: 'windowVisibilityChange', callback: Callback<boolean>): void

开启本窗口可见状态变化事件的监听。本接口返回的可见性与肉眼所见的可见性可能存在区别，如以下场景：

* 非主窗口的阴影区域（可分别通过[setWindowShadowEnabled](arkts-apis-window-window.md#setwindowshadowenabled20)和[setWindowShadowRadius](arkts-apis-window-window.md#setwindowshadowradius17)设置是否显示阴影以及对应的阴影半径）被挡住也算遮挡，此时肉眼所见虽是完全可见，但实际返回的是部分可见。
* 上层窗口带有透明效果时（包括完全不透明之外的所有透明程度）不会遮挡下层窗口，此时下层窗口是可见的。
* 窗口通过[setWindowMask](arkts-apis-window-window.md#setwindowmask12)接口设置异形窗口蒙层时，不会影响窗口可见状态计算，窗口仍可见，即使掩码全部设置为0，窗口依然按照其原本矩形大小参与可见状态计算。
* 大多数处于动画效果下的窗口也不会遮挡住下层窗口，比如在手机设备上拖动悬浮窗时返回的下层窗口依然是可见的。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowVisibilityChange'，即本窗口可见状态变化的事件。 |
| callback | Callback<boolean> | 是 | 回调函数。当本窗口可见状态发生变化后的回调。回调函数返回boolean类型参数，当返回参数为true时表示窗口可见，否则表示窗口不可见。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. try {
2. windowClass.on('windowVisibilityChange', (boolean) => {
3. console.info('Window visibility changed, isVisible=' + boolean);
4. });
5. } catch (exception) {
6. console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
7. }
```

## off('windowVisibilityChange')11+

PhonePC/2in1TabletTVWearable

off(type: 'windowVisibilityChange', callback?: Callback<boolean>): void

关闭本窗口可见状态变化事件的监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowVisibilityChange'，即本窗口可见状态变化的事件。 |
| callback | Callback<boolean> | 否 | 回调函数。当本窗口可见状态发生变化时的回调。如果传入参数，则关闭该监听。如果未传入参数，则关闭所有本窗口可见状态变化事件的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. const callback = (bool: boolean) => {
2. // ...
3. }
4. try {
5. // 通过on接口开启监听
6. windowClass.on('windowVisibilityChange', callback);
7. // 关闭指定callback的监听
8. windowClass.off('windowVisibilityChange', callback);
9. // 如果通过on开启多个callback进行监听，同时关闭所有监听：
10. windowClass.off('windowVisibilityChange');
11. } catch (exception) {
12. console.error(`Failed to unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
13. }
```

## on('occlusionStateChanged')22+

PhonePC/2in1TabletTVWearable

on(type: 'occlusionStateChanged', callback: Callback<OcclusionState>): void

开启窗口可见性状态变化事件的监听。本接口返回的可见性与肉眼所见的可见性可能存在区别，如以下场景：

* 非主窗口的阴影区域（可分别通过[setWindowShadowEnabled](arkts-apis-window-window.md#setwindowshadowenabled20)和[setWindowShadowRadius](arkts-apis-window-window.md#setwindowshadowradius17)设置是否显示阴影以及对应的阴影半径）被挡住也算遮挡，此时肉眼所见虽是完全可见，但实际返回的是部分可见。
* 上层窗口带有透明效果时（包括完全不透明之外的所有透明程度）不会遮挡下层窗口，此时下层窗口是可见的。
* 窗口通过[setWindowMask](arkts-apis-window-window.md#setwindowmask12)接口设置异形窗口蒙层时，不会影响窗口可见状态计算，窗口仍可见，即使掩码全部设置为0，窗口依然按照其原本矩形大小参与可见状态计算。
* 大多数处于动画效果下的窗口也不会遮挡住下层窗口，比如在手机设备上拖动悬浮窗时返回的下层窗口依然是可见的。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'occlusionStateChanged'，即窗口可见性变化事件。 |
| callback | Callback<[OcclusionState](arkts-apis-window-e.md#occlusionstate22)> | 是 | 窗口可见性变化时的回调函数。详情见[可见性状态](arkts-apis-window-e.md#occlusionstate22)。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. try {
2. let callback: Callback<window.OcclusionState> = (data: window.OcclusionState) => {
3. console.info(`Window occlusion state changed: ${data}`);
4. };
5. windowClass.on('occlusionStateChanged', callback);
6. } catch (exception) {
7. console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
8. }
```

## off('occlusionStateChanged')22+

PhonePC/2in1TabletTVWearable

off(type: 'occlusionStateChanged', callback?: Callback<OcclusionState>): void

关闭窗口可见性状态变化事件的监听。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'occlusionStateChanged'，即窗口可见性变化事件。 |
| callback | Callback<[OcclusionState](arkts-apis-window-e.md#occlusionstate22)> | 否 | 若传入参数，则关闭该监听。若未传入参数，则关闭所有窗口可见性变化的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. try {
2. let callback: Callback<window.OcclusionState> = (data: window.OcclusionState) => {
3. console.info(`Window occlusion state changed: ${data}`);
4. };
5. // 通过on接口开启监听
6. windowClass.on('occlusionStateChanged', callback);
7. // 关闭指定callback的监听
8. windowClass.off('occlusionStateChanged', callback);
9. // 如果通过on开启多个callback进行监听，同时关闭所有监听：
10. windowClass.off('occlusionStateChanged');
11. } catch (exception) {
12. console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
13. }
```

## on('frameMetricsMeasured')22+

PhonePC/2in1TabletTVWearable

on(type: 'frameMetricsMeasured', callback: Callback<FrameMetrics>): void

开启窗口帧率指标变化事件的监听。该接口需要在[loadContent()](arkts-apis-window-window.md#loadcontent9)或[setUIContent()](arkts-apis-window-window.md#setuicontent9)调用生效后使用。

应用注册帧率变化监听后，只有当客户端UI内容发生重绘时（如页面切换、和可响应组件交互、设置背景色和透明度等），才会触发注册的回调。但当同时使用该接口和[postFrameCallback](arkts-apis-uicontext-uicontext.md#postframecallback12)、[postDelayedFrameCallback](arkts-apis-uicontext-uicontext.md#postdelayedframecallback12)、[displaySync.on('frame')](js-apis-graphics-displaysync.md#onframe)中的任意一个时，即使无UI内容重绘，也可能触发回调。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件类型，固定为'frameMetricsMeasured'，即窗口帧率指标变化事件。 |
| callback | Callback<[FrameMetrics](arkts-apis-window-i.md#framemetrics22)> | 是 | 窗口帧率指标变化时的回调函数。详情见帧率指标[FrameMetrics](arkts-apis-window-i.md#framemetrics22)。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```
1. try {
2. let callback: Callback<window.FrameMetrics> = (data: window.FrameMetrics) => {
3. console.info(`Window frame metrics changed: ${JSON.stringify(data)}`);
4. };
5. windowClass.on('frameMetricsMeasured', callback);
6. } catch (exception) {
7. console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
8. }
```

## off('frameMetricsMeasured')22+

PhonePC/2in1TabletTVWearable

off(type: 'frameMetricsMeasured', callback?: Callback<FrameMetrics>): void

关闭窗口帧率指标变化事件的监听。该接口需要在[loadContent()](arkts-apis-window-window.md#loadcontent9)或[setUIContent()](arkts-apis-window-window.md#setuicontent9)调用生效后使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件类型，固定为'frameMetricsMeasured'，即窗口帧率指标变化事件。 |
| callback | Callback<[FrameMetrics](arkts-apis-window-i.md#framemetrics22)> | 否 | 若传入参数，则关闭该监听。若未传入参数，则关闭所有窗口帧率指标变化的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```
1. try {
2. let callback: Callback<window.FrameMetrics> = (data: window.FrameMetrics) => {
3. console.info(`Window frame metrics changed: ${JSON.stringify(data)}`);
4. };
5. // 通过on接口开启监听
6. windowClass.on('frameMetricsMeasured', callback);
7. // 关闭指定callback的监听
8. windowClass.off('frameMetricsMeasured', callback);
9. // 如果通过on开启多个callback进行监听，同时关闭所有监听：
10. windowClass.off('frameMetricsMeasured');
11. } catch (exception) {
12. console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
13. }
```

## on('systemDensityChange')15+

PhonePC/2in1TabletTVWearable

on(type: 'systemDensityChange', callback: Callback<number>): void

开启本窗口所处屏幕的系统显示大小缩放系数变化事件的监听。比如，当调整窗口所处屏幕的显示大小缩放系数时，可以从此接口监听到这个行为。

在接口回调函数中，建议直接使用返回值进行vp和px的转换。例如，若返回值为density，计算px可使用vp \* density = px。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'systemDensityChange'，即本窗口所处屏幕的系统显示大小缩放系数变化的事件。 |
| callback | Callback<number> | 是 | 回调函数。当本窗口所处屏幕的系统显示大小缩放系数发生变化后的回调。回调函数返回number类型参数，表示当前窗口所处屏幕的系统显示大小缩放系数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```
1. const callback = (density: number) => {
2. console.info('System density changed, density=' + JSON.stringify(density));
3. // 通过回调返回值计算px
4. let vp = 100;
5. let px = vp * density;
6. }
7. try {
8. windowClass.on('systemDensityChange', callback);
9. } catch (exception) {
10. console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
11. }
```

## off('systemDensityChange')15+

PhonePC/2in1TabletTVWearable

off(type: 'systemDensityChange', callback?: Callback<number>): void

关闭本窗口所处屏幕的系统显示大小缩放系数变化事件的监听。

在接口回调函数中，建议直接使用返回值进行vp和px的转换。例如，若返回值为density，计算px可使用vp \* density = px。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'systemDensityChange'，即本窗口所处屏幕的系统显示大小缩放系数变化的事件。 |
| callback | Callback<number> | 否 | 回调函数。当本窗口所处屏幕的系统显示大小缩放系数发生变化后的回调。如果传入参数，则关闭该监听。如果未传入参数，则关闭所有本窗口所处屏幕的系统显示大小缩放系数变化事件的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```
1. const callback = (density: number) => {
2. // ...
3. }
4. try {
5. // 通过on接口开启监听
6. windowClass.on('systemDensityChange', callback);
7. // 关闭指定callback的监听
8. windowClass.off('systemDensityChange', callback);
9. // 如果通过on开启多个callback进行监听，同时关闭所有监听：
10. windowClass.off('systemDensityChange');
11. } catch (exception) {
12. console.error(`Failed to unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
13. }
```

## on('noInteractionDetected')12+

PhonePC/2in1TabletTVWearable

on(type: 'noInteractionDetected', timeout: number, callback: Callback<void>): void

开启本窗口在指定超时时间内无交互事件的监听，交互事件支持物理键盘输入事件和屏幕触控点击事件，不支持软键盘输入事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'noInteractionDetected'，即本窗口在指定超时时间内无交互的事件。 |
| timeout | number | 是 | 指定本窗口在多长时间内无交互即回调，单位为秒(s)。该参数仅支持整数输入，负数和小数为非法参数。 |
| callback | Callback<void> | 是 | 回调函数。当本窗口在指定超时时间内无交互事件时的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. try {
2. windowClass.on('noInteractionDetected', 60, () => {
3. console.info('no interaction in 60s');
4. });
5. } catch (exception) {
6. console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
7. }
```

## off('noInteractionDetected')12+

PhonePC/2in1TabletTVWearable

off(type: 'noInteractionDetected', callback?: Callback<void>): void

关闭本窗口在指定超时时间内无交互事件的监听，交互事件支持物理键盘输入事件和屏幕触控点击事件，不支持软键盘输入事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'noInteractionDetected'，即本窗口在指定超时时间内无交互的事件。 |
| callback | Callback<void> | 否 | 回调函数，当本窗口在指定超时时间内无交互事件时的回调。如果传入参数，则关闭该监听。如果未传入参数，则关闭所有本窗口在指定超时时间内无交互事件的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. const callback = () => {
2. // ...
3. }
4. try {
5. windowClass.on('noInteractionDetected', 60, callback);
6. windowClass.off('noInteractionDetected', callback);
7. // 如果通过on开启多个callback进行监听，同时关闭所有监听：
8. windowClass.off('noInteractionDetected');
9. } catch (exception) {
10. console.error(`Failed to register or unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
11. }
```

## on('windowStatusChange')11+

PhonePC/2in1TabletTVWearable

on(type: 'windowStatusChange', callback: Callback<WindowStatusType>): void

开启窗口模式变化的监听，当窗口windowStatus发生变化时进行通知（此时窗口属性可能还没有更新，如果需要在收到windowStatus变化通知时能够立即获取到变化后的窗口大小、位置，建议使用[on('windowStatusDidChange')](arkts-apis-window-window.md#onwindowstatusdidchange20)）。

使用当前接口开启监听后，在调用maximize、recover方法时会收到多次回调，如需获取去重后的回调，可使用[on('windowStatusDidChange')](arkts-apis-window-window.md#onwindowstatusdidchange20)。

说明

在[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态下，应用的[targetAPIVersion](../harmonyos-guides/app-configuration-file.md#配置文件标签)设置小于14时，在窗口最大化状态（窗口铺满整个屏幕，2in1设备会有dock栏和状态栏，Tablet设备会有状态栏）时返回值对应为WindowStatusType::FULL\_SCREEN。应用的[targetAPIVersion](../harmonyos-guides/app-configuration-file.md#配置文件标签)设置大于等于14时，在窗口最大化状态（窗口铺满整个屏幕，2in1设备会有dock栏和状态栏，Tablet设备会有状态栏）时返回值对应为WindowStatusType::MAXIMIZE。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowStatusChange'，即窗口模式变化事件。 |
| callback | Callback<[WindowStatusType](arkts-apis-window-e.md#windowstatustype11)> | 是 | 回调函数。返回当前的窗口模式。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. try {
2. windowClass.on('windowStatusChange', (WindowStatusType) => {
3. console.info('Succeeded in enabling the listener for window status changes. Data: ' + JSON.stringify(WindowStatusType));
4. });
5. } catch (exception) {
6. console.error(`Failed to unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
7. }
```

## off('windowStatusChange')11+

PhonePC/2in1TabletTVWearable

off(type: 'windowStatusChange', callback?: Callback<WindowStatusType>): void

关闭窗口模式变化的监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowStatusChange'，即窗口模式变化事件。 |
| callback | Callback<[WindowStatusType](arkts-apis-window-e.md#windowstatustype11)> | 否 | 回调函数。返回当前的窗口模式。如果传入参数，则关闭该监听。如果未传入参数，则关闭所有窗口模式变化的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. const callback = (windowStatusType: window.WindowStatusType) => {
2. // ...
3. }
4. try {
5. windowClass.on('windowStatusChange', callback);
6. windowClass.off('windowStatusChange', callback);
7. // 如果通过on开启多个callback进行监听，同时关闭所有监听：
8. windowClass.off('windowStatusChange');
9. } catch (exception) {
10. console.error(`Failed to unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
11. }
```

## on('windowStatusDidChange')20+

PhonePC/2in1TabletTVWearable

on(type: 'windowStatusDidChange', callback: Callback<WindowStatusType>): void

开启窗口模式变化的监听，当窗口windowStatus发生变化后进行通知（此时窗口[Rect](arkts-apis-window-i.md#rect7)属性已经完成更新）。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowStatusDidChange'，即窗口模式变化完成事件。 |
| callback | Callback<[WindowStatusType](arkts-apis-window-e.md#windowstatustype11)> | 是 | 回调函数。返回当前的窗口模式。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```
1. try {
2. windowClass.on('windowStatusDidChange', (WindowStatusType) => {
3. console.info(`Succeeded in enabling the listener for window status changes. Data: ${JSON.stringify(WindowStatusType)}`);
4. });
5. } catch (exception) {
6. console.error(`Failed to unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
7. }
```

## off('windowStatusDidChange')20+

PhonePC/2in1TabletTVWearable

off(type: 'windowStatusDidChange', callback?: Callback<WindowStatusType>): void

关闭窗口模式变化的监听。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowStatusDidChange'，即窗口模式变化完成事件。 |
| callback | Callback<[WindowStatusType](arkts-apis-window-e.md#windowstatustype11)> | 否 | 回调函数。返回当前的窗口模式。如果传入参数，则关闭该监听。如果未传入参数，则关闭所有窗口模式变化的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```
1. const callback = (windowStatusType: window.WindowStatusType) => {
2. // ...
3. }
4. try {
5. windowClass.on('windowStatusDidChange', callback);
6. windowClass.off('windowStatusDidChange', callback);
7. // 如果通过on开启多个callback进行监听，同时关闭所有监听：
8. windowClass.off('windowStatusDidChange');
9. } catch (exception) {
10. console.error(`Failed to unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
11. }
```

## setWindowGrayScale12+

PhonePC/2in1TabletTVWearable

setWindowGrayScale(grayScale: number): Promise<void>

设置窗口灰阶，使用Promise异步回调。该接口需要在调用[loadContent()](arkts-apis-window-window.md#loadcontent9)或[setUIContent()](arkts-apis-window-window.md#setuicontent9)使窗口加载页面内容后调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| grayScale | number | 是 | 窗口灰阶。该参数为浮点数，取值范围为[0.0, 1.0]。0.0表示窗口图像无变化，1.0表示窗口图像完全转为灰度图像，0.0至1.0之间时效果呈线性变化。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. windowClass?.setUIContent('pages/Index', (error: BusinessError) => {
4. if (error.code) {
5. console.error(`Failed to set the content. Cause code: ${error.code}`);
6. return;
7. }
8. console.info('Succeeded in setting the content.');
9. let grayScale: number = 0.5;
10. try {
11. if (canIUse("SystemCapability.Window.SessionManager")) {
12. let promise = windowClass?.setWindowGrayScale(grayScale);
13. promise?.then(() => {
14. console.info('Succeeded in setting the grayScale.');
15. }).catch((err: BusinessError) => {
16. console.error(`Failed to set the grayScale. Cause code: ${err.code}, message: ${err.message}`);
17. });
18. }
19. } catch (exception) {
20. console.error(`Failed to set the grayScale. Cause code: ${exception.code}, message: ${exception.message}`);
21. }
22. });
```

## on('windowTitleButtonRectChange')11+

PhonePC/2in1TabletTVWearable

on(type: 'windowTitleButtonRectChange', callback: Callback<TitleButtonRect>): void

开启窗口标题栏上的最小化、最大化、关闭按钮矩形区域变化的监听，对存在标题栏和三键区的窗口形态生效。如果使用Stage模型，该接口需要在[loadContent()](arkts-apis-window-window.md#loadcontent9)或[setUIContent()](arkts-apis-window-window.md#setuicontent9)调用生效后使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowTitleButtonRectChange'，即标题栏上的最小化、最大化、关闭按钮矩形区域变化事件。 |
| callback | Callback<[TitleButtonRect](arkts-apis-window-i.md#titlebuttonrect11)> | 是 | 回调函数。返回当前标题栏上的最小化、最大化、关闭按钮矩形区域。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```
1. windowClass.setUIContent('pages/WindowPage').then(() => {
2. try {
3. windowClass?.on('windowTitleButtonRectChange', (titleButtonRect) => {
4. console.info('Succeeded in enabling the listener for window title buttons area changes. Data: ' + JSON.stringify(titleButtonRect));
5. });
6. } catch (exception) {
7. console.error(`Failed to enable the listener for window title buttons area changes. Cause code: ${exception.code}, message: ${exception.message}`);
8. }
9. })
```

## off('windowTitleButtonRectChange')11+

PhonePC/2in1TabletTVWearable

off(type: 'windowTitleButtonRectChange', callback?: Callback<TitleButtonRect>): void

关闭窗口标题栏上的最小化、最大化、关闭按钮矩形区域变化的监听，对存在标题栏和三键区的窗口形态生效。如果使用Stage模型，该接口需要在[loadContent()](arkts-apis-window-window.md#loadcontent9)或[setUIContent()](arkts-apis-window-window.md#setuicontent9)调用生效后使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowTitleButtonRectChange'，即标题栏上的最小化、最大化、关闭按钮矩形区域变化事件。 |
| callback | Callback<[TitleButtonRect](arkts-apis-window-i.md#titlebuttonrect11)> | 否 | 回调函数。返回当前标题栏上的最小化、最大化、关闭按钮矩形区域。如果传入参数，则关闭该监听。如果未传入参数，则关闭所有标题栏上的最小化、最大化、关闭按钮矩形区域变化的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```
1. windowClass.setUIContent('pages/WindowPage').then(() => {
2. const callback = (titleButtonRect: window.TitleButtonRect) => {
3. // ...
4. }
5. try {
6. // 通过on接口开启监听
7. windowClass?.on('windowTitleButtonRectChange', callback);
8. // 关闭指定callback的监听
9. windowClass?.off('windowTitleButtonRectChange', callback);
10. // 如果通过on开启多个callback进行监听，同时关闭所有监听：
11. windowClass?.off('windowTitleButtonRectChange');
12. } catch (exception) {
13. console.error(`Failed to disable the listener for window title buttons area changes. Cause code: ${exception.code}, message: ${exception.message}`);
14. }
15. })
```

## on('windowRectChange')12+

PhonePC/2in1TabletTVWearable

on(type: 'windowRectChange', callback: Callback<RectChangeOptions>): void

开启窗口矩形（窗口位置及窗口大小）变化的监听。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowRectChange'，即窗口矩形变化事件。 |
| callback | Callback<[RectChangeOptions](arkts-apis-window-i.md#rectchangeoptions12)> | 是 | 回调函数。返回当前窗口矩形变化值及变化原因。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. try {
2. windowClass.on('windowRectChange', (data: window.RectChangeOptions) => {
3. console.info(`Succeeded in enabling the listener for window rect changes. Data: ${JSON.stringify(data)}`);
4. });
5. } catch (exception) {
6. console.error(`Failed to disable the listener for window rect changes. Cause code: ${exception.code}, message: ${exception.message}`);
7. }
```

## off('windowRectChange')12+

PhonePC/2in1TabletTVWearable

off(type: 'windowRectChange', callback?: Callback<RectChangeOptions>): void

关闭窗口矩形（窗口位置及窗口大小）变化的监听。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowRectChange'，即窗口矩形变化事件。 |
| callback | Callback<[RectChangeOptions](arkts-apis-window-i.md#rectchangeoptions12)> | 否 | 回调函数。返回当前的窗口矩形及变化原因。如果传入参数，则关闭该监听。如果未传入参数，则关闭所有窗口矩形变化的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. const callback = (rectChangeOptions: window.RectChangeOptions) => {
2. // ...
3. }

5. try {
6. windowClass.on('windowRectChange', callback);
7. windowClass.off('windowRectChange', callback);
8. // 如果通过on开启多个callback进行监听，同时关闭所有监听：
9. windowClass.off('windowRectChange');
10. } catch (exception) {
11. console.error(`Failed to disable the listener for window rect changes. Cause code: ${exception.code}, message: ${exception.message}`);
12. }
```

## on('rectChangeInGlobalDisplay')20+

PhonePC/2in1TabletTVWearable

on(type: 'rectChangeInGlobalDisplay', callback: Callback<RectChangeOptions>): void

开启[全局坐标系](../harmonyos-guides/window-terminology.md#全局坐标系)下窗口矩形（窗口位置及窗口大小）变化的监听事件。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'rectChangeInGlobalDisplay'，即全局坐标系下窗口矩形变化事件。 |
| callback | Callback<[RectChangeOptions](arkts-apis-window-i.md#rectchangeoptions12)> | 是 | 回调函数。返回当前窗口矩形变化值及变化原因。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. const callback = (rectChangeOptions: window.RectChangeOptions) => {
2. console.info(`Succeeded in enabling the listener for window rect changes in global display. Data: ` + JSON.stringify(rectChangeOptions));
3. }

5. try {
6. windowClass.on('rectChangeInGlobalDisplay', callback);
7. } catch (exception) {
8. console.error(`Failed to enable the listener for window rect changes in global display. Cause code: ${exception.code}, message: ${exception.message}`);
9. }
```

## off('rectChangeInGlobalDisplay')20+

PhonePC/2in1TabletTVWearable

off(type: 'rectChangeInGlobalDisplay', callback?: Callback<RectChangeOptions>): void

关闭[全局坐标系](../harmonyos-guides/window-terminology.md#全局坐标系)下窗口矩形（窗口位置及窗口大小）变化的监听事件。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'rectChangeInGlobalDisplay'，即全局坐标系下窗口矩形变化事件。 |
| callback | Callback<[RectChangeOptions](arkts-apis-window-i.md#rectchangeoptions12)> | 否 | 回调函数。返回当前的窗口矩形及变化原因。如果传入参数，则关闭该监听。如果未传入参数，则关闭所有全局坐标系下窗口矩形变化的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. const callback = (rectChangeOptions: window.RectChangeOptions) => {
2. // ...
3. }

5. try {
6. windowClass.on('rectChangeInGlobalDisplay', callback);
7. windowClass.off('rectChangeInGlobalDisplay', callback);
8. // 如果通过on开启多个callback进行监听，同时关闭所有监听：
9. windowClass.off('rectChangeInGlobalDisplay');
10. } catch (exception) {
11. console.error(`Failed to disable the listener for window rect changes in global display. Cause code: ${exception.code}, message: ${exception.message}`);
12. }
```

## on('subWindowClose')12+

PhonePC/2in1TabletTVWearable

on(type: 'subWindowClose', callback: Callback<void>): void

开启子窗口关闭事件的监听。此监听仅在点击系统提供的右上角关闭按钮关闭子窗时触发，其余关闭方式不触发回调。

当重复注册窗口关闭事件的监听时，最后一次注册成功的监听事件生效。

该接口触发的窗口关闭事件监听回调函数是同步执行，子窗口的异步关闭事件监听参考[on('windowWillClose')](arkts-apis-window-window.md#onwindowwillclose15)方法。

如果存在[on('windowWillClose')](arkts-apis-window-window.md#onwindowwillclose15)监听事件，只响应[on('windowWillClose')](arkts-apis-window-window.md#onwindowwillclose15)接口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'subWindowClose'，即子窗口关闭事件。 |
| callback | Callback<void> | 是 | 回调函数。当点击子窗口右上角关闭按钮事件发生时的回调。该回调函数不返回任何参数。回调函数内部逻辑的返回值决定当前子窗是否继续关闭，如果返回boolean类型的true表示不关闭子窗，返回false或者其他非boolean类型表示关闭子窗。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. |

**示例：**

```
1. const callback = () => {
2. // ...
3. return true;
4. }
5. try {
6. windowClass.on('subWindowClose', callback);
7. } catch (exception) {
8. console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
9. }
```

## off('subWindowClose')12+

PhonePC/2in1TabletTVWearable

off(type: 'subWindowClose', callback?: Callback<void>): void

关闭子窗口关闭事件的监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'subWindowClose'，即子窗口关闭事件。 |
| callback | Callback<void> | 否 | 回调函数。当点击子窗口右上角关闭按钮事件发生时的回调。该回调函数不返回任何参数。回调函数内部逻辑的返回值决定当前子窗是否继续关闭，如果返回boolean类型的true表示不关闭子窗，返回false或者其他非boolean类型表示关闭子窗。如果传入参数，则关闭该监听。如果未传入参数，则关闭所有子窗口关闭的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. |

**示例：**

```
1. const callback = () => {
2. // ...
3. return true;
4. }
5. try {
6. windowClass.on('subWindowClose', callback);
7. windowClass.off('subWindowClose', callback);
8. // 如果通过on开启多个callback进行监听，同时关闭所有监听：
9. windowClass.off('subWindowClose');
10. } catch (exception) {
11. console.error(`Failed to register or unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
12. }
```

## on('windowWillClose')15+

PhonePC/2in1TabletTVWearable

on(type: 'windowWillClose', callback: Callback<void, Promise<boolean>>): void

开启主窗口或子窗口关闭事件的监听。此监听仅能通过系统提供的窗口标题栏关闭按键触发，其余关闭窗口的方式不触发回调。

该接口触发的回调函数是异步执行。子窗口的同步关闭事件监听参考[on('subWindowClose')](arkts-apis-window-window.md#onsubwindowclose12)方法。主窗口的同步关闭事件监听参考[on('windowStageClose')](arkts-apis-window-windowstage.md#onwindowstageclose14)方法。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：**

在HarmonyOS 6.1.0之前，该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备及不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上调用返回801错误码。

从HarmonyOS 6.1.0开始，该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备调用不报错不生效，切换到[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态后生效；在不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备调用不报错不生效。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowWillClose'，即窗口关闭事件。 |
| callback | Callback<void, Promise<boolean>> | 是 | 回调函数。当点击窗口系统提供的右上角关闭按钮事件发生时的回调。该回调函数不返回任何参数。回调函数内部逻辑需要有Promise<boolean>类型的返回值。在返回的Promise函数里，执行resolve(true) 方法表示不关闭当前窗口，执行resolve(false) 方法或者reject方法均表示关闭当前窗口。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { window } from '@kit.ArkUI';

5. export default class EntryAbility extends UIAbility {

7. onWindowStageCreate(windowStage: window.WindowStage) {
8. console.info('onWindowStageCreate');
9. const callback = () => {
10. // ...
11. return new Promise<boolean>((resolve, reject) => {
12. // 是否关闭该窗口
13. let result: boolean = true;
14. resolve(result);
15. });
16. }
17. try {
18. let windowClass = windowStage.getMainWindowSync();
19. windowClass.on('windowWillClose', callback);
20. } catch (exception) {
21. console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
22. }
23. }
24. }
```

## off('windowWillClose')15+

PhonePC/2in1TabletTVWearable

off(type: 'windowWillClose', callback?: Callback<void, Promise<boolean>>): void

用于关闭主窗口或子窗口关闭事件的监听。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：**

在HarmonyOS 6.1.0之前，该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备及不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上调用返回801错误码。

从HarmonyOS 6.1.0开始，该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备调用不报错不生效，切换到[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态后生效；在不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备调用不报错不生效。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowWillClose'，即窗口关闭事件。 |
| callback | Callback<void, Promise<boolean>> | 否 | 回调函数。当点击窗口系统提供的右上角关闭按钮事件发生时的回调。该回调函数不返回任何参数。回调函数内部逻辑需要有Promise<boolean>类型的返回值。在返回的Promise函数里，执行resolve(true) 方法表示不关闭当前窗口，执行resolve(false) 方法或者reject方法均表示关闭当前窗口。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { window } from '@kit.ArkUI';

5. export default class EntryAbility extends UIAbility {

7. onWindowStageCreate(windowStage: window.WindowStage) {
8. console.info('onWindowStageCreate');
9. try {
10. const callback = () => {
11. // ...
12. return new Promise<boolean>((resolve, reject) => {
13. // 是否关闭该窗口
14. let result: boolean = true;
15. resolve(result);
16. });
17. }
18. let windowClass = windowStage.getMainWindowSync();
19. windowClass.on('windowWillClose', callback);
20. windowClass.off('windowWillClose', callback);
21. // 如果通过on开启多个callback进行监听，同时关闭所有监听：
22. windowClass.off('windowWillClose');
23. } catch (exception) {
24. console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
25. }
26. }
27. }
```

## on('windowHighlightChange')15+

PhonePC/2in1TabletTVWearable

on(type: 'windowHighlightChange', callback: Callback<boolean>): void

开启窗口激活态变化事件的监听。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowHighlightChange'，即窗口激活态变化事件。 |
| callback | Callback<boolean> | 是 | 回调函数。当本窗口的激活态发生变化时的回调。回调函数返回boolean类型参数。当返回参数为true表示激活态；false表示非激活态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. try {
2. windowClass.on('windowHighlightChange', (data: boolean) => {
3. console.info(`Window highlight Change: ${data}`);
4. });
5. } catch (exception) {
6. console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
7. }
```

## off('windowHighlightChange')15+

PhonePC/2in1TabletTVWearable

off(type: 'windowHighlightChange', callback?: Callback<boolean>): void

关闭窗口激活态变化事件的监听。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowHighlightChange'，即窗口激活态变化事件。 |
| callback | Callback<boolean> | 否 | 回调函数。当本窗口的激活态发生变化时的回调。若传入参数，则关闭该监听。若未传入参数，则关闭所有窗口激活态变化的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. const callback = (data: boolean) => {
2. // ...
3. }
4. try {
5. // 通过on接口开启监听
6. windowClass.on('windowHighlightChange', callback);
7. // 关闭指定callback的监听
8. windowClass.off('windowHighlightChange', callback);
9. // 如果通过on开启多个callback进行监听，同时关闭所有监听：
10. windowClass.off('windowHighlightChange');
11. } catch (exception) {
12. console.error(`Failed to unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
13. }
```

## on('rotationChange')19+

PhonePC/2in1TabletTVWearable

on(type: 'rotationChange', callback: RotationChangeCallback<RotationChangeInfo, RotationChangeResult | void>): void

开启窗口旋转变化的监听。[RotationChangeInfo](arkts-apis-window-i.md#rotationchangeinfo19)中窗口旋转事件类型为窗口即将旋转时，必须返回[RotationChangeResult](arkts-apis-window-i.md#rotationchangeresult19)。窗口旋转事件类型为窗口旋转结束时返回[RotationChangeResult](arkts-apis-window-i.md#rotationchangeresult19)不生效。

该函数只允许在主线程注册。同一个窗口多次注册同类型回调函数，只生效最新注册的同类型回调函数返回值。系统提供了超时保护机制，若20ms内窗口未返回[RotationChangeResult](arkts-apis-window-i.md#rotationchangeresult19)，系统不处理该返回值。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：**

针对PC/2in1设备：在API version 23之前，调用该接口会返回801错误码；从API version 23开始，可正常调用该接口且立即生效。

针对非PC/2in1且支持sensor旋转但不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备：可正常调用且立即生效。

针对非PC/2in1且支持sensor旋转，支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备：当处于非[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态时可正常调用该接口且立即生效；当处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态时，调用该接口时不生效也不报错，切换到非[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态下生效。

针对其他设备：调用该接口不生效也不报错。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'rotationChange'，即窗口旋转变化事件。 |
| callback | RotationChangeCallback<[RotationChangeInfo](arkts-apis-window-i.md#rotationchangeinfo19), [RotationChangeResult](arkts-apis-window-i.md#rotationchangeresult19) | void> | 是 | 回调函数。返回窗口旋转信息[RotationChangeInfo](arkts-apis-window-i.md#rotationchangeinfo19)，应用返回当前窗口变化结果[RotationChangeResult](arkts-apis-window-i.md#rotationchangeresult19)。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { window } from '@kit.ArkUI';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. function calculateRect(info: window.RotationChangeInfo): window.Rect {
7. // calculate result with info
8. let rect: window.Rect = {
9. left: 0,
10. top: 0,
11. width: 500,
12. height: 600,
13. };
14. return rect;
15. }

17. function callback(info: window.RotationChangeInfo): window.RotationChangeResult | void {
18. let result: window.RotationChangeResult = {
19. rectType: window.RectType.RELATIVE_TO_SCREEN,
20. windowRect: {
21. left: 0,
22. top: 0,
23. width: 0,
24. height: 0,
25. }
26. };

28. if (info.type === window.RotationChangeType.WINDOW_WILL_ROTATE) {
29. result.rectType = window.RectType.RELATIVE_TO_SCREEN;
30. result.windowRect = calculateRect(info);
31. return result;
32. } else {
33. // do something after rotate
34. return;
35. }
36. }

38. export default class EntryAbility extends UIAbility {
39. // ...
40. onWindowStageCreate(windowStage: window.WindowStage): void {
41. let windowClass: window.Window | undefined = undefined;
42. let config: window.Configuration = {
43. name: 'test',
44. windowType: window.WindowType.TYPE_DIALOG,
45. ctx: this.context
46. };

48. try {
49. window.createWindow(config, (err: BusinessError, data: window.Window) => {
50. const errCode: number = err.code;
51. if (errCode) {
52. console.error(`Failed to create the window. Cause code: ${err.code}, message: ${err.message}`);
53. return;
54. }
55. windowClass = data;
56. try {
57. windowClass.on('rotationChange', callback);
58. } catch (exception) {
59. console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
60. }
61. windowClass.resize(500, 1000);
62. });
63. } catch (exception) {
64. console.error(`Failed to create the window. Cause code: ${exception.code}, message: ${exception.message}`);
65. }
66. }
67. }
```

## off('rotationChange')19+

PhonePC/2in1TabletTVWearable

off(type: 'rotationChange', callback?: RotationChangeCallback<RotationChangeInfo, RotationChangeResult | void>): void

关闭窗口旋转变化的监听。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：**

针对PC/2in1设备：在API version 23之前，调用该接口会返回801错误码；从API version 23开始，可正常调用该接口且立即生效。

针对非PC/2in1且支持sensor旋转但不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备：可正常调用且立即生效。

针对非PC/2in1且支持sensor旋转，支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备：当处于非[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态时可正常调用该接口且立即生效；当处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态时，调用该接口时不生效也不报错，切换到非[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态下生效。

针对其他设备：调用该接口不生效也不报错。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'rotationChange'，即窗口旋转变化事件。 |
| callback | RotationChangeCallback<[RotationChangeInfo](arkts-apis-window-i.md#rotationchangeinfo19), [RotationChangeResult](arkts-apis-window-i.md#rotationchangeresult19) | void> | 否 | 回调函数。如果传入参数，则关闭该监听。如果未传入参数，则关闭该窗口的所有监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. const callback = (info: window.RotationChangeInfo): window.RotationChangeResult | void => {
2. // ...
3. return;
4. }
5. try {
6. windowClass.off('rotationChange', callback);
7. // 如果通过on开启多个callback进行监听，同时关闭所有监听。
8. windowClass.off('rotationChange');
9. } catch (exception) {
10. console.error(`Failed to unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
11. }
```

## on('uiExtensionSecureLimitChange')20+

PhonePC/2in1TabletTVWearable

on(eventType: 'uiExtensionSecureLimitChange', callback: Callback<boolean>): void

开启窗口内uiExtension安全限制变化事件的监听, 建议在窗口创建后立即监听。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventType | string | 是 | 监听事件，固定为'uiExtensionSecureLimitChange'，即窗口内uiExtension安全限制变化事件。 |
| callback | Callback<boolean> | 是 | 回调函数。当窗口内uiExtension安全限制变化时触发回调。当返回参数为true表示窗口内uiExtension开启了隐藏不安全窗口；当返回参数为false表示窗口内uiExtension关闭了隐藏不安全窗口。若窗口内存在多个uiExtension，当返回参数为true表示窗口内至少一个uiExtension开启了隐藏不安全窗口；当返回参数为false表示窗口内所有uiExtension关闭了隐藏不安全窗口。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.Function on('uiExtensionSecureLimitChange') can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. try {
2. windowClass.on('uiExtensionSecureLimitChange', (data: boolean) => {
3. console.info(`Window secure limit Change: ${data}`);
4. });
5. } catch (exception) {
6. console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
7. }
```

## off('uiExtensionSecureLimitChange')20+

PhonePC/2in1TabletTVWearable

off(eventType: 'uiExtensionSecureLimitChange', callback?: Callback<boolean>): void

关闭窗口内uiextension安全限制变化事件的监听。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventType | string | 是 | 监听事件，固定为'uiExtensionSecureLimitChange'，即窗口内uiExtension安全限制变化事件。 |
| callback | Callback<boolean> | 否 | 回调函数。若传入参数，则关闭该监听。若未传入参数，则关闭所有窗口安全限制变化的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.Function off('uiExtensionSecureLimitChange') can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. const callback = (data: boolean) => {
2. // ...
3. }
4. try {
5. // 通过on接口开启监听
6. windowClass.on('uiExtensionSecureLimitChange', callback);
7. // 关闭指定callback的监听
8. windowClass.off('uiExtensionSecureLimitChange', callback);
9. // 如果通过on开启多个callback进行监听，同时关闭所有监听：
10. windowClass.off('uiExtensionSecureLimitChange');
11. } catch (exception) {
12. console.error(`Failed to unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
13. }
```

## isWindowSupportWideGamut9+

PhonePC/2in1TabletTVWearable

isWindowSupportWideGamut(callback: AsyncCallback<boolean>): void

判断当前窗口是否支持广色域模式，使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示当前窗口支持广色域模式，返回false表示当前窗口不支持广色域模式。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. windowClass.isWindowSupportWideGamut((err: BusinessError, data) => {
4. const errCode: number = err.code;
5. if (errCode) {
6. console.error(`Failed to check whether the window support WideGamut. Cause code: ${err.code}, message: ${err.message}`);
7. return;
8. }
9. console.info(`Succeeded in checking whether the window support WideGamut Data: ${data}`);
10. });
```

## isWindowSupportWideGamut9+

PhonePC/2in1TabletTVWearable

isWindowSupportWideGamut(): Promise<boolean>

判断当前窗口是否支持广色域模式，使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示当前窗口支持广色域模式，返回false表示当前窗口不支持广色域模式。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let promise = windowClass.isWindowSupportWideGamut();
4. promise.then((data) => {
5. console.info(`Succeeded in checking whether the window support WideGamut. Data: ${data}`);
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to check whether the window support WideGamut. Cause code: ${err.code}, message: ${err.message}`);
8. });
```

## setWindowColorSpace9+

PhonePC/2in1TabletTVWearable

setWindowColorSpace(colorSpace:ColorSpace, callback: AsyncCallback<void>): void

设置当前窗口为广色域模式或默认色域模式，使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colorSpace | [ColorSpace](arkts-apis-window-e.md#colorspace8) | 是 | 设置色域模式。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. windowClass.setWindowColorSpace(window.ColorSpace.WIDE_GAMUT, (err: BusinessError) => {
5. const errCode: number = err.code;
6. if (errCode) {
7. console.error(`Failed to set window colorspace. Cause code: ${err.code}, message: ${err.message}`);
8. return;
9. }
10. console.info('Succeeded in setting window colorspace.');
11. });
12. } catch (exception) {
13. console.error(`Failed to set window colorspace. Cause code: ${exception.code}, message: ${exception.message}`);
14. }
```

## setWindowColorSpace9+

PhonePC/2in1TabletTVWearable

setWindowColorSpace(colorSpace:ColorSpace): Promise<void>

设置当前窗口为广色域模式或默认色域模式，使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colorSpace | [ColorSpace](arkts-apis-window-e.md#colorspace8) | 是 | 设置色域模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let promise = windowClass.setWindowColorSpace(window.ColorSpace.WIDE_GAMUT);
5. promise.then(() => {
6. console.info('Succeeded in setting window colorspace.');
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to set window colorspace. Cause code: ${err.code}, message: ${err.message}`);
9. });
10. } catch (exception) {
11. console.error(`Failed to set window colorspace. Cause code: ${exception.code}, message: ${exception.message}`);
12. }
```

## getWindowColorSpace9+

PhonePC/2in1TabletTVWearable

getWindowColorSpace(): ColorSpace

获取当前窗口色域模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ColorSpace](arkts-apis-window-e.md#colorspace8) | 当前色域模式。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let colorSpace = windowClass.getWindowColorSpace();
5. console.info(`Succeeded in getting the window color space. ColorSpace: ${colorSpace}`);
6. } catch (exception) {
7. console.error(`Failed to get the window color space. Cause code: ${exception.code}, message: ${exception.message}`);
8. }
```

## setWindowBackgroundColor9+

PhonePC/2in1TabletTVWearable

setWindowBackgroundColor(color: string | ColorMetrics): void

设置窗口的背景色。

未调用该接口时，窗口在浅色模式默认背景色为'#FFF0F0F0'，在深色模式默认背景色为'#FF1A1A1A'。

Stage模型下，该接口需要在[loadContent()](arkts-apis-window-window.md#loadcontent9)或[setUIContent()](arkts-apis-window-window.md#setuicontent9)调用生效后使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | string | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12)18+ | 是 | 需要设置的背景色，为十六进制RGB或ARGB颜色，不区分大小写，例如'#00FF00'或'#FF00FF00'。  从API version 18开始，此参数支持ColorMetrics类型。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { ColorMetrics } from '@kit.ArkUI';

4. let storage: LocalStorage = new LocalStorage();
5. storage.setOrCreate('storageSimpleProp', 121);
6. windowClass.loadContent("pages/page2", storage, (err: BusinessError) => {
7. let errCode: number = err.code;
8. if (errCode) {
9. console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
10. return;
11. }
12. console.info('Succeeded in loading the content.');
13. let color1: string = '#00FF33';
14. let color2: ColorMetrics = ColorMetrics.numeric(0xff112233);
15. try {
16. windowClass?.setWindowBackgroundColor(color1);
17. windowClass?.setWindowBackgroundColor(color2);
18. } catch (exception) {
19. console.error(`Failed to set the background color. Cause code: ${exception.code}, message: ${exception.message}`);
20. };
21. });
```

## setWindowShadowEnabled20+

PhonePC/2in1TabletTVWearable

setWindowShadowEnabled(enable: boolean): Promise<void>

设置主窗口是否显示阴影，使用Promise异步回调。未调用该接口时，主窗口默认显示阴影。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 在HarmonyOS 6.1.0之前，该接口在2in1设备中可正常调用，在其他设备中返回801错误码；从HarmonyOS 6.1.0开始，该接口在2in1和Tablet设备中可正常调用，在Tablet设备时仅在开启[自由多窗模式](../harmonyos-guides/window-terminology.md#自由多窗模式)下生效，在其他设备中返回801错误码。

**需要权限：** ohos.permission.SET\_WINDOW\_TRANSPARENT

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 设置主窗口是否显示阴影。true表示显示阴影，false表示不显示阴影。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. onWindowStageCreate(windowStage: window.WindowStage) {
8. windowStage.loadContent("pages/page2", (err: BusinessError) => {
9. let errCode: number = err.code;
10. if (errCode) {
11. console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
12. return;
13. }
14. console.info('Succeeded in loading the content.');
15. // 获取应用主窗口。
16. let windowClass: window.Window | undefined = undefined;
17. windowStage.getMainWindow((err: BusinessError, data) => {
18. let errCode: number = err.code;
19. if (errCode) {
20. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
21. return;
22. }
23. windowClass = data;
24. let enable = true;
25. let promise = windowClass.setWindowShadowEnabled(enable);
26. promise.then(() => {
27. console.info('Succeeded in setting window shadow.');
28. }).catch((err: BusinessError) => {
29. console.error(`Failed to set the window shadow. Cause code: ${err.code}, message: ${err.message}`);
30. });
31. });
32. });
33. }
34. }
```

## setWindowBrightness9+

PhonePC/2in1TabletTVWearable

setWindowBrightness(brightness: number, callback: AsyncCallback<void>): void

主窗口设置窗口亮度。当窗口处于前台且获焦时，窗口亮度生效。使用callback异步回调。

窗口亮度生效时只会影响当前设备屏幕亮度，无法修改虚拟屏（如投屏所在的屏幕）的屏幕亮度。

当接口入参为-1时，窗口亮度恢复为系统屏幕亮度（可以通过控制中心或快捷键调整）。

当窗口退至后台时，窗口亮度失效，可以通过控制中心或快捷键调整。不建议连续调用或窗口退至后台时调用此接口，否则可能产生时序问题。

说明

* 针对非2in1设备：
  + 在HarmonyOS 6.1.0之前，当前窗口的窗口亮度生效时，控制中心调整系统屏幕亮度不生效。
  + 从HarmonyOS 6.1.0开始，当前窗口的窗口亮度生效时，控制中心可以调整系统屏幕亮度，同时会将当前窗口恢复为系统屏幕亮度。
* 针对2in1设备：
  + 在HarmonyOS5.0.2之前，窗口设置屏幕亮度生效时，控制中心或快捷键调整系统屏幕亮度不生效。
  + 从HarmonyOS5.0.2开始，窗口亮度与系统屏幕亮度保持一致，可以通过本接口、控制中心或者快捷键设置系统屏幕亮度。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| brightness | number | 是 | 屏幕亮度值。该参数为浮点数，取值范围为[0.0, 1.0]或-1.0。1.0表示最亮，-1.0表示恢复成设置窗口亮度前的系统控制中心亮度。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. // ...
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. console.info('onWindowStageCreate');
10. windowStage.loadContent('pages/Index', (loadError: BusinessError) => {
11. if (loadError.code) {
12. console.error(`Failed to load the content. Cause code: ${loadError.code}, message: ${loadError.message}`);
13. return;
14. }
15. let windowClass: window.Window | undefined = undefined;
16. windowStage.getMainWindow((err: BusinessError, data) => {
17. const errCode: number = err.code;
18. if (errCode) {
19. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
20. return;
21. }
22. windowClass = data;
23. let brightness: number = 1.0;
24. try {
25. windowClass.setWindowBrightness(brightness, (err: BusinessError) => {
26. const errCode: number = err.code;
27. if (errCode) {
28. console.error(`Failed to set the brightness. Cause code: ${err.code}, message: ${err.message}`);
29. return;
30. }
31. console.info('Succeeded in setting the brightness.');
32. });
33. } catch (exception) {
34. console.error(`Failed to set the brightness. Cause code: ${exception.code}, message: ${exception.message}`);
35. }
36. });
37. });
38. }
39. }
```

## setWindowBrightness9+

PhonePC/2in1TabletTVWearable

setWindowBrightness(brightness: number): Promise<void>

主窗口设置窗口亮度。当窗口处于前台且获焦时，窗口亮度生效。使用Promise异步回调。

窗口亮度生效时只会影响当前设备屏幕亮度，无法修改虚拟屏（如投屏所在的屏幕）的屏幕亮度。

当接口入参为-1时，窗口亮度恢复为系统屏幕亮度（可以通过控制中心或快捷键调整）。

当窗口退至后台时，窗口亮度失效，可以通过控制中心或快捷键调整。不建议连续调用或窗口退至后台时调用此接口，否则可能产生时序问题。

说明

* 针对非2in1设备：
  + 在HarmonyOS 6.1.0之前，当前窗口的窗口亮度生效时，控制中心调整系统屏幕亮度不生效。
  + 从HarmonyOS 6.1.0开始，当前窗口的窗口亮度生效时，控制中心可以调整系统屏幕亮度，同时会将当前窗口恢复为系统屏幕亮度。
* 针对2in1设备：
  + 在HarmonyOS5.0.2之前，窗口设置屏幕亮度生效时，控制中心或快捷键调整系统屏幕亮度不生效。
  + 从HarmonyOS5.0.2开始，窗口亮度与系统屏幕亮度保持一致，可以通过本接口、控制中心或者快捷键设置系统屏幕亮度。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| brightness | number | 是 | 屏幕亮度值。该参数为浮点数，取值范围为[0.0, 1.0]或-1.0。1.0表示最亮，-1.0表示恢复成设置窗口亮度前的系统控制中心亮度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. // ...
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. console.info('onWindowStageCreate');
10. windowStage.loadContent('pages/Index', (loadError: BusinessError) => {
11. if (loadError.code) {
12. console.error(`Failed to load the content. Cause code: ${loadError.code}, message: ${loadError.message}`);
13. return;
14. }
15. let windowClass: window.Window | undefined = undefined;
16. windowStage.getMainWindow((err: BusinessError, data) => {
17. const errCode: number = err.code;
18. if (errCode) {
19. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
20. return;
21. }
22. windowClass = data;
23. let brightness: number = 1.0;
24. try {
25. let promise = windowClass.setWindowBrightness(brightness);
26. promise.then(() => {
27. console.info('Succeeded in setting the brightness.');
28. }).catch((err: BusinessError) => {
29. console.error(`Failed to set the brightness. Cause code: ${err.code}, message: ${err.message}`);
30. });
31. } catch (exception) {
32. console.error(`Failed to set the brightness. Cause code: ${exception.code}, message: ${exception.message}`);
33. }
34. });
35. });
36. }
37. }
```

## setWindowFocusable9+

PhonePC/2in1TabletTVWearable

setWindowFocusable(isFocusable: boolean, callback: AsyncCallback<void>): void

设置窗口是否具有获得焦点的能力，使用callback异步回调。

从API version 22开始，调用[createVirtualScreen](js-apis-display.md#displaycreatevirtualscreen16)接口创建虚拟屏，并设置supportsFocus配置项为false时，位于该虚拟屏的窗口无法调用该接口修改窗口的可获焦能力，如果调用，会抛出1300002错误码。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isFocusable | boolean | 是 | 窗口是否可获焦。true表示支持；false表示不支持。设置为false时，该窗口不支持绑定输入法和接收键盘事件，如需处理输入逻辑，建议参考[不可获焦窗口中输入框与输入法交互指南](../harmonyos-guides/use-inputmethod-in-not-focusable-window.md)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let isFocusable: boolean = true;
4. try {
5. windowClass.setWindowFocusable(isFocusable, (err: BusinessError) => {
6. const errCode: number = err.code;
7. if (errCode) {
8. console.error(`Failed to set the window to be focusable. Cause code: ${err.code}, message: ${err.message}`);
9. return;
10. }
11. console.info('Succeeded in setting the window to be focusable.');
12. });
13. } catch (exception) {
14. console.error(`Failed to set the window to be focusable. Cause code: ${exception.code}, message: ${exception.message}`);
15. }
```

## setWindowFocusable9+

PhonePC/2in1TabletTVWearable

setWindowFocusable(isFocusable: boolean): Promise<void>

设置窗口是否具有获得焦点的能力，使用Promise异步回调。

从API version 22开始，调用[createVirtualScreen](js-apis-display.md#displaycreatevirtualscreen16)接口创建虚拟屏，并设置supportsFocus配置项为false时，位于该虚拟屏的窗口无法调用该接口修改窗口的可获焦能力，如果调用，会抛出1300002错误码。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isFocusable | boolean | 是 | 窗口是否可获焦。true表示支持；false表示不支持。设置为false时，该窗口不支持绑定输入法和接收键盘事件，如需处理输入逻辑，建议参考[不可获焦窗口中输入框与输入法交互指南](../harmonyos-guides/use-inputmethod-in-not-focusable-window.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let isFocusable: boolean = true;
4. try {
5. let promise = windowClass.setWindowFocusable(isFocusable);
6. promise.then(() => {
7. console.info('Succeeded in setting the window to be focusable.');
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to set the window to be focusable. Cause code: ${err.code}, message: ${err.message}`);
10. });
11. } catch (exception) {
12. console.error(`Failed to set the window to be focusable. Cause code: ${exception.code}, message: ${exception.message}`);
13. }
```

## setWindowKeepScreenOn9+

PhonePC/2in1TabletTVWearable

setWindowKeepScreenOn(isKeepScreenOn: boolean, callback: AsyncCallback<void>): void

设置当前窗口位于前台时当前设备的屏幕是否为常亮状态，异源虚拟屏下不生效。使用callback异步回调。

仅在必要场景（导航、视频播放、绘画、游戏等场景）下，设置该属性为true；退出上述场景后，应当重置该属性为false；其他场景（无屏幕互动、音频播放等）下，不使用该接口；系统检测到非规范使用该接口时，可能会恢复自动灭屏功能。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isKeepScreenOn | boolean | 是 | 设置屏幕是否为常亮状态。true表示常亮；false表示不常亮。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let isKeepScreenOn: boolean = true;
4. try {
5. windowClass.setWindowKeepScreenOn(isKeepScreenOn, (err: BusinessError) => {
6. const errCode: number = err.code;
7. if (errCode) {
8. console.error(`Failed to set the screen to be always on. Cause code: ${err.code}, message: ${err.message}`);
9. return;
10. }
11. console.info('Succeeded in setting the screen to be always on.');
12. });
13. } catch (exception) {
14. console.error(`Failed to set the screen to be always on. Cause code: ${exception.code}, message: ${exception.message}`);
15. }
```

## setWindowKeepScreenOn9+

PhonePC/2in1TabletTVWearable

setWindowKeepScreenOn(isKeepScreenOn: boolean): Promise<void>

设置当前窗口位于前台时当前设备的屏幕是否为常亮状态，异源虚拟屏下不生效。使用Promise异步回调。

仅在必要场景（导航、视频播放、绘画、游戏等场景）下，设置该属性为true；退出上述场景后，应当重置该属性为false；其他场景（无屏幕互动、音频播放等）下，不使用该接口；系统检测到非规范使用该接口时，可能会恢复自动灭屏功能。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isKeepScreenOn | boolean | 是 | 设置屏幕是否为常亮状态。true表示常亮；false表示不常亮。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let isKeepScreenOn: boolean = true;
4. try {
5. let promise = windowClass.setWindowKeepScreenOn(isKeepScreenOn);
6. promise.then(() => {
7. console.info('Succeeded in setting the screen to be always on.');
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to set the screen to be always on. Cause code: ${err.code}, message: ${err.message}`);
10. });
11. } catch (exception) {
12. console.error(`Failed to set the screen to be always on. Cause code: ${exception.code}, message: ${exception.message}`);
13. }
```

## setWindowPrivacyMode9+

PhonePC/2in1TabletTVWearable

setWindowPrivacyMode(isPrivacyMode: boolean, callback: AsyncCallback<void>): void

设置窗口是否为隐私模式，使用callback异步回调。

设置为隐私模式的窗口，窗口内容将无法被截屏或录屏。

隐私模式窗口退后台后在多任务卡片中显示为白色蒙层或隐私蒙层。

未调用此接口时，窗口默认不开启隐私模式，可以被截屏或录屏。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**需要权限：** ohos.permission.PRIVACY\_WINDOW

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isPrivacyMode | boolean | 是 | 窗口是否为隐私模式。true表示为隐私模式，false表示为非隐私模式。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. Possible cause: Need ohos.permission.PRIVACY\_WINDOW permission. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let isPrivacyMode: boolean = true;
4. try {
5. windowClass.setWindowPrivacyMode(isPrivacyMode, (err: BusinessError) => {
6. const errCode: number = err.code;
7. if (errCode) {
8. console.error(`Failed to set the window to privacy mode. Cause code: ${err.code}, message: ${err.message}`);
9. return;
10. }
11. console.info('Succeeded in setting the window to privacy mode.');
12. });
13. } catch (exception) {
14. console.error(`Failed to set the window to privacy mode. Cause code: ${exception.code}, message: ${exception.message}`);
15. }
```

## setWindowPrivacyMode9+

PhonePC/2in1TabletTVWearable

setWindowPrivacyMode(isPrivacyMode: boolean): Promise<void>

设置窗口是否为隐私模式，使用Promise异步回调。

设置为隐私模式的窗口，窗口内容将无法被截屏或录屏。

隐私模式窗口退后台后在多任务卡片中显示为白色蒙层或隐私蒙层。

未调用此接口时，窗口默认不开启隐私模式，可以被截屏或录屏。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**需要权限：** ohos.permission.PRIVACY\_WINDOW

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isPrivacyMode | boolean | 是 | 窗口是否为隐私模式。true表示为隐私模式，false表示为非隐私模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. Possible cause: Need ohos.permission.PRIVACY\_WINDOW permission. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let isPrivacyMode: boolean = true;
4. try {
5. let promise = windowClass.setWindowPrivacyMode(isPrivacyMode);
6. promise.then(() => {
7. console.info('Succeeded in setting the window to privacy mode.');
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to set the window to privacy mode. Cause code: ${err.code}, message: ${err.message}`);
10. });
11. } catch (exception) {
12. console.error(`Failed to set the window to privacy mode. Cause code: ${exception.code}, message: ${exception.message}`);
13. }
```

## setWindowTouchable9+

PhonePC/2in1TabletTVWearable

setWindowTouchable(isTouchable: boolean, callback: AsyncCallback<void>): void

设置窗口是否为可点击状态，使用callback异步回调。

当窗口处于可点击状态时，若用户点击命中该窗口，事件将发送给该窗口处理。当窗口处于不可点击状态时，透传点击事件，传递给下层窗口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isTouchable | boolean | 是 | 窗口是否为可点击状态。true表示可点击；false表示不可点击。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let isTouchable = true;
4. try {
5. windowClass.setWindowTouchable(isTouchable, (err: BusinessError) => {
6. const errCode: number = err.code;
7. if (errCode) {
8. console.error(`Failed to set the window to be touchable. Cause code: ${err.code}, message: ${err.message}`);
9. return;
10. }
11. console.info('Succeeded in setting the window to be touchable.');
12. });
13. } catch (exception) {
14. console.error(`Failed to set the window to be touchable. Cause code: ${exception.code}, message: ${exception.message}`);
15. }
```

## setWindowTouchable9+

PhonePC/2in1TabletTVWearable

setWindowTouchable(isTouchable: boolean): Promise<void>

设置窗口是否为可点击状态，使用Promise异步回调。

当窗口处于可点击状态时，若用户点击命中该窗口，事件将发送给该窗口处理。当窗口处于不可点击状态时，透传点击事件，传递给下层窗口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isTouchable | boolean | 是 | 窗口是否为可点击状态。true表示可点击；false表示不可点击。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let isTouchable: boolean = true;
4. try {
5. let promise = windowClass.setWindowTouchable(isTouchable);
6. promise.then(() => {
7. console.info('Succeeded in setting the window to be touchable.');
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to set the window to be touchable. Cause code: ${err.code}, message: ${err.message}`);
10. });
11. } catch (exception) {
12. console.error(`Failed to set the window to be touchable. Cause code: ${exception.code}, message: ${exception.message}`);
13. }
```

## snapshot9+

PhonePC/2in1TabletTVWearable

snapshot(callback: AsyncCallback<image.PixelMap>): void

获取窗口截图，使用callback异步回调。若当前窗口设置为隐私模式（可通过[setWindowPrivacyMode](arkts-apis-window-window.md#setwindowprivacymode9)接口设置），截图结果为白屏。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[image.PixelMap](arkts-apis-image-pixelmap.md)> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Get pixelMap failed; 3. Internal task error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { image } from '@kit.ImageKit';

4. windowClass.snapshot((err: BusinessError, pixelMap: image.PixelMap) => {
5. const errCode: number = err.code;
6. if (errCode) {
7. console.error(`Failed to snapshot window. Cause code: ${err.code}, message: ${err.message}`);
8. return;
9. }
10. console.info('Succeeded in snapshotting window. Pixel bytes number: ' + pixelMap.getPixelBytesNumber());
11. pixelMap.release(); // PixelMap使用完后及时释放内存
12. });
```

## snapshot9+

PhonePC/2in1TabletTVWearable

snapshot(): Promise<image.PixelMap>

获取当前窗口截图。若当前窗口设置为隐私模式（可通过[setWindowPrivacyMode](arkts-apis-window-window.md#setwindowprivacymode9)接口设置），截图结果为白屏。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[image.PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象。返回当前窗口截图。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Get pixelMap failed; 3. Internal task error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { image } from '@kit.ImageKit';

4. let promise = windowClass.snapshot();
5. promise.then((pixelMap: image.PixelMap) => {
6. console.info('Succeeded in snapshotting window. Pixel bytes number: ' + pixelMap.getPixelBytesNumber());
7. pixelMap.release(); // PixelMap使用完后及时释放内存
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to snapshot window. Cause code: ${err.code}, message: ${err.message}`);
10. });
```

## snapshotSync20+

PhonePC/2in1TabletTVWearable

snapshotSync(): image.PixelMap

获取当前窗口截图，此接口为同步接口。若当前窗口设置为隐私模式（[setWindowPrivacyMode](arkts-apis-window-window.md#setwindowprivacymode9)接口设置），截图结果为白屏。

Stage模型下，该接口需要在[loadContent()](arkts-apis-window-window.md#loadcontent9)或[setUIContent()](arkts-apis-window-window.md#setuicontent9)调用生效后使用。

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [image.PixelMap](arkts-apis-image-pixelmap.md) | 返回当前窗口截图。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Create pixelMap failed. |
| 1300018 | Timeout. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { image } from '@kit.ImageKit';

4. try {
5. let pixelMap = windowClass.snapshotSync();
6. console.info(`Succeeded in snapshotting window`);
7. pixelMap.release(); // PixelMap使用完后及时释放内存
8. } catch (exception) {
9. console.error(`Failed to snapshot window. Cause code: ${exception.code}, message: ${exception.message}`);
10. }
```

## snapshotIgnorePrivacy18+

PhonePC/2in1TabletTVWearable

snapshotIgnorePrivacy(): Promise<image.PixelMap>

获取当前窗口截图。即使当前窗口设置为隐私模式（可通过[setWindowPrivacyMode](arkts-apis-window-window.md#setwindowprivacymode9)接口设置），仍可调用本接口返回当前窗口截图。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[image.PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象。返回当前窗口截图。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function snapshotIgnorePrivacy can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Create pixelMap failed; 3. Internal task error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { image } from '@kit.ImageKit';

4. let promise = windowClass.snapshotIgnorePrivacy();
5. promise.then((pixelMap: image.PixelMap) => {
6. console.info('Succeeded in snapshotting window. Pixel bytes number: ' + pixelMap.getPixelBytesNumber());
7. pixelMap.release(); // PixelMap使用完后及时释放内存
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to snapshot window. Cause code: ${err.code}, message: ${err.message}`);
10. });
```

## setAspectRatio10+

PhonePC/2in1TabletTVWearable

setAspectRatio(ratio: number): Promise<void>

设置窗口内容布局（不含边框和标题栏等装饰）的比例，使用Promise异步回调。

说明

* 通过其他接口如[resize](arkts-apis-window-window.md#resize9)、[resizeAsync](arkts-apis-window-window.md#resizeasync12)设置窗口大小时，不受ratio约束。
* 仅主窗可设置，且仅在自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING）下生效。此比例参数将持久化保存，关闭应用或重启设备后，切换到自由悬浮窗口模式时，设置的比例仍然生效。
* 当同一应用的某个主窗口调用此接口设置宽高比生效后，后续打开的主窗口均会沿用该宽高比。若需为单个主窗口单独设置宽高比，请使用[setContentAspectRatio](arkts-apis-window-window.md#setcontentaspectratio21)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ratio | number | 是 | 窗口内容布局（不含边框和标题栏等装饰）的宽高比。该参数为浮点数，受窗口最大最小尺寸限制，比例值下限为最小宽度/最大高度，上限为最大宽度/最小高度。窗口最大最小尺寸由[WindowLimits](arkts-apis-window-i.md#windowlimits11)和系统限制的交集决定，系统限制优先级高于[WindowLimits](arkts-apis-window-i.md#windowlimits11)。ratio的有效范围会随[WindowLimits](arkts-apis-window-i.md#windowlimits11)变化而变化。如果先设置了[WindowLimits](arkts-apis-window-i.md#windowlimits11)，后设置的ratio与其冲突，会返回错误码；如果先设置了ratio，后设置的[WindowLimits](arkts-apis-window-i.md#windowlimits11)与其冲突，窗口的宽高比可能会不跟随设置的宽高比（ratio）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: Invalid parameter range. |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only main windows are supported. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {

8. // ...
9. onWindowStageCreate(windowStage: window.WindowStage) {
10. console.info('onWindowStageCreate');
11. let windowClass: window.Window = windowStage.getMainWindowSync(); // 获取应用主窗口
12. if (!windowClass) {
13. console.info('windowClass is null');
14. }
15. try {
16. let ratio = 1.0;
17. let promise = windowClass.setAspectRatio(ratio);
18. promise.then(() => {
19. console.info('Succeeded in setting aspect ratio of window.');
20. }).catch((err: BusinessError) => {
21. console.error(`Failed to set the aspect ratio of window. Cause code: ${err.code}, message: ${err.message}`);
22. });
23. } catch (exception) {
24. console.error(`Failed to set the aspect ratio of window. Cause code: ${exception.code}, message: ${exception.message}`);
25. }
26. }
27. }
```

## setAspectRatio10+

PhonePC/2in1TabletTVWearable

setAspectRatio(ratio: number, callback: AsyncCallback<void>): void

设置窗口内容布局（不含边框和标题栏等装饰）的比例，使用callback异步回调。

说明

* 通过其他接口如[resize](arkts-apis-window-window.md#resize9)、[resizeAsync](arkts-apis-window-window.md#resizeasync12)设置窗口大小时，不受ratio约束。
* 仅主窗可设置，且仅在自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING）下生效。此比例参数将持久化保存，关闭应用或重启设备后，切换到自由悬浮窗口模式时，设置的比例仍然生效。
* 当同一应用的某个主窗口调用此接口设置宽高比生效后，后续打开的主窗口均会沿用该宽高比。若需为单个主窗口单独设置宽高比，请使用[setContentAspectRatio](arkts-apis-window-window.md#setcontentaspectratio21)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ratio | number | 是 | 窗口内容布局（不含边框和标题栏等装饰）的宽高比。该参数为浮点数，受窗口最大最小尺寸限制，比例值下限为最小宽度/最大高度，上限为最大宽度/最小高度。窗口最大最小尺寸由[WindowLimits](arkts-apis-window-i.md#windowlimits11)和系统限制的交集决定，系统限制优先级高于[WindowLimits](arkts-apis-window-i.md#windowlimits11)。ratio的有效范围会随[WindowLimits](arkts-apis-window-i.md#windowlimits11)变化而变化。如果先设置了[WindowLimits](arkts-apis-window-i.md#windowlimits11)，后设置的ratio与其冲突，会返回错误码；如果先设置了ratio，后设置的[WindowLimits](arkts-apis-window-i.md#windowlimits11)与其冲突，窗口的宽高比可能会不跟随设置的宽高比（ratio）。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: Invalid parameter range. |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only main windows are supported. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {

8. // ...
9. onWindowStageCreate(windowStage: window.WindowStage) {
10. console.info('onWindowStageCreate');
11. let windowClass: window.Window = windowStage.getMainWindowSync(); // 获取应用主窗口
12. if (!windowClass) {
13. console.info('Failed to load the content. Cause: windowClass is null');
14. }
15. try {
16. let ratio = 1.0;
17. windowClass.setAspectRatio(ratio, (err: BusinessError) => {
18. const errCode: number = err.code;
19. if (errCode) {
20. console.error(`Failed to set the aspect ratio of window. Cause code: ${err.code}, message: ${err.message}`);
21. return;
22. }
23. console.info('Succeeded in setting the aspect ratio of window.');
24. });
25. } catch (exception) {
26. console.error(`Failed to set the aspect ratio of window. Cause code: ${exception.code}, message: ${exception.message}`);
27. }
28. }
29. }
```

## setContentAspectRatio21+

PhonePC/2in1TabletTVWearable

setContentAspectRatio(ratio: number, isPersistent?: boolean, needUpdateRect?: boolean): Promise<void>

设置窗口内容布局（不含边框和标题栏等装饰）的比例，使用Promise异步回调。

说明

* 根据相同的ratio参数调整窗口宽高时，窗口宽高会跟随窗口边框装饰尺寸或可见性变化而调整。
* 通过[setWindowDecorVisible](arkts-apis-window-window.md#setwindowdecorvisible11)将窗口标题栏设置为不可见时，窗口内容区域将占据原本标题栏的高度空间。
* 通过其他接口如[resize](arkts-apis-window-window.md#resize9)、[resizeAsync](arkts-apis-window-window.md#resizeasync12)设置窗口大小时，不受ratio约束。
* 仅主窗可设置，且仅在自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING）下生效。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ratio | number | 是 | 窗口内容布局（不含边框和标题栏等装饰）的宽高比。该参数为浮点数，受窗口最大最小尺寸限制，比例值下限为最小宽度/最大高度，上限为最大宽度/最小高度。窗口最大最小尺寸由[WindowLimits](arkts-apis-window-i.md#windowlimits11)和系统限制的交集决定，系统限制优先级高于[WindowLimits](arkts-apis-window-i.md#windowlimits11)。ratio的有效范围会随[WindowLimits](arkts-apis-window-i.md#windowlimits11)变化而变化。如果先设置了[WindowLimits](arkts-apis-window-i.md#windowlimits11)，后设置的ratio与其冲突，会返回错误码；如果先设置了ratio，后设置的[WindowLimits](arkts-apis-window-i.md#windowlimits11)与其冲突，窗口的宽高比可能会不跟随设置的宽高比（ratio）。 |
| isPersistent | boolean | 否 | 是否持久化保存该比例参数。  如为true，比例参数会持久化保存，销毁窗口、关闭应用或重启设备后，当再次切换到自由悬浮窗口模式时仍然生效。可通过[resetAspectRatio](arkts-apis-window-window.md#resetaspectratio10)清除持久化保存的比例参数。  如为false，比例参数仅对当前窗口生效，窗口销毁后清除该数据。  默认值为true。 |
| needUpdateRect | boolean | 否 | 是否立即根据当前比例更新窗口大小。  如为true，立即根据当前比例更新窗口大小。  如为false，窗口将在拖拽缩放时根据当前比例更新，也可以使用[resize](arkts-apis-window-window.md#resize9)或[resizeAsync](arkts-apis-window-window.md#resizeasync12)进行主动更新。  默认值为true。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only main windows are supported. |
| 1300016 | Parameter error. Possible cause: 1. Invalid parameter range. 2. Invalid parameter length. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. // ...
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. try {
10. let windowClass = windowStage.getMainWindowSync();
11. let ratio = 1.0;
12. let promise = windowClass.setContentAspectRatio(ratio, true, true);
13. promise.then(() => {
14. console.info('Succeeded in setting aspect ratio of window.');
15. }).catch((err: BusinessError) => {
16. console.error(`Failed to set the aspect ratio of window. Cause code: ${err.code}, message: ${err.message}`);
17. });
18. } catch (exception) {
19. console.error(`Failed to set the aspect ratio of window. Cause code: ${exception.code}, message: ${exception.message}`);
20. }
21. }
22. }
```

## resetAspectRatio10+

PhonePC/2in1TabletTVWearable

resetAspectRatio(): Promise<void>

取消设置窗口内容布局的比例，使用Promise异步回调。

仅主窗可设置，调用后将清除持久化储存的比例信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {

8. // ...
9. onWindowStageCreate(windowStage: window.WindowStage) {
10. console.info('onWindowStageCreate');
11. let windowClass: window.Window = windowStage.getMainWindowSync(); // 获取应用主窗口
12. if (!windowClass) {
13. console.info('Failed to load the content. Cause: windowClass is null');
14. }
15. try {
16. let promise = windowClass.resetAspectRatio();
17. promise.then(() => {
18. console.info('Succeeded in resetting aspect ratio of window.');
19. }).catch((err: BusinessError) => {
20. console.error(`Failed to reset the aspect ratio of window. Cause code: ${err.code}, message: ${err.message}`);
21. });
22. } catch (exception) {
23. console.error(`Failed to reset the aspect ratio of window. Cause code: ${exception.code}, message: ${exception.message}`);
24. }
25. }
26. }
```

## resetAspectRatio10+

PhonePC/2in1TabletTVWearable

resetAspectRatio(callback: AsyncCallback<void>): void

取消设置窗口内容布局的比例，使用callback异步回调。

仅主窗可设置，调用后将清除持久化储存的比例信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {

8. // ...
9. onWindowStageCreate(windowStage: window.WindowStage) {
10. console.info('onWindowStageCreate');
11. let windowClass: window.Window = windowStage.getMainWindowSync(); // 获取应用主窗口
12. if (!windowClass) {
13. console.info('Failed to load the content. Cause: windowClass is null');
14. }
15. try {
16. windowClass.resetAspectRatio((err: BusinessError) => {
17. const errCode: number = err.code;
18. if (errCode) {
19. console.error(`Failed to reset the aspect ratio of window. Cause code: ${err.code}, message: ${err.message}`);
20. return;
21. }
22. console.info('Succeeded in resetting aspect ratio of window.');
23. });
24. } catch (exception) {
25. console.error(`Failed to reset the aspect ratio of window. Cause code: ${exception.code}, message: ${exception.message}`);
26. }
27. }
28. }
```

## minimize11+

PhonePC/2in1TabletTVWearable

minimize(callback: AsyncCallback<void>): void

此接口根据调用对象不同，实现不同的功能：

* 当调用对象为主窗口时，实现最小化功能，可在Dock栏中还原，2in1 设备上可以使用[restore()](arkts-apis-window-window.md#restore14)进行还原。
* 当调用对象为子窗口或全局悬浮窗时，实现隐藏功能，不可在Dock栏中还原，可以使用[showWindow()](arkts-apis-window-window.md#showwindow9)进行还原。

该接口仅支持主窗口、子窗口或全局悬浮窗，其它窗口调用返回1300002错误码，使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error; 3.Invalid window type. Only main windows, subwindows, and float windows are supported. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. windowClass.minimize((err: BusinessError) => {
4. const errCode: number = err.code;
5. if (errCode) {
6. console.error(`Failed to minimize the window. Cause code: ${err.code}, message: ${err.message}`);
7. return;
8. }
9. console.info('Succeeded in minimizing the window.');
10. });
```

## minimize11+

PhonePC/2in1TabletTVWearable

minimize(): Promise<void>

此接口根据调用对象不同，实现不同的功能：

* 当调用对象为主窗口时，实现最小化功能，可在Dock栏中还原，2in1 设备上可以使用[restore()](arkts-apis-window-window.md#restore14)进行还原。
* 当调用对象为子窗口或全局悬浮窗时，实现隐藏功能，不可在Dock栏中还原，可以使用[showWindow()](arkts-apis-window-window.md#showwindow9)进行还原。

该接口仅支持主窗口、子窗口或全局悬浮窗，其它窗口调用返回1300002错误码，使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error; 3.Invalid window type. Only main windows, subwindows, and float windows are supported. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let promise = windowClass.minimize();
4. promise.then(() => {
5. console.info('Succeeded in minimizing the window.');
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to minimize the window. Cause code: ${err.code}, message: ${err.message}`);
8. });
```

## maximize12+

PhonePC/2in1TabletTVWearable

maximize(presentation?: MaximizePresentation): Promise<void>

实现最大化功能。主窗口可调用此接口实现最大化功能；子窗口需在创建时设置子窗口参数maximizeSupported为true，再调用此接口可实现最大化功能。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备及不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上调用不生效也不报错。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| presentation | [MaximizePresentation](arkts-apis-window-e.md#maximizepresentation12) | 否 | 主窗口或子窗口最大化时的布局枚举。默认值window.MaximizePresentation.ENTER\_IMMERSIVE，即默认最大化时进入全屏模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function maximize can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only main windows and maximizable subwindows are supported. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. // ...

9. onWindowStageCreate(windowStage: window.WindowStage) {
10. console.info('onWindowStageCreate');
11. let windowClass: window.Window | undefined = undefined;
12. windowStage.getMainWindow((err: BusinessError, data) => {
13. const errCode: number = err.code;
14. if (errCode) {
15. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
16. return;
17. }
18. windowClass = data;
19. let promise = windowClass.maximize();
20. // let promise = windowClass.maximize(window.MaximizePresentation.ENTER_IMMERSIVE);
21. promise.then(() => {
22. console.info('Succeeded in maximizing the window.');
23. }).catch((err: BusinessError) => {
24. console.error(`Failed to maximize the window. Cause code: ${err.code}, message: ${err.message}`);
25. });
26. });
27. }
28. };
```

## maximize22+

PhonePC/2in1TabletTVWearable

maximize(presentation?: MaximizePresentation, acrossDisplay?: boolean): Promise<void>

实现最大化功能。主窗口可调用此接口实现最大化功能；子窗口需在创建时设置子窗口参数maximizeSupported为true，再调用此接口可实现最大化功能。在具备折叠功能的2in1设备上，支持控制悬停态（参考[折叠屏悬停态最佳实践](../best-practices/bpta-folded-hover.md)）下主窗口的瀑布流模式行为，即窗口在悬停态下最大化时是否跨上下两个半屏显示。使用Promise异步回调。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备及不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上调用不生效也不报错。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| presentation | [MaximizePresentation](arkts-apis-window-e.md#maximizepresentation12) | 否 | 主窗口或子窗口最大化时的布局枚举。默认值window.MaximizePresentation.ENTER\_IMMERSIVE，即默认最大化时进入全屏模式。 |
| acrossDisplay | boolean | 否 | 控制悬停态下主窗口在最大化时的瀑布流模式行为。默认值为undefined。  仅主窗口可设置此参数，非主窗口调用时返回错误码1300004。  取值为true时：  - 悬停态下，窗口将直接进入瀑布流模式；  - 展开态下，窗口进入最大化，并在悬停态下保持瀑布流模式。  取值为false时：  - 悬停态下，窗口将退出瀑布流模式，进入单面最大化（即窗口最大化时只在上半屏或下半屏显示）；  - 展开态下，窗口进入最大化，并在悬停态下退出瀑布流模式。  取值为undefined时，不修改窗口瀑布流模式行为：  - 悬停态下，窗口进入单面最大化；  - 展开态下，窗口进入最大化，并在悬停态下默认保持瀑布流模式。  **设备行为差异：** 仅在具备折叠功能的2in1设备可正常调用；在其他设备上调用不生效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function maximize can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only main windows and maximizable subwindows are supported. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. // ...
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. windowStage.loadContent('pages/Index', (err) => {
10. if (err.code) {
11. console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
12. return;
13. }
14. let mainWindow = windowStage.getMainWindowSync();
15. mainWindow.maximize(window.MaximizePresentation.ENTER_IMMERSIVE, true)
16. .then(() => {
17. console.info('Window maximized successfully.');
18. })
19. .catch((err: BusinessError) => {
20. console.error(`Failed to maximize the window. Cause code: ${err.code}, message: ${err.message}`);
21. });
22. });
23. }
24. };
```

## setResizeByDragEnabled14+

PhonePC/2in1TabletTVWearable

setResizeByDragEnabled(enable: boolean, callback: AsyncCallback<void>): void

禁止/使能通过拖拽方式缩放主窗口或启用装饰的子窗口的功能。使用callback异步回调。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 设置窗口是否使能通过拖拽进行缩放，true表示使能，false表示禁止。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. try {
2. let enabled = false;
3. windowClass.setResizeByDragEnabled(enabled, (err) => {
4. if (err.code) {
5. console.error(`Failed to set the function of disabling the resize by drag window. Cause code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. console.info(`Succeeded in setting the function of disabling the resize by drag window.`);
9. });
10. } catch (exception) {
11. console.error(`Failed to set the function of disabling the resize by drag window. Cause code: ${exception.code}, message: ${exception.message}`);
12. }
```

## setResizeByDragEnabled14+

PhonePC/2in1TabletTVWearable

setResizeByDragEnabled(enable: boolean): Promise<void>

禁止/使能通过拖拽方式缩放主窗口或启用装饰的子窗口的功能。使用Promise异步回调。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 设置窗口是否使能通过拖拽进行缩放，true表示使能，false表示禁止。 |

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
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let enabled = false;
5. let promise = windowClass.setResizeByDragEnabled(enabled);
6. promise.then(() => {
7. console.info(`Succeeded in setting the function of disabling the resize by drag window.`);
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to set the function of disabling the resize by drag window. Cause code: ${err.code}, message: ${err.message}`);
10. });
11. } catch (exception) {
12. console.error(`Failed to set the function of disabling the resize by drag window. Cause code: ${exception.code}, message: ${exception.message}`);
13. }
```

## recover11+

PhonePC/2in1TabletTVWearable

recover(): Promise<void>

将主窗口从全屏、最大化、分屏模式下还原为自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING），并恢复到进入该模式之前的大小和位置，已经是自由悬浮窗口模式不可再还原。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备及不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上调用返回801错误码。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300001 | Repeated operation. |
| 1300002 | This window state is abnormal. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. // ...
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. console.info('onWindowStageCreate');
10. try {
11. let windowClass = windowStage.getMainWindowSync();
12. if (!windowClass) {
13. console.error('Failed to get main window.');
14. return;
15. }
16. let promise = windowClass.recover();
17. promise.then(() => {
18. console.info('Succeeded in recovering the window.');
19. }).catch((err: BusinessError) => {
20. console.error(`Failed to recover the window. Cause code: ${err.code}, message: ${err.message}`);
21. });
22. } catch (exception) {
23. console.error(`Failed to recover the window. Cause code: ${exception.code}, message: ${exception.message}`);
24. }
25. }
26. }
```

## restore14+

PhonePC/2in1TabletTVWearable

restore(): Promise<void>

主窗口为最小化状态且UIAbility生命周期为onForeground时，将主窗口从最小化状态，恢复到前台显示，并恢复到进入最小化状态之前的大小和位置。主窗口为前台状态时，仅抬升主窗口层级。使用Promise异步回调。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在2in1设备中可正常调用，在其他设备中返回801错误码。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only main windows are supported. |

**示例**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. onWindowStageCreate(windowStage: window.WindowStage): void {
8. try {
9. let windowClass = windowStage.getMainWindowSync();
10. // 调用minimize, 使主窗最小化
11. windowClass.minimize();
12. // 设置延时函数延时5秒钟后对主窗进行恢复。
13. setTimeout(()=>{
14. // 调用restore()函数对主窗进行恢复。
15. let promise = windowClass.restore();
16. promise.then(() => {
17. console.info('Succeeded in restoring the window.');
18. }).catch((err: BusinessError) => {
19. console.error(`Failed to restore the window. Cause code: ${err.code}, message: ${err.message}`);
20. });
21. }, 5000);
22. } catch (exception) {
23. console.error(`Failed to restore the window. Cause code: ${exception.code}, message: ${exception.message}`);
24. }
25. }
26. }
```

## restoreMainWindow23+

PhonePC/2in1TabletTVWearable

restoreMainWindow(wantParameters?: Record<string, Object>): Promise<void>

将当前窗口的主窗口恢复到前台显示，如果主窗口已处于前台，则会抬升主窗层级。此接口仅适用于类型为[TYPE\_FLOAT](arkts-apis-window-e.md#windowtype7)的窗口，并且需在窗口触发过[DOWN](ts-appendix-enums.md#touchtype)事件后才能调用。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wantParameters | Record<string, Object> | 否 | 拉起窗口时会给主窗传递的自定义参数，主窗会在触发[onNewWant](js-apis-app-ability-abilitylifecyclecallback.md#onnewwant12)回调时收到。默认值为空，代表不向主窗传入任何自定义参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed. 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. Possible cause: 1. The window is not float window. 2. The window is not at foreground or has never been clicked. 3. The window cannot find main window. |
| 1300007 | Restore parent main window failed. Possible cause: 1. The main window is in PAUSED lifecycle state. 2. The main window is in background during recent. |

**示例：**

```
1. // Float.ets
2. import { window } from '@kit.ArkUI'
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { JSON } from '@kit.ArkTS';

6. @Entry
7. @Component
8. struct Float {
9. build() {
10. Button('CreateFloatWindow').onClick(() => {
11. this.createFloatWindow();
12. })
13. }

15. private createFloatWindow() {
16. let windowClass: window.Window | undefined = undefined;
17. let config: window.Configuration = {
18. name: 'testFloatWindow',
19. title: 'floatWindow',
20. windowType: window.WindowType.TYPE_FLOAT,
21. ctx: this.getUIContext()?.getHostContext(),
22. decorEnabled: true,
23. };
24. try {
25. window.createWindow(config, (err: BusinessError, data) => {
26. const errCode: number = err.code;
27. if (errCode) {
28. console.error(`failed to create the window. Cause code: ${err.code}, message: ${err.message}`);
29. return;
30. }
31. windowClass = data;
32. console.info(`succedded in creating the window. Data: ${JSON.stringify(data)}`);
33. windowClass.resize(500, 1600).then(() => {
34. console.info('Succeeded in changing the window size.');
35. }).catch((err: BusinessError) => {
36. console.error(`Failed to change the window size. Cause code: ${err.code}, message: ${err.message}`);
37. });
38. windowClass.setUIContent("pages/FloatWindowInfo").then(() => {
39. console.info('Succeeded in loading the content.');
40. }).catch((err: BusinessError) => {
41. console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
42. });
43. windowClass.showWindow().then(() => {
44. console.info("showWindow success");
45. }).catch((err: BusinessError) => {
46. console.error(`showWindow err: ${JSON.stringify(err)}`);
47. });
48. windowClass.moveWindowToAsync(20, 200).then(() => {
49. console.info('Succeeded in moving the window.');
50. }).catch((err: BusinessError) => {
51. console.error(`Failed to move the window. Cause code: ${err.code}, message: ${err.message}`);
52. });
53. });
54. } catch (exception) {
55. console.error(`failed to create the window. Cause code: ${exception.code}, message: ${exception.message}`);
56. }
57. }
58. }
```

```
1. // FloatWindowInfo.ets
2. import { window } from '@kit.ArkUI'
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct FloatWindowInfo {
8. @State subWindow: window.Window | undefined = undefined;
9. @State windowId: number = -1;
10. async aboutToAppear(): Promise<void> {
11. this.subWindow = window.findWindow('testFloatWindow');
12. this.windowId = this.subWindow?.getWindowProperties()?.id;
13. }

15. build() {
16. Column() {
17. Text('Hello')
18. }
19. .width('100%')
20. .height('100%')
21. .onTouch((event: TouchEvent) => {
22. // 保证有Down事件产生，实际调用时机可由开发者决定
23. if (event.type === TouchType.Down) {
24. let param: Record<string, Object> = {
25. "info": "helloworld",
26. };
27. try {
28. let promise = this.subWindow?.restoreMainWindow(param);
29. promise?.then(() => {
30. console.info('Succeeded in restoring the main window.');
31. }).catch((err: BusinessError) => {
32. console.error(`Failed to restore the main window. Cause code: ${err.code}, message: ${err.message}`);
33. });
34. } catch (exception) {
35. console.error(`Failed to restore the main window. Cause code: ${exception.code}, message: ${exception.message}`);
36. }
37. }
38. })
39. }
40. }
```

## getWindowLimits11+

PhonePC/2in1TabletTVWearable

getWindowLimits(): WindowLimits

获取当前应用窗口的尺寸限制，单位为物理像素px。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WindowLimits](arkts-apis-window-i.md#windowlimits11) | 当前窗口尺寸限制。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```
1. try {
2. let windowLimits = windowClass.getWindowLimits();
3. } catch (exception) {
4. console.error(`Failed to obtain the window limits of window. Cause code: ${exception.code}, message: ${exception.message}`);
5. }
```

## getWindowLimitsVP22+

PhonePC/2in1TabletTVWearable

getWindowLimitsVP(): WindowLimits

获取当前应用窗口的尺寸限制，单位为虚拟像素vp。

对于系统窗口和全局悬浮窗，默认窗口宽高的系统限制最小值为1px，通过此接口获取到的1vp，是计算取整后的值。

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WindowLimits](arkts-apis-window-i.md#windowlimits11) | 当前窗口尺寸限制。 |

**错误码：**

错误码详情请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```
1. try {
2. let windowLimits: window.WindowLimits = windowClass.getWindowLimitsVP();
3. } catch (exception) {
4. console.error(`Failed to obtain the window limits. Cause code: ${exception.code}, message: ${exception.message}`);
5. }
```

## setWindowLimits11+

PhonePC/2in1TabletTVWearable

setWindowLimits(windowLimits: WindowLimits): Promise<WindowLimits>

设置当前窗口的尺寸限制，使用Promise异步回调。

默认存在一个系统尺寸限制，系统尺寸限制由产品配置决定，不可修改。

未调用setWindowLimits配置过WindowLimits时，使用[getWindowLimits](arkts-apis-window-window.md#getwindowlimits11)或[getWindowLimitsVP](arkts-apis-window-window.md#getwindowlimitsvp22)可获取系统限制。

说明

* [自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态下，处于自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING）的窗口在尺寸变化时受[WindowLimits](arkts-apis-window-i.md#windowlimits11)约束。触发场景包括：应用主动改变窗口大小（如调用[resize()](arkts-apis-window-window.md#resize9)）；系统调节窗口大小（如分辨率变化、显示大小缩放系数变化）；用户拖拽缩放窗口。
* 非[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态下，主窗口尺寸不受[WindowLimits](arkts-apis-window-i.md#windowlimits11)约束，其他类型窗口仍受[WindowLimits](arkts-apis-window-i.md#windowlimits11)约束。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| windowLimits | [WindowLimits](arkts-apis-window-i.md#windowlimits11) | 是 | 目标窗口的尺寸限制，单位为px或vp。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[WindowLimits](arkts-apis-window-i.md#windowlimits11)> | Promise对象。返回设置后的尺寸限制，为入参与系统尺寸限制的交集。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. try {
3. let windowLimits: window.WindowLimits = {
4. maxWidth: 1500,
5. maxHeight: 1000,
6. minWidth: 500,
7. minHeight: 400
8. };
9. let promise = windowClass.setWindowLimits(windowLimits);
10. promise.then((data) => {
11. console.info('Succeeded in changing the window limits. Cause:' + JSON.stringify(data));
12. }).catch((err: BusinessError) => {
13. console.error(`Failed to change the window limits. Cause code: ${err.code}, message: ${err.message}`);
14. });
15. } catch (exception) {
16. console.error(`Failed to change the window limits. Cause code: ${exception.code}, message: ${exception.message}`);
17. }
```

## setWindowLimits15+

PhonePC/2in1TabletTVWearable

setWindowLimits(windowLimits: WindowLimits, isForcible: boolean): Promise<WindowLimits>

设置当前窗口的尺寸限制，使用Promise异步回调。

默认存在一个系统尺寸限制，系统尺寸限制由产品配置决定，不可修改。

未调用setWindowLimits配置过WindowLimits时，使用[getWindowLimits](arkts-apis-window-window.md#getwindowlimits11)或[getWindowLimitsVP](arkts-apis-window-window.md#getwindowlimitsvp22)可获取系统限制。

说明

* [自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态下，处于自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING）的窗口在尺寸变化时受[WindowLimits](arkts-apis-window-i.md#windowlimits11)约束。触发场景包括：应用主动改变窗口大小（如调用[resize()](arkts-apis-window-window.md#resize9)）；系统调节窗口大小（如分辨率变化、显示大小缩放系数变化）；用户拖拽缩放窗口。
* 非[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态下，主窗口尺寸不受[WindowLimits](arkts-apis-window-i.md#windowlimits11)约束，其他类型窗口仍受[WindowLimits](arkts-apis-window-i.md#windowlimits11)约束。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：**

在HarmonyOS 5.1.1之前，该接口在2in1设备中可正常调用，在其他设备中返回801错误码。

从HarmonyOS 5.1.1开始，该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备及不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上调用返回801错误码。

从HarmonyOS 6.1.0开始，该接口在Phone、Tablet、PC/2in1设备可正常调用，在其他设备调用返回801错误码。主窗在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备调用不报错不生效，切换到[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态后生效。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| windowLimits | [WindowLimits](arkts-apis-window-i.md#windowlimits11) | 是 | 目标窗口的尺寸限制，单位为px或vp。 |
| isForcible | boolean | 是 | 是否强制设置窗口的尺寸限制。  入参[windowLimits](arkts-apis-window-i.md#windowlimits11)的单位为vp时：无论设置true还是false，都按照false处理，窗口宽高的最小值和最大值都取决于系统限制。  入参[windowLimits](arkts-apis-window-i.md#windowlimits11)的单位为px时：设置为true，表示窗口宽高最小值以系统限制值和40vp两者中的低数值为准，窗口宽高的最大值仍取决于系统限制；设置为false，表示窗口宽高的最小值和最大值都取决于系统限制。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[WindowLimits](arkts-apis-window-i.md#windowlimits11)> | Promise对象。返回设置后的窗口尺寸限制。  入参[windowLimits](arkts-apis-window-i.md#windowlimits11)的单位为vp时，返回入参与系统默认窗口尺寸限制的交集。  入参[windowLimits](arkts-apis-window-i.md#windowlimits11)的单位为px时，isForcible为false则返回入参与系统默认窗口尺寸限制的交集；isForcible为true则返回入参与[系统限制的最小值与40vp两者中的低数值，系统限制的最大值]的交集。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. try {
3. let windowLimits: window.WindowLimits = {
4. maxWidth: 1500,
5. maxHeight: 1000,
6. minWidth: 100,
7. minHeight: 100
8. };
9. let promise = windowClass.setWindowLimits(windowLimits, true);
10. promise.then((data) => {
11. console.info(`Succeeded in changing the window limits. Cause: ${JSON.stringify(data)}`);
12. }).catch((err: BusinessError) => {
13. console.error(`Failed to change the window limits. Cause code: ${err.code}, message: ${err.message}`);
14. });
15. } catch (exception) {
16. console.error(`Failed to change the window limits. Cause code: ${exception.code}, message: ${exception.message}`);
17. }
```

## setWindowMask12+

PhonePC/2in1TabletTVWearable

setWindowMask(windowMask: Array<Array<number>>): Promise<void>;

设置异形窗口的掩码，使用Promise异步回调。异形窗口为非常规形状的窗口，掩码用于描述异形窗口的形状。此接口仅限子窗和全局悬浮窗可用。

当异形窗口大小发生变化时，实际的显示内容为掩码大小和窗口大小的交集部分。

异形窗口蒙层设置不会影响窗口可见状态(可通过[on('windowVisibilityChange')](arkts-apis-window-window.md#onwindowvisibilitychange11)或[on('occlusionStateChanged')](arkts-apis-window-window.md#onocclusionstatechanged22)监听）计算。即使掩码全部设置为0，窗口仍可见，窗口依然按照其原本矩形大小参与可见状态计算。

该接口只在多个线程操作同一个窗口时可能返回错误码1300002。窗口被销毁场景下错误码返回401。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| windowMask | Array<Array<number>> | 是 | 异形窗口的掩码，该参数仅支持宽高为窗口宽高、取值为整数0和整数1的二维数组输入，整数0代表所在像素透明，整数1代表所在像素不透明，宽高不符合的二维数组或二维数组取值不为整数0和整数1的二维数组为非法参数。 |

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
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only subwindows and float windows are supported. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. try {
3. let maskWidth = windowClass.getWindowProperties().windowRect.width;
4. let maskHeight = windowClass.getWindowProperties().windowRect.height;
5. let windowMask = Array<Array<number>>(maskHeight).fill([]).map((_, row) => {
6. let array = Array<number>(maskWidth);
7. for (let i = 0 ; i < maskWidth; i++) {
8. array[i] = (i + row) > (maskWidth + maskHeight) / 2 ? 1 : 0;
9. }
10. return array;
11. });
12. let promise = windowClass.setWindowMask(windowMask);
13. promise.then(() => {
14. console.info('Succeeded in setting the window mask.');
15. }).catch((err: BusinessError) => {
16. console.error(`Failed to set the window mask. Cause code: ${err.code}, message: ${err.message}`);
17. });
18. } catch (exception) {
19. console.error(`Failed to set the window mask. Cause code: ${exception.code}, message: ${exception.message}`);
20. }
```

## keepKeyboardOnFocus11+

PhonePC/2in1TabletTVWearable

keepKeyboardOnFocus(keepKeyboardFlag: boolean): void

当前窗口获焦时是否保留由其他窗口创建的软键盘，支持系统窗口、应用子窗口、模态窗和全局悬浮窗。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keepKeyboardFlag | boolean | 是 | 是否保留其他窗口创建的软键盘。true表示保留；false表示不保留。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. |

**示例：**

```
1. try {
2. windowClass.keepKeyboardOnFocus(true);
3. } catch (exception) {
4. console.error(`Failed to keep keyboard onFocus. Cause code: ${exception.code}, message: ${exception.message}`);
5. }
```

## setWindowDecorVisible11+

PhonePC/2in1TabletTVWearable

setWindowDecorVisible(isVisible: boolean): void

设置窗口标题栏是否可见，对存在标题栏和三键区的窗口形态生效。Stage模型下，该接口需要在[loadContent()](arkts-apis-window-window.md#loadcontent9)或[setUIContent()](arkts-apis-window-window.md#setuicontent9)调用生效后使用。

设置窗口标题栏不可见后，当主窗口进入全屏沉浸状态时，此时鼠标Hover到上方窗口标题栏热区上会显示悬浮标题栏。若想禁用悬浮标题栏显示，请使用[setTitleAndDockHoverShown()](arkts-apis-window-window.md#settitleanddockhovershown14)接口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isVisible | boolean | 是 | 设置标题栏是否可见，true为可见，false为隐藏。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. let storage: LocalStorage = new LocalStorage();
3. storage.setOrCreate('storageSimpleProp', 121);
4. windowClass.loadContent("pages/page2", storage, (err: BusinessError) => {
5. let errCode: number = err.code;
6. if (errCode) {
7. console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
8. return;
9. }
10. console.info('Succeeded in loading the content.');
11. let isVisible = false;
12. // 调用setWindowDecorVisible接口
13. try {
14. windowClass?.setWindowDecorVisible(isVisible);
15. } catch (exception) {
16. console.error(`Failed to set the visibility of window decor. Cause code: ${exception.code}, message: ${exception.message}`);
17. }
18. });
```

## getWindowDecorVisible18+

PhonePC/2in1TabletTVWearable

getWindowDecorVisible(): boolean

查询窗口标题栏是否可见。如果使用Stage模型，该接口需要在[loadContent()](arkts-apis-window-window.md#loadcontent9)或[setUIContent()](arkts-apis-window-window.md#setuicontent9)调用生效后使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备及不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上调用返回801错误码。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回当前窗口标题栏是否可见，true表示可见，false表示不可见。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```
1. let isVisible: boolean | undefined = undefined;
2. windowClass.setUIContent('pages/WindowPage').then(() => {
3. try {
4. isVisible = windowClass?.getWindowDecorVisible();
5. } catch (exception) {
6. console.error(`Failed to get the window decor visibility. Cause code: ${exception.code}, message: ${exception.message}`);
7. }
8. })
```

## setWindowTitle15+

PhonePC/2in1TabletTVWearable

setWindowTitle(titleName: string): Promise<void>

设置窗口标题，使用Promise异步回调。如果使用Stage模型，该接口需要在[loadContent()](arkts-apis-window-window.md#loadcontent9)或[setUIContent()](arkts-apis-window-window.md#setuicontent9)调用生效后使用。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备调用不报错不生效，切换到[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态后生效；在不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上调用返回1300002或801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| titleName | string | 是 | 窗口标题。标题显示区域最右端不超过系统三键区域最左端，超过部分以省略号表示。 |

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

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let title = "title";
5. windowClass.setWindowTitle(title).then(() => {
6. console.info('Succeeded in setting the window title.');
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to set the window title. Cause code: ${err.code}, message: ${err.message}`);
9. });
10. } catch (exception) {
11. console.error(`Failed to set the window title. Cause code: ${exception.code}, message: ${exception.message}`);
12. }
```

## setWindowTitleMoveEnabled14+

PhonePC/2in1TabletTVWearable

setWindowTitleMoveEnabled(enabled: boolean): void

禁止/使能主窗或子窗标题栏默认移动窗口和双击最大化的功能，当禁用标题栏默认移动窗口和双击最大化的功能时，可使用[startMoving()](arkts-apis-window-window.md#startmoving14)在应用热区中发起拖拽移动，使用[maximize()](arkts-apis-window-window.md#maximize12)实现最大化功能。如果使用Stage模型，该接口需要在[loadContent()](arkts-apis-window-window.md#loadcontent9)或[setUIContent()](arkts-apis-window-window.md#setuicontent9)调用生效后使用。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备及不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上调用返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 是否使能标题栏默认移动窗口和双击最大化功能，true表示使能，false表示不使能。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300004 | Unauthorized operation. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { window } from '@kit.ArkUI';

5. export default class EntryAbility extends UIAbility {
6. onWindowStageCreate(windowStage: window.WindowStage): void {
7. try {
8. windowStage.loadContent("pages/Index").then(() =>{
9. let windowClass = windowStage.getMainWindowSync();
10. let enabled = false;
11. windowClass.setWindowTitleMoveEnabled(enabled);
12. console.info(`Succeeded in setting the the window title move enabled: ${enabled}`);
13. });
14. } catch (exception) {
15. console.error(`Failed to set the window title move enabled. Cause code: ${exception.code}, message: ${exception.message}`);
16. }
17. }
18. }
```

## setSubWindowModal12+

PhonePC/2in1TabletTVWearable

setSubWindowModal(isModal: boolean): Promise<void>

设置子窗的模态属性是否启用，使用Promise异步回调。

子窗口调用该接口时，设置子窗口模态属性是否启用。启用子窗口模态属性后，其父级窗口不能响应用户操作，直到子窗口关闭或者子窗口的模态属性被禁用。

子窗口之外的窗口调用该接口时，会报错。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isModal | boolean | 是 | 设置子窗口模态属性是否启用，true为启用，false为不启用。 |

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
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. // ...
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. console.info('onWindowStageCreate');
10. let windowClass: window.Window | undefined = undefined;
11. // 创建子窗
12. try {
13. let subWindow = windowStage.createSubWindow("testSubWindow");
14. subWindow.then((data) => {
15. if (data == null) {
16. console.error("Failed to create the subWindow. Cause: The data is empty");
17. return;
18. }
19. windowClass = data;
20. let promise = windowClass.setSubWindowModal(true);
21. promise.then(() => {
22. console.info('Succeeded in setting subwindow modal');
23. }).catch((err: BusinessError) => {
24. console.error(`Failed to set subwindow modal. Cause code: ${err.code}, message: ${err.message}`);
25. });
26. });
27. } catch (exception) {
28. console.error(`Failed to create the subWindow. Cause code: ${exception.code}, message: ${exception.message}`);
29. }
30. }
31. }
```

## setSubWindowModal14+

PhonePC/2in1TabletTVWearable

setSubWindowModal(isModal: boolean, modalityType: ModalityType): Promise<void>

设置子窗的模态类型，使用Promise异步回调。

当子窗口模态类型为模窗口子窗时，其父级窗口不能响应用户操作，直到子窗口关闭或者子窗口的模态类型被禁用。

当子窗口模态类型为模应用子窗时，其父级窗口与该应用其他实例的窗口不能响应用户操作，直到子窗口关闭或者子窗口的模态类型被禁用。

此接口仅支持设置子窗口模态类型，当需要禁用子窗口模态属性时，建议使用[setSubWindowModal12+](arkts-apis-window-window.md#setsubwindowmodal12)。

子窗口之外的窗口调用该接口时，会报错。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isModal | boolean | 是 | 设置子窗口模态属性是否启用，true为启用，false为不启用。当前仅支持设置为true。 |
| modalityType | [ModalityType](arkts-apis-window-e.md#modalitytype14) | 是 | 子窗口模态类型。 |

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
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. // ...
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. console.info('onWindowStageCreate');
10. let windowClass: window.Window | undefined = undefined;
11. // 创建子窗
12. try {
13. let subWindow = windowStage.createSubWindow("testSubWindow");
14. subWindow.then((data) => {
15. if (!data) {
16. console.error("Failed to create the subWindow. Cause: The data is empty");
17. return;
18. }
19. windowClass = data;
20. let promise = windowClass.setSubWindowModal(true, window.ModalityType.WINDOW_MODALITY);
21. promise.then(() => {
22. console.info('Succeeded in setting subwindow modal');
23. }).catch((err: BusinessError) => {
24. console.error(`Failed to set subwindow modal. Cause code: ${err.code}, message: ${err.message}`);
25. });
26. });
27. } catch (exception) {
28. console.error(`Failed to create the subWindow. Cause code: ${exception.code}, message: ${exception.message}`);
29. }
30. }
31. }
```

## setWindowDecorHeight11+

PhonePC/2in1TabletTVWearable

setWindowDecorHeight(height: number): void

设置窗口的标题栏高度，对存在标题栏和三键区的窗口形态生效。如果使用Stage模型，该接口需要在[loadContent()](arkts-apis-window-window.md#loadcontent9)或[setUIContent()](arkts-apis-window-window.md#setuicontent9)调用生效后使用。

当主窗口进入全屏沉浸状态时，此时鼠标Hover到窗口标题栏热区时，会显示悬浮标题栏，悬浮标题栏高度固定为37vp。

由于系统像素转换可能存在精度误差，设置后调用[getWindowDecorHeight()](arkts-apis-window-window.md#getwindowdecorheight11)获取的值可能与设置的值存在1vp的差异。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备调用不报错不生效，切换到[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态后生效；在不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备调用不报错不生效。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| height | number | 是 | 设置的窗口标题栏高度，仅支持具有窗口标题栏的窗口。该参数为整数，浮点数输入将向下取整，取值范围为[37,112]，范围外为非法参数，单位为vp。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: Invalid parameter range. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```
1. windowClass.setUIContent('pages/WindowPage').then(() => {
2. let height: number = 50;
3. try {
4. windowClass?.setWindowDecorHeight(height);
5. console.info(`Succeeded in setting the height of window decor: ${height}`);
6. } catch (exception) {
7. console.error(`Failed to set the height of window decor. Cause code: ${exception.code}, message: ${exception.message}`);
8. }
9. })
```

## setDecorButtonStyle14+

PhonePC/2in1TabletTVWearable

setDecorButtonStyle(dectorStyle: DecorButtonStyle): void

设置装饰栏按钮样式，仅对主窗和子窗生效。如果使用Stage模型，该接口需要在[loadContent()](arkts-apis-window-window.md#loadcontent9)或[setUIContent()](arkts-apis-window-window.md#setuicontent9)调用生效后使用。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：**

在HarmonyOS 5.1.0之前，该接口在2in1设备中可正常调用，在其他设备中返回801错误码。

从HarmonyOS 5.1.0开始，该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备及不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上调用返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dectorStyle | [DecorButtonStyle](arkts-apis-window-i.md#decorbuttonstyle14) | 是 | 要设置的装饰栏按钮样式。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only main windows and subwindows are supported. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { ConfigurationConstant } from '@kit.AbilityKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. onWindowStageCreate(windowStage: window.WindowStage): void {
8. try {
9. windowStage.loadContent("pages/Index").then(() =>{
10. let windowClass = windowStage.getMainWindowSync();
11. let colorMode : ConfigurationConstant.ColorMode = ConfigurationConstant.ColorMode.COLOR_MODE_LIGHT;
12. let style: window.DecorButtonStyle = {
13. colorMode: colorMode,
14. buttonBackgroundSize: 28,
15. spacingBetweenButtons: 12,
16. closeButtonRightMargin: 20,
17. buttonIconSize: 20,
18. buttonBackgroundCornerRadius: 4
19. };
20. windowClass.setDecorButtonStyle(style);
21. console.info(`Succeeded in setting the style of button. Data: ${JSON.stringify(style)}`);
22. });
23. } catch (exception) {
24. console.error(`Failed to set the style of button. Cause code: ${exception.code}, message: ${exception.message}`);
25. }
26. }
27. }
```

## getDecorButtonStyle14+

PhonePC/2in1TabletTVWearable

getDecorButtonStyle(): DecorButtonStyle

获取装饰栏按钮样式，仅对主窗和子窗生效。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：**

在HarmonyOS 5.1.0之前，该接口在2in1设备中可正常调用，在其他设备中返回801错误码。

从HarmonyOS 5.1.0开始，该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备及不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上调用返回801错误码。

从HarmonyOS 6.1.0开始，该接口在各设备均可正常调用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DecorButtonStyle](arkts-apis-window-i.md#decorbuttonstyle14) | 返回当前窗口装饰栏上的按钮样式，窗口装饰按钮区域位于窗口的右上角。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**示例：**

```
1. try {
2. let decorButtonStyle = windowClass.getDecorButtonStyle();
3. console.info(`Succeeded in getting the style of button. Data: ${JSON.stringify(decorButtonStyle)}`);
4. } catch (exception) {
5. console.error(`Failed to get the style of button. Cause code: ${exception.code}, message: ${exception.message}`);
6. }
```

## getWindowDecorHeight11+

PhonePC/2in1TabletTVWearable

getWindowDecorHeight(): number

对存在标题栏和三键区的窗口形态生效，用于获取窗口的标题栏高度。如果使用Stage模型，该接口需要在[loadContent()](arkts-apis-window-window.md#loadcontent9)或[setUIContent()](arkts-apis-window-window.md#setuicontent9)调用生效后使用。

由于系统像素转换可能存在精度误差，调用[setWindowDecorHeight()](arkts-apis-window-window.md#setwindowdecorheight11)设置的值与获取的值可能存在1vp的差异。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用；在不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上调用不生效也不报错。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回的窗口标题栏高度。该参数为整数，取值范围为[37,112]，单位为vp。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |

**示例：**

```
1. windowClass.setUIContent('pages/WindowPage').then(() => {
2. try {
3. let height = windowClass?.getWindowDecorHeight();
4. console.info(`Succeeded in getting the height of window decor: ${height}`);
5. } catch (exception) {
6. console.error(`Failed to get the height of window decor. Cause code: ${exception.code}, message: ${exception.message}`);
7. }
8. })
```

## getTitleButtonRect11+

PhonePC/2in1TabletTVWearable

getTitleButtonRect(): TitleButtonRect

获取主窗口或启用装饰的子窗口的标题栏上的最小化、最大化、关闭按钮矩形区域。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TitleButtonRect](arkts-apis-window-i.md#titlebuttonrect11) | 标题栏上的最小化、最大化、关闭按钮矩形区域，该区域位置坐标相对窗口右上角。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. // ...
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. console.info('onWindowStageCreate');
10. let windowClass: window.Window | undefined = undefined;
11. windowStage.getMainWindow((err: BusinessError, data) => {
12. const errCode: number = err.code;
13. if (errCode) {
14. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
15. return;
16. }
17. windowClass = data;
18. try {
19. let titleButtonArea = windowClass.getTitleButtonRect();
20. console.info('Succeeded in obtaining the area of title buttons. Data: ' + JSON.stringify(titleButtonArea));
21. } catch (exception) {
22. console.error(`Failed to get the area of title buttons. Cause code: ${exception.code}, message: ${exception.message}`);
23. }
24. });
25. }
26. }
```

## getWindowStatus12+

PhonePC/2in1TabletTVWearable

getWindowStatus(): WindowStatusType

获取当前应用窗口的模式。

说明

在[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态下，应用的[targetAPIVersion](../harmonyos-guides/app-configuration-file.md#配置文件标签)设置小于14时，在窗口最大化状态（窗口铺满整个屏幕，2in1设备会有dock栏和状态栏，Tablet设备会有状态栏）时返回值对应为WindowStatusType::FULL\_SCREEN。应用的[targetAPIVersion](../harmonyos-guides/app-configuration-file.md#配置文件标签)设置大于等于14时，在窗口最大化状态（窗口铺满整个屏幕，2in1设备会有dock栏和状态栏，Tablet设备会有状态栏）时返回值对应为WindowStatusType::MAXIMIZE。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WindowStatusType](arkts-apis-window-e.md#windowstatustype11) | 当前窗口模式。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```
1. try {
2. let windowStatusType = windowClass.getWindowStatus();
3. } catch (exception) {
4. console.error(`Failed to obtain the window status of window. Cause code: ${exception.code}, message: ${exception.message}`);
5. }
```

## isFocused12+

PhonePC/2in1TabletTVWearable

isFocused(): boolean

判断当前窗口是否已获焦。为获取准确的获焦状态，需要在[WindowEventType](arkts-apis-window-e.md#windoweventtype10)生命周期处于WINDOW\_ACTIVE之后调用。

可使用[on('windowEvent')](arkts-apis-window-window.md#onwindowevent10)监听对应状态变更，再执行对应具体业务。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 当前窗口是否已获焦。true表示当前窗口已获焦，false则表示当前窗口未获焦。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```
1. try {
2. let focus = windowClass.isFocused();
3. console.info(`Succeeded in checking whether the window is focused. Data: ${focus}`);
4. } catch (exception) {
5. console.error(`Failed to check whether the window is focused. Cause code: ${exception.code}, message: ${exception.message}`);
6. }
```

## createSubWindowWithOptions12+

PhonePC/2in1TabletTVWearable

createSubWindowWithOptions(name: string, options: SubWindowOptions): Promise<Window>

创建主窗口、子窗口或悬浮窗下的子窗口，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**设备行为差异：** 该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备及不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上调用返回undefined。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 子窗口的名字。 |
| options | [SubWindowOptions](arkts-apis-window-i.md#subwindowoptions11) | 是 | 子窗口参数。decorEnabled为true时，子窗口为非[沉浸式布局](../harmonyos-guides/window-terminology.md#沉浸式布局)；decorEnabled为false时，子窗口为沉浸式布局。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Window](arkts-apis-window-window.md)> | Promise对象。返回当前Window下创建的子窗口对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error; 3. The subWindow has been created and can not be created again. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only main windows, subwindows, and floating windows are supported. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let options : window.SubWindowOptions = {
5. title: 'title',
6. decorEnabled: true,
7. isModal: true
8. };
9. let promise = windowClass.createSubWindowWithOptions('mySubWindow', options);
10. promise.then((data) => {
11. console.info(`Succeeded in creating the subwindow. Data: ${JSON.stringify(data)}`);
12. }).catch((err: BusinessError) => {
13. console.error(`Failed to create the subwindow. Cause code: ${err.code}, message: ${err.message}`);
14. });
15. } catch (exception) {
16. console.error(`Failed to create the subwindow. Cause code: ${exception.code}, message: ${exception.message}`);
17. }
```

## setParentWindow19+

PhonePC/2in1TabletTVWearable

setParentWindow(windowId: number): Promise<void>

更改子窗口的父窗口，该父窗口仅支持同进程下的主窗口、子窗口或悬浮窗，使用Promise异步回调。

如果该子窗口处于获焦状态，且新的父窗口处于前台，则会抬升父窗口的层级。

如果该子窗口处于获焦状态，且新的父窗口的子窗口存在层级更高的模态子窗口，则焦点会转移给该模态子窗口。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：**

在HarmonyOS 6.1.0之前，该接口在2in1设备中可正常调用，在其他设备中返回801错误码。

从HarmonyOS 6.1.0开始，该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备及不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上调用返回801错误码。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| windowId | number | 是 | 父窗口id，该参数应为整数。推荐使用[getWindowProperties()](arkts-apis-window-window.md#getwindowproperties9)方法获取父窗口id属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |
| 1300009 | The parent window is invalid. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let windowClass: window.Window = window.findWindow("subWindow");
5. let newParentWindow: window.Window = window.findWindow("newParentWindow");
6. let newParentWindowId: number = newParentWindow.getWindowProperties().id;
7. let promise = windowClass.setParentWindow(newParentWindowId);
8. promise.then(() => {
9. console.info('Succeeded in setting the new parent window.');
10. }).catch((err: BusinessError) => {
11. console.error(`Failed to set the new parent window. Cause code: ${err.code}, message: ${err.message}`);
12. });
13. } catch (exception) {
14. console.error(`Failed to set the new parent window. Cause code: ${exception.code}, message: ${exception.message}`);
15. }
```

## getParentWindow19+

PhonePC/2in1TabletTVWearable

getParentWindow(): Window

获取子窗口的父窗口。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：**

在HarmonyOS 6.1.0之前，该接口在2in1设备中可正常调用，在其他设备中返回801错误码。

从HarmonyOS 6.1.0开始，该接口在各设备均可正常调用。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Window](arkts-apis-window-window.md) | 子窗口的父窗口对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300004 | Unauthorized operation. |
| 1300009 | The parent window is invalid. |

**示例：**

```
1. try {
2. let windowClass: window.Window = window.findWindow("subWindow");
3. let parentWindow: window.Window = windowClass.getParentWindow();
4. let properties = parentWindow.getWindowProperties();
5. console.info(`Succeeded in obtaining parent window properties. Property: ${JSON.stringify(properties)}`);
6. } catch (exception) {
7. console.error(`Failed to get the parent window. Cause code: ${exception.code}, message: ${exception.message}`);
8. }
```

## setWindowTitleButtonVisible14+

PhonePC/2in1TabletTVWearable

setWindowTitleButtonVisible(isMaximizeButtonVisible: boolean, isMinimizeButtonVisible: boolean, isCloseButtonVisible?: boolean): void

设置主窗标题栏上的最大化、最小化、关闭按钮是否可见。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备及不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上调用返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isMaximizeButtonVisible | boolean | 是 | 设置最大化按钮是否可见，true为可见，false为隐藏。如果最大化按钮隐藏，那么在最大化场景下，也隐藏对应的还原按钮。 |
| isMinimizeButtonVisible | boolean | 是 | 设置最小化按钮是否可见，true为可见，false为隐藏。 |
| isCloseButtonVisible | boolean | 否 | 设置关闭按钮是否可见，true为可见，false为隐藏，默认值true。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300004 | Unauthorized operation. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. onWindowStageCreate(windowStage: window.WindowStage): void {
8. // 加载主窗口对应的页面
9. windowStage.loadContent('pages/Index', (err) => {
10. let mainWindow: window.Window | undefined = undefined;
11. // 获取应用主窗口。
12. windowStage.getMainWindow().then(
13. data => {
14. if (!data) {
15. console.error('Failed to get main window. Cause: The data is undefined.');
16. return;
17. }
18. mainWindow = data;
19. console.info('Succeeded in obtaining the main window. Data: ' + JSON.stringify(data));
20. // 调用setWindowTitleButtonVisible接口，隐藏主窗标题栏最大化、最小化、关闭按钮。
21. mainWindow.setWindowTitleButtonVisible(false, false, false);
22. }
23. ).catch((err: BusinessError) => {
24. if(err.code){
25. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
26. }
27. });
28. });
29. }
30. }
```

## setWindowTopmost14+

PhonePC/2in1TabletTVWearable

setWindowTopmost(isWindowTopmost: boolean): Promise<void>

应用主窗口调用，用于实现将窗口置于其他应用窗口之上不被遮挡，使用Promise异步回调。

应用可通过自定义快捷键实现主窗口的置顶和取消置顶。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备及不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上调用返回801错误码。

**需要权限：** ohos.permission.WINDOW\_TOPMOST

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isWindowTopmost | boolean | 是 | 设置主窗口置顶，true为置顶，false为取消置顶。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only main windows are supported. |

**示例：**

```
1. // Index.ets
2. import { window } from '@kit.ArkUI';
3. import { common } from '@kit.AbilityKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. let windowClass: window.Window | undefined;
7. let keyUpEventAry: string[] = [];

9. @Entry
10. @Component
11. struct Index {
12. private context = (this.getUIContext()?.getHostContext() as common.UIAbilityContext);
13. private windowStage = this.context.windowStage;

15. build() {
16. RelativeContainer() {
17. Button("窗口置顶")
18. .onClick(() => {
19. try {
20. windowClass = this.windowStage.getMainWindowSync();
21. // true:窗口置顶，false:取消窗口置顶
22. let isWindowTopmost: boolean = true;
23. let promiseTopmost = windowClass.setWindowTopmost(isWindowTopmost);
24. promiseTopmost.then(() => {
25. console.info('Succeeded in setting the main window to be topmost.');
26. }).catch((err: BusinessError) => {
27. console.error(`Failed to set the main window to be topmost. Cause code: ${err.code}, message: ${err.message}`);
28. });
29. } catch (exception) {
30. console.error(`Failed to obtain the top window. Cause code: ${exception.code}, message: ${exception.message}`)
31. }
32. })
33. }
34. .height('100%')
35. .width('100%')
36. .onKeyEvent((event) => {
37. if(event) {
38. if(event.type === KeyType.Down) {
39. keyUpEventAry = [];
40. }
41. if(event.type === KeyType.Up) {
42. keyUpEventAry.push(event.keyText);
43. // 自定义快捷键 ctrl+T 执行主窗口置顶、取消置顶的操作
44. if(windowClass && keyUpEventAry.includes('KEYCODE_CTRL_LEFT') && keyUpEventAry.includes('KEYCODE_T')) {
45. let isWindowTopmost: boolean = false;
46. windowClass.setWindowTopmost(isWindowTopmost);
47. }
48. }
49. }
50. })
51. }
52. }
```

## raiseToAppTop14+

PhonePC/2in1TabletTVWearable

raiseToAppTop(): Promise<void>

应用子窗口调用，提升应用子窗口到顶层，只在当前应用同一个父窗口下的相同类型子窗范围内生效，对于自定义了zLevel属性的子窗口，只在当前应用同一个父窗口下相同zLevel值的子窗范围内生效。使用Promise异步回调。

使用该接口需要先创建子窗口，并确保该子窗口调用[showWindow()](arkts-apis-window-window.md#showwindow9)并执行完毕。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |
| 1300009 | The parent window is invalid. |

**示例：**

```
1. // EntryAbility.ets
2. import { window } from '@kit.ArkUI';
3. import { UIAbility } from '@kit.AbilityKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. export default class EntryAbility extends UIAbility {
7. // ...
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. console.info('onWindowStageCreate');
10. // 创建子窗
11. windowStage.createSubWindow('testSubWindow').then((subWindow) => {
12. if (subWindow == null) {
13. console.error('Failed to create the subWindow. Cause: The data is empty');
14. return;
15. }
16. subWindow.showWindow().then(() => {
17. subWindow.raiseToAppTop().then(() => {
18. console.info('Succeeded in raising window to app top');
19. }).catch((err: BusinessError)=>{
20. console.error(`Failed to raise window to app top. Cause code: ${err.code}, message: ${err.message}`);
21. });
22. });
23. });
24. }
25. }
```

## setRaiseByClickEnabled14+

PhonePC/2in1TabletTVWearable

setRaiseByClickEnabled(enable: boolean): Promise<void>

禁止/使能子窗点击抬升功能。使用Promise异步回调。

通常来说，点击一个子窗口，会将该子窗口显示抬升到应用内同一个父窗口下同类型子窗口的最上方，如果设置为false，那么点击子窗口的时候，不会将该子窗口进行抬升，而是保持不变。

使用该接口需要先创建子窗口，并确保该子窗口调用[showWindow()](arkts-apis-window-window.md#showwindow9)并执行完毕。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 设置子窗口点击抬升功能是否使能，true表示使能，false表示禁止。 |

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
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |
| 1300009 | The parent window is invalid. |

**示例：**

```
1. // EntryAbility.ets
2. import { window } from '@kit.ArkUI';
3. import { UIAbility } from '@kit.AbilityKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. export default class EntryAbility extends UIAbility {
7. // ...
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. console.info('onWindowStageCreate');
10. // 创建子窗
11. windowStage.createSubWindow("testSubWindow").then((subWindow) => {
12. if (subWindow == null) {
13. console.error('Failed to create the subWindow. Cause: The data is empty');
14. return;
15. }
16. subWindow.showWindow().then(() => {
17. try {
18. let enabled = false;
19. subWindow.setRaiseByClickEnabled(enabled).then(() => {
20. console.info('Succeeded in disabling the raise-by-click function.');
21. }).catch((err: BusinessError) => {
22. console.error(`Failed to disable the raise-by-click function. Cause code: ${err.code}, message: ${err.message}`);
23. });
24. } catch (err) {
25. console.error(`Failed to disable the raise-by-click function. Cause code: ${err.code}, message: ${err.message}`);
26. }
27. });
28. });
29. }
30. }
```

## enableLandscapeMultiWindow12+

PhonePC/2in1TabletTVWearable

enableLandscapeMultiWindow(): Promise<void>

应用部分界面支持横向布局时，在进入该界面时使能，使能后可支持进入横向多窗。不建议竖向布局界面使用。

此接口只对应用主窗口生效，且需要在module.json5配置文件中[abilities](../harmonyos-guides/module-configuration-file.md#abilities标签)标签中配置preferMultiWindowOrientation属性为"landscape\_auto"。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

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

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. // ...
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. console.info('onWindowStageCreate');
10. let windowClass: window.Window | undefined = undefined;
11. windowStage.getMainWindow((err: BusinessError, data) => {
12. const errCode: number = err.code;
13. if (errCode) {
14. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
15. return;
16. }
17. windowClass = data;
18. let promise = windowClass.enableLandscapeMultiWindow();
19. promise.then(() => {
20. console.info('Succeeded in making multi-window become landscape.');
21. }).catch((err: BusinessError) => {
22. console.error(`Failed to make multi-window become landscape. Cause code: ${err.code}, message: ${err.message}`);
23. });
24. });
25. }
26. }
```

## disableLandscapeMultiWindow12+

PhonePC/2in1TabletTVWearable

disableLandscapeMultiWindow(): Promise<void>

应用部分界面支持横向布局时，在退出该界面时去使能，去使能后不支持进入横向多窗。

此接口只对应用主窗口生效，且需要在module.json5配置文件中[abilities](../harmonyos-guides/module-configuration-file.md#abilities标签)标签中配置preferMultiWindowOrientation属性为"landscape\_auto"。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

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

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. // ...
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. console.info('onWindowStageCreate');
10. let windowClass: window.Window | undefined = undefined;
11. windowStage.getMainWindow((err: BusinessError, data) => {
12. const errCode: number = err.code;
13. if (errCode) {
14. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
15. return;
16. }
17. windowClass = data;
18. let promise = windowClass.disableLandscapeMultiWindow();
19. promise.then(() => {
20. console.info('Succeeded in making multi-window become not landscape.');
21. }).catch((err: BusinessError) => {
22. console.error(`Failed to make multi-window become not landscape. Cause code: ${err.code}, message: ${err.message}`);
23. });
24. });
25. }
26. }
```

## setDialogBackGestureEnabled12+

PhonePC/2in1TabletTVWearable

setDialogBackGestureEnabled(enabled: boolean): Promise<void>

设置模态窗口是否响应手势返回事件，非模态窗口调用返回错误码。

**系统能力**：SystemCapability.Window.SessionManager

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 是否响应手势返回事件。  true表示响应手势返回事件，触发onBackPress回调；false表示不响应手势返回事件，不触发onBackPress回调。 |

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
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. onWindowStageCreate(windowStage: window.WindowStage): void {
8. console.info('onWindowStageCreate');
9. let windowClass: window.Window | undefined = undefined;
10. let config: window.Configuration = {
11. name: "test",
12. windowType: window.WindowType.TYPE_DIALOG,
13. ctx: this.context
14. };
15. try {
16. window.createWindow(config, (err: BusinessError, data) => {
17. const errCode: number = err.code;
18. if (errCode) {
19. console.error(`Failed to create the window. Cause code: ${err.code}, message: ${err.message}`);
20. return;
21. }
22. windowClass = data;
23. windowClass.setUIContent("pages/Index");
24. let enabled = true;
25. let promise = windowClass.setDialogBackGestureEnabled(enabled);
26. promise.then(() => {
27. console.info('Succeeded in setting dialog window to respond back gesture.');
28. }).catch((err: BusinessError) => {
29. console.error(`Failed to set dialog window to respond back gesture. Cause code: ${err.code}, message: ${err.message}`);
30. });
31. });
32. } catch (exception) {
33. console.error(`Failed to create the window. Cause code: ${exception.code}, message: ${exception.message}`);
34. }
35. }
36. }
```

```
1. // ets/pages/Index.ets
2. @Entry
3. @Component
4. struct Index {
5. @State message: string = 'Hello World'
6. build() {
7. RelativeContainer() {
8. Text(this.message)
9. .id('HelloWorld')
10. .fontSize(50)
11. .fontWeight(FontWeight.Bold)
12. }
13. .height('100%')
14. .width('100%')
15. }

17. onBackPress(): boolean | void {
18. console.info('Succeeded in setting dialog window to respond back gesture.');
19. return true;
20. }
21. }
```

## enableDrag20+

PhonePC/2in1TabletTVWearable

enableDrag(enable: boolean): Promise<void>

使能/禁止拖拽窗口，仅对系统窗口、应用子窗口、全局悬浮窗和模态窗口生效。使用Promise异步回调。

使能后，将允许通过鼠标操作或触摸对窗口进行拉伸操作。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在Phone设备、Tablet设备和2in1设备上可正常调用，在其他设备中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 是否允许拖拽。  true表示允许，false表示不允许。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. windowClass.enableDrag(true).then(() => {
5. console.info('succeeded in setting window draggable');
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to set window draggable. Cause code: ${err.code}, message: ${err.message}`);
8. });
9. } catch (exception) {
10. console.error(`Failed to set window draggable. Cause code: ${exception.code}, message: ${exception.message}`);
11. }
```

## startMoving14+

PhonePC/2in1TabletTVWearable

startMoving(): Promise<void>

开始移动窗口，使用Promise异步回调。

[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态下，对系统窗口、应用主窗口、应用子窗口、全局悬浮窗和模态窗口生效。非自由窗口状态下，仅对系统窗口、应用子窗口、全局悬浮窗和模态窗口生效，应用主窗口调用该接口返回801或1300004错误码。

仅在[onTouch](ts-universal-events-touch.md#touchevent对象说明)事件（其中，事件类型必须为TouchType.Down）的回调方法中调用此接口才会有移动效果，成功调用此接口后，窗口将跟随鼠标或触摸点移动。

在点击拖拽场景下，若不期望在按下时触发拖拽事件，则可以在事件类型为[TouchType.Move](ts-appendix-enums.md#touchtype)（需要保证当前行为已经触发TouchType.Down事件）时调用此接口，触发移动效果。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300001 | Repeated operation. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**示例：**

```
1. // Index.ets
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { window } from '@kit.ArkUI';

5. @Entry
6. @Component
7. struct Index {
8. private isTouchDown: boolean = false;
9. build() {
10. Row() {
11. Column() {
12. Blank('160')
13. .color(Color.Red)
14. .onTouch((event: TouchEvent) => {
15. if(event.type == TouchType.Down){
16. this.isTouchDown = true;
17. } else if (event.type === TouchType.Move && this.isTouchDown) {
18. try {
19. let context = this.getUIContext()?.getHostContext();
20. if (!context) {
21. console.error('Failed to get host context.');
22. return;
23. }
24. window.getLastWindow(context).then((data)=>{
25. if (!data) {
26. console.error('Failed to get last window.');
27. return;
28. }
29. let windowClass: window.Window = data;
30. windowClass.startMoving().then(() => {
31. console.info('Succeeded in starting moving window.')
32. }).catch((err: BusinessError) => {
33. console.error(`Failed to start moving. Cause code: ${err.code}, message: ${err.message}`);
34. });
35. });
36. } catch (exception) {
37. console.error(`Failed to start moving window. Cause code: ${exception.code}, message: ${exception.message}`);
38. }
39. } else {
40. this.isTouchDown = false;
41. }
42. })
43. }.width('100%')
44. }.height('100%').width('100%')
45. }
46. }
```

## startMoving15+

PhonePC/2in1TabletTVWearable

startMoving(offsetX: number, offsetY: number): Promise<void>

指定鼠标在窗口内的位置并移动窗口，使用Promise异步回调。

在同应用内窗口分合后，且鼠标保持按下状态直接移动新窗口，如果此时鼠标快速移动，窗口移动时鼠标可能会在窗口外。可以使用本接口指定窗口移动时鼠标在窗口内的位置，先移动窗口到鼠标位置，再开始移动窗口。

仅在[onTouch](ts-universal-events-touch.md#touchevent对象说明)事件（其中，事件类型必须为TouchType.Down）的回调方法中调用此接口才会有移动效果，成功调用此接口后，窗口将跟随鼠标移动。

在点击拖拽场景下，若不期望在按下时触发拖拽事件，则可以在事件类型为[TouchType.Move](ts-appendix-enums.md#touchtype)（需要保证当前行为已经触发TouchType.Down事件）时调用此接口，触发移动效果。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备及不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上调用返回801错误码。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offsetX | number | 是 | 窗口移动时预期鼠标位置相对窗口左上角的x轴偏移量，单位为px，该参数仅支持整数输入，浮点数向下取整。负值为非法参数，大于窗口宽度为非法参数，窗口宽度可以在窗口属性[WindowProperties](arkts-apis-window-i.md#windowproperties)中获取。 |
| offsetY | number | 是 | 窗口移动时预期鼠标位置相对窗口左上角的y轴偏移量，单位为px，该参数仅支持整数输入，浮点数向下取整。负值为非法参数，大于窗口高度为非法参数，窗口高度可以在窗口属性[WindowProperties](arkts-apis-window-i.md#windowproperties)中获取。 |

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
| 1300001 | Repeated operation. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**示例：**

```
1. // Index.ets
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { window } from '@kit.ArkUI';

5. @Entry
6. @Component
7. struct Index {
8. private isTouchDown: boolean = false;
9. build() {
10. Row() {
11. Column() {
12. Blank('160')
13. .color(Color.Red)
14. .onTouch((event: TouchEvent) => {
15. if(event.type == TouchType.Down){
16. this.isTouchDown = true;
17. } else if (event.type === TouchType.Move && this.isTouchDown) {
18. try {
19. let context = this.getUIContext()?.getHostContext();
20. if (!context) {
21. console.error('Failed to get host context.');
22. return;
23. }
24. window.getLastWindow(context).then((data)=>{
25. let windowClass: window.Window = data;
26. windowClass.startMoving(100, 50).then(() => {
27. console.info('Succeeded in starting moving window.')
28. }).catch((err: BusinessError) => {
29. console.error(`Failed to start moving. Cause code: ${err.code}, message: ${err.message}`);
30. });
31. });
32. } catch (exception) {
33. console.error(`Failed to start moving window. Cause code: ${exception.code}, message: ${exception.message}`);
34. }
35. } else {
36. this.isTouchDown = false;
37. }
38. })
39. }.width('100%')
40. }.height('100%').width('100%')
41. }
42. }
```

## stopMoving15+

PhonePC/2in1TabletTVWearable

stopMoving(): Promise<void>

在窗口拖拽移动过程中，通过此接口来停止窗口移动，使用Promise异步回调。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备及不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上调用返回801错误码。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { window } from '@kit.ArkUI';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. export default class EntryAbility extends UIAbility {

8. onWindowStageCreate(windowStage: window.WindowStage) {
9. try {
10. let windowClass = windowStage.getMainWindowSync();
11. windowClass.on('windowRectChange', (data: window.RectChangeOptions) => {
12. if (data.reason === window.RectChangeReason.MOVE) {
13. windowClass.stopMoving().then(() => {
14. console.info('Succeeded in stopping moving window.')
15. }).catch((err: BusinessError) => {
16. console.error(`Failed to stop moving. Cause code: ${err.code}, message: ${err.message}`);
17. });
18. }
19. });
20. } catch (exception) {
21. console.error(`Failed to stop moving window. Cause code: ${exception.code}, message: ${exception.message}`);
22. }
23. }
24. }
```

## setGestureBackEnabled13+

PhonePC/2in1TabletTVWearable

setGestureBackEnabled(enabled: boolean): Promise<void>

设置当前窗口是否启用手势侧滑返回功能，仅主窗可以调用成功，其他类型的窗口调用返回1300004错误码。

开启此功能后，仅当窗口处于全屏模式且位于前台获焦状态下才会生效。

禁用此功能后，当前应用会禁用手势热区，侧滑返回功能失效；切换到其他应用或者回到桌面后，手势热区恢复，侧滑返回功能正常。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在2in1、其他设备的电脑模式中调用会返回801错误码，在其他设备和其他模式中可正常调用。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | true时开启返回手势功能，false时禁用返回手势功能。 |

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
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only main windows are supported. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. // ...
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. console.info('onWindowStageCreate');
10. let windowClass: window.Window | undefined = undefined;
11. windowStage.getMainWindow((err: BusinessError, data) => {
12. const errCode: number = err.code;
13. if (errCode) {
14. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
15. return;
16. }
17. windowClass = data;

19. // 设置当前窗口禁用返回手势功能
20. try {
21. let gestureBackEnabled: boolean = false;
22. let promise = windowClass.setGestureBackEnabled(gestureBackEnabled);
23. promise.then(() => {
24. console.info(`Succeeded in setting gesture back disabled`);
25. }).catch((err: BusinessError) => {
26. console.error(`Failed to set gesture back disabled, Cause code: ${err.code}, message: ${err.message}`);
27. });
28. } catch(exception) {
29. console.error(`Failed to set gesture back disabled, Cause code: ${exception.code}, message: ${exception.message}`);
30. }
31. });
32. }
33. }
```

## isGestureBackEnabled13+

PhonePC/2in1TabletTVWearable

isGestureBackEnabled(): boolean

获取当前窗口是否启用返回手势功能，仅主窗可以调用成功，其他类型的窗口调用返回1300004错误码。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在2in1、其他设备的电脑模式中调用会返回801错误码，在其他设备和其他模式中可正常调用。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否已经启用返回手势。true表示已启用返回手势功能，false表示已禁用返回手势功能。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only main windows are supported. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. // ...
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. console.info('onWindowStageCreate');
10. let windowClass: window.Window | undefined = undefined;
11. windowStage.getMainWindow((err: BusinessError, data) => {
12. const errCode: number = err.code;
13. if (errCode) {
14. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
15. return;
16. }
17. windowClass = data;

19. // 获取当前窗口是否禁用返回手势功能
20. try {
21. let gestureBackEnabled: boolean = windowClass.isGestureBackEnabled();
22. console.info(`Succeeded in obtaining gesture back enabled status: ${gestureBackEnabled}`);
23. } catch (exception) {
24. console.error(`Failed to get gesture back enabled status. Cause code: ${exception.code}, message: ${exception.message}`);
25. }
26. });
27. }
28. }
```

## setSeparationTouchEnabled23+

PhonePC/2in1TabletTVWearable

setSeparationTouchEnabled(enabled: boolean): Promise<void>

设置当前窗口是否支持事件分离状态，使用Promise异步回调。默认场景下为true，支持事件分离状态。

当enable为true，支持事件分离状态下：

* 所有手指点击产生的事件均会发送给其手指命中的窗口。

当enable为false，不支持事件分离状态下：

* 当第一根手指点击持续命中该窗口未抬起时，后续其他手指无论是否点击命中该窗口，其产生的事件均会分发给该窗口。
* 当第一根手指点击未保持持续命中该窗口时，后续其他手指即使点击命中该窗口，其产生的事件也不会分发给该窗口，该事件会被系统丢弃。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 窗口是否支持事件分离状态。true表示支持；false表示不支持。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function can not work because the current device does not support this ability. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. Possible cause: Internal IPC error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let enabled = false;
4. try {
5. let promise = windowClass.setSeparationTouchEnabled(enabled);
6. promise.then(() => {
7. console.info('Succeeded in setting the window to be separationTouchEnabled.');
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to set the window to be separationTouchEnabled. Cause code: ${err.code}, message: ${err.message}`);
10. });
11. } catch (exception) {
12. console.error(`Failed to set the separationTouchEnabled. Cause code: ${exception.code}, message: ${exception.message}`);
13. }
```

## isSeparationTouchEnabled23+

PhonePC/2in1TabletTVWearable

isSeparationTouchEnabled():boolean

获取当前窗口是否支持事件分离的状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 当前窗口是否支持事件分离。  true表示支持窗口事件分离，false表示不支持窗口事件分离。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function can not work because the current device does not support this ability. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let isSeparationTouchEnabled = windowClass.isSeparationTouchEnabled();
5. console.info(`Succeeded in getting the window separationTouchEnabled status: ${isSeparationTouchEnabled}`);
6. } catch (exception) {
7. console.error(`Failed to get the window separationTouchEnabled status.. Cause code: ${exception.code}, message: ${exception.message}`);
8. }
```

## setReceiveDragEventEnabled23+

PhonePC/2in1TabletTVWearable

setReceiveDragEventEnabled(enabled: boolean): Promise<void>

设置当前窗口是否能接收[拖拽事件](ts-universal-events-drag-drop.md#dragevent7)，使用Promise异步回调。

默认场景下为true，能够接收拖拽事件。

当enable为false，当前窗口不能接收拖拽事件。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 窗口是否能接收拖拽事件。true表示能够接收拖拽事件；false表示不能接收拖拽事件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function can not work because the current device does not support this ability. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. Possible cause: Internal IPC error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let enabled = false;
4. try {
5. let promise = windowClass.setReceiveDragEventEnabled(enabled);
6. promise.then(() => {
7. console.info('Succeeded in setting the window to be WindowReceiveDragEventEnabled.');
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to set the window to be the window ReceiveDragEventEnabled. Cause code: ${err.code}, message: ${err.message}`);
10. });
11. } catch (exception) {
12. console.error(`Failed to set the window ReceiveDragEventEnabled. Cause code: ${exception.code}, message: ${exception.message}`);
13. }
```

## isReceiveDragEventEnabled23+

PhonePC/2in1TabletTVWearable

isReceiveDragEventEnabled():boolean

获取当前窗口是否能接收[拖拽事件](ts-universal-events-drag-drop.md#dragevent7)的状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 当前窗口是否能接收拖拽事件的状态。  true表示能接收拖拽事件的状态，false表示不能接收拖拽事件的状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function can not work because the current device does not support this ability. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let isReceiveDragEventEnabled = windowClass.isReceiveDragEventEnabled();
5. console.info(`Succeeded in getting the window receiveDragEvent status: ${isReceiveDragEventEnabled}`);
6. } catch (exception) {
7. console.error(`Failed to get the window receiveDragEvent status. Cause code: ${exception.code}, message: ${exception.message}`);
8. }
```

## setWindowShadowRadius17+

PhonePC/2in1TabletTVWearable

setWindowShadowRadius(radius: number): void

设置子窗或悬浮窗窗口边缘阴影的模糊半径。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：**

在HarmonyOS 5.1.0之前，该接口在2in1设备、Tablet设备中可正常调用，在其他设备中返回801错误码。

从HarmonyOS 5.1.0开始，该接口在Phone设备、Tablet设备和2in1设备中可正常调用，在其他设备中返回801错误码。

**元服务API：** 从API version 17开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radius | number | 是 | 表示窗口边缘阴影的模糊半径。该参数为浮点数，单位为px，取值范围为[0.0, +∞)，取值为0.0时表示关闭窗口边缘阴影。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: The shadow radius is less than zero. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only subwindows and float windows are supported. |

**示例：**

```
1. try {
2. windowClass.setWindowShadowRadius(4.0);
3. } catch (exception) {
4. console.error(`Failed to set shadow. Cause code: ${exception.code}, message: ${exception.message}`);
5. }
```

## setWindowCornerRadius17+

PhonePC/2in1TabletTVWearable

setWindowCornerRadius(cornerRadius: number): Promise<void>

设置子窗或悬浮窗的圆角半径值，使用Promise异步回调。

圆角半径值过大将会导致三键（最大化、最小化、关闭按钮）位置被裁切，且会导致热区不易识别，请根据窗口大小设置合适的圆角半径值。

在调用此接口之前调用[getWindowCornerRadius()](arkts-apis-window-window.md#getwindowcornerradius17)接口可以获得窗口默认圆角半径值。

**系统能力**：SystemCapability.Window.SessionManager

**设备行为差异：**

在HarmonyOS 6.0.0之前，该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备及不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上调用返回801错误码。

从HarmonyOS 6.0.0开始，该接口在Phone设备、Tablet设备和2in1设备下可正常调用，在其他设备中返回801错误码。

**元服务API：** 从API version 17开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cornerRadius | number | 是 | 表示窗口圆角的半径值。该参数为浮点数，单位为vp，取值范围为[0.0, +∞)，取值为0.0时表示没有窗口圆角。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: The corner radius is less than zero. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let promise = windowClass.setWindowCornerRadius(1.0);
5. promise.then(() => {
6. console.info('Succeeded in setting window corner radius.');
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to set window corner radius. Cause code: ${err.code}, message: ${err.message}`);
9. });
10. } catch (exception) {
11. console.error(`Failed to set corner radius. Cause code: ${exception.code}, message: ${exception.message}`);
12. }
```

## getWindowCornerRadius17+

PhonePC/2in1TabletTVWearable

getWindowCornerRadius(): number

该接口用于获取子窗或悬浮窗的圆角半径值，在未调用[setWindowCornerRadius()](arkts-apis-window-window.md#setwindowcornerradius17)接口设置窗口圆角半径值时，调用此接口可获取窗口默认圆角半径值。

**系统能力**：SystemCapability.Window.SessionManager

**设备行为差异：**

在HarmonyOS 6.1.0之前，该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备及不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上调用返回801错误码。

从HarmonyOS 6.1.0开始，该接口在Phone、Tablet、PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**元服务API：** 从API version 17开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前子窗或悬浮窗的圆角半径值，单位为vp。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only subwindows and float windows are supported. |

**示例：**

```
1. try {
2. let cornerRadius = windowClass.getWindowCornerRadius();
3. } catch (exception) {
4. console.error(`Failed to get corner radius. Cause code: ${exception.code}, message: ${exception.message}`);
5. }
```

## setExclusivelyHighlighted15+

PhonePC/2in1TabletTVWearable

setExclusivelyHighlighted(exclusivelyHighlighted: boolean): Promise<void>

设置窗口独占激活态属性。独占激活态表示窗口获焦时，会导致当前父子窗口链中处于激活态的其他窗口失去激活态。使用Promise异步回调。

此接口对主窗、模态窗不生效。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| exclusivelyHighlighted | boolean | 是 | 窗口是否独占激活态。true表示独占激活态；false表示不独占激活态。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let exclusivelyHighlighted: boolean = true;
4. try {
5. let promise = windowClass.setExclusivelyHighlighted(exclusivelyHighlighted);
6. promise.then(() => {
7. console.info('Succeeded in setting the window to be exclusively highlight.');
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to set the window to be exclusively highlight. Cause code: ${err.code}, message: ${err.message}`);
10. });
11. } catch (exception) {
12. console.error(`Failed to set the window to be exclusively highlight. Cause code: ${exception.code}, message: ${exception.message}`);
13. }
```

## isWindowHighlighted18+

PhonePC/2in1TabletTVWearable

isWindowHighlighted(): boolean

获取当前窗口是否为激活态。为准确获取激活态，需要在[WindowEventType](arkts-apis-window-e.md#windoweventtype10)生命周期处于WINDOW\_ACTIVE之后调用。

可使用[on('windowHighlightChange')](arkts-apis-window-window.md#onwindowhighlightchange15)监听对应状态变更，再执行对应具体业务。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 当前窗口是否为激活态。true表示当前窗口为激活态，false表示当前窗口非激活态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal Possible cause: The window is not created or destroyed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let isHighlighted = windowClass.isWindowHighlighted();
5. console.info(`Succeeded in getting the window highlight status: ${isHighlighted}`);
6. } catch (exception) {
7. console.error(`Failed to get the window highlight status.. Cause code: ${exception.code}, message: ${exception.message}`);
8. }
```

## setFollowParentMultiScreenPolicy17+

PhonePC/2in1TabletTVWearable

setFollowParentMultiScreenPolicy(enabled: boolean): Promise<void>

设置子窗口在其父窗口处于拖拽移动或拖拽缩放过程时，该子窗口是否支持跨多个屏幕同时显示。使用Promise异步回调。

通过监听父窗口大小位置变化，对子窗口调用[moveWindowTo()](arkts-apis-window-window.md#movewindowto9)等接口实现子窗口跟随父窗口布局时，此时子窗口默认不支持跨多个屏幕同时显示。

对子窗口调用此接口后可以使能子窗口在跟随父窗口布局过程中跨多个屏幕同时显示。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：**

在HarmonyOS 6.1.0之前，该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备及不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上调用返回801错误码。

从HarmonyOS 6.1.0开始，该接口在Phone、Tablet、PC/2in1设备可正常调用，在其他设备调用返回801错误码。

**元服务API：** 从API version 17开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 设置子窗口在其父窗口处于拖拽移动或拖拽缩放过程时，该子窗口是否支持跨多个屏幕同时显示。true表示支持；false表示不支持。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported.Function setFollowParentMultiScreenPolicy can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let windowClass: window.Window = window.findWindow("subWindow");
5. let enabled: boolean = true;
6. let promise = windowClass?.setFollowParentMultiScreenPolicy(enabled);
7. promise.then(() => {
8. console.info('Succeeded in setting the sub window supports multi-screen simultaneous display')
9. }).catch((err: BusinessError) => {
10. console.error(`Failed to set the sub window supports multi-screen simultaneous display. Cause code: ${err.code}, message: ${err.message}`);
11. });
12. } catch (exception) {
13. console.error(`Failed to set the sub window supports multi-screen simultaneous display. Cause code: ${exception.code}, message: ${exception.message}`);
14. }
```

## setFollowParentWindowLayoutEnabled17+

PhonePC/2in1TabletTVWearable

setFollowParentWindowLayoutEnabled(enabled: boolean): Promise<void>

设置子窗或模态窗口（即WindowType为TYPE\_DIALOG的窗口）的布局信息（position和size）是否跟随主窗，使用Promise异步回调。

1、只支持主窗的一级子窗或模态窗口使用该接口。

2、当子窗或模态窗口调用该接口后，立即使其布局信息与主窗完全一致并保持，除非传入false再次调用该接口，否则效果将持续。

3、当子窗或模态窗口调用该接口后，再调用moveTo、resize等修改布局信息的接口将不生效。

4、当子窗或模态窗口不再使用该功能后，不保证子窗或模态窗口的布局信息（position和size）为确定的值，需要应用重新进行设置。

该接口调用生效后，[setRelativePositionToParentWindowEnabled()](arkts-apis-window-window.md#setrelativepositiontoparentwindowenabled20)接口调用不生效。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 17开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 设置是否启用跟随主窗布局。true表示启用，false表示不启用。 |

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
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed. 2. Internal task error. 3. The subwindow level is more than one. 4. The subwindow is following its parent window's position. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only subwindows and dialog windows are supported. |

**示例：**

```
1. // EntryAbility.ets
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { UIAbility } from '@kit.AbilityKit';

6. export default class EntryAbility extends UIAbility {
7. onWindowStageCreate(windowStage: window.WindowStage): void {
8. windowStage.loadContent('pages/Index', (loadError) => {
9. if (loadError.code) {
10. console.error(`Failed to load the content. Cause code: ${loadError.code}, message: ${loadError.message}`);
11. return;
12. }
13. console.info("Succeeded in loading the content.");
14. windowStage.createSubWindow("subWindow").then((subWindow: window.Window) => {
15. if (subWindow == null) {
16. console.error("Failed to create the subWindow. Cause: The data is empty");
17. return;
18. }
19. subWindow.setFollowParentWindowLayoutEnabled(true).then(() => {
20. console.info("after set follow parent window layout")
21. }).catch((error: BusinessError) => {
22. console.error(`setFollowParentWindowLayoutEnabled failed. ${error.code} ${error.message}`);
23. })
24. }).catch((error: BusinessError) => {
25. console.error(`createSubWindow failed. ${error.code} ${error.message}`);
26. })
27. });
28. }
29. }
```

## setRelativePositionToParentWindowEnabled20+

PhonePC/2in1TabletTVWearable

setRelativePositionToParentWindowEnabled(enabled: boolean, anchor?: WindowAnchor, offsetX?: number, offsetY?: number): Promise<void>

用于设置一级子窗是否支持与主窗保持相对位置不变。使用Promise异步回调。

该相对位置通过一级子窗与主窗之间锚点的偏移量表示，子窗和主窗使用的窗口锚点相同。

1. 只支持一级子窗调用该接口，子窗需处于自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING）。
2. 当子窗调用该接口后，立即使其显示位置跟随主窗并保持相对位置不变，除非传入false再次调用该接口，否则效果将持续。
3. 当子窗调用该接口后，再调用[moveWindowTo()](arkts-apis-window-window.md#movewindowto9)、[maximize()](arkts-apis-window-window.md#maximize12)修改窗口位置或大小的接口将不生效。

该接口调用生效后，[setFollowParentWindowLayoutEnabled()](arkts-apis-window-window.md#setfollowparentwindowlayoutenabled17)接口调用不生效。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：**

在HarmonyOS 6.1.0之前，该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备（Phone设备除外，在Phone设备上调用该接口会返回801错误码）上可正常调用；在支持并不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上调用不报错不生效；在不支持自由窗口的设备中返回801错误码。

从HarmonyOS 6.1.0开始，该接口在Phone、Tablet、2in1设备上可调用且不报错（当设备处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态时可正常调用此接口并生效；当设备不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态时调用此接口不生效不报错，设备切换到自由窗口状态时生效）；在其他设备中调用返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 一级子窗是否支持与主窗保持相对位置不变。true表示支持；false表示不支持。 |
| anchor | [WindowAnchor](arkts-apis-window-e.md#windowanchor20) | 否 | 一级子窗与主窗保持相对位置不变时的窗口锚点枚举。该参数仅在enabled为true时生效，默认值为window.WindowAnchor.TopStart，即默认锚点为窗口左上角。 |
| offsetX | number | 否 | 一级子窗锚点与主窗锚点位置的x轴偏移量，单位为px。该参数仅在enabled为true时生效，仅支持整数输入，浮点数向下取整，默认值为0。 |
| offsetY | number | 否 | 一级子窗锚点与主窗锚点位置的y轴偏移量，单位为px。该参数仅在enabled为true时生效，仅支持整数输入，浮点数向下取整，默认值为0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.Function setRelativePositionToParentWindowEnabled can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only subwindows are supported. |

**示例：**

```
1. // EntryAbility.ets
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { UIAbility } from '@kit.AbilityKit';

6. export default class EntryAbility extends UIAbility {
7. onWindowStageCreate(windowStage: window.WindowStage): void {
8. windowStage.loadContent('pages/Index', (loadError: BusinessError) => {
9. if (loadError.code) {
10. console.error(`Failed to load the content. Cause code: ${loadError.code}, message: ${loadError.message}`);
11. return;
12. }
13. console.info("Succeeded in loading the content.");
14. windowStage.createSubWindow("subWindow").then((subWindow: window.Window) => {
15. if (subWindow == null) {
16. console.error("Failed to create the subWindow. Cause: The data is empty");
17. return;
18. }
19. subWindow.setRelativePositionToParentWindowEnabled(true).then(() => {
20. console.info("after set relative position to parent window enabled");
21. }).catch((error: BusinessError) => {
22. console.error(`setRelativePositionToParentWindowEnabled failed. ${error.code} ${error.message}`);
23. })
24. }).catch((error: BusinessError) => {
25. console.error(`createSubWindow failed. ${error.code} ${error.message}`);
26. })
27. });
28. }
29. }
```

## setWindowTransitionAnimation20+

PhonePC/2in1TabletTVWearable

setWindowTransitionAnimation(transitionType: WindowTransitionType, animation: TransitionAnimation): Promise<void>

给特定场景下的窗口增加转场动画。

当前只支持在应用主窗下使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用，在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备及不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上调用返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| transitionType | [WindowTransitionType](arkts-apis-window-e.md#windowtransitiontype20) | 是 | 本次转场动画场景。当前只支持销毁场景。 |
| animation | [TransitionAnimation](arkts-apis-window-i.md#transitionanimation20) | 是 | 本次转场动画配置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |
| 1300016 | Parameter error. Possible cause: 1. Invalid parameter range; 2. Invalid parameter length. |

**示例：**

```
1. // EntryAbility.ets
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { UIAbility } from '@kit.AbilityKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. // ...
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. console.info('onWindowStageCreate');
10. let windowClass: window.Window | undefined = undefined;
11. windowStage.getMainWindow((err: BusinessError, data) => {
12. const errCode: number = err.code;
13. if (errCode) {
14. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
15. return;
16. }
17. windowClass = data;
18. try {
19. const animationConfig: window.WindowAnimationConfig = {
20. duration: 1000,
21. curve: window.WindowAnimationCurve.LINEAR,
22. };
23. const transitionAnimation: window.TransitionAnimation = {
24. opacity: 0.5,
25. config: animationConfig
26. };
27. let promise = windowClass.setWindowTransitionAnimation(window.WindowTransitionType.DESTROY, transitionAnimation);
28. promise.then((data) => {
29. console.info('Succeeded in setting window transition animation. Cause:' + JSON.stringify(data));
30. }).catch((err: BusinessError) => {
31. console.error(`Failed to set window transition animation. Cause code: ${err.code}, message: ${err.message}`);
32. });
33. } catch (exception) {
34. console.error(`Failed to obtain the window status of window. Cause code: ${exception.code}, message: ${exception.message}`);
35. }
36. })
37. }
38. }
```

## getWindowTransitionAnimation20+

PhonePC/2in1TabletTVWearable

getWindowTransitionAnimation(transitionType: WindowTransitionType): TransitionAnimation | undefined

获取特定场景下的窗口转场动画配置。

当前只支持在应用主窗下使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用，在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备及不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上调用返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| transitionType | [WindowTransitionType](arkts-apis-window-e.md#windowtransitiontype20) | 是 | 本次转场动画场景。当前只支持销毁场景。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TransitionAnimation](arkts-apis-window-i.md#transitionanimation20) | undefined | 对应场景下的转场动画配置。当未使用过[setWindowTransitionAnimation](arkts-apis-window-window.md#setwindowtransitionanimation20)接口时，返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |
| 1300016 | Parameter error. Possible cause: 1. Invalid parameter range. |

**示例：**

```
1. // EntryAbility.ets
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { UIAbility } from '@kit.AbilityKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. // ...
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. console.info('onWindowStageCreate');
10. let windowClass: window.Window | undefined = undefined;
11. windowStage.getMainWindow((err: BusinessError, data) => {
12. const errCode: number = err.code;
13. if (errCode) {
14. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
15. return;
16. }
17. windowClass = data;
18. try {
19. let transitionAnimationResult = windowClass.getWindowTransitionAnimation(window.WindowTransitionType.DESTROY);
20. console.info('Succeeded in getting window transition animation: ' + JSON.stringify(transitionAnimationResult));
21. } catch (exception) {
22. console.error(`Failed to obtain the window transition animation. Cause code: ${exception.code}, message: ${exception.message}`);
23. }
24. })
25. }
26. }
```

## setSubWindowZLevel18+

PhonePC/2in1TabletTVWearable

setSubWindowZLevel(zLevel: number): Promise<void>

设置当前子窗口层级级别，设置了模态属性的子窗不支持。使用Promise异步回调。

通过该接口改变子窗口的显示层级时，不会发生焦点切换。推荐使用[shiftAppWindowFocus()](arkts-apis-window-f.md#windowshiftappwindowfocus11)进行焦点切换。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**设备行为差异：** 该接口在Phone、Tablet、PC/2in1设备可正常调用，在其他设备中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| zLevel | number | 是 | 子窗口层级级别。默认值为0，取值范围为[-10000, 10000]，该参数仅支持整数输入，浮点数输入将向下取整。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Function setSubWindowZLevel can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only non-modal subwindows are supported. |
| 1300009 | The parent window is invalid. |

**示例：**

```
1. // EntryAbility.ets
2. import { window } from '@kit.ArkUI';
3. import { UIAbility } from '@kit.AbilityKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. export default class EntryAbility extends UIAbility {
7. // ...
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. console.info('onWindowStageCreate');
10. let zLevel: number = 1;
11. // 创建子窗
12. try {
13. windowStage.createSubWindow('testSubWindow').then((subWindow) => {
14. if (subWindow == null) {
15. console.error('Failed to create the sub window. Cause: The sub window is null');
16. return;
17. }
18. subWindow.setSubWindowZLevel(zLevel).then(() => {
19. console.info('Succeeded in setting sub window zLevel.');
20. }).catch((err: BusinessError) => {
21. console.error(`Failed to set sub window zLevel. Cause code: ${err.code}, message: ${err.message}`);
22. });
23. });
24. } catch (err) {
25. console.error(`Failed to create the sub window or set zLevel. Cause code: ${err.code}, message: ${err.message}`);
26. }
27. }
28. }
```

## getSubWindowZLevel18+

PhonePC/2in1TabletTVWearable

getSubWindowZLevel(): number

获取当前子窗口层级级别。不支持主窗、系统窗调用。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**设备行为差异：** 该接口在Phone、Tablet、PC/2in1设备可正常调用，在其他设备中返回801错误码。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前子窗口层级级别。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function getSubWindowZLevel can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. |

**示例：**

```
1. // EntryAbility.ets
2. import { window } from '@kit.ArkUI';
3. import { UIAbility } from '@kit.AbilityKit';

5. export default class EntryAbility extends UIAbility {
6. // ...
7. onWindowStageCreate(windowStage: window.WindowStage): void {
8. console.info('onWindowStageCreate');
9. let subWindowZLevel = -1;
10. // 创建子窗
11. windowStage.createSubWindow('testSubWindow').then((subWindow) => {
12. if (subWindow == null) {
13. console.error('Failed to create the sub window. Cause: The sub window is null');
14. return;
15. }
16. try {
17. subWindowZLevel = subWindow.getSubWindowZLevel();
18. console.info(`Succeeded in obtaining sub window zLevel: ${subWindowZLevel}`);
19. } catch (err) {
20. console.error(`Failed to obtain the sub window zLevel. Cause code: ${err.code}, message: ${err.message}`);
21. }
22. });
23. }
24. }
```

## isInFreeWindowMode22+

PhonePC/2in1TabletTVWearable

isInFreeWindowMode(): boolean

查询当前窗口是否为[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)模式。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示在自由窗口模式，false表示非自由窗口模式。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. let isInFreeWindowMode: boolean = windowClass.isInFreeWindowMode();
2. console.info(`isInFreeWindowMode: ${isInFreeWindowMode}`);
```

## on('freeWindowModeChange')22+

PhonePC/2in1TabletTVWearable

on(type: 'freeWindowModeChange', callback: Callback<boolean>): void

开启自由窗口模式变化事件的监听。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'freeWindowModeChange'，即自由窗口模式变化事件。 |
| callback | Callback<boolean> | 是 | 回调函数。返回当前窗口是否在自由窗口模式，true表示是自由窗口模式，false表示非自由窗口模式。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. try {
2. windowClass.on('freeWindowModeChange', (data) => {
3. console.info('Succeeded in enabling the listener for free window mode changes. Data: ' + JSON.stringify(data));
4. });
5. } catch (exception) {
6. console.error(`Failed to enable the listener for free window mode changes. Cause code: ${exception.code}, message: ${exception.message}`);
7. }
```

## off('freeWindowModeChange')22+

PhonePC/2in1TabletTVWearable

off(type: 'freeWindowModeChange', callback?: Callback<boolean>): void

关闭自由窗口模式变化事件的监听。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'freeWindowModeChange'，即自由窗口模式变化事件。 |
| callback | Callback<boolean> | 否 | 回调函数。返回当前窗口是否在自由窗口模式。如果传入参数，则关闭该监听。如果未传入参数，则关闭自由窗口模式变化事件的监听。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. const callback = (isInFreeWindowMode: boolean) => {
2. // ...
3. }
4. try {
5. // 通过on接口开启监听
6. windowClass.on('freeWindowModeChange', callback);
7. // 关闭指定callback的监听
8. windowClass.off('freeWindowModeChange', callback);
9. // 如果通过on开启多个callback进行监听，同时关闭所有监听
10. windowClass.off('freeWindowModeChange');
11. } catch (exception) {
12. console.error(`Failed to disable the listener for free window mode change. Cause code: ${exception.code}, message: ${exception.message}`);
13. }
```

## convertOrientationAndRotation23+

PhonePC/2in1TabletTVWearable

convertOrientationAndRotation(from: RotationInfoType, to: RotationInfoType, value: number): number

提供窗口方向、屏幕方向和屏幕角度互相转换的能力。

窗口方向指窗口所在屏幕的方向，以窗口模块对横竖屏的定义方式表示，窗口的方向分别用0、1、2和3表示竖屏、反向横屏、反向竖屏和横屏四个方向，其对横竖屏的定义与[RotationChangeInfo](arkts-apis-window-i.md#rotationchangeinfo19)和枚举类[Orientation](arkts-apis-window-e.md#orientation9)中对横竖屏的定义一致，如Orientation设置为LANDSCAPE时，窗口方向为横屏。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在Phone和Tablet设备可正常调用，在其他设备中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| from | [RotationInfoType](arkts-apis-window-e.md#rotationinfotype23) | 是 | 待转换的值的类型。 |
| to | [RotationInfoType](arkts-apis-window-e.md#rotationinfotype23) | 是 | 目标值的类型。 |
| value | number | 是 | 待转换的值。该参数为整数，浮点数输入将向下取整，取值范围为[0, 3]，范围外为非法参数（抛出错误码[401](errorcode-universal.md#section401-参数检查失败)）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回目标类型的转换值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. try {
2. let originalValue: number = 0;
3. let fromType: window.RotationInfoType = window.RotationInfoType.WINDOW_ORIENTATION;
4. let toType: window.RotationInfoType = window.RotationInfoType.DISPLAY_ORIENTATION;
5. let convertedValue: number = windowClass.convertOrientationAndRotation(fromType, toType, originalValue);
6. console.info(`Convert ${originalValue} of type: ${fromType} to ${convertedValue} of type: ${toType}`);
7. } catch (exception) {
8. console.error(`Failed to convert orientation and rotation between window and display. Cause code: ${exception.code}, message: ${exception.message}`);
9. }
```

## setWindowSystemBarProperties(deprecated)

PhonePC/2in1TabletTVWearable

setWindowSystemBarProperties(systemBarProperties: SystemBarProperties, callback: AsyncCallback<void>): void

设置主窗口状态栏的属性，使用callback异步回调，该接口在2in1设备上调用不生效，其他设备在分屏模式（即窗口模式为window.WindowStatusType.SPLIT\_SCREEN）、自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING）、自由多窗模式（可点击设备控制中心中的自由多窗按钮开启）下调用不会立刻生效，只有进入全屏主窗口才会生效。

子窗口调用后不生效。

说明

从API version 9开始支持，从API version 12开始废弃，建议使用Promise方式的[setWindowSystemBarProperties()](arkts-apis-window-window.md#setwindowsystembarproperties9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| systemBarProperties | [SystemBarProperties](arkts-apis-window-i.md#systembarproperties) | 是 | 状态栏的属性。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. // ...
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. console.info('onWindowStageCreate');
10. let windowClass: window.Window | undefined = undefined;
11. windowStage.getMainWindow((err: BusinessError, data) => {
12. const errCode: number = err.code;
13. if (errCode) {
14. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
15. return;
16. }
17. windowClass = data;
18. let SystemBarProperties: window.SystemBarProperties = {
19. statusBarColor: '#ff00ff',
20. navigationBarColor: '#00ff00',
21. // 以下两个属性从API Version8开始支持
22. statusBarContentColor: '#ffffff',
23. navigationBarContentColor: '#00ffff'
24. };
25. try {
26. windowClass.setWindowSystemBarProperties(SystemBarProperties, (err: BusinessError) => {
27. const errCode: number = err.code;
28. if (errCode) {
29. console.error(`Failed to set the system bar properties. Cause code: ${err.code}, message: ${err.message}`);
30. return;
31. }
32. console.info('Succeeded in setting the system bar properties.');
33. });
34. } catch (exception) {
35. console.error(`Failed to set the system bar properties. Cause code: ${exception.code}, message: ${exception.message}`);
36. }
37. });
38. }
39. }
```

## setWindowSystemBarEnable(deprecated)

PhonePC/2in1TabletTVWearable

setWindowSystemBarEnable(names: Array<'status' | 'navigation'>, callback: AsyncCallback<void>): void

设置主窗口状态栏、底部导航（根据用户设置，可表现为导航条或三键导航栏）的可见模式，状态栏和底部导航通过status控制、navigation参数无效果，使用callback异步回调。

从API version 12开始，该接口在2in1设备上调用不生效，其他设备在分屏模式（即窗口模式为window.WindowStatusType.SPLIT\_SCREEN）、自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING）、自由多窗模式（可点击设备控制中心中的自由多窗按钮开启）下调用不会立刻生效，只有进入全屏主窗口才会生效。

调用生效后返回并不表示状态栏和底部导航区域的显示或隐藏已完成。子窗口调用后不生效。非全屏模式（悬浮窗、分屏等场景）下配置不生效。

说明

从API version 9开始支持，从API version 12开始废弃，建议使用Promise方式的[setWindowSystemBarEnable()](arkts-apis-window-window.md#setwindowsystembarenable9)替代。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| names | Array<'status'|'navigation'> | 是 | 设置窗口全屏模式时状态栏和底部导航区域是否显示。  例如，需全部显示，该参数设置为['status', 'navigation']；设置为[]，则不显示。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. // 此处以状态栏等均不显示为例
2. // EntryAbility.ets
3. import { UIAbility } from '@kit.AbilityKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { window } from '@kit.ArkUI';

7. export default class EntryAbility extends UIAbility {
8. // ...
9. onWindowStageCreate(windowStage: window.WindowStage): void {
10. console.info('onWindowStageCreate');
11. let windowClass: window.Window | undefined = undefined;
12. windowStage.getMainWindow((err: BusinessError, data) => {
13. const errCode: number = err.code;
14. if (errCode) {
15. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
16. return;
17. }
18. windowClass = data;
19. let names: Array<'status' | 'navigation'> = [];
20. try {
21. windowClass.setWindowSystemBarEnable(names, (err: BusinessError) => {
22. const errCode: number = err.code;
23. if (errCode) {
24. console.error(`Failed to set the system bar to be invisible. Cause code: ${err.code}, message: ${err.message}`);
25. return;
26. }
27. console.info('Succeeded in setting the system bar to be invisible.');
28. });
29. } catch (exception) {
30. console.error(`Failed to set the system bar to be invisible. Cause code: ${exception.code}, message: ${exception.message}`);
31. }
32. });
33. }
34. }
```

## setWindowLayoutFullScreen(deprecated)

PhonePC/2in1TabletTVWearable

setWindowLayoutFullScreen(isLayoutFullScreen: boolean, callback: AsyncCallback<void>): void

设置主窗口或子窗口的布局是否为沉浸式布局，使用callback异步回调。系统窗口调用不生效。

沉浸式布局生效时，布局不避让状态栏与底部导航区域，组件可能产生与其重叠的情况。

非沉浸式布局生效时，布局避让状态栏与底部导航区域，组件不会与其重叠。

说明

从API version 9开始支持，从API version 12开始废弃，建议使用Promise方式的[setWindowLayoutFullScreen()](arkts-apis-window-window.md#setwindowlayoutfullscreen9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**设备行为差异：**

在HarmonyOS 5.0.2之前，该接口在所有设备中可正常调用。

从HarmonyOS 5.0.2开始，该接口在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上调用不生效也不报错；在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备及不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isLayoutFullScreen | boolean | 是 | 窗口的布局是否为沉浸式布局（该沉浸式布局状态栏、底部导航区域仍然显示）。true表示沉浸式布局；false表示非沉浸式布局。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[窗口错误码](errorcode-window.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. // ...
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. console.info('onWindowStageCreate');
10. let windowClass: window.Window | undefined = undefined;
11. windowStage.getMainWindow((err: BusinessError, data) => {
12. const errCode: number = err.code;
13. if (errCode) {
14. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
15. return;
16. }
17. windowClass = data;
18. let isLayoutFullScreen = true;
19. try {
20. windowClass.setWindowLayoutFullScreen(isLayoutFullScreen, (err: BusinessError) => {
21. const errCode: number = err.code;
22. if (errCode) {
23. console.error(`Failed to set the window layout to full-screen mode. Cause code: ${err.code}, message: ${err.message}`);
24. return;
25. }
26. console.info('Succeeded in setting the window layout to full-screen mode.');
27. });
28. } catch (exception) {
29. console.error(`Failed to set the window layout to full-screen mode. Cause code: ${exception.code}, message: ${exception.message}`);
30. }
31. });
32. }
33. }
```

## show(deprecated)

PhonePC/2in1TabletTVWearable

show(callback: AsyncCallback<void>): void

显示当前窗口，使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[showWindow()](arkts-apis-window-window.md#showwindow9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. windowClass.show((err: BusinessError) => {
4. const errCode: number = err.code;
5. if (errCode) {
6. console.error(`Failed to show the window. Cause code: ${err.code}, message: ${err.message}`);
7. return;
8. }
9. console.info('Succeeded in showing the window.');
10. });
```

## show(deprecated)

PhonePC/2in1TabletTVWearable

show(): Promise<void>

显示当前窗口，使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[showWindow()](arkts-apis-window-window.md#showwindow9-1)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let promise = windowClass.show();
4. promise.then(() => {
5. console.info('Succeeded in showing the window.');
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to show the window. Cause code: ${err.code}, message: ${err.message}`);
8. });
```

## destroy(deprecated)

PhonePC/2in1TabletTVWearable

destroy(callback: AsyncCallback<void>): void

销毁当前窗口，使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[destroyWindow()](arkts-apis-window-window.md#destroywindow9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. windowClass.destroy((err: BusinessError) => {
4. const errCode: number = err.code;
5. if (err.code) {
6. console.error(`Failed to destroy the window. Cause code: ${err.code}, message: ${err.message}`);
7. return;
8. }
9. console.info('Succeeded in destroying the window.');
10. });
```

## destroy(deprecated)

PhonePC/2in1TabletTVWearable

destroy(): Promise<void>

销毁当前窗口，使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[destroyWindow()](arkts-apis-window-window.md#destroywindow9-1)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let promise = windowClass.destroy();
4. promise.then(() => {
5. console.info('Succeeded in destroying the window.');
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to destroy the window. Cause code: ${err.code}, message: ${err.message}`);
8. });
```

## moveTo(deprecated)

PhonePC/2in1TabletTVWearable

moveTo(x: number, y: number, callback: AsyncCallback<void>): void

移动窗口位置，使用callback异步回调。

全屏模式窗口不支持该操作。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[moveWindowTo()](arkts-apis-window-window.md#movewindowto9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 窗口在x轴方向移动到的坐标位置，单位为px，值为正表示位置在x轴右侧；值为负表示位置在x轴左侧；值为0表示位置在x轴坐标原点。该参数仅支持整数输入，浮点数输入将向下取整。 |
| y | number | 是 | 窗口在y轴方向移动到的坐标位置，单位为px，值为正表示位置在y轴下侧；值为负表示位置在y轴上侧；值为0表示位置在x轴坐标原点。该参数仅支持整数输入，浮点数输入将向下取整。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. windowClass.moveTo(300, 300, (err: BusinessError) => {
4. const errCode: number = err.code;
5. if (errCode) {
6. console.error(`Failed to move the window. Cause code: ${err.code}, message: ${err.message}`);
7. return;
8. }
9. console.info('Succeeded in moving the window.');
10. });
```

## moveTo(deprecated)

PhonePC/2in1TabletTVWearable

moveTo(x: number, y: number): Promise<void>

移动窗口位置，使用Promise异步回调。

全屏模式窗口不支持该操作。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[moveWindowTo()](arkts-apis-window-window.md#movewindowto9-1)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 窗口在x轴方向移动到的坐标位置，单位为px，值为正表示位置在x轴右侧；值为负表示位置在x轴左侧；值为0表示位置在x轴坐标原点。该参数仅支持整数输入，浮点数输入将向下取整。 |
| y | number | 是 | 窗口在y轴方向移动到的坐标位置，单位为px，值为正表示位置在y轴下侧；值为负表示位置在y轴上侧；值为0表示位置在y轴坐标原点。该参数仅支持整数输入，浮点数输入将向下取整。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let promise = windowClass.moveTo(300, 300);
4. promise.then(() => {
5. console.info('Succeeded in moving the window.');
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to move the window. Cause code: ${err.code}, message: ${err.message}`);
8. });
```

## resetSize(deprecated)

PhonePC/2in1TabletTVWearable

resetSize(width: number, height: number, callback: AsyncCallback<void>): void

基于窗口左上角顶点改变当前窗口大小，使用callback异步回调。

应用主窗口与子窗口存在大小限制，默认宽度范围：[320, 1920]，默认高度范围：[240, 1920]，单位为vp。

应用主窗口与子窗口的最小宽度与最小高度可由产品端进行配置，配置后的最小宽度与最小高度以产品段配置值为准，具体尺寸限制范围可以通过[getWindowLimits](arkts-apis-window-window.md#getwindowlimits11)接口进行查询。

系统窗口存在大小限制，宽度范围：(0, 1920]，高度范围：(0, 1920]，单位为vp。

设置的宽度与高度受到此限制约束，规则：

若所设置的窗口宽/高尺寸小于窗口最小宽/高限制值，则窗口最小宽/高限制值生效；

若所设置的窗口宽/高尺寸大于窗口最大宽/高限制值，则窗口最大宽/高限制值生效。

全屏模式窗口不支持该操作。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[resize()](arkts-apis-window-window.md#resize9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 当前窗口的目标宽度，单位为px，该参数仅支持整数输入，浮点数输入将向下取整，负值为非法参数（抛出错误码[401](errorcode-universal.md#section401-参数检查失败)）。 |
| height | number | 是 | 当前窗口的目标高度，单位为px，该参数仅支持整数输入，浮点数输入将向下取整，负值为非法参数（抛出错误码[401](errorcode-universal.md#section401-参数检查失败)）。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. windowClass.resetSize(500, 1000, (err: BusinessError) => {
4. const errCode: number = err.code;
5. if (errCode) {
6. console.error(`Failed to change the window size. Cause code: ${err.code}, message: ${err.message}`);
7. return;
8. }
9. console.info('Succeeded in changing the window size.');
10. });
```

## resetSize(deprecated)

PhonePC/2in1TabletTVWearable

resetSize(width: number, height: number): Promise<void>

基于窗口左上角顶点改变当前窗口大小，使用Promise异步回调。

应用主窗口与子窗口存在大小限制，默认宽度范围：[320, 1920]，默认高度范围：[240, 1920]，单位为vp。

应用主窗口与子窗口的最小宽度与最小高度可由产品端进行配置，配置后的最小宽度与最小高度以产品段配置值为准，具体尺寸限制范围可以通过[getWindowLimits](arkts-apis-window-window.md#getwindowlimits11)接口进行查询。

系统窗口存在大小限制，宽度范围：(0, 1920]，高度范围：(0, 1920]，单位为vp。

设置的宽度与高度受到此限制约束，规则：

若所设置的窗口宽/高尺寸小于窗口最小宽/高限制值，则窗口最小宽/高限制值生效；

若所设置的窗口宽/高尺寸大于窗口最大宽/高限制值，则窗口最大宽/高限制值生效。

全屏模式窗口不支持该操作。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[resize()](arkts-apis-window-window.md#resize9-1)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 当前窗口的目标宽度，单位为px，该参数仅支持整数输入，浮点数输入将向下取整，负值为非法参数（抛出错误码[401](errorcode-universal.md#section401-参数检查失败)）。 |
| height | number | 是 | 当前窗口的目标高度，单位为px，该参数仅支持整数输入，浮点数输入将向下取整，负值为非法参数（抛出错误码[401](errorcode-universal.md#section401-参数检查失败)）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let promise = windowClass.resetSize(500, 1000);
4. promise.then(() => {
5. console.info('Succeeded in changing the window size.');
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to change the window size. Cause code: ${err.code}, message: ${err.message}`);
8. });
```

## getProperties(deprecated)

PhonePC/2in1TabletTVWearable

getProperties(callback: AsyncCallback<WindowProperties>): void

获取当前窗口的属性，使用callback异步回调，返回WindowProperties。

说明

从API version 6开始支持，从API version 9开始废弃，建议使用[getWindowProperties()](arkts-apis-window-window.md#getwindowproperties9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[WindowProperties](arkts-apis-window-i.md#windowproperties)> | 是 | 回调函数。返回当前窗口属性。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. windowClass.getProperties((err: BusinessError, data) => {
4. const errCode: number = err.code;
5. if (errCode) {
6. console.error(`Failed to obtain the window properties. Cause code: ${err.code}, message: ${err.message}`);
7. return;
8. }
9. console.info('Succeeded in obtaining the window properties. Data: ' + JSON.stringify(data));
10. });
```

## getProperties(deprecated)

PhonePC/2in1TabletTVWearable

getProperties(): Promise<WindowProperties>

获取当前窗口的属性，使用Promise异步回调，返回WindowProperties。

说明

从API version 6开始支持，从API version 9开始废弃，建议使用[getWindowProperties()](arkts-apis-window-window.md#getwindowproperties9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[WindowProperties](arkts-apis-window-i.md#windowproperties)> | Promise对象。返回当前窗口属性。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let promise = windowClass.getProperties();
4. promise.then((data) => {
5. console.info('Succeeded in obtaining the window properties. Data: ' + JSON.stringify(data));
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to obtain the window properties. Cause code: ${err.code}, message: ${err.message}`);
8. });
```

## getAvoidArea(deprecated)

PhonePC/2in1TabletTVWearable

getAvoidArea(type: [AvoidAreaType](arkts-apis-window-e.md#avoidareatype7), callback: AsyncCallback<[AvoidArea](arkts-apis-window-i.md#avoidarea7)>): void

获取当前窗口内容规避的区域；如系统栏区域、刘海屏区域、手势区域、软键盘区域等与窗口内容重叠时，需要窗口内容避让的区域。

主窗口/子窗口：

* [自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING）下，仅存在固定态软键盘（[AvoidAreaType](arkts-apis-window-e.md#avoidareatype7)为TYPE\_KEYBOARD）类型的避让区域。
* 主窗口在非自由窗口状态的自由悬浮窗口模式下，仅存在系统栏（[AvoidAreaType](arkts-apis-window-e.md#avoidareatype7)为TYPE\_SYSTEM）类型的避让区域。
* 主窗口在其余场景下，仅当在非自由悬浮窗口模式下或设备类型为Phone和Tablet，才能通过此接口获取计算后的避让区域，否则获取的避让区域为空。
* 子窗口在非自由窗口状态或非自由悬浮窗口模式下，仅当窗口的位置和大小与主窗口一致时，才能通过此接口获取计算后的避让区域，否则获取的避让区域为空。

全局悬浮窗、模态窗或系统窗口：

* 仅在调用[setSystemAvoidAreaEnabled](arkts-apis-window-window.md#setsystemavoidareaenabled18)方法使能后，才能通过此接口获取计算后的避让区域，否则获取的避让区域为空。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[getWindowAvoidArea()](arkts-apis-window-window.md#getwindowavoidarea9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [AvoidAreaType](arkts-apis-window-e.md#avoidareatype7) | 是 | 表示避让区类型。 |
| callback | AsyncCallback<[AvoidArea](arkts-apis-window-i.md#avoidarea7)> | 是 | 回调函数。返回窗口内容避让区域。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let type = window.AvoidAreaType.TYPE_SYSTEM;
4. windowClass.getAvoidArea(type, (err: BusinessError, data) => {
5. const errCode: number = err.code;
6. if (errCode) {
7. console.error(`Failed to obtain the area. Cause code: ${err.code}, message: ${err.message}`);
8. return;
9. }
10. console.info('Succeeded in obtaining the area. Data:' + JSON.stringify(data));
11. });
```

## getAvoidArea(deprecated)

PhonePC/2in1TabletTVWearable

getAvoidArea(type: [AvoidAreaType](arkts-apis-window-e.md#avoidareatype7)): Promise<[AvoidArea](arkts-apis-window-i.md#avoidarea7)>

获取当前窗口内容规避的区域；如系统栏区域、刘海屏区域、手势区域、软键盘区域等与窗口内容重叠时，需要窗口内容避让的区域。

主窗口/子窗口：

* [自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING）下，仅存在固定态软键盘（[AvoidAreaType](arkts-apis-window-e.md#avoidareatype7)为TYPE\_KEYBOARD）类型的避让区域。
* 主窗口在非自由窗口状态的自由悬浮窗口模式下，仅存在系统栏（[AvoidAreaType](arkts-apis-window-e.md#avoidareatype7)为TYPE\_SYSTEM）类型的避让区域。
* 主窗口在其余场景下，仅当在非自由悬浮窗口模式下或设备类型为Phone和Tablet，才能通过此接口获取计算后的避让区域，否则获取的避让区域为空。
* 子窗口在非自由窗口状态或非自由悬浮窗口模式下，仅当窗口的位置和大小与主窗口一致时，才能通过此接口获取计算后的避让区域，否则获取的避让区域为空。

全局悬浮窗、模态窗或系统窗口：

* 仅在调用[setSystemAvoidAreaEnabled](arkts-apis-window-window.md#setsystemavoidareaenabled18)方法使能后，才能通过此接口获取计算后的避让区域，否则获取的避让区域为空。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[getWindowAvoidArea()](arkts-apis-window-window.md#getwindowavoidarea9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [AvoidAreaType](arkts-apis-window-e.md#avoidareatype7) | 是 | 表示避让区类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AvoidArea](arkts-apis-window-i.md#avoidarea7)> | Promise对象。返回窗口内容避让区域。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let type = window.AvoidAreaType.TYPE_SYSTEM;
4. let promise = windowClass.getAvoidArea(type);
5. promise.then((data) => {
6. console.info('Succeeded in obtaining the area. Data:' + JSON.stringify(data));
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to obtain the area. Cause code: ${err.code}, message: ${err.message}`);
9. });
```

## setFullScreen(deprecated)

PhonePC/2in1TabletTVWearable

setFullScreen(isFullScreen: boolean, callback: AsyncCallback<void>): void

设置主窗口或子窗口的布局是否为全屏布局，使用callback异步回调。

全屏布局生效时，布局不避让状态栏与底部导航区域，组件可能产生与其重叠的情况。

非全屏布局生效时，布局避让状态栏与底部导航区域，组件不会与其重叠。

说明

从API version 6开始支持，从API version 9开始废弃，建议联合使用[setWindowSystemBarEnable()](arkts-apis-window-window.md#setwindowsystembarenable9)和[setWindowLayoutFullScreen()](arkts-apis-window-window.md#setwindowlayoutfullscreen9)替代实现全屏。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isFullScreen | boolean | 是 | 是否设为全屏布局（该全屏布局影响状态栏、底部导航区域显示）。true表示全屏；false表示非全屏。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. // ...
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. console.info('onWindowStageCreate');
10. let windowClass: window.Window | undefined = undefined;
11. windowStage.getMainWindow((err: BusinessError, data) => {
12. const errCode: number = err.code;
13. if (errCode) {
14. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
15. return;
16. }
17. windowClass = data;
18. let isFullScreen: boolean = true;
19. windowClass.setFullScreen(isFullScreen, (err: BusinessError) => {
20. const errCode: number = err.code;
21. if (errCode) {
22. console.error(`Failed to enable the full-screen mode. Cause code: ${err.code}, message: ${err.message}`);
23. return;
24. }
25. console.info('Succeeded in enabling the full-screen mode.');
26. });
27. });
28. }
29. }
```

## setFullScreen(deprecated)

PhonePC/2in1TabletTVWearable

setFullScreen(isFullScreen: boolean): Promise<void>

设置主窗口或子窗口的布局是否为全屏布局，使用Promise异步回调。

全屏布局生效时，布局不避让状态栏与底部导航区域，组件可能产生与其重叠的情况。

非全屏布局生效时，布局避让状态栏与底部导航区域，组件不会与其重叠。

说明

从API version 6开始支持，从API version 9开始废弃，建议联合使用[setWindowSystemBarEnable()](arkts-apis-window-window.md#setwindowsystembarenable9)和[setWindowLayoutFullScreen()](arkts-apis-window-window.md#setwindowlayoutfullscreen9)替代实现全屏。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isFullScreen | boolean | 是 | 是否设为全屏布局（该全屏布局影响状态栏、底部导航区域显示）。true表示全屏；false表示非全屏。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. // ...
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. console.info('onWindowStageCreate');
10. let windowClass: window.Window | undefined = undefined;
11. windowStage.getMainWindow((err: BusinessError, data) => {
12. const errCode: number = err.code;
13. if (errCode) {
14. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
15. return;
16. }
17. windowClass = data;
18. let isFullScreen: boolean = true;
19. let promise = windowClass.setFullScreen(isFullScreen);
20. promise.then(() => {
21. console.info('Succeeded in enabling the full-screen mode.');
22. }).catch((err: BusinessError) => {
23. console.error(`Failed to enable the full-screen mode. Cause code: ${err.code}, message: ${err.message}`);
24. });
25. });
26. }
27. }
```

## setLayoutFullScreen(deprecated)

PhonePC/2in1TabletTVWearable

setLayoutFullScreen(isLayoutFullScreen: boolean, callback: AsyncCallback<void>): void

设置主窗口或子窗口的布局是否为沉浸式布局，使用callback异步回调。

沉浸式布局生效时，布局不避让状态栏与底部导航区域，组件可能产生与其重叠的情况。

非沉浸式布局生效时，布局避让状态栏与底部导航区域，组件不会与其重叠。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[setWindowLayoutFullScreen()](arkts-apis-window-window.md#setwindowlayoutfullscreen9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isLayoutFullScreen | boolean | 是 | 窗口的布局是否为沉浸式布局（该沉浸式布局不影响状态栏、底部导航区域显示）。true表示沉浸式布局；false表示非沉浸式布局。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. // ...
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. console.info('onWindowStageCreate');
10. let windowClass: window.Window | undefined = undefined;
11. windowStage.getMainWindow((err: BusinessError, data) => {
12. const errCode: number = err.code;
13. if (errCode) {
14. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
15. return;
16. }
17. windowClass = data;
18. let isLayoutFullScreen: boolean = true;
19. windowClass.setLayoutFullScreen(isLayoutFullScreen, (err: BusinessError) => {
20. const errCode: number = err.code;
21. if (errCode) {
22. console.error(`Failed to set the window layout to full-screen mode. Cause code: ${err.code}, message: ${err.message}`);
23. return;
24. }
25. console.info('Succeeded in setting the window layout to full-screen mode.');
26. });
27. });
28. }
29. }
```

## setLayoutFullScreen(deprecated)

PhonePC/2in1TabletTVWearable

setLayoutFullScreen(isLayoutFullScreen: boolean): Promise<void>

设置主窗口或子窗口的布局是否为沉浸式布局，使用Promise异步回调。

沉浸式布局生效时，布局不避让状态栏与底部导航区域，组件可能产生与其重叠的情况。

非沉浸式布局生效时，布局避让状态栏与底部导航区域，组件不会与其重叠。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[setWindowLayoutFullScreen()](arkts-apis-window-window.md#setwindowlayoutfullscreen9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isLayoutFullScreen | boolean | 是 | 窗口的布局是否为沉浸式布局（该沉浸式布局不影响状态栏、底部导航区域显示）。true表示沉浸式布局；false表示非沉浸式布局。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. // ...
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. console.info('onWindowStageCreate');
10. let windowClass: window.Window | undefined = undefined;
11. windowStage.getMainWindow((err: BusinessError, data) => {
12. const errCode: number = err.code;
13. if (errCode) {
14. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
15. return;
16. }
17. windowClass = data;
18. let isLayoutFullScreen: boolean = true;
19. let promise = windowClass.setLayoutFullScreen(isLayoutFullScreen);
20. promise.then(() => {
21. console.info('Succeeded in setting the window layout to full-screen mode.');
22. }).catch((err: BusinessError) => {
23. console.error(`Failed to set the window layout to full-screen mode. Cause code: ${err.code}, message: ${err.message}`);
24. });
25. });
26. }
27. }
```

## setSystemBarEnable(deprecated)

PhonePC/2in1TabletTVWearable

setSystemBarEnable(names: Array<'status' | 'navigation'>, callback: AsyncCallback<void>): void

设置主窗口状态栏、底部导航（根据用户设置，可表现为导航条或三键导航栏）的可见模式，状态栏和底部导航通过status控制、navigation参数无效果，使用callback异步回调。

从API version 12开始，该接口在2in1设备上调用不生效，其他设备在分屏模式（即窗口模式为window.WindowStatusType.SPLIT\_SCREEN）、自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING）、自由多窗模式（可点击设备控制中心中的自由多窗按钮开启）下调用不会立刻生效，只有进入全屏主窗口才会生效。

调用生效后返回并不表示状态栏和底部导航区域的显示或隐藏已完成。子窗口调用后不生效。非全屏模式（悬浮窗、分屏等场景）下配置不生效。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[setWindowSystemBarEnable()](arkts-apis-window-window.md#setwindowsystembarenable9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| names | Array<'status'|'navigation'> | 是 | 设置窗口全屏模式时状态栏和底部导航区域是否显示。  例如，需全部显示，该参数设置为['status', 'navigation']；设置为[]，则不显示。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. // 此处以状态栏等均不显示为例
2. // EntryAbility.ets
3. import { UIAbility } from '@kit.AbilityKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { window } from '@kit.ArkUI';

7. export default class EntryAbility extends UIAbility {
8. // ...
9. onWindowStageCreate(windowStage: window.WindowStage): void {
10. console.info('onWindowStageCreate');
11. let windowClass: window.Window | undefined = undefined;
12. windowStage.getMainWindow((err: BusinessError, data) => {
13. const errCode: number = err.code;
14. if (errCode) {
15. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
16. return;
17. }
18. windowClass = data;
19. let names: Array<'status' | 'navigation'> = [];
20. windowClass.setSystemBarEnable(names, (err: BusinessError) => {
21. const errCode: number = err.code;
22. if (errCode) {
23. console.error(`Failed to set the system bar to be invisible. Cause code: ${err.code}, message: ${err.message}`);
24. return;
25. }
26. console.info('Succeeded in setting the system bar to be invisible.');
27. });
28. });
29. }
30. }
```

## setSystemBarEnable(deprecated)

PhonePC/2in1TabletTVWearable

setSystemBarEnable(names: Array<'status' | 'navigation'>): Promise<void>

设置主窗口状态栏、底部导航（根据用户设置，可表现为导航条或三键导航栏）的可见模式，状态栏和底部导航通过status控制、navigation参数无效果，使用Promise异步回调。

从API version 12开始，该接口在2in1设备上调用不生效，其他设备在分屏模式（即窗口模式为window.WindowStatusType.SPLIT\_SCREEN）、自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING）、自由多窗模式（可点击设备控制中心中的自由多窗按钮开启）下调用不会立刻生效，只有进入全屏主窗口才会生效。

调用生效后返回并不表示状态栏和底部导航区域的显示或隐藏已完成。子窗口调用后不生效。非全屏模式（悬浮窗、分屏等场景）下配置不生效。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[setWindowSystemBarEnable()](arkts-apis-window-window.md#setwindowsystembarenable9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| names | Array<'status'|'navigation'> | 是 | 设置窗口全屏模式时状态栏和底部导航区域是否显示。  例如，需全部显示，该参数设置为['status', 'navigation']；设置为[]，则不显示。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. // 此处以状态栏等均不显示为例
2. // EntryAbility.ets
3. import { UIAbility } from '@kit.AbilityKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { window } from '@kit.ArkUI';

7. export default class EntryAbility extends UIAbility {
8. // ...
9. onWindowStageCreate(windowStage: window.WindowStage): void {
10. console.info('onWindowStageCreate');
11. let windowClass: window.Window | undefined = undefined;
12. windowStage.getMainWindow((err: BusinessError, data) => {
13. const errCode: number = err.code;
14. if (errCode) {
15. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
16. return;
17. }
18. windowClass = data;
19. let names: Array<'status' | 'navigation'> = [];
20. let promise = windowClass.setSystemBarEnable(names);
21. promise.then(() => {
22. console.info('Succeeded in setting the system bar to be invisible.');
23. }).catch((err: BusinessError) => {
24. console.error(`Failed to set the system bar to be invisible. Cause code: ${err.code}, message: ${err.message}`);
25. });
26. });
27. }
28. }
```

## setSystemBarProperties(deprecated)

PhonePC/2in1TabletTVWearable

setSystemBarProperties(systemBarProperties: SystemBarProperties, callback: AsyncCallback<void>): void

设置主窗口状态栏的属性，使用callback异步回调，该接口在2in1设备上调用不生效，其他设备在分屏模式（即窗口模式为window.WindowStatusType.SPLIT\_SCREEN）、自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING）、自由多窗模式（可点击设备控制中心中的自由多窗按钮开启）下调用不会立刻生效，只有进入全屏主窗口才会生效。

子窗口调用后不生效。非全屏模式（悬浮窗、分屏等场景）下配置不生效。

说明

从API version 6开始支持，从API version 9开始废弃，建议使用[setWindowSystemBarProperties()](arkts-apis-window-window.md#setwindowsystembarproperties9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| systemBarProperties | [SystemBarProperties](arkts-apis-window-i.md#systembarproperties) | 是 | 状态栏的属性。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. // ...
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. console.info('onWindowStageCreate');
10. let windowClass: window.Window | undefined = undefined;
11. windowStage.getMainWindow((err: BusinessError, data) => {
12. const errCode: number = err.code;
13. if (errCode) {
14. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
15. return;
16. }
17. windowClass = data;
18. let SystemBarProperties: window.SystemBarProperties = {
19. statusBarColor: '#ff00ff',
20. navigationBarColor: '#00ff00',
21. // 以下两个属性从API Version8开始支持
22. statusBarContentColor: '#ffffff',
23. navigationBarContentColor: '#00ffff'
24. };
25. windowClass.setSystemBarProperties(SystemBarProperties, (err) => {
26. const errCode: number = err.code;
27. if (errCode) {
28. console.error(`Failed to set the system bar properties. Cause code: ${err.code}, message: ${err.message}`);
29. return;
30. }
31. console.info('Succeeded in setting the system bar properties.');
32. });
33. });
34. }
35. }
```

## setSystemBarProperties(deprecated)

PhonePC/2in1TabletTVWearable

setSystemBarProperties(systemBarProperties: SystemBarProperties): Promise<void>

设置主窗口状态栏的属性，使用Promise异步回调，该接口在2in1设备上调用不生效，其他设备在分屏模式（即窗口模式为window.WindowStatusType.SPLIT\_SCREEN）、自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING）、自由多窗模式（可点击设备控制中心中的自由多窗按钮开启）下调用不会立刻生效，只有进入全屏主窗口才会生效。

子窗口调用后不生效。

说明

从API version 6开始支持，从API version 9开始废弃，建议使用[setWindowSystemBarProperties()](arkts-apis-window-window.md#setwindowsystembarproperties9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| systemBarProperties | [SystemBarProperties](arkts-apis-window-i.md#systembarproperties) | 是 | 状态栏的属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. // ...
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. console.info('onWindowStageCreate');
10. let windowClass: window.Window | undefined = undefined;
11. windowStage.getMainWindow((err: BusinessError, data) => {
12. const errCode: number = err.code;
13. if (errCode) {
14. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
15. return;
16. }
17. windowClass = data;
18. let SystemBarProperties: window.SystemBarProperties = {
19. statusBarColor: '#ff00ff',
20. navigationBarColor: '#00ff00',
21. // 以下两个属性从API Version8开始支持
22. statusBarContentColor: '#ffffff',
23. navigationBarContentColor: '#00ffff'
24. };
25. let promise = windowClass.setSystemBarProperties(SystemBarProperties);
26. promise.then(() => {
27. console.info('Succeeded in setting the system bar properties.');
28. }).catch((err: BusinessError) => {
29. console.error(`Failed to set the system bar properties. Cause code: ${err.code}, message: ${err.message}`);
30. });
31. });
32. }
33. }
```

## loadContent(deprecated)

PhonePC/2in1TabletTVWearable

loadContent(path: string, callback: AsyncCallback<void>): void

为当前窗口加载具体页面内容，使用callback异步回调。

建议在UIAbility启动过程中使用该接口，多次调用该接口会先销毁旧的页面内容（即UIContent）再加载新的页面内容，请谨慎使用。

当前UI的执行上下文可能不明确，所以不建议在本接口的回调函数中做UI相关的操作。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[setUIContent()](arkts-apis-window-window.md#setuicontent9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 要加载到窗口中的页面内容的路径，Stage模型下该路径需添加到工程的main\_pages.json文件中，FA模型下该路径需添加到工程的config.json文件中。不支持相对路径写法，需与main\_pages.json或config.json中的src取值保持一致。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. windowClass.loadContent('pages/page2/page3', (err: BusinessError) => {
4. const errCode: number = err.code;
5. if (errCode) {
6. console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
7. return;
8. }
9. console.info('Succeeded in loading the content.');
10. });
```

## loadContent(deprecated)

PhonePC/2in1TabletTVWearable

loadContent(path: string): Promise<void>

为当前窗口加载具体页面内容，使用Promise异步回调。

建议在UIAbility启动过程中使用该接口，多次调用该接口会先销毁旧的页面内容（即UIContent）再加载新的页面内容，请谨慎使用。

当前UI的执行上下文可能不明确，所以不建议在本接口的回调函数中做UI相关的操作。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[setUIContent()](arkts-apis-window-window.md#setuicontent9-1)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 要加载到窗口中的页面内容的路径，Stage模型下该路径需添加到工程的main\_pages.json文件中，FA模型下该路径需添加到工程的config.json文件中。不支持相对路径写法，需与main\_pages.json或config.json中的src取值保持一致。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let promise = windowClass.loadContent('pages/page2/page3');
4. promise.then(() => {
5. console.info('Succeeded in loading the content.');
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
8. });
```

## isShowing(deprecated)

PhonePC/2in1TabletTVWearable

isShowing(callback: AsyncCallback<boolean>): void

判断当前窗口是否已显示，使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[isWindowShowing()](arkts-apis-window-window.md#iswindowshowing9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示当前窗口已显示，返回false表示当前窗口未显示。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. windowClass.isShowing((err: BusinessError, data) => {
4. const errCode: number = err.code;
5. if (errCode) {
6. console.error(`Failed to check whether the window is showing. Cause code: ${err.code}, message: ${err.message}`);
7. return;
8. }
9. console.info('Succeeded in checking whether the window is showing. Data: ' + JSON.stringify(data));
10. });
```

## isShowing(deprecated)

PhonePC/2in1TabletTVWearable

isShowing(): Promise<boolean>

判断当前窗口是否已显示，使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[isWindowShowing()](arkts-apis-window-window.md#iswindowshowing9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示当前窗口已显示，返回false表示当前窗口未显示。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let promise = windowClass.isShowing();
4. promise.then((data) => {
5. console.info('Succeeded in checking whether the window is showing. Data: ' + JSON.stringify(data));
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to check whether the window is showing. Cause code: ${err.code}, message: ${err.message}`);
8. });
```

## on('systemAvoidAreaChange')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'systemAvoidAreaChange', callback: Callback<AvoidArea>): void

开启当前窗口系统避让区变化的监听。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[on('avoidAreaChange')](arkts-apis-window-window.md#onavoidareachange9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'systemAvoidAreaChange'，即系统避让区变化事件。 |
| callback | Callback<[AvoidArea](arkts-apis-window-i.md#avoidarea7)> | 是 | 回调函数。返回当前避让区。 |

**示例：**

```
1. windowClass.on('systemAvoidAreaChange', (data) => {
2. console.info('Succeeded in enabling the listener for system avoid area changes. Data: ' + JSON.stringify(data));
3. });
```

## off('systemAvoidAreaChange')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'systemAvoidAreaChange', callback?: Callback<AvoidArea>): void

关闭当前窗口系统避让区变化的监听。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[off('avoidAreaChange')](arkts-apis-window-window.md#offavoidareachange9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'systemAvoidAreaChange'，即系统避让区变化事件。 |
| callback | Callback<[AvoidArea](arkts-apis-window-i.md#avoidarea7)> | 否 | 回调函数。返回当前避让区。若传入参数，则关闭该监听。若未传入参数，则关闭所有系统避让区变化的监听。 |

**示例：**

```
1. const callback = (avoidArea: window.AvoidArea) => {
2. // ...
3. }
4. windowClass.on('systemAvoidAreaChange', callback);
5. windowClass.off('systemAvoidAreaChange', callback);
6. // 如果通过on开启多个callback进行监听，同时关闭所有监听：
7. windowClass.off('systemAvoidAreaChange');
```

## isSupportWideGamut(deprecated)

PhonePC/2in1TabletTVWearable

isSupportWideGamut(callback: AsyncCallback<boolean>): void

判断当前窗口是否支持广色域模式，使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[isWindowSupportWideGamut()](arkts-apis-window-window.md#iswindowsupportwidegamut9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示当前窗口支持广色域模式，返回false表示当前窗口不支持广色域模式。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. windowClass.isSupportWideGamut((err: BusinessError, data) => {
4. const errCode: number = err.code;
5. if (errCode) {
6. console.error(`Failed to check whether the window support WideGamut. Cause code: ${err.code}, message: ${err.message}`);
7. return;
8. }
9. console.info('Succeeded in checking whether the window support WideGamut Data: ' + JSON.stringify(data));
10. });
```

## isSupportWideGamut(deprecated)

PhonePC/2in1TabletTVWearable

isSupportWideGamut(): Promise<boolean>

判断当前窗口是否支持广色域模式，使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[isWindowSupportWideGamut()](arkts-apis-window-window.md#iswindowsupportwidegamut9-1)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示当前窗口支持广色域模式，返回false表示当前窗口不支持广色域模式。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let promise = windowClass.isSupportWideGamut();
4. promise.then((data) => {
5. console.info('Succeeded in checking whether the window support WideGamut. Data: ' + JSON.stringify(data));
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to check whether the window support WideGamut. Cause code: ${err.code}, message: ${err.message}`);
8. });
```

## setColorSpace(deprecated)

PhonePC/2in1TabletTVWearable

setColorSpace(colorSpace:ColorSpace, callback: AsyncCallback<void>): void

设置当前窗口为广色域模式或默认色域模式，使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[setWindowColorSpace()](arkts-apis-window-window.md#setwindowcolorspace9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colorSpace | [ColorSpace](arkts-apis-window-e.md#colorspace8) | 是 | 设置色域模式。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. windowClass.setColorSpace(window.ColorSpace.WIDE_GAMUT, (err: BusinessError) => {
4. const errCode: number = err.code;
5. if (errCode) {
6. console.error(`Failed to set window colorspace. Cause code: ${err.code}, message: ${err.message}`);
7. return;
8. }
9. console.info('Succeeded in setting window colorspace.');
10. });
```

## setColorSpace(deprecated)

PhonePC/2in1TabletTVWearable

setColorSpace(colorSpace:ColorSpace): Promise<void>

设置当前窗口为广色域模式或默认色域模式，使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[setWindowColorSpace()](arkts-apis-window-window.md#setwindowcolorspace9-1)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colorSpace | [ColorSpace](arkts-apis-window-e.md#colorspace8) | 是 | 设置色域模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let promise = windowClass.setColorSpace(window.ColorSpace.WIDE_GAMUT);
4. promise.then(() => {
5. console.info('Succeeded in setting window colorspace.');
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to set window colorspace. Cause code: ${err.code}, message: ${err.message}`);
8. });
```

## getColorSpace(deprecated)

PhonePC/2in1TabletTVWearable

getColorSpace(callback: AsyncCallback<ColorSpace>): void

获取当前窗口色域模式，使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[getWindowColorSpace()](arkts-apis-window-window.md#getwindowcolorspace9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[ColorSpace](arkts-apis-window-e.md#colorspace8)> | 是 | 回调函数。当获取成功，err为undefined，data为当前色域模式。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. windowClass.getColorSpace((err: BusinessError, data) => {
4. const errCode: number = err.code;
5. if (errCode) {
6. console.error(`Failed to get window colorspace. Cause code: ${err.code}, message: ${err.message}`);
7. return;
8. }
9. console.info('Succeeded in getting window colorspace. Cause:' + JSON.stringify(data));
10. });
```

## getColorSpace(deprecated)

PhonePC/2in1TabletTVWearable

getColorSpace(): Promise<ColorSpace>

获取当前窗口色域模式，使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[getWindowColorSpace()](arkts-apis-window-window.md#getwindowcolorspace9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ColorSpace](arkts-apis-window-e.md#colorspace8)> | Promise对象。返回当前色域模式。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let promise = windowClass.getColorSpace();
4. promise.then((data) => {
5. console.info('Succeeded in getting window color space. Cause:' + JSON.stringify(data));
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to get window colorspace. Cause code: ${err.code}, message: ${err.message}`);
8. });
```

## setBackgroundColor(deprecated)

PhonePC/2in1TabletTVWearable

setBackgroundColor(color: string, callback: AsyncCallback<void>): void

设置窗口的背景色，使用callback异步回调。Stage模型下，该接口需要在[loadContent()](arkts-apis-window-window.md#loadcontent9)或[setUIContent()](arkts-apis-window-window.md#setuicontent9)调用生效后使用。

说明

从API version 6开始支持，从API version 9开始废弃，建议使用[setWindowBackgroundColor()](arkts-apis-window-window.md#setwindowbackgroundcolor9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | string | 是 | 需要设置的背景色，为十六进制RGB或ARGB颜色，不区分大小写，例如'#00FF00'或'#FF00FF00'。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let color: string = '#00ff33';
4. windowClass.setBackgroundColor(color, (err: BusinessError) => {
5. const errCode: number = err.code;
6. if (errCode) {
7. console.error(`Failed to set the background color. Cause code: ${err.code}, message: ${err.message}`);
8. return;
9. }
10. console.info('Succeeded in setting the background color.');
11. });
```

## setBackgroundColor(deprecated)

PhonePC/2in1TabletTVWearable

setBackgroundColor(color: string): Promise<void>

设置窗口的背景色，使用Promise异步回调。Stage模型下，该接口需要在[loadContent()](arkts-apis-window-window.md#loadcontent9)或[setUIContent()](arkts-apis-window-window.md#setuicontent9)调用生效后使用。

说明

从API version 6开始支持，从API version 9开始废弃，建议使用[setWindowBackgroundColor()](arkts-apis-window-window.md#setwindowbackgroundcolor9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | string | 是 | 需要设置的背景色，为十六进制RGB或ARGB颜色，不区分大小写，例如'#00FF00'或'#FF00FF00'。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let color: string = '#00ff33';
4. let promise = windowClass.setBackgroundColor(color);
5. promise.then(() => {
6. console.info('Succeeded in setting the background color.');
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to set the background color. Cause code: ${err.code}, message: ${err.message}`);
9. });
```

## setBrightness(deprecated)

PhonePC/2in1TabletTVWearable

setBrightness(brightness: number, callback: AsyncCallback<void>): void

允许应用窗口设置屏幕亮度值，使用callback异步回调。

当前屏幕亮度规格：窗口设置屏幕亮度生效时，控制中心不可以调整系统屏幕亮度，窗口恢复默认系统亮度之后，控制中心可以调整系统屏幕亮度。

说明

从API version 6开始支持，从API version 9开始废弃，建议使用[setWindowBrightness()](arkts-apis-window-window.md#setwindowbrightness9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| brightness | number | 是 | 屏幕亮度值。该参数为浮点数，取值范围为[0.0, 1.0]或-1.0。1.0表示最亮，-1.0表示恢复成设置窗口亮度前的系统控制中心亮度。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let brightness: number = 1;
4. windowClass.setBrightness(brightness, (err: BusinessError) => {
5. const errCode: number = err.code;
6. if (errCode) {
7. console.error(`Failed to set the brightness. Cause code: ${err.code}, message: ${err.message}`);
8. return;
9. }
10. console.info('Succeeded in setting the brightness.');
11. });
```

## setBrightness(deprecated)

PhonePC/2in1TabletTVWearable

setBrightness(brightness: number): Promise<void>

允许应用窗口设置屏幕亮度值，使用Promise异步回调。

当前屏幕亮度规格：窗口设置屏幕亮度生效时，控制中心不可以调整系统屏幕亮度，窗口恢复默认系统亮度之后，控制中心可以调整系统屏幕亮度。

说明

从API version 6开始支持，从API version 9开始废弃，建议使用[setWindowBrightness()](arkts-apis-window-window.md#setwindowbrightness9-1)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| brightness | number | 是 | 屏幕亮度值。该参数为浮点数，取值范围为[0.0, 1.0]或-1.0。1.0表示最亮，-1.0表示恢复成设置窗口亮度前的系统控制中心亮度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let brightness: number = 1;
4. let promise = windowClass.setBrightness(brightness);
5. promise.then(() => {
6. console.info('Succeeded in setting the brightness.');
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to set the brightness. Cause code: ${err.code}, message: ${err.message}`);
9. });
```

## setDimBehind(deprecated)

PhonePC/2in1TabletTVWearable

setDimBehind(dimBehindValue: number, callback: AsyncCallback<void>): void

窗口叠加时，设备有子窗口的情况下设置靠后的窗口的暗度值，使用callback异步回调。

说明

该接口不支持使用。从API version 7开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dimBehindValue | number | 是 | 表示靠后的窗口的暗度值，取值范围为[0.0, 1.0]，取1.0时表示最暗。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. windowClass.setDimBehind(0.5, (err: BusinessError) => {
4. const errCode: number = err.code;
5. if (errCode) {
6. console.error(`Failed to set the dimness. Cause code: ${err.code}, message: ${err.message}`);
7. return;
8. }
9. console.info('Succeeded in setting the dimness.');
10. });
```

## setDimBehind(deprecated)

PhonePC/2in1TabletTVWearable

setDimBehind(dimBehindValue: number): Promise<void>

窗口叠加时，设备有子窗口的情况下设置靠后的窗口的暗度值，使用Promise异步回调。

说明

该接口不支持使用。从API version 7开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dimBehindValue | number | 是 | 表示靠后的窗口的暗度值，取值范围为0-1，1表示最暗。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let promise = windowClass.setDimBehind(0.5);
4. promise.then(() => {
5. console.info('Succeeded in setting the dimness.');
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to set the dimness. Cause code: ${err.code}, message: ${err.message}`);
8. });
```

## setFocusable(deprecated)

PhonePC/2in1TabletTVWearable

setFocusable(isFocusable: boolean, callback: AsyncCallback<void>): void

设置使用点击或其他方式使该窗口获焦的场景时，该窗口是否支持窗口焦点从操作前的获焦窗口切换到该窗口，使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[setWindowFocusable()](arkts-apis-window-window.md#setwindowfocusable9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isFocusable | boolean | 是 | 点击时是否支持切换焦点窗口。true表示支持；false表示不支持。设置为false时，该窗口不支持绑定输入法和接收键盘事件，如需处理输入逻辑，建议参考[不可获焦窗口中输入框与输入法交互指南](../harmonyos-guides/use-inputmethod-in-not-focusable-window.md)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let isFocusable: boolean = true;
4. windowClass.setFocusable(isFocusable, (err: BusinessError) => {
5. const errCode: number = err.code;
6. if (errCode) {
7. console.error(`Failed to set the window to be focusable. Cause code: ${err.code}, message: ${err.message}`);
8. return;
9. }
10. console.info('Succeeded in setting the window to be focusable.');
11. });
```

## setFocusable(deprecated)

PhonePC/2in1TabletTVWearable

setFocusable(isFocusable: boolean): Promise<void>

设置使用点击或其他方式使该窗口获焦的场景时，该窗口是否支持窗口焦点从点击前的获焦窗口切换到该窗口，使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[setWindowFocusable()](arkts-apis-window-window.md#setwindowfocusable9-1)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isFocusable | boolean | 是 | 点击时是否支持切换焦点窗口。true表示支持；false表示不支持。设置为false时，该窗口不支持绑定输入法和接收键盘事件，如需处理输入逻辑，建议参考[不可获焦窗口中输入框与输入法交互指南](../harmonyos-guides/use-inputmethod-in-not-focusable-window.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let isFocusable: boolean = true;
4. let promise = windowClass.setFocusable(isFocusable);
5. promise.then(() => {
6. console.info('Succeeded in setting the window to be focusable.');
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to set the window to be focusable. Cause code: ${err.code}, message: ${err.message}`);
9. });
```

## setKeepScreenOn(deprecated)

PhonePC/2in1TabletTVWearable

setKeepScreenOn(isKeepScreenOn: boolean, callback: AsyncCallback<void>): void

设置屏幕是否为常亮状态，使用callback异步回调。

说明

从API version 6开始支持，从API version 9开始废弃，建议使用[setWindowKeepScreenOn()](arkts-apis-window-window.md#setwindowkeepscreenon9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isKeepScreenOn | boolean | 是 | 设置屏幕是否为常亮状态。true表示常亮；false表示不常亮。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let isKeepScreenOn: boolean = true;
4. windowClass.setKeepScreenOn(isKeepScreenOn, (err: BusinessError) => {
5. const errCode: number = err.code;
6. if (errCode) {
7. console.error(`Failed to set the screen to be always on. Cause code: ${err.code}, message: ${err.message}`);
8. return;
9. }
10. console.info('Succeeded in setting the screen to be always on.');
11. });
```

## setKeepScreenOn(deprecated)

PhonePC/2in1TabletTVWearable

setKeepScreenOn(isKeepScreenOn: boolean): Promise<void>

设置屏幕是否为常亮状态，使用Promise异步回调。

说明

从API version 6开始支持，从API version 9开始废弃，建议使用[setWindowKeepScreenOn()](arkts-apis-window-window.md#setwindowkeepscreenon9-1)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isKeepScreenOn | boolean | 是 | 设置屏幕是否为常亮状态。true表示常亮；false表示不常亮。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let isKeepScreenOn: boolean = true;
4. let promise = windowClass.setKeepScreenOn(isKeepScreenOn);
5. promise.then(() => {
6. console.info('Succeeded in setting the screen to be always on.');
7. }).catch((err: BusinessError) => {
8. console.info(`Failed to set the screen to be always on. Cause code: ${err.code}, message: ${err.message}`);
9. });
```

## setOutsideTouchable(deprecated)

PhonePC/2in1TabletTVWearable

setOutsideTouchable(touchable: boolean, callback: AsyncCallback<void>): void

设置是否允许可点击子窗口之外的区域，使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。

从API version 9开始，系统默认允许点击子窗口之外的区域，此接口不再支持使用，也不再提供替代接口。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| touchable | boolean | 是 | 设置是否可点击。true表示可点击；false表示不可点击。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. windowClass.setOutsideTouchable(true, (err: BusinessError) => {
4. const errCode: number = err.code;
5. if (errCode) {
6. console.error(`Failed to set the area to be touchable. Cause code: ${err.code}, message: ${err.message}`);
7. return;
8. }
9. console.info('Succeeded in setting the area to be touchable.');
10. });
```

## setOutsideTouchable(deprecated)

PhonePC/2in1TabletTVWearable

setOutsideTouchable(touchable: boolean): Promise<void>

设置是否允许可点击子窗口之外的区域，使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。

从API version 9开始，系统默认允许点击子窗口之外的区域，此接口不再支持使用，也不再提供替代接口。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| touchable | boolean | 是 | 设置是否可点击。true表示可点击；false表示不可点击。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let promise = windowClass.setOutsideTouchable(true);
4. promise.then(() => {
5. console.info('Succeeded in setting the area to be touchable.');
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to set the area to be touchable. Cause code: ${err.code}, message: ${err.message}`);
8. });
```

## setPrivacyMode(deprecated)

PhonePC/2in1TabletTVWearable

setPrivacyMode(isPrivacyMode: boolean, callback: AsyncCallback<void>): void

设置窗口是否为隐私模式，使用callback异步回调。设置为隐私模式的窗口，窗口内容将无法被截屏或录屏。此接口可用于禁止截屏/录屏的场景。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[setWindowPrivacyMode()](arkts-apis-window-window.md#setwindowprivacymode9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isPrivacyMode | boolean | 是 | 窗口是否为隐私模式。true表示模式开启；false表示模式关闭。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let isPrivacyMode: boolean = true;
4. windowClass.setPrivacyMode(isPrivacyMode, (err: BusinessError) => {
5. const errCode: number = err.code;
6. if (errCode) {
7. console.error(`Failed to set the window to privacy mode. Cause code: ${err.code}, message: ${err.message}`);
8. return;
9. }
10. console.info('Succeeded in setting the window to privacy mode.');
11. });
```

## setPrivacyMode(deprecated)

PhonePC/2in1TabletTVWearable

setPrivacyMode(isPrivacyMode: boolean): Promise<void>

设置窗口是否为隐私模式，使用Promise异步回调。设置为隐私模式的窗口，窗口内容将无法被截屏或录屏。此接口可用于禁止截屏/录屏的场景。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[setWindowPrivacyMode()](arkts-apis-window-window.md#setwindowprivacymode9-1)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isPrivacyMode | boolean | 是 | 窗口是否为隐私模式。true表示模式开启；false表示模式关闭。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let isPrivacyMode: boolean = true;
4. let promise = windowClass.setPrivacyMode(isPrivacyMode);
5. promise.then(() => {
6. console.info('Succeeded in setting the window to privacy mode.');
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to set the window to privacy mode. Cause code: ${err.code}, message: ${err.message}`);
9. });
```

## setTouchable(deprecated)

PhonePC/2in1TabletTVWearable

setTouchable(isTouchable: boolean, callback: AsyncCallback<void>): void

设置窗口是否为可触状态，使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[setWindowTouchable()](arkts-apis-window-window.md#setwindowtouchable9)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isTouchable | boolean | 是 | 窗口是否为可触状态。true表示可触；false表示不可触。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let isTouchable = true;
4. windowClass.setTouchable(isTouchable, (err: BusinessError) => {
5. const errCode: number = err.code;
6. if (errCode) {
7. console.error(`Failed to set the window to be touchable. Cause code: ${err.code}, message: ${err.message}`);
8. return;
9. }
10. console.info('Succeeded in setting the window to be touchable.');
11. });
```

## setTouchable(deprecated)

PhonePC/2in1TabletTVWearable

setTouchable(isTouchable: boolean): Promise<void>

设置窗口是否为可触状态，使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[setWindowTouchable()](arkts-apis-window-window.md#setwindowtouchable9-1)替代。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isTouchable | boolean | 是 | 窗口是否为可触状态。true表示可触；false表示不可触。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let isTouchable = true;
4. let promise = windowClass.setTouchable(isTouchable);
5. promise.then(() => {
6. console.info('Succeeded in setting the window to be touchable.');
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to set the window to be touchable. Cause code: ${err.code}, message: ${err.message}`);
9. });
```
