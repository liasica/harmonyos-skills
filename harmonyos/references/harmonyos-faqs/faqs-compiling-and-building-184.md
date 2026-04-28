---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-184
title: 编译报错“Cannot read properties of undefined (reading 'split')”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Cannot read properties of undefined (reading 'split')”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:48+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e12d31e78a5ab4651869dd9914b15e533ffd23cc896a143a08dbcb1581332222
---

* 场景一：

  **问题现象**

  当前使用的DevEco Studio版本与SDK版本不配套，导致DevEco Studio抛出异常：“TypeError: Cannot read properties of undefined (reading 'split')”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/45-85tBmT4uOxDHtaKO39g/zh-cn_image_0000002264138776.png?HW-CC-KV=V1&HW-CC-Date=20260428T002946Z&HW-CC-Expire=86400&HW-CC-Sign=89C45EA6F208BAB1C7A8BF703A446901443D91B056D5A63ED3C308557A7A022A)

  **解决措施**

  1. 访问华为[开发者官网](https://developer.huawei.com/consumer/cn/download/deveco-studio)下载最新版DevEco Studio。
  2. 使用新版本DevEco Studio打开待迁移项目。
  3. 根据DevEco Studio自动弹出的迁移提示进行操作。
     + 点击“Migrate Assistant”功能。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/KG_IjWdRTfal5I-5ily6Rw/zh-cn_image_0000002264083104.png?HW-CC-KV=V1&HW-CC-Date=20260428T002946Z&HW-CC-Expire=86400&HW-CC-Sign=75FD1468B36BA4CD728ACD3470B227C6CAF250FE65A51A2AAEF620CF68C1E00C)

     + 从版本列表中选择目标迁移版本。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/47LWDn0HRWS04QG6M_Ay7g/zh-cn_image_0000002264081160.png?HW-CC-KV=V1&HW-CC-Date=20260428T002946Z&HW-CC-Expire=86400&HW-CC-Sign=DB1B45E8E956E9E5A0600DE8B85C8DC835557A997202AE5BC2B8BD207A448FFD)

     + 按照向导完成项目迁移流程。
* 场景二：

  **问题现象**

  当工程级 build-profile.json5 文件未配置工程外模块依赖，而模块级 oh-package.json5 声明了工程外模块依赖并在代码中实际引用时，编译阶段会抛出异常：”Error: Cannot read properties of undefined (reading 'split')”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/S-KzPiRPTCiiVuzcS3na1w/zh-cn_image_0000002264140556.png?HW-CC-KV=V1&HW-CC-Date=20260428T002946Z&HW-CC-Expire=86400&HW-CC-Sign=1012531DEA3E7E823184528545F3725339CED49C1C4F3BB928D6B44BF353744A)

  **解决措施**

  1. 检查下报错子模块中所引用的依赖，确保目标模块已在工程级 build-profile.json5 文件的 modules 字段中正确声明。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/2Ssn1DovTfOztEK_GHfr1Q/zh-cn_image_0000002264140648.png?HW-CC-KV=V1&HW-CC-Date=20260428T002946Z&HW-CC-Expire=86400&HW-CC-Sign=04714E6D1729FA2EF55DC6219A1FEA7D68358ED37E97C2D3585CB013F8AD8E21)
  2. 确认当前子模块的 oh-package.json5 中，该模块已添加到 dependencies 依赖列表。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/6CKyZkFuT9iUwGii71DD0w/zh-cn_image_0000002298773813.png?HW-CC-KV=V1&HW-CC-Date=20260428T002946Z&HW-CC-Expire=86400&HW-CC-Sign=A3E9CA1059755AB22A9637816042E66923AECC99BB1A60E8BB2D38F70EE2E890)
  3. 若发现配置缺失，请手动补充完整。删除项目中的 oh\_modules 缓存目录，然后重新执行编译。
* 场景三：

  **问题现象**

  在HAP依赖字节码HAR进行编译的场景下，当import语句中的模块别名与dependencies中声明的别名大小写不一致时，编译系统将无法正确识别该依赖为字节码HAR，进而导致编译错误。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/BmVhWeL9R9W1libC1oji8A/zh-cn_image_0000002264083960.png?HW-CC-KV=V1&HW-CC-Date=20260428T002946Z&HW-CC-Expire=86400&HW-CC-Sign=BF80663BFCCF83D461AD1C0227CDAD0C515BC92E33C5ED3634115D3CF5599E4C)

  **解决措施**

  请检查并确保所有import语句的模块别名与其在dependencies中的声明保持完全一致的大小写格式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/d58_Ad5HQHCkVPLb0MeOrw/zh-cn_image_0000002298661041.png?HW-CC-KV=V1&HW-CC-Date=20260428T002946Z&HW-CC-Expire=86400&HW-CC-Sign=945A1784653864BF146A9D945CD97548A13F38FC84F3A821338F9F91702A90D8)
* 场景四：

  **问题现象**

  在编译字节码HAR时，若将依赖配置于devDependencies下，hvigor构建系统在编译阶段不会收集devDependencies中的依赖项，导致依赖解析失败并引发编译错误。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/-KjZmZKxTYSypCrRFweB6A/zh-cn_image_0000002264141304.png?HW-CC-KV=V1&HW-CC-Date=20260428T002946Z&HW-CC-Expire=86400&HW-CC-Sign=F1CE8E82151D39540F0378BED29209CF0925CDB28861D1EAAC6FBFC7FB73C541)

  **解决措施**

  请将依赖项从devDependencies移至dependencies。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/SQuZPANSR5WrUgxpHJ4BAA/zh-cn_image_0000002264084432.png?HW-CC-KV=V1&HW-CC-Date=20260428T002946Z&HW-CC-Expire=86400&HW-CC-Sign=FDC94E51DBC9F9861C612585528725C2A85938B091E06B8E61F5A29784191EA2)
