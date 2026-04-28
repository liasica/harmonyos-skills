---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-development-scenarios-for-tabs
title: Tabs选项卡常见开发场景
breadcrumb: 最佳实践 > 布局与弹窗 > Tabs选项卡常见开发场景
category: best-practices
scraped_at: 2026-04-28T08:19:53+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:26f5a0073fcc7a176b4548214f7ae35822b5f5fd3184a6222f2e6ee98d64be9c
---

## 概述

在日常开发中，开发者经常遇到使用Tabs作为导航的场景，包括多层嵌套的Tabs、自定义Tabs样式、Tabs数据加载和动态变更显示的Tabs等。

开发者在实际开发中往往需要处理多个功能点的配合，以及与其他组件或数据的互动。为了帮助开发者更直观和全面地理解Tabs组件，本文通过将这些场景整合到一个应用首页的具体实例中，展示Tabs组件的各项功能及其协同效果，以及与其他组件或数据的联动。

本文将从以下几个方面进行介绍。

* [Tabs显示排版](bpta-development-scenarios-for-tabs.md#section166991845192018)
* [Tabs滑动](bpta-development-scenarios-for-tabs.md#section16601444172310)
* [Tabs页签加载/更新](bpta-development-scenarios-for-tabs.md#section1731618032613)
* [Tabs切换动效](bpta-development-scenarios-for-tabs.md#section595454372613)

## Tabs显示排版

在Tabs组件的应用场景中，开发者通常会自定义Tabs的布局和样式。本章节将介绍Tabs组件提供的几种常用的布局和样式功能。

### Tabs导航样式

常见的应用页签导航效果包括底部导航、顶部导航和侧边导航。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/ZvseOuFzS6qdvyNkPNOZog/zh-cn_image_0000002357892246.png?HW-CC-KV=V1&HW-CC-Date=20260428T001947Z&HW-CC-Expire=86400&HW-CC-Sign=71304052ABE90B4C58D3CAF48D5AFE6D20FB9967042F70F1CA734058CA72F22A "点击放大")

底部导航栏通常用于应用的主导航，其标签数量相对固定，不涉及TabBar滑动。作为应用的主导航，开发者通常会自定义TabBar的样式。底部导航栏可通过设置Tabs的barPosition参数来实现，需将barPosition设置为BarPosition.End。

```
1. Tabs({
2. barPosition: BarPosition.End,
3. // ...
4. }) {
5. // ...
6. }
```

[OutTabsComponent.ets](https://gitcode.com/harmonyos_samples/PureTabs/blob/master/entry/src/main/ets/view/OutTabsComponent.ets#L73-L121)

顶部导航栏主要用于主栏目的二级导航。由于二级导航可能包含较多的页签项，其TabBar通常设计为可滚动显示，并能动态调整所显示的页签。同样地，顶部导航栏通过将Tabs的barPosition参数设置为BarPosition.Start来实现。

```
1. Tabs({
2. barPosition: BarPosition.Start,
3. // ...
4. }) {
5. // ...
6. }
```

[InTabsComponent.ets](https://gitcode.com/harmonyos_samples/PureTabs/blob/master/entry/src/main/ets/view/InTabsComponent.ets#L234-L355)

侧边导航栏常见于横屏界面的导航。由于横屏界面尺寸规格的差异，导航条的页签需要适配宽度和高度，以确保更佳的显示效果。侧边导航栏的实现方式有所不同，需要将Tabs的vertical属性设置为true，而Tabs的barPosition参数则用于控制导航栏显示在左侧或右侧。

```
1. Tabs({
2. // ...
3. }) {
4. // ...
5. }
6. .vertical(false) // true to make the tab bar in side
```

[OutTabsComponent.ets](https://gitcode.com/harmonyos_samples/PureTabs/blob/master/entry/src/main/ets/view/OutTabsComponent.ets#L74-L127)

详情请参见[选项卡 (Tabs)](../harmonyos-guides/arkts-navigation-tabs.md)。

### 页签对齐方式

当页签数量不足，无法铺满屏幕宽度或高度，或者铺满后影响到UI美观时，Tabs提供了自定义导航条页签对齐方式的API。例如，在应用的二级导航中，如果页签较少，可以考虑将页签居左对齐。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/yO3oAB7CSASpGdfIC_jY4Q/zh-cn_image_0000002391492305.png?HW-CC-KV=V1&HW-CC-Date=20260428T001947Z&HW-CC-Expire=86400&HW-CC-Sign=668D0996BA3C28B0BE2ACF41D84DCC178052D786633E6D9C479C35266165E4EF "点击放大")

**实现原理**

通过[barModifier](../harmonyos-references/ts-container-tabs.md#tabsoptions15)属性设置tabBar的align参数，可以实现页签对齐布局效果。类似于文本对齐，开发者可以自行设置居中、居上、居下、居左或者居右对齐。

说明

* 只有在TabBar的barMode为BarMode.Scrollable时，这些设置才会生效。除此之外，还可以通过barModifier参数设置一系列的通用属性，具体参考：[TabsOptions](../harmonyos-references/ts-container-tabs.md#tabsoptions15)。
* 居上居下对齐仅在侧边导航栏中生效。若要控制顶部和底部导航栏中页签与顶部的距离，同样可以使用barModifier设置padding属性，以保持页签与TabBar顶部的特定间距。

**开发步骤**

定义tabBarModifier属性，并将其作为参数构造Tabs，然后通过tabBarModifier设置对齐方式。

```
1. @Component
2. export default struct InTabsComponent {
3. // ...
4. @State tabBarModifier: CommonModifier = new CommonModifier();
5. // ...
6. async aboutToAppear() {
7. // ...
8. this.tabBarModifier.margin({ right: 56 }).align(Alignment.Start);
9. // ...
10. }
11. // ...
12. build() {
13. // ...
14. Tabs({
15. // ...
16. barModifier: this.tabBarModifier
17. }) {
18. // ...
19. }
20. // ...
21. }
22. }
```

[InTabsComponent.ets](https://gitcode.com/harmonyos_samples/PureTabs/blob/master/entry/src/main/ets/view/InTabsComponent.ets#L28-L422)

### 自定义页签

对于底部导航栏，通常用于应用主页面的功能区分。为了更好的用户体验，开发者通常会自定义页签样式。开发者可以使用Tabs组件提供的定制页签样式的API，将页签自定义为图标加文字标题的形式，并且在选中和非选中的状态下，提供不同的样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/oZ8GSrLRS9ewCvGGhsS-gQ/zh-cn_image_0000002358052198.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001947Z&HW-CC-Expire=86400&HW-CC-Sign=E036AF99EB94FFB2017B2A2B8720BF039EDCBBF0454A946A7E3BDBD8C24ABBE6 "点击放大")

**实现原理**

Tabs组件的[tabBar()](../harmonyos-references/ts-container-tabcontent.md#tabbar)方法接受联合类型的参数，可以将由@Builder修饰的UI构建函数作为参数传入，以自定义TabBar的样式。因此，开发者可以定义一个UI构建函数tabBuilder()，作为参数传递给[tabBar()](../harmonyos-references/ts-container-tabcontent.md#tabbar)方法。由于选中的页签和未选中的页签需要不同的样式，还需定义一个由@State修饰的数值型变量currentIndex，用于在tabBuilder()函数中判断当前页签是否被选中。当currentIndex发生变化时，能够触发tabBar样式的更新。最后，注册Tabs组件的onchange函数，在该函数中更新currentIndex的值。

**开发步骤**

1. 定义currentIndex属性。

   ```
   1. @Component
   2. export default struct OutTabsComponent {
   3. @State currentIndex: number = 0;
   4. // ...
   5. }
   ```

   [OutTabsComponent.ets](https://gitcode.com/harmonyos_samples/PureTabs/blob/master/entry/src/main/ets/view/OutTabsComponent.ets#L22-L155)
2. 定义@Builder装饰器修饰的自定义样式构建方法tabBuilder()。

   ```
   1. @Builder
   2. tabBuilder(index: number, name: string | Resource, icon: Resource) {
   3. Column() {
   4. // set special styles if selected

   6. SymbolGlyph(icon).fontColor([this.currentIndex === index
   7. ? $r('app.color.out_tab_bar_font_active_color')
   8. : $r('app.color.out_tab_bar_font_inactive_color')])
   9. .fontSize(25)

   11. Text(name)
   12. .margin({ top: 4 })
   13. .fontSize(10)
   14. .fontColor(this.currentIndex === index
   15. ? $r('app.color.out_tab_bar_font_active_color')
   16. : $r('app.color.out_tab_bar_font_inactive_color'))
   17. }
   18. .justifyContent(FlexAlign.Center)
   19. .height(Constants.FULL_HEIGHT)
   20. .width(Constants.FULL_WIDTH)
   21. .padding({ bottom: 60 })
   22. // .backgroundColor($r('app.color.out_tab_bar_background_color'))
   23. }
   ```

   [OutTabsComponent.ets](https://gitcode.com/harmonyos_samples/PureTabs/blob/master/entry/src/main/ets/view/OutTabsComponent.ets#L43-L69)
3. 将tabBuilder()方法传入Tabs，并在Tabs注册onChange()函数，并在其中更新currentIndex属性。

   ```
   1. Tabs({
   2. // ...
   3. }) {
   4. TabContent() {
   5. InTabsComponent({ switchNext: this.switchNext })
   6. }.tabBar(this.tabBuilder(0, $r('app.string.out_bar_text_home'), $r('sys.symbol.house')))
   7. // ...
   8. }
   9. // ...
   10. .onChange((index: number) => {
   11. this.currentIndex = index;
   12. })
   ```

   [OutTabsComponent.ets](https://gitcode.com/harmonyos_samples/PureTabs/blob/master/entry/src/main/ets/view/OutTabsComponent.ets#L75-L138)

### Tabs吸顶

在一些二级导航栏页面中，二级页签的内容上方通常会放置一些banner位或其他优先级较高的内容，并且在向上滑动时会退出显示区域。为了提供更好的用户体验，建议在上划的过程中，导航条能够吸附在顶部，便于用户进行内容切换。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/JXvpRxQlR_GVTcaOWib0EA/zh-cn_image_0000002391532177.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001947Z&HW-CC-Expire=86400&HW-CC-Sign=D299AB6F6AB251759956C2D12BB50CB993A8E4449B9AC7C72F96A0622522964C "点击放大")

**实现原理**

开发者可以通过设置滑动组件的属性[nestedScroll](../harmonyos-references/ts-container-scroll.md#nestedscroll10)来控制父子组件的滑动顺序，从而实现吸顶效果。具体而言，需确保TabContent内容是可滑动的，并且Tabs的上层父组件也必须是可滑动的。为内容组件添加[nestedScroll](../harmonyos-references/ts-container-scroll.md#nestedscroll10)属性，设置为当向上滑动时父组件先动，而向下滑动时自己先动，从而实现滑动吸顶效果。

**开发步骤**

在Tabs父组件上嵌套Scroll组件，TabContent中的List组件显示内容，List组件本身是可滑动的，仅需设置其滑动触发行为即可。

```
1. Scroll() {
2. Column() {
3. BannerComponent()

5. Stack({ alignContent: Alignment.TopEnd }) {
6. // ...
7. Column() {
8. Tabs({
9. // ...
10. }) {
11. // bind selected tabs to ui
12. ForEach(this.selectTabsViewModel.selectedTabs, (tab: TabItemViewModel, index: number) => {
13. if (index === this.selectTabsViewModel.selectedTabs.length - 1) {
14. TabContent() {
15. List({ space: 10 }) {
16. // ...
17. }
18. // ...
19. // set the sliding behavior to move up parent first, and move down self first
20. .nestedScroll({
21. scrollForward: NestedScrollMode.PARENT_FIRST,
22. scrollBackward: NestedScrollMode.SELF_FIRST
23. })
24. }
25. // ...
26. } else {
27. // ...
28. }
29. }, (tab: TabItemViewModel, index: number) => index + '_' + JSON.stringify(tab))
30. }
31. // ...
32. }
33. .width(Constants.FULL_WIDTH)
34. .height(Constants.FULL_HEIGHT)
35. .backgroundColor($r('app.color.out_tab_bar_background_color'))
36. }
37. }
38. }
```

[InTabsComponent.ets](https://gitcode.com/harmonyos_samples/PureTabs/blob/master/entry/src/main/ets/view/InTabsComponent.ets#L179-L405)

### TabsBar显示效果

在某些UI设计风格中，可能需要为TabBar采用特殊样式，比如首页导航栏的毛玻璃背景效果等。

* 通过设置Tabs组件的[barOverlap](../harmonyos-references/ts-container-tabs.md#baroverlap10)属性，可以实现TabBar变模糊并叠加在TabContent之上，并且配合[barBackgroundBlurStyle](../harmonyos-references/ts-container-tabs.md#barbackgroundblurstyle11)属性实现毛玻璃效果。详情请参见[TabBar背景模糊效果](../architecture-guides/tab_bar_blur-0000002257193008.md)。

  ```
  1. Tabs({
  2. // ...
  3. }) {
  4. // ...
  5. }
  6. // ...
  7. .barOverlap(true)
  8. .barBackgroundBlurStyle(BlurStyle.Thin)
  ```

  [OutTabComponent.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkUI/PureTabsExt/entry/src/main/ets/view/OutTabComponent.ets#L62-L119)

  底部导航栏覆盖在内容上方，并具有毛玻璃效果。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/7PL_HASDSq-_ev2cZ8aDDw/zh-cn_image_0000002357892250.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001947Z&HW-CC-Expire=86400&HW-CC-Sign=F06DA4CD418F5F28EAB5724DEA4CA0C67BC3380043FBE02557B5A54D6EEF5C24 "点击放大")
* 通过[barModifier](../harmonyos-references/ts-container-tabs.md#tabsoptions15)设置tabBar的clip属性，实现页签超出tabBar区域显示效果。详情请参见[页签超出TabBar区域显示](../harmonyos-references/ts-container-tabs.md#示例15页签超出tabbar区域显示)。

  ```
  1. @Component
  2. export default struct OutTabComponent {
  3. // ...
  4. private controller: TabsController = new TabsController();

  6. aboutToAppear(): void {
  7. this.tabBarModifier.clip(false);
  8. }

  10. // ...

  12. build() {
  13. Column() {
  14. Tabs({
  15. // ...
  16. barModifier: this.tabBarModifier
  17. }) {
  18. // ...
  19. }
  20. // ...

  22. }
  23. .width('100%')
  24. .height('calc(100% + 60vp)')
  25. .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
  26. }
  27. }
  ```

  [OutTabComponent.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkUI/PureTabsExt/entry/src/main/ets/view/OutTabComponent.ets#L21-L128)

  底层导航栏图标可超出导航条范围。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/rLbDmFLoQpmIM6xY1OTwtg/zh-cn_image_0000002391492309.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001947Z&HW-CC-Expire=86400&HW-CC-Sign=13374D041213B9C71CD788362DCA6988627E37574718CDF49F5AB0DA1F3EBA0B "点击放大")
* 通过配置[fadingEdge](../harmonyos-references/ts-container-tabs.md#fadingedge10)(true)实现TabBar边缘渐隐。详情请参见[设置TabBar渐隐](../harmonyos-references/ts-container-tabs.md#示例5设置tabbar渐隐)。

  ```
  1. Tabs({controller: this.subController}){
  2. // ...
  3. }
  4. .fadingEdge(this.isFadingEdge) // true set tab bar edge fade
  ```

  [InTabComponent.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkUI/PureTabsExt/entry/src/main/ets/view/InTabComponent.ets#L118-L134)

  顶部导航栏页签靠近两侧会模糊化。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/VIwqR3RZTPqBQBEPGZ07zA/zh-cn_image_0000002358052202.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001947Z&HW-CC-Expire=86400&HW-CC-Sign=B754A828D41C075D118DCFC5A6C99557FEBEF153127A4C8E78A80A77461AB554 "点击放大")
* 通过TabsController的[setTabBarTranslate()](../harmonyos-references/ts-container-tabs.md#settabbartranslate13)、[setTabBarOpacity()](../harmonyos-references/ts-container-tabs.md#settabbaropacity13)方法可以设置TabBar偏移量及透明度。详情请参见[设置TabBar平移距离和不透明度](../harmonyos-references/ts-container-tabs.md#示例12设置tabbar平移距离和不透明度)。

  ```
  1. @Component
  2. export default struct InTabComponent {
  3. // ...
  4. private subController: TabsController = new TabsController();

  6. onDidBuild(): void {
  7. if (this.isSetTabBarTranslateAndOpacity) {
  8. this.subController.setTabBarTranslate({x:-20,y:30});
  9. this.subController.setTabBarOpacity(0.5);
  10. }
  11. }
  12. // ...

  14. build() {
  15. Tabs({controller: this.subController}){
  16. // ...
  17. }
  18. // ...
  19. .barMode(BarMode.Scrollable)
  20. }
  21. }
  ```

  [InTabComponent.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkUI/PureTabsExt/entry/src/main/ets/view/InTabComponent.ets#L20-L141)

  顶部导航栏位置向左下偏移，并且呈现半透明效果。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/ozp8JlWIQMyzjN1uC9OPaw/zh-cn_image_0000002391532181.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001947Z&HW-CC-Expire=86400&HW-CC-Sign=DB48765144AD959B2590294705B34763457103CC1557730253072A1A614849E4 "点击放大")

说明

在以下情况下，该设置无法生效：当显示内容过长时，通常会将其置于可滚动容器组件中，并在向上滑动时隐藏TabBar，向下滑动时显示。此时，会使用[bindTabsToScrollable](../harmonyos-references/arkts-apis-uicontext-uicontext.md#bindtabstoscrollable13)或[bindTabsToNestedScrollable](../harmonyos-references/arkts-apis-uicontext-uicontext.md#bindtabstonestedscrollable13)等接口将Tabs组件与可滚动容器组件绑定。由于TabBar的控制与滚动组件联动，通过setTabBarOpacity接口设置的TabBar偏移量和不透明度将不再生效。

## Tabs滑动

Tabs组件在用户交互方面提供了丰富的特性，其中与滑动动作相关的交互尤为常见。下文将介绍几种与Tabs和滑动动作相关的特性。

### 双层Tabs嵌套滑动

在应用开发中，开发者经常遇到多层Tabs嵌套使用的场景。如果父子Tabs组件均需滑动切换时，开发者需要对父子Tabs的滑动切换行为进行约束，以避免冲突。通常做法是，让滑动操作优先切换子Tabs页签，当子Tabs页签切换到最后一个后，再触发父Tabs的页签切换。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/eNkw7hJTSBO5h2dfpwsMcg/zh-cn_image_0000002357892254.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001947Z&HW-CC-Expire=86400&HW-CC-Sign=6ADB054A81F2BD363AA015D7BB624C0D06250F3C7E893ABC49D3902009D85E59 "点击放大")

**实现原理**

可以通过[PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)结合[TabsController](../harmonyos-references/ts-container-tabs.md#tabscontroller)的changeIndex()方法实现双层Tabs的切换。具体操作为：开启子Tabs的滑动切换功能，同时关闭父Tabs的滑动切换。在子Tabs的第一个或者最后一个页面上添加PanGesture事件处理函数，用于判断滑动方向，并根据滑动方向使用TabsController的changeIndex()方法切换到父Tabs的相应页签。这样一来，子Tabs的中间页签滑动时，仅会触发子Tabs页签的切换，而最后一个页签的滑动则会通过changeIndex()方法间接触发父Tabs页签的切换。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/MzHRLpsTR3KvrpPt-wNczw/zh-cn_image_0000002391492313.png?HW-CC-KV=V1&HW-CC-Date=20260428T001947Z&HW-CC-Expire=86400&HW-CC-Sign=6C059579380283FB486BB1D14FC4C04CA7D9C591805F8CED92B60A29FFD7D9D2 "点击放大")

**开发步骤**

1. 外层Tabs组件中定义[TabsController](../harmonyos-references/ts-container-tabs.md#tabscontroller)属性，以及内层Tabs双向绑定的状态属性变量switchNext及其监听函数。当监听到需要切换页签时，利用TabsController切换到对应页签。因为本示例外层Tabs和内层Tabs封装到不同的自定义组件中了，所以需要@Link修饰的switchNext变量作为父子组件的交互媒介。

   ```
   1. @Component
   2. export default struct OutTabsComponent {
   3. // ...
   4. @State @Watch('onchangeSwitchNext') switchNext: boolean = false;
   5. // ...
   6. onchangeSwitchNext() {
   7. if (this.switchNext) {
   8. this.switchNext = false;
   9. this.tabsController.changeIndex(1);
   10. }
   11. }
   12. // ...
   13. build() {
   14. Tabs({
   15. // ...
   16. controller: this.tabsController,
   17. }) {
   18. TabContent() {
   19. InTabsComponent({ switchNext: this.switchNext })
   20. }.tabBar(this.tabBuilder(0, $r('app.string.out_bar_text_home'), $r('sys.symbol.house')))
   21. // ...
   22. }
   23. // ...
   24. }
   25. }
   ```

   [OutTabsComponent.ets](https://gitcode.com/harmonyos_samples/PureTabs/blob/master/entry/src/main/ets/view/OutTabsComponent.ets#L21-L154)
2. 内层Tabs组件在最后一个TabContent中注册滑动事件处理函数，监听向左滑动作，触发时修改switchNext变量值传递给外层Tabs组件触发切换。

   ```
   1. @Component
   2. export default struct InTabsComponent {
   3. // ...
   4. @Link switchNext: boolean;
   5. // ...
   6. build() {
   7. // ...
   8. Tabs({
   9. // ...
   10. }) {
   11. // bind selected tabs to ui
   12. ForEach(this.selectTabsViewModel.selectedTabs, (tab: TabItemViewModel, index: number) => {
   13. if (index === this.selectTabsViewModel.selectedTabs.length - 1) {
   14. TabContent() {
   15. // ...
   16. }
   17. .tabBar(this.tabBuilder(index, tab))
   18. .gesture(PanGesture(new PanGestureOptions({ direction: PanDirection.Left })).onActionStart(() => {
   19. this.switchNext = true;
   20. }))
   21. // ...
   22. } else {
   23. // ...
   24. }
   25. }, (tab: TabItemViewModel, index: number) => index + '_' + JSON.stringify(tab))
   26. }
   27. // ...
   28. }
   29. }
   ```

   [InTabsComponent.ets](https://gitcode.com/harmonyos_samples/PureTabs/blob/master/entry/src/main/ets/view/InTabsComponent.ets#L30-L424)
3. 注意滑动切换在自定义切换动画场景下失效，故需要注释掉切换动画函数注册。

   ```
   1. Tabs({
   2. barPosition: BarPosition.Start,
   3. controller: this.subsController,
   4. barModifier: this.tabBarModifier
   5. }) {
   6. // ...
   7. }
   8. // add animation function
   9. .customContentTransition(this.customContentTransition) // comment out to slide to switch
   ```

   [InTabsComponent.ets](https://gitcode.com/harmonyos_samples/PureTabs/blob/master/entry/src/main/ets/view/InTabsComponent.ets#L229-L367)

### 可滚动Tabs页签栏+更多按钮

可滚动页签栏通常设置在顶部或侧边导航栏，当内容分类较多，屏幕显示区域无法完全展示所有分类页签时，该页签栏允许用户通过滚动来访问隐藏的页签内容。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/4Wytw1vQSEaP0bebtqg87A/zh-cn_image_0000002358052206.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001947Z&HW-CC-Expire=86400&HW-CC-Sign=2186572CAAAB01D4AE2950E1DDEAA8AF023A5AC2C65BF7B4FE875665A9BD697F "点击放大")

**实现原理**

通过将Tabs组件的[barMode](../harmonyos-references/ts-container-tabs.md#barmode)属性设置为BarMode.Scrollable，可以实现可滚动的页签栏。若要实现添加更多按钮的效果，可以通过Stack布局结合[barModifier](../harmonyos-references/ts-container-tabs.md#tabsoptions15)功能实现。具体做法是在Tabs组件的TabBar位置的末端上层利用Stack布局添加更多按钮，并且点击该按钮时可以弹出窗口，在弹窗中自定义需要显示的页签。

**开发步骤**

设置barMode属性为BarMode.Scrollable，并利用[Stack](../harmonyos-guides/arkts-layout-development-stack-layout.md)布局在TabBar右上角添加更多按钮。

```
1. Stack({ alignContent: Alignment.TopEnd }) {
2. Row() {
3. Image($r('app.media.more'))
4. // ...
5. .onClick(() => {
6. this.showSelectTabsComponent = !this.showSelectTabsComponent;
7. })
8. }
9. // ...
10. .zIndex(1)
11. .bindSheet($$this.showSelectTabsComponent, this.sheetBuilder(), {
12. detents: [SheetSize.MEDIUM, SheetSize.MEDIUM, 500],
13. preferType: SheetType.BOTTOM,
14. title: { title: $r('app.string.bind_sheet_title') },
15. onWillDismiss: (dismissSheetAction: DismissSheetAction) => {
16. // update tab when closing modal box
17. this.selectTabsViewModel.updateSelectedTabs();
18. if (this.selectTabsViewModel.selectedTabs.length > 0) {
19. this.subsController.changeIndex(0);
20. }
21. dismissSheetAction.dismiss();
22. }
23. })
24. Column() {
25. Tabs({
26. // ...
27. }) {
28. // ...
29. }
30. // ...
31. .barMode(BarMode.Scrollable)
32. // ...
33. }
34. .width(Constants.FULL_WIDTH)
35. .height(Constants.FULL_HEIGHT)
36. .backgroundColor($r('app.color.out_tab_bar_background_color'))
37. }
```

[InTabsComponent.ets](https://gitcode.com/harmonyos_samples/PureTabs/blob/master/entry/src/main/ets/view/InTabsComponent.ets#L184-L402)

### 禁用TabContent左右滑动

默认情况下，导航栏支持滑动切换。当存在多级导航栏嵌套或导航栏中的其他组件需要占用滑动动作时，为避免滑动响应冲突，开发者可选择禁用Tabs组件的滑动切换功能。通过将Tabs组件的[scrollable](../harmonyos-references/ts-container-tabs.md#scrollable)属性设置为false，可以禁止通过滑动TabContent来切换页签。同样，若想禁用边缘回弹效果，可将[edgeEffect](../harmonyos-references/ts-container-tabs.md#edgeeffect12)的值设置为EdgeEffect.None。

示例代码：

```
1. build() {
2. Tabs({
3. // ...
4. }) {
5. // ...
6. }
7. // ...
8. .scrollable(true) // false to disable scroll to switch
9. // .edgeEffect(EdgeEffect.None) // disables edge springback
10. // ...
11. }
```

[OutTabsComponent.ets](https://gitcode.com/harmonyos_samples/PureTabs/blob/master/entry/src/main/ets/view/OutTabsComponent.ets#L69-L151)

## Tabs页签加载/更新

在使用Tabs组件进行开发时，特别是当Tabs组件作为二级导航使用时，业务需求往往需要对Tabs的标签页进行更精细的控制。下文将介绍几种定制标签页显示逻辑的场景。

### 显示指定页签与预加载

Tabs组件的TabContent默认在首次切换到该标签页时加载。如果TabContent中的内容或初始化逻辑较为复杂，加载速度较慢，则会影响标签页切换的流畅性，进而影响用户体验。此时，如果应用能在切换前预加载相应的标签页，将显著提升使用流畅度。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/XIGIQzPKQ6SL3Omfpf62Vw/zh-cn_image_0000002391532185.png?HW-CC-KV=V1&HW-CC-Date=20260428T001947Z&HW-CC-Expire=86400&HW-CC-Sign=E1A723663786E04E98DA80A37F2182F189F42308FD5C08BA8866F27ADC111D76 "点击放大")

**实现原理**

通过[TabController](../harmonyos-references/ts-container-tabs.md#tabscontroller)的[preloadItem()](../harmonyos-references/ts-container-tabs.md#preloaditems12)方法可以预加载指定子节点。该方法参数为需要预加载的index数组，无参调用此方法时，会一次性加载所有指定的子节点。因此，为了性能考虑，建议分批加载子节点。代码示例这里做法是当切换到某页签时，预加载所选页签左右两侧的页签内容。

**开发步骤**

定义subsController属性，并在Tabs的onChange函数中调用[preloadItem()](../harmonyos-references/ts-container-tabs.md#preloaditems12)预加载当前页签两侧页签。

```
1. @Component
2. export default struct InTabsComponent {
3. // ...
4. private subsController: TabsController = new TabsController();
5. // ...
6. build() {
7. // ...
8. Tabs({
9. // ...
10. controller: this.subsController,
11. // ...
12. }) {
13. // ...
14. }
15. // ...
16. .onChange((index: number) => {
17. this.focusIndex = index;
18. this.tabBarItemScroller.scrollToIndex(index, true, ScrollAlign.CENTER);
19. // preload the left and right item
20. let preloadItems: number[] = [];
21. if (index - 1 >= 0) {
22. preloadItems.push(index - 1);
23. }
24. if (index + 1 < this.selectTabsViewModel.selectedTabs.length) {
25. preloadItems.push(index + 1);
26. }
27. this.subsController.preloadItems(preloadItems);
28. })
29. // ...
30. }
31. }
```

[InTabsComponent.ets](https://gitcode.com/harmonyos_samples/PureTabs/blob/master/entry/src/main/ets/view/InTabsComponent.ets#L29-L423)

### 切换到指定页签

Tabs组件除了自带的滑动切换和点击切换功能外，还提供了两种可编程方式来切换页签。第一种是通过调用TabsController的[changeIndex()](../harmonyos-references/ts-container-tabs.md#changeindex)方法，切换到指定的index；第二种是定义一个由@State修饰的变量currentIndex，并将其绑定到Tabs，通过修改currentIndex的值来触发页签切换。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/KSYPazbmS3KRYn7EBeZZVQ/zh-cn_image_0000002357892258.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001947Z&HW-CC-Expire=86400&HW-CC-Sign=C3F5DDA51DC3E6C6CD8930905CF101AA0F338018FC6319B86708AA4B575B8C16 "点击放大")

**开发步骤**

定义currentIndex变量和tabController属性，并绑定到Tabs。在按钮onClick函数中，调用tabController.changeIndex()或者直接修改currentIndex变量切换页签。

```
1. @Component
2. export default struct SwitchTabComponent {
3. // ...
4. @State currentIndex: number = 0;
5. private tabController: TabsController = new TabsController();

7. // ...

9. build() {
10. Column() {
11. Row() {
12. Button('Previous Tab')
13. .onClick(() => {
14. this.tabController.changeIndex((this.currentIndex + 3) % 4); // call tabController.changeIndex() to switch tab
15. })
16. // ...

18. Button('Next Tab')
19. .onClick(() => {
20. this.currentIndex = (this.currentIndex + 1) % 4; // change currentIndex to switch tab
21. })
22. // ...
23. }

25. Tabs({
26. controller: this.tabController,
27. index: $$this.currentIndex // use $$ for two-way data binding
28. }) {
29. // ...
30. }
31. }

33. }
34. }
```

[SwitchTabComponent.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkUI/PureTabsExt/entry/src/main/ets/view/SwitchTabComponent.ets#L20-L117)

此外，Tabs可注册切换前的处理函数，进一步控制切换行为。详情请参见[切换至指定页签](../harmonyos-guides/arkts-navigation-tabs.md#切换至指定页签)。

### 增删Tabs页签

在日常的应用开发中，经常需要实现用户自定义选择频道的功能。通常，这些自定义选择的频道会通过Tabs组件来展示，因此需要动态地更新Tabs的页签。本示例设计了一对父子组件来演示这一功能。父组件负责显示页签及其内容，并在页签栏的最右侧设置一个“更多”按钮。点击此按钮会弹出一个窗口，供用户选择需要显示的页签。该弹窗内容由子组件提供，关闭弹窗后，父组件的页签将被更新。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/bWMewaNYQ46qK6l05_NvJA/zh-cn_image_0000002391492317.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001947Z&HW-CC-Expire=86400&HW-CC-Sign=4B3843A51556B4D9562789F9768EDB53B35A2820E6724D4F4693610B27F4028F "点击放大")

**实现原理**

定义selectTabsViewModel对象，其中的数组allTabs表示所有可选择页签，数组selectedTabs表示选中的需要显示的页签，并通过[@Link](../harmonyos-guides/arkts-link.md)绑定到父组件InTabComponent和子组件SelectTabsComponent中。子组件SelectTabsComponent作为一个弹窗用于选择需要显示的页签。选择完成后，关闭弹窗并更新 selectTabsViewModel对象中的选中页签数组 selectedTabs，以触发父组件InTabComponent的页签更新。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/NyDSPX8_SUCO_4xH5ubOXQ/zh-cn_image_0000002358052210.png?HW-CC-KV=V1&HW-CC-Date=20260428T001947Z&HW-CC-Expire=86400&HW-CC-Sign=7E5CE1D94FFA45FC4148726CD778B87080EF1EBD0D1501E74093440054236C9D "点击放大")

**开发步骤**

1. 定义SelectTabsViewModel类，包含所有可选择页签数组allTabs属性，和需要显示的页签数组selectedTabs属性，及更新显示页签数组的方法updateSelectedTabs()。

   ```
   1. @Observed
   2. class TabItemArray extends Array<TabItemViewModel> {
   3. }

   5. @Observed
   6. export default class SelectTabsViewModel {
   7. allTabs: TabItemArray = new TabItemArray();
   8. selectedTabs: TabItemArray = new TabItemArray();
   9. // ...

   11. async loadTabs(ctx: Context) {
   12. // ...
   13. }

   15. // apply changes to the selected tabs
   16. updateSelectedTabs() {
   17. let tempTabs: TabItemViewModel[] = [];
   18. for (let tab of this.allTabs) {
   19. if (tab.isChecked) {
   20. tempTabs.push(tab);
   21. }
   22. }
   23. this.selectedTabs = tempTabs;
   24. }
   25. }
   ```

   [SelectTabsViewModel.ets](https://gitcode.com/harmonyos_samples/PureTabs/blob/master/entry/src/main/ets/viewmodel/SelectTabsViewModel.ets#L20-L58)
2. 在InTabsComponent中定义selectTabsViewModel属性，并且在aboutToAppear()方法中初始化。

   ```
   1. @Component
   2. export default struct InTabsComponent {
   3. @State selectTabsViewModel: SelectTabsViewModel = new SelectTabsViewModel();
   4. // ...
   5. async aboutToAppear() {
   6. // ...

   8. await this.selectTabsViewModel.loadTabs(this.ctx);
   9. // ...
   10. }
   11. // ...
   12. }
   ```

   [InTabsComponent.ets](https://gitcode.com/harmonyos_samples/PureTabs/blob/master/entry/src/main/ets/view/InTabsComponent.ets#L31-L425)
3. 利用ForEach组件将selectTabsViewModel.selectedTabs属性绑定到Tabs的页签上。

   ```
   1. Tabs({
   2. // ...
   3. }) {
   4. // bind selected tabs to ui
   5. ForEach(this.selectTabsViewModel.selectedTabs, (tab: TabItemViewModel, index: number) => {
   6. if (index === this.selectTabsViewModel.selectedTabs.length - 1) {
   7. TabContent() {
   8. // ...
   9. }
   10. .tabBar(this.tabBuilder(index, tab))
   11. // ...
   12. } else {
   13. // ...
   14. }
   15. }, (tab: TabItemViewModel, index: number) => index + '_' + JSON.stringify(tab))
   16. }
   ```

   [InTabsComponent.ets](https://gitcode.com/harmonyos_samples/PureTabs/blob/master/entry/src/main/ets/view/InTabsComponent.ets#L231-L362)
4. 在更多按钮的弹窗中初始化SelectTabsComponent，并将selectTabsViewModel属性作为双向绑定属性传入。在关闭弹窗处理函数中调用selectTabsViewModel.updateSelectedTabs()方法，更新需要显示的组件。

   ```
   1. @Builder
   2. sheetBuilder() {
   3. //select tabs to show
   4. SelectTabsComponent({ selectTabsViewModel: this.selectTabsViewModel })
   5. }
   6. build() {
   7. Scroll() {
   8. Column() {
   9. BannerComponent()

   11. Stack({ alignContent: Alignment.TopEnd }) {
   12. Row() {
   13. Image($r('app.media.more'))
   14. // ...
   15. .onClick(() => {
   16. this.showSelectTabsComponent = !this.showSelectTabsComponent;
   17. })
   18. }
   19. // ...
   20. .zIndex(1)
   21. .bindSheet($$this.showSelectTabsComponent, this.sheetBuilder(), {
   22. detents: [SheetSize.MEDIUM, SheetSize.MEDIUM, 500],
   23. preferType: SheetType.BOTTOM,
   24. title: { title: $r('app.string.bind_sheet_title') },
   25. onWillDismiss: (dismissSheetAction: DismissSheetAction) => {
   26. // update tab when closing modal box
   27. this.selectTabsViewModel.updateSelectedTabs();
   28. if (this.selectTabsViewModel.selectedTabs.length > 0) {
   29. this.subsController.changeIndex(0);
   30. }
   31. dismissSheetAction.dismiss();
   32. }
   33. })
   34. // ...
   35. }
   36. }
   37. }
   38. // ...
   39. }
   ```

   [InTabsComponent.ets](https://gitcode.com/harmonyos_samples/PureTabs/blob/master/entry/src/main/ets/view/InTabsComponent.ets#L166-L418)
5. 在SelectTabsComponent中将selectTabsViewModel.allTabs属性渲染成toggle组件，并且注册toggle组件的切换处理函数onChange()，在其中修改该页签的选择状态isChecked属性，供更新显示页签方法selectTabsViewModel.updateSelectedTabs()使用。

   ```
   1. @Component
   2. export default struct SelectTabsComponent {
   3. @State checkedChange: boolean = false;
   4. @Link selectTabsViewModel: SelectTabsViewModel;

   6. build() {
   7. Grid() {
   8. ForEach(this.selectTabsViewModel.allTabs, (tab: TabItemViewModel) => {
   9. GridItem() {
   10. Row() {
   11. Toggle({ type: ToggleType.Button, isOn: tab.isChecked }) {
   12. // ...
   13. }
   14. // ...
   15. .onChange((isOn: boolean) => {
   16. tab.isChecked = isOn;
   17. this.checkedChange = !this.checkedChange;
   18. })
   19. }
   20. }
   21. }, (tab: TabItemViewModel, index: number) => index + '_' + JSON.stringify(tab))
   22. }
   23. .columnsTemplate(('1fr 1fr 1fr 1fr') as string)
   24. .height(Constants.FULL_HEIGHT)
   25. }
   26. }
   ```

   [SelectTabsComponent.ets](https://gitcode.com/harmonyos_samples/PureTabs/blob/master/entry/src/main/ets/view/SelectTabsComponent.ets#L21-L68)

## Tabs切换动效

### TabContent切换动画

Tabs 自带的页签切换动画为平移动画。若开发者需实现更高级的动画效果，可通过Tabs提供的API实现自定义动画。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/LX6-_Kf6SueUtgF7K43F8A/zh-cn_image_0000002391532189.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001947Z&HW-CC-Expire=86400&HW-CC-Sign=946A45BA65D29C9D50298D78FDB83275D0FBA7A3EA2E38FC0248A3AEB19C7742 "点击放大")

**实现原理**

使用[customContentTransition()](../harmonyos-references/ts-container-tabs.md#customcontenttransition11)函数来自定义Tabs页面的切换动画。本场景采用属性动画实现，开发者可以定义由@State修饰的可动画属性，并在build()方法中将这些属性绑定到对应的页签上。这里，淡入淡出动画选用了TabContent的尺寸属性scale和透明度属性opacity作为生成动画属性。然后，在[customContentTransition()](../harmonyos-references/ts-container-tabs.md#customcontenttransition11)函数中，设置动画的起始帧和结束帧对应的可动画属性值，系统将自动补全中间帧从而生成动画。关于属性动画详情可参考：[实现属性动画](../harmonyos-guides/arkts-attribute-animation-apis.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/CqWYxNgiQxOOI-IaLGZtqw/zh-cn_image_0000002357892262.png?HW-CC-KV=V1&HW-CC-Date=20260428T001947Z&HW-CC-Expire=86400&HW-CC-Sign=B8113BCAE61F1369E88716052A04BCAA305468745E6506A3A03F395B5E80B301 "点击放大")

说明

* 使用自定义切换动画时，Tabs组件的默认切换动画将被禁用，且页面将无法通过手势滑动切换。
* 将customContentTransition设置为undefined表示不使用自定义切换动画，继续使用组件自带的默认切换动画。
* 当前自定义切换动画不支持中途打断。
* 目前，自定义切换动画仅支持以下两种触发场景：点击页签或通过调用TabsController.changeIndex()方法。

**开发步骤**

1. 定义动画所需用到的属性数组。

   ```
   1. @Component
   2. export default struct InTabsComponent {
   3. // ...
   4. @State scaleList: number[] = [];
   5. @State opacityList: number[] = [];
   6. // ...
   7. }
   ```

   [InTabsComponent.ets](https://gitcode.com/harmonyos_samples/PureTabs/blob/master/entry/src/main/ets/view/InTabsComponent.ets#L32-L426)
2. 将属性数组绑定到对应的页签上。

   ```
   1. Tabs({
   2. // ...
   3. }) {
   4. // bind selected tabs to ui
   5. ForEach(this.selectTabsViewModel.selectedTabs, (tab: TabItemViewModel, index: number) => {
   6. if (index === this.selectTabsViewModel.selectedTabs.length - 1) {
   7. TabContent() {
   8. // ...
   9. }
   10. // ...
   11. // bind animation properties
   12. .opacity(this.opacityList[index])
   13. .scale({
   14. x: this.scaleList[index], y: this.scaleList[index]
   15. })
   16. } else {
   17. // ...
   18. }
   19. }, (tab: TabItemViewModel, index: number) => index + '_' + JSON.stringify(tab))
   20. }
   ```

   [InTabsComponent.ets](https://gitcode.com/harmonyos_samples/PureTabs/blob/master/entry/src/main/ets/view/InTabsComponent.ets#L232-L363)
3. 定义Tabs的自定义转场函数。

   ```
   1. @Component
   2. export default struct InTabsComponent {
   3. // ...
   4. @State scaleList: number[] = [];
   5. @State opacityList: number[] = [];
   6. // ...
   7. private animateDuration: number = 1000;
   8. private animateTimeout: number = 1000;
   9. private customContentTransition: (from: number, to: number) => TabContentAnimatedTransition =
   10. (from: number, to: number) => {
   11. let tabContentAnimatedTransition = {
   12. timeout: this.animateTimeout,
   13. transition: (proxy: TabContentTransitionProxy) => {
   14. // start frame
   15. this.scaleList[from] = 1.0;
   16. this.scaleList[to] = 0.5;
   17. this.opacityList[from] = 1.0;
   18. this.opacityList[to] = 0.5;
   19. this.getUIContext().animateTo({
   20. duration: this.animateDuration,
   21. onFinish: () => {
   22. proxy.finishTransition();
   23. }
   24. }, () => {
   25. // end frame
   26. this.scaleList[from] = 0.5;
   27. this.scaleList[to] = 1.0;
   28. this.opacityList[from] = 0.5;
   29. this.opacityList[to] = 1.0;
   30. });
   31. }
   32. } as TabContentAnimatedTransition;
   33. return tabContentAnimatedTransition;
   34. };

   36. // ...
   37. }
   ```

   [InTabsComponent.ets](https://gitcode.com/harmonyos_samples/PureTabs/blob/master/entry/src/main/ets/view/InTabsComponent.ets#L33-L427)
4. 将转场函数作为参数传递给Tabs的customContentTransition()方法。

   ```
   1. Tabs({
   2. barPosition: BarPosition.Start,
   3. controller: this.subsController,
   4. barModifier: this.tabBarModifier
   5. }) {
   6. // ...
   7. }
   8. // add animation function
   9. .customContentTransition(this.customContentTransition) // comment out to slide to switch
   ```

   [InTabsComponent.ets](https://gitcode.com/harmonyos_samples/PureTabs/blob/master/entry/src/main/ets/view/InTabsComponent.ets#L233-L366)

### 自定义Tabs页签切换联动

在自定义页签样式中，页签的选中和非选中状态显示样式不同时，页签的样式依赖于Tabs组件的切换动作。这种情况下，需要实现Tabs页签的联动，页签切换时，页签样式自动变更。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/qhAlXqlETQyQYaeY7aJwZg/zh-cn_image_0000002391492321.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001947Z&HW-CC-Expire=86400&HW-CC-Sign=37277A89CFA199B56D4C0F6F2903374CC322A4A5096455D771E4FB8645948AE5 "点击放大")

**实现原理**

可以通过onChange事件，在切换页签时自定义TabBar和TabContent的联动效果。具体做法是定义一个由@State修饰的变量currentIndex，用于标识当前显示的页签索引。然后，利用onChange()方法注册处理函数，并在处理函数中更新currentIndex，确保其与当前选择的页签的索引一致。在页签样式的实现中，通过判断currentIndex变量与各页签索引是否相等来决定显示的样式，同时currentIndex属性的变化会触发页签样式的更新。

**开发步骤**

定义currentIndex属性，tabBuilder方法，并在onChange函数中更新currentIndex属性值。

```
1. @Component
2. export default struct OutTabsComponent {
3. @State currentIndex: number = 0;
4. // ...
5. @Builder
6. tabBuilder(index: number, name: string | Resource, icon: Resource) {
7. Column() {
8. // set special styles if selected

10. SymbolGlyph(icon).fontColor([this.currentIndex === index
11. ? $r('app.color.out_tab_bar_font_active_color')
12. : $r('app.color.out_tab_bar_font_inactive_color')])
13. .fontSize(25)

15. Text(name)
16. .margin({ top: 4 })
17. .fontSize(10)
18. .fontColor(this.currentIndex === index
19. ? $r('app.color.out_tab_bar_font_active_color')
20. : $r('app.color.out_tab_bar_font_inactive_color'))
21. }
22. // ...
23. }
24. build() {
25. Tabs({
26. // ...
27. }) {
28. // ...
29. }
30. // ...
31. .onChange((index: number) => {
32. this.currentIndex = index;
33. })
34. // ...
35. }
36. }
```

[OutTabsComponent.ets](https://gitcode.com/harmonyos_samples/PureTabs/blob/master/entry/src/main/ets/view/OutTabsComponent.ets#L23-L156)

## 常见问题

### 如何实现页面懒加载效果

Tabs页面不支持懒加载。 若要实现页面懒加载效果，可以通过自定义TabBar与[Swiper](../harmonyos-guides/arkts-layout-development-create-looping.md)组件结合[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)来实现页面的懒加载和释放。在使用Tabs组件时，仅保留TabBar，TabContent部分留空，用Swiper组件替代TabContent以显示内容。定义一个数值属性currentIndex，利用[TabsController](../harmonyos-references/ts-container-tabs.md#tabscontroller)、[SwiperController](../harmonyos-references/ts-container-swiper.md#swipercontroller)及onchange函数，使其同时绑定Tabs组件和Swiper组件，从而实现联动。这是因为Swiper组件内支持LazyForEach组件，而原生Tabs组件不支持。在Swiper中利用LazyForEach显示内容，以实现Tabs的懒加载效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/9MH_zXZQTYGaZ2LJ_7x95A/zh-cn_image_0000002358052214.png?HW-CC-KV=V1&HW-CC-Date=20260428T001947Z&HW-CC-Expire=86400&HW-CC-Sign=A7F4F61CC7E69CABBD9F2931C839184A8CBBF17C6DFB8B6E58B891BC7C41148A "点击放大")

详情请参见[页面懒加载和释放](../harmonyos-references/ts-container-tabs.md#示例13页面懒加载和释放)。

## 示例代码

* [Tabs组件应用场景](https://gitcode.com/harmonyos_samples/PureTabs)
