---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-buffer-guidelines
title: NativeBuffer开发指导 (C/C++)
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 图形缓冲区 > NativeBuffer开发指导 (C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d2ae0f7978a73cfcf793aeae7b90eb86f7345e213b53fa5af22171c75ce97ff8
---

## 场景介绍

NativeBuffer模块提供**共享内存**功能，支持内存的申请、使用、查询和释放等操作。

NativeBuffer的常见开发场景：通过Native API申请OH\_NativeBuffer实例，获取内存属性，将ION内存映射到进程空间。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| OH\_NativeBuffer\_Alloc (const OH\_NativeBuffer\_Config \*config) | 通过OH\_NativeBuffer\_Config创建OH\_NativeBuffer实例，每次调用都会产生一个新的OH\_NativeBuffer实例。本接口需要与OH\_NativeBuffer\_Unreference接口配合使用，否则会存在内存泄露。 |
| OH\_NativeBuffer\_Reference (OH\_NativeBuffer \*buffer) | 将OH\_NativeBuffer对象的引用计数增加1。 |
| OH\_NativeBuffer\_Unreference (OH\_NativeBuffer \*buffer) | 将OH\_NativeBuffer对象的引用计数减1，当引用计数为0的时候，该NativeBuffer对象会被析构掉。 |
| OH\_NativeBuffer\_GetConfig (OH\_NativeBuffer \*buffer, OH\_NativeBuffer\_Config \*config) | 用于获取OH\_NativeBuffer的属性。 |
| OH\_NativeBuffer\_Map (OH\_NativeBuffer \*buffer, void \*\*virAddr) | 将OH\_NativeBuffer对应的ION内存映射到进程空间。 |
| OH\_NativeBuffer\_Unmap (OH\_NativeBuffer \*buffer) | 将OH\_NativeBuffer对应的ION内存从进程空间移除。 |
| OH\_NativeBuffer\_GetSeqNum (OH\_NativeBuffer \*buffer) | 获取OH\_NativeBuffer的序列号。 |

详细的接口说明请参考[native\_buffer](../harmonyos-references/capi-oh-nativebuffer.md)。

## 开发步骤

以下步骤描述了如何使用NativeBuffer提供的Native API接口创建OH\_NativeBuffer实例，获取内存属性信息，并将ION内存映射到进程空间。

**添加动态链接库**

CMakeLists.txt中添加以下lib。

```
1. libnative_buffer.so
```

**头文件**

```
1. #include <native_buffer/native_buffer.h>
```

1. **创建OH\_NativeBuffer实例**。

   ```
   1. OH_NativeBuffer_Config config {
   2. .width = 0x100,
   3. .height = 0x100,
   4. .format = NATIVEBUFFER_PIXEL_FMT_RGBA_8888,
   5. .usage = NATIVEBUFFER_USAGE_CPU_READ | NATIVEBUFFER_USAGE_CPU_WRITE | NATIVEBUFFER_USAGE_MEM_DMA,
   6. };

   8. OH_NativeBuffer *nativeBuffer = OH_NativeBuffer_Alloc(&config);
   9. if (nativeBuffer == nullptr) {
   10. LOGE("OH_NativeBuffer_Alloc fail, nativeBuffer is null");
   11. }
   ```

   [NativeRender.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/NdkNativeWindow/entry/src/main/cpp/NativeRender.cpp#L200-L212)
2. **将OH\_NativeBuffer对应的ION内存映射到进程空间**。

   应用如需访问buffer内存空间，可通过OH\_NativeBuffer\_Map接口将ION内存映射到进程空间。

   ```
   1. void* virAddr = nullptr;
   2. int32_t ret = OH_NativeBuffer_Map(nativeBuffer, &virAddr);
   3. if (ret != 0) {
   4. LOGE("OH_NativeBuffer_Map Failed");
   5. }
   6. // ...
   7. ret = OH_NativeBuffer_Unmap(nativeBuffer);
   8. if (ret != 0) {
   9. LOGE("OH_NativeBuffer_Unmap Failed");
   10. }
   ```

   [NativeRender.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/NdkNativeWindow/entry/src/main/cpp/NativeRender.cpp#L213-L244)
3. **获取内存的属性信息**。

   ```
   1. OH_NativeBuffer_Config config2 = {};
   2. OH_NativeBuffer_GetConfig(nativeBuffer, &config2);
   3. uint32_t hwBufferID = OH_NativeBuffer_GetSeqNum(nativeBuffer);
   ```

   [NativeRender.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/NdkNativeWindow/entry/src/main/cpp/NativeRender.cpp#L220-L224)
4. **销毁OH\_NativeBuffer**。

   ```
   1. OH_NativeBuffer_Unreference(nativeBuffer);
   2. nativeBuffer = nullptr;
   ```

   [NativeRender.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/NdkNativeWindow/entry/src/main/cpp/NativeRender.cpp#L245-L248)
