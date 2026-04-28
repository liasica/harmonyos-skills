---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-env-system-property
title: @Env：环境变量
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 响应式环境变量 > @Env：环境变量
category: harmonyos-references
scraped_at: 2026-04-28T08:02:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:51a6cb9adca501e50777230a956ed0c2c5db0f8946e58a6bef1a56a63b694f40
---

说明

本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

开发者指南见：[@Env开发者指南](../harmonyos-guides/arkts-env-system-property.md)。

## @Env

PhonePC/2in1TabletTVWearable

Env: EnvDecorator

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| Env | [EnvDecorator](ts-env-system-property.md#envdecorator) | 环境变量装饰器。 |

**示例：**

```
1. import { uiObserver } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. @Env(SystemProperties.BREAK_POINT) breakpoint: uiObserver.WindowSizeLayoutBreakpointInfo;

8. build() {}
9. }
```

## EnvDecorator

PhonePC/2in1TabletTVWearable

type EnvDecorator = (value: SystemProperties) => PropertyDecorator

定义@Env装饰器类型。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SystemProperties](ts-env-system-property.md#systemproperties) | 是 | 环境变量属性名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| PropertyDecorator | 属性装饰器。 |

**错误码：**

详细介绍请参见[环境变量错误码](errorcode-env.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 140000 | Invalid key for @Env |

## SystemProperties

PhonePC/2in1TabletTVWearable

定义环境变量枚举值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BREAK\_POINT | 'system.arkui.breakpoint' | [@Env](ts-env-system-property.md#env)变量参数，通过@Env(SystemProperties.BREAK\_POINT)可获取[WindowSizeLayoutBreakpointInfo](js-apis-arkui-observer.md#windowsizelayoutbreakpointinfo22)实例。  当该装饰器声明在[@Component](../harmonyos-guides/arkts-create-custom-components.md#component)或[@ComponentV2](../harmonyos-guides/arkts-create-custom-components.md#componentv2)中时，用于获取当前自定义组件所在窗口的尺寸布局断点信息。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| WINDOW\_SIZE23+ | 'system.window.size' | [@Env](ts-env-system-property.md#env)变量参数，通过@Env(SystemProperties.WINDOW\_SIZE)可获取[SizeInVP](arkts-apis-window-i.md#sizeinvp23)实例。  当该装饰器声明在[@Component](../harmonyos-guides/arkts-create-custom-components.md#component)或[@ComponentV2](../harmonyos-guides/arkts-create-custom-components.md#componentv2)中时，用于获取当前自定义组件所在窗口的大小信息，单位为vp。  **模型约束**：此接口仅可在Stage模型下使用。 |
| WINDOW\_SIZE\_PX23+ | 'system.window.size.px' | [@Env](ts-env-system-property.md#env)变量参数，通过@Env(SystemProperties.WINDOW\_SIZE\_PX)可获取[Size](arkts-apis-window-i.md#size7)实例。  当该装饰器声明在[@Component](../harmonyos-guides/arkts-create-custom-components.md#component)或[@ComponentV2](../harmonyos-guides/arkts-create-custom-components.md#componentv2)中时，用于获取当前自定义组件所在窗口的大小信息，单位为px。  **模型约束**：此接口仅可在Stage模型下使用。 |
| WINDOW\_AVOID\_AREA23+ | 'system.window.avoidarea' | [@Env](ts-env-system-property.md#env)变量参数，通过@Env(SystemProperties.WINDOW\_AVOID\_AREA)可获取[UIEnvWindowAvoidAreaInfoVP](arkts-apis-window-i.md#uienvwindowavoidareainfovp23)实例。  当该装饰器声明在[@Component](../harmonyos-guides/arkts-create-custom-components.md#component)或[@ComponentV2](../harmonyos-guides/arkts-create-custom-components.md#componentv2)中时，用于获取当前自定义组件所在窗口的避让区域信息，单位为vp。  **模型约束**：此接口仅可在Stage模型下使用。 |
| WINDOW\_AVOID\_AREA\_PX23+ | 'system.window.avoidarea.px' | [@Env](ts-env-system-property.md#env)变量参数，通过@Env(SystemProperties.WINDOW\_AVOID\_AREA\_PX)可获取[UIEnvWindowAvoidAreaInfoPX](arkts-apis-window-i.md#uienvwindowavoidareainfopx23)实例。  当该装饰器声明在[@Component](../harmonyos-guides/arkts-create-custom-components.md#component)或[@ComponentV2](../harmonyos-guides/arkts-create-custom-components.md#componentv2)中时，用于获取当前自定义组件所在窗口的避让区域信息，单位为px。  **模型约束**：此接口仅可在Stage模型下使用。 |
