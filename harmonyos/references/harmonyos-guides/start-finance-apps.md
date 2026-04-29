---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/start-finance-apps
title: 拉起金融类应用（startAbilityByType）
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Stage模型开发指导 > 应用间跳转 > 拉起指定类型的应用 > 拉起金融类应用（startAbilityByType）
category: harmonyos-guides
scraped_at: 2026-04-29T13:25:53+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ef8c0ad76d53393563730532aa86fedde3cdaaf1edfde77f5b2511fca3942a82
---

本章节介绍如何拉起金融类应用扩展面板。

## 金融类应用扩展面板参数说明

startAbilityByType接口中type字段为finance，对应的wantParam参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sceneType | number | 否 | 意图场景，表明本次请求对应的操作意图。1：转账汇款 2：信用卡还款。默认为1 |
| bankCardNo | string | 否 | 银行卡卡号 |

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
   16. "bankCardNo": '123456789'
   17. };
   18. let abilityStartCallback: common.AbilityStartCallback = {
   19. onError: (code: number, name: string, message: string) => {
   20. console.error(`onError code ${code} name: ${name} message: ${message}`);
   21. },
   22. onResult: (result) => {
   23. console.info(`onResult result: ${JSON.stringify(result)}`);
   24. }
   25. }

   27. context.startAbilityByType("finance", wantParam, abilityStartCallback,
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/wDE4Mc7hSMaafOn7ZEifYQ/zh-cn_image_0000002558604342.png?HW-CC-KV=V1&HW-CC-Date=20260429T052552Z&HW-CC-Expire=86400&HW-CC-Sign=7513A9D5689CAAE52EED8375EA0016D977674D382D6DDF2099209036FB71EEDC)

## 目标方开发步骤

1. 在module.json5中配置[uris](module-configuration-file.md#skills标签)，步骤如下：

   1. 设置linkFeature属性以声明当前应用支持的特性功能，从而系统可以从设备已安装应用中找到当前支持该特性的应用，取值范围如下：

      | 取值 | 含义 |
      | --- | --- |
      | Transfer | 声明应用支持转账汇款功能 |
      | CreditCardRepayment | 声明应用支持信用卡还款功能 |
   2. 设置scheme、host、port、path/pathStartWith属性，与Want中URI相匹配，以便区分不同功能。

   ```
   1. {
   2. "abilities": [
   3. {
   4. "skills": [
   5. {
   6. "uris": [
   7. {
   8. "scheme": "finance", // 这里仅示意，应用需确保这里声明的uri能被外部正常拉起
   9. "host": "transfer",
   10. "path": "",
   11. "linkFeature": "Transfer" // 声明应用支持转账汇款功能
   12. },
   13. {
   14. "scheme": "finance", // 这里仅示意，应用需确保这里声明的uri能被外部正常拉起
   15. "host": "credit_card_repayment",
   16. "path": "",
   17. "linkFeature": "CreditCardRepayment" // 声明应用支持信用卡还款功能
   18. }
   19. ]
   20. }
   21. ]
   22. }
   23. ]
   24. }
   ```
2. 解析面板传过来的参数并做对应处理。

   ```
   1. UIAbility.onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void
   ```

   在参数**want.uri**中会携带目标方配置的linkFeature对应的uri。

   在参数**want.parameters**中会携带Caller方传入的参数，如下表所示：

   | 参数名 | 类型 | 必填 | 说明 |
   | --- | --- | --- | --- |
   | bankCardNo | string | 否 | 银行卡卡号 |

   应用可根据[linkFeature](module-configuration-file.md#skills标签)中定义的特性功能，比如转账汇款和信用卡还款，结合接收到的uri开发不同的样式页面。

**完整示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { window } from '@kit.ArkUI';

5. const TAG = 'EntryAbility';

7. export default class EntryAbility extends UIAbility {
8. windowStage: window.WindowStage | null = null;

10. uri?: string;
11. bankCardNo?: string;

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
33. this.bankCardNo = want.parameters?.bankCardNo as string | undefined;
34. }

36. private loadPage(windowStage: window.WindowStage): void {
37. hilog.info(0x0000, TAG, `loadPage, uri=${this.uri}`);
38. if (this.uri === 'finance://transfer') {
39. // 构建转账场景参数
40. const storage: LocalStorage = new LocalStorage({
41. "bankCardNo": this.bankCardNo
42. } as Record<string, Object>);
43. // 拉起转账页面
44. windowStage.loadContent('pages/TransferPage', storage)
45. } else if (this.uri === 'finance://credit_card_repayment') {
46. // 构建信用卡还款场景参数
47. const storage: LocalStorage = new LocalStorage({
48. "bankCardNo": this.bankCardNo
49. } as Record<string, Object>);
50. // 拉起信用卡还款页面
51. windowStage.loadContent('pages/CreditCardRepaymentPage', storage)
52. } else {
53. // 默认拉起首页
54. windowStage.loadContent('pages/Index', (err) => {
55. if (err.code) {
56. hilog.error(0x0000, TAG, 'Failed to load the content. Cause: %{public}s',
57. JSON.stringify(err) ?? '');
58. return;
59. }
60. hilog.info(0x0000, TAG, 'Succeeded in loading the content.');
61. });
62. }
63. }

65. onDestroy(): void {
66. hilog.info(0x0000, TAG, `onDestroy`);
67. }

69. onWindowStageCreate(windowStage: window.WindowStage): void {
70. hilog.info(0x0000, TAG, `onWindowStageCreate`);
71. this.windowStage = windowStage;
72. this.loadPage(this.windowStage);
73. }

75. onWindowStageDestroy(): void {
76. hilog.info(0x0000, TAG, '%{public}s', 'Ability onWindowStageDestroy');
77. }

79. onForeground(): void {
80. hilog.info(0x0000, TAG, '%{public}s', 'Ability onForeground');
81. }

83. onBackground(): void {
84. hilog.info(0x0000, TAG, '%{public}s', 'Ability onBackground');
85. }
86. }
```
