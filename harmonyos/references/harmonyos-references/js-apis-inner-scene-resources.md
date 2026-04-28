---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene-resources
title: SceneResource
breadcrumb: API参考 > 图形 > ArkGraphics 3D（方舟3D图形） > ArkTS API > graphics3d > SceneResource
category: harmonyos-references
scraped_at: 2026-04-28T08:15:37+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:201b010de28324e688cc20bf8822466529d5fca753d5bba623e34e9cb41a7b10
---

本模块提供3D图形中常用的基本资源类型。

说明

* 本模块首批接口从API version 12开始支持，后续版本的新增接口，采用上角标标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { SceneResourceType, SceneResource, Shader, MaterialType, CullMode, Blend, RenderSort, Material,
2. MaterialProperty, MetallicRoughnessMaterial, ShaderMaterial, SamplerFilter, SamplerAddressMode, Sampler,
3. SubMesh, Morpher, Mesh, MeshResource, Animation, EnvironmentBackgroundType, Environment, Image } from '@kit.ArkGraphics3D';
```

## SceneResourceType

PhonePC/2in1TabletTVWearable

场景资源类型枚举，对场景中的资源进行分类。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN | 0 | 未定义类型。 |
| NODE | 1 | 节点类型。 |
| ENVIRONMENT | 2 | 环境类型。 |
| MATERIAL | 3 | 材质类型。 |
| MESH | 4 | 网格类型。 |
| ANIMATION | 5 | 动画类型。 |
| SHADER | 6 | 着色器类型。 |
| IMAGE | 7 | 图片类型。 |
| MESH\_RESOURCE18+ | 8 | 网格资源类型。 |
| EFFECT21+ | 9 | 后处理特效类型。 |

## SceneResource

PhonePC/2in1TabletTVWearable

用于表示场景中的资源。

### 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 名称，没有特殊格式要求。 |
| resourceType | [SceneResourceType](js-apis-inner-scene-resources.md#sceneresourcetype) | 是 | 否 | 场景资源类型，默认值为undefined。 |
| uri | [ResourceStr](ts-types.md#resourcestr) | 是 | 是 | 需要加载的资源，默认值为undefined。 |

### destroy

PhonePC/2in1TabletTVWearable

destroy(): void

销毁场景资源，释放所有关联的资源或引用，一旦被释放，资源就不能被再次使用或访问。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**示例：**

```
1. import { Shader, SceneResourceParameters, SceneResourceFactory, Scene } from '@kit.ArkGraphics3D';

3. function destroy(): void {
4. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
5. let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
6. scene.then(async (result: Scene) => {
7. if (result) {
8. let sceneFactory: SceneResourceFactory = result.getResourceFactory();
9. // 创建shader资源，路径和文件名可根据项目实际资源自定义
10. let sceneResourceParameter: SceneResourceParameters = { name: "shaderResource",
11. uri: $rawfile("shaders/custom_shader/custom_material_sample.shader") };
12. let shader: Promise<Shader> = sceneFactory.createShader(sceneResourceParameter);
13. shader.then(async (shaderResult:Shader) => {
14. // 释放资源
15. shaderResult.destroy();
16. });
17. }
18. });
19. }
```

## Shader

PhonePC/2in1TabletTVWearable

着色器，继承自[SceneResource](js-apis-inner-scene-resources.md#sceneresource-1)。

### 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| inputs | Record<string, number | [Vec2](js-apis-inner-scene-types.md#vec2) | [Vec3](js-apis-inner-scene-types.md#vec3) | [Vec4](js-apis-inner-scene-types.md#vec4) | Image> | 是 | 否 | 着色器输入。 |

### setShaderInputs23+

PhonePC/2in1TabletTVWearable

setShaderInputs(inputs: Record<string, number | Vec2 | Vec3 | Vec4 | Image>): void

设置[Shader](js-apis-inner-scene-resources.md#shader)的输入，该接口性能优于直接设置inputs属性。

**模型约束**： 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inputs | Record<string, number | [Vec2](js-apis-inner-scene-types.md#vec2) | [Vec3](js-apis-inner-scene-types.md#vec3) | [Vec4](js-apis-inner-scene-types.md#vec4) | Image> | 是 | 一个字符串到值的映射，用于设置shader输入。 |

**示例：**

```
1. import { Image, MaterialType, Scene, SceneResourceFactory, Shader, ShaderMaterial } from '@kit.ArkGraphics3D';

