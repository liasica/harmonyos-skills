---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-87
title: 编译报错：platform/OHOS to use this system, please post your config file on discourse.cmake.org so it
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错：platform/OHOS to use this system, please post your config file on discourse.cmake.org so it
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:26+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:cb8d795a8f5070b275db293b452e31dd7fe543cf00e801de5949a7dcd11736c5
---

**问题描述**

在编译C++库时出现多条警告。

要使用此系统，请将配置文件发布到 discourse.cmake.org。

这个是否会带来影响？

**解决方案**

问题源于Mac的SDK中缺少OHOS.cmake文件。

在SDK存放目录的default/base/native/build-tools/cmake/share/cmake-3.16/Modules/Platform层级下，新建名为OHOS.cmake的文件，并写入以下内容：include(Platform/Linux)。
