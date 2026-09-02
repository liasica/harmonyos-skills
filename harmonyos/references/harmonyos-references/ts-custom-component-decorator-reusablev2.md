---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-decorator-reusablev2
title: "@ReusableV2：组件复用V2"
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 自定义组件 > 组件扩展装饰器 > @ReusableV2：组件复用V2
category: harmonyos-references
scraped_at: 2026-09-02T15:01:08+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5da9c9388d79fef3a13bb5cf65f82dbe4feeab260266e383b2c32f673df53421
---

为了降低反复创建销毁自定义组件带来的性能开销，开发者可以使用@ReusableV2装饰[@ComponentV2](ts-custom-component-decorator-componentv2.md#componentv2)装饰的自定义组件，达成组件复用的效果，适用于列表滚动、频繁切换组件显示/隐藏等需要反复创建和销毁组件的场景，支持通过参数配置内存优化策略。

开发指南参考：[@ReusableV2装饰器：组件复用](../harmonyos-guides/arkts-new-reusablev2.md)。

组件复用的原理与适用场景参考：[组件复用最佳实践](../best-practices/bpta-component-reuse.md)。

**说明** 

本装饰器首批接口从API version 18开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## @ReusableV2

const ReusableV2: ClassDecorator & ((options: ReusableOptions) => ClassDecorator)

声明一个可复用的自定义组件。该装饰器必须与@ComponentV2搭配使用，用于装饰自定义组件，以实现组件复用。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ReusableOptions](ts-custom-component-parameter.md#reusableoptions) | 否 | 可复用自定义组件的配置参数，用于配置内存优化策略，在复用组件数量较多（例如同一页面中复用组件实例达到数十个以上）或设备内存有限、应用内存占用较高的场景下可配置此参数进行优化；缺省时无内存优化策略。  **起始版本：** 26.0.0 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ClassDecorator | 类装饰器。开发者无需关注该返回值。 |

**示例：**

```ts
@ObservedV2
class Info {
  @Trace age: number;

  constructor(age: number) {
    this.age = age;
  }
}

@Entry
@ComponentV2
struct Index {
  // 使用@Local控制子组件的显示与隐藏
  @Local condition: boolean = true;

  build() {
    Column() {
      Button('Reuse')
        .onClick(() => {
          // 点击按钮切换子组件的显示状态
          this.condition = !this.condition;
        })
      if (this.condition) {
        ReusableV2Component()
      }
    }
  }
}

// 使用@ReusableV2装饰器标记可复用组件，配合@ComponentV2使用
@ReusableV2
@ComponentV2
struct ReusableV2Component {
  noDecoratorInfo: Info = new Info(30);

  @Monitor('noDecoratorInfo.age')
  onAgeChange(monitor: IMonitor) {
    console.info(`age change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
  }

  // 组件被回收时的回调
  aboutToRecycle() {
    this.noDecoratorInfo.age = 25;
  }

  // 组件被复用时的回调
  aboutToReuse() {
    this.noDecoratorInfo.age = 35;
  }

  build() {
    Column() {
      Text(`noDecoratorInfo.age: ${this.noDecoratorInfo.age}`)
        .onClick(() => {
          // 能够触发刷新但是不会被重置
          this.noDecoratorInfo.age++;
        })
    }
  }
}
```
