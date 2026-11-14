---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-peak-background-cpu-usage-0420
title: 后台CPU占用峰值
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 附录 > 体检规则 > 后台CPU占用峰值
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:01+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:c243590c91c1d05394d2aaf326cc0f4f3580e06abb2a3dd3a2718c7aeb941fec
---

## 规则详情

应用/元服务后台CPU占用峰值：应用/元服务切换到后台等待3min后，开始采集3min内CPU Load < 5%。

## 检测逻辑

1. 执行hdc shell。
2. 执行hidumper --cpuusage <进程pid>命令，获取总的CPU使用率。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/Rc2j4gBLQ0S3bFClY5v8Wg/zh-cn_image_0000002808766567.png?HW-CC-KV=V1&HW-CC-Date=20261114T004714Z&HW-CC-Expire=31536000000&HW-CC-Sign=20959F4D3B2757ED4BCF9F051D7FE156870427F2DD4B3F18BBC295FB3A3CF878)

## 计算逻辑

执行多轮测试，取最大值为CPU占用峰值，CPU占用率须小于5%。
