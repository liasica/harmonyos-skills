---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/intents-arkts-api-insightintent-uiextension
title: InsightIntentUIExtensionAbility (意图调用UI扩展能力)
breadcrumb: API参考 > AI > Intents Kit（意图框架服务） > ArkTS API > InsightIntentUIExtensionAbility (意图调用UI扩展能力)
category: harmonyos-references
scraped_at: 2026-09-02T14:53:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9b61a2b7168717adf53f4cdf90cd7aa1252a2aeeffc2c342a121d3509b7162c5
---

InsightIntentUIExtensionAbility用于小艺对话过程中的意图调用时的信息展示，为意图调用UI扩展能力，应用可以声明一个或多个InsightIntentUI来展示其意图的窗口化界面，继承自[UIExtensionAbility](js-apis-app-ability-uiextensionability.md)。

**起始版本：** 5.0.0(12)

## 导入模块

```typescript
import { InsightIntentUIExtensionAbility } from '@kit.IntentsKit';
```

## InsightIntentUIExtensionAbility

**模型约束：** 该类仅可在Stage模型下使用。

**系统能力：** SystemCapability.AI.InsightIntent

**起始版本：** 5.0.0(12)

**示例：**

```typescript
import { InsightIntentUIExtensionAbility } from '@kit.IntentsKit';
import { UIExtensionContentSession, Want } from '@kit.AbilityKit';

const TAG: string = 'TestUiExtAbility';

// 此处以TestUiExtAbility继承InsightIntentUIExtensionAbility为例
export default class TestUiExtAbility extends InsightIntentUIExtensionAbility {
  onCreate() {
    console.info(TAG, `onCreate`);
  }
  onForeground() {
    console.info(TAG, `onForeground`);
  }
  onBackground() {
    console.info(TAG, `onBackground`);
  }
  onDestroy() {
    console.info(TAG, `onDestroy`);
  }
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
      console.info(TAG, `onSessionCreate, want: ${JSON.stringify(want)}`);
      session.loadContent('pages/Index');
  }
  onSessionDestroy(session: UIExtensionContentSession) {
    console.info(TAG, `onSessionDestroy`);
  }
}
```
