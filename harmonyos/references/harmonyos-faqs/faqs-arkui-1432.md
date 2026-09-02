---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1432
title: 如何在SDK包中获取宿主应用的沉浸式状态
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 如何在SDK包中获取宿主应用的沉浸式状态
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:30eaf425c632af6d82161663c19767015e38bb14231a5b9dd131f3b98ec3919c
---

## 问题现象

SDK项目采用HAR包的方式集成到宿主应用中，如何在SDK包中获取宿主应用的沉浸式状态？

## 背景知识

[@ohos.window (窗口)](../harmonyos-references/js-apis-window.md)提供了窗口管理器[WindowStage](../harmonyos-references/arkts-apis-window-windowstage.md)，用于管理各个基本窗口单元。同时，可通过[getWindowProperties](../harmonyos-references/arkts-apis-window-window.md#getwindowproperties9)方法获取当前窗口的属性，其中isLayoutFullScreen可以判断窗口是否为沉浸式且处于全屏模式。

初次创建SDK项目可参考[创建及发布三方库](https://ohpm.openharmony.cn/#/cn/help/createandpublish)。利用DevEco Studio对开发后的库模块打成HAR包，详情请见：[构建HAR](../harmonyos-guides/ide-hvigor-build-har.md)。在项目中引入三方库参考[配置依赖项](../harmonyos-guides/ide-hvigor-dependencies.md#section15420141487)。

## 解决方案

* 主要思路：HAR通过提供接口的方式，将相关功能模块开放给HAP使用。在HAP包中调用这些接口方法，将所需数据传递至HAR，从而实现数据交互与共享。

  实现步骤：
  1. 通过AppStorage.setAndLink存储WindowStage。可参考[如何在Page中获取WindowStage实例](faqs-arkui-298.md)。
  2. 在HAR包中定义方法，通过AppStorage.get获取WindowStage，使用getWindowProperties().isLayoutFullScreen获取宿主应用沉浸式状态，通过export[导出类和方法](../harmonyos-guides/har-package.md#导出类和方法)：

     ```ts
     import { window } from '@kit.ArkUI';

     export function saveWindowStage(windowStage: window.WindowStage) {
       AppStorage.setAndLink('windowStage', windowStage);
     }

     export function getFullScreenStatus(): string {
       let winStage: window.WindowStage = AppStorage.get('windowStage') as window.WindowStage;
       let isLayoutFullScreen = winStage.getMainWindowSync().getWindowProperties().isLayoutFullScreen;
       console.info(isLayoutFullScreen ? 'isFullScreen' : 'isNotFullScreen');
       // 返回结果给应用页，如不需要则不返回。在应用侧直接调用该函数。
       return (isLayoutFullScreen ? 'isFullScreen' : 'isNotFullScreen');
     }
     ```
  3. 在HAP中调用HAR方法，获取HAP窗口沉浸式状态信息，注意代码中SDKName需要替换成HAR包名称。

     ```ts
     import { PromptAction } from '@kit.ArkUI';
     import { getFullScreenStatus } from 'sdkname';
     import { common } from '@kit.AbilityKit';

     @Entry
     @Component
     struct Index {
       @State isFullScreen: boolean = false; // 切换屏幕全屏
       @State state: string = ''; // 存储HAR中获取沉浸式状态
       promptAction: PromptAction = this.getUIContext().getPromptAction();
       context = this.getUIContext().getHostContext() as common.UIAbilityContext;

       aboutToAppear(): void {
         // 通过AppStorage.setAndLink存储WindowStage
         AppStorage.setAndLink('windowStage', this.context.windowStage);
         // 进入应用调用HAR方法获取屏幕状态
         this.state = getFullScreenStatus();
         this.promptAction.showToast({
           message: this.state,
           duration: 2000
         });
       }

       build() {
         Row() {
           Column({ space: 5 }) {
             Text('获取宿主应用窗口是否沉浸式')
               .fontSize(30)
               .fontWeight(FontWeight.Bold);
             Button('changeFullScreenStatus').onClick(async () => {
               // 切换屏幕状态
               this.isFullScreen = !this.isFullScreen;
               await this.context.windowStage.getMainWindowSync().setWindowLayoutFullScreen(this.isFullScreen);
               // 调用SDK方法获取屏幕状态
               this.state = getFullScreenStatus();
               this.promptAction.showToast({
                 message: this.state,
                 duration: 2000
               });
             });
           }
           .width('100%');
         }
         .height('100%')
         .backgroundColor('#eaeaea');
       }
     }
     ```
