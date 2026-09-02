---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-23
title: "安装HAP时提示“error: failed to start ability”"
breadcrumb: "FAQ > DevEco Studio > 应用调试 > 安装HAP时提示“error: failed to start ability”"
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:56+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:2ae4380888d8d4c5f9dad24b5d68f4370787a01428ed8e710350c0c8112e4260
---

**问题现象**

启动调试或运行应用/服务时，如果安装HAP出错，提示“error: failed to start ability. error: ability visible false deny request”，请检查应用的可见性设置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/_69LUbkyTRKYlqMOPW_B_g/zh-cn_image_0000002654798147.png)

**解决措施**

* 在Stage模型工程的module.json5文件中，将abilities字段内的exported设置为true。
* FA模型工程：在config.json文件的abilities字段中，将visible设置为true。
