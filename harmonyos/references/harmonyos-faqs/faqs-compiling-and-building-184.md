---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-184
title: 编译报错“Cannot read properties of undefined (reading 'split')”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Cannot read properties of undefined (reading 'split')”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:02+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:2ba26aef44bac6a3fe9339ea440f73e7e75213d6f19c9eaeb7e04302b6e35721
---

* 场景一：

  **问题现象**

  当前使用的DevEco Studio版本与SDK版本不配套，导致DevEco Studio抛出异常：“TypeError: Cannot read properties of undefined (reading 'split')”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/45-85tBmT4uOxDHtaKO39g/zh-cn_image_0000002264138776.png?HW-CC-KV=V1&HW-CC-Date=20260429T062101Z&HW-CC-Expire=86400&HW-CC-Sign=93B82EBCDD13E1AB27208858E13110EB6867BC14DBABCA56E599676D35242FD1)

  **解决措施**

  1. 访问华为[开发者官网](https://developer.huawei.com/consumer/cn/download/deveco-studio)下载最新版DevEco Studio。
  2. 使用新版本DevEco Studio打开待迁移项目。
  3. 根据DevEco Studio自动弹出的迁移提示进行操作。
     + 点击“Migrate Assistant”功能。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/KG_IjWdRTfal5I-5ily6Rw/zh-cn_image_0000002264083104.png?HW-CC-KV=V1&HW-CC-Date=20260429T062101Z&HW-CC-Expire=86400&HW-CC-Sign=8BDE2EB34210C37D862FC499A9BA215F1ED9488D9BA403094C0AAD66290B943E)

     + 从版本列表中选择目标迁移版本。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/47LWDn0HRWS04QG6M_Ay7g/zh-cn_image_0000002264081160.png?HW-CC-KV=V1&HW-CC-Date=20260429T062101Z&HW-CC-Expire=86400&HW-CC-Sign=018E0BE407CC7E546E2644FFFF8682B766FD4E2F87B21E0C0B8BADA37E4EDBB8)

     + 按照向导完成项目迁移流程。
* 场景二：

  **问题现象**

  当工程级 build-profile.json5 文件未配置工程外模块依赖，而模块级 oh-package.json5 声明了工程外模块依赖并在代码中实际引用时，编译阶段会抛出异常：”Error: Cannot read properties of undefined (reading 'split')”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/S-KzPiRPTCiiVuzcS3na1w/zh-cn_image_0000002264140556.png?HW-CC-KV=V1&HW-CC-Date=20260429T062101Z&HW-CC-Expire=86400&HW-CC-Sign=CBB7B0BA8A696B28F09642AD054055074A0ED1F433196D03CC748ADBAAE15079)

  **解决措施**

  1. 检查下报错子模块中所引用的依赖，确保目标模块已在工程级 build-profile.json5 文件的 modules 字段中正确声明。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/2Ssn1DovTfOztEK_GHfr1Q/zh-cn_image_0000002264140648.png?HW-CC-KV=V1&HW-CC-Date=20260429T062101Z&HW-CC-Expire=86400&HW-CC-Sign=F0F613084D853910B8D5A58F080FB5385F84C24D76BC993D64DF0A8197AB199A)
  2. 确认当前子模块的 oh-package.json5 中，该模块已添加到 dependencies 依赖列表。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/6CKyZkFuT9iUwGii71DD0w/zh-cn_image_0000002298773813.png?HW-CC-KV=V1&HW-CC-Date=20260429T062101Z&HW-CC-Expire=86400&HW-CC-Sign=464DFCF49D3AD0D66BEF12CC2321741F03577EE7A189D168C90436BEFEF618D2)
  3. 若发现配置缺失，请手动补充完整。删除项目中的 oh\_modules 缓存目录，然后重新执行编译。
* 场景三：

  **问题现象**

  在HAP依赖字节码HAR进行编译的场景下，当import语句中的模块别名与dependencies中声明的别名大小写不一致时，编译系统将无法正确识别该依赖为字节码HAR，进而导致编译错误。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/BmVhWeL9R9W1libC1oji8A/zh-cn_image_0000002264083960.png?HW-CC-KV=V1&HW-CC-Date=20260429T062101Z&HW-CC-Expire=86400&HW-CC-Sign=A48536FC47A1ED8066150B8E1FFD22F9725538FB5D8910B91DFF860D0060F5FB)

  **解决措施**

  请检查并确保所有import语句的模块别名与其在dependencies中的声明保持完全一致的大小写格式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/d58_Ad5HQHCkVPLb0MeOrw/zh-cn_image_0000002298661041.png?HW-CC-KV=V1&HW-CC-Date=20260429T062101Z&HW-CC-Expire=86400&HW-CC-Sign=26622531E3E82C11ACB3C037608399B9ABD242D79252875B498347A00F5BEE16)
* 场景四：

  **问题现象**

  在编译字节码HAR时，若将依赖配置于devDependencies下，hvigor构建系统在编译阶段不会收集devDependencies中的依赖项，导致依赖解析失败并引发编译错误。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/-KjZmZKxTYSypCrRFweB6A/zh-cn_image_0000002264141304.png?HW-CC-KV=V1&HW-CC-Date=20260429T062101Z&HW-CC-Expire=86400&HW-CC-Sign=24DB2352700F10503CEDAE5B90E1376B4AE43C78508B7D2B2EB4C95B881FC15C)

  **解决措施**

  请将依赖项从devDependencies移至dependencies。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/SQuZPANSR5WrUgxpHJ4BAA/zh-cn_image_0000002264084432.png?HW-CC-KV=V1&HW-CC-Date=20260429T062101Z&HW-CC-Expire=86400&HW-CC-Sign=59CCAC2BA0510B8513615DE1156F4C4E33FB918B6B25EF8F110B0783EB62641E)
