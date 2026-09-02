---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-915
title: 如何设置半模态转场弹窗与设备屏幕底部的边距
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何设置半模态转场弹窗与设备屏幕底部的边距
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:19+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:dcd49f8cd72f1a37953892a88ff08a3f88c806e6af21c700b3c97ce68d442cc5
---

## 问题现象

如何实现半模态转场弹窗与设备屏幕底部设置边距。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/fXF0ej1WTs-GU6QtA1vQjQ/zh-cn_image_0000002628559678.png "点击放大")

## 背景知识

* [半模态转场](../harmonyos-references/ts-universal-attributes-sheet-transition.md)：通过[bindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)属性为组件绑定半模态页面，在组件插入时可通过设置自定义或默认的内置高度确定半模态大小。
* [自定义弹窗](../harmonyos-references/ts-methods-custom-dialog-box.md)：通过CustomDialogController类显示自定义弹窗。使用弹窗组件时，优先考虑自定义弹窗，便于弹窗样式与内容的自定义。

## 解决方案

目前半模态转场弹窗设计的交互特性就是从屏幕底部滑入，因此无法实现设置与屏幕底部的边距。设置弹窗与设备屏幕底部的边距，可以通过自定义弹窗(CustomDialog)实现。通过给自定义弹窗最外层容器设置margin属性，达到实现设置与屏幕底部边距的目的。示例代码如下：

```ts
@CustomDialog
@Component
struct CustomDialogExp {
  controller?: CustomDialogController;
  cancel: () => void = () => {
  };
  confirm: () => void = () => {
  };

  build() {
    Column() {
      // 在这里实现弹窗页面
      Blank();
      Button('关闭')
        .onClick(() => {
          this.controller?.close();
        });
    }
    .margin({ bottom: 100 })
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM]) // 设置底部绘制延伸到导航区域
    .borderRadius({ topLeft: 25, topRight: 25 }) // 设置左上右上边框圆角半径
    .width('100%')
    .height(500)
    .backgroundColor(Color.Gray)
    .transition(TransitionEffect.OPACITY.animation({ duration: 1000 })
      .combine(TransitionEffect.translate({ y: 1000 }))); // 组件转场动画
  }
}

@Entry
@Component
struct CustomDialogPage {
  dialogController: CustomDialogController | null = new CustomDialogController({
    builder: CustomDialogExp({
      cancel: () => {
        this.onCancel();
      },
      confirm: () => {
        this.onAccept();
      },
    }),
    autoCancel: false, // 不允许点击遮障层退出
    customStyle: true, // 自定义弹窗容器样式
    alignment: DialogAlignment.Bottom, // 垂直底部对齐
  });

  // 在自定义组件即将析构销毁时将dialogController置空
  aboutToDisappear() {
    // 将dialogController置空
    this.dialogController = null;
  }

  onCancel() {
    console.info('Callback when the first button is clicked');
  }

  onAccept() {
    console.info('Callback when the second button is clicked');
  }

  exitApp() {
    console.info('Click the callback in the blank area');
  }

  build() {
    Column() {
      Button('打开')
        .onClick(() => {
          if (this.dialogController != null) {
            this.dialogController.open();
          }
        }).backgroundColor(0x317aff);
    }.width('100%').margin({ top: 5 });
  }
}
```

## 总结

目前半模态转场弹窗无法实现设置与设备屏幕底部的边距，开发者在使用弹窗组件时，优先考虑自定义弹窗，便于弹窗样式与内容的自定义。
