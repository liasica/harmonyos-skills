---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-58
title: 能否同步webview的cookie与app中的cookie
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 能否同步webview的cookie与app中的cookie
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:43+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:0849cc4e1a7d5722fb247653ab3fa741b7ff507a1660ec762ca9ab518c2c652a
---

由于App和Web组件属于不同的应用程序域且会话上下文独立，二者的请求通常使用不同的Cookie进行身份验证和会话管理。当App采用WebView加载同源页面时，可通过CookieManager实现Cookie同步。例如，如果用户在Web浏览器中登录了一个网站，并且该网站也有一个App，那么该App可能使用与Web浏览器相同的Cookie来验证用户身份和管理会话。
