---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ocal-knowledge
title: 本地知识库配置
breadcrumb: 指南 > 使用AI智能辅助编程 > 本地知识库配置
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:529e001553fe01da73abe12a2e57e07f77ccd3bf8025fe4cbf5c2c2f10b59328
---

从DevEco Studio 6.0.0 Beta5开始，CodeGenie允许用户导入设计文档和代码等文件形成文档集，多个文档集组合成本地知识库。智能问答时，根据用户输入内容检索本地知识库以提升AI生成的能力。

1. 点击**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> CodeGenie****> Knowledge >** **Docs**，或在DevEco Studio右侧边栏点击**CodeGenie**（或输入快捷键**Alt/Option+U**） **>** **@****Add Context** **> Docs > Set Local Knowledge Base**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/D4DvGiuKTaK1Vb4FE4UH7Q/zh-cn_image_0000002561833287.png?HW-CC-KV=V1&HW-CC-Date=20260427T235518Z&HW-CC-Expire=86400&HW-CC-Sign=2DD3F516B6997D78E111D7AD508D3B0A6654F35EFB33A15854E6BDB425CC77A0)
2. 首次打开时，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/0fW_Q3e9RUWc6IfOfzKIQQ/zh-cn_image_0000002530913360.png?HW-CC-KV=V1&HW-CC-Date=20260427T235518Z&HW-CC-Expire=86400&HW-CC-Sign=6100B4F2721A1C9984008072917B7EAA1F09FAC3A83C91D686E61B7A5D97AF9A)按钮，填写相关信息，创建文档集。
   * **Knowledge Base Path**：知识库保存路径。在同一个路径下保存的文档集，会形成一个知识库。
   * **Document set name**：文档集名称。
   * **Description**：可选，文档集描述。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/a3ss3JTtTzu4r07QgBlFzw/zh-cn_image_0000002561833291.png?HW-CC-KV=V1&HW-CC-Date=20260427T235518Z&HW-CC-Expire=86400&HW-CC-Sign=CDC40389DC011B36D74867865DAD60EC54CC469AD9D0CE37D4DE41BDAFCFF680)
3. 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/rn_8La8ATpiFp04n_9cjzQ/zh-cn_image_0000002561753303.png?HW-CC-KV=V1&HW-CC-Date=20260427T235518Z&HW-CC-Expire=86400&HW-CC-Sign=7C1875BEF06772FE95FBE661E141EDBF9095DA508E04F3C91BBB3F4DCB39CCEC)按钮，添加文档集中的文件，添加成功的文件在下方展示。

   说明

   1. 支持的文件格式：txt、md、json、html、cpp、ets、ts、js。
   2. 单个文档集中文件个数：不超过1000个。
   3. 单个文件大小：不超过10M。
   4. 单个知识库中文档集个数：不超过20个。
   5. 单个知识库大小：不超过50M。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/CLYCzKAXTdezJLefGB6nlg/zh-cn_image_0000002530913362.png?HW-CC-KV=V1&HW-CC-Date=20260427T235518Z&HW-CC-Expire=86400&HW-CC-Sign=FBBCAE5CCA3344276F167A655A8B388452E529881023A99056AD9AA0E9310879)
4. 点击“**OK**”，完成本地知识库配置和同步，在DevEco Studio页面下方**Storing document set**可查看同步进度。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/TvnYbxHnRnajn4FwinZ-HA/zh-cn_image_0000002561753309.png?HW-CC-KV=V1&HW-CC-Date=20260427T235518Z&HW-CC-Expire=86400&HW-CC-Sign=AE49EABDFD07BE54F908CFFDAC1C5FC955EECA6B76C8B8F945A63CD4B4086157 "点击放大")
5. 同步完成后，在对话框中输入**@**符号选择**Docs** ，或点击上方**@****Add Context** **> Docs** ，选择需要的文档集。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/p_-vnfyJSO-2t700H1fdMA/zh-cn_image_0000002561833283.png?HW-CC-KV=V1&HW-CC-Date=20260427T235518Z&HW-CC-Expire=86400&HW-CC-Sign=6EA19787DD71F3AAFE02965D00786F59E143BFBD3459237BFD21A11CAAF9BFC0)
6. 选择代码文件进行问答，具体请参考[智能问答](ide-harmonyos-ask.md)
