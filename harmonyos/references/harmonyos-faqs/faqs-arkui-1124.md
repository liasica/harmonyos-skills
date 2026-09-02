---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1124
title: 应用所有页面不允许截图和录屏
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 应用所有页面不允许截图和录屏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:13+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:197fb52cdc76b53b81e4eb4b772203339cc33f1e870cfa282b712d9b28f06e1f
---

## 问题现象

应用所有页面不允许截屏和录屏，并提醒用户涉及隐私。

## 背景知识

* [@ohos.window（窗口）](../harmonyos-references/arkts-apis-window.md)：窗口提供管理窗口的一些基础能力，包括对当前窗口的创建、销毁、各属性设置，以及对各窗口间的管理调度。
* [setWindowPrivacyMode](../harmonyos-references/arkts-apis-window-window.md#setwindowprivacymode9-1)：设置窗口是否为隐私模式，使用callback异步回调。设置为隐私模式的窗口，窗口内容将无法被截屏或录屏。此接口可用于禁止截屏/录屏的场景。
* [声明权限](../harmonyos-guides/declare-permissions.md)：应用在申请权限时，需要在项目的配置文件中，逐个声明需要的权限，否则应用将无法获取授权。

## 问题定位

1. 检查是否设置了主窗口为隐私模式。EntryAbility.ets文件的[onWindowStageCreate](../harmonyos-references/js-apis-app-ability-uiability.md#onwindowstagecreate)回调中使用了window.setWindowPrivacyMode(true)方法，设置了隐私模式，此时就是主窗口隐私模式，适用于整个应用都防截屏的场景。
2. 如果是进入页面开启隐私模式，离开页面取消，则检查在离开页面时是否取消隐私模式。例如：进入页面时在onPageShow()中获取当前窗口对象并设置隐私模式，退出页面时在onPageHide()生命周期中取消隐私模式。

## 分析结论

1. 设置了主窗口隐私模式。
2. 进入页面开启隐私模式，离开页面时未取消。

## 修改建议

如果是设置了主窗口隐私模式，整个应用是防截屏的，建议按照如下方式实现：进入页面开启隐私模式，离开页面取消。

1. 在module.json5文件中配置权限ohos.permission.PRIVACY\_WINDOW。
2. 配置WindowUtils工具类用于封装设置隐私模式的逻辑，示例代码如下：

   ```ts
   export class windowUtils {
     static setWindowPrivacyModeInPage(context: common.UIAbilityContext, isFlag: boolean) {
       window.getLastWindow(context).then((lastWindow) => {
         lastWindow.setWindowPrivacyMode(isFlag);
       });
     }
   }
   ```
3. 进入页面时在onPageShow()中获取当前窗口对象并设置隐私模式，退出页面时在onPageHide()生命周期中取消隐私模式即可，示例代码如下：

   ```ts
   import { window } from '@kit.ArkUI';
   import { common } from '@kit.AbilityKit';

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
         }
         .width('100%');
       }
       .height('100%');
     }
   }
   ```
