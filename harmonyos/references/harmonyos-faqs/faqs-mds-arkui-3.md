---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-mds-arkui-3
title: 控制折叠屏展开态和折叠态时弹窗的位置
breadcrumb: FAQ > 多设备场景 > UI框架 > 方舟UI框架（ArkUI） > 控制折叠屏展开态和折叠态时弹窗的位置
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:79c754124c9cfa7fe1b6f01e6cc29182db431e3e6b6ac93407486828007eaa68
---

## 问题现象

折叠屏展开态和折叠态的弹窗默认在屏幕中间，期望展开态弹窗在左侧页面，折叠态弹窗仍居中。

| 默认展开态弹窗 | 期望展开态弹窗 |
| --- | --- |
|  |  |

## 背景知识

折叠屏相对于普通手机有一个明显的特点：可随时折叠展开、折叠展开会导致屏幕属性改变。HarmonyOS提供了[display.on('foldStatusChange')](../harmonyos-references/js-apis-display.md#displayonfoldstatuschange10)接口开启折叠设备折叠状态变化的监听，具体来说，包括折叠态、展开态、悬停态等。为了适配不同的折叠状态，可以通过设置弹窗[offset](../harmonyos-references/ts-types.md#offset)位置坐标偏移量在不同位置进行弹窗。

## 解决方案

进入页面后，先调用display.isFoldable判断设备是否可折叠、display.getFoldStatus获取当前折叠状态，再设置弹窗offset实现在不同位置进行弹窗，并添加display.on('foldStatusChange')监听折叠状态变化，实时修改弹窗位置。

```ts
import { display } from '@kit.ArkUI';

@CustomDialog
struct CustomDialogExample {
  controller?: CustomDialogController;
  cancel: () => void = () => {
  };
  confirm: () => void = () => {
  };

  build() {
    Column() {
      Text('Change text')
        .fontSize(20).margin({ top: 10, bottom: 10 });
      Text('Whether to change a text?')
        .fontSize(17).margin({ top: 10, bottom: 10 });
      Flex({ justifyContent: FlexAlign.SpaceAround }) {
        Button('cancel')
          .onClick(() => {
            this.controller?.close();
            if (this.cancel) {
              this.cancel();
            }
          }).backgroundColor(0xffffff).fontColor(Color.Black);
        Button('confirm')
          .onClick(() => {
            this.controller?.close();
            if (this.confirm) {
              this.confirm();
            }
          }).backgroundColor(0xffffff).fontColor(Color.Red);
      }.margin({ bottom: 10 });
    }
    .borderRadius(6)
    .width(300)
    .backgroundColor(Color.White);
  }
}

@Entry
@Component
struct Index {
  dialogController: CustomDialogController | null = null;

  aboutToAppear(): void {
    // 进入页面根据当前折叠状态重置弹窗位置
    this.resetDialog();
    if (display.isFoldable()) { // 判断是否是折叠设备
      let callback: Callback<display.FoldStatus> = () => {
        // 切换折叠状态重置弹窗位置
        this.resetDialog();
      };
      // 监听折叠状态变化
      display.on('foldStatusChange', callback);
    }
  }

  resetDialog() {
    // 重置弹窗位置
    let offsetDx = 0;
    if (display.isFoldable()) { // 判断是否是折叠设备
      let status: display.FoldStatus = display.getFoldStatus(); // 获取当前可折叠设备的折叠状态
      if (status === display.FoldStatus.FOLD_STATUS_EXPANDED) { // 判断是否是折叠态
        let displayClass = display.getDefaultDisplaySync();
        offsetDx = -this.getUIContext().px2vp(displayClass.width) / 4;
      }
    }
    this.dialogController = new CustomDialogController({
      builder: CustomDialogExample({}),
      onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
        if (dismissDialogAction.reason == DismissReason.PRESS_BACK) {
          dismissDialogAction.dismiss();
        }
        if (dismissDialogAction.reason == DismissReason.TOUCH_OUTSIDE) {
          dismissDialogAction.dismiss();
        }
      },
      offset: { dx: offsetDx, dy: 0 }, // 设置offset
      customStyle: true,
    });
  }

  build() {
    Row() {
      Button('打开弹窗')
        .onClick(() => {
          this.dialogController?.open();
        });
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%');
  }
}
```
