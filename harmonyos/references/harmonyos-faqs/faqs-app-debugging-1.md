---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-1
title: 调试过程中无法添加断点
breadcrumb: FAQ > DevEco Studio > 应用调试 > 调试过程中无法添加断点
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:03+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e62581a500be421336ecba315b52512fc02cd5f9a7700ff71dd0158044b8893d
---

**问题现象**

调试过程中无法添加断点，提示“Can't set breakpoint to remote debug server”，如图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/w7-kNsTORqGnBaXLFFlc9g/zh-cn_image_0000002250578541.png?HW-CC-KV=V1&HW-CC-Date=20260428T003002Z&HW-CC-Expire=86400&HW-CC-Sign=C18DD0F013009384309542A2BC2D094D25321B0AAC227AD090025B5598616246)

**解决措施**

请使用以下方法排查原因：

1. 检查是否存在xx.map文件。如果不存在，则需重新编译构建生成map文件，然后进行断点调试。

   * 对于stage模型工程，需检查sourceMaps.map文件是否存在。该文件由编译构建生成，位于模块的“entry\build\default\intermediates\loader\_out\default”目录下，如下图所示：

     **图1** stage模型工程中sourceMaps.map文件目录  
     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/4wRhfl0-QDeXxtRhL_dKLg/zh-cn_image_0000002250498437.png?HW-CC-KV=V1&HW-CC-Date=20260428T003002Z&HW-CC-Expire=86400&HW-CC-Sign=6220CBB7A71C791D40D940168331BBC66690F0D7A4ADD364D785A37621AF0E59)
   * 对于FA模型工程，需检查断点所在文件对应的map文件是否存在。该文件由编译构建生成，位于模块的“entry\build\default\intermediates\loader\_out\default”目录下，如下图所示：

     **图2** FA模型工程中map文件目录  
     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/V5ag1XnxRmyYW3WliUr0sw/zh-cn_image_0000002215658548.png?HW-CC-KV=V1&HW-CC-Date=20260428T003002Z&HW-CC-Expire=86400&HW-CC-Sign=31EB5B7B332D81BE943EE2EFE41C14C29A6968CC2956B2134540B4C3D935655F)

2. 检查代码文件是否已加载。启动调试后，如果断点所在代码文件未加载（已加载的代码文件会显示在下方**Console**中），则断点将无法添加。程序运行并加载代码文件后，断点即可正常添加。代码文件未加载的原因是未被入口模块直接或间接引入。

   **图3** 断点所在代码文件未加载  
   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/kSUPteQtRMy5m6wLy3miHA/zh-cn_image_0000002215498752.png?HW-CC-KV=V1&HW-CC-Date=20260428T003002Z&HW-CC-Expire=86400&HW-CC-Sign=CCF9FF746839599F9CF2197E99F1C79DF917603DC1C7925430CD639C5C2E9E44 "点击放大")
3. 断点添加位置无效。ArkTS不支持在方法的右括号单独所在行添加断点。

   **图4** 断点位置无效  
   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/etuhLe7mRzG6n1G4Wiz0IQ/zh-cn_image_0000002250578549.png?HW-CC-KV=V1&HW-CC-Date=20260428T003002Z&HW-CC-Expire=86400&HW-CC-Sign=F99E7CEC9A2767571E686B9CBDABFA289513CCC96D52DAE7306F3E6A9B881E49 "点击放大")
