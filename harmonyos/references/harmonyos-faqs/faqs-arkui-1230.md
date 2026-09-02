---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1230
title: deleteSpans删除光标前一个内容
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > deleteSpans删除光标前一个内容
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:07+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:97ab83f36cefa4ea732889eed60b10eb5ffd7b5ff30a8b2e8c3186126387f2de
---

## 问题现象

使用deleteSpans方法，如何实现仅删除富文本光标前的一个内容？

## 背景知识

[RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)是支持图文混排和文本交互式编辑的组件，其包含getCaretOffset方法用于获取光标位置。

## 解决方案

通过[getCaretOffset](../harmonyos-references/ts-basic-components-richeditor.md#getcaretoffset10)方法获取光标位置，计算前一个内容的起始位置，并将其传入[deleteSpans](../harmonyos-references/ts-basic-components-richeditor.md#deletespans)方法。

```ts
@Entry
@Component
struct RichEditorDeleteDemo {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };

  build() {
    Column() {
      Column() {
        RichEditor(this.options)
          .onReady(() => {
            this.controller.addTextSpan('点击delete，一次只删除一个内容');
          });
      }.width('100%');

      Button('delete').onClick(() => {
        let offset = this.controller.getCaretOffset();
        this.controller.deleteSpans({ start: offset - 1, end: offset });
      });
    }.height('100%');
  }
}
```