3. function setinputs(): void {
4. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
5. let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
6. scene.then(async (result: Scene) => {
7. if (result) {
8. let rf : SceneResourceFactory | null = await result.getResourceFactory();
9. if (!rf) {
10. return;
11. }
12. // 创建材质和shader
13. let material: ShaderMaterial | null = await rf.createMaterial({name: "CustomMaterial"}, MaterialType.SHADER);
14. let shader : Shader | null = await rf.createShader(
15. {name: "CustomShader", uri: $rawfile("shaders/custom_shader/custom_material_sample.shader")});
16. if (!material || !shader) {
17. return;
18. }
19. // 加载纹理资源
20. let image : Image | null = await rf.createImage({name: "envImg", uri: $rawfile("custom_image.jpg")});
21. if (!image) {
22. return;
23. }
24. // 绑定shader到纹理上
25. material.colorShader = shader;
26. // 设置shader输入
27. material.colorShader.setShaderInputs({
28. "uTime": 1.0,
29. "uVelocity": {x: 1.0, y: 1.0, z:-1.0, w:-1.0},
30. "uTexture": image
31. })
32. }
33. });
34. }
```

## MaterialType

PhonePC/2in1TabletTVWearable

场景中物体材质类型枚举，定义材质的渲染方式。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SHADER | 1 | 材质由着色器定义。 |
| METALLIC\_ROUGHNESS20+ | 2 | 采用基于物理渲染（PBR）的金属-粗糙度模型，通过金属度与粗糙度参数，模拟更真实的材质光照效果。 |
| UNLIT23+ | 3 | 不受光照影响的材质。 |
| OCCLUSION23+ | 4 | 遮挡材质，能够遮挡场景中的其他物体但不会遮挡环境。 |

## CullMode20+

PhonePC/2in1TabletTVWearable

用于设置基于物理渲染（PBR）材质的剔除模式枚举。通过控制剔除物体的正面或背面几何面片，提升渲染性能和视觉效果。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 禁用剔除。 |
| FRONT | 1 | 剔除正面几何面片。 |
| BACK | 2 | 剔除背面几何面片。 |

## Blend20+

PhonePC/2in1TabletTVWearable

用于控制材质的透明效果。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| enabled | boolean | 否 | 否 | 是否启用材质的透明效果模式。true表示开启透明，false表示关闭透明。 |

## RenderSort20+

PhonePC/2in1TabletTVWearable

定义材质物体的渲染顺序，控制不同物体在渲染管线中的绘制先后。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| renderSortLayer | number | 否 | 是 | 渲染图层id，数值越小，渲染顺序越靠前。取值范围[0, 63]，默认图层id为32。 |
| renderSortLayerOrder | number | 否 | 是 | 同一渲染图层内，不同物体的渲染顺序，数值越小，越先渲染。取值范围[0, 255]，默认值为0。 |

## PolygonMode23+

PhonePC/2in1TabletTVWearable

控制多边形绘制模式的枚举。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FILL | 0 | 绘制多边形的每个面。 |
| LINE | 1 | 仅绘制多边形线框。 |
| POINT | 2 | 仅绘制多边形顶点。 |

## Material

PhonePC/2in1TabletTVWearable

材质类型，继承自[SceneResource](js-apis-inner-scene-resources.md#sceneresource-1)。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| materialType | [MaterialType](js-apis-inner-scene-resources.md#materialtype) | 是 | 否 | 材质类型。 |
| shadowReceiver20+ | boolean | 否 | 是 | 材质是否接收阴影。true表示该材质接收阴影，false表示不接收，默认值为false。 |
| cullMode20+ | [CullMode](js-apis-inner-scene-resources.md#cullmode20) | 否 | 是 | 当前材质的剔除模式设置，用于控制是否剔除背面几何面片，默认值为BACK。 |
| blend20+ | [Blend](js-apis-inner-scene-resources.md#blend20) | 否 | 是 | 材质是否透明，默认值为false。 |
| alphaCutoff20+ | number | 否 | 是 | 透明通道阈值，如果像素的alpha值等于或高于此阈值，则渲染该像素；如果低于此阈值，则不会渲染该像素。设置值小于1时，则开启该模式，取值范围为[0, 1]，默认值为1。 |
| renderSort20+ | [RenderSort](js-apis-inner-scene-resources.md#rendersort20) | 否 | 是 | 渲染排序设置，用于控制材质在渲染管线中的渲染顺序，渲染图层id默认值为32，同一图层内的渲染顺序默认值为0。 |
| polygonMode23+ | [PolygonMode](js-apis-inner-scene-resources.md#polygonmode23) | 否 | 是 | 模型的多边形绘制模式，默认值为FILL。 |

## MaterialProperty20+

PhonePC/2in1TabletTVWearable

材质属性接口，用于定义材质所使用的纹理、属性因子及纹理采样器信息。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| image | [Image](js-apis-inner-scene-resources.md#image) | null | 否 | 否 | 基于物理渲染（PBR）属性纹理贴图，用于表达材质的纹理信息。 |
| factor | [Vec4](js-apis-inner-scene-types.md#vec4) | 否 | 否 | 基于物理渲染（PBR）属性因子，不同属性不同含义。 |
| sampler | [Sampler](js-apis-inner-scene-resources.md#sampler20) | 否 | 是 | 纹理贴图采样器，默认使用放大、缩小和mipmap过滤模式为线性过滤（LINEAR），纹理贴图U、V、W方向的寻址模式为重复（REPEAT）。 |

## MetallicRoughnessMaterial20+

PhonePC/2in1TabletTVWearable

用于实现真实感外观的材质资源。采用基于物理渲染（PBR）的金属-粗糙度模型，通过调节金属度和粗糙度参数，可模拟金属、塑料等不同材质的表面光照与反射效果，继承自[Material](js-apis-inner-scene-resources.md#material)。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| baseColor | [MaterialProperty](js-apis-inner-scene-resources.md#materialproperty20) | 否 | 否 | 基础颜色贴图，用于表达材质在没有光照情况下所表达的颜色信息。 |
| normal | [MaterialProperty](js-apis-inner-scene-resources.md#materialproperty20) | 否 | 否 | 法线贴图，表达物体表面结构细节，使光照效果更真实，不改变几何结构。 |
| material | [MaterialProperty](js-apis-inner-scene-resources.md#materialproperty20) | 否 | 否 | 金属材质参数。  粗糙度（Roughness）：表达材质因其表面细微的结构细节所导致的反光强弱程度。  金属度（Metallic）：表达材质的金属属性。  反射度（Reflectance）：材质的光反射率。 |
| ambientOcclusion | [MaterialProperty](js-apis-inner-scene-resources.md#materialproperty20) | 否 | 否 | 环境光遮蔽贴图，用于模拟环境光在物体凹陷或细节部分的遮挡效果，增强局部阴影表现，提高细节真实感。 |
| emissive | [MaterialProperty](js-apis-inner-scene-resources.md#materialproperty20) | 否 | 否 | 自发光颜色，表达材质自身作为光源向外发光的颜色信息。 |
| clearCoat | [MaterialProperty](js-apis-inner-scene-resources.md#materialproperty20) | 否 | 否 | 透明图层，类似于车漆、碳纤、被水打湿的表面的材质需要在面上再增加一个透明的、具有一定反光特性的面。 |
| clearCoatRoughness | [MaterialProperty](js-apis-inner-scene-resources.md#materialproperty20) | 否 | 否 | 透明图层粗糙度。 |
| clearCoatNormal | [MaterialProperty](js-apis-inner-scene-resources.md#materialproperty20) | 否 | 否 | 透明图层法线贴图。 |
| sheen | [MaterialProperty](js-apis-inner-scene-resources.md#materialproperty20) | 否 | 否 | 微纤维漫反射材质光泽，可用于表示布料和织物材料。 |
| specular | [MaterialProperty](js-apis-inner-scene-resources.md#materialproperty20) | 否 | 否 | 非金属材质的高光反射，表示传统镜面反射强度。 |

## ShaderMaterial

PhonePC/2in1TabletTVWearable

着色器材质，继承自[Material](js-apis-inner-scene-resources.md#material)。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| colorShader | [Shader](js-apis-inner-scene-resources.md#shader) | 否 | 是 | 着色器，默认值为undefined。 |

## UnlitMaterial23+

PhonePC/2in1TabletTVWearable

不受光照影响的材质，其着色值只与设置的基础颜色有关，与光照条件无关，继承自[Material](js-apis-inner-scene-resources.md#material)。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| baseColor | [MaterialProperty](js-apis-inner-scene-resources.md#materialproperty20) | 否 | 否 | 基础颜色属性，用于表达材质的基础颜色信息。 |

## OcclusionMaterial23+

PhonePC/2in1TabletTVWearable

遮挡材质，能够遮挡场景中的其他物体但不会遮挡环境，继承自[Material](js-apis-inner-scene-resources.md#material)。

**系统能力：** SystemCapability.ArkUi.Graphics3D

## SamplerFilter20+

PhonePC/2in1TabletTVWearable

采样器过滤模式枚举，定义纹理采样时的插值方法，用于控制纹理在缩放或变形时如何计算最终像素的颜色值。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NEAREST | 0 | 使用最近邻插值进行采样，速度快但边缘可能锯齿明显。 |
| LINEAR | 1 | 使用线性插值进行采样，效果更平滑但性能略低。 |

## SamplerAddressMode20+

PhonePC/2in1TabletTVWearable

采样器寻址模式枚举，用于控制纹理坐标超出[0, 1]范围时的处理方式。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 值 | 说明 |
| --- | --- | --- |
| REPEAT | 0 | 纹理坐标超出范围时，纹理会重复平铺。 |
| MIRRORED\_REPEAT | 1 | 纹理坐标超出范围时，纹理以镜像方式重复。 |
| CLAMP\_TO\_EDGE | 2 | 纹理坐标超出范围时，贴图边缘像素会被拉伸延伸。 |

## Sampler20+

PhonePC/2in1TabletTVWearable

采样器接口，用于定义纹理贴图采样时的过滤方式。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| magFilter | [SamplerFilter](js-apis-inner-scene-resources.md#samplerfilter20) | 否 | 是 | 放大过滤模式，控制纹理贴图被放大时的采样方式，默认值为LINEAR。 |
| minFilter | [SamplerFilter](js-apis-inner-scene-resources.md#samplerfilter20) | 否 | 是 | 缩小过滤模式，控制纹理贴图被缩小时的采样方式，默认值为LINEAR。 |
| mipMapMode | [SamplerFilter](js-apis-inner-scene-resources.md#samplerfilter20) | 否 | 是 | mipmap过滤模式，控制纹理贴图在多层不同分辨率之间的采样方式，默认值为LINEAR。 |
| addressModeU | [SamplerAddressMode](js-apis-inner-scene-resources.md#sampleraddressmode20) | 否 | 是 | 纹理贴图U方向（水平）的采样方式，默认值为REPEAT。 |
| addressModeV | [SamplerAddressMode](js-apis-inner-scene-resources.md#sampleraddressmode20) | 否 | 是 | 纹理贴图V方向（垂直）的采样方式，默认值为REPEAT。 |

## SubMesh

PhonePC/2in1TabletTVWearable

子网格类型。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 名称，没有特殊格式要求。 |
| material | [Material](js-apis-inner-scene-resources.md#material) | 否 | 否 | 材质。 |
| aabb | [Aabb](js-apis-inner-scene-types.md#aabb) | 是 | 否 | 轴对齐边界盒。 |

## Morpher20+

PhonePC/2in1TabletTVWearable

用于控制3D模型的形变，通过调整不同形变目标的权重，实现模型的动态变形效果。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| targets | Record<string, number> | 是 | 否 | 用于存储所有形变目标的名称和对应的权重。权重值通常在[0.0, 1.0]范围内。 |

## Mesh

PhonePC/2in1TabletTVWearable

网格类型，继承自[SceneResource](js-apis-inner-scene-resources.md#sceneresource-1)。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| subMeshes | [SubMesh](js-apis-inner-scene-resources.md#submesh)[] | 是 | 否 | 子网格数组。 |
| aabb | [Aabb](js-apis-inner-scene-types.md#aabb) | 是 | 否 | 轴对齐包围盒。 |
| materialOverride | [Material](js-apis-inner-scene-resources.md#material) | 否 | 是 | 材质，默认为空。 |

## MeshResource18+

PhonePC/2in1TabletTVWearable

网格资源，继承自[SceneResource](js-apis-inner-scene-resources.md#sceneresource-1)。

**系统能力：** SystemCapability.ArkUi.Graphics3D

## Animation

PhonePC/2in1TabletTVWearable

动画类型，继承自[SceneResource](js-apis-inner-scene-resources.md#sceneresource-1)。

### 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| enabled | boolean | 否 | 否 | 动画是否使能。true表示可以播放动画，false表示不可以播放动画。 |
| speed20+ | number | 否 | 是 | 动画的播放速度因子。默认值为1.0，表示正常速度播放。如果设置为负值，动画将以反向速度播放。 |
| duration | number | 是 | 否 | 动画持续时间，单位为秒（s），取值范围大于等于0。 |
| running | boolean | 是 | 否 | 动画运行状态。true表示动画正在播放，false表示动画停止播放。 |
| progress | number | 是 | 否 | 动画进度状态，取值区间为[0, 1]。 |

### onFinished

PhonePC/2in1TabletTVWearable

onFinished(callback: Callback<void>): void

动画播放结束时执行的回调函数，动画播放完成或者finish操作会触发这个回调。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<void> | 是 | 回调函数，返回值为空。 |

**示例：**

```
1. import { Animation, Scene } from '@kit.ArkGraphics3D';

