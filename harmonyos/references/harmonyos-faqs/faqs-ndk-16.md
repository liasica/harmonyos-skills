---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-16
title: 如何获取Native侧printf等方法打印的信息
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何获取Native侧printf等方法打印的信息
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e889ccb6e08a53e761baf18a99489f8b4fcafd78293988f0b7b6edf7076b47cb
---

**问题详情**

Native侧引用的三方库使用printf等方法打印到stdout、stderr的信息怎么获取？在三方库代码里有许多fprintf, std::cout printf 的标准日志打印log，在程序开发中无法查看这些日志。

**解决措施**

cout/printf是语言提供的打印函数，并不能填充到hilog日志中。可通过重定向的方法将日志打印到文件来获取打印信息。具体方法如下：

Native侧重定向方法主体。

```screen
#include "napi/native_api.h" 
#include <hilog/log.h> 
#include <string> 
#include "iostream" 
#include "fstream" 
#define LOG_TAG "Pure" 
 
static napi_value Redirect(napi_env env, napi_callback_info info) { 
    // Get the JS parameters of the function 
    size_t argc = 1; 
    napi_value argv[1] = {nullptr}; 
    napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr); 
    // Resolve parameter 1, the destination directory for saving the file
    size_t targetDirectoryNameSize; 
    char targetDirectoryNameBuf[512]; 
    napi_get_value_string_utf8(env, argv[0], targetDirectoryNameBuf, sizeof(targetDirectoryNameBuf), 
                               &targetDirectoryNameSize); 
    std::string targetDirectoryName(targetDirectoryNameBuf, targetDirectoryNameSize); // target directory 
    OH_LOG_INFO(LOG_APP, "C++Received target path on the side === %{public}s", targetDirectoryNameBuf); 
    std::string targetSandboxPath = targetDirectoryName + "/Log.log"; // Saved file path 
     
    // Use the freopen function to associate files with standard output 
    FILE *stdoutFile = NULL; 
    FILE *stderrFile = NULL; 
    stdoutFile = freopen(targetSandboxPath.c_str(), "a", stdout); 
    stderrFile = freopen(targetSandboxPath.c_str(), "a", stderr); 
    if (NULL == stdoutFile || NULL == stderrFile) { 
        OH_LOG_INFO(LOG_APP, "Recreate！"); 
        // Opening the file output stream of the sandbox file will create a file
        std::ofstream outputFile(targetSandboxPath, std::ios::binary); 
        if (!outputFile) { 
            OH_LOG_ERROR(LOG_APP, "Unable to create target file!"); 
            return nullptr; 
        } 
        stdoutFile = freopen(targetSandboxPath.c_str(), "a", stdout); 
        stderrFile = freopen(targetSandboxPath.c_str(), "a", stderr); 
        if (NULL == stdoutFile || NULL == stderrFile) { 
            OH_LOG_ERROR(LOG_APP, "fail!"); 
            return nullptr; 
        } 
    } 
    OH_LOG_WARN(LOG_APP, "redirect!"); 
    printf("\n*****************Redirect dividing line*****************\n"); 
    return 0; 
}
```

在ArkTS侧调用并传入路径信息。

在EntryAbility的onCreate()方法中调用重定向。

```ts
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  let file : string = this.context.getApplicationContext().filesDir;
  testNapi.redirect(file);
  hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
}
```
