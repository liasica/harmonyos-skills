---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/archive-buffer-compression-guidelines
title: 缓冲区压缩解压缩(C/C++)
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 文件压缩解压缩 > 缓冲区压缩解压缩(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:24+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:faec691912d1d7d16dc88d8c2f67d6a4178d53f117ef20cb0d6b8801644e1a2d
---

## 场景介绍

从API版本26.0.0开始，提供了缓冲区压缩解压缩能力，可以对内存中的整块数据进行一次性压缩或解压缩。主要适用于数据量较小且完整的场景，接口简单，操作快捷。

* 缓冲区压缩：对内存中的数据进行快速压缩，节省存储空间。
* 缓冲区解压缩：对已压缩的数据进行内存解压缩，还原原始数据。

## 接口说明

接口的详细说明，请参考[oh\_archive.h](../harmonyos-references/capi-oh-archive-h.md)。

| 接口名称 | 描述 |
| --- | --- |
| OH\_Archive\_BufferWriteCompressBound(OH\_Archive\_CompressMethod method, uint64\_t sourceLen) | 计算缓冲区压缩所需输出缓冲区大小。 |
| OH\_Archive\_BufferWrite(uint8\_t \*dstBuffer, uint64\_t \*dstSize, const uint8\_t \*srcBuffer, uint64\_t srcSize, OH\_Archive\_CompressMethod method, int32\_t compressLevel) | 对缓冲区数据进行压缩。 |
| OH\_Archive\_BufferRead(uint8\_t \*dstBuffer, uint64\_t \*dstSize, const uint8\_t \*srcBuffer, uint64\_t srcSize, OH\_Archive\_CompressMethod method) | 对缓冲区数据进行解压缩。 |

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

### 缓冲区压缩

1. 调用OH\_Archive\_BufferWriteCompressBound计算输出缓冲区大小。压缩前先调用此接口获取输出缓冲区所需大小，确保输出缓冲区足够容纳压缩后的数据。
2. 调用OH\_Archive\_BufferWrite对缓冲区数据进行压缩。调用时需指定输入数据、输出缓冲区、数据长度、压缩算法和压缩级别。压缩后的实际数据大小通过dstSize参数返回。

```
static napi_value BufferCompress(napi_env env, napi_callback_info info)
{
    // 获取输入文件路径和输出文件路径
    size_t argc = 2;
    napi_value argv[2] = {nullptr};
    napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);

    size_t inPathSize;
    size_t outPathSize;
    char inPathBuf[PATH_BUFFER_SIZE];
    char outPathBuf[PATH_BUFFER_SIZE];
    napi_get_value_string_utf8(env, argv[0], inPathBuf, sizeof(inPathBuf), &inPathSize);
    napi_get_value_string_utf8(env, argv[1], outPathBuf, sizeof(outPathBuf), &outPathSize);

    CreateRandomFile(inPathBuf, 1024 * 1024); // 创建1024K大小的测试文件
    // 读取文件数据到内存缓冲区
    char *source = nullptr;
    uint64_t sourceLen;
    ReadFileData(inPathBuf, &source, &sourceLen);

    uint64_t destLen = 0;
    uint8_t *dest = nullptr;

    // 计算压缩后数据所需的最大输出缓冲区大小
    uint64_t bound = OH_Archive_BufferWriteCompressBound(OH_ARCHIVE_COMPRESS_DEFLATE, sourceLen);
    if (bound > MALLOC_THRESHOLD) {
        return nullptr;
    }
    dest = (uint8_t *)malloc(bound);
    if (dest == nullptr) {
        free(source);
        return nullptr;
    }
    destLen = bound;

    // 对缓冲区数据进行压缩，使用DEFLATE算法，压缩级别为0
    OH_Archive_ErrCode ret = OH_Archive_BufferWrite(dest, &destLen, reinterpret_cast<uint8_t *>(source), sourceLen,
                                                    OH_ARCHIVE_COMPRESS_DEFLATE, 0);

    free(source);
    free(dest);
    napi_value result = nullptr;
    napi_create_int32(env, ret, &result);
    return result;
}
```

### 缓冲区解压缩

准备输出缓冲区并调用OH\_Archive\_BufferRead解压缩数据。解压缩时需指定压缩数据缓冲区、输出缓冲区、数据长度和压缩算法，解压缩后的实际数据大小通过dstSize参数返回。建议压缩和解压缩使用相同的压缩算法参数。

```
static napi_value BufferDecompress(napi_env env, napi_callback_info info)
{
    size_t argc = 0;
    napi_get_cb_info(env, info, &argc, nullptr, nullptr, nullptr);

    int ret;
    // 生成随机测试数据
    uint64_t dataSize = 1024 * 1024;
    uint8_t *srcBuffer = (uint8_t *)malloc(dataSize);
    if (srcBuffer == nullptr) {
        return nullptr;
    }

    for (size_t i = 0; i < dataSize; ++i) {
        srcBuffer[i] = static_cast<uint8_t>(TestRandomInt(0, 256)); // 小于256, byte范围内
    }

    // 先压缩数据，用于后续解压缩验证
    uint64_t bound = OH_Archive_BufferWriteCompressBound(OH_ARCHIVE_COMPRESS_DEFLATE, dataSize);
    uint64_t compressedSize = bound;
    uint8_t *compressedBuffer = (uint8_t *)malloc(compressedSize);
    if (compressedBuffer == nullptr) {
        return nullptr;
    }
    ret = OH_Archive_BufferWrite(compressedBuffer, &compressedSize, srcBuffer, dataSize, OH_ARCHIVE_COMPRESS_DEFLATE,
                                 int32_t(6)); // 压缩等级为6
    // 分配解压缩输出缓冲区并执行解压缩
    uint8_t *decompressedBuffer = (uint8_t *)malloc(dataSize);
    if (decompressedBuffer == nullptr) {
        return nullptr;
    }
    uint64_t decompressedSize = dataSize;
    ret = OH_Archive_BufferRead(decompressedBuffer, &decompressedSize, compressedBuffer, compressedSize,
                                OH_ARCHIVE_COMPRESS_DEFLATE);
    // 校验解压缩后的数据与原始数据是否一致
    bool isEqual = std::memcmp(decompressedBuffer, srcBuffer, dataSize) == 0;
    free(srcBuffer);
    free(compressedBuffer);
    free(decompressedBuffer);

    napi_value result = nullptr;
    napi_create_int32(env, !isEqual, &result);
    return result;
}
```

## 调测验证关键点

缓冲区压缩解压缩：验证压缩后再解压缩的数据与原始数据完全一致，无数据丢失。
