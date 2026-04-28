---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-10
title: 编译报错“Failed to get a resolved OhmUrl by filepath xx”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Failed to get a resolved OhmUrl by filepath xx”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:09+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:8e82e5cc5193d0e4f16a384e220701e848e0b1c906c07e1bd0b7ad25d92932fd
---

* **场景一：**

  **问题现象**

  如果工程在本地可编译成功，压缩后拷贝到其他环境中再打开该工程编译构建失败，提示 “ERROR: ArkTS:ERROR Failed to get a resolved OhmUrl by filepath xx”。

  **解决措施**

  该问题源于工程中存在oh\_modules目录。由于oh\_modules中包含软链接，压缩后软链接失效，导致在其他环境中编译时无法找到对应的文件。

  删除工程中的oh\_modules，执行File > Sync and Refresh Project。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/-1vdUEAARw2pzDaSUJ-9XA/zh-cn_image_0000002194158588.png?HW-CC-KV=V1&HW-CC-Date=20260428T002908Z&HW-CC-Expire=86400&HW-CC-Sign=751742D101CE6334ECD8D4697B310044CE2BC12816C6B073F26D56DA24DBA012)
* **场景二：**

  **问题现象**

  当配置第三方包依赖时，如果将依赖配置到devDependencies，而源码中又引用了这些依赖中的 API，会导致编译失败。例如，第三方包@hms-security/ucs-appauth将依赖@network/gr配置在devDependencies中，源码中使用了@network/gr的 API 时，编译会失败，提示错误信息：“ERROR: ArkTS:ERROR Failed to get a resolved OhmUrl by filepath xxx”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/1nNVRmS7R226ppzvxY1f4A/zh-cn_image_0000002229603977.png?HW-CC-KV=V1&HW-CC-Date=20260428T002908Z&HW-CC-Expire=86400&HW-CC-Sign=78546BBD4D1A9CB1D67DE5B3265E60B593FC7FF6036A2AD7F7185F688CC56DF7)

  **问题确认**
  1. 进入上面标黄色的源码文件中，可以看到依赖有红色告警信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/vTN__BEXQ_CINx_MHgkJAg/zh-cn_image_0000002194318188.png?HW-CC-KV=V1&HW-CC-Date=20260428T002908Z&HW-CC-Expire=86400&HW-CC-Sign=CB03073C9A9E7179BCED7C6460D632CAB9C05403631255C714B82DD8255B49B4 "点击放大")
  2. 进入包下的oh-package.json5文件，查看依赖配置为devDependencies。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/sbEw0DmjT3SKLrFZTXz64g/zh-cn_image_0000002229603989.png?HW-CC-KV=V1&HW-CC-Date=20260428T002908Z&HW-CC-Expire=86400&HW-CC-Sign=91790AA92B53DE750D1C8227109F535AF69467020A03E10C43CB18CC3F99A5F9)

  **解决措施**

  + 向开发团队建议：运行时的依赖不应配置在devDependencies中。
  + 在依赖上层引入对应的devDependencies中的第三方包规避此问题。

* **场景三：**

  **问题现象**

  DevEco Studio编译失败，提示“ERROR: ArkTS:ERROR Failed to get a resolved OhmUrl by filepath xxx”。

  **问题确认**

  检查工程目录下的build-profile.json5文件中modules字段配置的srcPath路径是否与实际路径不同，以及是否存在大小写不一致的问题。

  **解决措施**

  将build-profile.json5文件中modules字段的srcPath路径与真实路径保持一致。
* **场景四：**

  **问题现象**

  工程A以相对路径引用了工程B的模块，这种引用会导致报错。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/KDxDPwAiSwm0gTmg_dB6cg/zh-cn_image_0000002194318200.png?HW-CC-KV=V1&HW-CC-Date=20260428T002908Z&HW-CC-Expire=86400&HW-CC-Sign=F475BA7AC5BD1098FA2AC718B02C4C6B47C57F5C60245569A6FF0523946D601B)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/bmu8-_idQLagFPv3xC00QQ/zh-cn_image_0000002194158572.png?HW-CC-KV=V1&HW-CC-Date=20260428T002908Z&HW-CC-Expire=86400&HW-CC-Sign=DEC81C8D32199D63CC6F2FD0F07880184144C00F57D244C018F7DE59E86D9E17)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/wBiXdWoGSe29KPO_tAzawA/zh-cn_image_0000002229758449.png?HW-CC-KV=V1&HW-CC-Date=20260428T002908Z&HW-CC-Expire=86400&HW-CC-Sign=6E7D6AC2941DD4C8D627A77B53158F01E67AF34DE1863D8FEF12677B0FBFF56B)**处理措施**

  + 将工程B的har转换为工程A的一个模块引用。
  + 把工程B的har提前打包，在A中 以.har的方式引用。
  + 上传到仓库，以版本号的方式引用。
