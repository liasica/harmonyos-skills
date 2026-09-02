---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-63
title: 预览帧处理时如何选择format
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 预览帧处理时如何选择format
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:19+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4ebbe36e4beefd7e4ca36abfb4f1263b7e559caadcbb1b4c7a5d0736bd5cfcad
---

## 问题现象

在双路预览开发时，可能会出现下面两种异常场景：

* **画面色彩混乱、画面错位。** 画面出现大面积偏色或者局部色彩错误，甚至出现色块杂乱等情况，如下图所示（图一为正常图案，图二三为异常现象）：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/zNhl3NqVRVGBNJXqkplqZw/zh-cn_image_0000002658911805.png "点击放大") ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/TL0y_JCATyCHOfoJos6iaA/zh-cn_image_0000002628392596.png "点击放大") ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/rJia_y43TuSa1Yb3wXqF-A/zh-cn_image_0000002658791863.png "点击放大")
* **预览界面直接闪退。** 相机预览界面打开后快速闪退，并伴有如下crash日志：

  ```txt
  Process name:com.example.personaltest
  Process life time:4s
  Process Memory(kB): 242962(Rss)
  Device Memory(kB): Total 16017036, Free 771396, Available 7143424
  Reason:Signal:SIGSEGV(SEGV_MAPERR)@0x0000005b5f0be000 
  Fault thread info:
  Tid:54261, Name:OS_FFRT_2_2
  #00 pc 000000000001d8b8 /system/lib64/libhispeed_image.so(HSD_Image_RGBA_to_rgbA+120)(3eaf5c382d6322f2adbc21b9e86197ea)
  #01 pc 0000000000fc9024 /system/lib64/libskia_canvaskit.z.so(SkConvertPixels(SkImageInfo const&, void*, unsigned long, SkImageInfo const&, void const*, unsigned long)+356)(7098d0b1d31420779f28556b877e2b29)
  #02 pc 0000000000fddddc /system/lib64/libskia_canvaskit.z.so(SkBitmap::writePixels(SkPixmap const&, int, int)+344)(7098d0b1d31420779f28556b877e2b29)
  #03 pc 00000000000043a0 /system/lib64/platformsdk/libpixelconvertadapter.z.so(OHOS::Media::PixelConvertAdapter::WritePixelsConvert(void const*, unsigned int, OHOS::Media::ImageInfo const&, void*, OHOS::Media::Position const&, unsigned int, OHOS::Media::ImageInfo const&) (.cfi)+664)(5368e33cc90cfc45cc93c5145375d9db)
  #04 pc 000000000010d8b4 /system/lib64/platformsdk/libimage_native.z.so(OHOS::Media::PixelConvert::PixelsConvert(OHOS::Media::BufferInfo const&, OHOS::Media::BufferInfo&, int, bool) (.cfi)+7220)(cbd62a0ff3d78c60f180e38726228131)
  #05 pc 00000000000f8d14 /system/lib64/platformsdk/libimage_native.z.so(OHOS::Media::PixelMap::Create(unsigned int const*, unsigned int, OHOS::Media::BuildParam&, OHOS::Media::InitializationOptions const&, int&) (.cfi)+748)(cbd62a0ff3d78c60f180e38726228131)
  #06 pc 00000000000f89e8 /system/lib64/platformsdk/libimage_native.z.so(OHOS::Media::PixelMap::Create(unsigned int const*, unsigned int, OHOS::Media::InitializationOptions const&) (.cfi)+208)(cbd62a0ff3d78c60f180e38726228131)
  #07 pc 00000000000d14b4 /system/lib64/platformsdk/libimage_napi.z.so(OHOS::Media::CreatePixelMapExec(napi_env__*, void*) (.cfi)+464)(8a4937c6722b56ca6a98bec4c504c48f)
  #08 pc 000000000005d130 /system/lib64/platformsdk/libace_napi.z.so(NativeAsyncWork::AsyncWorkCallback(uv_work_s*)+304)(0cebf964e89dab5a2ce4cefd8e58beea)
  #09 pc 00000000000135bc /system/lib64/platformsdk/libuv.so(uv__queue_work+60)(00cee7c8797de4a98569c4744411c891)
  #10 pc 00000000000ad964 /system/lib64/ndk/libffrt.so(ffrt::UVTask::ExecuteImpl(ffrt::UVTask*, void (*)(ffrt_executor_task*, int))+256)(5c382a50e711fcf0b33083e1da8d8ed1)
  #11 pc 00000000000a8f4c /system/lib64/ndk/libffrt.so(ffrt::ExecuteTask(ffrt::TaskBase*)+252)(5c382a50e711fcf0b33083e1da8d8ed1)
  #12 pc 000000000006abe4 /system/lib64/ndk/libffrt.so(ffrt::CPUWorker::RunTask(ffrt::TaskBase*, ffrt::CPUWorker*)+84)(5c382a50e711fcf0b33083e1da8d8ed1)
  #13 pc 000000000006ae88 /system/lib64/ndk/libffrt.so(ffrt::CPUWorker::WorkerLooper(ffrt::CPUWorker*)+396)(5c382a50e711fcf0b33083e1da8d8ed1)
  #14 pc 00000000000474d0 /system/lib64/ndk/libffrt.so(ffrt::CPUWorker::Dispatch(ffrt::CPUWorker*)+212)(5c382a50e711fcf0b33083e1da8d8ed1)
  #15 pc 00000000000472a4 /system/lib64/ndk/libffrt.so(ffrt::CPUWorker::WrapDispatch(void*)+60)(5c382a50e711fcf0b33083e1da8d8ed1)
  #16 pc 00000000001d8938 /system/lib/ld-musl-aarch64.so.1(start+240)(73c8ccfd08a34c45800c16fb998a68cc)
  ========SubmitterStacktrace========
  #00 pc 000000000001382c /system/lib64/platformsdk/libuv.so(uv_queue_work_internal+316)(00cee7c8797de4a98569c4744411c891)
  #01 pc 000000000005ce6c /system/lib64/platformsdk/libace_napi.z.so(NativeAsyncWork::Queue(NativeEngine*)+412)(0cebf964e89dab5a2ce4cefd8e58beea)
  #02 pc 000000000008bf38 /system/lib64/platformsdk/libace_napi.z.so(napi_queue_async_work+40)(0cebf964e89dab5a2ce4cefd8e58beea)
  #03 pc 00000000000c0488 /system/lib64/platformsdk/libimage_napi.z.so(OHOS::Media::PixelMapNapi::CreatePixelMap(napi_env__*, napi_callback_info__*) (.cfi)+524)(8a4937c6722b56ca6a98bec4c504c48f)
  #04 pc 0000000000066fd4 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+292)(0cebf964e89dab5a2ce4cefd8e58beea)
  #05 pc 0000000000e0d9f0 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+44)
  #06 pc 0000000000465018 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis2Imm8V8V8V8StwCopy+436)
  #07 at anonymous entry (entry/src/main/ets/pages/Index.ets:230:38)
  #08 pc 00000000004a60b0 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::InterpreterAssembly::Execute(panda::ecmascript::EcmaRuntimeCallInfo*)+608)(3beab3d3995f1b1c11f542938d599a63)
  #09 pc 00000000004a5644 /system/lib64/platformsdk/libark_jsruntime.so(panda::FunctionRef::CallForNapi(panda::ecmascript::EcmaVM const*, panda::JSValueRef*, panda::JSValueRef* const*, int)+536)(3beab3d3995f1b1c11f542938d599a63)
  #10 pc 000000000007a7e4 /system/lib64/platformsdk/libace_napi.z.so(napi_call_function+212)(0cebf964e89dab5a2ce4cefd8e58beea)
  #11 pc 0000000000093740 /system/lib64/platformsdk/libimage_napi.z.so(OHOS::Media::CommonCallbackRoutine(napi_env__*, OHOS::Media::ImageAsyncContext*&, napi_value__* const&)+444)(8a4937c6722b56ca6a98bec4c504c48f)
  #12 pc 0000000000093a24 /system/lib64/platformsdk/libimage_napi.z.so(OHOS::Media::JsGetComponentCallBack(napi_env__*, napi_status, OHOS::Media::ImageAsyncContext*) (.cfi)+336)(8a4937c6722b56ca6a98bec4c504c48f)
  #13 pc 000000000003f4f4 /system/lib64/platformsdk/libace_napi.z.so(NativeAsyncWork::AsyncAfterWorkCallback(uv_work_s*, int)+468)(0cebf964e89dab5a2ce4cefd8e58beea)
  #14 pc 00000000000722c0 /system/lib64/platformsdk/libruntime.z.so(std::__h::__function::__func<OHOS::AbilityRuntime::OHOSJsEnvironmentImpl::PostTaskToHandler(uv_task_info_s const*)::$_0, std::__h::allocator<OHOS::AbilityRuntime::OHOSJsEnvironmentImpl::PostTaskToHandler(uv_task_info_s const*)::$_0>, void ()>::operator()()+128)(6fac88a3788b167d65c694c7b98b5186)
  #15 pc 000000000001efe4 /system/lib64/chipset-sdk-sp/libeventhandler.z.so(OHOS::AppExecFwk::(anonymous namespace)::EventRunnerImpl::ExecuteEventHandler(std::__h::unique_ptr<OHOS::AppExecFwk::InnerEvent, void (*)(OHOS::AppExecFwk::InnerEvent*)>&)+1824)(cb50d8e3b11e95df8dfdd059d8351e8d)
  ```

