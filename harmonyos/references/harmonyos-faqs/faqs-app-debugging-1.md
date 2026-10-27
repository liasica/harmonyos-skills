---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-1
title: 调试过程中无法添加断点
breadcrumb: FAQ > DevEco Studio > 应用调试 > 调试过程中无法添加断点
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:59+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:971899091b95e7c2d1e41609b4a3dbc5790bff0d9d00882fef6ee4a752833917
---

**问题现象**

调试过程中无法添加断点，提示“Can't set breakpoint to remote debug server”，如图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/YzXvO8xhQZSM7IGDb8AMlA/zh-cn_image_0000002654798139.png)

**解决措施**

请使用以下方法排查原因：

1. 检查是否存在xx.map文件。如果不存在，则需重新编译构建生成map文件，然后进行断点调试。

   * 对于stage模型工程，需检查sourceMaps.map文件是否存在。该文件由编译构建生成，位于模块的“entry\build\default\intermediates\loader\_out\default”目录下，如下图所示：

     **图1** stage模型工程中sourceMaps.map文件目录  
     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/nVgkzRDNSPKp5gyKoGlzGQ/zh-cn_image_0000002624638682.png)
   * 对于FA模型工程，需检查断点所在文件对应的map文件是否存在。该文件由编译构建生成，位于模块的“entry\build\default\intermediates\loader\_out\default”目录下，如下图所示：

     **图2** FA模型工程中map文件目录  
     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/veK_5r9_Raa9vXsOieSaKw/zh-cn_image_0000002654838091.png)

2. 检查代码文件是否已加载。启动调试后，如果断点所在代码文件未加载（已加载的代码文件会显示在下方**Console**中），则断点将无法添加。程序运行并加载代码文件后，断点即可正常添加。代码文件未加载的原因是未被入口模块直接或间接引入。

   **图3** 断点所在代码文件未加载  
   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/7Hec5dsPTKWn14ug_QkEsg/zh-cn_image_0000002624478774.png "点击放大")
3. 断点添加位置无效。ArkTS不支持在方法的右括号单独所在行添加断点。

   **图4** 断点位置无效  
   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/R0K_iJZMR-GYVnlO1Mf3zg/zh-cn_image_0000002654798141.png "点击放大")
