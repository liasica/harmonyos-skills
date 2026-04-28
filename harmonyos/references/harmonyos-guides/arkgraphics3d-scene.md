---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkgraphics3d-scene
title: ArkGraphics 3D场景搭建以及管理
breadcrumb: 指南 > 图形 > ArkGraphics 3D（方舟3D图形） > ArkGraphics 3D场景搭建以及管理
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:77d24707af6c45415175f13ccd70d3bbeadb9a53aa26cfb5898fcd114492c06d
---

一个3D场景通常由光源、相机、模型三个关键部分组成。

* 光源：为整个3D场景提供光照，使得3D场景中的模型变得可见。与真实物理场景一致，没有光源场景将变得一片漆黑，得到的渲染结果也就是全黑色。
* 相机：为3D场景提供一个观察者。3D渲染本质上是从一个角度观察3D场景并投影到2D图片上。没有相机就没有3D场景的观察者，也就不会得到渲染结果。
* 模型：3D场景中的模型用于描述对象的形状、结构和外观，一般具有网格、材质、纹理、动画等属性。一些常见的3D模型格式有OBJ、FBX、glTF等。

模型加载后，可以通过ArkUI的[Component3D](../harmonyos-references/ts-basic-components-component3d.md)渲染组件呈现给用户，Component3D负责将ArkGraphics 3D场景渲染到界面中。在自定义场景模式下，开发者可以使用ArkTS API创建并管理相机和光源节点，从而设置合适的观察角度和光照效果；在自动场景模式下，框架会根据模型自动创建基础相机和光照。ArkTS API可通过napi调用AGP中由C++实现的相应能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/Dr30X-_LR66qpChONmNZRA/zh-cn_image_0000002552799054.png?HW-CC-KV=V1&HW-CC-Date=20260427T234720Z&HW-CC-Expire=86400&HW-CC-Sign=6E2B6D0342682D868CE8B74923CC39C375D51D5DBB375AFFC7CC13433BD8BE3D)

## 模型的加载及呈现

模型的格式多种多样，目前ArkGraphics 3D仅支持glTF模型的加载，glTF是一种对于3D场景描述的格式，glTF作为一种开源3D场景格式在业界被广泛采用。关于glTF的介绍可以参照[glTF-2.0](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html)。

一个glTF模型可以包含光源、相机、模型等3D场景关键要素，如果一个glTF模型中包含相机，使用ArkGraphics 3D提供的接口加载glTF就可以直接完成该相机视角下3D场景的渲染。如果不包含相机，也可以利用ArkGraphics 3D创建一个相机完成渲染。由于3D模型往往数据量很大，通常采用异步方式进行加载，加载成功后将返回一个scene对象，通过该对象可对整个3D场景进行编辑。

