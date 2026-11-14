---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-sec-panel-back
title: 分享详情页关闭分享面板
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 系统分享 > 目标应用处理分享内容 > 分享详情页关闭分享面板
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:32+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:d65343fedf6799e8ce3a2ef72a166173ec451586992303d8ec56ac0c2924ed09
---

从分享详情页返回分享面板时，可通过设置resultCode值为特定的[ShareAbilityResultCode](../harmonyos-references/share-system-share.md#shareabilityresultcode)，以告知分享面板做出不同的处理，具体处理方式如下：

* ERROR：返回分享面板，并提示用户发生错误。
* BACK：正常返回分享面板。
* CLOSE：关闭分享面板。

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { ShareExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
   import { systemShare } from '@kit.ShareKit';
   ```
2. 目标应用可以通过terminateSelfWithResult接口，设置resultCode值为systemShare.ShareAbilityResultCode.CLOSE，以关闭分享面板。

   ```typescript
   export default class TestShareAbility extends ShareExtensionAbility {
     onSessionCreate(want: Want, session: UIExtensionContentSession) {
       session.terminateSelfWithResult({
         resultCode: systemShare.ShareAbilityResultCode.CLOSE
       });
     }
   }
   ```
