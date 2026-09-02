---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-23
title: 如何实现前置镜头的录像镜像功能
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 如何实现前置镜头的录像镜像功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c01fc0074028e57bbd05c27dec47dc9bd776d0f04f66e8cbefd53e3b498e15e9
---

录像的前置镜头录像，需要开启镜像功能，调用[enableMirror()](../harmonyos-references/arkts-apis-camera-videooutput.md#enablemirror15)可以启用/关闭镜像录像。

启用镜像录像前需要先通过[isMirrorSupported](../harmonyos-references/arkts-apis-camera-videooutput.md#ismirrorsupported15)查询是否支持录像镜像功能，示例代码如下：

```typescript
function testIsMirrorSupported(videoOutput: camera.VideoOutput): boolean {
  let isSupported: boolean = videoOutput.isMirrorSupported();
  return isSupported;
}
```

* 若支持录像镜像功能，调用[enableMirror()](../harmonyos-references/arkts-apis-camera-videooutput.md#enablemirror15)可以启用/关闭镜像录像。示例代码如下：

  ```typescript
  import { camera } from '@kit.CameraKit';
  import { media } from '@kit.MediaKit';
  import { BusinessError } from '@kit.BasicServicesKit';

  // ...

  function enableMirror(videoOutput: camera.VideoOutput, mirrorMode: boolean): void {
    try {
      videoOutput.enableMirror(mirrorMode);
    } catch (error) {
      let err = error as BusinessError;
    }
  }
  ```

  启用/关闭录像镜像后，需要通过[getVideoRotation](../harmonyos-references/arkts-apis-camera-videooutput.md#getvideorotation12)以及[updateRotation](../harmonyos-references/arkts-apis-media-avrecorder.md#updaterotation12)更新旋转角度。
* 若不支持录像镜像功能，可以使用[rotate](../harmonyos-references/ts-universal-attributes-transformation.md#rotate)实现组件翻转效果，对预览流进行镜像，方便用户对录像内容进行预览，之后对录像文件单独处理，利用三方库FFmpeg实现录像文件的内容镜像。
  1. 录像预览流设置：使用rotate对预览流组件XComponent进行镜像翻转，代码示例如下：

     ```typescript
     // Flip Angle
     @State angle: number = 180;
     // Use rotate to control whether the preview stream component XComponent is mirrored
     XComponent({
       type: XComponentType.SURFACE,
       controller: this.mXComponentController,
       imageAIOptions: {
         types: [ImageAnalyzerType.SUBJECT],
         aiController: this.aiController
       }
     })
       .onLoad(() => {
         // The aspect ratio of the preview stream must match that of the recording output stream
         this.mXComponentController.setXComponentSurfaceRect({
           surfaceWidth: this.videoSize.width,
           surfaceHeight: this.videoSize.height
         });
         this.surfaceId = this.mXComponentController.getXComponentSurfaceId()
       })
       .width(StyleConstants.FULL_WIDTH)
       .height(StyleConstants.XCOMPONENT_HEIGHT)
       .rotate({ y: 1, angle: this.angle, })
     ```
  2. 使用FFmpeg三方库的能力，对录像文件内容镜像。执行镜像操作前，需要先安装，具体步骤可参考[FFmpeg官网](https://ohpm.openharmony.cn/#/cn/detail/@sj%2Fffmpeg)。镜像命令执行代码如下：

     ```typescript
     import { FFProgressMessageParser, FFmpeg } from '@sj/ffmpeg';

     let commands = ["ffmpeg", "-i", inputPath, "-vf", "hflip", outputPath];
     FFmpeg.execute(commands, {
       logCallback: (logLevel: number, logMessage: string) => console.log(`[${logLevel}]${logMessage}`),
       progressCallback: (message: string) =>  console.log(`[progress]${JSON.stringify(FFProgressMessageParser.parse(message))}`),
     }).then(() => {
       console.info("FFmpeg execution succeeded.");
     }).catch((error: Error) => {
       console.error("FFmpeg execution failed with error: ${error.message}");
     });
     ```
