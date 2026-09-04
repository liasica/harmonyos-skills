---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/preview-filecacheboost
title: 通用文件缓存加速（C/C++）
breadcrumb: 指南 > 应用服务 > Preview Kit（文件预览服务） > 通用文件缓存加速（C/C++）
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:17+08:00
doc_updated_at: 2026-09-04
content_hash: sha256:c318d41f3f8d4c70c3025b8d3112b2e36b59fb4d7a889123aac629d331fa31f0
---

从6.1.0(23)版本开始，新增通用文件缓存加速功能。提供了缓存机制将文件的解码数据缓存到磁盘中，后续用户再次打开或浏览该文件，应用无需执行解码流程，可直接从磁盘中获取缓存的解码数据，省去耗时的解码时间。

## 接口说明

具体API说明详见[API参考](../harmonyos-references/openfileboost_preview.md)。

**表1** 文件缓存接口介绍

| 接口名 | 描述 |
| --- | --- |
| bool HMS\_Preview\_FileCacheBoost\_IsSupported (void) | 查询当前设备是否支持文件缓存加速功能。建议使用本接口检查，确认设备支持文件缓存加速功能后，再使用其他文件缓存加速接口如HMS\_FileCacheBoost\_Init等。 |
| FileCacheBoost\_ErrCode HMS\_FileCacheBoost\_Init (  const char\* path, size\_t pathLen, uint32\_t cacheUpperLimitMb, const char\* dbName, size\_t dbNameLen) | 初始化缓存路径、缓存容量上限、数据库名称。系统保证了线程并发安全控制，如需支持多进程并发场景，建议各进程使用不同的数据库文件名以保证访问安全性。 |
| FileCacheBoost\_ErrCode HMS\_FileCacheBoost\_AddObjectByKey (  const uint8\_t \*key, size\_t keyLen, const uint8\_t \*data, size\_t dataLen, uint32\_t weight) | 向系统添加缓存。计算的key为缓存的唯一标识。用户可传入缓存的权重，系统会参考该权重计算缓存的优先级进行容量管理，若开发者希望某个缓存对象优先保留，应为其分配较高的权重。 |
| FileCacheBoost\_ErrCode HMS\_FileCacheBoost\_GetObjectByKey (  const uint8\_t \*key, size\_t keyLen, uint8\_t \*\*data, size\_t \*dataLen) | 根据key值获取对应的缓存。 |
| FileCacheBoost\_ErrCode HMS\_FileCacheBoost\_RemoveObjectByKey (const uint8\_t \*key, size\_t keyLen) | 根据key值删除对应的缓存。 |
| FileCacheBoost\_ErrCode HMS\_FileCacheBoost\_ClearAllCache (void) | 删除当前所有的缓存。 |
| FileCacheBoost\_ErrCode HMS\_FileCacheBoost\_AddSerialObjectByKey (const uint8\_t \*key, size\_t keyLen, SerializeFunc func, const void \*object, uint32\_t weight) | 创建一个复杂类型对象的缓存项，通过传入自定义的序列化函数SerializeFunc对该象进行序列化处理，以便将其存储至磁盘并支持后续恢复。 |
| FileCacheBoost\_ErrCode HMS\_FileCacheBoost\_GetSerialObjectByKey (const uint8\_t \*key, size\_t keyLen, DeserializeFunc func, void \*\*object) | 根据指定的key值从缓存中获取复杂类型对象，并通过传入的反序列化函数DeserializeFunc将其还原为原始数据，从而获得完整的对象内容。 |

## 约束限制

支持的设备类型：PC/2in1，从26.0.0版本开始，新增支持tablet设备。

## 开发步骤

1. 添加对应的头文件。

   ```cpp
   #include "PreviewKit/file_cache_boost.h"
   #include <string>
   ```
2. 编写CMakeLists.txt，新增对通用文件缓存功能的依赖。

   ```cmake
   find_library(
       FILE_CACHE_BOOST
       NAMES libfile_cache_boost.so
       PATHS ${CMAKE_FIND_ROOT_PATH}/lib/aarch64-linux-ohos
   )
   # ...
   target_link_libraries(entry PUBLIC ${FILE_CACHE_BOOST})
   ```
