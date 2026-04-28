---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkgraphics3d-resource-environment
title: 创建并使用环境资源
breadcrumb: 指南 > 图形 > ArkGraphics 3D（方舟3D图形） > ArkGraphics 3D资源创建以及使用 > 创建并使用环境资源
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:65b6892db730cbfd47b29457e2ffa31b012ae51f308c500b09ba14849c2a3488
---

环境（Environment）：环境是3D场景背景的一种描述，可以基于图片进行创建。通过将一张图片进行正方体或者球体的映射处理，将图片贴在正方体或者球体上，在3D场景中模拟真实的环境。

ArkGraphics 3D支持用户创建环境资源，定义3D场景的背景。

## 开发步骤

1. 导入相关模块。

   在页面脚本中导入ArkGraphics 3D提供的核心类型，用于创建场景、相机、材质、图片等对象。

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
5. 创建环境并绑定图片。

   使用SceneResourceFactory.createEnvironment()创建环境对象，并通过createImage()加载环境贴图。设置backgroundType为等距柱状投影背景，将图片绑定到environmentImage，再调整indirectDiffuseFactor等属性以控制环境光强度。

   ```
   1. function createEnvironmentPromise() : Promise<Environment> {
   2. return new Promise((resolve, reject) => {
   3. // Ensure the scene is loaded before accessing sceneFactory
   4. if (globalScene) {
   5. let sceneFactory: SceneResourceFactory = globalScene.getResourceFactory();

   7. // Manually load environment maps (.ktx/.jpg/.png etc.)
   8. let sceneImageParameter: SceneResourceParameters = { name: 'image', uri: $rawfile('image/Cube_BaseColor.png') };
   9. let image: Promise<Image> = sceneFactory.createImage(sceneImageParameter);
   10. image.then(async (imageEntity: Image) => {
   11. // Create Environment
   12. let sceneEnvironmentParameter: SceneResourceParameters = { name: 'env' };
   13. let env: Promise<Environment> = sceneFactory.createEnvironment(sceneEnvironmentParameter);
   14. env.then(async (envEntity: Environment) => {
   15. envEntity.backgroundType = EnvironmentBackgroundType.BACKGROUND_EQUIRECTANGULAR;
   16. envEntity.environmentImage  = imageEntity;
   17. // Set environment related properties
   18. envEntity.indirectDiffuseFactor.x = 1;
   19. envEntity.indirectDiffuseFactor.y = 1;
   20. envEntity.indirectDiffuseFactor.z = 1;
   21. envEntity.indirectDiffuseFactor.w = 1;
   22. resolve(envEntity);
   23. }).catch((err: string) => {
   24. console.error('Environment mapping material create failed: ' + err + '.');
   25. reject(err);
   26. });
   27. }).catch((err: string) => {
   28. console.error('Image load failed: ' + err);
   29. reject(err);
   30. });
   31. } else {
   32. reject('Scene is not loaded yet.');
   33. }
   34. });
   35. }
   ```

   [resource.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/arkgraphic/resource.ets#L98-L134)
6. 应用环境到场景。

   在按钮点击事件中调用createEnvironmentPromise()创建环境资源，并将其赋值给场景的environment属性，使环境背景立即生效。

   ```
   1. Button('Add to Environment')
   2. // ...
   3. .onClick(async (): Promise<void> => {
   4. console.info('Start to replace with a material of image');

   6. if (!this.scene || !this.cam) {
   7. return;
   8. }

   10. this.env = await createEnvironmentPromise();
   11. if (this.env) {
   12. this.scene.environment = this.env;
   13. }
   14. });
   ```

   [resource.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/arkgraphic/resource.ets#L325-L345)
