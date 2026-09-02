---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-55
title: 应用运行报错：hap path error
breadcrumb: FAQ > DevEco Studio > 应用调试 > 应用运行报错：hap path error
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:a8006b7eb6c31ceaa07b287bb5a4e25c7c719106fb343bb5352d946371092c32
---

**问题现象**

启动调试或运行应用/服务时，应用运行崩溃，提示错误信息“errorMsg: hap path error”。

**解决措施**

如果依赖的应用包未安装，建议进入**Run/Debug Configurations > Deploy Multi Hap****/Hsp**页签，勾选**Deploy Multi Hap/Hsp Packages**，选择所需依赖的应用包，然后重新运行应用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/VjDQhbbsR9OHHNvfT2aQjQ/zh-cn_image_0000002654798169.png)
