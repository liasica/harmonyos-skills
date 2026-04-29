---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ocal-knowledge
title: 本地知识库配置
breadcrumb: 指南 > 使用AI智能辅助编程 > 本地知识库配置
category: harmonyos-guides
scraped_at: 2026-04-29T13:45:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:14cd04ed409031d3e0a9dd3270e67fffd36d01cb696a8b3f9057fe211423df29
---

从DevEco Studio 6.0.0 Beta5开始，CodeGenie允许用户导入设计文档和代码等文件形成文档集，多个文档集组合成本地知识库。智能问答时，根据用户输入内容检索本地知识库以提升AI生成的能力。

1. 点击**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> CodeGenie****> Knowledge >** **Docs**，或在DevEco Studio右侧边栏点击**CodeGenie**（或输入快捷键**Alt/Option+U**） **>** **@****Add Context** **> Docs > Set Local Knowledge Base**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/o_F_GR8MSZa0yz_1wzA7QQ/zh-cn_image_0000002561833287.png?HW-CC-KV=V1&HW-CC-Date=20260429T054514Z&HW-CC-Expire=86400&HW-CC-Sign=7979C104A628300F1E8348BC24B3EDB8F4352723D2BFCBD38EC60EEBA0754727)
2. 首次打开时，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/zDgJmQBbSAezdADXfPVPaA/zh-cn_image_0000002530913360.png?HW-CC-KV=V1&HW-CC-Date=20260429T054514Z&HW-CC-Expire=86400&HW-CC-Sign=0266B75980B25C66B37C3F19238A28B8656BF5FE4F7207B81524B809E710320A)按钮，填写相关信息，创建文档集。
   * **Knowledge Base Path**：知识库保存路径。在同一个路径下保存的文档集，会形成一个知识库。
   * **Document set name**：文档集名称。
   * **Description**：可选，文档集描述。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/31GP-MuxQ1y3YUVLw9nfew/zh-cn_image_0000002561833291.png?HW-CC-KV=V1&HW-CC-Date=20260429T054514Z&HW-CC-Expire=86400&HW-CC-Sign=ACFEF327D73FC3D5FFA9211577AED3D2B9A31179DF71069F33F73317271BA434)
3. 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/ADhZ1tcYTQW4ZjeiGtL-HQ/zh-cn_image_0000002561753303.png?HW-CC-KV=V1&HW-CC-Date=20260429T054514Z&HW-CC-Expire=86400&HW-CC-Sign=49F9BC35FF9F90C6F79962FB6AB335FC4C5A65A465794B561DC1F053A11BCF14)按钮，添加文档集中的文件，添加成功的文件在下方展示。

   说明

   1. 支持的文件格式：txt、md、json、html、cpp、ets、ts、js。
   2. 单个文档集中文件个数：不超过1000个。
   3. 单个文件大小：不超过10M。
   4. 单个知识库中文档集个数：不超过20个。
   5. 单个知识库大小：不超过50M。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/FKldF5KrSRGpm0gokim4zA/zh-cn_image_0000002530913362.png?HW-CC-KV=V1&HW-CC-Date=20260429T054514Z&HW-CC-Expire=86400&HW-CC-Sign=CDFD332182ED71B3FA0452AF07568ADB6BC31E74296F5C3C0B30C02F16837BE8)
4. 点击“**OK**”，完成本地知识库配置和同步，在DevEco Studio页面下方**Storing document set**可查看同步进度。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/tQMGMjh_SQen3cV2dAn7Kw/zh-cn_image_0000002561753309.png?HW-CC-KV=V1&HW-CC-Date=20260429T054514Z&HW-CC-Expire=86400&HW-CC-Sign=4BF390C5B616E91822A10B3632555FC86A9EB4F8D32C6CE2CD86B446E86A63B9 "点击放大")
5. 同步完成后，在对话框中输入**@**符号选择**Docs** ，或点击上方**@****Add Context** **> Docs** ，选择需要的文档集。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/RJ6XaMyBQVCxFDuWOUshZg/zh-cn_image_0000002561833283.png?HW-CC-KV=V1&HW-CC-Date=20260429T054514Z&HW-CC-Expire=86400&HW-CC-Sign=A52F15FA40BA85023422CB6DA2159FDA6DAD1D2CBDEA2907DEBC7CDFDDB9993B)
6. 选择代码文件进行问答，具体请参考[智能问答](ide-harmonyos-ask.md)
