---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-encoding-native
title: 图片编码
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(依赖JS对象)(不再推荐) > 图片编码
category: harmonyos-guides
scraped_at: 2026-04-29T13:35:22+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:7264d7b0c8da5ef763e569263ec2de8d9bb082ba00c5ee3a0c787f97f3f7aa0f
---

说明

当前开发指导使用的接口为[Image](../harmonyos-references/capi-image.md)模块下的C API，可完成图片编解码，图片接收器，处理图像数据等功能。这部分API在API version 11之前发布，在后续的版本不再增加新功能，**不再推荐使用**。

开发者可使用[Image\_NativeModule](../harmonyos-references/capi-image-nativemodule.md)模块下的C API，不仅提供上述图片框架基础功能，还可以完成多图编解码等新特性，相关开发指导请参考[图片开发指导(C/C++)](image-source-c.md)节点下的内容。这部分API从API version 12开始支持，并将持续演进，**推荐开发者使用**。

两套C API不建议同时使用，在部分场景下存在不兼容的问题。

开发者可以调用本模块的Native API接口，完成图片编码，即将PixelMap压缩成不同格式的图片文件。

当前支持编码为JPEG、WebP、PNG和 HEIF（不同硬件设备支持情况不同）格式。

**适用场景**

* 图片编码转换。

  通过传入ImageSource，封装成想要的格式。
* 图片编辑。

  编辑PixelMap后导出图片文件的场景，需要编码成对应图片格式文件。

## 开发指导

详细的API说明请参考文件[image\_packer\_mdk.h](../harmonyos-references/capi-image-packer-mdk-h.md)。

参考以下示例代码，完成图片编码的全流程，包括：创建编码器、初始化资源、编码过程、销毁资源。

在应用开发过程中，开发者应按一定顺序调用方法，执行对应操作，否则系统可能会抛出异常或生成其他未定义的行为。具体顺序可参考下列开发步骤及对应说明。

如下为图片编码调用关系图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/6soAkzX1Ru-vSfjt6oUjtA/zh-cn_image_0000002558765092.png?HW-CC-KV=V1&HW-CC-Date=20260429T053520Z&HW-CC-Expire=86400&HW-CC-Sign=917030B4D5283F2955863E05103CE736EF98DF19DBBED64F2916F3B02A93A1E6)

### 在 CMake 脚本中链接动态库

```
1. target_link_libraries(entry PUBLIC libace_napi.z.so)
2. target_link_libraries(entry PUBLIC libimage_packer_ndk.z.so)
```

### 开发步骤

1. 引入编码器头文件：image\_packer\_mdk.h。

   ```
   1. // 引入编码器image_packer_mdk.h头文件。
   2. #include <multimedia/image_framework/image_packer_mdk.h>
   ```
2. 创建编码器实例对象。

   应用需要napi\_env来创建编码器。

   ```
   1. // 使用napi_value 承接创建的编码器对象。
   2. napi_value packer;
   3. // 通过 napi_env 创建编码器，返回result为 IMAGE_RESULT_SUCCESS则创建成功。
   4. int32_t result = OH_ImagePacker_Create(env, &packer);
   ```
3. 初始化资源。

   通过OH\_ImagePacker\_InitNative来初始化编码器实例对象。

   ```
   1. // 通过 napi_env 及上述创建的编码器对象初始化实例对象。
   2. ImagePacker_Native* nativePacker = OH_ImagePacker_InitNative(env, packer);
   ```
