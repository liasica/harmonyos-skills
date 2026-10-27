---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1340
title: 在TextArea中复制完文字后如何取消文字的选中状态
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 在TextArea中复制完文字后如何取消文字的选中状态
category: harmonyos-faqs
scraped_at: 2026-10-28T07:47:21+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:869dd42605a2783cb10777317c2823cf26b2b2431ddf6d4f4478c05b9696ee2b
---

## 问题现象

TextArea组件输入若干内容，长按选择文字并点击“复制”后所选文字仍然是选中状态，如何取消其选中状态？

问题代码示例参考如下：

```screen
@Entry
@Component
struct Index {
  @State message: string = '123456';
  controller: TextAreaController = new TextAreaController();
  startIndex: number = -1;
  endIndex: number = -1;

  build() {
    Column() {
      TextArea({ controller: this.controller, text: this.message })
        .onTextSelectionChange((selectionStart: number, selectionEnd: number) => {
          this.startIndex = selectionStart;
          this.endIndex = selectionEnd;
        })
        .margin(40)
    }
    .height('100%')
    .width('100%')
  }
}
```

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/5NakZOSHQ3WVWpz1_vZj2g/zh-cn_image_0000002628761404.gif "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/ggnvyTKGRUiGkz4CAIi0jw/zh-cn_image_0000002658960733.gif "点击放大")

## 背景知识

* [onTextSelectionChange](../harmonyos-references/ts-basic-components-textarea.md#ontextselectionchange10)：文本选择的位置或编辑状态下光标位置发生变化时，触发该回调。
* [onCopy](../harmonyos-references/ts-basic-components-textarea.md#oncopy8)：进行复制操作时，触发该回调。
* [caretPosition](../harmonyos-references/ts-basic-components-textarea.md#caretposition8)：设置输入光标的位置。

## 问题定位

在使用系统提供的复制功能时，复制完成后并未对光标位置进行修改，故文本还是呈现选中状态。

## 分析结论

在TextArea的onCopy回调中修改光标位置，即可实现取消文字的选中状态。

## 修改建议

1. 选中文字时在[onTextSelectionChange](../harmonyos-references/ts-basic-components-textarea.md#ontextselectionchange10)回调里记录光标结束位置，
2. 点击“复制”时在[onCopy](../harmonyos-references/ts-basic-components-textarea.md#oncopy8)回调里使用[caretPosition](../harmonyos-references/ts-basic-components-textarea.md#caretposition8)将光标定位到所记录的结束位置。

```screen
@Entry
@Component
struct TextAreaSelectionChangeDemo {
  @State message: string = '123456';
  controller: TextAreaController = new TextAreaController();
  startIndex: number = -1;
  endIndex: number = -1;

  build() {
    Column() {
      TextArea({ controller: this.controller, text: this.message })
        .onTextSelectionChange((selectionStart: number, selectionEnd: number) => {
          // 记录光标起始和结束位置
          this.startIndex = selectionStart;
          this.endIndex = selectionEnd;
        })
        .onCopy(() => {
          // 完成复制后将光标定位到记录下来的结束位置
          this.controller.caretPosition(this.endIndex);
        })
        .margin(40)
    }
    .height('100%')
    .width('100%')
  }
}
```
