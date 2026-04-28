---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-common-mistakes
title: 图形缓冲区常见稳定性问题 (C/C++)
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 图形缓冲区 > 图形缓冲区常见稳定性问题 (C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:20+08:00
doc_updated_at: 2026-04-17
content_hash: sha256:348f580ac1d4541ef276246b677b0d77205b47025ba75c2bcfe3cc83bb2c9dbc
---

本文档主要针对NativeWindow、NativeBuffer和NativeImage开发过程中的常见问题进行说明，帮助开发者及时避免或定位对应问题，提高应用稳定性。

## OHNativeWindow与NativeWindowBuffer

OHNativeWindow与NativeWindowBuffer在系统多个模块与应用之间传递，通过增加与减少引用计数的NDK接口实现伪智能指针，由各模块维护自己的引用计数，超过90%的问题都是由于增减引用计数接口未匹配导致的。

增加NativeWindow引用计数的接口：

```
1. int32_t OH_NativeWindow_NativeObjectReference(void *obj)

3. int32_t OH_NativeWindow_CreateNativeWindowFromSurfaceId(uint64_t surfaceId, OHNativeWindow **window)

5. OHNativeWindow* OH_NativeImage_AcquireNativeWindow(OH_NativeImage* image)

7. int32_t OH_NativeWindow_ReadFromParcel(OHIPCParcel *parcel, OHNativeWindow **window)
```

减少NativeWindow引用计数的接口：

```
1. int32_t OH_NativeWindow_NativeObjectUnreference(void *obj)

3. void OH_NativeWindow_DestroyNativeWindow(OHNativeWindow* window)

5. void OH_NativeImage_Destroy(OH_NativeImage** image)
```

增加NativeWindowBuffer引用计数的接口：

```
1. int32_t OH_NativeWindow_NativeObjectReference(void *obj)

3. int32_t OH_NativeWindow_GetLastFlushedBufferV2(OHNativeWindow *window, OHNativeWindowBuffer **buffer,int *fenceFd, float matrix[16])

5. OHNativeWindowBuffer* OH_NativeWindow_CreateNativeWindowBufferFromNativeBuffer(OH_NativeBuffer* nativeBuffer)

7. int32_t OH_NativeImage_AcquireNativeWindowBuffer(OH_NativeImage* image,OHNativeWindowBuffer** nativeWindowBuffer, int* fenceFd)
```

减少NativeWindowBuffer引用计数的接口：

```
1. int32_t OH_NativeWindow_NativeObjectUnreference(void *obj)

3. void OH_NativeWindow_DestroyNativeWindowBuffer(OHNativeWindowBuffer* buffer)

5. int32_t OH_NativeImage_ReleaseNativeWindowBuffer(OH_NativeImage* image,OHNativeWindowBuffer* nativeWindowBuffer, int fenceFd) // 仅接口返回成功时减少引用计数
```

## NativeWindow生命周期问题

### 典型崩溃日志及原因

典型崩溃日志如下：

```
1. **典型崩溃日志1**
2. 00 /system/lib64/chipset-sdk-sp/libsurface.z.so(OH_NativeWindow_DestroyNativeWindow())

4. **典型崩溃日志2**
5. 00 /system/lib64/chipset-sdk-sp/libsurface.z.so(……)
6. 01 /system/lib64/chipset-sdk-sp/libsurface.z.so(……)
7. 02 /system/lib64/chipset-sdk-sp/libsurface.z.so(OH_NativeWindow_NativeWindowHandleOpt)

9. **典型崩溃日志3**
10. 00 /system/lib64/chipset-sdk-sp/libsurface.z.so(OH_NativeWindow_NativeObjectUnreference())
```

可能原因如下：

1.错误地减少了一次NativeWindow引用计数，导致NativeWindow计数减为0释放后，其他地方调用或者再次减计数时崩溃。

2.从XComponent组件获取的NativeWindow，抛向子线程使用，XComponent组件销毁时将NativeWindow引用计数减一，若减为0析构后，子线程仍在使用会导致崩溃。

### 典型错误代码及解决方案

**典型错误代码1**

```
1. OH_NativeImage *image_ = OH_NativeImage_Create(textureId, GL_TEXTURE_2D);
2. OHNativeWindow *nativewindow_ = OH_NativeImage_AcquireNativeWindow();

4. // 错误：OH_NativeImage_Destroy中会减少OHNativeWindow引用计数，无需再调用OH_NativeWindow_DestroyNativeWindow
5. OH_NativeImage_Destroy(image_);
6. OH_NativeWindow_DestroyNativeWindow(nativewindow_);
```

**具体解析**

OH\_NativeImage\_Destroy中会减少OHNativeWindow引用计数，无需再调用OH\_NativeWindow\_DestroyNativeWindow。

修改：删除OH\_NativeWindow\_DestroyNativeWindow(nativewindow\_)，并在OH\_NativeImage\_Destroy后及时将image\_和nativewindow\_置空，防止后续使用野指针。

```
1. OH_NativeImage *image_ = OH_NativeImage_Create(textureId, GL_TEXTURE_2D);
2. OHNativeWindow *nativewindow_ = OH_NativeImage_AcquireNativeWindow();

4. // 释放NativeImage时将image_和nativewindow_置空，防止后续使用野指针
5. OH_NativeImage_Destroy(image_);
6. image_ = nullptr;
7. nativewindow_ = nullptr;
```

**典型错误代码2**

```
1. void OnSurfaceCreatedCB(OH_NativeXComponent* component, void* window)
2. {
3. uint64_t width = 0;
4. uint64_t height = 0;
5. int32_t ret = OH_NativeXComponent_GetXComponentSize(component, window, &width, &height);
6. OHNativeWindow* nativewindow_ = static_cast<OHNativeWindow*>(window);

8. // 未对NativeWindow增加引用计数直接抛向子线程使用
9. NativeRender::GetInstance()->SetNativeWindow(nativewindow_, width, height);
10. }

12. void OnSurfaceDestroyedCB(OH_NativeXComponent* component, void* window)
13. {
14. if ((component == nullptr) || (window == nullptr)) {
15. LOGE("OnSurfaceDestroyedCB: component or window is null");
16. return;
17. }

19. // 错误：通知子线程停止，但未做等待操作，OnSurfaceDestroyedCB结束后NativeWindow可能被释放，子线程正在使用可能崩溃
20. NativeRender::GetInstance()->Release();
21. OHNativeWindow* nativewindow_ = static_cast<OHNativeWindow*>(window);
22. // 错误：未对nativewindow_引用计数加一的情况下调用DestroyNativeWindow会使nativewindow_提前释放，导致崩溃
23. OH_NativeWindow_DestroyNativeWindow(nativewindow_);
24. }
```

**具体解析**

从XComponent组件获取NativeWindow后，传递给渲染子线程使用，当页面退出，XComponent组件销毁时，会将NativeWindow引用计数减一，应用未对NativeWindow引用加一的情况下NativeWindow会被释放，此时子线程仍在使用可能导致并发崩溃。

修改方案一：在将NativeWindow传递给子线程前，将其引用计数加一，此时XComponent组件销毁时，因应用持有NativeWindow引用计数，NativeWindow不会销毁，当子线程使用完成后将其引用计数减一。

```
1. void OnSurfaceCreatedCB(OH_NativeXComponent* component, void* window)
2. {
3. uint64_t width = 0;
4. uint64_t height = 0;
5. int32_t ret = OH_NativeXComponent_GetXComponentSize(component, window, &width, &height);
6. OHNativeWindow* nativewindow_ = static_cast<OHNativeWindow*>(window);

8. // 抛任务前将nativeWindow引用计数加一
9. OH_NativeWindow_NativeObjectReference(nativewindow_);
10. NativeRender::GetInstance()->SetNativeWindow(nativewindow_, width, height);
11. }

13. void OnSurfaceDestroyedCB(OH_NativeXComponent* component, void* window)
14. {
15. if ((component == nullptr) || (window == nullptr)) {
16. LOGE("OnSurfaceDestroyedCB: component or window is null");
17. return;
18. }

20. // 通知子线程停止，因为前面有对引用计数加一，OnSurfaceDestroyedCB结束时不会释放
21. // 当子线程使用完毕后执行OH_NativeWindow_NativeObjectUnreference(nativewindow_)对引用计数减一
22. NativeRender::GetInstance()->Release();
23. }
```

修改方案二：在XComponent组件销毁的OnSurfaceDestroyedCB回调通知中，通知子线程停止并等待，直到子线程结束，避免NativeWindow销毁后子线程还在使用。

```
1. void OnSurfaceCreatedCB(OH_NativeXComponent* component, void* window)
2. {
3. uint64_t width = 0;
4. uint64_t height = 0;
5. int32_t ret = OH_NativeXComponent_GetXComponentSize(component, window, &width, &height);
6. OHNativeWindow* nativewindow_ = static_cast<OHNativeWindow*>(window);

8. NativeRender::GetInstance()->SetNativeWindow(nativewindow_, width, height);
9. }

11. void OnSurfaceDestroyedCB(OH_NativeXComponent* component, void* window)
12. {
13. if ((component == nullptr) || (window == nullptr)) {
14. LOGE("OnSurfaceDestroyedCB: component or window is null");
15. return;
16. }

18. NativeRender::GetInstance()->Release();
19. // 通知子线程停止后等待子线程任务结束再结束OnSurfaceDestroyedCB
20. renderThread.join();
21. }
```

## NativeWindowBuffer生命周期问题

### 典型崩溃日志及原因

典型崩溃日志如下：

```
1. **典型崩溃日志1**
2. 00 /system/lib64/chipset-sdk-sp/libsurface.z.so(OH_NativeWindow_GetBufferHandleFromNative())

4. **典型崩溃日志2**
5. 00 /system/lib64/chipset-sdk-sp/libsurface.z.so(OH_NativeWindow_NativeObjectUnreference())

7. **典型崩溃日志3**
8. 00 /system/lib64/chipset-sdk-sp/libsurface.z.so(OH_NativeWindow_NativeObjectReference())
```

可能原因如下：

从XComponent组件获取的NativeWindow，抛向子线程使用，XComponent组件销毁时将NativeWindow计数减一，NativeWindow销毁时对内部的NativeWindowBuffer引用计数减一，此时子线程刚RequestBuffer拿到buffer正在使用导致崩溃。

### 典型错误代码及解决方案

同上述NativeWindow生命周期问题的典型错误代码及解决方案。

## NativeWindowBuffer卡死问题

### 典型卡死日志及原因

典型卡死日志如下：

```
1. /system/lib64/chipset-sdk-sp/libsurface.z.so(RequestBufferLocked())
```

可能原因如下：

应用申请了buffer，但未归还，导致后续无可用buffer，再次申请buffer时卡住。

**典型错误代码**

```
1. auto ret = OH_NativeWindow_NativeWindowRequestBuffer(nativewindow_, &buffer, &fence);
2. if (ret != NATIVE_ERROR_OK) {
3. return;
4. }

6. // 错误：异常分支未归还buffer，NativeWindow内buffer数量固定，可能导致后续无buffer可用卡死
7. if (error) {
8. return;
9. }

11. OH_NativeWindow_NativeWindowFlushBuffer(nativewindow_, buffer, fence, region);
```

**具体解析**

NativeWindow中的NativeWindowBuffer数量固定，当只申请buffer未归还，会导致NativeWindow内buffer耗尽，再次申请buffer时卡死。

修改：确保申请的buffer一定会归还到NativeWindow中，成功绘制的可通过OH\_NativeWindow\_NativeWindowFlushBuffer归还，未绘制的可通过OH\_NativeWindow\_NativeWindowAbortBuffer归还。

```
1. auto ret = OH_NativeWindow_NativeWindowRequestBuffer(nativewindow_, &buffer, &fence);
2. if (ret != NATIVE_ERROR_OK) {
3. return;
4. }

6. if (error) {
7. // 异常分支归还buffer
8. OH_NativeWindow_NativeWindowAbortBuffer(nativewindow_, buffer);
9. return;
10. }

12. OH_NativeWindow_NativeWindowFlushBuffer(nativewindow_, buffer, fence, region);
```

## 内存泄露问题

### 典型内存泄露原因

额外执行了增加引用计数接口，未配套执行减少引用计数接口导致泄露。

### 典型错误代码及解决方案

**典型错误代码1**

```
1. auto ret = OH_NativeWindow_NativeWindowRequestBuffer(nativewindow_, &buffer, &fence);
2. if (ret != NATIVE_ERROR_OK) {
3. return;
4. }
5. ret = OH_NativeWindow_NativeObjectReference(buffer);
6. if (ret != NATIVE_ERROR_OK) {
7. return;
8. }

10. // 错误：对buffer增加了引用计数，绘制流程走到异常分支，异常分支未相应减少引用计数，导致泄露
11. if (error) {
12. OH_NativeWindow_NativeWindowAbortBuffer(nativewindow_, buffer);
13. return;
14. }

16. OH_NativeWindow_NativeWindowFlushBuffer(nativewindow_, buffer, fence, region);
17. OH_NativeWindow_NativeObjectReference(buffer);
```

**具体解析**

申请buffer后增加引用计数延长其生命周期，未配套减少引用计数，导致该buffer无法被释放。

修改：确保增加引用计数后有配套调用减少引用计数接口。

```
1. auto ret = OH_NativeWindow_NativeWindowRequestBuffer(nativewindow_, &buffer, &fence);
2. if (ret != NATIVE_ERROR_OK) {
3. return;
4. }
5. ret = OH_NativeWindow_NativeObjectReference(buffer);
6. if (ret != NATIVE_ERROR_OK) {
7. return;
8. }

10. if (error) {
11. // 异常分支配套减少引用计数
12. OH_NativeWindow_NativeWindowAbortBuffer(nativewindow_, buffer);
13. OH_NativeWindow_NativeObjectUnreference(buffer);
14. return;
15. }

17. OH_NativeWindow_NativeWindowFlushBuffer(nativewindow_, buffer, fence, region);
18. OH_NativeWindow_NativeObjectReference(buffer);
```

**典型错误代码2**

```
1. auto ret = OH_NativeImage_AcquireNativeWindowBuffer(nativeimage, &buffer, &fence);
2. if (ret != NATIVE_ERROR_OK) {
3. return;
4. }
5. ret = OH_NativeWindow_NativeObjectReference(buffer);
6. if (ret != NATIVE_ERROR_OK) {
7. return;
8. }

10. // 错误：未对Release失败场景处理，AcquireNativeWindowBuffer成功会对buffer引用计数加一，ReleaseNativeWindowBuffer失败不会减一
11. OH_NativeImage_ReleaseNativeWindowBuffer(nativeimage, buffer, fence);
12. OH_NativeWindow_NativeObjectUnreference(buffer);
```

**具体解析**

OH\_NativeImage\_AcquireNativeWindowBuffer接口获取的buffer会增加引用计数，OH\_NativeImage\_ReleaseNativeWindowBuffer接口只在成功时减少引用计数，未对返回值做处理会导致内存泄露。

修改：OH\_NativeImage\_ReleaseNativeWindowBuffer接口返回不为NATIVE\_ERROR\_OK时，额外调用OH\_NativeWindow\_NativeObjectUnreference减少一次引用计数。

```
1. auto ret = OH_NativeImage_AcquireNativeWindowBuffer(nativeimage, &buffer, &fence);
2. if (ret != NATIVE_ERROR_OK) {
3. return;
4. }
5. ret = OH_NativeWindow_NativeObjectReference(buffer);
6. if (ret != NATIVE_ERROR_OK) {
7. return;
8. }

10. // 对OH_NativeImage_ReleaseNativeWindowBuffer失败做异常处理
11. ret = OH_NativeImage_ReleaseNativeWindowBuffer(nativeimage, buffer, fence);
12. if (ret != NATIVE_ERROR_OK) {
13. OH_NativeWindow_NativeObjectUnreference(buffer);
14. }
15. OH_NativeWindow_NativeObjectUnreference(buffer);
```
