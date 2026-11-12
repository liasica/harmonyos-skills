---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-config-agc
title: 开发准备
breadcrumb: 指南 > 媒体 > Scan Kit（统一扫码服务） > 开发准备
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:09+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:d5352d856d01b413f324cd0c7258c232a6f23bf9ac3f723fe858abfe05a8cc1a
---

1. 参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作。
2. （**仅针对“扫码直达”必选**）接入[App Linking](app-linking-startupapp.md)，您需要完成以下步骤：

   1. 在HarmonyOS 开发者中心平台开通App Linking服务。
   2. 在开发者网站上关联应用。
   3. 在App Linking中配置二维码、条形码关联的网址域名。
   4. 在应用的module.json5文件中关联域名。

**说明** 

* App Linking方式当前仅支持HTTPS网址，具备应用和网页两种呈现方式。当应用安装时则优先直达应用内服务页，当应用未安装时，浏览器也可以为用户提供服务。
* App Linking还广泛应用于社交分享、沉默唤醒、广告引流等场景。
* 接入App Linking不能使用DevEco的自动签名功能，必须使用[手动签名](ide-signing-manual.md)。
