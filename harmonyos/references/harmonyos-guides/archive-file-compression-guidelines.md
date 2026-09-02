---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/archive-file-compression-guidelines
title: 文件归档类压缩解压缩(C/C++)
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 文件压缩解压缩 > 文件归档类压缩解压缩(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:24+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:65ac6714a6608b3e1e541c01903707af5c6ed1e021c5922dff2d50708e3fc84f
---

## 场景介绍

从API版本26.0.0开始支持文件归档类压缩解压缩，适用于将多个文件和目录打包为一个归档文件，或者从归档文件中提取文件到指定目录的场景。主要应用场景包括：

* 将多个文件或目录打包压缩为一个归档文件，便于存储和传输。
* 解压缩归档文件，将压缩包中的文件提取到指定目录。

## 约束限制

* 压缩解压缩接口的输入输出路径均为沙箱路径，具体请参考[应用沙箱目录](app-sandbox-directory.md)。
* 当前仅支持ZIP格式的归档文件。

## 接口说明

接口的详细说明，请参考[oh\_archive.h](../harmonyos-references/capi-oh-archive-h.md)。

### 归档文件压缩接口

| 接口名称 | 描述 |
| --- | --- |
| OH\_Archive\_Writer\_OpenFile(const char \*outFile, OH\_Archive\_OpenMode openMode, OH\_Archive\_Format fmt) | 打开归档文件并创建写入器。 |
| OH\_Archive\_Writer\_Add(OH\_Archive\_Writer\_Ctx arc, const char \*\*infiles, uint64\_t fileNum) | 向归档文件中添加文件或目录。 |
| OH\_Archive\_Writer\_Close(OH\_Archive\_Writer\_Ctx arc) | 关闭归档写入器。 |

### 归档文件解压缩接口

| 接口名称 | 描述 |
| --- | --- |
| OH\_Archive\_Reader\_OpenFile(const char \*inFile) | 打开归档文件并创建读取器。 |
| OH\_Archive\_Reader\_ExtractAllFile(OH\_Archive\_Reader\_Ctx arc, const char \*outDir) | 解压缩归档文件中的所有文件到指定目录。 |
| OH\_Archive\_Reader\_Close(OH\_Archive\_Reader\_Ctx arc) | 关闭归档读取器。 |

## 开发准备

**在CMake脚本中链接动态库**

CMakeLists.txt中添加以下lib。

```txt
target_link_libraries(sample PUBLIC liboharchive.so)
```

**添加头文件**

```
#include <filemanagement/archive/oh_archive.h>
```

## 开发步骤

### 归档文件压缩

1. 调用OH\_Archive\_Writer\_OpenFile创建归档写入器。需指定输出文件路径、打开模式（如OH\_ARCHIVE\_OPEN\_MODE\_CREATE）和归档格式（如OH\_ARCHIVE\_FMT\_ZIP）。
2. （可选）调用OH\_Archive\_Writer\_SetCompressMethod设置压缩算法和压缩级别。默认使用DEFLATE压缩算法，压缩级别为6，开发者可根据需要调整。
3. （可选）调用OH\_Archive\_Writer\_SetProgressHandlerWithData设置进度回调，用于获取压缩进度信息。
4. 调用OH\_Archive\_Writer\_Add向归档中添加文件或目录，支持同时添加多个文件或目录。
5. 调用OH\_Archive\_Writer\_Close完成归档写入并释放资源。压缩完成后必须调用此接口释放资源。

```
static napi_value ZipFileCompress(napi_env env, napi_callback_info info)
{
    // 获取输入文件路径和输出归档文件路径
    size_t argc = 2;
    napi_value argv[2] = {nullptr};
    napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);

    size_t inPathSize;
    size_t zipPathSize;
    char inPathBuf[PATH_BUFFER_SIZE];
    char zipPathBuf[PATH_BUFFER_SIZE];
    napi_get_value_string_utf8(env, argv[0], inPathBuf, sizeof(inPathBuf), &inPathSize);
    napi_get_value_string_utf8(env, argv[1], zipPathBuf, sizeof(zipPathBuf), &zipPathSize);

    // 创建测试文件并写入内容
    std::string content = "test content这是测试内容Hello, hello!第一行数据";
    std::string file(inPathBuf);
    std::ofstream stdfile(file, std::ios::out | std::ios::trunc);
    if (stdfile.is_open()) {
        stdfile << content;
        stdfile.close();
    }
    std::vector<const char *> srcFiles;
    srcFiles.push_back(file.c_str());

    int ret;
    // 打开归档文件并创建写入器，指定ZIP格式
    OH_Archive_Writer_Ctx arc = OH_Archive_Writer_OpenFile(zipPathBuf, OH_ARCHIVE_OPEN_MODE_CREATE, OH_ARCHIVE_FMT_ZIP);
    // 设置压缩算法为DEFLATE，压缩级别为6
    ret = OH_Archive_Writer_SetCompressMethod(arc, OH_ARCHIVE_COMPRESS_DEFLATE, int32_t(6)); // 压缩等级为6

    // 设置进度回调，用于获取压缩进度信息
    OH_Archive_ProgressHandlerWithData progressHandlerFunc = ProgressHandler;
    ret = OH_Archive_Writer_SetProgressHandlerWithData(arc, progressHandlerFunc, nullptr);
    // 添加文件到归档中
    ret = OH_Archive_Writer_Add(arc, srcFiles.data(), srcFiles.size());
    // 关闭归档写入器，完成压缩并释放资源
    ret = OH_Archive_Writer_Close(arc);
    napi_value retVal = nullptr;
    napi_create_int32(env, ret, &retVal);
    return retVal;
}
```

### 归档文件解压缩

1. 调用OH\_Archive\_Reader\_OpenFile打开归档文件并创建读取器。需指定ZIP文件路径。
2. （可选）调用OH\_Archive\_Reader\_SetProgressHandlerWithData设置解压缩进度回调。
3. 调用OH\_Archive\_Reader\_ExtractAllFile将归档文件解压缩到指定目录。解压缩后的文件将保持原有的目录结构。
4. 调用OH\_Archive\_Reader\_Close关闭归档读取器。解压缩完成后必须调用此接口释放资源。

```
static napi_value ZipFileDecompress(napi_env env, napi_callback_info info)
{
    // 获取输入文件路径、归档文件路径和解压输出目录路径
    size_t argc = 3;
    napi_value argv[3] = {nullptr};
    napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);

    size_t inPathSize;
    size_t zipPathSize;
    size_t outDirSize;
    char inPathBuf[PATH_BUFFER_SIZE];
    char zipPathBuf[PATH_BUFFER_SIZE];
    char outDirBuf[PATH_BUFFER_SIZE];
    napi_get_value_string_utf8(env, argv[0], inPathBuf, sizeof(inPathBuf), &inPathSize);
    napi_get_value_string_utf8(env, argv[1], zipPathBuf, sizeof(zipPathBuf), &zipPathSize);
    napi_get_value_string_utf8(env, argv[2], outDirBuf, sizeof(outDirBuf), &outDirSize); // 第2个参数

    // 先压缩文件生成归档文件，用于后续解压缩
    int ret = ArchiveCompressFile(inPathBuf, zipPathBuf);
    // 打开归档文件并创建读取器
    OH_Archive_Reader_Ctx ctx = OH_Archive_Reader_OpenFile(zipPathBuf);
    int userData[2] = {0};
    // 设置解压缩进度回调
    ret = OH_Archive_Reader_SetProgressHandlerWithData(ctx, ProgressHandler, (void *)userData);
    // 解压缩归档文件中的所有文件到指定目录
    ret = OH_Archive_Reader_ExtractAllFile(ctx, outDirBuf);
    // 关闭归档读取器，释放资源
    ret = OH_Archive_Reader_Close(ctx);

    napi_value result = nullptr;
    napi_create_int32(env, ret, &result);
    return result;
}
```

## 调测验证关键点

* 归档文件压缩：验证生成的ZIP文件可以使用标准解压缩工具打开，文件内容完整，目录结构正确。
* 归档文件解压缩：验证解压缩后的文件和目录结构与压缩前一致，文件内容无损坏。
