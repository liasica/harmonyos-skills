---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-decorator-componentv2
title: "@ComponentV2：自定义组件V2"
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 自定义组件 > 自定义组件装饰器 > @ComponentV2：自定义组件V2
category: harmonyos-references
scraped_at: 2026-09-02T15:01:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7b5071bebf533f84e7f3e043efbea3201102a970b7a8d6b0423046a9744cd3e2
---

@ComponentV2主要配合状态管理V2使用，相比[@Component](../harmonyos-guides/arkts-create-custom-components.md#component)，@ComponentV2支持对象的深度观测和深度监听，装饰器易用性高、拓展性强，适用于需要深度观测嵌套对象状态的场景。除非特别说明，@ComponentV2装饰的自定义组件将与@Component装饰的自定义组件保持相同的行为。

开发指南参考：[@ComponentV2](../harmonyos-guides/arkts-create-custom-components.md#componentv2)。

**说明** 

* 本装饰器首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 从API版本26.0.0开始，@ComponentV2的[ComponentOptions](ts-custom-component-parameter.md#componentoptions)参数支持可选属性reusePool和poolAccepts，用于配置全局复用池，开发指南参考：[全局复用：集中化的组件回收与复用](../harmonyos-guides/arkts-global-reuse-pool.md)。

## @ComponentV2

const ComponentV2: ClassDecorator & ((options: ComponentOptions) => ClassDecorator)

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ComponentOptions](ts-custom-component-parameter.md#componentoptions) | 否 | @ComponentV2装饰器选项。当需要开启组件冻结或全局复用功能时传入此参数进行自定义配置；缺省时关闭组件冻结和全局复用功能。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ClassDecorator | 类装饰器，开发者无需关注该返回值。 |

**示例：**

```ts
@Entry
@ComponentV2({ freezeWhenInactive: true }) // 开启组件冻结功能
struct MyComponent {
  build() {
    Column() {
      Text('Hello World!')
    }
  }
}
```
