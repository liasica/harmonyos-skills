---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-peak-dynamic-memory-usage-0417
title: 动态内存峰值占用
breadcrumb: 指南 > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 附录 > 体检规则 > 动态内存峰值占用
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:55+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:661d23d892581f0d41c7636ab8d5ce34442a77163b90db72a7ccaa17277c0b2a
---

## 规则详情

应用/元服务完成操作后，各类应用在后台的内存占用峰值应≤1300MB；应用完成操作后切换到后台，静置3min以后采集内存占用。

## 检测逻辑

1. 执行hdc shell。
2. 执行hidumper --mem <进程pid>命令，获取如图Pss字段。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/h8tBHioJRYi1KEhahF4f6w/zh-cn_image_0000002731543113.png)

## 计算逻辑

执行多轮测试，取最大Pss值为内存占用峰值，内存占用须小于1300MB。
