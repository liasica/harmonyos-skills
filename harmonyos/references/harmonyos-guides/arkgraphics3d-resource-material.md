---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkgraphics3d-resource-material
title: 创建并使用材质资源
breadcrumb: 指南 > 图形 > ArkGraphics 3D（方舟3D图形） > ArkGraphics 3D资源创建以及使用 > 创建并使用材质资源
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1a5e6965ed57422db0fd50bf44996db3f5247f99b417a6754abde1944cad4369
---

材质（Material）：材质是用于定义物体表面视觉效果的重要资源。材质决定了物体如何与光线交互，从而影响其最终的渲染效果，如颜色、金属感、粗糙度等外观属性。

ArkGraphics 3D采用基于物理的渲染（PBR, Physically-Based Rendering）模型，其材质实现遵循通用的PBR原理。开发者既可以使用标准材质快速实现真实感效果，也可以通过自定义Shader材质灵活控制渲染逻辑。

## 基本概念

着色器（Shader）：着色器是GPU上可以执行的一段程序，可以控制GPU执行哪些并行计算操作。AGP引擎提供的默认着色器实现了PBR渲染，开发者只需要指定对应的参数就可以完成不同的PBR渲染。

ArkGraphics 3D支持开发者创建自定义的着色器，开发者可以通过自定义着色器自定义渲染计算过程，完全控制渲染计算流程，比如控制某物体不受某光源的影响、自定义边缘描边、高亮效果等个性化视觉呈现。

着色器通常配合MaterialType.SHADER材质使用，是实现个性化渲染的重要手段。其创建依赖名称及沙箱路径，创建后可绑定至材质上，替代默认的渲染行为。

## 材质类型（MaterialType）

