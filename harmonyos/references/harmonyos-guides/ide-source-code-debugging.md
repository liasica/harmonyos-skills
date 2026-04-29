---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-source-code-debugging
title: 三方库源码调试
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > 三方库源码调试
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9e2a6d8ed36907113c243b746a6c0639f1f5c37dd343cb3795d6000f6e6ab36b
---

三方共享包分为静态共享包HAR和动态共享包HSP，两种共享包的源码调试方式有所区别，具体请查看以下指导。

## 区分字节码HAR和源码HAR

HAR包分为字节码HAR和源码HAR，同时满足以下两个条件的是字节码HAR，否则是源码HAR，更多关于如何构建源码HAR和字节码HAR的指导请查看[构建HAR](ide-hvigor-build-har.md)。

1. 查看HAR包的ets目录下存在.abc文件。
2. 查看HAR包的oh-package.json5文件，存在byteCodeHar字段并且值为true。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/IM5RlJBqRYiNxloLIEk_SQ/zh-cn_image_0000002530752836.png?HW-CC-KV=V1&HW-CC-Date=20260429T054647Z&HW-CC-Expire=86400&HW-CC-Sign=4FE1A6A5C7F3AB4208383E89C4B044EC13A7D21052A0399213ABDE2BA4CEC458)

## 字节码HAR调试

### C++代码调试

如果HAP/HSP引用字节码HAR包，同时HAR包中包含C++代码，参考以下步骤对该HAR包进行调试。

1. 点击**Run > Edit Configurations > Debugger** **>** **Symbol Directories**页签，点击**+**，添加带调试信息的so文件，so文件在{ProjectPath}/{ModuleName}/build/{product}/intermediates/libs/default/arm64-v8a路径下。

   说明

   在工程级或模块级build-profile.json5中添加strip字段并设置为false，可以生成带调试信息的so文件，具体请参考[配置CPP](ide-hvigor-cpp.md#section2182144382320)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/Uf82nfZDTsONQmVzNRCu9g/zh-cn_image_0000002561752777.png?HW-CC-KV=V1&HW-CC-Date=20260429T054647Z&HW-CC-Expire=86400&HW-CC-Sign=5436683E38DAE85256954639B098CEA1092811CD8E1246B743C4468568A58EDF)
2. DevEco Studio调试应用时会优先加载配置的so文件，本地so文件包含调试信息时，可以正常调试源码。由于so的源码文件信息为编译时的文件路径，若与本地的源码文件路径不一致时，需要关联源码文件，有两种方式：
   * 方式一：可以在**LLDB Startup Commands**页签中添加命令做映射，示例如下。

     ```
     1. settings set -- target.source-map {old-path} {new-path}
     ```

     + old-path：编译时的文件路径。
     + new-path：本地的源码文件路径。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/JrwBwre_R66QG2m5llBBbg/zh-cn_image_0000002530912838.png?HW-CC-KV=V1&HW-CC-Date=20260429T054647Z&HW-CC-Expire=86400&HW-CC-Sign=F2956C78FB9F244AF7E3B31E3A52AFBB1E6448DDE393930BA141BBDC30F2186A)
   * 方式二：当Step Into进入汇编代码后，会弹出源码关联的提示，请点击**Select file**，选择本地对应C++源码进行关联。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/AWRBrqAVQuy3NKbQyFA40g/zh-cn_image_0000002561832745.png?HW-CC-KV=V1&HW-CC-Date=20260429T054647Z&HW-CC-Expire=86400&HW-CC-Sign=7FC7D175A37FD4DD50F73599D175FD7670CB7BCA6C1A9E72A42DC1018FAF70CA)

### ArkTS代码调试

假如在工程A（HAR包工程）中以debug模式编译得到字节码HAR包，工程B（主工程）中引用该字节码HAR包，并且本地有HAR包的源码，要调试该字节码HAR，有两种方式：在主工程中调试或在HAR包工程中调试。

说明

release模式编译的字节码HAR不支持调试。

* **方式一：在主工程中调试。**
  1. 在主工程中导入字节码HAR对应的模块，确保模块的层级目录与HAR包工程的保持一致，例如HAR模块都在工程根目录下。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/uju74WvWSESd1Okc2NNx7A/zh-cn_image_0000002561752775.png?HW-CC-KV=V1&HW-CC-Date=20260429T054647Z&HW-CC-Expire=86400&HW-CC-Sign=EF38ECE1046833E5B5077423EB883C383E062A623F8DFC567E36416640B4CA67)
  2. 导入成功后，由于debug模式编译的字节码HAR中包含[sourceMap](ide-exception-stack-parsing-principle.md)，调试时默认会关联当前工程的源码，此时可以在HAR模块上直接添加断点。
