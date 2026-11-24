---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-app-analyzer-history-reports
title: 管理体检报告
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 管理体检报告
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:31+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:d09a004884c55a2b2a2d6777b4f361998856705fa8c04c6743c68694f925ece8
---

AppAnalyzer支持查看、导出、导入体检报告，具体如下。

## 查看报告

### DevEco Studio 6.0.1 Beta1及以上版本

1. 在DevEco Studio中，点击菜单栏**Tools >** **AppAnalyzer**，弹出AppAnalyzer页面。
2. 点击底部**History**按钮，可查看体检报告卡片，点击卡片可跳转至详细的体检报告。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/CzuOg9LyTY2bHPacGuN2hw/zh-cn_image_0000002808886733.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=1636F6A11B4ADD2435E839A9BD7ABF5EE91DFD09034D6D6787FA2657FDF27AE9)

### DevEco Studio 6.0.1 Beta1以下版本

1. 在DevEco Studio中，点击菜单栏**Tools >** **AppAnalyzer**，弹出AppAnalyzer页面。
2. 点击底部**历史记录**按钮，可查看最近15次的体检报告记录，点击时间戳可跳转至详细的体检报告。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/E1AZXUJEQKG4wY8Hhj8yLg/zh-cn_image_0000002808886737.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=C45F6FA839B4C08D1D696BAE6768F2E596188A7C7D04802E2D9B4EA5BD8B4FF4)

## 导出报告

从DevEco Studio 6.1.0 Release版本开始，AppAnalyzer支持导出体检报告，以实现报告的共享。使用该功能，需要满足以下条件。

* 支持导出场景化体检、规则体检、上架前体检这三种体检方式的报告。
* 历史版本生成的体检报告不支持导出，仅DevEco Studio 6.1.0 Release及以上版本生成的体检报告才支持导出。

操作步骤如下：

1. 点击AppAnalyzer底部的**History**按钮，选择符合条件的报告卡片进入报告页面，点击右上角的**Export**按钮，选择需要保存的路径，点击**OK**后，等待报告导出。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/lPdHZrx3QyW_D1igH7LXwQ/zh-cn_image_0000002808766657.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=001411E9F905B39A4AEA8889CBE66FA61BC4403A6998AC68FA0C56C45D9F0FB0)
2. 报告导出成功后，在DevEco Studio右下角会弹框提示，点击**View the report**可打开报告保存的路径。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/mfaL1OPuRhyFPSQn_y159A/zh-cn_image_0000002808766653.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=457A4483620A7A6F17B996DC5700CE7A46DF880DC41C9830E5954A08B5138198)

## 导入报告

从DevEco Studio 6.1.0 Release版本开始，如需查看他人的体检报告，可使用导入报告功能，需要满足以下条件。

* 支持导入场景化体检、规则体检、上架前体检这三种体检方式的报告。如需导入DevEco Testing的报告，请查看[导入DevEco Testing的检测报告进行诊断](ide-app-analyzer-testing.md)。
* 导入报告使用的DevEco Studio版本，要求不低于导出报告时使用的版本，仅校验版本号前两位，例如6.1.x.x导出的报告，可以在6.1.x.x及以上版本中导入。

操作步骤如下：

1. 点击AppAnalyzer底部的**History**按钮，点击右上角的**Import** **> Analyzer Report**，根据界面提示，确保即将导入的报告满足相关要求。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/Z0xcEqK6Q8SMqtJvwUghsg/zh-cn_image_0000002808766655.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=4EC9366F98660E51FDFB7D28562ECD40B84ACABF60B55BAF0D33D95796F2F64E)
2. 选择本地的体检报告zip文件，点击**OK**后，等待报告导入。导入成功后，AppAnalyzer会自动打开报告。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/pPhTmlSoTl6k42T4nFHVPg/zh-cn_image_0000002808886735.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=1FC7E1AF8001785D5F851489DE10AB6773AC781ED3D0D59E6304BF8A5254D624)
