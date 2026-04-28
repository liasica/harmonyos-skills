---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pi-arkui-nativemodule-arkui-pickerindicatordivider
title: ArkUI_PickerIndicatorDivider
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_PickerIndicatorDivider
category: harmonyos-references
scraped_at: 2026-04-28T08:04:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0c724a95e174c700678e855c1d64159133714b2647b67ee7f8fd0027d9ec3b40
---

```
1. typedef struct {...} ArkUI_PickerIndicatorDivider
```

## 概述

PhonePC/2in1TabletTVWearable

分割线样式指示器的样式参数。

**起始版本：** 23

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_type.h](capi-native-type-h.md)

**相关示例：** [native\_type\_sample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeType/native_type_sample)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| float strokeWidth | 分割线的线宽。  默认值：0  单位：vp  取值范围：[0, 选中项高度的一半（即20vp）]。strokeWidth小于0时设置分割线样式指示器的样式参数失败，strokeWidth大于选中项高度的一半时使用2.0px。不支持“百分比”类型。 |
| uint32\_t dividerColor | 分割线的颜色。  默认值：0  取值范围：0xARGB格式，例如**0xFF1122FF**。 |
| float startMargin | 分割线与Picker容器侧边起始端的距离。  默认值：0  单位：vp  取值范围：startMargin与endMargin之和不得超过Picker容器的宽度。设置小于0时设置分割线样式指示器的样式参数失败，startMargin与endMargin之和超过Picker容器的宽度时，使用默认值。不支持“百分比”类型。 |
| float endMargin | 分割线与Picker容器侧边结束端的距离。  默认值：0  单位：vp  取值范围：startMargin与endMargin之和不得超过Picker容器的宽度。设置小于0时设置分割线样式指示器的样式参数失败，startMargin与endMargin之和超过Picker容器的宽度时，使用默认值。不支持“百分比”类型。 |