3. 初始化操作，开发者可初始化缓存路径、缓存容量上限、数据库名称，系统会创建缓存路径和对应的数据库。

   ```
   napi_value OH_Init(napi_env env, napi_callback_info info) {
       // 获取参数数量
       size_t argc = 2; // 需要2个参数：path和cacheUpperLimitMb
       napi_value args[2];
       napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

       // 检查参数数量
       if (argc < 2) {
           napi_throw_error(env, nullptr, "Invalid number of arguments");
           return nullptr;
       }

       // 获取path
       size_t pathLen;
       char *path;
       napi_status status = napi_get_value_string_utf8(env, args[0], nullptr, 0, &pathLen);
       if (status != napi_ok) {
           napi_throw_error(env, nullptr, "Failed to get path length");
           return nullptr;
       }

       // 分配内存并获取path的内容
       path = new char[pathLen + 1];
       napi_get_value_string_utf8(env, args[0], path, pathLen + 1, &pathLen);

       // 获取cacheUpperLimitMb
       uint32_t cacheUpperLimitMb;
       napi_get_value_uint32(env, args[1], &cacheUpperLimitMb);

       // 设置固定的dbName参数
       const char *dbName = "hwcache"; // 硬编码数据库名称
       int32_t dbNameLen = static_cast<int32_t>(strlen(dbName));
       // path开发者可传入一个相对路径，如"ohcache"，cacheUpperLimitMb以MB为单位，2GB = 2048MB
       int result = HMS_FileCacheBoost_Init(path, pathLen, cacheUpperLimitMb, dbName, dbNameLen);
       if (result != FILE_CACHE_BOOST_SUCCESS) {
           // 初始化失败，开发者可自定义错误处理
       }
       // 释放path的内存
       delete[] path;

       // 将result转换为napi_value
       napi_value jsResult;
       napi_create_int32(env, result, &jsResult);

       return jsResult;
   }
   ```
4. 初始化完成后，开发者可实现添加缓存操作，将需要的缓存数据落盘，下次使用时直接获取缓存数据。

   ```
   napi_value OH_AddObjectByKey(napi_env env, napi_callback_info info) {
       // 获取参数数量
       size_t argc = 3;
       napi_value args[3];
       napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
       // 检查参数数量
       if (argc < 3) {
           napi_throw_error(env, nullptr, "Invalid number of arguments");
           return nullptr;
       }

       // 获取key
       size_t keyLen;
       size_t fillStrLen;
       uint8_t *key = GetStringArg(env, args[0], keyLen);
       // 获取填充字符串
       uint8_t *fillStr = GetStringArg(env, args[1], fillStrLen);
       if (!key || !fillStr) {
           delete[] key;
           delete[] fillStr;
           napi_throw_error(env, nullptr, "Key or fill string is empty");
           return nullptr;
       }

       // 获取内存大小
       uint32_t bufferMB;
       napi_get_value_uint32(env, args[2], &bufferMB);
       // 计算内存大小
       size_t bufferLen = static_cast<size_t>(bufferMB) * 1024 * 1024;
       // 分配内存
       uint8_t *buffer = new uint8_t[bufferLen];

       // 用填充字符串填充内存
       for (size_t i = 0; i < bufferLen; i++) {
           buffer[i] = fillStr[i % fillStrLen]; // 用填充字符串循环填充
       }

       OH_LOG_Print(LOG_APP, LOG_INFO, LOG_DOMAIN, LOG_TAG, "add Get Key is : %{public}s, KeyLen: %{public}zu", key,
                keyLen);
       uint32_t weight = 0;
       int result = isEableCancel
           ? ExecuteAddWithCancel(key, keyLen, buffer, bufferLen, weight)
           : HMS_FileCacheBoost_AddObjectByKey(key, keyLen, buffer, bufferLen, weight);

       v1.push_back(*key);
       delete[] key;
       delete[] fillStr;
       delete[] buffer;
       napi_value jsResult;
       napi_create_int32(env, result, &jsResult);
       return jsResult;
   }
   ```