ArkGraphics 3D中的材质类型通过[MaterialType](../harmonyos-references/js-apis-inner-scene-resources.md#materialtype)枚举指定，目前支持以下两种类型：

* MaterialType.SHADER：基于Shader（着色器）的材质类型，支持绑定自定义着色器，开发者可通过自定义渲染程序实现个性化的视觉表现，适用于高级图形渲染需求。
* MaterialType.METALLIC\_ROUGHNESS：基于金属-粗糙度模型的标准PBR材质类型，符合glTF材质规范，适合快速构建真实感渲染效果，支持设置基础色、金属度、粗糙度、法线贴图等常见属性。

材质的创建一般通过[SceneResourceFactory.createMaterial()](../harmonyos-references/js-apis-inner-scene.md#creatematerial)方法完成，需指定材质名称和类型。不同类型的材质支持不同的参数配置，开发者可按需选择以实现预期的渲染效果。

## 材质的属性

材质的属性定义了其在渲染时的视觉表现行为，例如颜色、金属感、粗糙度、光照响应以及透明度控制等。通过设置这些属性，开发者可以精准控制物体在场景中的外观效果。

在ArkGraphics 3D中，材质属性设计既提供了统一的基础能力，也根据材质类型提供了差异化扩展，满足从基础场景搭建到高级视觉定制的多样需求。

### 通用属性

所有材质均具备以下基础属性（如materialType、shadowReceiver、blend等）可通过设置[Material](../harmonyos-references/js-apis-inner-scene-resources.md#material)类型对象实现，用于控制材质的类型及其渲染基础行为：

* materialType：材质类型，标识该材质是标准PBR材质还是基于Shader的自定义材质。

  适用场景：当需要快速使用预设真实感材质时选择PBR材质，需实现个性化或特殊渲染效果时选择Shader材质。
* shadowReceiver：材质是否可以接收场景中的阴影投射，true表示可以接收，false表示不能接收，默认为false。

  适用场景：需要表现阴影效果的物体，如地面、墙体、角色等开启；纯发光物体或不参与阴影计算的可关闭以优化性能。
* cullMode：剔除模式，决定是否剔除背面几何体，默认值为BACK，即剔除背面。

  适用场景：普通实体模型一般开启剔除背面提升渲染效率；透明或双面材质（如树叶、布料）需要禁用剔除以显示完整模型。
* blend：是否启用材质的透明效果模式。true表示开启透明，false表示关闭透明，默认值为false。

  适用场景：表现透明或半透明材质时开启，如玻璃、水面、烟雾、透明塑料等。
* alphaCutoff：透明度阈值，取值范围[0,1]，默认值为1。像素的alpha值低于该阈值时不进行渲染，用于实现透明裁剪效果。

  适用场景：需要硬透明裁剪的材质，比如树叶、铁丝网、布料边缘等带有透明区域但无半透明渐变的模型。通过设置阈值，可以快速裁剪掉透明部分像素。
* renderSort：渲染排序设置，用于控制材质在渲染队列中的渲染顺序，确保透明或特殊效果材质正确叠加显示。

  适用场景：多重透明材质、叠加特效、UI元素等需要严格渲染顺序的场景。

### PBR材质属性

符合glTF标准的基于物理渲染（PBR）的金属-粗糙度材质，通过设置[MetallicRoughnessMaterial](../harmonyos-references/js-apis-inner-scene-resources.md#metallicroughnessmaterial20)实现，其中各项属性采用[MaterialProperty](../harmonyos-references/js-apis-inner-scene-resources.md#materialproperty20)类型封装，支持绑定纹理和设置因子（factor）值。具体属性包括：

* baseColor：基础颜色和透明度，包含纹理及对应因子，用于定义材质表面的主色调。

  适用场景：所有材质的基本颜色设置，适用于任何物体表面，尤其是需要表现颜色和透明度的模型。
* normal：法线贴图，用于模拟表面细节凹凸，增强光照效果的真实感。

  适用场景：需要表现表面细节如石材纹理、皮肤毛孔、木纹凹凸等，提升真实感的模型。
* material：金属度、粗糙度与反射率参数，描述材质表面的光学特性。

  适用场景：区分金属和非金属表面，控制材质的光滑或粗糙程度，常用于金属件、塑料、橡胶等多种材质。
* ambientOcclusion：环境光遮蔽贴图，提升材质细节处的阴影层次和真实感。

  适用场景：增强模型细节阴影效果，适合复杂结构或细节丰富的物体，如建筑物裂缝、机械零件缝隙。
* emissive：自发光颜色及纹理，表达材质自发光的效果。

  适用场景：灯光、屏幕、发光标志、荧光材料等需要表现光源或自发光效果的材质。
* clearCoat：清漆层强度，模拟车漆等具有透明反光层的材质。

  适用场景：汽车车身、家具表面等有光泽涂层的材质，表现透明光泽和反射。
* clearCoatRoughness：清漆层的粗糙度，控制清漆层的反光细节。

  适用场景：配合clearCoat使用，调节涂层表面的光滑度或粗糙感。
* clearCoatNormal：清漆层法线贴图，增强清漆层的光照变化。

  适用场景：清漆层带有细节纹理时使用，增加涂层的真实光照反馈。
* sheen：微纤维漫反射层，用于表现布料、织物的光泽感。

  适用场景：衣物、窗帘、沙发等纺织品，表现柔和的光泽和细腻质感。
* specular：镜面反射属性，控制非金属材质的高光反射强度。

  适用场景：玻璃、水面、塑料等非金属材质的高光表现，增强材质的镜面反射效果。

## 创建Shader材质并设置属性

在需要自定义渲染逻辑或实现特殊视觉效果时，可以通过MaterialType.SHADER类型创建Shader材质。Shader材质支持绑定自定义的.shader文件，开发者可以在其中编写自定义的渲染计算逻辑，灵活控制模型的外观表现，实现如描边、高光、发光等个性化视觉效果。以下示例展示了Shader材质的创建与使用流程，包括场景加载、Shader资源创建与绑定，以及将Shader材质应用到目标几何体节点的过程。

1. 导入相关模块。

   在页面脚本中导入ArkGraphics 3D提供的核心类型，用于创建Shader材质及绑定Shader资源。

   ```
   1. import { Camera, Environment, Geometry, Image, Material, MaterialType, Scene, SceneResourceFactory,
   2. SceneResourceParameters, Shader, ShaderMaterial, EnvironmentBackgroundType } from '@kit.ArkGraphics3D';
   ```

   [resource.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/arkgraphic/resource.ets#L16-L19)
2. 加载场景并设置渲染参数。

   调用Scene.load()方法加载.glb或.gltf格式的模型文件，并在加载完成后获取Scene对象。随后构建SceneOptions对象，指定场景及渲染模式，用于后续通过Component3D将场景内容渲染到界面中。

   ```
   1. if (this.scene === null) {
   2. // Switched from .gltf to .glb; same content, different format
   3. Scene.load($rawfile('gltf/CubeWithFloor/glTF/AnimatedCube.glb'))
   4. .then(async (result: Scene) => {
   5. // Assign loaded scene to globalScene for unified resource creation
   6. globalScene = result;
   7. this.scene = result;
   8. this.sceneOpt = { scene: this.scene, modelType: ModelType.SURFACE } as SceneOptions;
   9. this.rf = this.scene.getResourceFactory();
   10. // ...
   11. })
   12. .catch((error: string) => {
   13. console.error('init error: ' + error + '.');
   14. });
   15. }
   ```

   [resource.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/arkgraphic/resource.ets#L178-L207)
3. 初始化相机。

   创建相机对象并设置相机启用状态与观察位置，用于后续展示模型。

   ```
   1. this.cam = await this.rf.createCamera({ 'name': 'Camera1' });
   2. this.cam.enabled = true;
   3. this.cam.position.z = 5;
   ```

   [resource.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/arkgraphic/resource.ets#L189-L193)
4. 获取几何体节点。

   通过Scene.getNodeByPath()方法获取目标模型的几何体（Geometry）节点，并记录其原始材质，以便在后续修改材质后可进行回退或恢复操作。

   ```
   1. this.geom = this.scene.getNodeByPath('rootNode_/Unnamed Node 1/AnimatedCube') as Geometry;

   3. // record original material
   4. this.originalMat = this.geom.mesh.subMeshes[0].material;
   ```

   [resource.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/arkgraphic/resource.ets#L195-L200)
5. 创建Shader材质（空白）。

   调用SceneResourceFactory.createMaterial()创建Shader类型的空白材质，为后续绑定自定义Shader做准备。

   ```
   1. function createMaterialPromise(): Promise<Material> {
   2. return new Promise((resolve, reject) => {
   3. // Ensure the scene is loaded before accessing sceneFactory
   4. if (globalScene) {
   5. let sceneFactory: SceneResourceFactory = globalScene.getResourceFactory();
   6. let sceneMaterialParameter: SceneResourceParameters = { name: 'material' };
   7. // Create Material
   8. let material: Promise<Material> = sceneFactory.createMaterial(sceneMaterialParameter, MaterialType.SHADER);
   9. material.then(resolve)
   10. .catch((err: string) => {
   11. console.error('Blank material create failed: ' + err);
   12. reject(err);
   13. });
   14. } else {
   15. reject('Scene is not loaded yet.');
   16. }
   17. });
   18. }
   ```

   [resource.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/arkgraphic/resource.ets#L24-L43)
6. 创建并绑定Shader资源。

   通过SceneResourceFactory.createShader()创建自定义着色器资源，并将其绑定到Shader材质上，实现自定义渲染逻辑。

   ```
   1. function createShaderPromise(): Promise<Shader> {
   2. return new Promise((resolve, reject) => {
   3. // Ensure the scene is loaded before accessing sceneFactory
   4. if (globalScene) {
   5. let sceneFactory: SceneResourceFactory = globalScene.getResourceFactory();

   7. // Create a SceneResourceParameters object and use it to create a shader
   8. let sceneResourceParameter: SceneResourceParameters = {
   9. name: 'shaderResource',
   10. uri: $rawfile('shaders/custom_shader/custom_material_sample.shader')
   11. };

   13. let shader: Promise<Shader> = sceneFactory.createShader(sceneResourceParameter);
   14. shader.then((shaderEntity: Shader) => {
   15. resolve(shaderEntity);
   16. }).catch((err: string) => {
   17. console.error('Shader load failed: ' + err + '.');
   18. reject(err);
   19. });
   20. } else {
   21. reject('Scene is not loaded yet.');
   22. }
   23. });
   24. }
   ```

   [resource.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/arkgraphic/resource.ets#L45-L70)
7. 应用Shader材质到几何体节点。

   通过按钮点击事件调用不同的函数，可在运行时动态切换模型的材质，实现从默认材质到Shader材质的过渡效果。

   ```
   1. Button('Replace with a blank material')
   2. // ...
   3. .onClick(async (): Promise<void> => {
   4. console.info('Start to replace with a blank material');

   6. if (!this.blankMat) {
   7. this.blankMat = await createMaterialPromise();
   8. }

   10. if (!this.scene || !this.rf) {
   11. return;
   12. }

   14. this.geom = this.scene.getNodeByPath('rootNode_/Unnamed Node 1/AnimatedCube') as Geometry;

   16. this.geom.mesh.materialOverride = undefined;
   17. if (this.blankMat) {
   18. this.geom.mesh.subMeshes[0].material = this.blankMat;
   19. }

   21. });

   23. Button('Replace with a Shader material')
   24. // ...
   25. .onClick(async (): Promise<void> => {
   26. console.info('Start to replace with a shader material');

   28. if (!this.shader) {
   29. this.shader = await createShaderPromise();
   30. }

   32. if (!this.scene || !this.rf) {
   33. return;
   34. }

   36. if (!this.shaderMat) {
   37. let rf = this.scene.getResourceFactory();
   38. this.shaderMat = await rf.createMaterial({ name: 'shaderMat' }, MaterialType.SHADER);
   39. }

   41. if (this.shader) {
   42. this.shaderMat.colorShader = this.shader;
   43. }

   45. this.geom = this.scene.getNodeByPath('rootNode_/Unnamed Node 1/AnimatedCube') as Geometry;

   47. this.geom.mesh.materialOverride = undefined;

   49. if (this.shaderMat) {
   50. this.geom.mesh.subMeshes[0].material = this.shaderMat;
   51. }
   52. })
   ```

   [resource.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/arkgraphic/resource.ets#L222-L285)

## 创建PBR材质并设置属性

在ArkGraphics 3D中，基于物理的渲染（PBR）材质允许开发者通过调整金属度、粗糙度、透明度等参数精确控制物体的外观效果，从而实现高度真实的渲染表现。由于不同模型在导出时所携带的PBR属性可能存在差异，因此在设置材质前建议根据模型内容进行适配。本示例选用CompareClearcoat模型，该模型自带清漆层（Clearcoat）相关的材质参数，适合用于演示清漆效果的调节。通过设置clearCoat与clearCoatRoughness等属性，可以直观观察清漆层的强度、光泽度与反射特性的变化。

1. 导入相关模块。

   在页面脚本中导入ArkGraphics 3D提供的核心类型，用于创建PBR材质及绑定贴图资源。

   ```
   1. import { Scene, Camera, Material, Node, Image, SceneResourceFactory, Geometry, EnvironmentBackgroundType,
   2. PostProcessSettings, ToneMappingType, MetallicRoughnessMaterial, Vec4 } from '@kit.ArkGraphics3D';
   3. import {lookAt, OrbitCameraHelper } from '../common/utils';
   ```

   [pbr\_clearcoat.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/material/pbr_clearcoat.ets#L17-L21)
2. 加载场景资源。

   调用Scene.load()方法加载.glb或.gltf格式的模型文件，并在加载完成后获取Scene对象。场景加载完成后，可以访问场景的资源工厂以创建材质和其他资源。

   ```
   1. if (this.scene == null) {
   2. // Switched from .gltf to .glb; same content, different format
   3. Scene.load($rawfile('gltf/CompareClearcoat/CompareClearcoat.glb'))
   4. .then(async (scene: Scene) => {
   5. this.scene = scene;
   6. if (!this.scene.root) {
   7. return;
   8. }
   9. let rf: SceneResourceFactory = scene.getResourceFactory();

   11. // ...
   12. });
   13. }
   ```

   [pbr\_clearcoat.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/material/pbr_clearcoat.ets#L49-L117)
3. 获取几何体节点并预加载纹理。

   通过场景的节点路径获取目标几何体节点，并提取其材质，随后预加载清漆层（Clearcoat）相关的纹理资源。

   ```
   1. let pbrNode: Node | null | undefined = this.scene.root?.getNodeByPath('Unnamed Node 1/GeoSphere003');
   2. if (pbrNode) {
   3. this.material = (pbrNode as Geometry).mesh.subMeshes[0].material;
   4. let mrMaterial = (this.material as MetallicRoughnessMaterial);
   5. let original: Image | null = mrMaterial.clearCoat.image;
   6. const helmAlbedo: Resource = $rawfile('image/round_pattern.png');
   7. const irregularUri: Resource = $rawfile('image/irregular_pattern.png');
   8. let round: Image | null = await rf.createImage({name: 'round', uri: helmAlbedo });
   9. let irregular: Image | null = await rf.createImage({name: 'irregular', uri: irregularUri });
   10. if (original && round && irregular ) {
   11. this.textures.push(original);
   12. this.textures.push(round);
   13. this.textures.push(irregular);
   14. }
   15. }
   ```

   [pbr\_clearcoat.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/material/pbr_clearcoat.ets#L62-L78)
4. 配置环境光照。

   创建图像基础的光照（IBL）环境，配置环境贴图和辐射贴图，以实现真实的环境光照效果。

   ```
   1. scene.environment = await rf.createEnvironment({ name: 'env' });
   2. scene.environment.backgroundType = EnvironmentBackgroundType.BACKGROUND_CUBEMAP;
   3. scene.environment.environmentImage = await rf.createImage({ name: 'cube', uri: $rawfile('Environment/quarry_02_2k_skybox.ktx') });
   4. scene.environment.radianceImage = await rf.createImage({ name: 'rad', uri: $rawfile('Environment/quarry_02_2k_radiance.ktx') });
   5. scene.environment.irradianceCoefficients =
   6. [{ x: 1.080343842506409, y: 0.936282396316528, z: 0.665518164634705 },
   7. { x: 0.959947884082794, y: 0.828918874263763, z: 0.569704353809357 },
   8. { x: 0.848236382007599, y: 0.715092182159424, z: 0.473145037889481 },
   9. { x: -0.591795265674591, y: -0.501678705215454, z: -0.334018945693970 },
   10. { x: -0.775423347949982, y: -0.655484378337860, z: -0.437325984239578 },
   11. { x: 1.053589701652527, y: 0.887459456920624, z: 0.587381422519684 },
   12. { x: -0.018954016268253, y: -0.014871496707201, z: -0.008891185745597 },
   13. { x: -0.566255271434784, y: -0.476870059967041, z: -0.314557582139969 },
   14. { x: -0.239390164613724, y: -0.200478553771973, z: -0.132790848612785 }];
   ```

   [pbr\_clearcoat.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/material/pbr_clearcoat.ets#L81-L96)
5. 创建相机并设置视角。

   创建一个相机对象，并设置其位置和观察目标。然后启用轨道控制功能，让用户可以通过手势旋转和缩放视图。

   ```
   1. this.cam = await rf.createCamera({ 'name': 'ClearcoatCam' });
   2. this.cam.enabled = true;
   3. lookAt(this.cam,{x:0,y:0,z:-3},{x:0,y:0,z:0},{x:0,y:1,z:0});
   4. this.sceneOpt = { scene: this.scene, modelType: ModelType.SURFACE } as SceneOptions;
   5. this.orbitCamera.SetOrbitFromEye(this.cam.position, this.scene.root.position, this.cam.rotation);
   ```

   [pbr\_clearcoat.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/material/pbr_clearcoat.ets#L98-L104)
6. 切换清漆层纹理。

   允许用户在不同的清漆纹理之间切换。通过按下按钮或触发事件来实现纹理的动态切换。

   ```
   1. changeClearcoatTex() {
   2. if (this.textures.length > 0) {
   3. let i = ++this.textureInUse % this.textures.length;
   4. (this.material as MetallicRoughnessMaterial).clearCoat.image = this.textures[i];
   5. }
   6. }
   ```

   [pbr\_clearcoat.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/material/pbr_clearcoat.ets#L121-L128)
7. 调整清漆层强度。

   通过滑动条调整清漆层的强度。这个方法通过更新材质的clearCoat.factor属性来实现。

   ```
   1. setClearcoat(v: number) {
   2. if (this.material) {
   3. const f: Vec4 = (this.material as MetallicRoughnessMaterial).clearCoat.factor;
   4. f.x = v / RESO;
   5. (this.material as MetallicRoughnessMaterial).clearCoat.factor = f;
   6. }
   7. }
   ```

   [pbr\_clearcoat.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/material/pbr_clearcoat.ets#L131-L139)
8. 切换粗糙度纹理。

   类似于清漆层纹理切换，用户也可以在不同的粗糙度纹理之间切换。

   ```
   1. changeClearcoatRoughTex() {
   2. if (this.textures.length > 0) {
   3. let i = ++this.textureInUse % this.textures.length;
   4. (this.material as MetallicRoughnessMaterial).clearCoatRoughness.image = this.textures[i];
   5. }
   6. }
   ```

   [pbr\_clearcoat.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/material/pbr_clearcoat.ets#L142-L149)
9. 调整清漆层粗糙度。

   通过滑动条调整清漆层的粗糙度，同样地，这通过更新clearCoatRoughness.factor来实现。

   ```
   1. setClearcoatRoughness(v: number) {
   2. if (this.material) {
   3. const f: Vec4 = (this.material as MetallicRoughnessMaterial).clearCoatRoughness.factor;
   4. f.y = v / RESO;
   5. (this.material as MetallicRoughnessMaterial).clearCoatRoughness.factor = f;
   6. }
   7. }
   ```

   [pbr\_clearcoat.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/material/pbr_clearcoat.ets#L152-L160)
