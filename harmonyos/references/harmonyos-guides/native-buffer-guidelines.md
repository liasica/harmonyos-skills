---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-buffer-guidelines
title: NativeBuffer开发指导 (C/C++)
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 图形缓冲区 > NativeBuffer开发指导 (C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:21+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:74aa1abceb4d69fa9b082b39ef78b43a1120fc133ee0df5808ed04f091ca6e5a
---

## 场景介绍

NativeBuffer模块提供**共享内存**功能，支持内存的申请、使用、查询和释放等操作。

NativeBuffer的常见应用场景包括：图像数据处理、视频编解码、跨进程内存共享等。开发流程通常包括：申请OH\_NativeBuffer实例、获取内存属性和将ION内存映射到进程空间。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| OH\_NativeBuffer\_Alloc (const OH\_NativeBuffer\_Config \*config) | 通过OH\_NativeBuffer\_Config创建OH\_NativeBuffer实例，每次调用都会产生一个新的OH\_NativeBuffer实例。本接口需要与OH\_NativeBuffer\_Unreference接口配合使用，否则会存在内存泄漏。 |
| OH\_NativeBuffer\_Reference (OH\_NativeBuffer \*buffer) | 将OH\_NativeBuffer对象的引用计数增加1。 |
| OH\_NativeBuffer\_Unreference (OH\_NativeBuffer \*buffer) | 将OH\_NativeBuffer对象的引用计数减1，当引用计数为0的时候，该NativeBuffer对象会被析构掉。 |
| OH\_NativeBuffer\_GetConfig (OH\_NativeBuffer \*buffer, OH\_NativeBuffer\_Config \*config) | 用于获取OH\_NativeBuffer的属性。 |
| OH\_NativeBuffer\_Map (OH\_NativeBuffer \*buffer, void \*\*virAddr) | 将OH\_NativeBuffer对应的ION内存映射到进程空间。 |
| OH\_NativeBuffer\_Unmap (OH\_NativeBuffer \*buffer) | 将OH\_NativeBuffer对应的ION内存从进程空间解除映射。 |
| OH\_NativeBuffer\_GetSeqNum (OH\_NativeBuffer \*buffer) | 获取OH\_NativeBuffer的序列号。 |

详细的接口说明请参考[OH\_NativeBuffer](../harmonyos-references/capi-oh-nativebuffer.md)。

## 开发步骤

以下步骤描述了如何使用NativeBuffer提供的Native API接口创建OH\_NativeBuffer实例，获取内存属性信息，并将ION内存映射到进程空间。

**添加动态链接库**

CMakeLists.txt中添加以下lib。

```txt
libnative_buffer.so
```

**头文件**

```
#include <native_buffer/native_buffer.h>
```

1. **创建OH\_NativeBuffer实例**。

   ```
   OH_NativeBuffer_Config config {
       .width = 0x100,
       .height = 0x100,
       .format = NATIVEBUFFER_PIXEL_FMT_RGBA_8888,
       .usage = NATIVEBUFFER_USAGE_CPU_READ | NATIVEBUFFER_USAGE_CPU_WRITE | NATIVEBUFFER_USAGE_MEM_DMA,
   };

   OH_NativeBuffer *nativeBuffer = OH_NativeBuffer_Alloc(&config);
   if (nativeBuffer == nullptr) {
       LOGE("OH_NativeBuffer_Alloc fail, nativeBuffer is null");
   }
   ```
2. **将OH\_NativeBuffer对应的ION内存映射到进程空间**。

   应用如需访问buffer内存空间，可通过OH\_NativeBuffer\_Map接口将ION内存映射到进程空间。

   ```
   void* virAddr = nullptr;
   int32_t ret = OH_NativeBuffer_Map(nativeBuffer, &virAddr);
   if (ret != 0) {
       LOGE("OH_NativeBuffer_Map Failed");
   }
   // ...
   ret = OH_NativeBuffer_Unmap(nativeBuffer);
   if (ret != 0) {
       LOGE("OH_NativeBuffer_Unmap Failed");
   }
   ```
3. **获取内存的属性信息**。

   ```
   OH_NativeBuffer_Config config2 = {};
   OH_NativeBuffer_GetConfig(nativeBuffer, &config2);
   uint32_t hwBufferID = OH_NativeBuffer_GetSeqNum(nativeBuffer);
   ```
4. **销毁OH\_NativeBuffer**。

   ```
   OH_NativeBuffer_Unreference(nativeBuffer);
   nativeBuffer = nullptr;
   ```
