---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management-objectlink
title: "@ObjectLink：嵌套类对象属性变化"
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 状态管理与渲染控制 > 状态管理V1装饰器 > @ObjectLink：嵌套类对象属性变化
category: harmonyos-references
scraped_at: 2026-09-02T15:01:10+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:039011875d3976599a6b822ad9954fa9e926cb435f46841cf845f3219203ed75
---

@ObjectLink用于[状态管理V1](../harmonyos-guides/arkts-state-management-overview.md#状态管理v1)中，接收[@Observed](ts-state-management-observed.md)装饰的类的实例，并与父组件中的数据源建立双向数据绑定，适用于在子组件中独立观察并监听嵌套类属性并触发UI刷新的场景。

开发指南参考：[@Observed装饰器和@ObjectLink装饰器：嵌套类对象属性变化](../harmonyos-guides/arkts-observed-and-objectlink.md)。

**说明** 

从API version 7开始，支持该装饰器。

## @ObjectLink

const ObjectLink: PropertyDecorator

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ts
@Observed
class Info {
  name: string;
  constructor(name: string) {
    this.name = name;
  }
}

@Component
struct Child {
  @ObjectLink info: Info; // @ObjectLink接收父组件@State变量
  build() {
    Column() {
      Text(`name: ${this.info.name}`)
    }
  }
}

@Entry
@Component
struct Index {
  @State info: Info = new Info('Tom');
  build() {
    Column() {
      Child({info: this.info}) // @State状态变量作为@ObjectLink的初始值
    }
  }
}
```
