---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-scan-2
title: 如何解决生成的二维码无法使用的问题
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 扫码服务（Scan） > 如何解决生成的二维码无法使用的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:20+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f348d371e71af99e26f3245ef8363959dcf2042f59832e0c78ee00c79dce1dcf
---

## 问题现象

在HarmonyOS中生成二维码异常，生成的二维码无法使用。应用的业务逻辑主要分两步：

1. 把后端返回的base64字符串解码。
2. 根据解码后的Byte数组生成二维码。

```ts
 let content = "AQDwAUUBAAIZAAAAAAABBJWHOWbBlc8AHgOj0dsvCpdMZpMy3f+3+887rj5/ydMF+V50PqwhbHkSoZAgAAAAZrRmzyACrsxSAWIgAQEBAQEBAAAAAJiWfwAAAAAAAAAAAAAAAAoAAFlCQgAAAAAAJLChYJ0Mi0Pw/wSMZ8D2ByTDvmtxRinyNDCP0+VzsVoTaaXIcfNv4i8Ru6P3uHWjCVGUS3WE8faSSvxdnkLgnGa0Zs/bnwae2W8jT5krtgt2I4c+yg691kbq8zcYBEOmvioBUZ6B6e9D1c5jc3N0FmQsO0SAXVu0U4CMSao4xBxgIg+m";
 // base64字符串解码
 let that = new util.Base64Helper();
 let uArrayRes = that.decodeSync(content,util.Type.MIME)
 let str = buffer.from(uArrayRes.buffer).toString()
 // ISO-8859-1编码
 let textEncoder = new util.TextEncoder('iso-8859-1')
 let res = textEncoder.encodeInto(str)
 let resStr = buffer.from(res.buffer).toString()
 let options: generateBarcode.CreateOptions = {
   scanType: scanCore.ScanType.QR_CODE,
   height: 800,
   width: 800,
   level: generateBarcode.ErrorCorrectionLevel.LEVEL_Q
 }
 // 码图生成接口，成功返回PixelMap格式图片
 generateBarcode.createBarcode(resStr, options)
```

按照以上代码生成后的二维码如下图，需要通过二维码读取字符串的**二进制字节**信息，扫码后得到的是字符串信息。最终导致扫码设备无法识别，说明二维码生成失败。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/jtDUPDDQRHqgLNaqEblGMg/zh-cn_image_0000002628392618.png "点击放大")

## 背景知识

根据指定编码格式的字符串，[创建新的Buffer对象](../harmonyos-references/js-apis-buffer.md#bufferfrom-4)。

**说明** 

generateBarcode目前不支持在模拟器上运行。

## 问题定位

需要通过二维码读取字符串的二进制字节信息，扫码后得到的是字符串信息。

[TextEncoder](../harmonyos-references/js-apis-util.md#textencoder)用于将字节数组解码为字符串，支持多种不同的编码格式。

使用TextEncoder解码结果为字符串，而不是业务需要的二进制字节信息，所以需要更换解码方式。

## 分析结论

数据转为二进制参数应该使用buffer.from，其中encoding入参Latin1是ISO-8859-1的别名。

修改转码方式为：

```ts
buffer.from(str, 'latin1').buffer;
```

入参由字符串改为ArrayBuffer，成功生成预期码图。

## 修改建议

ISO-8859-1编码采用buffer.from操作转为二进制数据，不再通过textEncoder.encodeInto进行转换，Latin1是ISO-8859-1的别名，向下兼容ASCII格式。

```ts
// 导入码图生成需要的图片模块、错误码模块
import { scanCore, generateBarcode } from '@kit.ScanKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { buffer, util } from '@kit.ArkTS';

const TAG: string = 'Create barcode';

@Entry
@Component
struct Index {
  @State pixelMap1: image.PixelMap | undefined = undefined;

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button('generateBarcode Promise').onClick(() => {
        this.pixelMap1 = undefined;
        let content =
          'AQDwAUUBAAIZAAAAAAABBJWHOWbBlc8AHgOj0dsvCpdMZpMy3f+3+887rj5/ydMF+V50PqwhbHkSoZAgAAAAZrRmzyACrsxSAWIgAQEBAQEBAAAAAJiWfwAAAAAAAAAAAAAAAAoAAFlCQgAAAAAAJLChYJ0Mi0Pw/wSMZ8D2ByTDvmtxRinyNDCP0+VzsVoTaaXIcfNv4i8Ru6P3uHWjCVGUS3WE8faSSvxdnkLgnGa0Zs/bnwae2W8jT5krtgt2I4c+yg691kbq8zcYBEOmvioBUZ6B6e9D1c5jc3N0FmQsO0SAXVu0U4CMSao4xBxgIg+m';
        // base64字符串解密
        let that = new util.Base64Helper();
        let uArrayRes = that.decodeSync(content, util.Type.MIME);
        // ISO-8859-1编码
        let str = buffer.from(uArrayRes.buffer).toString();
        let contentBuffer: ArrayBuffer = buffer.from(str, 'latin1').buffer;
        let options: generateBarcode.CreateOptions = {
          scanType: scanCore.ScanType.QR_CODE,
          height: 800,
          width: 800,
          level: generateBarcode.ErrorCorrectionLevel.LEVEL_Q
        };
        // 码图生成接口，成功返回PixelMap格式图片
        generateBarcode.createBarcode(contentBuffer, options).then((pixelMap: image.PixelMap) => {
          this.pixelMap1 = pixelMap;
          hilog.info(0x0001, TAG, 'Succeeded in creating barCode.');
        }).catch((error: BusinessError) => {
          hilog.error(0x0001, TAG, `Failed to createBarCode. Code: ${error.code}, message: ${error.message}`);
        });
      })
        .margin({ top: 20, bottom: 20 });
      // 获取生成码后显示
      if (this.pixelMap1) {
        Image(this.pixelMap1).width(300).height(300).objectFit(ImageFit.Contain);
      }
    }
    .width('100%')
    .height('100%');

  }
}
```
