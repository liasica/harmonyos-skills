---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-104
title: 如何处理大整数
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何处理大整数
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:df8e28de57e034e1632cc5d41ff14b790a8d9deb9667993d4f7479e561ec8981
---

使用BigInt来处理大整数。

BigInt可以表示任意大小的整数。使用BigInt时，在整数字面量后面添加n后缀或使用BigInt()构造函数。

示例如下：

```ts
@Entry
@Component
struct BigIntNum {
  build() {
    Row() {
      Column() {
        Button('BigInt num')
          .onClick(() => {
            let bigIntNum: bigint = 12345678901234567890n; // Add n suffix after integer
            let anotherBigInt: bigint = BigInt(9007199254740992); // Use BigInt() constructor
            let sumBigInt: bigint = bigIntNum + anotherBigInt;
            console.info('bigIntNum:' + bigIntNum);
            console.info('anotherBigInt:' + anotherBigInt);
            console.info('bigIntNum + anotherBigInt:' + sumBigInt);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
