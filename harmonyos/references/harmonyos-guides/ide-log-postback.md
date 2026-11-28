---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-log-postback
title: 日志收集和诊断数据
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 附录 > 日志收集和诊断数据
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:41+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:5d199194edde92583c41ecdb3793924ff79cf2f02026848e79053520e90b9df5
---

若开发过程中遇到DevEco Studio卡顿、卡死或其他故障时，可通过如下两种方式回传日志信息，帮助DevEco Studio提升稳定性体验。

**说明** 

该功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

**方式一**

可点击**DevEco Studio** **Error**问题弹窗中的**Send Report**，点击**OK**后向DevEco Studio回传日志信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/ibNwdziUTriuW8-sJbMzOA/zh-cn_image_0000002779407318.png?HW-CC-KV=V1&HW-CC-Date=20261128T023441Z&HW-CC-Expire=31536000000&HW-CC-Sign=B0B5F45F3FF17D43C4CAD9517394CB2BD254FC5E0338E1F4AF01A9D2A492BB47)

**方式二**

1. 开发者需要开启数据采集功能，请在**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**）**> Appearance & Behavior > System Settings > Data Sharing**设置界面，勾选**Send usage statistics**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/S0IOe-ovQy6npN6fJNqHag/zh-cn_image_0000002779407320.png?HW-CC-KV=V1&HW-CC-Date=20261128T023441Z&HW-CC-Expire=31536000000&HW-CC-Sign=CD378D506F55A29E53F5F267B8CB4C79429B275EB0E935E8ACC1A60D74F31A67)
2. 回传DevEco Studio日志信息。

   * 26.0.0及以上版本
     1. 点击菜单栏**Help > Collect Logs and Diagnostic Data**或点击工具窗口右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/Jzl7NvNIRXeZue-toRDxVg/zh-cn_image_0000002779567300.png?HW-CC-KV=V1&HW-CC-Date=20261128T023441Z&HW-CC-Expire=31536000000&HW-CC-Sign=FEAE93B3B34F007E75517964E7D28698E3D18B91F4E09D17662ED734BB5CD194)Feedback按钮。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/emi1gqrUSySWnjaKDJs8wA/zh-cn_image_0000002779567298.png?HW-CC-KV=V1&HW-CC-Date=20261128T023441Z&HW-CC-Expire=31536000000&HW-CC-Sign=74EFE3F2FBB8758A9EB00D8CE9B5807E046A916728D2BE8518D89244EF75C0D0 "点击放大")
     2. 在**Problem Description**中填写问题描述，点击**Add**可上传图片或视频文件，点击**View Details**查看和选择要上传的.log文件。若需上传日志文件，请勾选**Upload DevEco Studio Logs。**点击**Submit**，向DevEco Studio回传日志信息。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/OeReCoLdTAqNuW7jdV3sig/zh-cn_image_0000002808886963.png?HW-CC-KV=V1&HW-CC-Date=20261128T023441Z&HW-CC-Expire=31536000000&HW-CC-Sign=5DEAA74F8B03E7FA6AEECEE46822C8184DD07D9047F4BC4394D148B07C6D0191)

        **说明** 

        附件和日志文件最大支持上传500MB的文件，且附件仅支持上传图片或视频文件。
   * 26.0.0以下版本
     1. 点击菜单栏**Help > Collect Logs and Diagnostic Data。**

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/0uvQzCxMRsyiGmbnhuZq-Q/zh-cn_image_0000002808886965.png?HW-CC-KV=V1&HW-CC-Date=20261128T023441Z&HW-CC-Expire=31536000000&HW-CC-Sign=0E9E74F6D97F4C566F4DE5B3929DB808D24620BF11A004B1170FC2EDFBBBEA8A "点击放大")
     2. 选择.log文件后，点击**OK**向DevEco Studio回传日志信息。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/m4kespzQQrGul-hgBKUwcw/zh-cn_image_0000002808766883.png?HW-CC-KV=V1&HW-CC-Date=20261128T023441Z&HW-CC-Expire=31536000000&HW-CC-Sign=657DC7143A47E0E64FC4A54C299142C5F430C24B3B8F26CAC5A9DADA72B16D92 "点击放大")
