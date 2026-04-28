---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene-nodes
title: SceneNode
breadcrumb: API参考 > 图形 > ArkGraphics 3D（方舟3D图形） > ArkTS API > graphics3d > SceneNode
category: harmonyos-references
scraped_at: 2026-04-28T08:15:37+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:0a749b83685dd8e25bdb4f8dc613c903903510475c476c36caa8a416a1ac198c
---

本模块提供3D图形中场景资源节点的类型及操作方法。SceneNode是3D场景的基础构建单元，它允许开发者通过层级结构管理场景中的对象，实现高效的场景组织与交互控制。

说明

本模块首批接口从API version 12开始支持，后续版本的新增接口，采用上角标标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { LayerMask, NodeType, Container, Node, Geometry, LightType, Light, SpotLight, DirectionalLight,
2. Camera } from '@kit.ArkGraphics3D';
```

## LayerMask

PhonePC/2in1TabletTVWearable

用于定义节点的图层掩码。

### getEnabled

PhonePC/2in1TabletTVWearable

getEnabled(index: number): boolean

获取指定图层下标图层掩码的使能状态。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 要使能图层的下标，值域为大于等于0的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回特定下标的图层是否使能。true表示使用图层掩码，false表示不使用。 |

**示例：**

```
1. import { Scene, Node } from '@kit.ArkGraphics3D';

3. function layerMask(): void {
4. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
5. let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
6. scene.then(async (result: Scene) => {
7. if (result) {
8. let node : Node | null = result.getNodeByPath("rootNode_");
9. if (node) {
10. // 获取掩码的使能状态，可根据业务需求对返回值进行后续处理
11. let enabled: boolean = node.layerMask.getEnabled(1);
12. }
13. }
14. }).catch((error: Error) => {
15. console.error('Scene load failed:', error);
16. });
17. }
```

### setEnabled

PhonePC/2in1TabletTVWearable

setEnabled(index: number, enabled: boolean): void

将特定下标的图层掩码使能。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 要使能图层的下标，值域为大于等于0的整数。 |
| enabled | boolean | 是 | 要设置的使能状态。true表示使用图层掩码，false表示不使用。 |

**示例：**

```
1. import { Scene, Node } from '@kit.ArkGraphics3D';

3. function layerMask(): void {
4. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
5. let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
6. scene.then(async (result: Scene) => {
7. if (result) {
8. let node : Node | null = result.getNodeByPath("rootNode/Scene/");
9. if (node) {
10. // 设置掩码状态
11. node.layerMask.setEnabled(1, true);
12. }
13. }
14. }).catch((error: Error) => {
15. console.error('Scene load failed:', error);
16. });
17. }
```

## NodeType

PhonePC/2in1TabletTVWearable

节点类型枚举。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NODE | 1 | 节点是空节点。 |
| GEOMETRY | 2 | 几何类型节点。 |
| CAMERA | 3 | 相机类型节点。 |
| LIGHT | 4 | 灯光类型节点。 |
| CUSTOM21+ | 255 | 自定义类型节点，通常这意味着该节点是在扩展插件中定义的类型。 |

## Container<T>

PhonePC/2in1TabletTVWearable

定义场景对象的容器。容器提供了一种将场景对象分组到层次结构中的方法。

### append

PhonePC/2in1TabletTVWearable

append(item: T): void

追加一个对象到容器。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| item | T | 是 | T类型对象。 |

**示例：**

```
1. import { Scene, Node } from '@kit.ArkGraphics3D';

3. function append(): void {
4. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
5. let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
6. scene.then(async (result: Scene) => {
7. if (result) {
8. let node : Node | null = result.getNodeByPath("rootNode/Scene/");
9. if (node) {
10. // append 节点，如果node已经在children中，数量不会增加，但操作仍然生效
11. result.root?.children.get(0)?.children.append(node);
12. }
13. }
14. }).catch((error: Error) => {
15. console.error('Scene load failed:', error);
16. });
17. }
```

### insertAfter

PhonePC/2in1TabletTVWearable

insertAfter(item: T, sibling: T | null): void

在兄弟节点后面插入对象。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| item | T | 是 | 要插入节点。 |
| sibling | T | null | 是 | 兄弟节点。 |

**示例：**

```
1. import { Scene, Node } from '@kit.ArkGraphics3D';

