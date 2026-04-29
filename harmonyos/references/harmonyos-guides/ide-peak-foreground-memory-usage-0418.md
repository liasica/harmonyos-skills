---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-peak-foreground-memory-usage-0418
title: 前台场景内存峰值占用
breadcrumb: 指南 > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 附录 > 体检规则 > 前台场景内存峰值占用
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f5704f947624d9382711a0d573f14322944c351ed9e4f4fd4e37c4278f83135f
---

## 规则详情

应用/元服务前台场景峰值内存占用：应用在前台且亮屏使用规程的内存占用应≤ 1500MB。

## 检测逻辑

1. 执行hdc shell。
2. 执行hidumper --mem <进程pid>命令，获取如图Pss字段。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/8f1V2VtKSryYTKYT676aXw/zh-cn_image_0000002561832611.png?HW-CC-KV=V1&HW-CC-Date=20260429T054704Z&HW-CC-Expire=86400&HW-CC-Sign=8F0E00A83A5BA3E9AC02DAF0B0E9DAFFF310FA9403328B4E25C8FF15B4C45582)

## 计算逻辑

执行多轮测试，取最大Pss值为占用峰值，内存占用小于1500M。
