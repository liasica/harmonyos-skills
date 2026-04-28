---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-type
title: @Type装饰器：标记类属性的类型
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理（V2） > 管理数据对象的状态 > @Type装饰器：标记类属性的类型
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2520dcce167790350c2c77db853f09b39277f2531b32949e0e303b27673cc7fc
---

为了实现序列化类时不丢失属性的复杂类型，开发者可以使用@Type装饰器装饰类属性。

@Type的目的是标记类属性，配合PersistenceV2使用，防止序列化时类丢失。在阅读本文档前，建议提前阅读：[PersistenceV2](arkts-new-persistencev2.md)。

说明

@Type从API version 12开始支持。

从API version 12开始，该装饰器支持在元服务中使用。

## 概述

@Type标记类属性，使得类属性序列化时不丢失类型信息，便于类的反序列化。

## 装饰器说明

| @Type装饰器 | 说明 |
| --- | --- |
| 装饰器参数 | type：类型。 |
| 可装饰的类型 | Object class以及Array、Date、Map、Set等内嵌类型。 |

## 使用限制

1. 只能用在[@ObservedV2](arkts-new-observedv2-and-trace.md)装饰的类中，不能用在自定义组件中。

   ```
   1. class Sample {
   2. private data: number = 0;
   3. }
   4. @ObservedV2
   5. class Info {
   6. @Type(Sample)
   7. @Trace public sample: Sample = new Sample(); // 正确用法
   8. }
   ```

   [DataModel.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NewType/entry/src/main/ets/pages/DataModel.ets#L16-L25)

   ```
   1. @Observed
   2. class Info2 {
   3. @Type(Sample)
   4. sample: Sample = new Sample(); // 错误用法，不能用在@Observed装饰的类中，编译时报错
   5. }
   6. @ComponentV2
   7. struct Index {
   8. @Type(Sample)
   9. sample: Sample = new Sample(); // 错误用法，不能用在自定义组件中，编译时报错
   10. build() {
   11. }
   12. }
   ```
2. 不支持collections.Set、collections.Map等类型。
3. 不支持非built-in类型。如[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)、NativePointer、[ArrayList](../harmonyos-references/js-apis-arraylist.md)等Native类型。
4. 不支持简单类型。如string、number、boolean等。
5. 不支持构造函数含参的类。

## 使用场景

### 持久化数据

```
1. import { PersistenceV2, Type } from '@kit.ArkUI';

3. @ObservedV2
4. class SampleChild {
5. @Trace childNumber: number = 1;
6. }

8. @ObservedV2
9. class Sample {
10. // 对于复杂对象需要@Type修饰，确保反序列化成功，去掉@Type会反序列化值失败。
11. @Type(SampleChild)
12. // 对于没有初值的类属性，经过@Type修饰后，需要手动保存，否则持久化失败。
13. // 无法使用@Type修饰的类属性，必须要有初值才能持久化。
14. @Trace sampleChild?: SampleChild = undefined;
15. }

17. @Entry
18. @ComponentV2
19. struct TestCase {
20. @Local sample: Sample = PersistenceV2.connect(Sample, () => new Sample)!;

22. build() {
23. Column() {
24. Text('childNumber value:' + this.sample.sampleChild?.childNumber)
25. .onClick(() => {
26. this.sample.sampleChild = new SampleChild();
27. this.sample.sampleChild.childNumber = 2;
28. PersistenceV2.save(Sample);
29. })
30. .fontSize(30)
31. }
32. }
33. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NewType/entry/src/main/ets/pages/Index.ets#L15-L49)
