---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-resolveduicontext
title: Class (ResolvedUIContext)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > Class (ResolvedUIContext)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:50+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:cd68bfbf95a5457c28b50df96fe379d461b7d7d87862e877da70f9b3252b1546
---

ResolvedUIContext用于表示通过[resolveUIContext](arkts-apis-uicontext-uicontext.md#resolveuicontext22)获取到的UIContext实例及其解析策略，适用于需要获取并识别UIContext来源策略的场景。

**说明** 

* 本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 示例效果请以真机运行为准，当前DevEco Studio预览器不支持。
* ResolvedUIContext继承自[UIContext](arkts-apis-uicontext-uicontext.md)，并新增strategy属性用于记录该UIContext实例的解析策略。
* 本模块接口仅可在Stage模型下使用。

## 属性

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| strategy | [ResolveStrategy](arkts-apis-uicontext-e.md#resolvestrategy22) | 否 | 否 | [UIContext](arkts-apis-uicontext-uicontext.md)的解析策略，用于标识[resolveUIContext](arkts-apis-uicontext-uicontext.md#resolveuicontext22)返回该UIContext实例时采用的解析规则。 |
