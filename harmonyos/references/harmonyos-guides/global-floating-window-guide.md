---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/global-floating-window-guide
title: 全局悬浮窗开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 窗口类型 > 全局悬浮窗开发指导
category: harmonyos-guides
scraped_at: 2026-09-15T07:01:33+08:00
doc_updated_at: 2026-09-14
content_hash: sha256:f8c3a5bd0e7ac80cbd6fe955d06f381610e444d83ec4b8dd2613735f5f4b62b5
---

## 场景介绍

全局悬浮窗具有在应用主窗口退后台时，继续在前台显示的能力，适用于如多人视频通话、屏幕共享等场景。

全局悬浮窗的层级比所有应用主窗口、子窗口的层级高。

## 约束限制

全局悬浮窗当前仅支持在PC/2in1设备上使用。

## 前提条件

创建WindowType.TYPE\_FLOAT即全局悬浮窗类型的窗口，需要申请[ohos.permission.SYSTEM\_FLOAT\_WINDOW](restricted-permissions.md#ohospermissionsystem_float_window)权限，该权限为受控开放权限。申请方式请参考：[申请使用受限权限](declare-permissions-in-acl.md)。

**注意** 

如果应用未在应用市场（AGC）申请相应的权限证书，却试图在配置文件中声明此类权限，将会导致应用安装失败。

## 开发步骤

1. 创建全局悬浮窗。

   通过[window.createWindow()](../harmonyos-references/arkts-apis-window-f.md#windowcreatewindow9-1)接口创建全局悬浮窗类型（TYPE\_FLOAT）的窗口。

   ```typescript
   let floatWindowClass: window.Window | undefined = undefined;
   // ...
         // 1.创建全局悬浮窗。
         let context: common.UIAbilityContext | undefined = AppStorage.get<common.UIAbilityContext>('context');
         let config: window.Configuration = {
           name: 'floatWindow', windowType: window.WindowType.TYPE_FLOAT, ctx: context as common.BaseContext
         };
         window.createWindow(config, (err, data) => {
           if (err?.code) {
             console.error(`Failed to create the floatWindow. Cause code: ${err.code}, message: ${err.message}`);
             return;
           }
           floatWindowClass = data;
           console.info('Succeeded in creating the floatWindow. Data: ' + JSON.stringify(data));
           // ...
         });
   ```
2. 对全局悬浮窗进行属性设置等操作。

   全局悬浮窗创建成功后，可以改变其大小、位置等，还可以根据应用需要设置全局悬浮窗的背景色、亮度等属性。

   ```typescript
   // 2.全局悬浮窗窗口创建成功后，设置全局悬浮窗的位置、大小及相关属性等。
   floatWindowClass.moveWindowTo(100, 100, (err) => {
     if (err?.code) {
       console.error(`Failed to move the window. Cause code: ${err.code}, message: ${err.message}`);
       return;
     }
     console.info('Succeeded in moving the window.');
     if (!floatWindowClass) {
       console.error('float_windowClass is null');
       return;
     }
     floatWindowClass.resize(600, 900, (err) => {
       if (err?.code) {
         console.error(`Failed to change the window size. Cause code: ${err.code}, message: ${err.message}`);
         return;
       }
       console.info('Succeeded in changing the window size.');
     });
   });
   ```
3. 加载显示全局悬浮窗的具体内容。

   通过[setUIContent()](../harmonyos-references/arkts-apis-window-window.md#setuicontent9-1)和[showWindow()](../harmonyos-references/arkts-apis-window-window.md#showwindow9-1)接口加载显示全局悬浮窗的具体内容。

   ```typescript
   // 3.为全局悬浮窗加载对应的目标页面。
   floatWindowClass.setUIContent('pages/FloatWindow', (err) => {
     if (err?.code) {
       console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
       return;
     }
     console.info('Succeeded in loading the content.');
     // 显示全局悬浮窗。
     (floatWindowClass as window.Window).showWindow((err) => {
       if (err?.code) {
         console.error(`Failed to show the window. Cause code: ${err.code}, message: ${err.message}`);
         return;
       }
       console.info('Succeeded in showing the window.');
     });
   });
   ```
4. 销毁全局悬浮窗。

   当不再需要全局悬浮窗时，可根据具体实现逻辑，使用[destroyWindow()](../harmonyos-references/arkts-apis-window-window.md#destroywindow9-1)接口销毁全局悬浮窗。

   ```typescript
   // 4.销毁全局悬浮窗。当不再需要全局悬浮窗时，可根据具体实现逻辑，使用destroy对其进行销毁。
   floatWindowClass.destroyWindow((err) => {
     if (err?.code) {
       console.error(`Failed to destroy the window. Cause code: ${err.code}, message: ${err.message}`);
       return;
     }
     console.info('Succeeded in destroying the window.');
   });
   ```
