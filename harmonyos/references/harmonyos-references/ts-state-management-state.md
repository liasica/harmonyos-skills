---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management-state
title: "@State：组件内状态"
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 状态管理与渲染控制 > 状态管理V1装饰器 > @State：组件内状态
category: harmonyos-references
scraped_at: 2026-09-02T15:01:10+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1d84d2287cd0ecd5435153dff1d4fd015ff471e4e97631461c5a970d1ed05924
---

@State用于[状态管理V1](../harmonyos-guides/arkts-state-management-overview.md#状态管理v1)，将自定义组件内的普通变量转变为状态变量，当状态变量变化时，触发组件内UI重新渲染。适用于需要在组件内管理可变状态的场景。

开发指南参考：[@State装饰器：组件内状态](../harmonyos-guides/arkts-state.md)。

**说明** 

从API version 7开始，支持该装饰器。

## @State

const State: PropertyDecorator

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ts
@Entry
@Component
struct StateExample {
  @State count: number = 0; // 状态变量

  build() {
    Column() {
      Text(`${this.count}`)
    }
  }
}
```
