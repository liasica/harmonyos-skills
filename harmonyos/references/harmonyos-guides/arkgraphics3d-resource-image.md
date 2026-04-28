---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkgraphics3d-resource-image
title: 创建并使用图片资源
breadcrumb: 指南 > 图形 > ArkGraphics 3D（方舟3D图形） > ArkGraphics 3D资源创建以及使用 > 创建并使用图片资源
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:22+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:1c4076fed85c2248bf55ec6decc102c06a7d1d29f89f63d86a7133fc778c2644
---

图片（Image）：图片本质上是一个储存信息的二维内存块(buffer)，用于储存3D渲染计算过程需要的相关信息，比如基础颜色、法线等等。

ArkGraphics 3D提供基于png、jpg、ktx格式创建Image资源的能力，支持用户自定义需要的Image资源。

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

   通过Scene.getNodeByPath()方法获取目标模型的几何体（Geometry）节点，并记录其原始材质，以便在后续修改材质后能够恢复至原始材质状态。

   ```
   1. this.geom = this.scene.getNodeByPath('rootNode_/Unnamed Node 1/AnimatedCube') as Geometry;

   3. // record original material
   4. this.originalMat = this.geom.mesh.subMeshes[0].material;
   ```

   [resource.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/arkgraphic/resource.ets#L195-L200)
5. 创建图片资源并绑定到材质。

   使用SceneResourceFactory.createImage()创建图片资源，再通过createMaterial()创建Shader材质。将图片资源绑定到Shader输入属性BASE\_COLOR\_Image上，使模型表面贴图生效。

   ```
   1. function createImagePromise(): Promise<Image> {
   2. return new Promise((resolve, reject) => {
   3. // Ensure the scene is loaded before accessing sceneFactory
   4. if (globalScene) {
   5. let sceneFactory: SceneResourceFactory = globalScene.getResourceFactory();

   7. let sceneImageParameter: SceneResourceParameters = {
   8. name: 'image',
   9. uri: $rawfile('image/Cube_BaseColor.png')
   10. };

   12. let image: Promise<Image> = sceneFactory.createImage(sceneImageParameter);
   13. image.then((imageEntity: Image) => {
   14. resolve(imageEntity);
   15. }).catch((err: string) => {
   16. console.error('Image load failed: ' + err + '.');
   17. reject(err);
   18. });
   19. } else {
   20. reject('Scene is not loaded yet.');
   21. }
   22. });
   23. }
   ```

   [resource.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/arkgraphic/resource.ets#L72-L96)
6. 应用图片材质到模型节点。

   在按钮点击回调中，通过createShader()创建Shader并绑定材质对象，调用createImagePromise()获取图片资源并将其应用到模型几何体上，实现贴图替换。

   ```
   1. Button('Replace with a Image material')
   2. // ...
   3. .onClick(async (): Promise<void> => {
   4. console.info('Start to replace with a material of image');

   6. if (!this.scene || !this.cam || !this.rf) {
   7. return;
   8. }

   10. // create shader
   11. this.shader = await this.rf.createShader({
   12. name: 'shaderResource',
   13. uri: $rawfile('shaders/custom_shader/custom_material_sample.shader')
   14. });

   16. // create imageMat
   17. this.imageMat = await this.rf.createMaterial({ name: 'imageMat' }, MaterialType.SHADER) as ShaderMaterial;

   19. // bind between shader and imageMat
   20. this.imageMat.colorShader = this.shader;
   21. let createdImage =  await createImagePromise();
   22. if (createdImage) {
   23. this.imageMat.colorShader.inputs['BASE_COLOR_Image'] = createdImage;
   24. }

   26. this.geom = this.scene.getNodeByPath('rootNode_/Unnamed Node 1/AnimatedCube') as Geometry;

   28. this.geom.mesh.materialOverride = undefined;
   29. this.geom.mesh.subMeshes[0].material = this.imageMat;
   30. })
   ```

   [resource.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/arkgraphic/resource.ets#L287-L323)
