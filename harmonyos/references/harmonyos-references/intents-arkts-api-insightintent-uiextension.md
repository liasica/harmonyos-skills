---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/intents-arkts-api-insightintent-uiextension
title: InsightIntentUIExtensionAbility (意图调用UI扩展能力)
breadcrumb: API参考 > AI > Intents Kit（意图框架服务） > ArkTS API > InsightIntentUIExtensionAbility (意图调用UI扩展能力)
category: harmonyos-references
scraped_at: 2026-04-28T08:18:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8a49305e610c7cf104a55ecabfb40ff13959d56e59b2760274801d451e4cb142
---

InsightIntentUIExtensionAbility用于小艺对话过程中的意图调用时的信息展示，为意图调用UI扩展能力，应用可以声明一个或多个InsightIntentUI来展示其意图的窗口化界面，继承自[UIExtensionAbility](js-apis-app-ability-uiextensionability.md)。

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1Tablet

```
1. import { InsightIntentUIExtensionAbility } from '@kit.IntentsKit';
```

## InsightIntentUIExtensionAbility

PhonePC/2in1Tablet

**模型约束：** 该类仅可在Stage模型下使用。

**系统能力：** SystemCapability.AI.InsightIntent

**起始版本：** 5.0.0(12)

## 示例

PhonePC/2in1Tablet

```
1. import { InsightIntentUIExtensionAbility } from '@kit.IntentsKit';
2. import { UIExtensionContentSession, Want } from '@kit.AbilityKit';

4. // 此处以TestUiExtAbility继承InsightIntentUIExtensionAbility为例
5. export default class TestUiExtAbility extends InsightIntentUIExtensionAbility {
6. onCreate() {
7. }

9. onForeground() {
10. }

12. onBackground() {
13. }

15. onDestroy() {
16. }

18. onSessionCreate(want: Want, session: UIExtensionContentSession) {
19. }

21. onSessionDestroy(session: UIExtensionContentSession) {
22. }
23. }
```
