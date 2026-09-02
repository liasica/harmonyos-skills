---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-33
title: 录制过程中音视频帧数据的转换
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > 录制过程中音视频帧数据的转换
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ed6657ef3a7dd6f542f0e3a606f26108e0d3b1cb8018025ecb5e3bfa4749ee20
---

## 问题现象

通过OH\_AVScreenCapture获取原始码流的方式录制mp4文件，在录制过程中，需要将音视频帧转成图片或PCM数据，进行图像识别或语音识别，如何在录制过程中将音视频帧数据转换为JPEG图片或PCM音频。

## 背景知识

录屏取码流相关可详细参考[AVScreenCapture录屏取码流](../harmonyos-guides/using-avscreencapture-for-buffer.md)。通过录屏获取码流的方式获取的流数据可根据场景，进行不同的处理。例如：

* 对接NativeImage作为消费者端，提供Surface关联OpenGL外部纹理，具体使用请参考[NativeImage开发指导](../harmonyos-guides/native-image-guidelines.md)。
* 对接编码器、封装器进行数据的编码、封装，具体使用请参考[视频编码](../harmonyos-guides/video-encoding.md)、[媒体数据封装](../harmonyos-guides/audio-video-muxer.md)。
* 对接网络模块，上传流数据到服务器，具体使用请参考[实现同步读写流](../harmonyos-guides/remote-communication-syncstreamreq.md)。

## 解决方案

要在录制过程中获取音视频帧数据转换为对应格式的图片和音频，可以在[AVScreenCapture](../harmonyos-references/capi-avscreencapture.md)的OH\_AVBuffer中获取buffer流数据保存，再将保存的数据进行转换。

1. 从buffer流中获取数据，获取数据为PCM格式码流。

   ```cpp
   void Buffer2Png(OH_AVBuffer* buffer)
   {
       int bufferLen = OH_AVBuffer_GetCapacity(buffer);
       OH_LOG_INFO (LOG_APP,"png length: %{public}d",bufferLen);
       OH_NativeBuffer *nativeBuffer = OH_AVBuffer_GetNativeBuffer(buffer);
       OH_NativeBuffer_Config config;
       OH_NativeBuffer_GetConfig(nativeBuffer, &config);
       int32_t videoSize = config.height * config.width * 4;
       uint8_t *buf = OH_AVBuffer_GetAddr(buffer);
       TestSavePng(config.width, config.height, (uint8_t *)buf);
   }
   ```

   ```cpp
   void OnBufferAvailable(OH_AVScreenCapture *capture, OH_AVBuffer *buffer, OH_AVScreenCaptureBufferType bufferType, int64_t timestamp, void *userData) 
   {
       // 处于录屏取码流状态。
       if (g_isCaptureStreamRunning) {
           // 视频buffer。
           Buffer2Png(buffer);
           OH_LOG_INFO(LOG_APP, "this is an info level log");
       }
   }

   struct OH_AVScreenCapture * g_capture;
   // 开始录屏时调用StartScreenCapture。
   static napi_value StartScreenCapture(napi_env env, napi_callback_info info) 
   {
       size_t argc = 1;
       napi_value args[1] = {nullptr};
       // 获取参数。
       napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
       int32_t Frame_Rate;
       napi_get_value_int32(env, args[0], &Frame_Rate);
       g_isCaptureStreamRunning = true;
       // 实例化ScreenCapture。
       g_capture = OH_AVScreenCapture_Create();
       // 设置回调 。
       OH_AVScreenCapture_SetErrorCallback(g_capture, OnError, nullptr);
       OH_AVScreenCapture_SetStateCallback(g_capture, OnStateChange, nullptr);
       OH_AVScreenCapture_SetDataCallback(g_capture, OnBufferAvailable, nullptr);
       OH_VideoCaptureInfo videocapinfo = {.videoFrameWidth = 768, .videoFrameHeight = 1280, .videoSource = OH_VIDEO_SOURCE_SURFACE_RGBA};
       OH_VideoInfo videoinfo = {.videoCapInfo = videocapinfo};
       OH_AVScreenCaptureConfig config = {.captureMode = OH_CAPTURE_HOME_SCREEN,.dataType = OH_ORIGINAL_STREAM,.videoInfo = videoinfo};
       OH_AVScreenCapture_Init(g_capture, config);
       // 开始录屏。
       OH_AVScreenCapture_StartScreenCapture(g_capture);
       // mic开关设置。
       OH_AVScreenCapture_SetMicrophoneEnabled(g_capture, false);
       // 可选 设置录屏时的最大帧率 需在启动后调用。
       OH_AVScreenCapture_SetMaxVideoFrameRate(g_capture, Frame_Rate);
       // 返回调用结果，仅返回随意值。
       napi_value sum;
       napi_create_double(env, 0, &sum);
       return sum;
   }
   ```
