---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-code-plugin-install
title: 快速入门
breadcrumb: 指南 > DevEco Code > DevEco Code Plugin > 快速入门
category: harmonyos-guides
scraped_at: 2026-11-28T10:35:01+08:00
doc_updated_at: 2026-11-27
content_hash: sha256:a936b20852be4305372fecf916ece5bdc5023a0b2580a2803416535635188c46
---

## 环境准备（Windows/macOS）

1. DevEco Studio版本要求：DevEco Studio 6.0.0、DevEco Studio 6.0.1、DevEco Studio 6.0.2、DevEco Studio 6.1.0、DevEco Studio 6.1.1、DevEco Studio 26.0.0 Beta2及以上版本。
2. DevEco Code插件依赖CodeGenie，需要在DevEco Studio菜单栏点击**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**）**> Plugins**，搜索和启用CodeGenie插件。CodeGenie插件默认已启用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/IXmk_dbnQuKmUyi6gnlDjw/zh-cn_image_0000002808766603.png?HW-CC-KV=V1&HW-CC-Date=20261128T023500Z&HW-CC-Expire=31536000000&HW-CC-Sign=D8C37186B5D676C6A6B4CD8A57F4C8DE2B87F5D682F8248BC3B9A22F1A542317)

## 环境准备（鸿蒙电脑）

在**设置** > **隐私和安全** > **高级**，开启**允许来自非应用市场的应用**开关。

若未开启**允许来自非应用市场的应用**开关，会导致DevEco Code新建会话失败，需要重启DevEco Studio。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/BwseVRImQQa20xEnDKG3Rw/zh-cn_image_0000002824400181.png?HW-CC-KV=V1&HW-CC-Date=20261128T023500Z&HW-CC-Expire=31536000000&HW-CC-Sign=C115AFC089E883138107B2B6B98BDCD76F9239B163F2466518374FF65717F8A1)

## 安装和更新

### 一键安装

1. 在DevEco Studio左侧边栏点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/TmndDTHuTNOmWqExtvGVRg/zh-cn_image_0000002808766607.png?HW-CC-KV=V1&HW-CC-Date=20261128T023500Z&HW-CC-Expire=31536000000&HW-CC-Sign=7D72DFF9EF995809612867D65EE6D0D5A67C1230E6DFBA3BABB5A9228B4374EA)图标，打开DevEco Code**。**
2. 点击**Install Now**安装DevEco Code插件。若未登录请先点击**Sign in**，在华为账号登录页面完成登录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/SHpygYTTQgaXg7fmYjRraw/zh-cn_image_0000002821941261.png?HW-CC-KV=V1&HW-CC-Date=20261128T023500Z&HW-CC-Expire=31536000000&HW-CC-Sign=EAB7A1BAC8C87C474E58D36AC27D26CCE5EBD3CEE5EDEBCE320AE0B2ED10E5A0)
3. 点击**Installation complete.Restart IDE.**，重启DevEco Studio后开始使用。

**说明** 

* 若Windows/macOS版DevEco Studio的左侧边栏未出现![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/_YoJexziQ-66nltQNn1SAA/zh-cn_image_0000002793261316.png?HW-CC-KV=V1&HW-CC-Date=20261128T023500Z&HW-CC-Expire=31536000000&HW-CC-Sign=41676725F0AB748BD79F58F4F7FA06E1747FB2251FD8DE3559A5B99FFF3350EB)图标，需先点击弹窗中的**立即更新**，升级CodeGenie版本后，再安装DevEco Code插件。
* 鸿蒙电脑版DevEco Code插件安装后，无需重启DevEco Studio，即可开始使用。

### 本地安装

鸿蒙电脑版DevEco Code不支持该功能。

