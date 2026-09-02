---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-computer-7
title: PC应用如何隐藏导航栏右上角三键
breadcrumb: FAQ > 多设备场景 > 电脑 > 常见问题 > PC应用如何隐藏导航栏右上角三键
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:d8a0d0dc41459614e90c432dcc358a1e81ed7c190d55dce9148dbddc5eae0d4c
---

## 问题现象

PC应用非全屏状态下或者自由多窗模式下如何不显示右上角三键？

## 背景知识

[Window](../harmonyos-references/arkts-apis-window-window.md)提供管理窗口的一些基础能力，包括对当前窗口的创建、销毁、各属性设置，以及对各窗口间的管理调度。

## 解决方案

1. 配置定时任务间隔，通过[onMouse](../harmonyos-references/ts-universal-mouse-key.md#onmouse)事件判断鼠标在应用中是否保持静止。
2. 若鼠标静止，获取应用窗口实例，使用[setWindowDecorVisible](../harmonyos-references/arkts-apis-window-window.md#setwindowdecorvisible11)主动隐藏状态栏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/q8YT7SveSUePqrsocquaVA/zh-cn_image_0000002680372243.png "点击放大")
3. 如上图窗口右上角三键此时未隐藏，使用[setWindowTitleButtonVisible](../harmonyos-references/arkts-apis-window-window.md#setwindowtitlebuttonvisible14)主动隐藏三键，以获取沉浸式体验。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/M1OAl2AVSsCleGqfH7d6_Q/zh-cn_image_0000002680212499.png "点击放大")

   ```ts
   import { common } from '@kit.AbilityKit';
   import { window } from '@kit.ArkUI';
   import { BusinessError } from '@kit.BasicServicesKit';

   @Entry
   @Component
   struct Index {
     @State message: string = 'Hello World';
     preX: number = 0;
     preY: number = 0;
     curX: number = 0;
     curY: number = 0;
     context: Context | undefined = this.getUIContext().getHostContext();

     onPageShow(): void {
       // 设置定时任务检测一定时间内鼠标是否移动
       setInterval(() => {
         if (this.curX == this.preX && this.curY == this.preY) {
           // 设置导航栏不可见
           changeRight(this.context, false, false, false);
         } else {
           this.preX = this.curX;
           this.preY = this.curY;
         }
       }, 1000);
     }

     build() {
       RelativeContainer() {
         Text(this.message)
           .id('HelloWorld')
           .fontSize($r('app.float.page_text_font_size'))
           .fontWeight(FontWeight.Bold)
           .alignRules({
             center: { anchor: '__container__', align: VerticalAlign.Center },
             middle: { anchor: '__container__', align: HorizontalAlign.Center }
           })
           .onClick(() => {
             this.message = 'Welcome';
           })
       }
       .onMouse((event?: MouseEvent) => {
         // 设置页面的onMouse回调记录鼠标位置
         if (event) {
           this.curX = event.windowX;
           this.curY = event.windowY;
           // 设置导航栏可见
           changeRight(this.context, true, true, true);
         }
       })
       .height('100%')
       .width('100%')
     }
   }

   function changeRight(context: Context | undefined, max: boolean, min: boolean, isClose: boolean) {
     if (!context) {
       return;
     }
     let uiContext = context as common.UIAbilityContext;
     let mainWindow: window.Window | undefined = undefined;
     uiContext.windowStage.getMainWindow().then(
       data => {
         mainWindow = data;
         // setWindowDecorVisible用于隐藏图标、名称与状态栏
         mainWindow.setWindowDecorVisible(max);
         // setWindowTitleButtonVisible接口，隐藏主窗标题栏最大化、最小化、关闭按钮。
         mainWindow.setWindowTitleButtonVisible(max, min, isClose);
       }
     ).catch((err: BusinessError) => {
       if (err.code) {
         console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
       }
     });
   }
   ```

## 常见FAQ

Q：setWindowSystemBarEnable等部分接口使用中发现在2in1模拟器中不生效是为什么？

A：Window部分接口虽然显示支持PC/2in1设备，文档中也有标识说明，接口在部分机型下不生效，在使用Window或者其他接口时需要注意接口适配性，避免影响开发效率。

Q：深色模式下PC应用窗口右上角的三键颜色不够清晰，如何处理？

A：将设备系统版本升级至最新Release版本。系统在新版本中已优化深色模式下右上角三键的显示颜色，升级后三键将显示为白色，提升视觉清晰度。
