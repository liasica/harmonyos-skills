---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-dialogdismissevent
title: ArkUI_DialogDismissEvent
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_DialogDismissEvent
category: harmonyos-references
scraped_at: 2026-09-02T14:51:50+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7a8de23402c2625ef3e00b95ac68040699d8501e31725fddaf42aeedebd1d4a5
---

```c
typedef struct ArkUI_DialogDismissEvent ArkUI_DialogDismissEvent
```

## 概述

定义弹窗关闭事件对象，用于在弹窗被关闭时通知开发者，适用于需要监听弹窗关闭事件的场景。该事件对象采用回调机制，当弹窗触发关闭操作时，系统会创建并传递此事件对象到开发者注册的回调函数中，开发者可通过该对象获取关闭原因、设置是否拦截关闭或传递自定义数据。该事件对象不暴露内部成员，需通过对应的接口（如 OH\_ArkUI\_DialogDismissEvent\_SetShouldBlockDismiss、OH\_ArkUI\_DialogDismissEvent\_GetUserData、OH\_ArkUI\_DialogDismissEvent\_GetDismissReason）获取或设置相关信息。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_dialog.h](capi-native-dialog-h.md)
