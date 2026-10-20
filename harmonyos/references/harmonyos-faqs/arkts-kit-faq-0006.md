---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkts-kit-faq-0006
title: Uint8Array与String及hex类型转换常见问题
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 常见问题 > Uint8Array与String及hex类型转换常见问题
category: harmonyos-faqs
scraped_at: 2026-10-21T07:10:19+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:5f98ea3070629b5d1a852b7118f32efe714bd8dd7d9778ae81ddb650ffabe4d1
---

**Q：Uint8Array类型和String以及hex如何互相转换？**

**A**：Uint8Array类型和String以及hex实现互相转换，可参考如下代码：

```ts
import { buffer, util } from '@kit.ArkTS';

// Convert string to byte stream
function stringToUint8Array(str: string) {
  console.info('Convert string to byte stream:' + new Uint8Array(buffer.from(str, 'utf-8').buffer));
  return new Uint8Array(buffer.from(str, 'utf-8').buffer);
}

// Byte flow into understandable strings
function uint8ArrayToString(array: Uint8Array) {
  let textDecoderOptions: util.TextDecoderOptions = {
    fatal: false,
    ignoreBOM: true
  }
  let decodeToStringOptions: util.DecodeToStringOptions = {
    stream: false
  }
  let textDecoder = util.TextDecoder.create('utf-8', textDecoderOptions);
  let retStr = textDecoder.decodeToString(array, decodeToStringOptions);
  console.info('Byte flow into understandable strings：' + retStr);
  return retStr;
}

//Hexadecimal to Uint8Array
function HexStrTouint8Array(data: string): Uint8Array {
  console.info('Hexadecimal to Uint8Array:' + new Uint8Array(buffer.from(data, 'hex').buffer));
  return new Uint8Array(buffer.from(data, 'hex').buffer);
}

// Uint8Array to hexadecimal
function uint8ArrayToHexStr(data: Uint8Array): string {
  let hexString = '';
  let i: number;
  for (i = 0; i < data.length; i++) {
    let char = ('00' + data[i].toString(16)).slice(-2);
    hexString += char;
  }
  console.info('Uint8Array to hexadecimal:' + hexString);
  return hexString;
}

let uint8Array: Uint8Array;

@Entry
@Component
struct TypeConversion {
  build() {
    Column({ space: 12 }) {
      Button('Convert string to byte stream')
        .onClick(() => {
          let str = 'hello';
          uint8Array = stringToUint8Array(str);
        })
      Button('Byte flow string')
        .onClick(() => {
          if (uint8Array) {
            uint8ArrayToString(uint8Array);
          }
        })
      Button('Hexadecimal to Uint8Array')
        .onClick(() => {
          let data = '05160b22';
          HexStrTouint8Array(data);
        })
      Button('Uint8Array to hexadecimal')
        .onClick(() => {
          let uint8Array = new Uint8Array([5, 22, 11, 34]);
          uint8ArrayToHexStr(uint8Array);
        })
    }
    .width('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```
