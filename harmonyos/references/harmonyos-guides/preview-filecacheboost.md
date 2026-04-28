---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/preview-filecacheboost
title: 通用文件缓存加速（C/C++）
breadcrumb: 指南 > 应用服务 > Preview Kit（文件预览服务） > 通用文件缓存加速（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b744000e5856c7f293d351b2f74ebbdf6622c2498141fb65e1b004fcd3ed56ce
---

从6.1.0(23)版本开始，新增通用文件缓存加速功能。提供了缓存机制将文件的解码数据缓存到磁盘中，后续用户再次打开或浏览该文件，应用无需执行解码流程，可直接从磁盘中获取缓存的解码数据，省去耗时的解码时间。

## 接口说明

具体API说明详见[API参考](../harmonyos-references/openfileboost_preview.md)。

**表1** 文件缓存接口介绍

| 接口名 | 描述 |
| --- | --- |
| FileCacheBoost\_ErrCode HMS\_FileCacheBoost\_Init (  const char\* path, size\_t pathLen, uint32\_t cacheUpperLimitMb, const char\* dbName, size\_t dbNameLen) | 初始化缓存路径、缓存容量上限、数据库名称。系统保证了线程并发安全控制，如需支持多进程并发场景，建议各进程使用不同的数据库文件名以保证访问安全性。 |
| FileCacheBoost\_ErrCode HMS\_FileCacheBoost\_AddObjectByKey (  const uint8\_t \*key, size\_t keyLen, const uint8\_t \*data, size\_t dataLen, uint32\_t weight) | 向系统添加缓存。计算的key为缓存的唯一标识。用户可传入缓存的权重，系统会参考该权重计算缓存的优先级进行容量管理，若开发者希望某个缓存对象优先保留，应为其分配较高的权重。 |
| FileCacheBoost\_ErrCode HMS\_FileCacheBoost\_GetObjectByKey (  const uint8\_t \*key, size\_t keyLen, uint8\_t \*\*data, size\_t \*dataLen) | 根据key值获取对应的缓存。 |
| FileCacheBoost\_ErrCode HMS\_FileCacheBoost\_RemoveObjectByKey (const uint8\_t \*key, size\_t keyLen) | 根据key值删除对应的缓存。 |
| FileCacheBoost\_ErrCode HMS\_FileCacheBoost\_ClearAllCache (void) | 删除当前所有的缓存。 |
| FileCacheBoost\_ErrCode HMS\_FileCacheBoost\_AddSerialObjectByKey (const uint8\_t \*key, size\_t keyLen, SerializeFunc func, const void \*object, uint32\_t weight) | 创建一个复杂类型对象的缓存项，通过传入自定义的序列化函数SerializeFunc对该象进行序列化处理，以便将其存储至磁盘并支持后续恢复。 |
| FileCacheBoost\_ErrCode HMS\_FileCacheBoost\_GetSerialObjectByKey (const uint8\_t \*key, size\_t keyLen, DeserializeFunc func, void \*\*object) | 根据指定的key值从缓存中获取复杂类型对象，并通过传入的反序列化函数DeserializeFunc将其还原为原始数据，从而获得完整的对象内容。 |

## 开发准备

