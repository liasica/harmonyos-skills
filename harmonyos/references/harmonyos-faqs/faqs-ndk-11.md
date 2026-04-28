---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-11
title: 如何在Native侧往用户目录写临时文件
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何在Native侧往用户目录写临时文件
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:30+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1d6779306d3094ddaa4995bb04bb44321dc976fb7be47e8617c445448cd24ebc
---

**问题详情**

应用目录中，用户可以将临时文件写入以下目录。请查看native层写文件的代码示例：

cpp

#include <stdio.h>

void writeTempFile(const char\* path, const char\* content) {

FILE\* file = fopen(path, "w");

if (file != NULL) {

fprintf(file, "%s", content);

fclose(file);

}

}

可写入临时文件的目录包括：

cache：用于存放缓存文件。

files：用于存放应用数据文件。

**解决措施**

目前没有直接写文件的Native接口，但可以通过C++基础库结合沙箱路径实现写文件操作。

代码如下：

```
1. #include "WriteFile.h"
2. #include "napi/native_api.h"
3. #include <fstream>
4. napi_value WriteFile::WriteTemporaryFile(napi_env env, napi_callback_info info) {
5. std::ofstream file("data/storage/el2/base/temp/2.txt");
6. if (file.is_open()) {        // Determine if the file can be opened normally
7. file << "Hello, World!"; // Write content to a file
8. file.close();            // close file
9. }
10. return nullptr;
11. }
```

[WriteFile.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/entry/src/main/cpp/WriteFile/WriteFile.cpp#L19-L29)

用户可访问的目录可参考以下链接：[应用沙箱目录](../harmonyos-guides/app-sandbox-directory.md)
