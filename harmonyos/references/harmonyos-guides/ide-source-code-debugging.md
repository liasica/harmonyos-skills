---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-source-code-debugging
title: 三方库源码调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > 三方库源码调试
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:30+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:b545f5da21b4885136be8f7cff348ed7978bb692cece647b78f8e4ab9daafaa0
---

三方共享包分为静态共享包HAR和动态共享包HSP，两种共享包的源码调试方式有所区别，具体请查看以下指导。

## 区分字节码HAR和源码HAR

HAR包分为字节码HAR和源码HAR，同时满足以下两个条件的是字节码HAR，否则是源码HAR，更多关于如何构建源码HAR和字节码HAR的指导请查看[构建HAR](ide-hvigor-build-har.md)。

1. 查看HAR包的ets目录下存在.abc文件。
2. 查看HAR包的oh-package.json5文件，存在byteCodeHar字段并且值为true。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/niMs2Q0JTvGnqOzDAjB9jg/zh-cn_image_0000002808886335.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=F5FEFC3F3D77F974026F440F7D1D19FD1E8BEB6507083616F5A2CC111E73939B)

## 字节码HAR调试

### C++代码调试

如果HAP/HSP引用字节码HAR包，同时HAR包中包含C++代码，参考以下步骤对该HAR包进行调试。

1. 点击**Run > Edit Configurations > Debugger** **>** **Symbol Directories**页签，点击**+**，添加带调试信息的so文件，so文件在{ProjectPath}/{ModuleName}/build/{product}/intermediates/libs/default/arm64-v8a路径下。

   **说明** 

   在工程级或模块级build-profile.json5中添加strip字段并设置为false，可以生成带调试信息的so文件，具体请参考[配置CPP](ide-hvigor-cpp.md#section2182144382320)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/-hgzxR64Tvi-NimmGg_FQQ/zh-cn_image_0000002808766255.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=6CA7427498BADDDF8C09336CDCD9F08623E866C431C32F40BDF23E1826F4D9AE)
2. DevEco Studio调试应用时会优先加载配置的so文件，本地so文件包含调试信息时，可以正常调试源码。由于so的源码文件信息为编译时的文件路径，若与本地的源码文件路径不一致时，需要关联源码文件，有两种方式：
   * 方式一：可以在**LLDB Startup Commands**页签中添加命令做映射，示例如下。

     ```bash
     settings set -- target.source-map {old-path} {new-path}
     ```

     + old-path：编译时的文件路径。
     + new-path：本地的源码文件路径。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/1IS6TQ-eTpiMV0U1RSzTbA/zh-cn_image_0000002779566680.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=77CA94DD79C73A8F405F3094224F64B18F40D45A86B255822ABAF5B08D7F5601)
   * 方式二：当Step Into进入汇编代码后，会弹出源码关联的提示，请点击**Select file**，选择本地对应C++源码进行关联。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/DwGCEyncTOK1mWPWBQeIlg/zh-cn_image_0000002779566666.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=BADC8DBEB42B1A0F49762FAEF601A5FF0E7A1FA220D35C87EBEE141E01733090)

### ArkTS代码调试

假如在工程A（HAR包工程）中以debug模式编译得到字节码HAR包，工程B（主工程）中引用该字节码HAR包，并且本地有HAR包的源码，要调试该字节码HAR，有两种方式：在主工程中调试或在HAR包工程中调试。

**说明** 

release模式编译的字节码HAR不支持调试。

* **方式一：在主工程中调试。**
  1. 在主工程中导入字节码HAR对应的模块，确保模块的层级目录与HAR包工程的保持一致，例如HAR模块都在工程根目录下。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/W1AwdTorSbiidwySvoR7hA/zh-cn_image_0000002779406694.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=7FAB25E72DD43F6D6D9527ADFD372445F0A9A1DA1259FD00A9BF75A3D61C37F9)
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

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/SI7sGJKESmmOKgQWsq7cVA/zh-cn_image_0000002779406688.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=0AC102B25AA06E232D9DB1A02ECB90394220F655099A7A557CCA8A31F0D4C9E6)
  5. 主工程应用在设备上运行起来后，在HAR包工程中通过attach方式对该应用进行调试，在Debug窗口获取程序加载时的前缀，记录为remoteUrl，例如以下的entry|@ohos/test\_stage\_ets\_library|1.0.0。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/bOv4WKfCTPyumdKEEG8uTw/zh-cn_image_0000002779566670.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=5F51974CDA44F178EAA8F7FC86A6D4ACAB4C439E626674DBBC4B402CFB21F08A)
  6. 点击**Run > Edit Configurations > Debugger** **> ArkTS Source Pairs**，点击**+**，填写前两个步骤获取到的**remoteUrl**和**localUrl**。
     + remoteUrl：应用程序加载HAR包的前缀路径。
     + localUrl：本地生成sourceMap中HAR的前缀路径。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/KZ9CjRhKQAiNR4VhQcBEWQ/zh-cn_image_0000002808766259.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=199E468D8DFDC554A712FFABE416049353191D7C5A20566192942B458BEAABF2)
  7. 在HAR包工程中重新通过attach方式对主工程应用进行调试，此时可以在HAR模块上添加断点进行调试。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/XDDXS_MFSXC_l2792u_0Bw/zh-cn_image_0000002779406692.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=674E7D9529C99F706163099ECECE5467775E712DA64E8D49CC4E1413450D1EA1)

  **说明** 

  如果在HAR包工程中同时配置[Symbol Directories](ide-source-code-debugging.md#section177418333199)和ArkTS Source Pairs，可同时attach调试ArkTS和C++断点。

## 源码HAR调试

### C++代码调试

如果HAP/HSP引用源码HAR包，同时HAR包中包含C++代码，可参考[字节码HAR](ide-source-code-debugging.md#section177418333199)进行调试。

### ArkTS代码调试

工程中引用源码HAR包，对该HAR包进行调试，根据本地是否有源码，调试方式分别如下：

* 如果HAR包在本地没有对应源码，此时应用构建打包时引用的源码来源是工程级oh\_modules目录下的源码，只能针对oh\_modules下的源码进行调试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/iCs-R4D7SUytINWpOQCJCQ/zh-cn_image_0000002808766253.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=AF6632BB3F9ACE9EFB63467E72DDDC5016BD64B95C2C8F83246812A3C00B340D)
* 如果HAR包在本地有对应源码，调试时可关联本地源码以实现对源码的调试，有两种方式。
  + 方式一：参考[字节码HAR调试](ide-source-code-debugging.md#section1035165781918)。
  + 方式二：当Step Into进入oh\_modules中的ets代码后，会弹出源码关联的提示时，请点击**Choose Sources**，选择本地对应ets源码进行关联。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/YLv0rpqkTMKvs1h_xuAZvg/zh-cn_image_0000002808886339.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=BA9C0D12A65F6BF34A0D034D808A680B0B35216CE41E4DE4AF72AEEC68F21405)

## HSP源码调试

如果要调试HSP源码，需要将源码置于本地工程模块下，参考[字节码HAR的方式一](ide-source-code-debugging.md#li17359570194)进行调试。
