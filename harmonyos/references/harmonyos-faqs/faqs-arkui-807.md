---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-807
title: 如何实现页面上滑tabBar和顶部标题的悬停以及属性动画效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现页面上滑tabBar和顶部标题的悬停以及属性动画效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:18+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d2a9cd08d1c31868c49cda089abd281fec358651334203f02ae5ea8f074e43b3
---

## 问题现象

参照Scroll的[示例3](../harmonyos-references/ts-container-scroll.md#示例3嵌套滚动实现方式二)，实现了tabBar在页面顶部的悬停效果。

如果页面顶部还有一个标题栏（即下图中“首页”），现在要实现tab内容向上滚动时tabBar悬停到标题栏下方（即下图中“同城”，“推荐”，“活动”，“玩机”这一行），且可以实现标题栏在滚动过程中样式变化（如下图背景变化），该如何实现？

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/zEyTqjJlQGaBMschjh-wOQ/zh-cn_image_0000002628557796.png "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/oroN3jKURw2xn_cwV3bmcg/zh-cn_image_0000002658917113.png "点击放大")

## 背景知识

[Stack](../harmonyos-references/ts-container-stack.md)：堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。

[Scroll](../harmonyos-references/ts-container-scroll.md)：可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。

* [nestedScroll](../harmonyos-references/ts-container-scroll.md#nestedscroll10)：设置前后两个方向的嵌套滚动模式，实现与父组件的滚动联动。
* [onDidScroll](../harmonyos-references/ts-container-scroll.md#ondidscroll12)：滚动事件回调，Scroll滚动时触发。

## 解决方案

1. 使用Stack层叠布局，将标题栏悬浮展示在页面顶部。
2. 考虑页面滚动以及tabContent里面的list滚动，就要考虑滚动嵌套问题，目前场景需要选择：
   * 向上滚动时：父组件先滚动，父组件滚动到边缘以后自身滚动；
   * 向下滚动时：自身先滚动，自身滚动到边缘以后父组件滚动。

   示例代码如下：

   ```ts
   .nestedScroll({
     scrollForward: NestedScrollMode.PARENT_FIRST,
     scrollBackward: NestedScrollMode.SELF_FIRST
   });
   ```
3. 父组件滚动过程中，根据滚动偏移量线性修改标题栏样式（如字体大小、透明度、背景等），onDidScroll可以返回当前帧滚动的偏移量和当前滚动状态。

   示例代码如下：

   ```ts
   @Entry
   @Component
   struct StickyNestedScroll {
     @State arr: number[] = [];
     @State opacityNum: number = 0;
     @State curYOffset: number = 0;
     @State currentIndex: number = 0;

     aboutToAppear() {
       for (let i = 0; i < 30; i++) {
         this.arr.push(i);
       }
     }

     @Styles
     listCard() {
       .backgroundColor('#FFF')
       .height(64)
       .width('calc(100% - 32vp)')
       .borderRadius(20)
       .margin({
         left: 16,
         right: 16,
       });
     }

     @Builder
     tabBuilder(title: string, targetIndex: number) {
       Column() {
         Text(title)
           .fontColor(this.currentIndex === targetIndex ? '#FFF' : '#000')
           .fontSize(14)
           .fontWeight(this.currentIndex === targetIndex ? 500 : 400);
       }
       .height(36)
       .padding({
         left: 16,
         right: 16,
       })
       .margin({ left: 8 })
       .borderRadius(20)
       .backgroundColor(this.currentIndex === targetIndex ? '#0A59F7' : 'rgba(0, 0, 0, 0.05)')
       .alignItems(HorizontalAlign.Center)
       .justifyContent(FlexAlign.Center);
     }

     build() {
       Stack() {
         Scroll() {
           Column() {
             Image($r('app.media.scrollTopbg')) // 图片资源需自行替换
               .width('100%')
               .height(300);
             Tabs({ barPosition: BarPosition.Start }) {
               ForEach(this.arr.slice(0, 6),
                 (item: number, index: number) => {
                   TabContent() {
                     List({ space: 16 }) {
                       ForEach(this.arr, (item1: number) => {
                         ListItem() {
                           Text('item' + item1)
                             .fontSize(16).fontWeight(400);
                         }.listCard();
                       }, (item1: string) => item1);
                     }.width('100%')
                     .edgeEffect(EdgeEffect.None)
                     .nestedScroll({
                       scrollForward: NestedScrollMode.PARENT_FIRST,
                       scrollBackward: NestedScrollMode.SELF_FIRST
                     });

                   }.tabBar(this.tabBuilder(`标签${item + 1}`, index));
                 }, (item: number, index: number) => JSON.stringify(item) + index);
             }
             .onChange((index) => {
               this.currentIndex = index;
             })
             .barMode(BarMode.Scrollable)
             .barHeight(72)
             .vertical(false)
             .width('100%')
             .height('calc(100% - 80vp)');
           }.width('100%');
         }
         .friction(0.6)
         .scrollBar(BarState.Off)
         .width('100%')
         .height('100%')
         .onDidScroll((xOffset: number, yOffset: number, scrollState: ScrollState): void => {
           // 累计计算当前父组件滚动在Y轴方向的偏移量
           this.curYOffset += yOffset;
           // 根据父组件一共可以滚动的距离计算当前每帧的当前透明度
           let opacity = this.curYOffset / 220;
           if (opacity >= 1) {
             opacity = 1;
           }
           if (opacity <= 0) {
             opacity = 0;
           }
           this.opacityNum = opacity;
           console.info(`xOffset: ${xOffset},scrollState:${scrollState}`);
         });

         // 悬浮标题栏
         Text('工作台')
           .fontSize(24)
           .fontColor('#000')
           .fontWeight(FontWeight.Bold)
           .backgroundColor(`rgba(255,255,255,${this.opacityNum})`)
           .position({ x: 0, y: 0 })
           .width('100%')
           .height(80)
           .padding({ left: 16, top: 44 });
       }.width('100%')
       .height('100%').background('#F1F3F5');
     }
   }
   ```

   效果如图：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/yFj47ZBHTqipBN61SNE6mA/zh-cn_image_0000002628397892.png "点击放大")

## 总结

1. 悬浮类布局首先考虑Stack层叠布局。
2. 嵌套滚动，考虑父子组件之间的先后滚动模式，选择合适的滚动模式。
3. 滚动过程中，获取当前滚动每帧偏移量和滚动状态，做合适的UI更新。
