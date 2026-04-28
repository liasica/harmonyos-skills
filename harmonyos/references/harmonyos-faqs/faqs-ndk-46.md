---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-46
title: Native C++模板中，生成的so库的名称在哪里定义，需要与哪些内容保持一致
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > Native C++模板中，生成的so库的名称在哪里定义，需要与哪些内容保持一致
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:37+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:56f29ee2f704ef896a658f8a3416f23d6f3a3c814e08fd764747a1b9146a47cc
---

导入使用的模块名和注册时的模块名大小写保持一致。例如，模块名为 entry，则so的名字为libentry.so，napi\_module中nm\_modname字段应为entry，ArkTS侧使用时，代码为：import xxx from 'libentry.so'。
