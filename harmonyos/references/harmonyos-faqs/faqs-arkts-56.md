---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-56
title: 如何访问类的静态变量和方法
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何访问类的静态变量和方法
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4d51a7da467fed73150cdb9af657543365397e67ead21aca7d5cf4c9ef97485c
---

在ArkTS中，静态变量和方法属于类自身，无法通过this访问，因为this指向类的实例。 若要在类中访问静态变量和方法，需要使用类名。

```ts
// Accessing static variables or executing static methods
class TestStatic {
  static aaa: string = '3333';

  static getAAA () {
    // console.log(this.aaa) Static variables cannot be accessed through this and can only be used in static methods
    return TestStatic.aaa;
  }
}
TestStatic.aaa;
```
