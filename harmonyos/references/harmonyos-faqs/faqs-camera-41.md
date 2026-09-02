---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-41
title: 应用频繁开关摄像头偶现AppFreeze
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 应用频繁开关摄像头偶现AppFreeze
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cbfee7f9b4fe43433bccf44605fa19f8c7e86c1155eca22c0fb07b29909d2418
---

## 问题现象

应用在进行会议时，频繁开关摄像头，偶现AppFreeze。

## 背景知识

* [拍照](../harmonyos-guides/native-camera-shooting.md)是相机的最重要功能之一，拍照模块基于相机复杂的逻辑，为了保证用户拍出的照片质量，在中间步骤可以设置分辨率、闪光灯、焦距、照片质量及旋转角度等信息。使用C/C++进行拍照的主要流程包括设备输入、会话管理、拍照等，具体可参考[拍照实践(C/C++)](../harmonyos-guides/native-camera-shooting-case.md)。
* 应用出现卡死现象，在faultlogger目录或者eventlog目录下生成了AppFreeze日志文件，具体定位方法可参考[AppFreeze（应用冻屏）检测](../harmonyos-guides/appfreeze-guidelines.md)。

## 问题定位

1. 应用代码在关闭相机时，在关闭相机的方法StopCapture()中执行了[OH\_CameraInput\_Close()](../harmonyos-references/capi-camera-input-h.md#oh_camerainput_close)方法，进入到相机的关闭流程。相机关闭流程日志的关键信息如下：

   ```txt
   #00 pc 00000000001b6e14 /system/lib/ld-musl-aarch64.so.1(__timedwait_cp+192)(9961028567d943f810edfa4c2aa71a31)
   #01 pc 00000000001bcf90 /system/lib/ld-musl-aarch64.so.1(__pthread_mutex_timedlock_inner+592)(9961028567d943f810edfa4c2aa71a31)
   #02 pc 00000000000c6108 /data/storage/el1/bundle/libs/arm64/libc++_shared.so(std::__n1::mutex::lock()+8)(cdf97be9396a35e8f4806f252f90a11320d26ec6)
   #03 pc 0000000000054b54 /data/storage/el1/bundle/libs/arm64/libhimedia.so(8eb21c47ffcf54f6343dc471cc653c07385ccfd6)
   #04 pc 0000000000062860 /data/storage/el1/bundle/libs/arm64/libhimedia.so(VCCameraCapture::OnImageReceiverCallback(OH_ImageReceiverNative*)+2204)(8eb21c47ffcf54f6343dc471cc653c07385ccfd6)
   #05 pc 0000000000113864 /system/lib64/platformsdk/libimage_native.z.so(OHOS::Media::ImageReceiverSurfaceListener::OnBufferAvailable()+156)(bcd0c974911e66ecc960744f372db153)
   ```
2. 上层应用通知底层关闭相机时，底层还未处理完的surfaceBuffer需要交还给BufferQueue，将surfaceBuffer flush进BufferQueue时，BufferQueue会触发回调OnBufferAvailable()通知消费端，也就是三方，Buffer已填充完毕，但该回调中三方所持的锁和三方关闭相机持的锁为同一把，于是进入了锁等待\_\_pthread\_mutex\_timedlock\_inner->\_\_timedwait\_cp形成死锁，最终导致AppFreeze。

## 分析结论

通过应用代码和日志可以发现，应用在执行StopCapture()方法时加的锁和OnImageReceiverCallback()中添加的是同一把锁。在会议进行中，应用加锁后执行StopCapture()方法，然后程序执行到OnImageReceiverCallback()，此时在进入画面渲染推流时又遇到了同一把锁，造成锁等待形成死锁，最终导致AppFreeze。

## 修改建议

应用在执行关闭相机StopCapture()方法时重新使用一把锁，不与图像数据回调OnImageReceiverCallback()方法使用同一把锁，即可解决死锁造成的AppFreeze问题。
