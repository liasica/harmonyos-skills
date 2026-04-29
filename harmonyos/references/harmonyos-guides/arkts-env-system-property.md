---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-env-system-property
title: @Env：环境变量
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习响应式环境变量 > @Env：环境变量
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:35+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:b0d37be43466be78ba9cb079d44156e7dbe2c4a284811d615deaf0562a105ab1
---

在多设备开发的场景中，开发者可以使用[@Env](../harmonyos-references/ts-env-system-property.md)装饰器监听系统环境变量的改变，并根据系统环境变量来进行相应的场景判断，以减少不同设备间的适配逻辑和重复开发。

说明

从API version 22开始，@Env支持在[@Component](arkts-create-custom-components.md#component)和[@ComponentV2](arkts-create-custom-components.md#componentv2)中使用。

从API version 22开始，该装饰器支持在元服务中使用。

## 概述

@Env是响应式系统环境变量装饰器，其功能包括：

* 根据入参读取相应的环境变量信息，详情见[@Env支持参数](arkts-env-system-property.md#env支持参数)。目前支持以下几种环境变量：
  + [SystemProperties.BREAK\_POINT](../harmonyos-references/ts-env-system-property.md#systemproperties)，用于获取窗口不同宽高阈值下对应的断点值信息。
  + [SystemProperties.WINDOW\_SIZE23+](../harmonyos-references/ts-env-system-property.md#systemproperties)，用于获取窗口的大小信息，单位为vp。
  + [SystemProperties.WINDOW\_SIZE\_PX23+](../harmonyos-references/ts-env-system-property.md#systemproperties)，用于获取窗口的大小信息，单位为px。
  + [SystemProperties.WINDOW\_AVOID\_AREA23+](../harmonyos-references/ts-env-system-property.md#systemproperties)，用于获取窗口的避让区域信息，单位为vp。
  + [SystemProperties.WINDOW\_AVOID\_AREA\_PX23+](../harmonyos-references/ts-env-system-property.md#systemproperties)，用于获取窗口的避让区域信息，单位为px。
* 系统环境变量改变时，通知@Env装饰的变量更新，并触发@Env关联组件刷新，以实现界面内容的同步更新。
* @Env装饰的变量不允许开发者初始化。@Env会返回给开发者可观察的环境变量类（由[@ObservedV2](arkts-new-observedv2-and-trace.md)装饰，且其由属性[@Trace](arkts-new-observedv2-and-trace.md)装饰）的实例。开发者如果想监听环境变量的变化，可以使用[addMonitor](arkts-new-addmonitor-clearmonitor.md)，具体示例见[在@ComponentV2中使用@Env](arkts-env-system-property.md#在componentv2中使用env)。

## @Env支持参数

@Env支持的参数请参考[SystemProperties枚举类型说明](../harmonyos-references/ts-env-system-property.md#systemproperties)。

## @Env和Environment能力对比

@Env和[Environment](arkts-environment.md)都是系统环境变量相关，但两者能力有较大的不同，具体能力对比见下表。

| 能力 | @Env | Environment |
| --- | --- | --- |
| 起始API version | 从API version 22开始支持。 | 从API version 7开始支持。 |
| 支持参数 | [SystemProperties的枚举值](../harmonyos-references/ts-env-system-property.md#systemproperties) | 支持languageCode等参数，详情见[Environment内置参数](arkts-environment.md#environment内置参数)。 |
| 使用形式 | @Env为装饰器，可声明在@Component或@ComponentV2中，获取对应参数的环境变量信息。 | 通过[envProp](../harmonyos-references/ts-state-management.md#envprop10)等接口获取当前应用的环境变量，并存入[AppStorage](arkts-appstorage.md)中，开发者可通过AppStorage的接口访问系统环境变量的值，具体例子见[从ui中访问environment参数](arkts-environment.md#从ui中访问environment参数)。 |
| 是否有响应式能力 | 有，当系统环境变量变化时，会通知@Env装饰的环境变量的改变，并通知@Env关联组件刷新。 | 无，系统环境变量变化时，不会通知Environment改变。 |

## 限制条件

* @Env仅支持在@Component和@ComponentV2中使用，否则会有编译时报错。如果开发者绕过编译时检查，则会有运行时报错。

  ```
  1. import { uiObserver } from '@kit.ArkUI';

  3. class Info {
  4. @Env(SystemProperties.BREAK_POINT) breakpoint: uiObserver.WindowSizeLayoutBreakpointInfo; // 错误用法，编译时报错
  5. }

  7. @Entry
  8. @Component
  9. struct Index {
  10. @Env(SystemProperties.BREAK_POINT) breakpoint: uiObserver.WindowSizeLayoutBreakpointInfo; // 正确用法

  12. build() {
  13. }
  14. }
  ```
* @Env装饰的变量为只读属性，不允许开发者进行初始化或赋值操作，否则会有编译时报错。如果开发者绕过编译时检查，则会有运行时报错。

  ```
  1. import { uiObserver } from '@kit.ArkUI';

  3. @Entry
  4. @Component
  5. struct Index {
  6. @Env(SystemProperties.BREAK_POINT) breakpoint: uiObserver.WindowSizeLayoutBreakpointInfo =
  7. new uiObserver.WindowSizeLayoutBreakpointInfo(); // 错误用法，编译时报错

  9. build() {
  10. Column() {
  11. Text(`breakpoint height ${this.breakpoint.heightBreakpoint}`).fontSize(20)
  12. Text(`breakpoint width ${this.breakpoint.widthBreakpoint}`).fontSize(20)
  13. Button('change breakpoint').onClick(() => {
  14. this.breakpoint = new uiObserver.WindowSizeLayoutBreakpointInfo(); // 错误用法，编译时报错
  15. })
  16. }
  17. }
  18. }
  ```
* @Env当前支持[SystemProperties的枚举值](../harmonyos-references/ts-env-system-property.md#systemproperties)。若使用不支持的参数，将触发编译时报错。

  ```
  1. import { uiObserver } from '@kit.ArkUI';

  3. @Entry
  4. @Component
  5. struct Index {
  6. @Env(SystemProperties.BREAK_POINT) breakpoint1: uiObserver.WindowSizeLayoutBreakpointInfo; // 正确写法
  7. @Env('unsupported_key') breakpoint2: uiObserver.WindowSizeLayoutBreakpointInfo; // 错误写法，@Env非法入参，编译时报错。

  9. build() {
  10. Text(`breakpoint2 width: ${this.breakpoint2.widthBreakpoint} height: ${this.breakpoint2.heightBreakpoint}`)
  11. }
  12. }
  ```
* @Env使用不同的key值时，装饰的变量类型必须一一对应，否则会有编译时报错。

  + @Env使用SystemProperties.BREAK\_POINT时，装饰的变量类型必须为uiObserver.WindowSizeLayoutBreakpointInfo类型。
  + @Env使用SystemProperties.WINDOW\_SIZE时，装饰的变量类型必须为window.SizeInVP类型。
  + @Env使用SystemProperties.WINDOW\_SIZE\_PX时，装饰的变量类型必须为window.Size类型。
  + @Env使用SystemProperties.WINDOW\_AVOID\_AREA时，装饰的变量类型必须为window.UIEnvWindowAvoidAreaInfoVP类型。
  + @Env使用SystemProperties.WINDOW\_AVOID\_AREA\_PX时，装饰的变量类型必须为window.UIEnvWindowAvoidAreaInfoPX类型。

  ```
  1. import { uiObserver } from '@kit.ArkUI';

  3. @Entry
  4. @Component
  5. struct Index {
  6. @Env(SystemProperties.BREAK_POINT) breakpoint1: uiObserver.WindowSizeLayoutBreakpointInfo; // 正确写法
  7. @Env(SystemProperties.BREAK_POINT) breakpoint2: string; // 错误写法，@Env使用SystemProperties.BREAK_POINT时仅支持装饰WindowSizeLayoutBreakpointInfo类型

  9. build() {
  10. }
  11. }
  ```
* @Env只能单独使用，不能和其他V1V2状态变量装饰器或@Require联用，否则会有编译时报错。

  ```
  1. @Env(SystemProperties.BREAK_POINT) breakpoint1: uiObserver.WindowSizeLayoutBreakpointInfo; // 正确写法
  2. @State @Env(SystemProperties.BREAK_POINT) breakpoint2: uiObserver.WindowSizeLayoutBreakpointInfo; // 错误写法，编译时报错
  3. @Require @Env(SystemProperties.BREAK_POINT) breakpoint3: uiObserver.WindowSizeLayoutBreakpointInfo; // 错误写法，编译时报错
  4. @Local @Env(SystemProperties.BREAK_POINT) breakpoint4: uiObserver.WindowSizeLayoutBreakpointInfo; // 错误写法，编译时报错
  ```
* @Env装饰的变量在@Component和@ComponentV2传递遵循以下规则：

  + @Env装饰的变量仅能用于初始化@ComponentV2中@Param装饰的变量，否则会有编译时报错。
  + @Env装饰的变量仅能用于初始化@Component中常规变量，否则会有编译时报错。需要注意，通过[BuilderNode](../harmonyos-references/js-apis-arkui-buildernode.md)切换窗口，会导致@Env依据新的窗口更新环境变量实例。在切换窗口的场景中，不建议开发者使用@Env变量来初始化子组件的常规变量，否则会造成该常规变量无法被@Env通知触发其关联UI组件刷新。具体示例可见[通过BuilderNode切换窗口](arkts-env-system-property.md#通过buildernode切换窗口)。

  ```
  1. import { uiObserver } from '@kit.ArkUI';

  3. @Entry
  4. @Component
  5. struct Index {
  6. @Env(SystemProperties.BREAK_POINT) breakpoint: uiObserver.WindowSizeLayoutBreakpointInfo; // 正确写法

  8. build() {
  9. Column() {
  10. CompV2({ breakpoint: this.breakpoint }) // 正确写法
  11. Comp({ breakpoint: this.breakpoint }) // 正确写法

  13. CompV2Invalid({ breakpoint: this.breakpoint }) // 错误写法，@Env装饰的变量仅能初始化V2的@Param变量
  14. CompInvalid({ breakpoint: this.breakpoint }) // 错误写法，@Env装饰的变量仅能初始化V1的常规变量
  15. }
  16. }
  17. }

  19. @ComponentV2
  20. struct CompV2 {
  21. @Require @Param breakpoint: uiObserver.WindowSizeLayoutBreakpointInfo; // 正确写法

  23. build() {
  24. }
  25. }

  27. @ComponentV2
  28. struct CompV2Invalid {
  29. @Require breakpoint: uiObserver.WindowSizeLayoutBreakpointInfo; // 错误写法

  31. build() {
  32. }
  33. }

  35. @Component
  36. struct Comp {
  37. @Require breakpoint: uiObserver.WindowSizeLayoutBreakpointInfo; // 正确写法

  39. build() {
  40. }
  41. }

  43. @Component
  44. struct CompInvalid {
  45. @ObjectLink breakpoint: uiObserver.WindowSizeLayoutBreakpointInfo; // 错误写法

  47. build() {
  48. }
  49. }
  ```

## @Env初始化流程

@Env变量不允许开发者初始化，其值由框架根据当前窗口的环境变量自动提供，@Env变量在被第一次读值的时候，会触发初始化。@Env变量初始化遵循以下流程：

1. 从父组件中查找已有实例：
   * 向上递归查找父组件。
   * 如果某个父组件在同一窗口中已经初始化过相同key的@Env变量，则直接复用该实例。
   * 若未找到，则继续向上查找，直到父组件为空。需要注意，向上查找父组件的流程会被BuilderNode打断。
2. 查找当前窗口的@Env实例。
   * 如果在父组件中未找到对应的实例，则检查当前窗口是否已有相同key的@Env变量实例。
   * 如存在，则复用该窗口内的@Env实例。
3. 首次请求：创建新环境变量实例。
   * 若以上两步都无法得到实例，则说明当前窗口第一次读取该环境变量。
   * 框架会创建一个新的可观察环境变量实例并与当前窗口绑定，然后完成初始化。

流程图如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/-Euf2zUNQ2W0jIwDFYA83A/zh-cn_image_0000002589243973.png?HW-CC-KV=V1&HW-CC-Date=20260429T052734Z&HW-CC-Expire=86400&HW-CC-Sign=A214291342B81F1B3CE23F9D6756A07A4D6F99A1DFF0A5E6B58DD7BDCEBE7F42)

基于上面流程，下面的示例中以@Env使用SystemProperties.BREAK\_POINT为例，各个组件中的初始化如下图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/WZchCLX-R3WscL2Wsi6pXQ/zh-cn_image_0000002558764166.png?HW-CC-KV=V1&HW-CC-Date=20260429T052734Z&HW-CC-Expire=86400&HW-CC-Sign=F11F5A72E558B672E6DDE942B9C38F5B94DA504DFACE5F0AD14500D81C29CF0F)

1. Child1初始化@Env(SystemProperties.BREAK\_POINT)：
   * 递归查找直到父组件为空：向上查找父组件Index，没有@Env对应的SystemProperties.BREAK\_POINT实例。
   * 查找当前窗口：没有@Env对应的SystemProperties.BREAK\_POINT实例。
   * 创建SystemProperties.BREAK\_POINT对应的可观察的环境变量实例，并和当前窗口绑定。
2. GrandChild1初始化@Env(SystemProperties.BREAK\_POINT)：
   * 递归查找父组件，直到父组件为空：向上查找父组件Child1，查找到Child1有@Env对应的SystemProperties.BREAK\_POINT实例。
   * 复用Child1中@Env对应的SystemProperties.BREAK\_POINT实例。
3. GrandChild2初始化@Env(SystemProperties.BREAK\_POINT)：
   * 递归查找直到父组件为空：向上查找父组件Child2和祖先节点Index，均没有@Env对应的SystemProperties.BREAK\_POINT实例。
   * 查找当前窗口：有@Env对应的SystemProperties.BREAK\_POINT实例。
   * 复用窗口中SystemProperties.BREAK\_POINT对应的环境变量实例。

```
1. import { uiObserver } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. build() {
7. Column() {
8. Text(`Index`)
9. Child1()
10. Child2()
11. }
12. .height('100%')
13. .width('100%')
14. }
15. }

17. @Component
18. struct Child1 {
19. // @Env读取系统环境变量
20. @Env(SystemProperties.BREAK_POINT) breakpoint: uiObserver.WindowSizeLayoutBreakpointInfo;

22. build() {
23. Column() {
24. Text(`Child1 breakpoint width: ${this.breakpoint.widthBreakpoint}`).fontSize(20)
25. Text(`Child1 breakpoint height: ${this.breakpoint.heightBreakpoint}`).fontSize(20)
26. GrandChild1()
27. }
28. }
29. }

31. @Component
32. struct Child2 {
33. build() {
34. Column() {
35. GrandChild2()
36. }
37. }
38. }

40. @Component
41. struct GrandChild1 {
42. @Env(SystemProperties.BREAK_POINT) breakpoint: uiObserver.WindowSizeLayoutBreakpointInfo;

44. build() {
45. Column() {
46. Text(`GrandChild1 breakpoint width: ${this.breakpoint.widthBreakpoint}`).fontSize(20)
47. Text(`GrandChild1 breakpoint height: ${this.breakpoint.heightBreakpoint}`).fontSize(20)
48. }
49. }
50. }

53. @Component
54. struct GrandChild2 {
55. @Env(SystemProperties.BREAK_POINT) breakpoint: uiObserver.WindowSizeLayoutBreakpointInfo;

57. build() {
58. Column() {
59. Text(`GrandChild2 breakpoint width: ${this.breakpoint.widthBreakpoint}`).fontSize(20)
60. Text(`GrandChild2 breakpoint height: ${this.breakpoint.heightBreakpoint}`).fontSize(20)
61. }
62. }
63. }
```

## 使用场景

### 在@ComponentV2中使用@Env

下面的例子中：

* 在@ComponentV2中声明@Env，获取当前@ComponentV2组件创建时所在窗口尺寸的布局断点信息，并用[addMonitor](arkts-new-addmonitor-clearmonitor.md)监听this.breakpoint的属性的变化。
* 在@ComponentV2中声明@Env，获取当前@ComponentV2组件创建时所在窗口的大小信息，单位为vp，并用[addMonitor](arkts-new-addmonitor-clearmonitor.md)监听this.sizeInVP的属性的变化。
* 在@ComponentV2中声明@Env，获取当前@ComponentV2组件创建时所在窗口的大小信息，单位为px，并用[addMonitor](arkts-new-addmonitor-clearmonitor.md)监听this.sizeInPX的属性的变化。
* 将@Env装饰的变量传递给CompV2中[@Param](arkts-new-param.md)装饰的变量和Comp中的常规变量。
* 点击Button('Landscape')和Button('Portrait')切换横竖屏，Index、CompV2和Comp关联组件进行对应的刷新，orientationChange被触发监听回调。

```
1. import { uiObserver, UIUtils, window } from '@kit.ArkUI';
2. import { common } from '@kit.AbilityKit';

4. @Entry
5. @ComponentV2
6. struct Index {
7. @Env(SystemProperties.BREAK_POINT) breakpoint: uiObserver.WindowSizeLayoutBreakpointInfo;
8. @Env(SystemProperties.WINDOW_SIZE) sizeInVP: window.SizeInVP;
9. @Env(SystemProperties.WINDOW_SIZE_PX) sizeInPX: window.Size;

11. private changeOrientation(isLandscape: boolean) {
12. const context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
13. window.getLastWindow(context).then((lastWindow) => {
14. lastWindow.setPreferredOrientation(isLandscape ? window.Orientation.LANDSCAPE : window.Orientation.PORTRAIT);
15. });
16. }

18. orientationChange(mon: IMonitor) {
19. mon.dirty.forEach((path: string) => {
20. console.info(`${path} changes from ${mon.value(path)?.before} to ${mon.value(path)?.now}`);
21. })
22. }

24. aboutToAppear(): void {
25. // @Env返回的对象实际上是@ObservedV2装饰的对象（其属性是@Trace装饰的），所以其属性的改变可以通过addMonitor监听
26. UIUtils.addMonitor(this.breakpoint, ['widthBreakpoint', 'heightBreakpoint'], this.orientationChange);
27. UIUtils.addMonitor(this.sizeInVP, ['width', 'height'], this.orientationChange);
28. UIUtils.addMonitor(this.sizeInPX, ['width', 'height'], this.orientationChange);
29. }

31. build() {
32. Column() {
33. Text(`Index breakpoint width: ${this.breakpoint.widthBreakpoint}`).fontSize(20)
34. Text(`Index breakpoint height: ${this.breakpoint.heightBreakpoint}`).fontSize(20)
35. Text(`Index sizeInVP width: ${this.sizeInVP.width}`).fontSize(20)
36. Text(`Index sizeInVP height: ${this.sizeInVP.height}`).fontSize(20)
37. Text(`Index sizeInPX width: ${this.sizeInPX.width}`).fontSize(20)
38. Text(`Index sizeInPX height: ${this.sizeInPX.height}`).fontSize(20)

40. Button('Landscape').onClick(() => {
41. this.changeOrientation(true);
42. })

44. Button('Portrait').onClick(() => {
45. this.changeOrientation(false);
46. })

48. CompV2({ breakpoint: this.breakpoint, sizeInVP: this.sizeInVP, sizeInPX: this.sizeInPX })
49. Comp({ breakpoint: this.breakpoint, sizeInVP: this.sizeInVP, sizeInPX: this.sizeInPX })
50. }
51. }
52. }

54. @ComponentV2
55. struct CompV2 {
56. @Require @Param breakpoint: uiObserver.WindowSizeLayoutBreakpointInfo;
57. @Require @Param sizeInVP: window.SizeInVP;
58. @Require @Param sizeInPX: window.Size;

60. build() {
61. Column() {
62. Text(`CompV2 breakpoint width: ${this.breakpoint.widthBreakpoint}`).fontSize(20)
63. Text(`CompV2 breakpoint height: ${this.breakpoint.heightBreakpoint}`).fontSize(20)
64. Text(`CompV2 sizeInVP width: ${this.sizeInVP.width}`).fontSize(20)
65. Text(`CompV2 sizeInVP height: ${this.sizeInVP.height}`).fontSize(20)
66. Text(`CompV2 sizeInPX width: ${this.sizeInPX.width}`).fontSize(20)
67. Text(`CompV2 sizeInPX height: ${this.sizeInPX.height}`).fontSize(20)
68. }
69. }
70. }

72. @Component
73. struct Comp {
74. @Require breakpoint: uiObserver.WindowSizeLayoutBreakpointInfo;
75. @Require sizeInVP: window.SizeInVP;
76. @Require sizeInPX: window.Size;

78. build() {
79. Column() {
80. Text(`Comp breakpoint width: ${this.breakpoint.widthBreakpoint}`).fontSize(20)
81. Text(`Comp breakpoint height: ${this.breakpoint.heightBreakpoint}`).fontSize(20)
82. Text(`Comp sizeInVP width: ${this.sizeInVP.width}`).fontSize(20)
83. Text(`Comp sizeInVP height: ${this.sizeInVP.height}`).fontSize(20)
84. Text(`Comp sizeInPX width: ${this.sizeInPX.width}`).fontSize(20)
85. Text(`Comp sizeInPX height: ${this.sizeInPX.height}`).fontSize(20)
86. }
87. }
88. }
```

### 在@Component中使用@Env

@Env在@Component中使用和其在@ComponentV2中使用类似，示例如下。

```
1. import { uiObserver, UIUtils, window } from '@kit.ArkUI';
2. import { common } from '@kit.AbilityKit';

4. @Entry
5. @Component
6. struct Index {
7. @Env(SystemProperties.BREAK_POINT) breakpoint: uiObserver.WindowSizeLayoutBreakpointInfo;
8. @Env(SystemProperties.WINDOW_SIZE) sizeInVP: window.SizeInVP;
9. @Env(SystemProperties.WINDOW_SIZE_PX) sizeInPX: window.Size;

11. private changeOrientation(isLandscape: boolean) {
12. const context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
13. window.getLastWindow(context).then((lastWindow) => {
14. lastWindow.setPreferredOrientation(isLandscape ? window.Orientation.LANDSCAPE : window.Orientation.PORTRAIT);
15. });
16. }

18. orientationChange(mon: IMonitor) {
19. mon.dirty.forEach((path: string) => {
20. console.info(`${path} changes from ${mon.value(path)?.before} to ${mon.value(path)?.now}`);
21. })
22. }

24. aboutToAppear(): void {
25. // @Env返回的对象实际上是@ObservedV2装饰的对象（其属性是@Trace装饰的），所以其属性的改变可以通过addMonitor监听
26. UIUtils.addMonitor(this.breakpoint, ['widthBreakpoint', 'heightBreakpoint'], this.orientationChange);
27. UIUtils.addMonitor(this.sizeInVP, ['width', 'height'], this.orientationChange);
28. UIUtils.addMonitor(this.sizeInPX, ['width', 'height'], this.orientationChange);
29. }

31. build() {
32. Column() {
33. Text(`Index breakpoint width: ${this.breakpoint.widthBreakpoint}`).fontSize(20)
34. Text(`Index breakpoint height: ${this.breakpoint.heightBreakpoint}`).fontSize(20)
35. Text(`Index sizeInVP width: ${this.sizeInVP.width}`).fontSize(20)
36. Text(`Index sizeInVP height: ${this.sizeInVP.height}`).fontSize(20)
37. Text(`Index sizeInPX width: ${this.sizeInPX.width}`).fontSize(20)
38. Text(`Index sizeInPX height: ${this.sizeInPX.height}`).fontSize(20)

40. Button('Landscape').onClick(() => {
41. this.changeOrientation(true);
42. })

44. Button('Portrait').onClick(() => {
45. this.changeOrientation(false);
46. })

48. CompV2({ breakpoint: this.breakpoint, sizeInVP: this.sizeInVP, sizeInPX: this.sizeInPX })
49. Comp({ breakpoint: this.breakpoint, sizeInVP: this.sizeInVP, sizeInPX: this.sizeInPX })
50. }
51. }
52. }

54. @ComponentV2
55. struct CompV2 {
56. @Require @Param breakpoint: uiObserver.WindowSizeLayoutBreakpointInfo;
57. @Require @Param sizeInVP: window.SizeInVP;
58. @Require @Param sizeInPX: window.Size;

60. build() {
61. Column() {
62. Text(`CompV2 breakpoint width: ${this.breakpoint.widthBreakpoint}`).fontSize(20)
63. Text(`CompV2 breakpoint height: ${this.breakpoint.heightBreakpoint}`).fontSize(20)
64. Text(`CompV2 sizeInVP width: ${this.sizeInVP.width}`).fontSize(20)
65. Text(`CompV2 sizeInVP height: ${this.sizeInVP.height}`).fontSize(20)
66. Text(`CompV2 sizeInPX width: ${this.sizeInPX.width}`).fontSize(20)
67. Text(`CompV2 sizeInPX height: ${this.sizeInPX.height}`).fontSize(20)
68. }
69. }
70. }

72. @Component
73. struct Comp {
74. @Require breakpoint: uiObserver.WindowSizeLayoutBreakpointInfo;
75. @Require sizeInVP: window.SizeInVP;
76. @Require sizeInPX: window.Size;

78. build() {
79. Column() {
80. Text(`Comp breakpoint width: ${this.breakpoint.widthBreakpoint}`).fontSize(20)
81. Text(`Comp breakpoint height: ${this.breakpoint.heightBreakpoint}`).fontSize(20)
82. Text(`Comp sizeInVP width: ${this.sizeInVP.width}`).fontSize(20)
83. Text(`Comp sizeInVP height: ${this.sizeInVP.height}`).fontSize(20)
84. Text(`Comp sizeInPX width: ${this.sizeInPX.width}`).fontSize(20)
85. Text(`Comp sizeInPX height: ${this.sizeInPX.height}`).fontSize(20)
86. }
87. }
88. }
```

### 通过BuilderNode切换窗口

@Env用于展示@Component/@ComponentV2所在[窗口](../harmonyos-references/arkts-apis-window-window.md)的环境变量信息。开发者通过BuilderNode切换@Component@ComponentV2所在的窗口实例时，@Env会根据新的窗口获取对应的环境变量信息，并触发关联的UI组件刷新。以SystemProperties.BREAK\_POINT为例。

在下面的示例中：

1. 点击Button('add node to tree')，创建BuilderNode节点挂载到NodeContainer下。
2. 点击Button('remove node from tree')，将BuilderNode节点从NodeContainer上移除。
3. 点击Button(`create sub window`)，创建子窗并显示SubWindow窗口。
4. 点击SubWindow窗口内的Button('add node to tree')，将BuilderNode节点重新挂载到SubWindow内的NodeContainer下。
   * ComponentUnderBuilderNode在被挂载到新的窗口下时，会触发@Env重新获取新的环境变量。
   * @Env重新获取新的环境变量后，触发其关联组件的刷新。其中ComponentUnderBuilderNode中@Env(SystemProperties.BREAK\_POINT) breakpoint: uiObserver.WindowSizeLayoutBreakpointInfo会通知CompV2内的@Param breakpoint刷新，但是并不会通知Comp内的常规变量breakpoint触发UI刷新。所以在切换窗口，@Env重新获取环境变量的场景下，建议开发者不要将@Env传递给常规变量，以避免常规变量不能被通知UI刷新的问题。

下面的示例包含了创建子窗的流程，具体可参考[管理应用窗口（Stage模型）](application-window-stage.md)。

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { window } from '@kit.ArkUI';

6. const DOMAIN = 0x0000;

8. export default class EntryAbility extends UIAbility {
9. onWindowStageCreate(windowStage: window.WindowStage) {
10. windowStage.loadContent('pages/Index', (err) => {
11. if (err.code) {
12. hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
13. return;
14. }
15. hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
16. })

18. // 给Index页面传递windowStage
19. AppStorage.setOrCreate('windowStage', windowStage);
20. }
21. }
```

```
1. // Index.ets
2. import { BuilderNode, FrameNode, NodeController, uiObserver, window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. const DOMAIN = 0x0000;

8. let windowStage_: window.WindowStage | undefined = undefined;
9. let sub_windowClass: window.Window | undefined = undefined;
10. let globalBuilderNode: BuilderNode<[]> | undefined = undefined;

12. export class MyNodeController extends NodeController {
13. private rootNode: FrameNode | null = null;
14. private uiContext: UIContext | null = null;

16. makeNode(uiContext: UIContext): FrameNode | null {
17. this.rootNode = new FrameNode(uiContext);
18. this.uiContext = uiContext;
19. return this.rootNode;
20. }

22. addBuilderNode(): void {
23. if (!globalBuilderNode && this.uiContext) {
24. globalBuilderNode = new BuilderNode(this.uiContext);
25. globalBuilderNode.build(wrapBuilder<[]>(buildComponent), undefined);
26. }
27. if (this.rootNode && globalBuilderNode) {
28. this.rootNode.appendChild(globalBuilderNode.getFrameNode());
29. }
30. }

32. removeBuilderNode(): void {
33. if (this.rootNode && globalBuilderNode) {
34. this.rootNode.removeChild(globalBuilderNode.getFrameNode());
35. }
36. }

38. disposeNode(): void {
39. if (this.rootNode && globalBuilderNode) {
40. globalBuilderNode.dispose();
41. globalBuilderNode = undefined;
42. }
43. }
44. }

46. @Builder
47. function buildComponent() {
48. Column() {
49. ComponentUnderBuilderNode()
50. }
51. }

53. @Entry
54. @ComponentV2
55. struct Index {
56. private nodeController: MyNodeController = new MyNodeController();

58. private createSubWindow() {
59. windowStage_ = AppStorage.get('windowStage');
60. if (windowStage_ == null) {
61. hilog.error(DOMAIN, 'testTag', 'Failed to create the subwindow. Cause: windowStage_ is null');
62. } else {
63. // 创建应用子窗口。
64. windowStage_.createSubWindow('mySubWindow', (err: BusinessError, data) => {
65. let errCode: number = err.code;
66. if (errCode) {
67. hilog.error(DOMAIN, 'testTag', 'Failed to create the subwindow. Cause: ' + JSON.stringify(err));
68. return;
69. }
70. sub_windowClass = data;
71. if (!sub_windowClass) {
72. hilog.error(DOMAIN, 'testTag', 'sub_windowClass is null');
73. return;
74. }
75. hilog.info(DOMAIN, 'testTag', 'Succeeded in creating the subwindow. Data: ' + JSON.stringify(data));
76. // 子窗口创建成功后，设置子窗口的位置、大小及相关属性等。
77. sub_windowClass.moveWindowTo(200, 1300, (err: BusinessError) => {
78. let errCode: number = err.code;
79. if (errCode) {
80. hilog.error(DOMAIN, 'testTag', 'Failed to move the window. Cause:' + JSON.stringify(err));
81. return;
82. }
83. hilog.info(DOMAIN, 'testTag', 'Succeeded in moving the window.');
84. });
85. sub_windowClass.resize(900, 1800, (err: BusinessError) => {
86. let errCode: number = err.code;
87. if (errCode) {
88. hilog.error(DOMAIN, 'testTag', 'Failed to change the window size. Cause:' + JSON.stringify(err));
89. return;
90. }
91. hilog.info(DOMAIN, 'testTag', 'Succeeded in changing the window size.');
92. });
93. // 为子窗口加载对应的目标页面。
94. sub_windowClass.setUIContent('pages/SubWindow', (err: BusinessError) => {
95. let errCode: number = err.code;
96. if (errCode) {
97. hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause:' + JSON.stringify(err));
98. return;
99. }
100. hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
101. if (!sub_windowClass) {
102. hilog.error(DOMAIN, 'testTag', 'sub_windowClass is null');
103. return;
104. }
105. sub_windowClass.showWindow((err: BusinessError) => {
106. let errCode: number = err.code;
107. if (errCode) {
108. hilog.error(DOMAIN, 'testTag', 'Failed to show the window. Cause: ' + JSON.stringify(err));
109. return;
110. }
111. hilog.info(DOMAIN, 'testTag', 'Succeeded in showing the window.');
112. });
113. });
114. })
115. }
116. }

118. private destroySubWindow() {
119. if (!sub_windowClass) {
120. console.error('sub_windowClass is null');
121. return;
122. }
123. // 销毁子窗口。当不再需要子窗口时，可根据具体实现逻辑，使用destroy对其进行销毁。
124. sub_windowClass.destroyWindow((err: BusinessError) => {
125. let errCode: number = err.code;
126. if (errCode) {
127. console.error('Failed to destroy the window. Cause: ' + JSON.stringify(err));
128. return;
129. }
130. console.info('Succeeded in destroying the window.');
131. });
132. }

134. build() {
135. Column({ space: 10 }) {
136. Text(`Index`)
137. // 第一步：创建globalBuilderNode，并将globalBuilderNode下的节点挂在NodeContainer的占位节点下
138. Button('add node to tree').width(200).onClick(() => {
139. this.nodeController.addBuilderNode();
140. })
141. // 第二步：从NodeContainer的占位节点下移除globalBuilderNode下的节点
142. Button('remove node from tree').width(200).onClick(() => {
143. this.nodeController.removeBuilderNode();
144. })
145. // 销毁globalBuilderNode下的节点
146. Button('dispose node').width(200).onClick(() => {
147. this.nodeController.disposeNode();
148. })
149. // 第三步：创建子窗
150. Button(`create sub window`).width(200).onClick(() => {
151. this.createSubWindow();
152. })
153. // 销毁子窗
154. Button(`destroy sub window`).width(200).onClick(() => {
155. this.destroySubWindow();
156. })
157. NodeContainer(this.nodeController).backgroundColor('#FFEEF0')
158. }
159. .width('100%')
160. .height('100%')
161. }
162. }

164. @Component
165. struct ComponentUnderBuilderNode {
166. @Env(SystemProperties.BREAK_POINT) breakpoint: uiObserver.WindowSizeLayoutBreakpointInfo;

168. build() {
169. Column() {
170. Text(`ComponentUnderBuilderNode breakpoint width: ${this.breakpoint.widthBreakpoint}`)
171. Text(`ComponentUnderBuilderNode breakpoint height: ${this.breakpoint.heightBreakpoint}`)

173. CompV2({ breakpoint: this.breakpoint })
174. Comp({ breakpoint: this.breakpoint })
175. }
176. }
177. }

179. @ComponentV2
180. struct CompV2 {
181. @Require @Param breakpoint: uiObserver.WindowSizeLayoutBreakpointInfo;

183. build() {
184. Column() {
185. Text(`CompV2 breakpoint width: ${this.breakpoint.widthBreakpoint}`)
186. Text(`CompV2 breakpoint height: ${this.breakpoint.heightBreakpoint}`)
187. }
188. }
189. }

191. @Component
192. struct Comp {
193. @Require breakpoint: uiObserver.WindowSizeLayoutBreakpointInfo;

195. build() {
196. Column() {
197. Text(`Comp breakpoint width: ${this.breakpoint.widthBreakpoint}`)
198. Text(`Comp breakpoint height: ${this.breakpoint.heightBreakpoint}`)
199. }
200. }
201. }
```

```
1. // SubWindow.ets
2. import { MyNodeController } from './Index';

4. @Entry
5. @Component
6. struct SubWindow {
7. private nodeController: MyNodeController = new MyNodeController();

9. build() {
10. Column({ space: 10 }) {
11. Text(`SubWindow`)
12. // 第四步：在第一步中已在创建globalBuilderNode。将globalBuilderNode下的节点挂子窗的NodeContainer的占位节点下
13. Button('add node to tree').width(200).onClick(() => {
14. this.nodeController.addBuilderNode();
15. })
16. Button('remove node from tree').width(200).onClick(() => {
17. this.nodeController.removeBuilderNode();
18. })
19. Button('dispose node').width(200).onClick(() => {
20. this.nodeController.disposeNode();
21. })
22. NodeContainer(this.nodeController).backgroundColor('#FFEEF0')
23. }
24. .height('100%')
25. .width('100%')
26. .backgroundColor('#0D9FFB')
27. }
28. }
```

运行效果图如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/pGGmmeArQhmVUdFubihUkA/zh-cn_image_0000002558604510.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052734Z&HW-CC-Expire=86400&HW-CC-Sign=89FD63D26540F427ED9FB164C7DC78723D5D2F2DD295A10091C0512E2359A326)

可以使用lambda闭包函数将ComponentUnderBuilderNode中的@Env向下传递。通过这种方式ComponentUnderBuilderNode中的@Env可以收集到子组件Comp内组件的依赖，在切换窗口实例的时候触发Comp内组件的刷新。

具体示例如下。

```
1. import { BuilderNode, FrameNode, NodeController, uiObserver, window } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const DOMAIN = 0x0000;

7. let windowStage_: window.WindowStage | undefined = undefined;
8. let sub_windowClass: window.Window | undefined = undefined;
9. let globalBuilderNode: BuilderNode<[]> | undefined = undefined;

11. export class MyNodeController extends NodeController {
12. private rootNode: FrameNode | null = null;
13. private uiContext: UIContext | null = null;

15. makeNode(uiContext: UIContext): FrameNode | null {
16. this.rootNode = new FrameNode(uiContext);
17. this.uiContext = uiContext;
18. return this.rootNode;
19. }

21. addBuilderNode(): void {
22. if (!globalBuilderNode && this.uiContext) {
23. globalBuilderNode = new BuilderNode(this.uiContext);
24. globalBuilderNode.build(wrapBuilder<[]>(buildComponent), undefined);
25. }
26. if (this.rootNode && globalBuilderNode) {
27. this.rootNode.appendChild(globalBuilderNode.getFrameNode());
28. }
29. }

31. removeBuilderNode(): void {
32. if (this.rootNode && globalBuilderNode) {
33. this.rootNode.removeChild(globalBuilderNode.getFrameNode());
34. }
35. }

37. disposeNode(): void {
38. if (this.rootNode && globalBuilderNode) {
39. globalBuilderNode.dispose();
40. globalBuilderNode = undefined;
41. }
42. }
43. }

45. @Builder
46. function buildComponent() {
47. Column() {
48. ComponentUnderBuilderNode()
49. }
50. }

52. @Entry
53. @ComponentV2
54. struct Index {
55. private nodeController: MyNodeController = new MyNodeController();

57. private createSubWindow() {
58. windowStage_ = AppStorage.get('windowStage');
59. if (windowStage_ == null) {
60. hilog.error(DOMAIN, 'testTag', 'Failed to create the subwindow. Cause: windowStage_ is null');
61. } else {
62. // 创建应用子窗口。
63. windowStage_.createSubWindow('mySubWindow', (err: BusinessError, data) => {
64. let errCode: number = err.code;
65. if (errCode) {
66. hilog.error(DOMAIN, 'testTag', 'Failed to create the subwindow. Cause: ' + JSON.stringify(err));
67. return;
68. }
69. sub_windowClass = data;
70. if (!sub_windowClass) {
71. hilog.error(DOMAIN, 'testTag', 'sub_windowClass is null');
72. return;
73. }
74. hilog.info(DOMAIN, 'testTag', 'Succeeded in creating the subwindow. Data: ' + JSON.stringify(data));
75. // 子窗口创建成功后，设置子窗口的位置、大小及相关属性等。
76. sub_windowClass.moveWindowTo(200, 1300, (err: BusinessError) => {
77. let errCode: number = err.code;
78. if (errCode) {
79. hilog.error(DOMAIN, 'testTag', 'Failed to move the window. Cause:' + JSON.stringify(err));
80. return;
81. }
82. hilog.info(DOMAIN, 'testTag', 'Succeeded in moving the window.');
83. });
84. sub_windowClass.resize(900, 1800, (err: BusinessError) => {
85. let errCode: number = err.code;
86. if (errCode) {
87. hilog.error(DOMAIN, 'testTag', 'Failed to change the window size. Cause:' + JSON.stringify(err));
88. return;
89. }
90. hilog.info(DOMAIN, 'testTag', 'Succeeded in changing the window size.');
91. });
92. // 为子窗口加载对应的目标页面。
93. sub_windowClass.setUIContent('pages/SubWindow', (err: BusinessError) => {
94. let errCode: number = err.code;
95. if (errCode) {
96. hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause:' + JSON.stringify(err));
97. return;
98. }
99. hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
100. if (!sub_windowClass) {
101. hilog.error(DOMAIN, 'testTag', 'sub_windowClass is null');
102. return;
103. }
104. sub_windowClass.showWindow((err: BusinessError) => {
105. let errCode: number = err.code;
106. if (errCode) {
107. hilog.error(DOMAIN, 'testTag', 'Failed to show the window. Cause: ' + JSON.stringify(err));
108. return;
109. }
110. hilog.info(DOMAIN, 'testTag', 'Succeeded in showing the window.');
111. });
112. });
113. })
114. }
115. }

117. private destroySubWindow() {
118. if (!sub_windowClass) {
119. console.error('sub_windowClass is null');
120. return;
121. }
122. // 销毁子窗口。当不再需要子窗口时，可根据具体实现逻辑，使用destroy对其进行销毁。
123. sub_windowClass.destroyWindow((err: BusinessError) => {
124. let errCode: number = err.code;
125. if (errCode) {
126. console.error('Failed to destroy the window. Cause: ' + JSON.stringify(err));
127. return;
128. }
129. console.info('Succeeded in destroying the window.');
130. });
131. }

133. build() {
134. Column({ space: 10 }) {
135. Text(`Index`)
136. // 第一步：创建globalBuilderNode，并将globalBuilderNode下的节点挂在NodeContainer的占位节点下
137. Button('add node to tree').width(200).onClick(() => {
138. this.nodeController.addBuilderNode();
139. })
140. // 第二步：从NodeContainer的占位节点下移除globalBuilderNode下的节点
141. Button('remove node from tree').width(200).onClick(() => {
142. this.nodeController.removeBuilderNode();
143. })
144. // 销毁globalBuilderNode下的节点
145. Button('dispose node').width(200).onClick(() => {
146. this.nodeController.disposeNode();
147. })
148. // 第三步：创建子窗
149. Button(`create sub window`).width(200).onClick(() => {
150. this.createSubWindow();
151. })
152. // 销毁子窗
153. Button(`destroy sub window`).width(200).onClick(() => {
154. this.destroySubWindow();
155. })
156. NodeContainer(this.nodeController).backgroundColor('#FFEEF0')
157. }
158. .width('100%')
159. .height('100%')
160. }
161. }

163. @Component
164. struct ComponentUnderBuilderNode {
165. @Env(SystemProperties.BREAK_POINT) breakpoint: uiObserver.WindowSizeLayoutBreakpointInfo;

167. build() {
168. Column() {
169. Text(`ComponentUnderBuilderNode breakpoint width: ${this.breakpoint.widthBreakpoint}`)
170. Text(`ComponentUnderBuilderNode breakpoint height: ${this.breakpoint.heightBreakpoint}`)

172. CompV2({ breakpoint: this.breakpoint })
173. // 通过lambda闭包函数，使得@Env可以关联到Comp内的组件
174. Comp({ getEnv: () => this.breakpoint })
175. }
176. }
177. }

179. @ComponentV2
180. struct CompV2 {
181. @Require @Param breakpoint: uiObserver.WindowSizeLayoutBreakpointInfo;

183. build() {
184. Column() {
185. Text(`CompV2 breakpoint width: ${this.breakpoint.widthBreakpoint}`)
186. Text(`CompV2 breakpoint height: ${this.breakpoint.heightBreakpoint}`)
187. }
188. }
189. }

191. @Component
192. struct Comp {
193. // 通过lambda闭包函数获取父组件的@Env的实例
194. @Require getEnv: () => uiObserver.WindowSizeLayoutBreakpointInfo;

196. build() {
197. Column() {
198. Text(`Comp breakpoint width: ${this.getEnv().widthBreakpoint}`)
199. Text(`Comp breakpoint height: ${this.getEnv().heightBreakpoint}`)
200. }
201. }
202. }
```

运行效果图如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/w-ZNVJljSEm408-7jLYx4w/zh-cn_image_0000002589324035.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052734Z&HW-CC-Expire=86400&HW-CC-Sign=466CFC47497BCD18C657B55619BE7C847BD7382676F8AD453DAF8DE75400A64B)
