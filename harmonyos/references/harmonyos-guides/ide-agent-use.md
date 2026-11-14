---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-agent-use
title: 自定义智能体（Agent）配置和调用
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 自定义智能体配置 > 自定义智能体（Agent）配置和调用
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:09+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:ad5e25fe8b7024382f69477024a36bf863068a39deac2794dd2142011aa73fb1
---

从DevEco Studio 6.0.1 Beta1开始，CodeGenie支持用户添加模型和自定义Agent，增强AI问答能力，提升AI辅助编程和分析能力。

从DevEco Studio 6.0.2 Release（6.0.2.646）开始，支持智能体切换模型和配置三方模型。

## Agent配置

1. 可以通过如下两种方式进入Agent配置页面。
   * 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/5Qe_Gz_vSsqkEzQky8niUQ/zh-cn_image_0000002779407086.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=4665C7A9134F341296D38E941A1C5DD03BCA85DFC32C1E5D780F7E9203D5B324 "点击放大")按钮或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/wEHrMYSXQXihLadBmj4j5w/zh-cn_image_0000002779407082.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=5C7C343E6F2B41CC3D056E82EA7B7C20AE8C0DC2AA0483B38366D236E7CB18D9)按钮，选择**Agent**。
   * 在输入框左下角下拉框选择**Create Agent**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/aw1SU0AoTpup8Q7hh6ihPg/zh-cn_image_0000002779567068.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=999DB6DEF97A5B8BC2A953E4C1D368B5F0F747929CC5B8CFD5E595CE79827944 "点击放大")
2. 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/i37gahZ_TWGE-uT_HCxrTA/zh-cn_image_0000002779407088.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=41DB169653C9BA7C94908C792525821FE2FA4DD03647E8DB6E081D5E5547B4F2 "点击放大")按钮，填写自定义Agent的相关信息。点击**Add**，将创建自定义Agent。
   * **Name**：必填，自定义Agent的名称。
   * **Prompt Description**：可选，自定义Agent的提示词。
   * **MCP Tools**：可选，添加MCP工具，具体请参考[MCP配置](ide-agent-mcp.md)。
   * **Built-in Tools**：可选，内置工具，包含File Manager、Terminal、Compile and Build、Web Rag、To Do、Skill、UI Verification，默认开启。

     | 工具名称 | 说明 |
     | --- | --- |
     | File Manager | DevEco Studio 6.0.2 Beta1新增。开启后，支持读写本地的代码文件。 |
     | Terminal | DevEco Studio 6.0.2 Beta1新增。开启后，在CodeGenie对话框执行命令时可自动拉起Terminal终端。 |
     | Compile and Build | DevEco Studio 6.0.2 Beta1新增。开启后，支持编译与构建项目。 |
     | Web Rag | DevEco Studio 6.1.0 Beta2新增。开启后，支持在问答过程中检索鸿蒙相关的资料，提升答复准确性。 |
     | To Do | DevEco Studio 6.0.2 Release（6.0.2.646）新增。开启后，支持把一个复杂任务拆解成多步执行，帮助CodeGenie聚焦任务，避免遗忘任务，提升答复准确性。 |
     | Skill | DevEco Studio 6.1.0 Release（6.1.0.830）新增。开启后，支持在自定义智能体中使用配置的Skill。 |
     | UI Verification | 26.0.0 Beta1新增。开启后，支持通过自然语言描述测试步骤，自动在HarmonyOS设备上执行UI操作并验证结果。  从26.0.0 Beta2版本开始，支持折叠、展开特性，适用于双折叠/阔折叠/三折叠的模拟器；以及支持动态效果分析（如视频是否正常播放、是否出现弹窗）。 |
   * **Select Model**：必填，选择需要使用的模型，具体请参考[模型（Model）配置](ide-agent-model.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/v5ut7fidRFyoq7vtODHItw/zh-cn_image_0000002779407090.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=08CE07DBAA7C0C06216614ACE714D7FC2A73040916CC8B9799AB015A29BA0A9A "点击放大")
3. 在**All Agents**下展示所有智能体。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/G_BCUUCwTP2UitXWqNcFvQ/zh-cn_image_0000002779567064.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=582E16C9A53C40478D47573170A7F1D6F18ED5D488BF0DBE432065C726EA77F4)
4. 设置自动执行开关和白名单列表。
   * **Auto Run**：DevEco Studio 6.0.2 Beta1新增，内置工具（命令行工具除外）和MCP工具被调用过程中，自动执行的开启开关。开启时，工具被调用可自动执行和输出内容；关闭时，工具被调用需开发者授权。默认关闭。
   * **AllowList**：DevEco Studio 6.0.2 Beta1新增，白名单列表，开启Auto Run后，白名单中的命令同样会自动执行。点击**Enter Command**中输入命令，点击**Add**可将命令添加至白名单列表；点击命令后×，可将命令从白名单列表中删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/PYvZTfXWQsC-AvkMv_Kxzg/zh-cn_image_0000002808766639.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=203B3546340474AC76F538D211CE45BA91D586BD475A4AA7022D0D48667CC915 "点击放大")
5. 选择自定义智能体后，开发者可以切换模型，包括内置模型/默认模型（deepseek-v4-flash、glm-5.2）和三方模型（如deepseek-v4-pro）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/iZPx2iVhS2S8UqVaYz4KKw/zh-cn_image_0000002779567062.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=5A9FE5B1AC1C1150BA8EA0026A0A28825E9E7F388D5304771C902BCCE14601B6)
6. 点击置灰的三方模型会跳转到Service Provider配置界面（如**deepseek-chat**），填写**API Key**字段即可添加模型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/CCGQrs-ARde35EVlOxMeqw/zh-cn_image_0000002779567060.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=A161E7C1EAB3CED37A0E9645FAF2B00B37CA9C8F673D32A33DFFF0F7B9534A2B "点击放大")

## Agent调用

1. Agent配置完成后，可以通过如下两种方式开启调用：
   * 在对话区域输入"/"调出命令，选择自定义的Agent（如**figma2code**）。从DevEco Studio 6.1.0 Beta2开始不支持。
   * 在输入框左下角HarmonyOS Ask处下拉框中选择自定义的Agent（如**figma2code**）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/H4XdkHa2S-WhT5AOHEMkHw/zh-cn_image_0000002779407084.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=28B4BF8E54E8CBC9A8BB4C4622C2C44E5859224A070889F9FCA7DD5C9F004FA7)
2. 选择自定义Agent后，在右侧可以切换模型，默认使用配置Agent时添加的模型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/bO_JDYdqRI2dcACcUZvvYQ/zh-cn_image_0000002779567066.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=4967EBE3BA7C320ECD03BF97FFCD58E34425AA5CD30300136E34A30127C0F2FC)
3. 根据业务需要，进行智能问答、代码生成、代码智能解读等，CodeGenie将会调用自定义Agent和选择的模型生成内容。
