---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1102
title: 如何监听屏幕截屏、录屏及投屏状态变化
breadcrumb: FAQ > 应用框架开发 > UI框架 > 屏幕管理 > 如何监听屏幕截屏、录屏及投屏状态变化
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:13+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:2d1140552282f0379167eb2171683aa6c96cc3bec8bd9091ef62e1d337c7baba
---

## 问题现象

当用户处理隐私敏感数据时（如支付验证、身份信息录入），需主动监听用户的截屏、录屏及投屏行为。一旦检测到此类操作，应立即触发防护机制包括实时提醒用户风险或强制终止可能造成数据泄露的操作。

## 背景知识

* [on('screenshot')](../harmonyos-references/arkts-apis-window-window.md#onscreenshot9)：开启截屏事件的监听。
* [AppStorage](../harmonyos-references/ts-state-management.md#appstorage)：AppStorage是与应用进程绑定的全局UI状态存储中心，由UI框架在应用启动时创建，将UI状态数据存储于运行内存，实现应用级全局状态共享。
* [display.on('captureStatusChange')](../harmonyos-references/js-apis-display.md#displayoncapturestatuschange12)：开启设备的屏幕显示信息是否被获取的监听。
* [display.isCaptured](../harmonyos-references/js-apis-display.md#displayiscaptured12)：检查设备的屏幕显示信息是否被获取。
* [showToast](../harmonyos-references/arkts-apis-uicontext-promptaction.md#showtoast)：创建并显示即时反馈。
* [setWindowPrivacyMode](../harmonyos-references/arkts-apis-window-window.md#setwindowprivacymode9)：设置窗口是否为隐私模式，使用callback异步回调。设置为隐私模式的窗口，窗口内容将无法被截屏或录屏。
* [window.getLastWindow](../harmonyos-references/arkts-apis-window-f.md#windowgetlastwindow9)：获取当前应用内层级最高的子窗口，使用callback异步回调。

## 解决方案

* 方案一：通过display.on('captureStatusChange')监听设备的屏幕显示信息是否被获取，并在监听回调内给用户提示，具体实现如下：

  ```ts
  import { display } from '@kit.ArkUI';

  @Entry
  @Component
  struct Index {
    aboutToAppear(): void {

      let callback: Callback<boolean> = (captureStatus: boolean) => {
        console.info('Listening capture status: ' + captureStatus);
        if (captureStatus) {
          this.getUIContext().getPromptAction().showToast({
            message: '您在尝试截屏、录屏，请注意保护隐私。',
            duration: 2000
          });
        }
      };
      // 开启设备的屏幕显示信息是否被获取的监听。
      display.on('captureStatusChange', callback);
    }

    build() {
      RelativeContainer() {
        Text('通过display.on(\'captureStatusChange\')监听屏幕状态')
          .padding({ left: 20, right: 20 })
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          });
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

  效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/ETVFXDvfQF6wPpHg8RWUbw/zh-cn_image_0000002698150521.png "点击放大")
* 方案二：通过display.isCaptured方法主动获取屏幕状态，具体实现如下：

  ```ts
  import { display } from '@kit.ArkUI';

  @Entry
  @Component
  struct CaptureThree {
    build() {
      RelativeContainer() {
        Button('通过display.isCaptured主动获取屏幕状态')
          .backgroundColor('#0A59F7')
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onClick(() => {
            // 通过display.isCaptured主动获取当前屏幕状态。
            if (display.isCaptured()) {
              this.getUIContext().getPromptAction().showToast({
                message: '您在尝试截屏、录屏、投屏，请注意保护隐私。',
                duration: 2000
              });
            } else {
              this.getUIContext().getPromptAction().showToast({
                message: '屏幕未进行截屏、录屏、投屏行为。',
                duration: 2000
              });
            }
          });
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/0DC_GfidR6S-6pWIdcIxAw/zh-cn_image_0000002698150609.png "点击放大")
* 方案三：在代码中同时添加window.on('screenshot')和录屏display.on('captureStatusChange')的监听，观察到截屏事件的执行总是发生在录屏事件之前，事件的触发顺序提供了一种方式来区分应用程序中的截屏与录屏动作。
  1. 在EntryAbility中通过window.on('screenshot')监听用户的截屏操作，并保存在AppStorage中，具体实现如下：

     ```ts
     import { UIAbility } from '@kit.AbilityKit';
     import { hilog } from '@kit.PerformanceAnalysisKit';
     import { window } from '@kit.ArkUI';

     const DOMAIN = 0x0000;

     export default class EntryAbility extends UIAbility {
       onDestroy(): void {
         hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
       }

       onWindowStageCreate(windowStage: window.WindowStage): void {
         // Main window is created, set main page for this ability
         hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

         windowStage.loadContent('pages/Page', (err) => {
           if (err.code) {
             hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
             return;
           }
           AppStorage.setOrCreate('Status', 0);
           let windowClass = windowStage.getMainWindowSync();
           windowClass.on('screenshot', () => {
             // 保存截屏回调状态，走回调时为1，不走为0
             AppStorage.setOrCreate('Status', 1);
           });
           hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
         });
       }

       onWindowStageDestroy(): void {
         // Main window is destroyed, release UI related resources
         hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
       }

       onForeground(): void {
         // Ability has brought to foreground
         hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
       }

       onBackground(): void {
         // Ability has back to background
         hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
       }
     };
     ```
  2. 在Page.ets中通过display.on('captureStatusChange')监听配合EntryAbility中保存的截屏状态来区分是截屏还是录屏和投屏，具体实现如下：

     ```ts
     import { display } from '@kit.ArkUI';

     @Entry
     @Component
     struct Page {
       aboutToAppear(): void {
         let callback: Callback<boolean> = (captureStatus: boolean) => {
           // 获取Status的值判断是不是截屏：0不是截屏，1是截屏
           let status = AppStorage.get('Status')!;
           if (status == 0) {
             if (captureStatus) {
               this.getUIContext().getPromptAction().showToast({
                 message: '您在尝试投屏、录屏，请注意保护隐私。',
                 duration: 2000
               });
             } else {
               this.getUIContext().getPromptAction().showToast({
                 message: '投屏、录屏，已结束。',
                 duration: 2000
               });
             }
           } else {
             this.getUIContext().getPromptAction().showToast({
               message: '您在尝试截屏，请注意保护隐私。',
               duration: 2000
             });
           }
           AppStorage.setOrCreate('Status', 0);
         };
         display.on('captureStatusChange', callback);
       }

       build() {
         RelativeContainer() {
           Text('截屏、投屏、录屏监听')
             .fontSize(15)
             .fontWeight(FontWeight.Bold)
             .alignRules({
               center: { anchor: '__container__', align: VerticalAlign.Center },
               middle: { anchor: '__container__', align: HorizontalAlign.Center }
             });
         }
         .height('100%')
         .width('100%');
       }
     }
     ```

     效果如下：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/GzGMHUV3QlyE2OKTFNR7Lw/zh-cn_image_0000002698230865.png "点击放大")

## 常见FAQ

Q：为什么DevEco Testing工具的投屏，会不断触发window.on('screenshot')监听？

A：DevEco Testing投屏功能需持续捕获设备屏幕画面，其底层实现依赖系统截屏API。当投屏刷新率较高时，会频繁触发系统截屏事件，导致on('screenshot')监听被多次调用。

Q：应用监听用户截屏和录屏行为是否符合应用审核规范？

A：应用不得含有试图滥用或不当使用任何网络、设备以及干扰其他应用的安全隐患。具体审核要求请参考[应用审核指南](../app/50104.md)。
