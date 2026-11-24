---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ocal-knowledge
title: 本地知识库配置
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 本地知识库配置
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:39+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:5dcc682280a9db68e80c1aa1dc3de312c65c2a8df1686735c8471301b205b1d0
---

从DevEco Studio 6.0.0 Beta5开始，CodeGenie允许用户导入设计文档和代码等文件形成文档集，多个文档集组合成本地知识库。智能问答时，根据用户输入内容检索本地知识库以提升AI生成的能力。

## 操作步骤

1. 点击**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> CodeGenie****> Knowledge >** **Docs**，或在DevEco Studio右侧边栏点击**CodeGenie**（或输入快捷键**Alt/Option+U**） **>** **@****Add Context** **> Docs > Set Local Knowledge Base**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/iP7LZLqlTeCEkUSNawE-4A/zh-cn_image_0000002779407332.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=6222F2C28FF8C671C7F50C31FFC71DF5638A75410FCF40B710AB849A7F85C200)
2. 首次打开时，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/ndlkWOGrRmS9BDBQ8GTpCw/zh-cn_image_0000002808886971.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=F7FF1FDFFE0F872E74BEE9C6243CB923DFD3C84940148F84A60B084EC8268AE3 "点击放大")按钮，填写相关信息，创建文档集。
   * **Knowledge Base Path**：知识库保存路径。在同一个路径下保存的文档集，会形成一个知识库。
   * **Document set name**：文档集名称。
   * **Description**：可选，文档集描述。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/gz0LZzJMTDinRdNq_qZtZw/zh-cn_image_0000002779407334.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=FFCEE1F4F9510196D0E1DD131F583FA174AB2DDDDD6B1CC856C325AE5314A7B4)
3. 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/t_sSI2LOS1ydfa9nEtUicQ/zh-cn_image_0000002779567314.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=8EAD11607C0F99DA0D0A3E67C98DCF0B97EC8E1C4701B0A8173679AEF1EE482D "点击放大")按钮，添加文档集中的文件，添加成功的文件在下方展示。

   **说明** 

   1. 支持的文件格式：txt、md、json、html、cpp、ets、ts、js。
   2. 单个文档集中文件个数：不超过1000个。
   3. 单个文件大小：不超过10M。
   4. 单个知识库中文档集个数：不超过20个。
   5. 单个知识库大小：不超过50M。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/HjWocUw3SwKZxxTpqQR2Fw/zh-cn_image_0000002808766895.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=5CAF12178354EE10817EC615FB9C6A6AA286F8F1D040B30A91B6083E5E61D7AE)
4. 点击“**OK**”，完成本地知识库配置和同步，在DevEco Studio页面下方**Storing document set**可查看同步进度。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/GF2KW3A9SyO40YgdBNjZVw/zh-cn_image_0000002779567312.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=9565C41442FCD18DF146AF15A8B3B6FD4397155E47A7E57F55D1B2F4EF1E56BC "点击放大")
5. 同步完成后，在对话框中输入**@**符号选择**Docs** ，或点击上方**@****Add Context** **> Docs** ，选择需要的文档集。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/sYPSB_PMSvq0DXLTTUKdzQ/zh-cn_image_0000002808886975.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=4B59C5C93F153086A96C51E39CF321DB2F4AEB3AC3E5AEACF86A0BC5E1A8B13D)
6. 选择代码文件进行问答，具体请参考[智能问答](ide-harmonyos-ask.md)。
