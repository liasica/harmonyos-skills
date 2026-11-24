---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-agent-use
title: 自定义智能体（Agent）配置和调用
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 自定义智能体配置 > 自定义智能体（Agent）配置和调用
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:39+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:22f0e0cb0fec507b1d00785777b22f30c5b733bcccabee88c089ac002b626992
---

从DevEco Studio 6.0.1 Beta1开始，CodeGenie支持用户添加模型和自定义Agent，增强AI问答能力，提升AI辅助编程和分析能力。

从DevEco Studio 6.0.2 Release（6.0.2.646）开始，支持智能体切换模型和配置三方模型。

## Agent配置

1. 可以通过如下两种方式进入Agent配置页面。
   * 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/dF7uDJqmRtqvrZH6nh_YBQ/zh-cn_image_0000002779407086.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=AC7A030151707ECD993160D7F4948DCA15624D22832A5277D2558A695EEABADF "点击放大")按钮或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/MQY1r6tTTwu6_fRxo0U6AQ/zh-cn_image_0000002779407082.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=C10E377ED2D20BED4E6933396D1A46F05673501D8E42F59C07EF09378A21E641)按钮，选择**Agent**。
   * 在输入框左下角下拉框选择**Create Agent**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/-RyBizqQRAqARJdsyNjl_Q/zh-cn_image_0000002779567068.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=EDD6F71D9FEA50A0608BA09B23AEC64D58F35486EAA053072A73592D862E146C "点击放大")
2. 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/bYiw7MSAQUuOc5oYagfQdA/zh-cn_image_0000002779407088.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=5E88EE54B45C78C65293FEC80EBD96AD51383453A59F73C7CB50E00945149F6C "点击放大")按钮，填写自定义Agent的相关信息。点击**Add**，将创建自定义Agent。
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/ICoXnB4yTOCOjbIfjvoUCA/zh-cn_image_0000002779407090.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=2953100C7084DCC5F9EF0F8FE3D430459423364C2AAFA66DE1AC584799FE0F26 "点击放大")
3. 在**All Agents**下展示所有智能体。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/-W-_kEQfTnS9c1ipWB0wNA/zh-cn_image_0000002779567064.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=CA0B1046B923D53B845ACBE2FD50BFF5AE0B31D869BCD1F3681ACB8CEFD36B11)
4. 设置自动执行开关和白名单列表。
   * **Auto Run**：DevEco Studio 6.0.2 Beta1新增，内置工具（命令行工具除外）和MCP工具被调用过程中，自动执行的开启开关。开启时，工具被调用可自动执行和输出内容；关闭时，工具被调用需开发者授权。默认关闭。
   * **AllowList**：DevEco Studio 6.0.2 Beta1新增，白名单列表，开启Auto Run后，白名单中的命令同样会自动执行。点击**Enter Command**中输入命令，点击**Add**可将命令添加至白名单列表；点击命令后×，可将命令从白名单列表中删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/hdT1Llj9QjCZjS7GCbekdQ/zh-cn_image_0000002808766639.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=77CE6ECE0B018E852181E23F176294C06CFC1E6F104306FF42391E2C90E6DE9C "点击放大")
5. 选择自定义智能体后，开发者可以切换模型，包括内置模型/默认模型（deepseek-v4-flash、glm-5.2）和三方模型（如deepseek-v4-pro）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/riI4gczkSg2PIeVtpz2zTQ/zh-cn_image_0000002779567062.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=07032603C79D5C5AED3AC2FB9C72A85E5396F1EC3BE44D6C121A3167014DA849)
6. 点击置灰的三方模型会跳转到Service Provider配置界面（如**deepseek-chat**），填写**API Key**字段即可添加模型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/26Uh7q0sTK2conZD0WRWzw/zh-cn_image_0000002779567060.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=BA77E01B1DD88FF33CA7E70F8BA389DBB9EF5BD1AC22CFA473FC78B58EB94F21 "点击放大")

## Agent调用

1. Agent配置完成后，可以通过如下两种方式开启调用：
   * 在对话区域输入"/"调出命令，选择自定义的Agent（如**figma2code**）。从DevEco Studio 6.1.0 Beta2开始不支持。
   * 在输入框左下角HarmonyOS Ask处下拉框中选择自定义的Agent（如**figma2code**）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/7PFs4wGyTWOz3l-fWirADg/zh-cn_image_0000002779407084.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=0D9DFF247A1EA1492E0A0F276E3F740A72AB411EF171CEFAB8984623D17A40B3)
2. 选择自定义Agent后，在右侧可以切换模型，默认使用配置Agent时添加的模型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/at6asgU8S7ebtN985hqAdw/zh-cn_image_0000002779567066.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=E99442035C7B100F06BE68E126F4467A1BFB78A7C9533805DC50256D37124C66)
3. 根据业务需要，进行智能问答、代码生成、代码智能解读等，CodeGenie将会调用自定义Agent和选择的模型生成内容。
