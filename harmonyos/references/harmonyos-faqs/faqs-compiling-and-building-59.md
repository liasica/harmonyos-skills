---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-59
title: 如何处理include <stddef.h>编译报错
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何处理include <stddef.h>编译报错
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:20+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:025229c1d229a6560dd1efbb39d3dea325ab3845148a391fbdf5a80db88e55ef
---

**问题现象**

C语言代码中包含<stddef.h>时编译报错：

lib/clang/15.0.4/include/stddef. h:74:24: error: typedef redefinition with different types ('unsigned short" vs 'unsigned int")typedef*WCHAR\_TYPE* \_ wchar\_t;… 10/native/sysroot/us/include/aarch64-linux-ohos/bits/alltypes.h:15:18: note: previous definition is here typedef unsigned wchar\_t。

**解决措施**

在CMakeLists.txt中删除TARGET\_COMPILE\_OPTIONS内的参数-fshort-wchar。
