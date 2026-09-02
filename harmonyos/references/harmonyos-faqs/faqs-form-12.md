---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-form-12
title: 应用桌面服务卡片上图片显示不全
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 卡片开发（Form） > 应用桌面服务卡片上图片显示不全
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:774753842f2fb66d8b73fc14753897b65b564cf37000a942501867fc8b396231
---

## 问题现象

应用通过将卡片添加到桌面上展示应用内图片，未调整图片大小及显示方式，导致图片在卡片视图下显示不全。

## 背景知识

* [Image](../harmonyos-references/ts-basic-components-image.md)：Image为图片组件，常用于在应用中显示图片。
* [服务卡片](../harmonyos-guides/formkit-overview.md)：Form Kit（卡片开发框架）提供了一种在桌面、锁屏等系统入口嵌入显示应用信息的开发框架和API，可以将应用内用户关注的重要信息或常用操作抽取到服务卡片（以下简称“卡片”）上。

## 问题定位

建议检查服务卡片代码中针对图片展示设置是否使用objectFit设置了图片的填充方式为Contain，确保图片保持宽高比的同时，也可以完整的展示在卡片视图内。当填充方式设置有误时，系统会通过视图尺寸裁剪图片，导致出现图片显示不全的现象。

## 分析结论

应用未考虑到卡片的尺寸较小，未调整图片尺寸以及objectFit填充效果，导致大尺寸图片在服务卡片上显示时展示不全。

## 修改建议

针对卡片小尺寸，调整图片尺寸以及填充方式，确保图片可以完整的在卡片上显示。部分填充方式区别可见[图像填充效果](../harmonyos-references/ts-basic-components-image.md#示例10为图像设置填充效果)。
