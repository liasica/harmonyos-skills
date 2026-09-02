---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1484
title: 防截屏功能实现及判断窗口是否允许截屏
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 防截屏功能实现及判断窗口是否允许截屏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a8bdab8079d9f5973cb9896bb256c7c01fb65366d49c6bdb7bb28829af30d257
---

## 问题现象

应用内隐私内容防止截屏是一个非常常见的功能，本文将对如何实现防截屏，以及如何判断应用内某窗口是否允许截屏进行详细阐述。

## 背景知识

* [@ohos.window（窗口）](../harmonyos-references/js-apis-window.md)：窗口提供管理窗口的一些基础能力，包括对当前窗口的创建、销毁、各属性设置，以及对各窗口间的管理调度。
* [setWindowPrivacyMode](../harmonyos-references/arkts-apis-window-window.md#setwindowprivacymode9)：设置窗口是否为隐私模式，使用callback异步回调。设置为隐私模式的窗口，窗口内容将无法被截屏或录屏。此接口可用于禁止截屏/录屏的场景。
* [声明权限](../harmonyos-guides/declare-permissions.md)：应用在申请权限时，需要在项目的配置文件中，逐个声明需要的权限，否则应用将无法获取授权。
* [onFocus](../harmonyos-references/ts-universal-focus-event.md#onfocus)：当前组件获取焦点时触发的回调。
* [onBlur](../harmonyos-references/ts-universal-focus-event.md#onblur)：当前组件失去焦点时触发的回调。
* [window.getLastWindow](../harmonyos-references/arkts-apis-window-f.md#windowgetlastwindow9)：获取当前应用内层级最高的子窗口，若无应用子窗口或子窗口未调用showWindow()进行显示，则返回应用主窗口。
* [getWindowProperties](../harmonyos-references/arkts-apis-window-window.md#getwindowproperties9)：获取当前窗口的属性。
* [onPageShow](../harmonyos-references/ts-custom-component-lifecycle.md#onpageshow)：router路由页面（即[@Entry](../harmonyos-guides/arkts-create-custom-components.md#entry)装饰的自定义组件）每次显示时触发一次，包括路由跳转、应用进入前台等场景。
* [onPageHide](../harmonyos-references/ts-custom-component-lifecycle.md#onpagehide)：router路由页面（即@Entry装饰的自定义组件）每次隐藏时触发一次，包括路由跳转、应用进入后台等场景。

## 解决方案

* 方案一：设置主窗口为隐私模式，可参考[如何实现防截屏功能](faqs-arkui-3.md)中的方式二。
* 方案二：针对单个页面需要设置隐私模式，可以在进入页面开启隐私模式，离开页面取消，具体步骤如下。
  1. 在module.json5文件中配置权限[ohos.permission.PRIVACY\_WINDOW](../harmonyos-guides/permissions-for-all.md#ohospermissionprivacy_window)，示例代码如下：

     ```json
     "requestPermissions": [
       {
         "name": "ohos.permission.PRIVACY_WINDOW"
       }
     ],
     ```
  2. 配置WindowUtils工具类用于封装设置隐私模式的逻辑，示例代码如下：

     ```ts
     import window from '@ohos.window';
     import common from '@ohos.app.ability.common';
     import { BusinessError } from '@kit.BasicServicesKit';

     export class windowUtils {
       static setWindowPrivacyModeInPage(context: common.UIAbilityContext, isFlag: boolean) {
         window.getLastWindow(context).then((lastWindow) => {
           lastWindow.setWindowPrivacyMode(isFlag, (err: BusinessError) => {
             const errCode: number = err.code;
             if (errCode) {
               console.error('Failed to set the window to privacy mode. Cause:' + JSON.stringify(err));
               return;
             }
             console.info('Succeeded in setting the window to privacy mode.');
           });
         });
       }
     }
     ```
  3. 进入页面时在onPageShow中获取当前窗口对象并设置隐私模式，退出页面时在onPageHide生命周期中取消隐私模式即可，并且通过getLastWindow获取当前窗口，通过getWindowProperties方法获取当前窗口的isPrivacyMode，来判断窗口是否允许截屏，示例代码如下：

     ```ts
     import common from '@ohos.app.ability.common';
     import { windowUtils } from './WindowUtils';
     import { window } from '@kit.ArkUI';

     @Entry
     @Component
     struct Index {
       onPageShow(): void {
         windowUtils.setWindowPrivacyModeInPage(this.getUIContext().getHostContext() as common.UIAbilityContext, true);
       }
       onPageHide() {
         windowUtils.setWindowPrivacyModeInPage(this.getUIContext().getHostContext() as common.UIAbilityContext, false);
       }
       build() {
         Row() {
           Column() {
             Button('获取当前屏幕是否可截图状态')
               .fontSize(20)
               .onClick(() => {
                 window.getLastWindow(this.getUIContext().getHostContext()).then(win => {
                   console.info(`win.getWindowProperties().isPrivacyMode:${win.getWindowProperties().isPrivacyMode}`);
                 });
               });
           }
           .width('100%');
         }
         .height('100%');
       }
     }
     ```

## 总结

以上两种设置防截屏功能的方案各有其应用场景，总结如下：

| 防截屏方案 | 优点 | 缺点 | 应用场景 |
| --- | --- | --- | --- |
| 设置主窗口为隐私模式 | 在onWindowStageCreate中设置，整个应用的主窗口都会进入隐私模式，安全性更高。 | 全局设置不够灵活，无法按页面粒度控制。 | 适用于整个应用都需防截屏的场景（如金融类应用）。 |
| 进入页面开启隐私模式，离开页面取消 | 可以在组件中调用windowUtils.setWindowPrivacyModeInPage，实现页面级别的控制。 | window.getLastWindow可能只获取当前页面的窗口，不适用于多窗口防截屏的场景 | 适用于某些页面需要防截屏的场景（如密码输入、支付界面），也可根据组件状态动态切换隐私模式。 |

## 常见FAQ

Q：密码输入界面设置了隐私防截屏为什么不生效？

A：可从以下几个场景排查：

1. 检查module.json5文件中是否配置ohos.permission.PRIVACY\_WINDOW权限。
2. 确认设置防截屏的地方是否执行。常见的场景是放在了组件的onPageShow里，而该生命周期没被执行。
3. 检查是否两个页面防截屏设置相互冲突。A跳转B时，在A隐藏时设置了取消防截屏。在B展示时，设置了开启防截屏。但结果A的取消防截屏操作在B开启防截屏操作之后执行。

Q：在禁止截图/录屏的情况下进行截图/录屏操作时，弹出的提示框在未升级前是toast提示，升级到5.0.1.130后，弹出新的警告弹窗（[AlertDialog](../harmonyos-references/ts-methods-alert-dialog-box.md#alertdialog)），请问是130版本新特性吗？

A：不是版本新特性。升级后的禁止截屏/录屏提示仍为toast提示没有新的警告弹窗。
