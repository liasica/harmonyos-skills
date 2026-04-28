---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-16
title: 如何获取Native侧printf等方法打印的信息
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何获取Native侧printf等方法打印的信息
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:31+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:85813e88bf92dda35f410631267fa169340af36e82ace30ce2e2dbffb0029681
---

**问题详情**

Native侧引用的三方库使用printf等方法打印到stdout、stderr的信息怎么获取？在三方库代码里有许多fprintf, std::cout printf 的标准日志打印log，在程序开发中无法查看这些日志。

**解决措施**

cout/printf是语言提供的打印函数，并不能填充到hilog日志中。可通过重定向的方法将日志打印到文件来获取打印信息。具体方法如下：

Native侧重定向方法主体。

```
1. #include "napi/native_api.h"
2. #include <hilog/log.h>
3. #include <string>
4. #include "iostream"
5. #include "fstream"
6. #define LOG_TAG "Pure"

8. static napi_value Redirect(napi_env env, napi_callback_info info) {
9. // Get the JS parameters of the function
10. size_t argc = 1;
11. napi_value argv[1] = {nullptr};
12. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
13. // Resolve parameter 1, the destination directory for saving the file
14. size_t targetDirectoryNameSize;
15. char targetDirectoryNameBuf[512];
16. napi_get_value_string_utf8(env, argv[0], targetDirectoryNameBuf, sizeof(targetDirectoryNameBuf),
17. &targetDirectoryNameSize);
18. std::string targetDirectoryName(targetDirectoryNameBuf, targetDirectoryNameSize); // target directory
19. OH_LOG_INFO(LOG_APP, "C++Received target path on the side === %{public}s", targetDirectoryNameBuf);
20. std::string targetSandboxPath = targetDirectoryName + "/Log.log"; // Saved file path

22. // Use the freopen function to associate files with standard output
23. FILE *stdoutFile = NULL;
24. FILE *stderrFile = NULL;
25. stdoutFile = freopen(targetSandboxPath.c_str(), "a", stdout);
26. stderrFile = freopen(targetSandboxPath.c_str(), "a", stderr);
27. if (NULL == stdoutFile || NULL == stderrFile) {
28. OH_LOG_INFO(LOG_APP, "Recreate！");
29. // Opening the file output stream of the sandbox file will create a file
30. std::ofstream outputFile(targetSandboxPath, std::ios::binary);
31. if (!outputFile) {
32. OH_LOG_ERROR(LOG_APP, "Unable to create target file!");
33. return nullptr;
34. }
35. stdoutFile = freopen(targetSandboxPath.c_str(), "a", stdout);
36. stderrFile = freopen(targetSandboxPath.c_str(), "a", stderr);
37. if (NULL == stdoutFile || NULL == stderrFile) {
38. OH_LOG_ERROR(LOG_APP, "fail!");
39. return nullptr;
40. }
41. }
42. OH_LOG_WARN(LOG_APP, "redirect!");
43. printf("\n*****************Redirect dividing line*****************\n");
44. return 0;
45. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/LogRedirect/src/main/cpp/napi_init.cpp#L20-L64)

在ArkTS侧调用并传入路径信息。

在EntryAbility的onCreate()方法中调用重定向。

```
1. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
2. let file : string = this.context.getApplicationContext().filesDir;
3. testNapi.redirect(file);
4. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
5. }
```

[LogRedirectAbility.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/LogRedirect/src/main/ets/logredirectability/LogRedirectAbility.ets#L29-L33)
