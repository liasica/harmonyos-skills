---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-windmana-troubleshooting-0001
title: 应用所有页面不允许截图和录屏
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 故障排查 > 应用所有页面不允许截图和录屏
category: harmonyos-faqs
scraped_at: 2026-10-15T07:14:28+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:82f7ccd0a8ba49a33804be60de7dbfc2e941ec86a953ecc07f0b9859bfbf8815
---

## 问题现象

应用所有页面不允许截屏和录屏，并提醒用户涉及隐私。

## 定位过程

1. 检查是否设置了主窗口为隐私模式。

   EntryAbility.ets文件的[onWindowStageCreate](../harmonyos-references/js-apis-app-ability-uiability.md#onwindowstagecreate)回调中使用了window.setWindowPrivacyMode(true)方法，设置了隐私模式，此时就是主窗口隐私模式，适用于整个应用都防截屏的场景。
2. 如果是进入页面开启隐私模式，离开页面取消，则检查在离开页面时是否取消隐私模式。例如：进入页面时在onPageShow()中获取当前窗口对象并设置隐私模式，退出页面时在onPageHide()生命周期中取消隐私模式。

## 分析结论

1. 设置了主窗口隐私模式。
2. 进入页面开启隐私模式，离开页面时未取消。

## 修改建议

如果是设置了主窗口隐私模式，整个应用是防截屏的，建议按照如下方式实现：

进入页面开启隐私模式，离开页面取消。

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
