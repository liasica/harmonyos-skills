---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-23
title: "安装HAP时提示“error: failed to start ability”"
breadcrumb: "FAQ > DevEco Studio > 应用调试 > 安装HAP时提示“error: failed to start ability”"
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:23+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:7e2404f951354056d1a3df990011ee256b8192b57f26ae1714428b415cc6f5cf
---

**问题现象**

启动调试或运行应用/服务时，如果安装HAP出错，提示“error: failed to start ability. error: ability visible false deny request”，请检查应用的可见性设置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/-_1hPEeKSFOAF5f2_ZS85g/zh-cn_image_0000002229758621.png)

**解决措施**

* 在Stage模型工程的module.json5文件中，将abilities字段内的exported设置为true。
* FA模型工程：在config.json文件的abilities字段中，将visible设置为true。
