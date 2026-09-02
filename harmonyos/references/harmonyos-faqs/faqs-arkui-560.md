---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-560
title: 如何解决子窗口设置状态栏颜色失败问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 如何解决子窗口设置状态栏颜色失败问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:13+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f279ba16f72e7987848e8488b165885c1e6f8a5e7102fdac3fc83b6613379ebc
---

## 问题现象

通过createSubWindow开启子窗口后，调用setWindowSystemBarProperties方法设置状态栏颜色无效，如何设置状态栏颜色？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/YvhV-RTPSdaoGi8Ld9c_UQ/zh-cn_image_0000002658791403.gif "点击放大")

## 背景知识

* [@ohos.window (窗口)](../harmonyos-references/js-apis-window.md)：提供管理窗口的一些基础能力，包括对当前窗口的创建、销毁、各属性设置，以及对各窗口间的管理调度。
* [setWindowSystemBarProperties](../harmonyos-references/arkts-apis-window-window.md#setwindowsystembarproperties9)：可以设置主窗口三键导航栏、状态栏的属性。
* [AppStorage](../harmonyos-guides/arkts-appstorage.md#概述)：是应用全局的UI状态存储，和应用的进程绑定，由UI框架在应用程序启动时创建，为应用程序UI状态属性提供中央存储。
* [getLastWindow](../harmonyos-references/arkts-apis-window-f.md#windowgetlastwindow9)：获取当前应用内最上层显示的子窗口，若无应用子窗口或子窗口未调用showWindow()进行显示，则返回应用主窗口。
* [createWindow](../harmonyos-references/arkts-apis-window-f.md#windowcreatewindow9)：创建子窗口或者系统窗口。

* getLastWindow和createWindow区别如下：

| API | 功能定位 | 应用场景 | 权限与限制 |
| --- | --- | --- | --- |
| createWindow | 用于创建新的窗口实例，属于主动生成窗口的操作。需明确指定窗口类型（如应用主窗口、子窗口或系统窗口）及相关参数。 | 创建弹窗、分屏窗口、初始化应用主窗口时动态生成窗口。 | 部分窗口类型（如系统窗口）需要特定权限。 |
| getLastWindow | 用于获取当前窗口栈中位于顶部的窗口实例（即最近使用的窗口），属于被动获取已有窗口的操作。 | 设置屏幕常亮、修改状态栏颜色、调整窗口方向。 | 若无活动窗口或窗口状态异常（如已被销毁），可能抛出错误码 1300002（窗口状态异常）。 |

## 解决方案

设置状态栏颜色需要在主窗口中设置才能生效，可以在EntryAbility中先获取到主窗口，存储后在子窗口中获取并使用。

1. 在EntryAbility.ets中获取window.getLastWindow，使用AppStorage存储windowClass。

   ```ts
   onWindowStageCreate(windowStage: window.WindowStage): void {
     windowStage.loadContent('pages/Index', (err) => {
       let windowClass: window.Window | undefined = undefined;
       window.getLastWindow(this.context, (err: BusinessError, data) => {
         if (err.code) {
           return;
         }
         windowClass = data;
         // 通过AppStorage存储windowClass
         AppStorage.setOrCreate("windowClass", windowClass);
         AppStorage.setOrCreate('windowStage', windowStage);
       });
       if (err.code) {
         return;
       }
     });
   }
   ```
2. 在子窗口中使用AppStorage取出windowClass设置状态栏颜色。

   ```ts
   // 通过AppStorage获取windowClass
   let windowClass = AppStorage.get('windowClass') as window.Window;
   // 配置状态栏颜色参数
   let sysBarProps: window.SystemBarProperties = {
     // 支持十六进制RGB/ARGB格式（如'#FFC0CB'或'FFC0CB'），需注意颜色值包含透明度通道。
     statusBarColor: '#0A59F7',
     statusBarContentColor: '#ffffff',
   };
   // 通过windowClass设置状态栏颜色
   try {
     let promise = windowClass.setWindowSystemBarProperties(sysBarProps);
     promise.then(() => {
       console.info('Succeeded in setting the system bar properties.');
     }).catch((err: BusinessError) => {
       console.error(`Failed to set the system bar properties. Cause code: ${err.code}, message: ${err.message}`);
     });
   } catch (exception) {
     console.error(`Failed to set the system bar properties. Cause code: ${exception.code}, message: ${exception.message}`);
   }
   ```

完整示例参考如下：

1. Index.ets。

   ```ts
   import { display, window } from '@kit.ArkUI';
   import { BusinessError } from '@kit.BasicServicesKit';

   let windowStage_: window.WindowStage | undefined = undefined;
   let sub_windowClass: window.Window | undefined = undefined;

   @Entry
   @Component
   struct Index {
     build() {
       Column() {
         Button('打开子窗口')
           .onClick(() => {
             this.createSubWindow();
           })
           .margin({ top: 60 })
       }
       .alignItems(HorizontalAlign.Center)
       .justifyContent(FlexAlign.Center)
       .height('100%')
       .width('100%')
     }

     private createSubWindow() {
       let displayClass: display.Display = display.getDefaultDisplaySync();
       // 计算中心点坐标
       let centerX: number = displayClass.width / 2;
       let centerY: number = displayClass.height / 2;
       // 获取windowStage
       windowStage_ = AppStorage.get('windowStage');
       // 1.创建应用子窗口。
       if (windowStage_ == null) {
         console.error('Failed to create the subwindow. Cause: windowStage_ is null');
       } else {
         windowStage_.createSubWindow("mySubWindow", (err: BusinessError, data) => {
           let errCode: number = err.code;
           if (errCode) {
             console.error('Failed to create the subwindow. Cause: ' + JSON.stringify(err));
             return;
           }
           sub_windowClass = data;
           if (!sub_windowClass) {
             console.error('sub_windowClass is null');
             return;
           }
           console.info('Succeeded in creating the subwindow. Data: ' + JSON.stringify(data));
           // 2.子窗口创建成功后，设置子窗口的位置、大小及相关属性等。
           sub_windowClass.moveWindowTo(centerX-300, centerY-300, (err: BusinessError) => {
             let errCode: number = err.code;
             if (errCode) {
               console.error('Failed to move the window. Cause:' + JSON.stringify(err));
               return;
             }
             console.info('Succeeded in moving the window.');
           });
           sub_windowClass.resize(600, 600, (err: BusinessError) => {
             let errCode: number = err.code;
             if (errCode) {
               console.error('Failed to change the window size. Cause:' + JSON.stringify(err));
               return;
             }
             console.info('Succeeded in changing the window size.');
           });
           // 3.为子窗口加载对应的目标页面。
           sub_windowClass.setUIContent("pages/SubPage", (err: BusinessError) => {
             let errCode: number = err.code;
             if (errCode) {
               console.error('Failed to load the content. Cause:' + JSON.stringify(err));
               return;
             }
             console.info('Succeeded in loading the content.');
             if (!sub_windowClass) {
               console.error('sub_windowClass is null');
               return;
             }
             // 3.显示子窗口。
             sub_windowClass.showWindow((err: BusinessError) => {
               let errCode: number = err.code;
               if (errCode) {
                 console.error('Failed to show the window. Cause: ' + JSON.stringify(err));
                 return;
               }
               console.info('Succeeded in showing the window.');
             });
           });
         });
       }
     }
   }
   ```
2. SubPage.ets。

   ```ts
   import { window } from '@kit.ArkUI';
   import { BusinessError } from '@kit.BasicServicesKit';

   @Entry
   @Component
   struct SubPage {
     build() {
       Column() {
         Text('Change BarColor')
           .fontSize(18)
           .fontWeight(FontWeight.Bold)
           .onClick(() => {
             // 通过AppStorage获取windowClass
             let windowClass = AppStorage.get('windowClass') as window.Window;
             // 配置状态栏颜色参数
             let sysBarProps: window.SystemBarProperties = {
               // 支持十六进制RGB/ARGB格式（如'#FFC0CB'或'FFC0CB'），需注意颜色值包含透明度通道。
               statusBarColor: '#0A59F7',
               statusBarContentColor: '#ffffff',
             };
             // 通过windowClass设置状态栏颜色
             try {
               let promise = windowClass.setWindowSystemBarProperties(sysBarProps);
               promise.then(() => {
                 console.info('Succeeded in setting the system bar properties.');
               }).catch((err: BusinessError) => {
                 console.error(`Failed to set the system bar properties. Cause code: ${err.code}, message: ${err.message}`);
               });
             } catch (exception) {
               console.error(`Failed to set the system bar properties. Cause code: ${exception.code}, message: ${exception.message}`);
             }
           })
       }
       .justifyContent(FlexAlign.Center)
       .backgroundColor('#EFF1F4')
       .height('100%')
       .width('100%')
     }
   }
   ```

## 常见FAQ

Q：调用window实例的setWindowSystemBarProperties接口时，设置isStatusBarLightIcon和isNavigationBarLightIcon属性无效。

A：可以参考：[调用window实例的setWindowSystemBarProperties接口设置窗口状态栏和导航栏的高亮属性时不生效](faqs-arkui-195.md)。

Q：setWindowSystemBarProperties配置修改后，如何恢复默认配置，让其跟随深色模式切换？

A：setWindowSystemBarProperties配置修改后，无法直接恢复默认，需要根据系统的当前颜色模式来动态设置状态栏的颜色。详细可参考官方文档：[在深色模式切换下如何适配状态栏颜色?](faqs-arkui-359.md)

Q：window.createWindow接口是否有改动？之前在应用商店上架的版本弹窗能正常弹出，现在弹窗没法正常弹出。

A：从API 18版本起，创建窗口类型为window.WindowType.TYPE\_FLOAT需要申请ohos.permission.SYSTEM\_FLOAT\_WINDOW权限才能弹窗，需要注意的是，该权限属于受限权限，当前仅PC/2in1设备应用可申请此权限，具体可参考：[悬浮窗权限说明](../harmonyos-guides/restricted-permissions.md#ohospermissionsystem_float_window)，在其他设备或场景下，请使用“画中画”功能，使用方式请参考：[画中画开发指导](../harmonyos-guides/window-pipwindow.md)。
