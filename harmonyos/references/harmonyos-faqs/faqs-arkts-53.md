---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-53
title: .ets文件和.ts文件的区别及如何互相调用文件中定义的方法
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > .ets文件和.ts文件的区别及如何互相调用文件中定义的方法
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:01+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:4bc7ee4ef4625b249fe7e94f5241d5137afb408f68c027a9c75ce0fed4ea13b1
---

ArkTS基于兼容了TS语法，继承了TS的所有特性，当前，ArkTS在TS的基础上主要扩展了声明式UI能力，让开发者能够以更简洁、更自然的方式开发高性能应用。推荐用ArkTS开发UI相关内容，TS可以用来开发业务逻辑相关内容。

ts文件不支持调用ets文件中定义的方法。

ets调用ts文件中定义的方法，可以使用ES6中import引入及export导出的语法，将ts文件中的方法进行export导出，在ets文件中import引入该方法进行调用。

可以参考如下示例：

```
1. // Declare and export the method 'test' for external file import calls
2. export default function test() {
3. // to do something
4. }
```

[ExportTest.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/ExportTest.ts#L21-L24)

```
1. // Introduce the method defined in the ts file
2. import test from './ExportTest';

4. @Entry
5. @Component
6. struct eventTestExample {
7. build() {
8. Button('test')
9. .onClick(() => {
10. test(); // Call the methods defined in the ts file
11. })
12. }
13. }
```

[EventTestExample.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/EventTestExample.ets#L21-L33)
