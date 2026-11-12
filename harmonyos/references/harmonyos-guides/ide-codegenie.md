---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-codegenie
title: 工具概述
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 工具概述
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:47cbd27beae71ad92b90f622fb4545a03382166c9a834e5278d883762b6d3ff6
---

DevEco CodeGenie是DevEco Studio AI辅助编程工具，支持智能问答、代码生成、页面生成、万能卡片生成、单元测试用例生成、代码智能解读、编译报错智能分析、智慧调优、应用UI生成、意图装饰器生成、小艺智能体创建、自定义Agent等能力，帮助开发者更高效地开发应用。

## 使用方式

在DevEco Studio右侧边栏点击**CodeGenie**，26.0.0 Beta1之前版本，可直接进入CodeGenie问答界面；从26.0.0 Beta1版本开始，进入CodeGenie后界面如下图显示，点击**View Installation Guide**可查看DevEco Code的具体操作指导，点击**Continue with CodeGenie**可进入CodeGenie问答界面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/NJBHl2kiSHW3plMw6TGLVQ/zh-cn_image_0000002808767087.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=ED9D114FAC1FBBB2ED050EB5320D77CE3181567A75E368A96F5D1E38F7422174 "点击放大")

进入CodeGenie问答界面后，若未登录点击**Sign in**，跳转至华为账号登录页面。授权登录完成后返回DevEco Studio，提示登录成功后点击**Agree**，同意隐私安全政策及使用条款后开始体验。

若需使用最新版本的CodeGenie，可通过[下载中心](https://developer.huawei.com/consumer/cn/download/deveco-codegenie)获取并使用相关功能，具体请参考[插件获取及安装](ide-codegenie.md#section18337533718)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/dHuq5eYORqmK9Wsc1d2DNw/zh-cn_image_0000002808887171.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=A9A1926E2193F0351024931CF14076B72C94CD4B42DC427E7707AB4740699C20)

**说明** 

* 若已经安装DevEco Code，打开CodeGenie后直接进入CodeGenie问答界面。
* 支持通过快捷键**Alt****/Option+U**，进入或隐藏CodeGenie问答界面。

## 插件获取及安装

若在历史版本的DevEco Studio中使用最新版本的CodeGenie，可通过[下载中心](https://developer.huawei.com/consumer/cn/download/deveco-codegenie)获取最新的CodeGenie插件版本，并根据下载中心页面**工具完整性**指导进行完整性校验。插件安装包的存放路径不能包含中文字符。

下载完成后，插件安装包**无需解压**，依照下方步骤进行安装：

1. 在DevEco Studio菜单栏，点击**File > Settings**（macOS为**DevEco Studio > Preferences****/****Settings**）**> Plugins**，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/0sgfvUckQoaHBwseb0w4dQ/zh-cn_image_0000002779567510.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=69BDD2F9A7425EA6CF196592BDA9B8EF3A266AF86B57A9FE2018AFF021FC5446) **> Install Plugin from Disk…**安装本地插件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/h1xHoBvkRKGF9LaSJeCzAQ/zh-cn_image_0000002779567508.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=6A2EB55C3B4A02EE37D3E81485E78335032D7F1FC8DAF7755C6A3358E412F870)
2. 在弹出的文件选择窗口中，选择**未解压的插件****包**的存放位置，点击**OK**确认安装插件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/xqpt-t2CQZ6ZbeLD0NAtCg/zh-cn_image_0000002779407532.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=6569D09A5D432638D96AEDA26F92F305F1D4CFF8E97CE638C6387E4193EEE8FE)
3. 点击**Restart IDE**，重新启动DevEco Studio。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/8TuBr5eeReOmA6juKwzZWw/zh-cn_image_0000002808887173.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=CA07F2F3636D1EDEFB3DFF9D31ACDEDE0E2F0361BFAC2FF8E3EB3DF06E0ECB59)
4. 在DevEco Studio右侧边栏点击**CodeGenie**，完成登录并开始体验。

**说明** 

进入**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> CodeGenie****> General**页面，勾选**Auto Update**，可以自动升级插件配置。

若管理台配置的插件可以静默升级，且系统检测到插件需要更新时，插件会自动升级；不勾选时会有弹框提示用户手动升级。若管理台配置的插件不支持静默升级，均有弹框提示用户手动升级。
