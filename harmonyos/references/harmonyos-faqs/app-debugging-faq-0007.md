---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/app-debugging-faq-0007
title: DevEco Studio C/C++断点调试配置问题排查
breadcrumb: FAQ > DevEco Studio > 应用调试 > 常见问题 > DevEco Studio C/C++断点调试配置问题排查
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:59+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:c2738a3964a7e82c41b1da323b6d9b69c450b5ffc6356020694df09fa9ef3c6d
---

**Q：在DevEco Studio上的C/C++代码处打断点，调试运行时断点不生效。**

**A**：DevEco Studio进行ArkTS/JS + Native混合调试时需要配置DevEco Studio的调试模式。选择配置项：Run/Debug Configurations > Debugger > Dual(ArkTS/JS + Native)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/7sXQ38ZlQfqz0lNfxkpvZA/zh-cn_image_0000002800299111.png "点击放大")
