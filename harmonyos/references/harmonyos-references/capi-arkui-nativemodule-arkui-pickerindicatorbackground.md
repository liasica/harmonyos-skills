---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-pickerindicatorbackground
title: ArkUI_PickerIndicatorBackground
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_PickerIndicatorBackground
category: harmonyos-references
scraped_at: 2026-09-02T15:01:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5d289bd3c76a9e19a5e077f39919a4139b785a52123d219959214d03203eeada
---

```c
typedef struct {...} ArkUI_PickerIndicatorBackground
```

## 概述

选择器指示器背景的样式参数。用于设置选择器指示器背景样式的参数结构体；指示器背景样式以背景色和圆角高亮显示选择器的选中项，包括选中项背景颜色和圆角半径。

使用场景：

* 在选择器（Picker）组件中为选中项设置自定义背景样式，如音乐播放器中的歌曲列表选中背景。
* 在日期选择器中突出显示当前选中的日期或时间，提升用户体验。
* 在选项列表中为选中项添加圆角背景，增强视觉层次感。

**起始版本：** 23

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [picker.h](capi-picker-h.md)

**相关示例：** [native\_type\_sample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeType/native_type_sample)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t backgroundColor | 选中项背景的颜色。  默认值：0（完全透明，ARGB值为0x00000000，背景不可见）。  格式要求：0xAARRGGBB格式，第1个字节为透明度（00表示全透明，FF表示完全不透明），第2-4个字节分别为红、绿、蓝通道，例如**0xFF1122FF**。 |
| float topLeftRadius | 左上角圆角半径。  默认值：0  单位：vp  取值范围：取选中项的宽和高之中较小的边长为x，最大不超过x的一半。当取值小于0时，设置选择器指示器背景的样式参数失败；当取值大于最大值时，使用最大值。 |
| float topRightRadius | 右上角圆角半径。  默认值：0  单位：vp  取值范围：取选中项的宽和高之中较小的边长为x，最大不超过x的一半。当取值小于0时，设置选择器指示器背景的样式参数失败；当取值大于最大值时，使用最大值。 |
| float bottomLeftRadius | 左下角圆角半径。  默认值：0  单位：vp  取值范围：取选中项的宽和高之中较小的边长为x，最大不超过x的一半。当取值小于0时，设置选择器指示器背景的样式参数失败；当取值大于最大值时，使用最大值。 |
| float bottomRightRadius | 右下角圆角半径。  默认值：0  单位：vp  取值范围：取选中项的宽和高之中较小的边长为x，最大不超过x的一半。当取值小于0时，设置选择器指示器背景的样式参数失败；当取值大于最大值时，使用最大值。 |
