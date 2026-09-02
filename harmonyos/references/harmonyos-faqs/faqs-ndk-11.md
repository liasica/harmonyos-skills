---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-11
title: 如何在Native侧往用户目录写临时文件
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何在Native侧往用户目录写临时文件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f6faa0552018b32de75523217f311f3cca2bfc6c121d76605b0efc76b38fa5f7
---

**问题详情**

应用目录中，用户可以将临时文件写入以下目录。请查看native层写文件的代码示例：

```cpp
#include <stdio.h>

void writeTempFile(const char* path, const char* content) {
FILE* file = fopen(path, "w");
if (file != NULL) {
fprintf(file, "%s", content);
fclose(file);
}
}
```

可写入临时文件的目录包括：

cache：用于存放缓存文件。

files：用于存放应用数据文件。

**解决措施**

目前没有直接写文件的Native接口，但可以通过C++基础库结合沙箱路径实现写文件操作。

代码如下：

```ts
#include "WriteFile.h"
#include "napi/native_api.h"
#include <fstream>
napi_value WriteFile::WriteTemporaryFile(napi_env env, napi_callback_info info) {
    std::ofstream file("data/storage/el2/base/temp/2.txt");
    if (file.is_open()) {        // Determine if the file can be opened normally
        file << "Hello, World!"; // Write content to a file
        file.close();            // close file
    }
    return nullptr;
}
```

用户可访问的目录可参考以下链接：[应用沙箱目录](../harmonyos-guides/app-sandbox-directory.md)
