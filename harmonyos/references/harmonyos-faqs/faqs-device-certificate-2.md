---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-device-certificate-2
title: 证书链校验器的参数如何获取
breadcrumb: FAQ > 系统开发 > 安全 > 证书管理（Device Certificate） > 证书链校验器的参数如何获取
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:03+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a0bed08b041c7b765f10c7a0acc2c7bb07ff8cde3d2c19512a0ba347638991b5
---

可通过[getSubjectName](../harmonyos-references/js-apis-cert.md#getsubjectname)和[getPublicKey](../harmonyos-references/js-apis-cert.md#getpublickey)接口获取CASubject和CAPubKey的字节数据，然后将值传入CertChainValidationParameters。
