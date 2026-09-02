---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-500
title: 自由多窗小页面，页面向上滑动，正文内容跳动
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 自由多窗小页面，页面向上滑动，正文内容跳动
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:569bf8592e700e6dd48f68933f17da722ea71bd74b4d48c06ef5f7bbc2450c1e
---

## 问题现象

自由多窗模式下，应用小窗口展示时，页面向上滑动，部分正文内容跳动恢复到屏幕固定区域展示。

## 背景知识

1. [Scroll](../harmonyos-references/ts-container-scroll.md)可实现当子组件的布局尺寸超过父组件的尺寸时，内容可滚动。
2. [scrollTo](../harmonyos-references/ts-container-scroll.md#scrollto)方法可将滚动组件滚动到某个位置，滚动组件内容的回弹一般是调用了该方法。
3. 通过设置组件的[height](../harmonyos-references/ts-universal-attributes-size.md#height)属性，可控制组件的高度。
4. [Tabs](../harmonyos-references/ts-container-tabs.md)组件可实现通过页签进行内容视图切换的容器组件，每个页签对应一个内容视图。

## 问题定位

* 通过UIView查阅页面布局，找到跳动的内容区域，如下所示。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/VoABkKHQR9CXdAq7dsDl_Q/zh-cn_image_0000002658907555.png "点击放大")
* 查阅页面代码中Scroll组件的一级子组件的height属性，判断Scroll组件滑动到底部时，跳动区域是否会滑出Scroll组件之外，下图通过Tabs组件的tabBar模拟跳动区域，当前TabContent的区域高度大于Scroll组件展示区域，tabBar会滑出Scroll组件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/yw2ys-8_QQe4MIxFJ3pzhg/zh-cn_image_0000002628388356.png "点击放大")
* 查阅页面代码中是否调用scrollTo方法将Scroll组件强制滚动到某个位置。

## 分析结论

页面代码结构为Scroll组件套Tabs组件套List组件，当给Tabs组件设置了固定高度，并且自由多窗小窗场景，Tabs组件的高度高于Scroll组件的显示高度，滑动页面时tabBar会滑出Scroll组件，并且页面代码中调用了scrollTo方法强制将tabBar滑动到页面某个位置，这样就出现了页面内容跳动的情况。

## 修改建议

1. 把Scroll组件中Tabs组件的height属性设置成100%，这样在滑动页面时，滑动的就是TabContent中的List组件内容，tabBar不会滑出Scroll。
2. 删掉调用scrollTo方法强制将tabBar滑动到页面某个位置的代码。

   ```ts
   @Entry
   @Component
   struct WindowLeap {
     scrollController: Scroller = new Scroller();
     list1: Array<string> = [];

     aboutToAppear(): void {
       for (let index = 0; index < 200; index++) {
         this.list1.push(`hello${index}`);
       }
     }

     build() {
       Column() {
         Row()
           .backgroundColor(Color.Red)
           .width('100%')
           .height('20%')
         Scroll() {
           Column() {
             Text("Scroll Area")
               .width("100%")
               .height("40%")
               .backgroundColor('#0080DC')
               .textAlign(TextAlign.Center)
             Tabs({ barPosition: BarPosition.Start }) {
               TabContent() {
                 List({ space: 10 }) {
                   ForEach(this.list1, (item: number) => {
                     ListItem() {
                       Text("item" + item)
                         .fontSize(16)
                     }
                   }, (item: string) => item)
                 }.width("100%")
                 .edgeEffect(EdgeEffect.Spring)
                 .nestedScroll({
                   scrollForward: NestedScrollMode.PARENT_FIRST,
                   scrollBackward: NestedScrollMode.SELF_FIRST
                 })
               }.tabBar("Tab1")

               TabContent() {
               }.tabBar("Tab2")
             }
             .vertical(false)
             // 设置Tabs组件的高度，保证页面滑动过程中tabBar不会滑动到Scroll组件外。
             .height("100%")
           }.width("100%")
         }
         .edgeEffect(EdgeEffect.Spring)
         .friction(0.6)
         .backgroundColor('#DCDCDC')
         .scrollBar(BarState.Off)
         .width('100%')
       }
     }
   }
   ```

效果图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/WZTk9GitQQmjWoNr_cWCFg/zh-cn_image_0000002658787627.png "点击放大")
