---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-128
title: 如何指定对象某些属性参与序列化
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何指定对象某些属性参与序列化
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ae7ad7502880f3fa8a5dedcb5c8099b1eff831ee2b23e9bb420282390631dc41
---

可以通过[JSON.stringify()](../harmonyos-references/js-apis-json.md#jsonstringify)方法实现，stringify(value: Object, replacer?: (number | string)[] | null, space?: string | number): string中，当replacer为数组时，只有包含在这个数组中的属性名才会被序列化到最终的JSON字符串中；当参数为null或者未提供时，则对象所有的属性都会被序列化。

示例代码参考如下：

```ts
import { JSON } from '@kit.ArkTS';

interface Person {
  name: string;
  age: number;
  city: string;
}

let obj: Person = { name: 'John', age: 30, city: 'ChongQing' };

@Entry
@Component
struct JSONDemo {
  @State str: string = 'to json';

  build() {
    Row() {
      Column() {
        Button(this.str)
          .onClick(() => {
            let jsonStr1 = JSON.stringify(obj); // All attributes are serialized
            console.info('jsonStr1：', jsonStr1); // jsonStr1： {"name":"John","age":30,"city":"ChongQing"}
            let jsonStr2 = JSON.stringify(obj, ['name']); // Specify the name attribute and serialize it
            console.info('jsonStr2：', jsonStr2); // jsonStr2： {"name":"John"}
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