可通过[下载中心](https://developer.huawei.com/consumer/cn/download/deveco-code)获取最新的DevEco Code插件版本，并根据下载中心页面**工具完整性**指导进行完整性校验。插件安装包的存放路径不能包含中文字符。

DevEco Code插件版本需与DevEco Studio版本相匹配，具体对应关系如下：

* DevEco Studio 6.0.0、DevEco Studio 6.0.1、DevEco Studio 6.0.2、DevEco Studio 6.1.0、DevEco Studio 6.1.1支持安装DevEco Code Plugin 6.1.1 Release版本。
* DevEco Studio 26.0.0 Beta2及以上版本支持安装DevEco Code Plugin 26.0.1 Beta1及以上版本。

下载完成后，插件安装包无需解压，依照下方步骤进行安装：

1. 在DevEco Studio菜单栏，点击**File > Settings**（macOS为**DevEco Studio > Preferences****/****Settings**）**> Plugins**，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/sEjfi9wRRgS9zLpkJYtYCA/zh-cn_image_0000002779407052.png?HW-CC-KV=V1&HW-CC-Date=20261128T023500Z&HW-CC-Expire=31536000000&HW-CC-Sign=7C0AB2AC4CB9FD68AD29F29446AB0AFBB0429163AE7D4F6A95B5710CBEA70BD3) **> Install Plugin from Disk…**安装本地插件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/Le6FDdaaRbSowP45_3thvw/zh-cn_image_0000002779567022.png?HW-CC-KV=V1&HW-CC-Date=20261128T023500Z&HW-CC-Expire=31536000000&HW-CC-Sign=8F840259021789E7E253E69CE0E97AC51F580C8B84198EE5E3336F4FF9B4D5CA)
2. 在弹出的文件选择窗口中，选择**未解压的插件****包**的存放位置，点击**OK**确认安装插件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/Y1PILMISQLuBJ28izhpSBg/zh-cn_image_0000002808766597.png?HW-CC-KV=V1&HW-CC-Date=20261128T023500Z&HW-CC-Expire=31536000000&HW-CC-Sign=8FD814C2FD52C5C98675FB738DACC3530C80F4AFCBD615C5863BF8984F3FB529)
3. 在DevEco Studio左侧边栏点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/USzqZYa8RwuxyZ4RBlYOCQ/zh-cn_image_0000002808886693.png?HW-CC-KV=V1&HW-CC-Date=20261128T023500Z&HW-CC-Expire=31536000000&HW-CC-Sign=E72DADB5D16D8940C2EFE9E5220F91C16F27CB949DC442A944911F4B09BCB4FB)图标，登录后开始体验DevEco Code。

### 更新

鸿蒙电脑版DevEco Code不支持该功能。

进入**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> CodeGenie****> General**页面，勾选**Auto Update**，可以自动升级插件配置。

开启自动升级后，若管理台配置的插件可以静默升级，且系统检测到插件需要更新时，插件会自动升级；若管理台配置的插件不支持静默升级，会有弹框提示用户手动升级。未开启自动升级，也会有弹框提示用户手动升级。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/TCJT91kIQ0Kpj6Fp1pM2lw/zh-cn_image_0000002808766615.png?HW-CC-KV=V1&HW-CC-Date=20261128T023500Z&HW-CC-Expire=31536000000&HW-CC-Sign=1CAA189DA8CEB915267BD021110A38EBDA624C1E8724788794CCF7932C926D74)

## 会话管理

* **新建会话**：点击顶部**New Conversation**，即可创建新会话。
* **重命名会话**：在会话标题上右键，点击**Rename**，即可输入新的会话名称。
* **收藏****会话**：在会话标题上右键，点击**Favorite**，即可收藏或者取消收藏。
* **归档****会话**：在会话标题上右键 ，点击**Archive**，即可归档。鸿蒙电脑版DevEco Code不支持该功能。
* **删除****会话**：在会话标题上点删除图标（鸿蒙电脑版DevEco Code为在会话标题上右键点击**Delete**），即可以删除会话。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/VujQO7saTcaS3eGdgd1-OQ/zh-cn_image_0000002793101334.png?HW-CC-KV=V1&HW-CC-Date=20261128T023500Z&HW-CC-Expire=31536000000&HW-CC-Sign=DDC182FE9FCFFB3B07F3E793B16615925386B130DECB41F78C494DD1C0004CA1 "点击放大")

## 会话交互

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/4S-Y7SUySUa56ex7799BOQ/zh-cn_image_0000002783548358.png?HW-CC-KV=V1&HW-CC-Date=20261128T023500Z&HW-CC-Expire=31536000000&HW-CC-Sign=532561FE29029833FEAD2348C741EF9C2D6D11243E6E186FD15AED4E86566121 "点击放大")

* **发送消息**：在输入框需求描述，按**Enter**或点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/XA0IGCecSV214xUMdOB-zQ/zh-cn_image_0000002779407042.png?HW-CC-KV=V1&HW-CC-Date=20261128T023500Z&HW-CC-Expire=31536000000&HW-CC-Sign=31A1616EC00EFAEFE994DB005CCF591009238861C7CCA0C98AE1A3538FAF78E8)按钮发送后，等待回复。
* **停止生成**：内容生成过程中，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/PKKVq8SpQhSh4u2IBwmZpA/zh-cn_image_0000002808886695.png?HW-CC-KV=V1&HW-CC-Date=20261128T023500Z&HW-CC-Expire=31536000000&HW-CC-Sign=01B41898B9ED45A9FEF8CD3B816D1B78273C7D2FE2473930320359A6DBE191C5)按钮，即可停止生成。
* **查看历史输入对话**：输入框为空时，通过键盘上/下方向键可浏览已发送的会话，包括附件和文件引用。
* **添加上下文：**为会话添加上下文帮助工具更准确地理解开发者需求，可通过如下方式添加：

  + 方式一：在输入框中输入**@**符号，在弹出的项目文件搜索列表中选择所需文件，所选文件以标签形式显示在输入框上方（如@index.d.ts），问答时将自动读取所选文件内容。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/T-uxe5wqQI2PKPFSHwp6cw/zh-cn_image_0000002812947819.png?HW-CC-KV=V1&HW-CC-Date=20261128T023500Z&HW-CC-Expire=31536000000&HW-CC-Sign=91090C1E9D3871621B9084D3E361264D3F2D9AAD336F22F6C2E8875264838D8D)
  + 方式二：点击输入框中**＋**按钮，可以添加文件或图片（格式包括PNG、JPG、GIF、WEBP），问答时将自动读取附件内容。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/lByKxbTgRFemkgXHn9fjvg/zh-cn_image_0000002783708300.png?HW-CC-KV=V1&HW-CC-Date=20261128T023500Z&HW-CC-Expire=31536000000&HW-CC-Sign=6E1B1E92F6436A76A404866F325609FF11E9E64F9A4AEF8261EECC42389DD57A)
  + 方式三：在编辑器选中代码后右键，选择**DevEco Code > Quick Chat**（鸿蒙电脑版DevEco Code为**Add to** **DevEco Code**），问答时将自动定位和读取所选代码行。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/7z5YskXBR1SPu8ZcoZE_mw/zh-cn_image_0000002779407054.png?HW-CC-KV=V1&HW-CC-Date=20261128T023500Z&HW-CC-Expire=31536000000&HW-CC-Sign=1224E996F556339F9F8135872AD7B6F7BBF5382B56D5A3DF21E5E646626F7E8F "点击放大")

## 模型切换

点击底部输入框的模型名称下拉框，即可切换模型；在搜索框输入模型名称快速过滤模型；点击**Add model**配置更多模型，配置模型具体请参考[配置Models](ide-deveco-code-plugin-models.md)。鸿蒙电脑版DevEco Code不支持模型搜索功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/r8nDRHm3T8a6qvot6qYQ9A/zh-cn_image_0000002779567028.png?HW-CC-KV=V1&HW-CC-Date=20261128T023500Z&HW-CC-Expire=31536000000&HW-CC-Sign=CDF0DEB9CC3A589586AEDCB5FB1254C9C1F77940EAE0AE5777A07DB8D8037442)

## Agent模式切换

在底部输入框点击**Build**后的下拉框，可切换不同Agent模式。Agent模式介绍请参考[Agent模式](ide-deveco-code-agent.md)。

鸿蒙电脑版DevEco Code不支持Ask模式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/lql7kSQLSUOmv54_qNrd-Q/zh-cn_image_0000002812947047.png?HW-CC-KV=V1&HW-CC-Date=20261128T023500Z&HW-CC-Expire=31536000000&HW-CC-Sign=7C15AB5F300BB619F9F760B512581AFC1FA280029077BB8659B880A337256C96)

## 快捷命令

在底部输入框输入"**/**"，即可调用斜杠命令，通过键盘**上/下键**选择不同命令，点击**Enter**确认和点击**Esc**退出命令。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/cX09NjY4TlCLC6AbYEEmCg/zh-cn_image_0000002783548360.png?HW-CC-KV=V1&HW-CC-Date=20261128T023500Z&HW-CC-Expire=31536000000&HW-CC-Sign=4B711E22FB5406BF9449859A1CFDB33489F99F6EDB4ACECFB36E56CEA921D117)
