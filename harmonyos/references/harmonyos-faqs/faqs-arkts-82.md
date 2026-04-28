---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-82
title: 是否支持在TS文件中加载ArkTS文件，TS是否会被限制使用
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 是否支持在TS文件中加载ArkTS文件，TS是否会被限制使用
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:05+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5dfce18bb5f1763d299384881989f9bbbc31ad4135cb2581a9559f589762c9ec
---

不支持在TS文件中调用ArkTS文件。对于ArkTS中禁用的语法，例如：with语句等，可以考虑在TS文件中编写相关内容，再在ArkTS文件中调用。

不会限制使用TS/JS文件，但会在TS/JS文件中限制import ets文件。
