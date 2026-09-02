---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avcodec-24
title: 如何为AI合成的媒体文件添加隐式标识
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频编解码（AVCodec） > 如何为AI合成的媒体文件添加隐式标识
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:46+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:2fc17d43137dbf18d6589b3a334b99d21c94c791a5e213941eaa9b7012355655
---

## 问题现象

根据HarmonyOS应用上架要求，对于人工智能合成的内容，需要在合成内容的文件元数据中添加隐式标识。如何为人工智能合成的媒体文件（图片、音频、视频）添加文件隐式标识。

## 背景知识

* 文件元数据指的是按照特定编码格式嵌入到文件头部的描述性信息，用于记录文件来源、属性、用途、版权等信息。
* 依照《人工智能生成合成内容标识方法》的规定，服务提供者需要在生成合成内容的文件元数据中添加隐式标识。具体可参考：[添加生成合成内容文件元数据隐式标识的具体方法是什么](../app/50111-10.md#section3871118114720)。
* [@ohos/mp4parser(V2.0.7)](https://ohpm.openharmony.cn/#/cn/detail/@ohos%2Fmp4parser)是用于编辑音视频文件的三方库，可以调用ffmpeg命令完成音视频文件的编辑，比如新增或者修改音视频文件的元数据。
* EXIF（Exchangeable image file format）是专门为数码相机的照片设定的文件格式，可以记录数码照片的属性信息和拍摄数据。[ImageSource](../harmonyos-references/arkts-apis-image-imagesource.md)的[modifyImageProperty](../harmonyos-references/arkts-apis-image-imagesource.md#modifyimageproperty11)可以修改图片文件的EXIF，为图片增加文件元数据信息。

## 解决方案

对于音视频媒体文件可以使用ffmpeg工具为音视频文件添加元数据，在HarmonyOS中可以使用三方库[@ohos/mp4parser(V2.0.7)](https://ohpm.openharmony.cn/#/cn/detail/@ohos%2Fmp4parser)调用ffmpeg命令为音视频文件添加隐式标识。对于图片文件，通过[modifyImageProperty](../harmonyos-references/arkts-apis-image-imagesource.md#modifyimageproperty11)接口将隐式元数据标识添加到图片的EXIF属性UserComment中。

1. 对于人工智能合成的音频（m4a, mp3）以及视频文件(mp4, mkv)，直接使用三方库[@ohos/mp4parser(V2.0.7)](https://ohpm.openharmony.cn/#/cn/detail/@ohos%2Fmp4parser)调用ffmpeg命令添加文件隐式标识。参考代码如下：

   ```ts
   const AV_AIGC_METADATA =
     '{"Label":"value1","ContentProducer":"value2","ProduceID":"value3","ReservedCode1":"value4","ContentPropagator":"value5","PropagateID":"value6","ReservedCode2":"value7"}';

   /**
    *
    * @param inputPath 输入音视频文件的沙箱路径（无隐式标识）
    * @param outputPath 输出文件的沙箱路径（添加隐式标识）
    * @param aigcMetadata 需要写入的AIGC文件元数据
    * @returns
    */
   async function addAIGC4AVFile(inputPath: string, outputPath: string, aigcMetadata: string): Promise<void> {
     let callback: ICallBack = {
       callBackResult: (code: number) => {
         if (code === 0) {
           console.info('Add aigc metadata succeed');
         } else {
           console.error('Add aigc metadata failed');
         }
       },
     };
     let cmd =
       `ffmpeg -i ${inputPath} -metadata AIGC="${aigcMetadata}" -movflags use_metadata_tags -c copy ${outputPath} -y`;
     MP4Parser.ffmpegCmd(cmd, callback);
   }
   ```
2. 对于人工智能合成的图片文件（jpg、png），通过[modifyImageProperty](../harmonyos-references/arkts-apis-image-imagesource.md#modifyimageproperty11)接口添加文件隐式标识到图片的EXIF属性UserComment中。参考代码如下：

   ```ts
   const IMAGE_AIGC_METADATA =
     '{"AIGC":{"Label":"value1","ContentProducer":"value2","ProduceID":"value3","ReservedCode1":"value4","ContentPropagator":"value5","PropagateID":"value6","ReservedCode2":"value7"}}';

   /**
    *
    * @param imageFilePath 输入图片文件的沙箱路径
    * @param aigcMetadata 需要写入的AIGC文件元数据
    */
   async function addAIGC4ImageFile(imageFilePath: string, aigcMetadata: string) {
     let imageSource: image.ImageSource | undefined;
     try {
       imageSource = image.createImageSource(imageFilePath);
       await imageSource.modifyImageProperty(image.PropertyKey.USER_COMMENT, aigcMetadata);
       console.info(`Add aigc metadata succeed.`);
     } catch (error) {
       console.error(`Failed to invoke ImageSource.modifyImageProperty. Cause: ${JSON.stringify(error)}`);
     } finally {
       await imageSource?.release();
     }
   }
   ```

完整参考代码如下：

```ts
import { ICallBack, MP4Parser } from '@ohos/mp4parser';
import image from '@ohos.multimedia.image';
import { fileIo } from '@kit.CoreFileKit';

const AV_AIGC_METADATA =
  '{"Label":"value1","ContentProducer":"value2","ProduceID":"value3","ReservedCode1":"value4","ContentPropagator":"value5","PropagateID":"value6","ReservedCode2":"value7"}';

/**
 *
 * @param inputPath 输入音视频文件的沙箱路径（无隐式标识）
 * @param outputPath 输出文件的沙箱路径（添加隐式标识）
 * @param aigcMetadata 需要写入的AIGC文件元数据
 * @returns
 */
async function addAIGC4AVFile(inputPath: string, outputPath: string, aigcMetadata: string): Promise<void> {
  let callback: ICallBack = {
    callBackResult: (code: number) => {
      if (code === 0) {
        console.info('Add aigc metadata succeed');
      } else {
        console.error('Add aigc metadata failed');
      }
    },
  };
  let cmd =
    `ffmpeg -i ${inputPath} -metadata AIGC="${aigcMetadata}" -movflags use_metadata_tags -c copy ${outputPath} -y`;
  MP4Parser.ffmpegCmd(cmd, callback);
}

const IMAGE_AIGC_METADATA =
  '{"AIGC":{"Label":"value1","ContentProducer":"value2","ProduceID":"value3","ReservedCode1":"value4","ContentPropagator":"value5","PropagateID":"value6","ReservedCode2":"value7"}}';

/**
 *
 * @param imageFilePath 输入图片文件的沙箱路径
 * @param aigcMetadata 需要写入的AIGC文件元数据
 */
async function addAIGC4ImageFile(imageFilePath: string, aigcMetadata: string) {
  let imageSource: image.ImageSource | undefined;
  try {
    imageSource = image.createImageSource(imageFilePath);
    await imageSource.modifyImageProperty(image.PropertyKey.USER_COMMENT, aigcMetadata);
    console.info(`Add aigc metadata succeed.`);
  } catch (error) {
    console.error(`Failed to invoke ImageSource.modifyImageProperty. Cause: ${JSON.stringify(error)}`);
  } finally {
    await imageSource?.release();
  }
}

async function copyFile2Sandbox(rawFilePath: string, sandboxFilePath: string, context: Context) {
  let sandboxFile: fileIo.File | undefined;
  try {
    sandboxFile = await fileIo.open(sandboxFilePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.WRITE_ONLY);
    let content = await context.resourceManager.getRawFileContent(rawFilePath);
    await fileIo.write(sandboxFile.fd, content.buffer.slice(0));
  } catch (error) {
    console.error(`Failed to copy rawfile to sandbox. Cause: ${JSON.stringify(error)}`);
  } finally {
    if (sandboxFile) {
      await fileIo.close(sandboxFile.fd);
    }
  }
}

@Entry
@Component
struct Index {
  build() {
    Column({ space: 20 }) {
      Button('Video')
        .padding(9)
        .fontSize(30)
        .onClick(async () => {
          let context = this.getUIContext().getHostContext() as Context;
          const inputPath = context.filesDir + '/input.mp4';
          const outputPath = context.filesDir + '/output.mp4';
          await copyFile2Sandbox('input.mp4', inputPath, context); // input.mp4为rawfile文件，根据实际使用的文件替换
          await addAIGC4AVFile(inputPath, outputPath, AV_AIGC_METADATA);
        });

      Button('Audio')
        .padding(9)
        .fontSize(30)
        .onClick(async () => {
          let context = this.getUIContext().getHostContext() as Context;
          const inputPath = context.filesDir + '/input.m4a';
          const outputPath = context.filesDir + '/output.m4a';
          await copyFile2Sandbox('input.m4a', inputPath, context); // input.m4a为rawfile文件，根据实际使用的文件替换
          await addAIGC4AVFile(inputPath, outputPath, AV_AIGC_METADATA);
        });

      Button('Image')
        .padding(9)
        .fontSize(30)
        .onClick(async () => {
          let context = this.getUIContext().getHostContext() as Context;
          const inputPath = context.filesDir + '/image.jpg';
          await copyFile2Sandbox('image.jpg', inputPath, context); // image.jpg为rawfile文件，根据实际使用的文件替换
          await addAIGC4ImageFile(inputPath, IMAGE_AIGC_METADATA);
        });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center);
  }
}
```