1. 导入相关模块。

   在页面脚本中导入ArkGraphics 3D提供的核心类型，用于创建和管理3D场景与相机。

   ```
   1. import { Camera, Scene, SceneResourceFactory } from '@kit.ArkGraphics3D';
   ```

   [init.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/scene/init.ets#L16-L18)
2. 加载场景资源。

   ArkGraphics 3D提供Scene.load()接口用于加载glTF模型文件，模型加载成功后会返回一个Scene实例，可通过它继续创建相机或光照等组件。模型文件支持.gltf与.glb格式，其中.glb为二进制封装形式，与.gltf内容等价但更便于加载与使用。模型加载支持相对路径和绝对路径两种方式：相对路径加载使用$rawfile()，从应用的resources/rawfile/目录读取内置资源文件；绝对路径加载需从应用沙箱目录读取文件，Scene.load()仅支持访问应用自身创建或写入的沙箱文件，具体示例可参见[load()](../harmonyos-references/js-apis-inner-scene.md#load)。

   以下示例展示通过相对路径加载.glb模型：

   ```
   1. if (this.scene == null) {
   2. // Load the model and place the gltf file in the related path. Use the actual path during loading.
   3. // Switched from .gltf to .glb; same content, different format
   4. Scene.load($rawfile('gltf/DamagedHelmet/glTF/DamagedHelmet.glb'))
   5. .then(async (result: Scene) => {
   6. this.scene = result;
   7. let rf: SceneResourceFactory = this.scene.getResourceFactory();
   8. // ...
   9. })
   10. .catch((error: string) => {
   11. console.error('Scene load failed: ' + error);
   12. });
   13. }
   ```

   [init.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/scene/init.ets#L42-L67)
3. 创建相机并设置场景渲染参数。

   使用SceneResourceFactory.createCamera()创建相机，并设置相机启用状态与观察位置。通过调整相机的z轴位置，可控制观察距离。随后将加载完成的Scene封装为SceneOptions，并指定渲染类型为ModelType.SURFACE，用于Component3D渲染显示。

   ```
   1. // Create a Camera.
   2. this.cam = await rf.createCamera({ 'name': 'Camera' });
   3. // Set proper camera parameters.
   4. this.cam.enabled = true;
   5. this.cam.position.z = 5;

   7. this.sceneOpt = { scene: this.scene, modelType: ModelType.SURFACE } as SceneOptions;
   ```

   [init.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/scene/init.ets#L51-L59)
4. 渲染3D模型。

   通过Component3D渲染加载完成的3D场景。若模型尚未加载完成，则显示提示文本。Component3D会根据传入的SceneOptions自动进行渲染。

   ```
   1. if (this.sceneOpt) {
   2. // Use Component3D to display the 3D scenario.
   3. Component3D(this.sceneOpt);
   4. } else {
   5. Text('Loading···');
   6. }
   ```

   [init.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/scene/init.ets#L73-L80)

## 相机的创建及管理

相机作为3D场景中的重要部分，决定了整个3D场景向2D图片的投影过程，相机的近远平面、FoV角等关键参数也会对整个3D渲染产生重要的影响。开发者可以通过设置相机参数，控制这个渲染过程，得到开发者想要的渲染效果。

ArkGraphics 3D提供了灵活的相机接口，开发者可根据需要动态创建、配置与控制相机。

1. 导入相关模块。

   在页面脚本中导入ArkGraphics 3D提供的核心类型，用于加载场景、创建相机及资源管理。

   ```
   1. import { Camera, Scene, SceneNodeParameters, SceneResourceFactory } from '@kit.ArkGraphics3D';
   ```

   [camera.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/scene/camera.ets#L16-L18)
2. 加载场景资源。

   使用Scene.load()从应用的resources/rawfile/目录加载.glb模型文件，.glb为glTF的二进制封装格式，与.gltf内容等价但更便于加载与使用。模型加载成功后返回Scene对象，可通过它获取SceneResourceFactory用于后续创建相机。

   ```
   1. let scene: Promise<Scene> = Scene.load($rawfile('gltf/CubeWithFloor/glTF/AnimatedCube.glb'));
   2. scene.then(async (result: Scene) => {
   3. // ...
   4. let sceneFactory: SceneResourceFactory = result.getResourceFactory();
   5. let sceneCameraParameter: SceneNodeParameters = { name: 'camera' };
   6. // ...
   7. }).catch((error: string) => {
   8. console.error('Scene load failed: ' + error);
   9. reject(error);
   10. });
   ```

   [camera.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/scene/camera.ets#L26-L66)
3. 创建相机并配置相机参数。

   调用 SceneResourceFactory.createCamera()创建相机，并配置相机的启用状态、位置、视场角（FoV）等参数。相机位置影响场景的观察距离，FoV决定画面透视范围。

   ```
   1. let camera: Promise<Camera> = sceneFactory.createCamera(sceneCameraParameter);
   2. camera.then(async (cameraEntity: Camera) => {
   3. // Enable the camera node.
   4. cameraEntity.enabled = true;

   6. // Set the camera position.
   7. cameraEntity.position.z = 5;

   9. // Set the FoV.
   10. cameraEntity.fov = 60 * Math.PI / 180;

   12. // Set other camera parameters.
   13. // ...
   14. // ...
   15. }).catch((error: string) => {
   16. console.error('Camera create failed: ' + error + '.');
   17. // ...
   18. });
   ```

   [camera.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/scene/camera.ets#L37-L60)
4. 初始化与渲染绑定。

   完成相机初始化后，将加载好的场景与相机绑定，并设置场景渲染参数。通过构建SceneOptions对象，即可将场景交由Component3D渲染显示，具体渲染方式可参考模型加载示例。

   ```
   1. this.camera = await createCameraPromise();
   2. if (globalScene && this.camera) {
   3. this.scene = globalScene;
   4. this.positionX = this.camera.position.x;
   5. this.positionY = this.camera.position.y;
   6. this.positionZ = this.camera.position.z;
   7. this.sceneOpt = { scene: this.scene, modelType: ModelType.SURFACE } as SceneOptions;
   8. }
   ```

   [camera.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/scene/camera.ets#L95-L104)
5. 相机交互。

   开发者可通过设置相机的位置、旋转、缩放、FoV等参数，以实现交互式视角控制。以下示例以Z轴控制为例，X/Y轴逻辑与此类似。

   ```
   1. Slider({
   2. value: this.positionZ,
   3. min: 5,
   4. max: 10,
   5. step: 0.1,
   6. style: SliderStyle.OutSet
   7. })
   8. .showTips(false)
   9. .onChange((value: number, mode: SliderChangeMode) => {
   10. this.positionZ = value;
   11. if (mode === SliderChangeMode.End) {
   12. if (!this.scene || !this.camera) {
   13. return;
   14. }
   15. this.camera.position.z = value;
   16. }
   17. })
   18. .width('100%')
   ```

   [camera.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/scene/camera.ets#L168-L187)

## 光源的创建及管理

3D场景的光源是对于物理世界中光源的一种数据建模，模拟物理世界的光源对于3D场景中的物体产生影响。

光源具有多种类型，例如平行光、锥形光。平行光用于模拟生活中的太阳光照，其光线平行且强度均匀。锥形光类似于手电筒，从一个点向扇形区域发射光线，光线强度随距离衰减。光源的颜色会影响场景中物体的最终着色，渲染时依据物理规律计算光源与物体表面颜色的交互，使光照效果更加真实。

ArkGraphics 3D提供创建光源及修改光源参数的功能，支持开发者通过设置光源属性调整3D场景，以实现预期的渲染效果。

1. 导入相关模块。

   在页面脚本中导入ArkGraphics 3D提供的核心类型，用于加载场景、创建相机与灯光。

   ```
   1. import { Camera, Light, LightType, Scene, SceneNodeParameters, SceneResourceFactory } from '@kit.ArkGraphics3D';
   ```

   [light.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/scene/light.ets#L16-L18)
2. 加载场景资源。

   使用Scene.load()从应用的resources/rawfile/目录加载.glb模型文件，.glb为glTF的二进制封装格式，与.gltf内容等价但更便于加载与使用。模型加载成功后返回Scene对象，可通过它获取SceneResourceFactory用于后续创建灯光。

   ```
   1. let scene: Promise<Scene> = Scene.load($rawfile('gltf/CubeWithFloor/glTF/AnimatedCube.glb'));
   2. scene.then(async (result: Scene) => {
   3. // ...
   4. let sceneFactory: SceneResourceFactory = result.getResourceFactory();
   5. let lightParameter: SceneNodeParameters = { name: 'light' };
   6. // ...
   7. }).catch((error: string) => {
   8. console.error('Scene load failed: ' + error);
   9. // ...
   10. });
   ```

   [light.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/scene/light.ets#L26-L62)
3. 创建灯光并配置灯光参数。

   调用 SceneResourceFactory.createLight()创建灯光，并配置灯光的类型、位置、颜色等参数。灯光类型决定了光线的方向，位置决定了光线的位置，颜色决定了光线的颜色。

   ```
   1. let light: Promise<Light> = sceneFactory.createLight(lightParameter, LightType.DIRECTIONAL);
   2. light.then(async (lightEntity: Light) => {
   3. // Set the color of the directional light.
   4. lightEntity.color = { r: 0.8, g: 0.1, b: 0.2, a: 1.0 };

   6. // Set other light parameters.
   7. // ...
   8. // ...
   9. }).catch((err: string) => {
   10. console.error('Light create failed: ' + err + '.');
   11. // ...
   12. });
   ```

   [light.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/scene/light.ets#L37-L54)
4. 初始化与渲染绑定。

   完成灯光初始化后，将加载好的场景与灯光进行绑定，并设置场景渲染参数。通过构建SceneOptions对象，即可将场景交由Component3D渲染显示。同时创建相机并设置观察位置，用于控制场景显示效果。

   ```
   1. this.light = await createLightPromise();
   2. if (globalScene && this.light) {
   3. this.scene = globalScene;
   4. this.sceneOpt = { scene: this.scene, modelType: ModelType.SURFACE } as SceneOptions;
   5. this.rf = this.scene.getResourceFactory();
   6. this.cam = await this.rf.createCamera({ 'name': 'Camera1' });
   7. this.cam.enabled = true;
   8. this.cam.position.z = 5;
   9. // Initialize color value
   10. this.red = this.light.color.r;
   11. this.green = this.light.color.g;
   12. this.blue = this.light.color.b;
   13. }
   ```

   [light.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/scene/light.ets#L95-L109)
5. 灯光交互。

   开发者可通过调整灯光的颜色、位置或方向等参数，实现交互式光照控制。以下示例展示了基于颜色分量（R/G/B）的交互逻辑，其余参数的控制方式与此类似。

   ```
   1. Slider({
   2. value: this.red,
   3. min: 0,
   4. max: 1,
   5. step: 0.01,
   6. style: SliderStyle.OutSet
   7. })
   8. .showTips(false)
   9. .onChange((value: number, mode: SliderChangeMode) => {
   10. this.red = value;
   11. if (mode === SliderChangeMode.End) {
   12. if (!this.scene || !this.light) {
   13. return;
   14. }
   15. this.light.color = {
   16. r: this.red,
   17. g: this.green,
   18. b: this.blue,
   19. a: 1.0
   20. }
   21. }
   22. })
   23. .width('100%')
   ```

   [light.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/scene/light.ets#L123-L147)

## 示例代码

* [基于3D引擎接口实现3D图形渲染功能（ArkTS）](https://gitcode.com/HarmonyOS_Samples/Graphics3D)
