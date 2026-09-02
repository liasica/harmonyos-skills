---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1567
title: 应用首页在手机上侧滑能弹出弹窗，在平板上无法弹出弹窗
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 应用首页在手机上侧滑能弹出弹窗，在平板上无法弹出弹窗
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b490ef86df162b157e3542bc35a2857d115a15fac6c53b3f773a34c82ccdc9e7
---

## 问题现象

打开应用，首页侧滑可以弹出自定义弹窗，平板打开应用，首页侧滑，无法弹出弹窗。

## 背景知识

[onBackPress](../harmonyos-references/ts-custom-component-lifecycle.md#onbackpress)：当用户点击返回按钮时触发（仅router路由页面生效）。返回true表示页面自己处理返回逻辑，不进行页面路由；返回false表示使用默认的路由返回逻辑，不设置返回值按照false处理。

## 问题定位

1. 查阅手机上，首页侧滑时onBackPress相关的日志信息，表明侧滑事件响应成功。

   ```shell
   07-23 11:02:31.842   5374-14672    C03900/com.example.deviceinfousage/Ace  com.example.deviceinfousage  I     [(-1:100000:singleton)] [com.example.deviceinfousage][entry][100000]: OnBackPressed called
   07-23 11:02:31.844   5374-5374     C03925/com.example.deviceinfousage/AceRouter  com.example.deviceinfousage  I     [(100000:100000:scope)] router user onBackPress return true
   07-23 11:02:31.844   5374-5374     C03900/com.example.deviceinfousage/Ace  com.example.deviceinfousage  I     [(100000:100000:scope)] router consumed backpressed event
   ```
2. 查阅平板上，首页侧滑时onBackPress相关的日志信息，未出现侧滑响应事件成功，表明侧滑事件响应失败。

   ```shell
   07-23 10:31:11.215   45223-45563   C03900/com.example.deviceinfousage/Ace  com.example.deviceinfousage  I     [(-1:100000:singleton)] [com.example.deviceinfousage][entry][100000]: OnBackPressed called
   07-23 10:31:11.215   45223-45223   C03900/com.example.deviceinfousage/Ace  com.example.deviceinfousage  I     [(100000:100000:scope)] Overlay consumed backpressed event
   ```
3. 查阅首页onBackPress相关代码是否对设备类型进行了响应区分。

## 分析结论

1. 应用代码中重写了首页的onBackPress方法，在应用首页侧滑返回时会弹出自定义弹窗。
2. onBackPress方法中代码逻辑存在问题，导致只在手机上会响应成功，在平板上响应失败。

## 修改建议

修改首页侧滑自定义事件代码逻辑，保证在所有设备均生效。

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
      Text('温馨提示')
        .fontSize(25)
        .margin({ top: 10 });
      Text('受低温雨雪冰冻和大雾天气影响，部分地区易同时出现道路结冰、湿滑、能见度低等复合灾害效应。请广大群众加强安全防范，谨防事故发生。')
        .padding({ left: 20, right: 20 });
      Row({ space: 50 }) {
        Button('确认').onClick(() => {
          if (this.controller) {
            this.controller.close();
          }
        });
        Button('取消').onClick(() => {
          if (this.controller) {
            this.controller.close();
          }
        });
      };
    }.height(200).padding(5).justifyContent(FlexAlign.SpaceAround);
  }
}

@Entry
@Component
struct CustomDialogUser {
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
    backgroundColor: Color.White,
  });

  // 在自定义组件即将析构销毁时将dialogController置空
  aboutToDisappear() {
    this.dialogController = null; // 将dialogController置空
  }

  onBackPress(): boolean | void {
    if (this.dialogController != null) {
      this.dialogController.open();
    }
    return true;
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
    RelativeContainer() {
      Button('click me')
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          if (this.dialogController != null) {
            this.dialogController.open();
          }
        }).backgroundColor(0x317aff);
    }.width('100%').margin({ top: 5 });
  }
}
```

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/3iqX6PE5RPmNv5jHJs8ryQ/zh-cn_image_0000002628769760.png "点击放大")
