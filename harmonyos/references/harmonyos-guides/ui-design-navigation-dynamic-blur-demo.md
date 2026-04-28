---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-navigation-dynamic-blur-demo
title: 开发实例
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 组件导航 > 开发实例
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:52+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:320b8a56972f9bbde3553fd47e2c2aef2eb9ce3b4a9b57795d889ed32d2c8c9c
---

1. 在首页创建一级导航，适用于需要构建具有导航结构的主界面，支持动态标题栏样式切换与页面跳转功能。通过titleBar接口设置导航栏的内容和样式，包括标题、菜单项、返回按钮等元素。通过pushPath路由方法跳转至二级导航页面。

   ```
   1. // 模块导入
   2. // 从6.0.2(22)版本开始，无需手动导入HdsNavigationAttribute。具体请参考HdsNavigation的导入模块说明。
   3. import { HdsNavigation, ScrollEffectType, HdsNavigationTitleMode, HdsNavigationAttribute } from '@kit.UIDesignKit';

   5. @Entry
   6. @Component
   7. struct Index {
   8. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];
   9. @Provide('pageInfos') pageInfos: NavPathStack = new NavPathStack();
   10. scroller: Scroller = new Scroller();

   12. build() {
   13. HdsNavigation(this.pageInfos) { // 创建HdsNavigation组件
   14. Stack() {
   15. Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
   16. .width('80%')
   17. .height(40)
   18. .margin({ top: '5%', right: '50vp', left: '50vp' })
   19. .onClick(() => {
   20. this.pageInfos.pushPath({ name: 'pageOne' });
   21. })
   22. }
   23. .zIndex(5)

   25. List({ space: 12, initialIndex: 0, scroller: this.scroller }) {
   26. ForEach(this.arr, (item: number) => {
   27. ListItem() {
   28. Column() {
   29. Row({ space: 8 }) {
   30. Button() {
   31. SymbolGlyph($r('sys.symbol.wifi'))
   32. .fontColor([$r('sys.color.icon_on_primary')])
   33. .fontSize(24)
   34. }
   35. .width(35)
   36. .height(35)

   38. Text('list_' + item)
   39. .width('100%')
   40. .height(72)
   41. .fontSize(16)
   42. .fontWeight(500)
   43. }

   45. Divider().margin({ left: 40 })
   46. }
   47. }
   48. .height(56)
   49. }, (item: number) => item.toString())
   50. }
   51. .margin({ left: 16, right: 16 })
   52. .clip(false) // 设置不对子组件超出当前组件范围外的区域进行裁剪，使内容区可以穿透到标题栏下方
   53. .cachedCount(3, true) // 设置列表中ListItem/ListItemGroup的预加载数量，列表穿透到标题栏下方不会消失
   54. .scrollBar(BarState.Off)
   55. .edgeEffect(EdgeEffect.Spring, { alwaysEnabled: true })
   56. }
   57. .titleBar({
   58. // HdsNavigation标题栏设置
   59. enableComponentSafeArea: true, // 将标题栏设置为组件级安全区，内容区可避让标题栏
   60. style: {
   61. // HdsNavigation标题栏样式设置
   62. // 标题栏动态模糊样式：通用模糊
   63. scrollEffectOpts: {
   64. enableScrollEffect: true,
   65. scrollEffectType: ScrollEffectType.COMMON_BLUR,
   66. },
   67. },
   68. content: {
   69. // HdsNavigation标题栏内容区设置
   70. title: {
   71. // HdsNavigation标题栏标题设置
   72. mainTitle: 'MainTitle',
   73. },
   74. menu: {
   75. // HdsNavigation标题栏菜单项设置
   76. value: [{
   77. // 第一个菜单项内容设置
   78. content: {
   79. label: 'menu1',
   80. icon: $r('sys.symbol.ohos_wifi'),
   81. isEnabled: true,
   82. },
   83. badge: {
   84. count: 1,
   85. }
   86. }, {
   87. // 第二个菜单项内容设置
   88. content: {
   89. label: 'menu2',
   90. icon: $r('sys.symbol.ohos_lock'),
   91. isEnabled: true,
   92. action: () => {
   93. console.info(`HDS_NAV HELLO 2`);
   94. }
   95. }
   96. }, {
   97. // 第三个菜单项内容设置
   98. content: {
   99. label: 'menu3',
   100. icon: $r('sys.symbol.speaker_plus'),
   101. }
   102. }, {
   103. content: {
   104. // 第三个菜单项内容设置
   105. label: 'menu4',
   106. icon: $r('sys.symbol.ohos_star'),
   107. }
   108. }]
   109. },
   110. }
   111. })
   112. .titleMode(HdsNavigationTitleMode.MINI)
   113. .hideBackButton(true)
   114. .bindToScrollable([this.scroller]) // 绑定导航组件和可滚动容器组件
   115. }
   116. }
   ```
