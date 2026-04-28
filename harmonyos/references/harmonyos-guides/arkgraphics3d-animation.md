---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkgraphics3d-animation
title: ArkGraphics 3D场景动画控制以及管理
breadcrumb: 指南 > 图形 > ArkGraphics 3D（方舟3D图形） > ArkGraphics 3D场景动画控制以及管理
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:22+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:a43b3186d0edb74879fb9705e95baf6be1d12ff1f8acb2027a48aae0fe4ff95d
---

动画（animation）：动画是3D场景中重要的资源类型，用于控制场景中各种元素的运动。比如想要场景中的人物进行走路这个动作，每帧计算人物每一个关节的旋转角并进行设置是难以实现的。所以在完成类似的要求时，3D场景资源的制作者会将动画制作好，在模型文件中保存动画的关键帧数据以及关键帧间的插值器类型。

ArkGraphics 3D提供播放并控制场景动画的能力，支持开发者灵活地控制动画的状态，达到预期的渲染效果。

## 开发步骤

1. 导入相关模块。

   在页面脚本中导入ArkGraphics 3D提供的核心类型，用于创建和控制3D场景、相机以及动画资源。

   ```
   1. import { Animation, Camera, Scene, SceneResourceFactory } from '@kit.ArkGraphics3D';
   ```

   [animation.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/arkgraphic/animation.ets#L16-L18)
2. 加载场景资源。

   调用Scene.load()方法从应用的resources/rawfile/目录加载.glb（或.gltf）模型，并在加载完成后获取Scene对象。

   ```
   1. Scene.load($rawfile('gltf/BrainStem/glTF/BrainStem.glb'))
   2. .then(async (result: Scene) => {
   3. this.scene = result;
   4. let rf: SceneResourceFactory = this.scene.getResourceFactory();
   5. // ...
   6. }).catch((err: string) => {
   7. console.error(err);
   8. });
   ```

   [animation.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/arkgraphic/animation.ets#L48-L92)
3. 获取动画并注册回调。

   从scene.animations[0]获取动画资源，启用并注册onStarted()、onFinished()回调，用于监听动画播放状态或触发逻辑。

   ArkGraphics 3D提供以下动画回调接口：

   * onStarted()：动画开始播放时触发，start与restart操作均会触发该回调。
   * onFinished()：动画播放完成或执行finish操作时触发。

   ```
   1. this.anim = this.scene.animations[0];
   2. if (this.anim) {
   3. this.anim.enabled = true;
   4. // Register callback function
   5. this.anim.onStarted(() => {
   6. // ...
   7. this.animationCallbackInvoked = 'animation on start';
   8. });

   10. this.anim.onFinished(() => {
   11. // ...
   12. this.animationCallbackInvoked = 'animation on finish';
   13. });
   14. // ...
   15. } else {
   16. console.error('No animation found in scene.');
   17. }
   ```

   [animation.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/arkgraphic/animation.ets#L55-L79)
4. 创建相机与设置场景渲染参数。

   通过SceneResourceFactory.createCamera()创建相机并调整观察位置。随后将加载完成的Scene封装为SceneOptions，并指定渲染类型为ModelType.SURFACE，以便通过Component3D在界面上进行渲染。

   ```
   1. // create a new camera.
   2. this.cam = await rf.createCamera({ 'name': 'Camera' });
   3. // set the camera.
   4. this.cam.enabled = true;
   5. this.cam.position.z = 5;
   6. this.sceneOpt = { scene: this.scene, modelType: ModelType.SURFACE } as SceneOptions;
   ```

   [animation.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/arkgraphic/animation.ets#L80-L87)
5. 构建界面与动画控制。

   通过Component3D渲染3D场景，并在界面中添加按钮以控制动画播放状态。

   ArkGraphics 3D提供的动画状态控制操作主要包含如下几种：

   * 开始（start）：基于当前进度开始播放一个动画。
   * 停止（stop）：停止播放一个动画，并将动画的进度设置到未开始状态。
   * 结束（finish）：直接跳转到动画的最后，并将动画的进度设置到已结束状态。
   * 暂停（pause）：将动画暂停，动画的播放进度保持在当前状态。
   * 重启（restart）：从动画的起点开始播放动画。
   * 跳转（seek）：按比例跳转动画进度（例如seek(0.3)跳至总时长的30%）。

   ```
   1. Button('start')
   2. // ...
   3. .onClick(async () => {
   4. if (!this.scene || !this.scene.animations[0]) {
   5. return;
   6. }
   7. this.anim = this.scene.animations[0];
   8. this.anim.start();
   9. });

   11. Button('pause')
   12. // ...
   13. .onClick(async () => {
   14. if (!this.scene || !this.scene.animations[0]) {
   15. return;
   16. }
   17. this.anim = this.scene.animations[0];
   18. this.anim.pause();
   19. });

   21. Button('stop')
   22. // ...
   23. .onClick(async () => {
   24. if (!this.scene || !this.scene.animations[0]) {
   25. return;
   26. }
   27. this.anim = this.scene.animations[0];
   28. this.anim.stop();
   29. });

   31. Button('finish')
   32. // ...
   33. .onClick(async () => {
   34. if (!this.scene || !this.scene.animations[0]) {
   35. return;
   36. }
   37. this.anim = this.scene.animations[0];
   38. this.anim.finish();
   39. });

   41. Button('restart')
   42. // ...
   43. .onClick(async () => {
   44. if (!this.scene || !this.scene.animations[0]) {
   45. return;
   46. }
   47. this.anim = this.scene.animations[0];
   48. this.anim.restart();
   49. });

   51. Button('seek to 30% progress')
   52. // ...
   53. .onClick(async () => {
   54. if (!this.scene || !this.scene.animations[0]) {
   55. return;
   56. }
   57. this.anim = this.scene.animations[0];
   58. // seek to 30%
   59. this.anim.seek(0.3);
   60. });
   ```

   [animation.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics3D/entry/src/main/ets/arkgraphic/animation.ets#L113-L204)

## 示例代码

* [基于3D引擎接口实现3D图形渲染功能（ArkTS）](https://gitcode.com/HarmonyOS_Samples/Graphics3D)
