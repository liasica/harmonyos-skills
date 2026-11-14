---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-split-mode
title: Navigation分栏开发
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 设置组件导航和页面路由 > 组件导航(Navigation) (推荐) > Navigation分栏开发
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:02+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:8e1b99581de3801c25dfb76df09ee97cca46e42520003cbbe39d8ac676bee5ae
---

[Navigation](../harmonyos-references/ts-basic-components-navigation.md)作为一个容器组件，提供了两种布局样式：单栏布局、分栏布局。分栏布局一般适用于宽屏设备，在分栏布局下，导航栏（navBar）会固定显示， 子页面（NavDestination）通过导航控制器（NavPathStack）切换显示， 在导航栏和子页面之间有一条分割线， 可以通过分割线拖拽控制左右显示的比例。架构图详见[Navigation基础架构介绍](arkts-navigation-architecture.md)。

## 分栏相关接口介绍

### mode

[mode](../harmonyos-references/ts-basic-components-navigation.md#mode9)属性用于控制Navigation的显示模式，有四种模式：单栏，分栏，自适应，根据高宽比自适应。

**图1** 单栏（NavigationMode.Stack）效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/DdUCax7lSDmg4loU6FdExA/zh-cn_image_0000002788306494.png?HW-CC-KV=V1&HW-CC-Date=20261114T004701Z&HW-CC-Expire=31536000000&HW-CC-Sign=35D3ADEFA5EC77505897BBF2F3CC7A677CE9DE100C8AF2997E54B648FB06DEF7)

**图2** 分栏（NavigationMode.Split）效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/TzA-KFQoRRC7w9_W0uPp4w/zh-cn_image_0000002817425857.png?HW-CC-KV=V1&HW-CC-Date=20261114T004701Z&HW-CC-Expire=31536000000&HW-CC-Sign=8BBD0B619B71EF81228626DB38C4D0E749082CC1A58E9C86069E8677130A1B73)

**图3** 自适应（NavigationMode.Auto）效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/SGI0c-miQv23HjC4SzB20Q/zh-cn_image_0000002788466438.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004701Z&HW-CC-Expire=31536000000&HW-CC-Sign=6853BF935FE9767EF5CFAC1DF490CB58992879FC6196548B7D51FB2CF615F735)

**图4** 根据高宽比自适应（NavigationMode.AUTO\_WITH\_ASPECT\_RATIO）效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/49fJhq_4SryDqEC7k9tOrg/zh-cn_image_0000002817505925.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004701Z&HW-CC-Expire=31536000000&HW-CC-Sign=6E5061CBEF1B87997A4A59F123BA0A737AA81B98FDBA6D63BC5996BBB0A3CB03)

### navBarPosition

[navBarPosition](../harmonyos-references/ts-basic-components-navigation.md#navbarposition9)用于控制导航栏显示的位置，用navBarPosition控制导航栏显示位置时，会被系统语言所影响。比如，在以汉语、英语为代表的LTR语言体系下，NavBarPosition.Start指代的是导航栏出现在左侧，而在以阿拉伯语为代表的RTL语言体系下，NavBarPosition.Start则指代导航栏出现在右侧。类似的效果也出现在NavBarPosition.End上。

**NavBarPosition.Start**

**图5** 系统语言为LTR时NavBarPosition.Start效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/NN_AcTomT_aE3WItPEAf7A/zh-cn_image_0000002788306496.png?HW-CC-KV=V1&HW-CC-Date=20261114T004701Z&HW-CC-Expire=31536000000&HW-CC-Sign=0B0A84D22177C99FC461D7F723F3DCC93AFC5F35B8C231DCD7CEEA1602020C7F)

**图6** 系统语言为RTL时NavBarPosition.Start效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/LfVblXHeT4elsJ2j1grX8Q/zh-cn_image_0000002817425859.png?HW-CC-KV=V1&HW-CC-Date=20261114T004701Z&HW-CC-Expire=31536000000&HW-CC-Sign=3B24B5074BC0FA7ED0DE0853163D21D09687B8517797FF432906A30E70F7604A)

**NavBarPosition.End**

**图7** 系统语言为LTR时NavBarPosition.End效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/4fkIFyY4Tji4_II1j8ivYQ/zh-cn_image_0000002788466440.png?HW-CC-KV=V1&HW-CC-Date=20261114T004701Z&HW-CC-Expire=31536000000&HW-CC-Sign=203D1D4A3A312D176E11CA5A7C56BA668BE968E39B4EF1336F2207D257D964D2)

**图8** 系统语言为RTL时NavBarPosition.End效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/YkpALZQ9T9S4JyZ-LsD7nA/zh-cn_image_0000002817505927.png?HW-CC-KV=V1&HW-CC-Date=20261114T004701Z&HW-CC-Expire=31536000000&HW-CC-Sign=AC7F4497A3996C191A002A56E34DB33E1B6F01A7FFDB10BDC00E73D3A82C9BDC)

