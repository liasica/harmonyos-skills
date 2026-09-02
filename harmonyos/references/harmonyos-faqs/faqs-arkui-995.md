---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-995
title: PC上如何实现全局悬浮窗效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > PC上如何实现全局悬浮窗效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-07-02
content_hash: sha256:4f7d286c7d0caa88a1d1551ade880d78757dee0e29a660d979c42b4bdf1dc611
---

## 问题现象

在PC上如何实现全局悬浮窗的效果？

## 背景知识

* [startAbility](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)方法：启动一个UIAbility。使用callback异步回调。仅支持在主线程调用。
* [resize](../harmonyos-references/arkts-apis-window-window.md#resize9-1)方法：基于窗口左上角顶点改变当前窗口大小，使用Promise异步回调。
* [setWindowDecorVisible](../harmonyos-references/arkts-apis-window-window.md#setwindowdecorvisible11)方法：设置窗口标题栏是否可见。
* [setWindowTitleButtonVisible](../harmonyos-references/arkts-apis-window-window.md#setwindowtitlebuttonvisible14)方法：设置标题栏上最大化、最小化、关闭按钮是否可见。
* [setWindowTopmost](../harmonyos-references/arkts-apis-window-window.md#setwindowtopmost14)方法：将窗口置于其他应用窗口之上不被遮挡。使用该接口需要配置权限：[ohos.permission.WINDOW\_TOPMOST](../harmonyos-guides/permissions-for-all.md#ohospermissionwindow_topmost)。
* 窗口不响应拖拽到屏幕边缘最大化、分屏等效果：应用配置文件[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中的[abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)中设置supportWindowMode属性，可参考[应用声明支持智慧多窗](../harmonyos-guides/multi-window-support.md)。

## 解决方案

实现悬浮窗有设置全局悬浮窗和多开Ability窗口这两种方案。

方法一：可以参考官方文档[全局悬浮窗开发指导](../harmonyos-guides/global-floating-window-guide.md)，需要申请受限权限[ohos.permission.SYSTEM\_FLOAT\_WINDOW](../harmonyos-guides/restricted-permissions.md#ohospermissionsystem_float_window)。

方法二：使用多开Ability的方案，拉起新的Ability窗口，悬浮窗口需要满足如下特点：无窗口标签栏；无最大化、最小化、关闭窗口按钮；悬浮窗口保持全局置顶效果；主窗口最小化之后，悬浮窗口不跟随最小化；悬浮窗口不响应拖拽到屏幕边缘最大化、分屏等效果。

1. 新建独立窗口的代码src/main/ets/pages/pageTwo.ets并在配置文件src/main/resources/base/profile/main\_pages.json中新增路径：

   ```ts
   @Entry
   @Component
   struct PageTwo {
     build() {
       Column() {
         Text('Float Window')
           .width('100%')
           .height('100%')
           .fontSize(30)
           .textAlign(TextAlign.Center)
       }
     }
   }
   ```

   ```json
   {
     "src": [
       "pages/Index",
       "pages/pageTwo"
     ]
   }
   ```
2. 在src/main/module.json5中配置窗口全局置顶权限：

   ```json
   "requestPermissions": [
     {
       "name": "ohos.permission.WINDOW_TOPMOST"
     }
   ],
   ```
3. 新增文件src/main/ets/entryability/FloatWindowAbility.ets，声明FloatWindowAbility类，继承自UIAbility，在接口[onWindowStageCreate](../harmonyos-guides/uiability-lifecycle.md#onwindowstagecreate)中[loadContent](../harmonyos-references/arkts-apis-window-windowstage.md#loadcontent9)之后获取主窗口对象。对该窗口设置标题栏不可见，最大化、最小化、关闭按钮不可见，设置窗口全局置顶等属性：

   ```ts
   export default class FloatWindowAbility extends UIAbility {
     private async resizeWindow(win: window.Window, width: number, height: number): Promise<void> {
       try {
         await win.resize(width, height);
         console.info('Succeeded in resizing window.');
       } catch (err) {
         console.error(`resize window failed: <${err.code}>${err.message}`);
       }
     }

     private setDecorVisible(win: window.Window, isVisible: boolean) {
       try {
         win.setWindowDecorVisible(isVisible);
         console.info('set window decor visible success.');
       } catch (err) {
         console.error(`set window decor visible failed: <${err.code}>${err.message}`);
       }
     }

     private setTitleButtonVisible(win: window.Window, isMaxVisible: boolean,
       isMinVisible: boolean, isCloseVisible?: boolean) {
       try {
         win.setWindowTitleButtonVisible(isMaxVisible, isMinVisible, isCloseVisible);
         console.info('set window title button visible success.');
       } catch (err) {
         console.error(`set window title button visible failed: <${err.code}>${err.message}`);
       }
     }

     private async setTopmost(win: window.Window, isWindowTopmost: boolean): Promise<void> {
       try {
         await win.setWindowTopmost(isWindowTopmost);
         console.info('set window topmost success.');
       } catch (err) {
         console.error(`set window topmost failed: <${err.code}>${err.message}`);
       }
     }

     onWindowStageCreate(windowStage: window.WindowStage): void {
       // 加载主窗口对应的页面。
       windowStage.loadContent('pages/pageTwo', () => {
         let mainWindow: window.Window | undefined = undefined;
         // 获取应用主窗口。
         windowStage.getMainWindow().then(async (data: window.Window) => {
           if (!data) {
             return;
           }
           mainWindow = data;
           // 设置窗口大小
           await this.resizeWindow(mainWindow, 200, 100);
           // 设置窗口标题可见
           this.setDecorVisible(mainWindow, false);
           // 设置窗口最大化、最小化、关闭按钮可见
           this.setTitleButtonVisible(mainWindow, false, false, false);
           // 设置窗口置顶
           await this.setTopmost(mainWindow, true);
         }).catch((err: BusinessError) => {
           if (err.code) {
             console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
           }
         });
       });
     }
   }
   ```
4. 在应用配置文件src/main/module.json5的abilities属性中，新增FloatWindowAbility配置项以及supportWindowMode属性为floating：

   ```json
   {
     "name": "FloatWindowAbility",
     "srcEntry": "./ets/entryability/FloatWindowAbility.ets",
     "description": "$string:EntryAbility_desc",
     "icon": "$media:layered_image",
     "label": "$string:EntryAbility_label",
     "supportWindowMode": ["floating"],
     "startWindowIcon": "$media:startIcon",
     "startWindowBackground": "$color:start_window_background",
     "exported": true,
     "skills": [
       {
         "entities": [
           "entity.system.home"
         ],
         "actions": [
           "ohos.want.action.home"
         ]
       }
     ]
   }
   ```
5. 在主界面配置拉起FloatWindowAbility窗口按钮：

   ```ts
   import { common, Want } from '@kit.AbilityKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   @Entry
   @Component
   struct Index {
     private abilityContext: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

     build() {
       Column({ space: 20 }) {
         Button('拉起悬浮窗')
           .onClick(() => {
             let want: Want = {
               // 此处需要根据实际包名进行更改
               bundleName: 'com.example.myapplication',
               abilityName: 'FloatWindowAbility',
               moduleName: 'entry',
             };
             this.abilityContext?.startAbility(want)
               .then(() => {
                 console.info('start ability success');
               }).catch((error: BusinessError) => {
               console.error(`start ability failed, code: ${error.code}, message: ${error.message}`);
             });
           })
       }
       .width('100%')
       .height('100%')
       .justifyContent(FlexAlign.Center)
     }
   }
   ```
