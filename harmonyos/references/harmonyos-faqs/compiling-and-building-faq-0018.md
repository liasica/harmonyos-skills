---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/compiling-and-building-faq-0018
title: arm64、armv7、x86_64三种架构的适用范围
breadcrumb: FAQ > DevEco Studio > 编译构建 > 常见问题 > arm64、armv7、x86_64三种架构的适用范围
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:51+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:cb98b36566a7a2d7e2c876b7bb926a6c86bc7ab6c000df0305390d78bcdf0ac6
---

**Q：创建的Native C++项目默认支持三种架构：arm64、armv7和x86\_64。这些架构分别用在什么地方？**

在DevEco Studio 3.1.1 Release版本中，模拟器仅支持使用arm64。

在DevEco Studio Next Preview1版本中，Next真机仅支持使用arm64。

是否需要对外提供armv7和x86\_64的SDK？这两种架构分别在什么情况下会被使用？

**A**：arm64：这是一种64位的ARM架构，适用于现代移动设备和嵌入式系统，如智能手机、平板电脑、物联网设备等。

armv7：这是一种32位的ARM架构，适用于早期移动设备和低功耗物联网设备。

x86\_64：这是一种64位的x86架构，适用于桌面电脑、服务器和基于x86处理器的虚拟机。无需额外提供armv7和x86\_64版本。
