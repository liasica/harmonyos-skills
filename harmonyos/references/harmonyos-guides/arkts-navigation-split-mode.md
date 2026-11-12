---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-split-mode
title: Navigation分栏开发
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 设置组件导航和页面路由 > 组件导航(Navigation) (推荐) > Navigation分栏开发
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:21658beb0e470eb7a04569bdebac58bb84aab21cd0b81072bf957e0d537814e2
---

[Navigation](../harmonyos-references/ts-basic-components-navigation.md)作为一个容器组件，提供了两种布局样式：单栏布局、分栏布局。分栏布局一般适用于宽屏设备，在分栏布局下，导航栏（navBar）会固定显示， 子页面（NavDestination）通过导航控制器（NavPathStack）切换显示， 在导航栏和子页面之间有一条分割线， 可以通过分割线拖拽控制左右显示的比例。架构图详见[Navigation基础架构介绍](arkts-navigation-architecture.md)。

## 分栏相关接口介绍

### mode

[mode](../harmonyos-references/ts-basic-components-navigation.md#mode9)属性用于控制Navigation的显示模式，有四种模式：单栏，分栏，自适应，根据高宽比自适应。

**图1** 单栏（NavigationMode.Stack）效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/N_rE_P5GRfesx_kbQOe7lw/zh-cn_image_0000002786518690.png?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=227A03349E23F0596029BBC7E45CD340F02C84A3A697022A9B60299B08FB3F75)

**图2** 分栏（NavigationMode.Split）效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/FhzvqzsZRAa3Qy_EyISAOA/zh-cn_image_0000002786358762.png?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=0441EB174D6B21144234D7AC663BFB1A49BB5E83098DE582559E050B03563A12)

**图3** 自适应（NavigationMode.Auto）效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/zhM--GiARCGMQFUlv4GEvw/zh-cn_image_0000002815558183.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=5D00B7CCFAADF1521BC3EBDCA65972FED95B036122DCF4AE0602D4B0C6591B07)

**图4** 根据高宽比自适应（NavigationMode.AUTO\_WITH\_ASPECT\_RATIO）效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/yGX4Uz51R3OmQhSTQNrrHg/zh-cn_image_0000002815398267.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=2AD8483FED3C84D7189304A5F4D5F133B06AE64C27B67C0B4C014CC9126DDD7E)

### navBarPosition

[navBarPosition](../harmonyos-references/ts-basic-components-navigation.md#navbarposition9)用于控制导航栏显示的位置，用navBarPosition控制导航栏显示位置时，会被系统语言所影响。比如，在以汉语、英语为代表的LTR语言体系下，NavBarPosition.Start指代的是导航栏出现在左侧，而在以阿拉伯语为代表的RTL语言体系下，NavBarPosition.Start则指代导航栏出现在右侧。类似的效果也出现在NavBarPosition.End上。

**NavBarPosition.Start**

**图5** 系统语言为LTR时NavBarPosition.Start效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/ORFUKLUhSK-IbhhZpoj4ig/zh-cn_image_0000002786518692.png?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=04EEDEC5CB3BDC405E07A3536323EE6FC8D732CBCC4CFD5FE7C415A0ABBC4908)

**图6** 系统语言为RTL时NavBarPosition.Start效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/YQkGujFiTIGA7ReQBnwFxw/zh-cn_image_0000002786358764.png?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=E0D2DE60AC072F802D6432EE92445BC6B9EA05EEB9044FFEF1B6618BE66C92EA)

**NavBarPosition.End**

**图7** 系统语言为LTR时NavBarPosition.End效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/W4lj2kUFT4uPInXvLHr7ew/zh-cn_image_0000002815558185.png?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=026728FB2E6E9983087905A11628320401815D260E475C88DC5FF3FB1929A943)

**图8** 系统语言为RTL时NavBarPosition.End效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/6T8v1d-bQtO2XR1EzsKQNw/zh-cn_image_0000002815398269.png?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=9E65F2D8B8AFC66748F7894742C4A11C928137FA17A3A185F9D57D6B3FBCB88F)

### enableDragBar

[enableDragBar](../harmonyos-references/ts-basic-components-navigation.md#enabledragbar14)用于控制是否显示分栏的拖动按钮。

**图9** enableDragBar为false效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/CwVJ8HaGTYmbTJTXeJHDCQ/zh-cn_image_0000002786518694.png?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=7AFA08E838C58A546E1A81365C5C23624613294B7A98F9DBE76D900FB2B64470)

**图10** enableDragBar为true

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/YxEsOyRZQvy4VdIz1fVWCg/zh-cn_image_0000002786358766.png?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=52A364BD8BF9EB72A3BDFBE3D02429ACA2AEE097AE74EFCE4FD648A22AFC60C3)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/wDV8lyh0QG-E-_j630oSCA/zh-cn_image_0000002815558187.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=B964C2DB1D8A768BD0619EFDF02C3F0994F5C350B952824246FD7EF69D0C0134)
