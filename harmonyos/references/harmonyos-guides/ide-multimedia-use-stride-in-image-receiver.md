---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-multimedia-use-stride-in-image-receiver
title: "@correctness/multimedia-use-stride-in-image-receiver"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 正确性规则@correctness > @correctness/multimedia-use-stride-in-image-receiver
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:15efdb1ca5bab758d47b34a8d81f304d66cd4609c01acd1b8d16410d4b9e3984
---

在使用ImageReceiver组件中[readNextImage](../harmonyos-references/arkts-apis-image-imagereceiver.md#readnextimage9)接口时，建议调用rowStride属性，避免出现相机获取预览流数据异常的问题。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@correctness/multimedia-use-stride-in-image-receiver": "warn"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```screen
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

function onImageArrival(receiver: image.ImageReceiver): void {
   receiver.on('imageArrival', () => {
      receiver.readNextImage((err: BusinessError, nextImage: image.Image) => {
      if (err || nextImage === undefined) {
        console.error('readNextImage failed');
        return;
      }
      nextImage.getComponent(image.ComponentType.JPEG, async (err: BusinessError, imgComponent: image.Component) => {
        if (err || imgComponent === undefined) {
          console.error('getComponent failed');
        }
        if (imgComponent.byteBuffer) {
          let width = nextImage.size.width; 
          let height = nextImage.size.height; 
          let stride = imgComponent.rowStride;  // 调用rowStride
          console.debug(`getComponent with width:${width} height:${height} stride:${stride}`);
          if (stride == width) {
            let pixelMap = await image.createPixelMap(imgComponent.byteBuffer, {
              size: { height: height, width: width },
              srcPixelFormat: 8,
            })
          } else {
            const dstBufferSize = width * height * 1.5
            const dstArr = new Uint8Array(dstBufferSize)
            for (let j = 0; j < height * 1.5; j++) {
              const srcBuf = new Uint8Array(imgComponent.byteBuffer, j * stride, width)
              dstArr.set(srcBuf, j * width)
            }
            let pixelMap = await image.createPixelMap(dstArr.buffer, {
              size: { height: height, width: width },
              srcPixelFormat: 8,
            })
          }
        } else {
          console.error('byteBuffer is null');
        }
        nextImage.release();
      })
    })
  })
}
```

## 反例

```screen
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

function onImageArrival(receiver: image.ImageReceiver): void {
  receiver.on('imageArrival', () => {
    receiver.readNextImage((err: BusinessError, nextImage: image.Image) => {
      if (err || nextImage === undefined) {
        console.error('readNextImage failed');
        return;
      }
      nextImage.getComponent(image.ComponentType.JPEG, async (err: BusinessError, imgComponent: image.Component) => {
        if (err || imgComponent === undefined) {
          console.error('getComponent failed');
        }
        if (imgComponent.byteBuffer) {
          let width = nextImage.size.width;
          let height = nextImage.size.height; // 未调用rowStride
        } else {
          console.error('byteBuffer is null');
        }
        nextImage.release();
      })
    })
  })
}
```

## 规则集

```screen
plugin:@correctness/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