3. function onFinished(): void {
4. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
5. let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
6. scene.then(async (result: Scene) => {
7. if (result && result.animations && result.animations[0]) {
8. let anim: Animation = result.animations[0];
9. // 注册回调函数
10. anim.onFinished(()=>{
11. console.info("onFinished");
12. });
13. }
14. });
15. }
```

### onStarted

PhonePC/2in1TabletTVWearable

onStarted(callback: Callback<void>): void

当动画开始播放时执行的回调函数，start操作以及restart操作也会触发这个回调。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<void> | 是 | 回调函数，返回值为空。 |

**系统能力：** SystemCapability.ArkUi.Graphics3D

**示例：**

```
1. import { Animation, Scene } from '@kit.ArkGraphics3D';

3. function onStarted(): void {
4. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
5. let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
6. scene.then(async (result: Scene) => {
7. if (result && result.animations && result.animations[0]) {
8. let anim: Animation = result.animations[0];
9. // 注册回调函数
10. anim.onStarted(()=>{
11. console.info("onStarted");
12. });
13. }
14. });
15. }
```

### pause

PhonePC/2in1TabletTVWearable

pause(): void

将动画暂停，动画的播放进度保持在当前状态。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**示例：**

```
1. import { Animation, Scene } from '@kit.ArkGraphics3D';

