---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-750
title: RichEditor实现上下角标数字的效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > RichEditor实现上下角标数字的效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:20+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:31bbda80028dd91ed8c99f994ad5131a351147849fce7eb2a3b9f7764dfd208d
---

## 问题现象

如何在RichEditor组件中实现上下角标的输入？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/SMJAbSFxQ86Arkz78rHitg/zh-cn_image_0000002658794735.png "点击放大")

## 背景知识

* [RichEditor](../harmonyos-guides/arkts-common-components-richeditor.md)是支持图文混排和文本交互式编辑的组件，通常用于响应用户对图文混合内容的输入操作，例如可以输入图文的评论区。
* [RichEditorController](../harmonyos-references/ts-basic-components-richeditor.md#richeditorcontroller)是RichEditor组件的控制器，该控制器的[addTextSpan](../harmonyos-references/ts-basic-components-richeditor.md#addtextspan)方法可用于添加文本内容并设置文本样式属性。
* [fontFeature](../harmonyos-references/ts-basic-components-text.md#fontfeature12)属性可用于设置文字特性效果，其中sups表示上标、subs表示下标。
* [onReady](../harmonyos-references/ts-basic-components-richeditor.md#onready)方法是富文本组件提供的一个回调函数，在组件初始化完成后会触发该回调。

## 解决方案

1. 创建RichEditor组件与RichEditorController控制器，在该组件的onReady回调方法中，调用控制器的addTextSpan方法，在该方法的第一个参数中输入文本值，在第二个参数设置style中fontFeature属性为subs，用于实现数字的下角标效果。
2. 设置上角标同理，只需在第二个参数中设置fontFeature属性为sups即可。

完整示例参考如下：

```ts
@Entry
@Component
struct RichEditorExample {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };

  build() {
    Row() {
      Column() {
        RichEditor(this.options)
          .onReady(() => { // 组件初始化完成后会触发onReady回调
            // 在addTextSpan第一个参数中输入文本值，在第二个参数添加style，style中fontFeature属性为subs
            this.controller.addTextSpan('下角标效果示例：二氧化碳，CO2\n',
              {
                style:
                {
                  fontSize: 20,
                  fontFeature: '\"subs\"'
                }
              });
            this.controller.addTextSpan('上角标效果示例：X的平方，X2\n',
              {
                style:
                {
                  fontSize: 20,
                  fontFeature: '\"sups\"'
                }
              });
          })
          .borderWidth(1)
          .padding(5)
          .width('100%')
      }
      .width('100%')
    }
  }
}
```
