---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-fileuri-guidelines
title: FileUri开发指导(C/C++)
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 用户文件 > FileUri开发指导(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:802d820aae31865ce93f3781bac47619869604eab214f5130cb85bfbb2a60254
---

## 场景介绍

FileUri提供了关于文件URI的基本操作，将URI转换成对应的沙箱路径、将应用沙箱路径转换成对应应用自己的URI、获取URI所在目录路径的URI等接口能力，方便应用对文件分享业务中URI的访问。

## 基本概念

**结果集**：满足使用场景的路径或URI。

## 约束限制

* URI转路径时，URI来源建议使用系统能力获取，例如：picker、剪贴板、拖拽、及系统提供的路径转URI接口等系统能力返回的URI；如果转换应用或用户拼接的URI，则转换后的路径可能无法访问。
* 为保证数据的准确性，在转换或判断过程中应保持单对象处理，避免资源竞争导致数据异常。

## 接口说明

接口的详细说明，请参考[oh\_file\_uri.h](../harmonyos-references/capi-oh-file-uri-h.md)。

| 接口名称 | 描述 |
| --- | --- |
| FileManagement\_ErrCode OH\_FileUri\_GetUriFromPath(const char \*path, unsigned int length, char \*\*result) | 通过传入的path生成应用自己的URI。将path转URI时，path中的中文及非数字字母的特殊字符会被编码为对应的ASCII码，并拼接在URI中。 |
| FileManagement\_ErrCode OH\_FileUri\_GetPathFromUri(const char \*uri, unsigned int length, char \*\*result) | 将uri转换成对应的沙箱路径。  1. uri转路径过程中会将uri中存在的ASCII码进行解码后拼接在原处，非系统接口生成的uri中可能存在ASCII码解析范围之外的字符，导致字符串无法正常拼接。  2. 转换处理遵循系统约定的字符串替换规则（规则可能随系统演进而变化），转换过程中不进行路径校验操作，无法保证转换结果的可访问性。 |
| FileManagement\_ErrCode OH\_FileUri\_GetFullDirectoryUri(const char \*uri, unsigned int length, char \*\*result) | 获取所在路径uri。  1. uri指向文件则返回所在路径的uri。  2. uri指向目录则不处理直接返回原串。  3. uri指向的文件不存在或属性获取失败则返回空串。 |
| bool OH\_FileUri\_IsValidUri(const char \*uri, unsigned int length) | 判断传入的uri的格式是否正确。仅校验uri是否满足系统定义的格式规范，不校验uri的有效性。 |
| FileManagement\_ErrCode OH\_FileUri\_GetFileName(const char \*uri, unsigned int length, char \*\*result) | 通过传入的uri获取到对应的文件名称（如果文件名中存在ASCII码将会被解码处理后拼接在原处）。 |

## 开发步骤

**在CMake脚本中链接动态库**

CMakeLists.txt中添加以下lib。

```txt
target_link_libraries(sample PUBLIC libohfileuri.so)
```

**添加头文件**

```
#include <filemanagement/file_uri/oh_file_uri.h>
```

1. 调用OH\_FileUri\_GetUriFromPath接口，在接口中malloc的内存需要在使用完后释放，因此需要free对应的内存，避免内存泄漏。示例代码如下所示：

   ```
   static napi_value NAPI_Global_OH_FileUri_GetUriFromPathExample(napi_env env, napi_callback_info info)
   {
       // ...
       // 为 char* uri 分配内存
       char *path = new char[strLength + 1]; // +1 for null terminator
       // 将 JavaScript 字符串复制到 uri
       // ...
       unsigned int length = strlen(path);
       // 输出传入路径字符串
       // ...
       char *uriResult = nullptr;
       FileManagement_ErrCode ret = OH_FileUri_GetUriFromPath(path, length, &uriResult);
       // 输出结果uri字符串
       // ...
       if (ret == 0 && uriResult != nullptr) {
           // 将C字符串转换为napi_value
           napi_status status = napi_create_string_utf8(env, uriResult, NAPI_AUTO_LENGTH, &result);
           if (status != napi_ok) {
               free(uriResult);
               return nullptr;
           }
           free(uriResult); // 释放临时字符串
       } else {
           // 将C字符串转换为napi_value
           napi_status status = napi_create_string_utf8(env, "Hello World", NAPI_AUTO_LENGTH, &result);
           if (status != napi_ok) {
               return nullptr;
           }
       }
       return result;
   }
   ```
2. 调用OH\_FileUri\_GetPathFromUri通过URI转成对应的路径，在接口中malloc的内存需要在使用完后释放，因此需要free对应的内存，避免内存泄漏。示例代码如下所示。

   ```
   static napi_value NAPI_Global_OH_FileUri_GetPathFromUriExample(napi_env env, napi_callback_info info)
   {
       // ...
       char *uri = new char[strLength + 1]; // +1 for null terminator
       // 将 JavaScript 字符串复制到 uri
       napi_get_value_string_utf8(env, args[0], uri, strLength + 1, &strLength);

       unsigned int length = strlen(uri);
       // 输出传入uri字符串
       OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.WatcherType=OnTrigger: %{public}s", uri);
       char *pathResult = nullptr;
       FileManagement_ErrCode ret = OH_FileUri_GetPathFromUri(uri, length, &pathResult);
       // 输出获取路径结果字符串
       // ...
       if (ret == 0 && pathResult != nullptr) {
           // 将C字符串转换为napi_value
           napi_status status = napi_create_string_utf8(env, pathResult, NAPI_AUTO_LENGTH, &result);
           if (status != napi_ok) {
               free(pathResult);
               return nullptr;
           }
           free(pathResult); // 释放临时字符串
       } else {
           // 将空字符串转换为napi_value
           napi_status status = napi_create_string_utf8(env, "", NAPI_AUTO_LENGTH, &result);
           if (status != napi_ok) {
               return nullptr;
           }
       }
       return result;
   }
   ```
3. 调用OH\_FileUri\_GetFullDirectoryUri获取URI所在路径的URI，在接口中malloc的内存需要在使用完后释放，因此需要free对应的内存，避免内存泄漏。示例代码如下所示。

   ```
   static napi_value NAPI_Global_OH_FileUri_GetFullDirectoryUriExample(napi_env env, napi_callback_info info)
   {
       // ...
       char *uri = new char[strLength + 1]; // +1 for null terminator
       // 将 JavaScript 字符串复制到 uri
       napi_get_value_string_utf8(env, args[0], uri, strLength + 1, &strLength);

       unsigned int length = strlen(uri);
       // 输出传入uri字符串
       OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.WatcherType=OnTrigger: %{public}s", uri);
       char *uriResult = nullptr;
       FileManagement_ErrCode ret = OH_FileUri_GetFullDirectoryUri(uri, length, &uriResult);
       // 输出所在路径uri字符串
       // ...
       if (ret == 0 && uriResult != nullptr) {
           // 使用napi接口创建一个字符串类型的napi_value来返回正确结果
           napi_create_string_utf8(env, uriResult, NAPI_AUTO_LENGTH, &result);
       } else {
           // 使用napi接口创建一个表示null值的napi_value来返回错误或空值情况
           napi_get_null(env, &result);
       }
       if (uriResult != nullptr) {
           free(uriResult);
       }
       return result;
   }
   ```
4. 可以调用OH\_FileUri\_IsValidUri接口进行URI格式验证。 示例代码如下所示。

   ```
   static napi_value NAPI_Global_OH_FileUri_IsValidUriExample(napi_env env, napi_callback_info info)
   {
       // ...
       char *uri = new char[strLength + 1]; // +1 for null terminator
       // 将 JavaScript 字符串复制到 uri
       napi_get_value_string_utf8(env, args[0], uri, strLength + 1, &strLength);
       unsigned int length = strlen(uri);
       // 输出传入uri字符串
       OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.WatcherType=OnTrigger: %{public}s", uri);
       bool flags = OH_FileUri_IsValidUri(uri, length);
       // ...
   }
   ```
5. 调用OH\_FileUri\_GetFileName获取URI中的文件名称，在接口中malloc的内存需要在使用完后释放，因此需要free对应的内存，避免内存泄漏。示例代码如下所示。

   ```
   static napi_value NAPI_Global_OH_FileUri_GetFileNameExample(napi_env env, napi_callback_info info)
   {
       // ...
       char *uri = new char[strLength + 1]; // +1 for null terminator
       // 将 JavaScript 字符串复制到 uri
       napi_get_value_string_utf8(env, args[0], uri, strLength + 1, &strLength);

       unsigned int length = strlen(uri);
       // 输出传入uri字符串
       OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.WatcherType=OnTrigger: %{public}s", uri);
       char *uriResult = nullptr;
       FileManagement_ErrCode ret = OH_FileUri_GetFileName(uri, length, &uriResult);
       // 输出获取到的文件名称
       // ...
       if (ret == 0 && uriResult != nullptr) {
           // 将C字符串转换为napi_value
           napi_status status = napi_create_string_utf8(env, uriResult, NAPI_AUTO_LENGTH, &result);
           if (status != napi_ok) {
               free(uriResult);
               return NULL;
           }
           free(uriResult); // 释放临时字符串
       } else {
           // 将空字符串转换为napi_value
           napi_status status = napi_create_string_utf8(env, "", NAPI_AUTO_LENGTH, &result);
           if (status != napi_ok) {
               return nullptr;
           }
       }
       return result;
   }
   ```