2. 在PageOne页面创建二级导航组件。通过titleBar接口设置HdsNavDestination标题栏HarmonyOS风格化样式及内容设置。展示NavPathStack路由使用示例。

   ```
   1. // PageOne.ets
   2. // 模块导入
   3. // 从6.0.2(22)版本开始，无需手动导入HdsNavDestinationAttribute。具体请参考HdsNavDestination的导入模块说明。
   4. import { HdsNavDestination, HdsNavDestinationAttribute } from '@kit.UIDesignKit';

   6. @Builder
   7. export function PageOneBuilder() {
   8. PageOne()
   9. }

   11. @Component
   12. export struct PageOne {
   13. @Consume('pageInfos') pageInfos: NavPathStack;
   14. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];
   15. scroller: Scroller = new Scroller();
   16. listScroller: Scroller = new Scroller();

   18. build() {
   19. HdsNavDestination() { // 创建HdsNavDestination组件
   20. Scroll(this.scroller) { // HdsNavDestination内容区设置可滚动容器组件，用于实现内容区滚动联动标题栏动态模糊样式
   21. Column() {
   22. Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
   23. .width('80%')
   24. .height(40)
   25. .margin({
   26. top: '5%',
   27. right: '50vp',
   28. left: '50vp',
   29. bottom: '5%'
   30. })
   31. .onClick(() => {
   32. this.pageInfos.pushPath({ name: 'pageTwo' }); // 将name指定的HdsNavDestination页面信息入栈
   33. })
   34. Button('popToName', { stateEffect: true, type: ButtonType.Capsule })
   35. .width('80%')
   36. .height(40)
   37. .margin(20)
   38. .onClick(() => {
   39. this.pageInfos.popToName('pageTwo'); // 回退路由栈到首个名为name的HdsNavDestination页面
   40. })
   41. Button('popToIndex', { stateEffect: true, type: ButtonType.Capsule })
   42. .width('80%')
   43. .height(40)
   44. .margin(20)
   45. .onClick(() => {
   46. this.pageInfos.popToIndex(1); // 回退路由栈到index指定的HdsNavDestination页面
   47. })
   48. Button('moveIndexToTop', { stateEffect: true, type: ButtonType.Capsule })
   49. .width('80%')
   50. .height(40)
   51. .margin(20)
   52. .onClick(() => {
   53. this.pageInfos.moveIndexToTop(1); // 将index指定的HdsNavDestination页面移到栈顶
   54. })
   55. Button('clear', { stateEffect: true, type: ButtonType.Capsule })
   56. .width('80%')
   57. .height(40)
   58. .margin(20)
   59. .onClick(() => {
   60. this.pageInfos.clear(); // 清除栈中所有页面
   61. })
   62. List({ space: 12, initialIndex: 0 }) {
   63. ForEach(this.arr, (item: number) => {
   64. ListItem() {
   65. Column() {
   66. Row({ space: 8 }) {
   67. Button() {
   68. SymbolGlyph($r('sys.symbol.wifi'))
   69. .fontColor([$r('sys.color.icon_on_primary')])
   70. .fontSize(24)
   71. }
   72. .width(35)
   73. .height(35)

   75. Text('list_' + item)
   76. .width('100%')
   77. .height(72)
   78. .fontSize(16)
   79. .fontWeight(500)
   80. }

   82. Divider().margin({ left: 40 })
   83. }
   84. }
   85. .height(56)
   86. .borderRadius(24)
   87. }, (item: number) => item.toString())
   88. }
   89. .edgeEffect(EdgeEffect.None)
   90. .scrollBar(BarState.Off)
   91. .width('100%')
   92. .height('100%')
   93. .cachedCount(3, true) // 设置列表中ListItem/ListItemGroup的预加载数量，列表穿透到标题栏下方不会消失
   94. .clip(false) // 设置不对子组件超出当前组件范围外的区域进行裁剪，使内容区可以穿透到标题栏下方
   95. .nestedScroll({ scrollForward: NestedScrollMode.PARENT_FIRST, scrollBackward: NestedScrollMode.PARENT_FIRST })
   96. }
   97. }
   98. .edgeEffect(EdgeEffect.Spring)
   99. .scrollBar(BarState.Off)
   100. .margin({ left: 16, right: 16 })
   101. .clip(false) // 设置不对子组件超出当前组件范围外的区域进行裁剪，使内容区可以穿透到标题栏下方
   102. }
   103. .titleBar({
   104. enableComponentSafeArea: true, // 将标题栏设置为组件级安全区，内容区可避让标题栏
   105. content: {
   106. // HdsNavigation标题栏内容区设置
   107. title: {
   108. // HdsNavigation标题栏标题设置
   109. mainTitle: 'PageOne',
   110. },
   111. // HdsNavigation标题栏返回按钮设置
   112. backIcon: {
   113. label: 'backIcon', // 无障碍播报内容
   114. componentId: 'backIconId', // 返回按钮id
   115. },
   116. menu: {
   117. // HdsNavigation标题栏菜单设置
   118. value: [{
   119. // 第一个菜单项内容设置
   120. content: {
   121. label: 'menu1',
   122. icon: $r('sys.symbol.ohos_star'),
   123. }
   124. }, {
   125. // 第二个菜单项内容设置
   126. content: {
   127. label: 'menu2',
   128. icon: $r('sys.symbol.ohos_circle'),
   129. },
   130. badge: {
   131. value: '66'
   132. }
   133. }]
   134. },
   135. }
   136. })
   137. .bindToNestedScrollable([{ parent: this.scroller, child: this.listScroller }]) // 绑定导航组件和可滚动容器组件
   138. }
   139. }
   ```
