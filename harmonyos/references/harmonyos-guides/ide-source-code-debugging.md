---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-source-code-debugging
title: 三方库源码调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > 三方库源码调试
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:f6d02f48de76ee1d6bdd8ee56fc2c9adb63215e98fe39c3651aad8a77540a866
---

三方共享包分为静态共享包HAR和动态共享包HSP，两种共享包的源码调试方式有所区别，具体请查看以下指导。

## 区分字节码HAR和源码HAR

HAR包分为字节码HAR和源码HAR，同时满足以下两个条件的是字节码HAR，否则是源码HAR，更多关于如何构建源码HAR和字节码HAR的指导请查看[构建HAR](ide-hvigor-build-har.md)。

1. 查看HAR包的ets目录下存在.abc文件。
2. 查看HAR包的oh-package.json5文件，存在byteCodeHar字段并且值为true。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/UNeNmlnRQeuLcgLBKJcjWQ/zh-cn_image_0000002808886335.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=5AC33C57D8E2DDD33049724D9869D848B951C5A7A105FAEAE70FC10EAD4DC008)

## 字节码HAR调试

### C++代码调试

如果HAP/HSP引用字节码HAR包，同时HAR包中包含C++代码，参考以下步骤对该HAR包进行调试。

1. 点击**Run > Edit Configurations > Debugger** **>** **Symbol Directories**页签，点击**+**，添加带调试信息的so文件，so文件在{ProjectPath}/{ModuleName}/build/{product}/intermediates/libs/default/arm64-v8a路径下。

   **说明** 

   在工程级或模块级build-profile.json5中添加strip字段并设置为false，可以生成带调试信息的so文件，具体请参考[配置CPP](ide-hvigor-cpp.md#section2182144382320)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/ushBMWabTf2n1XM-amB69w/zh-cn_image_0000002808766255.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=D6322153FD751A9E2E39E2908889FCB335E6B7CB6430332F3EF26211EA142925)
2. DevEco Studio调试应用时会优先加载配置的so文件，本地so文件包含调试信息时，可以正常调试源码。由于so的源码文件信息为编译时的文件路径，若与本地的源码文件路径不一致时，需要关联源码文件，有两种方式：
   * 方式一：可以在**LLDB Startup Commands**页签中添加命令做映射，示例如下。

     ```bash
     settings set -- target.source-map {old-path} {new-path}
     ```

     + old-path：编译时的文件路径。
     + new-path：本地的源码文件路径。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/iuc0p31URNGCrokb9s4blQ/zh-cn_image_0000002779566680.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=C17755B3D3D4021259215D0A3B7F76AD93FE22651EF0092EB1EAFF0A59D80770)
   * 方式二：当Step Into进入汇编代码后，会弹出源码关联的提示，请点击**Select file**，选择本地对应C++源码进行关联。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/qSH9NHwfTtm890g6fCd39g/zh-cn_image_0000002779566666.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=FC29C715EF50C69F4AD0892A69E067B9F58ABC1F914BA2BBACA15729589D2F4A)

### ArkTS代码调试

假如在工程A（HAR包工程）中以debug模式编译得到字节码HAR包，工程B（主工程）中引用该字节码HAR包，并且本地有HAR包的源码，要调试该字节码HAR，有两种方式：在主工程中调试或在HAR包工程中调试。

**说明** 

release模式编译的字节码HAR不支持调试。

* **方式一：在主工程中调试。**
  1. 在主工程中导入字节码HAR对应的模块，确保模块的层级目录与HAR包工程的保持一致，例如HAR模块都在工程根目录下。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/GOE-wFYqRPa6peehfnlPog/zh-cn_image_0000002779406694.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=E80985F6499022CE14592A31E277611ED82ADA34A2F90B4757FC02A859173DAA)
  2. 导入成功后，由于debug模式编译的字节码HAR中包含[sourceMap](ide-exception-stack-parsing-principle.md)，调试时默认会关联当前工程的源码，此时可以在HAR模块上直接添加断点。
