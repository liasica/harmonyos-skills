---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-pickerindicatordivider
title: ArkUI_PickerIndicatorDivider
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_PickerIndicatorDivider
category: harmonyos-references
scraped_at: 2026-09-02T15:01:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8bb1a1137639b74f3e2b3eb3f3f613860e951ea66a857d74f626033942da4992
---

```c
typedef struct {...} ArkUI_PickerIndicatorDivider
```

## 概述

用于定义分割线样式指示器的样式参数，支持自定义分割线的线宽、颜色以及与容器侧边的距离，适用于需要美化Picker控件分割线外观的场景。开发者可通过配置该结构体实现个性化分割线效果，提升UI界面的美观度和用户体验。

**起始版本：** 23

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [picker.h](capi-picker-h.md)

**相关示例：** [native\_type\_sample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeType/native_type_sample)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| float strokeWidth | 分割线的线宽。  默认值：0  单位：vp  取值范围：[0, 选中项高度的一半（即20vp）]。  小于0时设置失败，大于选中项高度的一半时使用默认值0。不支持百分比类型。 |
| uint32\_t dividerColor | 分割线的颜色。  默认值：0（表示全透明颜色，分割线不可见）  格式要求：0xARGB格式，例如**0xFF1122FF**。未设置颜色时使用默认值。 |
| float startMargin | 分割线与Picker容器侧边起始端的距离。  默认值：0  单位：vp  取值范围：startMargin与endMargin之和不得超过Picker容器的宽度。  小于0时设置失败。startMargin与endMargin之和超过容器宽度时使用默认值0。不支持百分比类型。 |
| float endMargin | 分割线与Picker容器侧边结束端的距离。  默认值：0  单位：vp  取值范围：startMargin与endMargin之和不得超过Picker容器的宽度。  小于0时设置失败。startMargin与endMargin之和超过容器宽度时使用默认值0。不支持百分比类型。 |
