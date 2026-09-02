---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-jsvm-7
title: 如何解决应用运行时OH_JSVM_CreateVM多线程创建发生竞争，导致VM内部的成员变量（array_buffer_allocator_）内存异常应用退出问题
breadcrumb: FAQ > 应用框架开发 > NDK开发 > JSVM > 如何解决应用运行时OH_JSVM_CreateVM多线程创建发生竞争，导致VM内部的成员变量（array_buffer_allocator_）内存异常应用退出问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f81d0a94157022d6ca04e48661aa3e6a294baa958d99f8358103f68ba09c5319
---

**问题现象**

崩溃的调用栈如下：

```text
#00 pc 00000000017793f8 /system/lib64/ndk/libjsvm.so
#01 pc 000000000163cef4 /system/lib64/ndk/libjsvm.so(v8::internal::Heap::AllocateExternalBackingStore(std::__h::function<void* (unsigned long)> const&, unsigned long)+212)
#02 pc 0000000001777454 /system/lib64/ndk/libjsvm.so(v8::internal::BackingStore::Allocate(v8::internal::Isolate*, unsigned long, v8::internal::SharedFlag, v8::internal::InitializedFlag)+220)
#03 pc 000000000149e420 /system/lib64/ndk/libjsvm.so
#04 pc 000000000149d99c /system/lib64/ndk/libjsvm.so(v8::internal::Builtin_ArrayBufferConstructor(int, unsigned long*, v8::internal::Isolate*)+260)
#05 pc 0000000000f75984 /system/lib64/ndk/libjsvm.so(Builtins_CEntry_Return1_ArgvOnStack_BuiltinExit+100)
#06 pc 0000000000ee6e40 /system/lib64/ndk/libjsvm.so(Builtins_JSBuiltinsConstructStub+320)
#07 pc 000000000102eae4 /system/lib64/ndk/libjsvm.so(Builtins_ConstructHandler+644)
#08 pc 0000000000ee9b88 /system/lib64/ndk/libjsvm.so(Builtins_InterpreterEntryTrampoline+264)
#09 pc 0000000000ee9b88 /system/lib64/ndk/libjsvm.so(Builtins_InterpreterEntryTrampoline+264)
```

**原因分析**

从调用栈分析，错误发生在 libjsvm.so 库中的 v8::internal::Heap::AllocateExternalBackingStore 函数。该函数在尝试分配外部存储时调用了 allocate 函数，并在 allocate 函数中出现了空指针异常。

```cpp
std::unique_ptr<BackingStore> BackingStore::Allocate(
    Isolate* isolate, size_t byte_length, SharedFlag shared,
    InitializedFlag initialized) {
  ...
  auto allocator = isolate->array_buffer_allocator();
  ...
  auto allocate_buffer = [allocator, initialized](size_t byte_length) {
      if (initialized == InitializedFlag::kUninitialized) {
        return allocator->AllocateUninitialized(byte_length);
      }
      void* buffer_start = allocator->Allocate(byte_length);
      if (buffer_start) {
        // TODO(wasm): node does not implement the zero-initialization API.
        // Reenable this debug check when node does implement it properly.
        constexpr bool
            kDebugCheckZeroDisabledDueToNodeNotImplementingZeroInitAPI = true;
        if ((!(kDebugCheckZeroDisabledDueToNodeNotImplementingZeroInitAPI)) &&
            !v8_flags.mock_arraybuffer_allocator) {
          DebugCheckZero(buffer_start, byte_length);
        }
      }
      return buffer_start;
  };
  buffer_start = isolate->heap()->AllocateExternalBackingStore(
      allocate_buffer, byte_length);
  ...
}
```

根据代码逻辑推断，错误的根本原因是 allocator为空。allocator 由 Isolate 的 array\_buffer\_allocator()方法返回，而 Isolate 是在 OH\_JSVM\_CreateVM 函数中通过 v8::Isolate::New(create\_params)创建的。因此，array\_buffer\_allocator 的初始化过程可能存在问题。array\_buffer\_allocator是在 OH\_JSVM\_CreateVM 函数中通过 GetOrCreateDefaultArrayBufferAllocator() 创建的。如果在多线程环境下，多个线程同时调用 OH\_JSVM\_CreateVM 函数，可能会导致 array\_buffer\_allocator 的创建过程出现竞争条件，从而引发内存异常。

在多线程环境下，OH\_JSVM\_CreateVM 函数的调用导致了 array\_buffer\_allocator 的创建过程出现竞争条件，从而使 allocator 对象为空。最终，AllocateExternalBackingStore 函数中引发了空指针异常。

**解决措施**

应用方需加锁处理，确保 OH\_JSVM\_CreateVM 调用期间，其他线程无法同时进入该代码块。这样可以确保每次只有一个线程可以创建 VM 实例，从而避免竞争条件。示例如下：

```cpp
// Create an instance of JSVM.
const JSVM_CreateVMOptions* options = new JSVM_CreateVMOptions();
JSVM_Status res = USVM_OK;
{
  std::Lock_guard<std::mutex> Lock(create_jsym_mutex_);
  res = OH_JSVM_CreateVM(options, &vm_);
}
if (res != JSVM_OK vm_ == nullptr) {
  XLOG(ERROR) << "JSVM create vm failed";
}
// When we start, open vm scope.
```
