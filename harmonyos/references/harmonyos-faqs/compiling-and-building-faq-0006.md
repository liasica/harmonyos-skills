---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/compiling-and-building-faq-0006
title: FA模型config.json配置错误编译报错问题排查
breadcrumb: FAQ > DevEco Studio > 编译构建 > 常见问题 > FA模型config.json配置错误编译报错问题排查
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:51+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:d028cc4ce63264744fd1bc2ad44ea094006790bcd346656d2ce8e0e51a6527b6
---

**Q：编译报错“Failed to obtain the module type.”如何解决？**

**A**：错误描述：未找到指定的模块类型。

可能原因：在FA模型中，config.json文件中的module/distro/moduleType字段缺失或配置错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/swafKztiR8mub1Vv0ss6Tw/zh-cn_image_0000002793773235.png "点击放大")

解决措施：确保在FA模型的config.json文件中，module/distro/moduleType字段存在且配置正确。
