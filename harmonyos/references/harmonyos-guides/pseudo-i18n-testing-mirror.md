---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pseudo-i18n-testing-mirror
title: 界面镜像伪本地化测试
breadcrumb: 指南 > 应用框架 > Localization Kit（本地化开发服务） > 本地化测试 > 伪本地化测试 > 界面镜像伪本地化测试
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:49+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f01342e132c10de5f807d0ffc0962ec565262c8c8fe700b36dd7f25632aeba8c
---

## 使用场景

界面镜像测试主要检查文字阅读顺序是否出现问题。一些语言的阅读顺序不是从左到右。例如，在阿拉伯语中，界面的阅读顺序是从右到左（RTL）。

## 测试流程

1. 切换到伪本地化测试区域，如“ar-XB”。

   说明

   测试区域的切换接口为系统接口，需由系统应用调用。系统应用切换测试区域成功后，普通应用可以进行伪本地化测试。
2. 遍历需要测试的APP。

## 测试事项

1. 检查界面布局、文字方向和控制逻辑是否符合从右至左的阅读习惯。具体要点见[界面镜像](i18n-ui-design.md#界面镜像)章节。
2. 检查相关功能是否异常无法使用。
