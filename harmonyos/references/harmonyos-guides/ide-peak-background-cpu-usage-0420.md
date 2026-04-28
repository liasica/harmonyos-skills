---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-peak-background-cpu-usage-0420
title: 后台CPU占用峰值
breadcrumb: 指南 > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 附录 > 体检规则 > 后台CPU占用峰值
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3e29dcf60765b984347adce40123ca8a1f9e3d0eb4b6b8e928166334577b395d
---

## 规则详情

应用/元服务后台CPU占用峰值：应用/元服务切换到后台等待3min后，开始采集3min内CPU Load < 5%。

## 检测逻辑

1. 执行hdc shell。
2. 执行hidumper --cpuusage <进程pid>命令，获取总的cpu使用率。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/JgOHYf2jSd-xpEkCS1lgcw/zh-cn_image_0000002530753024.png?HW-CC-KV=V1&HW-CC-Date=20260427T235707Z&HW-CC-Expire=86400&HW-CC-Sign=846309289C9C8942D2C7989123C1449CAF97F407868EDF59E773758D86A0B6EE)

## 计算逻辑

执行多轮测试，取最大值为cpu占用峰值，cpu占用率须小于5%。
