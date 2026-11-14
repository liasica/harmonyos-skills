---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ocal-knowledge
title: 本地知识库配置
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 本地知识库配置
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:09+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:76d5f3346f21705137ff502145a9791679dc9d84b5fb8f89d3b0fe47d6a19ddd
---

从DevEco Studio 6.0.0 Beta5开始，CodeGenie允许用户导入设计文档和代码等文件形成文档集，多个文档集组合成本地知识库。智能问答时，根据用户输入内容检索本地知识库以提升AI生成的能力。

## 操作步骤

1. 点击**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> CodeGenie****> Knowledge >** **Docs**，或在DevEco Studio右侧边栏点击**CodeGenie**（或输入快捷键**Alt/Option+U**） **>** **@****Add Context** **> Docs > Set Local Knowledge Base**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/rDrjBuHrQZqr9LsHHUyc-w/zh-cn_image_0000002779407332.png?HW-CC-KV=V1&HW-CC-Date=20261114T004909Z&HW-CC-Expire=31536000000&HW-CC-Sign=2265083D9CE8844AF63A6B4358010919A9766B9BA0A0EDD0D0383C4C73BB58FF)
2. 首次打开时，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/erfvIMOsR8KEvSD1bOqiNQ/zh-cn_image_0000002808886971.png?HW-CC-KV=V1&HW-CC-Date=20261114T004909Z&HW-CC-Expire=31536000000&HW-CC-Sign=8308DB850DDBC9F1ED8E7A5E6238C431C90F85368B8C67C8C87FB963BE452DAA "点击放大")按钮，填写相关信息，创建文档集。
   * **Knowledge Base Path**：知识库保存路径。在同一个路径下保存的文档集，会形成一个知识库。
   * **Document set name**：文档集名称。
   * **Description**：可选，文档集描述。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/W7DBkoc9TcOYHPK_AI6ESg/zh-cn_image_0000002779407334.png?HW-CC-KV=V1&HW-CC-Date=20261114T004909Z&HW-CC-Expire=31536000000&HW-CC-Sign=2B615186E8963A77934439C216CDB8D1345B0AD792E78313250758DC00427544)
3. 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/12nruJL_Qai1QDsIQ2Vueg/zh-cn_image_0000002779567314.png?HW-CC-KV=V1&HW-CC-Date=20261114T004909Z&HW-CC-Expire=31536000000&HW-CC-Sign=57373F362ED239570F9B5845CDF12DDCB222EE5082EB77E5A4F3CBE9B1AA2441 "点击放大")按钮，添加文档集中的文件，添加成功的文件在下方展示。

   **说明** 

   1. 支持的文件格式：txt、md、json、html、cpp、ets、ts、js。
   2. 单个文档集中文件个数：不超过1000个。
   3. 单个文件大小：不超过10M。
   4. 单个知识库中文档集个数：不超过20个。
   5. 单个知识库大小：不超过50M。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/5qFAJhtsSr2eARc886f5aQ/zh-cn_image_0000002808766895.png?HW-CC-KV=V1&HW-CC-Date=20261114T004909Z&HW-CC-Expire=31536000000&HW-CC-Sign=9B6B0E5FB05307F4F5DFD3DD8A1E8512F679BB3245B8DA7329898ED0F0E6C6CF)
4. 点击“**OK**”，完成本地知识库配置和同步，在DevEco Studio页面下方**Storing document set**可查看同步进度。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/hDyWoXTkQ5qXklDGGtD8BQ/zh-cn_image_0000002779567312.png?HW-CC-KV=V1&HW-CC-Date=20261114T004909Z&HW-CC-Expire=31536000000&HW-CC-Sign=268CA89834A36102B87757CF09723BF7E8AF262987828E543F9FA3F077CEFDA9 "点击放大")
5. 同步完成后，在对话框中输入**@**符号选择**Docs** ，或点击上方**@****Add Context** **> Docs** ，选择需要的文档集。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/HjjaG8csSqC2eJSh7LgRKQ/zh-cn_image_0000002808886975.png?HW-CC-KV=V1&HW-CC-Date=20261114T004909Z&HW-CC-Expire=31536000000&HW-CC-Sign=48FDBCA08771106A2728693ED24EE63F5BB6453CCF8D654A356056B72A79448C)
6. 选择代码文件进行问答，具体请参考[智能问答](ide-harmonyos-ask.md)。
