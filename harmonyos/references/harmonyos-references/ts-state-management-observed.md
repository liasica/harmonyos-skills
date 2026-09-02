---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management-observed
title: "@Observed：嵌套类对象属性变化"
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 状态管理与渲染控制 > 状态管理V1装饰器 > @Observed：嵌套类对象属性变化
category: harmonyos-references
scraped_at: 2026-09-02T15:01:10+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6682eaa9b012411c78f9b9f4dd3d8a32b73db5e4878eb88a5d1548d8afb19e8d
---

@Observed是类装饰器，用于[状态管理V1](../harmonyos-guides/arkts-state-management-overview.md#状态管理v1)中，观察嵌套类对象的属性变化。

开发指南参考：[@Observed装饰器和@ObjectLink装饰器：嵌套类对象属性变化](../harmonyos-guides/arkts-observed-and-objectlink.md)。

**说明** 

从API version 7开始，支持该装饰器。

## @Observed

const Observed: ClassDecorator

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ts
// 使用@Observed类装饰器，使Info类的属性变化可被ArkUI框架观察
@Observed
class Info {
  name: string;
  constructor(name: string) {
    this.name = name;
  }
}

@Entry
@Component
struct Index {
  @State info: Info = new Info('Tom');
  build() {
    Column() {
      Text(`name: ${this.info.name}`)
    }
  }
}
```
