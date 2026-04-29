---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-codegenie
title: 工具概述
breadcrumb: 指南 > 使用AI智能辅助编程 > 工具概述
category: harmonyos-guides
scraped_at: 2026-04-29T13:45:09+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:e0644626ab3bc0b3abbe62a577baba1f9a8e8e329ee472fee77bf209f890b456
---

DevEco CodeGenie是DevEco Studio AI辅助编程工具，支持智能问答、代码生成、页面生成、万能卡片生成、单元测试用例生成、代码智能解读、编译报错智能分析、智慧调优、应用UI生成、意图装饰器生成、小艺智能体创建、自定义Agent等能力，帮助开发者更高效地开发应用。

## 使用方式

在DevEco Studio右侧边栏点击**CodeGenie**或通过快捷键**Alt/Option+U**，进入或隐藏CodeGenie。点击**Sign in** ，跳转至华为账号登录页面。授权登录完成后返回DevEco Studio，提示登录成功后点击**Agree**，同意隐私安全政策及使用条款后开始体验。

若需使用最新版本的CodeGenie，可通过[下载中心](https://developer.huawei.com/consumer/cn/download/deveco-codegenie)获取并使用相关功能，具体请参考[插件获取及安装](ide-codegenie.md#section18337533718)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/kfh96owzRGy1Mn1FMKjEDQ/zh-cn_image_0000002561833547.png?HW-CC-KV=V1&HW-CC-Date=20260429T054507Z&HW-CC-Expire=86400&HW-CC-Sign=7C2735EC53FD838A2B900DEDDC95370FAA29BE7D13B14A2512A8AAC4EC68BDF1)

## 插件获取及安装

若在历史版本的DevEco Studio中使用最新版本的CodeGenie，可通过[下载中心](https://developer.huawei.com/consumer/cn/download/deveco-codegenie)获取最新的CodeGenie插件版本，并根据下载中心页面**工具完整性**指导进行完整性校验。插件安装包的存放路径不能包含中文字符。

下载完成后，插件安装包**无需解压**，依照下方步骤进行安装：

1. 在DevEco Studio菜单栏，点击**File > Settings**（macOS为**DevEco Studio > Preferences****/****Settings**）**> Plugins**，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/QWrbmdnITOWpMne7UqkFdQ/zh-cn_image_0000002530753624.png?HW-CC-KV=V1&HW-CC-Date=20260429T054507Z&HW-CC-Expire=86400&HW-CC-Sign=C1679DD716A1949F616B12265A039A71D4E63EF55717D31089E2E871CC581111) **> Install Plugin from Disk…**安装本地插件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/awTVISO7RciajP1SHKk4UQ/zh-cn_image_0000002530753626.png?HW-CC-KV=V1&HW-CC-Date=20260429T054507Z&HW-CC-Expire=86400&HW-CC-Sign=1FCF9036A2A0B5F975A8319F88602171D1BF3097BC31BA7C8C87C7D77A9A34BF)
2. 在弹出的文件选择窗口中，选择**未解压的插件****包**的存放位置，点击**OK**确认安装插件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/tLdJ3WDmTcWznGf1aeIVDA/zh-cn_image_0000002561753567.png?HW-CC-KV=V1&HW-CC-Date=20260429T054507Z&HW-CC-Expire=86400&HW-CC-Sign=0861741A875574D229DACD326E9A52944183FE4A7741191637EF014EB8BE1D27)
3. 点击**Restart IDE**，重新启动DevEco Studio。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/QSbR_9bYTuq2cCbnhmJFeA/zh-cn_image_0000002561753563.png?HW-CC-KV=V1&HW-CC-Date=20260429T054507Z&HW-CC-Expire=86400&HW-CC-Sign=36D7A5EFC768415B6AACEE2D415B7F154BB07C33A770D294D95E1581F66167F6)
4. 在DevEco Studio右侧边栏点击**CodeGenie**，完成登录并开始体验。

说明

进入**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> CodeGenie****> General**页面，勾选**Auto Update**，可以自动升级插件配置。

若管理台配置的插件可以静默升级，且系统检测到插件需要更新时，插件会自动升级；不勾选时会有弹框提示用户手动升级。若管理台配置的插件不支持静默升级，均有弹框提示用户手动升级。
