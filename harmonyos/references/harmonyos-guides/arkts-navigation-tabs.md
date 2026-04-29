---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-tabs
title: 选项卡 (Tabs)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 组件布局 > 构建布局 > 选项卡 (Tabs)
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3ca4cab15fb6ed6aada2fa62aa1eab69772ac2830dc005e36bf92ceaa009b472
---

当页面信息较多时，为了让用户能够聚焦于当前显示的内容，需要对页面内容进行分类，提高页面空间利用率。[Tabs](../harmonyos-references/ts-container-tabs.md)组件可以在一个页面内快速实现视图内容的切换，一方面提升查找信息的效率，另一方面精简用户单次获取到的信息量。

## 基本布局

Tabs组件的页面组成包含两个部分，分别是[TabContent](../harmonyos-references/ts-container-tabcontent.md)和[TabBar](../harmonyos-references/ts-container-tabcontent.md#tabbar)。TabContent是内容页，TabBar是导航页签栏，页面结构如下图所示，根据不同的导航类型，布局会有区别，可以分为底部导航、顶部导航、侧边导航，其导航栏分别位于底部、顶部和侧边。

**图1** Tabs组件布局示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/0Bj2-HpjRh6Dm4qbvHuKoA/zh-cn_image_0000002589244045.png?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=3962804726102D294A9D1074C30959A6380E02CE91674F416A5B3D202EC83DC1)

说明

* TabContent组件不支持设置通用宽度属性，其宽度默认撑满Tabs父组件。
* TabContent组件不支持设置通用高度属性，其高度由Tabs父组件高度与TabBar组件高度决定。

Tabs使用花括号包裹TabContent，如图2，其中TabContent显示相应的内容页。

**图2** Tabs与TabContent使用

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/0w4lnfITTqeWMXi-lg1Z9g/zh-cn_image_0000002558764238.png?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=8BE90752E3B2915762724087AD8B478D7D5E7C3DCD77E6F02D40547A5A5D2BC7)

每一个TabContent对应的内容需要有一个页签，可以通过TabContent的tabBar属性进行配置。在如下TabContent组件上设置tabBar属性，可以设置其对应页签中的内容，tabBar作为内容的页签。

```
1. TabContent() {
2. // app.string.homepage_content资源文件中的value值为“首页的内容”
3. Text($r('app.string.homepage_content'))
4. .fontSize(30)
5. }
6. // app.string.homepage资源文件中的value值为“首页”
7. .tabBar($r('app.string.homepage'))
```

