---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-agent-use
title: 自定义智能体（Agent）配置和调用
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 自定义智能体配置 > 自定义智能体（Agent）配置和调用
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:f2ef7d9eaa56d3361f04b89369a60675baab6256fdf977c0f9d0e5a7a6a64290
---

从DevEco Studio 6.0.1 Beta1开始，CodeGenie支持用户添加模型和自定义Agent，增强AI问答能力，提升AI辅助编程和分析能力。

从DevEco Studio 6.0.2 Release（6.0.2.646）开始，支持智能体切换模型和配置三方模型。

## Agent配置

1. 可以通过如下两种方式进入Agent配置页面。
   * 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/iFAJ22L5QqeKUEZTALst5Q/zh-cn_image_0000002779407086.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=E15997888C1219F4B7BD57561C45C8E529E265B62081BAE3DA168F74EA6E113E "点击放大")按钮或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/KRC1uPO0R_GYevnTokM0KQ/zh-cn_image_0000002779407082.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=8A9568443F7E5BFAC0C5B98874DCE9C5B7E4067E66D92055790E37C0F766515D)按钮，选择**Agent**。
   * 在输入框左下角下拉框选择**Create Agent**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/NZcsJlbZR1WEjA1iVstMZQ/zh-cn_image_0000002779567068.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=027C71DF730C69AC8272D9F822B4A93734C1F6BEEF239BA6AE083ED15BB87DB3 "点击放大")
2. 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/_bjNfAOCTVO70TzZTAjBJQ/zh-cn_image_0000002779407088.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=4D30FBE730989AA25CA6C7C6FDF556C622F7A0729AF67A1C46B91EA5329CE9AA "点击放大")按钮，填写自定义Agent的相关信息。点击**Add**，将创建自定义Agent。
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/rbGE85K6Rce0-s0t3-_5cg/zh-cn_image_0000002779407090.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=6BAEE8A5F78B3E25ABC1749548EBB00E9B2BB97B9809E5240E5A4E28E9574A56 "点击放大")
3. 在**All Agents**下展示所有智能体。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/uAEzePG0QzePBXLK61IwDw/zh-cn_image_0000002779567064.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=FC15369CADD757F2FE57E0386FB15BB42542D4A916396C0D0BD99E14AA54466E)
4. 设置自动执行开关和白名单列表。
   * **Auto Run**：DevEco Studio 6.0.2 Beta1新增，内置工具（命令行工具除外）和MCP工具被调用过程中，自动执行的开启开关。开启时，工具被调用可自动执行和输出内容；关闭时，工具被调用需开发者授权。默认关闭。
   * **AllowList**：DevEco Studio 6.0.2 Beta1新增，白名单列表，开启Auto Run后，白名单中的命令同样会自动执行。点击**Enter Command**中输入命令，点击**Add**可将命令添加至白名单列表；点击命令后×，可将命令从白名单列表中删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/QIbvNeJvSGaD0lxWey0Qjg/zh-cn_image_0000002808766639.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=00C7F9CCCD506C461B8D6D01DF3F548B73393B890B362D682D0EFF430C70EEE4 "点击放大")
5. 选择自定义智能体后，开发者可以切换模型，包括内置模型/默认模型（deepseek-v4-flash、glm-5.2）和三方模型（如deepseek-v4-pro）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/xRxOEyrHS5-1jAgEoUxq4Q/zh-cn_image_0000002779567062.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=24AD8F60A5BA77734084D6D4A1DC75DB2D9D98C88493290F6EDF9B527D0B4431)
6. 点击置灰的三方模型会跳转到Service Provider配置界面（如**deepseek-chat**），填写**API Key**字段即可添加模型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/_DXobflhQsq--TL3JR0dOQ/zh-cn_image_0000002779567060.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=A68E2A439C4432B9A3C62025270C3C291D310A9E5E73250D9E0346D79BCF141D "点击放大")

## Agent调用

1. Agent配置完成后，可以通过如下两种方式开启调用：
   * 在对话区域输入"/"调出命令，选择自定义的Agent（如**figma2code**）。从DevEco Studio 6.1.0 Beta2开始不支持。
   * 在输入框左下角HarmonyOS Ask处下拉框中选择自定义的Agent（如**figma2code**）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/u0me453xT46fOPgXHRNUiQ/zh-cn_image_0000002779407084.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=8C638D768D2AAFB844BFD23D56F92C33616EC9D36859453960C7AE742B0ACB7A)
2. 选择自定义Agent后，在右侧可以切换模型，默认使用配置Agent时添加的模型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/AEAvT451Qk68BbPzwsr--g/zh-cn_image_0000002779567066.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=C3B043AAA68DECBA536AFD9CF5F71926916D1C4F04EE6646B1411B4EECF2DB78)
3. 根据业务需要，进行智能问答、代码生成、代码智能解读等，CodeGenie将会调用自定义Agent和选择的模型生成内容。
