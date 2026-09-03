---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-app-analyzer-before-appgallery
title: 上架前体检
breadcrumb: 指南 > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 上架前体检
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:19+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:fcc98760581b81c19a1524057ca1f823cd48369909064183e05b1c96eda39996
---

从DevEco Studio 6.0.0 Beta1版本开始，AppAnalyzer新增上架前体检，针对上架阻塞问题进行快速检测，提前发现可能影响上架的问题，检测完成之后可以选择上传检测结果，用于应用市场上架参考，提升上架效率。

## 前置操作

1. 通过以下任意一种方式，打开AppAnalyzer。
   * 点击菜单栏**Tools >** **AppAnalyzer**，打开AppAnalyzer页面。
   * 在编辑窗口右侧的工具栏，点击**AppAnalyzer**或![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/UMO9VONZSEi0ZmLhRecBwQ/zh-cn_image_0000002701822910.png)，打开AppAnalyzer页面。
2. 确保[DevEco Studio与真机设备已连接](ide-run-device.md)，并对应用进行[签名](ide-signing.md)。
3. 如果使用DevEco Studio 6.0.1版本，未配置Python环境时，请根据界面提示，下载Python及三方库。或者点击AppAnalyzer底部**Python 配置**按钮进行配置。

## 进行体检

### DevEco Studio 6.0.1 Beta1及以上版本

1. 在**AppAnalyzer**页面，选择**上架前体检**，点击预置的体检卡片，在弹框中选择待上架的产物和调试签名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/0SUv6BW4SayQfJzJjqudDQ/zh-cn_image_0000002731382219.png)
2. 该体检模式无法自定义测试方式和体检规则，默认勾选所有规则，这些规则是[规则体检](ide-app-analyzer-all-rules.md)的子集。单击底部的**开始体检**按钮，等待AppAnalyzer完成构建、签名、安装等操作。
3. 安装完成后，根据提示登录账号，开始进行测试。在测试过程中，请保持连接的设备为解锁亮屏状态。
4. 测试完成后，查看测试报告如下。
   * 如果测试分数是100分，可点击右上角**Sync To AG**按钮，确认弹框内容后点击**OK**，上传本次的检测报告，用于应用市场上架参考。上传报告后，无法再次上传报告。

     **说明** 

     如需上传报告，请在体检结束后上传，[历史报告](ide-app-analyzer-history-reports.md)中无法上传报告。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/Jw7OZt0AS164fyQ9jsm8kA/zh-cn_image_0000002731382215.png)
   * 如果测试分数不是100分，无法上传报告，可根据详情报告中的信息，对问题进行分析优化，详情报告的具体内容可参考[规则体检](ide-app-analyzer-rules.md#li22241112508)。

   从DevEco Studio 6.0.2 Beta1版本开始，如果在体检中遇到问题，可点击报告右上角的**User Feedback**向我们反馈。

   从DevEco Studio 6.1.0 Release版本开始，支持导出报告，以实现报告的共享，具体可查看[导出报告](ide-app-analyzer-history-reports.md#section78017171818)。

### DevEco Studio 6.0.1 Beta1以下版本

1. 在**AppAnalyzer**页面，选择**上架前体检**，弹出上架前检测配置的弹框，选择待上架的产物和调试签名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/7RN1lInDQgyS6T6pEs18eg/zh-cn_image_0000002701822908.png)
2. 该体检模式无法自定义测试方式、模块和体检规则，默认勾选所有规则，这些规则是[规则体检](ide-app-analyzer-all-rules.md)的子集。单击底部的**开始**按钮，等待AppAnalyzer完成构建、签名、安装等操作。
3. 安装完成后，根据提示登录账号，开始进行测试。在测试过程中，请保持连接的设备为解锁亮屏状态。
4. 测试完成后点击**结束**按钮停止测试任务，等待数据解析完成后，查看测试结果如下。
   * 如果测试分数是100分，可点击右上角**报告同步**按钮，确认弹框内容后点击**OK**，上传本次的检测报告，用于应用市场上架参考。上传报告后，无法再次上传报告。

     **说明** 

     如需上传报告，请在体检结束后上传，[历史报告](ide-app-analyzer-history-reports.md)中无法上传报告。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/UZlnQWZ_TP2F4YZ46V_PlQ/zh-cn_image_0000002701662996.png)
   * 如果测试分数不是100分，无法上传报告，可根据详情报告中的信息，对问题进行分析优化，详情报告的具体内容可参考[规则体检](ide-app-analyzer-rules.md#li131614342254)。
