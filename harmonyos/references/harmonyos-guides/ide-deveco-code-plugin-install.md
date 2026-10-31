---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-code-plugin-install
title: 快速入门
breadcrumb: 指南 > DevEco Code > DevEco Studio Plugin > 快速入门
category: harmonyos-guides
scraped_at: 2026-11-01T07:13:14+08:00
doc_updated_at: 2026-10-31
content_hash: sha256:4d96223abaf6230cbaf137ef13f2312661ecb2b2a7c6ba63bfdf4877a450e977
---

## 环境准备

1. DevEco Studio版本要求：DevEco Studio 26.0.0 Beta2及以上版本。
2. DevEco Code插件依赖CodeGenie，需要在DevEco Studio菜单栏点击**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**）**> Plugins**，搜索和启用CodeGenie插件。CodeGenie插件默认已启用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/Pvip76O2R_qlvdvrGRrlug/zh-cn_image_0000002776793476.png)

## 安装和更新

### 一键安装

1. 在DevEco Studio左侧边栏点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/h33eXJLQSo-Lr2jJImwULA/zh-cn_image_0000002806073173.png)图标，打开DevEco Code**。**
2. 点击**Install Now**安装DevEco Code插件。若未登录请先点击**Sign in**，在华为账号登录页面完成登录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/C2KNuQ5fQUeU8yqc2V7o0g/zh-cn_image_0000002776953452.png "点击放大")
3. 点击**Installation complete.Restart IDE.**，重启DevEco Studio后开始使用。

**说明** 

若左侧边栏未出现![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/Q4gsHTY_Q1aLlcJZdOfdZQ/zh-cn_image_0000002806153081.png)图标，需先点击弹窗中的**立即更新**，升级CodeGenie版本。

### 更新

进入**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> CodeGenie****> General**页面，勾选**Auto Update**，可以自动升级插件配置。

开启自动升级后，若管理台配置的插件可以静默升级，且系统检测到插件需要更新时，插件会自动升级；若管理台配置的插件不支持静默升级，会有弹框提示用户手动升级。未开启自动升级，也会有弹框提示用户手动升级。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/UxMPaHZcQW2NwSA_rooANg/zh-cn_image_0000002776793482.png)

## 会话管理

* **新建会话**：点击顶部**New Conversation**，即可创建新会话。
* **重命名会话**：在会话标题上右键，点击**Rename**，即可输入新的会话名称。
* **收藏****会话**：在会话标题上右键，点击**Favorite**，即可收藏或者取消收藏。
* **归档****会话**：在会话标题上右键 ，点击**Archive**，即可归档。
* **删除****会话**：在会话标题上点删除图标，即可以删除会话。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/6_pixqbETES-ZUlLjqKi0w/zh-cn_image_0000002806073177.png)

## 会话交互

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/UzBLQJuURJ2UDL0dL-K8eg/zh-cn_image_0000002806083591.png "点击放大")

* **发送消息**：在输入框需求描述，按**Enter**或点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/sj7JtM_ATeWclGLlqzPwkQ/zh-cn_image_0000002776963870.png)按钮发送后，等待回复。
* **停止生成**：内容生成过程中，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/6uDimH-oSFuF1LIa8VEBjA/zh-cn_image_0000002806163507.png)按钮，即可停止生成。
* **查看历史输入对话**：输入框为空时，通过键盘上/下方向键可浏览已发送的会话，包括附件和文件引用。
* **添加上下文：**为会话添加上下文帮助工具更准确地理解开发者需求，可通过如下方式添加：

  + 方式一：在输入框中输入**@**符号，在弹出的项目文件搜索列表中选择所需文件，所选文件以标签形式显示在输入框上方（如@index.d.ts），问答时将自动读取所选文件内容。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/1vmE-axXS--Cge73gyNZpQ/zh-cn_image_0000002776803888.png "点击放大")
  + 方式二：点击输入框中**＋**按钮，可以添加文件或图片（格式包括PNG、JPG、GIF、WEBP），问答时将自动读取附件内容。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/_DxvYfSaTU-UD0LoJTX9Hw/zh-cn_image_0000002806083595.png)
  + 方式三：在编辑器选中代码后右键，选择**DevEco Code > Quick Chat**，问答时将自动定位和读取所选代码行。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/1AstOnbDReGkDAn0GUa6WA/zh-cn_image_0000002776963874.png "点击放大")

## 模型切换

点击底部输入框的模型名称下拉框，即可切换模型；在搜索框输入模型名称快速过滤模型；点击**Add model**配置更多模型，配置模型具体请参考[配置Models](ide-deveco-code-plugin-models.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/xDSIkEOBSQSe4Ot-PD4igA/zh-cn_image_0000002806073183.png)

## Agent模式切换

在底部输入框点击**Build**后的下拉框，可切换不同Agent模式。Agent模式介绍请参考[Agent模式](ide-deveco-code-agent.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/bfLa3bmbQ5OXiZ088LMCag/zh-cn_image_0000002776953462.png)

## 快捷命令

在底部输入框输入"**/**"，即可调用斜杠命令，通过键盘**上/下键**选择不同命令，点击**Enter**确认和点击**Esc**退出命令。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/g2WQI-TiRKqNBAnQvghCUA/zh-cn_image_0000002806153089.png)
