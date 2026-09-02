---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1292
title: 如何扩展安全区域实现全屏遮罩
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何扩展安全区域实现全屏遮罩
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:21+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:44dbeb9e8b9ca3507ecccced4bbe199e6d74fe9d8d627d3a21d1b929c1a20489
---

## 问题现象

如何结合安全区域扩展与全屏遮罩组件实现沉浸式界面？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/m_rCp3UgT02DmSq4To2nKg/zh-cn_image_0000002658837243.gif "点击放大")

## 背景知识

* 安全区域是指页面的显示区域，默认情况下开发者开发的界面都布局在安全区域内，不与系统设置的避让区比如状态栏、导航栏区域重叠。通过[expandSafeArea](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#expandsafearea)属性支持组件不改变布局情况下扩展其绘制区域至安全区外。
* [CustomDialogController](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontroller)是HarmonyOS提供的弹窗控制器，用于动态管理自定义弹窗的显示、样式和交互逻辑。

## 解决方案

调用expandSafeArea将页面内容扩展至系统安全区域外部，同时，CustomDialogController会自动为弹窗添加半透明遮罩层，用于阻断用户与底层内容的交互，通过CustomDialogController弹出对话框，实现遮罩效果。

```ts
@CustomDialog
struct CustomDialogExample {
  controller?: CustomDialogController;

  build() {
    Column() {
      Text('遮罩层')
        .fontColor(Color.White)
        .fontSize(30);
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .borderRadius(10)
    .onClick(() => {
      this.controller?.close();
    });
  }
}

@Entry
@Component
struct CustomDialogMask {
  dialogController: CustomDialogController = new CustomDialogController({
    builder: CustomDialogExample(),
    customStyle: true
  });

  build() {
    Column() {
      Button('click me')
        .onClick(() => {
          this.dialogController.open();
        });
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#ffe2eeff')
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
  }
}
```
