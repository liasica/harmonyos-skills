---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-77
title: 如何在ArkTS中实现运行时注解的能力
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何在ArkTS中实现运行时注解的能力
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:05+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:9f658a8ac98699711b9182cdb0c1f6199062cae7e9100517e82f9447a8904fc7
---

可以使用TS三方库reflect-metadata获得类似Java运行时注解的功能。参考[reflect-metadata](https://gitcode.com/openharmony-tpc/openharmony_tpc_samples/tree/master/reflect-metadata#https://gitee.com/openharmony-tpc/docs/blob/master/OpenHarmony_har_usage.md)

reflect-metadata提供的装饰器允许对类、属性和方法进行标记，并提供了接口以在运行时获取这些标记信息。

```
1. import "reflect-metadata";

3. // The ability of third-party packaging is exposed in Reflect
4. @Reflect.metadata("TargetClass", 'classData')
5. // Tag class, key is "targetClass", data is classData
6. class MyClass {
7. @Reflect.metadata("TargetMethod", 'methodData')
8. // Tag method, key is' Target Method ', data is' methodData'
9. myMethod() {
10. }

12. @Reflect.metadata("Static", 'staticData')
13. static invoke() {
14. }
15. }

17. // Retrieve tag information at runtime
18. console.info(Reflect.getMetadata("TargetClass", MyClass)); //classData
19. console.info(Reflect.getMetadata("TargetMethod", new MyClass(), "myMethod")); //methodData
20. console.info(Reflect.getMetadata("Static", MyClass, "invoke")); // staticData
```

[MetaData.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/MetaData.ets#L21-L40)
