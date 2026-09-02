---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-pdf-19
title: PDF添加水印是替换还是叠加
breadcrumb: FAQ > 应用服务开发 > PDF文档解析服务（PDF Kit） > PDF添加水印是替换还是叠加
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2a06834fa1e94857ec7eb4f06ff6e074f9aa9fc2a7cb1ac876066cd7077e55ea
---

## 问题现象

PDF添加水印、背景、前景方法的行为是替换还是叠加？

## 解决方案

水印、背景、前景均以独立图层叠加到原始文档上。

PDF原始内容不受影响，仅新增装饰性图层（水印/背景等）。

可同时叠加多种元素（如文本水印+图片背景），通过opacity控制层叠效果。
