---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-log-postback
title: 日志收集和诊断数据
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 附录 > 日志收集和诊断数据
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:32+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:a678fcdb597e934b9b68dd1a06c107b347eb31e2124f46602ef5027b1ba9bce2
---

若开发过程中遇到DevEco Studio卡顿、卡死或其他故障时，可通过如下两种方式回传日志信息，帮助DevEco Studio提升稳定性体验。

**说明** 

该功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

**方式一**

可点击**DevEco Studio** **Error**问题弹窗中的**Send Report**，点击**OK**后向DevEco Studio回传日志信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/buSHi8m6SfyfeuqSlSTDlw/zh-cn_image_0000002779407318.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=3670D15E20E76908DCE2B5FEE4898EFAF3A6A99802EFC288B26595A2C375D695)

**方式二**

1. 开发者需要开启数据采集功能，请在**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**）**> Appearance & Behavior > System Settings > Data Sharing**设置界面，勾选**Send usage statistics**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/z4cu13c_QW-lCfOfABTJ6g/zh-cn_image_0000002779407320.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=419BCB270CEC488F5E119F1BC7820DCF10CCC82E62FF8A0BBC8D8D41FEBAC1F0)
2. 回传DevEco Studio日志信息。

   * 26.0.0及以上版本
     1. 点击菜单栏**Help > Collect Logs and Diagnostic Data**或点击工具窗口右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/aP3jIDylSoakucprhef9rg/zh-cn_image_0000002779567300.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=10D889D87DF6D075A6534ED2416D16121A1B1E8A02D1946A938E42AEEA4C7E15)Feedback按钮。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/tPw2_eapSCyI9HWZjFtCMw/zh-cn_image_0000002779567298.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=735284B37F5EE22F6C1B4B14A58902C0D0BC8380DB3872BE0829577C5EFC7781 "点击放大")
     2. 在**Problem Description**中填写问题描述，点击**Add**可上传图片或视频文件，点击**View Details**查看和选择要上传的.log文件。若需上传日志文件，请勾选**Upload DevEco Studio Logs。**点击**Submit**，向DevEco Studio回传日志信息。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/5ddK0EkUQBaZR7ohGUsJow/zh-cn_image_0000002808886963.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=BE862FB0901A069419438A29CEBABC213250129E7AA14EC2F8C9807D7668B537)

        **说明** 

        附件和日志文件最大支持上传500MB的文件，且附件仅支持上传图片或视频文件。
   * 26.0.0以下版本
     1. 点击菜单栏**Help > Collect Logs and Diagnostic Data。**

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/jQMxKh-kQTaU2gimy-TV8g/zh-cn_image_0000002808886965.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=8FC76072F67B96DBED52AAC47BF440A3D1427A4874732895FA2F985C045F4B51 "点击放大")
     2. 选择.log文件后，点击**OK**向DevEco Studio回传日志信息。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/ccPke3GeSzmBI9cCRq5Wgg/zh-cn_image_0000002808766883.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=9CF69D037C56C65F0C2816C9AAA45692C347F90E7160BAB88447FEB19CB3FCAE "点击放大")
