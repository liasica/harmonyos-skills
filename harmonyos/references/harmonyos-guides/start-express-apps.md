---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/start-express-apps
title: 拉起快递类应用（startAbilityByType）
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Stage模型开发指导 > 应用间跳转 > 拉起指定类型的应用 > 拉起快递类应用（startAbilityByType）
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:75ca03043361c1dd545ce08dc8b2cfb5d3b5bbeffcacadf2e87f1d12cc23770c
---

本章节介绍如何拉起快递类应用扩展面板。

例如，在消息类App中，用户收到快递单号，应用能够识别快递单号信息并提供快递查询的链接。用户点击链接后，应用将通过调用[UIAbilityContext.startAbilityByType](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startabilitybytype11)或[UIExtensionContentSession.startAbilityByType](../harmonyos-references/js-apis-app-ability-uiextensioncontentsession.md#startabilitybytype11)接口，拉起快递类应用的扩展面板。面板上将展示设备上所有支持快递查询的应用，供用户选择并跳转至所需应用。

## 快递类应用扩展面板参数说明

startAbilityByType接口中type字段为express，支持查询快递意图，对应的wantParam参数如下：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sceneType | number | 否 | 意图场景，表明本次请求对应的操作意图。默认为1，查询快递填场景填1或不填。 |
| expressNo | string | 是 | 快递单号。 |

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
   4. @State hideAbility: string = 'hideAbility';

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
   16. 'expressNo': 'SF123456'
   17. };
   18. let abilityStartCallback: common.AbilityStartCallback = {
   19. onError: (code: number, name: string, message: string) => {
   20. console.error(`onError code ${code} name: ${name} message: ${message}`);
   21. },
   22. onResult: (result) => {
   23. console.info(`onResult result: ${JSON.stringify(result)}`);
   24. }
   25. }

   27. context.startAbilityByType("express", wantParam, abilityStartCallback,
   28. (err) => {
   29. if (err) {
   30. console.error(`startAbilityByType fail, err: ${JSON.stringify(err)}`);
   31. } else {
   32. console.info(`success`);
   33. }
   34. });
   35. });
   36. }
   37. .width('100%')
   38. }
   39. .height('100%')
   40. }
   41. }
   ```

   效果示例图：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/opAuWANRR-yEiSMuAfMiPw/zh-cn_image_0000002552957508.png?HW-CC-KV=V1&HW-CC-Date=20260427T233750Z&HW-CC-Expire=86400&HW-CC-Sign=36321663084AD374355F34C44149414C29BE57A7AEE2FB99228FE6B743444A17)

## 目标方开发步骤

1. 在module.json5中配置[uris](module-configuration-file.md#skills标签)：

   1. 设置linkFeature属性以声明当前应用支持的特性功能，从而系统可以从设备已安装应用中找到当前支持该特性的应用，取值范围如下：

      | 取值 | 含义 |
      | --- | --- |
      | QueryExpress | 声明应用支持快递查询。 |
   2. 设置scheme、host、port、path/pathStartWith属性，与Want中URI相匹配，以便区分不同功能。

      ```
      1. {
      2. "abilities": [
      3. {
      4. "skills": [
      5. {
      6. "uris": [
      7. {
      8. "scheme": "express",
      9. "host": "queryExpress",
      10. "path": "",
      11. "linkFeature": "QueryExpress"
      12. }
      13. ]
      14. }
      15. ]
      16. }
      17. ]
      18. }
      ```
2. 解析参数并做对应处理。

   ```
   1. UIAbility.onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void
   ```

   在参数**want.uri**中会携带目标方配置的linkFeature对应的uri。

   在参数**want.parameters**中会携带Caller方传入的参数，如下所示：

   | 参数名 | 类型 | 必填 | 说明 |
   | --- | --- | --- | --- |
   | expressNo | string | 是 | 快递单号。 |

**完整示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { window } from '@kit.ArkUI';

5. const TAG = 'EntryAbility';

7. export default class EntryAbility extends UIAbility {
8. windowStage: window.WindowStage | null = null;

10. uri?: string;
11. expressNo?: string;

13. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
14. hilog.info(0x0000, TAG, `onCreate, want=${JSON.stringify(want)}`);
15. super.onCreate(want, launchParam);
16. this.parseWant(want);
17. }

19. onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
20. hilog.info(0x0000, TAG, `onNewWant, want=${JSON.stringify(want)}`);
21. super.onNewWant(want, launchParam);
22. this.parseWant(want);
23. if (!this.windowStage) {
24. hilog.error(0x0000, TAG, 'windowStage is null');
25. this.context.terminateSelf();
26. return;
27. }
28. this.loadPage(this.windowStage);
29. }

31. private parseWant(want: Want): void {
32. this.uri = want.uri as string | undefined;
33. this.expressNo = want.parameters?.expressNo as string | undefined;
34. }

36. private loadPage(windowStage: window.WindowStage): void {
37. hilog.info(0x0000, TAG, `loadPage, uri=${this.uri}`);
38. if (this.uri === 'express://queryExpress') {
39. // 构建快递查询参数
40. const storage: LocalStorage = new LocalStorage({
41. "expressNo": this.expressNo
42. } as Record<string, Object>);
43. // 拉起快递查询页面
44. windowStage.loadContent('pages/QueryExpressPage', storage)
45. } else {
46. // 默认拉起首页
47. windowStage.loadContent('pages/Index', (err) => {
48. if (err.code) {
49. hilog.error(0x0000, TAG, 'Failed to load the content. Cause: %{public}s',
50. JSON.stringify(err) ?? '');
51. return;
52. }
53. hilog.info(0x0000, TAG, 'Succeeded in loading the content.');
54. });
55. }
56. }

58. onDestroy(): void {
59. hilog.info(0x0000, TAG, `onDestroy`);
60. }

62. onWindowStageCreate(windowStage: window.WindowStage): void {
63. hilog.info(0x0000, TAG, `onWindowStageCreate`);
64. this.windowStage = windowStage;
65. this.loadPage(this.windowStage);
66. }

68. onWindowStageDestroy(): void {
69. hilog.info(0x0000, TAG, '%{public}s', 'Ability onWindowStageDestroy');
70. }

72. onForeground(): void {
73. hilog.info(0x0000, TAG, '%{public}s', 'Ability onForeground');
74. }

76. onBackground(): void {
77. hilog.info(0x0000, TAG, '%{public}s', 'Ability onBackground');
78. }
79. }
```