3. function insertAfter(): void {
4. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
5. let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
6. scene.then(async (result: Scene) => {
7. if (result) {
8. let node : Node | null = result.getNodeByPath("rootNode/Scene/");
9. if (node) {
10. // insertAfter 节点，如果node已经在children中，数量不会增加，但操作仍然生效
11. result.root?.children.get(0)?.children.insertAfter(node, null);
12. }
13. }
14. }).catch((error: Error) => {
15. console.error('Scene load failed:', error);
16. });
17. }
```

### remove

PhonePC/2in1TabletTVWearable

remove(item: T): void

移除指定对象。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| item | T | 是 | 要移除的对象。 |

**示例：**

```
1. import { Scene, Node } from '@kit.ArkGraphics3D';

3. function remove(): void {
4. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
5. let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
6. scene.then(async (result: Scene) => {
7. if (result) {
8. let node : Node | null = result.getNodeByPath("rootNode/Scene/");
9. if (node) {
10. // remove 节点
11. result.root?.children.remove(node);
12. }
13. }
14. }).catch((error: Error) => {
15. console.error('Scene load failed:', error);
16. });
17. }
```

### get

PhonePC/2in1TabletTVWearable

get(index: number): T | null

获取特定下标对象，获取不到则返回空。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 要获取对象的下标，取值范围是大于等于0的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | null | 返回获取到的对象，获取不到则返回空值。 |

**示例：**

```
1. import { Scene, Node } from '@kit.ArkGraphics3D';

3. function get(): void {
4. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
5. let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
6. scene.then(async (result: Scene) => {
7. if (result) {
8. let node : Node | null = result.getNodeByPath("rootNode/Scene/");
9. // 从children中get 0号节点
10. result.root?.children.get(0)?.children.insertAfter(node, null);
11. }
12. }).catch((error: Error) => {
13. console.error('Scene load failed:', error);
14. });
15. }
```

### clear

PhonePC/2in1TabletTVWearable

clear(): void

清空容器内的所有对象。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**示例：**

```
1. import { Scene, Node } from '@kit.ArkGraphics3D';

3. function clear(): void {
4. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
5. let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
6. scene.then(async (result: Scene) => {
7. if (result) {
8. let node : Node | null = result.getNodeByPath("rootNode/Scene/");
9. if (node) {
10. // 清空 node 节点下的所有子节点
11. node.children.clear();
12. }
13. }
14. }).catch((error: Error) => {
15. console.error('Scene load failed:', error);
16. });
17. }
```

### count

PhonePC/2in1TabletTVWearable

count(): number

获取容器中对象的数量。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回容器中对象个数，取值范围是非负整数。 |

**示例：**

```
1. import { Container, Scene, Node } from '@kit.ArkGraphics3D';

3. function count(): void {
4. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
5. let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
6. scene.then(async (result: Scene) => {
7. if (result) {
8. let node : Node | null = result.getNodeByPath("rootNode_");
9. if (node) {
10. let container: Container<Node> = node.children;
11. // 获取children中的节点数
12. let count: number = container.count();
13. }
14. }
15. });
16. }
```

## Node

PhonePC/2in1TabletTVWearable

3D场景由树状层次结构的节点组成，其中每个节点都实现了Node接口。继承自[SceneResource](js-apis-inner-scene-resources.md#sceneresource-1)。

### 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| position | [Position3](js-apis-inner-scene-types.md#position3) | 否 | 否 | 节点位置，单位为世界坐标系下的场景单位（比如cm、m、km等）。 |
| rotation | [Quaternion](js-apis-inner-scene-types.md#quaternion) | 否 | 否 | 节点旋转角度。 |
| scale | [Scale3](js-apis-inner-scene-types.md#scale3) | 否 | 否 | 节点缩放。 |
| visible | boolean | 否 | 否 | 节点是否可见。true表示该节点可见，false表示不可见。 |
| nodeType | [NodeType](js-apis-inner-scene-nodes.md#nodetype) | 是 | 否 | 节点类型。 |
| layerMask | [LayerMask](js-apis-inner-scene-nodes.md#layermask) | 是 | 否 | 节点的图层掩码。 |
| path | string | 是 | 否 | 节点路径。 |
| parent | [Node](js-apis-inner-scene-nodes.md#node) | null | 是 | 否 | 节点的父节点，不存在则为空值。 |
| children | [Container](js-apis-inner-scene-nodes.md#containert)<[Node](js-apis-inner-scene-nodes.md#node)> | 是 | 否 | 节点的子节点，不存在则为空值。为只读属性，表示不能替换整个children容器，但可以通过容器方法操作子节点（如[append()](js-apis-inner-scene-nodes.md#append)、[insertAfter()](js-apis-inner-scene-nodes.md#insertafter)、[remove()](js-apis-inner-scene-nodes.md#remove)或[clear()](js-apis-inner-scene-nodes.md#clear)）。如果append或insertAfter的节点已存在于容器中，容器会先移除该节点再插入，因此数量不会增加，看似“无效”；添加新节点才会真正增加子节点数量。 |

### getNodeByPath

PhonePC/2in1TabletTVWearable

getNodeByPath(path: string): Node | null

根据路径获取节点，如果获取不到则返回空。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 场景节点层次中的路径。每层之间使用'/'符号进行分割。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Node](js-apis-inner-scene-nodes.md#node) | null | 返回节点对象。 |

**示例：**

```
1. import { Scene, Node } from '@kit.ArkGraphics3D';

