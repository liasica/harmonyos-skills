---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-176
title: HarmonyOS系统浏览器下载内容页面如何获取到文件类型对应的图标
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > HarmonyOS系统浏览器下载内容页面如何获取到文件类型对应的图标
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:33+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7df14e1f51bbb1cf1485fdc521d97f64c4b0316d08c51b5d4a77a66afb082ef5
---

## 问题现象

浏览器下载任务中可以展示下载内容的分类图标，如压缩文件、text、ppt、excel等图片，这个功能是如何实现的。

## 解决方案

浏览器下载任务的图标是预置在浏览器内部的资源文件，根据下载资源的资源类型和资源库内的图标进行匹配后展示。文件类型和大小通过解析下载链接返回的Content-type和Content-size获取。