3. function pause(): void {
4. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
5. let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
6. scene.then(async (result: Scene) => {
7. if (result && result.animations && result.animations[0]) {
8. let anim: Animation = result.animations[0];
9. // 暂停动画
10. anim.pause();
11. }
12. });
13. }
```

### restart

PhonePC/2in1TabletTVWearable

restart(): void

从动画的起点开始播放动画。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**示例：**

```
1. import { Animation, Scene } from '@kit.ArkGraphics3D';

3. function restart(): void {
4. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
5. let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
6. scene.then(async (result: Scene) => {
7. if (result && result.animations && result.animations[0]) {
8. let anim: Animation = result.animations[0];
9. // 重启动画
10. anim.restart();
11. }
12. });
13. }
```

### seek

PhonePC/2in1TabletTVWearable

seek(position: number): void

从指定位置开始播放动画。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| position | number | 是 | 要重新播放动画的起始位置，取值区间为[0, 1]。 |

**示例：**

```
1. import { Animation, Scene } from '@kit.ArkGraphics3D';

3. function seek(): void {
4. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
5. let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
6. scene.then(async (result: Scene) => {
7. if (result && result.animations && result.animations[0]) {
8. let anim: Animation = result.animations[0];
9. // 指定动画的播放进度到10%
10. anim.seek(0.1);
11. }
12. });
13. }
```

### start

PhonePC/2in1TabletTVWearable

start(): void

基于当前进度开始播放一个动画。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**示例：**

```
1. import { Animation, Scene } from '@kit.ArkGraphics3D';