3. function getNode(): void {
4. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
5. let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
6. scene.then(async (result: Scene) => {
7. if (result && result.root) {
8. // 查找节点
9. let geo : Node | null = result.root.getNodeByPath("scene/node");
10. }
11. });
12. }
```

## Geometry

PhonePC/2in1TabletTVWearable

几何节点类型，用于承载可渲染的网格数据，并支持可选的形变功能，继承自[Node](js-apis-inner-scene-nodes.md#node)。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| mesh | [Mesh](js-apis-inner-scene-resources.md#mesh) | 是 | 否 | 网格属性。 |
| morpher20+ | [Morpher](js-apis-inner-scene-resources.md#morpher20) | 是 | 是 | 可选的形变器，用于为几何体添加基于顶点的形变或动画效果。若未设置，则该几何体不支持形变功能。 |

## LightType

PhonePC/2in1TabletTVWearable

光源类型枚举。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DIRECTIONAL | 1 | 平行光类型。 |
| SPOT | 2 | 点光源类型。 |

## Light

PhonePC/2in1TabletTVWearable

光源，继承自[Node](js-apis-inner-scene-nodes.md#node)。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| lightType | [LightType](js-apis-inner-scene-nodes.md#lighttype) | 是 | 否 | 光源类型。 |
| color | [Color](js-apis-inner-scene-types.md#color) | 否 | 否 | 颜色。 |
| intensity | number | 否 | 否 | 光照密度，单位为坎德拉（cd），取值范围是大于0的实数。 |
| shadowEnabled | boolean | 否 | 否 | 是否使能阴影。true表示添加阴影，false表示没有阴影效果。 |
| enabled | boolean | 否 | 否 | 是否使能光源。true表示使用光源，false表示不使用。 |

## SpotLight

PhonePC/2in1TabletTVWearable

聚光灯类型，继承自[Light](js-apis-inner-scene-nodes.md#light)。

聚光灯会朝某个方向发出锥形光，强度随着圆锥角度的衰减由innerAngle和outerAngle两个参数定义。另外与点光源类似，强度也会随着距离光源位置的增加而衰减。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| innerAngle23+ | number | 否 | 是 | 从聚光灯中心到开始衰减的角度，对应圆锥的半顶角，在这个圆锥体内光强不随角度衰减。单位为弧度（rad），默认值为0。设置的值必须大于等于0，小于等于outerAngle。 |
| outerAngle23+ | number | 否 | 是 | 从聚光灯中心到衰减结束的角度，对应圆锥的半顶角，在这个圆锥体外不再有光强度。单位为弧度（rad），默认值为PI/4。设置的值必须大于等于innerAngle，小于等于PI/2。 |

注意

用户需要保证设置的innerAngle与outerAngle值是合理的。当outerAngle设置的值大于PI/2时，内部会强制其等于PI/2。当outerAngle设置的值小于innerAngle时，内部会强制其等于innerAngle。

## DirectionalLight

PhonePC/2in1TabletTVWearable

平行光类型，继承自[Light](js-apis-inner-scene-nodes.md#light)。

**系统能力：** SystemCapability.ArkUi.Graphics3D

## Camera

PhonePC/2in1TabletTVWearable

相机类型，Camera继承自[Node](js-apis-inner-scene-nodes.md#node)。

### 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fov | number | 否 | 否 | 视场，单位为弧度（rad），取值在0到π弧度之间。 |
| nearPlane | number | 否 | 否 | 近平面，单位为世界坐标系下的场景单位（比如cm、m、km等），取值大于0。 |
| farPlane | number | 否 | 否 | 远平面，单位为世界坐标系下的场景单位（比如cm、m、km等），取值大于nearPlane。 |
| enabled | boolean | 否 | 否 | 是否使能相机。true表示使用相机，false表示不使用相机。 |
| postProcess | [PostProcessSettings](js-apis-inner-scene-post-process-settings.md#postprocesssettings) | null | 否 | 否 | 后处理设置。 |
| effects21+ | [Container](js-apis-inner-scene-nodes.md#containert)<[Effect](js-apis-inner-scene-resources.md#effect21)> | 是 | 否 | 应用于相机输出的后处理特效。 |
| clearColor | [Color](js-apis-inner-scene-types.md#color) | null | 否 | 否 | 将渲染目标（render target）清空后的特定颜色。 |
| msaa22+ | boolean | 否 | 是 | 控制MSAA是否使能。true表示使能MSAA，false表示不使能MSAA。若未设置，默认为false。 |
| renderingPipeline21+ | [RenderingPipelineType](js-apis-inner-scene-types.md#renderingpipelinetype21) | 否 | 是 | 控制渲染管线。若未设置，默认使用轻量级前向渲染管线。（如果选择了FORWARD\_LIGHTWEIGHT管线，某些功能将不可用。） |

### raycast20+

PhonePC/2in1TabletTVWearable

raycast(viewPosition: Vec2, params: RaycastParameters): Promise<RaycastResult[]>

从屏幕指定位置发射射线，检测并返回所有命中的3D物体信息。使用Promise异步回调。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| viewPosition | [Vec2](js-apis-inner-scene-types.md#vec2) | 是 | 使用屏幕归一化坐标，取值范围为[0, 1]。其中(0,0)表示Component3D控件的左上角，(1,1)表示Component3D控件的右下角。 |
| params | [RaycastParameters](js-apis-inner-scene.md#raycastparameters20) | 是 | 射线检测的配置参数（如检测范围、过滤节点等）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[RaycastResult](js-apis-inner-scene.md#raycastresult20)[]> | 返回命中的结果数组（按距离从近到远排序），若无命中则返回空数组。 |

**示例：**

```
1. import { SceneNodeParameters, Camera, SceneResourceFactory, Scene, Node, Vec2, Vec3, Quaternion,
2. RaycastParameters } from '@kit.ArkGraphics3D';

