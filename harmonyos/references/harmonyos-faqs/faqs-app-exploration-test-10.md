---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-exploration-test-10
title: 如何对指定的页面进行压测
breadcrumb: FAQ > DevEco Testing > 探索测试 > 应用探索测试 > 如何对指定的页面进行压测
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:963389736ec55d175e5dee9e7c6a21d8941d1f99d7b23b686c87634a9736b559
---

## 问题现象

如果希望对指定的页面进行稳定性测试或者压力测试，那么具体该如何操作呢？

## 背景知识

[DevEco Testing](../harmonyos-guides/deveco-testing.md)是一款专项集成测试工具，提供了多项测试能力，支持一键执行测试任务，同时提供了测试报告和分析，辅助开发者发现应用和产品问题，提升应用质量。

## 解决方案

1. 已完成[DevEco Testing的下载和安装](https://developer.huawei.com/consumer/cn/download/deveco-testing)。
2. 打开DevEco Testing工具，点击实用工具->应用图谱管理工具->创建图谱->空白图谱，填写图谱名、选择设备和应用包名，点击创建图谱。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/Wzvd6g_fQDScOH0n7-Twnw/zh-cn_image_0000002628563138.png?HW-CC-KV=V1&HW-CC-Date=20261112T233144Z&HW-CC-Expire=31536000000&HW-CC-Sign=8F43A707CC3062B64323063182E6C8474D549C07288DE0AD673DA42B98E89DF9 "点击放大")
3. 点击新增特性按钮，输入特性名称和特性描述（非必填），点击提交按钮；选择已有特性，点击新建场景路径按钮，设置场景名称，选择投屏设备，点击窗口中的“+”号添加步骤，选择通过屏幕录制添加，通过在左侧投屏设备的区域内，执行点击、滑动或者右键弹窗输入文本动作，添加相应的场景步骤，点击保存按钮完成场景创建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/522VCZVmTIahgxGZntcoLg/zh-cn_image_0000002658922461.png?HW-CC-KV=V1&HW-CC-Date=20261112T233144Z&HW-CC-Expire=31536000000&HW-CC-Sign=2133C59B770545854A19B6F118A43B6A3A2DB77AA07F03473DD47D5364433C21 "点击放大")
4. 点击调试，查看实际执行页面与图谱指定路径是否一致。如果不一致，可以进行场景路径编辑。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/wLTjRRirSe6fK_I7NT05gQ/zh-cn_image_0000002628403248.png?HW-CC-KV=V1&HW-CC-Date=20261112T233144Z&HW-CC-Expire=31536000000&HW-CC-Sign=D79F838FFF68019B3C45DD5EC4A916A304E122BA821F05D68B4905136B85A4FA "点击放大")
5. 点击DevEco Testing工具的探索测试->应用探索测试->创建任务->选择测试设备、选择应用、定义测试时长->模式类型选择“场景压测”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/Pa6sf6B5RRuh8cuzL2nonQ/zh-cn_image_0000002658802513.png?HW-CC-KV=V1&HW-CC-Date=20261112T233144Z&HW-CC-Expire=31536000000&HW-CC-Sign=489489EB4D97850B3CA09705FD065D90730F6C2459C718B0655FEC62883A592A "点击放大")