3. function start(): void {
4. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
5. let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
6. scene.then(async (result: Scene) => {
7. if (result && result.animations && result.animations[0]) {
8. let anim: Animation = result.animations[0];
9. // 开始动画
10. anim.start();
11. }
12. });
13. }
```

### stop

PhonePC/2in1TabletTVWearable

stop(): void

停止播放一个动画，并将动画的进度设置到未开始状态。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**示例：**

```
1. import { Animation, Scene } from '@kit.ArkGraphics3D';

3. function stop(): void {
4. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
5. let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
6. scene.then(async (result: Scene) => {
7. if (result && result.animations && result.animations[0]) {
8. let anim: Animation = result.animations[0];
9. // 停止播放动画，并将动画的进度设置到未开始状态
10. anim.stop();
11. }
12. });
13. }
```

### finish

PhonePC/2in1TabletTVWearable

finish(): void

直接跳转到动画的最后，并将动画的进度设置到已结束状态。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**示例：**

```
1. import { Animation, Scene } from '@kit.ArkGraphics3D';

3. function finish(): void {
4. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
5. let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
6. scene.then(async (result: Scene) => {
7. if (result && result.animations && result.animations[0]) {
8. let anim: Animation = result.animations[0];
9. // 直接跳转到动画的最后，并将动画的进度设置到已结束状态。
10. anim.finish();
11. }
12. });
13. }
```

## EnvironmentBackgroundType

PhonePC/2in1TabletTVWearable

环境背景类型枚举，用于定义场景的背景呈现方式。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BACKGROUND\_NONE | 0 | 无背景。 |
| BACKGROUND\_IMAGE | 1 | 图片背景。 |
| BACKGROUND\_CUBEMAP | 2 | 立方体贴图背景。 |
| BACKGROUND\_EQUIRECTANGULAR | 3 | 等距柱状投影背景。 |

## Environment

PhonePC/2in1TabletTVWearable

环境类型，继承自[SceneResource](js-apis-inner-scene-resources.md#sceneresource-1)。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| backgroundType | [EnvironmentBackgroundType](js-apis-inner-scene-resources.md#environmentbackgroundtype) | 否 | 否 | 环境背景类型。 |
| indirectDiffuseFactor | [Vec4](js-apis-inner-scene-types.md#vec4) | 否 | 否 | 间接散射系数。 |
| indirectSpecularFactor | [Vec4](js-apis-inner-scene-types.md#vec4) | 否 | 否 | 间接反射系数。 |
| environmentMapFactor | [Vec4](js-apis-inner-scene-types.md#vec4) | 否 | 否 | 环境地图系数。 |
| environmentImage | [Image](js-apis-inner-scene-resources.md#image) | null | 否 | 是 | 环境图片，默认为undefined。 |
| radianceImage | [Image](js-apis-inner-scene-resources.md#image) | null | 否 | 是 | 辐射图片，默认为undefined。 |
| irradianceCoefficients | [Vec3](js-apis-inner-scene-types.md#vec3)[] | 否 | 是 | 辐射系数，默认为undefined。 |
| environmentRotation23+ | [Quaternion](js-apis-inner-scene-types.md#quaternion) | 否 | 是 | 环境光的旋转，默认为undefined，接收参数需为归一化后的四元数。 |

## Image

PhonePC/2in1TabletTVWearable

图片类型，继承自[SceneResource](js-apis-inner-scene-resources.md#sceneresource-1)。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width | number | 是 | 否 | 图片宽度，单位为像素（px），取值范围大于0。 |
| height | number | 是 | 否 | 图片高度，单位为像素（px），取值范围大于0。 |

## Effect21+

PhonePC/2in1TabletTVWearable

特效类型，继承自[SceneResource](js-apis-inner-scene-resources.md#sceneresource-1)。由[createEffect](js-apis-inner-scene.md#createeffect21)接口获得。

### 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| enabled | boolean | 否 | 否 | 特效打开状态。true表示开启特效，false表示关闭特效。 |
| effectId | string | 是 | 否 | 特效ID，固定格式为'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'，用于特效的创建，比如'e68a7f45-2d21-4a0d-9aef-7d9c825d3f12'。 |

### getPropertyValue23+

PhonePC/2in1TabletTVWearable

getPropertyValue(propertyName: string): Object | null | undefined

获取特定特效属性的值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propertyName | string | 是 | 特定特效属性的名称。目前支持的字符串为：  -'exposure':该属性表示图像的曝光度。  -'vibrance': 该属性表示图像的自然饱和度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | null | undefined | 特效属性值。若当前Effect类型下不存在与传入的propertyName匹配的属性，则获取属性值失败，返回null；若propertyName对应的可选属性未设置，则返回undefined。 |

**示例：**

```
1. import { SceneResourceFactory, Scene, Effect, EffectParameters } from '@kit.ArkGraphics3D';

