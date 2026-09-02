---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-129
title: 对象反序列化时number类型丢失精度如何解决
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 对象反序列化时number类型丢失精度如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d6bb826de47548d52fa47a847575ef0b1ee212b9df84fe4f750aa88eccd56828
---

1. 通过[JSON.parse()](../harmonyos-references/js-apis-json.md#jsonparse)解析，可以通过传入options参数，指定options为bigIntMode: JSON.BigIntMode.PARSE\_AS\_BIGINT，来处理BigInt的模式。

   示例代码参考如下：

   ```screen
   import { JSON } from '@kit.ArkTS';

   let options: JSON.ParseOptions = {
     bigIntMode: JSON.BigIntMode.PARSE_AS_BIGINT,
   }
   let numberText = '{"largeNumber":1122333444455556666677777888889}';
   let numberObj = JSON.parse(numberText, (key: string, value: Object | undefined | null): Object | undefined | null => {
     if (key === "largeNumber") {
       return value;
     }
     return value;
   }, options) as Object;

   @Entry
   @Component
   struct BigIntDemo {
     @State str: string = 'bigint num';

     build() {
       Row() {
         Column() {
           Button(this.str)
             .onClick(() => {
               console.info((numberObj as object)?.["largeNumber"]); // 1122333444455556666677777888889
             })
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```
2. 使用三方库[json-bigint](https://ohpm.openharmony.cn/#/cn/detail/@ohmos%2Fjson-bigint)处理。
