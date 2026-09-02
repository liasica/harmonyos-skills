---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-651
title: List列表子组件按照顺序动画展示
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > List列表子组件按照顺序动画展示
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:24+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:34bb8619c27fc946ff89ed30edf3efc931eb462b74e3ebdbecaa5bd9f8e44010
---

## 问题现象

列表（List）通常会一次性全部展示出来，那么如何实现列表中的子组件能够依照链式先后顺序动画进行展示？

## 背景知识

组件的某些通用属性变化时，可以通过[animation](../harmonyos-references/ts-animatorproperty.md)属性动画实现渐变过渡效果。

## 解决方案

1. 根据数据源this.data创建List。

   ```ts
   if (this.isShow) {
     List() {
       ForEach(this.data, (item: number) => {
         ListItem() {
           CardItem({ index: item });
         }
         .margin(10)
       }, (item: number) => item.toString())
     }
   }
   ```
2. 创建List的每个子组件CardItem,该组件可以根据其在列表中的索引（index）来计算出一个适当的延迟时间，从而实现一种链式的动画效果，即前一个动画结束之后，下一个动画随即开始。

   ```ts
   .animation({
     duration: 500,
     delay: this.index * 120,
     curve: Curve.EaseOut
   })
   ```
3. 当CardItem组件首次出现在视图中（即onAppear事件被触发时），将启动该组件的入场动画。

   ```ts
   .onAppear(() => {
     this.isAppear = true;
   })
   .onDisAppear(() => {
     this.isAppear = false;
   })
   ```
4. 完整示例参考如下：

   ```ts
   @Component
   struct CardItem {
     // 创建List的每个子组件CardItem
     @Prop index: number;
     @State isAppear: boolean = false;
     build() {
       Column() {
         Text(`${this.index}`).fontColor(Color.Blue).fontSize(24);
       }
       .justifyContent(FlexAlign.Center)
       .alignItems(HorizontalAlign.Center)
       .backgroundColor(Color.Green)
       .height(60)
       .width('100%')
       .opacity(this.isAppear ? 1 : 0)
       .translate({ x: this.isAppear ? 0 : 100 })
       .borderRadius(8)
       // 增加动画效果
       .animation({
         duration: 500,
         delay: this.index * 120,
         curve: Curve.EaseOut
       })
       // 组件出现启动组件的入场动画
       .onAppear(() => {
         this.isAppear = true;
       })
       .onDisAppear(() => {
         this.isAppear = false;
       })
     }
   }

   @Entry
   @Component
   struct ChainList {
     private data: number[] = [0, 1, 2, 3, 4, 5];
     @State isShow: boolean = false;  // 是否展示List
     build() {
       Column() {
         Button('show list').onClick(() => {
           this.isShow = !this.isShow;
         })
         // 根据数据源this.data创建List
         if (this.isShow) {
           List() {
             ForEach(this.data, (item: number) => {
               ListItem() {
                 CardItem({ index: item });
               }
               .margin(10)
             }, (item: number) => item.toString())
           }
         }
       }.justifyContent(FlexAlign.Center).width('100%')
     }
   }
   ```

## 总结

属性动画（animation）能够与诸如列表(List)之类的组件相配合，通过调整这些组件的特定属性，如width、height、backgroundColor等，实现一系列动态视觉效果。
