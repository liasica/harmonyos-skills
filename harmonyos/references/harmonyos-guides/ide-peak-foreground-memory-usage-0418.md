---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-peak-foreground-memory-usage-0418
title: 前台场景内存峰值占用
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 附录 > 体检规则 > 前台场景内存峰值占用
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:64aae7d0cc5662cf26d3a4842a7ea85bf42760e46afba2437599204578927425
---

## 规则详情

应用/元服务前台场景峰值内存占用：应用在前台且亮屏使用过程的内存占用应≤1500MB。

## 检测逻辑

1. 执行hdc shell。
2. 执行hidumper --mem <进程pid>命令，获取如图Pss字段。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/jBEs7WwlTYmECm21iGrtTA/zh-cn_image_0000002779566420.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=24FC1DC0EB887BA2B6B604D8146A551C607452CC107D26F47F1782244E4AE8C3)

## 计算逻辑

执行多轮测试，取最大Pss值为占用峰值，内存占用小于1500MB。
