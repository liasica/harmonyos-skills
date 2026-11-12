---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ocal-knowledge
title: 本地知识库配置
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 本地知识库配置
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:5bf65a3cde7cab7932161a8dc5ebc5f2970ea08e4944605fe63207cee4e301be
---

从DevEco Studio 6.0.0 Beta5开始，CodeGenie允许用户导入设计文档和代码等文件形成文档集，多个文档集组合成本地知识库。智能问答时，根据用户输入内容检索本地知识库以提升AI生成的能力。

## 操作步骤

1. 点击**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> CodeGenie****> Knowledge >** **Docs**，或在DevEco Studio右侧边栏点击**CodeGenie**（或输入快捷键**Alt/Option+U**） **>** **@****Add Context** **> Docs > Set Local Knowledge Base**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/XDr8ZwfCTOK8omT4-iS1pQ/zh-cn_image_0000002779407332.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=14065A5EFC0106CCB85ED2D664EB877F593EE50F18800E90CC73F30FA4133896)
2. 首次打开时，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/AYWUKTeWSFm1NexXkuNdVg/zh-cn_image_0000002808886971.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=9563D02CC84960DDAE6499B933B83028B3DCD55B35B75ED1F0E4636C42B7EDF2 "点击放大")按钮，填写相关信息，创建文档集。
   * **Knowledge Base Path**：知识库保存路径。在同一个路径下保存的文档集，会形成一个知识库。
   * **Document set name**：文档集名称。
   * **Description**：可选，文档集描述。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/SOw4AUrhQdOpmsJGED-5Ig/zh-cn_image_0000002779407334.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=39A195CF01E2ABFAC3200B7602CDF14087ED4BD58682C2D44DA5DFB365EE8A73)
3. 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/SaCD3swDQOiTlvX7HOm8pQ/zh-cn_image_0000002779567314.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=64B3D3CFD7F2360E97EE877527BC3CFE6AC0BD1C6E8B0B7515C4202B35D24C72 "点击放大")按钮，添加文档集中的文件，添加成功的文件在下方展示。

   **说明** 

   1. 支持的文件格式：txt、md、json、html、cpp、ets、ts、js。
   2. 单个文档集中文件个数：不超过1000个。
   3. 单个文件大小：不超过10M。
   4. 单个知识库中文档集个数：不超过20个。
   5. 单个知识库大小：不超过50M。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/RDjdDEP9Q_mpXsxiJHc_HA/zh-cn_image_0000002808766895.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=8FF142E069845F445C3149425CE024D308BD6EEA3EDBBEFCB9C973A2B30E2556)
4. 点击“**OK**”，完成本地知识库配置和同步，在DevEco Studio页面下方**Storing document set**可查看同步进度。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/nxvtFUyiSn-flke2yLvUZw/zh-cn_image_0000002779567312.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=3BDC99941BE6757CA577B9A4161E0629414E8759B82632F35E491FC9AD534259 "点击放大")
5. 同步完成后，在对话框中输入**@**符号选择**Docs** ，或点击上方**@****Add Context** **> Docs** ，选择需要的文档集。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/137pItZtSPyRxtnZZ13sLA/zh-cn_image_0000002808886975.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=F0535E5E3D48511A379DBA5DFBEC5CD03652E125584AE0CB36B661DBDF13F1BF)
6. 选择代码文件进行问答，具体请参考[智能问答](ide-harmonyos-ask.md)。
