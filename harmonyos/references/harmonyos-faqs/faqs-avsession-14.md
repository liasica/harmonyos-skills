---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avsession-14
title: 如何将图片合成视频
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频编解码（AVCodec） > 如何将图片合成视频
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:45+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:38bef282e61068c9892cd9560efb74f886c47b6e9d3024298ff5c303e8dddf56
---

使用AVCodec Kit将图片合成视频，具体操作步骤如下：

1. 在ArkTS侧使用ImageSource将图片解码为PixelMap对象，具体参考指南：[使用ImageSource完成图片解码](../harmonyos-guides/image-decoding.md)。
2. 将PixelMap对象通过NDK跨语言交互流程传入Native侧。
3. 在Native侧通过OH\_PixelmapNative\_ConvertPixelmapNativeFromNapi获取ArkTS侧传过来的PixelMap对象，并存入OH\_PixelmapNative变量中。
4. 通过OH\_PixelmapImageInfo\_Create和OH\_PixelmapNative\_GetImageInfo获取PixelMap的像素信息，包括宽高、行跨距、像素格式以及是否为HDR等。各信息get接口具体为：OH\_PixelmapImageInfo\_GetWidth、OH\_PixelmapImageInfo\_GetHeight、OH\_PixelmapImageInfo\_GetPixelFormat。具体参考指南：[使用Image\_NativeModule完成位图操作](../harmonyos-guides/pixelmap-c.md)。
5. 通过OH\_PixelmapNative\_ReadPixels读取图像像素数据，并按照PixelMap的像素格式写入缓冲区buffer中。
6. 根据上述像素信息创建视频编码器VideoEncoder和媒体封装器Muxer，并初始化编码环境，包括编码参数设置、OnNeedInputBuffer和OnNewOutputBuffer回调注册等。该步骤的开发细节可参考Sample：[基于AVCodec能力的视频编解码](https://gitcode.com/harmonyos_samples/AVCodecVideo)。
7. 启动编码输入线程和编码输出线程。在输入线程中，将上述缓冲区buffer中的PixelMap数据通过OH\_VideoEncoder\_PushInputBuffer写入视频编码器中。在输出线程中，将视频编码器处理后的数据通过OH\_AVMuxer\_WriteSampleBuffer写入媒体封装器中，以供封装器进行视频文件封装。最后通过OH\_VideoEncoder\_FreeOutputBuffer释放编码器buffer，并实现轮转。
