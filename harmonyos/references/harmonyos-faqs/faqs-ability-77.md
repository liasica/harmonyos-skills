---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-77
title: 应用、元服务和卡片是什么关系
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 应用、元服务和卡片是什么关系
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:49+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:bc46d2f5d303181dcf6cc0177fe887f99b685230a23ee08583c08247c6d5824b
---

元服务是一种应用，没有图标，支持免安装启动。

应用和元服务不能共享包名，必须分别打包；元服务和应用之间是独立的，也不能共享 entry 模块。

应用和元服务都可以拥有卡片。

元服务的卡片在手机上表现为桌面卡片。长按桌面上已添加的任意卡片，如图库、备忘录，在弹出的菜单中选择“卡片中心”，进入卡片中心页面，可以找到卡片并添加到桌面。
