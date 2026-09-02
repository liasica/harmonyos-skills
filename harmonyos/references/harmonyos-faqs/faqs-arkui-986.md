---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-986
title: CustomContentDialog如何实现点击按钮不自动关闭弹窗
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > CustomContentDialog如何实现点击按钮不自动关闭弹窗
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:05+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a05cb64bd903f76395ce68865d200cf19c865be9ef099f173ba233a7e66ee15a
---

## 问题现象

参考官网示例[自定义内容弹出框](../harmonyos-references/ohos-arkui-advanced-dialog.md#示例8自定义内容弹出框)，使用CustomContentDialog做一个带两个button的弹窗，点击任何一个按钮都会关闭，如何做到点击按钮不自动关闭。

## 背景知识

[CustomContentDialog](../harmonyos-references/ohos-arkui-advanced-dialog.md#customcontentdialog12)自定义内容区弹出框，同时支持定义操作区按钮样式。

## 解决方案

CustomContentDialog自带的buttons属性在系统能力上设置了关闭弹窗的功能。可通过@Builder自定义button内容，实现不自动关闭弹窗。

```screen
import { CustomContentDialog } from '@kit.ArkUI';

@Entry
@Component
struct CustomerButtonDialog {
  dialogController: CustomDialogController = new CustomDialogController({
    builder: CustomContentDialog({
      primaryTitle: '标题',
      secondaryTitle: '辅助文本',
      contentBuilder: () => {
        this.buildContent();
      },
    }),
  });

  build() {
    Column() {
      Button("支持自定义内容弹出框")
        .onClick(() => {
          this.dialogController.open();
        });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }

  // 自定义弹出框的内容区
  @Builder
  buildContent(): void {
    Column() {
      Text('这里是弹窗内容');
      Button('点击不会关闭')
        .margin({ top: 10 });
    }
    .width('100%');
  }
}
```