4. function Raycast(): void {
5. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
6. Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"))
7. .then(async (result: Scene) => {
8. if (!result.root) {
9. return;
10. }
11. let node: Node | null | undefined = result.root.getNodeByPath("rootNode_/Unnamed Node 1/AnimatedCube");
12. let sceneFactory: SceneResourceFactory = result.getResourceFactory();
13. let sceneCameraParameter: SceneNodeParameters = { name: "camera1" };
14. // 创建相机
15. let camera: Camera = await sceneFactory.createCamera(sceneCameraParameter);
16. camera.enabled = true;
17. // 设置相机视角
18. lookAt(camera, { x: 0, y: 0, z: -3 }, { x: 0, y: 0, z: 0 }, { x: 0, y: 1, z: 0 });

20. let viewPos: Vec2 = { x: 0.5, y: 0.5 };
21. let raycastParams: RaycastParameters = {};
22. if (node) {
23. raycastParams.rootNode = node;
24. }
25. return camera.raycast(viewPos, raycastParams);
26. });
27. }

29. // 向量减法，返回l - r的结果
30. function Sub(l: Vec3, r: Vec3): Vec3 {
31. return { x: l.x - r.x, y: l.y - r.y, z: l.z - r.z };
32. }
33. // 向量点积，返回l和r的内积
34. function Dot(l: Vec3, r: Vec3): number {
35. return l.x * r.x + l.y * r.y + r.z * l.z;
36. }
37. // 向量归一化，返回l的单位向量
38. function Normalize(l: Vec3): Vec3 {
39. let d = Math.sqrt(Dot(l, l));
40. return { x: l.x / d, y: l.y / d, z: l.z / d };
41. }
42. // 向量叉积，返回l和r的叉乘结果
43. function Cross(l: Vec3, r: Vec3): Vec3 {
44. return { x: (l.y * r.z - l.z * r.y), y: (l.z * r.x - l.x * r.z), z: (l.x * r.y - l.y * r.x) };
45. }
46. // 四元数标量乘法，返回四元数l乘以标量d的结果
47. function Mul(l: Quaternion, d: number): Quaternion {
48. return {
49. x: l.x * d,
50. y: l.y * d,
51. z: l.z * d,
52. w: l.w * d
53. };
54. }
55. // lookAt函数：将节点的位置和朝向设置为从eye位置看向center位置，up为上方向
56. function lookAt(node: Node, eye: Vec3, center: Vec3, up: Vec3) {

58. let t: number;

60. let q: Quaternion = {
61. x: 0.0,
62. y: 0.0,
63. z: 0.0,
64. w: 0.0
65. };
66. let f = Normalize(Sub(center, eye));
67. let m0 = Normalize(Cross(f, up));
68. let m1 = Cross(m0, f);
69. let m2: Vec3 = { x: -f.x, y: -f.y, z: -f.z };
70. if (m2.z < 0) {
71. if (m0.x > m1.y) {
72. t = 1.0 + m0.x - m1.y - m2.z;
73. q = {
74. x: t,
75. y: m0.y + m1.x,
76. z: m2.x + m0.z,
77. w: m1.z - m2.y
78. };
79. } else {
80. t = 1.0 - m0.x + m1.y - m2.z;
81. q = {
82. x: m0.y + m1.x,
83. y: t,
84. z: m1.z + m2.y,
85. w: m2.x - m0.z
86. };
87. }
88. } else {
89. if (m0.x < -m1.y) {
90. t = 1.0 - m0.x - m1.y + m2.z;
91. q = {
92. x: m2.x + m0.z,
93. y: m1.z + m2.y,
94. z: t,
95. w: m0.y - m1.x
96. };
97. } else {
98. t = 1.0 + m0.x + m1.y + m2.z;
99. q = {
100. x: m1.z - m2.y,
101. y: m2.x - m0.z,
102. z: m0.y - m1.x,
103. w: t
104. }
105. }
106. }
107. node.position = eye;
108. node.rotation = Mul(q, 0.5 / Math.sqrt(t));
109. }
```

### getViewMatrix23+

PhonePC/2in1TabletTVWearable

getViewMatrix(): Mat4x4

获取相机的视图矩阵。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Mat4x4](js-apis-inner-scene-types.md#mat4x423) | 返回相机的视图矩阵。 |

**示例：**

```
1. import { Scene, SceneResourceFactory, SceneNodeParameters, Camera, Mat4x4 } from '@kit.ArkGraphics3D';

