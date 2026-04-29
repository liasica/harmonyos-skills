---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-app-analyzer-history-reports
title: 管理体检报告
breadcrumb: 指南 > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 管理体检报告
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:11f414e08195b0cc7907a5119cc9a1a4a36ad1fdcc89cb9096b65a51cad882d1
---

AppAnalyzer支持查看、导出、导入体检报告，具体如下。

## 查看报告

### DevEco Studio 6.0.1 Beta1及以上版本

1. 在DevEco Studio中，点击菜单栏**Tools >** **AppAnalyzer**，弹出AppAnalyzer页面。
2. 点击底部**体检历史**按钮，可查看最近15次的体检报告卡片，点击卡片可跳转至详细的体检报告。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/UB_0YBXIRBmHIhttOnzi_w/zh-cn_image_0000002530753246.png?HW-CC-KV=V1&HW-CC-Date=20260429T054701Z&HW-CC-Expire=86400&HW-CC-Sign=C1B677144B672B96594152D62390E151D53ADC8B3A24C3F1122E493FAB0E9B67)

### DevEco Studio 6.0.1 Beta1以下版本

1. 在DevEco Studio中，点击菜单栏**Tools >** **AppAnalyzer**，弹出AppAnalyzer页面。
2. 点击底部**历史记录**按钮，可查看最近15次的体检报告记录，点击时间戳可跳转至详细的体检报告。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/MLCY1oqJTHek70ncxz2iQw/zh-cn_image_0000002561753185.png?HW-CC-KV=V1&HW-CC-Date=20260429T054701Z&HW-CC-Expire=86400&HW-CC-Sign=9FBCAE4285648AED1387EED86C499942CFAF0A79051F3E2D84CF2BFEC065C617)

## 导出报告

从DevEco Studio 6.1.0 Release版本开始，AppAnalyzer支持导出体检报告，以实现报告的共享。使用该功能，需要满足以下条件。

* 支持导出场景化体检、规则体检、上架前体检这三种体检方式的报告。
* 历史版本生成的体检报告不支持导出，仅DevEco Studio 6.1.0 Release及以上版本生成的体检报告才支持导出。

操作步骤如下：

1. 点击AppAnalyzer底部的**体检历史**按钮，选择符合条件的报告卡片进入报告页面，点击右上角的**导出报告**按钮，选择需要保存的路径，点击**确定**后，等待报告导出。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/Z78pP6SSTrWKa4FxPXcDrA/zh-cn_image_0000002561753183.png?HW-CC-KV=V1&HW-CC-Date=20260429T054701Z&HW-CC-Expire=86400&HW-CC-Sign=FDEB158C7755D46EDBC03CBD964642D6F316CD478A41EFEFADCA9DD39571428C)
2. 报告导出成功后，在DevEco Studio右下角会弹框提示，点击**查看报告**可打开报告保存的路径。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/Cn5dGE03SIuRrBQ_iuU4qg/zh-cn_image_0000002530913242.png?HW-CC-KV=V1&HW-CC-Date=20260429T054701Z&HW-CC-Expire=86400&HW-CC-Sign=86B26E7AF0DDB749854BE197441F13B8E599098DB81B93EA7F6D2BE7AED0E1DB)

## 导入报告

从DevEco Studio 6.1.0 Release版本开始，如需查看他人的体检报告，可使用导入报告功能，需要满足以下条件。

* 支持导入场景化体检、规则体检、上架前体检这三种体检方式的报告。如需导入DevEco Testing的报告，请查看[导入DevEco Testing的检测报告进行诊断](ide-app-analyzer-testing.md)。
* 导入报告使用的DevEco Studio版本，要求不低于导出报告时使用的版本，仅校验版本号前两位，例如6.1.x.x导出的报告，可以在6.1.x.x及以上版本中导入。

操作步骤如下：

1. 点击AppAnalyzer底部的**体检历史**按钮，点击右上角的**导入报告**按钮，根据界面提示，确保即将导入的报告满足相关要求。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/udbRV5jyTL-HzL05HqhXgQ/zh-cn_image_0000002561833161.png?HW-CC-KV=V1&HW-CC-Date=20260429T054701Z&HW-CC-Expire=86400&HW-CC-Sign=B9F049FF66AAE29F9015E3EA3AA46D443C63F60D670EF163E331A695F2974202)
2. 选择本地的体检报告zip文件，点击**确定**后，等待报告导入。导入成功后，AppAnalyzer会自动打开报告。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/Pt0h7zXbSteszmiJPZddVw/zh-cn_image_0000002561833169.png?HW-CC-KV=V1&HW-CC-Date=20260429T054701Z&HW-CC-Expire=86400&HW-CC-Sign=E5F1E0DEF479575AD868A6F9A55C2DECF5BAC683B479BE4C1073474A8024051E)
