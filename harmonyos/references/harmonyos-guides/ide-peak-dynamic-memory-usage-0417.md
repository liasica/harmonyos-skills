---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-peak-dynamic-memory-usage-0417
title: 动态内存峰值占用
breadcrumb: 指南 > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 附录 > 体检规则 > 动态内存峰值占用
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:19+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:51e547569168a261ad724cf5455b44ea8f88fed24ba059b788d9732accbdc2f2
---

## 规则详情

应用/元服务完成操作后，各类应用在后台的内存占用峰值应≤1300MB；应用完成操作后切换到后台，静置3min以后采集内存占用。

## 检测逻辑

1. 执行hdc shell。
2. 执行hidumper --mem <进程pid>命令，获取如图Pss字段。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/UA52AdZVQTCCF__HsjIcYg/zh-cn_image_0000002731543113.png)

## 计算逻辑

执行多轮测试，取最大Pss值为内存占用峰值，内存占用须小于1300MB。
