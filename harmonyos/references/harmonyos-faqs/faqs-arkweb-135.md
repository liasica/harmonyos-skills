---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-135
title: Web组件点击全屏播放导致页面布局错乱的问题如何处理
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web组件点击全屏播放导致页面布局错乱的问题如何处理
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c4e0dcee9f89266517c88611150b92fc63d10022fdee3c3d95770c73c9ba9476
---

## 问题现象

Web组件引用三方H5页面加载的视频，当点击视频全屏，视频区域会被组件占用，无法进行全屏播放，导致布局错乱。如何通过HarmonyOS的方法来解决布局错乱的问题？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/vz6-dl3sThqJo3DqLM6FnA/zh-cn_image_0000002659258353.png "点击放大")

## 背景知识

* Web组件可以实现页面加载的功能。页面加载数据来源有三种常用场景：包括加载网络页面、加载本地页面、加载HTML格式的富文本数据。可以在官方文档中查看更多关于[使用Web组件加载页面](../harmonyos-guides/web-page-loading-with-web-components.md)的方法。
* Web组件可以通过[onFullScreenEnter](../harmonyos-references/arkts-basic-components-web-events.md#onfullscreenenter9)和[onFullScreenExit](../harmonyos-references/arkts-basic-components-web-events.md#onfullscreenexit9)回调来监听是否点击全屏的按键，其中onFullScreenEnter代表Web组件进入全屏模式，onFullScreenExit代表Web组件退出全屏模式，在这两个监听事件中，可以针对具体的业务场景，修改某些**全局变量**（例如组件的显隐状态、组件的[margin](../harmonyos-references/ts-universal-attributes-size.md#margin)属性等），达到全屏和非全屏显示不同的页面效果。可以在官方文档[ArkWeb(方舟Web)](../harmonyos-guides/arkweb.md)中查看更多关于Web组件的详细说明和使用方法。
* 开发者可以通过显隐控制的方式来实现组件在显示和隐藏间的切换，显隐控制[visibility](../harmonyos-references/ts-universal-attributes-visibility.md#visibility)是ArkUI应用开发框架提供的组件通用属性之一，开发者可以通过设定组件属性visibility不同的属性值，进而控制组件的显隐状态。visibility属性值及其描述如下：

| **名称** | **描述** |
| --- | --- |
| Visible | 组件状态为可见。 |
| Hidden | 组件状态为不可见，但参与布局、进行占位。 |
| None | 组件状态为不可见，不参与布局、不进行占位。 |

## 问题定位

当使用Web组件时，在点击全屏触发onFullScreenEnter回调的时候，视频区域会被Web之外的组件占用，导致页面布局异常。

1. 对于Stack布局，可以考虑使用修改Web组件的margin属性的方式来规避。
2. 对于Column布局，Web只是Column中的一部分，就需要每个组件的高度都设置成全局变量，切换全屏模式时，对各个组件的height都要进行变换，比较麻烦，此时采用Visibility.Visible和Visibility.None来控制组件的显隐状态更为简便。

## 分析结论

当Web组件与其他组件在一个容器的场景下，点击Web组件中调用的H5视频中的全屏会发生布局错乱的情况，此时可以通过修改一些布局属性，让视频充满全屏幕，达到全屏效果，或者根据实际业务场景对Web之外的组件进行显隐操作。

## 修改建议

1. 通过Stack布局，当视频进入全屏时，修改Web组件的margin属性为0，退出全屏时，恢复margin属性初始值。

   ```screen
   import { webview } from '@kit.ArkWeb';

   @Entry
   @Component
   struct SolutionOne {
     controller: webview.WebviewController = new webview.WebviewController();
     CONSTANT_HEIGHT = 150; // Web组件的高度默认值设置为150
     @State marginTop: number = this.CONSTANT_HEIGHT; // 自定义组件的margin高度属性为全局变量

     build() {
       Stack({ alignContent: Alignment.TopStart }) {
         Text('TextTextTextText')
           .width('100%')
           .height(this.CONSTANT_HEIGHT)
           .backgroundColor('#e1dede');
         Web({
           // 需替换为带有视频的网址才可达到预期效果
           src: 'www.example.com',
           controller: this.controller
         })
           .onFullScreenEnter(() => {
             console.info('onFullScreenEnter');
             // 当全屏的时候，web组件的margin属性高度设置为0
             this.marginTop = 0;
           })
           .onFullScreenExit(() => {
             console.info('onFullScreenExit');
             // 当退出全屏的时候，web组件的margin属性高度恢复初始值
             this.marginTop = this.CONSTANT_HEIGHT;
           })
           .width('100%')
           .height('100%')
           .zIndex(10)
             // Web组件margin属性高度呈动态变化
           .margin({ top: this.marginTop })
           .fileAccess(false)
           .geolocationAccess(false)
           .zoomAccess(true);
       }
       .width('100%')
       .height('100%');
     }
   }
   ```
2. 在Column布局下，可以采取Visibility.Visible和Visibility.None来控制组件的显隐状态。

   ```screen
   import { webview } from '@kit.ArkWeb';

   @Entry
   @Component
   struct SolutionTwo {
     controller: webview.WebviewController = new webview.WebviewController();
     CONSTANT_HEIGHT = 100;
     @State isVisible: boolean = true; // 自定义标志位isVisible，来控制是否需要显示组件

     build() {
       Column() {
         Text('TextTextTextText')
           .width('100%')
           .height(this.CONSTANT_HEIGHT)
           .backgroundColor('#e1dede') // 当isVisible标志位为true的时候，组件状态为可见，否则组件状态为不可见，不参与布局、不进行占位
           .visibility(this.isVisible ? Visibility.Visible :
           Visibility.None);
         Web({
           // 需替换为带有视频的网址才可达到预期效果
           src: 'www.example.com',
           controller: this.controller
         })
           .onFullScreenEnter(() => {
             console.info('onFullScreenEnter');
             // 当全屏的时候，isVisible标志位为false，组件状态为不可见，不参与布局、不进行占位
             this.isVisible = false;
           })
           .onFullScreenExit(() => {
             console.info('onFullScreenExit');
             // 当退出全屏的时候，isVisible标志位为true，组件状态为可见
             this.isVisible = true;
           })
           .width('100%')
           .height('100%')
           .zIndex(10)
           .fileAccess(false)
           .geolocationAccess(false)
           .zoomAccess(true);
       }
       .width('100%')
       .height('100%');
     }
   }
   ```

   通过以上方法实现后，运行程序，可以看到点击全屏，视频正常显示，无布局错乱情况。
