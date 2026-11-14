---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-code-plugin-install
title: 快速入门
breadcrumb: 指南 > DevEco Code > DevEco Code Plugin > 快速入门
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:22+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:790cfba4e8933b073c8f63e682a1296a0de57557ce5a81b4f58e1a3f427030f9
---

## 环境准备

1. DevEco Studio版本要求：DevEco Studio 6.0.0、DevEco Studio 6.0.1、DevEco Studio 6.0.2、DevEco Studio 6.1.0、DevEco Studio 6.1.1、DevEco Studio 26.0.0 Beta2及以上版本。
2. DevEco Code插件依赖CodeGenie，需要在DevEco Studio菜单栏点击**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**）**> Plugins**，搜索和启用CodeGenie插件。CodeGenie插件默认已启用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/gLxoASWMTgqDcMoxywrOjg/zh-cn_image_0000002808766603.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=88DFDAEA9B0447A3F12AA08AF94E2952122FE04F09B32F2689B8418ABA115BB6)

## 安装和更新

### 一键安装

1. 在DevEco Studio左侧边栏点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/fN6H6-KBR6OyNkNm-puIEA/zh-cn_image_0000002808766607.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=9B738E5278F8A56C1E7162988406A480A6E9166DFD0D77427787EB4F0F2E2AEA)图标，打开DevEco Code**。**
2. 点击**Install Now**安装DevEco Code插件。若未登录请先点击**Sign in**，在华为账号登录页面完成登录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/MSpPpzPHTfGSFz8zBPV7Zw/zh-cn_image_0000002779407036.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=E602C3DE9C89836A833FE8B005338CC3539AA006A43F6D5D8620B6EB9A72E322 "点击放大")
3. 点击**Installation complete.Restart IDE.**，重启DevEco Studio后开始使用。

**说明** 

若左侧边栏未出现![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/Dv6rEz1eQWeuo1i5dx0tsQ/zh-cn_image_0000002808886675.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=C4E22E3E93AA11A753F30D74D10C79F2E47EAFC60D4546F29914177FCBD2B2FF)图标，需先点击弹窗中的**立即更新**，升级CodeGenie版本。

### 本地安装

