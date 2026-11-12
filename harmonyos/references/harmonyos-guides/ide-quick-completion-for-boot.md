---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-quick-completion-for-boot
title: 启动加载完成快
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 附录 > 体检规则 > 启动加载完成快
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:05+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:b6d922fb0a3d926f80caf2a08d9e949ddc41fc4b550cb2a37b1659690f1cdc0c
---

## 规则详情

各类应用的冷启动首帧完成时延应 ≤ 1100ms；时间起点：桌面图标点击离手；时间终点：应用首页铺满全屏并且所有占位符加载完成。

## 检测逻辑

启动后，缓存本次冷启动过程中的截图，检测启动过程中的广告页面和加载完成页面。广告页面通过使用真实应用训练的广告检测AI模型进行检测，页面加载检测逻辑参考[点击操作完成快](ide-quick-completion-for-click-0404.md)。

**说明** 

如果首页内容加载需要网络请求，请确保网络连接已开启。

## 计算逻辑

以首帧页面铺满屏幕作为开始时刻，冷启动完成时延等于应用首页加载完成耗时减去广告时间。若冷启动完成时延小于等于1100ms，则检测通过；若大于1100ms，小于等于6300ms，则检测告警；若大于6300ms，则检测失败。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/Fxbgc9b2Qd6UghlMTZNyuA/zh-cn_image_0000002779407366.png)
