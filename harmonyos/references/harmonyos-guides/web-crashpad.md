---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-crashpad
title: 使用Crashpad收集Web组件崩溃信息
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > Web调试维测 > 使用Crashpad收集Web组件崩溃信息
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:08+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:320c4b30dc35a7013ef4e997392949310e467919357af1878394d2b8ed0dd4d5
---

Web组件支持使用Crashpad记录进程崩溃信息。Crashpad是Chromium内核提供的进程崩溃信息处理工具，在应用使用Web组件导致的进程（Web渲染进程）崩溃出现后，Crashpad会在应用主进程沙箱目录写入dmp文件。该文件为二进制格式，后缀为dmp，其记录了进程崩溃的原因、线程信息、寄存器信息等，应用可以使用该文件分析Web组件相关进程崩溃问题。Web组件分别从API version 9和API version 12开始支持接口onRenderExited和onRenderProcessNotResponding，开发者可以分别通过Web接口[onRenderExited](../harmonyos-references/arkts-basic-components-web-events.md#onrenderexited9)和[onRenderProcessNotResponding](../harmonyos-references/arkts-basic-components-web-events.md#onrenderprocessnotresponding12)来检测渲染进程退出和渲染进程不响应，也可以在这些接口中增加应用处理的逻辑。

使用步骤如下：

1. 在应用使用Web组件导致的进程崩溃出现后，Crashpad收到信号，对应Hilog日志（节选部分）如下

```
1. pid-30069             I     [crashpad_ohos.cc:254] crashpad SandboxedHandler::HandleCrash, received signo = 6
2. pid-30069             I     [crashpad_ohos.cc:182] crashpad SandboxedHandler::HandleCrashNonFatal, connect to handler successfully, need to request dump
3. ...
4. arkweb_cr..._handler  I     [crash_report_database.cc:91] crash dmp path : /data/storage/el2/log/crashpad/new/xxx.dmp
```

这时Crashpad开始请求dump，成功之后，会在应用主进程沙箱目录下产生对应的dmp文件，对应的沙箱路径如下：

```
1. /data/storage/el2/log/crashpad
```

1. 参考[Native访问应用沙箱](../best-practices/bpta-file-native-side.md)实现访问应用沙箱dmp文件；也可将存放dmp文件的沙箱路径的文件复制到可以查看的路径。示例如下

```
1. import { fileIo as fs } from '@kit.CoreFileKit'
2. import { BusinessError } from '@kit.BasicServicesKit'
3. import { webview } from '@kit.ArkWeb'

5. @Entry
6. @Component
7. struct Index {
8. controller: webview.WebviewController = new webview.WebviewController();
9. uiContext: UIContext = this.getUIContext();
10. build() {
11. RelativeContainer() {
12. Web({src:'chrome://memory-exhaust/', controller:this.controller})
13. Button('file')
14. .onClick(() => {
15. let pathDir = this.uiContext.getHostContext()?.filesDir;
16. console.info("pathdir=" + pathDir);
17. fs.copyDir("/data/storage/el2/log/crashpad/pending/", pathDir, 0)
18. .then(()=>{
19. console.info("copy files success");
20. })
21. .catch((err: BusinessError)=>{
22. console.error("copy failed with error message: " + err.message + ", error code: " + err.code);
23. })
24. })
25. }
26. .height('100%')
27. .width('100%')
28. }
29. }
```

以上示例将所有的dmp文件都复制到可查看的沙箱路径中，也可以搜索Hilog日志“.dmp”得到dmp文件名，这样就可以将某个dmp文件复制到另一个沙箱路径下了，具体的路径为

```
1. /data/app/el2/100/base/com.example.myapplication/haps/entry/files/
```

这个路径可以利用DevEco Studio查看。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/HGrqbmXhS22a6a27mkC5WA/zh-cn_image_0000002583478255.png?HW-CC-KV=V1&HW-CC-Date=20260427T234106Z&HW-CC-Expire=86400&HW-CC-Sign=033E75B75D39747E044F5583FC542AC8F7B54F2389F8C8BD1C7FD5F68AE8F3D4)

