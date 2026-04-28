---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-peak-foreground-memory-usage-0418
title: 前台场景内存峰值占用
breadcrumb: 指南 > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 附录 > 体检规则 > 前台场景内存峰值占用
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5107daa1c73d6199f341bc4539d32606eccb5fbc507de91347c5dd276da1658b
---

## 规则详情

应用/元服务前台场景峰值内存占用：应用在前台且亮屏使用规程的内存占用应≤ 1500MB。

## 检测逻辑

1. 执行hdc shell。
2. 执行hidumper --mem <进程pid>命令，获取如图Pss字段。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/zk_Cpr0-Rv6DUUljdvDGyQ/zh-cn_image_0000002561832611.png?HW-CC-KV=V1&HW-CC-Date=20260427T235707Z&HW-CC-Expire=86400&HW-CC-Sign=5C57B14CCDD552E32F1F06F46BF122BC35577EF14E57709005448CB1F353BD66)

## 计算逻辑

执行多轮测试，取最大Pss值为占用峰值，内存占用小于1500M。
