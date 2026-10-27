---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-92
title: 预置应用（未上架应用市场），是否需在HarmonyOS 开发者中心创建APPID
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 预置应用（未上架应用市场），是否需在HarmonyOS 开发者中心创建APPID
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:46+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:6c8da89bb24b71b4319559fdcb5b19318eaf828b17fe1369977e9ace40424d41
---

## 问题现象

预置应用使用了自定义签名和HarmonyOS 开发者中心证书打包，同时开发中需要调用定时任务、闹钟等依赖APPID的系统能力。是否需要先在HarmonyOS 开发者中心创建应用？

## 解决方案

是的，需要先在HarmonyOS 开发者中心创建应用以获取APPID。

APPID是应用开发与发布的关键要素，是识别应用的唯一标识。

无论应用是否上架华为应用市场，都必须在HarmonyOS 开发者中心中创建HarmonyOS应用，以此生成合法且唯一的APPID。

参考文档：[创建HarmonyOS应用](../app/agc-help-create-app-0000002247955506.md)。
