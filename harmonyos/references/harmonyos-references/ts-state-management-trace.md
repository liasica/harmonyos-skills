---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management-trace
title: "@Trace：类属性变化观测"
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 状态管理与渲染控制 > 状态管理V2装饰器 > @Trace：类属性变化观测
category: harmonyos-references
scraped_at: 2026-09-02T15:01:10+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:44be2a9605b0bc12e7624c0f5a3e4d32d4fedd9d1113243dcb00387c6dd60096
---

@Trace是属性装饰器，用于[状态管理V2](../harmonyos-guides/arkts-state-management-overview.md#状态管理v2)中。[@ObservedV2](ts-state-management-observedv2.md)与@Trace配套使用，装饰类以及类中的属性，使被装饰的类和属性具有深度观测能力，即能够深度观测嵌套对象中属性值的变化，并触发UI自动刷新，适用于需要精确观测和管理类属性变化状态的场景。

开发指南参考：[@ObservedV2装饰器和@Trace装饰器：类属性变化观测](../harmonyos-guides/arkts-new-observedv2-and-trace.md)。

**说明** 

从API version 12开始，支持该装饰器。

## @Trace

const Trace: PropertyDecorator

声明一个可观察属性，@Trace需与@ObservedV2配套使用，仅在@ObservedV2装饰的类中生效。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ts
@ObservedV2
class Son {
  // 使用@Trace属性装饰器标记需要观测的属性，属性变化时触发UI刷新
  @Trace age: number = 100;
}

class Father {
  son: Son = new Son();
}

@Entry
@ComponentV2
struct Index {
  father: Father = new Father();

  build() {
    Column() {
      Text(`${this.father.son.age}`)
      // 点击后age值加1，由于@Trace装饰器，UI会自动刷新
        .onClick(() => {
          this.father.son.age++;
        })
    }
  }
}
```
