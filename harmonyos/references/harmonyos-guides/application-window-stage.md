---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-window-stage
title: 管理应用窗口（Stage模型）
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 管理应用窗口（Stage模型）
category: harmonyos-guides
scraped_at: 2026-04-29T13:29:02+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:6b8d54c2a462b9393e787d7defb9b249344ea2dcf96355ebd152f3ee5599be33
---

## 基本概念

* 窗口沉浸式能力：指对状态栏、导航栏等系统窗口进行控制，减少状态栏导航栏等系统界面的突兀感，从而使用户获得最佳体验的能力。沉浸式能力只在应用主窗口作为全屏窗口时生效。通常情况下，应用的辅助窗口（子窗、全局悬浮窗等）和处于自由窗口下的应用主窗口无法使用沉浸式能力。
* 全局悬浮窗：全局悬浮窗是一种特殊的应用辅助窗口，具备在应用主窗口和对应Ability退至后台后仍然可以在前台显示的能力。全局悬浮窗可以用于应用退至后台后，使用小窗继续显示UI，例如音乐应用用于显示桌面歌词等。应用在创建全局悬浮窗前，需要申请对应的权限。

## 场景介绍

在Stage模型下，管理应用窗口的典型场景有：

* 设置应用主窗口属性及目标页面
* 设置应用子窗口属性及目标页面
* 体验窗口沉浸式能力
* 设置全局悬浮窗
* 监听窗口不可交互与可交互事件

以下分别介绍具体开发方式。

## 接口说明

上述场景涉及的常用接口如下表所示。更多API说明请参见[API参考](../harmonyos-references/arkts-apis-window.md)。

| 实例名 | 接口名 | 描述 |
| --- | --- | --- |
| WindowStage | getMainWindow(callback: AsyncCallback<Window>): void | 获取WindowStage实例下的主窗口。  此接口仅可在Stage模型下使用。 |
| WindowStage | loadContent(path: string, callback: AsyncCallback<void>): void | 为当前WindowStage的主窗口加载具体页面。  其中path为要加载到窗口中的页面内容的路径，该路径需添加到工程的main\_pages.json文件中。  此接口仅可在Stage模型下使用。 |
| WindowStage | createSubWindow(name: string, callback: AsyncCallback<Window>): void | 创建子窗口。  此接口仅可在Stage模型下使用。 |
| WindowStage | on(eventType: 'windowStageEvent', callback: Callback<WindowStageEventType>): void | 开启WindowStage生命周期变化的监听。  此接口仅可在Stage模型下使用。 |
| window静态方法 | createWindow(config: Configuration, callback: AsyncCallback<Window>): void | 创建子窗口或者系统窗口。  -config：创建窗口时的参数。 |
| Window | setUIContent(path: string, callback: AsyncCallback<void>): void | 根据当前工程中某个页面的路径为窗口加载具体的页面内容。  其中path为要加载到窗口中的页面内容的路径，在Stage模型下该路径需添加到工程的main\_pages.json文件中。 |
| Window | setWindowBrightness(brightness: number, callback: AsyncCallback<void>): void | 设置屏幕亮度值。 |
| Window | setWindowTouchable(isTouchable: boolean, callback: AsyncCallback<void>): void | 设置窗口是否为可触状态。true表示可触；false表示不可触。 |
| Window | moveWindowTo(x: number, y: number, callback: AsyncCallback<void>): void | 移动当前窗口位置。 |
| Window | resize(width: number, height: number, callback: AsyncCallback<void>): void | 改变当前窗口大小。 |
| Window | setWindowLayoutFullScreen(isLayoutFullScreen: boolean): Promise<void> | 设置主窗口或子窗口的布局是否为沉浸式布局。true表示沉浸式布局；false表示非沉浸式布局。 |
| Window | setWindowSystemBarEnable(names: Array<'status'|'navigation'>): Promise<void> | 设置主窗口状态栏、底部导航（根据用户设置，可表现为导航条或三键导航栏）的可见模式，状态栏和底部导航通过status控制、navigation参数无效果。  例如，该参数设置为['status', 'navigation']，则全部显示；设置为[]，则不显示。 |
| Window | setWindowSystemBarProperties(systemBarProperties: SystemBarProperties): Promise<void> | 设置窗口内导航栏、状态栏属性。  systemBarProperties：导航栏、状态栏的属性集合。 |
| Window | showWindow(callback: AsyncCallback<void>): void | 显示当前窗口。 |
| Window | on(type: 'touchOutside', callback: Callback<void>): void | 开启本窗口区域外的点击事件的监听。 |
| Window | destroyWindow(callback: AsyncCallback<void>): void | 销毁当前窗口。 |