5. 添加缓存完成后，开发者使用时调用HMS\_FileCacheBoost\_GetObjectByKey直接获取缓存数据。

   ```cpp
   napi_value OH_GetObjectByKey(napi_env env, napi_callback_info info) {
       // 获取参数数量
       size_t argc = 1;
       napi_value args[1];
       napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

       // 检查参数数量
       if (argc < 1) {
           napi_throw_error(env, nullptr, "Invalid number of arguments");
           return nullptr;
       }

       // 获取key和keyLen
       size_t keyLen;
       char *key;
       napi_get_value_string_utf8(env, args[0], nullptr, 0, &keyLen);
       key = new char[keyLen + 1];
       napi_get_value_string_utf8(env, args[0], key, keyLen + 1, &keyLen);
       OH_LOG_Print(LOG_APP, LOG_INFO, LOG_DOMAIN, LOG_TAG, "Get Key is : %{public}s", key);
       OH_LOG_Print(LOG_APP, LOG_INFO, LOG_DOMAIN, LOG_TAG, "Get KeyLen is : %{public}zu", keyLen);

       uint8_t *data = new uint8_t[500];
       size_t dataLen = 0;

       // 调用HMS_FileCacheBoost_GetObjectByKey
       int result = HMS_FileCacheBoost_GetObjectByKey(reinterpret_cast<uint8_t *>(key), keyLen, &data, &dataLen);

       OH_LOG_Print(LOG_APP, LOG_INFO, LOG_DOMAIN, LOG_TAG, "Data length: %{public}zu", dataLen);
       if (result != FILE_CACHE_BOOST_SUCCESS) {
           OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_DOMAIN, LOG_TAG, "key is no exits!");
           HMS_FileCacheBoost_FreeObject(data);
           delete[] key;
           napi_value jsResult;
           napi_create_int32(env, result, &jsResult);
           return jsResult;
       }
       if (data == nullptr || dataLen == 0) {
           OH_LOG_Print(LOG_APP, LOG_INFO, LOG_DOMAIN, LOG_TAG, "get object fail! and Data length: %{public}zu", dataLen);
           HMS_FileCacheBoost_FreeObject(data);
           delete[] key;
           napi_value jsResult;
           napi_create_int32(env, result, &jsResult);
           return jsResult;
       }
       size_t printLen = std::min(dataLen, static_cast<size_t>(100));
       OH_LOG_Print(LOG_APP, LOG_INFO, LOG_DOMAIN, LOG_TAG, "First 100 bytes of data:");
       for (size_t i = 0; i < printLen; ++i) {
           OH_LOG_Print(LOG_APP, LOG_INFO, LOG_DOMAIN, LOG_TAG, "Byte[%{public}zu]: %{public}c", i, data[i]);
       }
       HMS_FileCacheBoost_FreeObject(data);
       delete[] key;
       napi_value jsResult;
       napi_create_int32(env, result, &jsResult);
       return jsResult;
   }
   ```
6. 如果开发者需要删除不需要再使用的缓存，可以调用HMS\_FileCacheBoost\_RemoveObjectByKey。

   ```cpp
   napi_value OH_RemoveObjectByKey(napi_env env, napi_callback_info info) {
       // 获取参数数量
       size_t argc = 1; // 只需要一个参数：key
       napi_value args[1];
       napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

       // 检查参数数量
       if (argc < 1) {
           napi_throw_error(env, nullptr, "Invalid number of arguments");
           return nullptr;
       }

       // 获取key
       napi_value keyArg = args[0];

       // 获取key的字符串信息
       size_t keyLen;
       napi_get_value_string_utf8(env, keyArg, nullptr, 0, &keyLen); // 获取key的长度

       // 分配缓冲区并获取key的内容
       char *keyData = new char[keyLen + 1];
       napi_get_value_string_utf8(env, keyArg, keyData, keyLen + 1, &keyLen);

       // 调用HMS_FileCacheBoost_RemoveObjectByKey，删除缓存
       int result = HMS_FileCacheBoost_RemoveObjectByKey(reinterpret_cast<uint8_t *>(keyData), keyLen);
       // 新增key不存在的返回值
       if (result != FILE_CACHE_BOOST_SUCCESS) {
           // 删除失败，开发者可自定义错误处理
           OH_LOG_Print(LOG_APP, LOG_INFO, LOG_DOMAIN, LOG_TAG, "RemoveObjectByKey error");
       }
       // 释放缓冲区
       delete[] keyData;

       // 返回结果
       napi_value jsResult;
       napi_create_int32(env, result, &jsResult);
       return jsResult;
   }
   ```
