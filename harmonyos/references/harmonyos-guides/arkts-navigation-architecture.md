---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-architecture
title: Navigation基础架构介绍
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 设置组件导航和页面路由 > 组件导航(Navigation) (推荐) > Navigation基础架构介绍
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f00d9c30f16567c77d4576002cdce7e4d3f0c651fbf41469daeb54d4652b0780
---

导航组件（[Navigation](../harmonyos-references/ts-basic-components-navigation.md)）主要用于实现[NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)页面间的跳转，支持在不同NavDestination间传递参数，提供灵活的跳转栈操作，从而更便捷地实现对不同页面的访问和复用。

## Navigation整体架构

Navigation组件结构较为复杂，包含几个关键概念：

* [Navigation](../harmonyos-references/ts-basic-components-navigation.md)：导航根视图容器，所有的导航页面都被此容器包裹，提供分栏显示的能力，一般用作全局的根容器。
* [NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)：子页面容器，导航的所有页面路由操作均是针对NavDestination的操作，主要包含：
  + [标题栏](arkts-navigation-architecture.md#标题栏)：位于NavDestination顶部，包括返回按钮、标题，系统提供默认风格，同时支持自定义。
  + [菜单栏](arkts-navigation-architecture.md#菜单栏)：位于NavDestination顶部，系统提供默认风格，同时支持自定义。
  + 内容区：NavDestination的子组件，内容由开发者自定义。
  + [工具栏](arkts-navigation-architecture.md#工具栏)：位于NavDestination底部，系统提供默认风格，同时支持自定义。
* [NavBar](arkts-navigation-architecture.md#navbar导航栏)：导航栏，也称为主页面，主要包含：
  + [标题栏](arkts-navigation-architecture.md#标题栏)：位于NavBar顶部，包括返回按钮、标题，系统提供默认风格，同时支持自定义。
  + [菜单栏](arkts-navigation-architecture.md#菜单栏)：位于NavBar顶部，系统提供默认风格，同时支持自定义。
  + 内容区：位于NavBar中心区域，内容由开发者自定义。
  + [工具栏](arkts-navigation-architecture.md#工具栏)：位于NavBar底部，系统提供默认风格，同时支持自定义。
* [NavPathStack](../harmonyos-references/ts-basic-components-navigation.md#navpathstack10)：导航控制器，用于管理NavDestination页面栈，其封装了各种控制页面跳转的接口，支持继承后重写，需与Navigation绑定使用。

**图1** Navigation总体架构图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/ekGcOUBBTLarl8sYmj2HEw/zh-cn_image_0000002558764168.png?HW-CC-KV=V1&HW-CC-Date=20260429T052735Z&HW-CC-Expire=86400&HW-CC-Sign=CAE75326F15876EBB201617FD18A865078364CA7D1B17B18FB5A2AEB7CE0CBC3)

此外Navigation提供两种布局模式：单栏模式、分栏模式，不同模式下的结构如下。

* 单栏模式：

  当Navigation容器宽度小于600vp时，建议使用单栏模式。此模式下发生路由跳转时，整个页面都会被替换。

  **图2** 单栏布局示意图

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/KxxZhbHuRKKGhI-uJsNiKg/zh-cn_image_0000002558604512.png?HW-CC-KV=V1&HW-CC-Date=20260429T052735Z&HW-CC-Expire=86400&HW-CC-Sign=5CEB4A6B880A949A22D269305830CAB34A78CDB716E3D3F607F2681E316681CC)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/_9_BibSASiGg5XrJ-PdEFQ/zh-cn_image_0000002589324037.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T052735Z&HW-CC-Expire=86400&HW-CC-Sign=48DA8CDCCFE878A75A3B5CECF2E03B9519F7280FE3A4D253AFA9CEFD33063E91)
* 分栏模式：

  当Navigation容器宽度大于等于600vp时，建议使用分栏模式。此模式下Navigation分为左右两部分，左侧为导航栏（NavBar），右侧为子页面（NavDestination）。发生路由跳转时，只有右边子页会被替换。

  **图3** 分栏布局示意图

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/xd1CbSNNQbCIGISVybipmg/zh-cn_image_0000002589243977.png?HW-CC-KV=V1&HW-CC-Date=20260429T052735Z&HW-CC-Expire=86400&HW-CC-Sign=65AFB79322BCD564F2A398AAD08B9C0775F712618F6F135F94D52C75F616EFE7)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/MQAQ_W1ZQxqwE8o6hdwd1g/zh-cn_image_0000002558764170.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T052735Z&HW-CC-Expire=86400&HW-CC-Sign=2314909A74EF96B705E955B16399236D2A9BE82B6044FC00D3519E34FBC78D5C)

## Navigation（导航容器）

Navigation是路由导航的根视图容器，通常作为页面（@Entry修饰的自定义组件，定义为Router页面）的根容器（作为全局导航使用），包括单栏（Stack）、分栏（Split）和自适应（Auto）三种显示模式，Auto模式会基于Navigation组件的宽度自动在Stack和Split中切换。

Navigation组件本身可不作为显示容器，只用于承载路由的相关功能，如绑定导航控制器对象、路由切换、分栏显示、自定义转场动画控制等。

Navigation组件主要包含导航栏（NavBar）和子页（NavDestination），子页通过栈结构管理，存在NavPathStack中。导航栏又称Navbar，作为Navigation的子组件，直接挂载到Navigation上，可以通过[hideNavBar](../harmonyos-references/ts-basic-components-navigation.md#hidenavbar9)属性进行隐藏（单栏应用推荐隐藏导航页），导航栏不存在页面栈中。

子页面是一个以NavDestination为根节点的子树，通过[@Builder](arkts-builder.md)构造出来，再通过NavPathStack提供的栈操作方法挂载到Navigation上显示，详见[Navigation子页面](arkts-navigation-navdestination.md)。

## NavDestination（子页面容器）

Navigation子页面的根容器，每个子页面都需要包裹在一个NavDestination中，通过NavPathStack提供的栈操作方法（push、pop等）将子页面挂载到Navigation上显示或删除。

NavDestination作为页面根容器，除了支持普通组件的通用属性外，还支持页面相关的属性，如：[页面的生命周期](../harmonyos-references/ts-basic-components-navdestination.md#事件)，页面[工具栏](../harmonyos-references/ts-basic-components-navdestination.md#toolbarconfiguration13)、[标题栏](../harmonyos-references/ts-basic-components-navdestination.md#title)与[菜单栏](../harmonyos-references/ts-basic-components-navdestination.md#menus12)，[自定义页面转场动画](../harmonyos-references/ts-basic-components-navdestination.md#customtransition15)，页面级窗口属性控制（横竖屏、系统状态栏、系统导航条）等能力。

## NavBar（导航栏）

Navigation中直接加载的孩子节点称为导航栏（NavBar），单栏显示时它是整个导航的首页，分栏显示时它是固定的导航栏。分栏显示时默认显示在左边，也可以通过[navBarPosition](../harmonyos-references/ts-basic-components-navigation.md#navbarposition9)属性控制。

开发者可以通过[hideNavBar](../harmonyos-references/ts-basic-components-navigation.md#hidenavbar9)控制导航栏的显隐，也可以通过[navBarWidth](../harmonyos-references/ts-basic-components-navigation.md#navbarwidth9)属性控制双栏显示下的Navbar宽度，NavBar本身不属于页面栈中的页面，不具备页面的生命周期等，不能通过NavPathStack的方法控制。 开发者可以通过[onNavBarStateChange](../harmonyos-references/ts-basic-components-navigation.md#onnavbarstatechange9)去感知导航栏的显隐，通过[mode](../harmonyos-references/ts-basic-components-navigation.md#mode9)属性控制单双栏切换，也可以通过[onNavigationModeChange](../harmonyos-references/ts-basic-components-navigation.md#onnavigationmodechange11)去感知单双栏的切换。

NavBar的内容区可以通过两种方式指定：

* 方式一：直接指定Navigation的子节点。

```
1. @Entry
2. @Component
3. struct NavigationDemo {
4. @Provide('navPathStack') navPathStack: NavPathStack = new NavPathStack();
5. private listArray: Array<string> = ['WLAN', 'Bluetooth', 'Personal Hotspot', 'Connect & Share'];
6. context = this.getUIContext().getHostContext();
7. build() {
8. Column() {
9. Navigation(this.navPathStack) {
10. // 请将$r('app.string.enterKeyWordsToSearch')替换为实际资源文件，在本示例中该资源文件的value值为"输入关键字搜索"
11. TextInput({ placeholder: $r('app.string.enterKeyWordsToSearch') })
12. .width('90%')
13. .height(40)
14. .margin({ bottom: 10 })

16. // 通过List定义导航的一级界面
17. List({ space: 12, initialIndex: 0 }) {
18. ForEach(this.listArray, (item: string) => {
19. ListItem() {
20. Row() {
21. Row() {
22. Text(`${item.slice(0, 1)}`)
23. .fontColor(Color.White)
24. .fontSize(14)
25. .fontWeight(FontWeight.Bold)
26. }
27. .width(30)
28. .height(30)
29. .backgroundColor('#a8a8a8')
30. .margin({ right: 20 })
31. .borderRadius(20)
32. .justifyContent(FlexAlign.Center)

34. Column() {
35. Text(item)
36. .fontSize(16)
37. .margin({ bottom: 5 })
38. }
39. .alignItems(HorizontalAlign.Start)

41. Blank()

43. Row()
44. .width(12)
45. .height(12)
46. .margin({ right: 15 })
47. .border({
48. width: { top: 2, right: 2 },
49. color: 0xcccccc
50. })
51. .rotate({ angle: 45 })
52. }
53. .borderRadius(15)
54. .shadow({ radius: 100, color: '#ededed' })
55. .width('90%')
56. .alignItems(VerticalAlign.Center)
57. .padding({ left: 15, top: 15, bottom: 15 })
58. .backgroundColor(Color.White)
59. }
60. .width('100%')
61. .onClick(() => {
62. // $r('app.string.detailsPageParameters')需要替换为开发者所需的字符串资源文件,资源文件中的value值为“详情页面参数”
63. this.navPathStack.pushPathByName(`${item}`,
64. // 将name指定的NaviDestination页面信息入栈,传递的参数为param
65. this.context!.resourceManager.getStringSync($r('app.string.detailsPageParameters').id));
66. })
67. }, (item: string): string => item)
68. }
69. .listDirection(Axis.Vertical)
70. .edgeEffect(EdgeEffect.Spring)
71. .sticky(StickyStyle.Header)
72. .chainAnimation(false)
73. .width('100%')
74. }
75. .width('100%')
76. .mode(NavigationMode.Auto)
77. // $r('app.string.settings')需要替换为开发者所需的字符串资源文件,资源文件中的value值为“设置”
78. .title($r('app.string.settings')) // 设置标题文字
79. }
80. .size({ width: '100%', height: '100%' })
81. .backgroundColor(0xf4f4f5)
82. }
83. }
```

[NavigationExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template1/NavigationExample.ets#L15-L99)

* 方式二：从API version 20开始，使用[主页类型NavDestination](../harmonyos-references/ts-basic-components-navigation.md#navigation20)将某个NavDestination直接指定为导航栏内容，此方法需要配置路由表，配置方式请参考[路由表](arkts-navigation-cross-package.md#路由表能力对比)。

## NavPathStack（导航控制器）

Navigation的子页面栈存在NavPathStack中，每个Navigation都需要绑定一个NavPathStack对象，NavPathStack用于控制Navigation中所有子页的切换。NavPathStack提供了很多基础的路由切换方法，如：[pushPath](../harmonyos-references/ts-basic-components-navigation.md#pushpath10)、[pop](../harmonyos-references/ts-basic-components-navigation.md#pop10)、[replacePath](../harmonyos-references/ts-basic-components-navigation.md#replacepath11)等，以及路由拦截、转场动画控制、路由栈信息获取等能力。

NavPathStack也支持开发者继承并复写相关路由操作方法。NavPathStack跟Navigation一一对应，在每个子页中可以通过NavDestination的[onReady](../harmonyos-references/ts-basic-components-navdestination.md#onready11)回调获取，也可以全局维护一个单例的NavPathStack，在任意地方获取并执行路由操作（注意：页面切换动画和布局必须在UI线程中才可以生效，依赖Vsync信号）。

## 标题栏

标题栏在界面顶部，用于呈现界面名称和操作入口，Navigation组件通过[title](../harmonyos-references/ts-basic-components-navigation.md#title)属性设置标题内容，通过[titleMode](../harmonyos-references/ts-basic-components-navigation.md#titlemode)属性设置标题栏模式。NavDestination同样支持[title](../harmonyos-references/ts-basic-components-navdestination.md#title)属性用于设置标题内容。

说明

Navigation未设置[title](../harmonyos-references/ts-basic-components-navigation.md#title)、[titleMode](../harmonyos-references/ts-basic-components-navigation.md#titlemode)、[menus](../harmonyos-references/ts-basic-components-navigation.md#menus)等与标题、菜单栏相关的属性时，即使将[hideBackButton](../harmonyos-references/ts-basic-components-navigation.md#hidebackbutton)设置为false，返回按钮也不会展示。

* Mini模式：

  普通型标题栏，用于一级页面不需要突出标题的场景。

  **图4** Mini模式标题栏

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/jDv3fi2QTFq9bndor7Pfzw/zh-cn_image_0000002558604514.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T052735Z&HW-CC-Expire=86400&HW-CC-Sign=7CBC4A52C7BA443D3CF1AAAB404BF0ED1194A238090B996569473EE80E8206B7)

  ```
  1. Navigation() {
  2. // ...
  3. }
  4. .titleMode(NavigationTitleMode.Mini)
  ```

  [TitleModeMini.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template1/TitleModeMini.ets#L54-L64)
* Full模式：

  强调型标题栏，用于一级页面需要突出标题的场景。

  **图5** Full模式标题栏

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/__T27bRyTpGqWZCYD2DOaQ/zh-cn_image_0000002589324039.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T052735Z&HW-CC-Expire=86400&HW-CC-Sign=C0C805F67E0AFA796B66EF0B90EE788C0088D7102BA382DB7AB9C41C6A4EBE11)

  ```
  1. Navigation() {
  2. // ...
  3. }
  4. .titleMode(NavigationTitleMode.Full)
  ```

  [TitleModeFull.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template1/TitleModeFull.ets#L54-L64)

## 菜单栏

菜单栏位于组件的顶部，开发者可以通过[menus](../harmonyos-references/ts-basic-components-navigation.md#menus)属性设置Navigation的菜单栏。menus支持Array<[NavigationMenuItem](../harmonyos-references/ts-basic-components-navigation.md#navigationmenuitem)>和[CustomBuilder](../harmonyos-references/ts-types.md#custombuilder8)两种参数类型。使用Array<[NavigationMenuItem](../harmonyos-references/ts-basic-components-navigation.md#navigationmenuitem)>类型时，竖屏最多支持显示3个图标，横屏最多支持显示5个图标，多余的图标会被放入自动生成的更多图标。NavDestination同样支持[menus](../harmonyos-references/ts-basic-components-navdestination.md#menus12)属性用于设置菜单栏。

**图6** 设置了3个图标的菜单栏

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/XwFoIPqmTreqCCjqBLi3ow/zh-cn_image_0000002589243979.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T052735Z&HW-CC-Expire=86400&HW-CC-Sign=C6C1D0FB2DCF2F67BF89A5E279A347B766EED03EBA288CBF322D3B7BE993E4A0)

```
1. let menuItem: NavigationMenuItem  = {
2. 'value': 'func',
3. 'icon': 'ets/pages/navigation/template1/image/ic_public_add.svg',
4. 'action': () => {}
5. };
6. // ...
7. Navigation(this.navPathStack) {
8. // ...
9. }
10. .menus([menuItem, menuItem, menuItem])
```

[MenusThreeImage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template1/MenusThreeImage.ets#L16-L72)

图片也可以引用resources中的资源。

```
1. let menuItem: NavigationMenuItem  = {
2. 'value': 'func',
3. 'icon': 'resources/base/media/ic_public_add.svg',
4. 'action': () => {}
5. };
6. // ...
7. Navigation(this.navPathStack) {
8. // ...
9. }
10. .menus([menuItem, menuItem, menuItem])
```

[MenusThreeResource.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template1/MenusThreeResource.ets#L16-L72)

**图7** 设置了4个图标的菜单栏

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/PXkm4wcuQw67_O9a2WFJ5g/zh-cn_image_0000002558764172.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T052735Z&HW-CC-Expire=86400&HW-CC-Sign=ED03C531DBD7760533689AA0E9BF2A6E529BA6C16AC7BC8E99268C386791E6D2)

竖屏状态下菜单栏，最多支持显示3个按钮，当按钮超过3个时，多余的按钮会被折叠。

```
1. let menuItem: NavigationMenuItem  = {
2. 'value': 'func',
3. 'icon': 'ets/pages/navigation/template1/image/ic_public_add.svg',
4. 'action': () => {}
5. };
6. // ...
7. Navigation(this.navPathStack) {
8. // ...
9. }
10. // 竖屏最多支持显示3个图标，多余的图标会被放入自动生成的更多图标
11. .menus([menuItem, menuItem, menuItem, menuItem])
```

[MenusFour.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template1/MenusFour.ets#L16-L73)

## 工具栏

工具栏位于组件的底部，开发者可以通过[toolbarConfiguration](../harmonyos-references/ts-basic-components-navigation.md#toolbarconfiguration10)属性设置Navigation的工具栏。NavDestination同样支持[toolbarConfiguration](../harmonyos-references/ts-basic-components-navdestination.md#toolbarconfiguration13)属性用于设置工具栏。

**图8** 工具栏

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/4O4hyji-R7-V9H4g3PfjNg/zh-cn_image_0000002558604516.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T052735Z&HW-CC-Expire=86400&HW-CC-Sign=CB51C5A47F31038F88D21FE182751E005A022981827FB7148604704D6CC44E3F)

```
1. let toolTmp: ToolbarItem = {
2. 'value': 'func',
3. 'icon': 'ets/pages/navigation/template1/image/ic_public_highlights.svg',
4. 'action': () => {}
5. };
6. let toolBar: ToolbarItem[] = [toolTmp,toolTmp,toolTmp];
7. // ...
8. Navigation(this.navPathStack) {
9. // ...
10. }
11. .toolbarConfiguration(toolBar)
```

[ToolBar.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template1/ToolBar.ets#L16-L78)
