---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management-prop
title: "@Prop：父子单向同步"
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 状态管理与渲染控制 > 状态管理V1装饰器 > @Prop：父子单向同步
category: harmonyos-references
scraped_at: 2026-09-02T15:01:10+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bfe1235f6b3f194c7833031be84b3c63aaa026c0360948bb221fc94d7d2852d0
---

@Prop用于[状态管理V1](../harmonyos-guides/arkts-state-management-overview.md#状态管理v1)，接收外部传入值，并与父组件建立单向同步关系。当父组件中[@State](ts-state-management-state.md)等装饰的状态变量发生变化时，会同步更新到子组件中对应的@Prop变量，触发子组件重新渲染。@Prop采用单向数据流机制，子组件对@Prop变量的修改仅在子组件内部生效，不会反向同步到父组件。适用于子组件需要响应父组件状态变化但不需要反向修改的场景。

开发指南参考：[@Prop装饰器：父子单向同步](../harmonyos-guides/arkts-prop.md)。

**说明** 

从API version 7开始，支持该装饰器。

## @Prop

const Prop: PropertyDecorator

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ts
@Component
struct Child {
  // 使用@Prop装饰器接收父组件传入的值，与父组件建立单向同步关系
  // 父组件数据变化会同步到子组件，但子组件修改不会同步回父组件
  @Prop message: string = 'Hi';

  build() {
    Column() {
      Text(this.message)
    }
  }
}

@Entry
@Component
struct Index {
  // 使用@State声明状态变量，作为@Prop的数据源
  @State message: string = 'Hello';

  build() {
    Column() {
      // 创建子组件Child，将message单向绑定到子组件的@Prop变量
      Child({ message: this.message })
    }
  }
}
```