* **方式二：在HAR包工程中调试，****通过修改前缀配置进行attach调试。**
  1. 在HAR包工程新建一个entry类型的demo主模块，如果主模块已存在则跳过本步骤。
  2. 在demo主模块的oh-package.json5中配置对字节码HAR包的依赖。

     ```
     1. // demo主模块的oh-package.json5
     2. "dependencies": {
     3. "@ohos/test_stage_ets_library": "file:./lib/test_stage_ets_library.har",
     4. }
     ```

     说明

     如果在demo主模块的oh-package.json5中，配置对字节码HAR模块的依赖，如file:../test\_stage\_ets\_library，调试时可能导致断点无效。
  3. 在HAR包工程主模块中调用HAR模块的接口，确保编译后主模块的sourceMap文件中包含HAR模块的相关信息。
  4. 构建HAR包工程，打开主模块的sourceMap，根据HAR的oh-package.json5中的name进行查找，将Index文件的前缀路径记录为localUrl，例如以下的demo|test\_stage\_ets\_library|1.0.0。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/HOzISMWgTjW4--MWNsB1Cg/zh-cn_image_0000002530752824.png?HW-CC-KV=V1&HW-CC-Date=20260429T054647Z&HW-CC-Expire=86400&HW-CC-Sign=1097BC28927D85E6ECE7E2ECCA66179069B1C8994C0F03A72EB623F894249979)
  5. 主工程应用在设备上运行起来后，在HAR包工程中通过attach方式对该应用进行调试，在Debug窗口获取程序加载时的前缀，记录为remoteUrl，例如以下的entry|@ohos/test\_stage\_ets\_library|1.0.0。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/ln_DzdMfTvmwgApayL1Bew/zh-cn_image_0000002561752769.png?HW-CC-KV=V1&HW-CC-Date=20260429T054647Z&HW-CC-Expire=86400&HW-CC-Sign=88063D0FC9F7F374A63D4EE26A0CC59DAE868913FC96DE090A3DDBC3FCE4A501)
  6. 点击**Run > Edit Configurations > Debugger** **> Ets Source Pairs**，点击**+**，填写前两个步骤获取到的**remoteUrl**和**localUrl**。
     + remoteUrl：应用程序加载HAR包的前缀路径。
     + localUrl：本地生成sourceMap中HAR的前缀路径。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/Er1qe-dnR6-xs-zpzgRdZw/zh-cn_image_0000002530912816.png?HW-CC-KV=V1&HW-CC-Date=20260429T054647Z&HW-CC-Expire=86400&HW-CC-Sign=8E146A83FE797080794ED955A31A71D6378C9010B4861F910B211503F0DF03BE)
  7. 在HAR包工程中重新通过attach方式对主工程应用进行调试，此时可以在HAR模块上添加断点进行调试。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/K4lxopw2SKOMi_gNYdTDig/zh-cn_image_0000002561832747.png?HW-CC-KV=V1&HW-CC-Date=20260429T054647Z&HW-CC-Expire=86400&HW-CC-Sign=C744919BF537C0FDD79DCA090361FFD96AAE79592EF38F84F1469644DEE5550C)

  说明

  如果在HAR包工程中同时配置[Symbol Directories](ide-source-code-debugging.md#section177418333199)和Ets Source Pairs，可同时attach调试ArkTS和C++断点。

## 源码HAR调试

### C++代码调试

如果HAP/HSP引用源码HAR包，同时HAR包中包含C++代码，可参考[字节码HAR](ide-source-code-debugging.md#section177418333199)进行调试。

### ArkTS代码调试

工程中引用源码HAR包，对该HAR包进行调试，根据本地是否有源码，调试方式分别如下：

* 如果HAR包在本地没有对应源码，此时应用构建打包时引用的源码来源是工程级oh\_modules目录下的源码，只能针对oh\_modules下的源码进行调试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/ThremzjjR_iLPAtXM6MEog/zh-cn_image_0000002561752771.png?HW-CC-KV=V1&HW-CC-Date=20260429T054647Z&HW-CC-Expire=86400&HW-CC-Sign=1BE9566302320FB5E5450A4FA41EA72DCED7F88774CFD20B474305F2B37D450C)
* 如果HAR包在本地有对应源码，调试时可关联本地源码以实现对源码的调试，有两种方式。
  + 方式一：参考[字节码HAR调试](ide-source-code-debugging.md#section1035165781918)。
  + 方式二：当Step Into进入oh\_modules中的ets代码后，会弹出源码关联的提示时，请点击**Choose Sources**，选择本地对应ets源码进行关联。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/m1B11Kf4Sea6l1HdXy3q2g/zh-cn_image_0000002561752779.png?HW-CC-KV=V1&HW-CC-Date=20260429T054647Z&HW-CC-Expire=86400&HW-CC-Sign=6A180177A1ED08D3BE692CB7F2E23E59FB1B9886C5E726E1B4ACD96EF1BCD1AA)

## HSP源码调试

如果要调试HSP源码，需要将源码置于本地工程模块下，参考[字节码HAR的方式一](ide-source-code-debugging.md#li17359570194)进行调试。
