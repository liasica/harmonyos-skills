---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-development-8
title: 如何在C++侧打开Picker获取的用户文件
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何在C++侧打开Picker获取的用户文件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:bebb49ea51872d31f489bbcdedfbf18a4f718d38b2c4c8d0b424c97881b83ace
---

## 问题现象

通过Picker方式获取用户文件URI，在C++侧无法通过URI打开文件。

## 背景知识

[用户文件URI介绍](../harmonyos-guides/user-file-uri-intro.md)：用户文件URI是文件的唯一标识，在ArkTS侧可以通过该URI访问用户文件，在C++侧需要转换为路径或文件句柄访问。

## 解决方案

* 将URI直接传递到C++侧，通过C++侧提供的转换接口，将URI转换为path后访问文件。

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

## 常见FAQ

Q：应用[沙箱目录](../harmonyos-guides/app-sandbox-directory.md)文件如何在C++侧访问？

A：文件的沙箱路径，即文件在设备上的path，C++侧可通过文件操作接口访问。

Q：应用资源文件在C++侧如何访问？

A：需要访问的资源文件建议放在Rawfile目录，通过[Rawfile开发指导](../harmonyos-guides/rawfile-guidelines.md)提供的C++接口访问，或是将文件拷贝到沙箱目录，通过文件接口访问。
