---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-1
title: 调试过程中无法添加断点
breadcrumb: FAQ > DevEco Studio > 应用调试 > 调试过程中无法添加断点
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:21+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:0b7f4e95bb9e8b522ad0cf9bfb715e51a774bb4d9f7906a449853be6e703829d
---

**问题现象**

调试过程中无法添加断点，提示“Can't set breakpoint to remote debug server”，如图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/w7-kNsTORqGnBaXLFFlc9g/zh-cn_image_0000002250578541.png?HW-CC-KV=V1&HW-CC-Date=20260429T062120Z&HW-CC-Expire=86400&HW-CC-Sign=9566EE81EE147D41247664E9CF941B1674CBC7FBDE2F5A64DABB7FE49A276AC7)

**解决措施**

请使用以下方法排查原因：

1. 检查是否存在xx.map文件。如果不存在，则需重新编译构建生成map文件，然后进行断点调试。

   * 对于stage模型工程，需检查sourceMaps.map文件是否存在。该文件由编译构建生成，位于模块的“entry\build\default\intermediates\loader\_out\default”目录下，如下图所示：

     **图1** stage模型工程中sourceMaps.map文件目录  
     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/4wRhfl0-QDeXxtRhL_dKLg/zh-cn_image_0000002250498437.png?HW-CC-KV=V1&HW-CC-Date=20260429T062120Z&HW-CC-Expire=86400&HW-CC-Sign=A49AB7CF11154C837258D86AB65A8FD81499F59BA85DB13E0FE228EAC11A79D1)
   * 对于FA模型工程，需检查断点所在文件对应的map文件是否存在。该文件由编译构建生成，位于模块的“entry\build\default\intermediates\loader\_out\default”目录下，如下图所示：

     **图2** FA模型工程中map文件目录  
     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/V5ag1XnxRmyYW3WliUr0sw/zh-cn_image_0000002215658548.png?HW-CC-KV=V1&HW-CC-Date=20260429T062120Z&HW-CC-Expire=86400&HW-CC-Sign=8B6CA26A76D36F792CB12FE8E6A2854AB8093DE3B71BBD0B5420A37522F3405E)

2. 检查代码文件是否已加载。启动调试后，如果断点所在代码文件未加载（已加载的代码文件会显示在下方**Console**中），则断点将无法添加。程序运行并加载代码文件后，断点即可正常添加。代码文件未加载的原因是未被入口模块直接或间接引入。

   **图3** 断点所在代码文件未加载  
   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/kSUPteQtRMy5m6wLy3miHA/zh-cn_image_0000002215498752.png?HW-CC-KV=V1&HW-CC-Date=20260429T062120Z&HW-CC-Expire=86400&HW-CC-Sign=2622DD9BD88DF06FE4F643186BC0644575FE414C85AD8B9B1540035106F12BB7 "点击放大")
3. 断点添加位置无效。ArkTS不支持在方法的右括号单独所在行添加断点。

   **图4** 断点位置无效  
   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/etuhLe7mRzG6n1G4Wiz0IQ/zh-cn_image_0000002250578549.png?HW-CC-KV=V1&HW-CC-Date=20260429T062120Z&HW-CC-Expire=86400&HW-CC-Sign=292E810A4F6EC0F23250637A34EED1190F77E889B8093BD216D94877E7AEA61C "点击放大")
