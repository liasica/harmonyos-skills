---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-gesturehandlingresolution
title: Class (GestureHandlingResolution)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > Class (GestureHandlingResolution)
category: harmonyos-references
scraped_at: 2026-09-02T14:51:19+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0bbb98eb1dfb080cf314b8f26af64a2cffe3e839ff7ec62a92e37cbc2ca8128d
---

智慧手势处理结果声明类。

**起始版本：** 26.0.0

## constructor

constructor(isConsumed: boolean)

智慧手势处理结果的构造函数。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isConsumed | boolean | 是 | 是否消费当前智慧手势。  true表示消费当前智慧手势，此时如果未设置[selectedProposal](arkts-apis-uicontext-gesturehandlingresolution.md#属性)沿用系统默认动作处理，设置了[selectedProposal](arkts-apis-uicontext-gesturehandlingresolution.md#属性)以自定义动作处理。  false表示不消费，系统将本次智慧手势视为未处理。 |

## 属性

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isConsumed | boolean | 否 | 否 | 是否消费当前智慧手势。  true表示消费当前智慧手势，此时如果未设置selectedProposal沿用系统默认动作处理，设置了selectedProposal以自定义动作处理。  false表示不消费，系统将本次智慧手势视为未处理。 |
| selectedProposal | [BaseGestureHandlingProposal](arkts-apis-uicontext-basegesturehandlingproposal.md) | 否 | 是 | 用户指定的智慧手势处理行为。  当isConsumed为true时，如果未设置selectedProposal沿用系统默认动作处理，设置了selectedProposal以自定义动作处理。  当isConsumed为false时，selectedProposal设置不生效。 |
