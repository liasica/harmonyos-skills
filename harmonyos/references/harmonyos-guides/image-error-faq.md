---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-error-faq
title: Image Kit异常处理
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > Image Kit常见问题 > Image Kit异常处理
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:22+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:2d94672e1d999f9e9b26dca22acbf3dcded30e42b462b84c46c54fa9dbec8384
---

[Image Kit](image-overview.md)提供**ArkTS接口**和**C接口**。在遇到特殊情况时（例如输入参数无效、内存不足或函数无法处理请求等），系统会通过异常（ArkTS）或错误码（C接口）来反馈错误。开发者需要在应用层合理捕获和处理这些错误，以避免应用崩溃或出现未定义行为。在[Image错误码](../harmonyos-references/errorcode-image.md)中给出了Image Kit错误码对应的错误信息、可能原因、处理步骤。但由于部分场景引发错误的原因较为复杂，还需要开发者结合日志进一步定位。例如：401参数错误，可能是函数入参存在问题，也可能是由于缺少特定的文件读写权限导致无法访问或修改图片文件（Image Kit不感知权限，表现为传入文件异常的参数错误）。

## ArkTS接口异常处理

ArkTS接口调用时，如果传入的参数不符合要求，或者底层执行过程中出现不可恢复的错误，系统会返回或抛出[BusinessError](../harmonyos-references/js-apis-base.md#businesserror)异常，又或者在异步场景中返回一个[Promise](async-concurrency-overview.md#promise)的rejected状态。如果开发者忽略了异常处理，可能会出现功能问题或数据丢失，甚至直接导致应用崩溃。

典型的ArkTS接口形态及API示例和处理方法如下所示。

| 接口形态 | 示例API | 处理方式 |
| --- | --- | --- |
| **Promise异步接口** | getImageInfo(): Promise<ImageInfo>、modifyImageProperty(key: PropertyKey, value: string): Promise<void> | 使用await+try/catch，或promise.catch捕获BusinessError。 |
| **AsyncCallback异步接口** | getImageInfo(callback: AsyncCallback<ImageInfo>): void | 使用回调函数[AsyncCallback](../harmonyos-references/js-apis-base.md#asynccallback)的参数获取BusinessError。 |
| **同步接口** | getImageInfoSync(): ImageInfo | 使用try/catch捕获同步BusinessError。 |

1. AsyncCallback异步接口示例。

   ```
   1. import { image } from '@kit.ImageKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';

   4. function getImageInfoByCallback(pixelMap: image.PixelMap): void {
   5. if (!pixelMap) {
   6. console.error("pixelMap is null or undefined");
   7. return;
   8. }
   9. pixelMap.getImageInfo((err: BusinessError, info: image.ImageInfo) => {
   10. if (err) {
   11. console.error(`getImageInfo callback failed, code=${err.code}, msg=${err.message}`);
   12. return;
   13. }
   14. console.info(`Image width=${info.size.width}, height=${info.size.height}`);
   15. });
   16. }
   ```
2. Promise异步接口示例。

   ```
   1. import { image } from '@kit.ImageKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';

   4. // getImageInfo(): Promise<ImageInfo>
   5. async function getImageInfoByPromise(pixelMap: image.PixelMap): Promise<void> {
   6. try {
   7. const info = await pixelMap.getImageInfo();
   8. console.info(`Image width=${info.size.width}, height=${info.size.height}`);
   9. } catch (err) {
   10. const e = err as BusinessError;
   11. console.error(`getImageInfo promise failed, code=${e.code}, msg=${e.message}`);
   12. }
   13. }

   15. // modifyImageProperty(key: PropertyKey, value: string): Promise<void>
   16. function modifyImagePropertyPromise(imageSource: image.ImageSource): void {
   17. imageSource.modifyImageProperty(image.PropertyKey.ORIENTATION, 'Top-left').then(() => {
   18. console.info('modifyImageProperty success');
   19. }).catch((err: BusinessError) => {
   20. console.error(`modifyImageProperty failed, code=${err.code}, msg=${err.message}`);
   21. });
   22. }
   ```
3. 同步型示例。

   ```
   1. import { image } from '@kit.ImageKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';

   4. function getImageInfoBySync(pixelMap: image.PixelMap): void {
   5. try {
   6. const info = pixelMap.getImageInfoSync();
   7. console.info(`Image width=${info.size.width}, height=${info.size.height}`);
   8. } catch (err) {
   9. const e = err as BusinessError;
   10. console.error(`getImageInfoSync failed, code=${e.code}, msg=${e.message}`);
   11. }
   12. }
   ```

## C接口异常处理

C接口统一通过[Image错误码](../harmonyos-references/errorcode-image.md)来表示函数执行结果。返回IMAGE\_SUCCESS（0）表示执行成功，返回非零值表示发生错误。开发者应在调用后立即检查返回值，并进行必要的错误处理，如日志记录、资源释放等。C接口异常处理的典型示例如下所示。

1. 通过ImageInfo获取图像信息。

   Image\_ErrorCode OH\_PixelmapNative\_GetImageInfo(OH\_PixelmapNative \*pixelmap, OH\_Pixelmap\_ImageInfo \*imageInfo)

   ```
   1. // 需要在src/main/cpp/CMakeLists.txt文件中链接so库文件：target_link_libraries(entry PUBLIC libhilog_ndk.z.so libpixelmap.so)。
   2. #include <hilog/log.h>
   3. #include <multimedia/image_framework/image/pixelmap_native.h>

   5. #undef LOG_DOMAIN
   6. #undef LOG_TAG
   7. #define LOG_DOMAIN 0x02b6
   8. #define LOG_TAG "ImageKitDemo"

   10. void GetImageInfoExample(OH_PixelmapNative *pixelmap) {
   11. if (!pixelmap) {
   12. OH_LOG_ERROR(LOG_APP, "GetImageInfoExample: pixelmap is nullptr");
   13. return;
   14. }
   15. OH_Pixelmap_ImageInfo *imageInfo;
   16. Image_ErrorCode errCode = OH_PixelmapImageInfo_Create(&imageInfo);
   17. if (errCode != IMAGE_SUCCESS) {
   18. OH_LOG_ERROR(LOG_APP, "OH_PixelmapNative_Create failed, errCode: %{public}d.", errCode);
   19. return;
   20. }
   21. errCode = OH_PixelmapNative_GetImageInfo(pixelmap, imageInfo);
   22. if (errCode != IMAGE_SUCCESS) {
   23. OH_LOG_ERROR(LOG_APP, "OH_PixelmapNative_GetImageInfo failed, errCode: %{public}d.", errCode);
   24. return;
   25. }

   27. // 获取图片的宽、高、像素格式和透明度等信息。
   28. uint32_t width, height, rowStride;
   29. int32_t pixelFormat, alphaType;
   30. OH_PixelmapImageInfo_GetWidth(imageInfo, &width);
   31. OH_PixelmapImageInfo_GetHeight(imageInfo, &height);
   32. OH_PixelmapImageInfo_GetRowStride(imageInfo, &rowStride);
   33. OH_PixelmapImageInfo_GetPixelFormat(imageInfo, &pixelFormat);
   34. OH_PixelmapImageInfo_GetAlphaType(imageInfo, &alphaType);
   35. OH_PixelmapImageInfo_Release(imageInfo);
   36. OH_LOG_INFO(LOG_APP,
   37. "GetImageInfo success, width: %{public}d, height: %{public}d, "
   38. "rowStride: %{public}d, pixelFormat: %{public}d, alphaType: %{public}d.",
   39. width, height, rowStride, pixelFormat, alphaType);
   40. }
   ```
2. 修改EXIF信息。

   Image\_ErrorCode OH\_ImageSourceNative\_ModifyImageProperty(OH\_ImageSourceNative \*source, Image\_String \*key, Image\_String \*value)

   ```
   1. // 需要在src/main/cpp/CMakeLists.txt文件中链接so库文件：target_link_libraries(entry PUBLIC libhilog_ndk.z.so libimage_source.so)。
   2. #include <string>
   3. #include <hilog/log.h>
   4. #include <multimedia/image_framework/image/image_source_native.h>

   6. #undef LOG_DOMAIN
   7. #undef LOG_TAG
   8. #define LOG_DOMAIN 0x02b6
   9. #define LOG_TAG "ImageKitDemo"

   11. void ModifyImagePropertyExample(OH_ImageSourceNative *source) {
   12. if (!source) {
   13. OH_LOG_ERROR(LOG_APP, "ModifyImagePropertyExample: source is nullptr");
   14. return;
   15. }
   16. const std::string keyStr = OHOS_IMAGE_PROPERTY_ORIENTATION;
   17. const std::string valueStr = "Top-left";
   18. Image_String key{const_cast<char *>(keyStr.c_str()), keyStr.length()};
   19. Image_String value{const_cast<char *>(valueStr.c_str()), valueStr.length()};

   21. Image_ErrorCode ret = OH_ImageSourceNative_ModifyImageProperty(source, &key, &value);
   22. if (ret != IMAGE_SUCCESS) {
   23. OH_LOG_ERROR(LOG_APP, "ModifyImageProperty failed, code=%{public}d", ret);
   24. return;
   25. }

   27. OH_LOG_INFO(LOG_APP, "ModifyImageProperty success, key=%{public}s, value=%{public}s", keyStr.c_str(),
   28. valueStr.c_str());
   29. }
   ```
