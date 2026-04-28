---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-extension
title: extension调试
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > extension调试
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:47+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:06cf283a59a16311534ac213722088d2f291e5ec0c31ba2176ecdbb2e00bf9b1
---

开发者可通过两种方式对[Extension Ability](extensionability-overview.md)生命周期函数进行调试。

* 应用安装到设备上后，通过等待调试方式进行调试。
* 修改运行调试配置项，指定当前运行或调试的Ability为Extension Ability。

## 等待调试方式

1. 参考[等待调试](ide-debug-arkts-attach-to-process.md)对当前调试工程进行调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/eGJ33eaVTBKsL3Saw9kXRg/zh-cn_image_0000002530913458.png?HW-CC-KV=V1&HW-CC-Date=20260427T235646Z&HW-CC-Expire=86400&HW-CC-Sign=5C143CB5E18B97432EA3C2D8B5F71667180361DC2F161E0D8D1C27EA527D6794)
2. 在Extension Ability生命周期内设置断点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/Ir7GsXAGRmaDspxuOit9ig/zh-cn_image_0000002530913452.png?HW-CC-KV=V1&HW-CC-Date=20260427T235646Z&HW-CC-Expire=86400&HW-CC-Sign=7D5792F44FD22BD648889D7EA6CD79BAC11C36A6A0CDFAE7EA52E8A98923B263)
3. 等待Extension Ability生命周期函数代码调用从而命中断点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/v6usKOzaSReGleCgAsva8A/zh-cn_image_0000002561833381.png?HW-CC-KV=V1&HW-CC-Date=20260427T235646Z&HW-CC-Expire=86400&HW-CC-Sign=96BBE296D5094F062053EFC3D6BEF6634FAC5B02BD86DB0E4289CC52DF8979C0)

## 修改运行配置方式

1. 在运行调试窗口，运行配置项**Launch Options**选择**Specified Ability**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/gJTFxAXHR567IFsRloGcCg/zh-cn_image_0000002561833375.png?HW-CC-KV=V1&HW-CC-Date=20260427T235646Z&HW-CC-Expire=86400&HW-CC-Sign=979AF5A7EE34C739DC4163EC483BE618355F994740F78E1410510ED9E09EDA0F)
2. 选择需要进行调试的Extension Ability。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/RVesWrMlQYaoPRxU0hrM7w/zh-cn_image_0000002530913454.png?HW-CC-KV=V1&HW-CC-Date=20260427T235646Z&HW-CC-Expire=86400&HW-CC-Sign=DEF4C4A6547C1047E08D35D7FF32EAAF3A7F3A70C9681E32D028402E60A31C34)
3. 点击**OK**保存配置后，点击调试按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/6n1zmwLVTcmb3VubKmjdfw/zh-cn_image_0000002561833379.png?HW-CC-KV=V1&HW-CC-Date=20260427T235646Z&HW-CC-Expire=86400&HW-CC-Sign=682F26218EA49755D487B3BEC003CFA62D925E306520AE0C99B68CBCDEE08A8C)，启动调试即可命中 Extension Ability 中的生命周期函数断点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/uZF9iHgWSOWx8UQ8wDGnKg/zh-cn_image_0000002530913448.png?HW-CC-KV=V1&HW-CC-Date=20260427T235646Z&HW-CC-Expire=86400&HW-CC-Sign=84A40AD9E0CAEFBA728051C885778E732A9B2CCC779D5A0EE3D6D2E946D8105B)
