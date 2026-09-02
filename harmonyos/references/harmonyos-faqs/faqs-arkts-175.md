---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-175
title: 常见数据格式与ArrayBuffer的互相转换
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 常见数据格式与ArrayBuffer的互相转换
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:73cb9597a133b4d573efbce0f742546665d16310e322dbdaf4031aa651efeb69
---

## 问题现象

ArrayBuffer是HarmonyOS开发中经常用到的数据类型，很多接口的入参都要求是ArrayBuffer，如何将一些常见的数据类型转换为ArrayBuffer类型？

## 背景知识

* [Base64Helper](../harmonyos-references/js-apis-util.md#base64helper9)：Base64Helper类提供Base64编解码和Base64URL编解码功能。
* [TextEncoder](../harmonyos-references/js-apis-util.md#textencoder)：TextEncoder将字符串编码为字节数组，支持多种编码格式。

## 解决方案

**Base64与ArrayBuffer互相转换**

Base64转ArrayBuffer：

```ts
/**
 * 将Base64格式字符串转换为ArrayBuffer类型
 * @param src Base64字符串
 * @returns ArrayBuffer格式数据
 */
public static base64ToArrayBuffer(src: string): ArrayBuffer {
  if (src.length == 0) {
    return new ArrayBuffer(0);
  }
  let base64Helper = new util.Base64Helper();
  let uint8Array = base64Helper.decodeSync(src);
  return uint8Array.buffer as ArrayBuffer;
}
```

ArrayBuffer转Base64：

```ts
/**
 * 将ArrayBuffer转换为Base64格式
 * @param src ArrayBuffer数据
 * @returns Base64格式字符串
 */
public static arrayBufferToBase64(src: ArrayBuffer): string {
  if (src.byteLength == 0) {
    return '';
  }
  // 将ArrayBuffer转成string，再编码成base64
  let textDecoder = util.TextDecoder.create('utf-8');
  return textDecoder.decodeToString(new Uint8Array(src));
}
```

**string与ArrayBuffer的互相转换**

string转ArrayBuffer：

```ts
/**
 * 将字符串转换为ArrayBuffer格式
 * @param src 字符串
 * @returns ArrayBuffer格式数据
 */
public static stringToArrayBuffer(src: string): ArrayBuffer {
  if (src.length == 0) {
    return new ArrayBuffer(0);
  }
  let textEncoder = util.TextEncoder.create('UTF-8');
  const uint8Array = textEncoder.encodeInto(src);
  return uint8Array.buffer as ArrayBuffer;
}
```

ArrayBuffer转string：

```ts
/**
 * 将ArrayBuffer格式转换为字符串
 * @param src ArrayBuffer格式数据
 * @returns 字符串
 */
public static arrayBufferToString(src: ArrayBuffer): string {
  let textDecoder = util.TextDecoder.create('UTF-8');
  let uint8Array = new Uint8Array(src);
  return textDecoder.decodeToString(uint8Array);
}
```

**collections.ArrayBuffer与ArrayBuffer的互相转换**

collections.ArrayBuffer转ArrayBuffer：

```ts
/**
 * 将collections.ArrayBuffer格式数据转换为ArrayBuffer
 * @param src collections.ArrayBuffer格式数据
 * @returns ArrayBuffer格式数据
 */
public static CollectionsArrayBufferToArrayBuffer(src: collections.ArrayBuffer): ArrayBuffer {
  if (src.byteLength == 0) {
    return new ArrayBuffer(0);
  }
  let collectionsUint8Array = new collections.Uint8Array(src);
  let uint8Array = new Uint8Array(collectionsUint8Array);
  return uint8Array.buffer as ArrayBuffer;
}
```

ArrayBuffer转collections.ArrayBuffer：

```ts
/**
 * 将ArrayBuffer格式数据转换为collections.ArrayBuffer
 * @param src ArrayBuffer格式数据
 * @returns collections.ArrayBuffer格式数据
 */
public static ArrayBufferToCollectionsArrayBuffer(src: ArrayBuffer): collections.ArrayBuffer {
  if (src.byteLength == 0) {
    return new collections.ArrayBuffer(0);
  }
  let uint8Array: Uint8Array = new Uint8Array(src);
  let collectionsUint8Array: collections.Uint8Array = new collections.Uint8Array(uint8Array);
  return collectionsUint8Array.buffer as collections.ArrayBuffer;
}
```

完整代码及测试样例如下：

pages/Index.ets：

```ts
import { StringUtil, Base64Util, CollectionsArrayBufferUtil } from '../utils/ArrayBufferUtil';
import { collections } from '@kit.ArkTS';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button('Base64与Arraybuffer互相转换')
        .onClick(() => {
          let base64 = 'SGVsbG8gSGFybW9ueU9TLCBIZWxsbyBXb3JsZC4=';
          let ret: ArrayBuffer = Base64Util.base64ToArrayBuffer(base64);
          let uint8Array = new Uint8Array(ret);
          console.info(uint8Array.toString());

          base64 = Base64Util.arrayBufferToBase64(ret);
          console.info(base64);
        })
        .margin({
          bottom: 20
        });

      Button('string和ArrayBuffer互相转换')
        .onClick(() => {
          let str = 'Hello HarmonyOS, Hello World.';
          let ret: ArrayBuffer = StringUtil.stringToArrayBuffer(str);
          let uint8Array = new Uint8Array(ret);
          console.info(uint8Array.toString());

          str = StringUtil.arrayBufferToString(ret);
          console.info(str);
        })
        .margin({
          bottom: 20
        });

      Button('collections.ArrayBuffer与ArrayBuffer互相转换')
        .onClick(() => {
          let array =
            [72, 101, 108, 108, 111, 32, 72, 97, 114, 109, 111, 110, 121, 79, 83, 44, 32, 72, 101, 108, 108, 111, 32,
              87, 111, 114, 108, 100, 46];
          let collectionsArrayBuffer = new collections.Uint8Array(array).buffer;
          let ret: ArrayBuffer = CollectionsArrayBufferUtil.CollectionsArrayBufferToArrayBuffer(collectionsArrayBuffer);
          let uint8Array = new Uint8Array(ret);
          console.info(uint8Array.toString());

          collectionsArrayBuffer = CollectionsArrayBufferUtil.ArrayBufferToCollectionsArrayBuffer(ret);
          console.info(`collectionsArrayBuffer.byteLength: ${collectionsArrayBuffer.byteLength}`);
        });
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```

utils/ArrayBufferUtil.ets：

```ts
import { collections, util } from '@kit.ArkTS';

/**
 * 提供Base64格式数据与ArrayBuffer的互相转换能力
 */
export class Base64Util {
  /**
   * 将Base64格式字符串转换为ArrayBuffer类型
   * @param src Base64字符串
   * @returns ArrayBuffer格式数据
   */
  public static base64ToArrayBuffer(src: string): ArrayBuffer {
    if (src.length == 0) {
      return new ArrayBuffer(0);
    }
    let base64Helper = new util.Base64Helper();
    let uint8Array = base64Helper.decodeSync(src);
    return uint8Array.buffer as ArrayBuffer;
  }

  /**
   * 将ArrayBuffer转换为Base64格式
   * @param src ArrayBuffer数据
   * @returns Base64格式字符串
   */
  public static arrayBufferToBase64(src: ArrayBuffer): string {
    if (src.byteLength == 0) {
      return '';
    }
    // 将ArrayBuffer转成string，再编码成base64
    let textDecoder = util.TextDecoder.create('utf-8');
    return textDecoder.decodeToString(new Uint8Array(src));
  }

}
;

/**
 * 提供string格式数据与ArrayBuffer的互相转换能力
 */
export class StringUtil {
  /**
   * 将字符串转换为ArrayBuffer格式
   * @param src 字符串
   * @returns ArrayBuffer格式数据
   */
  public static stringToArrayBuffer(src: string): ArrayBuffer {
    if (src.length == 0) {
      return new ArrayBuffer(0);
    }
    let textEncoder = util.TextEncoder.create('UTF-8');
    const uint8Array = textEncoder.encodeInto(src);
    return uint8Array.buffer as ArrayBuffer;
  }

  /**
   * 将ArrayBuffer格式转换为字符串
   * @param src ArrayBuffer格式数据
   * @returns 字符串
   */
  public static arrayBufferToString(src: ArrayBuffer): string {
    let textDecoder = util.TextDecoder.create('UTF-8');
    let uint8Array = new Uint8Array(src);
    return textDecoder.decodeToString(uint8Array);
  }

}

/**
 * 提供collections.ArrayBuffer格式数据与ArrayBuffer的互相转换能力
 */
export class CollectionsArrayBufferUtil {
  /**
   * 将collections.ArrayBuffer格式数据转换为ArrayBuffer
   * @param src collections.ArrayBuffer格式数据
   * @returns ArrayBuffer格式数据
   */
  public static CollectionsArrayBufferToArrayBuffer(src: collections.ArrayBuffer): ArrayBuffer {
    if (src.byteLength == 0) {
      return new ArrayBuffer(0);
    }
    let collectionsUint8Array = new collections.Uint8Array(src);
    let uint8Array = new Uint8Array(collectionsUint8Array);
    return uint8Array.buffer as ArrayBuffer;
  }

  /**
   * 将ArrayBuffer格式数据转换为collections.ArrayBuffer
   * @param src ArrayBuffer格式数据
   * @returns collections.ArrayBuffer格式数据
   */
  public static ArrayBufferToCollectionsArrayBuffer(src: ArrayBuffer): collections.ArrayBuffer {
    if (src.byteLength == 0) {
      return new collections.ArrayBuffer(0);
    }
    let uint8Array: Uint8Array = new Uint8Array(src);
    let collectionsUint8Array: collections.Uint8Array = new collections.Uint8Array(uint8Array);
    return collectionsUint8Array.buffer as collections.ArrayBuffer;
  }

}
```
