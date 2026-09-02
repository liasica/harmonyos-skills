---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkgraphics3d-animation
title: ArkGraphics 3D场景动画控制以及管理
breadcrumb: 指南 > 图形 > ArkGraphics 3D（方舟3D图形） > ArkGraphics 3D场景动画控制以及管理
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:21+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:91060389c93e0669045d69478cb0af0ca630a78e1496cdd0342ebceed8aac19b
---

动画（animation）：动画是3D场景中重要的资源类型，用于控制场景中各种元素的运动。比如想要场景中的人物进行走路这个动作，每帧计算人物每一个关节的旋转角并进行设置是难以实现的。所以在完成类似的要求时，3D场景资源的制作者会将动画制作好，在模型文件中保存动画的关键帧数据以及关键帧间的插值器类型。

ArkGraphics 3D提供播放并控制场景动画的能力，支持开发者灵活地控制动画的状态，达到预期的渲染效果。

## 开发步骤

1. 导入相关模块。

   在页面脚本中导入ArkGraphics 3D提供的核心类型，用于创建和控制3D场景、相机以及动画资源。

   ```typescript
   import { Animation, Camera, Scene, SceneResourceFactory } from '@kit.ArkGraphics3D';
   ```
2. 加载场景资源。

   调用Scene.load()方法从应用的resources/rawfile/目录加载.glb（或.gltf）模型，并在加载完成后获取Scene对象。

   ```typescript
   Scene.load($rawfile('gltf/BrainStem/glTF/BrainStem.glb'))
     .then(async (result: Scene) => {
       this.scene = result;
       let rf: SceneResourceFactory = this.scene.getResourceFactory();
       // ...
     }).catch((err: string) => {
       console.error(err);
   });
   ```
3. 获取动画并注册回调。

   从scene.animations[0]获取动画资源，启用并注册onStarted()、onFinished()回调，用于监听动画播放状态或触发逻辑。

   ArkGraphics 3D提供以下动画回调接口：

   * onStarted()：动画开始播放时触发，start与restart操作均会触发该回调。
   * onFinished()：动画播放完成或执行finish操作时触发。

   ```typescript
   this.anim = this.scene.animations[0];
   if (this.anim) {
     this.anim.enabled = true;
     // Register callback function
     this.anim.onStarted(() => {
       // ...
       this.animationCallbackInvoked = 'animation on start';
     });

     this.anim.onFinished(() => {
       // ...
       this.animationCallbackInvoked = 'animation on finish';
     });
     // ...
   } else {
     console.error('No animation found in scene.');
   }
   ```
4. 创建相机与设置场景渲染参数。

   通过SceneResourceFactory.createCamera()创建相机并调整观察位置。随后将加载完成的Scene封装为SceneOptions，并指定渲染类型为ModelType.SURFACE，以便通过Component3D在界面上进行渲染。

   ```typescript
   // create a new camera.
   this.cam = await rf.createCamera({ 'name': 'Camera' });
   // set the camera.
   this.cam.enabled = true;
   this.cam.position.z = 5;
   this.sceneOpt = { scene: this.scene, modelType: ModelType.SURFACE } as SceneOptions;
   ```
5. 构建界面与动画控制。

   通过Component3D渲染3D场景，并在界面中添加按钮以控制动画播放状态。

   ArkGraphics 3D提供的动画状态控制操作主要包含如下几种：

   * 开始（start）：基于当前进度开始播放一个动画。
   * 停止（stop）：停止播放一个动画，并将动画的进度设置到未开始状态。
   * 结束（finish）：直接跳转到动画的最后，并将动画的进度设置到已结束状态。
   * 暂停（pause）：将动画暂停，动画的播放进度保持在当前状态。
   * 重启（restart）：从动画的起点开始播放动画。
   * 跳转（seek）：按比例跳转动画进度（例如seek(0.3)跳至总时长的30%）。

   ```typescript
   Button('start')
     // ...
     .onClick(async () => {
       if (!this.scene || !this.scene.animations[0]) {
         return;
       }
       this.anim = this.scene.animations[0];
       this.anim.start();
     });

   Button('pause')
     // ...
     .onClick(async () => {
       if (!this.scene || !this.scene.animations[0]) {
         return;
       }
       this.anim = this.scene.animations[0];
       this.anim.pause();
     });

   Button('stop')
     // ...
     .onClick(async () => {
       if (!this.scene || !this.scene.animations[0]) {
         return;
       }
       this.anim = this.scene.animations[0];
       this.anim.stop();
     });

   Button('finish')
     // ...
     .onClick(async () => {
       if (!this.scene || !this.scene.animations[0]) {
         return;
       }
       this.anim = this.scene.animations[0];
       this.anim.finish();
     });

   Button('restart')
     // ...
     .onClick(async () => {
       if (!this.scene || !this.scene.animations[0]) {
         return;
       }
       this.anim = this.scene.animations[0];
       this.anim.restart();
     });

   Button('seek to 30% progress')
     // ...
     .onClick(async () => {
       if (!this.scene || !this.scene.animations[0]) {
         return;
       }
       this.anim = this.scene.animations[0];
       // seek to 30%
       this.anim.seek(0.3);
     });
   ```

## 示例代码

* [基于3D引擎接口实现3D图形渲染功能（ArkTS）](https://gitcode.com/HarmonyOS_Samples/Graphics3D)
