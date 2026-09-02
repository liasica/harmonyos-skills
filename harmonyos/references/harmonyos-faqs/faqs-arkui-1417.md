---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1417
title: Scroll嵌套List滚动回顶部的动画实现
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Scroll嵌套List滚动回顶部的动画实现
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:10+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:07b502660a9bc04c1749388f0daf7efaa0f5b24f681bddef71e43d63301d90c7
---

## 问题现象

在Scroll嵌套List组件时，使用按钮回到顶部时List没有动画效果，仅有Scroll有滚动动画。如何在滚动回顶部时具有动画效果，并且Tab吸顶？

## 效果预览

点击按钮返回顶部时，Scroll和List同时出现滚动动画。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/IyUwNjPcRUGF9kCK7PoeRg/zh-cn_image_0000002628603272.gif "点击放大")

## 背景知识

* [Scroll](../harmonyos-references/ts-container-scroll.md)可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。
* [List](../harmonyos-references/ts-container-list.md)列表包含一系列相同宽度的列表项。
  + [nestedScroll](../harmonyos-references/ts-container-list.md#nestedscroll10)：设置前后两个方向的嵌套滚动模式，实现与父组件的滚动联动。
* [Scroller](../harmonyos-references/ts-container-scroll.md#scroller)可滚动容器组件的控制器，可以控制容器组件的滚动。
  + [scrollTo](../harmonyos-references/ts-container-scroll.md#scrollto)：滑动到指定位置，可以设置动画效果。
  + [scrollEdge](../harmonyos-references/ts-container-scroll.md#scrolledge)：滚动到容器边缘，Scroll组件默认有动画，Grid、List、WaterFlow组件默认无动画。

## 解决方案

1. 使用nestedScroll设置List与Scroll联动的方式。向尾部滚动时Scroll先滚动，向首部滚动时List先滚动。

   ```screen
   .nestedScroll({
     scrollForward: NestedScrollMode.PARENT_FIRST,
     scrollBackward: NestedScrollMode.SELF_FIRST
   });
   ```
2. 通过按钮控制滚动组件回到顶部，可以使用scrollTo来实现滚动动画效果。

   ```screen
   this.scrollerForScroll.scrollTo({ xOffset: 0, yOffset: 0, animation: { duration: 1000 } });
   this.scrollerForList.scrollTo({ xOffset: 0, yOffset: 0, animation: { duration: 1000 } });
   ```

完整示例参考如下：

```screen
@Entry
@Component
struct ListWithinScrollAnimation {
  private scrollerForScroll: Scroller = new Scroller();
  private scrollerForList: Scroller = new Scroller();
  private tabController: TabsController = new TabsController();
  @State listInfoItem: Array<ResourceStr> = new Array(10).fill($r('app.media.img1')); // 图片资源需自行替换
  @State tabBarContent: Array<string> = ['第一页', '第二页', '第三页'];

  @Builder
  tabBuilder(item: string) {
    Column() {
      Text(item)
        .width(100)
        .height(50)
        .textAlign(TextAlign.Center);
    }.width('100%');
  }

  @Builder
  tabContentData() {
    List({ space: 10, scroller: this.scrollerForList }) {
      ForEach(this.listInfoItem, (item: ResourceStr) => {
        ListItem() {
          Column() {
            Image(item).width('80%');
            Text('我不再迷茫，思念是唯一的行囊，满天的星光，有一颗是你的愿望')
              .fontSize(14)
              .margin({ top: 4 })
              .maxLines(2)
              .textOverflow({ overflow: TextOverflow.Ellipsis })
              .fontColor($r('sys.color.ohos_id_color_text_secondary'))
              .padding(10);
            Button('立即购买')
              .height(40)
              .backgroundColor(Color.Orange)
              .width('80%')
              .margin({ bottom: 24 });
          }
          .width('100%')
          .borderRadius(12)
          .alignItems(HorizontalAlign.Center)
          .backgroundColor($r('sys.color.ohos_id_color_background'));
        };
      });
    }
    .scrollBar(BarState.Off)
    .edgeEffect(EdgeEffect.None)
    .nestedScroll({
      scrollForward: NestedScrollMode.PARENT_FIRST,
      scrollBackward: NestedScrollMode.SELF_FIRST
    });
  }

  build() {
    Stack({ alignContent: Alignment.Center }) {
      Scroll(this.scrollerForScroll) {
        Column() {
          Swiper() {
            ForEach(this.listInfoItem, () => {
              Image($r('app.media.img2')); // 图片资源需自行替换
            });
          }
          .height(250)
          .loop(true)
          .autoPlay(true)
          .interval(1000);

          Tabs({ barPosition: BarPosition.Start, index: 0, controller: this.tabController }) {
            ForEach(this.tabBarContent, (item: string) => {
              TabContent() {
                this.tabContentData();
              }.tabBar(this.tabBuilder(item));
            });
          }.vertical(false).barWidth('100%');
        };
      }.scrollBar(BarState.Off);

      Button('back top')
        .height('5%')
        .onClick(() => {
          this.scrollerForScroll.scrollTo({ xOffset: 0, yOffset: 0, animation: { duration: 1000 } });
          this.scrollerForList.scrollTo({ xOffset: 0, yOffset: 0, animation: { duration: 1000 } });
        });
    };
  }
}
```
