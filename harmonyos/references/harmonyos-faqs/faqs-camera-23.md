---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-23
title: 如何实现前置镜头的录像镜像功能
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 如何实现前置镜头的录像镜像功能
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:29+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:43b5b0a48b49d330c41418e0b30fd718129b3d249bdc1525bf89acb44b87f3be
---

录像的前置镜头录像，需要开启镜像功能，调用[enableMirror()](../harmonyos-references/arkts-apis-camera-videooutput.md#enablemirror15)可以启用/关闭镜像录像。

启用镜像录像前需要先通过[isMirrorSupported](../harmonyos-references/arkts-apis-camera-videooutput.md#ismirrorsupported15)查询是否支持录像镜像功能，示例代码如下：

```
1. function testIsMirrorSupported(videoOutput: camera.VideoOutput): boolean {
2. let isSupported: boolean = videoOutput.isMirrorSupported();
3. return isSupported;
4. }
```

* 若支持录像镜像功能，调用[enableMirror()](../harmonyos-references/arkts-apis-camera-videooutput.md#enablemirror15)可以启用/关闭镜像录像。示例代码如下：

  ```
  1. import { camera } from '@kit.CameraKit';
  2. import { media } from '@kit.MediaKit';
  3. import { BusinessError } from '@kit.BasicServicesKit';

  5. // ...

  7. function enableMirror(videoOutput: camera.VideoOutput, mirrorMode: boolean): void {
  8. try {
  9. videoOutput.enableMirror(mirrorMode);
  10. } catch (error) {
  11. let err = error as BusinessError;
  12. }
  13. }
  ```

  启用/关闭录像镜像后，需要通过[getVideoRotation](../harmonyos-references/arkts-apis-camera-videooutput.md#getvideorotation12)以及[updateRotation](../harmonyos-references/arkts-apis-media-avrecorder.md#updaterotation12)更新旋转角度。
* 若不支持录像镜像功能，可以使用[rotate](../harmonyos-references/ts-universal-attributes-transformation.md#rotate)实现组件翻转效果，对预览流进行镜像，方便用户对录像内容进行预览，之后对录像文件单独处理，利用三方库FFmpeg实现录像文件的内容镜像。
  1. 录像预览流设置：使用rotate对预览流组件XComponent进行镜像翻转，代码示例如下：

     ```
     1. // Flip Angle
     2. @State angle: number = 180;
     3. // Use rotate to control whether the preview stream component XComponent is mirrored
     4. XComponent({
     5. type: XComponentType.SURFACE,
     6. controller: this.mXComponentController,
     7. imageAIOptions: {
     8. types: [ImageAnalyzerType.SUBJECT],
     9. aiController: this.aiController
     10. }
     11. })
     12. .onLoad(() => {
     13. // The aspect ratio of the preview stream must match that of the recording output stream
     14. this.mXComponentController.setXComponentSurfaceRect({
     15. surfaceWidth: this.videoSize.width,
     16. surfaceHeight: this.videoSize.height
     17. });
     18. this.surfaceId = this.mXComponentController.getXComponentSurfaceId()
     19. })
     20. .width(StyleConstants.FULL_WIDTH)
     21. .height(StyleConstants.XCOMPONENT_HEIGHT)
     22. .rotate({ y: 1, angle: this.angle, })
     ```
  2. 使用FFmpeg三方库的能力，对录像文件内容镜像。执行镜像操作前，需要先安装，具体步骤可参考[FFmpeg官网](https://ohpm.openharmony.cn/#/cn/detail/@sj%2Fffmpeg)。镜像命令执行代码如下：

     ```
     1. import { FFProgressMessageParser, FFmpeg } from '@sj/ffmpeg';

     3. let commands = ["ffmpeg", "-i", inputPath, "-vf", "hflip", outputPath];
     4. FFmpeg.execute(commands, {
     5. logCallback: (logLevel: number, logMessage: string) => console.log(`[${logLevel}]${logMessage}`),
     6. progressCallback: (message: string) =>  console.log(`[progress]${JSON.stringify(FFProgressMessageParser.parse(message))}`),
     7. }).then(() => {
     8. console.info("FFmpeg execution succeeded.");
     9. }).catch((error: Error) => {
     10. console.error("FFmpeg execution failed with error: ${error.message}");
     11. });
     ```
