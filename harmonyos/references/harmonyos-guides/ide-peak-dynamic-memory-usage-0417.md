---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-peak-dynamic-memory-usage-0417
title: 动态内存峰值占用
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 附录 > 体检规则 > 动态内存峰值占用
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:01+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:c67d9ded960a86b6c07b71f1040f1e49d45c178aebc164da89b1ad47a8707da1
---

## 规则详情

应用/元服务完成操作后，各类应用在后台的内存占用峰值应≤1300MB；应用完成操作后切换到后台，静置3min以后采集内存占用。

## 检测逻辑

1. 执行hdc shell。
2. 执行hidumper --mem <进程pid>命令，获取如图Pss字段。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/ESOKoL68RveiPbNhvOStJg/zh-cn_image_0000002779567538.png?HW-CC-KV=V1&HW-CC-Date=20261114T004901Z&HW-CC-Expire=31536000000&HW-CC-Sign=0436778AA501D7B057DB6C9DF939F08F624759B62950DC3EEF8B08CCBA940DD7)

## 计算逻辑

执行多轮测试，取最大Pss值为内存占用峰值，内存占用须小于1300MB。
