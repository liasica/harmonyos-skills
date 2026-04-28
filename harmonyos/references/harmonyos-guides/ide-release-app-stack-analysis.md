---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-release-app-stack-analysis
title: 堆栈轨迹分析
breadcrumb: 指南 > 编写与调试应用 > 日志与故障分析 > 故障分析 > 堆栈轨迹分析
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6b8f8602f83e4f63abe1f2a0049075b8824806bc43ac12704b8922ff995dc766
---

对于发布的应用（Release应用），为减小应用程序大小，提高运行效率，会对代码进行优化，去除其中的debug信息。因此无法直接通过Release应用的堆栈信息定位到源码的具体文件和行位置，不易于开发者快速定位解决问题。

针对该场景，DevEco Studio提供了Release应用堆栈解析功能，开发者可以利用构建产物中包含Debug信息的文件（so文件、sourceMap文件、nameCache文件等），对Release应用中C++堆栈、ArkTS堆栈以及ArkTS堆栈中混淆的方法名和文件名进行还原。关于构建产物的介绍和堆栈解析的原理，请查看[异常堆栈解析原理](ide-exception-stack-parsing-principle.md)。

Release应用堆栈解析功能操作方法如下：

1. 单击菜单栏**Code > Analyze Stack Trace**，或在FaultLog页面异常堆栈信息处右键选择**Analyze Stack Trace。**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/ONfdkVhUTt6IqnZrdmqBMw/zh-cn_image_0000002530912690.png?HW-CC-KV=V1&HW-CC-Date=20260427T235657Z&HW-CC-Expire=86400&HW-CC-Sign=7C527133A9E48684A2B7CB4AAD67BB7BEA0A9A6F976584B988EB5C5182E1DD66)
2. 在弹出的**Analyze Stack Trace**对话框中，粘贴Release应用的异常堆栈信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/oTnanXwsQF2WKajoY-AhRw/zh-cn_image_0000002530912692.png?HW-CC-KV=V1&HW-CC-Date=20260427T235657Z&HW-CC-Expire=86400&HW-CC-Sign=432F9B4AA0659985FF6B713DD6CF4B7F8476A09F5342CD17AD89A037DD0087EB)
3. 如果当前工程为堆栈所在应用对应的工程，且存在Release构建产物，点击**Start Analyze**即可进行解析。

   如果当前工程不是堆栈所在应用对应的工程，则需要配置应用对应构建产物：勾选**Unscramble stack trace**, 在下方的文件选择框中，分别添加应用对应的sourceMap文件、so文件以及nameCache文件，点击**Start Analyze**进行转换。

   DevEco Studio将解析后的堆栈信息显示在右侧的输出框中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/vWmjVcqbTu24_PAVJhtlMg/zh-cn_image_0000002561832613.png?HW-CC-KV=V1&HW-CC-Date=20260427T235657Z&HW-CC-Expire=86400&HW-CC-Sign=C967D4C466758F09C313047F0A4D74A3E6267F0C39BF3EC9D8A0181674FAAEBA)

   在构建Release应用时，so文件是默认不包含符号表信息的，如果需要在构建Release应用时生成包含符号表的so文件，需要在工程的[模块级build-profile.json5](ide-hvigor-cpp.md)文件的buildOption属性中，配置如下信息：

   ```
   1. "buildOption": {
   2. "externalNativeOptions": {
   3. "arguments": "-DCMAKE_BUILD_TYPE=RelWithDebInfo"
   4. }
   5. }
   ```

   如果引用release Har包中native方法产生了异常堆栈，解析时请勾选**Unscramble stack trace**, 并选择har模块中编译出的带有符号信息的so文件，引用方build产物中的har模块so不带有符号信息。so文件在模块中相对路径为build/default/intermediates/libs/default/{cpu类型}/libxxx.so。
