---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-peak-foreground-memory-usage-0418
title: 前台场景内存峰值占用
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 附录 > 体检规则 > 前台场景内存峰值占用
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:01+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:e7b46dd79f2e98834bd856f8b31c2d84f876a71aa462e9934a33877b907e612b
---

## 规则详情

应用/元服务前台场景峰值内存占用：应用在前台且亮屏使用过程的内存占用应≤1500MB。

## 检测逻辑

1. 执行hdc shell。
2. 执行hidumper --mem <进程pid>命令，获取如图Pss字段。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/pNaJAUVTQymbFzNR2bTdfA/zh-cn_image_0000002779566420.png?HW-CC-KV=V1&HW-CC-Date=20261114T004714Z&HW-CC-Expire=31536000000&HW-CC-Sign=D655045BC98F508BBB2D6EF10CC8E620B55BB256C10AD51F0CED6608FE70CEAB)

## 计算逻辑

执行多轮测试，取最大Pss值为占用峰值，内存占用小于1500MB。
