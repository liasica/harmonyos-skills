---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsmaterial
title: hdsMaterial
breadcrumb: API参考 > 应用框架 > UI Design Kit（UI设计套件） > ArkTS API > hdsMaterial
category: harmonyos-references
scraped_at: 2026-04-28T08:06:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:91b63b9dcaf44f19532a504157f637a0b48d2bcf752964c18b542f12c676ee37
---

本模块提供材质效果能力，支持通过配置材质类型、等级等参数，实现多样化的材质表现。

**起始版本：** 6.1.0(23)

## 导入模块

PhonePC/2in1TabletTV

```
1. import { hdsMaterial } from '@kit.UIDesignKit';
```

## getSystemMaterialTypes

PhonePC/2in1TabletTV

getSystemMaterialTypes(): Array<MaterialType>

获取设备支持的所有材质类型。

**卡片能力：** 从6.1.0(23)开始，该接口支持在ArkTS卡片中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.1.0(23)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Array<[MaterialType](ui-design-hdsmaterial.md#materialtype)> | 设备支持的材质类型。 |

**示例：**

```
1. import { hdsMaterial } from '@kit.UIDesignKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let materialTypes: Array<hdsMaterial.MaterialType> = hdsMaterial.getSystemMaterialTypes();
6. } catch (err) {
7. let message = (err as BusinessError).message;
8. let code = (err as BusinessError).code;
9. console.error(`getSystemMaterialTypes failed, code: ${code}, message: ${message}`);
10. }
```

## MaterialType

PhonePC/2in1TabletTV

材质类型枚举。

**卡片能力：** 从6.1.0(23)开始，该接口支持在ArkTS卡片中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.1.0(23)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 无材质效果。 |
| ADAPTIVE | 100 | 自适应系统材质。默认为沉浸式材质。 |
| IMMERSIVE | 101 | 沉浸式材质（新材质）。 |

## MaterialLevel

PhonePC/2in1TabletTV

材质等级枚举。各等级效果承载在支持配置材质属性的组件上，其中精美等级材质需要耗费的性能更多，流畅等级材质需要耗费的性能较少。

**卡片能力：** 从6.1.0(23)开始，该接口支持在ArkTS卡片中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.1.0(23)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EXQUISITE | 0 | 精美。 |
| GENTLE | 1 | 轻柔。 |
| SMOOTH | 2 | 流畅。 |
| ADAPTIVE | 10 | 材质生效策略由系统策略决定，系统根据设备性能自适应材质等级。 |

说明

* **推荐使用默认值ADAPTIVE档位：** 该模式下，系统会根据当前设备的算力动态调整组件的材质效果，实现性能与显示效果的最佳平衡体验。
* **若未采用系统自适应能力。** 请先调用[getSystemMaterialTypes()](ui-design-hdsmaterial.md#getsystemmaterialtypes)接口查询当前设备支持的材质能力，再根据查询结果选用相应的材质效果枚举：
  + 如果查询结果显示当前设备支持IMMERSIVE材质类型，可选用EXQUISITE或GENTLE效果。
  + 如果查询结果显示当前设备不支持IMMERSIVE材质类型，则建议使用SMOOTH效果，以降低卡顿和发热风险，保障用户体验。
* **详细使用指导：** 请参见[HDS组件使用沉浸光感材质指南](../harmonyos-guides/ui-design-hds-component-material.md)。
