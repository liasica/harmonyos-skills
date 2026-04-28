---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod-subtype
title: @ohos.InputMethodSubtype (输入法子类型)
breadcrumb: API参考 > 应用框架 > IME Kit（输入法开发服务） > ArkTS API > @ohos.InputMethodSubtype (输入法子类型)
category: harmonyos-references
scraped_at: 2026-04-28T08:06:06+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:6b1c85ff8893469846967064e3ac6b30c00c9a55d4342f0e667ffcc836a56a9b
---

本模块提供对输入法子类型的属性管理。输入法子类型允许输入法根据需要显示不同的输入模式或语言，完成模式或语言切换，如：输入法的中文/英文键盘等均属于输入法的子类型。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { InputMethodSubtype } from '@kit.IMEKit';
```

## InputMethodSubtype

PhonePC/2in1TabletTVWearable

输入法子类型属性。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| label | string | 是 | 是 | 非必填。输入法子类型的标签。 |
| labelId10+ | number | 是 | 是 | 非必填。输入法子类型的标签资源号。 |
| name | string | 是 | 否 | 必填。输入法子类型所属应用的包名。 |
| id | string | 是 | 否 | 必填。输入法子类型的id。 |
| mode | 'upper' | 'lower' | 是 | 是 | 非必填。输入法子类型的模式，包括upper（大写）和lower（小写）。 |
| locale | string | 是 | 否 | 必填。输入法子类型的方言版本。 |
| language | string | 是 | 否 | 必填。 输入法子类型的语言。 |
| icon | string | 是 | 是 | 非必填。输入法子类型的图标，可以通过iconId查询获取。预留字段，暂不支持使用。 |
| iconId | number | 是 | 是 | 非必填。输入法子类型的图标id。 |
| extra | object | 否 | 是 | 必填。输入法子类型的其他信息。  说明：  - 从API version 10开始为非必填参数。  - 预留字段，当前无具体含义，暂不支持使用。 |