3. function getEffectProperty() {
4. let scene: Promise<Scene> = Scene.load();
5. scene.then(async (result: Scene | undefined) => {
6. if (!result) {
7. return;
8. }
9. let sceneFactory: SceneResourceFactory = result.getResourceFactory();
10. // 特效ID，固定格式为'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'，比如'e68a7f45-2d21-4a0d-9aef-7d9c825d3f12'
11. let params: EffectParameters = {effectId: "e68a7f45-2d21-4a0d-9aef-7d9c825d3f12"};
12. let effect: Effect = await sceneFactory.createEffect(params);
13. effect.getPropertyValue('exposure');
14. });
15. }
```

### setPropertyValue23+

PhonePC/2in1TabletTVWearable

setPropertyValue(propertyName: string, value: Object | undefined): boolean

设置特定特效属性的值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propertyName | string | 是 | 特定特效属性的名称。目前支持的字符串为：  -'exposure':该属性表示图像的曝光度。  -'vibrance': 该属性表示图像的自然饱和度。 |
| value | Object | undefined | 是 | 要设置的特效属性值。  -'exposure'：value实际类型为number，推荐取值范围[-5, 5]。取值越大，图像越亮。  -'vibrance'：value实际类型为number，推荐取值范围 [-1, 1]。取值越大，图像颜色越鲜艳。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回设置特效属性值操作是否成功。true表示设置成功，false表示设置失败。 |

**示例：**

```
1. import { SceneResourceFactory, Scene, Effect, EffectParameters } from '@kit.ArkGraphics3D';

3. function setEffectProperty() {
4. let scene: Promise<Scene> = Scene.load();
5. scene.then(async (result: Scene | undefined) => {
6. if (!result) {
7. return;
8. }
9. let sceneFactory: SceneResourceFactory = result.getResourceFactory();
10. // 特效ID，固定格式为'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'，比如'e68a7f45-2d21-4a0d-9aef-7d9c825d3f12'
11. let params: EffectParameters = {effectId: "e68a7f45-2d21-4a0d-9aef-7d9c825d3f12"};
12. let effect: Effect = await sceneFactory.createEffect(params);
13. effect.setPropertyValue('exposure', 1);
14. });
15. }
```
