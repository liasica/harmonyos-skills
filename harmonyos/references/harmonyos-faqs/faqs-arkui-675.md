---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-675
title: 非交互式关闭弹窗实现方案
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 非交互式关闭弹窗实现方案
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:19+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5de70249056b04042bc867542d36396f9aaf7895dc268cd83aa964d3dcf98808
---

## 问题现象

对于一个弹窗，如何使用非交互方式关闭，即支持使用代码关闭它，不是用户触摸屏幕操作关闭。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/nWB5MFyySu2L2hR9dnkJaw/zh-cn_image_0000002658793947.png "点击放大")

## 背景知识

* [自定义弹窗](../harmonyos-references/ts-methods-custom-dialog-box.md)在HarmonyOS中是一种灵活的用户交互方式，用于显示临时信息或获取用户输入，并且当用户执行点击遮障层关闭、侧滑（左滑/右滑）、三键back、键盘ESC关闭交互操作时，如果注册自定义弹窗的[onWillDismiss](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)回调函数，则不会立刻关闭弹窗。在回调函数中可以通过reason得到阻拦关闭弹窗的操作类型，从而根据原因选择是否能关闭弹窗，具体用法可参见：[弹出嵌套弹窗](../harmonyos-references/ts-methods-custom-dialog-box.md#示例1弹出嵌套弹窗)示例中onWillDismiss的用法。
* [setInterval](../harmonyos-references/js-apis-timer.md#setinterval)用于按照指定的周期（以毫秒计）来执行注册的回调函数。
* [aboutToAppear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)函数在创建自定义组件的新实例后，在执行其build()函数之前执行；允许在aboutToAppear函数中改变状态变量，更改将在后续执行build()函数中生效。

## 解决方案

在aboutToAppear生命周期中调用setInterval方法实现一个倒计时功能，在倒计时结束后调用[关闭弹窗](../harmonyos-references/ts-methods-custom-dialog-box.md#close)的方法并清理interval任务。

1. 注册自定义弹窗的onWillDismiss回调函数，并在回调内拦截用户操作关闭弹窗。

   ```screen
   dialogController: CustomDialogController | null = new CustomDialogController({
     builder: AutoCloseCustomDialog({
       cancel: ()=> { this.onCancel(); },
       confirm: ()=> { this.onAccept(); },
       timeout: 5
     }),
     cancel: this.existApp,
     autoCancel: true,
     onWillDismiss:(dismissDialogAction: DismissDialogAction)=> {
       // 拦截三键back关闭弹窗
       if (dismissDialogAction.reason == DismissReason.PRESS_BACK) {
       }
       // 拦截点击遮障层关闭弹窗
       if (dismissDialogAction.reason == DismissReason.TOUCH_OUTSIDE) {
       }
     },
     alignment: DialogAlignment.Center,
     offset: { dx: 0, dy: -20 },
     customStyle: false,
     cornerRadius: 20,
     borderColor: Color.Blue,
     backgroundColor: Color.White
   });
   ```
2. aboutToAppear生命周期中通过setInterval方式对关闭按钮进行倒计时。

   ```screen
   aboutToAppear(): void {
     this.interval = setInterval(() => {
       // 倒计时结束，调用关闭弹窗方法并取消interval任务
       if (this.timeout <= 1) {
         this.closeDialog();
         return;
       }
       this.timeout -= 1;
       console.info(`interval timeout = ${this.timeout}`);
     }, 1000);
   }
   ```

完整示例参考如下：

```screen
@CustomDialog
@Component
struct AutoCloseCustomDialog {
  @State timeout: number = 10;
  interval: number = 0;
  controller?: CustomDialogController;
  cancel: () => void = () => {
  };
  confirm: () => void = () => {
  };

  // 生命周期中通过setInterval方式对关闭按钮进行倒计时
  aboutToAppear(): void {
    this.interval = setInterval(() => {
      // 倒计时结束，调用关闭弹窗方法并取消interval任务
      if (this.timeout <= 1) {
        this.closeDialog();
        return;
      }
      this.timeout -= 1;
      console.info(`interval timeout = ${this.timeout}`);
    }, 1000);
  }
  closeDialog() {
    // 取消interval任务
    clearInterval(this.interval);
    // 关闭自定义弹窗
    this.controller?.close();
    console.info(`closeDialog success and interval = ${this.interval}`);
  }

  build() {
    Column() {
      Text('这是个可以自动关闭的自定义弹窗').textTitleExtend()

      Text('关闭' + this.timeout + 's')
        .textButtonExtend()
        .onClick(() => {
          if (this.controller !== undefined) {
            this.controller.close();
            // 手动关闭，取消interval任务
            clearInterval(this.interval);
          }
        });
    }
    .height(150)
    .justifyContent(FlexAlign.SpaceEvenly)
  }
}

@Extend(Text)
function textButtonExtend() {
  .fontFamily("HarmonyHeiTi")
  .fontColor("#0A59F7")
  .fontSize(16)
  .fontWeight(500)
  .lineHeight(21)
  .textAlign(TextAlign.Center);
}

@Extend(Text)
function textTitleExtend() {
  .fontFamily("HarmonyHeiTi")
  .fontColor($r('sys.color.black'))
  .fontSize(16)
  .fontWeight(500)
  .lineHeight(21)
  .textAlign(TextAlign.Center);
}

@Entry
@Component
struct AutoCloseCustomDialogIndex {
  dialogController: CustomDialogController | null = new CustomDialogController({
    builder: AutoCloseCustomDialog({
      cancel: ()=> { this.onCancel(); },
      confirm: ()=> { this.onAccept(); },
      timeout: 5
    }),
    cancel: this.existApp,
    autoCancel: true,
    onWillDismiss:(dismissDialogAction: DismissDialogAction)=> {
      // 拦截三键back关闭弹窗
      if (dismissDialogAction.reason == DismissReason.PRESS_BACK) {
      }
      // 拦截点击遮障层关闭弹窗
      if (dismissDialogAction.reason == DismissReason.TOUCH_OUTSIDE) {
      }
    },
    alignment: DialogAlignment.Center,
    offset: { dx: 0, dy: -20 },
    customStyle: false,
    cornerRadius: 20,
    borderColor: Color.Blue,
    backgroundColor: Color.White
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

  existApp() {
    console.info('Click the callback in the blank area');
  }

  build() {
    Column() {
      Button('click me')
        .backgroundColor(0x317aff)
        .onClick(() => {
          if (this.dialogController != null) {
            this.dialogController.open();
          }
        });
    }
    .width('100%')
    .margin({ top: 5 })
  }
}
```

## 总结

自定义弹窗既可以用户触摸屏幕手动关闭也可以自动关闭，无论哪一种都是通过执行指定代码命令完成的，只是触发方式不同。弹窗自动关闭的触发方式有很多种，如某个状态变量的改变、订阅或接收到指定消息、倒计时等，也可以同时支持多种方式。上述代码示例即是同时支持触摸屏幕手动关闭和倒计时结束自动关闭弹窗两种方式。
