---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1504
title: 如何通过Refresh组件实现下拉刷新动画
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何通过Refresh组件实现下拉刷新动画
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:16+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9e9222337ec7b761f668badcb3bcca7371ae027dd958a470b7cfe218f6a8ed3c
---

## 问题现象

如何使用Refresh组件实现下拉刷新动画？要求下拉刷新时页面内容不动，刷新动画始终位于页面顶部，并在刷新过程中展示。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/HBhgB_akSqu8wgwpeo101A/zh-cn_image_0000002628766428.gif "点击放大")

## 背景知识

* [Refresh](../harmonyos-references/ts-container-refresh.md)组件是可以进行页面下拉操作并显示刷新动效的容器组件，它可以采用[animateTo](../harmonyos-references/ts-explicit-animation.md)显式动画来自定义动画效果。
* [Lottie](../quickApp-References/quickapp-component-lottie-0000001266273702.md)是一个适用于OpenHarmony的动画库，它可以解析json格式的动画，并在移动设备上进行本地渲染，以此来实现动画的播放、暂停等操作。

## 解决方案

* **方案一：**使用Refresh组件的默认刷新样式，可以参考文档[Refresh实现下拉刷新动画示例一](../harmonyos-references/ts-container-refresh.md#示例1默认刷新样式)。
* **方案二：**使用Refresh组件结合Lottie实现自定义刷新动画。具体步骤如下：
  1. 引入必要的组件和配置：首先，确保项目中已经引入了Lottie动画库。在项目地址中打开终端，输入以下命令安装组件：

     ```screen
     ohpm install @ohos/lottie
     ```
  2. 引入lottie.json自定义动画文件：json动画文件可以参考[工程示例中的json文件](https://gitcode.com/openharmony-tpc/lottieArkTS/tree/master/entry/src/main/ets/common/lottie)，在“resources/rawfile”文件夹下放入动画文件即可，例如在rawfile文件夹下创建“common/lottie/animation.json”动画文件。
  3. 加载并配置Lottie动画：使用Lottie来配置下拉时的动画效果。

     ```screen
     loadPullDownAnimation() {
       this.animateItem = lottie.loadAnimation({
         container: this.context, // 渲染上下文
         renderer: 'canvas', // canvas渲染模式
         loop: 10, // 是否循环播放,默认true
         autoplay: true, // 是否自动播放，默认true
         name: this.animateName,
         contentMode: 'Contain',
         path: 'common/lottie/animation.json', // json路径
       })
     }
     ```
  4. 在Refresh组件中使用[onStateChange](../harmonyos-references/ts-container-refresh.md#onstatechange)和[onRefreshing](../harmonyos-references/ts-container-refresh.md#onrefreshing)等事件来配置下拉时不同状态下的动画效果。

     ```screen
     import lottie, { AnimationItem } from '@ohos/lottie'

     @Entry
     @Component
     struct RefreshExample {
       @State isRefreshing: boolean = false
       @State arr: String[] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
       private mainCanvasRenderingContext: CanvasRenderingContext2D = new CanvasRenderingContext2D()
       private animateItem: AnimationItem | null = null
       private animateName: string = 'pullDownAnimate'
       private setting: RenderingContextSettings = new RenderingContextSettings(true);
       private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.setting);
       private lottieName: string = 'lottie_data';

       loadPullDownAnimation() {
         this.animateItem = lottie.loadAnimation({
           container: this.context, // 渲染上下文
           renderer: 'canvas', // canvas渲染模式
           loop: 10, // 是否循环播放,默认true
           autoplay: true, // 是否自动播放，默认true
           name: this.animateName,
           contentMode: 'Contain',
           path: 'common/lottie/animation.json', // json路径
         })
       }

       @Builder
       customRefreshComponent() {
         Stack() {
           Row() {
             Canvas(this.context)
               .width('50%')
               .backgroundColor('#aabbcc')
               .onDisAppear(() => {
                 lottie.destroy(this.lottieName) // Canvas销毁时顺带销毁lottie动画
               })
               .onReady(() => {
                 if (this.mainCanvasRenderingContext) {
                   this.mainCanvasRenderingContext.imageSmoothingEnabled = true;
                   this.mainCanvasRenderingContext.imageSmoothingQuality = 'medium';
                   this.loadPullDownAnimation();
                 } else {
                   console.error('mainCanvasRenderingContext is not initialized');
                 }
               })
           }
           .alignItems(VerticalAlign.Center)
         }
         .align(Alignment.Center)
         .clip(true)
         // 设置最小高度约束保证自定义组件高度随刷新区域高度变化时自定义组件高度不会低于minHeight
         .constraintSize({ minHeight: 32 })
         .width('100%')
       }

       build() {
         Column() {
           Refresh({ refreshing: $$this.isRefreshing, builder: this.customRefreshComponent() }) {
             List() {
               ForEach(this.arr, (item: string) => {
                 ListItem() {
                   Text('' + item)
                     .width('70%')
                     .height(80)
                     .fontSize(16)
                     .margin(10)
                     .textAlign(TextAlign.Center)
                     .borderRadius(10)
                     .backgroundColor(0xFFFFFF)
                 }
               }, (item: string) => item)
             }
             .onScrollIndex((first: number) => {
               console.info(first.toString())
             })
             .width('100%')
             .height('100%')
             .alignListItem(ListItemAlign.Center)
             .scrollBar(BarState.Off)
           }
           .backgroundColor(0x89CFF0)
           .pullToRefresh(true)
           .refreshOffset(64)
           .onStateChange((refreshStatus: RefreshStatus) => {
             console.info(`Refresh onStatueChange state is ${refreshStatus}`)
             if (refreshStatus === 0) { // 未下拉
               this.animateItem!.destroy()
               this.animateItem = null
             }
             if (refreshStatus === 1) { // 下拉中
               this.loadPullDownAnimation()
             }
             if (refreshStatus === 3) { // 刷新中
               this.animateItem?.play();
             }
             if (refreshStatus === 4) { // 刷新结束
               setTimeout(() => {
                 this.animateItem!.destroy()
                 this.animateItem = null
               }, 75)
             }
           })
           .onRefreshing(() => {
             setTimeout(() => {
               this.isRefreshing = false
             }, 2000)
             console.info(`onRefreshing test`)
           })
         }
       }
     }
     ```

## 常见FAQ

Q：在Tab栏中通过Refresh组件实现下拉刷新后，重复刷新同一项页面时，刷新效果不会重复显示。

A：可以给Refresh组件绑定一个参数用来控制刷新状态。

```screen
Refresh({ refreshing: $$this.isRefreshing })
```

每次重复刷新时，重置状态变量isRefreshing即可重复触发刷新效果。

Q：Refresh组件如何监听下拉高度变化？

A：可以通过[onOffsetChange](../harmonyos-references/ts-container-refresh.md#onoffsetchange12)方法实时获取下拉高度，以此来控制下拉动画状态。

## 总结

方案一、二都是通过Refresh组件实现下拉刷新动画，但实现方法略有不同，区别如下：

| 方案 | 特点 |
| --- | --- |
| 方案一 | 通过Refresh组件的通用属性来实现动画效果。 |
| 方案二 | 通过引入动画库来实现自定义动画效果。 |

常见场景如下：

* 工具类应用或功能型应用，如电话簿功能。
* 社交媒体应用或视频播放应用等。
