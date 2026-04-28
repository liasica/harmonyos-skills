---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-56
title: 如何访问类的静态变量和方法
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何访问类的静态变量和方法
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:02+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:fdba4e39d157f5c10d5c3592207eaaee9b5d6ada6d5e671ad702ea3a4bdfa934
---

在ArkTS中，静态变量和方法属于类自身，无法通过this访问，因为this指向类的实例。 若要在类中访问静态变量和方法，需要使用类名。

```
1. // Accessing static variables or executing static methods
2. class TestStatic {
3. static aaa: string = '3333';

5. static getAAA () {
6. // console.log(this.aaa) Static variables cannot be accessed through this and can only be used in static methods
7. return TestStatic.aaa;
8. }
9. }
10. TestStatic.aaa;
```

[TestStatic.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/TestStatic.ets#L21-L30)
