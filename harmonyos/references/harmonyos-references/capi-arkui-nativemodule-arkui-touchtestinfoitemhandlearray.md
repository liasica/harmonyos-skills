---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-touchtestinfoitemhandlearray
title: ArkUI_TouchTestInfoItemArray
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_TouchTestInfoItemArray
category: harmonyos-references
scraped_at: 2026-09-02T14:51:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5f2c034bc5f12a636b4b4fef3d4671cdc3973d7d2b6dd41179172c77382bc8ed
---

```
typedef ArkUI_TouchTestInfoItemHandle* ArkUI_TouchTestInfoItemArray
```

## 概述

定义触摸测试信息项句柄数组，用于表示多个触摸测试信息项句柄。在触摸事件分发与测试过程中，可通过此数组类型统一管理和访问多个触摸测试结果，适用于需要同时处理多个触点测试信息的场景。

**起始版本：** 22

**相关模块：** [ArkUI\_EventModule](capi-arkui-eventmodule.md)

**所在头文件：** [ui\_input\_event.h](capi-ui-input-event-h.md)
