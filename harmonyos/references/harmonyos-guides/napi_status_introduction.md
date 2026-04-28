---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/napi_status_introduction
title: Node-API接口返回状态码介绍
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API接口返回状态码介绍
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:00d06b9aa0544e3a3c4729b89e55e3b33412bd5b0c903652f0538205f17d25b9
---

## 概述

绝大部分Node-API接口在执行结束后，会返回一个数据类型为napi\_status的状态码枚举，表示操作成功与否的相关信息。本文将重点介绍Node-API接口返回的非napi\_ok的状态码详情与修复建议。

## 各Node-API接口返回的非napi\_ok状态码介绍

| 接口名称 | 接口功能 | 可能返回的非napi\_ok状态码 | 原因 | 修复建议 |
| --- | --- | --- | --- | --- |
| napi\_module\_register | napi native模块注册接口。 | 不涉及 | 不涉及 | 不涉及 |
| napi\_get\_last\_error\_info | 获取napi\_extended\_error\_info结构体，其中包含最近一次出现的error信息。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_last\_error\_info | 获取napi\_extended\_error\_info结构体，其中包含最近一次出现的error信息。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_throw | 抛出一个ArkTS Error。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_throw | 抛出一个ArkTS Error。 | napi\_invalid\_arg | 入参error为nullptr | 确保入参正确 |
| napi\_throw | 抛出一个ArkTS Error。 | napi\_invalid\_arg | 入参error不为ArkTS Error类型 | 确保入参正确 |
| napi\_throw\_error | 抛出一个带文本信息的ArkTS Error。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_throw\_error | 抛出一个带文本信息的ArkTS Error。 | napi\_invalid\_arg | 入参msg为nullptr | 确保入参正确 |
| napi\_throw\_business\_error | 抛出一个带文本信息且错误对象的code属性类型为number类型的ArkTS Error对象。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_throw\_business\_error | 抛出一个带文本信息且错误对象的code属性类型为number类型的ArkTS Error对象。 | napi\_invalid\_arg | 入参msg为nullptr | 确保入参正确 |
| napi\_throw\_business\_error | 抛出一个带文本信息且错误对象的code属性类型为number类型的ArkTS Error对象。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS Error | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_throw\_type\_error | 抛出一个带文本信息的ArkTS TypeError。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_throw\_type\_error | 抛出一个带文本信息的ArkTS TypeError。 | napi\_invalid\_arg | 入参msg为nullptr | 确保入参正确 |
| napi\_throw\_range\_error | 抛出一个带文本信息的ArkTS RangeError。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_throw\_range\_error | 抛出一个带文本信息的ArkTS RangeError。 | napi\_invalid\_arg | 入参msg为nullptr | 确保入参正确 |
| napi\_is\_error | 判断napi\_value是否表示为一个error对象。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_is\_error | 判断napi\_value是否表示为一个error对象。 | napi\_invalid\_arg | 入参value为nullptr | 确保入参正确 |
| napi\_is\_error | 判断napi\_value是否表示为一个error对象。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_error | 创建并获取一个带文本信息的ArkTS Error。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_error | 创建并获取一个带文本信息的ArkTS Error。 | napi\_invalid\_arg | 入参msg为nullptr | 确保入参正确 |
| napi\_create\_error | 创建并获取一个带文本信息的ArkTS Error。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_error | 创建并获取一个带文本信息的ArkTS Error。 | napi\_invalid\_arg | 入参code不为nullptr，但不为ArkTS String或ArkTS Number类型 | 确保入参正确 |
| napi\_create\_error | 创建并获取一个带文本信息的ArkTS Error。 | napi\_invalid\_arg | 入参msg不为nullptr，但不为ArkTS String类型 | 确保入参正确 |
| napi\_create\_type\_error | 创建并获取一个带文本信息的ArkTS TypeError。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_type\_error | 创建并获取一个带文本信息的ArkTS TypeError。 | napi\_invalid\_arg | 入参msg为nullptr | 确保入参正确 |
| napi\_create\_type\_error | 创建并获取一个带文本信息的ArkTS TypeError。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_type\_error | 创建并获取一个带文本信息的ArkTS TypeError。 | napi\_invalid\_arg | 入参code不为nullptr，但不为ArkTS String或ArkTS Number类型 | 确保入参正确 |
| napi\_create\_type\_error | 创建并获取一个带文本信息的ArkTS TypeError。 | napi\_invalid\_arg | 入参msg不为nullptr，但不为ArkTS String类型 | 确保入参正确 |
| napi\_create\_range\_error | 创建并获取一个带文本信息的ArkTS RangeError。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_range\_error | 创建并获取一个带文本信息的ArkTS RangeError。 | napi\_invalid\_arg | 入参msg为nullptr | 确保入参正确 |
| napi\_create\_range\_error | 创建并获取一个带文本信息的ArkTS RangeError。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_range\_error | 创建并获取一个带文本信息的ArkTS RangeError。 | napi\_invalid\_arg | 入参code不为nullptr，但不为ArkTS String或ArkTS Number类型 | 确保入参正确 |
| napi\_create\_range\_error | 创建并获取一个带文本信息的ArkTS RangeError。 | napi\_invalid\_arg | 入参msg不为nullptr，但不为ArkTS String类型 | 确保入参正确 |
| napi\_get\_and\_clear\_last\_exception | 获取并清除最近一次出现的异常。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_and\_clear\_last\_exception | 获取并清除最近一次出现的异常。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_is\_exception\_pending | 判断是否出现了异常。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_is\_exception\_pending | 判断是否出现了异常。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_fatal\_error | 引发致命错误以立即终止进程。 | 不涉及 | 不涉及 | 不涉及 |
| napi\_open\_handle\_scope | 创建一个上下文环境使用。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_open\_handle\_scope | 创建一个上下文环境使用。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_close\_handle\_scope | 关闭传入的上下文环境，关闭后，全部在其中声明的引用都将被关闭。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_close\_handle\_scope | 关闭传入的上下文环境，关闭后，全部在其中声明的引用都将被关闭。 | napi\_invalid\_arg | 入参scope为nullptr | 确保入参正确 |
| napi\_close\_handle\_scope | 关闭传入的上下文环境，关闭后，全部在其中声明的引用都将被关闭。 | napi\_handle\_scope\_mismatch | napi\_open\_handle\_scope调用次数小于napi\_close\_handle\_scope | napi\_open\_handle\_scope和napi\_close\_handle\_scope需要成对使用 |
| napi\_open\_escapable\_handle\_scope | 创建出一个可逃逸的handle scope，可将范围内声明的值返回到父作用域。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_open\_escapable\_handle\_scope | 创建出一个可逃逸的handle scope，可将范围内声明的值返回到父作用域。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_close\_escapable\_handle\_scope | 关闭传入的可逃逸的handle scope。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_close\_escapable\_handle\_scope | 关闭传入的可逃逸的handle scope。 | napi\_invalid\_arg | 入参scope为nullptr | 确保入参正确 |
| napi\_close\_escapable\_handle\_scope | 关闭传入的可逃逸的handle scope。 | napi\_handle\_scope\_mismatch | napi\_open\_escapable\_handle\_scope调用次数小于napi\_close\_escapable\_handle\_scope | napi\_open\_escapable\_handle\_scope和napi\_close\_escapable\_handle\_scope需要成对使用 |
| napi\_escape\_handle | 提升传入的ArkTS object的生命周期到其父作用域。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_escape\_handle | 提升传入的ArkTS object的生命周期到其父作用域。 | napi\_invalid\_arg | 入参scope为nullptr | 确保入参正确 |
| napi\_escape\_handle | 提升传入的ArkTS object的生命周期到其父作用域。 | napi\_invalid\_arg | 入参escapee为nullptr | 确保入参正确 |
| napi\_escape\_handle | 提升传入的ArkTS object的生命周期到其父作用域。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_escape\_handle | 提升传入的ArkTS object的生命周期到其父作用域。 | napi\_escape\_called\_twice | 该scope已经调用过napi\_escape\_handle | 请勿重复调用napi\_escape\_handle |
| napi\_create\_reference | 为Object创建一个reference，以延长其生命周期。调用者需要自己管理reference生命周期。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_reference | 为Object创建一个reference，以延长其生命周期。调用者需要自己管理reference生命周期。 | napi\_invalid\_arg | 入参value为nullptr | 确保入参正确 |
| napi\_create\_reference | 为Object创建一个reference，以延长其生命周期。调用者需要自己管理reference生命周期。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_delete\_reference | 删除传入的reference。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_delete\_reference | 删除传入的reference。 | napi\_invalid\_arg | 入参ref为nullptr | 确保入参正确 |
| napi\_reference\_ref | 增加传入的reference的引用计数，并获取该计数。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_reference\_ref | 增加传入的reference的引用计数，并获取该计数。 | napi\_invalid\_arg | 入参ref为nullptr | 确保入参正确 |
| napi\_reference\_unref | 减少传入的reference的引用计数，并获取该计数。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_reference\_unref | 减少传入的reference的引用计数，并获取该计数。 | napi\_invalid\_arg | 入参ref为nullptr | 确保入参正确 |
| napi\_get\_reference\_value | 获取与reference相关联的ArkTS Object。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_reference\_value | 获取与reference相关联的ArkTS Object。 | napi\_invalid\_arg | 入参ref为nullptr | 确保入参正确 |
| napi\_get\_reference\_value | 获取与reference相关联的ArkTS Object。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_array | 创建并获取一个ArkTS Array。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_array | 创建并获取一个ArkTS Array。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_array\_with\_length | 创建并获取一个指定长度的ArkTS Array。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_array\_with\_length | 创建并获取一个指定长度的ArkTS Array。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_arraybuffer | 创建并获取一个指定大小的ArkTS ArrayBuffer。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_arraybuffer | 创建并获取一个指定大小的ArkTS ArrayBuffer。 | napi\_invalid\_arg | 入参data为nullptr | 确保入参正确 |
| napi\_create\_arraybuffer | 创建并获取一个指定大小的ArkTS ArrayBuffer。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_arraybuffer | 创建并获取一个指定大小的ArkTS ArrayBuffer。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_create\_external | 分配一个附加有外部数据的ArkTS value。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_external | 分配一个附加有外部数据的ArkTS value。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_external | 分配一个附加有外部数据的ArkTS value。 | napi\_pending\_exception | 调用接口前有未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_create\_external\_arraybuffer | 分配一个附加有外部数据的ArkTS ArrayBuffer。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_external\_arraybuffer | 分配一个附加有外部数据的ArkTS ArrayBuffer。 | napi\_invalid\_arg | 入参external\_data为nullptr | 确保入参正确 |
| napi\_create\_external\_arraybuffer | 分配一个附加有外部数据的ArkTS ArrayBuffer。 | napi\_invalid\_arg | 入参finalize\_cb为nullptr | 确保入参正确 |
| napi\_create\_external\_arraybuffer | 分配一个附加有外部数据的ArkTS ArrayBuffer。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_external\_arraybuffer | 分配一个附加有外部数据的ArkTS ArrayBuffer。 | napi\_pending\_exception | 调用接口前有未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_create\_object | 创建一个默认的ArkTS Object。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_object | 创建一个默认的ArkTS Object。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_symbol | 创建一个ArkTS Symbol。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_symbol | 创建一个ArkTS Symbol。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_symbol | 创建一个ArkTS Symbol。 | napi\_invalid\_arg | 入参description不为nullptr，且不是ArkTS String类型 | 确保入参正确 |
| napi\_create\_typedarray | 通过现有的ArrayBuffer创建一个ArkTS TypeArray。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_typedarray | 通过现有的ArrayBuffer创建一个ArkTS TypeArray。 | napi\_invalid\_arg | 入参arraybuffer为nullptr | 确保入参正确 |
| napi\_create\_typedarray | 通过现有的ArrayBuffer创建一个ArkTS TypeArray。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_typedarray | 通过现有的ArrayBuffer创建一个ArkTS TypeArray。 | napi\_invalid\_arg | 入参type不为napi\_typedarray\_type类型 | 确保入参正确 |
| napi\_create\_typedarray | 通过现有的ArrayBuffer创建一个ArkTS TypeArray。 | napi\_arraybuffer\_expected | 入参arraybuffer不为ArkTS ArrayBuffer类型 | 确保入参正确 |
| napi\_create\_typedarray | 通过现有的ArrayBuffer创建一个ArkTS TypeArray。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_create\_dataview | 通过现有的ArrayBuffer创建一个ArkTS DataView。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_dataview | 通过现有的ArrayBuffer创建一个ArkTS DataView。 | napi\_invalid\_arg | 入参arraybuffer为nullptr | 确保入参正确 |
| napi\_create\_dataview | 通过现有的ArrayBuffer创建一个ArkTS DataView。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_dataview | 通过现有的ArrayBuffer创建一个ArkTS DataView。 | napi\_arraybuffer\_expected | 入参arraybuffer不为ArkTS ArrayBuffer类型 | 确保入参正确 |
| napi\_create\_dataview | 通过现有的ArrayBuffer创建一个ArkTS DataView。 | napi\_pending\_exception | 入参length与入参byte\_offset相加超过入参arraybuffer的byte长度 | 需要检查访问长度 |
| napi\_create\_dataview | 通过现有的ArrayBuffer创建一个ArkTS DataView。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_create\_int32 | 通过一个C的int32\_t数据创建ArkTS Number。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_int32 | 通过一个C的int32\_t数据创建ArkTS Number。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_uint32 | 通过一个C的uint32\_t数据创建ArkTS Number。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_uint32 | 通过一个C的uint32\_t数据创建ArkTS Number。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_int64 | 通过一个C的int64\_t数据创建ArkTS Number。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_int64 | 通过一个C的int64\_t数据创建ArkTS Number。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_double | 通过一个C的double数据创建ArkTS Number。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_double | 通过一个C的double数据创建ArkTS Number。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_string\_latin1 | 通过ISO-8859-1编码的C字符串数据创建ArkTS String。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_string\_latin1 | 通过ISO-8859-1编码的C字符串数据创建ArkTS String。 | napi\_invalid\_arg | 入参str为nullptr | 确保入参正确 |
| napi\_create\_string\_latin1 | 通过ISO-8859-1编码的C字符串数据创建ArkTS String。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_string\_utf8 | 通过UTF8编码的C字符串数据创建ArkTS String。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_string\_utf8 | 通过UTF8编码的C字符串数据创建ArkTS String。 | napi\_invalid\_arg | 入参str为nullptr | 确保入参正确 |
| napi\_create\_string\_utf8 | 通过UTF8编码的C字符串数据创建ArkTS String。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_string\_utf16 | 通过UTF16编码的C字符串数据创建ArkTS String。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_string\_utf16 | 通过UTF16编码的C字符串数据创建ArkTS String。 | napi\_invalid\_arg | 入参str为nullptr | 确保入参正确 |
| napi\_create\_string\_utf16 | 通过UTF16编码的C字符串数据创建ArkTS String。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_string\_utf16 | 通过UTF16编码的C字符串数据创建ArkTS String。 | napi\_invalid\_arg | 入参length值不为NAPI\_AUTO\_LENGTH，但超过INT\_MAX | 确保入参正确 |
| napi\_get\_array\_length | 获取array的length。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_array\_length | 获取array的length。 | napi\_invalid\_arg | 入参value为nullptr | 确保入参正确 |
| napi\_get\_array\_length | 获取array的length。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_get\_array\_length | 获取array的length。 | napi\_array\_expected | 入参value既不是ArkTS Array类型，也不是SharedArray类型 | 确保入参正确 |
| napi\_get\_array\_length | 获取array的length。 | napi\_pending\_exception | 调用接口前有未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_get\_arraybuffer\_info | 获取ArrayBuffer的底层data buffer及其长度。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_arraybuffer\_info | 获取ArrayBuffer的底层data buffer及其长度。 | napi\_invalid\_arg | 入参arraybuffer为nullptr | 确保入参正确 |
| napi\_get\_arraybuffer\_info | 获取ArrayBuffer的底层data buffer及其长度。 | napi\_invalid\_arg | 入参byte\_length为nullptr | 确保入参正确 |
| napi\_get\_arraybuffer\_info | 获取ArrayBuffer的底层data buffer及其长度。 | napi\_arraybuffer\_expected | 入参arraybuffer既不是ArkTS ArrayBuffer类型，也不是SharedArrayBuffer类型 | 确保入参正确 |
| napi\_get\_prototype | 获取给定ArkTS Object的prototype。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_prototype | 获取给定ArkTS Object的prototype。 | napi\_invalid\_arg | 入参object为nullptr | 确保入参正确 |
| napi\_get\_prototype | 获取给定ArkTS Object的prototype。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_get\_prototype | 获取给定ArkTS Object的prototype。 | napi\_object\_expected | 入参object不为ArkTS Object类型 | 确保入参正确 |
| napi\_get\_prototype | 获取给定ArkTS Object的prototype。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_get\_typedarray\_info | 获取给定TypedArray的各种属性。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_typedarray\_info | 获取给定TypedArray的各种属性。 | napi\_invalid\_arg | 入参typedarray为nullptr | 确保入参正确 |
| napi\_get\_typedarray\_info | 获取给定TypedArray的各种属性。 | napi\_invalid\_arg | 入参typedarray既不是ArkTS TypedArray类型，也不是ShareTypedArray类型 | 确保入参正确 |
| napi\_get\_dataview\_info | 获取给定DataView的各种属性。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_dataview\_info | 获取给定DataView的各种属性。 | napi\_invalid\_arg | 入参dataview为nullptr | 确保入参正确 |
| napi\_get\_dataview\_info | 获取给定DataView的各种属性。 | napi\_invalid\_arg | 入参dataview不为ArkTS DataView类型 | 确保入参正确 |
| napi\_get\_value\_bool | 获取给定ArkTS Boolean对应的C bool值。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_value\_bool | 获取给定ArkTS Boolean对应的C bool值。 | napi\_invalid\_arg | 入参value为nullptr | 确保入参正确 |
| napi\_get\_value\_bool | 获取给定ArkTS Boolean对应的C bool值。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_get\_value\_bool | 获取给定ArkTS Boolean对应的C bool值。 | napi\_boolean\_expected | 入参value不为ArkTS Bool类型 | 确保入参正确 |
| napi\_get\_value\_double | 获取给定ArkTS Number对应的C double值。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_value\_double | 获取给定ArkTS Number对应的C double值。 | napi\_invalid\_arg | 入参value为nullptr | 确保入参正确 |
| napi\_get\_value\_double | 获取给定ArkTS Number对应的C double值。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_get\_value\_double | 获取给定ArkTS Number对应的C double值。 | napi\_number\_expected | 入参value不为ArkTS Number类型 | 确保入参正确 |
| napi\_get\_value\_external | 获取先前通过napi\_create\_external()传递的外部数据指针。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_value\_external | 获取先前通过napi\_create\_external()传递的外部数据指针。 | napi\_invalid\_arg | 入参value为nullptr | 确保入参正确 |
| napi\_get\_value\_external | 获取先前通过napi\_create\_external()传递的外部数据指针。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_get\_value\_external | 获取先前通过napi\_create\_external()传递的外部数据指针。 | napi\_object\_expected | 入参value不为external类型 | 确保入参正确 |
| napi\_get\_value\_int32 | 获取给定ArkTS Number对应的C int32值。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_value\_int32 | 获取给定ArkTS Number对应的C int32值。 | napi\_invalid\_arg | 入参value为nullptr | 确保入参正确 |
| napi\_get\_value\_int32 | 获取给定ArkTS Number对应的C int32值。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_get\_value\_int32 | 获取给定ArkTS Number对应的C int32值。 | napi\_number\_expected | 入参value不为ArkTS Number类型 | 确保入参正确 |
| napi\_get\_value\_int64 | 获取给定ArkTS Number对应的C int64值。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_value\_int64 | 获取给定ArkTS Number对应的C int64值。 | napi\_invalid\_arg | 入参value为nullptr | 确保入参正确 |
| napi\_get\_value\_int64 | 获取给定ArkTS Number对应的C int64值。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_get\_value\_int64 | 获取给定ArkTS Number对应的C int64值。 | napi\_number\_expected | 入参value不为ArkTS Number类型 | 确保入参正确 |
| napi\_get\_value\_string\_latin1 | 获取给定ArkTS value对应的ISO-8859-1编码的字符串。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_value\_string\_latin1 | 获取给定ArkTS value对应的ISO-8859-1编码的字符串。 | napi\_invalid\_arg | 入参value为nullptr | 确保入参正确 |
| napi\_get\_value\_string\_latin1 | 获取给定ArkTS value对应的ISO-8859-1编码的字符串。 | napi\_invalid\_arg | 入参buf与result都为nullptr | 确保入参正确 |
| napi\_get\_value\_string\_latin1 | 获取给定ArkTS value对应的ISO-8859-1编码的字符串。 | napi\_string\_expected | 入参value不为ArkTS String类型 | 确保入参正确 |
| napi\_get\_value\_string\_utf8 | 获取给定ArkTS value对应的UTF8编码的字符串。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_value\_string\_utf8 | 获取给定ArkTS value对应的UTF8编码的字符串。 | napi\_invalid\_arg | 入参value为nullptr | 确保入参正确 |
| napi\_get\_value\_string\_utf8 | 获取给定ArkTS value对应的UTF8编码的字符串。 | napi\_invalid\_arg | 入参buf与result都为nullptr | 确保入参正确 |
| napi\_get\_value\_string\_utf8 | 获取给定ArkTS value对应的UTF8编码的字符串。 | napi\_string\_expected | 入参value不为ArkTS String类型 | 确保入参正确 |
| napi\_get\_value\_string\_utf16 | 获取给定ArkTS value对应的UTF16编码的字符串。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_value\_string\_utf16 | 获取给定ArkTS value对应的UTF16编码的字符串。 | napi\_invalid\_arg | 入参value为nullptr | 确保入参正确 |
| napi\_get\_value\_string\_utf16 | 获取给定ArkTS value对应的UTF16编码的字符串。 | napi\_invalid\_arg | 入参buf与result都为nullptr | 确保入参正确 |
| napi\_get\_value\_string\_utf16 | 获取给定ArkTS value对应的UTF16编码的字符串。 | napi\_string\_expected | 入参value不为ArkTS String类型 | 确保入参正确 |
| napi\_get\_value\_uint32 | 获取给定ArkTS Number对应的C uint32值。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_value\_uint32 | 获取给定ArkTS Number对应的C uint32值。 | napi\_invalid\_arg | 入参value为nullptr | 确保入参正确 |
| napi\_get\_value\_uint32 | 获取给定ArkTS Number对应的C uint32值。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_get\_value\_uint32 | 获取给定ArkTS Number对应的C uint32值。 | napi\_number\_expected | 入参value不为ArkTS Number类型 | 确保入参正确 |
| napi\_get\_boolean | 根据给定的C boolean值，获取ArkTS bool对象。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_boolean | 根据给定的C boolean值，获取ArkTS bool对象。 | napi\_invalid\_arg | 入参value为nullptr | 确保入参正确 |
| napi\_get\_global | 获取global对象。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_global | 获取global对象。 | napi\_invalid\_arg | 入参value为nullptr | 确保入参正确 |
| napi\_get\_null | 获取null对象。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_null | 获取null对象。 | napi\_invalid\_arg | 入参value为nullptr | 确保入参正确 |
| napi\_get\_undefined | 获取undefined对象。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_undefined | 获取undefined对象。 | napi\_invalid\_arg | 入参value为nullptr | 确保入参正确 |
| napi\_coerce\_to\_bool | 将给定的ArkTS value强转成ArkTS Boolean。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_coerce\_to\_bool | 将给定的ArkTS value强转成ArkTS Boolean。 | napi\_invalid\_arg | 入参value为nullptr | 确保入参正确 |
| napi\_coerce\_to\_bool | 将给定的ArkTS value强转成ArkTS Boolean。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_coerce\_to\_bool | 将给定的ArkTS value强转成ArkTS Boolean。 | napi\_pending\_exception | 调用接口前有未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_coerce\_to\_number | 将给定的ArkTS value强转成ArkTS Number。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_coerce\_to\_number | 将给定的ArkTS value强转成ArkTS Number。 | napi\_invalid\_arg | 入参value为nullptr | 确保入参正确 |
| napi\_coerce\_to\_number | 将给定的ArkTS value强转成ArkTS Number。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_coerce\_to\_object | 将给定的ArkTS value强转成ArkTS Object。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_coerce\_to\_object | 将给定的ArkTS value强转成ArkTS Object。 | napi\_invalid\_arg | 入参value为nullptr | 确保入参正确 |
| napi\_coerce\_to\_object | 将给定的ArkTS value强转成ArkTS Object。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_coerce\_to\_string | 将给定的ArkTS value强转成ArkTS String。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_coerce\_to\_string | 将给定的ArkTS value强转成ArkTS String。 | napi\_invalid\_arg | 入参value为nullptr | 确保入参正确 |
| napi\_coerce\_to\_string | 将给定的ArkTS value强转成ArkTS String。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_typeof | 获取给定ArkTS value的ArkTS type。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_typeof | 获取给定ArkTS value的ArkTS type。 | napi\_invalid\_arg | 入参value为nullptr | 确保入参正确 |
| napi\_typeof | 获取给定ArkTS value的ArkTS type。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_instanceof | 判断给定object是否为给定constructor的实例。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_instanceof | 判断给定object是否为给定constructor的实例。 | napi\_invalid\_arg | 入参object为nullptr | 确保入参正确 |
| napi\_instanceof | 判断给定object是否为给定constructor的实例。 | napi\_invalid\_arg | 入参constructor为nullptr | 确保入参正确 |
| napi\_instanceof | 判断给定object是否为给定constructor的实例。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_instanceof | 判断给定object是否为给定constructor的实例。 | napi\_object\_expected | 入参object不为ArkTS Object类型 | 确保入参正确 |
| napi\_instanceof | 判断给定object是否为给定constructor的实例。 | napi\_function\_expected | 入参constructor不为ArkTS Function类型 | 确保入参正确 |
| napi\_instanceof | 判断给定object是否为给定constructor的实例。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_is\_array | 判断给定ArkTS value是否为array。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_is\_array | 判断给定ArkTS value是否为array。 | napi\_invalid\_arg | 入参value为nullptr | 确保入参正确 |
| napi\_is\_array | 判断给定ArkTS value是否为array。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_is\_arraybuffer | 判断给定ArkTS value是否为ArrayBuffer。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_is\_arraybuffer | 判断给定ArkTS value是否为ArrayBuffer。 | napi\_invalid\_arg | 入参value为nullptr | 确保入参正确 |
| napi\_is\_arraybuffer | 判断给定ArkTS value是否为ArrayBuffer。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_is\_typedarray | 判断给定ArkTS value是否表示一个TypedArray。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_is\_typedarray | 判断给定ArkTS value是否表示一个TypedArray。 | napi\_invalid\_arg | 入参value为nullptr | 确保入参正确 |
| napi\_is\_typedarray | 判断给定ArkTS value是否表示一个TypedArray。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_is\_dataview | 判断给定ArkTS value是否表示一个DataView。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_is\_dataview | 判断给定ArkTS value是否表示一个DataView。 | napi\_invalid\_arg | 入参value为nullptr | 确保入参正确 |
| napi\_is\_dataview | 判断给定ArkTS value是否表示一个DataView。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_is\_date | 判断给定ArkTS value是否为ArkTS Date对象。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_is\_date | 判断给定ArkTS value是否为ArkTS Date对象。 | napi\_invalid\_arg | 入参value为nullptr | 确保入参正确 |
| napi\_is\_date | 判断给定ArkTS value是否为ArkTS Date对象。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_strict\_equals | 判断给定的两个ArkTS value是否严格相等。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_strict\_equals | 判断给定的两个ArkTS value是否严格相等。 | napi\_invalid\_arg | 入参lhs为nullptr | 确保入参正确 |
| napi\_strict\_equals | 判断给定的两个ArkTS value是否严格相等。 | napi\_invalid\_arg | 入参rhs为nullptr | 确保入参正确 |
| napi\_strict\_equals | 判断给定的两个ArkTS value是否严格相等。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_get\_property\_names | 以字符串数组的形式获取对象的可枚举属性的名称。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_property\_names | 以字符串数组的形式获取对象的可枚举属性的名称。 | napi\_invalid\_arg | 入参object为nullptr | 确保入参正确 |
| napi\_get\_property\_names | 以字符串数组的形式获取对象的可枚举属性的名称。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_get\_property\_names | 以字符串数组的形式获取对象的可枚举属性的名称。 | napi\_object\_expected | 入参object不为ArkTS Object类型 | 确保入参正确 |
| napi\_set\_property | 对给定Object设置属性。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_set\_property | 对给定Object设置属性。 | napi\_invalid\_arg | 入参object为nullptr | 确保入参正确 |
| napi\_set\_property | 对给定Object设置属性。 | napi\_invalid\_arg | 入参key为nullptr | 确保入参正确 |
| napi\_set\_property | 对给定Object设置属性。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_set\_property | 对给定Object设置属性。 | napi\_object\_expected | 入参object不为ArkTS Object类型 | 确保入参正确 |
| napi\_set\_property | 对给定Object设置属性。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_get\_property | 获取给定Object的给定属性。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_property | 获取给定Object的给定属性。 | napi\_invalid\_arg | 入参object为nullptr | 确保入参正确 |
| napi\_get\_property | 获取给定Object的给定属性。 | napi\_invalid\_arg | 入参key为nullptr | 确保入参正确 |
| napi\_get\_property | 获取给定Object的给定属性。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_get\_property | 获取给定Object的给定属性。 | napi\_object\_expected | 入参object不为ArkTS Object类型 | 确保入参正确 |
| napi\_get\_property | 获取给定Object的给定属性。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_has\_property | 判断给定对象中是否存在给定属性。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_has\_property | 判断给定对象中是否存在给定属性。 | napi\_invalid\_arg | 入参object为nullptr | 确保入参正确 |
| napi\_has\_property | 判断给定对象中是否存在给定属性。 | napi\_invalid\_arg | 入参key为nullptr | 确保入参正确 |
| napi\_has\_property | 判断给定对象中是否存在给定属性。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_has\_property | 判断给定对象中是否存在给定属性。 | napi\_object\_expected | 入参object不为ArkTS Object类型 | 确保入参正确 |
| napi\_has\_property | 判断给定对象中是否存在给定属性。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_delete\_property | 尝试从给定Object中删除给定key属性。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_delete\_property | 尝试从给定Object中删除给定key属性。 | napi\_invalid\_arg | 入参object为nullptr | 确保入参正确 |
| napi\_delete\_property | 尝试从给定Object中删除给定key属性。 | napi\_invalid\_arg | 入参key为nullptr | 确保入参正确 |
| napi\_delete\_property | 尝试从给定Object中删除给定key属性。 | napi\_object\_expected | 入参object不为ArkTS Object类型 | 确保入参正确 |
| napi\_delete\_property | 尝试从给定Object中删除给定key属性。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_has\_own\_property | 判断给定Object中是否有名为key的own property。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_has\_own\_property | 判断给定Object中是否有名为key的own property。 | napi\_invalid\_arg | 入参object为nullptr | 确保入参正确 |
| napi\_has\_own\_property | 判断给定Object中是否有名为key的own property。 | napi\_invalid\_arg | 入参key为nullptr | 确保入参正确 |
| napi\_has\_own\_property | 判断给定Object中是否有名为key的own property。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_has\_own\_property | 判断给定Object中是否有名为key的own property。 | napi\_object\_expected | 入参object不为ArkTS Object类型 | 确保入参正确 |
| napi\_has\_own\_property | 判断给定Object中是否有名为key的own property。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_set\_named\_property | 对给定Object设置一个给定名称的属性。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_set\_named\_property | 对给定Object设置一个给定名称的属性。 | napi\_invalid\_arg | 入参object为nullptr | 确保入参正确 |
| napi\_set\_named\_property | 对给定Object设置一个给定名称的属性。 | napi\_invalid\_arg | 入参utf8name为nullptr | 确保入参正确 |
| napi\_set\_named\_property | 对给定Object设置一个给定名称的属性。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_set\_named\_property | 对给定Object设置一个给定名称的属性。 | napi\_object\_expected | 入参object不为ArkTS Object类型 | 确保入参正确 |
| napi\_set\_named\_property | 对给定Object设置一个给定名称的属性。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_get\_named\_property | 获取给定Object中指定名称的属性。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_named\_property | 获取给定Object中指定名称的属性。 | napi\_invalid\_arg | 入参object为nullptr | 确保入参正确 |
| napi\_get\_named\_property | 获取给定Object中指定名称的属性。 | napi\_invalid\_arg | 入参utf8name为nullptr | 确保入参正确 |
| napi\_get\_named\_property | 获取给定Object中指定名称的属性。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_get\_named\_property | 获取给定Object中指定名称的属性。 | napi\_object\_expected | 入参object不为ArkTS Object类型 | 确保入参正确 |
| napi\_get\_named\_property | 获取给定Object中指定名称的属性。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_has\_named\_property | 判断给定Object中是否有给定名称的属性。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_has\_named\_property | 判断给定Object中是否有给定名称的属性。 | napi\_invalid\_arg | 入参object为nullptr | 确保入参正确 |
| napi\_has\_named\_property | 判断给定Object中是否有给定名称的属性。 | napi\_invalid\_arg | 入参utf8name为nullptr | 确保入参正确 |
| napi\_has\_named\_property | 判断给定Object中是否有给定名称的属性。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_has\_named\_property | 判断给定Object中是否有给定名称的属性。 | napi\_object\_expected | 入参object不为ArkTS Object类型 | 确保入参正确 |
| napi\_has\_named\_property | 判断给定Object中是否有给定名称的属性。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_set\_element | 在给定Object的指定索引处，设置元素。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_set\_element | 在给定Object的指定索引处，设置元素。 | napi\_invalid\_arg | 入参object为nullptr | 确保入参正确 |
| napi\_set\_element | 在给定Object的指定索引处，设置元素。 | napi\_invalid\_arg | 入参value为nullptr | 确保入参正确 |
| napi\_set\_element | 在给定Object的指定索引处，设置元素。 | napi\_object\_expected | 入参object不为ArkTS Object类型 | 确保入参正确 |
| napi\_set\_element | 在给定Object的指定索引处，设置元素。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_get\_element | 获取给定Object指定索引处的元素。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_element | 获取给定Object指定索引处的元素。 | napi\_invalid\_arg | 入参object为nullptr | 确保入参正确 |
| napi\_get\_element | 获取给定Object指定索引处的元素。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_get\_element | 获取给定Object指定索引处的元素。 | napi\_object\_expected | 入参object不为ArkTS Object类型 | 确保入参正确 |
| napi\_get\_element | 获取给定Object指定索引处的元素。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_has\_element | 若给定Object的指定索引处拥有属性，获取该元素。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_has\_element | 若给定Object的指定索引处拥有属性，获取该元素。 | napi\_invalid\_arg | 入参object为nullptr | 确保入参正确 |
| napi\_has\_element | 若给定Object的指定索引处拥有属性，获取该元素。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_has\_element | 若给定Object的指定索引处拥有属性，获取该元素。 | napi\_object\_expected | 入参object不为ArkTS Object类型 | 确保入参正确 |
| napi\_has\_element | 若给定Object的指定索引处拥有属性，获取该元素。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_delete\_element | 尝试删除给定Object的指定索引处的元素。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_delete\_element | 尝试删除给定Object的指定索引处的元素。 | napi\_invalid\_arg | 入参object为nullptr | 确保入参正确 |
| napi\_delete\_element | 尝试删除给定Object的指定索引处的元素。 | napi\_object\_expected | 入参object不为ArkTS Object类型 | 确保入参正确 |
| napi\_delete\_element | 尝试删除给定Object的指定索引处的元素。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_define\_properties | 批量的向给定Object中定义属性。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_define\_properties | 批量的向给定Object中定义属性。 | napi\_invalid\_arg | 入参object为nullptr | 确保入参正确 |
| napi\_define\_properties | 批量的向给定Object中定义属性。 | napi\_invalid\_arg | 入参properties为nullptr | 确保入参正确 |
| napi\_define\_properties | 批量的向给定Object中定义属性。 | napi\_object\_expected | 入参object不为ArkTS Object类型 | 确保入参正确 |
| napi\_define\_properties | 批量的向给定Object中定义属性。 | napi\_name\_expected | 入参properties中的某个property没有设utf8name，且它的name既不是ArkTS String类型也不是ArkTS Symbol类型 | 确保入参正确 |
| napi\_define\_properties | 批量的向给定Object中定义属性。 | napi\_pending\_exception | 调用接口前有未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_type\_tag\_object | 将tag指针的值与Object关联。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_type\_tag\_object | 将tag指针的值与Object关联。 | napi\_invalid\_arg | 入参js\_object为nullptr | 确保入参正确 |
| napi\_type\_tag\_object | 将tag指针的值与Object关联。 | napi\_invalid\_arg | 入参type\_tag为nullptr | 确保入参正确 |
| napi\_type\_tag\_object | 将tag指针的值与Object关联。 | napi\_invalid\_arg | ArkTS对象已被打过tag标记 | ArkTS对象需未被打过标记 |
| napi\_type\_tag\_object | 将tag指针的值与Object关联。 | napi\_invalid\_arg | 调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_type\_tag\_object | 将tag指针的值与Object关联。 | napi\_object\_expected | 入参js\_object不是ArkTS Object类型 | 确保入参正确 |
| napi\_type\_tag\_object | 将tag指针的值与Object关联。 | napi\_pending\_exception | 调用接口前有未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_check\_object\_type\_tag | 判断给定的tag指针是否被关联到了ArkTS Object上。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_check\_object\_type\_tag | 判断给定的tag指针是否被关联到了ArkTS Object上。 | napi\_invalid\_arg | 入参js\_object为nullptr | 确保入参正确 |
| napi\_check\_object\_type\_tag | 判断给定的tag指针是否被关联到了ArkTS Object上。 | napi\_invalid\_arg | 入参type\_tag为nullptr | 确保入参正确 |
| napi\_check\_object\_type\_tag | 判断给定的tag指针是否被关联到了ArkTS Object上。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_check\_object\_type\_tag | 判断给定的tag指针是否被关联到了ArkTS Object上。 | napi\_object\_expected | 入参js\_object不是ArkTS Object类型 | 确保入参正确 |
| napi\_check\_object\_type\_tag | 判断给定的tag指针是否被关联到了ArkTS Object上。 | napi\_pending\_exception | 调用接口前有未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_call\_function | 在Native方法中调用ArkTS function，即native call ArkTS。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_call\_function | 在Native方法中调用ArkTS function，即native call ArkTS。 | napi\_invalid\_arg | 入参func为nullptr | 确保入参正确 |
| napi\_call\_function | 在Native方法中调用ArkTS function，即native call ArkTS。 | napi\_invalid\_arg | 入参argc大于0且argv为nullptr | 确保入参正确 |
| napi\_call\_function | 在Native方法中调用ArkTS function，即native call ArkTS。 | napi\_function\_expected | 入参func不为ArkTS Function类型 | 确保入参正确 |
| napi\_call\_function | 在Native方法中调用ArkTS function，即native call ArkTS。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_create\_function | 创建native方法给ArkTS使用，以便于ArkTS call native。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_function | 创建native方法给ArkTS使用，以便于ArkTS call native。 | napi\_invalid\_arg | 入参cb为nullptr | 确保入参正确 |
| napi\_create\_function | 创建native方法给ArkTS使用，以便于ArkTS call native。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_function | 创建native方法给ArkTS使用，以便于ArkTS call native。 | napi\_invalid\_arg | new c++对象失败 | 内存不足，检查是否有c++内存泄漏 |
| napi\_create\_function | 创建native方法给ArkTS使用，以便于ArkTS call native。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_get\_cb\_info | 从给定的callback info中获取有关调用的详细信息，如参数和this指针。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_cb\_info | 从给定的callback info中获取有关调用的详细信息，如参数和this指针。 | napi\_invalid\_arg | 入参cbinfo为nullptr | 确保入参正确 |
| napi\_get\_new\_target | 获取构造函数调用的new.target。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_new\_target | 获取构造函数调用的new.target。 | napi\_invalid\_arg | 入参cbinfo为nullptr | 确保入参正确 |
| napi\_get\_new\_target | 获取构造函数调用的new.target。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_get\_new\_target | 获取构造函数调用的new.target。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_new\_instance | 通过给定的构造函数，构建一个实例。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_new\_instance | 通过给定的构造函数，构建一个实例。 | napi\_invalid\_arg | 入参constructor为nullptr | 确保入参正确 |
| napi\_new\_instance | 通过给定的构造函数，构建一个实例。 | napi\_invalid\_arg | 入参argc大于0且argv为nullptr | 确保入参正确 |
| napi\_new\_instance | 通过给定的构造函数，构建一个实例。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_new\_instance | 通过给定的构造函数，构建一个实例。 | napi\_function\_expected | 入参constructor不为ArkTS Function类型 | 确保入参正确 |
| napi\_new\_instance | 通过给定的构造函数，构建一个实例。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_define\_class | 定义与C++类相对应的JavaScript类。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_define\_class | 定义与C++类相对应的JavaScript类。 | napi\_invalid\_arg | 入参utf8name为nullptr | 确保入参正确 |
| napi\_define\_class | 定义与C++类相对应的JavaScript类。 | napi\_invalid\_arg | 入参constructor为nullptr | 确保入参正确 |
| napi\_define\_class | 定义与C++类相对应的JavaScript类。 | napi\_invalid\_arg | 入参property\_count大于0且properties为nullptr | 确保入参正确 |
| napi\_define\_class | 定义与C++类相对应的JavaScript类。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_define\_class | 定义与C++类相对应的JavaScript类。 | napi\_object\_expected | 入参length值不为NAPI\_AUTO\_LENGTH，但超过INT\_MAX | 确保入参正确 |
| napi\_define\_class | 定义与C++类相对应的JavaScript类。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_wrap | 在ArkTS object上绑定一个native对象实例。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_wrap | 在ArkTS object上绑定一个native对象实例。 | napi\_invalid\_arg | 入参js\_object为nullptr | 确保入参正确 |
| napi\_wrap | 在ArkTS object上绑定一个native对象实例。 | napi\_invalid\_arg | 入参native\_object为nullptr | 确保入参正确 |
| napi\_wrap | 在ArkTS object上绑定一个native对象实例。 | napi\_invalid\_arg | 入参finalize\_cb为nullptr | 确保入参正确 |
| napi\_wrap | 在ArkTS object上绑定一个native对象实例。 | napi\_object\_expected | 入参js\_object不是ArkTS Object类型 | 确保入参正确 |
| napi\_wrap | 在ArkTS object上绑定一个native对象实例。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_unwrap | 从ArkTS object上获取先前绑定的native对象实例。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_unwrap | 从ArkTS object上获取先前绑定的native对象实例。 | napi\_invalid\_arg | 入参js\_object为nullptr | 确保入参正确 |
| napi\_unwrap | 从ArkTS object上获取先前绑定的native对象实例。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_unwrap | 从ArkTS object上获取先前绑定的native对象实例。 | napi\_object\_expected | 入参js\_object不是ArkTS Object类型 | 确保入参正确 |
| napi\_unwrap | 从ArkTS object上获取先前绑定的native对象实例。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_remove\_wrap | 从ArkTS object上获取先前绑定的native对象实例，并解除绑定。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_remove\_wrap | 从ArkTS object上获取先前绑定的native对象实例，并解除绑定。 | napi\_invalid\_arg | 入参js\_object为nullptr | 确保入参正确 |
| napi\_remove\_wrap | 从ArkTS object上获取先前绑定的native对象实例，并解除绑定。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_remove\_wrap | 从ArkTS object上获取先前绑定的native对象实例，并解除绑定。 | napi\_object\_expected | 入参js\_object不是ArkTS Object类型 | 确保入参正确 |
| napi\_remove\_wrap | 从ArkTS object上获取先前绑定的native对象实例，并解除绑定。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_create\_async\_work | 创建一个异步工作对象。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_async\_work | 创建一个异步工作对象。 | napi\_invalid\_arg | 入参async\_resource\_name为nullptr | 确保入参正确 |
| napi\_create\_async\_work | 创建一个异步工作对象。 | napi\_invalid\_arg | 入参execute为nullptr | 确保入参正确 |
| napi\_create\_async\_work | 创建一个异步工作对象。 | napi\_invalid\_arg | 入参complete为nullptr | 确保入参正确 |
| napi\_create\_async\_work | 创建一个异步工作对象。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_delete\_async\_work | 释放先前创建的异步工作对象。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_delete\_async\_work | 释放先前创建的异步工作对象。 | napi\_invalid\_arg | 入参work为nullptr | 确保入参正确 |
| napi\_queue\_async\_work | 将异步工作对象加到队列，由底层去调度执行。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_queue\_async\_work | 将异步工作对象加到队列，由底层去调度执行。 | napi\_invalid\_arg | 入参work为nullptr | 确保入参正确 |
| napi\_cancel\_async\_work | 取消入队的异步任务。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_cancel\_async\_work | 取消入队的异步任务。 | napi\_invalid\_arg | 入参work为nullptr | 确保入参正确 |
| napi\_async\_init | 创建一个异步资源上下文环境（不支持与async\_hook相关功能）。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_async\_init | 创建一个异步资源上下文环境（不支持与async\_hook相关功能）。 | napi\_invalid\_arg | 入参async\_resource\_name为nullptr | 确保入参正确 |
| napi\_async\_init | 创建一个异步资源上下文环境（不支持与async\_hook相关功能）。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_make\_callback | 在异步资源上下文环境中回调ArkTS函数(不支持与async\_hook相关功能)。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_make\_callback | 在异步资源上下文环境中回调ArkTS函数(不支持与async\_hook相关功能)。 | napi\_invalid\_arg | 入参func为nullptr | 确保入参正确 |
| napi\_make\_callback | 在异步资源上下文环境中回调ArkTS函数(不支持与async\_hook相关功能)。 | napi\_invalid\_arg | 入参recv为nullptr | 确保入参正确 |
| napi\_make\_callback | 在异步资源上下文环境中回调ArkTS函数(不支持与async\_hook相关功能)。 | napi\_invalid\_arg | 入参argc大于0且argv为nullptr | 确保入参正确 |
| napi\_make\_callback | 在异步资源上下文环境中回调ArkTS函数(不支持与async\_hook相关功能)。 | napi\_object\_expected | 入参recv不为ArkTS Object类型 | 确保入参正确 |
| napi\_make\_callback | 在异步资源上下文环境中回调ArkTS函数(不支持与async\_hook相关功能)。 | napi\_function\_expected | 入参func不为ArkTS Function类型 | 确保入参正确 |
| napi\_make\_callback | 在异步资源上下文环境中回调ArkTS函数(不支持与async\_hook相关功能)。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_async\_destroy | 销毁先前创建的异步资源上下文环境（不支持与async\_hook相关功能）。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_async\_destroy | 销毁先前创建的异步资源上下文环境（不支持与async\_hook相关功能）。 | napi\_invalid\_arg | 入参async\_context为nullptr | 确保入参正确 |
| napi\_open\_callback\_scope | 创建一个回调作用域（不支持与async\_hook相关功能）。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_open\_callback\_scope | 创建一个回调作用域（不支持与async\_hook相关功能）。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_close\_callback\_scope | 关闭先前创建的回调作用域（不支持与async\_hook相关功能）。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_close\_callback\_scope | 关闭先前创建的回调作用域（不支持与async\_hook相关功能）。 | napi\_invalid\_arg | 入参scope为nullptr | 确保入参正确 |
| napi\_close\_callback\_scope | 关闭先前创建的回调作用域（不支持与async\_hook相关功能）。 | napi\_invalid\_arg | new c++对象失败 | 内存不足，检查是否有c++内存泄漏 |
| napi\_close\_callback\_scope | 关闭先前创建的回调作用域（不支持与async\_hook相关功能）。 | napi\_callback\_scope\_mismatch | napi\_open\_callback\_scope调用次数小于napi\_close\_callback\_scope | napi\_open\_callback\_scope和napi\_close\_callback\_scope需要成对使用 |
| napi\_get\_node\_version | 获取node的版本信息。 | 不涉及 | 不涉及 | 不涉及 |
| napi\_get\_version | 获取Node运行时支持的最高 N-API 版本。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_version | 获取Node运行时支持的最高 N-API 版本。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_promise | 创建一个延迟对象和ArkTS promise。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_promise | 创建一个延迟对象和ArkTS promise。 | napi\_invalid\_arg | 入参deferred为nullptr | 确保入参正确 |
| napi\_create\_promise | 创建一个延迟对象和ArkTS promise。 | napi\_invalid\_arg | 入参promise为nullptr | 确保入参正确 |
| napi\_create\_promise | 创建一个延迟对象和ArkTS promise。 | napi\_pending\_exception | 调用接口前有未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_resolve\_deferred | resolve与ArkTS promise对象关联的延迟函数。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_resolve\_deferred | resolve与ArkTS promise对象关联的延迟函数。 | napi\_invalid\_arg | 入参deferred为nullptr | 确保入参正确 |
| napi\_resolve\_deferred | resolve与ArkTS promise对象关联的延迟函数。 | napi\_invalid\_arg | 入参resolution为nullptr | 确保入参正确 |
| napi\_resolve\_deferred | resolve与ArkTS promise对象关联的延迟函数。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_reject\_deferred | reject与ArkTS promise对象关联的延迟函数。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_reject\_deferred | reject与ArkTS promise对象关联的延迟函数。 | napi\_invalid\_arg | 入参deferred为nullptr | 确保入参正确 |
| napi\_reject\_deferred | reject与ArkTS promise对象关联的延迟函数。 | napi\_invalid\_arg | 入参rejection为nullptr | 确保入参正确 |
| napi\_reject\_deferred | reject与ArkTS promise对象关联的延迟函数。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_is\_promise | 判断给定ArkTS value是否为promise对象。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_is\_promise | 判断给定ArkTS value是否为promise对象。 | napi\_invalid\_arg | 入参value为nullptr | 确保入参正确 |
| napi\_is\_promise | 判断给定ArkTS value是否为promise对象。 | napi\_invalid\_arg | 入参is\_promise为nullptr | 确保入参正确 |
| napi\_get\_uv\_event\_loop | 获取当前libuv loop实例。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_uv\_event\_loop | 获取当前libuv loop实例。 | napi\_invalid\_arg | 入参loop为nullptr | 确保入参正确 |
| napi\_get\_uv\_event\_loop | 获取当前libuv loop实例。 | napi\_generic\_failure | 入参env已销毁 | 确保入参正确 |
| napi\_create\_threadsafe\_function | 创建线程安全函数。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_threadsafe\_function | 创建线程安全函数。 | napi\_invalid\_arg | 入参async\_resource\_name为nullptr | 确保入参正确 |
| napi\_create\_threadsafe\_function | 创建线程安全函数。 | napi\_invalid\_arg | 入参initial\_thread\_count为0或者大于128 | 确保入参正确 |
| napi\_create\_threadsafe\_function | 创建线程安全函数。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_threadsafe\_function | 创建线程安全函数。 | napi\_invalid\_arg | 入参func与call\_js\_cb都为nullptr | 确保入参正确 |
| napi\_create\_threadsafe\_function | 创建线程安全函数。 | napi\_invalid\_arg | new c++对象失败 | 内存不足，检查是否有c++内存泄漏 |
| napi\_create\_threadsafe\_function | 创建线程安全函数。 | napi\_generic\_failure | uv\_loop\_t为nullptr | NA |
| napi\_create\_threadsafe\_function | 创建线程安全函数。 | napi\_generic\_failure | uv\_async\_init失败 | NA |
| napi\_get\_threadsafe\_function\_context | 获取线程安全函数中的context。 | napi\_invalid\_arg | 入参func为nullptr | 确保入参正确 |
| napi\_get\_threadsafe\_function\_context | 获取线程安全函数中的context。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_call\_threadsafe\_function | 调用线程安全函数。 | napi\_invalid\_arg | 入参func为nullptr | 确保入参正确 |
| napi\_call\_threadsafe\_function | 调用线程安全函数。 | napi\_invalid\_arg | threadsafe\_function已关闭 | 请勿在napi\_release\_threadsafe\_function关闭了func后再调用本接口 |
| napi\_call\_threadsafe\_function | 调用线程安全函数。 | napi\_queue\_full | 入参is\_blocking为napi\_tsfn\_nonblocking且queue已满 | 增大max\_queue\_size大小。或is\_blocking改为napi\_tsfn\_blocking |
| napi\_call\_threadsafe\_function | 调用线程安全函数。 | napi\_closing | threadsafe\_function正在关闭 | 请勿在napi\_release\_threadsafe\_function关闭了func后再调用本接口 |
| napi\_call\_threadsafe\_function | 调用线程安全函数。 | napi\_closing | 入参env已销毁，且env地址又被新env复用 | 请勿在env销毁后再使用本接口 |
| napi\_call\_threadsafe\_function | 调用线程安全函数。 | napi\_generic\_failure | uv\_async\_send失败 | NA |
| napi\_call\_threadsafe\_function | 调用线程安全函数。 | napi\_generic\_failure | 入参env已销毁 | 请勿在env销毁后再使用本接口 |
| napi\_acquire\_threadsafe\_function | 指示线程安全函数可以开始使用。 | napi\_invalid\_arg | 入参func为nullptr | 确保入参正确 |
| napi\_acquire\_threadsafe\_function | 指示线程安全函数可以开始使用。 | napi\_generic\_failure | threadsafe\_function正在关闭/已关闭 | 请勿在napi\_release\_threadsafe\_function关闭了func后再调用本接口 |
| napi\_release\_threadsafe\_function | 指示线程安全函数将停止使用。 | napi\_invalid\_arg | 入参func为nullptr | 确保入参正确 |
| napi\_release\_threadsafe\_function | 指示线程安全函数将停止使用。 | napi\_generic\_failure | threadsafe\_function正在关闭/已关闭 | 请勿在napi\_release\_threadsafe\_function关闭了func后再调用本接口 |
| napi\_release\_threadsafe\_function | 指示线程安全函数将停止使用。 | napi\_generic\_failure | 调用本接口时，占用threadsafe\_function的线程数是0 | release次数需要与initial\_thread\_count和acquire匹配 |
| napi\_release\_threadsafe\_function | 指示线程安全函数将停止使用。 | napi\_generic\_failure | uv\_async\_send失败 | NA |
| napi\_release\_threadsafe\_function | 指示线程安全函数将停止使用。 | napi\_generic\_failure | 入参env已销毁 | 确保入参正确 |
| napi\_ref\_threadsafe\_function | 指示在主线程上运行的事件循环在线程安全函数被销毁之前不应退出。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_ref\_threadsafe\_function | 指示在主线程上运行的事件循环在线程安全函数被销毁之前不应退出。 | napi\_invalid\_arg | 入参func为nullptr | 确保入参正确 |
| napi\_ref\_threadsafe\_function | 指示在主线程上运行的事件循环在线程安全函数被销毁之前不应退出。 | napi\_generic\_failure | 当前线程不是env所在线程 | 该接口只能从env所在线程调用 |
| napi\_unref\_threadsafe\_function | 指示在主线程上运行的事件循环可能会在线程安全函数被销毁之前退出。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_unref\_threadsafe\_function | 指示在主线程上运行的事件循环可能会在线程安全函数被销毁之前退出。 | napi\_invalid\_arg | 入参func为nullptr | 确保入参正确 |
| napi\_unref\_threadsafe\_function | 指示在主线程上运行的事件循环可能会在线程安全函数被销毁之前退出。 | napi\_generic\_failure | 当前线程不是env所在线程 | 该接口只能从env所在线程调用 |
| napi\_create\_date | 通过一个C的double数据创建ArkTS Date。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_date | 通过一个C的double数据创建ArkTS Date。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_date | 通过一个C的double数据创建ArkTS Date。 | napi\_pending\_exception | 调用接口前有未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_get\_date\_value | 获取给定ArkTS Date对应的C double值。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_date\_value | 获取给定ArkTS Date对应的C double值。 | napi\_invalid\_arg | 入参value为nullptr | 确保入参正确 |
| napi\_get\_date\_value | 获取给定ArkTS Date对应的C double值。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_get\_date\_value | 获取给定ArkTS Date对应的C double值。 | napi\_date\_expected | 入参value不为ArkTS Date类型 | 确保入参正确 |
| napi\_get\_date\_value | 获取给定ArkTS Date对应的C double值。 | napi\_pending\_exception | 调用接口前有未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_create\_bigint\_int64 | 通过一个C的int64数据创建ArkTS BigInt。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_bigint\_int64 | 通过一个C的int64数据创建ArkTS BigInt。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_bigint\_uint64 | 通过一个C的uint64数据创建ArkTS BigInt。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_bigint\_uint64 | 通过一个C的uint64数据创建ArkTS BigInt。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_bigint\_words | 通过一个C的uint64数组创建单个ArkTS BigInt。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_bigint\_words | 通过一个C的uint64数组创建单个ArkTS BigInt。 | napi\_invalid\_arg | 入参words为nullptr | 确保入参正确 |
| napi\_create\_bigint\_words | 通过一个C的uint64数组创建单个ArkTS BigInt。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_bigint\_words | 通过一个C的uint64数组创建单个ArkTS BigInt。 | napi\_invalid\_arg | 入参word\_count大于等于INT\_MAX | 确保入参正确 |
| napi\_create\_bigint\_words | 通过一个C的uint64数组创建单个ArkTS BigInt。 | napi\_pending\_exception | 调用接口前有未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_create\_bigint\_words | 通过一个C的uint64数组创建单个ArkTS BigInt。 | napi\_pending\_exception | 入参(word\_count\*2)>(1\_MB/32) | 确保入参正确 |
| napi\_get\_value\_bigint\_int64 | 获取给定ArkTS BigInt对应的C int64值。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_value\_bigint\_int64 | 获取给定ArkTS BigInt对应的C int64值。 | napi\_invalid\_arg | 入参value为nullptr | 确保入参正确 |
| napi\_get\_value\_bigint\_int64 | 获取给定ArkTS BigInt对应的C int64值。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_get\_value\_bigint\_int64 | 获取给定ArkTS BigInt对应的C int64值。 | napi\_invalid\_arg | 入参lossless为nullptr | 确保入参正确 |
| napi\_get\_value\_bigint\_int64 | 获取给定ArkTS BigInt对应的C int64值。 | napi\_bigint\_expected | 入参value不为ArkTS BigInt类型 | 确保入参正确 |
| napi\_get\_value\_bigint\_uint64 | 获取给定ArkTS BigInt对应的C uint64值。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_value\_bigint\_uint64 | 获取给定ArkTS BigInt对应的C uint64值。 | napi\_invalid\_arg | 入参value为nullptr | 确保入参正确 |
| napi\_get\_value\_bigint\_uint64 | 获取给定ArkTS BigInt对应的C uint64值。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_get\_value\_bigint\_uint64 | 获取给定ArkTS BigInt对应的C uint64值。 | napi\_invalid\_arg | 入参lossless为nullptr | 确保入参正确 |
| napi\_get\_value\_bigint\_uint64 | 获取给定ArkTS BigInt对应的C uint64值。 | napi\_bigint\_expected | 入参value不为ArkTS BigInt类型 | 确保入参正确 |
| napi\_get\_value\_bigint\_words | 获取给定ArkTS BigInt对应的信息，包括符号位、64位小端序数组和数组中的元素个数。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_value\_bigint\_words | 获取给定ArkTS BigInt对应的信息，包括符号位、64位小端序数组和数组中的元素个数。 | napi\_invalid\_arg | 入参value为nullptr | 确保入参正确 |
| napi\_get\_value\_bigint\_words | 获取给定ArkTS BigInt对应的信息，包括符号位、64位小端序数组和数组中的元素个数。 | napi\_invalid\_arg | 入参word\_count为nullptr | 确保入参正确 |
| napi\_get\_value\_bigint\_words | 获取给定ArkTS BigInt对应的信息，包括符号位、64位小端序数组和数组中的元素个数。 | napi\_object\_expected | 入参value不为ArkTS BigInt类型 | 确保入参正确 |
| napi\_create\_buffer | 创建并获取一个指定大小的ArkTS Buffer。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_buffer | 创建并获取一个指定大小的ArkTS Buffer。 | napi\_invalid\_arg | 入参data为nullptr | 确保入参正确 |
| napi\_create\_buffer | 创建并获取一个指定大小的ArkTS Buffer。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_buffer | 创建并获取一个指定大小的ArkTS Buffer。 | napi\_invalid\_arg | 入参size为0或超过2MiB(2097152) | 确保入参正确 |
| napi\_create\_buffer | 创建并获取一个指定大小的ArkTS Buffer。 | napi\_pending\_exception | 调用接口前有未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_create\_buffer\_copy | 创建并获取一个指定大小的ArkTS Buffer，并以给定数据进行初始化。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_buffer\_copy | 创建并获取一个指定大小的ArkTS Buffer，并以给定数据进行初始化。 | napi\_invalid\_arg | 入参data为nullptr | 确保入参正确 |
| napi\_create\_buffer\_copy | 创建并获取一个指定大小的ArkTS Buffer，并以给定数据进行初始化。 | napi\_invalid\_arg | 入参result\_data为nullptr | 确保入参正确 |
| napi\_create\_buffer\_copy | 创建并获取一个指定大小的ArkTS Buffer，并以给定数据进行初始化。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_buffer\_copy | 创建并获取一个指定大小的ArkTS Buffer，并以给定数据进行初始化。 | napi\_invalid\_arg | 入参size为0或超过2MiB(2097152) | 确保入参正确 |
| napi\_create\_buffer\_copy | 创建并获取一个指定大小的ArkTS Buffer，并以给定数据进行初始化。 | napi\_pending\_exception | 调用接口前有未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_create\_external\_buffer | 创建并获取一个指定大小的ArkTS Buffer，并以给定数据进行初始化，该接口可为Buffer附带额外数据。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_external\_buffer | 创建并获取一个指定大小的ArkTS Buffer，并以给定数据进行初始化，该接口可为Buffer附带额外数据。 | napi\_invalid\_arg | 入参data为nullptr | 确保入参正确 |
| napi\_create\_external\_buffer | 创建并获取一个指定大小的ArkTS Buffer，并以给定数据进行初始化，该接口可为Buffer附带额外数据。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_external\_buffer | 创建并获取一个指定大小的ArkTS Buffer，并以给定数据进行初始化，该接口可为Buffer附带额外数据。 | napi\_invalid\_arg | 入参size为0或超过2MiB(2097152) | 确保入参正确 |
| napi\_create\_external\_buffer | 创建并获取一个指定大小的ArkTS Buffer，并以给定数据进行初始化，该接口可为Buffer附带额外数据。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_get\_buffer\_info | 获取ArkTS Buffer底层data及其长度。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_buffer\_info | 获取ArkTS Buffer底层data及其长度。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_get\_buffer\_info | 获取ArkTS Buffer底层data及其长度。 | napi\_arraybuffer\_expected | 入参value不为ArkTS ArrayBuffer类型 | 确保入参正确 |
| napi\_is\_buffer | 判断给定ArkTS value是否为Buffer对象。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_is\_buffer | 判断给定ArkTS value是否为Buffer对象。 | napi\_invalid\_arg | 入参value为nullptr | 确保入参正确 |
| napi\_is\_buffer | 判断给定ArkTS value是否为Buffer对象。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_object\_freeze | 冻结给定的对象。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_object\_freeze | 冻结给定的对象。 | napi\_invalid\_arg | 入参object为nullptr | 确保入参正确 |
| napi\_object\_freeze | 冻结给定的对象。 | napi\_object\_expected | 入参object不为ArkTS Object类型 | 确保入参正确 |
| napi\_object\_freeze | 冻结给定的对象。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_object\_seal | 密封给定的对象。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_object\_seal | 密封给定的对象。 | napi\_invalid\_arg | 入参object为nullptr | 确保入参正确 |
| napi\_object\_seal | 密封给定的对象。 | napi\_object\_expected | 入参object不为ArkTS Object类型 | 确保入参正确 |
| napi\_object\_seal | 密封给定的对象。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_get\_all\_property\_names | 获取一个数组，其中包含此对象过滤后的属性名称。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_all\_property\_names | 获取一个数组，其中包含此对象过滤后的属性名称。 | napi\_invalid\_arg | 入参object为nullptr | 确保入参正确 |
| napi\_get\_all\_property\_names | 获取一个数组，其中包含此对象过滤后的属性名称。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_get\_all\_property\_names | 获取一个数组，其中包含此对象过滤后的属性名称。 | napi\_invalid\_arg | 入参key\_mode不在napi\_key\_collection\_mode枚举范围内 | 确保入参正确 |
| napi\_get\_all\_property\_names | 获取一个数组，其中包含此对象过滤后的属性名称。 | napi\_invalid\_arg | 入参key\_conversion不在napi\_key\_conversion枚举范围内 | 确保入参正确 |
| napi\_get\_all\_property\_names | 获取一个数组，其中包含此对象过滤后的属性名称。 | napi\_object\_expected | 入参object不为ArkTS Object类型 | 确保入参正确 |
| napi\_get\_all\_property\_names | 获取一个数组，其中包含此对象过滤后的属性名称。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_detach\_arraybuffer | 分离给定ArrayBuffer的底层数据。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_detach\_arraybuffer | 分离给定ArrayBuffer的底层数据。 | napi\_invalid\_arg | 入参arraybuffer为nullptr | 确保入参正确 |
| napi\_detach\_arraybuffer | 分离给定ArrayBuffer的底层数据。 | napi\_invalid\_arg | 入参arraybuffer是ArkTS Object类型，但不是ArkTS ArrayBuffer类型，也不是SharedArrayBuffer类型 | 确保入参正确 |
| napi\_detach\_arraybuffer | 分离给定ArrayBuffer的底层数据。 | napi\_invalid\_arg | 入参arraybuffer已被detach过 | 需arraybuffer未被detach过 |
| napi\_detach\_arraybuffer | 分离给定ArrayBuffer的底层数据。 | napi\_object\_expected | 入参arraybuffer不为ArkTS Object类型 | 确保入参正确 |
| napi\_is\_detached\_arraybuffer | 判断给定的ArrayBuffer是否已被分离过。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_is\_detached\_arraybuffer | 判断给定的ArrayBuffer是否已被分离过。 | napi\_invalid\_arg | 入参arraybuffer为nullptr | 确保入参正确 |
| napi\_is\_detached\_arraybuffer | 判断给定的ArrayBuffer是否已被分离过。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_is\_detached\_arraybuffer | 判断给定的ArrayBuffer是否已被分离过。 | napi\_invalid\_arg | 入参arraybuffer不为ArkTS ArrayBuffer类型 | 确保入参正确 |
| napi\_run\_script | 将给定对象作为ArkTS代码运行。当前接口实际为空实现，可使用系统拓展接口napi\_run\_script\_path接口，提升安全性。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_run\_script | 将给定对象作为ArkTS代码运行。当前接口实际为空实现，可使用系统拓展接口napi\_run\_script\_path接口，提升安全性。 | napi\_invalid\_arg | 入参script为nullptr | 确保入参正确 |
| napi\_run\_script | 将给定对象作为ArkTS代码运行。当前接口实际为空实现，可使用系统拓展接口napi\_run\_script\_path接口，提升安全性。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_set\_instance\_data | 绑定与当前运行的环境相关联的数据项。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_instance\_data | 检索与当前运行的环境相关联的数据项。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_instance\_data | 检索与当前运行的环境相关联的数据项。 | napi\_invalid\_arg | 入参data为nullptr | 确保入参正确 |
| napi\_add\_env\_cleanup\_hook | 注册环境清理钩子函数。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_add\_env\_cleanup\_hook | 注册环境清理钩子函数。 | napi\_invalid\_arg | 入参func为nullptr | 确保入参正确 |
| napi\_remove\_env\_cleanup\_hook | 取消环境清理钩子函数。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_remove\_env\_cleanup\_hook | 取消环境清理钩子函数。 | napi\_invalid\_arg | 入参func为nullptr | 确保入参正确 |
| napi\_add\_async\_cleanup\_hook | 注册清理异步钩子函数。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_add\_async\_cleanup\_hook | 注册清理异步钩子函数。 | napi\_invalid\_arg | 入参hook为nullptr | 确保入参正确 |
| napi\_remove\_async\_cleanup\_hook | 取消清理异步钩子函数。 | napi\_invalid\_arg | 入参remove\_handle为nullptr | 确保入参正确 |
| node\_api\_get\_module\_file\_name | 用于获取加载项加载位置的绝对路径。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| node\_api\_get\_module\_file\_name | 用于获取加载项加载位置的绝对路径。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_add\_finalizer | 当ArkTS Object中的对象被垃圾回收时调用注册的napi\_finalize回调。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_add\_finalizer | 当ArkTS Object中的对象被垃圾回收时调用注册的napi\_finalize回调。 | napi\_invalid\_arg | 入参js\_object为nullptr | 确保入参正确 |
| napi\_add\_finalizer | 当ArkTS Object中的对象被垃圾回收时调用注册的napi\_finalize回调。 | napi\_invalid\_arg | 入参finalize\_cb为nullptr | 确保入参正确 |
| napi\_add\_finalizer | 当ArkTS Object中的对象被垃圾回收时调用注册的napi\_finalize回调。 | napi\_object\_expected | 入参js\_object不是ArkTS Object类型 | 确保入参正确 |
| napi\_fatal\_exception | 向ArkTS抛出 UncaughtException。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_fatal\_exception | 向ArkTS抛出 UncaughtException。 | napi\_invalid\_arg | 入参err为nullptr | 确保入参正确 |
| napi\_fatal\_exception | 向ArkTS抛出 UncaughtException。 | napi\_invalid\_arg | 入参error不为ArkTS Error类型 | 确保入参正确 |
| napi\_fatal\_exception | 向ArkTS抛出 UncaughtException。 | napi\_pending\_exception | 调用接口前有未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_queue\_async\_work\_with\_qos | 将异步工作对象加到队列，由底层根据传入的qos优先级去调度执行。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_queue\_async\_work\_with\_qos | 将异步工作对象加到队列，由底层根据传入的qos优先级去调度执行。 | napi\_invalid\_arg | 入参work为nullptr | 确保入参正确 |
| napi\_run\_script\_path | 运行abc文件。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_run\_script\_path | 运行abc文件。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_run\_script\_path | 运行abc文件。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_load\_module | 将abc文件作为模块加载，返回模块的命名空间。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_load\_module | 将abc文件作为模块加载，返回模块的命名空间。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_load\_module | 将abc文件作为模块加载，返回模块的命名空间。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_create\_object\_with\_properties | 使用给定的napi\_property\_descriptor创建ArkTS Object。descriptor的键名必须为 string，且不可转为number。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_object\_with\_properties | 使用给定的napi\_property\_descriptor创建ArkTS Object。descriptor的键名必须为 string，且不可转为number。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_object\_with\_named\_properties | 使用给定的napi\_value和键名创建ArkTS Object。键名必须为 string，且不可转为number。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_object\_with\_named\_properties | 使用给定的napi\_value和键名创建ArkTS Object。键名必须为 string，且不可转为number。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_coerce\_to\_native\_binding\_object | 强制将ArkTS Object和Native对象绑定。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_coerce\_to\_native\_binding\_object | 强制将ArkTS Object和Native对象绑定。 | napi\_invalid\_arg | 入参js\_object为nullptr | 确保入参正确 |
| napi\_coerce\_to\_native\_binding\_object | 强制将ArkTS Object和Native对象绑定。 | napi\_invalid\_arg | 入参detach\_cb为nullptr | 确保入参正确 |
| napi\_coerce\_to\_native\_binding\_object | 强制将ArkTS Object和Native对象绑定。 | napi\_invalid\_arg | 入参attach\_cb为nullptr | 确保入参正确 |
| napi\_coerce\_to\_native\_binding\_object | 强制将ArkTS Object和Native对象绑定。 | napi\_invalid\_arg | 入参native\_object为nullptr | 确保入参正确 |
| napi\_coerce\_to\_native\_binding\_object | 强制将ArkTS Object和Native对象绑定。 | napi\_invalid\_arg | new c++对象失败 | 内存不足，检查是否有c++内存泄漏 |
| napi\_coerce\_to\_native\_binding\_object | 强制将ArkTS Object和Native对象绑定。 | napi\_object\_expected | js\_object不是ArkTS Object类型 | 确保入参正确 |
| napi\_coerce\_to\_native\_binding\_object | 强制将ArkTS Object和Native对象绑定。 | napi\_generic\_failure | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_create\_ark\_runtime | 创建基础运行时环境。 | napi\_invalid\_arg | g\_createNapiEnvCallback为nullptr | NA |
| napi\_create\_ark\_runtime | 创建基础运行时环境。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_ark\_runtime | 创建基础运行时环境。 | napi\_create\_ark\_runtime\_only\_one\_env\_per\_thread | 当前线程已创建过env | 避免重复创建 |
| napi\_create\_ark\_runtime | 创建基础运行时环境。 | napi\_create\_ark\_runtime\_too\_many\_envs | 达到最大ArkRuntime数量（64）或ArkTS线程数超上限（80） | 避免滥用接口 |
| napi\_create\_ark\_runtime | 创建基础运行时环境。 | napi\_generic\_failure | 创建ark\_runtime失败 | 根据hilog信息排查原因 |
| napi\_destroy\_ark\_runtime | 销毁基础运行时环境。 | napi\_invalid\_arg | g\_createNapiEnvCallback为nullptr | NA |
| napi\_destroy\_ark\_runtime | 销毁基础运行时环境。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_destroy\_ark\_runtime | 销毁基础运行时环境。 | napi\_destroy\_ark\_runtime\_env\_not\_exist | env未创建 | 与create接口配套使用 |
| napi\_run\_event\_loop | 触发底层的事件循环。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_run\_event\_loop | 触发底层的事件循环。 | napi\_invalid\_arg | 入参mode不为napi\_event\_mode枚举类型 | 确保入参正确 |
| napi\_run\_event\_loop | 触发底层的事件循环。 | napi\_invalid\_arg | env的loop为nullptr | 确保入参正确 |
| napi\_run\_event\_loop | 触发底层的事件循环。 | napi\_generic\_failure | 当前线程不是native线程 | 请使用napi\_create\_ark\_runtime接口创建出来的env |
| napi\_stop\_event\_loop | 停止底层的事件循环。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_stop\_event\_loop | 停止底层的事件循环。 | napi\_invalid\_arg | env的loop为nullptr | 确保入参正确 |
| napi\_stop\_event\_loop | 停止底层的事件循环。 | napi\_generic\_failure | 当前线程不是native线程 | 请使用napi\_create\_ark\_runtime接口创建出来的env |
| napi\_load\_module\_with\_info | 将abc文件作为模块加载，返回模块的命名空间。可在新创建的ArkTS基础运行时环境中使用。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_load\_module\_with\_info | 将abc文件作为模块加载，返回模块的命名空间。可在新创建的ArkTS基础运行时环境中使用。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_load\_module\_with\_info | 将abc文件作为模块加载，返回模块的命名空间。可在新创建的ArkTS基础运行时环境中使用。 | napi\_generic\_failure | 模块加载失败 | 根据hilog信息排查原因 |
| napi\_load\_module\_with\_info | 将abc文件作为模块加载，返回模块的命名空间。可在新创建的ArkTS基础运行时环境中使用。 | napi\_pending\_exception | 调用接口前有未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_serialize | 将ArkTS对象转换为native数据。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_serialize | 将ArkTS对象转换为native数据。 | napi\_invalid\_arg | 入参object为nullptr | 确保入参正确 |
| napi\_serialize | 将ArkTS对象转换为native数据。 | napi\_invalid\_arg | 入参transfer\_list为nullptr | 确保入参正确 |
| napi\_serialize | 将ArkTS对象转换为native数据。 | napi\_invalid\_arg | 入参clone\_list为nullptr | 确保入参正确 |
| napi\_serialize | 将ArkTS对象转换为native数据。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_serialize | 将ArkTS对象转换为native数据。 | napi\_invalid\_arg | 入参transfer\_list既不是undefined，也不是ArkTS Array | 确保入参正确 |
| napi\_serialize | 将ArkTS对象转换为native数据。 | napi\_invalid\_arg | 入参clone\_list既不是undefined，也不是ArkTS Array | 确保入参正确 |
| napi\_deserialize | 将native数据转为ArkTS对象。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_deserialize | 将native数据转为ArkTS对象。 | napi\_invalid\_arg | 入参buffer为nullptr | 确保入参正确 |
| napi\_deserialize | 将native数据转为ArkTS对象。 | napi\_invalid\_arg | 入参object为nullptr | 确保入参正确 |
| napi\_delete\_serialization\_data | 删除序列化数据。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_delete\_serialization\_data | 删除序列化数据。 | napi\_invalid\_arg | 入参buffer为nullptr | 确保入参正确 |
| napi\_call\_threadsafe\_function\_with\_priority | 将指定优先级和入队方式的任务投递到ArkTS主线程。 | napi\_invalid\_arg | 入参func为nullptr | 确保入参正确 |
| napi\_call\_threadsafe\_function\_with\_priority | 将指定优先级和入队方式的任务投递到ArkTS主线程。 | napi\_invalid\_arg | 入参priority不为napi\_task\_priority枚举类型 | 确保入参正确 |
| napi\_call\_threadsafe\_function\_with\_priority | 将指定优先级和入队方式的任务投递到ArkTS主线程。 | napi\_generic\_failure | 入参func非法 | 根据hilog信息排查原因 |
| napi\_call\_threadsafe\_function\_with\_priority | 将指定优先级和入队方式的任务投递到ArkTS主线程。 | napi\_generic\_failure | EventHandler不支持或EventHandler执行失败 | 根据hilog信息排查原因 |
| napi\_is\_sendable | 判断给定ArkTS value是否是Sendable的。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_is\_sendable | 判断给定ArkTS value是否是Sendable的。 | napi\_invalid\_arg | 入参value为nullptr | 确保入参正确 |
| napi\_is\_sendable | 判断给定ArkTS value是否是Sendable的。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_define\_sendable\_class | 创建一个Sendable类。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_define\_sendable\_class | 创建一个Sendable类。 | napi\_invalid\_arg | 入参utf8name为nullptr | 确保入参正确 |
| napi\_define\_sendable\_class | 创建一个Sendable类。 | napi\_invalid\_arg | 入参constructor为nullptr | 确保入参正确 |
| napi\_define\_sendable\_class | 创建一个Sendable类。 | napi\_invalid\_arg | 入参property\_count大于0且入参properties为nullptr | 确保入参正确 |
| napi\_define\_sendable\_class | 创建一个Sendable类。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_define\_sendable\_class | 创建一个Sendable类。 | napi\_object\_expected | 入参length值不为NAPI\_AUTO\_LENGTH，但超过INT\_MAX | 确保入参正确 |
| napi\_define\_sendable\_class | 创建一个Sendable类。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_create\_sendable\_object\_with\_properties | 使用给定的napi\_property\_descriptor创建一个Sendable对象。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_sendable\_object\_with\_properties | 使用给定的napi\_property\_descriptor创建一个Sendable对象。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_sendable\_array | 创建一个Sendable数组。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_sendable\_array | 创建一个Sendable数组。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_sendable\_array\_with\_length | 创建一个指定长度的Sendable数组。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_sendable\_array\_with\_length | 创建一个指定长度的Sendable数组。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_sendable\_arraybuffer | 创建一个Sendable ArrayBuffer。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_sendable\_arraybuffer | 创建一个Sendable ArrayBuffer。 | napi\_invalid\_arg | 入参data为nullptr | 确保入参正确 |
| napi\_create\_sendable\_arraybuffer | 创建一个Sendable ArrayBuffer。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_sendable\_arraybuffer | 创建一个Sendable ArrayBuffer。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_create\_sendable\_typedarray | 创建一个Sendable TypedArray。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_sendable\_typedarray | 创建一个Sendable TypedArray。 | napi\_invalid\_arg | 入参arraybuffer为nullptr | 确保入参正确 |
| napi\_create\_sendable\_typedarray | 创建一个Sendable TypedArray。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_sendable\_typedarray | 创建一个Sendable TypedArray。 | napi\_invalid\_arg | 入参type不为napi\_typedarray\_type类型 | 确保入参正确 |
| napi\_create\_sendable\_typedarray | 创建一个Sendable TypedArray。 | napi\_object\_expected | 入参arraybuffer不为SharedArrayBuffer类型 | 确保入参正确 |
| napi\_create\_sendable\_typedarray | 创建一个Sendable TypedArray。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_wrap\_sendable | 包裹一个native实例到ArkTS对象中。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_wrap\_sendable | 包裹一个native实例到ArkTS对象中。 | napi\_invalid\_arg | 入参js\_object为nullptr | 确保入参正确 |
| napi\_wrap\_sendable | 包裹一个native实例到ArkTS对象中。 | napi\_invalid\_arg | 入参native\_object为nullptr | 确保入参正确 |
| napi\_wrap\_sendable | 包裹一个native实例到ArkTS对象中。 | napi\_object\_expected | 入参js\_object不是SendableObject类型 | 确保入参正确 |
| napi\_wrap\_sendable | 包裹一个native实例到ArkTS对象中。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_wrap\_sendable\_with\_size | 包裹一个native实例到ArkTS对象中并指定大小。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_wrap\_sendable\_with\_size | 包裹一个native实例到ArkTS对象中并指定大小。 | napi\_invalid\_arg | 入参js\_object为nullptr | 确保入参正确 |
| napi\_wrap\_sendable\_with\_size | 包裹一个native实例到ArkTS对象中并指定大小。 | napi\_invalid\_arg | 入参native\_object为nullptr | 确保入参正确 |
| napi\_wrap\_sendable\_with\_size | 包裹一个native实例到ArkTS对象中并指定大小。 | napi\_object\_expected | 入参js\_object不是SendableObject类型 | 确保入参正确 |
| napi\_wrap\_sendable\_with\_size | 包裹一个native实例到ArkTS对象中并指定大小。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_unwrap\_sendable | 获取ArkTS对象包裹的native实例。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_unwrap\_sendable | 获取ArkTS对象包裹的native实例。 | napi\_invalid\_arg | 入参js\_object为nullptr | 确保入参正确 |
| napi\_unwrap\_sendable | 获取ArkTS对象包裹的native实例。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_unwrap\_sendable | 获取ArkTS对象包裹的native实例。 | napi\_object\_expected | 入参js\_object不是SendableObject类型 | 确保入参正确 |
| napi\_unwrap\_sendable | 获取ArkTS对象包裹的native实例。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_remove\_wrap\_sendable | 移除并获取ArkTS对象包裹的native实例。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_remove\_wrap\_sendable | 移除并获取ArkTS对象包裹的native实例。 | napi\_invalid\_arg | 入参js\_object为nullptr | 确保入参正确 |
| napi\_remove\_wrap\_sendable | 移除并获取ArkTS对象包裹的native实例。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_remove\_wrap\_sendable | 移除并获取ArkTS对象包裹的native实例。 | napi\_object\_expected | 入参js\_object不是SendableObject类型 | 确保入参正确 |
| napi\_remove\_wrap\_sendable | 移除并获取ArkTS对象包裹的native实例。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_wrap\_enhance | 在ArkTS对象上绑定一个native对象实例并指定实例大小，运行时会统计传入的实例大小并将其累加，当累计大小达到GC触发阈值时，运行时会启动垃圾回收流程。开发者可以指定绑定的回调函数是否异步执行，如果是异步执行，回调函数必须保证是线程安全的。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_wrap\_enhance | 在ArkTS对象上绑定一个native对象实例并指定实例大小，运行时会统计传入的实例大小并将其累加，当累计大小达到GC触发阈值时，运行时会启动垃圾回收流程。开发者可以指定绑定的回调函数是否异步执行，如果是异步执行，回调函数必须保证是线程安全的。 | napi\_invalid\_arg | 入参js\_object为nullptr | 确保入参正确 |
| napi\_wrap\_enhance | 在ArkTS对象上绑定一个native对象实例并指定实例大小，运行时会统计传入的实例大小并将其累加，当累计大小达到GC触发阈值时，运行时会启动垃圾回收流程。开发者可以指定绑定的回调函数是否异步执行，如果是异步执行，回调函数必须保证是线程安全的。 | napi\_invalid\_arg | 入参native\_object为nullptr | 确保入参正确 |
| napi\_wrap\_enhance | 在ArkTS对象上绑定一个native对象实例并指定实例大小，运行时会统计传入的实例大小并将其累加，当累计大小达到GC触发阈值时，运行时会启动垃圾回收流程。开发者可以指定绑定的回调函数是否异步执行，如果是异步执行，回调函数必须保证是线程安全的。 | napi\_object\_expected | 入参js\_object不是ArkTS Object类型 | 确保入参正确 |
| napi\_wrap\_enhance | 在ArkTS对象上绑定一个native对象实例并指定实例大小，运行时会统计传入的实例大小并将其累加，当累计大小达到GC触发阈值时，运行时会启动垃圾回收流程。开发者可以指定绑定的回调函数是否异步执行，如果是异步执行，回调函数必须保证是线程安全的。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_create\_ark\_context | 创建一个新的运行时上下文环境。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_ark\_context | 创建一个新的运行时上下文环境。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_switch\_ark\_context | 切换到指定的运行时上下文环境。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_switch\_ark\_context | 切换到指定的运行时上下文环境。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_destroy\_ark\_context | 销毁通过接口napi\_create\_ark\_context创建的一个上下文环境。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_destroy\_ark\_context | 销毁通过接口napi\_create\_ark\_context创建的一个上下文环境。 | napi\_pending\_exception | 调用该接口前或调用过程中出现未捕获的ArkTS异常 | 根据异常信息（hilog/crash栈）处理异常 |
| napi\_open\_critical\_scope | 打开临界区作用域 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_open\_critical\_scope | 打开临界区作用域 | napi\_invalid\_arg | 入参scope为nullptr | 确保入参正确 |
| napi\_close\_critical\_scope | 关闭临界区作用域 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_close\_critical\_scope | 关闭临界区作用域 | napi\_invalid\_arg | 入参scope为nullptr | 确保入参正确 |
| napi\_get\_buffer\_string\_utf16\_in\_critical\_scope | 获取ArkTS String的UTF-16编码内存缓冲区数据 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_buffer\_string\_utf16\_in\_critical\_scope | 获取ArkTS String的UTF-16编码内存缓冲区数据 | napi\_invalid\_arg | 入参value为nullptr | 确保入参正确 |
| napi\_get\_buffer\_string\_utf16\_in\_critical\_scope | 获取ArkTS String的UTF-16编码内存缓冲区数据 | napi\_invalid\_arg | 入参buffer为nullptr | 确保入参正确 |
| napi\_get\_buffer\_string\_utf16\_in\_critical\_scope | 获取ArkTS String的UTF-16编码内存缓冲区数据 | napi\_invalid\_arg | 入参length为nullptr | 确保入参正确 |
| napi\_create\_strong\_reference | 创建指向ArkTS对象的强引用 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_strong\_reference | 创建指向ArkTS对象的强引用 | napi\_invalid\_arg | 入参value为nullptr | 确保入参正确 |
| napi\_create\_strong\_reference | 创建指向ArkTS对象的强引用 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_delete\_strong\_reference | 删除强引用 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_delete\_strong\_reference | 删除强引用 | napi\_invalid\_arg | 入参ref为nullptr | 确保入参正确 |
| napi\_get\_strong\_reference\_value | 根据强引用对象获取其关联的ArkTS对象值 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_strong\_reference\_value | 根据强引用对象获取其关联的ArkTS对象值 | napi\_invalid\_arg | 入参ref为nullptr | 确保入参正确 |
| napi\_get\_strong\_reference\_value | 根据强引用对象获取其关联的ArkTS对象值 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_external\_string\_utf16 | 需要通过外部UTF-16编码的字符串缓冲区创建ArkTS字符串值且避免内存拷贝时使用此函数。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_external\_string\_utf16 | 需要通过外部UTF-16编码的字符串缓冲区创建ArkTS字符串值且避免内存拷贝时使用此函数。 | napi\_invalid\_arg | 入参str为nullptr | 确保入参正确 |
| napi\_create\_external\_string\_utf16 | 需要通过外部UTF-16编码的字符串缓冲区创建ArkTS字符串值且避免内存拷贝时使用此函数。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_external\_string\_utf16 | 需要通过外部UTF-16编码的字符串缓冲区创建ArkTS字符串值且避免内存拷贝时使用此函数。 | napi\_invalid\_arg | 入参length不等于NAPI\_AUTO\_LENGTH或length大于INT\_MAX | 确保入参length等于NAPI\_AUTO\_LENGTH且length不大于INT\_MAX |
| napi\_create\_external\_string\_ascii | 需要通过外部ASCII编码的字符串缓冲区创建ArkTS字符串值且避免内存拷贝时使用此函数。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_external\_string\_ascii | 需要通过外部ASCII编码的字符串缓冲区创建ArkTS字符串值且避免内存拷贝时使用此函数。 | napi\_invalid\_arg | 入参str为nullptr | 确保入参正确 |
| napi\_create\_external\_string\_ascii | 需要通过外部ASCII编码的字符串缓冲区创建ArkTS字符串值且避免内存拷贝时使用此函数。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_external\_string\_ascii | 需要通过外部ASCII编码的字符串缓冲区创建ArkTS字符串值且避免内存拷贝时使用此函数。 | napi\_invalid\_arg | 入参length不等于NAPI\_AUTO\_LENGTH或length大于INT\_MAX | 确保入参length等于NAPI\_AUTO\_LENGTH且length不大于INT\_MAX |
| napi\_create\_strong\_sendable\_reference | 创建指向Sendable ArkTS对象的Sendable强引用。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_create\_strong\_sendable\_reference | 创建指向Sendable ArkTS对象的Sendable强引用。 | napi\_invalid\_arg | 入参value为nullptr | 确保入参正确 |
| napi\_create\_strong\_sendable\_reference | 创建指向Sendable ArkTS对象的Sendable强引用。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_create\_strong\_sendable\_reference | 创建指向Sendable ArkTS对象的Sendable强引用。 | napi\_invalid\_arg | 入参env不是main context | 确保入参正确 |
| napi\_create\_strong\_sendable\_reference | 创建指向Sendable ArkTS对象的Sendable强引用。 | napi\_object\_expected | 入参value不是sendable的 | 确保入参正确 |
| napi\_delete\_strong\_sendable\_reference | 删除Sendable强引用。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_delete\_strong\_sendable\_reference | 删除Sendable强引用。 | napi\_invalid\_arg | 入参ref为nullptr | 确保入参正确 |
| napi\_delete\_strong\_sendable\_reference | 删除Sendable强引用。 | napi\_invalid\_arg | 入参env不是main context | 确保入参正确 |
| napi\_delete\_strong\_sendable\_reference | 删除Sendable强引用。 | napi\_generic\_failure | 从napi\_sendable\_ref中获取的napi\_value不是sendable的 | 确保入参正确 |
| napi\_get\_strong\_sendable\_reference\_value | 根据Sendable强引用获取其关联的ArkTS对象值。 | napi\_invalid\_arg | 入参env为nullptr | 确保入参正确 |
| napi\_get\_strong\_sendable\_reference\_value | 根据Sendable强引用获取其关联的ArkTS对象值。 | napi\_invalid\_arg | 入参ref为nullptr | 确保入参正确 |
| napi\_get\_strong\_sendable\_reference\_value | 根据Sendable强引用获取其关联的ArkTS对象值。 | napi\_invalid\_arg | 入参result为nullptr | 确保入参正确 |
| napi\_get\_strong\_sendable\_reference\_value | 根据Sendable强引用获取其关联的ArkTS对象值。 | napi\_invalid\_arg | 入参env不是main context | 确保入参正确 |
| napi\_get\_strong\_sendable\_reference\_value | 根据Sendable强引用获取其关联的ArkTS对象值。 | napi\_generic\_failure | 从napi\_sendable\_ref中获取的napi\_value不是sendable的 | 确保入参正确 |
