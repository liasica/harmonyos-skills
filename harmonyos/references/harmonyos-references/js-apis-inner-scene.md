---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene
title: Scene
breadcrumb: API参考 > 图形 > ArkGraphics 3D（方舟3D图形） > ArkTS API > graphics3d > Scene
category: harmonyos-references
scraped_at: 2026-04-28T08:15:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f4f622fcf1958c6f03c7dea9e36def972f10656dc6ca2f2c686f83c601448026
---

本模块作为ArkGraphics 3D基础模块，提供SceneResourceParameters、SceneNodeParameters等通用数据类型。同时提供glTF模型加载，场景元素、资源创建等基础方法。

说明

* 本模块首批接口从API version 12开始支持，后续版本的新增接口，采用上角标标记接口的起始版本。
* 关于.shader资源文件，具体请见[.shader资源文件格式要求](../harmonyos-guides/arkgraphics3d-shader-resource.md)。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { SceneResourceParameters, SceneNodeParameters, RaycastResult, RaycastParameters,RenderResourceFactory,
2. SceneResourceFactory, SceneComponent, RenderContext, RenderConfiguration, RenderParameters, Scene } from '@kit.ArkGraphics3D';
```

## SceneResourceParameters

PhonePC/2in1TabletTVWearable

场景资源参数对象，包含name和uri，用于提供场景资源的名称以及3D场景所需的资源文件路径。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 要创建资源的名称，可由开发者自定填写，用于标识该场景资源。 |
| uri | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 3D场景所需的资源文件路径。默认值为undefined。 |

**示例：**

```
1. import { Shader, SceneResourceParameters, SceneResourceFactory, Scene } from '@kit.ArkGraphics3D';

3. function createShaderPromise(): Promise<Shader> {
4. return new Promise((resolve, reject) => {
5. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
6. let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
7. scene.then(async (result: Scene) => {
8. let sceneFactory: SceneResourceFactory = result.getResourceFactory();

10. // 创建shader资源（通过SceneResourceParameters配置），路径和文件名可根据项目实际资源自定义
11. let sceneResourceParameter: SceneResourceParameters = { name: "shaderResource",
12. uri: $rawfile("shaders/custom_shader/custom_material_sample.shader") };
13. let shader: Shader = await sceneFactory.createShader(sceneResourceParameter);
14. resolve(shader);
15. }).catch((error: Error) => {
16. console.error('Scene load failed:', error);
17. reject(error);
18. });
19. });
20. }
```

## SceneNodeParameters

PhonePC/2in1TabletTVWearable

场景节点参数对象，它用于提供场景节点层次中的名称和路径。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 要创建的节点名称，可由开发者自定义填写，用于标识场景节点。 |
| path | string | 否 | 是 | 场景节点层次中的路径。用于指定创建的摄影机、灯光或节点在场景节点层次中的放置位置。每层之间使用'/'符号进行分割。如果未提供，则将其设置为根节点的子节点。默认值为undefined。 |

**示例：**

```
1. import { SceneNodeParameters, SceneResourceFactory, Scene, Node } from '@kit.ArkGraphics3D';

3. function createNodePromise() : Promise<Node> {
4. return new Promise((resolve, reject) => {
5. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
6. let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
7. scene.then(async (result: Scene) => {
8. let sceneFactory: SceneResourceFactory = result.getResourceFactory();

10. // 创建SceneNodeParameters类型变量并以此创建node
11. let sceneNodeParameter: SceneNodeParameters = { name: "empty_node",
12. path:"/rootNode_/empty_node" };
13. let node: Node = await sceneFactory.createNode(sceneNodeParameter);
14. resolve(node);
15. }).catch((error: Error) => {
16. console.error('Scene load failed:', error);
17. reject(error);
18. });
19. });
20. }
```

## RaycastResult20+

PhonePC/2in1TabletTVWearable

射线检测命中结果对象，包含被射线击中的3D物体详细信息。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| node | [Node](js-apis-inner-scene-nodes.md#node) | 否 | 否 | 被射线击中的3D场景节点，可通过该节点操作目标物体（如移动、旋转、隐藏）。 |
| centerDistance | number | 否 | 否 | 命中物体包围盒中心到摄像机中心的距离，单位为世界坐标系下的场景单位（比如cm、m、km等），取值范围大于0。 |
| hitPosition | [Position3](js-apis-inner-scene-types.md#position3) | 否 | 否 | 射线与物体碰撞点的精确世界坐标（{x: number, y: number, z: number}），单位为世界坐标系下的场景单位（比如cm、m、km等）。 |

## RaycastParameters20+

PhonePC/2in1TabletTVWearable

射线检测参数配置，用于定义射线检测的行为。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| rootNode | [Node](js-apis-inner-scene-nodes.md#node) | 否 | 是 | 限定检测范围：仅检测该节点及其子节点。未设置时检测全场景。 |

## RenderResourceFactory20+

PhonePC/2in1TabletTVWearable

用于创建可在共享[RenderContext](js-apis-inner-scene.md#rendercontext20)的多个场景（[Scene](js-apis-inner-scene.md#scene-1)）中共享的渲染资源。

### createShader20+

PhonePC/2in1TabletTVWearable

createShader(params: SceneResourceParameters): Promise<Shader>

根据指定场景资源参数创建一个着色器，使用Promise异步回调。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [SceneResourceParameters](js-apis-inner-scene.md#sceneresourceparameters) | 是 | 创建着色器的参数。详细.shader文件格式请参考[.shader资源文件格式要求](../harmonyos-guides/arkgraphics3d-shader-resource.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Shader](js-apis-inner-scene-resources.md#shader)> | Promise对象，返回创建的着色器对象。 |

**示例：**

```
1. import { Shader, SceneResourceParameters, Scene, RenderContext, RenderResourceFactory } from '@kit.ArkGraphics3D';

