---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management-type
title: "@Type：标记类属性的类型"
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 状态管理与渲染控制 > 状态管理V2装饰器 > @Type：标记类属性的类型
category: harmonyos-references
scraped_at: 2026-09-02T15:01:10+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7d4e63cc3dbfbd7b8a623fd579e23b005221053521356a20dde46ee80e576d53
---

@Type装饰类属性，用于[状态管理V2](../harmonyos-guides/arkts-state-management-overview.md#状态管理v2)，确保序列化类时不丢失属性的复杂类型。在使用[PersistenceV2](js-apis-statemanagement.md#persistencev2)等持久化能力对复杂类对象进行序列化和反序列化时，类的属性类型信息可能会丢失。通过@Type标记属性的原始类型，可确保在序列化过程中正确保留和还原属性的复杂类型信息，适用于需要持久化或序列化复杂对象的场景，例如应用状态持久化存储、跨组件复杂数据传递等。

开发指南参考：[@Type装饰器：标记类属性的类型](../harmonyos-guides/arkts-new-type.md)。

**说明** 

从API version 12开始，支持该装饰器。

## @Type

const Type: TypeDecorator

@Type标记属性的原始类型，可确保在序列化过程中正确保留和还原属性的复杂类型信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [TypeConstructor<T>](js-apis-statemanagement.md#typeconstructort) | 是 | 标记类属性的原始类型，取值为对应类的构造函数，需与被装饰属性的类型一致。 |

**示例：**

```ts
import { PersistenceV2, Type } from '@kit.ArkUI';

@ObservedV2
class SampleChild {
  @Trace childNumber: number = 1;
}

@ObservedV2
class Sample {
  // 使用@Type装饰器标记sampleChild属性的类型为SampleChild
  // 确保序列化时不会丢失属性的复杂类型信息
  @Type(SampleChild)
  @Trace sampleChild?: SampleChild = undefined;
}

@Entry
@ComponentV2
struct Index {
  // 使用@Local装饰器声明组件内部状态变量
  // 通过PersistenceV2.connect连接持久化数据，若不存在则创建新的Sample实例
  @Local sample: Sample = PersistenceV2.connect(Sample, () => new Sample)!;

  build() {
    Column() {
      Text(`childNumber value: ${this.sample.sampleChild?.childNumber}`)
        .onClick(() => {
          this.sample.sampleChild = new SampleChild();
          this.sample.sampleChild.childNumber = 2;
          PersistenceV2.save(Sample);
        })
        .fontSize(30)
    }
  }
}
```
