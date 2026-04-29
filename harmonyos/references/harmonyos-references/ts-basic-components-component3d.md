---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-component3d
title: Component3D
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 渲染绘制 > Component3D
category: harmonyos-references
scraped_at: 2026-04-29T13:52:39+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:cf01a1a12e91821525b1a57caef96a6c4d2e78dd89e7e4250b4dc95d1e1be995
---

3D渲染组件，用于将ArkGraphics 3D场景或glTF（.gltf文件和.glb文件）模型渲染到ArkUI界面中，支持自定义场景模式与自动场景模式，并提供自定义渲染管线能力。

说明

该组件从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

无

## 接口

PhonePC/2in1TabletTVWearable

Component3D(sceneOptions?: SceneOptions)

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sceneOptions | [SceneOptions](ts-basic-components-component3d.md#sceneoptions对象说明) | 否 | 3D场景配置选项，默认值为undefined。  **说明：**  3D场景配置选项在控件创建后不支持动态修改。 |

## SceneOptions对象说明

PhonePC/2in1TabletTVWearable

Component3D组件配置选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scene | [ResourceStr](ts-types.md#resourcestr) | [Scene](ts-basic-components-component3d.md#scene12) | 否 | 是 | 3D模型资源文件或场景对象，默认值为undefined。  当传入glTF（.gltf文件和.glb文件）模型时，组件以自动场景模式运行，框架会自动创建基础相机、光源和默认手势交互（旋转、缩放），其相关参数由框架内部管理，不支持外部修改，开发者仅可通过Component3D的属性对展示效果进行配置。  当传入Scene对象时，组件以自定义场景模式运行，相机、光源及交互由开发者通过ArkGraphics 3D API自行创建和管理。  当不填写此参数时，组件仅作为自定义渲染管线（shader/customRender）的输出容器使用。  **说明：**  自定义场景模式下未内置相机控制器，因此不会自动响应拖拽或缩放手势；如需交互，请开发者接入手势并更新相机的位置与旋转。 |
| modelType | [ModelType](ts-basic-components-component3d.md#modeltype枚举说明) | 否 | 是 | 3D场景显示合成方式。  默认值：ModelType.SURFACE  **说明：**  设置为ModelType.TEXTURE时通过GPU合成显示。  设置为ModelType.SURFACE时通过专有硬件合成显示。  一般开发者可以使用默认值而无需关心此项设置。 |

## ModelType枚举说明

PhonePC/2in1TabletTVWearable

渲染合成模式类型枚举，用于指定3D场景的渲染输出方式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TEXTURE | 0 | 使用GPU合成显示3D场景。 |
| SURFACE | 1 | 使用专有硬件显示3D场景。 |

## Scene12+

PhonePC/2in1TabletTVWearable

type Scene = Scene

设置3D场景。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 类型 | 说明 |
| --- | --- |
| [Scene](js-apis-inner-scene.md#scene-1) | 用于设置场景。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### environment

PhonePC/2in1TabletTVWearable

environment(uri: ResourceStr)

设置3D环境资源。目前仅支持GLTF格式资源，模型资源在控件创建后不支持动态修改。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | [ResourceStr](ts-types.md#resourcestr) | 是 | 3D环境资源。 |

### customRender

PhonePC/2in1TabletTVWearable

customRender(uri: ResourceStr, selfRenderUpdate: boolean)

设置三维场景渲染的渲染管线。管线配置及自渲染属性在控件创建后不支持动态修改。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | [ResourceStr](ts-types.md#resourcestr) | 是 | 自定义渲染管线的配置文件。 |
| selfRenderUpdate | boolean | 是 | 当设置为true时外部UI没有更新时也能触发动效渲染。  当设置为false时只有外部UI更新才能触发渲染。 |

### shader

PhonePC/2in1TabletTVWearable

shader(uri: ResourceStr)

设置自定义渲染的shader文件资源。自定义渲染的shader文件资源在控件创建后不支持动态修改。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | [ResourceStr](ts-types.md#resourcestr) | 是 | 自定义渲染的shader文件资源。详细.shader文件格式请参考[.shader资源文件格式要求](../harmonyos-guides/arkgraphics3d-shader-resource.md)。 |

### shaderImageTexture

PhonePC/2in1TabletTVWearable

shaderImageTexture(uri: ResourceStr)

设置自定义渲染用到的纹理资源。若自定义渲染用到多个纹理资源则调用多次，绑定点与调用顺序一致，不支持纹理更换。纹理资源在控件创建后不支持动态修改。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | [ResourceStr](ts-types.md#resourcestr) | 是 | 自定义渲染用到的纹理资源。 |

### shaderInputBuffer

PhonePC/2in1TabletTVWearable

shaderInputBuffer(buffer: Array<number>)

设置自定义渲染用到的动效参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | Array<number> | 是 | 自定义渲染用到的动效参数，数组长度范围为[0, 1048576]。 |

### renderWidth

PhonePC/2in1TabletTVWearable

renderWidth(value: Dimension)

设置3D渲染分辨率的宽度。渲染分辨率的宽高可以不同于控件的宽高，若渲染分辨率与控件分辨率宽高不一致时会上采样或下采样到控件宽高。

不调用此属性时默认渲染分辨率。

渲染分辨率在控件创建后不支持动态修改。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Dimension](ts-types.md#dimension10) | 是 | 3D渲染分辨率的宽度，当前仅支持设置Dimension.Percentage，取值范围是[0, 100%]。 |

### renderHeight

PhonePC/2in1TabletTVWearable

renderHeight(value: Dimension)

设置3D渲染分辨率的高度。渲染分辨率的宽高可以不同于控件的宽高，若渲染分辨率与控件分辨率宽高不一致时会上采样或下采样到控件宽高。

不调用此属性时默认渲染分辨率。

渲染分辨率在控件创建后不支持动态修改。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Dimension](ts-types.md#dimension10) | 是 | 3D渲染分辨率的高度，当前仅支持设置Dimension.Percentage，取值范围是[0, 100%]。 |

## 事件

PhonePC/2in1TabletTVWearable

支持[通用事件](ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

示例效果请以真机运行为准，当前DevEco Studio预览器不支持。

GLTF模型加载示例。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
6. scene: SceneOptions = { scene: $rawfile('gltf/DamagedHelmet/glTF/DamagedHelmet.gltf'), modelType: ModelType.SURFACE};
7. build() {
8. Row() {
9. Column() {
10. Text('GLTF Example')
11. Component3D( this.scene )
12. // 绑定环境资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
13. .environment($rawfile('gltf/Environment/glTF/Environment.gltf'))
14. .renderWidth('90%').renderHeight('90%')
15. }.width('100%')
16. }
17. .height('100%')
18. }
19. }
```

自定义渲染示例。

```
1. import { AnimatorResult } from '@kit.ArkUI';

3. class EngineTime {
4. totalTimeUs = 0;
5. deltaTimeUs = 0;
6. };

8. let engineTime = new EngineTime();
9. let frameCount: number = 0;

11. function TickFrame() {
12. if (frameCount == 10) {
13. engineTime.totalTimeUs += 1.0;
14. engineTime.deltaTimeUs += 1.0;
15. frameCount = 0;
16. } else {
17. frameCount++;
18. }
19. }

21. @Entry
22. @Component
23. struct Index {
24. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
25. scene: SceneOptions = { scene: $rawfile('gltf/DamagedHelmet/glTF/DamagedHelmet.gltf'), modelType: ModelType.SURFACE};
26. backAnimator: AnimatorResult = this.getUIContext().createAnimator({
27. duration: 2000,
28. easing: "ease",
29. delay: 0,
30. fill: "none",
31. direction: "normal",
32. iterations: -1,
33. begin: 100,
34. end: 200,
35. });
36. @State timeDelta: number[] = [1.0, 2.0];
37. create() {
38. this.backAnimator.onFinish = () => {
39. console.info('backAnimator onfinish');
40. }
41. this.backAnimator.onFrame = (value: number) => {
42. TickFrame();
43. this.timeDelta[0] = engineTime.deltaTimeUs;
44. }

46. }
47. build() {
48. Row() {
49. Column() {
50. Text('custom rendering')
51. Component3D()
52. // 绑定自定义shader脚本，路径和文件名可根据项目实际资源自定义
53. .shader($rawfile('assets/app/shaders/shader/London.shader'))
54. // 绑定贴图资源作为shader输入纹理，路径和文件名可根据项目实际资源自定义
55. .shaderImageTexture($rawfile('assets/London.jpg'))
56. .shaderInputBuffer(this.timeDelta)
57. // 绑定自定义渲染流程文件（如.rng），路径和文件名可根据项目实际资源自定义
58. .customRender($rawfile('assets/app/rendernodegraphs/London.rng'), true)
59. .renderWidth('90%').renderHeight('90%')
60. .onAppear(() => {
61. this.create();
62. this.backAnimator.play();
63. }).width('50%').height('50%')
64. }.width('100%')
65. }
66. .height('100%')
67. }
68. }
```
