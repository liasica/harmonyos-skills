---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-peak-background-cpu-usage-0420
title: 后台CPU占用峰值
breadcrumb: 指南 > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 附录 > 体检规则 > 后台CPU占用峰值
category: harmonyos-guides
scraped_at: 2026-09-30T07:35:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:97f1fb246210fc673eae82d8dcc271ca542f6a42aa8d794038c02972737a24be
---

## 规则详情

应用/元服务后台CPU占用峰值：应用/元服务切换到后台等待3min后，开始采集3min内CPU Load < 5%。

## 检测逻辑

1. 执行hdc shell。
2. 执行hidumper --cpuusage <进程pid>命令，获取总的CPU使用率。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/xPEeMu5GR1evqX9cuusmsg/zh-cn_image_0000002731382569.png)

## 计算逻辑

执行多轮测试，取最大值为CPU占用峰值，CPU占用率须小于5%。
