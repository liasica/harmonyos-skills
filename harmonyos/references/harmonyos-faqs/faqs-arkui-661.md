---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-661
title: Video组件自动播放控制的常见场景
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Video组件自动播放控制的常见场景
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:02+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6305f138dbef816f0b40ac56d62bd131e58d323ed0c52c7e0f16e02827695c56
---

## 问题现象

* 场景一：应用前后台切换自动播放控制。应用切换至后台时自动暂停播放，返回前台时自动恢复播放。
* 场景二：滚动容器可视区域内自动播放控制。视频组件在页面滚动时，离开可视区域自动暂停，进入可视区域自动续播。

## 背景知识

* [Video组件](../harmonyos-references/ts-media-components-video.md)用于播放视频文件并控制其播放状态的组件。一般配合[VideoController](../harmonyos-references/ts-media-components-video.md#videocontroller)控制器使用，其中可以通过[start()](../harmonyos-references/ts-media-components-video.md#start)和[pause()](../harmonyos-references/ts-media-components-video.md#pause)方法控制视频启动和暂停播放。
* 应用前后台切换与监听：组件的生命周期无法直接感知应用整体的前后台切换。可以在[UIAbility](../harmonyos-guides/uiability-lifecycle.md)中通过[onForeground()](../harmonyos-guides/uiability-lifecycle.md#onforeground)和[onBackground()](../harmonyos-guides/uiability-lifecycle.md#onbackground)生命周期回调事件监听应用的前台切换，并设置一个前后台切换状态变量到[AppStorage](../harmonyos-guides/arkts-appstorage.md)，在具体的组件中监听变量的变化。
* [组件可见区域变化事件](../harmonyos-references/ts-universal-component-visible-area-change-event.md)：组件在屏幕中的显示区域面积变化时触发的事件。当组件区域变化时触发[onVisibleAreaChange](../harmonyos-references/ts-universal-component-visible-area-change-event.md#onvisibleareachange)回调。而[onVisibleAreaApproximateChange](../harmonyos-references/ts-universal-component-visible-area-change-event.md#onvisibleareaapproximatechange17)回调可通过设置[expectedUpdateInterval](../harmonyos-references/ts-universal-component-visible-area-change-event.md#visibleareaeventoptions12)参数，可有效降低可见区域比例计算的触发频度。

## 解决方案

* 场景一：应用前后台切换自动播放控制，可通过UIAbility生命周期监听结合全局状态管理实现。具体实现思路：
  1. 在EntryAbility中的onForeground()与onBackground()回调里，通过AppStorage设置一个全局状态标志，用以标识应用的前后台状态。
  2. 在具体的组件中使用[@StorageLink](../cangjie-guides/cj-appstorage.md#storagelink)绑定此状态，并利用[@Watch](../harmonyos-guides/arkts-watch.md)装饰器监听其变化，从而自动调用VideoController的start()或pause()方法，以同步控制视频的播放与暂停。

     具体实现代码可参考该[指南](faqs-media-29.md)。
* 场景二：滚动容器可视区域内自动播放控制，可通过监听Video组件在滚动容器中的可见区域比例变化，实现滚动页面时“可见即播放，不可见即暂停”的播放控制。具体实现思路：
  1. 使用onVisibleAreaChange或onVisibleAreaApproximateChange回调监听组件的可见区域比例变化，并设置一个可见比例阈值（如0.5）。
  2. 当组件可见比例逐渐变大并且超过阈值时，调用VideoController.start()开始播放；当逐渐变小并低于阈值时，调用VideoController.pause()暂停播放。

     具体实现代码：

     ```ts
     @Entry
     @Component
     struct VideoAutoPlayByVisibility {
       @State videoUrl: ResourceStr = $rawfile('video1.mp4'); // 替换为您的本地视频文件路径
       controller: VideoController = new VideoController();

       build() {
         Scroll() {
           Column() {
             Video({
               src: this.videoUrl,
               controller: this.controller
             })
               .width('100%')
               .height(300)
               .autoPlay(false)
               .controls(true)
               .loop(false)
               .objectFit(ImageFit.Contain)
               .onVisibleAreaApproximateChange({ ratios: [0.5], expectedUpdateInterval: 200 },
                 (isExpanding: boolean, currentRatio: number) => {
                   console.info(`Test Video isExpanding: ${isExpanding}, currentRatio: ${currentRatio}`);
                   // 可见比例逐渐变大，并超过一半，开始播放
                   if (isExpanding && currentRatio >= 0.5) {
                     this.controller.start();
                   }
                   // 可见比例逐渐变小，并小于一半，暂停播放
                   if (!isExpanding && currentRatio <= 0.5) {
                     this.controller.pause();
                   }
                 });
             Row().width('100%').backgroundColor('#ffb3afbc').height(300);
             Row().width('100%').backgroundColor('#ff87848d').height(300);
             Row().width('100%').backgroundColor('#ff59575d').height(300);
           };
         }
         .width('100%');
       }
     }
     ```
