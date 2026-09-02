---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-parameter
title: 自定义组件参数
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 自定义组件 > 自定义组件参数
category: harmonyos-references
scraped_at: 2026-09-02T15:01:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5304e54756d36be6d8982941df88e7df0104ae4eec08dd5b42356be2d146945c
---

**说明** 

* 本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## ComponentOptions

自定义组件参数，用于配置是否支持组件冻结和全局复用池，适用于需要优化自定义组件性能表现和提升组件复用效率的场景。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| freezeWhenInactive | boolean | 否 | 否 | 配置自定义组件支持组件冻结。true：开启组件冻结，false：不开启组件冻结。当开发者未指定ComponentOptions时，freezeWhenInactive将使用false作为默认值。  从API version 11开始，支持通过此参数配置[@Component](../harmonyos-guides/arkts-create-custom-components.md#component)组件冻结。示例可见[自定义组件冻结](../harmonyos-guides/arkts-custom-components-freeze.md)。  从API version 12开始，支持通过此参数配置[@ComponentV2](../harmonyos-guides/arkts-create-custom-components.md#componentv2)组件冻结。示例可见[自定义组件冻结](../harmonyos-guides/arkts-custom-components-freezev2.md)。  **卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| reusePool | [ReusePoolOwnership](ts-custom-component-parameter.md#reusepoolownership) | 否 | 是 | 在自定义组件上配置全局复用池的类型，适用于应用中存在多个同类型可复用自定义组件、需要在组件实例间共享或隔离复用资源以提升复用效率的场景。如果不传入，则全局复用池不会生效。reusePool需与poolAccepts配合使用，reusePool参数被设置时，poolAccepts必须为非空数组，否则全局复用不生效。  **起始版本：** 26.0.0  **卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。 |
| poolAccepts | Function[] | 否 | 是 | 指定全局复用池可以接纳（即允许被复用）的自定义组件名称列表。当reusePool参数被设置时，系统会根据poolAccepts中列出的组件名称，将匹配的可复用组件缓存到该全局复用池中供后续复用。reusePool参数被设置时，poolAccepts必须为非空数组，单独设置poolAccepts不会使全局复用生效。当poolAccepts和reusePool都没有赋值时，全局复用不生效。  **起始版本：** 26.0.0  **卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。 |

## ReusableOptions

可复用自定义组件的参数，用于配置内存优化策略，适用于需要降低可复用自定义组件内存使用量的场景。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| memoryOptimizationStrategy | [ReusableMemOptStrategy](ts-custom-component-parameter.md#reusablememoptstrategy) | 否 | 是 | 可复用自定义组件的内存优化策略。该参数在创建可复用自定义组件时设定，不支持动态修改。传入[ENABLE\_AUTO\_CACHE\_OPTIMIZATION](ts-custom-component-parameter.md#reusablememoptstrategy)时可启用自动内存优化，在应用退后台、组件不可见或整机低内存等场景下自动释放复用池中的组件；不传入时使用默认值[DEFAULT](ts-custom-component-parameter.md#reusablememoptstrategy)（无内存优化策略）。 |

## ReusableMemOptStrategy

可复用自定义组件内存优化策略枚举。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 无内存优化策略。 |
| ENABLE\_AUTO\_CACHE\_OPTIMIZATION | 1 << 0 | 自动内存优化策略。建议在需要降低可复用自定义组件内存使用量的场景下使用此策略。  满足以下任一条件时，释放复用池内的所有该类型自定义组件：  - 应用退后台时。  - 复用池所在组件不可见时（[visibility](ts-universal-attributes-visibility.md#visibility)属性设置为[Visible](ts-appendix-enums.md#visibility)以外的值，或组件面积为0，不考虑遮挡）。  - 整机低内存时（[MemoryLevel](js-apis-app-ability-abilityconstant.md#memorylevel)达到MEMORY\_LEVEL\_LOW或MEMORY\_LEVEL\_CRITICAL）。  当复用池中相同ReuseId的该类型自定义组件数量超过复用池容量限额，且5秒钟内不再增加时，保留限额内的组件，释放其余组件。复用池容量限额设定如下：  - 设备内存大于8G时，限额为48。  - 设备内存大于6G且小于等于8G时，限额为4。  - 设备内存小于等于6G时，限额为2。  在释放节点时，会触发[自定义组件生命周期](../harmonyos-guides/arkts-page-custom-components-lifecycle.md)。 |

## 示例

### 示例1（使用自动内存优化策略）

以下示例中，可复用自定义组件ReusableComponent通过[ReusableOptions](ts-custom-component-parameter.md#reusableoptions)的memoryOptimizationStrategy属性使用了自动内存优化策略。点击Recycle按钮，可触发ReusableComponent组件回收。之后应用退后台，可触发复用池缓存释放。

从API版本26.0.0开始，新增ReusableOptions接口。

```ts
@Reusable({ memoryOptimizationStrategy: ReusableMemOptStrategy.ENABLE_AUTO_CACHE_OPTIMIZATION }) // 使用自动内存优化策略
@Component
struct ReusableComponent {
  aboutToRecycle() {
    console.info('ReusableComponent aboutToRecycle');
  }
  aboutToDisappear() {
    console.info('ReusableComponent aboutToDisappear');
  }
  build() {
    Text('ReusableComponent')
  }
}

@Entry
@Component
struct MemoryOptimizeDemo {
  @State showReusableComponent: boolean = true;
  build() {
    Column() {
      Button('Recycle').onClick(() => { // 点击按钮触发组件回收
        this.showReusableComponent = false;
      })
      if (this.showReusableComponent) {
        ReusableComponent()
      }
    }
  }
}
```

## ReusePoolOwnership

type ReusePoolOwnership = 'shared' | 'perInstance'

全局复用池的持有类型。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| 'shared' | @Component/@ComponentV2类的所有实例共享同一个复用池实例。适用于多个同类型组件实例间需要复用相同资源的场景，可最大化复用池利用率，减少内存占用。 |
| 'perInstance' | @Component/@ComponentV2的每个实例拥有独立的复用池实例。适用于需要隔离各组件实例复用资源的场景，避免不同实例间的复用资源相互影响。 |
