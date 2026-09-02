---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-572
title: 判断滚动与滑动容器组件的子组件是否可见
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 判断滚动与滑动容器组件的子组件是否可见
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:18+08:00
doc_updated_at: 2026-07-31
content_hash: sha256:1cfdb71e9f6e0ecd8fed2b2635634753f8f780ab9bf3cb5ad904a5190135d32a
---

## 问题现象

使用List组件时，子组件在滑动过程中会滑出主页面，如何确认子组件当前是否可见？

```ts
onScrollStop(() => {
  // 滚动结束后，判断是否需要播放新的视频（不是上一个索引&&上一个视频一半超出屏幕）
  if (this.scrollIndex !== this.currentPlayIndex && this.theLastIsOutScreen) {
    this.currentPlayIndex = this.scrollIndex
    this.theLastIsOutScreen = false
    this.isShowPlay = true
  }

  // 需求，在这里判断index为currentPlayIndex+1的Image视图是否可见？

})
```

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/jaUDbjl3RW6UBefPKB6CRQ/zh-cn_image_0000002658791435.png "点击放大")

## 背景知识

* [getItemRect](../harmonyos-references/ts-container-scroll.md#getitemrect11)：方法获取子组件的大小及相对于容器组件的位置。支持Scroll、List、Grid、WaterFlow组件。其参数index必须是当前显示区域显示的子组件的索引值，否则视为非法值。非法值返回的大小和位置均为0。
* [RectResult](../harmonyos-references/ts-universal-attributes-on-child-touch-test.md#rectresult)：子组件的大小和相对于组件的位置。getItemRect方法的返回值对象。

## 解决方案

通过getItemRect方法，获取RectResult对象，判断其属性x、y、width、height的值是否均不为0，否则不可见。

以List组件为例：

1. VideoListPage页面。

   ```ts
   import { display } from '@kit.ArkUI';

   @Entry
   @Component
   struct VideoListPage {
     // 图片资源需要开发者自行更换
     private list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
     // 是否在播放
     @State isShowPlay: boolean = false;
     @State screenHeight: number = 0;
     @State screenWidth: number = 0;
     // 记录当前播放的索引
     @State currentPlayIndex: number = 0;
     // 列表当前滚动到的位置
     @State scrollIndex: number = 0;
     // 上一个播放的视频是否一半已经超出屏幕
     @State theLastIsOutScreen: boolean = false;
     mDirection: number = 0;
     playPosition: number | undefined = 0;
     private listScroller: Scroller = new Scroller();

     aboutToAppear(): void {
       this.currentPlayIndex = 2;
       this.isShowPlay = true;

       this.screenWidth = this.getUIContext().px2vp(display.getDefaultDisplaySync().width);
       this.screenHeight = this.getUIContext().px2vp(display.getDefaultDisplaySync().width) * 9 / 16; // '30%';
     }

     build() {
       List({ scroller: this.listScroller }) {
         ForEach(this.list, (item: string, index: number) => {
           ListItem() {
             Stack() {
               if (this.isShowPlay && this.currentPlayIndex === index) {
                 VideoView()
                   .height(this.screenHeight)
                   .width(this.screenWidth)
                   .onVisibleAreaChange([0, 0.5], (isVisible: boolean, currentRatio: number) => {
                     if (this.currentPlayIndex === index) {
                       console.info(`isVisible: ${isVisible}`);
                       // 视频的一半超出屏幕
                       if (currentRatio <= 0.5) {
                         this.theLastIsOutScreen = true;
                       } else {
                         this.theLastIsOutScreen = false;
                       }
                     }
                   })
               } else {
                 Image($r('app.media.scrollDemo')) // 图片资源需开发者自行更换
                   .backgroundColor(Color.Gray)
                   .onClick(() => {
                     this.currentPlayIndex = index;
                     this.isShowPlay = true;
                     console.info(`item: ${item}`);
                   })
                   .height(this.screenHeight)
                   .width(this.screenWidth);
               }
             }
             .visibility(this.mDirection === 1 && this.currentPlayIndex !== index ? Visibility.None : Visibility.Visible);
           };
         });
       }
       .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
       .onScrollIndex((start: number, end: number, center: number) => {
         // 记录滚动最后一次中间的位置
         this.scrollIndex = center;
         console.info(`start: ${start}`);
         console.info(`end: ${end}`);
       })
       .onScrollStop(() => {
         // 滚动结束后，判断是否需要播放新的视频（不是上一个索引&&上一个视频一半超出屏幕）
         if (this.scrollIndex !== this.currentPlayIndex && this.theLastIsOutScreen) {
           this.theLastIsOutScreen = false;
           this.isShowPlay = true;
         }
         // 需求，在这里判断index为currentPlayIndex+1的Image视图是否可见？
         try {
           let rectResult = this.listScroller.getItemRect(this.currentPlayIndex + 1);
           console.info(`RectResult.x：${rectResult.x}`);
           console.info(`RectResult.y：${rectResult.y}`);
           console.info(`RectResult.width：${rectResult.width}`);
           console.info(`RectResult.height：${rectResult.height}`);
         } catch (error) {
           console.error(`error: ${error}`);
         }
       });
     }
   }
   ```
2. VideoView页面。

   ```ts
   @Component
   export struct VideoView {
     // 上下滑动手势，控制音量和亮度
     private panOptionBrightAndVolume: PanGestureOptions = new PanGestureOptions({ direction: PanDirection.Vertical });
     // 左右滑动手势，控制快进快退
     private panOptionSeek: PanGestureOptions = new PanGestureOptions({ direction: PanDirection.Horizontal });

     build() {
       Row()
         .gesture(GestureGroup(GestureMode.Exclusive,
           TapGesture({ count: 2 }).onAction((event: GestureEvent | undefined) => {
             // 双击
             console.info(`event: ${event}`);
           }),
           TapGesture().onAction((event: GestureEvent | undefined) => {
             // 单击
             console.info(`event: ${event}`);
           }),
           PanGesture(this.panOptionBrightAndVolume)
             .onActionStart((event: GestureEvent | undefined) => {
               console.info(`event: ${event}`);
             })
             .onActionUpdate((event: GestureEvent | undefined) => {
               console.info(`event: ${event}`);
             })
             .onActionEnd((event: GestureEvent | undefined) => {
               console.info(`event: ${event}`);
             }),
           PanGesture(this.panOptionSeek)
             .onActionStart((event: GestureEvent | undefined) => {
               console.info(`event: ${event}`);
             })
             .onActionUpdate((event: GestureEvent | undefined) => {
               console.info(`event: ${event}`);
             })
             .onActionEnd((event: GestureEvent | undefined) => {
               console.info(`event: ${event}`);

             })
         ))
         .onGestureJudgeBegin((gestureInfo: GestureInfo, event: BaseGestureEvent) => {
           console.info(`event: ${event}`);
           if (gestureInfo.type === GestureControl.GestureType.PAN_GESTURE) {
             // 返回，REJECT，会使拖动手势失败
             return GestureJudgeResult.REJECT;
           }
           return GestureJudgeResult.CONTINUE;
         })
         .height('100%')
         .width('100%')
         .backgroundColor(Color.White);
     }
   }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/f-iZdo8-T2CaFp1EXcR0nA/zh-cn_image_0000002628552048.png "点击放大")
