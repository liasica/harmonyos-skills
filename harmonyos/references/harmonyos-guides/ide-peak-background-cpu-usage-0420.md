---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-peak-background-cpu-usage-0420
title: 后台CPU占用峰值
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 附录 > 体检规则 > 后台CPU占用峰值
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:579d5a83533a897e239cfc5085f7b000ff644549bdd7dbf7065455a8e210c2af
---

## 规则详情

应用/元服务后台CPU占用峰值：应用/元服务切换到后台等待3min后，开始采集3min内CPU Load < 5%。

## 检测逻辑

1. 执行hdc shell。
2. 执行hidumper --cpuusage <进程pid>命令，获取总的CPU使用率。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/b0N1AcjgRluRf-XqvWZAvg/zh-cn_image_0000002808766567.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=4715E39E399D4DA11EDF7B1FFD135886FBAC41C63CA99C13BD5DCBAB1B11B271)

## 计算逻辑

执行多轮测试，取最大值为CPU占用峰值，CPU占用率须小于5%。
