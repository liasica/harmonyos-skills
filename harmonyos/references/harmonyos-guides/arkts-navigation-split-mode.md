---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-split-mode
title: Navigation分栏开发
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 设置组件导航和页面路由 > 组件导航(Navigation) (推荐) > Navigation分栏开发
category: harmonyos-guides
scraped_at: 2026-11-21T09:11:05+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:4790862ffff15d858db49f1978460065fa969d2502f6f27fde2e5cc0a56fe57c
---

[Navigation](../harmonyos-references/ts-basic-components-navigation.md)作为一个容器组件，提供了两种布局样式：单栏布局、分栏布局。分栏布局一般适用于宽屏设备，在分栏布局下，导航栏（navBar）会固定显示， 子页面（NavDestination）通过导航控制器（NavPathStack）切换显示， 在导航栏和子页面之间有一条分割线， 可以通过分割线拖拽控制左右显示的比例。架构图详见[Navigation基础架构介绍](arkts-navigation-architecture.md)。

## 分栏相关接口介绍

### mode

[mode](../harmonyos-references/ts-basic-components-navigation.md#mode9)属性用于控制Navigation的显示模式，有四种模式：单栏，分栏，自适应，根据高宽比自适应。

**图1** 单栏（NavigationMode.Stack）效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/BBK6kYyIQy22tSgouMGSlg/zh-cn_image_0000002792876472.png?HW-CC-KV=V1&HW-CC-Date=20261121T011105Z&HW-CC-Expire=31536000000&HW-CC-Sign=6560680FD03AD38DE60692648D8070BCF435D7545D3E0DE5C5C88D6573ACBA46)

**图2** 分栏（NavigationMode.Split）效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/6G453FWtRyi8z2W8KAtryg/zh-cn_image_0000002821836377.png?HW-CC-KV=V1&HW-CC-Date=20261121T011105Z&HW-CC-Expire=31536000000&HW-CC-Sign=AA69EF33111E6F18BE2C35F74396685D2741F25FF147C7417B96AD7B85E62291)

**图3** 自适应（NavigationMode.Auto）效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/WIsoewAPT1eSBtgj4B-f4w/zh-cn_image_0000002821756377.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011105Z&HW-CC-Expire=31536000000&HW-CC-Sign=BE95E89296F2198D00A707ABCC335D5A68A72E2A99B9E51CD5F8D83773FE4068)

**图4** 根据高宽比自适应（NavigationMode.AUTO\_WITH\_ASPECT\_RATIO）效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/qzjl9rFYRLK_qDMgi1NTjg/zh-cn_image_0000002793036442.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011105Z&HW-CC-Expire=31536000000&HW-CC-Sign=F015B573663EF5DCB11799CA1BB94908875C2DE811510E256E502B0EA6A1E18B)

### navBarPosition

[navBarPosition](../harmonyos-references/ts-basic-components-navigation.md#navbarposition9)用于控制导航栏显示的位置，用navBarPosition控制导航栏显示位置时，会被系统语言所影响。比如，在以汉语、英语为代表的LTR语言体系下，NavBarPosition.Start指代的是导航栏出现在左侧，而在以阿拉伯语为代表的RTL语言体系下，NavBarPosition.Start则指代导航栏出现在右侧。类似的效果也出现在NavBarPosition.End上。

**NavBarPosition.Start**

**图5** 系统语言为LTR时NavBarPosition.Start效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/0WTYJ9CIQxW9agMMxn9cYw/zh-cn_image_0000002792876474.png?HW-CC-KV=V1&HW-CC-Date=20261121T011105Z&HW-CC-Expire=31536000000&HW-CC-Sign=7BFE2D66BFF265553E29110E8BEEF442DF375B1F46AA6D7B226DCE2A7DDB8499)

**图6** 系统语言为RTL时NavBarPosition.Start效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/wp_4g6KDQZGI12kbNMbyxw/zh-cn_image_0000002821836379.png?HW-CC-KV=V1&HW-CC-Date=20261121T011105Z&HW-CC-Expire=31536000000&HW-CC-Sign=5A054C119CB14040E8F3A8A7C2EEF6D37BF29E8C9FCA490EB78347ADB889D673)

**NavBarPosition.End**

**图7** 系统语言为LTR时NavBarPosition.End效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/Nb8GVd53Q5uzYR_9b-9NOA/zh-cn_image_0000002821756381.png?HW-CC-KV=V1&HW-CC-Date=20261121T011105Z&HW-CC-Expire=31536000000&HW-CC-Sign=7A3674E3B6968D210D5378889E456A23F6D8ED0A4B6B042F73C3E49735A4D08D)

**图8** 系统语言为RTL时NavBarPosition.End效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/dQMSw-20QSSFiWhdk6M0MQ/zh-cn_image_0000002793036444.png?HW-CC-KV=V1&HW-CC-Date=20261121T011105Z&HW-CC-Expire=31536000000&HW-CC-Sign=AAF5697B398FE76FF42C4385A4B6346CD26346CF3C509BCA25DFEE240825E300)

### enableDragBar

[enableDragBar](../harmonyos-references/ts-basic-components-navigation.md#enabledragbar14)用于控制是否显示分栏的拖动按钮。

**图9** enableDragBar为false效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/WHjL0tRNTRmcwoX2HRbhVA/zh-cn_image_0000002792876476.png?HW-CC-KV=V1&HW-CC-Date=20261121T011105Z&HW-CC-Expire=31536000000&HW-CC-Sign=0CC37190EA020511C735AE1631EAF5ADBEA44F09963280B64F0C0E57C8F47FD7)

**图10** enableDragBar为true

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/l_CvRporR_qBM7pqrqEXzw/zh-cn_image_0000002821836381.png?HW-CC-KV=V1&HW-CC-Date=20261121T011105Z&HW-CC-Expire=31536000000&HW-CC-Sign=E8C045A2260FE4BE2ECA47C10F23F04BF06DCFA0C0AB6E24E84898955E961CA3)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/zzmdjr3dRG6dmOnExCPyAw/zh-cn_image_0000002821756383.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011105Z&HW-CC-Expire=31536000000&HW-CC-Sign=4DEB817180C3149C8974802F6A89CA46859D0BCA033D1C114C9165FD3E4CEF49)
