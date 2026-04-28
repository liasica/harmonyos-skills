---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-split-mode
title: Navigation分栏开发
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 设置组件导航和页面路由 > 组件导航(Navigation) (推荐) > Navigation分栏开发
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b030f467a02e8050295befa50260f965bfcc76929f4b4de98fc0d9e50ec05306
---

[Navigation](../harmonyos-references/ts-basic-components-navigation.md)作为一个容器组件，提供了两种布局样式：单栏布局、分栏布局。分栏布局一般适用于宽屏设备，在分栏布局下，导航栏（navBar）会固定显示， 子页面（NavDestination）通过导航控制器（NavPathStack）切换显示， 在导航栏和子页面之间有一条分割线， 可以通过分割线拖拽控制左右显示的比例。架构图详见[Navigation基础架构介绍](arkts-navigation-architecture.md)。

## 分栏相关接口介绍

### mode

[mode](../harmonyos-references/ts-basic-components-navigation.md#mode9)属性用于控制Navigation的显示模式，有三种模式：单栏，分栏，自适应。

**图1** 单栏（NavigationMode.Stack）效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/v7M4UMDfQ7i23VumpgwB3A/zh-cn_image_0000002583477685.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=5B34869035B3308E29256DF0B7C2A761DE4113C68739FEB28599B435F8711821)

**图2** 分栏（NavigationMode.Split）效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/0398Vx7uQka1lG5JBVSNfA/zh-cn_image_0000002552798036.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=08B894B98033F35C2B2C2BFD59262A8E0F2CC3326571C4D7A14B24C0978F9039)

**图3** 自适应（NavigationMode.Auto）效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/OQkyfv_ETz-K3iUYxDvjZQ/zh-cn_image_0000002583437731.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=79F66544E6767928871218BF543803D40D6D108A891E063D9622E46FEECEDAA5)

### navBarPosition

[navBarPosition](../harmonyos-references/ts-basic-components-navigation.md#navbarposition9)用于控制导航栏显示的位置，用navBarPosition控制导航栏显示位置时，会被系统语言所影响。比如，在以汉语、英语为代表的LTR语言体系下，NavBarPosition.Start指代的是导航栏出现在左侧，而在以阿拉伯语为代表的RTL语言体系下，NavBarPosition.Start则指代导航栏出现在右侧。类似的效果也出现在NavBarPosition.End上。

**NavBarPosition.Start**

**图4** 系统语言为LTR时NavBarPosition.Start效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/mIyZAfV6RXmZiBDDq2627w/zh-cn_image_0000002552957686.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=F1A8E800838F5782381C076345F732A872CA1B0BBA3246CA07EB3049F7DFBEE0)

**图5** 系统语言为RTL时NavBarPosition.Start效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/68TzpKdeTa-MVqzmoB957Q/zh-cn_image_0000002583477687.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=92FD79446916EB392FF51F1432CD62700F7C01D36F4F1D379E1297721B347182)

**NavBarPosition.End**

**图6** 系统语言为LTR时NavBarPosition.End效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/quDHDJ3kRcy8mAM_SlSZkg/zh-cn_image_0000002552798038.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=64DC59086CD5D71F37440C8CBE35F3E73BD8BA907DA7F2E88D936BF541E30352)

**图7** 系统语言为RTL时NavBarPosition.End效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/Rotl_O2VQHOHpvhLNVRBrg/zh-cn_image_0000002583437733.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=0CBED9A4DB223A8CF61DD8EE1BBEA8AAF6CE338D3588C238CADAC87560BDA89D)

### enableDragBar

[enableDragBar](../harmonyos-references/ts-basic-components-navigation.md#enabledragbar14)用于控制是否显示分栏的拖动按钮。

**图8** enableDragBar为false效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/FOHZwP3JSLOFOflTtus50w/zh-cn_image_0000002552957688.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=BB12811E1F1179139C7709181D9BAC141D6963CF549377265B9CA7B5F2FDB50F)

**图9** enableDragBar为true

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/PiTEzgcHTWqgUtytvIks-Q/zh-cn_image_0000002583477689.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=B16440F57C995212533451C76693E035924AD4A953D8723A4D47D3518A34AED2)

### navBarWidth

