---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-handlescope--8h
title: JSVM_HandleScope__*
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_HandleScope__*
category: harmonyos-references
scraped_at: 2026-04-28T08:19:28+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:688347dd53febc174dbc20718a7d5ad5f486f29507154113c27319b3cd5076a8
---

```
1. typedef struct JSVM_HandleScope__* JSVM_HandleScope
```

## 概述

PhonePC/2in1TabletWearable

表示JavaScript值的作用域，用于控制和修改在特定范围内创建的对象的生命周期。通常，JSVM-API值是在JSVM\_HandleScope的上下文中创建的。当从JavaScript调用native方法时，将存在默认JSVM\_HandleScope。如果用户没有显式创建新的JSVM\_HandleScope，将在默认JSVM\_HandleScope中创建JSVM-API值。对于native方法执行之外的任何代码调用（例如，在libuv回调调用期间），模块需要在调用任何可能导致创建JavaScript值的函数之前创建一个作用域。JSVM\_HandleScope是使用OH\_JSVM\_OpenHandleScope创建的，并使用OH\_JSVM\_CloseHandleScope销毁的。关闭作用域代表向GC指示在JSVM\_HandleScope作用域的生命周期内创建的所有JSVM\_Value将不再从当前堆的栈帧中引用。

**起始版本：** 11

**相关模块：** [JSVM](capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](capi-jsvm-types-h.md)
