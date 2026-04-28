---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-vsync-guidelines
title: NativeVSync开发指导 (C/C++)
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > NativeVSync开发指导 (C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d2adc9b165bcfcc7311c11ff81d1a71b2f0ebbcc18164b045ede6feaeeba8778
---

## 场景介绍

NativeVSync模块用于获取系统VSync信号，提供OH\_NativeVSync实例的创建、销毁及设置VSync回调函数的功能。VSync信号触发时，将调用已设置的回调函数。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| OH\_NativeVSync\_Create (const char \*name, unsigned int length) | 创建一个OH\_NativeVSync实例，每次调用都会产生一个新的实例并创建一个vsync线程接收处理回调。本接口需要与OH\_NativeVSync\_Destroy接口配合使用，否则会存在内存泄露。 |
| OH\_NativeVSync\_Destroy (OH\_NativeVSync \*nativeVsync) | 销毁OH\_NativeVSync实例。 |
| OH\_NativeVSync\_FrameCallback (long long timestamp, void \*data) | 回调函数的形式，timestamp表示时间戳，data为回调函数入参。回调的处理在vsync初始化时创建的线程内。 |
| OH\_NativeVSync\_RequestFrame (OH\_NativeVSync \*nativeVsync, OH\_NativeVSync\_FrameCallback callback, void \*data) | 请求下一次VSync信号，当信号到来时，调用回调函数callback。 |

详细的接口说明请参考[native\_vsync](../harmonyos-references/capi-nativevsync.md)。

## 开发步骤

以下步骤描述如何使用NativeVSync提供的Native API接口创建和销毁OH\_NativeVSync实例，以及如何设置VSync回调函数。

**添加动态链接库**

CMakeLists.txt中添加以下库文件。

```
1. libnative_vsync.so
```

**头文件**

```
1. #include <native_vsync/native_vsync.h>
```

1. **首先需要定义一个VSync回调函数**。

   ```
   1. void RenderEngine::OnVsync(long long timestamp, void *data)
   2. {
   3. OH_LOG_Print(LOG_APP, LOG_DEBUG, LOG_PRINT_DOMAIN, "RenderEngine", "OnVsync %{public}lld.", timestamp);
   4. auto renderEngine = reinterpret_cast<RenderEngine *>(data);
   5. if (renderEngine == nullptr) {
   6. return;
   7. }

   9. renderEngine->vSyncCnt_++;
   10. renderEngine->wakeUpCond_.notify_one();
   11. }
   ```

   [render\_engine.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/NdkNativeImage/entry/src/main/cpp/render/render_engine.cpp#L143-L155)
2. **创建OH\_NativeVSync实例**。

   ```
   1. const char* demoName = "NativeImageSample";
   2. nativeVsync_ = OH_NativeVSync_Create(demoName, strlen(demoName));
   ```

   [render\_engine.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/NdkNativeImage/entry/src/main/cpp/render/render_engine.cpp#L159-L162)
3. **通过OH\_NativeVSync实例设置VSync回调函数**。

   ```
   1. wakeUpCond_.wait(lock, [this]() { return wakeUp_ || vSyncCnt_ > 0; });
   2. wakeUp_ = false;
   3. if (vSyncCnt_ > 0) {
   4. vSyncCnt_--;
   5. (void)OH_NativeVSync_RequestFrame(nativeVsync_, &RenderEngine::OnVsync, this);
   6. OH_NativeVSync_GetPeriod(nativeVsync_, &period);
   7. }
   ```

   [render\_engine.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/NdkNativeImage/entry/src/main/cpp/render/render_engine.cpp#L132-L140)
4. **销毁OH\_NativeVSync实例**。

   ```
   1. OH_NativeVSync_Destroy(nativeVsync_);
   2. nativeVsync_ = nullptr;
   ```

   [render\_engine.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/NdkNativeImage/entry/src/main/cpp/render/render_engine.cpp#L174-L177)
