---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-form-formeditextensionability
title: @ohos.app.form.FormEditExtensionAbility (FormEditExtensionAbility)
breadcrumb: API参考 > 应用框架 > Form Kit（卡片开发服务） > ArkTS API > @ohos.app.form.FormEditExtensionAbility (FormEditExtensionAbility)
category: harmonyos-references
scraped_at: 2026-04-28T08:06:01+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:7688973ff5d896a018258263fb30d8d4070a6f27d9399ea15af1bab053c2ebe1
---

FormEditExtensionAbility模块提供卡片编辑功能，继承自[UIExtensionAbility](js-apis-app-ability-uiextensionability.md)。

说明

本模块首批接口从API version 18开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { FormEditExtensionAbility } from '@kit.FormKit';
```

## FormEditExtensionAbility

PhonePC/2in1TabletTVWearable

提供卡片编辑功能。

### 属性

PhonePC/2in1TabletTVWearable

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [FormEditExtensionContext](js-apis-inner-application-formeditextensioncontext.md) | 否 | 否 | FormEditExtensionAbility的上下文环境，默认值是继承自UIExtensionContext的对象。 |
