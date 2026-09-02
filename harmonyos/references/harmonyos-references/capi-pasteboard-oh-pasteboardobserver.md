---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboardobserver
title: OH_PasteboardObserver
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > OH_PasteboardObserver
category: harmonyos-references
scraped_at: 2026-09-02T14:52:31+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3faa4ddc8595ec2a19ba2ad2e815cb0a09a6c0c6f3d6f73d05656b95deaf1fae
---

```c
typedef struct OH_PasteboardObserver OH_PasteboardObserver
```

## 概述

定义剪贴板数据变更观察者。用于监听系统剪贴板数据的变化事件，当剪贴板内容发生更新时，通过回调通知应用。典型使用场景：需要响应剪贴板内容变化的应用。

**起始版本：** 13

**相关模块：** [Pasteboard](capi-pasteboard.md)

**所在头文件：** [oh\_pasteboard.h](capi-oh-pasteboard-h.md)
