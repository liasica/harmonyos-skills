---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-animation
title: 相机基础动效(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > 相机基础动效(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-29T13:34:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6e7eb1647296f7fb2144f41908861df3a19fe0ac088c046afda28cfb26d1bc02
---

在使用相机过程中，当遇到相机模式切换、前后置镜头切换等场景时，会不可避免地出现预览流替换。为优化用户体验，可合理使用动效过渡。本文主要介绍如何使用预览流截图，并通过ArkUI提供的[animateToImmediately](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animatetoimmediately23)接口触发显式动画功能，实现下方三种核心场景动效。

* 模式切换动效，使用预览流截图做模糊动效过渡。

  图片为从录像模式切换为拍照模式的效果。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/ii7HuZBLTLSBu0-LcXaLFA/zh-cn_image_0000002589244873.gif?HW-CC-KV=V1&HW-CC-Date=20260429T053457Z&HW-CC-Expire=86400&HW-CC-Sign=8542FFDFF1CB73093373500DA524A8CE60941ADC759632DDD4F6DA093D2B93FC)
* 前后置切换动效，使用预览流截图做翻转模糊动效过渡。

  图片为从前置相机切换为后置相机的效果。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/K4rnEp_1QnS8zZRxx-6AtQ/zh-cn_image_0000002558765068.gif?HW-CC-KV=V1&HW-CC-Date=20260429T053457Z&HW-CC-Expire=86400&HW-CC-Sign=8D7F6754CEDB99655856F7449B9ADC7F6DA81EFEC597388FB90BBC3757E08A8C)
* 拍照闪黑动效，使用闪黑组件覆盖预览流实现闪黑动效过渡。

  图片为点击完成拍摄的效果。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/KXymBP9FQ8-k6Bn3I8UQVw/zh-cn_image_0000002558605412.gif?HW-CC-KV=V1&HW-CC-Date=20260429T053457Z&HW-CC-Expire=86400&HW-CC-Sign=59FA88E7B325E5E0CE8BDBBAC7D439BF69BB9BE541CE522DE8F986D39E0D18D7)

## 闪黑动效

使用组件覆盖的形式实现闪黑效果。

以下步骤中的示例代码均为自定义组件（即被@Component修饰的组件）的内部方法或逻辑。

