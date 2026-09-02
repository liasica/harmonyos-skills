---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-17
title: 将pixelFormat设置为nv21或者nv12时抛出错误码62980096怎么处理
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 将pixelFormat设置为nv21或者nv12时抛出错误码62980096怎么处理
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:42+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3e580052c29f9bea0f5be8dc83b386a70aeb8f338d87c30e1f139483ef0ec13b
---

## 问题详情

调用createPixelMap方法时，如果将pixelFormat设置为nv21或nv12，可能会遇到错误代码62980096。建议检查以下几点：

确认pixelFormat参数值是否正确。

检查createPixelMap方法的其他参数是否符合要求。

确认系统环境是否支持nv21和nv12格式。

如果问题仍然存在，请参考官方文档或联系技术支持获取进一步帮助。

## 解决措施

pixelFormat枚举目前用于ImageSource。因此，如果要创建PixelMap，NV21或NV12格式的图片需要通过以下方式：

1. 使用createImageSource方法创建ImageSource。

   设置createImageSource的sourceOption参数时，sourcePixelFormat参数值8对应NV21格式，9对应NV12格式。sourceSize参数需设置为原始YUV图片的宽高，且宽度值必须为偶数。
2. 使用ImageSource的createPixelMap接口创建PixelMap。

具体代码如下：

```ts
import { image } from '@kit.ImageKit';

@Entry
@Component
struct Index {
  @State message: string = 'NV21AndNV12ToPixelMap';
  @State private pixelMap: PixelMap | null = null;
  @State private pixelMap2: PixelMap | null = null;

  build() {
    Row() {
      Column() {
        Image(this.pixelMap)
          .width(200).height(200).margin(15)
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(async () => {
            let resourceManager = this.getUIContext().getHostContext()!.resourceManager
            let imageArray = await resourceManager.getMediaContent($r("app.media.sample14_NV21_fromJPG_510X510"));
            let pixelBuffer = new Uint8Array(imageArray).buffer as Object as ArrayBuffer;
            // The value 8 of the sourcePixelFormat parameter corresponds to NV21 format, and 9 corresponds to NV12 format; The sourceSize parameter needs to set the width and height (the width and height data of the original yuv image), and the width value cannot be odd.
            let sourceOptions: image.SourceOptions =
              { sourceDensity: 120, sourcePixelFormat: 8, sourceSize: { width: 510, height: 510 } };
            let imageResource = image.createImageSource(pixelBuffer, sourceOptions);
            let opts: image.DecodingOptions = { editable: true }
            this.pixelMap = await imageResource.createPixelMap(opts);

            let imageArray2 = await resourceManager.getMediaContent($r('app.media.sample10_NV12_fromJPG_510X510'));
            let pixelBuffer2 = new Uint8Array(imageArray2).buffer as Object as ArrayBuffer;
            // The value 8 of the sourcePixelFormat parameter corresponds to NV21 format, and 9 corresponds to NV12 format; The sourceSize parameter needs to set the width and height (the width and height data of the original yuv image), and the width value cannot be odd.
            let sourceOptions2: image.SourceOptions =
              { sourceDensity: 120, sourcePixelFormat: 9, sourceSize: { width: 510, height: 510 } };
            let imageResource2 = image.createImageSource(pixelBuffer2, sourceOptions2);
            let opts2: image.DecodingOptions = { editable: true }
            this.pixelMap2 = await imageResource2.createPixelMap(opts2);
          })
        Image(this.pixelMap2)
          .width(200).height(200).margin(15)
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
