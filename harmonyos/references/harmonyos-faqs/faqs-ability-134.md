---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-134
title: 应用退到后台再打开时，页面会回到首页
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 应用退到后台再打开时，页面会回到首页
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-07-31
content_hash: sha256:ab9007dcb44c1a5ac227bd56da76bcec565b8f29e0e3275817c869068f07b0f4
---

## 问题现象

应用打开后，点击切换到其他页面，退出到后台，再通过桌面图标打开，会重新启动回到首页。

## 背景知识

* [启动指定页面](../lite-wearable-guides/start-page.md)：应用在默认模式下都是单例模式，当应用已经启动，后续点击图标，会调用UIAbility的onNewWant生命周期回调。
* [UIAbility组件生命周期](../harmonyos-guides/uiability-lifecycle.md)：用户在执行应用启动、应用前后台切换、应用退出等操作时，系统会触发相关应用组件的生命周期回调。UIAbility的生命周期回调都支持重载，开发者可以根据业务需要在重载回调时，加载和更新资源和数据等，实现自己的业务逻辑。

## 问题定位

1. 通过日志分析，当应用切到后台，再次点击图标启动时，在onNewWant回调里触发了onWindowStageCreate的回调。

   ```screen
   20016-20016   C04200/com.exa...owSessionImpl   com.exa...demo        I     (1965)OnNewWant: Window
   8153-8153     A00000/com.exa...demo/testTag    hidumper              I     Ability onWindowStageCreate
   20016-20016   C01332/com.exa...demo/UIAbility  com.exa...demo        I     [js_ui_ability.cpp:1401]end, name: onNewWant, time: 1
   ```
2. 对比其他正常的应用，onNewWant不会触发onWindowStageCreate回调。
3. 编写Demo，重载onNewWant，并在其中调用onWindowStageCreate，问题复现。

   错误效果的演示代码：

   ```screen
   export default class EntryAbility extends UIAbility {
     windowStage: window.WindowStage | null = null;
     // onCreate等回调重载略
     onWindowStageCreate(windowStage: window.WindowStage): void {
       this.windowStage = windowStage;
       windowStage.loadContent('pages/Index', (err) => {
         // ...
       });
     }
     // 此处调用onWindowStageCreate会复现问题所述的效果
     onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam) {
       if (this.windowStage) {
         this.onWindowStageCreate(this.windowStage);
       }
     }
   ```

## 分析结论

应用在onNewWant回调里调用了onWindowStageCreate，当应用在后台再次启动时，会重新加载启动页面，导致该问题。

## 修改建议

参考官方文档中[onNewWant](../harmonyos-guides/uiability-lifecycle.md#onnewwant)的用法，仅在onNewWant里更新数据和资源，而不调用onWindowStageCreate接口。