需要先通过[Syscap](../harmonyos-references/syscap.md#判断-api-是否可以使用)查询您的目标设备是否支持SystemCapability.PCService.OpenFileBoost系统能力，当前仅在2in1设备上支持该能力。

## 开发步骤

1. 添加对应的头文件。

   ```
   1. #include "PreviewKit/file_cache_boost.h"
   2. #include <string>
   ```
2. 编写CMakeLists.txt，新增对通用文件缓存功能的依赖。

   ```
   1. target_link_libraries(entry PUBLIC
   2. libfile_cache_boost.so
   3. )
   ```
3. 初始化操作，开发者可初始化缓存路径、缓存容量上限、数据库名称，系统会创建缓存路径和对应的数据库。

   ```
   1. // 开发者可传入一个相对路径
   2. const char* path = "ohcache";
   3. size_t pathLen = strlen(path);
   4. // 以MB为单位，2GB = 2048MB
   5. uint32_t cacheUpperLimitMb = 2048;
   6. const char* dbName = "cache";
   7. size_t dbNameLen = strlen(dbName);
   8. FileCacheBoost_ErrCode res = HMS_FileCacheBoost_Init(path, pathLen,
   9. cacheUpperLimitMb, dbName, dbNameLen);
   10. if (res != FILE_CACHE_BOOST_SUCCESS) {
   11. // 初始化失败，开发者可自定义错误处理
   12. }
   ```
4. 初始化完成后，开发者可实现添加、获取和删除等操作，将需要的缓存数据落盘，下次使用时直接获取缓存数据。

   ```
   1. // 添加缓存
   2. std::string keyStr = "test_000";
   3. std::vector<uint8_t> keyVector(keyStr.begin(), keyStr.end());
   4. size_t keyLen = keyStr.size();
   5. uint8_t *key = keyVector.data();
   6. uint8_t *data = new uint8_t[90 * 1024];
   7. size_t dataLen = 90 * 1024;
   8. uint32_t weight = 100;
   9. // 用 abc 填充
   10. for (size_t i = 0; i < dataLen; i++) {
   11. data[i] = 'a' + (i % 3);
   12. }
   13. FileCacheBoost_ErrCode res = HMS_FileCacheBoost_AddObjectByKey(key, keyLen, data, dataLen, weight);
   14. if (res == FILE_CACHE_BOOST_SUCCESS) {
   15. // 添加缓存成功，开发者后续可使用该缓存
   16. } else if (res == FILE_CACHE_BOOST_ERROR_KEY_EXIST) {
   17. // key缓存已经存在，如果开发者需要对缓存进行修改，需要先删除后再添加
   18. HMS_FileCacheBoost_RemoveObjectByKey(key, keyLen);
   19. } else if (res == FILE_CACHE_BOOST_ERROR_NOT_INITIALIZED) {
   20. // 未初始化，开发者可初始化后执行
   21. } else if (res == FILE_CACHE_BOOST_ERROR_EXCEED_LIMIT) {
   22. // 单个缓存大于容量上限，无法添加
   23. } else {
   24. // 添加缓存失败，开发者可自定义错误处理
   25. }

   27. // 获取缓存
   28. uint8_t *revData = new uint8_t[90 * 1024 * 1024];
   29. FileCacheBoost_ErrCode res = HMS_FileCacheBoost_GetObjectByKey(key, keyLen, &revData, &dataLen);
   30. if (res == FILE_CACHE_BOOST_SUCCESS) {
   31. // 获取缓存数据成功，开发者可直接使用该缓存数据执行后续逻辑

   33. // 使用完成后，开发者可以释放系统分配的内存空间
   34. HMS_FileCacheBoost_FreeObject(revData);
   35. } else if (res == FILE_CACHE_BOOST_ERROR_KEY_NOT_FOUND) {
   36. // key值不存在，开发者可对该key进行添加缓存
   37. HMS_FileCacheBoost_AddObjectByKey(key, keyLen, data, dataLen, weight);
   38. } else if (res == FILE_CACHE_BOOST_ERROR_NOT_INITIALIZED) {
   39. // 未初始化，开发者可初始化后执行
   40. } else {
   41. // 获取缓存失败，开发者可自定义错误处理
   42. }

   44. // 删除缓存
   45. FileCacheBoost_ErrCode res = HMS_FileCacheBoost_RemoveObjectByKey(key, keyLen);
   46. // 新增key不存在的返回值
   47. if (res != FILE_CACHE_BOOST_SUCCESS) {
   48. // 删除失败，开发者可自定义错误处理
   49. }
   ```
5. 如果开发者需要清除所有缓存，可以调用HMS\_FileCacheBoost\_ClearAllCache。

   ```
   1. FileCacheBoost_ErrCode res = HMS_FileCacheBoost_ClearAllCache();
   2. if (res != FILE_CACHE_BOOST_SUCCESS) {
   3. // 删除失败，开发者可自定义错误处理
   4. }
   ```
6. 如果缓存数据依附于一个复杂类的对象，该类中可能包含其他复杂对象数据结构、指针等不可控数据，不一并保存，落盘后无法恢复。对于这种复杂类型数据需要开发者提供序列化和反序列化函数，然后调用HMS\_FileCacheBoost\_AddSerialObjectByKey和HMS\_FileCacheBoost\_GetSerialObjectByKey实现添加和获取缓存。

   ```
   1. // 自定义的图片结构体样例
   2. struct SimpleImage {
   3. int width;
   4. int height;
   5. int format;
   6. unsigned char* pixels; // RGB 三通道或灰度图等
   7. };

   9. static FileCacheBoost_CbErrCode serialize(const void* object, WriteFunc writeFunc, struct CacheKey* key) {
   10. const struct SimpleImage* img = (const struct SimpleImage*)object;

   12. // 写头部信息: width, height, format
   13. int header[3] = {img->width, img->height, img->format};
   14. if (writeFunc(header, sizeof(header), key) != 0) {
   15. return FILE_CACHE_BOOST_CALLBACK_FAILURE;
   16. }

   18. // 计算像素总大小
   19. int dataSize = img->width * img->height *
   20. ((img->format == 1) ? 1 : 3); // 格式1为灰度图，其它当作RGB处理

   22. // 写入像素数据
   23. if (writeFunc(img->pixels, dataSize, key) != 0) {
   24. return FILE_CACHE_BOOST_CALLBACK_FAILURE;
   25. }
   26. return FILE_CACHE_BOOST_CALLBACK_SUCCESS;
   27. }
   28. // 添加复杂类数据缓存
   29. std::string keyStr = "test_000";
   30. std::vector<uint8_t> keyVector(keyStr.begin(), keyStr.end());
   31. size_t keyLen = keyStr.size();
   32. uint8_t *key = keyVector.data();
   33. void *object = nullptr;
   34. uint32_t weight = 100;
   35. HMS_FileCacheBoost_AddSerialObjectByKey(key, keyLen, serialize, object, weight);

   37. static FileCacheBoost_CbErrCode deserialize(void** object, ReadFunc readFunc, struct CacheKey* key) {
   38. // width, height, format
   39. int header[3];
   40. size_t headerSize = sizeof(header);
   41. if (readFunc(header, &headerSize, key) != 0) {
   42. return FILE_CACHE_BOOST_CALLBACK_FAILURE;
   43. }

   45. int w = header[0], h = header[1], fmt = header[2];
   46. int bytesPerPixel = (fmt == 1) ? 1 : 3;
   47. int dataSize = w * h * bytesPerPixel;

   49. // 分配像素内存
   50. unsigned char* pixelData = (unsigned char*)malloc(dataSize);
   51. if (!pixelData) {
   52. return FILE_CACHE_BOOST_CALLBACK_FAILURE;
   53. }

   55. size_t pixelSize = dataSize;
   56. if (readFunc(pixelData, &pixelSize, key) != 0 || pixelSize != (size_t)dataSize) {
   57. free(pixelData);
   58. return FILE_CACHE_BOOST_CALLBACK_FAILURE;
   59. }

   61. // 构造新结构体
   62. struct SimpleImage* newImg = (struct SimpleImage*)malloc(sizeof(struct SimpleImage));
   63. if (!newImg) {
   64. free(pixelData);
   65. return FILE_CACHE_BOOST_CALLBACK_FAILURE;
   66. }

   68. newImg->width = w;
   69. newImg->height = h;
   70. newImg->format = fmt;
   71. newImg->pixels = pixelData;

   73. *object = newImg;
   74. return FILE_CACHE_BOOST_CALLBACK_SUCCESS;
   75. }
   76. // 获取复杂类数据缓存
   77. HMS_FileCacheBoost_GetSerialObjectByKey(key, keyLen, deserialize, &object);
   ```
