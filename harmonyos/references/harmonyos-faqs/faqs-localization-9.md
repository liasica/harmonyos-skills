---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-localization-9
title: 如何将app.media.app_icon，转换为PixelMap
breadcrumb: FAQ > 应用框架开发 > 无障碍和本地化 > 本地化开发（Localization） > 如何将app.media.app_icon，转换为PixelMap
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:31+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6890a72935cce6c9e63cb8401afd3de3e9740460680faf40d2c5aaa05bddd7f1
---

使用getMediaContent获取媒体文件内容。使用createPixelMap创建PixelMap。

参考代码如下：

```screen
import { image } from '@kit.ImageKit';

@Entry
@Component
struct Index {
  @State pixelMap: PixelMap | null = null;

  convert() {
    try {
      // Byte array of media files
      this.getUIContext().getHostContext()!.resourceManager.getMediaContent($r('app.media.startIcon').id,
        (error: BusinessError, value: Uint8Array) => {
          if (error) {
            console.error(`getMediaContent failed: ${error.code}, ${error.message}`);
            return;
          }
          let pixelMapInitOptions: image.InitializationOptions = {
            editable: true,
            pixelFormat: 3,
            size: { height: 4, width: 6 }
          };
          // Create an imageSource instance
          let imageSource = image.createImageSource(value.buffer);
          // Decoding to generate PixelMap
          imageSource.createPixelMap(pixelMapInitOptions).then((pixelMap) => {
            this.pixelMap = pixelMap;
            // Pixel operations or rendering can be performed here.
          }).catch((decodeError: BusinessError) => {
            console.error(`Decode failed: ${decodeError.code}, ${decodeError.message}`);
          });
        });
    } catch (error) {
      console.error(`Global error: ${error.code}, ${error.message}`);
    }
  }

  build() {
    Column() {
      Button('Click to convert')
        .onClick(() => {
          this.convert();
        })
        .margin({ bottom: 16 })
      Image(this.pixelMap)
    }
    .padding(16)
  }
}
```

**参考链接**

[getMediaContent](../harmonyos-references/js-apis-resource-manager.md#getmediacontent9)

[image.createPixelMap](../harmonyos-references/arkts-apis-image-f.md#imagecreatepixelmap8)