* **场景五：**

  **问题现象**

  DevEco Studio编译失败，提示“Error Message: Failed to get a resolved OhmUrl for 'hvigor\\_ignore\\_xxxxx' imported by xxx”。

  **处理措施**

  如果hvigor\_ignore\_xxxxx所在的模块是一个har模块，需要排查oh-package.json5中是否存在“"packageType": "InterfaceHar"”，如果存在，请删除“"packageType": "InterfaceHar"”。

  如果hvigor\_ignore\_xxxxx所在的模块是一个hsp模块，需要排查${模块路径}\build\default\cache\default\default@CompileArkTS\esmodule\${debug/release}\filesInfo.txt文件中是否存在hvigor\_ignore\_xxxxx路径，如果存在，可将hvigor\_ignore\_xxxxx路径所在的模块或包添加到当前编译模块oh-package.json5的dependencies中临时规避。
* **场景六：**

  **问题现象**

  DevEco Studio编译失败，提示“Failed to get a resolved OhmUrl for‘xxx’imported by‘yyy’”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/aZ8encgmSaCX195rAk21gQ/zh-cn_image_0000002194318204.png?HW-CC-KV=V1&HW-CC-Date=20260428T002908Z&HW-CC-Expire=86400&HW-CC-Sign=5514119A4816803652C8ECEE51ED1FCB47C839504A961BDA14E7092BED6F97F1 "点击放大")

  **问题确认**

  1. 检查yyy所在模块是否为[字节码HAR](../harmonyos-guides/ide-hvigor-build-har.md#section16598338112415)，并查看工程级build-profile.json5的useNormalizedOHMUrl是否为true（缺省默认值为false）。如果为true，则默认构建字节码har。
  2. 如果yyy模块是字节码har，请检查xxx依赖是否已配置在工程级oh-package.json5的dependencies中，但未配置在yyy模块级oh-package.json5的dependencies中。

  **处理措施**

  + 将xxx依赖配置到yyy模块oh-package.json5的dependencies中。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/ReDyGYfgSveD3woThJS2eg/zh-cn_image_0000002229603981.png?HW-CC-KV=V1&HW-CC-Date=20260428T002908Z&HW-CC-Expire=86400&HW-CC-Sign=18E47E02B481589DFC7BC88CF9667B7F4D68322BA3BF5F9F260F0639CA9D548F "点击放大")
  + 将yyy模块改为非字节码har，在模块级build-profile.json5文件中添加byteCodeHar字段并设置为false。

* **场景七：**

  请确认当前使用的DevEco Studio和SDK版本是配套的，点击菜单栏**Help > About DevEco Studio**，**Help > About HarmonyOS SDK**分别查看DevEco Studio和SDK版本，版本配套关系请参考[版本概览](../harmonyos-releases/overview-502-release.md)。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/0fA27ZT3RqiLMazQHl1nDg/zh-cn_image_0000002229603985.png?HW-CC-KV=V1&HW-CC-Date=20260428T002908Z&HW-CC-Expire=86400&HW-CC-Sign=9423BF0AEF64B5BFF5BBAEEFF356AD709279938F7DE3FBB3FA3C7052866A94E5)
* **场景八：**

  **问题现象：**

  DevEco Studio编译失败，提示“ERROR: ArkTS:ERROR failed to execute es2abc ERROR: ArkTS:ERROR Failed to get a resolved OhmUrl by filepath xxx”。

  **处理措施**

  该问题由工程中引用了非标准模块目录（目录内无module.json5）引起，如下图所示。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/XJcjC0KaR1ykOzbsef9tBA/zh-cn_image_0000002194318192.png?HW-CC-KV=V1&HW-CC-Date=20260428T002908Z&HW-CC-Expire=86400&HW-CC-Sign=7DAFDD16887F69E184D44C66B507FF1D10367C14DD5C6FEA84BC6BD4CA9EE79E)

  请新建Static Library模块，并将utils/common里面的代码迁移至Static Library模块内，并使用HAP引用HAR方式进行模块间引用。
