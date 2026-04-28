---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-17
title: 环境中配置使用JDK25，打包失败报错，错误码：00303153 Configuration Error
breadcrumb: FAQ > DevEco Studio > 环境准备 > 环境中配置使用JDK25，打包失败报错，错误码：00303153 Configuration Error
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:55+08:00
doc_updated_at: 2026-04-08
content_hash: sha256:db471053336f80335e716ed1353868498a545ec1257b339dae86c90c082701cd
---

**问题现象**

在使用6.0.2.640版本的DevEco Studio和Command Line Tools时，若系统环境中配置使用JDK25，在命令行中执行打包命令会导致打包失败，报错信息如下图所示：

```
1. ERROR： 00303153 Configuration Error
```

**问题原因**

JDK25版本中JDK-8370216的接口行为变更，导致打包问题。

**解决措施**

使用系统命令行终端执行 java --version，判断是否默认使用JDK25版本，如果使用JDK25版本，有以下两种方案可解决本问题：

方案一：系统环境变量配置为低于JDK25的版本。

方案二：升级DevEco Studio和Command Line Tools到6.0.2.642及以上版本（建议）。