可通过[下载中心](https://developer.huawei.com/consumer/cn/download/deveco-code)获取最新的DevEco Code插件版本，并根据下载中心页面**工具完整性**指导进行完整性校验。插件安装包的存放路径不能包含中文字符。

DevEco Code插件版本需与DevEco Studio版本相匹配，具体对应关系如下：

* DevEco Studio 6.0.0、DevEco Studio 6.0.1、DevEco Studio 6.0.2、DevEco Studio 6.1.0、DevEco Studio 6.1.1支持安装DevEco Code Plugin 6.1.1 Release版本。
* DevEco Studio 26.0.0 Beta2及以上版本支持安装DevEco Code Plugin 26.0.1 Beta1及以上版本。

下载完成后，插件安装包无需解压，依照下方步骤进行安装：

1. 在DevEco Studio菜单栏，点击**File > Settings**（macOS为**DevEco Studio > Preferences****/****Settings**）**> Plugins**，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/SJuwo0rCSvaKSYq39tLrpw/zh-cn_image_0000002779407052.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=F3B96994829C6666EFAE57A272D15A95DD875044309779C18431E69EA5FBF484) **> Install Plugin from Disk…**安装本地插件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/Fl4maXgdSQaC9gF4DuPm6w/zh-cn_image_0000002779567022.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=CF81B9D5B7FDBC2F179D95BCEE1DAA0CFD7CD147007274F7AD0E25952589124A)
2. 在弹出的文件选择窗口中，选择**未解压的插件****包**的存放位置，点击**OK**确认安装插件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/-CRRZUITSNO-9KaAJOh7bQ/zh-cn_image_0000002808766597.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=C41670D99F0A7A537AE84B8839590DCC04321FDA46ECE27A99DC1B7367F4CE80)
3. 在DevEco Studio左侧边栏点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/N76RY4-6QE-dgMZsSD7c7A/zh-cn_image_0000002808886693.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=37730592A91EB33B59367E88A23BF1B6A3CBB1ABF431C6988B68EA9933B7AC9F)图标，登录后开始体验DevEco Code。

### 更新

进入**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> CodeGenie****> General**页面，勾选**Auto Update**，可以自动升级插件配置。

开启自动升级后，若管理台配置的插件可以静默升级，且系统检测到插件需要更新时，插件会自动升级；若管理台配置的插件不支持静默升级，会有弹框提示用户手动升级。未开启自动升级，也会有弹框提示用户手动升级。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/phrggSVcQb-FQCwQ1awerA/zh-cn_image_0000002808766615.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=2890F78C597B268526864CD2D16B5FEB55AB87D673AC74FE2668EE005B2C1123)

## 会话管理

* **新建会话**：点击顶部**New Conversation**，即可创建新会话。
* **重命名会话**：在会话标题上右键，点击**Rename**，即可输入新的会话名称。
* **收藏****会话**：在会话标题上右键，点击**Favorite**，即可收藏或者取消收藏。
* **归档****会话**：在会话标题上右键 ，点击**Archive**，即可归档。
* **删除****会话**：在会话标题上点删除图标，即可以删除会话。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/Ye61L58RSsqO1R6vXihWYA/zh-cn_image_0000002808886691.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=D0466A94571652C80F718948623B8AEAC0684182939D61C7CA7F9F94AED0DD07 "点击放大")

## 会话交互

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/AGUmbiAVRKeAc505mAIUYg/zh-cn_image_0000002783548358.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=B3E4DD59D25ECB170880D83AD6BFB75A90CABF9D98CD50CB1E31B57B8B64471E "点击放大")

* **发送消息**：在输入框需求描述，按**Enter**或点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/iLfrFkQ3QqmTAm9R6l7G0w/zh-cn_image_0000002779407042.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=4D4D3FC608A35A970F0611B6D514D80FCB34AC9CF9B2A885CF5FA67D0C3F5A9E)按钮发送后，等待回复。
* **停止生成**：内容生成过程中，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/2YqTMNnFRiuNn74qN6unIQ/zh-cn_image_0000002808886695.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=C4C975C5F80602DA7E20E07BA1A0812033A5644A79D7B4EB0BB7E82D1DAAB115)按钮，即可停止生成。
* **查看历史输入对话**：输入框为空时，通过键盘上/下方向键可浏览已发送的会话，包括附件和文件引用。
* **添加上下文：**为会话添加上下文帮助工具更准确地理解开发者需求，可通过如下方式添加：

  + 方式一：在输入框中输入**@**符号，在弹出的项目文件搜索列表中选择所需文件，所选文件以标签形式显示在输入框上方（如@index.d.ts），问答时将自动读取所选文件内容。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/_MWR9UQcSRSNLtM6CTXBMw/zh-cn_image_0000002812947819.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=7A3EA77DD0D6803E91868BF48CCCA300A38BC522667AF17B5117730C21B0428D)
  + 方式二：点击输入框中**＋**按钮，可以添加文件或图片（格式包括PNG、JPG、GIF、WEBP），问答时将自动读取附件内容。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/xY9o2OH9SDq8FKWmq1R1ow/zh-cn_image_0000002783708300.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=0AF3DA2933C411917697CD42305B8E27A1452594C2601421E87EA0A71EE44E8D)
  + 方式三：在编辑器选中代码后右键，选择**DevEco Code > Quick Chat**，问答时将自动定位和读取所选代码行。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/y3S7taY8Su-m9sryG7CQ7w/zh-cn_image_0000002779407054.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=6178CE491F68ED9ECEF57F0FD00309450D184C665F6B1F34AF21894755C167C4 "点击放大")

## 模型切换

点击底部输入框的模型名称下拉框，即可切换模型；在搜索框输入模型名称快速过滤模型；点击**Add model**配置更多模型，配置模型具体请参考[配置Models](ide-deveco-code-plugin-models.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/dBAXd6FaSBqZZ6I9fnRCIw/zh-cn_image_0000002779567028.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=446DEC5775140044B4C0947CAD86F7635557EFA5523636C20A05CCD004820AC7)

## Agent模式切换

在底部输入框点击**Build**后的下拉框，可切换不同Agent模式。Agent模式介绍请参考[Agent模式](ide-deveco-code-agent.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/yNI00rnTTZSzNtQYpNzfAA/zh-cn_image_0000002812947047.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=55837024C06D7EAF2123535BD672929E8088A4C1D834681E9B94E76FBA1BB365)

## 快捷命令

在底部输入框输入"**/**"，即可调用斜杠命令，通过键盘**上/下键**选择不同命令，点击**Enter**确认和点击**Esc**退出命令。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/W4C2uLfgRx2qGP-EYxaEGQ/zh-cn_image_0000002783548360.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=BB159D3A8EA33E631088365A9E7A9787F89CCA45987D682E8007FF1EDDB726C7)
