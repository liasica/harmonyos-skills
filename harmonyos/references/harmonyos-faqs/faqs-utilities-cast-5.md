---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-utilities-cast-5
title: 如何通过DevEco Testing将故障截图/录屏导出到电脑上
breadcrumb: FAQ > DevEco Testing > 实用工具 > 设备投屏 > 如何通过DevEco Testing将故障截图/录屏导出到电脑上
category: harmonyos-faqs
scraped_at: 2026-10-28T07:49:05+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:038b0440314e199940ac96f74740a1a49ae520b375028646a92298e362c8655d
---

## 问题现象

如何通过DevEco Testing将故障截图/录屏导出到电脑上，便于后续问题提单、分析等操作。

## 解决方案

1. 下载[DevEco Testing](https://developer.huawei.com/consumer/cn/download/deveco-testing)工具并完成安装。
2. 测试机打开开发者选项开关及USB调试开关：系统设置-关于本机，连续快速7次点击软件版本出现弹框，根据弹框提示确认重启并开启开发者模式，重启测试机后进入系统设置-系统，打开开发者选项开关和USB调试开关。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/6Dza3rfeSO6T0kcTEeQTlw/zh-cn_image_0000002658923405.png "点击放大")
3. 通过数据线连接PC和测试机，打开DevEco Testing工具，点击页面左侧实用工具，选择设备投屏，点击开始投屏按钮（如果未检测到测试机，请检查步骤2中是否成功打开开发者选项开关和USB调试开关）。点击快捷工具中截屏按钮则直接截取当前测试机页面；点击屏幕录制按钮则进入录屏模式，可进行问题复现操作并在操作结束后点击结束录屏。截图/录屏保存路径见执行日志。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/jXf-oe2kTY6lkSzg0sAI4A/zh-cn_image_0000002658803457.png "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/MtuAOOQQRgeDppHzuV_4tg/zh-cn_image_0000002628404194.png "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/u7HwbrLjRAuf_AVtjqbk8w/zh-cn_image_0000002628564098.png "点击放大")
