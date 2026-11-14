---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-log-postback
title: 日志收集和诊断数据
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 附录 > 日志收集和诊断数据
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:02+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:c9ddda812f807dce07aacb53edd44d156a8157c873d6ae7235780419afd4e63b
---

若开发过程中遇到DevEco Studio卡顿、卡死或其他故障时，可通过如下两种方式回传日志信息，帮助DevEco Studio提升稳定性体验。

**说明** 

该功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

**方式一**

可点击**DevEco Studio** **Error**问题弹窗中的**Send Report**，点击**OK**后向DevEco Studio回传日志信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/b5LF5cZGRs2wJzCqvipZ0w/zh-cn_image_0000002779407318.png?HW-CC-KV=V1&HW-CC-Date=20261114T004714Z&HW-CC-Expire=31536000000&HW-CC-Sign=BE2B075243CED2E401A75445D9BC30D566C829DCEC8183DC4AC75563B6AF7D34)

**方式二**

1. 开发者需要开启数据采集功能，请在**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**）**> Appearance & Behavior > System Settings > Data Sharing**设置界面，勾选**Send usage statistics**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/_EUIwsn_SdqMAsZlXbLWqQ/zh-cn_image_0000002779407320.png?HW-CC-KV=V1&HW-CC-Date=20261114T004714Z&HW-CC-Expire=31536000000&HW-CC-Sign=637F92B4CB86720C50AE0509B7FEC740AF9A9C90203C116DE5565891DFF3517D)
2. 回传DevEco Studio日志信息。

   * 26.0.0及以上版本
     1. 点击菜单栏**Help > Collect Logs and Diagnostic Data**或点击工具窗口右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/FVtdRBXIQVS7tFC88J0rwQ/zh-cn_image_0000002779567300.png?HW-CC-KV=V1&HW-CC-Date=20261114T004714Z&HW-CC-Expire=31536000000&HW-CC-Sign=93EAB6D053F49411A39CFEE7A5B713B7B0A998F2B40962EC24E99C4962FD7781)Feedback按钮。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/FxSvuYDIRJCgV1i-8_3N6Q/zh-cn_image_0000002779567298.png?HW-CC-KV=V1&HW-CC-Date=20261114T004714Z&HW-CC-Expire=31536000000&HW-CC-Sign=E958F72170CD3E337B26D163A4743DEF5281160E5F7D6089E605309810F58FE3 "点击放大")
     2. 在**Problem Description**中填写问题描述，点击**Add**可上传图片或视频文件，点击**View Details**查看和选择要上传的.log文件。若需上传日志文件，请勾选**Upload DevEco Studio Logs。**点击**Submit**，向DevEco Studio回传日志信息。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/1b5x2UJITuakVl18Kdqr8Q/zh-cn_image_0000002808886963.png?HW-CC-KV=V1&HW-CC-Date=20261114T004714Z&HW-CC-Expire=31536000000&HW-CC-Sign=E11AA3973F40418BC75672BC6F4149524F4A393C683E1EEF05440FAE00F723E1)

        **说明** 

        附件和日志文件最大支持上传500MB的文件，且附件仅支持上传图片或视频文件。
   * 26.0.0以下版本
     1. 点击菜单栏**Help > Collect Logs and Diagnostic Data。**

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/CEt3QbynS_Gq7yHSMu-vxg/zh-cn_image_0000002808886965.png?HW-CC-KV=V1&HW-CC-Date=20261114T004714Z&HW-CC-Expire=31536000000&HW-CC-Sign=A9BE4920D80F5887716801A92F1B89B8A394E1206AC2A46622C8DD7E0A02D34B "点击放大")
     2. 选择.log文件后，点击**OK**向DevEco Studio回传日志信息。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/Yd8chcYtSTeLMqz0WdTmPA/zh-cn_image_0000002808766883.png?HW-CC-KV=V1&HW-CC-Date=20261114T004714Z&HW-CC-Expire=31536000000&HW-CC-Sign=EF4179596F4E2100AD92D8DDBFB7CFC2517CA010F160C418664BD953A5493901 "点击放大")
