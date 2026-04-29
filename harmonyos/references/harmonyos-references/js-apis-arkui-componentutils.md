---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-componentutils
title: @ohos.arkui.componentUtils (componentUtils)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.componentUtils (componentUtils)
category: harmonyos-references
scraped_at: 2026-04-29T13:50:29+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:a962f1a6d29d4735690403f9f8502920a13a5d3b79e60125bb5a73136aec4016
---

提供获取组件绘制区域坐标和大小的能力。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块功能依赖UI的执行上下文，不可在[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的地方使用，参见[UIContext](arkts-apis-uicontext-uicontext.md)说明。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { componentUtils } from '@kit.ArkUI';
```

## componentUtils.getRectangleById(deprecated)

PhonePC/2in1TabletTVWearable

getRectangleById(id: string): ComponentInfo

根据组件ID获取组件实例对象，通过组件实例对象将获取的坐标位置和大小同步返回给开发者。

说明

* 从API version 10开始支持，从API version 18开始废弃，建议使用[getRectangleById](arkts-apis-uicontext-componentutils.md#getrectanglebyid)替代。getRectangleById需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getComponentUtils](arkts-apis-uicontext-uicontext.md#getcomponentutils)方法获取[ComponentUtils](arkts-apis-uicontext-componentutils.md)对象，然后通过该对象进行调用。
* 从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getComponentUtils](arkts-apis-uicontext-uicontext.md#getcomponentutils)方法获取当前UI上下文关联的[ComponentUtils](arkts-apis-uicontext-componentutils.md)对象。在目标组件布局完成后，通过该接口能够获取组件坐标和尺寸信息。建议在[布局回调](js-apis-arkui-inspector.md)中使用该接口。如果组件动态创建但未挂载组件树，则无法通过该接口获取正常的组件信息。因为组件在未挂载组件树的情况下，一般未经过UI框架正常的测量与布局，此时请确保组件正常挂载组件树后再尝试获取组件信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 指定组件id。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ComponentInfo](js-apis-arkui-componentutils.md#componentinfo) | 组件大小、位置、平移缩放旋转及仿射矩阵属性信息。 |

**错误码：**

以下错误码的详细介绍请参见[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100001 | UI execution context not found. |

**示例：**

```
1. import { componentUtils } from '@kit.ArkUI';
2. let modePosition:componentUtils.ComponentInfo = componentUtils.getRectangleById("onClick");
```

## ComponentInfo

PhonePC/2in1TabletTVWearable

组件大小、位置、平移缩放旋转及仿射矩阵属性信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| size | [Size](js-apis-arkui-componentutils.md#size) | 否 | 否 | 组件大小。 |
| localOffset | [Offset](js-apis-arkui-componentutils.md#offset) | 否 | 否 | 组件相对于父组件信息。 |
| windowOffset | [Offset](js-apis-arkui-componentutils.md#offset) | 否 | 否 | 组件相对于窗口信息。 |
| screenOffset | [Offset](js-apis-arkui-componentutils.md#offset) | 否 | 否 | 组件相对于屏幕信息。 |
| translate | [TranslateResult](js-apis-arkui-componentutils.md#translateresult) | 否 | 否 | 组件平移信息。 |
| scale | [ScaleResult](js-apis-arkui-componentutils.md#scaleresult) | 否 | 否 | 组件缩放信息。 |
| rotate | [RotateResult](js-apis-arkui-componentutils.md#rotateresult) | 否 | 否 | 组件旋转信息。 |
| transform | [Matrix4Result](js-apis-arkui-componentutils.md#matrix4result) | 否 | 否 | 仿射矩阵信息，根据入参创建的四阶矩阵对象。 |

### Size

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width | number | 否 | 否 | 组件宽度。  单位: px |
| height | number | 否 | 否 | 组件高度。  单位: px |

### Offset

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | x点坐标。  单位: px |
| y | number | 否 | 否 | y点坐标。  单位: px |

### TranslateResult

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | x轴平移距离。  单位: vp |
| y | number | 否 | 否 | y轴平移距离。  单位: vp |
| z | number | 否 | 否 | z轴平移距离。  单位: vp |

### ScaleResult

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | x轴缩放倍数。 |
| y | number | 否 | 否 | y轴缩放倍数。 |
| z | number | 否 | 否 | z轴缩放倍数。 |
| centerX | number | 否 | 否 | 变换中心点x轴坐标。  单位: vp |
| centerY | number | 否 | 否 | 变换中心点y轴坐标。  单位: vp |

### RotateResult

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 旋转轴向量x坐标。 |
| y | number | 否 | 否 | 旋转轴向量y坐标。 |
| z | number | 否 | 否 | 旋转轴向量z坐标。 |
| angle | number | 否 | 否 | 旋转角度。  单位: deg |
| centerX | number | 否 | 否 | 变换中心点x轴坐标。  单位: vp |
| centerY | number | 否 | 否 | 变换中心点y轴坐标。  单位: vp |

### Matrix4Result

PhonePC/2in1TabletTVWearable

type Matrix4Result = [number,number,number,number,number,number,number,number,number,number,number,number,number,number,number,number]

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [number,number,number,number,  number,number,number,number,  number,number,number,number,  number,number,number,number] | 取值范围为长度为16（4\*4）的number数组， 详情见四阶矩阵说明。 |

**四阶矩阵说明：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| m00 | number | 是 | x轴缩放值，单位矩阵默认为1。 |
| m01 | number | 是 | 第2个值，xyz轴旋转会影响这个值。 |
| m02 | number | 是 | 第3个值，xyz轴旋转会影响这个值。 |
| m03 | number | 是 | 无实际意义。 |
| m10 | number | 是 | 第5个值，xyz轴旋转会影响这个值。 |
| m11 | number | 是 | y轴缩放值，单位矩阵默认为1。 |
| m12 | number | 是 | 第7个值，xyz轴旋转会影响这个值。 |
| m13 | number | 是 | 无实际意义。 |
| m20 | number | 是 | 第9个值，xyz轴旋转会影响这个值。 |
| m21 | number | 是 | 第10个值，xyz轴旋转会影响这个值。 |
| m22 | number | 是 | z轴缩放值，单位矩阵默认为1。 |
| m23 | number | 是 | 无实际意义。 |
| m30 | number | 是 | x轴平移值，单位px，单位矩阵默认为0。 |
| m31 | number | 是 | y轴平移值，单位px，单位矩阵默认为0。 |
| m32 | number | 是 | z轴平移值，单位px，单位矩阵默认为0。 |
| m33 | number | 是 | 齐次坐标下生效，产生透视投影效果。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（获取ComponentUtils对象）

推荐通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getComponentUtils](arkts-apis-uicontext-uicontext.md#getcomponentutils)方法获取当前UI上下文关联的ComponentUtils对象。

```
1. import { matrix4, componentUtils } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Utils {
6. @State x: number = 120;
7. @State y: number = 10;
8. @State z: number = 100;
9. @State value: string = '';
10. private matrix1 = matrix4.identity().translate({ x: this.x, y: this.y, z: this.z });

12. build() {
13. Column() {
14. // $r("app.media.img")需要替换为开发者所需的图像资源文件
15. Image($r("app.media.img"))
16. .transform(this.matrix1)
17. .translate({ x: 20, y: 20, z: 20 })
18. .scale({ x: 0.5, y: 0.5, z: 1 })
19. .rotate({
20. x: 1,
21. y: 1,
22. z: 1,
23. centerX: '50%',
24. centerY: '50%',
25. angle: 300
26. })
27. .width(300)
28. .height(100)
29. .key("image_01")
30. Button('getRectangleById')
31. .onClick(() => {
32. this.value = JSON.stringify(this.getUIContext()
33. .getComponentUtils()
34. .getRectangleById("image_01")) // 建议使用this.getUIContext().getComponentUtils()接口
35. }).margin(10).id('onClick')
36. Text(this.value)
37. .margin(20)
38. .width(300)
39. .height(300)
40. .borderWidth(2)
41. }.margin({ left: 50 })
42. }
43. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/lrABA5UoSq2F0M30eMYvfw/zh-cn_image_0000002558606264.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055027Z&HW-CC-Expire=86400&HW-CC-Sign=601FB42323BEC763569E4168C918CA68861072C4C741ADEAE94AFD03D82B9EFB)
