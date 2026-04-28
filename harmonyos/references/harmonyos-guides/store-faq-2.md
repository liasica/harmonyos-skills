---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-faq-2
title: 按需加载场景中加载动态模块失败
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > AppGallery Kit常见问题 > 按需加载场景中加载动态模块失败
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:26+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a446675ff279621afa564cda396a2e243fd524bd7709bd3fb4f712544e255cd2
---

**问题现象**

调用加载接口时加载模块失败。

**解决措施**

支持按需加载的应用需要先上架到应用市场，然后从应用市场下载应用包。应用包安装后才能在应用中调用动态下载接口。开发者通过本地DevEco Studio编译的示例包无法直接调用下载接口。
