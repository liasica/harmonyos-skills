---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-startup-overview
title: 拉起指定应用概述
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Stage模型开发指导 > 应用间跳转 > 拉起指定应用 > 拉起指定应用概述
category: harmonyos-guides
scraped_at: 2026-04-29T13:25:49+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:5ec2250fc3d6c6ef2d93fb64cb9bdcfbb14deb8acbfc23f5ba67c461a5c5b6c3
---

本章节主要介绍如何通过应用链接跳转的方式拉起指定应用。

说明

从API 12开始，已不再推荐三方应用使用指定Ability方式（即显式Want）拉起其他应用。关于如何从指定Ability方式切换到指定[应用链接](app-startup-overview.md#应用链接)方式，详见[显式Want跳转切换应用链接跳转适配指导](uiability-startup-adjust.md)。

## 应用链接

应用链接是指可以将用户引导至应用内特定位置或相关网页的URL，常见的格式如下。更多关于应用链接格式与字段含义的说明，详见[应用链接说明](app-uri-config.md)。

```
1. scheme://host[:port]/path
```

## 运作机制

1. 目标应用在配置文件中注册自己的URL，并对外提供URL。
2. 拉起方应用在跳转接口中传入目标应用的URL等信息。
3. 系统接收到URL等相关信息，会寻找对应匹配项，并跳转至目标应用。

## 应用链接分类

按照应用链接的scheme以及校验机制的不同，可以分为Deep Linking与App Linking两种方式。

* **Deep Linking**：是一种通过链接跳转至应用特定页面的技术，其特点是支持开发者定义任意形式的scheme。由于缺乏域名校验机制，容易被其他应用所仿冒。
* **App Linking**：其限定了scheme必须为https，同时通过增加域名校验机制，可以从已匹配到的应用中筛选过滤出目标应用，消除应用查询和定位中产生的歧义，直达受信的目标应用。

相比Deep Linking，App Linking具有更高的安全性和可靠性，用户体验更佳。推荐开发者将App Linking作为首选方案。

| 类型 | App Linking（推荐） | Deep Linking |
| --- | --- | --- |
| 实现方案 | 目标应用需要在module.json5中声明应用链接；同时需要向系统注册域名并通过域名认证。 | 目标应用需要在module.json5中声明应用链接。 |
| 链接格式 | scheme必须为https。 | scheme可以自定义。通常不为https、http、file，否则会拉起默认的系统浏览器。 |
| 是否可用于分享或直接在网页中访问 | 可以 | 不可以，需在代码中调用。 |
| 是否可以直接拉起目标应用 | 可以 | 可以，但不推荐使用，存在被仿冒风险。 |

Deep Linking与App Linking均可以使用[openLink](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#openlink12)接口实现，不同条件下的跳转效果如下。

说明

该接口中的appLinkingOnly字段表示是否必须以App Linking的方式启动UIAbility，默认为false。appLinkingOnly为true一般只用于浏览器等应用。

| 应用链接类型 | App Linking（推荐） | Deep Linking |
| --- | --- | --- |
| appLinkingOnly为false且目标应用已安装 | 直接跳转打开目标应用。 | 跳转目标应用（如果有多个符合条件的应用时，展示应用选择弹框）。 |
| appLinkingOnly为false且目标应用未安装 | 跳转默认浏览器打开网页。 | 返回失败，系统不跳转，由应用自行处理；当前会展示“链接无法打开”弹框。 |
| appLinkingOnly为true且目标应用已安装 | 直接跳转打开目标应用。 | 返回失败，系统不跳转，由应用自行处理。 |
| appLinkingOnly为true且目标应用未安装 | 返回失败，系统不跳转由应用自行处理。 | 返回失败，系统不跳转，由应用自行处理。 |

通过App Linking方式拉起指定应用的示意图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/-4e3beLGTBi1APsAZ4NrcQ/zh-cn_image_0000002589323861.png?HW-CC-KV=V1&HW-CC-Date=20260429T052548Z&HW-CC-Expire=86400&HW-CC-Sign=975AEFCE7CDB73A9B5A760453DE1F9E2FEB23A6A141221FFFC989B01E64B2EAA)

通过Deep Linking方式拉起应用时，如果存在多个符合条件的应用，需要用户选择后方可跳转到指定应用。示意图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/v9waFtHNSTuwKQKwSCS8Tw/zh-cn_image_0000002589243799.png?HW-CC-KV=V1&HW-CC-Date=20260429T052548Z&HW-CC-Expire=86400&HW-CC-Sign=222CF9CE7D5E60C6C2EEE2F59BD5581FCEFB2FE8B77C3EF43DA39D1A5E28FF8F)

## FAQ

### 跨应用拉起UIAbility时，如何感知跳转弹框的用户选择结果

通过startAbility方式或Deep Linking方式拉起其他应用的UIAbility时，系统会弹出“是否允许跳转”的确认弹框，由用户进行选择。当前暂不支持获取用户操作结果，当用户取消跳转时，应用也无法感知。相关能力已纳入版本需求规划，请持续关注。

### 应用间跳转时如何取消“是否允许跳转”的确认弹框