2. 要将帧数据进行格式转换，可以将音视频buffer提取到的PCM格式数据，使用自定义PNG图片编码方法写进图片文件中。

   PNG图片由多个文件块构成，每个块都有特定的用途，常见PNG文件块组成如下表所示。

   | 块名 | 是否必须 | 说明 |
   | --- | --- | --- |
   | IHDR | 是 | 图像头信息（宽度、高度、比特深度、颜色类型等）。 |
   | PLTE | 否 | 调色板（仅当颜色类型为索引颜色时使用）。 |
   | tRNS | 否 | 透明度信息（仅当颜色类型为索引或 RGB 时使用）。 |
   | IDAT | 是 | 图像数据（经过压缩的图像像素数据）。 |
   | IEND | 是 | 图像结束标识。 |

   一个简单的PNG文件结构必须包含图像基本信息及图像数据。综上所述，可以参考以下步骤将录制传入的PCM格式buffer手动转化为PNG图片：

   1. 初始化定义CRC32冗余校验码，用于计算PNG文件中各块的校验和，验证数据完整性。
   2. 宏定义编码预处理函数，用于后续将buffer数据写入PNG各个文件块中。
   3. 将数据信息分别写入IHDR（图像头信息块），IDAT（图像数据块），IEND（图像结束标识）。

   完整示例参考如下：

   ```cpp
   void  Svpng (FILE* out, unsigned w, unsigned h, const  unsigned  char * img, int alpha);
   SVPNG_LINKAGE void Svpng(SVPNG_OUTPUT, unsigned w, unsigned h, const unsigned char* img, int alpha) 
   {
       static const unsigned T[] = { 0, 0x1db71064, 0x3b6e20c8, 0x26d930ac, 0x76dc4190, 0x6b6b51f4, 0x4db26158, 0x5005713c, 
       /* CRC32校验码表 */    0xedb88320, 0xf00f9344, 0xd6d6a3e8, 0xcb61b38c, 0x9b64c2b0, 0x86d3d2d4, 0xa00ae278, 0xbdbdf21c };
       unsigned a = 1, b = 0, c, p = w * (alpha ? 4 : 3) + 1, x, y, i;   /* 初始化CRC校验码的变量 */
   #define SVPNG_U8A(ua, l) do { \
       for (i = 0; i < (l); i++) { \
           SVPNG_PUT((ua)[i]); \
       } \
   } while(0)
   #define SVPNG_U32(u) do { \
       SVPNG_PUT(((u) >> 24) & 255); \
       SVPNG_PUT(((u) >> 16) & 255); \
       SVPNG_PUT(((u) >> 8) & 255); \
       SVPNG_PUT((u) & 255); \
   } while(0)
   #define SVPNG_U8C(u) do { \
       SVPNG_PUT(u); \
       c ^= (u); \
       c = (c >> 4) ^ T[c & 15]; \
       c = (c >> 4) ^ T[c & 15]; \
   } while(0)
   #define SVPNG_U8AC(ua, l) do { \
       for (i = 0; i < (l); i++) { \
           SVPNG_U8C((ua)[i]); \
       } \
   } while(0)
   #define SVPNG_U16LC(u) do { SVPNG_U8C((u) & 255); SVPNG_U8C(((u) >> 8) & 255); } while(0)
   #define SVPNG_U32C(u) do { SVPNG_U8C((u) >> 24); SVPNG_U8C(((u) >> 16) & 255); SVPNG_U8C(((u) >> 8) & 255); SVPNG_U8C((u) & 255); } while(0)
   #define SVPNG_U8ADLER(u) do { SVPNG_U8C(u); a = (a + (u)) % 65521; b = (b + a) % 65521; } while(0)
   #define SVPNG_BEGIN(s, l) do { SVPNG_U32(l); c = ~0U; SVPNG_U8AC(s, 4); } while(0)
   #define SVPNG_END() SVPNG_U32(~c)
       SVPNG_U8A("\x89PNG\r\n\32\n", 8);           /* 写入PNG文件头 */
       SVPNG_BEGIN("IHDR", 13);                    /* 将图像头信息写入IHDR块（图像头信息）中 */
       SVPNG_U32C(w); SVPNG_U32C(h);               /* 图像宽高(8字节) */
       SVPNG_U8C(8); SVPNG_U8C(alpha ? 6 : 2);     /* 深度为 8，颜色类型为带透明度（RGBA）或不带透明度（RGB） */
       SVPNG_U8AC("\0\0\0", 3);                    /* 压缩方法、滤波器和交错类型固定为默认值 */
       SVPNG_END();                                /* 结束图像文件头写入 */
       SVPNG_BEGIN("IDAT", 2 + h * (5 + p) + 4);   /* 将图像数据写入IDAT块中 */
       SVPNG_U8AC("\x78\1", 2);                    /* 写入压缩块起始头（2字节） */
       for (y = 0; y < h; y++) {                   /* 每行作为一个压缩块（Default Block） */
           SVPNG_U8C(y == h - 1);                  /* 写入一个字节判断是否到达最后一行，若是最后一行写1，否则写0 */
           SVPNG_U16LC(p); SVPNG_U16LC(~p);        /* 写入两个16位整数（共4字节），分别表示块大小及其1的补码，用于校验完整性 */
           SVPNG_U8ADLER(0);                       /* 写入一个字节表示未使用滤波 */
           for (x = 0; x < p - 1; x++, img++)
               SVPNG_U8ADLER(*img);                /* 将图像的每个像素依次写入压缩块中，完成图片数据压缩 */
       }
       SVPNG_U32C((b << 16) | a);                  /* 写入4字节整数用于表示压缩块的结束和Adler-32校验和 */
       SVPNG_END();                                /* } */
       SVPNG_BEGIN("IEND", 0); SVPNG_END();        /* 写入图像结束块标识IEND */
   }
   #endif /* SVPNG_INC_ */
   ```
3. 保存转换后的PNG图片，并在ArkTS侧通过保存文件路径展示图片。

   ```cpp
   void TestSavePng(unsigned int w, unsigned int h, const unsigned char *img)
   {
       static int num = 0;
       std::string tmpDir = std::getenv("TMPDIR");  // /data/storage/el2/base/cache
       std::string filename = tmpDir + "/" + GETPNGNAME + std::to_string(num) + ".png";
       FILE *fp = fopen(filename.c_str(), "wb");
       Svpng(fp, w, h, img, 1);
       fclose(fp);
       fp = nullptr;
   }
   ```

## 总结

将录制获取的音视频帧数据转换为可展示的PNG图片，可按照以下步骤。

1. 创建录制音视频流，获取音视频流数据buffer（PCM格式）。
2. 将获取的buffer传入自定义PNG编码函数中。
3. 保存PNG图片并在ArkTS侧展示。
