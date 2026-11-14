---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-app-analyzer-before-appgallery
title: 上架前体检
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 上架前体检
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:01+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:0bd781d4aac41dedadac01e6955e68bf62832191a45b0c64ecb86f83d8f03d99
---

从DevEco Studio 6.0.0 Beta1版本开始，AppAnalyzer新增上架前体检，针对上架阻塞问题进行快速检测，提前发现可能影响上架的问题，检测完成之后可以选择上传检测结果，用于应用市场上架参考，提升上架效率。

## 前置操作

1. 通过以下任意一种方式，打开AppAnalyzer。
   * 点击菜单栏**Tools >** **AppAnalyzer**，打开AppAnalyzer页面。
   * 在编辑窗口右侧的工具栏，点击**AppAnalyzer**或![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/upn3pkP1SWCeOpqAc96Ovw/zh-cn_image_0000002779566850.png?HW-CC-KV=V1&HW-CC-Date=20261114T004714Z&HW-CC-Expire=31536000000&HW-CC-Sign=547F47D54636815C329F748CCDC02543D7197D9B6E60D6CFFBF9A4AEB593FFBC)，打开AppAnalyzer页面。
2. 确保[DevEco Studio与真机设备已连接](ide-run-device.md)，并对应用进行[签名](ide-signing.md)。
3. 如果使用DevEco Studio 6.0.1版本，未配置Python环境时，请根据界面提示，下载Python及三方库。或者点击AppAnalyzer底部**Python 配置**按钮进行配置。

## 进行体检

### DevEco Studio 6.0.1 Beta1及以上版本

1. 在**AppAnalyzer**页面，选择**上架前体检**，点击预置的体检卡片，在弹框中选择待上架的产物和调试签名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/-insemtVTyqomtWng7Tizw/zh-cn_image_0000002779566852.png?HW-CC-KV=V1&HW-CC-Date=20261114T004714Z&HW-CC-Expire=31536000000&HW-CC-Sign=D012AF51A0414874296E3AC3947EBD99C7F01E06422CF75BDA2DA9C3D9DF60E7)
2. 该体检模式无法自定义测试方式和体检规则，默认勾选所有规则，这些规则是[规则体检](ide-app-analyzer-all-rules.md)的子集。单击底部的**开始体检**按钮，等待AppAnalyzer完成构建、签名、安装等操作。
3. 安装完成后，根据提示登录账号，开始进行测试。在测试过程中，请保持连接的设备为解锁亮屏状态。
4. 测试完成后，查看测试报告如下。
   * 如果测试分数是100分，可点击右上角**Sync To AG**按钮，确认弹框内容后点击**OK**，上传本次的检测报告，用于应用市场上架参考。上传报告后，无法再次上传报告。

     **说明** 

     如需上传报告，请在体检结束后上传，[历史报告](ide-app-analyzer-history-reports.md)中无法上传报告。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/QbGqxzBaT_KdvZg03VM03Q/zh-cn_image_0000002779406874.png?HW-CC-KV=V1&HW-CC-Date=20261114T004714Z&HW-CC-Expire=31536000000&HW-CC-Sign=F68B7142ADA404A03008DE5A92A8F787B5E676CDBAED845F6F8BFCEAC9D79A6E)
   * 如果测试分数不是100分，无法上传报告，可根据详情报告中的信息，对问题进行分析优化，详情报告的具体内容可参考[规则体检](ide-app-analyzer-rules.md#li22241112508)。

   从DevEco Studio 6.0.2 Beta1版本开始，如果在体检中遇到问题，可点击报告右上角的**User Feedback**向我们反馈。

   从DevEco Studio 6.1.0 Release版本开始，支持导出报告，以实现报告的共享，具体可查看[导出报告](ide-app-analyzer-history-reports.md#section78017171818)。

### DevEco Studio 6.0.1 Beta1以下版本

1. 在**AppAnalyzer**页面，选择**上架前体检**，弹出上架前检测配置的弹框，选择待上架的产物和调试签名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/wWjSsdadTEmVfOxRHBjWlg/zh-cn_image_0000002779406872.png?HW-CC-KV=V1&HW-CC-Date=20261114T004714Z&HW-CC-Expire=31536000000&HW-CC-Sign=7F1D784E1B08C8B7DB6358446F183FB9EB0C68C3A5BF3CA79CC8125BE5B1E8DA)
2. 该体检模式无法自定义测试方式、模块和体检规则，默认勾选所有规则，这些规则是[规则体检](ide-app-analyzer-all-rules.md)的子集。单击底部的**开始**按钮，等待AppAnalyzer完成构建、签名、安装等操作。
3. 安装完成后，根据提示登录账号，开始进行测试。在测试过程中，请保持连接的设备为解锁亮屏状态。
4. 测试完成后点击**结束**按钮停止测试任务，等待数据解析完成后，查看测试结果如下。
   * 如果测试分数是100分，可点击右上角**报告同步**按钮，确认弹框内容后点击**OK**，上传本次的检测报告，用于应用市场上架参考。上传报告后，无法再次上传报告。

     **说明** 

     如需上传报告，请在体检结束后上传，[历史报告](ide-app-analyzer-history-reports.md)中无法上传报告。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/z7cYL0NETaKnLA3iCaSJ_A/zh-cn_image_0000002808766435.png?HW-CC-KV=V1&HW-CC-Date=20261114T004714Z&HW-CC-Expire=31536000000&HW-CC-Sign=9DEEA7A4E238363C2897C3D2013BB607A67F22BD114CCC17978B6B27C4B939D8)
   * 如果测试分数不是100分，无法上传报告，可根据详情报告中的信息，对问题进行分析优化，详情报告的具体内容可参考[规则体检](ide-app-analyzer-rules.md#li131614342254)。