7. 如果开发者需要清除所有缓存，可以调用HMS\_FileCacheBoost\_ClearAllCache。

   ```cpp
   napi_value OH_ClearAllCache(napi_env env, napi_callback_info info) {
       int result = HMS_FileCacheBoost_ClearAllCache();

       // 返回结果
       napi_value jsResult;
       napi_create_int32(env, result, &jsResult);
       return jsResult;
   }
   ```
8. 当一个线程尝试删除数据对象的同时，有其他线程对其进行HMS\_FileCacheBoost\_AddObjectByKey操作， 调用HMS\_FileCacheBoost\_CancelOngoingIOByKey取消key对应的缓存对象当前正在进行的I/O操作。

   ```cpp
   napi_value OH_CancelAllOperation(napi_env env, napi_callback_info info) {
       // 获取参数数量
       size_t argc = 1; // 只需要一个参数：key
       napi_value args[1];
       napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

       // 检查参数数量
       if (argc < 1) {
           napi_throw_error(env, nullptr, "Invalid number of arguments");
           return nullptr;
       }

       // 获取key的字符串信息
       size_t keyLen;
       napi_get_value_string_utf8(env, args[0], nullptr, 0, &keyLen); // 获取key的长度

       // 分配缓冲区并获取key的内容
       uint8_t *keyData = new uint8_t[keyLen + 1];
       napi_get_value_string_utf8(env, args[0], reinterpret_cast<char *>(keyData), keyLen + 1, &keyLen);
       OH_LOG_Print(LOG_APP, LOG_INFO, LOG_DOMAIN, LOG_TAG, "OH_CancelAllOperation keyArg: %{public}s",
                    reinterpret_cast<uint8_t *>(keyData));
       // 调用HMS_FileCacheBoost_CancelOngoingIOByKey
       int result =
           HMS_FileCacheBoost_CancelOngoingIOByKey(reinterpret_cast<uint8_t *>(keyData), static_cast<size_t>(keyLen));
       OH_LOG_Print(LOG_APP, LOG_INFO, LOG_DOMAIN, LOG_TAG, "OH_CancelAllOperation result: %{public}d", result);
       delete[] keyData;

       // 返回结果
       napi_value jsResult;
       napi_create_int32(env, result, &jsResult);
       return jsResult;
   }
   ```