3. function GetViewMatrix(): void {
4. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
5. Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"))
6. .then(async (result: Scene) => {
7. if (!result.root) {
8. return;
9. }
10. let sceneFactory: SceneResourceFactory = result.getResourceFactory();
11. let sceneCameraParameter: SceneNodeParameters = { name: "camera1" };
12. // 创建相机
13. let camera: Camera = await sceneFactory.createCamera(sceneCameraParameter);
14. camera.enabled = true;
15. // 获取相机的视图矩阵
16. let viewMatrix: Mat4x4 = camera.getViewMatrix();
17. });
18. }
```

### getProjectionMatrix23+

PhonePC/2in1TabletTVWearable

getProjectionMatrix(): Mat4x4

获取相机的投影矩阵。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Mat4x4](js-apis-inner-scene-types.md#mat4x423) | 返回相机的投影矩阵。 |

**示例：**

```
1. import { Scene, SceneResourceFactory, SceneNodeParameters, Camera, Mat4x4 } from '@kit.ArkGraphics3D';

3. function GetProjectionMatrix(): void {
4. // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
5. Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"))
6. .then(async (result: Scene) => {
7. if (!result.root) {
8. return;
9. }
10. let sceneFactory: SceneResourceFactory = result.getResourceFactory();
11. let sceneCameraParameter: SceneNodeParameters = { name: "camera1" };
12. // 创建相机
13. let camera: Camera = await sceneFactory.createCamera(sceneCameraParameter);
14. camera.enabled = true;
15. // 获取相机的投影矩阵
16. let projectionMatrix: Mat4x4 = camera.getProjectionMatrix();
17. });
18. }
```
