---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkgraphics3d-resource-environment
title: 创建并使用环境资源
breadcrumb: 指南 > 图形 > ArkGraphics 3D（方舟3D图形） > ArkGraphics 3D资源创建以及使用 > 创建并使用环境资源
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:21+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8d7d5ff0288fae023974ecdf83b277bc28bb3307a7a6b0d51349263af5b7cd24
---

环境（Environment）：环境是3D场景背景的一种描述，可以基于图片进行创建。通过将一张图片进行正方体或者球体的映射处理，将图片贴在正方体或者球体上，在3D场景中模拟真实的环境。

ArkGraphics 3D支持用户创建环境资源，定义3D场景的背景。

## 开发步骤

1. 导入相关模块。

   在页面脚本中导入ArkGraphics 3D提供的核心类型，用于创建场景、相机、材质、图片等对象。

   ```typescript
   import { Camera, Environment, Geometry, Image, Material, MaterialType, Scene, SceneResourceFactory,
     SceneResourceParameters, Shader, ShaderMaterial, EnvironmentBackgroundType } from '@kit.ArkGraphics3D';
   ```
2. 加载场景并设置渲染参数。

   调用Scene.load()方法加载.glb或.gltf格式的模型文件，并在加载完成后获取Scene对象。随后构建SceneOptions对象，指定场景及渲染模式，用于后续通过Component3D将场景内容渲染到界面中。

   ```typescript
   if (this.scene === null) {
     // Switched from .gltf to .glb; same content, different format
     Scene.load($rawfile('gltf/CubeWithFloor/glTF/AnimatedCube.glb'))
       .then(async (result: Scene) => {
         // Assign loaded scene to globalScene for unified resource creation
         globalScene = result;
         this.scene = result;
         this.sceneOpt = { scene: this.scene, modelType: ModelType.SURFACE } as SceneOptions;
         this.rf = this.scene.getResourceFactory();
         // ...
       })
       .catch((error: string) => {
         console.error('init error: ' + error + '.');
       });
   }
   ```
3. 初始化相机。

   创建相机对象并设置相机启用状态与观察位置，用于后续展示模型。

   ```typescript
   this.cam = await this.rf.createCamera({ 'name': 'Camera1' });
   this.cam.enabled = true;
   this.cam.position.z = 5;
   ```
4. 获取几何体节点。

   通过Scene.getNodeByPath()方法获取目标模型的几何体（Geometry）节点，并记录其原始材质，以便在后续修改材质后可进行回退或恢复操作。

   ```typescript
   this.geom = this.scene.getNodeByPath('rootNode_/Unnamed Node 1/AnimatedCube') as Geometry;

   // record original material
   this.originalMat = this.geom.mesh.subMeshes[0].material;
   ```
5. 创建环境并绑定图片。

   使用SceneResourceFactory.createEnvironment()创建环境对象，并通过createImage()加载环境贴图。设置backgroundType为等距柱状投影背景，将图片绑定到environmentImage，再调整indirectDiffuseFactor等属性以控制环境光强度。

   ```typescript
   function createEnvironmentPromise() : Promise<Environment> {
     return new Promise((resolve, reject) => {
       // Ensure the scene is loaded before accessing sceneFactory
       if (globalScene) {
         let sceneFactory: SceneResourceFactory = globalScene.getResourceFactory();

         // Manually load environment maps (.ktx/.jpg/.png etc.)
         let sceneImageParameter: SceneResourceParameters = { name: 'image', uri: $rawfile('image/Cube_BaseColor.png') };
         let image: Promise<Image> = sceneFactory.createImage(sceneImageParameter);
         image.then(async (imageEntity: Image) => {
           // Create Environment
           let sceneEnvironmentParameter: SceneResourceParameters = { name: 'env' };
           let env: Promise<Environment> = sceneFactory.createEnvironment(sceneEnvironmentParameter);
           env.then(async (envEntity: Environment) => {
             envEntity.backgroundType = EnvironmentBackgroundType.BACKGROUND_EQUIRECTANGULAR;
             envEntity.environmentImage  = imageEntity;
             // Set environment related properties
             envEntity.indirectDiffuseFactor.x = 1;
             envEntity.indirectDiffuseFactor.y = 1;
             envEntity.indirectDiffuseFactor.z = 1;
             envEntity.indirectDiffuseFactor.w = 1;
             resolve(envEntity);
           }).catch((err: string) => {
             console.error('Environment mapping material create failed: ' + err + '.');
             reject(err);
           });
         }).catch((err: string) => {
           console.error('Image load failed: ' + err);
           reject(err);
         });
       } else {
         reject('Scene is not loaded yet.');
       }
     });
   }
   ```
6. 应用环境到场景。

   在按钮点击事件中调用createEnvironmentPromise()创建环境资源，并将其赋值给场景的environment属性，使环境背景立即生效。

   ```typescript
   Button('Add to Environment')
     // ...
     .onClick(async (): Promise<void> => {
       console.info('Start to replace with a material of image');

       if (!this.scene || !this.cam) {
         return;
       }

       this.env = await createEnvironmentPromise();
       if (this.env) {
         this.scene.environment = this.env;
       }
     });
   ```
