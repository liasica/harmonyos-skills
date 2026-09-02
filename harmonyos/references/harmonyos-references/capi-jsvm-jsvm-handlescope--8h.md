---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-handlescope--8h
title: JSVM_HandleScope__*
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_HandleScope__*
category: harmonyos-references
scraped_at: 2026-09-02T14:53:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8c648319f3a76c6627aca18fa0938eb6440d9a2bf5d3264fe6e8b8352e4e121f
---

```c
typedef struct JSVM_HandleScope__* JSVM_HandleScope
```

## 概述

表示JavaScript值的作用域，用于控制和修改在特定范围内创建的对象的生命周期。通常，JSVM-API值是在JSVM\_HandleScope的上下文中创建的。当从JavaScript调用native方法时，将存在默认JSVM\_HandleScope。如果用户没有显式创建新的JSVM\_HandleScope，将在默认JSVM\_HandleScope中创建JSVM-API值。对于native方法执行之外的任何代码调用（例如，在libuv回调调用期间），模块需要在调用任何可能导致创建JavaScript值的函数之前创建一个作用域。JSVM\_HandleScope是使用OH\_JSVM\_OpenHandleScope创建的，并使用OH\_JSVM\_CloseHandleScope销毁的。关闭作用域代表向GC指示在JSVM\_HandleScope作用域的生命周期内创建的所有JSVM\_Value将不再从当前堆的栈帧中引用。

**配对调用：** 必须成对调用OH\_JSVM\_OpenHandleScope()和OH\_JSVM\_CloseHandleScope()，每次调用OH\_JSVM\_OpenHandleScope()后，必须在使用完毕后调用OH\_JSVM\_CloseHandleScope()释放资源。

**违反后果：** 如果忘记调用OH\_JSVM\_CloseHandleScope()，会导致内存泄漏和资源无法释放。

**使用场景：** 在Native方法中创建JSVM-API值，在libuv回调等非native方法执行期间调用可能创建JavaScript值的函数，需要精确控制JavaScript对象生命周期。

**收益：** 避免内存泄漏：通过作用域管理对象生命周期，防止不必要的内存占用。提高GC效率：明确指示GC哪些对象可被回收，减少垃圾回收开销。

**系统能力：** SystemCapability.ArkCompiler.JSVM

**起始版本：** 11

**相关模块：** [JSVM](capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](capi-jsvm-types-h.md)
