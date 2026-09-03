---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-app-analyzer-history-reports
title: 管理体检报告
breadcrumb: 指南 > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 管理体检报告
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:19+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f0f0f7a926022a7358c7ea7898d621851dbec8e5ddde339975d2d4217a9bd353
---

AppAnalyzer支持查看、导出、导入体检报告，具体如下。

## 查看报告

### DevEco Studio 6.0.1 Beta1及以上版本

1. 在DevEco Studio中，点击菜单栏**Tools >** **AppAnalyzer**，弹出AppAnalyzer页面。
2. 点击底部**History**按钮，可查看体检报告卡片，点击卡片可跳转至详细的体检报告。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/LOML75wpRHyMCFNVcQ1bfg/zh-cn_image_0000002731542455.png)

### DevEco Studio 6.0.1 Beta1以下版本

1. 在DevEco Studio中，点击菜单栏**Tools >** **AppAnalyzer**，弹出AppAnalyzer页面。
2. 点击底部**历史记录**按钮，可查看最近15次的体检报告记录，点击时间戳可跳转至详细的体检报告。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/qxbcXsL2TYCEAc6HIitPfQ/zh-cn_image_0000002731542461.png)

## 导出报告

从DevEco Studio 6.1.0 Release版本开始，AppAnalyzer支持导出体检报告，以实现报告的共享。使用该功能，需要满足以下条件。

* 支持导出场景化体检、规则体检、上架前体检这三种体检方式的报告。
* 历史版本生成的体检报告不支持导出，仅DevEco Studio 6.1.0 Release及以上版本生成的体检报告才支持导出。

操作步骤如下：

1. 点击AppAnalyzer底部的**History**按钮，选择符合条件的报告卡片进入报告页面，点击右上角的**Export**按钮，选择需要保存的路径，点击**OK**后，等待报告导出。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/4U3dkGSKSIaUVL9LmDSF1Q/zh-cn_image_0000002701663268.png)
2. 报告导出成功后，在DevEco Studio右下角会弹框提示，点击**View the report**可打开报告保存的路径。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/mfPVUdVeSwmq_TlZkIG1OA/zh-cn_image_0000002701663262.png)

## 导入报告

从DevEco Studio 6.1.0 Release版本开始，如需查看他人的体检报告，可使用导入报告功能，需要满足以下条件。

* 支持导入场景化体检、规则体检、上架前体检这三种体检方式的报告。如需导入DevEco Testing的报告，请查看[导入DevEco Testing的检测报告进行诊断](ide-app-analyzer-testing.md)。
* 导入报告使用的DevEco Studio版本，要求不低于导出报告时使用的版本，仅校验版本号前两位，例如6.1.x.x导出的报告，可以在6.1.x.x及以上版本中导入。

操作步骤如下：

1. 点击AppAnalyzer底部的**History**按钮，点击右上角的**Import** **> Analyzer Report**，根据界面提示，确保即将导入的报告满足相关要求。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/9c7FmhM6RuSYTldWlNjm4g/zh-cn_image_0000002701663266.png)
2. 选择本地的体检报告zip文件，点击**OK**后，等待报告导入。导入成功后，AppAnalyzer会自动打开报告。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/3e2CB-DMTzC-O3UvKkKl5Q/zh-cn_image_0000002731382485.png)
