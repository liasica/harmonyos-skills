---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-112
title: HarmonyOS是否限制App进程fork子进程，是否允许app里自带的可执行文件运行（fork+exec）执行，并通过ptrace方式读取自身进程？这种方式以后是否会限制并禁止
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > HarmonyOS是否限制App进程fork子进程，是否允许app里自带的可执行文件运行（fork+exec）执行，并通过ptrace方式读取自身进程？这种方式以后是否会限制并禁止
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:52+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:cc789f8a36513e319ed40ce3069ef09e2f2b97bd8ad794890c3877efea11e9c5
---

**解决方案**

系统限制普通应用直接进行Fork进程操作；手机产品不允许普通应用直接创建进程。
