---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-115
title: 如何获取对象的所有方法
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何获取对象的所有方法
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4ea5656c9706c942a3df52925303491840fa8c82d714e58ee6b643d5247c60b7
---

可以使用Object.getOwnPropertyNames获取所有方法的字符串数组。注意，获取对象的原型prototype需要文件后缀为.ts。参考代码如下：

1. 定义需要获取方法的类文件testClass.ts；

```ts
export class TestClass {
  public test(): string {
    return 'ArkUI Web Component';
  }

  public toString(): void {
    console.info('Web Component toString');
  }

  public funToString(): void {
    console.info('Web Component toString');
  }
}
```

2. 获取文件中的方法；

```ts
import { TestClass } from '../utils/TestClass';

let protoType = testClass.prototype;
let methodsName: string[] = Object.getOwnPropertyNames(protoType);
console.info(methodsName.toString());

@Entry
@Component
struct GetObjectAllFun {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