1. 导入依赖，需要导入相机框架、图片、ArkUI相关领域依赖。

   ```
   1. import { camera } from '@kit.CameraKit';
   2. import { image } from '@kit.ImageKit';
   3. import { curves } from '@kit.ArkUI';
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/cameraAnimSample/entry/src/main/ets/pages/Index.ets#L16-L20)
2. 构建闪黑组件。

   此处定义一个闪黑组件，在拍照闪黑及前后置切换时显示，用来遮挡XComponent组件。

   属性定义：

   ```
   1. @State isShowBlur: boolean = false;
   2. @State isShowBlack: boolean = false;
   3. @StorageLink('modeChange') @Watch('onModeChange') modeChangeFlag: number = 0;
   4. @StorageLink('switchCamera') @Watch('onSwitchCamera') switchCameraFlag: number = 0;
   5. @StorageLink('frameStart') @Watch('onFrameStart') frameStartFlag: number = 0;
   6. @StorageLink('captureClick') @Watch('onCaptureClick') captureClickFlag: number = 0;
   7. @StorageLink('surfaceShot') screenshotPixelMap: image.PixelMap | undefined = undefined; // 预览流截图。
   8. @StorageLink('curPosition') curPosition: number = 0; // 当前镜头前后置状态。
   9. @State shotImgBlur: number = 0;
   10. @State shotImgOpacity: number = 1;
   11. @State shotImgScale: ScaleOptions = { x: 1, y: 1 };
   12. @State shotImgRotation: RotateOptions = { y: BlurAnimateUtil.ROTATE_AXIS, angle: BlurAnimateUtil.IMG_FLIP_ANGLE_0 }
   13. @State flashBlackOpacity: number = 1;
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/cameraAnimSample/entry/src/main/ets/pages/Index.ets#L51-L65)

   闪黑组件的实现逻辑参考：

   ```
   1. // 拍照闪黑及前后置切换时显示，用来遮挡XComponent组件。
   2. if (this.isShowBlack) {
   3. Column()
   4. .key('black')
   5. .width(this.getUIContext().px2vp(Constants.X_COMPONENT_SURFACE_HEIGHT))
   6. .height(this.getUIContext().px2vp(Constants.X_COMPONENT_SURFACE_WIDTH))
   7. .backgroundColor(Color.Black)
   8. .opacity(this.flashBlackOpacity)
   9. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/cameraAnimSample/entry/src/main/ets/pages/Index.ets#L373-L383)
3. 实现闪黑动效。

   ```
   1. private flashBlackAnim() {
   2. Logger.info(TAG, 'flashBlackAnim E');
   3. this.flashBlackOpacity = 1;
   4. this.isShowBlack = true;
   5. animateToImmediately({
   6. curve: curves.interpolatingSpring(1, 1, 410, 38),
   7. delay: 50,
   8. onFinish: () => {
   9. this.isShowBlack = false;
   10. this.flashBlackOpacity = 1;
   11. Logger.info(TAG, 'flashBlackAnim X');
   12. }
   13. }, () => {
   14. this.flashBlackOpacity = 0;
   15. })
   16. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/cameraAnimSample/entry/src/main/ets/pages/Index.ets#L296-L313)
4. 触发闪黑动效。

   点击或触控拍照按钮，更新[@StorageLink](arkts-appstorage.md#storagelink)绑定CaptureClick的值，触发onCaptureClick方法，动效开始播放。

   ```
   1. onCaptureClick(): void {
   2. Logger.info(TAG, 'onCaptureClick');
   3. this.flashBlackAnim();
   4. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/cameraAnimSample/entry/src/main/ets/pages/Index.ets#L337-L342)

## 模糊动效

通过预览流截图，实现模糊动效，从而完成模式切换，或是前后置切换的动效。

以下除了步骤2，其他步骤中的示例代码均为自定义组件（即被@Component修饰的组件）的内部方法或逻辑。

1. 导入依赖，需要导入相机框架、图片、ArkUI相关领域依赖。

   ```
   1. import { camera } from '@kit.CameraKit';
   2. import { image } from '@kit.ImageKit';
   3. import { curves } from '@kit.ArkUI';
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/cameraAnimSample/entry/src/main/ets/pages/Index.ets#L16-L20)
2. 获取预览流截图。

   预览流截图通过图形提供的[image.createPixelMapFromSurface](../harmonyos-references/arkts-apis-image-f.md#imagecreatepixelmapfromsurface11)接口实现，surfaceId为当前预览流的surfaceId，size为当前预览流profile的宽高。创建截图工具类（ts文件），导入依赖，导出获取截图方法供页面使用，截图工具类实现参考：

   ```
   1. export class BlurAnimateUtil {
   2. public static surfaceShot: image.PixelMap;
   3. // ...

   5. /**
   6. * 获取surface截图
   7. * @param surfaceId
   8. * @returns
   9. */
   10. public static async doSurfaceShot(surfaceId: string) {
   11. Logger.info(TAG, `doSurfaceShot surfaceId:${surfaceId}.`);
   12. if ('' === surfaceId) {
   13. Logger.error(TAG, 'surface not ready!');
   14. return;
   15. }
   16. try {
   17. if (this.surfaceShot) {
   18. await this.surfaceShot.release();
   19. }
   20. this.surfaceShot = await image.createPixelMapFromSurface(surfaceId, {
   21. size: { width: Constants.X_COMPONENT_SURFACE_WIDTH, height: Constants.X_COMPONENT_SURFACE_HEIGHT }, // 取预览流profile的宽高。
   22. x: 0,
   23. y: 0
   24. });
   25. let imageInfo: image.ImageInfo = await this.surfaceShot.getImageInfo();
   26. Logger.info('doSurfaceShot surfaceShot:' + JSON.stringify(imageInfo.size));
   27. } catch (err) {
   28. Logger.error(JSON.stringify(err))
   29. }
   30. }

   32. public static getSurfaceShot() {
   33. return this.surfaceShot;
   34. }
   35. }
   ```

   [BlurAnimateUtil.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/cameraAnimSample/entry/src/main/ets/common/utils/BlurAnimateUtil.ts#L22-L73)
3. 构建截图组件。

   此处定义一个截图组件，置于预览流XComponent组件之上，用来遮挡XComponent组件。

   属性定义：

   ```
   1. @State isShowBlur: boolean = false;
   2. @State isShowBlack: boolean = false;
   3. @StorageLink('modeChange') @Watch('onModeChange') modeChangeFlag: number = 0;
   4. @StorageLink('switchCamera') @Watch('onSwitchCamera') switchCameraFlag: number = 0;
   5. @StorageLink('frameStart') @Watch('onFrameStart') frameStartFlag: number = 0;
   6. @StorageLink('captureClick') @Watch('onCaptureClick') captureClickFlag: number = 0;
   7. @StorageLink('surfaceShot') screenshotPixelMap: image.PixelMap | undefined = undefined; // 预览流截图。
   8. @StorageLink('curPosition') curPosition: number = 0; // 当前镜头前后置状态。
   9. @State shotImgBlur: number = 0;
   10. @State shotImgOpacity: number = 1;
   11. @State shotImgScale: ScaleOptions = { x: 1, y: 1 };
   12. @State shotImgRotation: RotateOptions = { y: BlurAnimateUtil.ROTATE_AXIS, angle: BlurAnimateUtil.IMG_FLIP_ANGLE_0 }
   13. @State flashBlackOpacity: number = 1;
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/cameraAnimSample/entry/src/main/ets/pages/Index.ets#L51-L65)

   截图组件的实现参考：

   ```
   1. if (this.isShowBlur) {
   2. Column() {
   3. Image(this.screenshotPixelMap)
   4. .blur(this.shotImgBlur)
   5. .opacity(this.shotImgOpacity)
   6. .rotate(this.shotImgRotation)// ArkUI提供的旋转，用于组件沿指定坐标系进行旋转。
   7. .scale(this.shotImgScale)
   8. .width(this.getUIContext().px2vp(Constants.X_COMPONENT_SURFACE_HEIGHT))
   9. .height(this.getUIContext().px2vp(Constants.X_COMPONENT_SURFACE_WIDTH))
   10. .syncLoad(true)
   11. }
   12. .width(this.getUIContext().px2vp(Constants.X_COMPONENT_SURFACE_HEIGHT))
   13. .height(this.getUIContext().px2vp(Constants.X_COMPONENT_SURFACE_WIDTH))
   14. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/cameraAnimSample/entry/src/main/ets/pages/Index.ets#L385-L400)
4. （按实际情况选择）实现模糊出现动效。

   模式切换动效分两段实现，模糊出现动效和模糊消失动效。

   模糊出现动效：用户点击或触控事件触发预览流截图，显示截图组件，截图清晰到模糊，覆盖旧预览流。

   注意

   由于图形提供的[image.createPixelMapFromSurface](../harmonyos-references/arkts-apis-image-f.md#imagecreatepixelmapfromsurface11)接口是通过截取surface内容获取[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)，其内容和[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件绘制逻辑不同，需要根据**前后置**镜头做不同的**图片内容旋转补偿**和**组件旋转补偿**。

   ```
   1. private async showBlurAnim() {
   2. Logger.info(TAG, 'showBlurAnim E');
   3. // 获取已完成的surface截图。
   4. let shotPixel = BlurAnimateUtil.getSurfaceShot();
   5. // 后置。
   6. if (this.curPosition === 0) {
   7. Logger.info(TAG, 'showBlurAnim BACK');
   8. // 直板机后置截图旋转补偿90°。
   9. await shotPixel.rotate(BlurAnimateUtil.IMG_ROTATE_ANGLE_90);
   10. // 直板机后置截图初始翻转0°。
   11. this.shotImgRotation = { y: BlurAnimateUtil.ROTATE_AXIS, angle: BlurAnimateUtil.IMG_FLIP_ANGLE_0 };
   12. } else {
   13. Logger.info(TAG, 'showBlurAnim FRONT');
   14. // 直板机前置截图旋转补偿270°。
   15. await shotPixel.rotate(BlurAnimateUtil.IMG_ROTATE_ANGLE_270);
   16. // 直板机前置截图镜像补偿。
   17. this.shotImgRotation = { y: BlurAnimateUtil.ROTATE_AXIS, angle: BlurAnimateUtil.IMG_FLIP_ANGLE_180 };
   18. }
   19. this.screenshotPixelMap = shotPixel;
   20. // 初始化动效参数。
   21. this.shotImgBlur = 0; // 无模糊。
   22. this.shotImgOpacity = 1; // 不透明。
   23. // 触发页面渲染。
   24. this.isShowBlur = true;
   25. animateToImmediately(
   26. {
   27. duration: BlurAnimateUtil.SHOW_BLUR_DURATION,
   28. curve: Curve.Friction,
   29. onFinish: async () => {
   30. Logger.info(TAG, 'showBlurAnim X');
   31. }
   32. },
   33. () => {
   34. // 截图模糊度变化动效。
   35. this.shotImgBlur = BlurAnimateUtil.ANIM_MODE_SWITCH_BLUR;
   36. }
   37. );
   38. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/cameraAnimSample/entry/src/main/ets/pages/Index.ets#L93-L132)
5. 实现模糊消失动效。

   模糊消失动效：由新模式预览流首帧回调[on('frameStart')](../harmonyos-references/arkts-apis-camera-previewoutput.md#onframestart)触发，截图组件模糊到清晰，显示新预览流。

   ```
   1. private hideBlurAnim(): void {
   2. this.isShowBlack = false;
   3. Logger.info(TAG, 'hideBlurAnim E');
   4. animateToImmediately({
   5. duration: BlurAnimateUtil.HIDE_BLUR_DURATION,
   6. curve: Curve.FastOutSlowIn,
   7. onFinish: () => {
   8. // 模糊组件下树。
   9. this.isShowBlur = false;
   10. this.shotImgBlur = 0;
   11. this.shotImgOpacity = 1;
   12. Logger.info(TAG, 'hideBlurAnim X');
   13. }
   14. }, () => {
   15. // 截图透明度变化动效。
   16. this.shotImgOpacity = 0;
   17. });
   18. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/cameraAnimSample/entry/src/main/ets/pages/Index.ets#L137-L156)
6. （按实际情况选择）实现模糊翻转动效。

   模糊翻转动效分两段实现，模糊翻转动效和模糊消失动效，其中模糊消失动效同第5步。

   模糊翻转动效：分两段组件翻转实现，先向外翻转90°再向内翻转90°，同时还执行了模糊度、透明度、比例缩放等动效。

   为保证预览流在翻转时不露出，需要构建一个闪黑组件用于遮挡XComponent组件，构建方式参考[闪黑动效](camera-animation.md#闪黑动效)-步骤2。

   ```
   1. /**
   2. * 先向外翻转90°，前后置切换触发
   3. */
   4. private async rotateFirstAnim() {
   5. Logger.info(TAG, 'rotateFirstAnim E');
   6. // 获取已完成的surface截图。
   7. let shotPixel = BlurAnimateUtil.getSurfaceShot();
   8. // 后置切前置。
   9. if (this.curPosition === 1) {
   10. Logger.info(TAG, 'rotateFirstAnim BACK');
   11. // 直板机后置切前置截图旋转补偿90°。
   12. await shotPixel.rotate(BlurAnimateUtil.IMG_ROTATE_ANGLE_90); // Image Kit提供的旋转，用于处理图片本身的旋转。
   13. // 直板机后置切前置截图初始翻转0°。
   14. this.shotImgRotation = { y: BlurAnimateUtil.ROTATE_AXIS, angle: BlurAnimateUtil.IMG_FLIP_ANGLE_0 };
   15. } else {
   16. Logger.info(TAG, 'rotateFirstAnim FRONT');
   17. // 直板机前置切后置截图旋转补偿270°。
   18. await shotPixel.rotate(BlurAnimateUtil.IMG_ROTATE_ANGLE_270);
   19. // 直板机前置切后置截图初始翻转180°。
   20. this.shotImgRotation = { y: BlurAnimateUtil.ROTATE_AXIS, angle: BlurAnimateUtil.IMG_FLIP_ANGLE_180 };
   21. }
   22. this.screenshotPixelMap = shotPixel;
   23. // 触发页面渲染。
   24. this.isShowBlack = true;
   25. this.isShowBlur = true;
   26. animateToImmediately(
   27. {
   28. duration: BlurAnimateUtil.ROTATION_DURATION,
   29. delay: BlurAnimateUtil.FLIP_DELAY, // 时延保证组件缩放模糊动效先行，再翻转后视觉效果更好。
   30. curve: curves.cubicBezierCurve(0.20, 0.00, 0.83, 1.00),
   31. onFinish: () => {
   32. Logger.info(TAG, 'rotateFirstAnim X');
   33. // 在onFinish后触发二段旋转。
   34. this.rotateSecondAnim();
   35. }
   36. },
   37. () => {
   38. // 截图向翻转动效。
   39. if (this.curPosition === 1) {
   40. this.shotImgRotation = { y: BlurAnimateUtil.ROTATE_AXIS, angle: BlurAnimateUtil.IMG_FLIP_ANGLE_90 };
   41. } else {
   42. this.shotImgRotation = { y: BlurAnimateUtil.ROTATE_AXIS, angle: BlurAnimateUtil.IMG_FLIP_ANGLE_270 };
   43. }
   44. }
   45. )
   46. }

   48. /**
   49. * 再向内翻转90°
   50. */
   51. async rotateSecondAnim() {
   52. Logger.info(TAG, 'rotateSecondAnim E');
   53. // 获取已完成的surface截图。
   54. let shotPixel = BlurAnimateUtil.getSurfaceShot();
   55. // 后置。
   56. if (this.curPosition === 1) {
   57. // 直板机后置镜头旋转补偿90°。
   58. await shotPixel.rotate(BlurAnimateUtil.IMG_ROTATE_ANGLE_90); // Image Kit提供的旋转，用于处理图片本身的旋转。
   59. // 瞬时调整为-90°，保证二段旋转后，图片不是镜像的。
   60. this.shotImgRotation = { y: BlurAnimateUtil.ROTATE_AXIS, angle: BlurAnimateUtil.IMG_FLIP_ANGLE_MINUS_90 };
   61. } else { // 前置。
   62. // 直板机前置截图旋转补偿270°。
   63. await shotPixel.rotate(BlurAnimateUtil.IMG_ROTATE_ANGLE_270);
   64. // 直板机前置截图镜像补偿。
   65. this.shotImgRotation = { y: BlurAnimateUtil.ROTATE_AXIS, angle: BlurAnimateUtil.IMG_FLIP_ANGLE_180 };
   66. }
   67. this.screenshotPixelMap = shotPixel;

   69. animateToImmediately(
   70. {
   71. duration: BlurAnimateUtil.ROTATION_DURATION,
   72. curve: curves.cubicBezierCurve(0.17, 0.00, 0.20, 1.00),
   73. onFinish: () => {
   74. Logger.info(TAG, 'rotateSecondAnim X');
   75. }
   76. },
   77. () => {
   78. // 截图翻转为初始状态。
   79. if (this.curPosition === 1) {
   80. this.shotImgRotation = { y: BlurAnimateUtil.ROTATE_AXIS, angle: BlurAnimateUtil.IMG_FLIP_ANGLE_0 };
   81. } else {
   82. this.shotImgRotation = { y: BlurAnimateUtil.ROTATE_AXIS, angle: BlurAnimateUtil.IMG_FLIP_ANGLE_180 };
   83. }
   84. }
   85. )
   86. }

   88. /**
   89. * 向外翻转90°同时
   90. */
   91. blurFirstAnim() {
   92. Logger.info(TAG, 'blurFirstAnim E');
   93. // 初始化动效参数。
   94. this.shotImgBlur = 0; // 无模糊。
   95. this.shotImgOpacity = 1; // 不透明。
   96. this.shotImgScale = { x: 1, y: 1 };
   97. animateToImmediately(
   98. {
   99. duration: BlurAnimateUtil.ROTATION_DURATION,
   100. curve: Curve.Sharp,
   101. onFinish: () => {
   102. Logger.info(TAG, 'blurFirstAnim X');
   103. this.blurSecondAnim();
   104. }
   105. },
   106. () => {
   107. // 截图模糊度变化动效。
   108. this.shotImgBlur = BlurAnimateUtil.ANIM_MODE_SWITCH_BLUR;
   109. // 截图比例动效。
   110. this.shotImgScale = { x: BlurAnimateUtil.IMG_SCALE, y: BlurAnimateUtil.IMG_SCALE };
   111. }
   112. );
   113. }

   115. /**
   116. * 向内翻转90°同时
   117. */
   118. blurSecondAnim() {
   119. Logger.info(TAG, 'blurSecondAnim E');
   120. animateToImmediately(
   121. {
   122. duration: BlurAnimateUtil.ROTATION_DURATION,
   123. curve: Curve.Sharp,
   124. onFinish: () => {
   125. Logger.info(TAG, 'blurSecondAnim X');
   126. }
   127. },
   128. () => {
   129. this.shotImgScale = { x: 1, y: 1 };
   130. }
   131. )
   132. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/cameraAnimSample/entry/src/main/ets/pages/Index.ets#L158-L291)
7. 按需触发动效。

   模式切换动效触发：点击或触控模式按钮立即执行doSurfaceShot截图方法，更新[@StorageLink](arkts-appstorage.md#storagelink)绑定modeChange的值，触发onModeChange方法，开始动效。

   ```
   1. onModeChange(): void {
   2. Logger.info(TAG, 'onModeChange');
   3. this.showBlurAnim();
   4. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/cameraAnimSample/entry/src/main/ets/pages/Index.ets#L315-L320)

   前后置切换动效触发：点击或触控前后置切换按钮立即执行doSurfaceShot截图方法，更新[@StorageLink](arkts-appstorage.md#storagelink)绑定switchCamera的值，触发onSwitchCamera方法，开始动效。

   ```
   1. onSwitchCamera(): void {
   2. Logger.info(TAG, 'onSwitchCamera');
   3. this.blurFirstAnim();
   4. this.rotateFirstAnim();
   5. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/cameraAnimSample/entry/src/main/ets/pages/Index.ets#L322-L328)

   模糊消失动效触发：监听预览流首帧回调[on('frameStart')](../harmonyos-references/arkts-apis-camera-previewoutput.md#onframestart)，更新[@StorageLink](arkts-appstorage.md#storagelink)绑定frameStart的值，触发onFrameStart方法，开始动效。

   ```
   1. onFrameStart(): void {
   2. Logger.info(TAG, 'onFrameStart');
   3. this.hideBlurAnim();
   4. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/cameraAnimSample/entry/src/main/ets/pages/Index.ets#L330-L335)
