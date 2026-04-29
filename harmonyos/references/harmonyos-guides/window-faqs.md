---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-faqs
title: 窗口开发常见问题
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 窗口开发常见问题
category: harmonyos-guides
scraped_at: 2026-04-29T13:29:11+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:d3296c49e41e43c1ff3f0f66a5c24b40ffedd2ab25d7a2b79cb4c7ebe82c0a52
---

## 如何在应用A启动过程中拉起另一个应用B

**解决措施**

应用A调用[on('windowStageEvent')](../harmonyos-references/arkts-apis-window-windowstage.md#onwindowstageevent9)接口监听[WindowStageEvent.ACTIVE](../harmonyos-references/arkts-apis-window-e.md#windowstageeventtype9)事件后调用[startAbility](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)接口拉起应用B。

**代码示例**

```
1. // applicationA EntryAbility.ts
2. import { UIAbility } from '@kit.AbilityKit';
3. import { window } from '@kit.ArkUI';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { Want, StartOptions } from '@kit.AbilityKit';

7. export default class EntryAbility extends UIAbility {
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. let want: Want = {
10. deviceId: '',
11. bundleName: 'com.example.applicationB',
12. abilityName: 'EntryAbility'
13. };

15. let options: StartOptions = {
16. displayId: 0
17. };

19. windowStage.on('windowStageEvent', (data) => {
20. let eventType: window.WindowStageEventType = data;
21. // 监听应用A切换到ACTIVE状态
22. if (eventType === window.WindowStageEventType.ACTIVE) {
23. try {
24. // 拉起应用B
25. this.context.startAbility(want, options, (err: BusinessError) => {
26. if (err.code) {
27. // 处理业务逻辑错误
28. console.error(`Failed to start ability, code is ${err.code}, message is ${err.message}.`);
29. return;
30. }
31. // 执行正常业务
32. console.info('Succeeded in starting Ability.');
33. });
34. } catch (err) {
35. // 处理入参错误异常
36. let code = (err as BusinessError).code;
37. let message = (err as BusinessError).message;
38. console.error(`Failed to start ability, code is ${code}, message is ${message}.`);
39. }
40. }
41. });
42. }
43. }
```

## 如何动态获取窗口宽高

在应用开发中，动态获取窗口宽高主要用于实现响应式布局，以适应不同尺寸的设备或窗口状态变化（如分屏、最大化恢复、拖拽缩放等）。

推荐使用[getMainWindowSync()](../harmonyos-references/arkts-apis-window-windowstage.md#getmainwindowsync9)、[getMainWindow()](../harmonyos-references/arkts-apis-window-windowstage.md#getmainwindow9-1)、[getSubWindow()](../harmonyos-references/arkts-apis-window-windowstage.md#getsubwindow9-1)中的任一方法获取到Window实例（windowClass），再通过此实例调用[getWindowProperties()](../harmonyos-references/arkts-apis-window-window.md#getwindowproperties9)接口得到其属性WindowProperties，通过属性获取窗口宽高即可。示例代码如下：

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';

4. export default class EntryAbility extends UIAbility {
5. // ...
6. onWindowStageCreate(windowStage: window.WindowStage) {
7. console.info('onWindowStageCreate');
8. let windowClass: window.Window = windowStage.getMainWindowSync(); // 获取应用主窗口
9. if (!windowClass) {
10. console.info('windowClass is null');
11. }
12. try {
13. let properties = windowClass.getWindowProperties();
14. let rect = properties.windowRect;
15. let windowWidth = rect.width;  // 窗口宽度，单位px
16. let windowHeight = rect.height; // 窗口高度，单位px
17. console.info(`Window Size: ${windowWidth} x ${windowHeight}`);
18. } catch (exception) {
19. console.error('Failed to obtain the window properties. Cause: ' + JSON.stringify(exception));
20. }
21. }
22. }
```

## 如何获取软键盘高度

固定态软键盘为一种特定的避让区域类型，[AvoidAreaType](../harmonyos-references/arkts-apis-window-e.md#avoidareatype7)中对应为固定态软键盘（TYPE\_KEYBOARD）类型，可以通过[getWindowAvoidArea()](../harmonyos-references/arkts-apis-window-window.md#getwindowavoidarea9)和[on('avoidAreaChange')](../harmonyos-references/arkts-apis-window-window.md#onavoidareachange9)动态监听软键盘避让区高度的变化。

另外，开发者也可以通过[on('keyboardHeightChange')](../harmonyos-references/arkts-apis-window-window.md#onkeyboardheightchange7)接口监听软键盘的占用高度。与避让区域不同的是，此接口回调仅返回软键盘的高度数值（number），而[on('avoidAreaChange')](../harmonyos-references/arkts-apis-window-window.md#onavoidareachange9)回调会返回整个软键盘区域（[Rect](../harmonyos-references/arkts-apis-window-i.md#rect7)）。

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';

4. export default class EntryAbility extends UIAbility {
5. // ...
6. onWindowStageCreate(windowStage: window.WindowStage) {
7. console.info('onWindowStageCreate');
8. // 获取应用主窗口
9. let windowClass: window.Window = windowStage.getMainWindowSync();
10. if (!windowClass) {
11. console.info('windowClass is null');
12. }
13. try {
14. // 获取软键盘避让区高度
15. let keyboardHeight = windowClass.getWindowAvoidArea(window.AvoidAreaType.TYPE_KEYBOARD).bottomRect.height;
16. // 动态监听软键盘避让区高度
17. windowClass.on('avoidAreaChange', (data) => {
18. if (data.type == window.AvoidAreaType.TYPE_KEYBOARD) {
19. keyboardHeight = data.area.bottomRect.height;
20. }
21. });
22. } catch (exception) {
23. console.error(`Failed to enable the listener for system avoid area changes. Cause code: ${exception.code}, message: ${exception.message}`);
24. }
25. }
26. }
```

## 如何获取PC设备顶部系统默认标题栏的高度

通过调用[getWindowDecorHeight()](../harmonyos-references/arkts-apis-window-window.md#getwindowdecorheight11)获取窗口的标题栏高度。

示例代码如下所示：

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';

4. export default class EntryAbility extends UIAbility {
5. // ...
6. onWindowStageCreate(windowStage: window.WindowStage) {
7. console.info('onWindowStageCreate');
8. // 获取应用主窗口
9. let windowClass: window.Window = windowStage.getMainWindowSync();
10. if (!windowClass) {
11. console.info('windowClass is null');
12. }
13. windowClass.setUIContent('pages/WindowPage').then(() => {
14. try {
15. let height = windowClass?.getWindowDecorHeight();
16. console.info(`Succeeded in getting the height of window decor: ${height}`);
17. } catch (exception) {
18. console.error(`Failed to get the height of window decor. Cause code: ${exception.code}, message: ${exception.message}`);
19. }
20. })
21. }
22. }
```

## 如何实现或判断窗口沉浸式布局

[沉浸式布局](window-terminology.md#沉浸式布局)是一种让应用界面聚焦内容，减少无关元素干扰的窗口状态。

非[自由窗口](window-terminology.md#自由窗口)可以通过调用[setWindowLayoutFullScreen()](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)设置沉浸式布局；自由窗口可以通过[setWindowDecorVisible()](../harmonyos-references/arkts-apis-window-window.md#setwindowdecorvisible11)接口控制窗口标题栏显隐，当标题栏隐藏时，窗口处于沉浸式布局。

可以通过[isImmersiveLayout()](../harmonyos-references/arkts-apis-window-window.md#isimmersivelayout20)判断当前窗口是否处于沉浸式布局。

示例代码如下所示：

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';

4. export default class EntryAbility extends UIAbility {
5. // ...
6. onWindowStageCreate(windowStage: window.WindowStage) {
7. console.info('onWindowStageCreate');
8. // 获取应用主窗口
9. let windowClass: window.Window = windowStage.getMainWindowSync();
10. if (!windowClass) {
11. console.info('windowClass is null');
12. }
13. try {
14. // 设置沉浸式布局
15. let promise = windowClass.setWindowLayoutFullScreen(true);
16. // 判断当前窗口是否处于沉浸式布局
17. let isImmersiveLayout = windowClass.isImmersiveLayout();
18. console.info(`isImmersiveLayout: ${isImmersiveLayout}`);
19. } catch (exception) {
20. console.error('Failed to obtain isImmersiveLayout. Cause: ' + JSON.stringify(exception));
21. }
22. }
23. }
```

## 如何隐藏状态栏和底部导航区域

可以调用[setSpecificSystemBarEnabled()](../harmonyos-references/arkts-apis-window-window.md#setspecificsystembarenabled11)隐藏状态栏和底部导航区域。

示例代码如下所示：

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';

4. export default class EntryAbility extends UIAbility {
5. // ...
6. onWindowStageCreate(windowStage: window.WindowStage) {
7. console.info('onWindowStageCreate');
8. // 获取应用主窗口
9. let windowClass: window.Window = windowStage.getMainWindowSync();
10. if (!windowClass) {
11. console.info('windowClass is null');
12. }
13. try {
14. // 隐藏状态栏
15. windowClass.setSpecificSystemBarEnabled('status', false);
16. // 隐藏底部导航区域
17. windowClass.setSpecificSystemBarEnabled('navigationIndicator', false);
18. } catch (exception) {
19. console.error('Failed to obtain isImmersiveLayout. Cause: ' + JSON.stringify(exception));
20. }
21. }
22. }
```

## 如何获取状态栏高度

状态栏为一种特定的避让区域类型，[AvoidAreaType](../harmonyos-references/arkts-apis-window-e.md#avoidareatype7)中对应为系统栏（TYPE\_SYSTEM）类型。

主窗口全屏时，可以通过[getWindowAvoidArea()](../harmonyos-references/arkts-apis-window-window.md#getwindowavoidarea9)获取到包含状态栏的避让区域[AvoidArea](../harmonyos-references/arkts-apis-window-i.md#avoidarea7)，间接获取到状态栏的高度。

示例代码如下所示：

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';

4. export default class EntryAbility extends UIAbility {
5. // ...
6. onWindowStageCreate(windowStage: window.WindowStage) {
7. console.info('onWindowStageCreate');
8. let windowClass: window.Window = windowStage.getMainWindowSync(); // 获取应用主窗口
9. if (!windowClass) {
10. console.info('windowClass is null');
11. }
12. try {
13. // 获取状态栏避让区高度
14. let statusBarHeight = windowClass.getWindowAvoidArea(window.AvoidAreaType.TYPE_SYSTEM).topRect.height;
15. } catch (exception) {
16. console.error(`Failed to enable the listener for system avoid area changes. Cause code: ${exception.code}, message: ${exception.message}`);
17. }
18. }
19. }
```

## 如何设置窗口背景透明

可以通过调用[setWindowBackgroundColor()](../harmonyos-references/arkts-apis-window-window.md#getwindowavoidarea9)接口，传入'#00XXXXXX'（其中X代表任意十六进制数字）或者透明的[ColorMetrics](../harmonyos-references/js-apis-arkui-graphics.md#colormetrics12)实现窗口背景透明。

说明

* 在支持[自由多窗](window-terminology.md#自由多窗模式)的设备上，存在窗口容器，窗口容器背景色覆盖整个窗口区域，包括标题栏和内容区域。调用[setWindowBackgroundColor()](../harmonyos-references/arkts-apis-window-window.md#getwindowavoidarea9)接口仅可设置应用内容背景色，此时会透出窗口容器背景色。
* 在2in1和Tablet设备上可以调用[setWindowContainerColor()](../harmonyos-references/arkts-apis-window-window.md#setwindowcontainercolor20)接口设置容器透明，在其他设备上暂不支持设置容器背景色。

示例代码如下所示：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { ColorMetrics } from '@kit.ArkUI';
3. import { window } from '@kit.ArkUI';

5. let storage: LocalStorage = new LocalStorage();
6. storage.setOrCreate('storageSimpleProp', 121);
7. windowClass.loadContent("pages/page2", storage, (err: BusinessError) => {
8. let errCode: number = err.code;
9. if (errCode) {
10. console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
11. return;
12. }
13. console.info('Succeeded in loading the content.');
14. // 采用ARGB方式
15. let color1: string = '#0000FF33';
16. // 采用ColorMetrics方式
17. let color2: ColorMetrics = ColorMetrics.numeric(0x00112233);
18. try {
19. windowClass?.setWindowBackgroundColor(color1);
20. windowClass?.setWindowBackgroundColor(color2);
21. } catch (exception) {
22. console.error(`Failed to set the background color. Cause code: ${exception.code}, message: ${exception.message}`);
23. };
24. });
```

## 如何实现横竖屏切换

需要先获取到主窗实例，然后调用[setPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9-1)接口设置窗口方向。更多详细信息请参考[窗口旋转](window-rotation.md)。

示例代码如下所示：

```
1. import { BusinessError } from '@kit.BasicServicesKit'
2. import { common } from '@kit.AbilityKit'
3. import { window } from '@kit.ArkUI'

5. @Entry
6. @Component
7. struct OrientationTestView {
8. private orientation: number =  1;
9. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
10. private windowClass = (this.context as common.UIAbilityContext).windowStage.getMainWindowSync();
11. setOrientation(orientation: number) {
12. this.windowClass.setPreferredOrientation(orientation).then(() => {
13. console.info('setWindowOrientation: ' + orientation + ' Succeeded.');
14. }).catch((err: BusinessError) => {
15. console.error('setWindowOrientation: ' + orientation + ' Failed. Cause: ' + JSON.stringify(err));
16. })
17. }
18. build() {
19. Column() {
20. Button('changeOrientation')
21. .onClick(() => {
22. this.setOrientation(this.orientation++ % 4 + 1)
23. })
24. }
25. .height('100%')
26. .width('100%')
27. .margin({'top' : 100})
28. }
29. }
```

更多内容请参考：

* [最佳实践：横竖屏切换](../best-practices/bpta-landscape-and-portrait-development.md)
* [setPreferredOrientation()入参枚举：Orientation](../harmonyos-references/arkts-apis-window-e.md#orientation9)

## 如何保持屏幕为横屏/竖屏，不随传感器旋转

通过[setPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9-1)接口设置应用的旋转策略为LANDSCAPE，则应用保持在横屏；设置为PORTRAIT，则应用保持在竖屏；设置为LOCKED时，可以锁定当前应用方向，不随屏幕旋转（不建议使用LOCKED，可能会发生非预期的方向改变）。

对于单一页面（Navigation）的禁用旋转，可以通过设置组件的[preferredOrientation](../harmonyos-references/ts-basic-components-navdestination.md#preferredorientation19)属性来实现，如果设置为横屏、竖屏、反向横屏或反向竖屏中某一方向，则该页面无法旋转到其他方向，从而实现页面级的旋转禁用。

## 如何获取设备的横竖屏状态

先通过[display.getDefaultDisplaySync()](../harmonyos-references/js-apis-display.md#displaygetdefaultdisplaysync9)获取当前默认的Display实例对象。

再通过该实例对象获取对应的[Orientation](../harmonyos-references/js-apis-display.md#orientation10)属性，以判断当前设备的横竖屏状态。

Orientation是显示设备当前显示的方向枚举，具体包括以下四种类型：

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PORTRAIT | 0 | 表示设备当前以竖屏方式显示。 |
| LANDSCAPE | 1 | 表示设备当前以横屏方式显示。 |
| PORTRAIT\_INVERTED | 2 | 表示设备当前以反向竖屏方式显示。 |
| LANDSCAPE\_INVERTED | 3 | 表示设备当前以反向横屏方式显示。 |

说明

通过[setPreferredOrientation](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9-1)接口设置旋转策略为LANDSCAPE，此时通过以上步骤获取到的[Orientation](../harmonyos-references/js-apis-display.md#orientation10)属性为反向横屏（即LANDSCAPE\_INVERTED），这是因为窗口的方向与屏幕的方向定义不一致。开发者也可以通过[convertOrientationAndRotation()](../harmonyos-references/arkts-apis-window-window.md#convertorientationandrotation23)来获取转换结果。

示例代码如下所示：

```
1. import { display } from '@kit.ArkUI';

3. let displayClass: display.Display | null = null;
4. try {
5. displayClass = display.getDefaultDisplaySync();
6. let orientation = displayClass.Orientation;
7. } catch (exception) {
8. console.error(`Failed to get default display. Code: ${exception.code}, message: ${exception.message}`);
9. }
```

## 如何设置应用默认横屏宽高比例

应用开发中，推荐使用[setContentAspectRatio()](../harmonyos-references/arkts-apis-window-window.md#setcontentaspectratio21)设置窗口内容布局的比例。

说明

* 根据相同的ratio参数调整窗口宽高时，窗口宽高会跟随窗口边框装饰尺寸或可见性变化而调整。
* 通过[setWindowDecorVisible](../harmonyos-references/arkts-apis-window-window.md#setwindowdecorvisible11)将窗口标题栏设置为不可见时，窗口内容区域将占据原本标题栏的高度空间。
* 通过其他接口如[resize](../harmonyos-references/arkts-apis-window-window.md#resize9-1)、[resizeAsync](../harmonyos-references/arkts-apis-window-window.md#resizeasync12)设置窗口大小时，不受ratio约束。
* 仅主窗可设置，且仅在自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING）下生效。
* API version 21以前的版本，请使用[setAspectRatio()](../harmonyos-references/arkts-apis-window-window.md#setaspectratio10)设置窗口内容布局。

示例代码如下：

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

## 如何设置窗口支持的显示模式supportWindowMode

在应用开发中， 推荐通过[module.json5](module-configuration-file.md)配置文件中的[abilities标签](module-configuration-file.md#abilities标签)的supportWindowMode字段设置窗口支持的显示模式。

supportWindowMode支持的取值如下：

| 配置值 | 模式 |
| --- | --- |
| "fullscreen" | 全屏模式 |
| "split" | 分屏模式 |
| "floating" | 悬浮窗模式 |

说明

* supportWindowMode字段类型为字符串数组，可缺省，缺省值为["fullscreen", "split", "floating"]。
* 在[自由窗口](window-terminology.md#自由窗口)状态下同时配置fullscreen和split时，如果应用的[targetAPIVersion](app-configuration-file.md#配置文件标签)小于15，窗口将以悬浮窗模式启动；如果应用的[targetAPIVersion](app-configuration-file.md#配置文件标签)大于等于15，窗口将以全屏模式启动。

module.json5配置示例如下：

```
1. {
2. "module": {
3. "abilities": [
4. {
5. "name": "EntryAbility",
6. "srcEntry": "./ets/entryability/EntryAbility.ets",
7. "description": "$string:EntryAbility_desc",
8. "displayName": "$string:EntryAbility_displayName",
9. "windowSize": {
10. "minWidth": 320,
11. "minHeight": 240
12. },
13. // 控制支持的窗口模式
14. "supportWindowMode": ["fullscreen", "split", "floating"],
15. "launchType": "standard",
16. "excludeFromMissions": false
17. }
18. ]
19. }
20. }
```

除以上配置方式外，应用可参考以下几种方式配置窗口支持的模式：

* 使用[metadata](window-config-m.md)标签配置，name为'ohos.ability.window.supportWindowModeInFreeMultiWindow'，该字段配置仅在自由多窗下生效。
* 在启动UIAbility时，通过[StartOptions](../harmonyos-references/js-apis-app-ability-startoptions.md#startoptions)中的supportWindowModes字段指定窗口是否显示最大化/窗口化/分屏按键。
* 在启动后，可通过调用[setSupportedWindowModes()](../harmonyos-references/arkts-apis-window-windowstage.md#setsupportedwindowmodes15)接口动态修改当前主窗口支持的窗口模式。

说明

自由多窗下的可支持窗口模式可以采用多种方法进行配置，配置优先级为：

通过[setSupportedWindowModes](../harmonyos-references/arkts-apis-window-windowstage.md#setsupportedwindowmodes15)接口配置 > 通过StartAbility配置[StartOption](../harmonyos-references/js-apis-app-ability-startoptions.md#startoptions)中的SupportWindowMode > 使用metadata配置 > 配置module.json5中[abilities](module-configuration-file.md#abilities标签)标签下的SupportWindowMode属性。

## 如何判断当前窗口是否为自由悬浮窗口模式

在应用开发中，有以下两种方式可判断应用是否处于自由悬浮窗口模式。

* 可通过[getWindowStatus()](../harmonyos-references/arkts-apis-window-window.md#getwindowstatus12)直接查询当前的窗口模式。当WindowStatusType为FLOATING时，表示应用处于自由悬浮窗口模式。

  不同返回值及对应的窗口模式如下表所示：

  | 名称 | 值 | 说明 |
  | --- | --- | --- |
  | UNDEFINED | 0 | 表示APP未定义窗口模式。 |
  | FULL\_SCREEN | 1 | 表示APP全屏模式。  [自由窗口](window-terminology.md#自由窗口)状态下，窗口铺满整个屏幕，默认无dock栏、标题栏和状态栏显示。  可通过[maximize()](../harmonyos-references/arkts-apis-window-window.md#maximize12)和[setTitleAndDockHoverShown()](../harmonyos-references/arkts-apis-window-window.md#settitleanddockhovershown14)配置，当hover到热区时是否显示标题栏和dock栏。  当maximize()和setTitleAndDockHoverShown()接口都调用时，以最后调用设置的效果为准。  非[自由窗口](window-terminology.md#自由窗口)状态下，窗口铺满整个屏幕，无标题栏和dock栏显示。可通过[setSpecificSystemBarEnabled()](../harmonyos-references/arkts-apis-window-window.md#setspecificsystembarenabled11)配置是否显示状态栏。 |
  | MAXIMIZE | 2 | 表示APP窗口最大化模式，在2in1设备中，窗口铺满整个屏幕，有dock栏和状态栏。 |
  | MINIMIZE | 3 | 表示APP窗口最小化模式。 |
  | FLOATING | 4 | 表示APP自由悬浮窗口模式。 |
  | SPLIT\_SCREEN | 5 | 表示APP分屏模式。 |
* 可通过[on('windowStatusChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowstatuschange11)接口监听窗口模式变化。

  如果应用需要在窗口模式发生变化时（例如从全屏切换到悬浮窗）立即做出响应，可以使用此接口监听窗口模式变化，以实现对应业务适配。

  ```
  1. import { UIAbility } from '@kit.AbilityKit';
  2. import { window } from '@kit.ArkUI';

  4. export default class EntryAbility extends UIAbility {
  5. // ...
  6. onWindowStageCreate(windowStage: window.WindowStage) {
  7. console.info('onWindowStageCreate');
  8. let windowClass: window.Window = windowStage.getMainWindowSync(); // 获取应用主窗口
  9. if (!windowClass) {
  10. console.info('windowClass is null');
  11. }
  12. try {
  13. // 注册窗口状态变化监听
  14. windowClass.on('windowStatusChange', (windowStatusType: window.WindowStatusType) => {
  15. console.info(`status change, new status: ${windowStatusType}`);
  16. });
  17. } catch (error) {
  18. console.error(`status listen err: ${JSON.stringify(error)}`);
  19. }
  20. // 注意：在合适的时机，例如组件销毁时，记得取消监听
  21. // windowClass.off('windowStatusChange');
  22. }
  23. }
  ```
* 可通过[on('windowStatusDidChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowstatusdidchange20)接口监听窗口模式变化。

  使用此接口开启窗口模式变化的监听后，当窗口windowStatus发生变化后进行通知（此时窗口[Rect](../harmonyos-references/arkts-apis-window-i.md#rect7)属性已经完成更新）。

  ```
  1. import { window } from '@kit.ArkUI';

  3. try {
  4. // 请先获取Window实例
  5. windowClass.on('windowStatusDidChange', (WindowStatusType) => {
  6. console.info(`Succeeded in enabling the listener for window status changes. Data: ${JSON.stringify(WindowStatusType)}`);
  7. });
  8. } catch (exception) {
  9. console.error(`Failed to unregister callback. Cause code: ${exception.code}, message: ${exception.message}`);
  10. }
  ```

说明

[on('windowStatusChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowstatuschange11)和[on('windowStatusDidChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowstatusdidchange20)均在窗口windowStatus发生变化时进行通知，[on('windowStatusChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowstatuschange11)不保证回调发生时窗口属性更新完成，应用若需要在收到windowStatus变化通知时能够立即获取到变化后的窗口大小、位置，建议使用[on('windowStatusDidChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowstatusdidchange20)。

## 如何设置全局悬浮窗背景色为透明

可以通过调用[setWindowBackgroundColor()](../harmonyos-references/arkts-apis-window-window.md#getwindowavoidarea9)接口，传入'#00XXXXXX'（其中X代表任意十六进制数字）或者透明的[ColorMetrics](../harmonyos-references/js-apis-arkui-graphics.md#colormetrics12)实现窗口背景透明。

## 如何判断应用被部分遮挡或完全遮挡

目前要判断当前窗口是否被遮挡有两个接口：

* [on('windowVisibilityChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowvisibilitychange11)：监听窗口可见性，当回调为false时，表示当前窗口不可见，完全被遮挡；当回调返回true时，表示当前窗口可见，但不能区分是部分遮挡还是无遮挡。
* [on('occlusionStateChanged')](../harmonyos-references/arkts-apis-window-window.md#onocclusionstatechanged22)：监听窗口可见性，返回三种可见状态：无遮挡（表示完全可见，值为0）、部分遮挡（表示部分可见，值为1）、完全遮挡（表示不可见，值为2）。

## 如何判断设备是否开启了自由多窗

可通过[isInFreeWindowMode()](../harmonyos-references/arkts-apis-window-window.md#isinfreewindowmode22)接口查询是否处于自由窗口状态。返回值为true时，表示当前窗口在自由窗口模式，返回值为false时，表示在非自由窗口模式。

可通过[on('freeWindowModeChange')](../harmonyos-references/arkts-apis-window-window.md#onfreewindowmodechange22)接口监听自由窗口模式变化。

## 如何设置隐私窗口

可通过[setWindowPrivacyMode()](../harmonyos-references/arkts-apis-window-window.md#setwindowprivacymode9-1)接口设置窗口为隐私模式，设置为隐私模式的窗口，窗口内容将无法被截屏或录屏。

对于画中画和闪控球窗口，其隐私模式跟随父窗口。

若需要对隐私窗口进行截图，可使用[snapshotIgnorePrivacy()](../harmonyos-references/arkts-apis-window-window.md#snapshotignoreprivacy18)接口。

## resize、moveWindowTo等接口有什么位置/大小限制

当调用[resize()](../harmonyos-references/arkts-apis-window-window.md#resize9-1)接口调整窗口大小时，窗口尺寸大小范围会受到[WindowLimits](../harmonyos-references/arkts-apis-window-i.md#windowlimits11)限制，具体尺寸限制范围可以通过[getWindowLimits](../harmonyos-references/arkts-apis-window-window.md#getwindowlimits11)接口进行查询。

调用[moveWindowTo()](../harmonyos-references/arkts-apis-window-window.md#movewindowto9-1)接口调整窗口位置对窗口位置无限制。

说明

**resize接口其他限制：**

* 在[自由窗口](window-terminology.md#自由窗口)状态下，窗口为自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING，WindowStatusType可通过[getWindowStatus()](../harmonyos-references/arkts-apis-window-window.md#getwindowstatus12)获取）时调用生效，否则抛出错误码1300002。
* 在非[自由窗口](window-terminology.md#自由窗口)状态下，主窗口调用不生效。

**moveWindowTo接口其他限制：**

* 不建议在除自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING，WindowStatusType可通过[getWindowStatus()](../harmonyos-references/arkts-apis-window-window.md#getwindowstatus12)获取）外的其他窗口模式下使用。
* 在[自由窗口](window-terminology.md#自由窗口)状态下，窗口相对于屏幕移动；在非自由窗口状态下，窗口相对于父窗口移动。
* 若需在非自由窗口状态下实现相对于屏幕的移动，请使用[moveWindowToGlobal()](../harmonyos-references/arkts-apis-window-window.md#movewindowtoglobal15)。
* 在非[自由窗口](window-terminology.md#自由窗口)状态下，主窗口调用不生效。

## 如何设置或取消水印

* 进程级水印：可通过[setWatermarkImageForAppWindows()](../harmonyos-references/arkts-apis-window-f.md#windowsetwatermarkimageforappwindows21)设置或取消应用进程级水印，针对当前应用进程的窗口生效，包括后续该进程新创建的窗口。

## 如何将创建的窗口移动到扩展屏

* 应用可通过主动调用[moveWindowToGlobal()](../harmonyos-references/arkts-apis-window-window.md#movewindowtoglobal15)接口将当前窗口移动到扩展屏幕，通过配置接口参数中的[MoveConfiguration](../harmonyos-references/arkts-apis-window-i.md#moveconfiguration15)指定当前窗口期望移动的目标屏幕。
* 应用也可调用[startMoving()](../harmonyos-references/arkts-apis-window-window.md#startmoving14)接口通过鼠标或触摸点拖拽将当前窗口移动到目标屏幕上。该接口仅在[onTouch](../harmonyos-references/ts-universal-events-touch.md#ontouch)事件（其中，事件类型必须为TouchType.Down）的回调方法中调用才会有移动效果，成功调用此接口后，窗口将跟随鼠标或触摸点移动。

## 子窗口背景如何实现半透明效果

子窗口可以调用[setWindowBackgroundColor()](../harmonyos-references/arkts-apis-window-window.md#setwindowbackgroundcolor9)接口，传入'#XXYYYYYY'（其中XX代表任意十六进制且不为0数值，Y表示任意十六进制数字）或者半透明的[ColorMetrics](../harmonyos-references/js-apis-arkui-graphics.md#colormetrics12)。

示例代码如下所示：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { ColorMetrics } from '@kit.ArkUI';
3. import { window } from '@kit.ArkUI';

5. let storage: LocalStorage = new LocalStorage();
6. storage.setOrCreate('storageSimpleProp', 121);
7. windowClass.loadContent("pages/page2", storage, (err: BusinessError) => {
8. let errCode: number = err.code;
9. if (errCode) {
10. console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
11. return;
12. }
13. console.info('Succeeded in loading the content.');
14. let color1: string = '#8800FF33'; // 采用ARGB方式
15. let color2: ColorMetrics = ColorMetrics.numeric(0x88112233);  // 采用ColorMetrics方式
16. try {
17. windowClass?.setWindowBackgroundColor(color1);
18. windowClass?.setWindowBackgroundColor(color2);
19. } catch (exception) {
20. console.error(`Failed to set the background color. Cause code: ${exception.code}, message: ${exception.message}`);
21. };
22. });
```

## 如何设置页面级亮度

当前不支持设置页面级亮度，仅支持设置窗口级亮度。

应用若想实现页面级亮度调整，可以在进入特定页面时在主窗调用[setWindowBrightness()](../harmonyos-references/arkts-apis-window-window.md#setwindowbrightness9-1)调整亮度，在退出特定页面时，在主窗调用[setWindowBrightness()](../harmonyos-references/arkts-apis-window-window.md#setwindowbrightness9-1)传入-1，恢复为系统屏幕亮度。

## 如何恢复系统屏幕亮度

针对Phone、Tablet设备，应用可以调用[setWindowBrightness()](../harmonyos-references/arkts-apis-window-window.md#setwindowbrightness9-1)传入-1，即可恢复为系统屏幕亮度。

针对PC/2in1设备，由于窗口亮度和系统亮度已实现归一化，故调用[setWindowBrightness()](../harmonyos-references/arkts-apis-window-window.md#setwindowbrightness9-1)接口后将直接改变系统亮度，目前尚无恢复至调用前窗口亮度的方法。

## 如何正常获取顶层窗口

**问题现象**

当使用[getLastWindow()](../harmonyos-references/arkts-apis-window-f.md#windowgetlastwindow9)获取应用最顶层窗口时，获取到了正在销毁的子窗。

**产生原因**

当使用[destroyWindow()](../harmonyos-references/arkts-apis-window-window.md#destroywindow9)销毁子窗时，未等待其销毁完成即调用[getLastWindow()](../harmonyos-references/arkts-apis-window-f.md#windowgetlastwindow9)，导致获取到了正在销毁的子窗。

**解决措施**

在使用[getLastWindow()](../harmonyos-references/arkts-apis-window-f.md#windowgetlastwindow9)获取应用最顶层窗口前，应确保子窗销毁、窗口创建等操作已完成。

**示例代码**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { window } from '@kit.ArkUI';

4. let lastWindow: window.Window | undefined = undefined;
5. // 不建议写法
6. try {
7. // 请先获取window实例
8. windowClass.destroyWindow();
9. try {
10. window.getLastWindow(this.context).then((topWindow) => {
11. lastWindow = topWindow;
12. }).catch((err: BusinessError) => {
13. console.error(`Failed to obtain the last window. Cause code: ${err.code}, message: ${err.message}`);
14. });
15. } catch (exception) {
16. console.error(`Failed to obtain the last window. Cause code: ${exception.code}, message: ${exception.message}`);
17. }
18. } catch (exception) {
19. console.error(`Failed to destroy. Cause code: ${exception.code}, message: ${exception.message}`);
20. };

22. // 建议写法
23. try {
24. // 请先获取window实例
25. windowClass.destroyWindow().then(() => {
26. try {
27. window.getLastWindow(this.context).then((topWindow) => {
28. lastWindow = topWindow;
29. }).catch((err: BusinessError) => {
30. console.error(`Failed to obtain the last window. Cause code: ${err.code}, message: ${err.message}`);
31. });
32. } catch (exception) {
33. console.error(`Failed to obtain the last window. Cause code: ${exception.code}, message: ${exception.message}`);
34. }
35. }).catch((err: BusinessError) => {
36. console.error(`Failed to destroy the window. Cause code: ${err.code}, message: ${err.message}`);
37. });
38. } catch (exception) {
39. console.error(`Failed to destroy. Cause code: ${exception.code}, message: ${exception.message}`);
40. };
```

## getWindowProperties接口返回值中的窗口类型（type字段）不符合预期

**问题现象**

因为历史问题，主窗场景调用[getWindowProperties()](../harmonyos-references/arkts-apis-window-window.md#getwindowproperties9)获取到的窗口类型即[WindowType](../harmonyos-references/arkts-apis-window-e.md#windowtype7)为TYPE\_SYSTEM\_ALERT而不是TYPE\_MAIN。

**解决措施**

系统的后续API版本中将提供新的字段修正。

应用内创建窗口时需要指明窗口类型，开发者可以直接感知窗口类型，不必要通过此接口主动获取。

## on('windowSizeChange')等监听回调中通过getWindowAvoidArea()接口获取到的避让区域数据不是最新的

**问题现象**

在[on('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7)、[on('windowRectChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowrectchange12)等窗口属性变化监听回调中，通过[getWindowAvoidArea()](../harmonyos-references/arkts-apis-window-window.md#getwindowavoidarea9)接口获取到的避让区域数据不准确。

**产生原因**

避让区域更新同时依赖窗口位置/尺寸属性的更新和系统界面元素（如状态栏）的位置/尺寸更新，在窗口属性更新回调触发时系统界面元素不一定已完成更新，这个时候通过getWindowAvoidArea()接口不能拿到准确的避让区域。

**解决措施**

通过避让区域专有的监听接口[on('avoidAreaChange')](../harmonyos-references/arkts-apis-window-window.md#onavoidareachange9)监听避让区域变化，避免在其他窗口属性变化事件回调中通过getWindowAvoidArea()接口主动获取避让区域。

**示例代码**

```
1. import { window } from '@kit.ArkUI';

3. // 代码中假设windowClass为已获取的Window实例

5. // 错误写法：监听windowSizeChange事件主动获取避让区域
6. windowClass.on('windowSizeChange', () => {
7. try {
8. const systemAvoidArea = windowClass.getWindowAvoidArea(window.AvoidAreaType.TYPE_SYSTEM);  // 获取到的避让区域不准确
9. } catch (exception) {
10. console.error(`Failed to get window avoid area. Cause code: ${exception.code}, message: ${exception.message}`);
11. }
12. });

14. // 正确写法：监听avoidAreaChange事件
15. windowClass.on('avoidAreaChange', (data) => {
16. if (data.type === window.AvoidAreaType.TYPE_SYSTEM) {
17. const systemAvoidArea = data.area;  // 回调中的数据总是准确的避让区域
18. }
19. });
```