3. function createShaderResource(): Promise<Shader> {
4. const renderContext: RenderContext | null = Scene.getDefaultRenderContext();
5. if (!renderContext) {
6. return Promise.reject(new Error("RenderContext is null"));
7. }
8. const renderResourceFactory: RenderResourceFactory = renderContext.getRenderResourceFactory();
9. // 创建shader资源，路径和文件名可根据项目实际资源自定义
10. let shaderParams: SceneResourceParameters = {
11. name: "custom_shader",
12. uri: $rawfile("shaders/custom_shader/custom_material_sample.shader")
13. };
14. return renderResourceFactory.createShader(shaderParams);
15. }
```

### createImage20+

PhonePC/2in1TabletTVWearable

createImage(params: SceneResourceParameters): Promise<Image>

根据指定场景资源参数创建一个图像资源，使用Promise异步回调。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [SceneResourceParameters](js-apis-inner-scene.md#sceneresourceparameters) | 是 | 创建图像的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Image](js-apis-inner-scene-resources.md#image)> | Promise对象，返回创建的图像对象。 |

**示例：**

```
1. import { Image, SceneResourceParameters, Scene, RenderContext, RenderResourceFactory } from '@kit.ArkGraphics3D';

3. function createImageResource(): Promise<Image> {
4. const renderContext: RenderContext | null = Scene.getDefaultRenderContext();
5. if (!renderContext) {
6. return Promise.reject(new Error("RenderContext is null"));
7. }
8. const renderResourceFactory: RenderResourceFactory = renderContext.getRenderResourceFactory();
9. // 加载图片资源，路径和文件名可根据项目实际资源自定义
10. let imageParams: SceneResourceParameters = {
11. name: "sampleImage",
12. uri: $rawfile("image/Cube_BaseColor.png")
13. };
14. return renderResourceFactory.createImage(imageParams);
15. }
```

### createMesh20+

PhonePC/2in1TabletTVWearable

createMesh(params: SceneResourceParameters, geometry: GeometryDefinition): Promise<MeshResource>

根据指定场景资源参数和几何体定义（GeometryDefinition）创建一个网格资源（MeshResource），使用Promise异步回调。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [SceneResourceParameters](js-apis-inner-scene.md#sceneresourceparameters) | 是 | 创建网格资源的参数。 |
| geometry | [GeometryDefinition](js-apis-inner-scene-types.md#geometrydefinition18) | 是 | 几何形状定义，描述要创建的网格形状。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[MeshResource](js-apis-inner-scene-resources.md#meshresource18)> | Promise对象，返回创建的网格资源对象。 |

**示例：**

```
1. import { SceneResourceParameters, Scene, CustomGeometry, PrimitiveTopology, RenderContext, RenderResourceFactory,
2. MeshResource }  from '@kit.ArkGraphics3D';

4. function createMeshResource(): Promise<MeshResource> {
5. const renderContext: RenderContext | null = Scene.getDefaultRenderContext();
6. if (!renderContext) {
7. return Promise.reject(new Error("RenderContext is null"));
8. }
9. const renderResourceFactory: RenderResourceFactory = renderContext.getRenderResourceFactory();
10. const geometry = new CustomGeometry();
11. geometry.vertices = [
12. { x: 0, y: 0, z: 0 },
13. { x: 1, y: 0, z: 0 },
14. { x: 1, y: 1, z: 0 },
15. { x: 0, y: 1, z: 0 },
16. { x: 0, y: 0, z: 1 },
17. { x: 1, y: 0, z: 1 },
18. { x: 1, y: 1, z: 1 },
19. { x: 0, y: 1, z: 1 }
20. ];
21. geometry.indices = [
22. 0, 1, 2, 2, 3, 0,     // front
23. 4, 5, 6, 6, 7, 4,     // back
24. 0, 4, 5, 5, 1, 0,     // bottom
25. 1, 5, 6, 6, 2, 1,     // right
26. 3, 2, 6, 6, 7, 3,     // top
27. 3, 7, 4, 4, 0, 3      // left
28. ];
29. geometry.topology = PrimitiveTopology.TRIANGLE_LIST;
30. geometry.normals = [
31. { x: 0, y: 0, z: 1 },
32. { x: 0, y: 0, z: 1 },
33. { x: 0, y: 0, z: 1 },
34. { x: 0, y: 0, z: 1 },
35. { x: 0, y: 0, z: 1 },
36. { x: 0, y: 0, z: 1 },
37. { x: 0, y: 0, z: 1 },
38. { x: 0, y: 0, z: 1 }
39. ];
40. geometry.uvs = [
41. { x: 0, y: 0 },
42. { x: 1, y: 0 },
43. { x: 1, y: 1 },
44. { x: 0, y: 1 },
45. { x: 0, y: 0 },
46. { x: 1, y: 0 },
47. { x: 1, y: 1 },
48. { x: 0, y: 1 }
49. ];
50. geometry.colors = [
51. { r: 1, g: 0, b: 0, a: 1 },
52. { r: 0, g: 1, b: 0, a: 1 },
53. { r: 0, g: 0, b: 1, a: 1 },
54. { r: 1, g: 1, b: 0, a: 1 },
55. { r: 1, g: 0, b: 1, a: 1 },
56. { r: 0, g: 1, b: 1, a: 1 },
57. { r: 1, g: 1, b: 1, a: 1 },
58. { r: 0, g: 0, b: 0, a: 1 }
59. ];
60. // 加载图片资源，路径和文件名可根据项目实际资源自定义
61. let sceneResourceParameter: SceneResourceParameters = {
62. name: "cubeMesh",
63. uri: $rawfile("image/Cube_BaseColor.png")
64. };
65. return renderResourceFactory.createMesh(sceneResourceParameter, geometry);
66. }
```

### createSampler20+

PhonePC/2in1TabletTVWearable

createSampler(params:SceneResourceParameters): Promise<Sampler>

根据指定场景资源参数创建一个采样器资源，使用Promise异步回调。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [SceneResourceParameters](js-apis-inner-scene.md#sceneresourceparameters) | 是 | 创建采样器的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Sampler](js-apis-inner-scene-resources.md#sampler20)> | Promise对象，返回创建的采样器对象。 |

**示例：**

```
1. import { SceneResourceParameters, Scene, RenderContext, RenderResourceFactory, Sampler } from '@kit.ArkGraphics3D';

