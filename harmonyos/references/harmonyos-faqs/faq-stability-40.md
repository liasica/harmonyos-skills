---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-40
title: 快速连续点击拍照按钮，应用闪退
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 快速连续点击拍照按钮，应用闪退
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:28533979d424da561e4fde6ad07dd384f23c095dabf1baa20f170210c0a75e7a
---

## 问题现象

快速连续点击拍照按钮时，应用发生闪退。

## 背景知识

* CppCrash进程崩溃检测基于操作系统信号机制，目前支持的崩溃信号参考[Cpp Crash（进程崩溃）检测](../harmonyos-guides/cppcrash-guidelines.md)。
* CppCrash日志规格说明可以参考[日志规格](../harmonyos-guides/cppcrash-guidelines.md#日志规格)说明。

* [packToFile](../harmonyos-references/arkts-apis-image-imagepacker.md#packtofile13)：指定编码参数，将PixelMap直接编码进文件。使用Promise形式返回结果。
* [crop](../harmonyos-references/arkts-apis-image-pixelmap.md#crop9)：根据输入的尺寸对图片进行裁剪，使用Promise形式返回。
* [async/await](../harmonyos-guides/async-concurrency-overview.md#asyncawait)：async/await是用于处理异步操作的Promise语法糖，使编写异步代码更加简单和易读。使用async关键字声明异步函数，并使用await关键字等待Promise的解析（完成或拒绝），以同步方式编写异步操作的代码。

## 问题定位

1. 查看faultlogger目录下的故障日志，异常信号是SIGSEGV，无效内存访问。

   ```shell
   Reason:Signal:SIGSEGV(SEGV_MAPERR)@0x0000005ba5568000 
   Fault thread info:
   Tid:46346, Name:OS_FFRT_3_0
   #00 pc 000000000141f588 /system/lib64/libskia_canvaskit.z.so(jsimd_extrgbx_ycc_convert_neon+564)(60d1c4d658beecacdae715b752333a76)
   #01 pc 00000000013f449c /system/lib64/libskia_canvaskit.z.so(pre_process_data+152)(60d1c4d658beecacdae715b752333a76)
   #02 pc 00000000013ecedc /system/lib64/libskia_canvaskit.z.so(process_data_simple_main+208)(60d1c4d658beecacdae715b752333a76)
   #03 pc 00000000013d8b34 /system/lib64/libskia_canvaskit.z.so(jpeg_write_scanlines+176)(60d1c4d658beecacdae715b752333a76)
   #04 pc 00000000012ad848 /system/lib64/libskia_canvaskit.z.so(SkJpegEncoder::onEncodeRows(int)+372)(60d1c4d658beecacdae715b752333a76)
   #05 pc 00000000011663e8 /system/lib64/libskia_canvaskit.z.so(SkEncoder::encodeRows(int)+80)(60d1c4d658beecacdae715b752333a76)
   #06 pc 00000000012ad8d4 /system/lib64/libskia_canvaskit.z.so(SkJpegEncoder::Encode(SkWStream*, SkPixmap const&, SkJpegEncoder::Options const&)+64)(60d1c4d658beecacdae715b752333a76)
   #07 pc 0000000000fdf038 /system/lib64/libskia_canvaskit.z.so(SkEncodeImage(SkWStream*, SkPixmap const&, SkEncodedImageFormat, int)+252)(60d1c4d658beecacdae715b752333a76)
   #08 pc 0000000001166304 /system/lib64/libskia_canvaskit.z.so(SkEncodeImage(SkWStream*, SkBitmap const&, SkEncodedImageFormat, int)+148)(60d1c4d658beecacdae715b752333a76)
   #09 pc 000000000009c268 /system/lib64/platformsdk/libextplugin.z.so(OHOS::ImagePlugin::ExtEncoder::DoEncode(SkWStream*, SkBitmap const&, SkEncodedImageFormat const&)+280)(4f50f74b029138d69bf103f408e21784)
   #10 pc 000000000009c004 /system/lib64/platformsdk/libextplugin.z.so(OHOS::ImagePlugin::ExtEncoder::EncodeImageByBitmap(SkBitmap&, bool, SkWStream&)+320)(4f50f74b029138d69bf103f408e21784)
   #11 pc 000000000009a08c /system/lib64/platformsdk/libextplugin.z.so(OHOS::ImagePlugin::ExtEncoder::EncodeImageByPixelMap(OHOS::Media::PixelMap*, bool, SkWStream&)+968)(4f50f74b029138d69bf103f408e21784)
   #12 pc 0000000000099028 /system/lib64/platformsdk/libextplugin.z.so(OHOS::ImagePlugin::ExtEncoder::PixelmapEncode(OHOS::ImagePlugin::ExtWStream&)+132)(4f50f74b029138d69bf103f408e21784)
   #13 pc 0000000000098dcc /system/lib64/platformsdk/libextplugin.z.so(OHOS::ImagePlugin::ExtEncoder::FinalizeEncode()+824)(4f50f74b029138d69bf103f408e21784)
   #14 pc 00000000000c7430 /system/lib64/platformsdk/libimage_native.z.so(std::__h::__function::__func<OHOS::Media::ImagePacker::FinalizePacking()::$_3, std::__h::allocator<OHOS::Media::ImagePacker::FinalizePacking()::$_3>, unsigned int (OHOS::ImagePlugin::AbsImageEncoder*)>::operator()(OHOS::ImagePlugin::AbsImageEncoder*&&)+56)(bcd0c974911e66ecc960744f372db153)
   #15 pc 00000000000c53ac /system/lib64/platformsdk/libimage_native.z.so(OHOS::Media::ImagePacker::DoEncodingFunc(std::__h::function<unsigned int (OHOS::ImagePlugin::AbsImageEncoder*)>, bool)+300)(bcd0c974911e66ecc960744f372db153)
   #16 pc 00000000000c74e4 /system/lib64/platformsdk/libimage_native.z.so(OHOS::Media::ImagePacker::FinalizePacking(long&)+80)(bcd0c974911e66ecc960744f372db153)
   #17 pc 00000000000a531c /system/lib64/platformsdk/libimage_napi.z.so(OHOS::Media::PackToFileExec(napi_env__*, void*) (.cfi)+728)(ff41160588e3ec0d50afc636299767c8)
   ```
2. 查看故障堆栈，应用在调用packToFile函数时出现内存访问异常，需要排查在调用packToFile函数时编码的PixelMap资源是否被释放和修改。
3. 排查应用在调用packToFile函数前是否调用crop函数修改PixelMap。

   ```ts
   async function Packing(context: Context) {
     const resourceMgr = context.resourceManager;
     const rawFile = await resourceMgr.getRawFileContent("test.jpg");
     let ops: image.SourceOptions = {
       sourceDensity: 98,
     }
     let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
     let pixelMap: image.PixelMap = await imageSource.createPixelMap();
     const imagePackerApi: image.ImagePacker = image.createImagePacker();
     let funcName = "Packing";
     if (imagePackerApi != null) {
       try {
         let opts: image.PackingOption = { format: "image/jpeg", quality: 98};
         pixelMap.crop({x : 1, y : 1, size: {width : 200, height: 200}})
         const path : string = context.cacheDir + "/pixel_map.jpg";
         let file = fs.openSync(path, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
         imagePackerApi.packToFile(pixelMap, file.fd, opts).then(() => {
           // 直接编码进文件。
         }).catch((error : BusinessError) => {
           console.error(funcName, `Failed to pack the image.code ${error.code},message is ${error.message}`);
         }).finally(()=>{
           fs.closeSync(file.fd);
         })
       } catch (error) {
         console.error(funcName, `Failed to pack the image.code ${error.code},message is ${error.message}`);
       }
     }
   }
   ```

## 分析结论

在调用packToFile函数时编码的PixelMap资源被修改，导致应用闪退。

## 修改建议

使用await等待crop函数执行结束，再执行packToFile函数。

```ts
import { image } from '@kit.ImageKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function Packing(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent('test.jpg');
  let ops: image.SourceOptions = {
    sourceDensity: 98,
  };
  let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
  let pixelMap: image.PixelMap = await imageSource.createPixelMap();
  const imagePackerApi: image.ImagePacker = image.createImagePacker();
  let funcName = 'Packing';
  if (imagePackerApi != null) {
    try {
      let opts: image.PackingOption = { format: 'image/jpeg', quality: 98 };
      await pixelMap.crop({ x: 1, y: 1, size: { width: 50, height: 50 } });
      const path: string = context.cacheDir + '/pixel_map.jpg';
      let file = fs.openSync(path, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
      imagePackerApi.packToFile(pixelMap, file.fd, opts).then(() => {
        // 直接编码进文件。
      }).catch((error: BusinessError) => {
        console.error(funcName, `Failed to pack the image.code ${error.code},message is ${error.message}`);
      }).finally(() => {
        fs.closeSync(file.fd);
      });
    } catch (error) {
      console.error(funcName, `Failed to image.code ${error.code},message is ${error.message}`);
    }
  }
}

@Entry
@Component
struct Index {
  message: string = 'Hello World';

  build() {
    RelativeContainer() {
      Button(this.message)
        .id('HelloWorld')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          Packing(this.getUIContext().getHostContext() as Context);
        });
    }
    .height('100%')
    .width('100%');
  }
}
```
