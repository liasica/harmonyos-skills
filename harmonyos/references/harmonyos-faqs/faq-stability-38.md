---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-38
title: 打开扫一扫，扫描二维码时应用闪退
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 打开扫一扫，扫描二维码时应用闪退
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:c2945ac66a7b2c5c5de344c768447a7d31aab51ca2cbbe71bfc37b6133573821
---

## 问题现象

打开扫一扫，扫描二维码，应用闪退。

## 背景知识

[自定义界面扫码](../harmonyos-guides/scan-customscan.md)能力提供了相机流控制接口，可根据自身需求自定义扫码界面，适用于对扫码界面有定制化需求的应用开发，接口文档可见[customScan (自定义界面扫码)](../harmonyos-references/scan-customscan-api.md)。

## 问题定位

1. 从faultlogger目录下获取到应用的CppCrash故障日志，故障信号是SIGSEGV(SEGV\_MAPERR)，异常信息为@0x0000000000000010 probably caused by NULL pointer dereference，无效内存访问。崩溃堆栈不是应用进程，从堆栈内容可以看出是libcustomscan\_napi.z.so自定义扫码服务出现异常。

   ```shell
   Tid:33257, Name:OS_FFRT_3_19
   #00 pc 0000000000031e58 /system/lib64/module/hms/core/scan/libcustomscan_napi.z.so(HMS::HuaweiScan::CustomScan::Stop()+96)(983ce02b64616cda1c46b3c96e40d256)
   #01 pc 0000000000022ba4 /system/lib64/module/hms/core/scan/libcustomscan_napi.z.so(Stop(napi_env__*, napi_callback_info__*)::$_5::__invoke(uv_work_s*) (.cfi)+120)(983ce02b64616cda1c46b3c96e40d256)
   #02 pc 00000000000129a4 /system/lib64/platformsdk/libuv.so(uv__ffrt_work+52)(25c5e130ae25e495771607adc70da044)
   #03 pc 000000000006ab8c /system/lib64/ndk/libffrt.so(ffrt::CPUWorker::Run(ffrt_executor_task*, int)+488)(9322025bdb3c2fcf4efadf8730f620e8)
   #04 pc 000000000006b3c0 /system/lib64/ndk/libffrt.so(ffrt::CPUWorker::RunTask(ffrt_executor_task*, ffrt::CPUWorker*)+128)(9322025bdb3c2fcf4efadf8730f620e8)
   #05 pc 000000000006b750 /system/lib64/ndk/libffrt.so(ffrt::CPUWorker::WorkerLooperDefault(ffrt::WorkerThread*)+232)(9322025bdb3c2fcf4efadf8730f620e8)
   #06 pc 000000000006b258 /system/lib64/ndk/libffrt.so(ffrt::CPUWorker::Dispatch(ffrt::CPUWorker*)+144)(9322025bdb3c2fcf4efadf8730f620e8)
   #07 pc 000000000006b1b0 /system/lib64/ndk/libffrt.so(ffrt::CPUWorker::WrapDispatch(void*)+28)(9322025bdb3c2fcf4efadf8730f620e8)
   #08 pc 00000000001bade8 /system/lib/ld-musl-aarch64.so.1(start+236)(e9ff207f4340aee156e36fdd8af0ab22)
   ```
2. 排查hilog日志中customScan接口的调用情况，可以看出应用调用时序有问题，[customScan.init](../harmonyos-references/scan-customscan-api.md#init)->[customScan.stop](../harmonyos-references/scan-customscan-api.md#stop)->[customScan.release](../harmonyos-references/scan-customscan-api.md#release)->[customScan.start](../harmonyos-references/scan-customscan-api.md#start)同步调用，start创建完相机会话被release接口释放了，导致scan is not initialized。

   ```shell
   // requestCameraPermission请求相机权限
   01-16 15:40:01.091 27147 27147 I A0FF00/com.hx.example/VisionCamera: [Permission], checkAccessToken ohos.permission.CAMERA begin
   01-16 15:40:01.092 27147 27147 I A0FF00/com.hx.example/VisionCamera: [Permission], checkAccessToken permission:ohos.permission.CAMERA = 0
   01-16 15:40:01.092 27147 27147 I A0FF00/com.hx.example/VisionCamera: CameraDevice:, getCameraPermissionStatus:granted
   // customScan.init()初始化自定义界面扫码，加载资源
   01-16 15:40:01.129 27147 27147 I C05506/com.hx.example/ScanFramework: [InitScan:413] customScan.init is called
   01-16 15:40:01.129 27147 27147 I C05506/com.hx.example/ScanFramework: [InitScan:426] camera granted
   01-16 15:40:01.129 27147 27147 I C05506/com.hx.example/ScanFramework: [ParseVector:248] begin ParseVector
   01-16 15:40:01.129 27147 27147 I C05506/com.hx.example/ScanFramework: [InitScan:433] formatVec size 13
   01-16 15:40:01.129 27147 27147 I C05506/com.hx.example/ScanFramework: [ParseScanOptions:97] codeformat 8191
   01-16 15:40:01.129 27147 27147 I C05506/com.hx.example/ScanFramework: [ParseScanOptions:107] end ParseScanOptions
   01-16 15:40:01.129 27147 27147 I C05506/com.hx.example/ScanFramework: [InitScan:453] end InitScan
   // customScan.stop()暂停扫码相机流
   01-16 15:40:01.129 27147 27147 I C05506/com.hx.example/ScanFramework: [Stop:545] customScan.stop is called
   // customScan.release()释放扫码相机流
   01-16 15:40:01.129 27147 27147 I C05506/com.hx.example/ScanFramework: [Release:604] customScan.release is called
   // customScan.start()启动扫码相机流
   01-16 15:40:01.129 27147 27147 I C05506/com.hx.example/ScanFramework: [StartCustomScan:359] customScan.start is called
   01-16 15:40:01.129 27147 27147 I C05506/com.hx.example/ScanFramework: [Init:161] scan hi_analytics already init
   01-16 15:40:01.129 27147 27147 I C05506/com.hx.example/ScanFramework: [CheckStartParam:215] init scan
   01-16 15:40:01.129 27147 27147 I C05506/com.hx.example/ScanFramework: [CustomScan:54] CustomScan Constructor
   01-16 15:40:01.129 27147 33257 I C05506/com.hx.example/ScanFramework: [operator():574] scan stop
   01-16 15:40:01.129 27147 33257 I C05506/com.hx.example/ScanFramework: [ResetEvent:59] Reset camera event
   01-16 15:40:01.129 27147 33257 I C05506/com.hx.example/ScanFramework: [Stop:644] Session Stop
   01-16 15:40:01.129 27147 33269 E C05506/com.hx.example/ScanFramework: [operator():633] scan is not initialized
   ```
3. 排查customScan的代码逻辑，stop、release、start三个是异步接口，不能一起调用，否则会因为时序问题导致crash。

## 分析结论

customScan的stop、release、start三个接口调用出现了时序问题，导致发生CppCrash。

## 修改建议

调整customScan接口调用的时序，建议将初始化操作放在onPageShow中，释放操作放在onPageHide中，参考文档自定义扫码界面[开发步骤](../harmonyos-guides/scan-customscan.md#开发步骤)。
