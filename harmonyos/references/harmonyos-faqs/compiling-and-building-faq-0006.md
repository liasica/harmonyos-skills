---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/compiling-and-building-faq-0006
title: FA模型config.json配置错误编译报错问题排查
breadcrumb: FAQ > DevEco Studio > 编译构建 > 常见问题 > FA模型config.json配置错误编译报错问题排查
category: harmonyos-faqs
scraped_at: 2026-10-21T07:12:39+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:408135f141b56f5b9343acb540cf18b7dfb19bc518d232d7ae37d4262f00702d
---

**Q：编译报错“Failed to obtain the module type.”如何解决？**

**A**：错误描述：未找到指定的模块类型。

可能原因：在FA模型中，config.json文件中的module/distro/moduleType字段缺失或配置错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/jlpDIFM7QSCaxTDi-ESeFQ/zh-cn_image_0000002793773235.png "点击放大")

解决措施：确保在FA模型的config.json文件中，module/distro/moduleType字段存在且配置正确。
