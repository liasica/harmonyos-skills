---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-threading-model-3
title: 加载弹窗闪烁
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 加载弹窗闪烁
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:06f8a865447d24f99872a06c9a10049a509f26e627cc08a2393db44485cad4a7
---

## 问题现象

在点击验证码“获取”按钮时，加载弹窗出现闪烁。

## 背景知识

[async/await](../harmonyos-guides/async-concurrency-overview.md#asyncawait)是一种用于处理异步操作的Promise语法糖，使得编写异步代码变得更加简单和易读。通过使用async关键字声明一个函数为异步函数，并使用await关键字等待Promise的解析（完成或拒绝），以同步的方式编写异步操作的代码。

## 问题定位

1. 使用DevEco Studio查看日志，日志显示弹窗频繁关闭。

   ```screen
   03-10 16:08:16.862  3319  3319 I C0390F/com.ohos.sceneboard/AceDialog: [(100000:100000:scope)] CustomDialogController SetCloseDialog enter.
   03-10 16:08:16.862  3319  3319 I C0390F/com.ohos.sceneboard/AceDialog: [(100000:100000:scope)] CustomDialogController SetCloseDialog enter.
   03-10 16:08:16.862  3319  3319 I C0390F/com.ohos.sceneboard/AceDialog: [(100000:100000:scope)] CustomDialogController SetCloseDialog enter.
   ```
2. 查看按钮点击事件的设置，每个异步操作结束后都执行关闭弹窗的操作。

   ```screen
   async getVerificationCode() {
     await this.handleTaskA();
     await this.handleTaskB();
     await this.handleTaskC();
   }

   handleTaskA(): Promise<void> {
     return new Promise((resolve) => {
       this.dialogController.open();
       setTimeout(() => {
         // ...
         resolve();
       }, 100);
       this.dialogController.close();
     });
   }

   handleTaskB(): Promise<void> {
     return new Promise((resolve) => {
       this.dialogController.open();
       setTimeout(() => {
         // ...
         resolve();
       }, 100);
       this.dialogController.close();
     });
   }

   handleTaskC(): Promise<void> {
     return new Promise((resolve) => {
       this.dialogController.open();
       setTimeout(() => {
         // ...
         resolve();
       }, 100);
       this.dialogController.close();
     });
   }
   ```

## 分析结论

获取验证码的流程中，存在频繁调用关闭弹窗，导致出现闪烁。

## 修改建议

在处理一个业务流程中，同时存在多个异步事件，可以通过async/await简化异步编程，合并过程中频繁打开/关闭弹窗的操作。

```screen
@CustomDialog
struct CustomDialogExample {
  controller?: CustomDialogController;

  build() {
    Column() {
      Text('这是自定义弹窗')
        .fontSize(30)
        .height(100)
      Button('点我关闭弹窗')
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
struct CustomDialogUser {
  dialogController: CustomDialogController = new CustomDialogController({
    builder: CustomDialogExample({}),
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
    borderStyle: BorderStyle.Dashed,
    borderColor: Color.Blue,
    backgroundColor: Color.White,
    shadow: ({
      radius: 20,
      color: Color.Grey,
      offsetX: 50,
      offsetY: 0
    }),
  });

  async getVerificationCode() {
    this.dialogController.open();
    try {
      await this.handleTaskA();
      await this.handleTaskB();
      await this.handleTaskC();
    } catch (error) {
      // ...
    } finally {
      this.dialogController.close();
    }
  }

  handleTaskA(): Promise<void> {
    return new Promise((resolve) => {
      setTimeout(() => {
        // ...
        resolve();
      }, 100);
    });
  }

  handleTaskB(): Promise<void> {
    return new Promise((resolve) => {
      setTimeout(() => {
        // ...
        resolve();
      }, 100);
    });
  }

  handleTaskC(): Promise<void> {
    return new Promise((resolve) => {
      setTimeout(() => {
        // ...
        resolve();
      }, 100);
    });
  }

  build() {
    Column() {
      Button('click me')
        .onClick(() => {
          if (this.dialogController != null) {
            this.getVerificationCode();
          }
        }).backgroundColor(0x317aff)
    }.width('100%').margin({ top: 5 })
  }
}
```