4. 编码。

   编码接口入参包括：

   * 上述过程中获取的实例对象（ImagePacker\_Native）。
   * 需要编码的图像源（napi\_value）, PixelMap或ImageSource（未调用过CreatePixelMap）的实例对象均可。
   * 编码参数：包括编码格式与编码质量。

     说明

     根据MIME标准，标准编码格式为image/jpeg。当使用image编码时，编码参数中的编码格式format设置为image/jpeg，image编码后的文件扩展名可设为.jpg或.jpeg，可在支持image/jpeg解码的平台上使用。

   编码接口可按输出方式分为向缓存区（内存）输出和向文件输出两种接口，入参均为上述内容。

   应用可根据输出的不同需求选择编码接口。

   向缓存区（内存）输出。

   ```
   1. #include <cstdlib>
   2. #include <multimedia/image_framework/image_packer_mdk.h>

   4. int32_t packImageToData(napi_env env, napi_callback_info info)
   5. {
   6. napi_value source;
   7. // 使用napi_value承接创建的编码器对象。
   8. napi_value packer;
   9. // 通过napi_env创建编码器，返回result为IMAGE_RESULT_SUCCESS则创建成功。
   10. int32_t errorCode = OH_ImagePacker_Create(env, &packer);
   11. if (errorCode != IMAGE_RESULT_SUCCESS) {
   12. return errorCode;
   13. }
   14. // 通过napi_env及上述创建的编码器对象初始化实例对象。
   15. ImagePacker_Native* nativePacker = OH_ImagePacker_InitNative(env, packer);
   16. // 编码参数。
   17. struct ImagePacker_Opts_ opts;
   18. // 配置编码格式（必须）。
   19. opts.format = "image/jpeg";
   20. // 配置编码质量（必须）。
   21. opts.quality = 95;
   22. // 配置输出的缓存区大小为4k（缓存区大小视应用场景定）。
   23. size_t bufferSize = 4*1024;
   24. // 申请图片编码缓存区。
   25. uint8_t* outData = (uint8_t *)(malloc(bufferSize));
   26. if (outData == NULL) {
   27. errorCode = OH_ImagePacker_Release(nativePacker);
   28. if (errorCode != IMAGE_RESULT_SUCCESS) {
   29. return errorCode;
   30. } else {
   31. nativePacker = NULL; // 不可重复destroy。
   32. }
   33. return IMAGE_RESULT_MALLOC_ABNORMAL;
   34. }
   35. // 开始对输入source进行编码过程，返回result为IMAGE_RESULT_SUCCESS则编码成功，同时bufferSize中包含编码实际使用缓存区大小。
   36. int32_t result = OH_ImagePacker_PackToData(nativePacker, source, &opts, outData, &bufferSize);
   37. free(outData);
   38. outData = NULL;
   39. errorCode = OH_ImagePacker_Release(nativePacker);
   40. if (errorCode != IMAGE_RESULT_SUCCESS) {
   41. return errorCode;
   42. } else {
   43. nativePacker = NULL; // 不可重复destroy。
   44. }
   45. return result;
   46. }
   ```

   向文件输出。

   ```
   1. #include <fcntl.h>
   2. #include <unistd.h>
   3. #include <cstdlib>
   4. #include <multimedia/image_framework/image_packer_mdk.h>

   6. int32_t packImageToFile(napi_env env, napi_callback_info info)
   7. {
   8. napi_value source;
   9. // 使用napi_value承接创建的编码器对象。
   10. napi_value packer;
   11. // 通过napi_env创建编码器，返回result为IMAGE_RESULT_SUCCESS则创建成功。
   12. int32_t errorCode = OH_ImagePacker_Create(env, &packer);
   13. if (errorCode != IMAGE_RESULT_SUCCESS) {
   14. return errorCode;
   15. }
   16. // 通过napi_env及上述创建的编码器对象初始化实例对象。
   17. ImagePacker_Native* nativePacker = OH_ImagePacker_InitNative(env, packer);
   18. // 编码参数。
   19. struct ImagePacker_Opts_ opts;
   20. // 配置编码格式（必须）。
   21. opts.format = "image/jpeg";
   22. // 配置编码质量（必须）。
   23. opts.quality = 100;
   24. // 打开需要输出的文件（请确保应用有权限访问这个路径）。
   25. int fd = open("/data/test.jpg", O_RDWR | O_CREAT, S_IRUSR | S_IWUSR);
   26. int result;
   27. if (fd >= 0) {
   28. // 开始对输入source进行编码过程，返回result为IMAGE_RESULT_SUCCESS则编码成功。
   29. result = OH_ImagePacker_PackToFile(nativePacker, source, &opts, fd);
   30. // 关闭输出文件。
   31. close(fd);
   32. }
   33. errorCode = OH_ImagePacker_Release(nativePacker);
   34. if (errorCode != IMAGE_RESULT_SUCCESS) {
   35. return errorCode;
   36. } else {
   37. nativePacker = NULL; // 不可重复destroy。
   38. }
   39. return result;
   40. }
   ```
