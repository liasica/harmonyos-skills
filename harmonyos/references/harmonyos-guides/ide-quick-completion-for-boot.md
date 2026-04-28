---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-quick-completion-for-boot
title: 启动加载完成快
breadcrumb: 指南 > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 附录 > 体检规则 > 启动加载完成快
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5fa9a9f9aec4c3affcf6373339c46b40d80f587ac184abcd42849a26fdda5c87
---

## DevEco Studio 6.0.1 Beta1及以上版本

### 规则详情

各类应用的冷启动首帧完成时延应 ≤ 1100毫秒；时间起点：桌面图标点击离手；时间终点：应用首页铺满全屏并且所有占位符加载完成。

### 检测逻辑

启动后，缓存本次冷启动过程中的截图，检测启动过程中的广告页面和加载完成页面。广告页面通过使用真实应用训练的广告检测AI模型进行检测，页面加载检测逻辑参考[DevEco Studio 6.0.1 Beta1及以上版本的点击操作完成快](ide-quick-completion-for-click-0404.md#section15922054151911)。

说明

如果首页内容加载需要网络请求，请确保网络连接已开启。

### 计算逻辑

以首帧页面铺满屏幕作为开始时刻，冷启动完成时延等于应用首页加载完成耗时减去广告时间。若冷启动完成时延小于等于1100ms，则检测通过；若大于1100ms，小于等于6300ms，则检测告警；若大于6300ms，则检测失败。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/oRwkW4wcRpukuwgqIDENxA/zh-cn_image_0000002561833549.png?HW-CC-KV=V1&HW-CC-Date=20260427T235706Z&HW-CC-Expire=86400&HW-CC-Sign=E888394E668C9029F7191D88F3C0B900E1CFF96AC0631BB49F4B0AB1A98574AA)

## DevEco Studio 6.0.1 Beta1以下版本

### 规则详情

各类应用的冷启动首帧完成时延应 ≤ 1100毫秒；时间起点：桌面图标点击离手；时间终点：应用首页铺满全屏并且所有占位符加载完成。

### 检测逻辑

启动后，缓存本次冷启动过程中的截图，检测启动过程中的广告页面和加载完成页面。广告页面通过使用真实应用训练的广告检测AI模型进行检测，页面加载检测逻辑参考[DevEco Studio 6.0.1 Beta1以下版本的点击操作完成快](ide-quick-completion-for-click-0404.md#section191984031815)。

### 计算逻辑

以首帧页面铺满屏幕作为开始时刻，冷启动完成时延等于应用首页加载完成耗时减去广告时间。若冷启动完成时延小于等于1100ms，则检测通过；若大于1100ms，小于等于6300ms，则检测告警；若大于6300ms，则检测失败。
