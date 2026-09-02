---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-jsvm-4
title: 如何自排查OOM(v8::FatalProcessOutOfMemory)错误
breadcrumb: FAQ > 应用框架开发 > NDK开发 > JSVM > 如何自排查OOM(v8::FatalProcessOutOfMemory)错误
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a3d16dad8e9f4a75dc4ccb6376d516af5ab643244e734d731d47089ff0091c41
---

**问题现象**

当应用内部申请的内存达到v8内存上限时，会触发OOM(v8::FatalProcessOutOfMemory)问题。对应的Crash栈信息如下:

```txt
#00 pc 0000000001d28a24 /system/lib64/ndk/libjsvm.so(v8::base::OS::Abort()+28)#01 pc 00000000014102c0 /system/lib64/ndk/libjsvm.so(v8::internal::V8::FatalProcessOutOfMemory(v8::internal::Isolate*, char const*, v8::OOMDetails const&)+756)#02 pc 0000000001629960 /system/lib64/ndk/libjsvm.so(v8::internal::Heap::FatalProcessOutOfMemory(char const*)+28)#03 pc 00000000016284a4 /system/lib64/ndk/libjsvm.so(v8::internal::Heap::CollectGarbage(v8::internal::AllocationSpace, v8::internal::GarbageCollectionReason, v8::GCCallbackFlags)+2100)#04 pc 000000000161df8c /system/lib64/ndk/libjsvm.so(v8::internal::HeapAllocator::AllocateRawWithLightRetrySlowPath(int, v8::internal::AllocationType, v8::internal::AllocationOrigin, v8::internal::AllocationAlignment)+1952)#05 pc 000000000161e810 /system/lib64/ndk/libjsvm.so(v8::internal::HeapAllocator::AllocateRawWithRetryOrFailSlowPath(int, v8::internal::AllocationType, v8::internal::AllocationOrigin, v8::internal::AllocationAlignment)+68)#06 pc 0000000001602744 /system/lib64/ndk/libjsvm.so(v8::internal::Factory::AllocateRaw(int, v8::internal::AllocationType, v8::internal::AllocationAlignment)+724)#07 pc 00000000015f41dc /system/lib64/ndk/libjsvm.so(v8::internal::FactoryBase<v8::internal::Factory>::NewFixedArray(int, v8::internal::AllocationType)+96)#08 pc 00000000017e8698 /system/lib64/ndk/libjsvm.so#09 pc 00000000018d86a4 /system/lib64/ndk/libjsvm.so(v8::internal::Object::CreateListFromArrayLike(v8::internal::Isolate*, v8::internal::Handle<v8::internal::Object>, v8::internal::ElementTypes)+1168)#10 pc 0000000001a0dd9c /system/lib64/ndk/libjsvm.so(v8::internal::Runtime_CreateListFromArrayLike(int, unsigned long*, v8::internal::Isolate*)+48)#11 pc 0000000000f6d0b4 /system/lib64/ndk/libjsvm.so(Builtins_CEntry_Return1_ArgvOnStack_NoBuiltinExit+84)#12 pc 0000000000eddbac /system/lib64/ndk/libjsvm.so(Builtins_CallWithArrayLike+812)
```

**解决措施**

在 OH\_JSVM\_Init 中传入 max-semi-space-size 和 max-old-space-size（单位均为 MB）的设置参数，以扩大 V8 的内存上限。观察扩大 V8 内存上限后，应用是否仍然崩溃。如果应用仍然崩溃，则需要使用内存泄漏检测工具来排查应用中是否存在内存泄漏问题。

```cpp
// ...
JSVM_InitOptions init_options;
init_options.argc = (int*)malloc(sizeof(int));
*init_options.argc = 3;
init_options.argv = (char**)malloc(3 * sizeof(char*));
init_options.argv[1] = "--max-semi-space-size=1024";
init_options.argv[2] = "--max-old-space-size=1024";
init_options.removeFlags = true;
init_options.externalReferences = nullptr;
      
JSVM_Status status = OH_JSVM_Init(&init_options);

if (status != JSVM_OK)  {
  // If the status is not JSVM-OK, it indicates that OH_JSVM_Init execution failed and init_options was not successfully set.
}
// ...
```

JSVM中的内存默认值如下：

* max\_semi\_space\_size: 16MB
* max\_old\_space\_size: 1400MB
* initial\_semispace\_size: 1MB
* initial\_old\_space\_size: 512MB
