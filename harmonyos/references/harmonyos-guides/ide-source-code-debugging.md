---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-source-code-debugging
title: 三方库源码调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > 三方库源码调试
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:59+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:bfac3bff381c4933111590a02a8850ea91ea410e753c466564de7d17ae434faa
---

三方共享包分为静态共享包HAR和动态共享包HSP，两种共享包的源码调试方式有所区别，具体请查看以下指导。

## 区分字节码HAR和源码HAR

HAR包分为字节码HAR和源码HAR，同时满足以下两个条件的是字节码HAR，否则是源码HAR，更多关于如何构建源码HAR和字节码HAR的指导请查看[构建HAR](ide-hvigor-build-har.md)。

1. 查看HAR包的ets目录下存在.abc文件。
2. 查看HAR包的oh-package.json5文件，存在byteCodeHar字段并且值为true。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/eN4gEegvRC6bWmEuGnxZwQ/zh-cn_image_0000002808886335.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=CF7735694C2D68CB089CE1EE291A7B0D1BF267B5BC537300C11D278DD7E3DA47)

## 字节码HAR调试

### C++代码调试

如果HAP/HSP引用字节码HAR包，同时HAR包中包含C++代码，参考以下步骤对该HAR包进行调试。

1. 点击**Run > Edit Configurations > Debugger** **>** **Symbol Directories**页签，点击**+**，添加带调试信息的so文件，so文件在{ProjectPath}/{ModuleName}/build/{product}/intermediates/libs/default/arm64-v8a路径下。

   **说明** 

   在工程级或模块级build-profile.json5中添加strip字段并设置为false，可以生成带调试信息的so文件，具体请参考[配置CPP](ide-hvigor-cpp.md#section2182144382320)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/D_etQ6EzQeC5yUf81B7ETg/zh-cn_image_0000002808766255.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=8CF989469BE02AAB43F68E7358644A13D845EA3E1517CE7BD399F450D30CEF12)
2. DevEco Studio调试应用时会优先加载配置的so文件，本地so文件包含调试信息时，可以正常调试源码。由于so的源码文件信息为编译时的文件路径，若与本地的源码文件路径不一致时，需要关联源码文件，有两种方式：
   * 方式一：可以在**LLDB Startup Commands**页签中添加命令做映射，示例如下。

     ```bash
     settings set -- target.source-map {old-path} {new-path}
     ```

     + old-path：编译时的文件路径。
     + new-path：本地的源码文件路径。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/rxJrUGYWTvOH_q_hOOpP-g/zh-cn_image_0000002779566680.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=C721446455527590D1092956BAB0C167B38D3F1E8BA2EC7BBD8913031B66E595)
   * 方式二：当Step Into进入汇编代码后，会弹出源码关联的提示，请点击**Select file**，选择本地对应C++源码进行关联。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/3ieDflhwReWs1bUWrSEjcw/zh-cn_image_0000002779566666.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=A1B0472F53123BD69BF0E458F49ACAC179F440F71A993E3CDBCB8CB2443A18FA)

### ArkTS代码调试

假如在工程A（HAR包工程）中以debug模式编译得到字节码HAR包，工程B（主工程）中引用该字节码HAR包，并且本地有HAR包的源码，要调试该字节码HAR，有两种方式：在主工程中调试或在HAR包工程中调试。

**说明** 

release模式编译的字节码HAR不支持调试。

* **方式一：在主工程中调试。**
  1. 在主工程中导入字节码HAR对应的模块，确保模块的层级目录与HAR包工程的保持一致，例如HAR模块都在工程根目录下。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/ZEp-EJJfSgCvFCDi2bKW_A/zh-cn_image_0000002779406694.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=5EC1BA3BDE733FFD3FD75E3685DB61F06A40C1746C6225CBB434ED7B928246CB)
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

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/alFOROc1T4qfhwseD5-pEQ/zh-cn_image_0000002779406688.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=25F2C0F0B7F75929187F0E450E628648460EEC7EABF848799CB97D6902954861)
  5. 主工程应用在设备上运行起来后，在HAR包工程中通过attach方式对该应用进行调试，在Debug窗口获取程序加载时的前缀，记录为remoteUrl，例如以下的entry|@ohos/test\_stage\_ets\_library|1.0.0。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/b1jl2c40Q_2WLjDq4nUNPA/zh-cn_image_0000002779566670.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=C9983BFD570706005A359007C75EDE271DC73F53FE43AF6742CEB026128A9719)
  6. 点击**Run > Edit Configurations > Debugger** **> ArkTS Source Pairs**，点击**+**，填写前两个步骤获取到的**remoteUrl**和**localUrl**。
     + remoteUrl：应用程序加载HAR包的前缀路径。
     + localUrl：本地生成sourceMap中HAR的前缀路径。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/CLtk8GDNQGGWwJk1BwaXYQ/zh-cn_image_0000002808766259.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=77EF3803079D2C2BA86A1F86D4B0C8ED5DB81FC8D336459197162809D3650FE1)
  7. 在HAR包工程中重新通过attach方式对主工程应用进行调试，此时可以在HAR模块上添加断点进行调试。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/2-i5ROm2Q-O9frFnR_ubfg/zh-cn_image_0000002779406692.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=88E4A0C0E65B6FC4E7EC829C5F6EB92B456E7630D033F6894F41E79ABF772093)

  **说明** 

  如果在HAR包工程中同时配置[Symbol Directories](ide-source-code-debugging.md#section177418333199)和ArkTS Source Pairs，可同时attach调试ArkTS和C++断点。

## 源码HAR调试

### C++代码调试

如果HAP/HSP引用源码HAR包，同时HAR包中包含C++代码，可参考[字节码HAR](ide-source-code-debugging.md#section177418333199)进行调试。

### ArkTS代码调试

工程中引用源码HAR包，对该HAR包进行调试，根据本地是否有源码，调试方式分别如下：

* 如果HAR包在本地没有对应源码，此时应用构建打包时引用的源码来源是工程级oh\_modules目录下的源码，只能针对oh\_modules下的源码进行调试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/lHwjAE_pTxOa7Hdf092tSQ/zh-cn_image_0000002808766253.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=76B4CEF13CD08ACB444B68A013D097C64D2CD64D54EB9E8B95318880512AB278)
* 如果HAR包在本地有对应源码，调试时可关联本地源码以实现对源码的调试，有两种方式。
  + 方式一：参考[字节码HAR调试](ide-source-code-debugging.md#section1035165781918)。
  + 方式二：当Step Into进入oh\_modules中的ets代码后，会弹出源码关联的提示时，请点击**Choose Sources**，选择本地对应ets源码进行关联。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/e51G8QQWQ4uh4DV1CIPpBA/zh-cn_image_0000002808886339.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=7E2601008CC68FE691E603FF93472BE72F9D5734ACB90B9C27217EB2F8697A2D)

## HSP源码调试

如果要调试HSP源码，需要将源码置于本地工程模块下，参考[字节码HAR的方式一](ide-source-code-debugging.md#li17359570194)进行调试。
