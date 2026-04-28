---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-75
title: 如何解决构建流水线提示Couldn't find hvigor/hvigor-wrapper.js的问题
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何解决构建流水线提示Couldn't find hvigor/hvigor-wrapper.js的问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:23+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:eddf50da479db86816524362f71a1ac25b10d98fcb3c38bce1a2e1ca3113fb59
---

1. hvigorw脚本依赖于hvigor-wrapper.js。
2. 在工程外部使用脚本进行编译时：
   1. 确认hvigor-wrapper.js文件是否位于工程的hvigor文件夹中。
   2. 根据文档：[搭建流水线](../harmonyos-guides/ide-command-line-building-app.md#section14397105115226)，需要先cd到工程的根目录，再调用.hvigorw的各种命令。
