---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1180
title: 弹窗一直显示在最上层，无法关闭
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 弹窗一直显示在最上层，无法关闭
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:26+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8ab0940d5b3663bdb8341ddac755338a8495e0c5fa7d22db24f8e857e8e74f0b
---

## 问题现象

弹窗始终显示在最上层，无法关闭，遮挡页面其他内容。

## 背景知识

* [自定义弹窗CustomDialog](../harmonyos-references/ts-methods-custom-dialog-box.md)使用弹窗组件时，优先考虑自定义弹窗，便于弹窗样式与内容的自定义。
* [CustomDialogControllerOptions对象说明](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)中的autoCancel：是否允许点击遮障层退出。true表示关闭弹窗，false表示不关闭弹窗。
* [DismissDialogAction](../harmonyos-references/ts-methods-custom-dialog-box.md#dismissdialogaction12)：Dialog关闭回调函数。开发者需要退出时调用，不需要退出时无需调用。

## 问题定位

1. 排查弹窗组件上是否配置了autoCancel的值为true。

   ```ts
   dialogController: CustomDialogController | null = new CustomDialogController({
     builder: CustomDialogExample({
     // ...
     }),
     cancel: this.exitApp,
     // 不允许点击遮障层退出
     autoCancel: false,
     // ...
   })
   ```
2. 如果autoCancel的值为true，继续排查DismissDialogAction调用的场景是否正确。

## 分析结论

1. autoCancel的值设置为false，导致弹窗始终显示在最上层，无法关闭。
2. DismissDialogAction调用的场景不正确，在需要关闭弹窗时未调用，导致弹窗始终显示在最上层，无法关闭。

## 修改建议

1. 将autoCancel的值设置为true。
2. 在需要关闭弹窗的场景调用DismissDialogAction。具体示例请参考：[弹出嵌套弹窗](../harmonyos-references/ts-methods-custom-dialog-box.md#示例1弹出嵌套弹窗)。
