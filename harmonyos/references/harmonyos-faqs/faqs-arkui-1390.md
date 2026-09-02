---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1390
title: 侧滑无法关闭弹窗
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 侧滑无法关闭弹窗
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:09+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:523ac1fac426a977a07ebc5e088ea6038c1119dc2bcfe7689705b1586828ec12
---

## 问题现象

侧滑无响应，没有关闭弹窗。

## 背景知识

[onWillDismiss](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)：当用户执行点击遮障层关闭、左滑/右滑、三键back、键盘ESC关闭交互操作时，如果注册该回调函数，则不会立刻关闭弹窗。在回调函数中可以通过reason得到阻拦关闭弹窗的操作类型，从而根据原因选择是否能关闭弹窗。

## 问题定位

1. 日志过滤backPress，看到侧滑事件是被Overlay消费的，即叠加层，一般是一些弹窗组件。

   ```txt
   [(-1:100000:singleton)] [com.example][entry][100000]: OnBackPressed called
   [(100000:100000:scope)] Overlay consumed backpressed event
   ```
2. 排查弹窗组件是否注册onWillDismiss回调函数，检查拦截逻辑，看到应用只对下拉操作进行了处理。

   ```ts
   onWillDismiss:(dismissDialogAction: DismissDialogAction)=> {
     // 下拉
     if (dismissDialogAction.reason == DismissReason.SLIDE_DOWN) {
       // 关闭弹窗
       dismissDialogAction.dismiss()
     }
   }
   ```

关闭原因类型：

| 名称 | 值 | 描述 |
| --- | --- | --- |
| PRESS\_BACK | 0 | 点击三键back、左滑/右滑、键盘ESC。 |
| TOUCH\_OUTSIDE | 1 | 点击遮障层时。 |
| CLOSE\_BUTTON | 2 | 点击关闭按钮。 |
| SLIDE\_DOWN | 3 | 下拉关闭。该接口仅支持在半模态转场中使用。 |

## 分析结论

弹窗组件注册了onWillDismiss回调函数，然而未对侧滑场景做处理。

## 修改建议

对侧滑场景也进行关闭弹窗操作。

```ts
@CustomDialog
struct CustomDialogExample {
  controller?: CustomDialogController;
  cancel: () => void = () => {
  };
  confirm: () => void = () => {
  };

  build() {
    Column() {
      Text('这是自定义弹窗')
        .fontSize(30)
        .height(100)
      Button('关闭弹窗')
        .onClick(() => {
          if (this.controller != undefined) {
            this.controller.close();
          }
        })
        .margin(20)
    }
  }
}

@Entry
@Component
struct CustomDialogPage {
  dialogController: CustomDialogController | null = new CustomDialogController({
    builder: CustomDialogExample({
      cancel: () => {
        this.onCancel();
      },
      confirm: () => {
        this.onAccept();
      }
    }),
    cancel: this.existApp,
    autoCancel: true,
    onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
      console.info(`reason= ${dismissDialogAction.reason}`);
      console.info('dialog onWillDismiss');
      if (dismissDialogAction.reason == DismissReason.PRESS_BACK) {
        dismissDialogAction.dismiss();
      }
      if (dismissDialogAction.reason == DismissReason.TOUCH_OUTSIDE) {
        dismissDialogAction.dismiss();
      }
    },
    alignment: DialogAlignment.Center,
    offset: { dx: 0, dy: -20 },
    customStyle: false,
    cornerRadius: 20,
    width: 300,
    height: 200,
    borderWidth: 1,
  });

  // 在自定义组件即将析构销毁时将dialogController置空
  aboutToDisappear() {
    this.dialogController = null; // 将dialogController置空
  }

  onCancel() {
    console.info('Callback when the first button is clicked');
  }

  onAccept() {
    console.info('Callback when the second button is clicked');
  }

  existApp() {
    console.info('Click the callback in the blank area');
  }

  build() {
    Column() {
      Button('click me')
        .onClick(() => {
          if (this.dialogController != null) {
            this.dialogController.open();
          }
        }).backgroundColor(0x317aff)
    }.width('100%').margin({ top: 5 })
  }
}
```
