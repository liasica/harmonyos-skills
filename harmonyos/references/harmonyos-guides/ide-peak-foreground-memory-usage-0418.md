---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-peak-foreground-memory-usage-0418
title: 前台场景内存峰值占用
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 附录 > 体检规则 > 前台场景内存峰值占用
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:32+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:3c199e163aac57a4b4b3b4542472a3d66d59a9bba5a598c46569349c425ce3a3
---

## 规则详情

应用/元服务前台场景峰值内存占用：应用在前台且亮屏使用过程的内存占用应≤1500MB。

## 检测逻辑

1. 执行hdc shell。
2. 执行hidumper --mem <进程pid>命令，获取如图Pss字段。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/KGjsetiWQRGMfsM65bycFg/zh-cn_image_0000002779566420.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=C3B85BB8E7A8A344842E55056251A08C45AC6DD4063950844A6DE7E1D542FDF2)

## 计算逻辑

执行多轮测试，取最大Pss值为占用峰值，内存占用小于1500MB。
