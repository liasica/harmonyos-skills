---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-151
title: ArkTS自定义注解使用场景
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > ArkTS自定义注解使用场景
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:20+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ad5a00ac779273a270dea4d705330906a9e01b31f4dbfff06ecececa2edf9a1b
---

开发者使用自定义注解时，注解信息会在编译阶段被写入生成的方舟字节码文件中。方舟编译工具链提供了编译期自定义修改方舟字节码的能力。

基于该能力，开发者可以使用社区提供的[AbcKit](https://gitcode.com/openharmony/arkcompiler_runtime_core/tree/master/libabckit)库，对方舟字节码文件进行分析和修改。libabckit支持扫描字节码中的注解信息，并根据此信息修改字节码，相关用法可参考libabckit提供的文档（详见：[libabckit文档](https://gitcode.com/openharmony/arkcompiler_runtime_core/tree/master/libabckit/doc)）和场景示例（详见：[Router table](https://gitcode.com/openharmony/arkcompiler_runtime_core/tree/master/libabckit/tests/clean_scenarios/c_api/dynamic/router_table)）。

**参考链接**

[编译期自定义修改方舟字节码](../harmonyos-guides/customize-bytecode-during-compilation.md)