通过[openLink](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#openlink12)或[startAbility](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)拉起其他应用时，为了防止应用的恶意跳转，系统会弹出“是否允许跳转”的确认弹框，由用户进行确认。不支持开发者取消该弹框。

说明

“是否允许跳转”的确认弹框实际显示的提示语由系统定义，比如“xx想要拉起xx”，此处仅为举例。

### 应用间跳转时如何取消“暂无可用打开方式”弹框

当通过[openLink](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#openlink12)或[startAbility](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)隐式启动其他应用时，如果没有找到匹配的应用，系统会弹框提示“暂无可用打开方式”。

* openLink方式启动其他应用：API version 21版本之前，不支持取消弹框提示。从API version 21版本开始，可以将OpenLinkOptions中的hideFailureTipDialog字段设置为true，取消弹框提示。

  示例如下：

  ```
  1. import { common, OpenLinkOptions, wantConstant, CompletionHandler, bundleManager } from '@kit.AbilityKit';
  2. import { hilog } from '@kit.PerformanceAnalysisKit';
  3. import { BusinessError } from '@kit.BasicServicesKit';

  5. const DOMAIN = 0xeeee;
  6. const TAG: string = '[openLinkDemo]';

  8. @Entry
  9. @Component
  10. struct Index {
  11. @State message: string = 'I am caller';

  13. build() {
  14. Row() {
  15. Column() {
  16. Text(this.message)
  17. .fontSize(50)
  18. .fontWeight(FontWeight.Bold)
  19. Button('start browser', { type: ButtonType.Capsule, stateEffect: true })
  20. .width('87%')
  21. .height('5%')
  22. .margin({ bottom: '12vp' })
  23. .onClick(() => {
  24. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  25. let link: string = 'https://www.example.com';
  26. let completionHandler: CompletionHandler = {
  27. onRequestSuccess: (elementName: bundleManager.ElementName, message: string): void => {
  28. console.info(`${elementName.bundleName}-${elementName.moduleName}-${elementName.abilityName} start succeeded: ${message}`);
  29. },
  30. onRequestFailure: (elementName: bundleManager.ElementName, message: string): void => {
  31. console.error(`${elementName.bundleName}-${elementName.moduleName}-${elementName.abilityName} start failed: ${message}`);
  32. }
  33. };
  34. let openLinkOptions: OpenLinkOptions = {
  35. appLinkingOnly: false,
  36. // hideFailureTipDialog字段需要在appLinkingOnly字段是false时才生效
  37. hideFailureTipDialog: true,
  38. parameters: {
  39. [wantConstant.Params.CONTENT_TITLE_KEY]: 'contentTitle',
  40. keyString: 'str',
  41. keyNumber: 200,
  42. keyBool: false,
  43. keyObj: {
  44. keyObjKey: 'objValue',
  45. }
  46. },
  47. completionHandler: completionHandler
  48. };
  49. try {
  50. context.openLink(
  51. link,
  52. openLinkOptions,
  53. (err, result) => {
  54. hilog.error(DOMAIN, TAG, `openLink callback error.code: ${JSON.stringify(err)}`);
  55. hilog.info(DOMAIN, TAG, `openLink callback result: ${JSON.stringify(result.resultCode)}`);
  56. hilog.info(DOMAIN, TAG, `openLink callback result data: ${JSON.stringify(result.want)}`);
  57. }
  58. ).then(() => {
  59. hilog.info(DOMAIN, TAG, `open link success.`);
  60. }).catch((err: BusinessError) => {
  61. hilog.error(DOMAIN, TAG, `open link failed, errCode: ${JSON.stringify(err.code)}`);
  62. });
  63. } catch (e) {
  64. hilog.error(DOMAIN, TAG, `open link failed, errCode: ${JSON.stringify(e.code)}`);
  65. }
  66. })
  67. }
  68. .width('100%')
  69. }
  70. .height('100%')
  71. }
  72. }
  ```
* startAbility隐式启动其他应用：可以通过将Want中的[flags字段](../harmonyos-references/js-apis-app-ability-wantconstant.md#flags)设置为FLAG\_START\_WITHOUT\_TIPS，取消弹框提示。

  示例如下：

  ```
  1. import { common, Want, wantConstant } from '@kit.AbilityKit';
  2. import { hilog } from '@kit.PerformanceAnalysisKit';
  3. import { BusinessError } from '@kit.BasicServicesKit';

  5. const TAG: string = '[Page_UIAbilityComponentsInteractive]';
  6. const DOMAIN_NUMBER: number = 0xFF00;

  8. @Entry
  9. @Component
  10. struct Page_UIAbilityComponentsInteractive {
  11. private context = this.getUIContext().getHostContext() as common.   UIAbilityContext;

  13. build() {
  14. Column() {
  15. // ...
  16. List({ initialIndex: 0 }) {
  17. ListItem() {
  18. Row() {
  19. // ...
  20. }
  21. .onClick(() => {
  22. // context为UIAbility对象的成员
  23. let wantInfo: Want = {
  24. deviceId: '', // deviceId为空表示本设备
  25. action: 'xxxx', // 隐式启动
  26. flags: wantConstant.Flags.FLAG_START_WITHOUT_TIPS,
  27. };
  28. // context为调用方UIAbility的UIAbilityContext
  29. this.context.startAbility(wantInfo).then(() => {
  30. hilog.info(DOMAIN_NUMBER, TAG, 'startAbility success.');
  31. }).catch((error: BusinessError) => {
  32. hilog.error(DOMAIN_NUMBER, TAG, 'startAbility failed.');
  33. });
  34. })
  35. }
  36. // ...
  37. }
  38. // ...
  39. }
  40. // ...
  41. }
  42. }
  ```
