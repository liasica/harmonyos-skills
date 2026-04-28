---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-common-mistakes
title: Image Kit常见崩溃报错问题
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > Image Kit常见问题 > Image Kit常见崩溃报错问题
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:22+08:00
doc_updated_at: 2026-04-17
content_hash: sha256:47e758590a44f5b8ae54ce2a690fcf57c90e976f81d66c002f83d5ac3e6c7841
---

本文档展示了Image Kit接口的典型错误用法案例，帮助开发者避免常见的开发问题，提高应用的稳定性和性能。

## 编码过程中PixelMap被释放/修改导致崩溃

**典型崩溃堆栈示例：**

```
1. Fault thread info:
2. Tid:5005, Name:OS_FFRT_3_0
3. #00 pc 000000000006d1f0 /system/lib64/platformsdk/libextplugin.z.so(OHOS::ImagePlugin::ExtWStream::write(void const*, unsigned long)+24)(300e33eb41735f2d3c8fe2259a671217)
4. #01 pc 0000000001828c94 /system/lib64/libskia_canvaskit.z.so(sk_empty_output_buffer(jpeg_compress_struct*)+48)(484139254f1cae74fd86fe798dbea128)
5. #02 pc 00000000010d1bb4 /system/lib64/libskia_canvaskit.z.so(encode_mcu_huff+692)(484139254f1cae74fd86fe798dbea128)
6. #03 pc 00000000010c8a88 /system/lib64/libskia_canvaskit.z.so(compress_output+384)(484139254f1cae74fd86fe798dbea128)
7. #04 pc 0000000000f8c4b0 /system/lib64/libskia_canvaskit.z.so(jpeg_finish_compress+220)(484139254f1cae74fd86fe798dbea128)
8. #05 pc 0000000000f8bf08 /system/lib64/libskia_canvaskit.z.so(SkJpegEncoderImpl::onEncodeRows(int)+384)(484139254f1cae74fd86fe798dbea128)
9. #06 pc 0000000000fd25ac /system/lib64/libskia_canvaskit.z.so(SkEncoder::encodeRows(int)+68)(484139254f1cae74fd86fe798dbea128)
10. #07 pc 0000000000fd2514 /system/lib64/libskia_canvaskit.z.so(SkJpegEncoder::Encode(SkWStream*, SkPixmap const&, SkJpegEncoder::Options const&)+64)(484139254f1cae74fd86fe798dbea128)
11. #08 pc 00000000000545dc /system/lib64/platformsdk/libextplugin.z.so(OHOS::ImagePlugin::ExtEncoder::SkEncodeImage(SkWStream*, SkBitmap const&, SkEncodedImageFormat, int)+188)(300e33eb41735f2d3c8fe2259a671217)
12. #09 pc 00000000000547a4 /system/lib64/platformsdk/libextplugin.z.so(OHOS::ImagePlugin::ExtEncoder::DoEncode(SkWStream*, SkBitmap const&, SkEncodedImageFormat const&)+204)(300e33eb41735f2d3c8fe2259a671217)
13. #10 pc 0000000000055464 /system/lib64/platformsdk/libextplugin.z.so(OHOS::ImagePlugin::ExtEncoder::EncodeImageByBitmap(SkBitmap&, bool, SkWStream&)+284)(300e33eb41735f2d3c8fe2259a671217)
14. #11 pc 0000000000055ad8 /system/lib64/platformsdk/libextplugin.z.so(OHOS::ImagePlugin::ExtEncoder::EncodeImageByPixelMap(OHOS::Media::PixelMap*, bool, SkWStream&)+1356)(300e33eb41735f2d3c8fe2259a671217)
15. #12 pc 0000000000053350 /system/lib64/platformsdk/libextplugin.z.so(OHOS::ImagePlugin::ExtEncoder::EncodeSdrImage(OHOS::ImagePlugin::ExtWStream&)+984)(300e33eb41735f2d3c8fe2259a671217)
16. #13 pc 0000000000052684 /system/lib64/platformsdk/libextplugin.z.so(OHOS::ImagePlugin::ExtEncoder::PixelmapEncode(OHOS::ImagePlugin::ExtWStream&)+184)(300e33eb41735f2d3c8fe2259a671217)
17. #14 pc 0000000000053a7c /system/lib64/platformsdk/libextplugin.z.so(OHOS::ImagePlugin::ExtEncoder::FinalizeEncode()+952)(300e33eb41735f2d3c8fe2259a671217)
18. #15 pc 00000000000b7d00 /system/lib64/platformsdk/libimage_native.z.so(std::__h::__function::__func<OHOS::Media::ImagePacker::FinalizePacking()::$_3, std::__h::allocator<OHOS::Media::ImagePacker::FinalizePacking()::$_3>, unsigned int (OHOS::ImagePlugin::AbsImageEncoder*)>::operator()(OHOS::ImagePlugin::AbsImageEncoder*&&)+28)(abee48eb37a365d523ba3560f087b63a)
19. #16 pc 00000000000b58b4 /system/lib64/platformsdk/libimage_native.z.so(OHOS::Media::ImagePacker::DoEncodingFunc(std::__h::function<unsigned int (OHOS::ImagePlugin::AbsImageEncoder*)>, bool)+272)(abee48eb37a365d523ba3560f087b63a)
20. #17 pc 00000000000b6de4 /system/lib64/platformsdk/libimage_native.z.so(OHOS::Media::ImagePacker::FinalizePacking(long&)+80)(abee48eb37a365d523ba3560f087b63a)
21. #18 pc 000000000009a5b8 /system/lib64/platformsdk/libimage_napi.z.so(OHOS::Media::PackToFileExec(napi_env__*, void*)+912)(1d95fd2a148829930aeec8cbeaf92976)
22. #19 pc 000000000006258c /system/lib64/platformsdk/libace_napi.z.so(NativeAsyncWork::AsyncWorkCallback(uv_work_s*)+264)(f5de54fc91f8cc9643b4846b808f9d4c)
23. #20 pc 0000000000013bd4 /system/lib64/platformsdk/libuv.so(uv__queue_work+48)(7dfe11681838c768af19f3408663affb)
24. ...
```

