---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-81
title: 如何通过构建参数传入签名信息
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何通过构建参数传入签名信息
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:24+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5f5d461383c998531da1546ae58bbee965d0bd7c905168752e6d6039f4a3dd1f
---

如何通过构建参数传入签名信息，可参考：[准备申请签名所需文件](../harmonyos-guides/ide-command-line-building-app.md#section6103553181714)。

流水线构建应用可以通过构建命令行传入签名参数，并在自定义构建任务时获取命令行构建参数，但不支持通过自定义任务更改签名的配置。 在编译时进行签名目前可以采取自定义任务的实现方式，在编译打包时插入一个自定义签名任务调用签名工具进行签名，同时屏蔽掉原有的签名流程，可参考：[API使用示例](../harmonyos-guides/ide-build-expanding-sample.md)。
