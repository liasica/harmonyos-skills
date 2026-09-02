---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkgraphics3d-resource-image
title: 创建并使用图片资源
breadcrumb: 指南 > 图形 > ArkGraphics 3D（方舟3D图形） > ArkGraphics 3D资源创建以及使用 > 创建并使用图片资源
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:21+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:453e7aad4e3780a52dcce3524742071192cfc9a1399da2b6af0a4eaab705b163
---

图片（Image）：图片本质上是一个储存信息的二维内存块(buffer)，用于储存3D渲染计算过程需要的相关信息，比如基础颜色、法线等等。

ArkGraphics 3D提供基于png、jpg、ktx格式创建Image资源的能力，支持用户自定义需要的Image资源。

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

   通过Scene.getNodeByPath()方法获取目标模型的几何体（Geometry）节点，并记录其原始材质，以便在后续修改材质后能够恢复至原始材质状态。

   ```typescript
   this.geom = this.scene.getNodeByPath('rootNode_/Unnamed Node 1/AnimatedCube') as Geometry;

   // record original material
   this.originalMat = this.geom.mesh.subMeshes[0].material;
   ```
5. 创建图片资源。

   使用SceneResourceFactory.createImage()创建图片资源。

   ```typescript
   function createImagePromise(): Promise<Image> {
     return new Promise((resolve, reject) => {
       // Ensure the scene is loaded before accessing sceneFactory
       if (globalScene) {
         let sceneFactory: SceneResourceFactory = globalScene.getResourceFactory();

         let sceneImageParameter: SceneResourceParameters = {
           name: 'image',
           uri: $rawfile('image/Cube_BaseColor.png')
         };

         let image: Promise<Image> = sceneFactory.createImage(sceneImageParameter);
         image.then((imageEntity: Image) => {
           resolve(imageEntity);
         }).catch((err: string) => {
           console.error('Image load failed: ' + err + '.');
           reject(err);
         });
       } else {
         reject('Scene is not loaded yet.');
       }
     });
   }
   ```
6. 应用图片材质到模型节点。

   在按钮点击回调中，通过createShader()和createMaterial()创建Shader材质，调用createImagePromise()获取图片资源并绑定到Shader输入属性BASE\_COLOR\_Image上，最后将材质应用到模型几何体，使模型表面贴图生效，实现贴图替换。

   ```typescript
   Button('Replace with a Image material')
     // ...
     .onClick(async (): Promise<void> => {
       console.info('Start to replace with a material of image');

       if (!this.scene || !this.cam || !this.rf) {
         return;
       }

       // create shader
       this.shader = await this.rf.createShader({
         name: 'shaderResource',
         uri: $rawfile('shaders/custom_shader/custom_material_sample.shader')
       });

       // create imageMat
       this.imageMat = await this.rf.createMaterial({ name: 'imageMat' }, MaterialType.SHADER) as ShaderMaterial;

       // bind between shader and imageMat
       this.imageMat.colorShader = this.shader;
       let createdImage =  await createImagePromise();
       if (createdImage) {
         this.imageMat.colorShader.inputs['BASE_COLOR_Image'] = createdImage;
       }

       this.geom = this.scene.getNodeByPath('rootNode_/Unnamed Node 1/AnimatedCube') as Geometry;

       this.geom.mesh.materialOverride = undefined;
       this.geom.mesh.subMeshes[0].material = this.imageMat;
     })
   ```
