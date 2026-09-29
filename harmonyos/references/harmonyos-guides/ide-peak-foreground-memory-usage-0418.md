---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-peak-foreground-memory-usage-0418
title: 前台场景内存峰值占用
breadcrumb: 指南 > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 附录 > 体检规则 > 前台场景内存峰值占用
category: harmonyos-guides
scraped_at: 2026-09-30T07:35:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:904c1940021c335a223d3d7b921eb772f2c0efb2da5775af21c8263dfb55d900
---

## 规则详情

应用/元服务前台场景峰值内存占用：应用在前台且亮屏使用过程的内存占用应≤1500MB。

## 检测逻辑

1. 执行hdc shell。
2. 执行hidumper --mem <进程pid>命令，获取如图Pss字段。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/ZqMyiEOYRn-Xat2grQel1g/zh-cn_image_0000002731381845.png)

## 计算逻辑

执行多轮测试，取最大Pss值为占用峰值，内存占用小于1500MB。
