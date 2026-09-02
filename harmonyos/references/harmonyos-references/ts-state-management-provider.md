---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management-provider
title: "@Provider：跨组件层级双向同步"
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 状态管理与渲染控制 > 状态管理V2装饰器 > @Provider：跨组件层级双向同步
category: harmonyos-references
scraped_at: 2026-09-02T15:01:10+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3470f9c645e684dece8061ee5d9b32c5d4467ca080a7c5d948b131652904d548
---

@Provider和[@Consumer](ts-state-management-consumer.md)搭配使用，用于[状态管理V2](../harmonyos-guides/arkts-state-management-overview.md#状态管理v2)中，实现跨组件层级的数据双向同步。@Provider装饰数据提供方，为子组件提供数据，适用于组件层级较深、需要跨多层组件共享状态且避免逐层传递数据的场景，可简化状态管理流程，降低组件间的耦合度。

开发指南参考：[@Provider装饰器和@Consumer装饰器：跨组件层级双向同步](../harmonyos-guides/arkts-new-provider-and-consumer.md)。

**说明** 

从API version 12开始，支持该装饰器。

## @Provider

const Provider: (aliasName?: string) => PropertyDecorator

用于状态管理V2中，需与@Consumer搭配使用，实现跨组件层级的数据双向同步；装饰数据提供方，为子组件提供数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| aliasName | string | 否 | 用于设置别名，作为@Provider与@Consumer之间数据双向同步的匹配标识，需与@Consumer的别名一致；缺省时为变量名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| PropertyDecorator | 属性装饰器。开发者无需关注该返回值。 |

**示例：**

```ts
@Entry
@ComponentV2
struct Index {
  // @Provider提供原始数据
  @Provider() str: string = 'aaa';

  build() {
    Column() {
      Text(`parent: ${this.str}`)
      Child()
    }
  }
}

@ComponentV2
struct Child {
  // @Consumer同步数据
  @Consumer() str: string = '';

  build() {
    Column() {
      Text(`child: ${this.str}`)
    }
  }
}
```
