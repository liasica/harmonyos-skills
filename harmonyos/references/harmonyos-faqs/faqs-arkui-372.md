---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-372
title: 如何设置customspan不同位置的点击事件
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何设置customspan不同位置的点击事件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:7807b6bddeceee2537cd449662b41dcc6c60acb67f1cb78c064cf7a66de4eb41
---

CustomSpan 是最小单位的组件。若需实现特定功能，建议在多个 CustomSpan 上分别进行。如果必须在同一 CustomSpan 上实现，可从点击事件回调的 ClickEvent 中，根据属性判断实际点击位置，从而做出差异化响应。示例代码如下：

```typescript
@Entry
@Component
struct Index {
  controller: RichEditorController = new RichEditorController();
  option: RichEditorOptions = { controller: this.controller };

  @Builder
  comment() {
    Row() {
      Text() {
        Span('123123123')
        ImageSpan($r('app.media.startIcon')).width(20).height(20)
        Span('ggggggggggggggggggggggxxxxxxxxxxxxxxxxxxxxxxx')
      }
      .maxLines(1)
      .wordBreak(WordBreak.BREAK_ALL)
      .textOverflow({ overflow: TextOverflow.Ellipsis })
      .constraintSize({
        maxWidth: '90%'
      })

      Image($r('app.media.startIcon'))
        .width(25)
        .height(25)
        .onClick(() => {
          this.getUIContext().getPromptAction().showToast({
            message: 'Click to delete'
          })
        })
    }
    .width('100%')
    .align(Alignment.Center)
    .padding({
      top: 5,
      bottom: 5
    })
    .borderRadius(20)
    .backgroundColor(Color.Gray)
  }

  build() {
    Column() {
      Column() {
        RichEditor(this.option)
          .onReady(() => {
            this.controller.addBuilderSpan(() => this.comment())
          })
          .borderWidth(1)
          .borderColor(Color.Green)
          .width('100%')
          .height('30%')
      }
      .borderWidth(1)
      .borderColor(Color.Red)
      .width('100%')
      .height('70%')
    }
  }
}
```
