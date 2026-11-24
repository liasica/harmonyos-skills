---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-codegenie
title: 工具概述
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 工具概述
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:38+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:b1f579f3a3d916d5e988d0fc9224b8939480a050030c9195c6d17c2a4254ba25
---

DevEco CodeGenie是DevEco Studio AI辅助编程工具，支持智能问答、代码生成、页面生成、万能卡片生成、单元测试用例生成、代码智能解读、编译报错智能分析、智慧调优、应用UI生成、意图装饰器生成、小艺智能体创建、自定义Agent等能力，帮助开发者更高效地开发应用。

## 使用方式

在DevEco Studio右侧边栏点击**CodeGenie**，26.0.0 Beta1之前版本，可直接进入CodeGenie问答界面；从26.0.0 Beta1版本开始，进入CodeGenie后界面如下图显示，点击**View Installation Guide**可查看DevEco Code的具体操作指导，点击**Continue with CodeGenie**可进入CodeGenie问答界面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/Kxz62siDSt2fPXNC-PoG0w/zh-cn_image_0000002808767087.png?HW-CC-KV=V1&HW-CC-Date=20261124T044238Z&HW-CC-Expire=31536000000&HW-CC-Sign=5B513D8EA02B8208CB69F0960BB8B33A5F50902E4BAC39937E44F490B9616C26 "点击放大")

进入CodeGenie问答界面后，若未登录点击**Sign in**，跳转至华为账号登录页面。授权登录完成后返回DevEco Studio，提示登录成功后点击**Agree**，同意隐私安全政策及使用条款后开始体验。

若需使用最新版本的CodeGenie，可通过[下载中心](https://developer.huawei.com/consumer/cn/download/deveco-codegenie)获取并使用相关功能，具体请参考[插件获取及安装](ide-codegenie.md#section18337533718)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/q5KfrTwtQHK_8AXhYFD6cA/zh-cn_image_0000002808887171.png?HW-CC-KV=V1&HW-CC-Date=20261124T044238Z&HW-CC-Expire=31536000000&HW-CC-Sign=3E310BFDBB42F4FAC0D3EBA0847C08D6A567CD63C17988725F67597131E69926)

**说明** 

* 若已经安装DevEco Code，打开CodeGenie后直接进入CodeGenie问答界面。
* 支持通过快捷键**Alt****/Option+U**，进入或隐藏CodeGenie问答界面。

## 插件获取及安装

若在历史版本的DevEco Studio中使用最新版本的CodeGenie，可通过[下载中心](https://developer.huawei.com/consumer/cn/download/deveco-codegenie)获取最新的CodeGenie插件版本，并根据下载中心页面**工具完整性**指导进行完整性校验。插件安装包的存放路径不能包含中文字符。

下载完成后，插件安装包**无需解压**，依照下方步骤进行安装：

1. 在DevEco Studio菜单栏，点击**File > Settings**（macOS为**DevEco Studio > Preferences****/****Settings**）**> Plugins**，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/LYKberApSrO944OGl1So1w/zh-cn_image_0000002779567510.png?HW-CC-KV=V1&HW-CC-Date=20261124T044238Z&HW-CC-Expire=31536000000&HW-CC-Sign=1F4A2F0F89AF1423C57999459A0D1C85959124776272096FD9FB7C20559FE92A) **> Install Plugin from Disk…**安装本地插件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/qaZ1kp46TnugfzfFlRB02w/zh-cn_image_0000002779567508.png?HW-CC-KV=V1&HW-CC-Date=20261124T044238Z&HW-CC-Expire=31536000000&HW-CC-Sign=39AED9C0918C04675281A7614823E24B143BA34101EDB2A188667E42AD1F1633)
2. 在弹出的文件选择窗口中，选择**未解压的插件****包**的存放位置，点击**OK**确认安装插件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/oOet0NPvS0eXTNEwlX_8Og/zh-cn_image_0000002779407532.png?HW-CC-KV=V1&HW-CC-Date=20261124T044238Z&HW-CC-Expire=31536000000&HW-CC-Sign=35ECAD4A9F491A10D767510FF0C175D5EC763FEBBDBE700149B5A1F7071C060C)
3. 点击**Restart IDE**，重新启动DevEco Studio。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/lxidZAKGSl6cpCYZv-0nJQ/zh-cn_image_0000002808887173.png?HW-CC-KV=V1&HW-CC-Date=20261124T044238Z&HW-CC-Expire=31536000000&HW-CC-Sign=2DBBC270FF6D0A8BD064CB79B7BA59BA7B4CD278C1D85657D6634E43A326D380)
4. 在DevEco Studio右侧边栏点击**CodeGenie**，完成登录并开始体验。

**说明** 

进入**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> CodeGenie****> General**页面，勾选**Auto Update**，可以自动升级插件配置。

若管理台配置的插件可以静默升级，且系统检测到插件需要更新时，插件会自动升级；不勾选时会有弹框提示用户手动升级。若管理台配置的插件不支持静默升级，均有弹框提示用户手动升级。
