---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-992
title: 如何实现自定义动画的弹窗
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现自定义动画的弹窗
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:25+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6ae3ff4bd9fd81719b0a9acb7491cc92991a563d7e6b5e6377e53f97bc86b06e
---

## 问题现象

如何实现自定义动画的弹窗，在打开弹窗时，有弹出动画效果，关闭弹窗时，有关闭动画效果？

## 背景知识

* [组件内转场](../harmonyos-references/ts-transition-animation-component.md)主要通过transition属性配置转场参数，在组件插入和删除时显示过渡动效，主要用于容器组件中的子组件插入和删除时，提升用户体验。
* [visibility](../harmonyos-references/ts-universal-attributes-visibility.md#visibility)控制组件的显示或隐藏。当未设置visibility时，组件默认为显示。
* [CustomDialogController](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontroller)自定义弹窗的控制器，通过CustomDialogController类显示自定义弹窗。使用弹窗组件时，优先考虑自定义弹窗，便于弹窗样式与内容的自定义。

## 解决方案

实现自定义动画的弹窗，可以使用组件内转场[transition](../harmonyos-references/ts-transition-animation-component.md)自定义弹窗的动画效果，并配合visibility来控制弹窗的显示与隐藏状态变化，通过@Link监听状态变化实现双向绑定，进而根据状态变化调用自定义关闭弹窗的方法，从而达到有关闭动画的效果。示例代码如下：

```ts
@CustomDialog
struct CustomDialogExampleTest {
  controller: CustomDialogController;
  @Link showFlag: Visibility;
  private isAutoClose: boolean = false;
  private anmDuration: number = 1000; // 弹窗关闭时长
  textController: TextAreaController = new TextAreaController();

  build() {
    Column() {
      Column() {
        Text('这是自定义弹窗')
          .fontSize(30);
        Button('点我关闭弹窗')
          .onClick(() => {
            if (this.controller != undefined) {
              this.controller.close();
            }
          })
          .margin(20);
      }
      .padding(8)
      .backgroundColor('#FFFFFF')
      .margin({ bottom: 30 })
      .width('80%')
      .borderRadius(10);
    }
    .justifyContent(FlexAlign.End)
    .width('100%')
    .height('100%')
    .onClick(() => {
      console.info('dialogClick');
      if (this.isAutoClose) {
        console.info('dialogAutoClose');
        this.closeDialog();
      }
    })
    .visibility(this.showFlag)
    // 滑入滑出效果动画，根据需要自由设置动画属性参数
    .transition(TransitionEffect.move(TransitionEdge.START).animation({ duration: this.anmDuration }));
  }

  closeDialog() {
    this.showFlag = Visibility.Hidden;
    console.info('closeDialog');
    setTimeout(() => {
      this.controller.close();
    }, this.anmDuration);
  }
}

@Entry
@Component
struct CustomDialogUser {
  private isAutoClose: boolean = true;
  @State showFlag: Visibility = Visibility.Visible;
  private anmDuration: number = 1000;
  dialogController: CustomDialogController = new CustomDialogController({
    builder: CustomDialogExampleTest({ isAutoClose: this.isAutoClose, showFlag: this.showFlag }),
    autoCancel: this.isAutoClose,
    customStyle: true,
    onWillDismiss: () => {
      this.showFlag = Visibility.Hidden;
      console.info('onWillDismiss closeDialog');
      setTimeout(() => {
        this.dialogController.close();
      }, this.anmDuration);
    }
  });

  build() {
    Column() {
      Button('click me')
        .margin({ top: 50 })
        .onClick(() => {
          this.showFlag = Visibility.Visible;
          this.dialogController.open();
        });
    }.width('100%').height('100%');
  }
}
```

## 常见FAQ

Q：如何实现自定义动画的弹窗从底部向上弹出的效果。

A：可以参考[模态转场-转场动画](../harmonyos-guides/arkts-modal-transition.md)实现弹窗从底部向上弹出的这种动画效果。
