---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-window-guidelines
title: NativeWindow开发指导 (C/C++)
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 图形缓冲区 > NativeWindow开发指导 (C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cb5f4ea63c46eb1a16595bdca5829edbc03e4144d2a6fa89782db328a280e2d9
---

## 场景介绍

NativeWindow是**本地平台化窗口**，表示图形队列的生产者端。开发者可以通过NativeWindow接口进行申请和提交Buffer，配置Buffer属性信息。

针对NativeWindow，常见的开发场景如下：

* 通过NativeWindow提供的Native API接口申请图形Buffer，并将生成的图形内容写入图形Buffer，最终提交Buffer到图形队列。
* 在适配EGL层的eglswapbuffer接口时，进行申请和提交Buffer。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| OH\_NativeWindow\_NativeWindowRequestBuffer (OHNativeWindow \*window, OHNativeWindowBuffer \*\*buffer, int \*fenceFd) | 通过OHNativeWindow对象申请一块OHNativeWindowBuffer，用以内容生产。 |
| OH\_NativeWindow\_NativeWindowFlushBuffer (OHNativeWindow \*window, OHNativeWindowBuffer \*buffer, int fenceFd, Region region) | 通过OHNativeWindow将生产好内容的OHNativeWindowBuffer放回到Buffer队列中，用以内容消费。 |
| OH\_NativeWindow\_NativeWindowHandleOpt (OHNativeWindow \*window, int code,...) | 设置/获取OHNativeWindow的属性，包括设置/获取宽高、内容格式等。 |

详细的接口说明请参考[native\_window](../harmonyos-references/capi-nativewindow.md)。

## 开发步骤

以下步骤描述了如何使用NativeWindow提供的Native API接口申请图形Buffer，写入图形内容，并提交Buffer到图形队列。

**添加动态链接库**

CMakeLists.txt中添加以下lib。

```
1. libace_ndk.z.so
2. libnative_window.so
```

**头文件**

```
1. #include <sys/poll.h>
2. #include <sys/mman.h>
3. #include <unistd.h>
4. #include <ace/xcomponent/native_interface_xcomponent.h>
5. #include <native_window/external_window.h>
```

1. 获取OHNativeWindow实例。

   可通过[OH\_NativeXComponent\_Callback](../harmonyos-references/ent-native-xcomponent-oh-nativexcomponent-callback.md)接口获取OHNativeWindow。代码示例如下。关于XComponent模块的使用方法，详见[XComponent开发指导](napi-xcomponent-guidelines.md)。

   1. 在xxx.ets中添加一个XComponent组件。

      ```
      1. XComponent({ id: 'xcomponentId', type: 'texture', libraryname: 'nativerender' })
      2. .margin({ bottom: 26 })
      3. .onLoad((nativeWindowContext) => {
      4. this.nativeWindowContext = nativeWindowContext as NativeWindowContext;
      5. })
      ```

      [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/NdkNativeWindow/entry/src/main/ets/pages/Index.ets#L71-L77)
   2. 在 native c++ 层获取 NativeXComponent。

      ```
      1. napi_value exportInstance = nullptr;
      2. OH_NativeXComponent *nativeXComponent = nullptr;
      3. int32_t ret;
      4. char idStr[OH_XCOMPONENT_ID_LEN_MAX + 1] = {};
      5. uint64_t idSize = OH_XCOMPONENT_ID_LEN_MAX + 1;

      7. status = napi_get_named_property(env, exports, OH_NATIVE_XCOMPONENT_OBJ, &exportInstance);
      8. if (status != napi_ok) {
      9. return false;
      10. }

      12. status = napi_unwrap(env, exportInstance, reinterpret_cast<void**>(&nativeXComponent));
      13. if (status != napi_ok) {
      14. return false;
      15. }

      17. ret = OH_NativeXComponent_GetXComponentId(nativeXComponent, idStr, &idSize);
      18. if (ret != OH_NATIVEXCOMPONENT_RESULT_SUCCESS) {
      19. return false;
      20. }
      ```

      [NativeRender.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/NdkNativeWindow/entry/src/main/cpp/NativeRender.cpp#L145-L166)
   3. 定义 OH\_NativeXComponent\_Callback。

      ```
      1. void OnSurfaceCreatedCB(OH_NativeXComponent* component, void* window)
      2. {
      3. // ...
      4. OHNativeWindow* nativeWindow = static_cast<OHNativeWindow*>(window);
      5. // ...
      6. }

      8. void OnSurfaceChangedCB(OH_NativeXComponent* component, void* window)
      9. {
      10. // ...
      11. OHNativeWindow* nativeWindow = static_cast<OHNativeWindow*>(window);
      12. // ...
      13. }

      15. void OnSurfaceDestroyedCB(OH_NativeXComponent* component, void* window)
      16. {
      17. // ...
      18. OHNativeWindow* nativeWindow = static_cast<OHNativeWindow*>(window);
      19. // ...
      20. }

      22. void DispatchTouchEventCB(OH_NativeXComponent* component, void* window)
      23. {
      24. // ...
      25. OHNativeWindow* nativeWindow = static_cast<OHNativeWindow*>(window);
      26. }
      27. // ...
      28. callback_.OnSurfaceCreated = OnSurfaceCreatedCB;
      29. callback_.OnSurfaceChanged = OnSurfaceChangedCB;
      30. callback_.OnSurfaceDestroyed = OnSurfaceDestroyedCB;
      31. callback_.DispatchTouchEvent = DispatchTouchEventCB;
      ```

      [NativeRender.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/NdkNativeWindow/entry/src/main/cpp/NativeRender.cpp#L26-L144)
   4. 将OH\_NativeXComponent\_Callback 注册给 NativeXComponent。

      ```
      1. OH_NativeXComponent_RegisterCallback(nativeXComponent, &callback_);
      ```

      [NativeRender.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/NdkNativeWindow/entry/src/main/cpp/NativeRender.cpp#L167-L169)
2. 设置OHNativeWindowBuffer的属性。使用OH\_NativeWindow\_NativeWindowHandleOpt设置OHNativeWindowBuffer的属性（默认携带NATIVEBUFFER\_USAGE\_CPU\_READ usage参数，如果不使用CPU读写数据，建议去除NATIVEBUFFER\_USAGE\_CPU\_READ usage参数，具体可见[关闭CPU访问窗口缓冲区数据](../harmonyos-faqs/faqs-arkgraphics-2d-14.md)）。

   ```
   1. int code = SET_BUFFER_GEOMETRY;
   2. int32_t bufferHeight = static_cast<int32_t>(height_ / 4);
   3. int32_t bufferWidth = static_cast<int32_t>(width_ / 2);
   4. OH_NativeWindow_NativeWindowHandleOpt(nativeWindow_, code, bufferWidth, bufferHeight);
   ```

   [NativeRender.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/NdkNativeWindow/entry/src/main/cpp/NativeRender.cpp#L178-L183)
3. 从图形队列申请OHNativeWindowBuffer。

   ```
   1. int fenceFd = -1;
   2. OHNativeWindowBuffer *nativeWindowBuffer = nullptr;
   3. ret = OH_NativeWindow_NativeWindowRequestBuffer(nativeWindow, &nativeWindowBuffer, &fenceFd);
   4. if (ret != 0 || nativeWindowBuffer == nullptr) {
   5. return;
   6. }
   7. BufferHandle *bufferHandle = OH_NativeWindow_GetBufferHandleFromNative(nativeWindowBuffer);
   ```

   [NativeRender.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/NdkNativeWindow/entry/src/main/cpp/NativeRender.cpp#L297-L305)
4. 内存映射mmap。

   ```
   1. void *mappedAddr =
   2. mmap(bufferHandle->virAddr, bufferHandle->size, PROT_READ | PROT_WRITE, MAP_SHARED, bufferHandle->fd, 0);
   ```

   [NativeRender.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/NdkNativeWindow/entry/src/main/cpp/NativeRender.cpp#L306-L309)
5. 将生产的内容写入OHNativeWindowBuffer，在这之前需要等待releaseFenceFd可用（注意releaseFenceFd不等于-1才需要调用poll）。如果没有等待releaseFenceFd事件的数据可用（POLLIN），则可能造成花屏、裂屏、HEBC（High Efficiency Bandwidth Compression，高效带宽压缩） fault等问题。releaseFenceFd是消费者进程创建的一个文件句柄，代表消费者消费buffer完毕，buffer可读，生产者可以开始填充buffer内容。

   ```
   1. int retCode = -1;
   2. uint32_t timeout = 3000;
   3. if (fenceFd != -1) {
   4. struct pollfd pollfds = {0};
   5. pollfds.fd = fenceFd;
   6. pollfds.events = POLLIN;
   7. do {
   8. retCode = poll(&pollfds, 1, timeout);
   9. } while (retCode == -1 && (errno == EINTR || errno == EAGAIN));
   10. close(fenceFd);
   11. }
   12. uint32_t *pixel = static_cast<uint32_t *>(mappedAddr);
   13. for (uint64_t x = 0; x < bufferHandle->width; x++) {
   14. for (uint64_t y = 0; y < bufferHandle->height; y++) {
   15. *pixel++ = value;
   16. }
   17. }
   ```

   [NativeRender.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/NdkNativeWindow/entry/src/main/cpp/NativeRender.cpp#L311-L329)
6. 提交OHNativeWindowBuffer到图形队列。请注意OH\_NativeWindow\_NativeWindowFlushBuffer接口的acquireFenceFd不可以和OH\_NativeWindow\_NativeWindowRequestBuffer接口获取的releaseFenceFd相同，acquireFenceFd可传入默认值-1。acquireFenceFd是生产者需要传入的文件句柄，消费者获取到buffer后可根据生产者传入的acquireFenceFd决定何时去渲染并上屏buffer内容。

   ```
   1. struct Region *region = new Region();
   2. ret = OH_NativeWindow_NativeWindowFlushBuffer(nativeWindow, nativeWindowBuffer, fenceFd, *region);
   3. if (ret != NATIVE_ERROR_OK) {
   4. LOGE("flush failed");
   5. (void)OH_NativeWindow_NativeWindowAbortBuffer(nativeWindow, nativeWindowBuffer);
   6. return;
   7. }
   ```

   [NativeRender.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/NdkNativeWindow/entry/src/main/cpp/NativeRender.cpp#L330-L338)
7. 使用munmap取消内存映射。

   ```
   1. if (munmap(mappedAddr, bufferHandle->size) < 0) {
   2. OH_NativeWindow_DestroyNativeWindow(nativeWindow);
   3. LOGE("munmap failed");
   4. return;
   5. }
   ```

   [NativeRender.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/NdkNativeWindow/entry/src/main/cpp/NativeRender.cpp#L339-L345)
