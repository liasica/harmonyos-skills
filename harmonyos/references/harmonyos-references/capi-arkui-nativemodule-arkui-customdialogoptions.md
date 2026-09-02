---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-customdialogoptions
title: ArkUI_CustomDialogOptions
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_CustomDialogOptions
category: harmonyos-references
scraped_at: 2026-09-02T14:51:50+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e0864daf78be0d46051c63f14d8cafbb0e206835d8b5499c3dc6c7cb6e5d48a3
---

```c
typedef struct ArkUI_CustomDialogOptions ArkUI_CustomDialogOptions
```

## 概述

定义自定义弹窗的选项对象。该对象不暴露任何成员字段，开发者通过 [ArkUI\_NativeModule](capi-arkui-nativemodule.md) 中以 OH\_ArkUI\_CustomDialog\_Set 为前缀的接口（如设置背景、圆角、阴影、模糊、位置、模态等）配置弹窗属性，再调用 OH\_ArkUI\_CustomDialog\_OpenDialog 打开弹窗。

**起始版本：** 19

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_dialog.h](capi-native-dialog-h.md)
