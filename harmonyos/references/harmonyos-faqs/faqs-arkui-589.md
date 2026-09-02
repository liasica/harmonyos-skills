---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-589
title: 通过滑动Swiper进行router路由跳转时页面闪烁如何解决
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 通过滑动Swiper进行router路由跳转时页面闪烁如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:01+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c2645bf5dd6be052096b5d23de5c6a526cc0e01cdac7325d471bfeff1d85acd9
---

## 问题现象

在Swiper的onAnimationStart方法中进行监听，如果滑动的下一页是最后一页就调用router.back返回。在没有给Swiper添加自定义动效时是正常的，添加动效后，跳转页面时会闪一下。

问题代码示例参考如下：

1. Index.ets。

   ```ts
   @Entry
   @Component
   struct Index {
     build() {
       Column() {
         Button('点击跳转').onClick(() => {
           this.getUIContext().getRouter().pushUrl({ url: 'pages/SecondPage' })
         })
       }.width('100%').height('100%')
     }
   }
   ```
2. SecondPage.ets。

   ```ts
   import { Router, UIContext } from '@kit.ArkUI';

   let uiContext: UIContext = new UIContext();
   let router: Router = uiContext.getRouter();

   @Entry
   @Component
   struct SecondPage {
     private DISPLAY_COUNT: number = 1
     private MIN_SCALE: number = 0.75
     @State backgroundColors: string[] =
       ['#ffd2bf82', '#ff7db5db', '#ff95b784', '#ff867aa7', '#ffae8080', '#ffa98b6a', '#ffa9a9a9']
     @State opacityList: number[] = []
     @State scaleList: number[] = []
     @State translateList: number[] = []
     @State zIndexList: number[] = []

     aboutToAppear(): void {
       for (let i = 0; i < this.backgroundColors.length; i++) {
         this.opacityList.push(1.0)
         this.scaleList.push(1.0)
         this.translateList.push(0.0)
         this.zIndexList.push(0)
       }
     }

     build() {
       Column() {
         Swiper() {
           ForEach(this.backgroundColors, (backgroundColor: Color, index: number) => {
             Text(index.toString())
               .width('100%')
               .height('100%')
               .fontSize(50)
               .textAlign(TextAlign.Center)
               .backgroundColor(backgroundColor) // 自定义动画变化透明度、缩放页面、抵消系统默认位移、渲染层级等
               .opacity(this.opacityList[index])
               .scale({ x: this.scaleList[index], y: this.scaleList[index] })
               .translate({ x: this.translateList[index] })
               .zIndex(this.zIndexList[index])
           })
         }
         .height(300)
         .indicator(false)
         .displayCount(this.DISPLAY_COUNT, true)
         // 关键代码
         .onAnimationStart((index: number, targetIndex: number) => {
           // 目标页面是最后一页则可以开始返回了
           if (targetIndex === this.backgroundColors.length - 1) {
             router.back()
           }
         })
         .customContentTransition({
           // 页面移除视窗时超时1000ms下渲染树
           timeout: 1000,
           // 对视窗内所有页面逐帧回调transition，在回调中修改opacity、scale、translate、zIndex等属性值，实现自定义动画。
           transition: (proxy: SwiperContentTransitionProxy) => {
             if (proxy.position <= proxy.index % this.DISPLAY_COUNT ||
               proxy.position >= this.DISPLAY_COUNT + proxy.index % this.DISPLAY_COUNT) {
               // 同组页面往左滑或往右完全滑出视窗外时，重置属性值
               this.opacityList[proxy.index] = 1.0
               this.scaleList[proxy.index] = 1.0
               this.translateList[proxy.index] = 0.0
               this.zIndexList[proxy.index] = 0
             } else {
               // 同组页面往右滑且未滑出视窗外时，对同组中左右两个页面，逐帧根据position修改属性值，实现两个页面往Swiper中间靠拢并透明缩放的自定义切换动画。
               if (proxy.index % this.DISPLAY_COUNT === 0) {
                 this.opacityList[proxy.index] = 1 - proxy.position / this.DISPLAY_COUNT
                 this.scaleList[proxy.index] =
                   this.MIN_SCALE + (1 - this.MIN_SCALE) * (1 - proxy.position / this.DISPLAY_COUNT)
                 this.translateList[proxy.index] =
                   -proxy.position * proxy.mainAxisLength + (1 - this.scaleList[proxy.index]) * proxy.mainAxisLength / 2.0
               } else {
                 this.opacityList[proxy.index] = 1 - (proxy.position - 1) / this.DISPLAY_COUNT
                 this.scaleList[proxy.index] =
                   this.MIN_SCALE + (1 - this.MIN_SCALE) * (1 - (proxy.position - 1) / this.DISPLAY_COUNT)
                 this.translateList[proxy.index] = -(proxy.position - 1) * proxy.mainAxisLength -
                   (1 - this.scaleList[proxy.index]) * proxy.mainAxisLength / 2.0
               }
               this.zIndexList[proxy.index] = -1
             }
           }
         })
         .onContentDidScroll((selectedIndex: number, index: number, position: number, mainAxisLength: number) => {
           // 监听Swiper页面滑动事件，在该回调中可以实现自定义导航点切换动画等。
           console.info(`onContentDidScroll selectedIndex: ${selectedIndex}, index: ${index}, position: ${
           position} , mainAxisLength: ${mainAxisLength}`)
         })
       }.width('100%')
     }

     pageTransition() {
       PageTransitionEnter({ duration: 500 }).opacity(1)
       PageTransitionExit({ duration: 400 }).opacity(0)
     }
   }
   ```

   问题效果预览：翻到最后一页时会闪一下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/MFca8iSzR0KvalP3t4ubBw/zh-cn_image_0000002628392506.gif "点击放大")

