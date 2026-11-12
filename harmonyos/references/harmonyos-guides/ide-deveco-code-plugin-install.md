---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-code-plugin-install
title: 快速入门
breadcrumb: 指南 > DevEco Code > DevEco Code Plugin > 快速入门
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:26+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:83ae6a73eb82c139495a1d43c9aec9f283db742f3d746b94c31ec5bd384188a9
---

## 环境准备

1. DevEco Studio版本要求：DevEco Studio 6.0.0、DevEco Studio 6.0.1、DevEco Studio 6.0.2、DevEco Studio 6.1.0、DevEco Studio 6.1.1、DevEco Studio 26.0.0 Beta2及以上版本。
2. DevEco Code插件依赖CodeGenie，需要在DevEco Studio菜单栏点击**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**）**> Plugins**，搜索和启用CodeGenie插件。CodeGenie插件默认已启用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/PQvhk4OLT5W5aYyK0WWsgQ/zh-cn_image_0000002808766603.png)

## 安装和更新

### 一键安装

1. 在DevEco Studio左侧边栏点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/km2ko9LLSne46O7ZU5Untw/zh-cn_image_0000002808766607.png)图标，打开DevEco Code**。**
2. 点击**Install Now**安装DevEco Code插件。若未登录请先点击**Sign in**，在华为账号登录页面完成登录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/SQgnhfVDTTS0lsdnqCo3ug/zh-cn_image_0000002779407036.png "点击放大")
3. 点击**Installation complete.Restart IDE.**，重启DevEco Studio后开始使用。

**说明** 

若左侧边栏未出现![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/BSfGYWRMQBu9zcXXjtGBsQ/zh-cn_image_0000002808886675.png)图标，需先点击弹窗中的**立即更新**，升级CodeGenie版本。

### 本地安装

可通过[下载中心](https://developer.huawei.com/consumer/cn/download/deveco-code)获取最新的DevEco Code插件版本，并根据下载中心页面**工具完整性**指导进行完整性校验。插件安装包的存放路径不能包含中文字符。

DevEco Code插件版本需与DevEco Studio版本相匹配，具体对应关系如下：

* DevEco Studio 6.0.0、DevEco Studio 6.0.1、DevEco Studio 6.0.2、DevEco Studio 6.1.0、DevEco Studio 6.1.1支持安装DevEco Code Plugin 6.1.1 Release版本。
* DevEco Studio 26.0.0 Beta2及以上版本支持安装DevEco Code Plugin 26.0.1 Beta1及以上版本。

下载完成后，插件安装包无需解压，依照下方步骤进行安装：

1. 在DevEco Studio菜单栏，点击**File > Settings**（macOS为**DevEco Studio > Preferences****/****Settings**）**> Plugins**，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/iWmSbLCPSgOk2jOCyS-Z7Q/zh-cn_image_0000002779407052.png) **> Install Plugin from Disk…**安装本地插件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/zN82YCnkTPmp6PFrgNXcYA/zh-cn_image_0000002779567022.png)
2. 在弹出的文件选择窗口中，选择**未解压的插件****包**的存放位置，点击**OK**确认安装插件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/N4Iq8ujPRJGVDsnxcJqQRA/zh-cn_image_0000002808766597.png)
3. 在DevEco Studio左侧边栏点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/zyP2ndtOQNWnvY4t5fVIfA/zh-cn_image_0000002808886693.png)图标，登录后开始体验DevEco Code。

### 更新

进入**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> CodeGenie****> General**页面，勾选**Auto Update**，可以自动升级插件配置。

开启自动升级后，若管理台配置的插件可以静默升级，且系统检测到插件需要更新时，插件会自动升级；若管理台配置的插件不支持静默升级，会有弹框提示用户手动升级。未开启自动升级，也会有弹框提示用户手动升级。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/05PsO0_-RlWFQhswIB8dLg/zh-cn_image_0000002808766615.png)

## 会话管理

* **新建会话**：点击顶部**New Conversation**，即可创建新会话。
* **重命名会话**：在会话标题上右键，点击**Rename**，即可输入新的会话名称。
* **收藏****会话**：在会话标题上右键，点击**Favorite**，即可收藏或者取消收藏。
* **归档****会话**：在会话标题上右键 ，点击**Archive**，即可归档。
* **删除****会话**：在会话标题上点删除图标，即可以删除会话。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/wRdQFtfpRuKfunb86fXzRw/zh-cn_image_0000002808886691.png "点击放大")

## 会话交互

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/QxW0ccZsRWy4X1mHuAj2Vg/zh-cn_image_0000002783548358.png "点击放大")

* **发送消息**：在输入框需求描述，按**Enter**或点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/LOTGGNAaRAGunWU4sWj9eQ/zh-cn_image_0000002779407042.png)按钮发送后，等待回复。
* **停止生成**：内容生成过程中，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/q6-yXQ_6S9eJ3yMpehE6MQ/zh-cn_image_0000002808886695.png)按钮，即可停止生成。
* **查看历史输入对话**：输入框为空时，通过键盘上/下方向键可浏览已发送的会话，包括附件和文件引用。
* **添加上下文：**为会话添加上下文帮助工具更准确地理解开发者需求，可通过如下方式添加：

  + 方式一：在输入框中输入**@**符号，在弹出的项目文件搜索列表中选择所需文件，所选文件以标签形式显示在输入框上方（如@index.d.ts），问答时将自动读取所选文件内容。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/XsLB3zKSQLO6syte6dqOjQ/zh-cn_image_0000002812947819.png)
  + 方式二：点击输入框中**＋**按钮，可以添加文件或图片（格式包括PNG、JPG、GIF、WEBP），问答时将自动读取附件内容。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/UuegKO-0QnW7-D6AvM8l-A/zh-cn_image_0000002783708300.png)
  + 方式三：在编辑器选中代码后右键，选择**DevEco Code > Quick Chat**，问答时将自动定位和读取所选代码行。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/Gw1jDBSkRJGzOEtTcI573Q/zh-cn_image_0000002779407054.png "点击放大")

## 模型切换

点击底部输入框的模型名称下拉框，即可切换模型；在搜索框输入模型名称快速过滤模型；点击**Add model**配置更多模型，配置模型具体请参考[配置Models](ide-deveco-code-plugin-models.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/0esCH7H7QhOar4z9i56Uzw/zh-cn_image_0000002779567028.png)

## Agent模式切换

在底部输入框点击**Build**后的下拉框，可切换不同Agent模式。Agent模式介绍请参考[Agent模式](ide-deveco-code-agent.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/LjZVlHnSQL2e-PamPPwl5g/zh-cn_image_0000002812947047.png)

## 快捷命令

在底部输入框输入"**/**"，即可调用斜杠命令，通过键盘**上/下键**选择不同命令，点击**Enter**确认和点击**Esc**退出命令。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/9_FWLpNfRq-0s78VtEf5Eg/zh-cn_image_0000002783548360.png)