3. 在PageTwo页面创建二级导航组件。

   ```
   1. // PageTwo.ets
   2. // 模块导入
   3. // 从6.0.2(22)版本开始，无需手动导入HdsNavDestinationAttribute。具体请参考HdsNavDestination的导入模块说明。
   4. import { HdsNavDestination, HdsNavDestinationAttribute } from '@kit.UIDesignKit';

   6. @Builder
   7. export function PageTwoBuilder() {
   8. PageTwo()
   9. }

   11. @Component
   12. export struct PageTwo {
   13. @Consume('pageInfos') pageInfos: NavPathStack;
   14. private stack: NavPathStack | null = null;
   15. private name: string = '';
   16. scroller: Scroller = new Scroller();

   18. build() {
   19. HdsNavDestination() { // 创建HdsNavDestination组件
   20. Scroll(this.scroller) { // HdsNavDestination组件内容区设置
   21. Button('pushPathByName', { stateEffect: true, type: ButtonType.Capsule })
   22. .width('80%')
   23. .height(40)
   24. .margin(20)
   25. .onClick(() => {
   26. this.pageInfos.pushPathByName('pageOne', null); // 将name指定的HdsNavDestination页面信息入栈
   27. })
   28. }
   29. .align(Alignment.Top)
   30. .clip(false) // 设置不对子组件超出当前组件范围外的区域进行裁剪，使内容区可以穿透到标题栏下方
   31. .width('100%')
   32. .height('100%')
   33. .edgeEffect(EdgeEffect.Spring, { alwaysEnabled: true })
   34. }
   35. .titleBar({
   36. enableComponentSafeArea: true, // 将标题栏设置为组件级安全区，内容区可避让标题栏
   37. // HdsNavDestination组件标题栏设置
   38. content: {
   39. title: {
   40. mainTitle: 'PageTwo'
   41. },
   42. menu: {
   43. value: [{
   44. content: {
   45. label: 'menu1',
   46. icon: $r('sys.symbol.trunk'),
   47. }
   48. }]
   49. },
   50. },
   51. })
   52. .bindToScrollable([this.scroller]) // 绑定导航组件和可滚动容器组件
   53. .onReady((ctx: NavDestinationContext) => {
   54. // 在NavDestination中能够拿到传来的NavPathInfo和当前所处的NavPathStack
   55. try {
   56. this.name = ctx?.pathInfo?.name;
   57. this.stack = ctx.pathStack;
   58. } catch (e) {
   59. console.error(`testTag onReady catch exception code:
   60. ${JSON.stringify(e.code)}, message: ${JSON.stringify(e.message)}`);
   61. }
   62. })
   63. }
   64. }
   ```
4. 工程entry/src/main/module.json5文件中的“module”下新增如下配置，用于页面跳转。

   ```
   1. "routerMap": "$profile:route_map"
   ```
5. 工程entry/src/main/resources/base/profile目录下增加route\_map.json文件。

   ```
   1. {
   2. "routerMap": [
   3. {
   4. "name": "pageOne",
   5. "pageSourceFile": "src/main/ets/pages/PageOne.ets",
   6. "buildFunction": "PageOneBuilder",
   7. "data": {
   8. "description": "this is pageOne"
   9. }
   10. },
   11. {
   12. "name": "pageTwo",
   13. "pageSourceFile": "src/main/ets/pages/PageTwo.ets",
   14. "buildFunction": "PageTwoBuilder"
   15. }
   16. ]
   17. }
   ```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/lbJgI-rvTSOsUbBm4AwonA/zh-cn_image_0000002583438383.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234151Z&HW-CC-Expire=86400&HW-CC-Sign=3ADCBADEA7AC3B520417F1F63F22E5555338C8709AA5D8779B7471088DC20EAD "点击放大")
