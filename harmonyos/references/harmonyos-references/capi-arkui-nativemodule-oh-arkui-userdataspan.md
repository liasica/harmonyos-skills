---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-userdataspan
title: OH_ArkUI_UserDataSpan
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_UserDataSpan
category: harmonyos-references
scraped_at: 2026-09-02T14:51:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:872fbcb35972d829725c4a1e77fb0a2fdf7b2cf1c0ac0ebb388791192e1815c2
---

```c
typedef struct OH_ArkUI_UserDataSpan OH_ArkUI_UserDataSpan
```

## 概述

定义用户数据Span样式，用于在富文本中为属性字符串附加自定义用户数据，以便在文本交互或自定义渲染时进行数据标识与关联。例如，在即时通讯应用中可为消息文本Span附加消息ID，在富文本编辑器中可为文本片段附加自定义样式标签等场景中使用。

调用[OH\_ArkUI\_UserDataSpan\_Create](capi-styled-string-h.md#oh_arkui_userdataspan_create)接口创建用户数据Span样式对象。

使用完毕后应调用[OH\_ArkUI\_UserDataSpan\_Destroy](capi-styled-string-h.md#oh_arkui_userdataspan_destroy)接口销毁用户数据Span样式对象。

创建成功后，可调用[OH\_ArkUI\_UserDataSpan\_SetUserData](capi-styled-string-h.md#oh_arkui_userdataspan_setuserdata)接口设置用户数据。

调用[OH\_ArkUI\_UserDataSpan\_GetUserData](capi-styled-string-h.md#oh_arkui_userdataspan_getuserdata)接口获取用户数据。

**起始版本：** 24

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [styled\_string.h](capi-styled-string-h.md)
