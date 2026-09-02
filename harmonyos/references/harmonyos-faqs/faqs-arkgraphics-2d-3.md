---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-3
title: 多线程调用OH_Drawing_CreateFontCollection崩溃
breadcrumb: FAQ > 图形开发 > 2D图形（ArkGraphics 2D） > 多线程调用OH_Drawing_CreateFontCollection崩溃
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:46+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2dfd863f8d1a6535f1fe84bb20eafb478dc7a6652cdbc46c0b7ff5b149d0d682
---

## 问题详情

多线程调用OH\_Drawing\_TypographyCreate函数时，handler = OH\_Drawing\_CreateTypographyHandler(typoStyle, OH\_Drawing\_CreateFontCollection())会导致崩溃，而单线程调用则不会。

## 解决措施

该接口不支持多线程并发，但可以在异步线程中调用。
