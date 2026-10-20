---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/ndk-development-faq-0001
title: Native侧文件操作常见问题
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 常见问题 > Native侧文件操作常见问题
category: harmonyos-faqs
scraped_at: 2026-10-21T07:10:29+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:70ca5ed88d73eaf1bfe28c80fd026114658dd5887c2684bee85746bcc4a96e8e
---

**Q：通过Picker方式获取用户文件URI，在C++侧无法通过URI打开文件，如何解决？**

**A**：有以下几种解决方案：

* 将URI直接传递到C++侧，通过C++侧提供的转换接口，将URI转换为path后访问文件。

  参考代码：

  ```cpp
  napi_value ReadFileFromUri(napi_env env, napi_callback_info info)
  {
      size_t argc = 1;
      napi_value args[1] = {nullptr};
      napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
      size_t length = 0;
      napi_get_value_string_utf8(env, args[0], nullptr, 0, &length);
      char* uri = new char[length + 1];
      napi_get_value_string_utf8(env, args[0], uri, length + 1, &length);
      uri[length] = '\0';
      OH_LOG_INFO(LOG_APP, "Native ReadFileFromUri Uri: %{public}s", uri);
      char *pathResult = NULL;
      int ret = OH_FileUri_GetPathFromUri(uri, length, &pathResult);
      if (ret != 0 || pathResult == NULL) {
          delete []uri;
          return nullptr;
      }
      OH_LOG_INFO(LOG_APP, "Native ReadFileFromUri Path: %{public}s", pathResult);
      int fd = open(pathResult, O_RDONLY);
      struct stat fileInfo;
      if (fstat(fd, &fileInfo) == -1) {
          OH_LOG_INFO(LOG_APP, "Native ReadFileFromUri failed");
          delete []uri;
          return nullptr;
      }
      OH_LOG_INFO(LOG_APP, "Native ReadFileFromUri: %{public}d", (int)fileInfo.st_size);
      close(fd);
      delete []uri;
      return nullptr;
  }
  ```
* 在ArkTS侧，通过URI打开文件，将文件句柄fd传递到C++侧，通过句柄访问文件。

  参考代码：

  ```ts
  photoViewPicker.select(photoSelectOptions)
                .then((photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
                  let file = fs.openSync(photoSelectResult.photoUris[0], fs.OpenMode.READ_ONLY);
                  hilog.info(DOMAIN, TAG, 'file fd: ' + file.fd);
                  testNapi.readFileFromFd(file.fd);
                  fs.closeSync(file);
                })
                .catch((err: BusinessError) => {
                  hilog.error(DOMAIN, TAG, `photoPicker failed, code is ${err.code}, message is ${err.message}`);
                });
  ```

  ```cpp
  napi_value ReadFileFromFd(napi_env env, napi_callback_info info)
  {
      size_t argc = 1;
      napi_value args[1] = {nullptr};
      napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
      int fd;
      napi_get_value_int32(env, args[0], &fd);
      struct stat fileInfo;
      if (fstat(fd, &fileInfo) == -1) {
          OH_LOG_INFO(LOG_APP, "Native ReadFileFromFd failed");
          return nullptr;
      }
      OH_LOG_INFO(LOG_APP, "Native ReadFileFromFd: %{public}d", (int)fileInfo.st_size);
      return nullptr;
  }
  ```
* 文件URI可以通过在ArkTS侧获取文件path，传递到C++侧访问（媒体URI和应用目录不可用）。

  参考代码：

  ```ts
  documentViewPicker.select(documentSelectOptions)
                .then((documentSelectResult) => {
                  testNapi.readFileFromUri(documentSelectResult[0]);
                  let file = fs.openSync(documentSelectResult[0], fs.OpenMode.READ_ONLY);
                  hilog.info(DOMAIN, TAG, 'file path: ' + file.path);
                  let path = file.path;
                  fs.closeSync(file);
                  testNapi.readFileFromPath(path);
                })
                .catch((err: BusinessError) => {
                  hilog.error(DOMAIN, TAG, `filePicker failed, code is ${err.code}, message is ${err.message}`);
                });
  ```

  ```cpp
  napi_value ReadFileFromPath(napi_env env, napi_callback_info info)
  {
      size_t argc = 1;
      napi_value args[1] = {nullptr};
      napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
      size_t length = 0;
      napi_get_value_string_utf8(env, args[0], nullptr, 0, &length);
      char* path = new char[length + 1];
      napi_get_value_string_utf8(env, args[0], path, length + 1, &length);
      path[length] = '\0';

      OH_LOG_INFO(LOG_APP, "Native ReadFileFromPath: %{public}s", path);
      int fd = open(path, O_RDONLY);
      struct stat fileInfo;
      if (fstat(fd, &fileInfo) == -1) {
          OH_LOG_INFO(LOG_APP, "Native ReadFileFromPath failed");
          delete []path;
          return nullptr;
      }
      OH_LOG_INFO(LOG_APP, "Native ReadFileFromPath: %{public}d", (int)fileInfo.st_size);
      close(fd);
      delete []path;
      return nullptr;
  }
  ```

**Q：应用[沙箱目录](../harmonyos-guides/app-sandbox-directory.md)文件如何在C++侧访问？**

**A**：文件的沙箱路径，即文件在设备上的path，C++侧可通过文件操作接口访问。

**Q：应用资源文件在C++侧如何访问？**

**A**：需要访问的资源文件建议放在Rawfile目录，通过[Rawfile开发指导](../harmonyos-guides/rawfile-guidelines.md)提供的C++接口访问，或是将文件拷贝到沙箱目录，通过文件接口访问。

**Q：如何在Native侧往用户目录写临时文件？**

**A**：应用目录中，用户可以将临时文件写入以下目录。请查看native层写文件的代码示例：

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

目前没有直接写文件的Native接口，但可以通过C++基础库结合沙箱路径实现写文件操作。

代码如下：

```cpp
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

用户可访问的目录可参考以下链接：[应用沙箱目录](../harmonyos-guides/app-sandbox-directory.md)。
