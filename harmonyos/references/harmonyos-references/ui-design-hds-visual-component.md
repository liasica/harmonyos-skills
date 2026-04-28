---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hds-visual-component
title: HdsVisualComponent
breadcrumb: API参考 > 应用框架 > UI Design Kit（UI设计套件） > ArkTS组件 > HdsVisualComponent
category: harmonyos-references
scraped_at: 2026-04-28T08:06:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b5e8a1aa0210a99ccef652b8c35a2bdfe1323f1e38ea0f52c5eeac245ee1659f
---

HdsVisualComponent组件承载复杂视效实现，应用开发者通过HdsVisualComponent选择具体视效场景完成复杂视效的开发。

**起始版本：** 6.0.0(20)

## 导入模块

PhonePC/2in1TabletTV

说明

* HdsVisualComponentAttribute是用于配置HdsVisualComponent组件属性的关键接口。6.0.1(21)及之前版本，导入HdsVisualComponent组件后需要开发者手动导入HdsVisualComponentAttribute，否则会编译报错。从6.0.2(22)版本开始，编译工具链识别到导入HdsVisualComponent组件后，会自动导入HdsVisualComponentAttribute，无需开发者手动导入。
* 如果开发者手动导入HdsVisualComponentAttribute，DevEco Studio会显示置灰，6.0.1(21)及之前版本删除会编译报错，从6.0.2(22)版本开始，删除对功能无影响。

6.0.1(21)及之前版本：

```
1. import { HdsVisualComponent, HdsVisualComponentAttribute, HdsSceneController, HdsSceneType, hdsEffect } from '@kit.UIDesignKit';
```

6.0.2(22)及之后版本：

```
1. import { HdsVisualComponent, HdsSceneController, HdsSceneType, hdsEffect } from '@kit.UIDesignKit';
```

## 子组件

PhonePC/2in1TabletTV

无

## 接口

PhonePC/2in1TabletTV

HdsVisualComponent()

创建HdsVisualComponent通用视效组件。

**模型约束：** 此接口仅可在Stage模型下使用。

**卡片能力：** 从6.0.2(22)开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

## 属性

PhonePC/2in1TabletTV

除支持[通用属性](ts-component-general-attributes.md)，还支持以下属性：

### scene

PhonePC/2in1TabletTV

scene(sceneType: HdsSceneType, controller: HdsSceneController, callback?: HdsSceneFinishCallback, frameRateRange?: hdsEffect.ExpectedFrameRateRange)

设置视效场景

**模型约束：** 此接口仅可在Stage模型下使用。

**卡片能力：** 从6.0.2(22)开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sceneType | [HdsSceneType](ui-design-hds-visual-component.md#hdsscenetype) | 是 | 视效场景类型。 |
| controller | [HdsSceneController](ui-design-hds-visual-component.md#hdsscenecontroller) | 是 | 视效场景控制器。 |
| callback | [HdsSceneFinishCallback](ui-design-hds-visual-component.md#hdsscenefinishcallback) | 否 | 视效场景结束回调。 |
| frameRateRange | hdsEffect.[ExpectedFrameRateRange](ui-design-hdseffect.md#expectedframeraterange) | 否 | 视效场景帧率配置。 |

## 事件

PhonePC/2in1TabletTV

支持[通用事件](ts-component-general-events.md)。

## HdsSceneType

PhonePC/2in1TabletTV

视效场景。

**模型约束：** 此接口仅可在Stage模型下使用。

**卡片能力：** 从6.0.2(22)开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

| 名称 | 值 | **说明** |
| --- | --- | --- |
| DUAL\_EDGE\_FLOW\_LIGHT\_WITH\_BACKGROUND\_MASK | 0 | 自带背景的双边流光。  **说明**：该场景在TV中无效果，在其他设备类型中可正常显示。 |

## HdsSceneFinishCallback

PhonePC/2in1TabletTV

type HdsSceneFinishCallback = () => void

场景视效结束回调函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**卡片能力：** 从6.0.2(22)开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

## HdsSceneController

PhonePC/2in1TabletTV

场景控制器。

**模型约束：** 此接口仅可在Stage模型下使用。

**卡片能力：** 从6.0.2(22)开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

### constructor

PhonePC/2in1TabletTV

constructor()

HdsSceneController的构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**卡片能力：** 从6.0.2(22)开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

### start

PhonePC/2in1TabletTV

start(): void

开始视效场景。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

### pause

PhonePC/2in1TabletTV

pause(): void

暂停视效场景。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

### resume

PhonePC/2in1TabletTV

resume(): void

恢复视效场景。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

### stop

PhonePC/2in1TabletTV

stop(): void

停止视效场景。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

### setSceneParams

PhonePC/2in1TabletTV

setSceneParams(params: SceneParams): HdsSceneController

设置场景参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [SceneParams](ui-design-hds-visual-component.md#sceneparams) | 是 | 场景参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HdsSceneController](ui-design-hds-visual-component.md#hdsscenecontroller) | 返回[HdsSceneController](ui-design-hds-visual-component.md#hdsscenecontroller)对象。 |

## SceneParams

PhonePC/2in1TabletTV

type SceneParams = DualEdgeFlowLightWithMaskParam

场景视效参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

| 类型 | 说明 |
| --- | --- |
| [DualEdgeFlowLightWithMaskParam](ui-design-hds-visual-component.md#dualedgeflowlightwithmaskparam) | 双边边缘流光视效参数。 |

## DualEdgeFlowLightWithMaskParam

PhonePC/2in1TabletTV

双边边缘流光视效参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| backgroundMaskColors | Array<[ResourceColor](ts-types.md#resourcecolor)> | 否 | 否 | 背景蒙层颜色数组。 |
| firstEdgeFlowLight | hdsEffect.[EdgeFlowLightParam](ui-design-hdseffect.md#edgeflowlightparam) | 否 | 否 | 第一条流光参数配置。 |
| secondEdgeFlowLight | hdsEffect.[EdgeFlowLightParam](ui-design-hdseffect.md#edgeflowlightparam) | 否 | 否 | 第二条流光参数配置。 |

## 示例

PhonePC/2in1TabletTV

```
1. // 从6.0.2(22)版本开始，无需手动导入HdsVisualComponentAttribute。具体请参考HdsVisualComponent的导入模块说明。
2. import { HdsVisualComponent, HdsVisualComponentAttribute, HdsSceneController, HdsSceneType } from '@kit.UIDesignKit';

4. @Entry
5. @Component
6. struct EdgeFlowLightVisualComponent {
7. @State sceneController: HdsSceneController = new HdsSceneController()
8. .setSceneParams({
9. backgroundMaskColors: [Color.Green, Color.Red],
10. firstEdgeFlowLight: {
11. startPos: 0,
12. endPos: 0.5,
13. color: Color.Red
14. },
15. secondEdgeFlowLight: {
16. startPos: 0,
17. endPos: -0.5,
18. color: Color.Green
19. }
20. })

22. build() {
23. Stack() {
24. HdsVisualComponent()
25. .scene(HdsSceneType.DUAL_EDGE_FLOW_LIGHT_WITH_BACKGROUND_MASK, this.sceneController, () => {
26. console.info('Succeeded in finishing');
27. })
28. .width('100%')
29. .height('50%')
30. }
31. }
32. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/bLQJUMaWR1GTTEBf9ena_w/zh-cn_image_0000002583440577.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000642Z&HW-CC-Expire=86400&HW-CC-Sign=31161CA2A2D1852BCAC572BF3703D8FAA206283ABB04C0FC0BC8B21694AE4DAE)
