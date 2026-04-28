---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-codegenie
title: 工具概述
breadcrumb: 指南 > 使用AI智能辅助编程 > 工具概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6299412f812b70603b9730afbb6dceaabf65f49ee1633427d0163e88023a64e9
---

DevEco CodeGenie是DevEco Studio AI辅助编程工具，支持智能问答、代码生成、页面生成、万能卡片生成、单元测试用例生成、代码智能解读、编译报错智能分析、智慧调优、应用UI生成、意图装饰器生成、小艺智能体创建、自定义Agent等能力，帮助开发者更高效地开发应用。

## 使用方式

在DevEco Studio右侧边栏点击**CodeGenie**或通过快捷键**Alt/Option+U**，进入CodeGenie。点击**Sign in** ，跳转至华为账号登录页面。授权登录完成后返回DevEco Studio，提示登录成功后点击**Agree**，同意隐私安全政策及使用条款后开始体验。

若需使用最新版本的CodeGenie，可通过[下载中心](https://developer.huawei.com/consumer/cn/download/deveco-codegenie)获取并使用相关功能，具体请参考[插件获取及安装](ide-codegenie.md#section18337533718)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/yKAL3s0ZREqKirM0-OfhYw/zh-cn_image_0000002561833547.png?HW-CC-KV=V1&HW-CC-Date=20260427T235511Z&HW-CC-Expire=86400&HW-CC-Sign=D7D879C14795B35E8037B0FF3F5E9173254BBAEE3571FA2374258A35D083FBAB)

## 插件获取及安装

若在历史版本的DevEco Studio中使用最新版本的CodeGenie，可通过[下载中心](https://developer.huawei.com/consumer/cn/download/deveco-codegenie)获取最新的CodeGenie插件版本，并根据下载中心页面**工具完整性**指导进行完整性校验。插件安装包的存放路径不能包含中文字符。

下载完成后，插件安装包**无需解压**，依照下方步骤进行安装：

1. 在DevEco Studio菜单栏，点击**File > Settings**（macOS为**DevEco Studio > Preferences****/****Settings**）**> Plugins**，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/sY4DjvKZRCSDyazXmHeh8Q/zh-cn_image_0000002530753624.png?HW-CC-KV=V1&HW-CC-Date=20260427T235511Z&HW-CC-Expire=86400&HW-CC-Sign=F0A05FD63C28A48D0CDA488FBBE11ADA03135A18C9446904961F619DE691683A) **> Install Plugin from Disk…**安装本地插件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/kFF6IjG9Tqei5Mmskfqf3w/zh-cn_image_0000002530753626.png?HW-CC-KV=V1&HW-CC-Date=20260427T235511Z&HW-CC-Expire=86400&HW-CC-Sign=6F51FAED633B4D9555906BEF38635F04E16021FDDDF21A96FA336CCAA300F966)
2. 在弹出的文件选择窗口中，选择**未解压的插件****包**的存放位置，点击**OK**确认安装插件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/ywTml2xAQqC381EhREEnjA/zh-cn_image_0000002561753567.png?HW-CC-KV=V1&HW-CC-Date=20260427T235511Z&HW-CC-Expire=86400&HW-CC-Sign=8D08956B86A5B0D1D1272054534AF44978AA410BC25CE4253686C03F2A43B587)
3. 点击**Restart IDE**，重新启动DevEco Studio。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/H6omr4sNR2-n3PmrcyEWpw/zh-cn_image_0000002561753563.png?HW-CC-KV=V1&HW-CC-Date=20260427T235511Z&HW-CC-Expire=86400&HW-CC-Sign=39DEC30D90FF85AB86645A03A753EAC7356B044720424E0CE47D42E8CB4F1A73)
4. 在DevEco Studio右侧边栏点击**CodeGenie**，完成登录并开始体验。

说明

进入**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> CodeGenie****> General**页面，勾选**Auto Update**，可以自动升级插件配置。

若管理台配置的插件可以静默升级，且系统检测到插件需要更新时，插件会自动升级；不勾选时会有弹框提示用户手动升级。若管理台配置的插件不支持静默升级，均有弹框提示用户手动升级。
