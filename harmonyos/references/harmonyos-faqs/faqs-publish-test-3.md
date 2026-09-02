---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-publish-test-3
title: 测试报告中，为什么会批量出现待检测项
breadcrumb: FAQ > DevEco Testing > 上架预检 > 测试报告中，为什么会批量出现待检测项
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:59+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:8e9894638198c65f38ceff5cdbf82e3968979b214a368e1edfd2fe8964a23034
---

由于测试任务内部异常，偶现任务终止的情况。请查看【测试报告-执行日志】，如果应用信息为空，请重新创建任务并执行测试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/1uv44p_fReetxqhkWuhOHA/zh-cn_image_0000002654798345.png)

该问题由应用信息未完全解析导致。再次创建任务时，请等待右侧应用信息加载完成，再进行创建，即可解决该问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/jkHizuUuS2ewrft9ta6mqw/zh-cn_image_0000002624638880.png "点击放大")