**崩溃原因：**

编码过程中未使用await等待异步操作执行完毕，致使资源对象在异步操作完成前被提前释放或修改。

**解决措施：**

1. **异步操作的生命周期管理：** 在调用Image Kit的异步接口（如[packToData](../harmonyos-references/arkts-apis-image-imagepacker.md#packtodata13)、[packToFile](../harmonyos-references/arkts-apis-image-imagepacker.md#packtofile11)、[createPixelMap](../harmonyos-references/arkts-apis-image-imagesource.md#createpixelmap7)等）时，必须确保传入的资源对象（如PixelMap、ImageSource）在异步操作完成之前不被释放或修改。
2. **使用await或Promise.then：** 推荐使用await等待异步操作完成，或者在Promise.then()的回调中释放资源，确保释放时机正确。
3. **页面生命周期管理：** 如果在页面中使用异步图片操作，需要在页面销毁时确保所有异步操作已经完成或取消，避免页面卸载后异步回调访问已销毁的资源。

**错误代码示例：**

```
1. import { image } from '@kit.ImageKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. async function wrongPackingExample(pixelMap: image.PixelMap, fd: number): Promise<void> {
5. let imagePacker = image.ImagePacker | null = null;

7. try {
8. imagePacker = image.createImagePacker();
9. let packOpts: image.PackingOption = { format: 'image/jpeg', quality: 95 };
10. // 错误：异步编码执行过程中，对pixelMap进行修改。
11. pixelMap.crop({x:1, y:1, size: {height:200, width:200}});

13. // 错误：异步操作没有使用await。
14. imagePacker.packToFile(pixelMap, fd, packOpts).then(() => {
15. console.info('Succeeded in packing the image to file.');
16. }).catch((error: BusinessError) => {
17. console.error('Pack failed: ' + error);
18. });

20. } catch (error) {
21. console.error('Pack failed: ' + error);
22. } finally {
23. // 错误：异步编码未完成，直接释放PixelMap，触发应用闪退。
24. pixelMap?.release();
25. imagePacker?.release();
26. }
27. }
```

**正确代码示例：**

```
1. import { image } from '@kit.ImageKit';

3. async function correctPackingExample(pixelMap: image.PixelMap, fd: number): Promise<void> {
4. let imagePacker = image.ImagePacker | null = null;

6. try {
7. imagePacker = image.createImagePacker();
8. let packOpts: image.PackingOption = { format: 'image/jpeg', quality: 95 };

10. // 正确：对PixelMap做裁剪时，必须await等待操作完成。
11. await pixelMap.crop({x:1, y:1, size: {height:200, width:200}});

13. // 正确：使用await等待异步操作完成。
14. await imagePacker.packToFile(pixelMap, fd, packOpts);
15. console.info('Pack success');

17. } catch (error) {
18. console.error('Pack failed: ' + error)
19. } finally {
20. pixelMap?.release();
21. imagePacker?.release();
22. }
23. }
```

## 多个异步操作共享同一个ImageSource对象

**典型崩溃堆栈示例：**

```
1. Fault thread info:
2. Tid: 41048, Name: OS_FFRT_3_5
3. #00 pc 00000000000b0864 /system/lib64/platformsdk/libimage_napi.z.so(OHOS::Media::CreatePixelMapInner(OHOS::Media::ImageSourceNapi*, std::__h::shared_ptr<OHOS::Media::ImageSource>, unsigned int, OHOS::Media::DecodeOptions, unsigned int8)+116) (3a63d0a0dc3ac58d9e1a58a77ad194f9)
4. #01 pc 00000000000b1178 /system/lib64/platformsdk/libimage_napi.z.so(OHOS::Media::CreatePixelMapExecute(napi_env__*, void*) (.1167.cfi)+308) (3a63d0a0dc3ac58d9e1a58a77ad194f9)
5. #02 pc 000000000005c3c0 /system/lib64/platformsdk/libace_napi.z.so(NativeAsyncWork: :AsyncWorkCallback(uv_work_s*)+304) (68011f831ed16fa3d94d4f22664d2eaf)
6. #03 pc 0000000000013614 /system/lib64/platformsdk/libuv.so(uv__queue_work+60)(1399a989328aa340c8622e4a1d0ca961)
7. #04 pc 0000000000091794 /system/lib64/ndk/libffrt.so(ffrt::UVTask::Execute()+764) (7921196b695415b02aa2bódfb05c7deb)
8. #05
9. pc 000000000008d13c /system/lib64/ndk/libffrt.so(ffrt::ExecuteTask(ffrt::TaskBase*)+248) (7921196b695415b02aa2b6dfb05c7deb)
10. #06 pc 000000000002e054 /system/lib64/ndk/libffrt.so(ffrt::CPUWorker::RunTask(ffrt: :TaskBase*, ffrt::CPUWorker*)+84) (7921196b695415b02aa2bódfb05c7deb)
11. #07 pc 00000000000cóc58 /system/lib64/ndk/libffrt.so(7921196b695415b02aa2b6dfb05c7deb)
12. #08 pc 00000000001d8c5c /system/lib/ld-musl-aarch64.so.1(start+240)(05aecbbf0bdce12d75badb7b497d0f9f)
13. ...
```

**崩溃原因：**

并发操作同一个ImageSource对象，引发资源竞态问题导致崩溃。

**解决措施：**

1. **避免并发访问：** 不要对同一个ImageSource实例并发执行多个异步操作，推荐按顺序执行，确保一个操作完成后再执行下一个操作。
2. **资源生命周期：** ImageSource的生命周期应该覆盖所有使用它的异步操作，只有在确认所有异步操作都完成后才能释放。
3. **性能考虑：** 虽然顺序执行可能会降低并发性能，但可以避免竞态条件和崩溃问题。如果确实需要并发处理，应该创建多个独立的ImageSource实例。

**错误代码示例：**

```
1. import { image } from '@kit.ImageKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. async function wrongSharedImageSourceExample(filePath: string, decodingOptions: Array<image.DecodingOptions>): Promise<Array<image.PixelMap>> {
5. // 创建一个ImageSource实例。
6. const imageSource = image.createImageSource(filePath);
7. const pixelMaps: Array<image.PixelMap> = [];

9. // 错误：for循环中并发启动多个解码操作，共享同一个ImageSource。
10. for (const opts of decodingOptions) {
11. imageSource.createPixelMap(opts).then((pixelMap: image.PixelMap) => {
12. pixelMaps.push(pixelMap);
13. console.info('PixelMap created');
14. }).catch((error: BusinessError) => {
15. console.error('Create pixelMap failed: ' + error);
16. });
17. }

19. // 错误：立即释放ImageSource，此时异步操作可能还在执行。
20. imageSource.release();
21. return pixelMaps;
22. }
```

**正确代码示例：**

```
1. import { image } from '@kit.ImageKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. async function correctSharedImageSourceExample(filePath: string): Promise<void> {
5. // 创建一个ImageSource实例。
6. const imageSource = image.createImageSource(filePath);

8. try {
9. // 正确：按顺序执行异步操作，避免并发访问。
10. const imageInfo = await imageSource.getImageInfo();
11. console.info(`Image info: width=${imageInfo.size.width}, height=${imageInfo.size.height}`);

13. const pixelMap1 = await imageSource.createPixelMap({ editable: true });
14. console.info('First pixelMap created');

16. const pixelMap2 = await imageSource.createPixelMap({ editable: false });
17. console.info('Second pixelMap created');

19. // 使用完成后释放资源。
20. pixelMap1.release();
21. pixelMap2.release();
22. } catch (error) {
23. console.error('Operation failed: ' + error);
24. }

26. // 所有操作完成后，安全地释放ImageSource。
27. imageSource.release();
28. }
```
