---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-87
title: 如何获取对象的类名
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何获取对象的类名
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:07+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:2fbfe05b2d9c1251b065715292ca876f1ca00aacbe17c36b024aef461d17f756
---

获取类的实例，通过constructor的name属性获取类名。

示例如下：

```
1. class TestClass {
2. a: string = 'A';
3. b: string = 'B';
4. }

6. let testClassObj: TestClass = new TestClass();

8. @Entry
9. @Component
10. struct Index {
11. build() {
12. Row() {
13. Column() {
14. Button('get Class Name')
15. .onClick(() => {
16. console.log('TestClass Name:', testClassObj.constructor.name);
17. })
18. }
19. .width('100%')
20. }
21. .height('100%')
22. }
23. }
```

[ClassObjName.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/ClassObjName.ets#L21-L43)
