---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/start-flight-apps
title: 拉起航班类应用（startAbilityByType）
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Stage模型开发指导 > 应用间跳转 > 拉起指定类型的应用 > 拉起航班类应用（startAbilityByType）
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:51+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9690aedc51da13c648fb9230c399d0b54c5492d1a521d67a207c29f5cfdc8550
---

本章节介绍如何拉起航班类应用扩展面板。

例如，在行程安排类App中，当用户记录了某次行程的航班号，应用能够识别航班号信息并提供航班动态查询的链接。用户点击链接后，应用将通过调用[UIAbilityContext.startAbilityByType](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startabilitybytype11)或[UIExtensionContentSession.startAbilityByType](../harmonyos-references/js-apis-app-ability-uiextensioncontentsession.md#startabilitybytype11)接口，拉起航班类应用的扩展面板。面板上将展示设备上所有支持航班查询的应用，供用户选择并跳转至所需应用。

## 航班类应用扩展面板参数说明

startAbilityByType接口中type字段为flight，支持按航班号查询、按起降地查询两种意图场景，对应的wantParam参数如下：

* 按航班号查询场景

  | 参数名 | 类型 | 必填 | 说明 |
  | --- | --- | --- | --- |
  | sceneType | number | 否 | 意图场景，表明本次请求对应的操作意图。默认为1，按航班号查询场景填1或不填。 |
  | flightNo | string | 是 | 航班号，航司二位代码+数字。 |
  | departureDate | string | 否 | 航班出发时间：YYYY-MM-DD。 |
* 按起降地查询场景

  | 参数名 | 类型 | 必填 | 说明 |
  | --- | --- | --- | --- |
  | sceneType | number | 是 | 意图场景，表明本次请求对应的操作意图。按起降地查询场景填2。 |
  | originLocation | string | 是 | 出发地。 |
  | destinationLocation | string | 是 | 目的地。 |
  | departureDate | string | 否 | 航班出发时间：YYYY-MM-DD。 |

## 拉起方开发步骤

1. 导入相关模块。

   ```
   1. import { common } from '@kit.AbilityKit';
   ```
2. 构造接口参数并调用startAbilityByType接口。

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. @State hideAbility: string = 'hideAbility'

   6. build() {
   7. Row() {
   8. Column() {
   9. Text(this.hideAbility)
   10. .fontSize(30)
   11. .fontWeight(FontWeight.Bold)
   12. .onClick(() => {
   13. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   14. let wantParam: Record<string, Object> = {
   15. 'sceneType': 1,
   16. 'flightNo': 'ZH1509',
   17. 'departureDate': '2024-10-01'
   18. };
   19. let abilityStartCallback: common.AbilityStartCallback = {
   20. onError: (code: number, name: string, message: string) => {
   21. console.error(`onError code ${code} name: ${name} message: ${message}`);
   22. },
   23. onResult: (result) => {
   24. console.info(`onResult result: ${JSON.stringify(result)}`);
   25. }
   26. }

   28. context.startAbilityByType("flight", wantParam, abilityStartCallback,
   29. (err) => {
   30. if (err) {
   31. console.error(`startAbilityByType fail, err: ${JSON.stringify(err)}`);
   32. } else {
   33. console.info(`success`);
   34. }
   35. });
   36. });
   37. }
   38. .width('100%')
   39. }
   40. .height('100%')
   41. }
   42. }
   ```

   效果示例图：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/TzLz_sJaRzKYOg73-tEGlQ/zh-cn_image_0000002583437553.png?HW-CC-KV=V1&HW-CC-Date=20260427T233750Z&HW-CC-Expire=86400&HW-CC-Sign=14061CB45CED6219925EE614247ACB7ACDEABA9F170AB57F8EE37CFBB86EC87E)

## 目标方开发步骤

1. 在module.json5中配置[uris](module-configuration-file.md#skills标签)：

   1. 设置linkFeature属性以声明当前应用支持的特性功能，从而系统可以从设备已安装应用中找到当前支持该特性的应用，取值范围如下：

      | 取值 | 含义 |
      | --- | --- |
      | QueryByFlightNo | 声明应用支持按航班号查询航班。 |
      | QueryByLocation | 声明应用支持按起降地查询航班。 |
   2. 设置scheme、host、port、path/pathStartWith属性，与Want中URI相匹配，以便区分不同功能。

      ```
      1. {
      2. "abilities": [
      3. {
      4. "skills": [
      5. {
      6. "uris": [
      7. {
      8. "scheme": "flight",
      9. "host": "queryByFlightNo",
      10. "path": "",
      11. "linkFeature": "QueryByFlightNo"
      12. },
      13. {
      14. "scheme": "flight",
      15. "host": "queryByLocation",
      16. "path": "",
      17. "linkFeature": "QueryByLocation"
      18. }
      19. ]
      20. }
      21. ]
      22. }
      23. ]
      24. }
      ```
2. 解析参数并做对应处理。

   ```
   1. UIAbility.onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void
   ```

   在参数**want.uri**中会携带目标方配置的linkFeature对应的uri。

   在参数**want.parameters**中会携带Caller方传入的参数，不同场景参数如下所示

   * 按航班号查询场景

     | 参数名 | 类型 | 必填 | 说明 |
     | --- | --- | --- | --- |
     | flightNo | string | 是 | 航班号，航司二位代码+数字。 |
     | departureDate | string | 否 | 航班出发时间：YYYY-MM-DD。不填时，Target可按当天处理。 |
   * 按起降地查询场景

     | 参数名 | 类型 | 必填 | 说明 |
     | --- | --- | --- | --- |
     | originLocation | string | 是 | 出发地。 |
     | destinationLocation | string | 是 | 目的地。 |
     | departureDate | string | 否 | 航班出发时间：YYYY-MM-DD。不填时，Target可按当天处理。 |

   应用可根据[linkFeature](module-configuration-file.md#skills标签)中定义的特性功能，比如按航班号查询和按起降地查询，结合接收到的uri和参数开发不同的样式页面。

**完整示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { window } from '@kit.ArkUI';

5. const TAG = 'EntryAbility';

7. export default class EntryAbility extends UIAbility {
8. windowStage: window.WindowStage | null = null;

10. uri?: string;
11. flightNo?: string;
12. departureDate?: string;
13. originLocation?: string;
14. destinationLocation?: string;

16. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
17. hilog.info(0x0000, TAG, `onCreate, want=${JSON.stringify(want)}`);
18. super.onCreate(want, launchParam);
19. this.parseWant(want);
20. }

22. onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
23. hilog.info(0x0000, TAG, `onNewWant, want=${JSON.stringify(want)}`);
24. super.onNewWant(want, launchParam);
25. this.parseWant(want);
26. if (!this.windowStage) {
27. hilog.error(0x0000, TAG, 'windowStage is null');
28. this.context.terminateSelf();
29. return;
30. }
31. this.loadPage(this.windowStage);
32. }

34. private parseWant(want: Want): void {
35. this.uri = want.uri as string | undefined;
36. this.flightNo = want.parameters?.flightNo as string | undefined;
37. this.departureDate = want.parameters?.departureDate as string | undefined;
38. this.originLocation = want.parameters?.originLocation as string | undefined;
39. this.destinationLocation = want.parameters?.destinationLocation as string | undefined;
40. }

42. private loadPage(windowStage: window.WindowStage): void {
43. hilog.info(0x0000, TAG, `loadPage, uri=${this.uri}`);
44. if (this.uri === 'flight://queryByFlightNo') {
45. // 构建按航班号查询场景参数
46. const storage: LocalStorage = new LocalStorage({
47. "flightNo": this.flightNo,
48. "departureDate": this.departureDate
49. } as Record<string, Object>);
50. // 拉起按航班号查询页面
51. windowStage.loadContent('pages/QueryByFlightNoPage', storage)
52. } else if (this.uri === 'flight://queryByLocation') {
53. // 构建按起降地查询场景参数
54. const storage: LocalStorage = new LocalStorage({
55. "originLocation": this.originLocation,
56. "destinationLocation": this.destinationLocation,
57. "departureDate": this.departureDate
58. } as Record<string, Object>);
59. // 拉起按起降地查询页面
60. windowStage.loadContent('pages/QueryByLocationPage', storage)
61. } else {
62. // 默认拉起首页
63. windowStage.loadContent('pages/Index', (err) => {
64. if (err.code) {
65. hilog.error(0x0000, TAG, 'Failed to load the content. Cause: %{public}s',
66. JSON.stringify(err) ?? '');
67. return;
68. }
69. hilog.info(0x0000, TAG, 'Succeeded in loading the content.');
70. });
71. }
72. }

74. onDestroy(): void {
75. hilog.info(0x0000, TAG, `onDestroy`);
76. }

78. onWindowStageCreate(windowStage: window.WindowStage): void {
79. hilog.info(0x0000, TAG, `onWindowStageCreate`);
80. this.windowStage = windowStage;
81. this.loadPage(this.windowStage);
82. }

84. onWindowStageDestroy(): void {
85. hilog.info(0x0000, TAG, '%{public}s', 'Ability onWindowStageDestroy');
86. }

88. onForeground(): void {
89. hilog.info(0x0000, TAG, '%{public}s', 'Ability onForeground');
90. }

92. onBackground(): void {
93. hilog.info(0x0000, TAG, '%{public}s', 'Ability onBackground');
94. }
95. }
```
