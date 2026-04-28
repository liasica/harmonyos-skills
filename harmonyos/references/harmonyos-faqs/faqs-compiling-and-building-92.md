---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-92
title: arm64，armv7，x86_64 三种架构的适用范围
breadcrumb: FAQ > DevEco Studio > 编译构建 > arm64，armv7，x86_64 三种架构的适用范围
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:26+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:cb270d1d96ce794653726eaf75405a02e32f1dbab9176b0cefb606cf22dfab1b
---

**问题描述**

创建的 Native C++ 项目，默认支持三种架构：arm64、armv7 和 x86\_64。这些架构，分别用在什么地方？

在 DevEco-Studio 3.1.1 release 版本中，模拟器支持仅使用 arm64。

在 DevEco-Studio Next Preview1 版本中，Next 真机仅支持使用 arm64。

是否需要对外提供 armv7 和 x86\_64 的 SDK？这两种架构分别在什么情况下会被使用？

**解决方案**

arm64：这是一种64位的ARM架构，适用于现代移动设备和嵌入式系统，如智能手机、平板电脑、物联网设备等。

armv7：这是一种32位的ARM架构，适用于早期移动设备和低功耗物联网设备。

x86\_64：这是一种64位的x86架构，适用于桌面电脑、服务器和基于x86处理器的虚拟机。无需额外提供armv7和x86\_64版本。
