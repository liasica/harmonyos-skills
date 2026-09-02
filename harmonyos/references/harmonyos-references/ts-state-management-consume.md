---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management-consume
title: "@Consume：与后代组件双向同步"
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 状态管理与渲染控制 > 状态管理V1装饰器 > @Consume：与后代组件双向同步
category: harmonyos-references
scraped_at: 2026-09-02T15:01:10+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a7e2f258a1cfad439d350c30a666fcbf7200416efc1f88cfd4e481fb2444d0c9
---

[@Provide](ts-state-management-provide.md)和@Consume配套使用，用于[状态管理V1](../harmonyos-guides/arkts-state-management-overview.md#状态管理v1)，实现跨组件层级的双向同步，适用于需要在多层嵌套组件间共享状态的场景，能够避免逐层传递的繁琐，简化组件间的通信逻辑。@Consume装饰的变量作为数据消费方，通过别名或变量名与@Provide装饰的变量建立双向绑定关系。当@Provide或@Consume装饰的变量发生变化时，变化会自动同步到对方。匹配规则：优先使用别名匹配，若未设置别名则使用变量名匹配。

开发指南参考：[@Provide装饰器和@Consume装饰器：与后代组件双向同步](../harmonyos-guides/arkts-provide-and-consume.md)。

**说明** 

从API version 7开始，支持该装饰器。

从API version 20开始，@Consume装饰的变量支持设置默认值。当查找不到@Provide的匹配结果时，@Consume装饰的变量会使用默认值进行初始化；当查找到@Provide的匹配结果时，@Consume装饰的变量会优先使用@Provide匹配结果的值，默认值不生效。

从API version 20开始，支持跨BuilderNode配对@Provide/@Consume。在BuilderNode场景下，BuilderNode会在上树前构造节点，所以BuilderNode内部定义的@Consume需要设置默认值，并在BuilderNode上树后，重新获取最近的@Provide数据，与之建立双向同步关系。

## @Consume

const Consume: PropertyDecorator & ((value: string) => PropertyDecorator)

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 否 | 用于设置别名，缺省时默认为变量名。设置别名后，@Consume通过别名与@Provide装饰的变量进行匹配绑定；未设置别名时，通过变量名进行匹配绑定，实现跨组件层级的数据双向同步。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| PropertyDecorator | 属性装饰器，开发者无需关注该返回值。 |

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
