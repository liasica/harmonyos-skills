---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/applinking-glossary
title: App Linking Kit术语
breadcrumb: 指南 > 应用服务 > App Linking Kit（应用链接服务） > App Linking Kit术语
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:53+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:423044f8cb7df81211006d468014ec1937502316a40aa897ddacbebadd8beb31
---

## C

### Cross-Platform Link；聚合链接

App Linking Kit提供的按指定方式跳转至应用的能力。支持按照开发者指定的方式进行跳转，引导用户跳转到HarmonyOS平台预览页、应用市场详情页、自定义网址、深度链接地址等页面。

## D

### Deferred Link；延迟链接

App Linking Kit提供的延迟跳转至应用详情页的能力。当用户点击应用推广链接但应用未安装时，系统自动缓存用户点击信息（有效期10分钟、最多50条），待用户安装并启动应用后，仍可获取之前的点击参数，避免转化率损失。

### Direct Access to AppGallery；直达应用市场

App Linking Kit提供的跳转至应用市场下载详情页的能力。当应用已安装时，点击链接直接跳转应用；当应用未安装时，点击链接跳转应用市场下载详情页，引导用户下载应用。

### Domain Verification；域名校验

App Linking对链接域名进行合法性验证的安全机制。通过域名校验，可帮助用户消除歧义，识别合法归属于域名的应用，使链接更加安全可靠。
