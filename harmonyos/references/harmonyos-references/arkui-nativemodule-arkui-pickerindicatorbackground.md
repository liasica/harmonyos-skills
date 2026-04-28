---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkui-nativemodule-arkui-pickerindicatorbackground
title: ArkUI_PickerIndicatorBackground
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_PickerIndicatorBackground
category: harmonyos-references
scraped_at: 2026-04-28T08:04:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7fd20ca128976ea86e4672dcb3f7138541b8cfc228d2b3c2ab6dbfcbf5d08d9a
---

```
1. typedef struct {...} ArkUI_PickerIndicatorBackground
```

## 概述

PhonePC/2in1TabletTVWearable

背景样式指示器的样式参数。

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
| uint32\_t backgroundColor | 选中项背景的颜色。  默认值：0  取值范围：0xARGB格式，例如**0xFF1122FF**。 |
| float topLeftRadius | 左上角圆角半径。  默认值：0  单位：vp  取值范围：取选中项的宽和高之中较小的边长为x，最大不超过x的一半。当取值小于0时，设置背景样式指示器的样式参数失败；当取值大于最大值时，使用最大值。 |
| float topRightRadius | 右上角圆角半径。  默认值：0  单位：vp  取值范围：取选中项的宽和高之中较小的边长为x，最大不超过x的一半。当取值小于0时，设置背景样式指示器的样式参数失败；当取值大于最大值时，使用最大值。 |
| float bottomLeftRadius | 左下角圆角半径。  默认值：0  单位：vp  取值范围：取选中项的宽和高之中较小的边长为x，最大不超过x的一半。当取值小于0时，设置背景样式指示器的样式参数失败；当取值大于最大值时，使用最大值。 |
| float bottomRightRadius | 右下角圆角半径。  默认值：0  单位：vp  取值范围：取选中项的宽和高之中较小的边长为x，最大不超过x的一半。当取值小于0时，设置背景样式指示器的样式参数失败；当取值大于最大值时，使用最大值。 |
