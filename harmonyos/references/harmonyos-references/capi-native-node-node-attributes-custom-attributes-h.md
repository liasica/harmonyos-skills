---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-node-attributes-custom-attributes-h
title: custom_attributes.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > custom_attributes.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:18+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8d03c73b84edd47322a8010947356c264ab6495b94dbb8373d388817e640365c
---

## 概述

为NativeNode API提供自定义组件的测量、布局和绘制事件类型定义，用于注册和处理测量、布局以及内容层、前景层和浮层的绘制事件。

**引用文件：** <arkui/node\_attributes/custom\_attributes.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**相关示例：** [native\_node\_sample](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/native_node_sample)

## 汇总

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_NodeCustomEventType](capi-native-node-node-attributes-custom-attributes-h.md#arkui_nodecustomeventtype) | ArkUI\_NodeCustomEventType | 定义自定义组件事件类型。 |

## 枚举类型说明

### ArkUI\_NodeCustomEventType

```c
enum ArkUI_NodeCustomEventType
```

**描述：**

定义自定义组件事件类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_MEASURE = 1 << 0 | 自定义测量类型。  **起始版本：** 12 |
| ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_LAYOUT = 1 << 1 | 自定义布局类型。  **起始版本：** 12 |
| ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_DRAW = 1 << 2 | 自定义内容层绘制类型。  **起始版本：** 12 |
| ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_FOREGROUND\_DRAW = 1 << 3 | 自定义前景绘制类型。  **起始版本：** 12 |
| ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_OVERLAY\_DRAW = 1 << 4 | 自定义浮层绘制类型。  **起始版本：** 12 |
| ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_DRAW\_FRONT = 1 << 5 | 自定义内容层前景绘制类型。  **起始版本：** 20 |
| ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_DRAW\_BEHIND = 1 << 6 | 自定义内容层背景绘制类型。  **起始版本：** 20 |