## 设置应用主窗口

在Stage模型下，应用主窗口由UIAbility创建并维护生命周期。在UIAbility的onWindowStageCreate回调中，通过WindowStage获取应用主窗口，即可对其进行属性设置等操作。还可以在应用配置文件中设置应用主窗口的属性，如最大窗口宽度maxWindowWidth等，详见[module.json5配置文件中的abilities标签](module-configuration-file.md#abilities标签)。

### 开发步骤

1. 获取应用主窗口。

   通过getMainWindow接口获取应用主窗口。
2. 设置主窗口属性。

   可设置主窗口的背景色、亮度值、是否可触等多个属性，开发者可根据需要选择对应的接口。本示例以设置“是否可触”属性为例。
3. 为主窗口加载对应的目标页面。

   通过loadContent接口加载主窗口的目标页面。

```
1. import { UIAbility} from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. const DOMAIN = 0X0000;
7. const TAG: string = '[Sample_CreatMainWindow]';

9. export default class EntryAbility extends UIAbility {
10. onWindowStageCreate(windowStage: window.WindowStage) {
11. // 1.获取应用主窗口。
12. let windowClass: window.Window | null = null;
13. windowStage.getMainWindow((err: BusinessError, data) => {
14. let errCode: number = err.code;
15. if (errCode) {
16. hilog.error(DOMAIN, TAG, `Failed to obtain the main window. Code:${err.code}, message:${err.message}`);
17. return;
18. }
19. windowClass = data;
20. hilog.info(DOMAIN, TAG, `Succeeded in obtaining the main window. Result:${data}`);
21. // 2.设置主窗口属性。以设置"是否可触"属性为例。
22. let isTouchable: boolean = true;
23. windowClass.setWindowTouchable(isTouchable, (err: BusinessError) => {
24. let errCode: number = err.code;
25. if (errCode) {
26. hilog.error(DOMAIN, TAG, `Failed to set the window to be touchable. Cause: ${JSON.stringify(err)}`);
27. return;
28. }
29. hilog.info(DOMAIN, TAG, `Succeeded in setting the window to be touchable.`);
30. })
31. })
32. // 3.为主窗口加载对应的目标页面。
33. windowStage.loadContent('pages/Index', (err: BusinessError) => {
34. let errCode: number = err.code;
35. if (errCode) {
36. hilog.error(DOMAIN, TAG, `Failed to load the content. Cause: ${JSON.stringify(err)}`);
37. return;
38. }
39. hilog.info(DOMAIN, TAG, `Succeeded in loading the content.`);
40. });
41. }
42. };
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArkUIWindowSamples/CreateMainWindow/entry/src/main/ets/entryability/EntryAbility.ets#L16-L59)

## 设置应用子窗口

开发者可以按需创建应用子窗口，如弹窗等，并对其进行属性设置等操作。

说明

以下几种场景不建议使用子窗口，建议优先考虑使用控件[overlay](../harmonyos-references/ts-universal-attributes-overlay.md)能力实现。

* 移动设备（手机、在非自由模式下的平板设备）场景下子窗不能超出处于悬浮窗模式、分屏模式的应用主窗口范围，与控件一致。
* 分屏窗口与自由窗口模式下，主窗口位置大小发生改变时控件实时跟随变化能力优于子窗。
* 部分设备平台下根据实际的系统配置限制，子窗只有系统默认的动效和圆角阴影，应用无法设置，自由度低。

### 开发步骤

1. 创建应用子窗口。

   通过createSubWindow接口创建应用子窗口。

   子窗口创建后默认是[沉浸式布局](window-terminology.md#沉浸式布局)。
2. 设置子窗口属性。

   子窗口创建成功后，可以改变其大小、位置等，还可以根据应用需要设置窗口背景色、亮度等属性。

   在调用showWindow之前，建议设置子窗口的大小和位置。

   如果没有设置子窗口的大小，调用showWindow后:

   * [自由窗口](window-terminology.md#自由窗口)状态下，默认子窗口大小为当前物理屏幕的大小。其中，[MateBook Fold折叠电脑](../best-practices/bpta-mate-book-fold.md)半折叠态下，默认子窗口大小为竖向展开态的物理屏幕大小。
   * 非自由窗口状态下，默认子窗口大小为主窗口大小。
3. 加载显示子窗口的具体内容。

   通过setUIContent和showWindow接口加载显示子窗口的具体内容。
4. 销毁子窗口。

   当不再需要某些子窗口时，可根据具体实现逻辑，使用destroyWindow接口销毁子窗口。

直接在onWindowStageCreate里面创建子窗口的整体示例代码如下：

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. const DOMAIN = 0X0000;
7. const TAG: string = '[Sample_CreatSubWindow]';

9. let windowStage_: window.WindowStage | null = null;
10. let sub_windowClass: window.Window | null = null;

12. export default class EntryAbility extends UIAbility {
13. showSubWindow() {
14. // 1.创建应用子窗口。
15. if (windowStage_ == null) {
16. hilog.error(DOMAIN, TAG, `Failed to create the subwindow. Cause: windowStage_ is null`);
17. } else {
18. windowStage_.createSubWindow('mySubWindow', (err: BusinessError, data) => {
19. let errCode: number = err.code;
20. if (errCode) {
21. hilog.error(DOMAIN, TAG, `Failed to create the subwindow. Cause: ${JSON.stringify(err)}`);
22. return;
23. }
24. sub_windowClass = data;
25. if (!sub_windowClass) {
26. hilog.error(DOMAIN, TAG, `sub_windowClass is null`);
27. return;
28. }
29. hilog.info(DOMAIN, TAG, `Succeeded in creating the subwindow. Data: ${JSON.stringify(data)}`);
30. // 2.子窗口创建成功后，设置子窗口的位置、大小及相关属性等。
31. sub_windowClass.moveWindowTo(300, 300, (err: BusinessError) => {
32. let errCode: number = err.code;
33. if (errCode) {
34. hilog.error(DOMAIN, TAG, `Failed to move the window. Cause: ${JSON.stringify(err)}`);
35. return;
36. }
37. hilog.info(DOMAIN, TAG, `Succeeded in moving the window.`);
38. });
39. sub_windowClass.resize(500, 500, (err: BusinessError) => {
40. let errCode: number = err.code;
41. if (errCode) {
42. hilog.error(DOMAIN, TAG, `Failed to change the window size. Cause: ${JSON.stringify(err)}`);
43. return;
44. }
45. hilog.info(DOMAIN, TAG, `Succeeded in changing the window size.`);
46. });
47. // 3.为子窗口加载对应的目标页面。
48. sub_windowClass.setUIContent('pages/Index', (err: BusinessError) => {
49. let errCode: number = err.code;
50. if (errCode) {
51. hilog.info(DOMAIN, TAG, `Failed to load the content. Cause: ${JSON.stringify(err)}`);
52. return;
53. }
54. hilog.info(DOMAIN, TAG, `Succeeded in loading the content.`);
55. if (!sub_windowClass) {
56. hilog.error(DOMAIN, TAG, `sub_windowClass is null`);
57. return;
58. }
59. // 3.显示子窗口。
60. sub_windowClass.showWindow((err: BusinessError) => {
61. let errCode: number = err.code;
62. if (errCode) {
63. hilog.error(DOMAIN, TAG, `Failed to show the window. Cause: ${JSON.stringify(err)}`);
64. return;
65. }
66. hilog.info(DOMAIN, TAG, `Succeeded in showing the window.`);
67. });
68. });
69. })
70. }
71. }

73. destroySubWindow() {
74. if (!sub_windowClass) {
75. hilog.error(DOMAIN, TAG, `sub_windowClass is null`);
76. return;
77. }
78. // 4.销毁子窗口。当不再需要子窗口时，可根据具体实现逻辑，使用destroy对其进行销毁。
79. sub_windowClass.destroyWindow((err: BusinessError) => {
80. let errCode: number = err.code;
81. if (errCode) {
82. hilog.error(DOMAIN, TAG, `Failed to destroy the window. Cause: ${JSON.stringify(err)}`);
83. return;
84. }
85. hilog.info(DOMAIN, TAG, `Succeeded in destroying the window.`);
86. });
87. }

89. onWindowStageCreate(windowStage: window.WindowStage) {
90. windowStage_ = windowStage;
91. // 开发者可以在适当的时机，如主窗口上按钮点击事件等，创建子窗口。并不一定需要在onWindowStageCreate调用，这里仅作展示
92. this.showSubWindow();
93. }

95. onWindowStageDestroy() {
96. // 开发者可以在适当的时机，如子窗口上点击关闭按钮等，销毁子窗口。并不一定需要在onWindowStageDestroy调用，这里仅作展示
97. this.destroySubWindow();
98. }
99. };
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArkUIWindowSamples/CreateSubWindow/entry/src/main/ets/entryability/EntryAbility.ets#L16-L116)

另外，也可以在某个page页面通过点击按钮创建子窗口，整体示例代码如下：

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { window } from '@kit.ArkUI';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. const DOMAIN = 0X0000;
7. const TAG: string = '[Sample_CreatSubWindow2]';

9. export default class EntryAbility extends UIAbility {
10. onWindowStageCreate(windowStage: window.WindowStage) {
11. windowStage.loadContent('pages/Index', (err) => {
12. if (err.code) {
13. hilog.error(DOMAIN, TAG, `Failed to load the content. Cause: ${JSON.stringify(err)}`);
14. return;
15. }
16. hilog.info(DOMAIN, TAG, `Succeeded in loading the content.`);
17. });

19. // 给Index页面传递windowStage
20. AppStorage.setOrCreate('windowStage', windowStage);
21. }
22. }
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArkUIWindowSamples/CreateSubWindow2/entry/src/main/ets/entryability/EntryAbility.ets#L16-L39)

```
1. // Index.ets
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. const DOMAIN = 0X0000;
7. const TAG : string = '[Sample_CreatSubWindow2]';

9. let windowStage_: window.WindowStage | undefined = undefined;
10. let sub_windowClass: window.Window | undefined = undefined;
11. @Entry
12. @Component
13. struct Index {
14. @State message: string = 'Hello World';
15. private createSubWindow(){
16. // 获取windowStage
17. windowStage_ = AppStorage.get('windowStage');
18. // 1.创建应用子窗口。
19. if (windowStage_ == null) {
20. hilog.error(DOMAIN, TAG, `Failed to create the subwindow. Cause: windowStage_ is null`);
21. } else {
22. windowStage_.createSubWindow('mySubWindow', (err: BusinessError, data) => {
23. let errCode: number = err.code;
24. if (errCode) {
25. hilog.error(DOMAIN, TAG, `Failed to create the subwindow. Cause: ${JSON.stringify(err)}`);
26. return;
27. }
28. sub_windowClass = data;
29. if (!sub_windowClass) {
30. hilog.error(DOMAIN, TAG, `sub_windowClass is null`);
31. return;
32. }
33. hilog.info(DOMAIN, TAG, `Succeeded in creating the subwindow. Data: ${JSON.stringify(data)}`);
34. // 2.子窗口创建成功后，设置子窗口的位置、大小及相关属性等。
35. sub_windowClass.moveWindowTo(300, 300, (err: BusinessError) => {
36. let errCode: number = err.code;
37. if (errCode) {
38. hilog.error(DOMAIN, TAG, `Failed to move the window. Cause: ${JSON.stringify(err)}`);
39. return;
40. }
41. hilog.info(DOMAIN, TAG, `Succeeded in moving the window.`);
42. });
43. sub_windowClass.resize(500, 500, (err: BusinessError) => {
44. let errCode: number = err.code;
45. if (errCode) {
46. hilog.error(DOMAIN, TAG, `Failed to change the window size. Cause: ${JSON.stringify(err)}`);
47. return;
48. }
49. hilog.info(DOMAIN, TAG, `Succeeded in changing the window size.`);
50. });
51. // 3.为子窗口加载对应的目标页面。
52. sub_windowClass.setUIContent('pages/SubWindow', (err: BusinessError) => {
53. let errCode: number = err.code;
54. if (errCode) {
55. hilog.error(DOMAIN, TAG, `Failed to load the content. Cause: ${JSON.stringify(err)}`);
56. return;
57. }
58. hilog.info(DOMAIN, TAG, `Succeeded in loading the content.`);
59. if (!sub_windowClass) {
60. hilog.error(DOMAIN, TAG, `sub_windowClass is null`);
61. return;
62. }
63. // 3.显示子窗口。
64. sub_windowClass.showWindow((err: BusinessError) => {
65. let errCode: number = err.code;
66. if (errCode) {
67. hilog.error(DOMAIN, TAG, `Failed to show the window. Cause: ${JSON.stringify(err)}`);
68. return;
69. }
70. hilog.info(DOMAIN, TAG, `Succeeded in showing the window.`);
71. });
72. });
73. })
74. }
75. }
76. private destroySubWindow(){
77. if (!sub_windowClass) {
78. hilog.error(DOMAIN, TAG, `sub_windowClass is null`);
79. return;
80. }
81. // 4.销毁子窗口。当不再需要子窗口时，可根据具体实现逻辑，使用destroy对其进行销毁。
82. sub_windowClass.destroyWindow((err: BusinessError) => {
83. let errCode: number = err.code;
84. if (errCode) {
85. hilog.error(DOMAIN, TAG, `Failed to destroy the window. Cause: ${JSON.stringify(err)}`);
86. return;
87. }
88. hilog.info(DOMAIN, TAG, `Succeeded in destroying the window.`);
89. });
90. }
91. build() {
92. Row() {
93. Column() {
94. Text(this.message)
95. .fontSize(50)
96. .fontWeight(FontWeight.Bold)
97. Button(){
98. Text('CreateSubWindow')
99. .fontSize(24)
100. .fontWeight(FontWeight.Normal)
101. }.width(220).height(68)
102. .margin({left:10, top:60})
103. .onClick(() => {
104. this.createSubWindow()
105. })
106. Button(){
107. Text('destroySubWindow')
108. .fontSize(24)
109. .fontWeight(FontWeight.Normal)
110. }.width(220).height(68)
111. .margin({left:10, top:60})
112. .onClick(() => {
113. this.destroySubWindow()
114. })
115. }
116. .width('100%')
117. }
118. .height('100%')
119. }
120. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArkUIWindowSamples/CreateSubWindow2/entry/src/main/ets/pages/Index.ets#L15-L136)

```
1. // subWindow.ets
2. @Entry
3. @Component
4. struct SubWindow {
5. @State message: string = 'Hello subWindow';
6. build() {
7. Row() {
8. Column() {
9. Text(this.message)
10. .fontSize(20)
11. .fontWeight(FontWeight.Bold)
12. }
13. .width('100%')
14. }
15. .height('100%')
16. .backgroundColor('#0D9FFB')
17. }
18. }
```

[SubWindow.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArkUIWindowSamples/CreateSubWindow2/entry/src/main/ets/pages/SubWindow.ets#L16-L35)

## 体验窗口沉浸式能力

在看视频、玩游戏等场景下，用户往往希望隐藏状态栏、导航栏等不必要的系统窗口，从而获得更佳的沉浸式体验。此时可以借助窗口沉浸式能力（窗口沉浸式能力都是针对应用主窗口而言的），达到预期效果。从API version 10开始，沉浸式窗口默认配置为全屏大小并由组件模块控制布局，状态栏、导航栏背景颜色为透明，文字颜色为黑色；应用窗口调用setWindowLayoutFullScreen接口，设置为true表示由组件模块控制忽略状态栏、导航栏的沉浸式全屏布局，设置为false表示由组件模块控制避让状态栏、导航栏的非沉浸式全屏布局。

说明

当前沉浸式界面开发仅支持窗口级别的配置，暂不支持Page级别的配置。若有Page级别切换的需要，可以在页面生命周期开始，例如onPageShow中设置沉浸模式，然后在页面退出，例如onPageHide中恢复默认设置来实现。

### 开发步骤

1. 获取应用主窗口。

   通过getMainWindow接口获取应用主窗口。
2. 实现沉浸式效果。有以下两种方式：

   * 方式一：应用主窗口为全屏窗口时，调用setWindowSystemBarEnable接口，设置导航栏、状态栏不显示，从而达到沉浸式效果。
   * 方式二：调用setWindowLayoutFullScreen接口，设置应用主窗口为全屏布局；然后调用setWindowSystemBarProperties接口，设置导航栏、状态栏的透明度、背景/文字颜色以及高亮图标等属性，使之保持与主窗口显示协调一致，从而达到沉浸式效果。
3. 加载显示沉浸式窗口的具体内容。

   通过loadContent接口加载沉浸式窗口的具体内容。

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. const DOMAIN = 0X0000;
7. const TAG: string = '[Sample_SetWindowSystemBarEnable]';

9. export default class EntryAbility extends UIAbility {
10. onWindowStageCreate(windowStage: window.WindowStage) {
11. // 1.获取应用主窗口。
12. let windowClass: window.Window | null = null;
13. windowStage.getMainWindow((err: BusinessError, data) => {
14. let errCode: number = err.code;
15. if (errCode) {
16. hilog.error(DOMAIN, TAG, `Failed to obtain the main window. Cause: ${JSON.stringify(err)}`);
17. return;
18. }
19. windowClass = data;
20. hilog.info(DOMAIN, TAG, `Succeeded in obtaining the main window. Data: ${JSON.stringify(data)}`);

22. // 2.实现沉浸式效果。方式一：设置导航栏、状态栏不显示。
23. let names: 'status'[] | 'navigation'[] = [];
24. windowClass.setWindowSystemBarEnable(names)
25. .then(() => {
26. hilog.info(DOMAIN, TAG, `Succeeded in setting the system bar to be visible.`);
27. })
28. .catch((err: BusinessError) => {
29. hilog.error(DOMAIN, TAG, `Failed to set the system bar to be visible. Cause: ${JSON.stringify(err)}`);
30. });
31. // 2.实现沉浸式效果。方式二：设置窗口为全屏布局，配合设置导航栏、状态栏的透明度、背景/文字颜色及高亮图标等属性，与主窗口显示保持协调一致。
32. let isLayoutFullScreen = true;
33. windowClass.setWindowLayoutFullScreen(isLayoutFullScreen)
34. .then(() => {
35. hilog.info(DOMAIN, TAG, `Succeeded in setting the window layout to full-screen mode.`);
36. })
37. .catch((err: BusinessError) => {
38. hilog.error(DOMAIN, TAG, `Failed to set the window layout to full-screen mode. Cause: ${JSON.stringify(err)}`);
39. });
40. let sysBarProps: window.SystemBarProperties = {
41. statusBarColor: '#ff00ff',
42. navigationBarColor: '#00ff00',
43. // 以下两个属性从API Version 8开始支持
44. statusBarContentColor: '#ffffff',
45. navigationBarContentColor: '#ffffff'
46. };
47. windowClass.setWindowSystemBarProperties(sysBarProps)
48. .then(() => {
49. hilog.info(DOMAIN, TAG, `Succeeded in setting the system bar properties.`);
50. })
51. .catch((err: BusinessError) => {
52. hilog.error(DOMAIN, TAG, `Failed to set the system bar properties. Cause: ${JSON.stringify(err)}`);
53. });
54. })
55. // 3.为沉浸式窗口加载对应的目标页面。
56. windowStage.loadContent('pages/Index', (err: BusinessError) => {
57. let errCode: number = err.code;
58. if (errCode) {
59. hilog.error(DOMAIN, TAG, `Failed to load the content. Cause: ${JSON.stringify(err)}`);
60. return;
61. }
62. hilog.info(DOMAIN, TAG, `Succeeded in loading the content.`);
63. });
64. }
65. };
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArkUIWindowSamples/SetWindowSystemBarEnable/entry/src/main/ets/entryability/EntryAbility.ets#L16-L82)

## 设置全局悬浮窗（受限开放）

全局悬浮窗可以在已有的任务基础上，创建一个始终在前台显示的窗口。即使创建全局悬浮窗的任务退至后台，全局悬浮窗仍然可以在前台显示。通常全局悬浮窗位于所有应用窗口之上，开发者可以创建全局悬浮窗，并对全局悬浮窗进行属性设置等操作。

### 开发步骤

**前提条件：** 创建WindowType.TYPE\_FLOAT即全局悬浮窗类型的窗口，需要申请ohos.permission.SYSTEM\_FLOAT\_WINDOW权限，该权限为受控开放权限，仅符合[指定场景](restricted-permissions.md#ohospermissionsystem_float_window)的在2in1设备上的应用可申请该权限。申请方式请参考：[申请使用受限权限](declare-permissions-in-acl.md)。

在其他设备或场景下，请使用画中画功能，使用方式参考：[画中画开发指导](window-pipwindow.md)。

注意

如果应用未在AppGallery Connect申请相应的权限证书，却试图在配置文件中声明此类权限，将会导致应用安装失败。

1. 创建全局悬浮窗。

   通过window.createWindow接口创建全局悬浮窗类型的窗口。
2. 对全局悬浮窗进行属性设置等操作。

   全局悬浮窗窗口创建成功后，可以改变其大小、位置等，还可以根据应用需要设置全局悬浮窗背景色、亮度等属性。
3. 加载显示全局悬浮窗的具体内容。

   通过setUIContent和showWindow接口加载显示全局悬浮窗的具体内容。
4. 销毁全局悬浮窗。

   当不再需要全局悬浮窗时，可根据具体实现逻辑，使用destroyWindow接口销毁全局悬浮窗。

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. const DOMAIN = 0X0000;
7. const TAG: string = '[Sample_CreatFloatWindow]';

9. export default class EntryAbility extends UIAbility {
10. onWindowStageCreate(windowStage: window.WindowStage) {
11. // 1.创建悬浮窗。
12. let windowClass: window.Window | null = null;
13. let config: window.Configuration = {
14. name: 'floatWindow', windowType: window.WindowType.TYPE_FLOAT, ctx: this.context
15. };
16. window.createWindow(config, (err: BusinessError, data) => {
17. let errCode: number = err.code;
18. if (errCode) {
19. hilog.error(DOMAIN, TAG, `Failed to create the floatWindow. Cause: ${JSON.stringify(err)}`);
20. return;
21. }
22. hilog.info(DOMAIN, TAG, `Succeeded in creating the floatWindow. Data: ${JSON.stringify(data)}`);
23. windowClass = data;
24. // 2.悬浮窗窗口创建成功后，设置悬浮窗的位置、大小及相关属性等。
25. windowClass.moveWindowTo(300, 300, (err: BusinessError) => {
26. let errCode: number = err.code;
27. if (errCode) {
28. hilog.error(DOMAIN, TAG, `Failed to move the window. Cause: ${JSON.stringify(err)}`);
29. return;
30. }
31. hilog.info(DOMAIN, TAG, `Succeeded in moving the window.`);
32. });
33. windowClass.resize(500, 500, (err: BusinessError) => {
34. let errCode: number = err.code;
35. if (errCode) {
36. hilog.error(DOMAIN, TAG, `Failed to change the window size. Cause: ${JSON.stringify(err)}`);
37. return;
38. }
39. hilog.info(DOMAIN, TAG, `Succeeded in changing the window size.`);
40. });
41. // 3.为悬浮窗加载对应的目标页面。
42. windowClass.setUIContent('pages/Index', (err: BusinessError) => {
43. let errCode: number = err.code;
44. if (errCode) {
45. hilog.error(DOMAIN, TAG, `Failed to load the content. Cause: ${JSON.stringify(err)}`);
46. return;
47. }
48. hilog.info(DOMAIN, TAG, `Succeeded in loading the content.`);
49. // 3.显示悬浮窗。
50. (windowClass as window.Window).showWindow((err: BusinessError) => {
51. let errCode: number = err.code;
52. if (errCode) {
53. hilog.error(DOMAIN, TAG, `Failed to show the window. Cause: ${JSON.stringify(err)}`);
54. return;
55. }
56. hilog.info(DOMAIN, TAG, `Succeeded in showing the window.`);
57. });
58. });
59. // 4.销毁悬浮窗。当不再需要悬浮窗时，可根据具体实现逻辑，使用destroy对其进行销毁。
60. });
61. }
62. };
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArkUIWindowSamples/CreateFloatWindow/entry/src/main/ets/entryability/EntryAbility.ets#L16-L79)

## 监听窗口不可交互与可交互事件

应用在前台显示过程中可能会进入某些不可交互的场景，比较典型的是进入多任务界面。此时，对于一些应用可能需要选择暂停某个与用户正在交互的业务，如视频类应用暂停正在播放的视频或者相机暂停预览流等。而当该应用从多任务又切回前台时，又变成了可交互的状态，此时需要恢复被暂停中断的业务，如恢复视频播放或相机预览流等。

### 开发步骤

在创建WindowStage对象后可通过监听'windowStageEvent'事件类型，监听到窗口进入前台、后台、前台可交互、前台不可交互等事件，应用可根据这些上报的事件状态进行相应的业务处理。

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const DOMAIN = 0X0000;
6. const TAG: string = '[Sample_ListenWindowStage]';

8. export default class EntryAbility extends UIAbility {
9. onWindowStageCreate(windowStage: window.WindowStage) {
10. // ...
11. try {
12. windowStage.on('windowStageEvent', (data) => {
13. hilog.info(DOMAIN, TAG, `Succeeded in enabling the listener for window stage event changes. Data: ${JSON.stringify(data)}`);

15. // 根据事件状态类型选择进行相应的处理
16. if (data === window.WindowStageEventType.SHOWN) {
17. hilog.info(DOMAIN, TAG, `current window stage event is SHOWN`);
18. // 应用进入前台，默认为可交互状态
19. // ...
20. } else if (data === window.WindowStageEventType.HIDDEN) {
21. hilog.info(DOMAIN, TAG, `current window stage event is HIDDEN`);
22. // 应用进入后台，默认为不可交互状态
23. // ...
24. } else if (data === window.WindowStageEventType.PAUSED) {
25. hilog.info(DOMAIN, TAG, `current window stage event is PAUSED`);
26. // 前台应用进入多任务，转为不可交互状态
27. // ...
28. } else if (data === window.WindowStageEventType.RESUMED) {
29. hilog.info(DOMAIN, TAG, `current window stage event is RESUMED`);
30. // 进入多任务后又继续返回前台时，恢复可交互状态
31. // ...
32. }

34. // ...
35. });
36. } catch (exception) {
37. hilog.error(DOMAIN, TAG, `Failed to enable the listener for window stage event changes. Cause: ${JSON.stringify(exception)}`);
38. }
39. }
40. }
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArkUIWindowSamples/ListenWindowStage/entry/src/main/ets/entryability/EntryAbility.ets#L16-L65)
