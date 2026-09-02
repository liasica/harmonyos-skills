---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-87
title: 如何获取对象的类名
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何获取对象的类名
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7733a26b4f747d02a14013519f4cdd8da8b0b107d7be8325087db5c04893d6a9
---

获取类的实例，通过constructor的name属性获取类名。

示例如下：

```ts
class TestClass {
  a: string = 'A';
  b: string = 'B';
}

let testClassObj: TestClass = new TestClass();

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('get Class Name')
          .onClick(() => {
            console.log('TestClass Name:', testClassObj.constructor.name);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
