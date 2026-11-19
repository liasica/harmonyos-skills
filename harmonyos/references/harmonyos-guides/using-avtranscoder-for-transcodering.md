---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-avtranscoder-for-transcodering
title: 使用AVTranscoder实现音视频转码(ArkTS)
breadcrumb: 指南 > 媒体 > Media Kit（媒体服务） > 媒体开发指导(ArkTS) > 视频转码 > 使用AVTranscoder实现音视频转码(ArkTS)
category: harmonyos-guides
scraped_at: 2026-11-19T09:48:40+08:00
doc_updated_at: 2026-11-18
content_hash: sha256:7897efd5164abbbbf557e0f51851be14df798cafb6bf95387eb5ef6ab8e38736
---

使用[AVTranscoder](media-kit-intro.md#avtranscoder)可以实现视频转码功能，从API 20开始支持视频转码的C/C++开发，转码功能可在手机、平板、2in1设备上作为系统提供的基础能力使用。可以通过调用[canIUse](../harmonyos-references/js-apis-syscap.md#caniuse)接口来判断当前设备是否支持AVTranscoder，当canIUse("SystemCapability.Multimedia.Media.AVTranscoder")的返回值为true时，表示可以使用转码能力。

本开发指导将以“开始转码-暂停转码-恢复转码-转码完成”的一次流程为示例，向开发者讲解AVTranscoder视频转码相关功能。

## 整体框架与头文件引用

本示例的整体框架由界面（Index.ets）和转码功能管理类（AVTranscoderManager.ets）组成。界面负责用户交互和进度展示，转码功能管理类封装了完整的转码流程。开发前需引入以下头文件：

```typescript
import { media } from '@kit.MediaKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { fileIo } from '@kit.CoreFileKit';
```

转码功能管理类的整体结构如下：

```typescript
export class AVTranscoderDemo {
  private avTranscoder: media.AVTranscoder | undefined = undefined;
  private context: Context | undefined;
  private currentProgress: number = 0;
  constructor(context: Context | undefined) {
    if (context != undefined) {
      this.context = context;
    }
  }
  // ...
}
```

详细的API说明请参考[AVTranscoder](../harmonyos-references/arkts-apis-media-avtranscoder.md)。

**说明** 

如需对转码后的文件进行转发、上传、转存等处理，应用须收到complete事件后调用系统接口await avTranscoder.release()，以保证视频文件完整性。

## 开发步骤及注意事项

1. 创建[AVTranscoder](../harmonyos-references/arkts-apis-media-f.md#mediacreateavtranscoder12)实例。

   ```typescript
   // 1.创建转码实例。
   this.avTranscoder = await media.createAVTranscoder();
   ```
2. 设置业务需要的监听事件，监听状态变化及错误上报。

   | 事件类型 | 说明 |
   | --- | --- |
   | complete | 必要事件，监听AVTranscoder的转码完成。 |
   | error | 必要事件，监听AVTranscoder的错误信息。 |
   | progressUpdate | 监听AVTranscoder的进度。 |

   ```typescript
   // 注册avTranscoder回调函数。
   setAVTranscoderCallback() {
     if (canIUse('SystemCapability.Multimedia.Media.AVTranscoder')) {
       if (this.avTranscoder != undefined) {
         // 转码完成回调函数。
         this.avTranscoder.on('complete', async () => {
           console.info(`AVTranscoder is completed`);
           await this.releaseTranscoderingProcess();
         });
         // 错误上报回调函数。
         this.avTranscoder.on('error', (err: BusinessError) => {
           console.error(`AVTranscoder failed, code is ${err.code}, message is ${err.message}`);
         });
         // 进度上报回调函数。
         this.avTranscoder.on('progressUpdate', (progress: number) => {
           console.info(`AVTranscoder progressUpdate = ${progress}`);
           this.currentProgress = progress;
         })
       }
     }
   }
   // ...
   // 获取当前进度。
   getCurrentProgress(): number {
     console.info(`getCurrentProgress = ${this.currentProgress}`);
     return this.currentProgress;
   }
   ```
3. 设置源视频文件fd：设置属性fdSrc。

   **说明** 

   下面代码示例中的fdSrc仅作示意使用，开发者需根据实际情况，确认资源有效性并设置：

   * 如果使用本地资源转码，必须确认资源文件可用，并使用应用沙箱路径访问对应资源，参考[获取应用文件路径](application-context-stage.md#获取应用文件路径)。应用沙箱的介绍及如何向应用沙箱推送文件，请参考[应用沙箱目录](app-sandbox-directory.md)。
   * 应通过Context属性获取应用文件路径，建议使用getUIContext获取UIContext实例，并使用getHostContext调用绑定实例的getContext，请参考[getHostContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md#gethostcontext12)。
   * 如果使用ResourceManager.getRawFd()打开HAP资源文件描述符，使用方法可参考ResourceManager中的[getRawFd](../harmonyos-references/js-apis-resource-manager.md#getrawfd9)。

   ```typescript
   import {AVTranscoderDemo} from '../transcoder/AVTranscoderManager'

   @Entry
   @Component
   struct Index {
     // 获取当前组件所在Ability的Context，以通过Context获取应用文件路径。
     private context:Context | undefined = this.getUIContext().getHostContext();
     // 获取转码功能管理类。
     @State avTranscoder: AVTranscoderDemo = new AVTranscoderDemo(this.context);

     build() {
       RelativeContainer() {
         Column() {
           Button($r('app.string.StartTranscoder'))
             .onClick(async () => {
               console.info(`Button put`);
               await this.avTranscoder.avTranscoderDemo();
             })
             .id('AVTranscoderButton')
           Progress({ value: 0, total: 100, type: ProgressType.Linear }).value(this.avTranscoder.getCurrentProgress())
             .height(50)
             .width('80%')
         }
         .alignRules({
           center: { anchor: '__container__', align: VerticalAlign.Center },
           middle: { anchor: '__container__', align: HorizontalAlign.Center }
         })
       }
       .height('100%')
       .width('100%')
     }
   }
   ```

   ```typescript
   try {
     // 获取输入文件fd，H264_AAC.mp4为rawfile目录下的预置资源，需要开发者根据实际情况进行替换。
     let fileDescriptor = await this.context.resourceManager.getRawFd('H264_AAC.mp4');
     // 设置转码的源文件属性fdSrc。
     this.avTranscoder.fdSrc = fileDescriptor;
   } catch (error) {
     console.error('Failed to get the file descriptor, please check the resource and path.');
   }
   ```
4. 设置目标视频文件fd：设置属性fdDst。

   **说明** 

   转码输出文件fd（即示例里fdDst），形式为number。需要调用基础文件操作接口（[@ohos.file.fs (文件管理)](../harmonyos-references/js-apis-file-fs.md)）实现应用文件访问能力，获取方式参考[应用文件访问(ArkTS)](app-file-access.md)。

   ```typescript
   let outputFilePath = this.context.filesDir + '/output.mp4';
   let file = fileIo.openSync(outputFilePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
   // 设置转码的目标文件属性fdDst。
   this.avTranscoder.fdDst = file.fd;
   ```
5. 配置音视频转码参数，调用prepare()接口。

   **说明** 

   * 写入配置参数时需要注意，prepare()接口的入参avConfig中仅设置转码相关的配置参数。
   * 支持配置转码的数据格式请参考AVTranscoder[支持的格式](media-kit-intro.md#支持的格式)。

   ```typescript
   private avConfig: media.AVTranscoderConfig = {
     audioBitrate: 100000, // 音频比特率。
     audioCodec: media.CodecMimeType.AUDIO_AAC, // 音频编码格式。
     fileFormat: media.ContainerFormatType.CFT_MPEG_4, // 封装格式。
     videoBitrate: 200000, // 视频比特率。
     videoCodec: media.CodecMimeType.VIDEO_AVC, // 视频编码格式。
   };
   ```

   ```typescript
   // 3.配置转码参数完成准备工作。
   await this.avTranscoder.prepare(this.avConfig);
   ```

   可在avConfig中设置目标视频的分辨率。

   ```ts
   let avConfig: media.AVTranscoderConfig = {
     audioBitrate: 100000, // 音频比特率。
     audioCodec: media.CodecMimeType.AUDIO_AAC, // 音频编码格式。
     fileFormat: media.ContainerFormatType.CFT_MPEG_4, // 封装格式。
     videoBitrate: 2000000, // 视频比特率。
     videoCodec: media.CodecMimeType.VIDEO_AVC, // 视频编码格式。
     videoFrameWidth: 640, // 目标视频分辨率的宽为640。
     videoFrameHeight: 480, // 目标视频分辨率的高为480。
   };
   ```
6. 开始转码，调用start()接口。

   ```typescript
   // 4.开始转码。
   await this.avTranscoder.start();
   ```
7. 暂停转码，调用pause()接口。

   ```typescript
   // 暂停转码对应的流程。
   async pauseTranscoderingProcess() {
     if (canIUse('SystemCapability.Multimedia.Media.AVTranscoder')) {
       if (this.avTranscoder != undefined) { // 仅在调用start返回后调用pause为合理调用。
         await this.avTranscoder.pause();
       }
     }
   }
   ```
8. 恢复转码，调用resume()接口。

   ```typescript
   // 恢复对应的转码流程。
   async resumeTranscoderingProcess() {
     if (canIUse('SystemCapability.Multimedia.Media.AVTranscoder')) {
       if (this.avTranscoder != undefined) { // 仅在调用pause返回后调用resume为合理调用。
         await this.avTranscoder.resume();
       }
     }
   }
   ```
9. 销毁实例，调用release()接口，退出转码。

   ```typescript
   // 释放转码流程。
   async releaseTranscoderingProcess() {
     if (canIUse('SystemCapability.Multimedia.Media.AVTranscoder')) {
       if (this.avTranscoder != undefined) {
         // 1.释放转码实例。
         await this.avTranscoder.release();
         let lastFdDst = this.avTranscoder.fdDst;
         let lastFdSrc = this.avTranscoder.fdSrc;
         this.avTranscoder = undefined;
         // 2.关闭转码目标文件fd。
         if (lastFdDst != undefined) {
           fileIo.closeSync(lastFdDst);
         }
         // 3.关闭转码源文件fd。
         if (lastFdSrc != undefined) {
           fileIo.closeSync(lastFdSrc.fd);
         }
       }
     }
   }
   ```
10. 完整的【开始转码-暂停转码-恢复转码-转码完成】流程。

    ```typescript
    // 一个完整的【开始转码-暂停转码-恢复转码-转码完成】示例。
    async avTranscoderDemo() {
      await this.startTranscoderingProcess(); // 开始转码。
      await this.pauseTranscoderingProcess(); // 暂停转码。
      await this.resumeTranscoderingProcess(); // 恢复转码。
    }
    ```

## 运行示例工程

参考以下示例，完成“开始转码-暂停转码-恢复转码-转码完成”的完整流程。

1. 新建工程，下载[完整示例工程](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/AVTranscoder/AVTranscoderArkTS)，并将示例工程的资源复制到对应目录。

   ```txt
   AVTranscoderArkTS
   entry/src/main/ets/
   └── pages
   │    └── Index.ets (转码界面)
   │
   └── transcoder
       └── AVTranscoderManager.ets (转码功能)

   entry/src/main/resources/
   ├── base
   │   ├── element
   │   │   ├── color.json
   │   │   ├── float.json
   │   │   └── string.json
   │   └── media
   │
   └── rawfile
       └── H264_AAC.mp4 (视频资源)
   ```
2. 编译新建工程并运行。
