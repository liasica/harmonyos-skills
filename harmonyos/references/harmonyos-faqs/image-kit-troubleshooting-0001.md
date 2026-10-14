---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/image-kit-troubleshooting-0001
title: PixelMap创建崩溃问题定位
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 故障排查 > PixelMap创建崩溃问题定位
category: harmonyos-faqs
scraped_at: 2026-10-15T07:15:35+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:8f0a47c11d35ade6c5a0a31d80c2f101087033775d944879e13fc879c9d29c63
---

## 问题现象

在使用image.createPixelMap()方法获取资源文件创建PixelMap时发生崩溃。

问题代码如下：

```ts
// 媒体文件字节数组
let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // 获取resourceManager资源管理
context.resourceManager.getMediaContent($r('app.media.ic_image1').id, (error, value: ArrayBuffer) => {
  let opts: image.InitializationOptions = {
    editable: true,
    pixelFormat: 3,
    size: { height: 479, width: 360 }
  };
  let uint8Array: Uint8Array = new Uint8Array(value);
  let buffer: ArrayBuffer = uint8Array.buffer.slice(0);

  // 创建PixelMap
  image.createPixelMap(buffer, opts).then((pixelMap) => {
    this.savePixelMapToAlbum('test', pixelMap, 0);
  })
});
```

## 定位过程

报错日志：

```txt
#00 pc 0000000000f370c0 /system/lib64/libskia_canvaskit.z.so(8c7ac378b6e1ceb62a01e16a3d8e1d8a)
#01 pc 0000000000eee00c /system/lib64/libskia_canvaskit.z.so(8c7ac378b6e1ceb62a01e16a3d8e1d8a)
#02 pc 0000000000eba02e /system/lib64/libskia_canvaskit.z.so(SkBitmap::writePixels(SkPixmap const&, int, int)+366)(8c7ac378b6e1ceb62a01e16a3d8e1d8a)
#03 pc 0000000000002f14 /system/lib64/platformsdk/libpixelconvertadapter.z.so(OHOS::Media::PixelConvertAdapter::WritePixelsConvert(void const*, unsigned int, OHOS::Media::ImageInfo const&, void*, OHOS::Media::Position const&, unsigned int, OHOS::Media::ImageInfo const&)+1044)(cc1095798d8f5a22097127a6e150bc1e)
#04 pc 00000000000d321b /system/lib64/platformsdk/libimage_native.z.so(OHOS::Media::PixelConvert::PixelsConvert(OHOS::Media::BufferInfo const&, OHOS::Media::BufferInfo&, int, bool)+2827)(fac8598ca077a00cb33235d60fb4b283)
#05 pc 00000000000c2482 /system/lib64/platformsdk/libimage_native.z.so(OHOS::Media::PixelMap::Create(unsigned int const*, unsigned int, OHOS::Media::BuildParam&, OHOS::Media::InitializationOptions const&, int&)+962)(fac8598ca077a00cb33235d60fb4b283)
#06 pc 00000000000c1f7d /system/lib64/platformsdk/libimage_native.z.so(OHOS::Media::PixelMap::Create(unsigned int const*, unsigned int, OHOS::Media::InitializationOptions const&)+157)(fac8598ca077a00cb33235d60fb4b283)
#07 pc 00000000000c236b /system/lib64/platformsdk/libimage_napi.z.so(09a8986de5dca463cddf850c48265e7c)
#08 pc 000000000006f15b /system/lib64/platformsdk/libace_napi.z.so(NativeAsyncWork::AsyncWorkCallback(uv_work_s*)+507)(2a6c165e9beb23b9bb2f2b037ff0bde9)
#09 pc 000000000001405b /system/lib64/platformsdk/libuv.so(c1f9def93b695f8d0e70b8a152aeb7f8)
#10 pc 000000000011b037 /system/lib/ld-musl-x86_64.so.1(a8ef7b533141722f2af1edecc50f33cf)
#11 pc 000000000008929e /system/lib/ld-musl-x86_64.so.1(a8ef7b533141722f2af1edecc50f33cf)
```

通过日志定位崩溃点在调用image.createPixelMap()方法生成PixelMap时。查看对应位置代码，发现代码中将resourceManager.getMediaContent返回的媒体文件数据作为参数传入image.createPixelMap()中。

## 分析结论

image.createPixelMap()方法的入参colors为图像像素数据，而resourceManager.getMediaContent()方法回调函数中得到的是媒体文件内容数据。媒体文件数据可以直接用于播放，但不能作为image.createPixelMap()方法的入参，需要通过解码转换为可用图片像素数据用于图片处理或渲染，两者的区别如下表所示：

| 数据类型 | 数据格式 | 是否需要解码 |
| --- | --- | --- |
| 媒体文件ArrayBuffer | JPEG、PNG、MP3等 | 是 |
| 图片像素数据ArrayBuffer | RGBA、YUV等像素格式 | 否 |

## 修改建议

使用图片解码image.createImageSource()将resourceManager.getMediaContent()方法回调中得到的媒体文件内容数据创建ImageSource实例。使用ImageSource下的[createPixelMap()](../harmonyos-references/arkts-apis-image-imagesource.md#createpixelmap7-2)方法创建PixelMap对象，关于图片解码可参考[官方文档](../harmonyos-guides/image-decoding.md)，示例如下：

```ts
import { common } from '@kit.AbilityKit';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct Index {
  @State pixelMap: image.PixelMap | undefined = undefined;

  // 把资源目录下的文件转为pixelMap
  async loadImage(resource: Resource): Promise<image.PixelMap> {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // 获取resourceManager资源管理
    const resourceManager = context.resourceManager; // 获取图片数据
    const fileData: Uint8Array = await resourceManager.getMediaContent(resource.id); // 返回对应的媒体文件内容。
    let buffer: ArrayBuffer = fileData.buffer.slice(0);
    const imageSource: image.ImageSource = image.createImageSource(buffer);
    const pixelMap: image.PixelMap = await imageSource.createPixelMap();
    imageSource.release();
    return pixelMap;
  }

  async aboutToAppear(): Promise<void> {
    this.pixelMap = await this.loadImage($r('app.media.startIcon'));
  }

  build() {
    Column() {
      Image(this.pixelMap)
        .width(200)
        .height(200)
    }
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%')
  }
}
```
