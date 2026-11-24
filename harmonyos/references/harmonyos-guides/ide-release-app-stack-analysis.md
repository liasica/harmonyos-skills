---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-release-app-stack-analysis
title: 堆栈轨迹分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > 堆栈轨迹分析
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:31+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:18650ef8eb647a82190f67760141c19cbd3f83b9bc3101658ba1f456c9fcbb28
---

对于发布的应用（Release应用），为减小应用程序大小，提高运行效率，会对代码进行优化，去除其中的调试信息。因此无法直接通过Release应用的堆栈信息定位到源码的具体文件和行位置，不易于开发者快速定位解决问题。

针对该场景，DevEco Studio提供了Release应用堆栈解析功能，开发者可以利用构建产物中包含调试信息的文件（so文件、sourceMap文件、nameCache文件等），对Release应用中C++堆栈、ArkTS堆栈以及ArkTS堆栈中混淆的方法名和文件名进行还原。关于构建产物的介绍和堆栈解析的原理，请查看[异常堆栈解析原理](ide-exception-stack-parsing-principle.md)。

Release应用堆栈解析功能操作方法如下：

1. 单击菜单栏**Code > Analyze Stack Trace**，或在FaultLog页面异常堆栈信息处右键选择**Analyze Stack Trace。**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/C6ItxZ-2QUe1OZM4iCLuOg/zh-cn_image_0000002808766007.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=536DC3F600528CC146D38E199975CFF196637D13716A4E4F97E0EABC7FF763BC)
2. 在弹出的**Analyze Stack Trace**对话框中，粘贴Release应用的异常堆栈信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/JBnxoUzFTs-Wuh4s-S7Z3g/zh-cn_image_0000002779406450.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=671D6260C360904970F77A61B011F2B0B40128448E83AA1140BD2B08845CA0A1)
3. 如果当前工程为堆栈所在应用对应的工程，且存在Release构建产物，点击**Start Analyze**即可进行解析。

   如果当前工程不是堆栈所在应用对应的工程，则需要配置应用对应构建产物：勾选**Unscramble stack trace**, 在下方的文件选择框中，分别添加应用对应的sourceMap文件、so文件以及nameCache文件，点击**Start Analyze**进行转换。

   DevEco Studio将解析后的堆栈信息显示在右侧的输出框中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/rnXe6T-QS66unAFxtM4AbA/zh-cn_image_0000002779566426.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=4F6A8C38BC58C8A8C1B49E5A22D357D7C37BCB648676A2FC444B934AEF572B7B)

   在构建Release应用时，so文件是默认不包含符号表信息的，如果需要在构建Release应用时生成包含符号表的so文件，需要在工程的[模块级build-profile.json5](ide-hvigor-cpp.md)文件的buildOption属性中，配置如下信息：

   ```json5
   "buildOption": {
     "externalNativeOptions": {
       "arguments": "-DCMAKE_BUILD_TYPE=RelWithDebInfo"
     }
   }
   ```

   如果引用Release har包中Native方法产生了异常堆栈，解析时请勾选**Unscramble stack trace**, 并选择har模块中编译出的带有符号信息的so文件，引用方build产物中的har模块so不带有符号信息。so文件在模块中相对路径为build/default/intermediates/libs/default/{cpu类型}/libxxx.so。
