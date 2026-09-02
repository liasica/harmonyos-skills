---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-gesturestyle
title: OH_ArkUI_GestureStyle
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_GestureStyle
category: harmonyos-references
scraped_at: 2026-09-02T14:51:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:723f0a45583b8c54f06c105aebb051b34e4e2cd74bc64504d8dd943ebdb2354a
---

```c
typedef struct OH_ArkUI_GestureStyle OH_ArkUI_GestureStyle
```

## 概述

定义手势样式，适用于需要配置手势样式并接收相关事件回调的场景，便于应用统一管理手势样式及事件回调。

调用[OH\_ArkUI\_GestureStyle\_Create](capi-styled-string-h.md#oh_arkui_gesturestyle_create)接口创建对应的手势样式对象。

对象创建后调用OH\_ArkUI\_GestureStyle\_RegisterOnXXXCallback系列接口注册具体的事件回调，例如调用[OH\_ArkUI\_GestureStyle\_RegisterOnClickCallback](capi-styled-string-h.md#oh_arkui_gesturestyle_registeronclickcallback)注册点击事件回调。

使用完毕后，调用[OH\_ArkUI\_GestureStyle\_Destroy](capi-styled-string-h.md#oh_arkui_gesturestyle_destroy)接口销毁手势样式对象。

**起始版本：** 24

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [styled\_string.h](capi-styled-string-h.md)
