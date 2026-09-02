---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-stringasyncevent
title: ArkUI_StringAsyncEvent
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_StringAsyncEvent
category: harmonyos-references
scraped_at: 2026-09-02T15:01:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:474eaff4c811539df079ae5f2db1ed8dea16340bfa925400a1a7f6aa111194b3
---

```c
typedef struct {...} ArkUI_StringAsyncEvent
```

## 概述

定义组件回调事件使用字符串参数的类型，用于在组件异步事件回调中传递字符串数据，适用于组件回调事件需要携带文本信息的场景。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_node.h](capi-native-node-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| const char\* pStr | 组件回调事件中传递的字符串数据。 |
