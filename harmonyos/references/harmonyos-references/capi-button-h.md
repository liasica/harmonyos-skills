---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-button-h
title: button.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > button.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:20+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d923ad811b217772748d53ec340e8cc52786ee7378261bd6cc96fb8dac7811ae
---

## 概述

为NativeNode API提供Button节点类型定义。

**引用文件：** <arkui/node\_attributes/button.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**相关示例：** [NativeTypeSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeTypeSample)

## 汇总

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_ButtonType](capi-button-h.md#arkui_buttontype) | ArkUI\_ButtonType | 定义按钮样式枚举值。 |

## 枚举类型说明

### ArkUI\_ButtonType

```c
enum ArkUI_ButtonType
```

**描述：**

定义按钮样式枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_BUTTON\_TYPE\_NORMAL = 0 | 普通按钮，默认不带圆角。 |
| ARKUI\_BUTTON\_TYPE\_CAPSULE = 1 | 胶囊型按钮，圆角默认为高度的一半。 |
| ARKUI\_BUTTON\_TYPE\_CIRCLE = 2 | 圆形按钮。 |
| ARKUI\_BUTTON\_ROUNDED\_RECTANGLE = 8 | 圆角矩形按钮。  **起始版本：** 19 |
