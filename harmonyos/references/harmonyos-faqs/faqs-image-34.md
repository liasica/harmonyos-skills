---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-34
title: 如何解决创建PixelMap出现Create PixelMap error错误
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 如何解决创建PixelMap出现Create PixelMap error错误
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:42+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d2cec547cfbfb4421bbd947c1f537cff5e2d90ebec2f720cb6e17ac6668d0421
---

## 问题现象

使用readPixelsToBuffer将PixelMap转换成buffer后，再将buffer转回PixelMap时出现报错，报错和代码如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/AulJ0kxYQ_SmEotEovcaqg/zh-cn_image_0000002628392606.png "点击放大")

```ts
this.pixel = await imageSource.createPixelMap(opts);
 let readBuffer: ArrayBuffer = new ArrayBuffer(this.pixel.getPixelBytesNumber());
 this.pixel.readPixelsToBuffer(readBuffer).then(() => {
   const pImgBigImageSource = image.createImageSource(readBuffer);
   pImgBigImageSource.createPixelMap().then((pixMap: image.PixelMap) => { 
     console.info('createPixelMap success');  
   }).catch((err: BusinessError) => { 
     console.error('createPixelMap error: ', err.toString());
   }) 
 })
```

## 背景知识

[readPixelsToBuffer](../harmonyos-references/js-apis-sendableimage.md#readpixelstobuffer)读取图像像素数据，并按照PixelMap的像素格式写入缓冲区中。[createImageSource](../harmonyos-references/arkts-apis-image-f.md#imagecreateimagesource9)用来创建图片源实例对象，可支持uri、文件描述符、图像资源文件的RawFileDescriptor、缓冲区等参数来创建。

## 问题定位

检查readPixelsToBuffer和createImageSource对传入参数及写入类型的要求，发现尽管[createImageSource](../harmonyos-references/arkts-apis-image-f.md#imagecreateimagesource9-3)支持传入ArrayBuffer的类型，但要求入参必须是未解码的数据，不能是类似于RBGA，YUV的像素buffer数据，而[readPixelsToBuffer](../harmonyos-references/arkts-apis-image-pixelmap.md#readpixelstobuffer7)写入缓冲区的是像素数据，不符合createImageSource的参数要求。

## 分析结论

对于已解码获取的图像像素数据，不能在创建ImageSource后创建PixelMap，而是要调用[image.createPixelMap](../harmonyos-references/arkts-apis-image-f.md#imagecreatepixelmap8)直接创建。

## 修改建议

对于图像像素buffer直接调用image.createPixelMap来创建PixelMap。

```ts
import { image } from '@kit.ImageKit';

@Entry
@Component
struct PixelBufferToAnotherPixel {
  @State targetPixel: PixelMap | undefined = undefined;
  private context = this.getUIContext();

  async creatPixel() {
    const resourceManager = this.context.getHostContext()?.resourceManager;
    const imageData = await resourceManager!.getMediaContent($r('app.media.startIcon').id);
    let arrayBuffer = imageData.buffer;
    const imageSource = image.createImageSource(arrayBuffer);
    let imageInfo = imageSource.getImageInfoSync(0);
    let width = imageInfo.size.width;
    let height = imageInfo.size.height;
    let format = imageInfo.pixelFormat;
    const opts: image.DecodingOptions = {
      editable: true,
      desiredPixelFormat : image.PixelMapFormat.BGRA_8888
    };
    let pixel = await imageSource.createPixelMap(opts);
    try {
      let readBuffer: ArrayBuffer = new ArrayBuffer(pixel.getPixelBytesNumber());
      pixel.readPixelsToBuffer(readBuffer).then(() => {
        let opts: image.InitializationOptions = {
          editable: true,
          pixelFormat: format,
          size: { height: height, width: width },
        };
        // 直接调用
        image.createPixelMap(readBuffer, opts).then((value) => {
          return this.targetPixel = value;
        });
        console.info("createPixelMap success");
      });
    } catch (error) {
      console.error("createPixelMap error", error.toString());
    }
  }

  build() {
    Column() {
      Button('创建PixelMap')
        .onClick(()=>{
          this.creatPixel();
        })
      Image(this.targetPixel)
        .objectFit(ImageFit.Contain)
        .height('50%')
    }
    .height('100%')
    .width('100%')
  }
}
```

## 总结

readPixelsToBuffer读取后的buffer里存放的是像素数据，而当createImageSource传入数据类型是ArrayBuffer时，buffer数据应该是未解码的数据，不能是类似于RBGA，YUV的像素buffer数据，如果想通过像素buffer数据创建PixelMap，可以调用image.createPixelMap接口。
