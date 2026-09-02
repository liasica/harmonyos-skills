---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-684
title: 如何准确统计List中Item的曝光
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何准确统计List中Item的曝光
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:02+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:960616ea1089420f314987407347f416bfd354e6f2ee239b0f1f9a8271a51a56
---

## 问题现象

当Scroll嵌套List且List跟随Scroll滚动时，如何在滚动停止后延迟统计曝光？此时List的onScrollStop未触发，且延迟上报时若再次发生滚动，可能导致误报已不可见的Item。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/yxKKf_iGQvasHbthq5BBug/zh-cn_image_0000002628394852.png "点击放大")

## 背景知识

* [Scroll组件](../harmonyos-references/ts-container-scroll.md)特性：外层Scroll控制整体滚动行为，嵌套的List不会独立触发滚动事件，其滚动状态依赖外层Scroll。
* [onScrollIndex](../harmonyos-references/ts-container-list.md#onscrollindex)：当List子组件（如ListItem）划入或划出可视区域时触发，返回当前可视区域的首索引（firstIndex）、尾索引（lastIndex）及中心索引（centerIndex）。
* [onScrollStop](../harmonyos-references/ts-container-list.md#onscrollstop)：仅在List滚动完全停止时触发一次，但需确保List未禁用边缘效果（如edgeEffect(EdgeEffect.None)），否则可能无法正常回调。

## 解决方案

在List的onScrollIndex中持续更新当前可视区域的起始与结束索引，在onScrollStop中记录此时的索引快照，并设置一个500ms的定时器进行验证：如果在该时间内没有新的滚动发生（即当前索引未发生变化），则说明可视区域稳定，可安全上报曝光；反之则取消此次上报，避免因后续滚动导致的误判。

步骤如下：

1. 实时记录可视索引：在List的onScrollIndex中更新startIndex和endIndex，确保这两个状态变量始终反映当前可视区域的首尾Item索引。

   ```ts
   .onScrollIndex((firstIndex: number, lastIndex: number) => {
     this.startIndex = firstIndex; // 实时更新可视区域起始索引
     this.endIndex = lastIndex; // 实时更新可视区域结束索引
   })
   ```
2. 滚动停止后启动延迟验证：在外层Scroll的onScrollStop中，保存当前的startIndex和endIndex作为快照（如upStartIndex），并设置一个500ms的定时器验证是否发生新滚动。

   ```ts
   .onScrollStop(() => {
     let upStartIndex = this.startIndex; // 滚动停止时保存当前索引快照
     setTimeout(() => {
       console.info('输出：upStartIndex', upStartIndex);
       console.info('输出：this.startIndex', this.startIndex); // onScrollStop只在滚动停止时回调
       if (upStartIndex !== this.startIndex) {
         // 若在此期间发生了新滚动，则不执行曝光上报
         this.getUIContext().showAlertDialog({
           message: '输出：不上报',
           autoCancel: true,
           alignment: DialogAlignment.Bottom,
           offset: { dx: 0, dy: -20 },
         });
       } else {
         // 若索引一致，说明可视区域稳定，可执行曝光上报
         this.getUIContext().showAlertDialog({
           message: '输出：上报',
           autoCancel: true,
           alignment: DialogAlignment.Bottom,
           offset: { dx: 0, dy: -20 },
         });
       }
     }, 3000); // 延迟时间可根据实际需求调整为500ms
   })
   .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
   ```
3. 通过索引快照判断是否误报：定时器内对比保存的快照索引（upStartIndex）与当前索引（this.startIndex）：若一致，说明500ms内未发生新滚动，可视区域稳定，可上报；若不一致，说明后续滚动导致Item不可见，需取消上报。
4. 完整代码如下：

   ```ts
   @Entry
   @Component
   struct NestedScroll {
     private arr: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
     private scrollerForScroll: Scroller = new Scroller();
     private scrollerForList: Scroller = new Scroller();
     @State startIndex: number = 0; // 当前可视区域起始索引
     @State endIndex: number = 0; // 当前可视区域结束索引

     build() {
       List({ space: 20, scroller: this.scrollerForList }) {
         ForEach(this.arr, (item: number) => {
           ListItem() {
             Text('ListItem' + item)
               .width('100%')
               .height('100%')
               .borderRadius(15)
               .fontSize(16)
               .textAlign(TextAlign.Center)
               .backgroundColor('#f1f3f5');
           }
           .width('85%')
           .height(100);
         }, (item: string) => item);
       }
       .scrollBar(BarState.Off)
       .alignListItem(ListItemAlign.Center)
       .edgeEffect(EdgeEffect.None) // 禁用边缘效果以确保onScrollStop正确触发
       .friction(0.6)
       .onScrollIndex((firstIndex: number, lastIndex: number) => {
         this.startIndex = firstIndex; // 实时更新可视区域起始索引
         this.endIndex = lastIndex; // 实时更新可视区域结束索引
       })
       .onScrollStop(() => {
         let upStartIndex = this.startIndex; // 滚动停止时保存当前索引快照
         setTimeout(() => {
           console.info('输出：upStartIndex', upStartIndex);
           console.info('输出：this.startIndex', this.startIndex); // onScrollStop只在滚动停止时回调
           if (upStartIndex !== this.startIndex) {
             // 若在此期间发生了新滚动，则不执行曝光上报
             this.getUIContext().showAlertDialog({
               message: '输出：不上报',
               autoCancel: true,
               alignment: DialogAlignment.Bottom,
               offset: { dx: 0, dy: -20 },
             });
           } else {
             // 若索引一致，说明可视区域稳定，可执行曝光上报
             this.getUIContext().showAlertDialog({
               message: '输出：上报',
               autoCancel: true,
               alignment: DialogAlignment.Bottom,
               offset: { dx: 0, dy: -20 },
             });
           }
         }, 3000); // 延迟时间可根据实际需求调整为500ms
       })
       .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
     }
   }
   ```
