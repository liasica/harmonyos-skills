---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-peak-dynamic-memory-usage-0417
title: 动态内存峰值占用
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 附录 > 体检规则 > 动态内存峰值占用
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:32+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:352cef9d2ad22fe1b490a1eb654b957513cb219ef51e1a5e66daa215d9358e9b
---

## 规则详情

应用/元服务完成操作后，各类应用在后台的内存占用峰值应≤1300MB；应用完成操作后切换到后台，静置3min以后采集内存占用。

## 检测逻辑

1. 执行hdc shell。
2. 执行hidumper --mem <进程pid>命令，获取如图Pss字段。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/Mn5PFpMNSDGLKs-z3Nj5dQ/zh-cn_image_0000002779567538.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=81595EF2E58DEF8CF43E8C9B6C8C6DAC8D0F02FD22D787C6228D107B09D951D4)

## 计算逻辑

执行多轮测试，取最大Pss值为内存占用峰值，内存占用须小于1300MB。
