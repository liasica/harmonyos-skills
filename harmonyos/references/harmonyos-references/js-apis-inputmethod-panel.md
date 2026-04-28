---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod-panel
title: @ohos.inputMethod.Panel (输入法面板)
breadcrumb: API参考 > 应用框架 > IME Kit（输入法开发服务） > ArkTS API > @ohos.inputMethod.Panel (输入法面板)
category: harmonyos-references
scraped_at: 2026-04-28T08:06:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a517d12120663909e32d6bfc2fdb2be6237a857c62878717f231d6ac869de927
---

本模块提供对输入法面板的属性管理。

说明

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { PanelInfo, PanelType, PanelFlag } from '@kit.IMEKit';
```

## PanelInfo

PhonePC/2in1TabletTVWearable

输入法面板属性信息。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [PanelType](js-apis-inputmethod-panel.md#paneltype) | 否 | 否 | 输入法面板类型。 |
| flag | [PanelFlag](js-apis-inputmethod-panel.md#panelflag) | 否 | 是 | 输入法面板状态类型。  - 默认值为固定态。  - 当前仅用于描述软键盘类型的面板的状态。 |

## PanelType

PhonePC/2in1TabletTVWearable

输入法面板类型枚举。

**系统能力**：SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SOFT\_KEYBOARD | 0 | 软键盘类型。 |
| STATUS\_BAR | 1 | 状态栏类型。 |

## PanelFlag

PhonePC/2in1TabletTVWearable

输入法面板状态类型枚举。

说明

目前仅用于SOFT\_KEYBOARD类型的面板。

**系统能力**：SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FLAG\_FIXED | 0 | 固定态面板类型。 |
| FLAG\_FLOATING | 1 | 悬浮态面板类型。 |
| FLAG\_CANDIDATE | 2 | 候选词态面板类型。  - 当输入面板为候选词态时，面板为显示用户输入候选词的窗口。  - 输入法服务不会主动控制候选词态面板的显示和隐藏，需要开发者根据情况自行控制。 |
