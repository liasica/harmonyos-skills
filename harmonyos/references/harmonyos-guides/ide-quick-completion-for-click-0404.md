---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-quick-completion-for-click-0404
title: 点击操作完成快
breadcrumb: 指南 > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 附录 > 体检规则 > 点击操作完成快
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3d094fe1ea251222d41119a52978c401616519ffb4530d9dbd8248f817ca6665
---

## DevEco Studio 6.0.1 Beta1及以上版本

### 规则详情

应用内点击操作完成时延应≤ 900毫秒；时间起点：点击离手；时间终点：转场页面所有占位符加载完成。

### 检测逻辑

点击后，缓存本次操作与下次操作前的截图，检测图片中的页面是否加载完成。页面加载检测逻辑为：

1. 利用光流法对下次操作前的多张截图进行检测，判断出轮播区与视频区。
2. 检测非轮播区与非视频区是否加载完成：默认下一次操作前页面已经加载完成，并以下次操作前的最后一张截图为目标图片，利用二分法在缓存的图片中搜索。

   说明

   若页面出现第二次刷新行为时，将以第二次刷新后呈现的页面作为加载完成页面（即目标图片），首次刷新结果不作为参考。

   1. 如果检索图片的非轮播区与非视频区和目标图片不存在像素差异，则判断非轮播区与非视频区加载完成；
   2. 若存在像素差异，则进一步判断差异区域是否有内容填充，如果所有差异区域均有内容填充，则判断非轮播区与非视频区加载完成。
3. 若上一步判断非轮播区与非视频区加载完成，再根据是否有内容填充判断轮播区与视频区是否加载完成。
4. 若上一步判断轮播区与视频区加载完成，则该检索图片加载完成，利用二分法继续向前搜索，找到第一张加载完成的图片。

### 计算逻辑

以点击时刻为准，若第一张加载完成图片的时间小于等于900ms，则检测通过；若大于900ms，小于等于1600ms，则检测告警；若大于1600ms，则检测失败。

## DevEco Studio 6.0.1 Beta1以下版本

### 规则详情

时间起点：点击离手；时间终点：转场页面所有占位符加载完成；应用/元服务内点击操作完成时延应≤ 1600毫秒。

### 检测逻辑

点击后，经过1600ms后截图，检测图片是否存在白块。白块检测逻辑为：AppAnalyzer通过真实应用训练的白块检测AI模型，进行页面白块识别。例如：如下左图输入到白块检测AI模型后，可以识别到白块位置，如下右图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/QM6uChpqQ2aHqR5LSiZ3qw/zh-cn_image_0000002530753280.png?HW-CC-KV=V1&HW-CC-Date=20260429T054702Z&HW-CC-Expire=86400&HW-CC-Sign=4583EADF0221705D4F48CB48C5981B4A665505F43A75272C4413A3E1D0BD5672)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/foDWcpv1QB2O5OAfhc838w/zh-cn_image_0000002561833195.png?HW-CC-KV=V1&HW-CC-Date=20260429T054702Z&HW-CC-Expire=86400&HW-CC-Sign=7CF4A361E6DC9644A92834E07E0072A18BC66B42734AFED49A8DBE7F0065E24E)

### 计算逻辑

点击后，经过1600ms后截图，截图页面查找白块数量为0，则检测通过。