### enableDragBar

[enableDragBar](../harmonyos-references/ts-basic-components-navigation.md#enabledragbar14)用于控制是否显示分栏的拖动按钮。

**图9** enableDragBar为false效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/avCCxPNxRHqQmDgZUHp7lA/zh-cn_image_0000002788306498.png?HW-CC-KV=V1&HW-CC-Date=20261114T004701Z&HW-CC-Expire=31536000000&HW-CC-Sign=CA4645670C20673D3C377E0D4F1B1764CE2BF040B15CCED93C009B1F387DE60D)

**图10** enableDragBar为true

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/diBBWO6zS-SiSPShRjsUeA/zh-cn_image_0000002817425861.png?HW-CC-KV=V1&HW-CC-Date=20261114T004701Z&HW-CC-Expire=31536000000&HW-CC-Sign=7E0CAF46C8C31FC7697EF04C50360D2133F8249AF808547E444069529EDAE511)

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

```json
{
  "routerMap": [
    {
      "name": "NewsDetail",
      "pageSourceFile": "src/main/ets/pages/navigation/splitmode/NewsDetail.ets",
      "buildFunction": "NewsDetailPageBuilder",
      "data": {
        "description": "this is NewsDetail"
      }
    }
  ]
}
```

子页代码：

```typescript
// 自定义的参数类型，用于在push页面时给子页传递参数
export class NewsItem {
  public title: string;
  public overview: string;
  public content: string;

  constructor(title: string, overview: string, content: string) {
    this.title = title;
    this.overview = overview;
    this.content = content;
  }
}

@Builder
export function NewsDetailPageBuilder() {
  NewsDetail()
}

@Component
struct NewsDetail {
  @State title: string = '';
  @State content: string = '';

  build() {
    NavDestination() {
      Column() {
        Text(this.content)
      }
    }
    .title(this.title)
    .backgroundColor('#fff6e3c8')
    .onReady((ctx: NavDestinationContext) => {
      // 在onReady生命周期拿到传来的页面参数
      let param = ctx.pathInfo.param as NewsItem;
      this.title = param?.title;
      this.content = param?.content;
    })
  }
}
```

主页代码：

```typescript
import { NewsItem } from './NewsDetail'

@Component
struct NewsHome {
  private newsItemArray: Array<NewsItem> = [];
  private stack: NavPathStack | undefined = undefined;

  aboutToAppear(): void {
    // 这里省略了从网络获取新闻信息的过程
    for (let i = 0; i < 50; i++) {
      this.newsItemArray.push(new NewsItem(`新闻标题${i + 1}`, `新闻概述${i + 1}`, `新闻详情${i + 1}`))
    }
    let info = this.queryNavigationInfo();
    this.stack = info?.pathStack;
  }

  build() {
    List() {
      ForEach(this.newsItemArray, (item: NewsItem, index: number) => {
        ListItem() {
          Column() {
            Text(`${item.title}`).margin(15).fontSize(25).fontColor(Color.Black)
            Text(`${item.overview}`).fontSize(13).fontColor(Color.Gray)
          }.margin({bottom: 15}).backgroundColor('#eeeeee').width('100%')
          .borderRadius(15).height(120).onClick(() => {
            // 用户点击某一个新闻标签时，就在右侧子页区域push一个NavDestination页面，用来展示新闻详情
            this.stack?.pushPath({name: 'NewsDetail', param: item})
          })
        }.width('100%')
      }, (item: NewsItem, index: number) => {
        return item.title;
      })
    }.width('100%').height('100%').padding(15)
  }
}

@Entry
@Component
struct Index {
  private stack: NavPathStack = new NavPathStack();
  @State navWidth: number = 100;

  build() {
    RelativeContainer() {
      Navigation(this.stack) {
        NewsHome().width('100%').height('100%')
      }
      .mode(NavigationMode.Split)
      .enableDragBar(true)
      .hideNavBar(false)
      .navBarWidthRange([100, 700]) // 指定NavBar区域的宽度范围
      .minContentWidth(100) // 指定子页区域的最小宽度
      .hideTitleBar(true)
      .hideToolBar(true)
      .height('100%')
      .width(`${this.navWidth}%`)
      .alignRules({
        top: { anchor: '__container__', align: VerticalAlign.Top },
        left: { anchor: '__container__', align: HorizontalAlign.Start }
      })
    }
  }
}
```

**图11** 运行效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/xWx4kEnZRAmxPlFHVI01EQ/zh-cn_image_0000002788466442.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004701Z&HW-CC-Expire=31536000000&HW-CC-Sign=EBACF0A3F44C5A656CE0E047F244310A444C2F2AAAF22A4C3E9EB92232E53D2F)
