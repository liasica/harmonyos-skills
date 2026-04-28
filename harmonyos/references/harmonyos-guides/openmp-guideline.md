---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/openmp-guideline
title: OpenMP应用构建和运行指南
breadcrumb: 指南 > NDK开发 > 代码开发 > OpenMP支持 > OpenMP应用构建和运行指南
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:29+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:17f33184a78ca7e719f41d07db6cb3b73c6d3728b67d6ce18c2cc7be3c2c26c1
---

HarmonyOS NDK中提供了OpenMP的动态库和静态库文件，支持开发者在Native应用中使用OpenMP。本文用于指导开发者在[DevEco Studio](https://developer.huawei.com/consumer/cn/deveco-studio/)中调用库文件使用OpenMP的并行化能力，更详细的使用示例和API标准请查看官方文档[clang-OpenMPSupport](https://clang.llvm.org/docs/OpenMPSupport.html)。

## 开发步骤

### 创建Native C++工程

[创建NDK工程](create-with-ndk.md)

### 添加依赖

OpenMP库的引入可以通过静态链接和动态链接两种方式实现。

注意

[OMPT(OpenMP Tools Interface)](https://www.openmp.org/spec-html/5.0/openmpsu15.html#x25-240001.5.1)工具目前仅支持静态链接时使用。

**静态链接**

（1）打开entry/src/main/cpp/CMakeLists.txt，在target\_link\_libraries依赖中添加静态库libomp.a以及日志依赖libhilog\_ndk.z.so。

```
1. target_link_libraries(entry PUBLIC libomp.a libace_napi.z.so libhilog_ndk.z.so)
```

（2）打开entry/build-profile.json5，在buildOption->externalNativeOptions->cppFlags下添加编译参数"-static-openmp -fopenmp"。

```
1. "buildOption": {
2. "externalNativeOptions": {
3. "path": "./src/main/cpp/CMakeLists.txt",
4. "arguments": "",
5. "cppFlags": "-static-openmp -fopenmp",
6. }
7. }
```

**动态链接**

（1）打开entry/src/main/cpp/CMakeLists.txt，在target\_link\_libraries依赖中添加动态库libomp.so以及日志依赖libhilog\_ndk.z.so。

```
1. target_link_libraries(entry PUBLIC libomp.so libace_napi.z.so libhilog_ndk.z.so)
```

（2）打开entry/build-profile.json5，在buildOption->externalNativeOptions->cppFlags下添加编译参数"-fopenmp"。

```
1. "buildOption": {
2. "externalNativeOptions": {
3. "path": "./src/main/cpp/CMakeLists.txt",
4. "arguments": "",
5. "cppFlags": "-fopenmp",
6. }
7. }
```

（3）打开Sdk安装目录，在“{Sdk安装目录}{版本号}\HarmonyOS\native\llvm\lib\aarch64-linux-ohos”目录下找到libomp.so动态库文件，并将其拷贝到工程目录entry/libs/arm64-v8a文件夹。

### 修改源文件

（1）修改entry/src/main/cpp/napi\_init.cpp，引入omp.h头文件，并添加OmpTest函数。

```
1. #include "napi/native_api.h"
2. #include "omp.h"
3. #include "hilog/log.h"

5. #undef LOG_DOMAIN
6. #undef LOG_TAG
7. #define LOG_DOMAIN 0x3200 // 全局domain宏，标识业务领域
8. #define LOG_TAG "MY_TAG"  // 全局tag宏，标识模块日志tag

10. static napi_value OmpTest(napi_env env, napi_callback_info info)
11. {

13. OH_LOG_INFO(LOG_APP, "=================Hello OpenMP test.====================");
14. #pragma omp parallel
15. {
16. OH_LOG_INFO(LOG_APP, "Hello OpenMP!");
17. }
18. return nullptr;
19. }

21. EXTERN_C_START
22. static napi_value Init(napi_env env, napi_value exports)
23. {
24. napi_property_descriptor desc[] = {
25. { "ompTest", nullptr, OmpTest, nullptr, nullptr, nullptr, napi_default, nullptr }
26. };
27. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
28. return exports;
29. }
30. EXTERN_C_END

32. static napi_module demoModule = {
33. .nm_version = 1,
34. .nm_flags = 0,
35. .nm_filename = nullptr,
36. .nm_register_func = Init,
37. .nm_modname = "entry",
38. .nm_priv = ((void*)0),
39. .reserved = { 0 },
40. };

42. extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
43. {
44. napi_module_register(&demoModule);
45. }
```

（2）修改entry/src/main/cpp/types/libentry/Index.d.ts，导出ompTest函数。

```
1. export const ompTest: () => null;
```

（3）Ts侧调用，修改entry/src/main/ets/pages/Index.ets，调用ompTest函数。

```
1. import testNapi from 'libentry.so';

3. @Entry
4. @Component
5. struct Index {
6. @State message: string = 'Hello OpenMP';

8. build() {
9. Row() {
10. Column() {
11. Text(this.message)
12. .fontSize(50)
13. .fontWeight(FontWeight.Bold)
14. .onClick(() => {
15. testNapi.ompTest();
16. })
17. }
18. .width('100%')
19. }
20. .height('100%')
21. }
22. }
```

### 运行并校验结果

运行前请检查设备连接并配置好[Signature](../harmonyos-guides-V5/ide-signing-V5.md)信息。直接点击右上角运行按钮，应用启动后设备进入“Hello OpenMP”界面，点击“Hello OpenMP”标签，打开DevEco Studio下方“Log”查看页面，即可看到并行打印的“Hello OpenMP！”消息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/yQRfdWX4TNG1_ou87J4_vQ/zh-cn_image_0000002552959386.png?HW-CC-KV=V1&HW-CC-Date=20260427T235428Z&HW-CC-Expire=86400&HW-CC-Sign=DA678F30AE5F9CCF97853B4CAEA57069A4C40AC90E8A9596F951F3A203629373)

注意

OpenMP程序运行时，HiLog中会输出“dlopen\_impl load library header failed for libarcher.so”的报错信息（如下图）。该报错信息中提到的libarcher.so，在OpenMP程序开启Tsan检测时才需要使用。目前HarmonyOS未支持OpenMP程序的Tsan检测能力，因此该错误信息可忽略，不影响程序正常运行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/vvetcES0RGWfxRcmw-CtnA/zh-cn_image_0000002583479387.png?HW-CC-KV=V1&HW-CC-Date=20260427T235428Z&HW-CC-Expire=86400&HW-CC-Sign=835BC3B3207058FF8DFF6EDC9FB3506B681E5B7C5AADAE1B8C0D34E9BA255E2B)
