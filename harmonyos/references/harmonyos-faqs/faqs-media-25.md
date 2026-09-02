---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-25
title: 使用AVTranscoder进行视频转码失败
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > 使用AVTranscoder进行视频转码失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:27c1cdae34071f5e77a88d80a6a9632338bcefaed8908b433885e5b6d4d5ddca
---

## 问题现象

开发过程中，使用AVTranscoder进行视频转码时，会出现转码失败的场景，如何解决？

## 背景知识

* [AVTranscoder](../harmonyos-guides/media-kit-intro.md#avtranscoder)主要用于将已压缩编码的视频文件按照指定参数转换为另一种格式的视频。
* 支持修改源视频文件的编码参数（格式、码率）和封装格式。源视频的音视频编码和封装格式为系统AVCodec支持的解码和解封装格式，目标视频的音视频编码和封装格式为系统AVCodec支持的编码和封装格式，详情可以参考[AVCodec支持的格式](../harmonyos-guides/avcodec-support-formats.md)。

## 解决方案

下面列举转码过程中，常见的一些错误场景。

* **场景一**：视频转码失败并报错。

  ```txt
  code = 5400103 message = "IO Error: unknown error"
  ```

IO错误原因通常有：

* 源文件、输出文件配置错误，不可是同一个文件。
* 目标文件格式错误，当前输出视频文件仅支持mp4，可参考[AVTranscoderConfig.fileFormat](../harmonyos-references/arkts-apis-media-i.md#avtranscoderconfig12)参数说明，核心代码如下，完整代码可[参考官网](../harmonyos-guides/using-avtranscoder-for-transcodering.md)。

  ```ts
  private avConfig: media.AVTranscoderConfig = {
    audioBitrate: 100000, // 音频比特率。
    audioCodec: media.CodecMimeType.AUDIO_AAC, // 音频编码格式。
    fileFormat: media.ContainerFormatType.CFT_MPEG_4, // 封装格式。
    videoBitrate: 200000, // 视频比特率。
    videoCodec: media.CodecMimeType.VIDEO_AVC, // 视频编码格式。
    videoFrameWidth: 640, // 视频分辨率的宽为640。
    videoFrameHeight: 480, // 视频分辨率的高为480。
  };
  ```
* 文件路径设置错误，如果使用本地资源转码，必须确认资源文件可用，并使用应用沙箱路径访问对应资源，参考[获取应用文件路径](../harmonyos-guides/application-context-stage.md#获取应用文件路径)。应用沙箱的介绍及如何向应用沙箱推送文件，请参考[应用沙箱目录](../harmonyos-guides/app-sandbox-directory.md)。完整示例代码可以参考[使用AVTranscoder实现视频转码示例工程](../harmonyos-guides/using-avtranscoder-for-transcodering.md#运行示例工程)。

* **场景二：**视频转码失败并报错：

  ```txt
  #223 errCode: 5400103, errMsg: IO error happened due to Prepare.
  ```

  ```txt
  #64 SendErrorCallback:errorCode 401, errorMsg Invalid Parameter: invalid argument
  #67 can not find error callback!
  #83 StateChange, currentState: idle to state: error
  #213 failed to Prepare, param , errCode = -7
  #223 errCode: 5400103, errMsg: IO error happened due to Prepare.
  #755 SignedError: IO error happened due to Prepare.
  ```

  此错误通常是由于目标视频宽、高分辨率大于源视频宽、高，或设置为奇数导致，可以通过[AVTranscoderConfig](../harmonyos-references/arkts-apis-media-i.md#avtranscoderconfig12)配置合适的视频的宽高分辨率（不配置默认采用源视频的宽高）：

  ```ts
  private avConfig: media.AVTranscoderConfig = {
    audioBitrate: 100000, // 音频比特率。
    audioCodec: media.CodecMimeType.AUDIO_AAC, // 音频编码格式。
    fileFormat: media.ContainerFormatType.CFT_MPEG_4, // 封装格式。
    videoBitrate: 200000, // 视频比特率。
    videoCodec: media.CodecMimeType.VIDEO_AVC, // 视频编码格式。
    videoFrameWidth: 640, // 视频分辨率的宽为640。
    videoFrameHeight: 480, // 视频分辨率的高为480。
  };
  ```
* **场景三**：用户媒体相册里的文件怎么转码，需要复制到沙箱再转码吗？

  用户使用[photoViewPicker](../harmonyos-guides/photoaccesshelper-photoviewpicker.md)选择视频文件获取uri后，可通过[fs.opensync](../harmonyos-references/js-apis-file-fs.md#fileioopensync)获取源视频文件fd后直接转码，不用复制到沙箱再转，示例代码如下，完整代码可[参考官网](../harmonyos-guides/using-avtranscoder-for-transcodering.md)。

  ```ts
  async picture() {
    let PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
    PhotoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.VIDEO_TYPE;
    PhotoSelectOptions.maxSelectNumber = 1;
    let photoPicker = new photoAccessHelper.PhotoViewPicker();
    let pathDir = this.context?.filesDir;
    photoPicker.select(PhotoSelectOptions).then((PhotoSelectResult: photoAccessHelper.PhotoSelectResult) => {
      let photouri: Array<string> = PhotoSelectResult.photoUris;
      let file = fs.openSync(photouri[0], fs.OpenMode.READ_ONLY);
      let file2 = fs.openSync(pathDir + '/h264_1280_720.mp4', fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
      this.filePath = pathDir + '/h264_1280_720.mp4';
      fs.copyFileSync(file.fd, file2.fd);
      fs.closeSync(file);
      fs.closeSync(file2);
    });
  }
  ```
* **场景四**：需要提取mp4视频中音频到mp3音频文件怎么实现？

  AVTranscoder当前不支持mp4转mp3文件，可以使用三方库[@ohos/mp4parser](https://ohpm.openharmony.cn/#/cn/detail/@ohos%2Fmp4parser)通过执行FFmpeg命令实现。
* **场景五**：在传入文件入参不变的情况下，调用avTranscoder.prepare，有时会报错，有时正常，报错code：5400106。

  该错误是因为在设置输入文件fd句柄后，又将同一个资源句柄传递给一个或多个AVPlayer / AVMetadataExtractor / AVImageGenerator / AVTranscoder实例。这是不允许的，可以查看[AVTranscoder属性](../harmonyos-references/arkts-apis-media-avtranscoder.md)文档的fdSrc属性。如果需要用到原文件，可以将其复制进沙箱目录后再用复制后的文件fd句柄来代替原来的句柄fd。

## 常见FAQ

Q：是否支持MOV格式视频转码？

A：支持的，可参考[使用AVTranscoder实现视频转码](../harmonyos-guides/using-avtranscoder-for-transcodering.md)。

Q：参数设置不正常，如目标宽高参数小于源视频宽高，且码率设置远超源视频码率，转码后视频打开后没有画面，宽高分辨率均为0，并且码率也是0，这个压缩后的视频理论上说已经异常了，为什么回调的不是error方法呢？

A：根据[on('error')](../harmonyos-references/arkts-apis-media-avtranscoder.md#onerror12)可知，该回调仅用于错误提示。虽然参数不正常，但根据参数转码压缩并未出现错误提示，最终压缩转码成功，所以并未走error回调。
