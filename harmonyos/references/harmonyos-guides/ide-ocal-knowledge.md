---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ocal-knowledge
title: 本地知识库配置
breadcrumb: 指南 > 使用AI智能辅助编程（不推荐） > 本地知识库配置
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:28+08:00
doc_updated_at: 2026-06-30
content_hash: sha256:4d62edcbd88b28a945a15e8bdd2a565f6b5c8c4800e4cbdb35a53549b5810095
---

从DevEco Studio 6.0.0 Beta5开始，CodeGenie允许用户导入设计文档和代码等文件形成文档集，多个文档集组合成本地知识库。智能问答时，根据用户输入内容检索本地知识库以提升AI生成的能力。

## 操作步骤

1. 点击**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> CodeGenie****> Knowledge >** **Docs**，或在DevEco Studio右侧边栏点击**CodeGenie**（或输入快捷键**Alt/Option+U**） **>** **@****Add Context** **> Docs > Set Local Knowledge Base**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/ZCXJ270ESGO1IaM8wZv7yQ/zh-cn_image_0000002731542537.png)
2. 首次打开时，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/IWZJxswAQyq7Ba1n29TAAA/zh-cn_image_0000002731542533.png "点击放大")按钮，填写相关信息，创建文档集。
   * **Knowledge Base Path**：知识库保存路径。在同一个路径下保存的文档集，会形成一个知识库。
   * **Document set name**：文档集名称。
   * **Description**：可选，文档集描述。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/ljE7cgAYREqj_C6lCDh66g/zh-cn_image_0000002731542541.png)
3. 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/rG5f1cYgSYmTrNwa8E0tEQ/zh-cn_image_0000002731542545.png "点击放大")按钮，添加文档集中的文件，添加成功的文件在下方展示。

   **说明** 

   1. 支持的文件格式：txt、md、json、html、cpp、ets、ts、js。
   2. 单个文档集中文件个数：不超过1000个。
   3. 单个文件大小：不超过10M。
   4. 单个知识库中文档集个数：不超过20个。
   5. 单个知识库大小：不超过50M。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/pgdb57fsTh6fu5DU9c5kUQ/zh-cn_image_0000002731542547.png)
4. 点击“**OK**”，完成本地知识库配置和同步，在DevEco Studio页面下方**Storing document set**可查看同步进度。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/DczkmsZ-QZSxyRjUFjhcIw/zh-cn_image_0000002701663346.png "点击放大")
5. 同步完成后，在对话框中输入**@**符号选择**Docs** ，或点击上方**@****Add Context** **> Docs** ，选择需要的文档集。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/Vfzo1iflSYeleQ501a-fvA/zh-cn_image_0000002701663350.png)
6. 选择代码文件进行问答，具体请参考[智能问答](ide-harmonyos-ask.md)。
