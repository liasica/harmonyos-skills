---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-env-system-property
title: "@Env：环境变量"
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 响应式环境变量 > @Env：环境变量
category: harmonyos-references
scraped_at: 2026-09-02T15:01:10+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d4ce148f682c22720f8da7310aa53d94d668b747194250d71809f6809b5ce853
---

@Env装饰器用于获取系统环境变量，帮助开发者感知系统环境变化并动态调整UI显示。

**说明** 

本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

开发者指南见：[@Env开发者指南](../harmonyos-guides/arkts-env-system-property.md)。

## @Env

Env<T>(key: SystemEnvKey<T> | SystemProperties): PropertyDecorator

用于获取系统环境变量。API版本26.0.0之前仅支持传入SystemProperties枚举，API版本26.0.0及以后版本支持传入[SystemEnvKey<T>](ts-env-system-property.md#systemenvkeyt)类或[SystemProperties](ts-env-system-property.md#systemproperties)枚举作为参数。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | SystemEnvKey<T> | SystemProperties | 是 | 环境变量key。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| PropertyDecorator | 属性装饰器，开发者无需关注该返回值。 |

**示例：**

```ts
import { uiObserver } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  // @Env读取系统环境变量
  @Env(SystemProperties.BREAK_POINT) breakpoint: uiObserver.WindowSizeLayoutBreakpointInfo;

  build() {
    Column() {
        Text(`breakpoint height ${this.breakpoint.heightBreakpoint}`)
        Text(`breakpoint width ${this.breakpoint.widthBreakpoint}`)
    }
  }
}
```

## EnvDecorator

type EnvDecorator = (value: SystemProperties) => PropertyDecorator

定义EnvDecorator属性装饰器类型。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SystemProperties](ts-env-system-property.md#systemproperties) | 是 | 环境变量属性名，用于指定要获取的系统环境变量。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| PropertyDecorator | 属性装饰器，开发者无需关注该返回值。 |

**错误码：**

详细介绍请参见[环境变量错误码](errorcode-env.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 140000 | Invalid key for @Env |

## SystemProperties

定义环境变量枚举值，用于通过[@Env](ts-env-system-property.md#env)装饰器获取系统环境变量。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BREAK\_POINT | 'system.arkui.breakpoint' | [@Env](ts-env-system-property.md#env)变量参数，通过@Env(SystemProperties.BREAK\_POINT)可获取[WindowSizeLayoutBreakpointInfo](js-apis-arkui-observer.md#windowsizelayoutbreakpointinfo22)实例。  当该装饰器声明在[@Component](../harmonyos-guides/arkts-create-custom-components.md#component)或[@ComponentV2](../harmonyos-guides/arkts-create-custom-components.md#componentv2)中时，用于获取当前自定义组件所在窗口的尺寸布局断点信息。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。  **模型约束**：此接口仅可在Stage模型下使用。 |
| WINDOW\_SIZE23+ | 'system.window.size' | [@Env](ts-env-system-property.md#env)变量参数，通过@Env(SystemProperties.WINDOW\_SIZE)可获取[SizeInVP](arkts-apis-window-i.md#sizeinvp23)实例。  当该装饰器声明在[@Component](../harmonyos-guides/arkts-create-custom-components.md#component)或[@ComponentV2](../harmonyos-guides/arkts-create-custom-components.md#componentv2)中时，用于获取当前自定义组件所在窗口的大小信息，单位为vp。  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。  **模型约束**：此接口仅可在Stage模型下使用。 |
| WINDOW\_SIZE\_PX23+ | 'system.window.size.px' | [@Env](ts-env-system-property.md#env)变量参数，通过@Env(SystemProperties.WINDOW\_SIZE\_PX)可获取[Size](arkts-apis-window-i.md#size7)实例。  当该装饰器声明在[@Component](../harmonyos-guides/arkts-create-custom-components.md#component)或[@ComponentV2](../harmonyos-guides/arkts-create-custom-components.md#componentv2)中时，用于获取当前自定义组件所在窗口的大小信息，单位为px。  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。  **模型约束**：此接口仅可在Stage模型下使用。 |
| WINDOW\_AVOID\_AREA23+ | 'system.window.avoidarea' | [@Env](ts-env-system-property.md#env)变量参数，通过@Env(SystemProperties.WINDOW\_AVOID\_AREA)可获取[UIEnvWindowAvoidAreaInfoVP](arkts-apis-window-i.md#uienvwindowavoidareainfovp23)实例。  当该装饰器声明在[@Component](../harmonyos-guides/arkts-create-custom-components.md#component)或[@ComponentV2](../harmonyos-guides/arkts-create-custom-components.md#componentv2)中时，用于获取当前自定义组件所在窗口的避让区域信息，单位为vp。  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。  **模型约束**：此接口仅可在Stage模型下使用。 |
| WINDOW\_AVOID\_AREA\_PX23+ | 'system.window.avoidarea.px' | [@Env](ts-env-system-property.md#env)变量参数，通过@Env(SystemProperties.WINDOW\_AVOID\_AREA\_PX)可获取[UIEnvWindowAvoidAreaInfoPX](arkts-apis-window-i.md#uienvwindowavoidareainfopx23)实例。  当该装饰器声明在[@Component](../harmonyos-guides/arkts-create-custom-components.md#component)或[@ComponentV2](../harmonyos-guides/arkts-create-custom-components.md#componentv2)中时，用于获取当前自定义组件所在窗口的避让区域信息，单位为px。  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。  **模型约束**：此接口仅可在Stage模型下使用。 |

## SystemEnvKey<T>

系统环境变量Key对应的类型。

### 属性

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | T | 否 | 是 | 系统环境变量Key对应值的数据类型，默认值为undefined。 |

### constructor

protected constructor()

用于创建该类的实例对象。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## WritableSystemEnvKey<T>

定义可写的系统环境变量Key，继承自[SystemEnvKey<T>](ts-env-system-property.md#systemenvkeyt)。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## ReadonlySystemEnvKey<T>

定义只读的系统环境变量Key，继承自[SystemEnvKey<T>](ts-env-system-property.md#systemenvkeyt)。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## WritableEnvKey

定义可写的系统环境变量Key集合，用于通过@Env装饰器获取对应的系统环境变量。可通过[WithEnv](ts-container-with-env.md)中的[env](ts-container-with-env.md#env)方法设置局部环境变量值以影响后代组件渲染，具体示例请参见[示例2（设置局部布局方向）](ts-container-with-env.md#示例2设置局部布局方向)。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| DIRECTION | [WritableSystemEnvKey](ts-env-system-property.md#writablesystemenvkeyt)<Direction> | 是 | 否 | [@Env](ts-env-system-property.md#env)变量参数，通过@Env(WritableEnvKey.DIRECTION)可获取[Direction](ts-appendix-enums.md#direction)枚举类型的值。  当该装饰器声明在[@Component](../harmonyos-guides/arkts-create-custom-components.md#component)或[@ComponentV2](../harmonyos-guides/arkts-create-custom-components.md#componentv2)中时，用于获取窗口所在屏幕的布局方向。 |
| FONT\_SCALE | [WritableSystemEnvKey](ts-env-system-property.md#writablesystemenvkeyt)<number> | 是 | 否 | [@Env](ts-env-system-property.md#env)变量参数，通过@Env(WritableEnvKey.FONT\_SCALE)可获取number类型的值，取值无上限，小于等于0的值按0处理。  当该装饰器声明在[@Component](../harmonyos-guides/arkts-create-custom-components.md#component)或[@ComponentV2](../harmonyos-guides/arkts-create-custom-components.md#componentv2)中时，用于为后代组件提供局部字体缩放倍数。 |

## ReadonlyEnvKey

定义只读的系统环境变量key集合，用于通过@Env装饰器获取对应的系统环境变量。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| WINDOW\_AVOID\_AREA | [ReadonlySystemEnvKey](ts-env-system-property.md#readonlysystemenvkeyt)<window.UIEnvWindowAvoidAreaInfoVP> | 是 | 否 | [@Env](ts-env-system-property.md#env)变量参数，通过@Env(ReadonlyEnvKey.WINDOW\_AVOID\_AREA)可获取[UIEnvWindowAvoidAreaInfoVP](arkts-apis-window-i.md#uienvwindowavoidareainfovp23)实例。  当该装饰器声明在[@Component](../harmonyos-guides/arkts-create-custom-components.md#component)或[@ComponentV2](../harmonyos-guides/arkts-create-custom-components.md#componentv2)中时，用于获取当前自定义组件所在窗口的避让区域信息，单位为vp。  **起始版本：** 26.0.0  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。  **模型约束：** 此接口仅可在Stage模型下使用。 |
| WINDOW\_AVOID\_AREA\_PX | [ReadonlySystemEnvKey](ts-env-system-property.md#readonlysystemenvkeyt)<window.UIEnvWindowAvoidAreaInfoPX> | 是 | 否 | [@Env](ts-env-system-property.md#env)变量参数，通过@Env(ReadonlyEnvKey.WINDOW\_AVOID\_AREA\_PX)可获取[UIEnvWindowAvoidAreaInfoPX](arkts-apis-window-i.md#uienvwindowavoidareainfopx23)实例。  当该装饰器声明在[@Component](../harmonyos-guides/arkts-create-custom-components.md#component)或[@ComponentV2](../harmonyos-guides/arkts-create-custom-components.md#componentv2)中时，用于获取当前自定义组件所在窗口的避让区域信息，单位为px。  **起始版本：** 26.0.0  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。  **模型约束：** 此接口仅可在Stage模型下使用。 |
| WINDOW\_SIZE | [ReadonlySystemEnvKey](ts-env-system-property.md#readonlysystemenvkeyt)<window.SizeInVP> | 是 | 否 | [@Env](ts-env-system-property.md#env)变量参数，通过@Env(ReadonlyEnvKey.WINDOW\_SIZE)可获取[SizeInVP](arkts-apis-window-i.md#sizeinvp23)实例。  当该装饰器声明在[@Component](../harmonyos-guides/arkts-create-custom-components.md#component)或[@ComponentV2](../harmonyos-guides/arkts-create-custom-components.md#componentv2)中时，用于获取当前自定义组件所在窗口的大小信息，单位为vp。  **起始版本：** 26.0.0  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。  **模型约束：** 此接口仅可在Stage模型下使用。 |
| WINDOW\_SIZE\_PX | [ReadonlySystemEnvKey](ts-env-system-property.md#readonlysystemenvkeyt)<window.Size> | 是 | 否 | [@Env](ts-env-system-property.md#env)变量参数，通过@Env(ReadonlyEnvKey.WINDOW\_SIZE\_PX)可获取[Size](arkts-apis-window-i.md#size7)实例。  当该装饰器声明在[@Component](../harmonyos-guides/arkts-create-custom-components.md#component)或[@ComponentV2](../harmonyos-guides/arkts-create-custom-components.md#componentv2)中时，用于获取当前自定义组件所在窗口的大小信息，单位为px。  **起始版本：** 26.0.0  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。  **模型约束：** 此接口仅可在Stage模型下使用。 |
| WINDOW\_DISPLAY\_ID | [ReadonlySystemEnvKey](ts-env-system-property.md#readonlysystemenvkeyt)<number> | 是 | 否 | [@Env](ts-env-system-property.md#env)变量参数，通过@Env(ReadonlyEnvKey.WINDOW\_DISPLAY\_ID)可获取number类型的值。  当该装饰器声明在[@Component](../harmonyos-guides/arkts-create-custom-components.md#component)或[@ComponentV2](../harmonyos-guides/arkts-create-custom-components.md#componentv2)中时，用于获取当前自定义组件所在窗口的屏幕ID。  **起始版本：** 26.0.0  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。  **模型约束：** 此接口仅可在Stage模型下使用。 |
| WINDOW\_SYSTEM\_DENSITY | [ReadonlySystemEnvKey](ts-env-system-property.md#readonlysystemenvkeyt)<number> | 是 | 否 | [@Env](ts-env-system-property.md#env)变量参数，通过@Env(ReadonlyEnvKey.WINDOW\_SYSTEM\_DENSITY)可获取number类型的值。  当该装饰器声明在[@Component](../harmonyos-guides/arkts-create-custom-components.md#component)或[@ComponentV2](../harmonyos-guides/arkts-create-custom-components.md#componentv2)中时，用于获取当前自定义组件所在窗口的系统显示大小缩放系数。该参数为浮点数，取值范围为[0.5, 4.0]或-1.0。4.0表示窗口可显示的最大显示大小缩放系数，-1.0表示窗口使用系统显示大小缩放系数。  **起始版本：** 26.0.0  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。  **模型约束：** 此接口仅可在Stage模型下使用。 |
| WINDOW\_IS\_FOCUSED | [ReadonlySystemEnvKey](ts-env-system-property.md#readonlysystemenvkeyt)<boolean> | 是 | 否 | [@Env](ts-env-system-property.md#env)变量参数，通过@Env(ReadonlyEnvKey.WINDOW\_IS\_FOCUSED)可获取boolean类型的值。  当该装饰器声明在[@Component](../harmonyos-guides/arkts-create-custom-components.md#component)或[@ComponentV2](../harmonyos-guides/arkts-create-custom-components.md#componentv2)中时，用于获取当前自定义组件所在窗口是否处于获焦状态，true表示当前处于获焦状态，false表示当前不处于获焦状态。  **起始版本：** 26.0.0  **模型约束：** 此接口仅可在Stage模型下使用。 |
| WINDOW\_IS\_HIGHLIGHTED | [ReadonlySystemEnvKey](ts-env-system-property.md#readonlysystemenvkeyt)<boolean> | 是 | 否 | [@Env](ts-env-system-property.md#env)变量参数，通过@Env(ReadonlyEnvKey.WINDOW\_IS\_HIGHLIGHTED)可获取boolean类型的值。  当该装饰器声明在[@Component](../harmonyos-guides/arkts-create-custom-components.md#component)或[@ComponentV2](../harmonyos-guides/arkts-create-custom-components.md#componentv2)中时，用于获取当前自定义组件所在窗口是否处于高亮状态，true表示当前处于高亮状态，false表示当前不处于高亮状态。  **起始版本：** 26.0.0  **模型约束：** 此接口仅可在Stage模型下使用。 |