3. function createSamplerResource(): Promise<Sampler> {
4. const renderContext: RenderContext | null = Scene.getDefaultRenderContext();
5. if (!renderContext) {
6. return Promise.reject(new Error("RenderContext is null"));
7. }
8. const renderResourceFactory: RenderResourceFactory = renderContext.getRenderResourceFactory();
9. // 加载图片资源，路径和文件名可根据项目实际资源自定义
10. let samplerParams: SceneResourceParameters = {
11. name: "sampler1",
12. uri: $rawfile("image/Cube_BaseColor.png")
13. };
14. return renderResourceFactory.createSampler(samplerParams);
15. }
```

### createScene20+

PhonePC/2in1TabletTVWearable

createScene(uri?: ResourceStr): Promise<Scene>

从指定的资源URI创建一个新的场景。如果不指定URI，则创建一个空场景，使用Promise异步回调。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | [ResourceStr](ts-types.md#resourcestr) | 否 | 创建场景使用的资源路径，如果未传入资源路径，则默认创建一个空场景。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Scene](js-apis-inner-scene.md#scene-1)> | Promise对象，返回创建的场景对象。 |

**示例：**

```
1. import { Scene, RenderContext, RenderResourceFactory } from '@kit.ArkGraphics3D';

3. // fromFile=true：从指定glb文件加载场景，fromFile=false：创建一个空场景，此参数是为了示例展示两种常见场景创建方式
4. function createScenePromise(fromFile: boolean = false): Promise<Scene> {
5. const renderContext: RenderContext | null = Scene.getDefaultRenderContext();
6. if (!renderContext) {
7. return Promise.reject(new Error("RenderContext is null"));
8. }

10. const renderResourceFactory: RenderResourceFactory = renderContext.getRenderResourceFactory();
11. if (fromFile) {
12. // 创建场景并加载.gltf或.glb文件作为初始内容，路径和名称可根据项目实际资源自定义
13. return renderResourceFactory.createScene($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
14. } else {
15. // 创建空场景
16. return renderResourceFactory.createScene();
17. }
18. }
```

## CameraParameters21+

PhonePC/2in1TabletTVWearable

相机创建参数配置，用于定义相机创建的额外选项。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| msaa22+ | boolean | 否 | 是 | 相机是否使能MSAA，true表示使能MSAA，false表示不使能MSAA。默认值为false。 |
| renderingPipeline21+ | [RenderingPipelineType](js-apis-inner-scene-types.md#renderingpipelinetype21) | 否 | 是 | 选择初始渲染管线类型，默认为轻量级前向渲染管线类型。 |

## EffectParameters21+

PhonePC/2in1TabletTVWearable

特效参数配置，用于指定创建特效时所需的特效ID，作为[createEffect](js-apis-inner-scene.md#createeffect21)接口的入参来创建特效对象。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| effectId | string | 否 | 否 | 用于创建特效的ID，固定格式为'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'，比如'e68a7f45-2d21-4a0d-9aef-7d9c825d3f12'。 |

## SceneResourceFactory

PhonePC/2in1TabletTVWearable

用于创建3D场景中资源的接口，例如相机、光源等，继承自[RenderResourceFactory](js-apis-inner-scene.md#renderresourcefactory20)。

### createCamera

PhonePC/2in1TabletTVWearable

createCamera(params: SceneNodeParameters): Promise<Camera>

根据节点参数创建相机，使用Promise异步回调。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [SceneNodeParameters](js-apis-inner-scene.md#scenenodeparameters) | 是 | 场景节点参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Camera](js-apis-inner-scene-nodes.md#camera)> | Promise对象，返回相机对象。 |

**示例：**

```
1. import { SceneNodeParameters, Camera, SceneResourceFactory, Scene } from '@kit.ArkGraphics3D';

3. function createCameraPromise(): Promise<Camera> {
4. return new Promise((resolve, reject) => {
5. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
6. let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
7. scene.then(async (result: Scene) => {
8. let sceneFactory: SceneResourceFactory = result.getResourceFactory();
9. let sceneCameraParameter: SceneNodeParameters = { name: "camera1" };
10. // 创建相机
11. let camera: Camera = await sceneFactory.createCamera(sceneCameraParameter);
12. resolve(camera);
13. }).catch((error: Error) => {
14. console.error('Scene load failed:', error);
15. reject(error);
16. });
17. });
18. }
```

### createCamera21+

PhonePC/2in1TabletTVWearable

createCamera(params: SceneNodeParameters, cameraParams: CameraParameters): Promise<Camera>

根据节点参数与相机参数创建相机，使用Promise异步回调。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [SceneNodeParameters](js-apis-inner-scene.md#scenenodeparameters) | 是 | 场景节点参数。 |
| cameraParams | [CameraParameters](js-apis-inner-scene.md#cameraparameters21) | 是 | 相机参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Camera](js-apis-inner-scene-nodes.md#camera)> | Promise对象，返回相机对象。 |

**示例：**

```
1. import { SceneNodeParameters, Camera, SceneResourceFactory, Scene, CameraParameters,
2. RenderingPipelineType } from '@kit.ArkGraphics3D';

4. function createCameraPromise(): Promise<Camera> {
5. return new Promise((resolve, reject) => {
6. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
7. let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
8. scene.then(async (result: Scene) => {
9. let sceneFactory: SceneResourceFactory = result.getResourceFactory();
10. let nodeParameter: SceneNodeParameters = { name: "camera1" };
11. let camParameter: CameraParameters = {renderingPipeline: RenderingPipelineType.FORWARD};
12. // 创建相机
13. let camera: Camera = await sceneFactory.createCamera(nodeParameter, camParameter);
14. resolve(camera);
15. }).catch((error: Error) => {
16. console.error('Scene load failed:', error);
17. reject(error);
18. });
19. });
20. }
```

### createLight

PhonePC/2in1TabletTVWearable

createLight(params: SceneNodeParameters, lightType: LightType): Promise<Light>

根据节点参数和灯光类型创建灯光，使用Promise异步回调。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [SceneNodeParameters](js-apis-inner-scene.md#scenenodeparameters) | 是 | 场景节点参数。 |
| lightType | [LightType](js-apis-inner-scene-nodes.md#lighttype) | 是 | 灯光类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Light](js-apis-inner-scene-nodes.md#light)> | Promise对象，返回灯光对象。 |

**示例：**

```
1. import { SceneNodeParameters, LightType, Light, SceneResourceFactory, Scene } from '@kit.ArkGraphics3D';

3. function createLightPromise() : Promise<Light> {
4. return new Promise((resolve, reject) => {
5. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
6. let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
7. scene.then(async (result: Scene) => {
8. let sceneFactory: SceneResourceFactory = result.getResourceFactory();
9. let sceneLightParameter: SceneNodeParameters = { name: "light" };
10. // 创建平行光
11. let light: Light = await sceneFactory.createLight(sceneLightParameter, LightType.DIRECTIONAL);
12. resolve(light);
13. }).catch((error: Error) => {
14. console.error('Scene load failed:', error);
15. reject(error);
16. });
17. });
18. }
```

### createNode

PhonePC/2in1TabletTVWearable

createNode(params: SceneNodeParameters): Promise<Node>

创建节点，使用Promise异步回调。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [SceneNodeParameters](js-apis-inner-scene.md#scenenodeparameters) | 是 | 场景节点参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Node](js-apis-inner-scene-nodes.md#node)> | Promise对象，返回节点对象。 |

**示例：**

```
1. import { SceneNodeParameters, SceneResourceFactory, Scene, Node } from '@kit.ArkGraphics3D';

3. function createNodePromise(): Promise<Node> {
4. return new Promise((resolve, reject) => {
5. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
6. let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
7. scene.then(async (result: Scene) => {
8. let sceneFactory: SceneResourceFactory = result.getResourceFactory();
9. let sceneNodeParameter: SceneNodeParameters = { name: "empty_node",
10. path:"/rootNode_/empty_node" };
11. // 创建节点
12. let node: Node = await sceneFactory.createNode(sceneNodeParameter);
13. resolve(node);
14. }).catch((error: Error) => {
15. console.error('Scene load failed:', error);
16. reject(error);
17. });
18. });
19. }
```

### createMaterial

PhonePC/2in1TabletTVWearable

createMaterial(params: SceneResourceParameters, materialType: MaterialType): Promise<Material>

根据场景资源参数和材质类型创建材质，使用Promise异步回调。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [SceneResourceParameters](js-apis-inner-scene.md#sceneresourceparameters) | 是 | 场景资源参数。 |
| materialType | [MaterialType](js-apis-inner-scene-resources.md#materialtype) | 是 | 材质类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Material](js-apis-inner-scene-resources.md#material)> | Promise对象，返回材质对象。 |

**示例：**

```
1. import { MaterialType, Material, SceneResourceParameters, SceneResourceFactory, Scene } from '@kit.ArkGraphics3D';

3. function createMaterialPromise() : Promise<Material> {
4. return new Promise((resolve, reject) => {
5. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
6. let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
7. scene.then(async (result: Scene) => {
8. let sceneFactory: SceneResourceFactory = result.getResourceFactory();
9. let sceneMaterialParameter: SceneResourceParameters = { name: "material" };
10. // 创建材质
11. let material: Material = await sceneFactory.createMaterial(sceneMaterialParameter, MaterialType.SHADER);
12. resolve(material);
13. }).catch((error: Error) => {
14. console.error('Scene load failed:', error);
15. reject(error);
16. });
17. });
18. }
```

### createEnvironment

PhonePC/2in1TabletTVWearable

createEnvironment(params: SceneResourceParameters): Promise<Environment>

根据场景资源参数创建环境，使用Promise异步回调。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [SceneResourceParameters](js-apis-inner-scene.md#sceneresourceparameters) | 是 | 场景资源参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Environment](js-apis-inner-scene-resources.md#environment)> | Promise对象，返回环境对象。 |

**示例：**

```
1. import { Environment, SceneResourceParameters, SceneResourceFactory, Scene } from '@kit.ArkGraphics3D';

3. function createEnvironmentPromise(): Promise<Environment> {
4. return new Promise((resolve, reject) => {
5. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
6. let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
7. scene.then(async (result: Scene) => {
8. let sceneFactory: SceneResourceFactory = result.getResourceFactory();
9. // 加载环境贴图资源，路径和文件名可根据项目实际资源自定义
10. let sceneEnvironmentParameter: SceneResourceParameters = { name: "env", uri: $rawfile("KTX/quarry_02_2k_radiance.ktx") };
11. // 创建Environment
12. let env: Environment = await sceneFactory.createEnvironment(sceneEnvironmentParameter);
13. resolve(env);
14. }).catch((error: Error) => {
15. console.error('Scene load failed:', error);
16. reject(error);
17. });
18. });
19. }
```

### createGeometry18+

PhonePC/2in1TabletTVWearable

createGeometry(params: SceneNodeParameters, mesh:MeshResource): Promise<Geometry>

根据场景节点参数和网格数据创建几何对象，使用Promise异步回调。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [SceneNodeParameters](js-apis-inner-scene.md#scenenodeparameters) | 是 | 场景节点参数。 |
| mesh | [MeshResource](js-apis-inner-scene-resources.md#meshresource18) | 是 | 网格数据参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Geometry](js-apis-inner-scene-nodes.md#geometry)> | Promise对象，返回几何对象。 |

**示例：**

```
1. import { SceneResourceFactory, Scene, Geometry, CubeGeometry } from '@kit.ArkGraphics3D';

3. function createGeometryPromise() : Promise<Geometry> {
4. return new Promise((resolve, reject) => {
5. let scene: Promise<Scene> = Scene.load();
6. scene.then(async (result: Scene | undefined) => {
7. if (!result) {
8. return;
9. }
10. let sceneFactory: SceneResourceFactory = result.getResourceFactory();
11. // 创建立方体几何数据
12. let cubeGeom = new CubeGeometry();
13. cubeGeom.size = { x: 1, y: 1, z: 1 };
14. // 根据立方体几何数据创建网格资源
15. let meshRes = await sceneFactory.createMesh({ name: "MeshName" }, cubeGeom);
16. console.info("TEST createGeometryPromise");
17. // 根据场景节点参数和网格资源创建几何对象
18. let geometry: Geometry = await sceneFactory.createGeometry({ name: "GeometryName" }, meshRes);
19. resolve(geometry);
20. }).catch((error: Error) => {
21. console.error('Scene load failed:', error);
22. reject(error);
23. });
24. });
25. }
```

### createEffect21+

PhonePC/2in1TabletTVWearable

createEffect(params: EffectParameters): Promise<Effect>

根据特效参数创建特效对象，使用Promise异步回调。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [EffectParameters](js-apis-inner-scene.md#effectparameters21) | 是 | 特效参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Effect](js-apis-inner-scene-resources.md#effect21)> | Promise对象，返回特效对象。 |

**示例：**

```
1. import { SceneResourceFactory, Scene, Effect, EffectParameters } from '@kit.ArkGraphics3D';

3. function createEffect() : Promise<Effect> {
4. return new Promise((resolve, reject) => {
5. let scene: Promise<Scene> = Scene.load();
6. scene.then(async (result: Scene | undefined) => {
7. if (!result) {
8. return;
9. }
10. let sceneFactory: SceneResourceFactory = result.getResourceFactory();
11. // 特效ID，固定格式为'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'，比如'e68a7f45-2d21-4a0d-9aef-7d9c825d3f12'
12. let params: EffectParameters = {effectId: "e68a7f45-2d21-4a0d-9aef-7d9c825d3f12"}
13. let effect: Effect = await sceneFactory.createEffect(params);
14. resolve(effect);
15. }).catch((error: Error) => {
16. console.error('Scene load failed:', error);
17. reject(error);
18. });
19. });
20. }
```

## SceneComponent20+

PhonePC/2in1TabletTVWearable

表示基础场景组件，用于描述场景节点的组件信息，包括组件名称及其对应的属性集合。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 要创建场景组件的名称，可由开发者自定填写，用于标识场景组件。 |
| property | Record<string, string | number | [Vec2](js-apis-inner-scene-types.md#vec2) | [Vec3](js-apis-inner-scene-types.md#vec3) | [Vec4](js-apis-inner-scene-types.md#vec4) | [SceneResource](js-apis-inner-scene-resources.md#sceneresource-1) | boolean | number[] | string[] | [SceneResource](js-apis-inner-scene-resources.md#sceneresource-1)[] | [Vec2](js-apis-inner-scene-types.md#vec2)[] | [Vec3](js-apis-inner-scene-types.md#vec3)[] | [Vec4](js-apis-inner-scene-types.md#vec4)[] | null | undefined> | 是 | 否 | 组件的属性集合，以键值对形式存储。支持多种基础类型和复杂类型，用于描述场景组件的各种属性，单位及取值范围取决于具体场景组件。 |

## RenderContext20+

PhonePC/2in1TabletTVWearable

定义了所有渲染资源的上下文。在同一渲染上下文中创建的多个场景之间，可以共享渲染资源。

### getRenderResourceFactory20+

PhonePC/2in1TabletTVWearable

getRenderResourceFactory() : RenderResourceFactory

获取渲染资源工厂，提供创建不同渲染资源的功能。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RenderResourceFactory](js-apis-inner-scene.md#renderresourcefactory20) | 返回一个RenderResourceFactory实例，用于创建渲染资源。 |

**示例：**

```
1. import { Scene, RenderContext, RenderResourceFactory } from '@kit.ArkGraphics3D';

3. function getRenderResourceFactory(): void {
4. const renderContext: RenderContext | null = Scene.getDefaultRenderContext();
5. if (!renderContext) {
6. console.error("RenderContext is null");
7. return;
8. }
9. const renderResourceFactory: RenderResourceFactory = renderContext.getRenderResourceFactory();
10. console.info("TEST getRenderResourceFactory");
11. }
```

### loadPlugin20+

PhonePC/2in1TabletTVWearable

loadPlugin(name: string): Promise<boolean>

用于加载指定名称的插件，通过插件名称查找并加载对应的插件资源，使用Promise异步回调。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 要加载的插件名称，必须是系统预定义或已注册且可用的插件名称，且符合命名规范。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | 返回一个Promise对象，解析结果为boolean类型，表示插件加载是否成功。true表示加载成功，false表示加载失败。 |

**示例：**

```
1. import { Scene, RenderContext } from '@kit.ArkGraphics3D';

3. function loadPlugin(): Promise<boolean> {
4. const renderContext: RenderContext | null = Scene.getDefaultRenderContext();
5. if (!renderContext) {
6. console.error("RenderContext is null");
7. return Promise.reject(new Error("RenderContext is null"));
8. }
9. return renderContext.loadPlugin("pluginName");
10. }
```

### registerResourcePath20+

PhonePC/2in1TabletTVWearable

registerResourcePath(protocol: string, uri: string): boolean

注册shader等资产文件所在的路径目录及其检索名，通过检索名查找并替换shader内部关联文件的路径描述，找到对应的资产路径目录，实现资产及其关联文件的正确加载。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| protocol | string | 是 | 要注册的路径检索名，用作shader内部关联文件路径的前缀标识，必须是系统未预定义或未注册且非空的检索名称。 |
| uri | string | 是 | 要注册的资产路径目录，与检索名对应，shader加载时会将路径中的检索名前缀替换为该目录，必须是资产文件所在文件夹路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回资产文件路径是否注册成功。true表示注册成功；false表示注册失败，可能原因为检索名已被注册或输入参数不可用。 |

**示例：**

```
1. import { Scene, RenderContext } from '@kit.ArkGraphics3D';

3. function registerResourcePath(): void {
4. // 创建shader资源，路径和文件名可根据项目实际资源自定义
5. Scene.load($rawfile("shaders/custom_shader/custom_material_sample.shader"))
6. .then(() => {
7. const renderContext: RenderContext | null = Scene.getDefaultRenderContext();
8. if (!renderContext) {
9. console.error("RenderContext is null");
10. return false;
11. }
12. // 注册路径检索名"myproto"及其对应的资产路径目录"OhosRawFile://shaders/custom_shader/"
13. // 当shader内部通过检索名引用关联文件，如路径为"myproto://textures/base.png"，
14. // 系统会将"myproto://"替换为"OhosRawFile://shaders/custom_shader/"，
15. // 最终从"OhosRawFile://shaders/custom_shader/textures/base.png"加载关联文件
16. return renderContext.registerResourcePath("myproto", "OhosRawFile://shaders/custom_shader/");
17. })
18. .then(result => {
19. if (result) {
20. console.info("resource path registration success");
21. } else {
22. console.error("resource path registration failed");
23. }
24. });
25. }
```

## RenderConfiguration23+

PhonePC/2in1TabletTVWearable

渲染配置接口。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| shadowResolution | [Vec2](js-apis-inner-scene-types.md#vec2) | 否 | 是 | 表示全局阴影贴图分辨率，单位为像素（px）。默认值为undefined，表示阴影贴图分辨率设置为1024 \* 1024。输入的值需要大于0才能正确生效。如果输入值为浮点数则自动截取整数部分；如果输入值小于或等于0则无视该输入，维持原有配置。 |

## RenderParameters15+

PhonePC/2in1TabletTVWearable

渲染参数接口。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| alwaysRender15+ | boolean | 否 | 是 | 表示是否每一帧都渲染。true表示每一帧都渲染，false表示按需渲染。默认值为true。 |

## Scene

PhonePC/2in1TabletTVWearable

用于设置场景。

### 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| environment | [Environment](js-apis-inner-scene-resources.md#environment) | 否 | 否 | 环境对象。 |
| animations | [Animation](js-apis-inner-scene-resources.md#animation)[] | 是 | 否 | 动画数组，用于保存3D场景中的动画对象。 |
| root | [Node](js-apis-inner-scene-nodes.md#node) | null | 是 | 否 | 3D场景树根节点。 |
| renderConfiguration23+ | [RenderConfiguration](js-apis-inner-scene.md#renderconfiguration23) | 是 | 否 | 渲染配置接口。 |

### load

PhonePC/2in1TabletTVWearable

static load(uri?: ResourceStr): Promise<Scene>

通过传入的资源路径加载资源，使用Promise异步回调。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | [ResourceStr](ts-types.md#resourcestr) | 否 | 待加载的模型文件资源路径，默认值为undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Scene](js-apis-inner-scene.md#scene-1)> | Promise对象，返回场景对象。 |

**示例：**

示例1：通过rawfile加载（相对路径）

```
1. import { Scene } from '@kit.ArkGraphics3D';

3. function loadModel(): void {
4. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
5. let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
6. scene.then((result: Scene) => {
7. console.info("Scene loaded, root node: " + result.root?.name);
8. });
9. }
```

示例2：通过绝对路径加载（从应用沙盒目录/data/storage/el2/base/files加载模型）

```
1. import { common } from '@kit.AbilityKit';
2. import { fileIo } from '@kit.CoreFileKit';
3. import { Scene } from '@kit.ArkGraphics3D';

5. async function loadModelFromAbsolutePath(context: common.UIAbilityContext): Promise<void> {
6. // 获取应用沙盒目录（Scene.load仅能读取应用自身写入的文件，不能读取hdc/adb push写入的文件）
7. const appCtx = context.getApplicationContext();
8. const filesDir = appCtx.filesDir; // /data/storage/el2/base/files

10. // 从rawfile读取模型内容（实际使用中也可以替换为其他来源的数据）
11. // 使用.glb文件更易于复制加载；若为.gltf，请将其.bin和贴图文件一并复制到同一目录
12. const src = 'gltf/CubeWithFloor/glTF/AnimatedCube.glb';
13. const load_uri = `${filesDir}/AnimatedCube.glb`;

15. // 写入模型文件到应用沙盒目录，生成可被Scene.load(绝对路径)访问的实际文件
16. const rawData = await context.resourceManager.getRawFileContent(src);
17. const file = fileIo.openSync(load_uri, fileIo.OpenMode.CREATE | fileIo.OpenMode.TRUNC | fileIo.OpenMode.WRITE_ONLY);
18. fileIo.writeSync(file.fd, rawData.buffer.slice(rawData.byteOffset, rawData.byteOffset + rawData.byteLength));
19. fileIo.closeSync(file);

21. // 使用绝对路径加载模型
22. Scene.load(load_uri).then((scene: Scene) => {
23. // 加载成功后的逻辑处理
24. }).catch((error: string) => {
25. console.error('Scene load failed: ' + error);
26. });
27. }
```

### getNodeByPath

PhonePC/2in1TabletTVWearable

getNodeByPath(path: string, type?: NodeType): Node | null

通过路径获取节点。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 场景节点层次中的路径。每层之间使用'/'符号进行分割。 |
| type | [NodeType](js-apis-inner-scene-nodes.md#nodetype) | 否 | 预期返回的节点类型。默认值为空。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Node](js-apis-inner-scene-nodes.md#node) | null | 返回请求节点的实例，如果没有找到或者找到的节点类型与传入的参数不相符则返回空。 |

**示例：**

```
1. import { Scene, Node } from '@kit.ArkGraphics3D';

3. function getNode(): void {
4. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
5. let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
6. scene.then(async (result: Scene) => {
7. if (result) {
8. // 寻找指定路径的节点
9. let node : Node | null = result.getNodeByPath("rootNode_");
10. }
11. });
12. }
```

### getResourceFactory

PhonePC/2in1TabletTVWearable

getResourceFactory(): SceneResourceFactory

获取场景资源工厂对象。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SceneResourceFactory](js-apis-inner-scene.md#sceneresourcefactory) | 返回场景资源工厂对象。 |

**示例：**

```
1. import { SceneResourceFactory, Scene } from '@kit.ArkGraphics3D';

3. function getFactory(): void {
4. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
5. let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
6. scene.then(async (result: Scene) => {
7. if (result) {
8. // 获得SceneResourceFactory对象
9. let sceneFactory: SceneResourceFactory = result.getResourceFactory();
10. }
11. });
12. }
```

### destroy

PhonePC/2in1TabletTVWearable

destroy(): void

销毁场景，释放所有的场景资源。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**示例：**

```
1. import { Scene } from '@kit.ArkGraphics3D';

3. function destroy(): void {
4. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
5. let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
6. scene.then(async (result: Scene) => {
7. if (result) {
8. // 销毁scene
9. result.destroy();
10. }
11. });
12. }
```

### importNode18+

PhonePC/2in1TabletTVWearable

importNode(name: string, node: Node, parent: Node | null): Node

一般用于从其他场景导入节点。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 导入节点后的名称，由开发者自定义，无特殊要求。 |
| node | [Node](js-apis-inner-scene-nodes.md#node) | 是 | 被导入的节点。 |
| parent | [Node](js-apis-inner-scene-nodes.md#node) | null | 是 | 被导入节点在新场景中的父节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Node](js-apis-inner-scene-nodes.md#node) | 被导入的节点。 |

**示例：**

```
1. import { Scene } from '@kit.ArkGraphics3D';

3. function ImportNodeTest() {
4. Scene.load().then(async (result: Scene | undefined) => {
5. if (!result) {
6. return;
7. }
8. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
9. Scene.load($rawfile("gltf/AnimatedCube/glTF/AnimatedCube.glb"))
10. .then(async (extScene: Scene) => {
11. let extNode = extScene.getNodeByPath("rootNode_/Unnamed Node 1/AnimatedCube");
12. console.info("TEST ImportNodeTest");
13. let node = result.importNode("scene", extNode, result.root);
14. if (node) {
15. node.position.x = 5;
16. }
17. });
18. });
19. }
```

### importScene18+

PhonePC/2in1TabletTVWearable

importScene(name: string, scene: Scene, parent: Node | null): Node

在当前场景中导入其他场景。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 导入场景的根节点名称，由开发者自定义，无特殊要求。 |
| scene | [Scene](js-apis-inner-scene.md#scene-1) | 是 | 被导入的场景。 |
| parent | [Node](js-apis-inner-scene-nodes.md#node) | null | 是 | 被导入场景在新场景中的父节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Node](js-apis-inner-scene-nodes.md#node) | 被导入场景的根节点。 |

**示例：**

```
1. import { Scene } from '@kit.ArkGraphics3D';

3. function ImportSceneTest() {
4. Scene.load().then(async (result: Scene | undefined) => {
5. if (!result) {
6. return;
7. }
8. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
9. let content = await result.getResourceFactory().createScene($rawfile("gltf/DamagedHelmet/glTF/DamagedHelmet.glb"))
10. console.info("TEST ImportSceneTest");
11. result.importScene("helmet", content, null);
12. });
13. }
```

### renderFrame15+

PhonePC/2in1TabletTVWearable

renderFrame(params?: RenderParameters): boolean

通过该接口可以实现按需渲染，例如控制渲染帧率。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [RenderParameters](js-apis-inner-scene.md#renderparameters15) | 否 | 渲染参数，默认值为undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 渲染被成功调度返回true，否则返回false。 |

**示例：**

```
1. import { Scene } from '@kit.ArkGraphics3D';

3. function RenderFrameTest() {
4. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
5. Scene.load($rawfile("gltf/DamagedHelmet/glTF/DamagedHelmet.glb"))
6. .then(async (result: Scene | undefined) => {
7. if (!result) {
8. return;
9. }
10. console.info("TEST RenderFrameTest");
11. result.renderFrame({ alwaysRender: true });
12. });
13. }
```

### createComponent20+

PhonePC/2in1TabletTVWearable

createComponent(node: Node, name: string): Promise<SceneComponent>

在指定节点上创建新的组件，根据组件名称异步创建并附加到节点上，使用Promise异步回调。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [Node](js-apis-inner-scene-nodes.md#node) | 是 | 组件需要附加到的节点。 |
| name | string | 是 | 要创建的组件名称，由各插件定义有效名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SceneComponent](js-apis-inner-scene.md#scenecomponent20)> | Promise对象，返回新创建的场景组件。 |

**示例：**

```
1. import { Scene, SceneComponent } from '@kit.ArkGraphics3D';

3. function createComponentTest(): Promise<SceneComponent> {
4. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
5. return Scene.load($rawfile("gltf/DamagedHelmet/glTF/DamagedHelmet.glb"))
6. .then(scene => {
7. if (!scene) {
8. return Promise.reject(new Error("Scene load failed"));
9. }
10. // RenderConfigurationComponent为引擎内置组件，创建时无需依赖插件
11. return scene.createComponent(scene.root, "RenderConfigurationComponent");
12. })
13. .then(component => {
14. if (!component) {
15. return Promise.reject(new Error("createComponent failed"));
16. }
17. return component;
18. });
19. }
```

### getComponent20+

PhonePC/2in1TabletTVWearable

getComponent(node: Node, name: string): SceneComponent | null

根据指定的组件名称，从给定节点上获取对应的组件实例。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [Node](js-apis-inner-scene-nodes.md#node) | 是 | 组件附加的节点。 |
| name | string | 是 | 需要获取的组件名称，必须为系统预定义或已注册的自定义组件名称，且需符合命名规范。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SceneComponent](js-apis-inner-scene.md#scenecomponent20) | null | 返回对应名称的组件对象，若未找到则返回null。 |

**示例：**

```
1. import { Scene } from '@kit.ArkGraphics3D';

3. function getComponentTest() {
4. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
5. Scene.load($rawfile("gltf/DamagedHelmet/glTF/DamagedHelmet.glb"))
6. .then(async (result: Scene | undefined) => {
7. if (!result) {
8. console.error("Scene load failed");
9. return;
10. }
11. console.info("TEST getComponentTest");
12. let component = result.getComponent(result.root, "myComponent");
13. if (component) {
14. console.info("getComponent success");
15. } else {
16. console.warn("Component not found");
17. }
18. });
19. }
```

### getDefaultRenderContext20+

PhonePC/2in1TabletTVWearable

static getDefaultRenderContext(): RenderContext | null

获取当前图形对象所关联的渲染环境信息。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RenderContext](js-apis-inner-scene.md#rendercontext20) | null | 返回当前对象关联的渲染上下文，若对象尚未关联任何渲染上下文，则返回null。 |

**示例：**

```
1. import { Scene, RenderContext } from '@kit.ArkGraphics3D';

3. function getDefaultRenderContextTest() {
4. console.info("TEST getDefaultRenderContextTest");
5. const renderContext: RenderContext | null = Scene.getDefaultRenderContext();
6. if (renderContext) {
7. console.info("getDefaultRenderContext success");
8. } else {
9. console.error("RenderContext is null");
10. }
11. }
```

### cloneNode23+

PhonePC/2in1TabletTVWearable

cloneNode(node: Node, parent: Node, name: string): Node | null

在当前所在场景中克隆节点，不支持跨场景克隆节点。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [Node](js-apis-inner-scene-nodes.md#node) | 是 | 被克隆的节点。 |
| parent | [Node](js-apis-inner-scene-nodes.md#node) | 是 | 被克隆的节点在当前所在场景中的目标父节点。被克隆的节点node和目标父节点parent需要属于同一个场景scene。 |
| name | string | 是 | 克隆节点的名称，由开发者自定义，无特殊要求。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Node](js-apis-inner-scene-nodes.md#node) | null | 返回克隆节点。克隆失败则返回null。 |

**示例：**

```
1. import { Scene, Node } from '@kit.ArkGraphics3D';

3. function CloneNode() {
4. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
5. Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.gltf"))
6. .then(async (result: Scene) => {
7. let node = result.getNodeByPath("rootNode_/Unnamed Node 1/AnimatedCube") as Node;
8. let parent = result.root as Node;
9. let name = "cloneNode_";
10. let clone = result.cloneNode(node, parent, name);
11. if (clone) {
12. console.info("cloneNode success");
13. } else {
14. console.error("cloneNode failed");
15. }
16. });
17. }
```
