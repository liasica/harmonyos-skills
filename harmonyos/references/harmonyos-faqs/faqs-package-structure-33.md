---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-33
title: HSP包编译之后的.har文件的作用是什么
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > HSP包编译之后的.har文件的作用是什么
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:31+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:fe58d7f294b9f11d6a669c7f46d1d6278cca8b54d20e136953435b81329047ed
---

HSP包编译后会生成.hsp文件和.har文件。.hsp文件用于安装，.har文件仅暴露接口，不包含具体实现。

HSP包中导出的方法头文件位于.har文件中，实现在.hsp文件中。
