---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-peak-foreground-memory-usage-0418
title: 前台场景内存峰值占用
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 附录 > 体检规则 > 前台场景内存峰值占用
category: harmonyos-guides
scraped_at: 2026-10-17T06:43:30+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:53f1aa3f1240a6340c7be07a459ae89cbca2bdbebdaf9172490adf34eab0e631
---

## 规则详情

应用/元服务前台场景峰值内存占用：应用在前台且亮屏使用过程的内存占用应≤1500MB。

## 检测逻辑

1. 执行hdc shell。
2. 执行hidumper --mem <进程pid>命令，获取如图Pss字段。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/Wu8Kn7bVS-GrXCLgjbJFBA/zh-cn_image_0000002731381845.png)

## 计算逻辑

执行多轮测试，取最大Pss值为占用峰值，内存占用小于1500MB。