[TabsLayout.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/tabs/TabsLayout.ets#L27-L35)

设置多个内容时，需在Tabs内按照顺序放置。

```
1. Tabs() {
2. TabContent() {
3. // app.string.homepage_content资源文件中的value值为“首页的内容”
4. Text($r('app.string.homepage_content'))
5. .fontSize(30)
6. }
7. // app.string.homepage资源文件中的value值为“首页”
8. .tabBar($r('app.string.homepage'))

10. TabContent() {
11. // app.string.recommend_content资源文件中的value值为“推荐的内容”
12. Text($r('app.string.recommend_content'))
13. .fontSize(30)
14. }
15. // app.string.recommend资源文件中的value值为“推荐”
16. .tabBar($r('app.string.recommend'))

18. TabContent() {
19. // app.string.discover_content资源文件中的value值为“发现的内容”
20. Text($r('app.string.discover_content'))
21. .fontSize(30)
22. }
23. // app.string.discover资源文件中的value值为“发现”
24. .tabBar($r('app.string.discover'))

26. TabContent() {
27. // app.string.mine_content资源文件中的value值为“我的内容”
28. Text($r('app.string.mine_content'))
29. .fontSize(30)
30. }
31. // app.string.mine_content资源文件中的value值为“我的”
32. .tabBar($r('app.string.mine'))
33. }
```

[TabsLayout.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/tabs/TabsLayout.ets#L25-L61)

## 底部导航

底部导航是应用中最常见的一种导航方式。底部导航位于应用一级页面的底部，用户打开应用，能够分清整个应用的功能分类，以及页签对应的内容，并且其位于底部更加方便用户单手操作。底部导航一般作为应用的主导航形式存在，其作用是将用户关心的内容按照功能进行分类，迎合用户使用习惯，方便在不同模块间的内容切换。

**图3** 底部导航栏

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/sitp5UjERKuG8BfnW1tv4w/zh-cn_image_0000002558604582.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=FE844EC9BA21C528F7A21A318770410DC2CFB7F48EED5AC510C40C31BDAEE24F)

导航栏位置使用Tabs的barPosition参数进行设置。默认情况下，导航栏位于顶部，此时，barPosition为BarPosition.Start。设置为底部导航时，需要将barPosition设置为BarPosition.End。

```
1. Tabs({ barPosition: BarPosition.End }) {
2. // TabContent的内容：首页、发现、推荐、我的
3. // ···
4. }
```

[BottomTabBar.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/tabs/BottomTabBar.ets#L25-L59)

底部导航栏可通过设置TabContent的[BottomTabBarStyle](../harmonyos-references/ts-container-tabcontent.md#bottomtabbarstyle9)来实现底部页签样式，详细示例请参考：[示例9（设置底部页签使用symbol图标）](../harmonyos-references/ts-container-tabcontent.md#示例9设置底部页签使用symbol图标)。

## 顶部导航

当内容分类较多，用户对不同内容的浏览概率相差不大，需要经常快速切换时，一般采用顶部导航模式进行设计，作为对底部导航内容的进一步划分，常见一些资讯类应用对内容的分类为关注、视频、数码，或者主题应用中对主题进行进一步划分为图片、视频、字体等。

**图4** 顶部导航栏

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/PxZ6yWl-TKOb2W6fM_ie-w/zh-cn_image_0000002589324107.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=7AEA6F1E610FE4E27B72A7E88CB88917A0D3286A7AE6D3426DB71FD4F57F9282)

```
1. Tabs({ barPosition: BarPosition.Start }) {
2. // TabContent的内容:关注、视频、游戏、数码、科技、体育、影视
3. // ···
4. }
```

[TopTabBar.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/tabs/TopTabBar.ets#L25-L65)

## 侧边导航

侧边导航是应用较为少见的一种导航模式，更多适用于横屏界面，用于对应用进行导航操作，由于用户的视觉习惯是从左到右，侧边导航栏默认为左侧侧边栏。

**图5** 侧边导航栏

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/fVKfa1QsS_u6zv5Nsd9njA/zh-cn_image_0000002589244047.png?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=2E9A7F5221DAA5988469ACFC6D41F42860124DD227F21303935BCC722594780E)

实现侧边导航栏需要将Tabs的[vertical](../harmonyos-references/ts-container-tabs.md#vertical)属性设置为true，vertical默认值为false，表明内容页和导航栏垂直方向排列。

```
1. Tabs({ barPosition: BarPosition.Start }) {
2. // TabContent的内容:首页、发现、推荐、我的
3. // ···
4. }
5. // ···
6. .vertical(true)
7. .barWidth(100)
8. .barHeight(200)
```

[SideTabBar.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/tabs/SideTabBar.ets#L25-L64)

说明

* vertical为false时，tabbar的宽度默认为撑满屏幕的宽度，需要设置[barWidth](../harmonyos-references/ts-container-tabs.md#barwidth)为合适值。
* vertical为true时，tabbar的高度默认为实际内容的高度，需要设置[barHeight](../harmonyos-references/ts-container-tabs.md#barheight)为合适值。

## 限制导航栏的滑动切换

默认情况下，导航栏都支持滑动切换，在一些内容信息量需要进行多级分类的页面，如支持底部导航+顶部导航组合的情况下，底部导航栏的滑动效果与顶部导航出现冲突，此时需要限制底部导航的滑动，避免引起不好的用户体验。

**图6** 限制底部导航栏滑动

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/pQIlEjgUQtaXYcZZxNsweg/zh-cn_image_0000002558764240.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=57F21026BFAC356413EAE3867B22FC8D96252DC7063CB84360938CAC9346C819)

控制滑动切换的属性为scrollable，默认值为true，表示可以滑动，若要限制滑动切换页签则需要设置为false。

```
1. Tabs({ barPosition: BarPosition.End }) {
2. TabContent() {
3. Column() {
4. Tabs() {
5. // 顶部导航栏内容
6. // ···
7. }
8. }
9. .backgroundColor('#ff08a8f1')
10. .width('100%')
11. }
12. // app.string.homepage资源文件中的value值为“首页”
13. .tabBar($r('app.string.homepage'))

15. // 其他TabContent内容：发现、推荐、我的
16. // ···
17. }
18. // ···
19. .scrollable(false)
```

[SwipeLockedTabBar.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/tabs/SwipeLockedTabBar.ets#L25-L98)

## 固定导航栏

当内容分类较为固定且不具有拓展性时，例如底部导航内容分类一般固定，分类数量一般在3-5个，此时使用固定导航栏。固定导航栏不可滚动，无法被拖拽滚动，内容均分tabBar的宽度。

**图7** 固定导航栏

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/vEqrcK3UQcKXTmM1TrM9zg/zh-cn_image_0000002558604584.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=37B6C51B6A0D827EE232E23D62A23D464BE32AE9BCF1EF82D0B8C8DC71AFA28C)

Tabs的[barMode](../harmonyos-references/ts-container-tabs.md#barmode10)属性用于控制导航栏是否可以滚动，默认值为BarMode.Fixed。

```
1. Tabs({ barPosition: BarPosition.End }) {
2. // TabContent的内容：首页、发现、推荐、我的
3. // ···
4. }
5. .barMode(BarMode.Fixed)
```

[FixedTabBar.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/tabs/FixedTabBar.ets#L25-L59)

## 滚动导航栏

滚动导航栏可以用于顶部导航栏或者侧边导航栏的设置，内容分类较多，屏幕宽度无法容纳所有分类页签的情况下，需要使用可滚动的导航栏，支持用户点击和滑动来加载隐藏的页签内容。

**图8** 可滚动导航栏

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/4m9JH6-mRzK-Aaf9d8Y2ag/zh-cn_image_0000002589324109.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=AD02A8F2F88F7AA002F0111E9E2C979D696E1938D284F9DDE17D7473D6DE7C93)

滚动导航栏需要设置Tabs组件的barMode属性，默认值为BarMode.Fixed表示为固定导航栏，BarMode.Scrollable表示可滚动导航栏。

```
1. Tabs({ barPosition: BarPosition.Start }) {
2. // TabContent的内容：关注、视频、游戏、数码、科技、体育、影视、人文、艺术、自然、军事
3. // ···
4. }
5. .barMode(BarMode.Scrollable)
```

[ScrollableTabBar.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/tabs/ScrollableTabBar.ets#L25-L87)

## 自定义导航栏

对于底部导航栏，一般作为应用主页面功能区分，为了更好的用户体验，会组合文字以及对应语义图标表示页签内容，这种情况下，需要自定义导航页签的样式。

**图9** 自定义导航栏

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/SUPoEQ8cQLSiOQT0CZiTrQ/zh-cn_image_0000002589244049.png?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=955D889577827A9BCD80E2B165A4F6B558DACAD3F3C1741E56E87CD51C3CFBCF)

系统默认情况下采用了下划线标识当前活跃的页签，而自定义导航栏需要自行实现相应的样式，用于区分当前活跃页签和未活跃页签。

设置自定义导航栏需要使用tabBar的参数，以其支持的CustomBuilder的方式传入自定义的函数组件样式。例如这里声明tabBuilder的自定义函数组件，传入参数包括页签文字title，对应位置index，以及选中状态和未选中状态的图片资源。通过当前活跃的currentIndex和页签对应的targetIndex匹配与否，决定UI显示的样式。

```
1. @State currentIndex: number = 0;

3. @Builder
4. tabBuilder(title: ResourceStr, targetIndex: number, selectedImg: Resource, normalImg: Resource) {
5. Column() {
6. Image(this.currentIndex === targetIndex ? selectedImg : normalImg)
7. .size({ width: 25, height: 25 })
8. Text(title)
9. .fontColor(this.currentIndex === targetIndex ? '#1698CE' : '#6B6B6B')
10. }
11. .width('100%')
12. .height(50)
13. .justifyContent(FlexAlign.Center)
14. }
```

[CustomTabBar.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/tabs/CustomTabBar.ets#L21-L36)

在TabContent对应tabBar属性中传入自定义函数组件，并传递相应的参数。

```
1. TabContent() {
2. Column() {
3. // app.string.mine_content资源文件中的value值为“我的内容”
4. Text($r('app.string.mine_content'))
5. }
6. .width('100%')
7. .height('100%')
8. .backgroundColor('#007DFF')
9. }
10. // app.string.mine资源文件中的value值为“我的”
11. .tabBar(this.tabBuilder($r('app.string.mine'), 0, $r('app.media.mine_selected'), $r('app.media.mine_normal')))
```

[CustomTabBar.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/tabs/CustomTabBar.ets#L43-L55)

## 切换至指定页签

在不使用自定义导航栏时，默认的Tabs会实现切换逻辑。在使用了自定义导航栏后，默认的Tabs仅实现滑动内容页和点击页签时内容页的切换逻辑，页签切换逻辑需要自行实现。即用户滑动内容页和点击页签时，页签栏需要同步切换至内容页对应的页签。

**图10** 内容页和页签不联动

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/3YnOwpHITJKJXgAEQGJmrw/zh-cn_image_0000002558764242.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=EF7B8BF400D309F50B65C7489895AE93C79774A987CF1883FB023FBAD5B79BC9)

从API version 18开始，支持使用Tabs提供的[onSelected](../harmonyos-references/ts-container-tabs.md#onselected18)事件方法，监听索引index的变化，并将选中元素的index值传递给selectIndex，实现页签的切换。

```
1. // 如需作为页面入口，请取消@Entry的注释并删除export关键字
2. // @Entry
3. @Component
4. export struct ContentPageNoAndTabLinkage {

6. @State selectIndex: number = 0;
7. @Builder tabBuilder(title: Resource, targetIndex: number) {
8. Column() {
9. Text(title)
10. .fontColor(this.selectIndex === targetIndex ? '#1698CE' : '#6B6B6B')
11. }
12. }
13. build() {
14. NavDestination() {
15. Column({ space: 12 }) {
16. // ...
17. Tabs({ barPosition: BarPosition.End }) {
18. TabContent() {
19. // app.string.homepage_content资源文件中的value值为“首页内容”
20. Text($r('app.string.homepage_content')).width('100%').height('100%').backgroundColor('rgb(213,213,213)')
21. .fontSize(40).fontColor(Color.Black).textAlign(TextAlign.Center)
22. // app.string.homepage资源文件中的value值为“首页”
23. }.tabBar(this.tabBuilder($r('app.string.homepage'), 0))

25. TabContent() {
26. // app.string.discover_content资源文件中的value值为“发现内容”
27. Text($r('app.string.discover_content')).width('100%').height('100%').backgroundColor('rgb(112,112,112)')
28. .fontSize(40).fontColor(Color.Black).textAlign(TextAlign.Center)
29. // app.string.discover资源文件中的value值为“发现”
30. }.tabBar(this.tabBuilder($r('app.string.discover'), 1))

32. TabContent() {
33. // app.string.recommend_content资源文件中的value值为“推荐内容”
34. Text($r('app.string.recommend_content')).width('100%').height('100%').backgroundColor('rgb(39,135,217)')
35. .fontSize(40).fontColor(Color.Black).textAlign(TextAlign.Center)
36. // app.string.recommend资源文件中的value值为“推荐”
37. }.tabBar(this.tabBuilder($r('app.string.recommend'), 2))

39. TabContent() {
40. // app.string.mine_content资源文件中的value值为“我的内容”
41. Text($r('app.string.mine_content')).width('100%').height('100%').backgroundColor('rgb(0,74,175)')
42. .fontSize(40).fontColor(Color.Black).textAlign(TextAlign.Center)
43. }
44. // app.string.mine资源文件中的value值为“我的”
45. .tabBar(this.tabBuilder($r('app.string.mine'), 3))
46. }
47. .animationDuration(0)
48. .backgroundColor('#F1F3F5')
49. .onSelected((index: number) => {
50. this.selectIndex = index;
51. })
52. // ...
53. }
54. .width('100%')
55. // ...
56. }
57. // ...
58. }
59. }
```

[ContentPageNoAndTabLinkage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/tabs/ContentPageNoAndTabLinkage.ets#L16-L85)

**图11** 内容页和页签联动

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/cMDHm94tQmy5PKORsovFrg/zh-cn_image_0000002558604586.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=89D3F7AFFCE1E1BE607B86D8C891F743B10BCF93B4A7C84162CFE9B50FD98554)

若希望不滑动内容页和点击页签也能实现内容页和页签的切换，可以将currentIndex传给Tabs的index参数，通过改变currentIndex来实现跳转至指定索引值对应的TabContent内容。也可以使用[TabsController](../harmonyos-references/ts-container-tabs.md#tabscontroller)，TabsController是Tabs组件的控制器，用于控制Tabs组件进行内容页切换。通过TabsController的changeIndex方法来实现跳转至指定索引值对应的TabContent内容。

```
1. // ...
2. @State currentIndex: number = 2;
3. @State currentAnimationMode: AnimationMode = AnimationMode.CONTENT_FIRST;
4. private controller: TabsController = new TabsController();

6. // ...
7. Tabs({ barPosition: BarPosition.End, index: this.currentIndex, controller: this.controller }) {
8. // ...
9. }
10. .animationDuration(0)
11. .height(300)
12. .animationMode(this.currentAnimationMode)
13. .onChange((index: number) => {
14. this.currentIndex = index;
15. })

17. // app.string.ContentWillChange_animationMode资源文件中的value值为“动态修改animationMode”
18. Button($r('app.string.ContentWillChange_animationMode')).width('50%').margin({ top: 20 })
19. .onClick(()=>{
20. if (this.currentAnimationMode === AnimationMode.CONTENT_FIRST) {
21. this.currentAnimationMode = AnimationMode.ACTION_FIRST;
22. } else if (this.currentAnimationMode === AnimationMode.ACTION_FIRST) {
23. this.currentAnimationMode = AnimationMode.NO_ANIMATION;
24. } else if (this.currentAnimationMode === AnimationMode.NO_ANIMATION) {
25. this.currentAnimationMode = AnimationMode.CONTENT_FIRST_WITH_JUMP;
26. } else if (this.currentAnimationMode === AnimationMode.CONTENT_FIRST_WITH_JUMP) {
27. this.currentAnimationMode = AnimationMode.ACTION_FIRST_WITH_JUMP;
28. } else if (this.currentAnimationMode === AnimationMode.ACTION_FIRST_WITH_JUMP) {
29. this.currentAnimationMode = AnimationMode.CONTENT_FIRST;
30. }
31. })

33. // app.string.ContentWillChange_changeIndex资源文件中的value值为“动态修改index”
34. Button($r('app.string.ContentWillChange_changeIndex')).width('50%').margin({ top: 20 })
35. .onClick(() => {
36. this.currentIndex = (this.currentIndex + 1) % 4;
37. })

39. Button('changeIndex').width('50%').margin({ top: 20 })
40. .onClick(() => {
41. let index = (this.currentIndex + 1) % 4;
42. this.controller.changeIndex(index);
43. })
```

[ContentWillChange.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/tabs/ContentWillChange.ets#L18-L164)

**图12** 切换指定页签

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/cIWPqvxBSged_OV2tu1zhQ/zh-cn_image_0000002589324111.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=64E59F212F7C3229F64353E5025E996F24D36AF1EFA892D6DA7D0BA4C348B015)

开发者可以通过Tabs组件的[onContentWillChange](../harmonyos-references/ts-container-tabs.md#oncontentwillchange12)接口，设置自定义拦截回调函数。拦截回调函数在下一个页面即将展示时被调用，如果回调返回true，新页面可以展示；如果回调返回false，新页面不会展示，仍显示原来页面。

```
1. Tabs({ barPosition: BarPosition.End, index: this.currentIndex, controller: this.controllerTwo }) {
2. // ...
3. }
4. // ...
5. .onContentWillChange((currentIndex, comingIndex) => {
6. if (comingIndex === 2) {
7. return false;
8. }
9. return true;
10. })
```

[ContentWillChange.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/tabs/ContentWillChange.ets#L170-L215)

**图13** 支持开发者自定义页面切换拦截事件

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/7ratR-SeQhG4-QtkFXcbaw/zh-cn_image_0000002589244051.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=147FCA57BA9CB69323DF5A65E0F75676AEE51940BAC2E96F26FF9D9DCD3FFC6C)

## 支持适老化

在适老化大字体场景下，底部页签提供大字体弹窗显示内容。当组件识别到大字体时，基于设置的文字和图标等内容，构建长按提示弹窗。当用户长按弹窗后，滑动到下一个页签位置时，使用新页签的弹窗提示内容替换上一个页签提示内容，抬手关闭弹窗并切换到对应TabContent内容页。

说明

弹窗只适用于底部页签BottomTabBarStyle。

**图14** 在适老化场景下通过长按底部页签显示适老化弹窗。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/zECkJ09vT1aL6B8EC2I9Cw/zh-cn_image_0000002558764244.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=2208ABF1D0FFDEE150B4C1D636F56D2A19A6183C529D70A6ACAA7EC564B29037)

```
1. // 如需作为页面入口，请取消@Entry的注释并删除export关键字
2. // @Entry
3. @Component
4. export struct AgeFriendlyTabs {

6. build() {
7. NavDestination() {
8. Column() {
9. Tabs({ barPosition: BarPosition.End }) {
10. TabContent() {
11. Column().width('100%').height('100%').backgroundColor(Color.Pink)
12. }.tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), 'OverLength'))

14. TabContent() {
15. Column().width('100%').height('100%').backgroundColor(Color.Yellow)
16. }.tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), 'SixLine'))

18. TabContent() {
19. Column().width('100%').height('100%').backgroundColor(Color.Blue)
20. }.tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), 'Blue'))

22. TabContent() {
23. Column().width('100%').height('100%').backgroundColor(Color.Green)
24. }.tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), 'Green'))
25. }
26. .vertical(false)
27. .scrollable(true)
28. .barMode(BarMode.Fixed)
29. .width('100%')
30. .backgroundColor(0xF1F3F5)
31. }.width('80%').height(200)
32. .margin({ top: 200 })
33. }
34. }
35. }
```

[AgeFriendlyTabs.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/master/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/tabs/AgeFriendlyTabs.ets#L16-L51)

## 控制页面缓存数

从API version 19开始，开发者可以通过[cachedMaxCount](../harmonyos-references/ts-container-tabs.md#cachedmaxcount19)接口，设置子组件的最大缓存个数和缓存模式。默认情况下Tabs创建时会一次性预加载所有TabContent，而且已加载的页面不会释放，可能会带来性能内存问题。此时可以设置[cachedMaxCount](../harmonyos-references/ts-container-tabs.md#cachedmaxcount19)属性控制缓存的页面数量，设置此属性后不会进行页面预加载，使用懒加载机制(仅切换到页面时才加载)，当切换页面时根据所设置的[TabsCacheMode](../harmonyos-references/ts-container-tabs.md#tabscachemode19枚举说明)决定保留缓存或者释放页面。

说明

* TabsCacheMode枚举值为CACHE\_BOTH\_SIDE时，缓存当前显示的子组件和其两侧的子组件。
* TabsCacheMode枚举值为CACHE\_LATEST\_SWITCHED时，缓存当前显示的子组件和最近切换过的子组件。
* 存在翻页动画时，从页面1直接切换到页面3，翻页动画会包含页面2，页面2也会被加载，如果此时页面2不在缓存范围内，页面切换完成后会立马释放。

**图15** 在页面缓存场景下通过点击yellow按键切换界面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/i5N8wZzOQCq-YwyDE-yBQw/zh-cn_image_0000002558604588.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=B724F27197DFAC33FE62497836C995E52A3419984986EDDFEC29556138C3B806)

```
1. // 如需作为页面入口，请取消@Entry的注释并删除export关键字
2. // @Entry
3. @Component
4. export struct NumberOfCachesTabBar {
5. build() {
6. // ...
7. Tabs({ barPosition: BarPosition.Start }) {
8. TabContent() {
9. MyComponent({ color: '#00CB87' })
10. }.tabBar(SubTabBarStyle.of('green'))

12. TabContent() {
13. MyComponent({ color: '#007DFF' })
14. }.tabBar(SubTabBarStyle.of('blue'))

16. TabContent() {
17. MyComponent({ color: '#FFBF00' })
18. }.tabBar(SubTabBarStyle.of('yellow'))

20. TabContent() {
21. MyComponent({ color: '#E67C92' })
22. }.tabBar(SubTabBarStyle.of('pink'))

24. TabContent() {
25. MyComponent({ color: '#FF0000' })
26. }.tabBar(SubTabBarStyle.of('red'))
27. }
28. .width(360)
29. .height(296)
30. .backgroundColor('#F1F3F5')
31. .cachedMaxCount(1, TabsCacheMode.CACHE_BOTH_SIDE)
32. // ...
33. }
34. }

36. @Component
37. struct MyComponent {
38. private color: string = '';

40. aboutToAppear(): void {
41. console.info('aboutToAppear backgroundColor:' + this.color);
42. }

44. aboutToDisappear(): void {
45. console.info('aboutToDisappear backgroundColor:' + this.color);
46. }

48. build() {
49. Column()
50. .width('100%')
51. .height('100%')
52. .backgroundColor(this.color)
53. }
54. }
```

[NumberOfCachesTabBar.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/tabs/NumberOfCachesTabBar.ets#L16-L83)

基于以上示例代码为例，不同场景下的缓存策略如下：

1. 如图16所示，使用默认翻页动画，CACHE\_BOTH\_SIDE模式，n设置为2，点击TabBar切换到yellow页，TabContent1~3被缓存。再切换到red页，TabContent1、2释放，TabContent3~5被缓存。

   **图16** 默认翻页动画，CACHE\_BOTH\_SIDE模式示意图

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/5llumwzrT9mLY8-35loFRg/zh-cn_image_0000002589324113.png?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=0BF275EE7EFFF5BCF1261BAFE96DD202139DD8DDC627E784DD74F29FC576A1CF)
2. 如图17所示，使用默认翻页动画，CACHE\_LATEST\_SWITCHED模式，n设置为2，点击TabBar切换到yellow页，TabContent1、3被缓存，TabContent2释放。再切换到red页，TabContent1、3、5被缓存，TabContent4释放。

   **图17** 默认翻页动画，CACHE\_LATEST\_SWITCHED模式示意图

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/T5DKOSWhRIWmhFqKwihN0A/zh-cn_image_0000002589244053.png?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=F82F49FA24B6362B5F797E2D16E6F841C84F0D0CFD7A8A37DA54E3D71ACFAC09)
3. 如图18所示，关闭翻页动画，CACHE\_BOTH\_SIDE模式，n设置为2，点击TabBar切换到yellow页，TabContent1、3被缓存。再切换到red页，TabContent3、5被缓存，TabContent1释放。

   **图18** 关闭翻页动画，CACHE\_BOTH\_SIDE模式示意图

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/lIFdAo6XSWOVjtS61CWvjw/zh-cn_image_0000002558764246.png?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=3D98934707AF57BE664659E682C53EC0B1B8254820062853208FA82EA19F71FD)
4. 如图19所示，关闭翻页动画，CACHE\_LATEST\_SWITCHED模式，n设置为2，点击TabBar切换到yellow页，TabContent1、3被缓存。再切换到red页，TabContent1、3、5被缓存。

   **图19** 关闭翻页动画，CACHE\_LATEST\_SWITCHED模式示意图

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/LHZgtpzWRvCT0wMGJsIh9g/zh-cn_image_0000002558604590.png?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=5495D3D7BB496D1B803CAB60BE7C19DB89E51037B0697E07C74AE173739A353D)

## 示例代码

* [基于Tabs组件实现常见导航样式](https://gitcode.com/HarmonyOS_Samples/multi-tab-navigation)
* [基于Tab组件实现增删Tab的功能](https://gitcode.com/HarmonyOS_Samples/handle-tabs)
