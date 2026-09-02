---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-launch-param
title: 判断应用是否被系统分享拉起
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 系统分享 > 目标应用处理分享内容 > 判断应用是否被系统分享拉起
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:27eb76318bcbcaf294855334535289c3e32062cffaa7492aeda2ede0a707cd16
---

从5.1.0(18)版本开始，支持应用判断是否被系统分享拉起。

作为目标应用接入系统分享时，当应用被拉起，需要判断本次启动原因是被系统分享拉起的，以便处理对应的分享业务。

* 通过[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)处理分享内容时，可使用[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)或[onNewWant](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)的[LaunchParam.launchReasonMessage](../harmonyos-references/js-apis-app-ability-abilityconstant.md#launchparam)字段是否为'ReasonMessage\_SystemShare'判断。
* 通过[UIExtensionAbility](../harmonyos-references/js-apis-app-ability-uiextensionability.md)处理分享内容时，可使用[onCreate](../harmonyos-references/js-apis-app-ability-uiextensionability.md#oncreate)的[LaunchParam.launchReasonMessage](../harmonyos-references/js-apis-app-ability-abilityconstant.md#launchparam)字段是否为'ReasonMessage\_SystemShare'判断。

## 示例代码

* 通过[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)处理分享内容。

  ```typescript
  import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
  import { window } from '@kit.ArkUI';

  export default class ShareUIAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
      if (launchParam.launchReasonMessage === 'ReasonMessage_SystemShare') {
        // 识别为被系统分享拉起
        console.info('被拉起原因：系统分享');
      }
    }

    onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
      if (launchParam.launchReasonMessage === 'ReasonMessage_SystemShare') {
        // 识别为被系统分享拉起
        console.info('被拉起原因：系统分享');
      }
    }

    onWindowStageCreate(windowStage: window.WindowStage): void {
      windowStage.loadContent('pages/ShareUIPage'); // 此路径仅为示例 请替换实际路径
    }
  }
  ```
* 通过[UIExtensionAbility](../harmonyos-references/js-apis-app-ability-uiextensionability.md)处理分享内容。

  ```typescript
  import { AbilityConstant, ShareExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';

  export default class ShareExtAbility extends ShareExtensionAbility {
    onCreate(launchParam: AbilityConstant.LaunchParam): void {
      if (launchParam.launchReasonMessage === 'ReasonMessage_SystemShare') {
        // 识别为被系统分享拉起
        console.info('被拉起原因：系统分享');
      }
    }

    onSessionCreate(want: Want, session: UIExtensionContentSession) {
      session.loadContent('pages/ShareExtDialog'); // 此路径仅为示例 请替换实际路径
    }
  }
  ```
