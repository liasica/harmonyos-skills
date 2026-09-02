---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-checkbox-h
title: checkbox.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > checkbox.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:20+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:abecb772468e0db98b87701625158ba8205cd7d27042bfbde79c1b96a7d0eb74
---

## 概述

为NativeNode API提供Checkbox节点类型定义。

**引用文件：** <arkui/node\_attributes/checkbox.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**相关示例：** [NativeTypeSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeTypeSample)

## 汇总

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_CheckboxShape](capi-checkbox-h.md#arkui_checkboxshape) | ArkUI\_CheckboxShape | 定义Checkbox组件形状。 |

## 枚举类型说明

### ArkUI\_CheckboxShape

```c
enum ArkUI_CheckboxShape
```

**描述：**

定义Checkbox组件形状。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ArkUI\_CHECKBOX\_SHAPE\_CIRCLE = 0 | 圆形。 |
| ArkUI\_CHECKBOX\_SHAPE\_ROUNDED\_SQUARE = 1 | 圆角方形。 |
