---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-model-size-reduction-faqs
title: 常见问题
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 模型优化 > 模型轻量化 > 常见问题
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:68d8466c071a3d3869670b8c1d713b854dde4f9f9b2c2ea70728d1ad8762c684
---

## 模型有多个输入时如何准备数据和填写配置文件？

如果模型定义了多个输入，开发者需要为每个输入节点各准备一份IMAGE或BINARY模式的校准集。如果不同节点所需的输入数据存在对应关系，推荐使用BINARY模式，以免由于读取图片的顺序不同导致非预期行为。在填写量化配置文件时，需要定义与输入节点个数相同的预处理参数，预处理参数的顺序则需要与开发者运行工具时指定的input\_shape顺序一致。

## Unsupported image format! Unsupported image: xxx问题怎么处理？

图片校准集中放入了不支持的图片格式的文件，删除该文件即可。请注意该文件夹下的隐藏文件。
