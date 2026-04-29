---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-4
title: ArkTS侧与Native侧分别如何动态加载SO库
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > ArkTS侧与Native侧分别如何动态加载SO库
category: harmonyos-faqs
scraped_at: 2026-04-29T14:15:45+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ec57def241a238891813f86840abc6efabc7da742fffe3469f5c702bbe545ef2
---

**解决措施**

1.ArkTS 可以通过动态 import 加载 so 库。

2.Native侧可以使用dlopen动态加载so库。

参考代码如下：

1.ArkTS 通过动态 import 加载 so 库。添加异步函数，在异步函数中通过let testNapi = await import ("libentry.so")实现动态加载so库。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. // import testNapi from 'libentry.so';

4. @Entry
5. @Component
6. struct LoadSoLibrary {
7. @State message: string = 'Hello World';

9. build() {
10. Row() {
11. Column() {
12. Text(this.message)
13. .fontSize(50)
14. .fontWeight(FontWeight.Bold)
15. .onClick(async() => {
16. let testNapi = await import("libentry.so")            // Load so library
17. hilog.info(0x0000, 'testTag', 'Test NAPI 2 + 3 = %{public}d', testNapi.default.add(2, 3));   // Call library functions by default
18. // hilog.info(0x0000, 'testTag', 'Test NAPI 2 + 3 = %{public}d', testNapi.add(2, 3));
19. })
20. }
21. .width('100%')
22. }
23. .height('100%')
24. }
25. }
```

[ImportSo.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/entry/src/main/ets/pages/ImportSo.ets#L5-L29)

2.Native侧使用dlopen动态加载so库。

需要调用liba.so中的add函数。

* 将liba.so文件放到libs/arm64-v8a/路径下。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/c9w0YwKZTo-rNVdtzDN2Yw/zh-cn_image_0000002229603757.png?HW-CC-KV=V1&HW-CC-Date=20260429T061544Z&HW-CC-Expire=86400&HW-CC-Sign=847A3D79197FEBE07832CF013B9EB8ABEEB0BF4B998BADF1A38F2390C403302E "点击放大")
* 需要在ArkTS侧传递so库路径信息到Native侧。

  ```
  1. import { hilog } from '@kit.PerformanceAnalysisKit';
  2. import testNapi from 'libentry.so';

  4. @Entry
  5. @Component
  6. struct Index {
  7. @State message: string = 'Hello World';

  9. build() {
  10. Row() {
  11. Column() {
  12. Text(this.message)
  13. .fontSize(50)
  14. .fontWeight(FontWeight.Bold)
  15. .onClick(() => {
  16. let path = this.getUIContext().getHostContext()!.bundleCodeDir;     // Get project path
  17. hilog.info(0x0000, 'testTag', 'Test NAPI 2 + 3 = %{public}d', testNapi.addByLibPath(2, 3, path + '/libs/arm64/liba.so'));   // Transfer parameter path information to the native side
  18. })
  19. }
  20. .width('100%')
  21. }
  22. .height('100%')
  23. }
  24. }
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/dynamicallyload/src/main/ets/pages/Index.ets#L5-L28)
* 在Native侧通过dlopen函数动态加载so库。

  ```
  1. #include "napi/native_api.h"
  2. #include <dlfcn.h>
  3. typedef double (*FUNC_ADD)(int, int);
  4. static napi_value AddByLibPath(napi_env env, napi_callback_info info) {
  5. size_t requireArgc = 3;
  6. size_t argc = 3;
  7. napi_value args[3] = {nullptr};
  8. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
  9. double value0;
  10. napi_get_value_double(env, args[0], &value0);
  11. double value1;
  12. napi_get_value_double(env, args[1], &value1);
  13. char path[255];
  14. size_t size = 255;
  15. napi_get_value_string_utf8(env, args[2], path, 255, &size); // Obtain dynamic library path information
  16. void *handle = dlopen(path, RTLD_LAZY);                     // Open a dynamic link library, The path is "path".
  17. dlerror();
  18. FUNC_ADD add_func = (FUNC_ADD)dlsym(handle, "add"); // Retrieve the function named "add"
  19. if (dlerror()) {
  20. return nullptr;
  21. }
  22. double res = add_func(value0, value1);              // Call add and pass the parameter information
  23. dlclose(handle);                                    // Close the dynamic library
  24. napi_value sum;
  25. napi_create_double(env, res, &sum);
  26. return sum;
  27. }
  28. // ...
  ```

  [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/dynamicallyload/src/main/cpp/napi_init.cpp#L5-L32)
