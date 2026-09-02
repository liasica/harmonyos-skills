---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1339
title: RichEditor组件如何阻止语音输入时触发aboutToDelete回调
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > RichEditor组件如何阻止语音输入时触发aboutToDelete回调
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:08+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8cd4663561058e4c1e8db90a154eeaa2d2b36dd1e2adb759e9dd5d5b8861940b
---

## 问题现象

使用RichEditor富文本输入组件时，使用软键盘的语音输入功能，会触发aboutToDelete回调（用软键盘输入文字则不会回调aboutToDelete），如何阻止aboutToDelete回调？

## 背景知识

[RichEditor](../harmonyos-guides/arkts-common-components-richeditor.md)是支持图文混排和文本交互式编辑的组件，通常用于响应用户对图文混合内容的输入操作，例如可以输入图文的评论区。具体用法参考：[RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)。

常用事件如下：

* [aboutToDelete](../harmonyos-references/ts-basic-components-richeditor.md#abouttodelete)在输入法删除内容前，触发回调。
* [onDeleteComplete](../harmonyos-references/ts-basic-components-richeditor.md#ondeletecomplete)在输入法删除内容后，触发回调。
* [getCaretOffset](../harmonyos-references/ts-basic-components-richeditor.md#getcaretoffset10)代表返回当前光标所在位置。

## 解决方案

语音输入功能的实现机制为'先选中文本再替换'，因此系统必然会触发aboutToDelete回调。虽然无法阻止系统调用该回调，但可通过判断回调来源区分语音输入与手动删除操作，从而避免误拦截或错误处理。具体解决方案如下：

1. 由于在语音输入过程中，光标位置不变，因此当前光标位置可以作为区分语音输入和手动Delete的判断条件。
2. 修改事件处理逻辑：当为语音输入时，不执行自定义内容。

```ts
@Entry
@Component
struct DisableRichEditor {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };
  @State careOff: number = 0;

  build() {
    Column({ space: 20 }) {
      Text('数字变化代表触发aboutToDelete之后执行了自定义内容')
        .fontColor(Color.Black)
        .width(300)
      Text(this.careOff.toString())
        .fontColor(Color.Black)

      RichEditor(this.options)
        .border({
          width: 1,
          radius: 20,
          color: Color.Pink
        })
        .backgroundColor(Color.Yellow)
        .margin({ left: 10, right: 10 })
        .aboutToDelete((value: RichEditorDeleteValue) => {
          // 在语音输入过程中，光标位置不变，所以可以以此作为判断条件，证明当前正在进行语音输入。
          if (this.controller.getCaretOffset() === value.offset) {
            return false;
          }
          this.careOff++;
          return true;
        })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```
