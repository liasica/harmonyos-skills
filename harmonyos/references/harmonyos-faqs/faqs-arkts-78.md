---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-78
title: 如何在ArkTS中实现自定义装饰器能力
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何在ArkTS中实现自定义装饰器能力
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:05+08:00
doc_updated_at: 2026-03-25
content_hash: sha256:744fb0648297b8e03aec5b84251b3faa42a1f863eab1d82b11b2c254859e6284
---

ArkTS支持TS5.0之前（如TS4.x及以下版本）的TS装饰器语法。关于装饰器的定义和运行时行为，可以参考[TS官方文档](https://www.typescriptlang.org/docs/handbook/decorators.html)。

注意，如果在.ets文件中定义装饰器，则需要同时满足[从TypeScript到ArkTS的适配规则](../harmonyos-guides/typescript-to-arkts-migration-guide.md)，比如不能使用any等。

参考代码如下：

```
1. function MyDescriptor(target: Object, key: string, descriptor: PropertyDescriptor) {
2. const originalMethod: Function = descriptor.value
3. descriptor.value = (...args: Object[]) => {
4. // Get the name, input parameters, and return value of the decorated method
5. console.log(`Calling ${target.constructor?.name} method ${key} with argument: ${args}`)
6. const result: Object = originalMethod(...args)
7. console.log(`Method ${key} returned: ${result}`)
8. return result
9. }
10. return descriptor
11. }

13. @Entry
14. @Component
15. export struct MyDescriptorCom {
16. @State message: string = 'Hello World';

18. @MyDescriptor
19. demoFunc(str: string) {
20. return str
21. }

23. aboutToAppear(): void {
24. this.demoFunc('DemoTest')
25. }

27. build() {
28. Row() {
29. Column() {
30. Text(this.message)
31. .fontSize(50)
32. .fontWeight(FontWeight.Bold)
33. }
34. .width('100%')
35. }
36. .height('100%')
37. }
38. }
```

[MyDescriptorCom.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/MyDescriptorCom.ets#L21-L58)

说明

由于ArkTS当前运行时限制，当前版本暂不支持同时应用多个自定义装饰器。
