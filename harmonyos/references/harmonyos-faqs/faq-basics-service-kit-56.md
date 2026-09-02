---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-56
title: Pocket2和PuraX机型进行UI适配，怎么区分
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > Pocket2和PuraX机型进行UI适配，怎么区分
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:39+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a6989fa5ae99f4b00729c88573d7f6b1c773fb625f7774232ae9fcf19a994af5
---

## 问题现象

Pocket2和PuraX机型进行UI适配，请问怎么区分这两个机型？

## 解决方案

Pocket2和PuraX机型在展开态时都是横向断点sm，纵向断点lg，无法通过断点区分。可根据当前机型来判断，通过[设备信息](../harmonyos-references/js-apis-device-info.md)的marketName字段获取外部产品系列名称。