[navBarWidth](../harmonyos-references/ts-basic-components-navigation.md#navbarwidth9)用于控制导航栏的宽度。

### navBarWidthRange

[navBarWidthRange](../harmonyos-references/ts-basic-components-navigation.md#navbarwidthrange10)用于设置导航栏宽度可调整的范围。

### minContentWidth

[minContentWidth](../harmonyos-references/ts-basic-components-navigation.md#mincontentwidth10)用于控制分栏子页的最小宽度；分栏模式导航栏和子页中间会有一个分割线，在可调范围内，用户可以通过拖动分割线来调整导航栏和子页的显示大小。

### hideNavBar

[hideNavBar](../harmonyos-references/ts-basic-components-navigation.md#hidenavbar9)用于控制导航栏的显示状态，默认值为false。如果同时将mode配置为NavigationMode.Split且hideNavBar设置为true，则实际效果会显示为单栏。

### enableModeChangeAnimation

[enableModeChangeAnimation](../harmonyos-references/ts-basic-components-navigation.md#enablemodechangeanimation15)用于控制是否开启单双栏切换的动画，默认开启。

### splitPlaceholder

[splitPlaceholder](../harmonyos-references/ts-basic-components-navigation.md#splitplaceholder20)用于设置分栏模式下内容区的默认占位页。分栏模式在默认情况下，栈中没有页面时内容区展示空白，可使用此接口设置此区域的UI布局。

需要注意的是，占位页仅作为UI展示页，仅分栏模式空栈的情况下才展示，不受路由栈管理也不可获焦和响应事件。

## 分栏开发示例

以开发一个新闻app的demo来演示如何使用Navigation分栏相关接口。

1. 新闻主页内容会放到左侧NavBar中，其中内容是一个新闻列表，用户点击每一条新闻标题时，右边会push一个详情页，用来展示新闻的信息。
2. 给左侧NavBar设置一个宽度范围，右侧子页区域也设置一个最小宽度。

配置的路由表：

```
1. {
2. "routerMap": [
3. {
4. "name": "NewsDetail",
5. "pageSourceFile": "src/main/ets/pages/navigation/splitmode/NewsDetail.ets",
6. "buildFunction": "NewsDetailPageBuilder",
7. "data": {
8. "description": "this is DetailPageA"
9. }
10. }
11. ]
12. }
```

子页代码：

```
1. // 自定义的参数类型，用于在push页面时给子页传递参数
2. export class NewsItem {
3. public title: string;
4. public overview: string;
5. public content: string;

7. constructor(title: string, overview: string, content: string) {
8. this.title = title;
9. this.overview = overview;
10. this.content = content;
11. }
12. }

14. @Builder
15. export function NewsDetailPageBuilder() {
16. NewsDetail()
17. }

19. @Component
20. struct NewsDetail {
21. @State title: string = '';
22. @State content: string = '';

24. build() {
25. NavDestination() {
26. Column() {
27. Text(this.content)
28. }
29. }
30. .title(this.title)
31. .backgroundColor('#fff6e3c8')
32. .onReady((ctx: NavDestinationContext) => {
33. // 在onReady生命周期拿到传来的页面参数
34. let param = ctx.pathInfo.param as NewsItem;
35. this.title = param?.title;
36. this.content = param?.content;
37. })
38. }
39. }
```

[NewsDetail.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/splitmode/NewsDetail.ets#L15-L55)

主页代码：

```
1. import { NewsItem } from './NewsDetail'

3. @Component
4. struct NewsHome {
5. private newsItemArray: Array<NewsItem> = [];
6. private stack: NavPathStack | undefined = undefined;

8. aboutToAppear(): void {
9. // 这里省略了从网络获取新闻信息的过程
10. for (let i = 0; i < 50; i++) {
11. this.newsItemArray.push(new NewsItem(`新闻标题${i + 1}`, `新闻概述${i + 1}`, `新闻详情${i + 1}`))
12. }
13. let info = this.queryNavigationInfo();
14. this.stack = info?.pathStack;
15. }

17. build() {
18. List() {
19. ForEach(this.newsItemArray, (item: NewsItem, index: number) => {
20. ListItem() {
21. Column() {
22. Text(`${item.title}`).margin(15).fontSize(25).fontColor(Color.Black)
23. Text(`${item.overview}`).fontSize(13).fontColor(Color.Gray)
24. }.margin({bottom: 15}).backgroundColor('#eeeeee').width('100%')
25. .borderRadius(15).height(120).onClick(() => {
26. // 用户点击某一个新闻标签时，就在右侧子页区域push一个NavDestination页面，用来展示新闻详情
27. this.stack?.pushPath({name: 'NewsDetail', param: item})
28. })
29. }.width('100%')
30. }, (item: NewsItem, index: number) => {
31. return item.title;
32. })
33. }.width('100%').height('100%').padding(15)
34. }
35. }

37. @Entry
38. @Component
39. struct Index {
40. private stack: NavPathStack = new NavPathStack();
41. @State navWidth: number = 100;

43. build() {
44. RelativeContainer() {
45. Navigation(this.stack) {
46. NewsHome().width('100%').height('100%')
47. }
48. .mode(NavigationMode.Split)
49. .enableDragBar(true)
50. .hideNavBar(false)
51. .navBarWidthRange([100, 700]) // 指定NavBar区域的宽度范围
52. .minContentWidth(100) // 指定子页区域的最小宽度
53. .hideTitleBar(true)
54. .hideToolBar(true)
55. .height('100%')
56. .width(`${this.navWidth}%`)
57. .alignRules({
58. top: { anchor: '__container__', align: VerticalAlign.Top },
59. left: { anchor: '__container__', align: HorizontalAlign.Start }
60. })
61. }
62. }
63. }
```

[SplitNavigation.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/splitmode/SplitNavigation.ets#L15-L79)

**图10** 运行效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/-n7KMHZTQz-RX7lDm59MHw/zh-cn_image_0000002552798040.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=ED9DAAF767F7C21DD4FC07B66E7923268A0A8CA259F1BD415DBFAFEA49305D75)
