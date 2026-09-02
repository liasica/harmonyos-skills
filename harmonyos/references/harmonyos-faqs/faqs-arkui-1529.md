---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1529
title: TextArea设置计数器显示效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > TextArea设置计数器显示效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:11+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:23626c0b5fcb5f4fbb593ee415183963f0976b18ae4e39d69a796769ad51d363
---

## 问题现象

使用TextArea组件显示计数器时，如何实现可以设置计数器的字体颜色、字体大小和显示位置，并且计数器输入字符数达到上限时，边框不变红也不晃动且字符计数器常显效果？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/cJfDWEwHQT6Gehr0jv5Sgg/zh-cn_image_0000002628606988.png "点击放大")

## 背景知识

* [TextArea](../harmonyos-references/ts-basic-components-textarea.md)：多行文本输入框组件，当输入的文本内容超过组件宽度时会自动换行显示。高度未设置时，组件无默认高度，自适应内容高度。宽度未设置时，默认撑满最大宽度。
* [overlay](../harmonyos-references/ts-universal-attributes-overlay.md#overlay)：在当前组件上，增加遮罩文本或者叠加自定义组件以及ComponentContent作为该组件的浮层。浮层不通过组件树进行渲染，部分接口（例如[getRectangleById](../harmonyos-references/arkts-apis-uicontext-componentutils.md#getrectanglebyid)）不支持获取浮层中的组件。
* [Stack](../harmonyos-references/ts-container-stack.md)：堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。

## 解决方案

* 方案一：通过给组件设置浮层显示字符计数器来实现。

  示例代码如下：

  ```ts
  @Entry
  @Component
  struct TextAreaDemo {
    @State inputValue: string = '';
    @State textAreaNum: number = 0;
    maxLength: number = 20;

    // 定义字符计数器的字体颜色，当输入字符数大于或者等于最大字符数时，字体颜色为红色
    @Builder
    OverlayNode() {
      Text(`${this.textAreaNum}/${this.maxLength}`)
        .fontSize(12).fontColor(this.textAreaNum === this.maxLength ? Color.Red : Color.Gray)
    }

    build() {
      Column() {
        TextArea({
          placeholder: '请输入',
          text: this.inputValue
        })
          .height(220)
          .borderRadius(16)
          .padding(12)
          .margin({ top: 50 })
          .textAlign(TextAlign.Start)
          .align(Alignment.TopStart)
          .maxLength(this.maxLength)
          .fontSize(14)
          .lineHeight(18)
          .onChange((value: string) => {
            this.inputValue = value;
            this.textAreaNum = value.length;
          })
          // 给组件设置浮层显示字符计数器
          .overlay(this.OverlayNode(), {
            align: Alignment.BottomEnd,
            offset: { x: -10, y: -15 }
          })
      }
      .padding({ left: 16, right: 16 })
    }
  }
  ```
* 方案二：使用Stack层叠布局，使Text覆盖在TextArea右下角，实现字符计数显示。

  示例代码如下：

  ```ts
  @Entry
  @Component
  struct TextAreaExample {
    @State textAreaNum: number = 0;
    maxLength: number = 20;
    @State text: string = '';
    controller: TextAreaController = new TextAreaController();

    build() {
      Column() {
        // 使用Stack使Text覆盖在TextArea上
        Stack({ alignContent: Alignment.BottomEnd }) {
          TextArea({
            text: this.text,
            placeholder: '请输入',
            controller: this.controller
          })
            .height(220)
            .fontSize(16)
            .fontColor('#ff100f0f')
            .backgroundColor('#FFFFFF')
            .maxLength(this.maxLength)
            .onChange((value: string) => {
              this.text = value;
              this.textAreaNum = value.length;
            })
            .backgroundColor('#F1F3F5')

          // 自定义右下角的Text组件
          Text(`${this.textAreaNum}/${this.maxLength}`)
            .fontSize(12)
            .fontColor(this.textAreaNum === this.maxLength ? Color.Red :
              Color.Gray)
            .margin({ right: 20, bottom: 10 })
        }
        .width('100%')
        .height('auto')
      }
      .width('100%')
      .height('100%')
      .padding({ top: 50, right: 20, left: 20 })
    }
  }
  ```

## 常见FAQ

Q：如何实现字符计数器常显？

A：将[showCounter](../harmonyos-references/ts-basic-components-textarea.md#showcounter10)属性的thresholdPercentage参数值设置为undefined，可实现字符计数器常显效果。