1. 获取dmp文件后进行解析，具体步骤如下：

   * 通过minidump\_stackwalk工具解析dmp文件，可以得到上述dmp文件对应的进程崩溃信息（崩溃的原因、线程信息、寄存器信息等），示例如下（Linux环境）：

     ```
     1. ./minidump_stackwalk b678e0b5-894b-4794-9ab3-fb5d6dda06a3.dmp > parsed_stacktrace.txt
     ```

     minidump\_stackwalk由Breakpad项目源码编译得到，编译方法见项目仓库：[Breakpad仓库地址](https://chromium.googlesource.com/breakpad/breakpad)。
   * 查看解析后的文件，以下示例列出部分内容：

     ```
     1. Crash reason:  SIGSEGV /SEGV_MAPERR    表示导致进程crash的信号，此处示例为段错误
     2. Crash address: 0x0
     3. Process uptime: 12 seconds

     5. Thread 0 (crashed)                     表示Thread 0发生crash
     6. 0  libweb_engine.so + 0x2e0b340       0层调用栈，0x2e0b340为so偏移地址，可用来反编译解析crash源码（依赖unstripped so）
     7. x0 = 0x00000006a5719ff8    x1 = 0x000000019a5a28c0
     8. x2 = 0x0000000000020441    x3 = 0x00000000000001b6
     9. x4 = 0x0000000000000018    x5 = 0x0000000000008065
     10. x6 = 0x0000000000008065    x7 = 0x63ff686067666d60
     11. x8 = 0x0000000000000000    x9 = 0x5f129cf9e7bf008c
     12. x10 = 0x0000000000000001   x11 = 0x0000000000000000
     13. x12 = 0x000000069bfcc6d8   x13 = 0x0000000009a1746e
     14. x14 = 0x0000000000000000   x15 = 0x0000000000000000
     15. x16 = 0x0000000690df4850   x17 = 0x000000010c0d47f8
     16. x18 = 0x0000000000000000   x19 = 0x0000005eea827db8
     17. x20 = 0x0000005eea827c38   x21 = 0x00000006a56b1000
     18. x22 = 0x00000006a8b85020   x23 = 0x00000020002103c0
     19. x24 = 0x00000006a56b8a70   x25 = 0x0000000000000000
     20. x26 = 0x00000006a8b84e00   x27 = 0x0000000000000001
     21. x28 = 0x0000000000000000    fp = 0x0000005eea827c10
     22. lr = 0x000000069fa4b33c    sp = 0x0000005eea827c10
     23. pc = 0x000000069fa4b340
     24. Found by: given as instruction pointer in context
     25. 1  libweb_engine.so + 0x2e0b338
     26. fp = 0x0000005eea827d80    lr = 0x000000069fa48d44
     27. sp = 0x0000005eea827c20    pc = 0x000000069fa4b33c
     28. Found by: previous frame's frame pointer
     29. 2  libweb_engine.so + 0x2e08d40
     30. fp = 0x0000005eea827e50    lr = 0x00000006a385cef8
     31. sp = 0x0000005eea827d90    pc = 0x000000069fa48d44
     32. Found by: previous frame's frame pointer
     33. 3  libweb_engine.so + 0x6c1cef4
     34. fp = 0x0000005eea828260    lr = 0x00000006a0f11298
     35. sp = 0x0000005eea827e60    pc = 0x00000006a385cef8
     36. ......
     ```
   * 使用LLVM工具链解析崩溃源码位置，需要注意的是，要解析的so文件必须是带有符号表的so文件，如果栈显示和web的so相关，开发者可以在社区提issue或IR单。示例如下（Linux环境）：

     ```
     1. ./llvm-addr2line -Cfpie libweb_engine.so 0x2e0b340
     ```

     llvm-addr2line工具链位于SDK中。
