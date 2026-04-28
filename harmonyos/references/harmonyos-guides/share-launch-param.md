---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-launch-param
title: 判断应用是否被系统分享拉起
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 系统分享 > 目标应用处理分享内容 > 判断应用是否被系统分享拉起
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0d197b57de1dbd9f6a44318f60acd90da40506ade322e29ba61925fba9d17d24
---

从5.1.0(18)版本开始，支持应用判断是否被系统分享拉起。

作为目标应用接入系统分享时，当应用被拉起，需要判断本次启动原因是被系统分享拉起的，以便处理对应的分享业务。

* 通过[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)处理分享内容时，可使用[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)或[onNewWant](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)的[LaunchParam.launchReasonMessage](../harmonyos-references/js-apis-app-ability-abilityconstant.md#launchparam)字段是否为'ReasonMessage\_SystemShare'判断。
* 通过[UIExtensionAbility](../harmonyos-references/js-apis-app-ability-uiextensionability.md)处理分享内容时，可使用[onCreate](../harmonyos-references/js-apis-app-ability-uiextensionability.md#oncreate)的[LaunchParam.launchReasonMessage](../harmonyos-references/js-apis-app-ability-abilityconstant.md#launchparam)字段是否为'ReasonMessage\_SystemShare'判断。

## 示例代码

* 通过[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)处理分享内容。

  ```
  1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
  2. import { window } from '@kit.ArkUI';

  4. export default class ShareUIAbility extends UIAbility {
  5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  6. if (launchParam.launchReasonMessage === 'ReasonMessage_SystemShare') {
  7. // 识别为被系统分享拉起
  8. console.info('被拉起原因：系统分享');
  9. }
  10. }

  12. onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  13. if (launchParam.launchReasonMessage === 'ReasonMessage_SystemShare') {
  14. // 识别为被系统分享拉起
  15. console.info('被拉起原因：系统分享');
  16. }
  17. }

  19. onWindowStageCreate(windowStage: window.WindowStage): void {
  20. windowStage.loadContent('pages/ShareUIPage'); // 此路径仅为示例 请替换实际路径
  21. }
  22. }
  ```
* 通过[UIExtensionAbility](../harmonyos-references/js-apis-app-ability-uiextensionability.md)处理分享内容。

  ```
  1. import { AbilityConstant, ShareExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';

  3. export default class ShareExtAbility extends ShareExtensionAbility {
  4. onCreate(launchParam: AbilityConstant.LaunchParam): void {
  5. if (launchParam.launchReasonMessage === 'ReasonMessage_SystemShare') {
  6. // 识别为被系统分享拉起
  7. console.info('被拉起原因：系统分享');
  8. }
  9. }

  11. onSessionCreate(want: Want, session: UIExtensionContentSession) {
  12. session.loadContent('pages/ShareExtDialog'); // 此路径仅为示例 请替换实际路径
  13. }
  14. }
  ```
