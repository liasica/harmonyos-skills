---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-publish-test-3
title: 测试报告中，为什么会批量出现待检测项
breadcrumb: FAQ > DevEco Testing > 上架预检 > 测试报告中，为什么会批量出现待检测项
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:52+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ae4e70c76d0ddd3ffc01587d74bc11c39d3d12bd0451588f12da61cb594920d2
---

由于测试任务内部异常，偶现任务终止的情况。请查看【测试报告-执行日志】，如果应用信息为空，请重新创建任务并执行测试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/OwsJiBtLTOC-SObLn-FkoQ/zh-cn_image_0000002229758645.png)

该问题由应用信息未完全解析导致。再次创建任务时，请等待右侧应用信息加载完成，再进行创建，即可解决该问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/hdIh4OqwSnOJP9WhGNrHpg/zh-cn_image_0000002194318380.png "点击放大")