9. 如果缓存数据依附于一个复杂类的对象，该类中可能包含其他复杂对象数据结构、指针等不可控数据，不一并保存，落盘后无法恢复。对于这种复杂类型数据，需要开发者提供序列化函数。

   ```cpp
   // 序列化函数：将ImageData对象序列化为字节流
   FileCacheBoost_CbErrCode Serialize(const void *object, WriteFunc write, struct CacheKey *key) {
       // 1. 参数校验
       if (object == nullptr || write == nullptr || key == nullptr) {
           OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_DOMAIN, LOG_TAG, "Serialize: invalid parameters!");
           return FILE_CACHE_BOOST_CALLBACK_FAILURE;
       }
       const struct ImageData* img = static_cast<const struct ImageData*>(object);
       // 2. 数据有效性检查
       if (img->width == 0 || img->height == 0 || img->pixels == nullptr) {
           OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_DOMAIN, LOG_TAG,
                        "Serialize: invalid image data! width=%{public}u, height=%{public}u",
                        img->width, img->height);
           return FILE_CACHE_BOOST_CALLBACK_FAILURE;
       }
       // 3. 计算数据大小
       size_t metaDataSize = sizeof(uint32_t) * 2;  // width + height
       size_t imageSize = img->width * img->height * sizeof(uint8_t);
       size_t totalSize = metaDataSize + imageSize;
       // 4. 分配缓冲区（一次写入策略，性能优化）
       uint8_t *buffer = new (std::nothrow) uint8_t[totalSize];
       if (buffer == nullptr) {
           OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_DOMAIN, LOG_TAG,
                        "Serialize: memory allocation failed! size=%{public}zu", totalSize);
           return FILE_CACHE_BOOST_CALLBACK_FAILURE;
       }
       // 5. 填充元数据（小端序）
       uint8_t *ptr = buffer;
       // 写入width（4字节，小端序）
       *ptr++ = static_cast<uint8_t>(img->width & 0xFF);
       *ptr++ = static_cast<uint8_t>((img->width >> 8) & 0xFF);
       *ptr++ = static_cast<uint8_t>((img->width >> 16) & 0xFF);
       *ptr++ = static_cast<uint8_t>((img->width >> 24) & 0xFF);
       // 写入height（4字节，小端序）
       *ptr++ = static_cast<uint8_t>(img->height & 0xFF);
       *ptr++ = static_cast<uint8_t>((img->height >> 8) & 0xFF);
       *ptr++ = static_cast<uint8_t>((img->height >> 16) & 0xFF);
       *ptr++ = static_cast<uint8_t>((img->height >> 24) & 0xFF);
       // 6. 复制像素数据
       std::copy(img->pixels, img->pixels + imageSize, ptr);
       // 7. 一次性写入所有数据（性能优化）
       FileCacheBoost_ErrCode errorCode = write(buffer, totalSize, key);
       // 8. 释放缓冲区
       delete[] buffer;
       if (errorCode == FILE_CACHE_BOOST_SUCCESS) {
           OH_LOG_Print(LOG_APP, LOG_INFO, LOG_DOMAIN, LOG_TAG,
                        "Serialize success! width=%{public}u, height=%{public}u, size=%{public}zu",
                        img->width, img->height, totalSize);
           return FILE_CACHE_BOOST_CALLBACK_SUCCESS;
       } else {
           OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_DOMAIN, LOG_TAG,
                        "Serialize: write failed! errorCode=%{public}d", errorCode);
           return FILE_CACHE_BOOST_CALLBACK_FAILURE;
       }
   }
   ```
