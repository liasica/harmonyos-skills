---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-peak-background-cpu-usage-0420
title: 后台CPU占用峰值
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 附录 > 体检规则 > 后台CPU占用峰值
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:41+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:826e9e3664f412d89104ec028495da03a6b40f1cba9333f2782f2e5625152565
---

## 规则详情

应用/元服务后台CPU占用峰值：应用/元服务切换到后台等待3min后，开始采集3min内CPU Load < 5%。

## 检测逻辑

1. 执行hdc shell。
2. 执行hidumper --cpuusage <进程pid>命令，获取总的CPU使用率。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/gC9GbKNHQfiz63eYqIWaBA/zh-cn_image_0000002808766567.png?HW-CC-KV=V1&HW-CC-Date=20261128T023441Z&HW-CC-Expire=31536000000&HW-CC-Sign=6BB6EE93C41E2A4045C81B937745F6FC1F9C2F0C506DF48B296EF19A86D80ECC)

## 计算逻辑

执行多轮测试，取最大值为CPU占用峰值，CPU占用率须小于5%。
