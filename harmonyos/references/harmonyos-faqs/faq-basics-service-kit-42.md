---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-42
title: zip.deflate压缩数据后，如何获取到编码后数据长度
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > zip.deflate压缩数据后，如何获取到编码后数据长度
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:39+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:77d04d287380eaae514ceb90b4fb152e30ccd7978efd52cc78118d213d967e1e
---

## 问题现象

zip.deflate压缩数据后调用zStream.totalOut，编码后zStream的totalOut都没有发生改变，一直都是0，应该怎么获取到编码后数据长度？

```ts
import { zlib } from '@kit.BasicServicesKit';

async function getTotalOutOfzStream() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray[i] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zStream: zlib.ZStream = {
    nextIn: arrayBufferIn,
    availableIn: arrayBufferIn.byteLength,
    nextOut: arrayBufferOut,
    availableOut: arrayBufferOut.byteLength,
    totalOut: 0
  };
  try {
    let zip = zlib.createZipSync();
    await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED)
    await zip.deflate(zStream, zlib.CompressFlushMode.FINISH)

    // 使用zStream获取totalOut
    let totalOut = zStream.totalOut
    console.info(`The total out of zStream is ` + totalOut)
  } catch (e) {
    console.error(e)
  }
}
```

## 解决方案

每次操作完成，需要重新getZStream()获取最新状态，参考：[压缩与解压](../harmonyos-guides/deflate-and-inflate.md#接口说明)。

```ts
import { zlib } from '@kit.BasicServicesKit';

async function getTotalOutOfzStream() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray[i] = str.charCodeAt(i);
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zStream: zlib.ZStream = {
    nextIn: arrayBufferIn,
    availableIn: arrayBufferIn.byteLength,
    nextOut: arrayBufferOut,
    availableOut: arrayBufferOut.byteLength,
    totalOut: 0
  };
  try {
    let zip = zlib.createZipSync();
    await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED);
    await zip.deflate(zStream, zlib.CompressFlushMode.FINISH);

    // 重新getZStream()获取最新状态，然后获取totalOut
    let totalOut = (await zip.getZStream()).totalOut;
    console.info('The total out of zStream is ' + totalOut);
  } catch (e) {
    console.error(e);
  }
}

@Entry
@Component
struct Index {
  message: string = 'Hello World';

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          getTotalOutOfzStream();
        });
    }
    .height('100%')
    .width('100%');
  }
}
```