10. 调用HMS\_FileCacheBoost\_AddSerialObjectByKey添加复杂数据的序列化缓存。

    ```cpp
    napi_value OH_AddSerialObjectByKey(napi_env env, napi_callback_info info) {
        size_t argc = 3;
        napi_value args[3];
        napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
        // 检查参数数量
        if (argc < 3) {
            napi_throw_error(env, nullptr, "Invalid number of arguments");
            return nullptr;
        }
        // 获取key
        char* key1;
        size_t keyLen;
        napi_get_value_string_utf8(env, args[0], nullptr, 0, &keyLen);
        key1 = new char[keyLen + 1];
        napi_get_value_string_utf8(env, args[0], key1, keyLen + 1, &keyLen);
        // 获取width和height（作为字符串接收，然后转换为数字）
        char* widthStr = nullptr;
        size_t widthStrLen = 0;
        napi_get_value_string_utf8(env, args[1], nullptr, 0, &widthStrLen);
        widthStr = new char[widthStrLen + 1];
        napi_get_value_string_utf8(env, args[1], widthStr, widthStrLen + 1, &widthStrLen);
        uint32_t width = static_cast<uint32_t>(atoi(widthStr));
        char* heightStr = nullptr;
        size_t heightStrLen = 0;
        napi_get_value_string_utf8(env, args[2], nullptr, 0, &heightStrLen);
        heightStr = new char[heightStrLen + 1];
        napi_get_value_string_utf8(env, args[2], heightStr, heightStrLen + 1, &heightStrLen);
        uint32_t height = static_cast<uint32_t>(atoi(heightStr));
        // 构造ImageData对象
        struct ImageData* img = new (std::nothrow) ImageData();
        if (img == nullptr) {
            OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_DOMAIN, LOG_TAG, "OH_AddSerialObjectByKey: ImageData allocation failed!");
            delete[] widthStr;
            delete[] heightStr;
            delete[] key1;
            napi_value jsResult;
            napi_create_int32(env, FILE_CACHE_BOOST_ERROR_NOMEM, &jsResult);
            return jsResult;
        }
        img->width = width;
        img->height = height;
        img->pixels = new (std::nothrow) uint8_t[width * height];
        if (img->pixels == nullptr) {
            OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_DOMAIN, LOG_TAG, "OH_AddSerialObjectByKey: pixels allocation failed!");
            delete img;
            delete[] widthStr;
            delete[] heightStr;
            delete[] key1;
            napi_value jsResult;
            napi_create_int32(env, FILE_CACHE_BOOST_ERROR_NOMEM, &jsResult);
            return jsResult;
        }
        // 填充测试数据（'a', 'b', 'c'循环）
        for (size_t i = 0; i < width * height; i++) {
            img->pixels[i] = 'a' + (i % 3);
        }
        OH_LOG_Print(LOG_APP, LOG_INFO, LOG_DOMAIN, LOG_TAG,
                     "HMS_FileCacheBoost_AddSerialObjectByKey: key=%{public}s, width=%{public}u, height=%{public}u",
                     key1, width, height);
        uint32_t weight = 100;
        // 添加复杂类数据缓存
        int result = HMS_FileCacheBoost_AddSerialObjectByKey(
            reinterpret_cast<uint8_t*>(key1), keyLen, Serialize, img, weight
        );
        // 释放临时对象（数据已序列化到缓存）
        delete[] img->pixels;
        delete img;
        // 将result转换为napi_value
        napi_value jsResult;
        napi_create_int32(env, result, &jsResult);
        delete[] widthStr;
        delete[] heightStr;
        delete[] key1;
        return jsResult;
    }
    ```
11. 对于使用序列化缓存的数据，获取时需要开发者提供反序列化函数。

    ```cpp
    // 反序列化函数：从字节流恢复ImageData对象
    FileCacheBoost_CbErrCode Deserialize(void **object, ReadFunc read, struct CacheKey *key) {
        // 1. 参数校验
        if (object == nullptr || read == nullptr || key == nullptr) {
            OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_DOMAIN, LOG_TAG, "Deserialize: invalid parameters!");
            return FILE_CACHE_BOOST_CALLBACK_FAILURE;
        }
        // 2. 读取元数据头部（8字节：width + height）
        uint8_t header[8];
        size_t headerSize = 8;
        FileCacheBoost_ErrCode errorCode = read(header, &headerSize, key);
        if (errorCode != FILE_CACHE_BOOST_SUCCESS || headerSize != 8) {
            OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_DOMAIN, LOG_TAG,
                         "Deserialize: read header failed! errorCode=%{public}d, size=%{public}zu",
                         errorCode, headerSize);
            return FILE_CACHE_BOOST_CALLBACK_FAILURE;
        }
        // 3. 解析元数据（小端序）
        uint32_t width = static_cast<uint32_t>(
            header[0] | (header[1] << 8) | (header[2] << 16) | (header[3] << 24)
        );
        uint32_t height = static_cast<uint32_t>(
            header[4] | (header[5] << 8) | (header[6] << 16) | (header[7] << 24)
        );
        // 4. 数据有效性检查
        if (width == 0 || height == 0 || width > 10000 || height > 10000) {
            OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_DOMAIN, LOG_TAG,
                         "Deserialize: invalid dimensions! width=%{public}u, height=%{public}u",
                         width, height);
            return FILE_CACHE_BOOST_CALLBACK_FAILURE;
        }
        // 5. 计算图像数据大小
        size_t imageSize = width * height * sizeof(uint8_t);
        // 6. 分配ImageData结构体内存
        struct ImageData* img = new (std::nothrow) struct ImageData;
        if (img == nullptr) {
            OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_DOMAIN, LOG_TAG,
                         "Deserialize: ImageData allocation failed!");
            return FILE_CACHE_BOOST_CALLBACK_FAILURE;
        }
        // 7. 分配像素数据内存
        img->pixels = new (std::nothrow) uint8_t[imageSize];
        if (img->pixels == nullptr) {
            OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_DOMAIN, LOG_TAG,
                         "Deserialize: pixels allocation failed! size=%{public}zu", imageSize);
            delete img;
            return FILE_CACHE_BOOST_CALLBACK_FAILURE;
        }
        // 8. 设置图像属性
        img->width = width;
        img->height = height;
        // 9. 读取像素数据
        size_t pixelSize = imageSize;
        errorCode = read(img->pixels, &pixelSize, key);
        if (errorCode != FILE_CACHE_BOOST_SUCCESS || pixelSize != imageSize) {
            OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_DOMAIN, LOG_TAG,
                         "Deserialize: read pixels failed! errorCode=%{public}d, expected=%{public}zu, actual=%{public}zu",
                         errorCode, imageSize, pixelSize);
            delete[] img->pixels;
            delete img;
            return FILE_CACHE_BOOST_CALLBACK_FAILURE;
        }
        // 10. 正确设置输出参数（修复原bug）
        *object = static_cast<void*>(img);
        OH_LOG_Print(LOG_APP, LOG_INFO, LOG_DOMAIN, LOG_TAG,
                     "Deserialize success! width=%{public}u, height=%{public}u, size=%{public}zu",
                     width, height, imageSize);
        return FILE_CACHE_BOOST_CALLBACK_SUCCESS;
    }
    ```
