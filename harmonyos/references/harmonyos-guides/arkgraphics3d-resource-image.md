---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkgraphics3d-resource-image
title: 创建并使用图片资源
breadcrumb: 指南 > 图形 > ArkGraphics 3D（方舟3D图形） > 资源创建与使用 > 创建并使用图片资源
category: harmonyos-guides
scraped_at: 2026-10-15T07:05:16+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:a3891e65db3bd9e6b196e0132c41820cdf4073567f4ba85bd1f563591396aa7a
---

图片（Image）：3D渲染中的二维纹理资源，本质为存储像素数据的内存缓冲区（buffer）。它提供物体表面渲染所需的数据，包括基础颜色、法线、金属度、粗糙度和环境遮蔽等贴图，也可作为材质或自定义着色器的纹理输入，最终决定物体表面的外观。

ArkGraphics 3D提供基于JPEG、PNG和KTX格式创建Image资源的能力，支持用户自定义需要的Image资源。各个格式的支持情况如下表所示：

| 格式 | 支持情况 |
| --- | --- |
| JPEG（.jpg/.jpeg） | 支持识别头部携带JFIF、Exif或ICC Profile标记的JPEG文件；  搭载HarmonyOS 7.0.0及以上版本的设备，新增支持识别头部包含DQT、XMP、MPF或Adobe标记的JPEG文件。 |
| PNG（.png） | 支持标准的PNG文件。 |
| KTX（.ktx） | 支持KTX格式的文件。KTX（Khronos Texture）是由Khronos Group定义的纹理容器格式，用于存储GPU可直接读取的纹理数据。 |

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
     // 从 .gltf 切换为 .glb；内容相同，格式不同
     Scene.load($rawfile('gltf/CubeWithFloor/glTF/AnimatedCube.glb'))
       .then(async (result: Scene) => {
         // 将加载的场景赋值给globalScene，以便统一创建资源
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
   this.cam = await this.rf.createCamera({ name: 'Camera1' });
   this.cam.enabled = true;
   this.cam.position.z = 5;
   ```
4. 获取几何体节点。

   通过Scene.getNodeByPath()方法获取目标模型的几何体（Geometry）节点，并记录其原始材质，以便在后续修改材质后能够恢复至原始材质状态。

   ```typescript
   this.geom = this.scene.getNodeByPath('rootNode_/Unnamed Node 1/AnimatedCube') as Geometry;

   // 记录原始材质
   this.originalMat = this.geom.mesh.subMeshes[0].material;
   ```
5. 创建图片资源。

   使用SceneResourceFactory.createImage()创建图片资源。

   ```typescript
   function createImagePromise(): Promise<Image> {
     return new Promise((resolve, reject) => {
       // 确保在访问sceneFactory之前场景已加载
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

       // 创建着色器
       this.shader = await this.rf.createShader({
         name: 'shaderResource',
         uri: $rawfile('shaders/custom_shader/custom_material_sample.shader')
       });

       // 创建图像材质
       this.imageMat = await this.rf.createMaterial({ name: 'imageMat' }, MaterialType.SHADER) as ShaderMaterial;

       // 在着色器和图像材质之间进行绑定
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
