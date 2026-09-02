---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-textcontroller
title: OH_ArkUI_TextController
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_TextController
category: harmonyos-references
scraped_at: 2026-09-02T14:51:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:24f82bef858d05b1e068e0869d5392eec8aa368c080a7533dd9d74c1b669846e
---

```c
typedef struct OH_ArkUI_TextController OH_ArkUI_TextController
```

## 概述

定义文本组件的控制器，用于在Native侧对文本组件进行控制和交互。可通过[OH\_ArkUI\_TextController\_Create](capi-text-h.md#oh_arkui_textcontroller_create)创建控制器对象，创建后必须在使用完毕后调用[OH\_ArkUI\_TextController\_Destroy](capi-text-h.md#oh_arkui_textcontroller_destroy)接口销毁对象以释放资源，二者必须成对使用，否则会导致内存泄漏。创建控制器后，可使用[OH\_ArkUI\_TextController\_SetStyledString](capi-native-type-h.md#oh_arkui_textcontroller_setstyledstring)等接口设置文本组件的属性字符串，实现对文本内容的动态管理和样式控制。适用于需要在Native层操作文本组件的场景。

**起始版本：** 26.0.0

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [text.h](capi-text-h.md)