12. 调用HMS\_FileCacheBoost\_GetSerialObjectByKey获取缓存数据。

    ```cpp
    napi_value OH_GetSerialObjectByKey(napi_env env, napi_callback_info info) {
        // 获取参数数量
        size_t argc = 1;
        napi_value args[1];
        napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

        // 检查参数数量
        if (argc < 1) {
            napi_throw_error(env, nullptr, "Invalid number of arguments");
            return nullptr;
        }
        char *key;
        size_t keyLen;
        napi_get_value_string_utf8(env, args[0], nullptr, 0, &keyLen);
        key = new char[keyLen + 1];
        napi_get_value_string_utf8(env, args[0], key, keyLen + 1, &keyLen);

        // 定义object
        void *object = nullptr;
        // 调用HMS_FileCacheBoost_GetSerialObjectByKey获取复杂类数据缓存
        int result = HMS_FileCacheBoost_GetSerialObjectByKey(
            reinterpret_cast<uint8_t*>(key), keyLen, Deserialize, &object
        );
        if (result == FILE_CACHE_BOOST_SUCCESS && object != nullptr) {
            // 获取成功，输出图像信息
            struct ImageData* img = static_cast<struct ImageData*>(object);
            OH_LOG_Print(LOG_APP, LOG_INFO, LOG_DOMAIN, LOG_TAG,
                         "GetSerialObject success! width=%{public}u, height=%{public}u",
                         img->width, img->height);
            // 打印部分像素数据（前100字节）
            size_t printLen = std::min(img->width * img->height, static_cast<uint32_t>(100));
            OH_LOG_Print(LOG_APP, LOG_INFO, LOG_DOMAIN, LOG_TAG, "First %{public}zu pixels:", printLen);
            for (size_t i = 0; i < printLen; i++) {
                OH_LOG_Print(LOG_APP, LOG_INFO, LOG_DOMAIN, LOG_TAG,
                             "Pixel[%{public}zu]=%{public}c", i, img->pixels[i]);
            }
            // 释放ImageData对象内存
            delete[] img->pixels;
            delete img;
        } else {
            OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_DOMAIN, LOG_TAG,
                         "GetSerialObject failed! result=%{public}d", result);
        }
        // 释放内存
        delete[] key;

        // 返回结果
        napi_value jsResult;
        napi_create_int32(env, result, &jsResult);
        return jsResult;
    }
    ```
