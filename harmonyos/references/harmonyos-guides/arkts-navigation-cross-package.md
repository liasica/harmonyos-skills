---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-cross-package
title: Navigation跨包路由
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 设置组件导航和页面路由 > 组件导航(Navigation) (推荐) > Navigation跨包路由
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:39+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:cd9a99119ffa8621f71fca85b8cadede0797c02001b819be8385e0b0383b7f54
---

Navigation提供[系统路由表](arkts-navigation-cross-package.md#系统路由表)和[自定义路由表](arkts-navigation-cross-package.md#自定义路由表)两种实现方式，通过路由表的配置可以完成本包和跨包的页面跳转。

支持自定义路由表和系统路由表混用。

## 路由表能力对比

不同路由方式适用于不同需求，易用性或可扩展性需根据项目特点权衡选择。

| 路由方式 | 跨包跳转能力 | 可扩展性 | 易用性 |
| --- | --- | --- | --- |
| [系统路由表](arkts-navigation-cross-package.md#系统路由表) | 跳转前无需import页面文件，页面按需动态加载。 | 可扩展性一般。 | 易用性更强，系统自动维护路由表。使用简单，开发者只需要添加对应页面跳转配置项，即可实现页面跳转。 |
| [自定义路由表](arkts-navigation-cross-package.md#自定义路由表) | 跳转前需要import页面文件。 | 可扩展性更强。 | 易用性一般，需要开发者自行维护路由表。使用复杂，但是可以根据应用业务进行定制处理。 |

## 系统路由表

系统路由表是动态路由的一种实现方式。从API version 12开始，Navigation支持使用系统路由表的方式进行动态路由。从API version 23开始，Navigation组件支持跳转到[按需加载](../best-practices/bpta-modular-design.md#section28312051291)的HSP页面。

系统路由表支持模拟器但不支持预览器。

要实现系统路由表，各业务模块（[HAP](hap-package.md)、[HSP](in-app-hsp.md)、[HAR](har-package.md)）中需要独立配置router\_map.json文件，在触发路由跳转时，应用只需要通过NavPathStack提供的路由方法，传入需要路由的页面配置名称，此时系统会自动完成路由模块的动态加载、页面组件构建，并完成路由跳转，从而实现了开发层面的模块解耦。其主要步骤如下：

1. 添加完路由配置文件地址后，在工程resources/base/profile路径下创建router\_map.json文件。添加如下配置信息，各字段含义详见[routerMap标签](module-configuration-file.md#routermap标签)。

   ```
   1. {
   2. "routerMap": [
   3. {
   4. "name": "PageOne",
   5. "pageSourceFile": "src/main/ets/pages/PageOne.ets",
   6. "buildFunction": "PageOneBuilder",
   7. "data": {
   8. "description" : "this is PageOne"
   9. }
   10. }
   11. ]
   12. }
   ```
2. 在跳转目标模块的配置文件[module.json5](module-configuration-file.md)添加路由表配置。

   ```
   1. {
   2. "module": {
   3. // ...
   4. "routerMap": "$profile:router_map",
   5. // ...
   6. }
   7. }
   ```

   [module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/module.json5#L15-L72)
3. 在跳转目标页面，配置入口Builder函数，函数名称需要和router\_map.json配置文件中的buildFunction保持一致，否则在编译时会报错。

   ```
   1. // 跳转页面入口函数
   2. @Builder
   3. export function PageOneBuilder() {
   4. PageOne();
   5. }

   7. @Component
   8. struct PageOne {
   9. pathStack: NavPathStack = new NavPathStack();

   11. build() {
   12. NavDestination() {
   13. }
   14. .title('PageOne')
   15. .onReady((context: NavDestinationContext) => {
   16. this.pathStack = context.pathStack;
   17. })
   18. }
   19. }
   ```

   [PageOne.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template1/PageOne.ets#L30-L50)
4. 通过pushPathByName等路由接口进行页面跳转。

   ```
   1. @Entry
   2. @Component
   3. struct SystemRoutingTable {
   4. pageStack : NavPathStack = new NavPathStack();

   6. build() {
   7. Navigation(this.pageStack){
   8. }.onAppear(() => {
   9. this.pageStack.pushPathByName('PageOne', null, false);
   10. })
   11. .hideNavBar(true)
   12. }
   13. }
   ```

   [PageOne.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template1/PageOne.ets#L15-L29)

## 自定义路由表

自定义路由表通过给Navigation的[navDestination](../harmonyos-references/ts-basic-components-navigation.md#navdestination10)属性设置Builder函数实现，其特点是需要import页面。有两种import页面的方式，静态import和动态import，二者的区别在于：

| import方式 | 模块间耦合度 | 实现复杂度 | 性能 |
| --- | --- | --- | --- |
| 动态import | 模块间解耦。 | 复杂度高。 | 性能好，按需加载，跳转前再加载对应页面。 |
| 静态import | 模块间耦合。 | 复杂度低。 | 性能一般，初始化时一次性加载所有依赖的页面。 |

### 动态import

动态import主要用于多个模块（HAR/HSP）复用相同业务逻辑的场景，实现各业务模块间的解耦，同时支持路由功能的扩展与整合，可以按需import。

动态import的优势：

* 路由定义除了跳转的URL以外，可以配置丰富的扩展信息，如横竖屏默认模式、是否需要鉴权等等，做路由跳转时统一处理。
* 给每个路由页面设置一个名字，按照名称进行跳转而不是文件路径。
* 页面的加载可以使用动态import（按需加载），防止首个页面加载大量代码导致卡顿。

实现步骤如下，具体请参考[自动生成动态路由](https://gitcode.com/HarmonyOS-Cases/cases/blob/master/CommonAppDevelopment/common/routermodule/README_AUTO_GENERATE.md)示例。

1. 定义页面跳转配置项。
   * 使用资源文件进行定义，通过资源管理[@ohos.resourceManager](../harmonyos-references/js-apis-resource-manager.md)在运行时对资源文件解析。
   * 在ets文件中配置路由加载配置项，一般包括路由页面名称（即pushPath等接口中页面的别名），文件所在模块名称（HSP/HAR的模块名），加载页面在模块内的路径（相对src目录的路径）。
2. 加载目标跳转页面，通过[动态import](arkts-dynamic-import.md)将跳转目标页面所在的模块在运行时加载，在模块加载完成后，调用模块中的方法，通过import在模块的方法中加载模块中显示的目标页面，并返回页面加载完成后定义的Builder函数。
3. 触发页面跳转，在Navigation的[navDestination](../harmonyos-references/ts-basic-components-navigation.md#navdestination10)属性中执行步骤2加载的Builder函数，即可跳转到目标页面。

### 静态import

静态import实现方式简单，但通过静态import页面进行路由跳转会导致不同模块之间的依赖耦合，并存在首页加载时间长等问题。建议使用[动态import](arkts-navigation-cross-package.md#动态import)或[系统路由表](arkts-navigation-cross-package.md#系统路由表)。

静态import实现步骤如下：

1. 使用[@Builder装饰器](arkts-builder.md)创建自定义构造函数pageMap。
2. 在自定义构造函数pageMap里实现路由表，根据传入的页面名称构造不同的页面。
3. 将pageMap配置到Navigation的[navDestination](../harmonyos-references/ts-basic-components-navigation.md#navdestination10)属性中，完成路由表注册。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const DOMAIN = 0x0000;

5. @Entry
6. @Component
7. struct NavigationExample {
8. @Provide('navPathStack') navPathStack: NavPathStack = new NavPathStack();
9. private arr: number[] = [1, 2];

11. @Builder
12. pageMap(name: string) {
13. if (name === 'NavDestinationTitle1') {
14. pageOneTmp();
15. } else if (name === 'NavDestinationTitle2') {
16. pageTwoTmp();
17. }
18. }

20. build() {
21. Column() {
22. Navigation(this.navPathStack) {
23. TextInput({ placeholder: 'search...' })
24. .width('90%')
25. .height(40)

27. List({ space: 12 }) {
28. ForEach(this.arr, (item: number) => {
29. ListItem() {
30. Text('Page' + item)
31. .width('100%')
32. .height(72)
33. .borderRadius(24)
34. .fontSize(16)
35. .fontWeight(500)
36. .textAlign(TextAlign.Center)
37. .onClick(() => {
38. this.navPathStack.pushPath({ name: 'NavDestinationTitle' + item });
39. })
40. }
41. }, (item: number) => item.toString())
42. }
43. .width('90%')
44. .margin({ top: 12 })
45. }
46. // $r('app.string.mainTitle')需要替换为开发者所需的字符串资源文件，资源文件中的value值为“主标题”
47. .title($r('app.string.mainTitle'))
48. .navDestination(this.pageMap)
49. .mode(NavigationMode.Split)
50. }
51. .height('100%')
52. .width('100%')
53. }
54. }

56. @Component
57. export struct pageTwoTmp {
58. @Consume('navPathStack') navPathStack: NavPathStack;
59. context = this.getUIContext().getHostContext();

61. build() {
62. NavDestination() {
63. Column() {
64. Text('NavDestinationContent2')
65. }.width('100%').height('100%')
66. }.title('NavDestinationTitle2')
67. .onBackPressed(() => {
68. const popDestinationInfo = this.navPathStack.pop(); // 弹出路由栈的栈顶元素
69. // $r('app.string.returnValue')需要替换为开发者所需的字符串资源文件，资源文件中的value值为“返回值”
70. hilog.info(DOMAIN, 'testTag', 'pop', this.context!.resourceManager.getStringSync($r('app.string.returnValue').id),
71. JSON.stringify(popDestinationInfo));
72. return true;
73. })
74. }
75. }

77. @Component
78. export struct pageOneTmp {
79. @Consume('navPathStack') navPathStack: NavPathStack;
80. context = this.getUIContext().getHostContext();

82. build() {
83. NavDestination() {
84. Column() {
85. Text('NavDestinationContent1')
86. }.width('100%').height('100%')
87. }.title('NavDestinationTitle1')
88. .onBackPressed(() => {
89. const popDestinationInfo = this.navPathStack.pop(); // 弹出路由栈的栈顶元素
90. // $r('app.string.returnValue')需要替换为开发者所需的字符串资源文件，资源文件中的value值为“返回值”
91. hilog.info(DOMAIN, 'testTag', 'pop', this.context!.resourceManager.getStringSync($r('app.string.returnValue').id),
92. JSON.stringify(popDestinationInfo));
93. return true;
94. })
95. }
96. }
```

[CustomRoutingTable.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template1/CustomRoutingTable.ets#L15-L108)

## 开发步骤

如下示例展示了基于系统路由表的跨包跳转，实现六个页面之间的相互跳转，其中HAP包有两个页面HapPageA和HapPageB，HSP包中有两个页面HspPageA和HspPageB，HAR包中也有两个页面HarPageA、HarPageB。

1. 配置路由表。

   参考[系统路由表](arkts-navigation-cross-package.md#系统路由表)在每个[HAP](hap-package.md)、[HAR](har-package.md)、[HSP](in-app-hsp.md)模块中配置各自的系统路由表，每个模块的src/main/resources/base/profile/目录都需要创建一个router\_map.json文件。

   在router\_map.json文件中填写具体的路由表信息（下面仅以HAP模块中的配置为例），示例如下：

   ```
   1. {
   2. "routerMap": [
   3. {
   4. "name": "HapPageA",
   5. "pageSourceFile": "src/main/ets/pages/HapPageA.ets",
   6. "buildFunction": "HapPageABuilder",
   7. "data": {
   8. "description": "this is HapPageA"
   9. }
   10. },
   11. {
   12. "name": "HapPageB",
   13. "pageSourceFile": "src/main/ets/pages/HapPageB.ets",
   14. "buildFunction": "HapPageBBuilder",
   15. "data": {
   16. "description": "this is HapPageB"
   17. }
   18. }
   19. ]
   20. }
   ```

   在每个模块的[module.json5](module-configuration-file.md)中配置各自的路由表。

   ```
   1. {
   2. "module": {
   3. // ...
   4. "routerMap": "$profile:router_map",
   5. // ...
   6. }
   7. }
   ```

   [module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/module.json5#L15-L72)
2. 跳转功能开发。

   以HAP包中的HapPageA为例：

   ```
   1. // 仅作为示例写法，其余页面、模块需自行创建
   2. import { ControlPanel } from './Common';

   4. @Component
   5. export struct HapPageA {
   6. build() {
   7. NavDestination() {
   8. Stack({alignContent: Alignment.Center}) {
   9. ControlPanel()
   10. }.width('100%').height('100%')
   11. }.title('HapPageA')
   12. .onReady((ctx: NavDestinationContext) => {
   13. let config = ctx.getConfigInRouteMap();
   14. })
   15. }
   16. }

   18. // 页面的buildFunction，用于构造页面
   19. @Builder
   20. export function HapPageABuilder(): void {
   21. HapPageA();
   22. }
   ```

   [HapPageA.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template4/HapPageA.ets#L16-L39)

   其中Common是为了方便演示页面间跳转抽出来的一个控制面板组件，示例如下：

   ```
   1. @Component
   2. export struct ControlPanel {
   3. private stack: NavPathStack | undefined = undefined;

   5. aboutToAppear(): void {
   6. let info = this.queryNavigationInfo();
   7. this.stack = info?.pathStack;
   8. }

   10. build() {
   11. Column({ space: 20 }) {
   12. Button('push HapPageA').onClick(() => {
   13. this.stack?.pushPath({ name: 'HapPageA' });
   14. })
   15. Button('push HapPageB').onClick(() => {
   16. this.stack?.pushPath({ name: 'HapPageB' });
   17. })
   18. Button('push HarPageA').onClick(() => {
   19. this.stack?.pushPath({ name: 'HarPageA' });
   20. })
   21. Button('push HarPageB').onClick(() => {
   22. this.stack?.pushPath({ name: 'HarPageB' });
   23. })
   24. Button('push HspPageA').onClick(() => {
   25. this.stack?.pushPath({ name: 'HspPageA' });
   26. })
   27. Button('push HspPageB').onClick(() => {
   28. this.stack?.pushPath({ name: 'HspPageB' });
   29. })
   30. }
   31. }
   32. }
   ```

   [Common.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template4/Common.ets#L16-L49)
3. 编译构建。

   因为HAR和HSP被HAP模块依赖，所以需要先编译HAR和HSP，为了方便演示，这里将编译产物放到一个公共目录里面。

   **图1** HSP、HAR编译产物示意图

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/PkjwOuZ_TcKMo-5BKZbV4Q/zh-cn_image_0000002558604518.png?HW-CC-KV=V1&HW-CC-Date=20260429T052736Z&HW-CC-Expire=86400&HW-CC-Sign=ACA56F45D2C422997F27E9788572EBC8587CAA3BF203A0DA1F181A67A9962A51)

   在HAP的oh-package.json5配置文件中配置对HAR与HSP的依赖。

   ```
   1. {
   2. "name": "entry",
   3. "version": "1.0.0",
   4. "description": "Please describe the basic information.",
   5. "main": "",
   6. "author": "",
   7. "license": "",
   8. "dependencies": {
   9. "har_a": "file:../libs/HAR_A.har", // 因为演示中使用的是本地依赖包，所以通过file指示一个固定的文件。
   10. "hsp_a": "file:../libs/HSP_A-default.tgz", // 因为演示中使用的是本地依赖包，所以通过file指示一个固定的文件。
   11. }
   12. }
   ```

   然后在DevEco Studio中直接运行HAP模块，此时会将HAP与HSP一起安装到设备中，效果如下：

   **图2** Navigation跨包跳转示例

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/dJa39JVqSIqm8s1RcrA87w/zh-cn_image_0000002589324043.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052736Z&HW-CC-Expire=86400&HW-CC-Sign=7A48DA8A6A4293499FEB0BBFD5F50579B57677CA5D38C34D8DBF811522ACD0A0)
