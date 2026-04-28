---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-faq-29
title: 按需加载场景中，应用在加载指定模块后重启，还是已加载状态吗？是否需要重新发起按需加载请求？
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > AppGallery Kit常见问题 > 按需加载场景中，应用在加载指定模块后重启，还是已加载状态吗？是否需要重新发起按需加载请求？
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:28+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5a9727a9880ede9bf5338037809865edb7e4b5aff93922a1bda0bbb8c2b520c9
---

在这种情况下，无需重新发起按需加载请求。产品特性按需分发服务分为两部分：按需加载安装和动态引入模块。只要已经下载安装了应用，就完成了按需下载安装。动态引入是运行时，即应用运行状态下去查找指定模块。
