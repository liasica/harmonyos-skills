---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-64
title: 系统使用了ArkTS作为开发语言，那这些代码在底层的解释运行的环境是自研的还是用的开源的，比如v8、jscore？另外系统也适配了React Native引擎，是不是也是复用的这个运行环境
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 系统使用了ArkTS作为开发语言，那这些代码在底层的解释运行的环境是自研的还是用的开源的，比如v8、jscore？另外系统也适配了React Native引擎，是不是也是复用的这个运行环境
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:03+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:786b3b4af6cb3be80f72eade60f66848dfe187648415b502f368a2c0cadaed58
---

1. 系统使用方舟编译器及运行时环境执行应用包中的字节码。字节码由方舟编译工具链从ArkTS、TS或JS源码编译生成。

2. 系统适配的React Native引擎目前运行JS源码，使用系统提供的V8引擎。