碰到上述两种情况，应该如何正确处理？

## 背景知识

* [CameraFormat](../harmonyos-references/arkts-apis-camera-e.md#cameraformat)：相机输出流的原始数据格式，定义相机硬件输出图像的编码方式（如YUV、RGB等）。决定Surface接收数据的底层结构。
* [nextImage.format](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_format)：ImageReceiver接收图像的格式，是相机输出流数据经系统封装后的中间格式，与CameraFormat强关联。
* [PixelMapFormat](../harmonyos-references/arkts-apis-image-e.md#pixelmapformat7)：PixelMap的处理格式，用于内存中处理图像数据的像素排列方式（如RGBA、NV21等）。
* 三者关系：CameraFormat决定nextImage.format，二次预览时则需要根据nextImage.format取值来选择对应的PixelMapFormat和单位像素字节数。芯片根据创建预览输出流时的CameraFormat类型来出图，因此nextImage.format是由CameraFormat来决定的。而在将nextImage处理成pixelMap时，需要根据nextImage.format的值选择对应的PixelMapFormat以及单位像素字节数。三者的对应关系如下表：

  | CameraFormat值 | 对应nextImage.format值 | PixelMapFormat取值 | 单位像素字节数 | 适用的输出流 |
  | --- | --- | --- | --- | --- |
  | CAMERA\_FORMAT\_RGBA\_8888 | - | - | - | - |
  | CAMERA\_FORMAT\_YUV\_420\_SP | 25 | image.PixelMapFormat.NV21 | 1.5 | 预览流，视频流（NORMAL\_VIDEO） |
  | CAMERA\_FORMAT\_JPEG | - | - | - | 拍照流（NORMAL\_PHOTO） |
  | CAMERA\_FORMAT\_YCBCR\_P010 | 35 | image.PixelMapFormat.YCBCR\_P010 | 3 | 预览流（NORMAL\_VIDEO），视频流（NORMAL\_VIDEO） |
  | CAMERA\_FORMAT\_YCRCB\_P010 | 36 | image.PixelMapFormat.YCRCB\_P010 | 3 | 预览流（NORMAL\_VIDEO），视频流（NORMAL\_VIDEO） |
  | CAMERA\_FORMAT\_HEIC | - | - | - | - |

  **说明** 

  注：表中的NORMAL\_VIDEO指的是相机模式为NORMAL\_VIDEO，NORMAL\_PHOTO则是指相机模式为NORMAL\_VIDEO，未特别标明的表示两种模式都可以。

## 问题定位

* 画面色彩杂乱。

  画面色彩异常现象明显，根本原因在于像素格式解析错配，由于CameraFormat与PixelMapFormat取值不匹配，导致色彩空间不匹配或者色彩通道顺序错位，进而造成色彩错乱。
* 预览界面发生crash闪退。
  1. 从日志可以看出crash是因为发生了严重的内存访问异常（SIGSEGV(SEGV\_MAPERR)），从日志33行可以看出问题出在Index.ets:230:38，对应代码中操作为：

     ```ts
     let pixelMapFormat = image.PixelMapFormat.YCRCB_P010;
     pixelMap = await image.createPixelMap(dstArr.buffer, {
       size: { height: height, width: width },
       srcPixelFormat: pixelMapFormat,
     });
     ```
  2. [image.createPixelMap](../harmonyos-references/arkts-apis-image-f.md#imagecreatepixelmap8)方法是通过图像像素数据的缓冲区（dstArr.buffer）内容创建PixelMap，而dstArr.buffer的创建过程为：

     ```ts
     let mSize = 1.5;
     const dstBufferSize = width * height * mSize; // 以NV21为例（YUV_420_SP格式的图片）YUV_420_SP内存计算公式：长x宽+(长x宽)/2
     const dstArr = new Uint8Array(dstBufferSize);
     for (let j = 0; j < height * mSize; j++) {
       const srcBuf = new Uint8Array(imgComponent.byteBuffer, j * stride, width);
       dstArr.set(srcBuf, j * width);
     }
     ```
  3. 从上面两段代码可知，创建图像缓冲区数据时选择的单位像素字节数为1.5，而createPixelMap时传入的格式是PixelMapFormat.YCRCB\_P010。PixelMapFormat.YCRCB\_P010格式对应的单位像素字节数应该为3。

## 分析结论

* 画面色彩杂乱：画面出现错乱是因为在转成pixelMap处理时，选择错了pixelMapFormat，导致画面色彩混乱。
* 预览界面发生crash闪退：crash闪退是因为图像数组拷贝时，单位像素字节数选择过小，使得图像缓冲区数据长度不符合要求，导致创建pixelMap时发生地址越界造成闪退。

## 修改建议

参照背景知识章节中的表格，选择正确的相机模式和CameraFormat值，然后在处理nextImage时选择对应的PixelMapFormat和单位像素字节数。

详细实现代码可参考[双路预览开发步骤](../harmonyos-guides/camera-dual-channel-preview.md#开发步骤)，其中关键步骤为[用于处理图像的第一路预览流](../harmonyos-guides/camera-dual-channel-preview.md#用于处理图像的第一路预览流)。
