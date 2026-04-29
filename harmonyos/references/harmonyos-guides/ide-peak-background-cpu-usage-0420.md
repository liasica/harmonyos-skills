---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-peak-background-cpu-usage-0420
title: 后台CPU占用峰值
breadcrumb: 指南 > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 附录 > 体检规则 > 后台CPU占用峰值
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:22c6179c52a27bca8a9eab2dea7473e69e59d1f5a96afeac08e4479b5ce22522
---

## 规则详情

应用/元服务后台CPU占用峰值：应用/元服务切换到后台等待3min后，开始采集3min内CPU Load < 5%。

## 检测逻辑

1. 执行hdc shell。
2. 执行hidumper --cpuusage <进程pid>命令，获取总的cpu使用率。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/mRnXb8XKT7yyYcwKawZAWQ/zh-cn_image_0000002530753024.png?HW-CC-KV=V1&HW-CC-Date=20260429T054704Z&HW-CC-Expire=86400&HW-CC-Sign=91B04E4520C0D9912D16B2A4A8E90CA4034B04B7ABAD628CF1D3CA7D65F471F1)

## 计算逻辑

执行多轮测试，取最大值为cpu占用峰值，cpu占用率须小于5%。
