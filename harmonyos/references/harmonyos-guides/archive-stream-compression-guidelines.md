---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/archive-stream-compression-guidelines
title: 流式压缩解压缩(C/C++)
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 文件压缩解压缩 > 流式压缩解压缩(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:24+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:e45252ed01ce5824f3986427c7e86129f7c354e0c8e2ff17720299b9ae082810
---

## 场景介绍

从API版本26.0.0开始支持流式压缩解压缩，适用于对连续数据流进行实时压缩或解压缩的场景。主要应用场景包括：

* 对实时产生的日志数据进行流式压缩，边生成边压缩。
* 对网络数据流进行实时压缩或解压缩，减少传输数据量。
* 对大量数据进行分段处理，避免一次性将全部数据加载到内存中。

## 接口说明

接口的详细说明，请参考[oh\_archive.h](../harmonyos-references/capi-oh-archive-h.md)。

### 流式压缩解压缩接口

| 接口名称 | 描述 |
| --- | --- |
| OH\_Archive\_StreamWrite\_Create(OH\_Archive\_Stream\_Config config) | 创建流式压缩写入器。 |
| OH\_Archive\_StreamWrite\_Start(OH\_Archive\_StreamWrite\_Ctx ctx, OH\_Archive\_Stream\_OutputHandler outputHandler, void \*userData) | 启动流式压缩。 |
| OH\_Archive\_StreamWrite\_Update(OH\_Archive\_StreamWrite\_Ctx ctx, const uint8\_t \*data, uint64\_t size) | 向流式压缩器输入数据进行压缩。 |
| OH\_Archive\_StreamWrite\_End(OH\_Archive\_StreamWrite\_Ctx ctx, OH\_Archive\_StreamInfo \*streamInfo) | 结束流式压缩并获取压缩结果信息。 |
| OH\_Archive\_StreamWrite\_Cancel(OH\_Archive\_StreamWrite\_Ctx ctx) | 取消流式压缩。 |
| OH\_Archive\_StreamWrite\_Destroy(OH\_Archive\_StreamWrite\_Ctx ctx) | 销毁流式压缩写入器。 |
| OH\_Archive\_StreamRead\_Create(OH\_Archive\_Stream\_Config config) | 创建流式解压缩读取器。 |
| OH\_Archive\_StreamRead\_Start(OH\_Archive\_StreamRead\_Ctx ctx, OH\_Archive\_Stream\_OutputHandler outputHandler, void \*userData) | 启动流式解压缩。 |
| OH\_Archive\_StreamRead\_Update(OH\_Archive\_StreamRead\_Ctx ctx, const uint8\_t \*data, uint64\_t size) | 向流式解压缩器输入数据进行解压缩。 |
| OH\_Archive\_StreamRead\_End(OH\_Archive\_StreamRead\_Ctx ctx, OH\_Archive\_StreamInfo \*streamInfo) | 结束流式解压缩并获取解压缩结果信息。 |
| OH\_Archive\_StreamRead\_Cancel(OH\_Archive\_StreamRead\_Ctx ctx) | 取消流式解压缩。 |
| OH\_Archive\_StreamRead\_Destroy(OH\_Archive\_StreamRead\_Ctx ctx) | 销毁流式解压缩读取器。 |

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

### 流式压缩

1. 创建流式压缩配置并调用OH\_Archive\_StreamWrite\_Create创建流式压缩写入器。需指定配置信息，包括block大小、线程数、压缩算法和校验方式。
2. 调用OH\_Archive\_StreamWrite\_Start启动流式压缩。压缩过程中通过输出回调函数处理压缩后的数据。
3. 调用OH\_Archive\_StreamWrite\_SetCompressLevel设置压缩级别（可选，默认为6）。
4. 多次调用OH\_Archive\_StreamWrite\_Update输入数据，适合流式处理。
5. 调用OH\_Archive\_StreamWrite\_End结束流式压缩并获取结果信息。
6. 调用OH\_Archive\_StreamWrite\_Destroy销毁流式压缩写入器，释放资源。

```
static void InitStreamConfig(OH_Archive_Stream_Config *config)
{
    config->blockSize = 65536; // 设置block大小为65536 bytes
    config->threadNum = 4;     // 设置线程数为4
    config->method = OH_ARCHIVE_COMPRESS_DEFLATE; // 设置压缩算法为DEFLATE
    config->checksum = OH_ARCHIVE_CRC32;          // 设置校验方式为CRC32
}

static napi_value StreamCompress(napi_env env, napi_callback_info info)
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

    // 初始化流式压缩配置并创建流式压缩写入器
    OH_Archive_Stream_Config config = {0};
    InitStreamConfig(&config);
    OH_Archive_StreamWrite_Ctx ctx = OH_Archive_StreamWrite_Create(config);

    const int bufferSize = 32 * 1024 * 4 + 2; // 设置读取缓冲区大小
    unsigned char buffer[bufferSize];

    CreateRandomFile(inPathBuf, 1024 * 1024); // 创建1024K大小的测试文件

    // 打开输出文件，用于写入压缩后的数据
    FILE *fout = fopen(outPathBuf, "wb");
    if (!fout) {
        return nullptr;
    }
    OH_Archive_ErrCode result = OH_ARCHIVE_OK;
    result = OH_Archive_StreamWrite_SetCompressLevel(ctx, 6); // 设置压缩等级为6
    // 启动流式压缩，通过WriteCallBack回调将压缩数据写入文件
    result = OH_Archive_StreamWrite_Start(ctx, WriteCallBack, fout);
    uint64_t totalSize = 0;
    FILE *fi = fopen(inPathBuf, "rb");
    if (!fi) {
        (void)fclose(fout);
        return nullptr;
    }
    (void)fseek(fi, 0, SEEK_SET);

    // 循环读取文件数据并输入到压缩器进行压缩
    uint64_t read = 0;
    while ((read = fread(buffer, 1, bufferSize, fi)) > 0) {
        totalSize += read;
        result = OH_Archive_StreamWrite_Update(ctx, buffer, read);
        if (result != OH_ARCHIVE_OK) {
            break;
        }
    }
    (void)fclose(fi);
    // 结束流式压缩并获取压缩结果信息
    OH_Archive_StreamInfo streamInfo;
    result = OH_Archive_StreamWrite_End(ctx, &streamInfo);
    (void)fclose(fout);

    napi_value retVal = nullptr;
    napi_create_int32(env, result, &retVal);
    return retVal;
}
```

### 取消流式压缩

1. 调用OH\_Archive\_StreamWrite\_Create创建流式压缩写入器。
2. 调用OH\_Archive\_StreamWrite\_Start启动流式压缩。
3. 多次调用OH\_Archive\_StreamWrite\_Update输入压缩数据。
4. 调用OH\_Archive\_StreamWrite\_Cancel取消流式压缩。
5. 调用OH\_Archive\_StreamWrite\_End结束流式压缩。
6. 调用OH\_Archive\_StreamWrite\_Destroy销毁流式压缩写入器，释放资源。

```
static napi_value StreamCompressCancel(napi_env env, napi_callback_info info)
{
    // 获取输入文件路径和输出文件路径
    size_t argc = 2;
    napi_value argv[2] = {nullptr};
    napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);

    char inPathBuf[PATH_BUFFER_SIZE];
    char outPathBuf[PATH_BUFFER_SIZE];
    napi_get_value_string_utf8(env, argv[0], inPathBuf, sizeof(inPathBuf), nullptr);
    napi_get_value_string_utf8(env, argv[1], outPathBuf, sizeof(outPathBuf), nullptr);

    // 初始化流式压缩配置并创建流式压缩写入器
    OH_Archive_Stream_Config config;
    InitStreamConfig(&config);
    OH_Archive_StreamWrite_Ctx ctx = OH_Archive_StreamWrite_Create(config);

    CreateRandomFile(inPathBuf, 1024 * 1024); // 创建1024K大小的测试文件
    // 打开输出文件，用于写入压缩后的数据
    FILE *fout = fopen(outPathBuf, "wb");
    if (!fout) {
        return nullptr;
    }
    OH_Archive_ErrCode result = OH_ARCHIVE_OK;
    result = OH_Archive_StreamWrite_SetCompressLevel(ctx, 6); // 设置压缩等级为6
    // 启动流式压缩，通过WriteCallBack回调将压缩数据写入文件
    result = OH_Archive_StreamWrite_Start(ctx, WriteCallBack, fout);
    const int bufferSize = 32 * 1024 * 4 + 2; // 设置读取缓冲区大小
    unsigned char buffer[bufferSize];
    uint64_t totalSize = 0;
    FILE *fi = fopen(inPathBuf, "rb");
    if (!fi) {
        (void)fclose(fout);
        return nullptr;
    }

    // 循环读取文件数据并输入到压缩器进行压缩，累计数据量超过阈值时取消压缩
    uint64_t read = 0;
    uint64_t cancelThreshold = 2000; // 设置取消阈值为2000 bytes
    while ((read = fread(buffer, 1, bufferSize, fi)) > 0) {
        totalSize += read;
        if (totalSize > cancelThreshold) {
            // 累计数据量超过阈值，取消流式压缩
            result = OH_Archive_StreamWrite_Cancel(ctx);
            break;
        } else {
            result = OH_Archive_StreamWrite_Update(ctx, buffer, read);
        }
        if (result != OH_ARCHIVE_OK) {
            break;
        }
    }
    (void)fclose(fi);
    // 结束流式压缩，取消场景下不获取压缩结果信息
    result = OH_Archive_StreamWrite_End(ctx, nullptr);
    (void)fclose(fout);
    napi_value retVal = nullptr;
    napi_create_int32(env, result, &retVal);
    return retVal;
}
```

### 流式解压缩

1. 创建流式解压缩配置并调用OH\_Archive\_StreamRead\_Create创建流式解压缩读取器。需指定配置信息，需与压缩时的配置一致。
2. 调用OH\_Archive\_StreamRead\_Start启动流式解压缩。解压缩过程中通过输出回调函数处理解压缩后的原始数据。
3. 多次调用OH\_Archive\_StreamRead\_Update输入压缩数据进行解压缩。
4. 调用OH\_Archive\_StreamRead\_End结束流式解压缩并获取结果信息。
5. 调用OH\_Archive\_StreamRead\_Destroy销毁流式解压缩读取器，释放资源。

```
static napi_value StreamDecompress(napi_env env, napi_callback_info info)
{
    size_t argc = 0;
    napi_get_cb_info(env, info, &argc, nullptr, nullptr, nullptr);

    int ret;
    // 初始化流式压缩配置，解压缩配置需与压缩时保持一致
    OH_Archive_Stream_Config config = {0};
    InitStreamConfig(&config);

    // 先通过流式压缩生成测试用的压缩数据
    uint64_t srcSize = 30 * 1024; // 数据长度为30 * 1024
    uint64_t zipSize = srcSize * 1.1;
    void *zipBuffer = reinterpret_cast<void *>(malloc(zipSize));
    OH_Archive_StreamInfo compressInfo = {0, 0, 0};
    CreateFileWithStreamWrite(&config, srcSize, zipBuffer, &compressInfo);

    // 创建流式解压缩读取器
    OH_Archive_StreamRead_Ctx readCtx = OH_Archive_StreamRead_Create(config);

    uint64_t unzipSize = srcSize;
    void *unzipBuffer = reinterpret_cast<void *>(malloc(unzipSize));

    // 启动流式解压缩，通过WriteHandler回调将解压后的数据写入unzipBuffer
    ret = OH_Archive_StreamRead_Start(readCtx, WriteHandler, unzipBuffer);

    // 分段输入压缩数据进行解压缩
    uint8_t *unzPtr = (uint8_t *)zipBuffer;
    size_t unzLeft = compressInfo.totalOutSize;

    while (unzLeft > 0) {
        size_t unzchunk = (unzLeft > 1024) ? 1024 : unzLeft; // 每次最多处理1024 bytes
        ret = OH_Archive_StreamRead_Update(readCtx, unzPtr, unzchunk);

        unzPtr += unzchunk;
        unzLeft -= unzchunk;
    }

    // 结束流式解压缩并获取解压缩结果信息
    OH_Archive_StreamInfo decompressInfo2 = {};
    ret = OH_Archive_StreamRead_End(readCtx, &decompressInfo2);

    // 销毁流式解压缩读取器，释放资源
    OH_Archive_StreamRead_Destroy(readCtx);

    free(zipBuffer);
    free(unzipBuffer);
    napi_value result = nullptr;
    napi_create_int32(env, ret, &result);
    return result;
}
```

### 取消流式解压缩

1. 调用OH\_Archive\_StreamRead\_Create创建流式解压缩读取器。
2. 调用OH\_Archive\_StreamRead\_Start启动流式解压缩。
3. 多次调用OH\_Archive\_StreamRead\_Update输入压缩数据。
4. 调用OH\_Archive\_StreamRead\_Cancel取消流式解压缩。
5. 调用OH\_Archive\_StreamRead\_End结束流式解压缩。
6. 调用OH\_Archive\_StreamRead\_Destroy销毁流式解压缩读取器，释放资源。

```
static napi_value StreamDecompressCancel(napi_env env, napi_callback_info info)
{
    size_t argc = 0;
    napi_get_cb_info(env, info, &argc, nullptr, nullptr, nullptr);

    int ret;

    // 初始化流式压缩配置，解压缩配置需与压缩时保持一致
    OH_Archive_Stream_Config config = {0};
    InitStreamConfig(&config);

    // 先通过流式压缩生成测试用的压缩数据
    uint64_t srcSize = 30 * 1024; // 数据长度为30 * 1024
    uint64_t zipSize = srcSize * 1.1;
    void *zipBuffer = reinterpret_cast<void *>(malloc(zipSize));
    OH_Archive_StreamInfo compressInfo = {0, 0, 0};
    CreateFileWithStreamWrite(&config, srcSize, zipBuffer, &compressInfo);
    // 创建流式解压缩读取器
    OH_Archive_StreamRead_Ctx readCtx = OH_Archive_StreamRead_Create(config);

    uint64_t unzipSize = srcSize;
    void *unzipBuffer = reinterpret_cast<void *>(malloc(unzipSize));

    // 启动流式解压缩，通过WriteHandler回调将解压后的数据写入unzipBuffer
    ret = OH_Archive_StreamRead_Start(readCtx, WriteHandler, unzipBuffer);
    uint8_t *unzPtr = (uint8_t *)zipBuffer;
    size_t unzLeft = compressInfo.totalOutSize;

    // 分段输入压缩数据进行解压缩，剩余数据量小于阈值时取消解压缩
    while (unzLeft > 0) {
        size_t unzchunk = (unzLeft > 1024) ? 1024 : unzLeft; // 每次最多处理1024 bytes
        if (unzLeft < 20 * 1024) { // 剩余数据小于 20 * 1024 bytes时取消
            // 取消流式解压缩
            ret = OH_Archive_StreamRead_Cancel(readCtx);
            ret = OH_Archive_StreamRead_Update(readCtx, unzPtr, unzchunk);
            break;
        }
        ret = OH_Archive_StreamRead_Update(readCtx, unzPtr, unzchunk);

        unzPtr += unzchunk;
        unzLeft -= unzchunk;
    }

    // 结束流式解压缩，取消场景下不获取解压缩结果信息
    OH_Archive_StreamInfo *decompressInfo2 = nullptr;
    ret = OH_Archive_StreamRead_End(readCtx, decompressInfo2);
    // 销毁流式解压缩读取器，释放资源
    OH_Archive_StreamRead_Destroy(readCtx);

    free(zipBuffer);
    free(unzipBuffer);
    napi_value result = nullptr;
    napi_create_int32(env, ret, &result);
    return result;
}
```

## 调测验证关键点

* 流式压缩解压缩：验证分段输入的数据经过压缩后再解压缩，最终结果与原始数据完全一致。
* 取消流式压缩：验证取消操作后，压缩过程正常终止，无资源泄漏。
* 取消流式解压缩：验证取消操作后，解压缩过程正常终止，无资源泄漏。
