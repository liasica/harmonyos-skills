---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-214
title: 如何设置沉浸式状态栏
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 如何设置沉浸式状态栏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6b20ded4e0130a38ef1ba10fc1c913c402e74d4c956ca3c04a0e67cd58d04167
---

1. 获取应用主窗口。通过getMainWindow接口获取应用主窗口。
2. 实现沉浸式效果。有以下两种方式：
   * 方式一：调用setWindowSystemBarEnable接口，设置导航栏、状态栏不显示，从而达到沉浸式效果。
   * 方式二：调用setWindowLayoutFullScreen接口，设置应用主窗口为全屏布局；然后调用setWindowSystemBarProperties接口，设置导航栏、状态栏的透明度、背景/文字颜色以及高亮图标等属性，使之保持与主窗口显示协调一致，从而达到沉浸式效果。
3. 加载显示沉浸式窗口的具体内容。通过loadContent接口加载沉浸式窗口的具体内容。

   ```ts
   import { UIAbility } from '@kit.AbilityKit';
   import { window } from '@kit.ArkUI';
   import { BusinessError } from '@kit.BasicServicesKit';

   export default class EntryAbility extends UIAbility {
     onWindowStageCreate(windowStage: window.WindowStage) {
       // 1.Get the main window of the application.
       let windowClass: window.Window | undefined = undefined;
       windowStage.getMainWindow((err: BusinessError, data) => {
         if (err.code) {
           console.error('Failed to obtain the main window. Cause: ' + JSON.stringify(err));
           return;
         }
         windowClass = data;
         console.info('Succeeded in obtaining the main window. Data: ' + JSON.stringify(data));

         // 2.Realize immersive effects. Method 1: Set the navigation bar and status bar to not display.
         let names = [];
         windowClass.setWindowSystemBarEnable(names).then(() => {
           console.info('Succeeded in setting the system bar to be visible.');
         }).catch((err: BusinessError) => {
           console.error('Failed to setting the system bar to be visible. Cause: ' + JSON.stringify(err));
         });
         // 2.Realize immersive effects. Method 2: Set the window to a full screen layout, and coordinate with the transparency, background/text color, and highlighted icons of the navigation bar and status bar to maintain consistency with the main window display.
         let isLayoutFullScreen = true;
         windowClass.setWindowLayoutFullScreen(isLayoutFullScreen).then(() => {
           console.info('Succeeded in setting the window layout to full-screen mode.');
         }).catch((err: BusinessError) => {
           console.error('Failed to setting the window layout. Cause: ' + JSON.stringify(err));
         });
         let sysBarProps: window.SystemBarProperties = {
           statusBarColor: '#ff00ff',
           navigationBarColor: '#00ff00',
           // The following two attributes are supported starting from API Version 8
           statusBarContentColor: '#ffffff',
           navigationBarContentColor: '#ffffff'
         };
         windowClass.setWindowSystemBarProperties(sysBarProps).then(() => {
           console.info('Succeeded in setting the system bar properties.');
         }).catch((err: BusinessError) => {
           console.error('Failed to setting the system bar properties. Cause: ' + JSON.stringify(err));
         });
       })
       // 3.Load the corresponding target page for the immersive window.
       windowStage.loadContent("pages/page2", (err) => {
         if (err.code) {
           console.error('Failed to load the content. Cause:' + JSON.stringify(err));
           return;
         }
         console.info('Succeeded in loading the content.');
       });
     }
   };
   ```
