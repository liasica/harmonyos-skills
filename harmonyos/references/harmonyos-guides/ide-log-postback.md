---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-log-postback
title: 日志收集和诊断数据
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 附录 > 日志收集和诊断数据
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:d60357c31a268b088b631e4e1c76d668f3e0bb520276a17427ade0bda8d3f362
---

若开发过程中遇到DevEco Studio卡顿、卡死或其他故障时，可通过如下两种方式回传日志信息，帮助DevEco Studio提升稳定性体验。

**说明** 

该功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

**方式一**

可点击**DevEco Studio** **Error**问题弹窗中的**Send Report**，点击**OK**后向DevEco Studio回传日志信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/slFPMs_tT8OxYscYkzlCsQ/zh-cn_image_0000002779407318.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=305E1A01B3CECD892755E8E8F3F43783D2E3EE79181A32DB56893BB80DB39C06)

**方式二**

1. 开发者需要开启数据采集功能，请在**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**）**> Appearance & Behavior > System Settings > Data Sharing**设置界面，勾选**Send usage statistics**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/tY6jHo3cS2WCFnwH05LFUQ/zh-cn_image_0000002779407320.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=506DFCCC34C9304C3EF8A49DB1F19420C0B8316C8F2879C24073023D45A3EB6F)
2. 回传DevEco Studio日志信息。

   * 26.0.0及以上版本
     1. 点击菜单栏**Help > Collect Logs and Diagnostic Data**或点击工具窗口右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/M0ILs5c9R6GZpxOBtoAo5w/zh-cn_image_0000002779567300.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=99C58B0EB57FB33F402F372433B23ECDEAEB3576CD4B593581999BA90899AFA3)Feedback按钮。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/2nDmPXwcSDuQ03ASBaiXAw/zh-cn_image_0000002779567298.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=7BF5C7785A0699C63A6608C35FBD87E4F39C9138D769893E00636CF37CB257D3 "点击放大")
     2. 在**Problem Description**中填写问题描述，点击**Add**可上传图片或视频文件，点击**View Details**查看和选择要上传的.log文件。若需上传日志文件，请勾选**Upload DevEco Studio Logs。**点击**Submit**，向DevEco Studio回传日志信息。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/mgvtZuuLTbuj832lyI1CgA/zh-cn_image_0000002808886963.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=4ACF95A28F7F91E49F0BF26085FDF65725AFDBE8A41E34C7B310F7B755428A0D)

        **说明** 

        附件和日志文件最大支持上传500MB的文件，且附件仅支持上传图片或视频文件。
   * 26.0.0以下版本
     1. 点击菜单栏**Help > Collect Logs and Diagnostic Data。**

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/62klE6D4Rn2XwQCaie4F1w/zh-cn_image_0000002808886965.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=CDA2F7D6A48F5CC87C159AF849B6F937DFA4D169DC188AFF9D90572027268904 "点击放大")
     2. 选择.log文件后，点击**OK**向DevEco Studio回传日志信息。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/YCbEGv5gTx62sb-Fb8WMnQ/zh-cn_image_0000002808766883.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=E00B42C31E28D3EE52267FCFC7FB0EE5205EC6BC5CF137D1F36E4D9D00011C4B "点击放大")
