---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-publish-test-3
title: 测试报告中，为什么会批量出现待检测项
breadcrumb: FAQ > DevEco Testing > 上架预检 > 测试报告中，为什么会批量出现待检测项
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:99f1cbfd8a0cc2100e9def384bac97738ed246edf4d9d50d1356e379c5c01b49
---

由于测试任务内部异常，偶现任务终止的情况。请查看【测试报告-执行日志】，如果应用信息为空，请重新创建任务并执行测试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/osF3lIs1TriVu-A-xBZF8w/zh-cn_image_0000002654798345.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=5C32C87AFCE101D78CC954A78ABF8DA43E6F40398363FF074B8ADCF21B347DDA)

该问题由应用信息未完全解析导致。再次创建任务时，请等待右侧应用信息加载完成，再进行创建，即可解决该问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/KnMvrLkzTBCfghET74YMgA/zh-cn_image_0000002624638880.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=E80BD0D314264622F0BD917C866305BF4C55142B579A1645924C95E586738DA8 "点击放大")
