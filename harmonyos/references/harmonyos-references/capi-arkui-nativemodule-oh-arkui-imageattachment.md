---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-imageattachment
title: OH_ArkUI_ImageAttachment
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_ImageAttachment
category: harmonyos-references
scraped_at: 2026-09-02T14:51:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2bb46f827a63f9ec2f30beeb1f3c009209410ccab0075511b428f0c5c4fed538
---

```c
typedef struct OH_ArkUI_ImageAttachment OH_ArkUI_ImageAttachment
```

## 概述

定义图片对象，用于在属性字符串中嵌入图片内容。图片作为属性字符串的组成部分，通过设置图片源及样式属性后，可附加到属性字符串中实现图文混排。

调用[OH\_ArkUI\_ImageAttachment\_Create](capi-styled-string-h.md#oh_arkui_imageattachment_create)接口创建图片样式对象。

调用[OH\_ArkUI\_ImageAttachment\_Destroy](capi-styled-string-h.md#oh_arkui_imageattachment_destroy)接口销毁图片样式对象。

对象创建后，调用OH\_ArkUI\_ImageAttachment\_SetXXX系列接口设置样式属性。例如调用[OH\_ArkUI\_ImageAttachment\_SetPixelMap](capi-styled-string-h.md#oh_arkui_imageattachment_setpixelmap)设置图片源。

**起始版本：** 24

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [styled\_string.h](capi-styled-string-h.md)
