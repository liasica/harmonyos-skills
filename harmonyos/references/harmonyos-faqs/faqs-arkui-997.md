---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-997
title: 通过弹窗生命周期实现广告弹窗的倒计时控制
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 通过弹窗生命周期实现广告弹窗的倒计时控制
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:25+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:363e13b1c0193bce3832a486762b8d543ecfd90ef99dbea69d13254ade0f6a27
---

## 问题现象

如何通过合理利用openCustomDialog的生命周期回调（如在onWillAppear中重置定时器、onDidAppear中启动定时器、在onWillDismiss中拦截广告弹窗的关闭等）来实现广告弹窗的精细化控制？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/nHvGmVUTSs-PBtLqK6olTA/zh-cn_image_0000002658801093.png "点击放大")

## 背景知识

* [openCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialog12-1)是用于创建全局自定义弹窗的核心接口，可通过[CustomDialogOptions](../harmonyos-references/js-apis-promptaction.md#customdialogoptions11)自定义弹窗的内容参数，其类型继承自[BaseDialogOptions](../harmonyos-references/js-apis-promptaction.md#basedialogoptions11)，BaseDialogOptions类型定义包含了onWillAppear、onDidAppear、onWillDisappear、onDidDisappear、onWillDismiss，这些生命周期的回调。
* [TextTimer](../harmonyos-references/ts-basic-components-texttimer.md)是用于显示计时信息并控制计时器状态的组件。

## 解决方案

使用openCustomDialog弹窗作为广告弹窗页面的载体，TextTimer作为倒计时组件，根据该组件控制广告的观看时间和关闭逻辑，具体实现如下：

1. 通过backgroundColor和backgroundBlurStyle设置弹窗背景色为透明。

   ```ts
   backgroundColor: Color.Transparent,
   backgroundBlurStyle: BlurStyle.NONE,
   ```
2. 通过Builder方法创建弹窗布局，使用[Stack](../harmonyos-references/ts-container-stack.md)堆叠容器，根据时机控制弹窗关闭按钮和倒计时组件的显示和隐藏，并通过[Web](../harmonyos-references/ts-basic-components-web.md)组件加载广告内容。

   ```ts
   @Builder
   customDialogComponent() {
     Column() {
       Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.SpaceBetween }) {
         Blank();
         Stack() {
           Image($r('sys.media.ohos_ic_public_close'))
             .width(30)
             .visibility(this.closeVisibility)
             .onClick(() => {
               this.getUIContext().getPromptAction().closeCustomDialog(this.customDialogComponentId);
             })
             .height(30);
           TextTimer({ isCountDown: true, count: 30000, controller: this.textTimerController })
             .format('ss')
             .fontColor(Color.Black)
             .fontSize(15)
             .padding({ left: 6 })
             .margin({ right: 20 })
             .width(30)
             .height(30)
             .borderRadius(15)
             .backgroundColor('#ff5f5e5e')
             .visibility(this.timerVisibility)
             .onTimer((utc: number, elapsedTime: number) => {
               console.info('utc=', utc);
               if (elapsedTime == 30) {
                 this.timerVisibility = Visibility.Hidden;
                 this.closeVisibility = Visibility.Visible;
               }
             });
         };
       };

       Web({ src: 'https://xxxxxx/', controller: this.webviewController })
         .margin({ top: 10 })
         .fileAccess(true)
         .geolocationAccess(false)
         .backgroundColor(Color.Transparent)
     }
     .backgroundColor(Color.Transparent);
   }
   ```
3. 在弹窗的生命周期内控制广告倒计时的开启和重置，并重置关闭按钮和倒计时的显示和隐藏，重写onWillDismiss方法，拦截点击遮障层、侧滑（左滑/右滑）、三键back交互操作时关闭弹窗。

   ```ts
   // 自定义弹窗生命周期回调
   onWillAppear: () => {
     // 在弹窗即将展示时重置定时器
     this.textTimerController.reset();
   },
   onDidAppear: () => {
     // 在弹窗展示时开始倒计时
     this.textTimerController.start();
   },
   onWillDisappear: () => {
   },
   onDidDisappear: () => {
     // 重置弹窗内按钮和倒计时的显示状态
     this.timerVisibility = Visibility.Visible;
     this.closeVisibility = Visibility.Hidden;
   },
   onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
     // 拦截用户执行点击遮障层关闭、侧滑（左滑/右滑）、三键back、键盘ESC关闭交互操作时关闭弹窗
     if (dismissDialogAction.reason == DismissReason.PRESS_BACK) {
     }
     if (dismissDialogAction.reason == DismissReason.TOUCH_OUTSIDE) {
     }
     if (dismissDialogAction.reason == DismissReason.SLIDE_DOWN) {
     }
   },
   ```
4. 在Entry模块下的module.json5中添加网络权限。

   ```json
   "requestPermissions": [
     {
       "name": "ohos.permission.INTERNET",
       "usedScene": {
         "abilities": ["EntryAbility"],         // 指定使用此权限的Ability
         "when": "always"                       // 权限使用时机
       }
     }
   ],
   ```

完整代码如下：

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct Index {
  private customDialogComponentId: number = 0;
  textTimerController: TextTimerController = new TextTimerController();
  webviewController: webview.WebviewController = new webview.WebviewController();
  @State timerVisibility: Visibility = Visibility.Visible;
  @State closeVisibility: Visibility = Visibility.Hidden;

  @Builder
  customDialogComponent() {
    Column() {
      Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.SpaceBetween }) {
        Blank();
        Stack() {
          Image($r('sys.media.ohos_ic_public_close'))
            .width(30)
            .visibility(this.closeVisibility)
            .onClick(() => {
              this.getUIContext().getPromptAction().closeCustomDialog(this.customDialogComponentId);
            })
            .height(30);
          TextTimer({ isCountDown: true, count: 30000, controller: this.textTimerController })
            .format('ss')
            .fontColor(Color.Black)
            .fontSize(15)
            .padding({ left: 6 })
            .margin({ right: 20 })
            .width(30)
            .height(30)
            .borderRadius(15)
            .backgroundColor('#ff5f5e5e')
            .visibility(this.timerVisibility)
            .onTimer((utc: number, elapsedTime: number) => {
              console.info('utc=', utc);
              if (elapsedTime == 30) {
                this.timerVisibility = Visibility.Hidden;
                this.closeVisibility = Visibility.Visible;
              }
            });
        };
      };

      Web({ src: 'https://xxxxxx/', controller: this.webviewController })
        .margin({ top: 10 })
        .fileAccess(true)
        .geolocationAccess(false)
        .backgroundColor(Color.Transparent)
    }
    .backgroundColor(Color.Transparent);
  }
  build() {
    Row() {
      Column({ space: 20 }) {
        Text('点击显示弹窗广告')
          .fontSize(30)
          .onClick(() => {
            this.getUIContext()
              .getPromptAction()
              .openCustomDialog({
                builder: () => {
                  this.customDialogComponent();
                },
                width: '80%',
                maskColor: '#ff8c8989',
                backgroundColor: Color.Transparent,
                backgroundBlurStyle: BlurStyle.NONE,
                // 自定义弹窗生命周期回调
                onWillAppear: () => {
                  // 在弹窗即将展示时重置定时器
                  this.textTimerController.reset();
                },
                onDidAppear: () => {
                  // 在弹窗展示时开始倒计时
                  this.textTimerController.start();
                },
                onWillDisappear: () => {
                },
                onDidDisappear: () => {
                  // 重置弹窗内按钮和倒计时的显示状态
                  this.timerVisibility = Visibility.Visible;
                  this.closeVisibility = Visibility.Hidden;
                },
                onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
                  // 拦截用户执行点击遮障层关闭、侧滑（左滑/右滑）、三键back、键盘ESC关闭交互操作时关闭弹窗
                  if (dismissDialogAction.reason == DismissReason.PRESS_BACK) {
                  }
                  if (dismissDialogAction.reason == DismissReason.TOUCH_OUTSIDE) {
                  }
                  if (dismissDialogAction.reason == DismissReason.SLIDE_DOWN) {
                  }
                },
              })
              .then((dialogId: number) => {
                this.customDialogComponentId = dialogId;
              })
              .catch((error: BusinessError) => {
                console.error(`openCustomDialog error code is ${error.code}, message is ${error.message}`);
              });
          });
      }
      .width('100%');
    }
    .height('100%');
  }
}
```
