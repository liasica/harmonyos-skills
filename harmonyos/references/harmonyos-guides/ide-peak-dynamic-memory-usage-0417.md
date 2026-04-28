---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-peak-dynamic-memory-usage-0417
title: 动态内存峰值占用
breadcrumb: 指南 > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 附录 > 体检规则 > 动态内存峰值占用
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cc0bf34c5d17e25cd8c4ecafbea6757e723d6f1154be59e23b1c58216643ba4c
---

## 规则详情

应用/元服务完成操作后，各类应用在后台的内存占用峰值应≤ 1300MB；应用完成操作后切换到后台，静置3min以后采集内存占用。

## 检测逻辑

1. 执行hdc shell。
2. 执行hidumper --mem <进程pid>命令，获取如图Pss字段。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/3lJtTjWRQfq_jt7F9KdRWg/zh-cn_image_0000002530753784.png?HW-CC-KV=V1&HW-CC-Date=20260427T235704Z&HW-CC-Expire=86400&HW-CC-Sign=7ECAD3B2BCBE3AFBA0FB8BB81D7A788535C724345E03C790685DF15D4DF1B08B)

## 计算逻辑

执行多轮测试，取最大Pss值为占用峰值，内存占用须小于1300M。
