---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management-provide
title: "@Provide：与后代组件双向同步"
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 状态管理与渲染控制 > 状态管理V1装饰器 > @Provide：与后代组件双向同步
category: harmonyos-references
scraped_at: 2026-09-02T15:01:10+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:27fd50a151df864c346c4f51792dd92450c428bf42f75476834ba9c01d259fc7
---

@Provide和[@Consume](ts-state-management-consume.md)配套使用，用于[状态管理V1](../harmonyos-guides/arkts-state-management-overview.md#状态管理v1)，实现跨组件层级的双向同步，适用于需要跨越多层组件传递状态、避免逐层传递的场景，能够解决组件层级较深时状态传递繁琐的问题。@Provide装饰的变量作为数据源，通过别名或变量名与@Consume装饰的变量建立双向绑定关系。当@Provide或@Consume装饰的变量发生变化时，变化会自动同步到对方。

开发指南参考：[@Provide装饰器和@Consume装饰器：与后代组件双向同步](../harmonyos-guides/arkts-provide-and-consume.md)。

**说明** 

本装饰器从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## @Provide

const Provide: PropertyDecorator & ((value: string | ProvideOptions) => PropertyDecorator)

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | [ProvideOptions](ts-state-management-provide.md#provideoptions11) | 否 | 用于设置别名或允许重写的别名。  类型为string时，将直接作为别名，后代组件可通过该别名访问数据。  类型为ProvideOptions时，若设置了allowOverride，allowOverride的值将作为别名且该别名允许重写；若未设置allowOverride，则别名为变量名，不允许重写。  value缺省时别名为变量名，不允许重写。若此时定义同名@Provide，运行时会报错。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| PropertyDecorator | 属性装饰器，开发者无需关注该返回值。 |

## ProvideOptions11+

ProvideOptions是@Provide的选项。允许在同一组件树上通过allowOverride重写同名的@Provide，适用于子组件需要覆盖父组件同名@Provide值的场景，提高了跨层级状态管理的灵活性。具体例子可见[@Provide支持allowOverride参数](../harmonyos-guides/arkts-provide-and-consume.md#provide支持allowoverride参数)。

**卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**属性**：

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| allowOverride | string | 否 | 是 | 允许@Provide重写的别名。允许在同一组件树下通过allowOverride重写同名的@Provide。  缺省时表示@Provide不允许重写。若在未设置allowOverride的情况下定义同名@Provide，运行时会报错。 |

**示例：**

```ts
@Entry
@Component
struct Index {
  @Provide message: string = 'aaa'; // @Provide提供数据，未设置别名，使用变量名message进行匹配

  build() {
    Column() {
      Text(`provide: ${this.message}`)
      Child()
    }
  }
}

@Component
struct Child {
  @Consume message: string; // @Consume消费数据，未设置别名，使用变量名message与@Provide建立配对关系

  build() {
    Column() {
      Text(`consume: ${this.message}`)
    }
  }
}
```
