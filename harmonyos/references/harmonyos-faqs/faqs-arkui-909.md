---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-909
title: 如何解决XComponent无法触发触摸事件问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何解决XComponent无法触发触摸事件问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:18+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c3316db80fcab018831cd1e50f178e3b449d5271948358404925ab2183a4cd9a
---

## 问题现象

在XComponent组件中绑定onTouch方法，但发现该方法中的日志未被输出，表明onTouch事件未能正常触发。

问题参考如下：

```ts
Column() {
  XComponent({
    id: 'xcomponentId-00',
    type: "12314",
    libraryname: 'nativerender'
  })
    .onTouch((event: TouchEvent) => {
      console.info(`onTouch ${event.type}`)
    })
}
.height(CommonConstants.XCOMPONENT_HEIGHT)
.width('100%')
```

## 背景知识

[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)接口提供用于图形绘制和媒体数据写入的Surface，XComponent负责将其嵌入到视图中，支持应用自定义Surface位置和大小。当XComponentType参数为SURFACE或TEXTURE时，支持[onTouch](../harmonyos-references/ts-universal-events-touch.md#ontouch)等通用事件。

## 解决方案

1. 当问题代码中使用[XComponent(value: {id: string, type: XComponentType, libraryname?: string, controller?: XComponentController})](../harmonyos-references/ts-basic-components-xcomponent.md#xcomponent10)接口时，若配置了libraryname参数，点击事件、触摸事件、按键事件等通用事件将仅响应C-API侧的事件接口，因此问题代码中的onTouch事件无法被触发。
2. 为使onTouch事件正常响应，建议改用不含libraryname参数的[XComponent(options: XComponentOptions)](../harmonyos-references/ts-basic-components-xcomponent.md#xcomponent12)接口进行配置。

   ```ts
   @Entry
   @Component
   struct TouchEventDemo {
     xComponentController: XComponentController = new XComponentController();
     private aiController: ImageAnalyzerController = new ImageAnalyzerController();
     private options: ImageAIOptions = {
       types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT],
       aiController: this.aiController
     };

     build() {
       RelativeContainer() {
         Column() {
           XComponent({
             type: XComponentType.SURFACE,
             controller: this.xComponentController,
             imageAIOptions: this.options
           })
             .onTouch((event: TouchEvent) => {
               console.info(`onTouch ${event.type}`);
             })
         }
         .height('100%')
         .width('100%')
       }
     }
   }
   ```
