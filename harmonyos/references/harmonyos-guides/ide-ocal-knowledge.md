---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ocal-knowledge
title: 本地知识库配置
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 本地知识库配置
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:48+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:89f159a9a8ef956fa12379531e036e5ca2b1c47fb7583d30b1d469aa28d3c47b
---

从DevEco Studio 6.0.0 Beta5开始，CodeGenie允许用户导入设计文档和代码等文件形成文档集，多个文档集组合成本地知识库。智能问答时，根据用户输入内容检索本地知识库以提升AI生成的能力。

## 操作步骤

1. 点击**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> CodeGenie****> Knowledge >** **Docs**，或在DevEco Studio右侧边栏点击**CodeGenie**（或输入快捷键**Alt/Option+U**） **>** **@****Add Context** **> Docs > Set Local Knowledge Base**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/8Bi8uq5UTJySbAW5eR0WWQ/zh-cn_image_0000002779407332.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=C8FDC5A97E74C663976A126C7E5B9106F383983A6C90F3441892E46C3E62DFD1)
2. 首次打开时，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/_08Pr2dIQ_6rwVRco5PYcw/zh-cn_image_0000002808886971.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=8E272D6C83C3BCABDE0066B39E3C14A9579FE3C88648E6D8BFFD391E9FD903A8 "点击放大")按钮，填写相关信息，创建文档集。
   * **Knowledge Base Path**：知识库保存路径。在同一个路径下保存的文档集，会形成一个知识库。
   * **Document set name**：文档集名称。
   * **Description**：可选，文档集描述。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/56i1c932Qi6d6EmmM_AXxg/zh-cn_image_0000002779407334.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=B7C716DC487B9D4E631EFC47ED71E40E480A827D7EDB74C8FB0B7D1816760EE4)
3. 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/rxfXvXD5SiqM_DwSMF-Uvw/zh-cn_image_0000002779567314.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=4B45FCDBAE98A38B22E2EB678E0AD348F94F2475975FD0730FC7F4623A1FD5A7 "点击放大")按钮，添加文档集中的文件，添加成功的文件在下方展示。

   **说明** 

   1. 支持的文件格式：txt、md、json、html、cpp、ets、ts、js。
   2. 单个文档集中文件个数：不超过1000个。
   3. 单个文件大小：不超过10M。
   4. 单个知识库中文档集个数：不超过20个。
   5. 单个知识库大小：不超过50M。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/45EjaeEzSd6ujR9fHK568w/zh-cn_image_0000002808766895.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=980F8D40D5BB04347356D762FD51A8AE3B9AD0BFC161ADDD910F1B98ED704A0E)
4. 点击“**OK**”，完成本地知识库配置和同步，在DevEco Studio页面下方**Storing document set**可查看同步进度。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/q0vYW35MS2KTcZ2Ra6SKyA/zh-cn_image_0000002779567312.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=C2AE2760BB5DEC8136F80E25D733EBC3F0AEA71A64C0D2130B4251CDEF2B1465 "点击放大")
5. 同步完成后，在对话框中输入**@**符号选择**Docs** ，或点击上方**@****Add Context** **> Docs** ，选择需要的文档集。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/OjhmdteLRTG2tM3dcDvcxA/zh-cn_image_0000002808886975.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=B4AF64D4B22A918340808E830D0D8D69C6C556B68EE9B5B01D007048CE82710B)
6. 选择代码文件进行问答，具体请参考[智能问答](ide-harmonyos-ask.md)。