* **方式二：在HAR包工程中调试，****通过修改前缀配置进行attach调试。**
  1. 在HAR包工程新建一个entry类型的demo主模块，如果主模块已存在则跳过本步骤。
  2. 在demo主模块的oh-package.json5中配置对字节码HAR包的依赖。

     ```json5
     // demo主模块的oh-package.json5
     "dependencies": {
       "@ohos/test_stage_ets_library": "file:./lib/test_stage_ets_library.har",
     }
     ```

     **说明** 

     如果在demo主模块的oh-package.json5中，配置对字节码HAR模块的依赖，如file:../test\_stage\_ets\_library，调试时可能导致断点无效。
  3. 在HAR包工程主模块中调用HAR模块的接口，确保编译后主模块的sourceMap文件中包含HAR模块的相关信息。
  4. 构建HAR包工程，打开主模块的sourceMap，根据HAR的oh-package.json5中的name进行查找，将Index文件的前缀路径记录为localUrl，例如以下的demo|test\_stage\_ets\_library|1.0.0。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/7eiAXHZkS7OnjsyyY6w-4g/zh-cn_image_0000002779406688.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=3682801E3488F9E2D16A160C733525A5E05E8FCF9D62714EA99C98828AF632A4)
  5. 主工程应用在设备上运行起来后，在HAR包工程中通过attach方式对该应用进行调试，在Debug窗口获取程序加载时的前缀，记录为remoteUrl，例如以下的entry|@ohos/test\_stage\_ets\_library|1.0.0。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/96dsIe3zSUy3N9_TGM6RkA/zh-cn_image_0000002779566670.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=2E5A3C396DAC9FC714BD9D6E2B81E884076019DE00FD501EF91C67CAB9D589AA)
  6. 点击**Run > Edit Configurations > Debugger** **> ArkTS Source Pairs**，点击**+**，填写前两个步骤获取到的**remoteUrl**和**localUrl**。
     + remoteUrl：应用程序加载HAR包的前缀路径。
     + localUrl：本地生成sourceMap中HAR的前缀路径。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/JRiYkcxaTYuHDr01CVHAIw/zh-cn_image_0000002808766259.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=F5C7B6999D02E257023254438EB9CE999C51CF6D010FBCCF36E459FA95DB9111)
  7. 在HAR包工程中重新通过attach方式对主工程应用进行调试，此时可以在HAR模块上添加断点进行调试。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/jt_Q_LkPTDmjpkAHSGRxIA/zh-cn_image_0000002779406692.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=77F7A8A8F9822336523ABF51295EAE5FE5A3659848642E7D70386C6AF18171AA)

  **说明** 

  如果在HAR包工程中同时配置[Symbol Directories](ide-source-code-debugging.md#section177418333199)和ArkTS Source Pairs，可同时attach调试ArkTS和C++断点。

## 源码HAR调试

### C++代码调试

如果HAP/HSP引用源码HAR包，同时HAR包中包含C++代码，可参考[字节码HAR](ide-source-code-debugging.md#section177418333199)进行调试。

### ArkTS代码调试

工程中引用源码HAR包，对该HAR包进行调试，根据本地是否有源码，调试方式分别如下：

* 如果HAR包在本地没有对应源码，此时应用构建打包时引用的源码来源是工程级oh\_modules目录下的源码，只能针对oh\_modules下的源码进行调试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/aBF_ny5lTha4adsEdmNO_w/zh-cn_image_0000002808766253.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=BA673D5E7B5B193652576FB25D70C113CCA307CEB3CB199E299C642EF2B1105D)
* 如果HAR包在本地有对应源码，调试时可关联本地源码以实现对源码的调试，有两种方式。
  + 方式一：参考[字节码HAR调试](ide-source-code-debugging.md#section1035165781918)。
  + 方式二：当Step Into进入oh\_modules中的ets代码后，会弹出源码关联的提示时，请点击**Choose Sources**，选择本地对应ets源码进行关联。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/CPz90uzhQ3egSCvrAp6b5w/zh-cn_image_0000002808886339.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=25BC47C2437877FE72D33EDD6C69AAFDD6B5E0CEC461235DD16AB376E37ABA2E)

## HSP源码调试

如果要调试HSP源码，需要将源码置于本地工程模块下，参考[字节码HAR的方式一](ide-source-code-debugging.md#li17359570194)进行调试。
