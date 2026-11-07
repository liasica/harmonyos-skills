---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-log-postback
title: 日志收集和诊断数据
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 附录 > 日志收集和诊断数据
category: harmonyos-guides
scraped_at: 2026-11-07T08:02:24+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:4b63d20b093f60fd0de3e8efa747e426b3562952dde3391f7e1a1bc62e704430
---

若开发过程中遇到DevEco Studio卡顿、卡死或其他故障时，可通过如下两种方式回传日志信息，帮助DevEco Studio提升稳定性体验。

**说明** 

该功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

**方式一**

可点击**DevEco Studio** **Error**问题弹窗中的**Send Report**，点击**OK**后向DevEco Studio回传日志信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/K1EBH-IUT-acr106sHkczQ/zh-cn_image_0000002701663516.png)

**方式二**

1. 开发者需要开启数据采集功能，请在**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**）**> Appearance & Behavior > System Settings > Data Sharing**设置界面，勾选**Send usage statistics**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/ByrrH5cXQXm2Y1E_S7gHAg/zh-cn_image_0000002701823434.png)
2. 回传DevEco Studio日志信息。

   * 26.0.0及以上版本
     1. 点击菜单栏**Help > Collect Logs and Diagnostic Data**或点击工具窗口右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/ElxIOYMzTd-7DXPt6RDw7A/zh-cn_image_0000002701663508.png)Feedback按钮。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/VbMbbZ9ySFmc4cP5YxIxDA/zh-cn_image_0000002731542705.png "点击放大")
     2. 在**Problem Description**中填写问题描述，点击**Add**可上传图片或视频文件，点击**View Details**查看和选择要上传的.log文件。若需上传日志文件，请勾选**Upload DevEco Studio Logs。**点击**Submit**，向DevEco Studio回传日志信息。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/tlXGTVgcRdOko1SVNpmGgw/zh-cn_image_0000002731542711.png)

        **说明** 

        附件和日志文件最大支持上传500MB的文件，且附件仅支持上传图片或视频文件。
   * 26.0.0以下版本
     1. 点击菜单栏**Help > Collect Logs and Diagnostic Data。**

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/_dDBBcz0Q-e6u4ETYaz4hw/zh-cn_image_0000002701663512.png "点击放大")
     2. 选择.log文件后，点击**OK**向DevEco Studio回传日志信息。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/wYjxGDbNRZ2_aNGzm_Ek6A/zh-cn_image_0000002731382733.png "点击放大")
