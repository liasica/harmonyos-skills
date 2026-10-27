---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-63
title: HarmonyOS 开发者中心的控制台无法选择要提交的新版本
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > HarmonyOS 开发者中心的控制台无法选择要提交的新版本
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:46+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:043490aa52437c6516e8cc92c442c1a234aacbe4ceb1566cdee9b7f83dafa696
---

## 问题现象

HarmonyOS 开发者中心的控制台进行新版本提交，无法选择需要提交的新版本。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/I-SoDFj8SlKLFDHYu7D92w/zh-cn_image_0000002628554516.png "点击放大")

## 解决方案

1. 在“上传包”窗口，先选择“使用场景”，然后点击“+”上传软件包。若软件包需要在全网正式发布，请选择“测试和正式上架”，根据需求选择是否在中国大陆发布。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/Od8Lcuo2RBKViwniiXTM_Q/zh-cn_image_0000002658913839.png "点击放大")
2. 配置发布国家或地区，选择“特定国家或地区”：应用仅在所选国家或地区发布。其中，发布国家的中国大陆选项选择需与“上传包”窗口中的选择保持一致。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/AyBsThqaRZm93hhtK8uV-Q/zh-cn_image_0000002658793897.png "点击放大")

## 总结

如果上传包时选择中国大陆，则发布国家必须包含中国大陆；如果上传包时没有选择中国大陆，则发布国家必须不包含中国大陆；如果不一致，则重新上传即可。
