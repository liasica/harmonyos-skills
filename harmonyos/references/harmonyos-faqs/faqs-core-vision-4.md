---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-core-vision-4
title: AI服务Cannot read property xxx of undefined报错
breadcrumb: FAQ > AI功能开发 > 机器学习 > 基础视觉（Core Vision） > AI服务Cannot read property xxx of undefined报错
category: harmonyos-faqs
scraped_at: 2026-09-02T14:55:00+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:5caecf76e3d44d301cae005ad5685f131bce330e81f8a33502cb484fde57eeb1
---

## 问题现象

当接入AI服务遇到Cannot read property xxx of undefined报错。如，接入文字转语音遇到Cannot read property createEngine of undefined报错，接入图文识别能力遇到Cannot read property recognizeText of undefined报错，如何解决。

## 解决方案

此类报错基本都是通过模拟器测试AI能力时出现。当前所有AI能力无法在模拟器中使用，模拟器能力支持情况详见[文档](../harmonyos-guides/ide-emulator-specification.md)。

## 总结

请勿使用模拟器测试AI能力。
