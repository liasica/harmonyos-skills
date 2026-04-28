---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-115
title: 如何获取对象的所有方法
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何获取对象的所有方法
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:14+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:cd76f5d7c6f61e79ad1fc337e2058ede445b14c233d2ec122c5e2a37e459f784
---

可以使用Object.getOwnPropertyNames获取所有方法的字符串数组。注意，获取对象的原型prototype需要文件后缀为.ts。参考代码如下：

1. 定义需要获取方法的类文件testClass.ts；

```
1. export class TestClass {
2. public test(): string {
3. return 'ArkUI Web Component';
4. }

6. public toString(): void {
7. console.info('Web Component toString');
8. }

10. public funToString(): void {
11. console.info('Web Component toString');
12. }
13. }
```

[TestClass.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/utils/TestClass.ts#L21-L34)

2. 获取文件中的方法；

```
1. import { TestClass } from '../utils/TestClass';

3. let protoType = testClass.prototype;
4. let methodsName: string[] = Object.getOwnPropertyNames(protoType);
5. console.info(methodsName.toString());

7. @Entry
8. @Component
9. struct GetObjectAllFun {
10. @State message: string = 'Hello World';

12. build() {
13. Row() {
14. Column() {
15. Text(this.message)
16. .fontSize(50)
17. .fontWeight(FontWeight.Bold)
18. }
19. .width('100%')
20. }
21. .height('100%')
22. }
23. }
```

[GetObjectAllFun.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/GetObjectAllFun.ets#L21-L44)
