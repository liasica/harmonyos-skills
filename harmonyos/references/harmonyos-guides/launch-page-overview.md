---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/launch-page-overview
title: 应用启动页简介
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 应用启动页的配置与使用 > 应用启动页简介
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:46+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f21ad5766232e8eba0aa941321b7015e0aec73eeae4b5cdf4acddac1d1ff66f8
---

启动页（Starting Window）是应用冷启动时显示的首个页面，在应用进程没有运行或者应用内容没有加载完成前，都将显示启动页。同时承载了应用展示品牌特性的功能，应用可以根据自己的设计配置资源，用于展示产品独特的标识，加强用户对产品的认知。

## 启动页展示场景

应用展示启动页主要包括如下场景，建议应用在进行启动页设计时，同时考虑如下场景的显示效果。

* 应用冷启动

  应用在没有后台进程的情况下启动，会先展示启动页。启动页到应用内容有200ms的透明渐隐动效过渡。
* 多任务卡片

  在应用还处于启动页阶段时退出到后台，多任务中将会展示该应用的启动页。
* 应用主动销毁退出

  当应用主动销毁，且系统侧未生成快照时，会在应用退出动效中展示为启动页。