## 效果预览

在切换动画完成后进行跳转则正常展示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/THp_uLSLSWuOHjbvdeK65g/zh-cn_image_0000002658911721.gif "点击放大")

## 背景知识

* [Swiper](../harmonyos-references/ts-container-swiper.md)组件为滑块视图容器，提供子组件滑动轮播显示的能力。
* [onAnimationStart](../harmonyos-references/ts-container-swiper.md#onanimationstart9)方法用于切换动画开始时触发该回调。调用此回调后，切换动画的逻辑将在渲染线程中执行，从而使处于空闲状态的主线程能够充分利用这段时间来加载子组件所需资源，减少后续在cachedCount范围内节点的预加载时间。[onAnimationEnd](../harmonyos-references/ts-container-swiper.md#onanimationend9)方法用于切换动画结束时触发该回调。

## 解决方案

经过测试发现是onAnimationStart动画与router路由的页面切换效果存在冲突，目前没有办法解决。

可修改为在onAnimationEnd中执行router.back()进行规避。

即将上述SecondPage.ets中的onAnimationStart方法改为：

```screen
.onAnimationEnd((index: number, extraInfo: SwiperAnimationEvent) => {
  if (index === this.backgroundColors.length - 1) {
    router.back()
  }
})
```

完整示例参考如下：

1. Index.ets：

   ```screen
   @Entry
   @Component
   struct Index {
     build() {
       Column() {
         Button('点击跳转').onClick(() => {
           this.getUIContext().getRouter().pushUrl({ url: 'pages/SecondPage' })
         })
       }.width('100%').height('100%')
     }
   }
   ```
2. SecondPage.ets：

   ```screen
   import { Router, UIContext } from '@kit.ArkUI';

   let uiContext: UIContext = new UIContext();
   let router: Router = uiContext.getRouter();

   @Entry
   @Component
   struct SecondPage {
     private DISPLAY_COUNT: number = 1
     private MIN_SCALE: number = 0.75
     @State backgroundColors: string[] =
       ['#ffd2bf82', '#ff7db5db', '#ff95b784', '#ff867aa7', '#ffae8080', '#ffa98b6a', '#ffa9a9a9']
     @State opacityList: number[] = []
     @State scaleList: number[] = []
     @State translateList: number[] = []
     @State zIndexList: number[] = []

     aboutToAppear(): void {
       for (let i = 0; i < this.backgroundColors.length; i++) {
         this.opacityList.push(1.0)
         this.scaleList.push(1.0)
         this.translateList.push(0.0)
         this.zIndexList.push(0)
       }
     }

     build() {
       Column() {
         Swiper() {
           ForEach(this.backgroundColors, (backgroundColor: Color, index: number) => {
             Text(index.toString())
               .width('100%')
               .height('100%')
               .fontSize(50)
               .textAlign(TextAlign.Center)
               .backgroundColor(backgroundColor) // 自定义动画变化透明度、缩放页面、抵消系统默认位移、渲染层级等
               .opacity(this.opacityList[index])
               .scale({ x: this.scaleList[index], y: this.scaleList[index] })
               .translate({ x: this.translateList[index] })
               .zIndex(this.zIndexList[index])
           })
         }
         .height(300)
         .indicator(false)
         .displayCount(this.DISPLAY_COUNT, true)
         // 关键代码
         .onAnimationEnd((index: number, extraInfo: SwiperAnimationEvent) => {
           if (index === this.backgroundColors.length - 1) {
             router.back()
           }
         })
         .customContentTransition({
           // 页面移除视窗时超时1000ms下渲染树
           timeout: 1000,
           // 对视窗内所有页面逐帧回调transition，在回调中修改opacity、scale、translate、zIndex等属性值，实现自定义动画。
           transition: (proxy: SwiperContentTransitionProxy) => {
             if (proxy.position <= proxy.index % this.DISPLAY_COUNT ||
               proxy.position >= this.DISPLAY_COUNT + proxy.index % this.DISPLAY_COUNT) {
               // 同组页面往左滑或往右完全滑出视窗外时，重置属性值
               this.opacityList[proxy.index] = 1.0
               this.scaleList[proxy.index] = 1.0
               this.translateList[proxy.index] = 0.0
               this.zIndexList[proxy.index] = 0
             } else {
               // 同组页面往右滑且未滑出视窗外时，对同组中左右两个页面，逐帧根据position修改属性值，实现两个页面往Swiper中间靠拢并透明缩放的自定义切换动画。
               if (proxy.index % this.DISPLAY_COUNT === 0) {
                 this.opacityList[proxy.index] = 1 - proxy.position / this.DISPLAY_COUNT
                 this.scaleList[proxy.index] =
                   this.MIN_SCALE + (1 - this.MIN_SCALE) * (1 - proxy.position / this.DISPLAY_COUNT)
                 this.translateList[proxy.index] =
                   -proxy.position * proxy.mainAxisLength + (1 - this.scaleList[proxy.index]) * proxy.mainAxisLength / 2.0
               } else {
                 this.opacityList[proxy.index] = 1 - (proxy.position - 1) / this.DISPLAY_COUNT
                 this.scaleList[proxy.index] =
                   this.MIN_SCALE + (1 - this.MIN_SCALE) * (1 - (proxy.position - 1) / this.DISPLAY_COUNT)
                 this.translateList[proxy.index] = -(proxy.position - 1) * proxy.mainAxisLength -
                   (1 - this.scaleList[proxy.index]) * proxy.mainAxisLength / 2.0
               }
               this.zIndexList[proxy.index] = -1
             }
           }
         })
         .onContentDidScroll((selectedIndex: number, index: number, position: number, mainAxisLength: number) => {
           // 监听Swiper页面滑动事件，在该回调中可以实现自定义导航点切换动画等。
           console.info(`onContentDidScroll selectedIndex: ${selectedIndex}, index: ${index}, position: ${
           position} , mainAxisLength: ${mainAxisLength}`)
         })
       }.width('100%')
     }

     pageTransition() {
       PageTransitionEnter({ duration: 500 }).opacity(1)
       PageTransitionExit({ duration: 400 }).opacity(0)
     }
   }
   ```
