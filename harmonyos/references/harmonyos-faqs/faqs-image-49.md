---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-49
title: 图片数据通过线程传输后打包的图片显示纯黑
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 图片数据通过线程传输后打包的图片显示纯黑
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:43+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a714a0d77fa95d0e6c0d3b7e56c42a314c8727225d452d555a3d45d9855a1785
---

## 问题现象

图片数据作为[SharedArrayBuffer](../harmonyos-guides/shared-arraybuffer-object.md)对象通过线程间通信传输，使用图片处理服务下的[writeBufferToPixels](../harmonyos-references/arkts-apis-image-pixelmap.md#writebuffertopixels7)将图片数据写入PixelMap，通过图片编码器[ImagePacker](../harmonyos-references/arkts-apis-image-imagepacker.md)重新生成的图片文件显示纯黑，与原始图片不符。

原始图片如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/Q7AunDFiTrC0Ufd3OTOm9Q/zh-cn_image_0000002658791877.png "点击放大")

异常图片如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/DA7Dq3laSsKlAoWqavmgnA/zh-cn_image_0000002628552510.png "点击放大")

## 背景知识

* [SharedArrayBuffer对象](../harmonyos-guides/shared-arraybuffer-object.md)：支持跨并发实例间共享，但是访问及修改需要采用Atomics类，防止数据竞争。SharedArrayBuffer可以用于多个并发实例间的状态共享或者数据共享。
* SharedArrayBuffer和ArrayBuffer都是用于处理二进制数据的，但它们的用途有所不同。SharedArrayBuffer主要用于跨线程共享内存，通常使用Int32Array创建视图进行读取；而ArrayBuffer则通常用于单线程内的二进制数据处理，可以用来存储像素buffer数据。
* [writeBufferToPixels](../harmonyos-references/arkts-apis-image-pixelmap.md#writebuffertopixels7)：支持按照PixelMap的像素格式，读取缓冲区中的图像像素数据，并写入PixelMap。

## 问题定位

问题代码示例参考如下：

```ts
let callback = async (eventData: emitter.EventData): Promise<void> => {
  if (eventData.data != null) {
    // eventData.data.result数据类型为SharedArrayBuffer
    let pixelByte: Uint8Array = new Uint8Array(eventData.data.result)
    let pixelMap = image.createPixelMapSync({
      size: { width, height },
      srcPixelFormat: image.PixelMapFormat.RGBA_8888,
      pixelFormat: image.PixelMapFormat.RGBA_8888,
    })
    for (let index = 0; index < 100; index++) {
      hilog.debug(0x00, "getImagePixelByTexture",  `${pixelByte[index]}`)
    }
    await pixelMap.writeBufferToPixels(pixelByte.buffer)
    resolve(pixelMap)
  } else {
    resolve(null)
  }
}
```

报错日志参考如下：

```log
C02B05/PixelMapNapi us.pinguo...era_ohos E colors mismatch
C02B05/PixelMapNapi us.pinguo...era_ohos E fail to get buffer info
```

根据报错日志获取buffer信息失败（fail to get buffer info），而buffer数据来源于eventData.data.result，是线程间通信传输的数据，在业务逻辑中是一个SharedArrayBuffer对象，判断通过writeBufferToPixels读取缓冲区中数据写入PixelMap时，该buffer不符合想要的数据类型预期。

## 分析结论

SharedArrayBuffer对象与像素buffer数据不兼容，导致通过writeBufferToPixels获取缓冲区数据异常，写入PixelMap后生成的图片显示纯黑。

## 修改建议

需要将SharedArrayBuffer建立Int32Array类型的视图读取，再将Int32Array转为Uint8Array类型，通过Uint8Array类型得到的buffer数据为正确的二进制图像像素数据格式。

```ts
let callback = async (eventData: emitter.EventData): Promise<void> => {
  if (eventData.data != null) {
    let sab: SharedArrayBuffer = eventData.data.result as SharedArrayBuffer;
    let int32: Int32Array = new Int32Array(sab);
    let length = int32.length;
    let uint8Array = new Uint8Array(length * 4); // 每 Int32占用4字节

    for (let i = 0; i < length; i++) {
      let value = int32[i];
      uint8Array[i * 4] = value & 0xff; // 最低位字节
      uint8Array[i * 4 + 1] = (value >> 8) & 0xff; // 第二低位字节
      uint8Array[i * 4 + 2] = (value >> 16) & 0xff; // 第三低位字节
      uint8Array[i * 4 + 3] = (value >> 24) & 0xff; // 最高位字节
    }
    let pixelMap = image.createPixelMapSync({
      size: { width, height },
      srcPixelFormat: image.PixelMapFormat.RGBA_8888,
      pixelFormat: image.PixelMapFormat.RGBA_8888,
    });
    await pixelMap.writeBufferToPixels(uint8Array.buffer);
    resolve(pixelMap);
  } else {
    resolve(null);
  }
};
```

完整示例参考如下：

```ts
import { BusinessError, emitter } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

const getImagePixelByTextureEvent: number = 1;

class GLInterface {
  static getImagePixelByTexture(tid: number, width: number, height: number): Promise<PixelMap | null> {
    return new Promise<PixelMap | null>((resolve) => {
      let event: emitter.InnerEvent = {
        eventId: getImagePixelByTextureEvent
      };
      let callback = async (eventData: emitter.EventData): Promise<void> => {
        if (eventData.data != null) {
          let sab: SharedArrayBuffer = eventData.data.result as SharedArrayBuffer;
          let int32: Int32Array = new Int32Array(sab);
          let length = int32.length;
          let uint8Array = new Uint8Array(length * 4); // 每 Int32占用4字节

          for (let i = 0; i < length; i++) {
            let value = int32[i];
            uint8Array[i * 4] = value & 0xff; // 最低位字节
            uint8Array[i * 4 + 1] = (value >> 8) & 0xff; // 第二低位字节
            uint8Array[i * 4 + 2] = (value >> 16) & 0xff; // 第三低位字节
            uint8Array[i * 4 + 3] = (value >> 24) & 0xff; // 最高位字节
          }
          let pixelMap = image.createPixelMapSync({
            size: { width, height },
            srcPixelFormat: image.PixelMapFormat.RGBA_8888,
            pixelFormat: image.PixelMapFormat.RGBA_8888,
          });
          await pixelMap.writeBufferToPixels(uint8Array.buffer);
          resolve(pixelMap);
        } else {
          resolve(null);
        }
      };
      emitter.once(event, callback);
    });
  }
}

@Entry
@Component
struct Index {
  pixMap: image.PixelMap | undefined = undefined;
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  async mainFunc(): Promise<void> {
    let pixelMap: PixelMap | null = await GLInterface.getImagePixelByTexture(0, 1024, 1024);
    let packImageByte: ArrayBuffer = await image.createImagePacker().packToData(pixelMap!, {
      format: 'image/jpeg',
      quality: 100
    });
    let file =
      await fileIo.open(`${this.context.tempDir}/readImage1.jpg`, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
    try {
      fileIo.writeSync(file.fd, packImageByte);
    } finally {
      fileIo.closeSync(file);
    }
  }

  build() {
    Row() {
      Column() {
        Image(this.pixMap)
          .width(64)
          .height(64);
        Button('taskpoolEmitterTest')
          .onClick(async () => {
            this.context.resourceManager.getRawFileContent('background.png',
              (error: BusinessError, value: Uint8Array) => {
                let pixelBuffer = new Uint8Array(value).buffer as Object as ArrayBuffer;
                let imageResource = image.createImageSource(pixelBuffer);
                let imPix = imageResource.createPixelMapSync();
                this.pixMap = imPix;
                let buffer1 = new ArrayBuffer(imPix.getPixelBytesNumber());
                imPix.readPixelsToBufferSync(buffer1);
                let uint8 = new Uint8Array(buffer1);
                let buffer2 = new SharedArrayBuffer(uint8.length);
                let int32 = new Int32Array(buffer2);
                // 将uint8转为uint32
                for (let i = 0; i < uint8.length; i += 4) {
                  int32[i/4] = (uint8[i + 0] << 0) |
                    (uint8[i + 1] << 8) |
                    (uint8[i + 2] << 16) |
                    (uint8[i + 3] << 24);
                }

                let eventData: emitter.EventData = {
                  data: {
                    'result': buffer2,
                  }
                };
                let innerEvent: emitter.InnerEvent = {
                  eventId: getImagePixelByTextureEvent,
                  priority: emitter.EventPriority.HIGH
                };
                emitter.emit(innerEvent, eventData);
              });
            this.mainFunc();
          });
      }
      .width('100%')
      .height('100%');
    };
  }
}
```
