---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-974
title: RichEditor组件实现图片插入后换行并横向居中效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > RichEditor组件实现图片插入后换行并横向居中效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:05+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c5058621a9bd46f207e57018b497738b9ed1639b0da07c32437183f000e876ff
---

## 问题现象

RichEditor组件如何实现文本中插入图片后，图片换行并横向居中的场景。

## 背景知识

[RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)是支持图文混排和文本交互式编辑的组件，适用于需要复杂文本输入的场景（如评论区、富文本编辑器）。

## 解决方案

* **方案一**：文本中插入图片后，图片换行并横向居中的场景，可以使用[addBuilderSpan](../harmonyos-references/ts-basic-components-richeditor.md#addbuilderspan11)在RichEditor中添加用户自定义布局（BuilderSpan），自定义布局中设置图片横向居中，并用Text组件设置换行。

  ```ts
  @Entry
  @Component
  struct BuilderSpanExample {
    controller: RichEditorController = new RichEditorController();
    option: RichEditorOptions = { controller: this.controller };
    private customBuilder: CustomBuilder = undefined;

    @Builder
    imageTextBuilder() {
      Row({ space: 2 }) {
        // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
        Image($r('app.media.startIcon')).width(24).height(24).margin({ left: -5 });
        Text('\n').fontSize(10);
      }
      .width('100%')
      .height(50)
      .padding(5)
      .alignItems(VerticalAlign.Center)
      .justifyContent(FlexAlign.Center)
    }

    build() {
      Column() {
        Button('addImageTextBuilder')
          .onClick(() => {
            let insertOffset = this.controller.getCaretOffset();
            this.customBuilder = () => {
              this.imageTextBuilder();
            };
            this.controller.addBuilderSpan(this.customBuilder, { offset: insertOffset });
          })
        Column() {
          RichEditor(this.option)
            .onReady(() => {
              this.controller.addTextSpan('0123456789',
                {
                  style:
                  {
                    fontColor: Color.Orange,
                    fontSize: 30
                  }
                });
            })
        }
        .margin({ top: 60 })
        .borderWidth(1)
        .borderColor(Color.Red)
        .width('100%')
        .height('70%')
      }
    }
  }
  ```
* **方案二**：文本中插入图片后，图片不换行并横向居中的场景，可以使用addBuilderSpan在RichEditor中添加用户自定义布局（BuilderSpan），自定义布局中设置图片横向居中，并用Text组件设置换行。

  ```ts
  @Entry
  @Component
  struct Index {
    controller: RichEditorController = new RichEditorController();
    option: RichEditorOptions = { controller: this.controller };
    private customBuilder: CustomBuilder = undefined;
    uiContext: UIContext = this.getUIContext();
    @State imageTextHeight: number = 50;

    @Builder
    imageTextBuilder() {
      Row({ space: 2 }) {
        // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
        Image($r('app.media.startIcon')).width(70).height(70).margin({ left: -5 });
      }
      .height(this.imageTextHeight)
      .padding(5)
      .alignItems(VerticalAlign.Center)
    }

    build() {
      Column() {
        Button('addImageTextBuilder')
          .onClick(() => {
            let insertOffset = this.controller.getCaretOffset();
            this.imageTextHeight = 70;
            this.customBuilder = () => {
              this.imageTextBuilder();
            };
            this.controller.addBuilderSpan(this.customBuilder, { offset: insertOffset });
            this.controller.updateSpanStyle({
              start: insertOffset - 1,
              end: insertOffset,
              textStyle: { lineHeight: this.imageTextHeight, halfLeading: true }
            });
          });

        Button('addText')
          .onClick(() => {
            let insertOffset = this.controller.getCaretOffset();
            this.controller.addTextSpan('一个测试',
              {
                offset: insertOffset,
                style:
                {
                  fontColor: Color.Orange,
                  fontSize: 30
                }
              });
          })
          .margin({ top: 10 })
        Column() {
          RichEditor(this.option)
            .onReady(() => {
              this.controller.addTextSpan('一个测试',
                {
                  style:
                  {
                    fontColor: Color.Orange,
                    fontSize: 30
                  }
                });
            })
        }
        .margin({ top: 60 })
        .width('100%')
        .height('70%');
      }
      .margin({ top: 50 })
    }
  }
  ```
