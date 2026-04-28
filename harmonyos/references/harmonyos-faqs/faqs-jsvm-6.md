---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-jsvm-6
title: 如何解决Finalizer方法中执行JS代码崩溃问题
breadcrumb: FAQ > 应用框架开发 > NDK开发 > JSVM > 如何解决Finalizer方法中执行JS代码崩溃问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:58+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:4888f9e825ee2cb098fe38d556c266a2e8329b1c48cf292a98ffe765fa57b666
---

**问题现象**

崩溃的调用栈如下：

```
1. #00 pc 0000000001d2cfa8 /system/lib64/ndk/libjsvm.so(v8::base::OS::Abort()+28)
2. #01 pc 0000000001d21bfc /system/lib64/ndk/libjsvm.so(V8_Fatal(char const*, ...)+384)
3. #02 pc 000000000159ba30 /system/lib64/ndk/libjsvm.so(v8::internal::(anonymous namespace)::Invoke(v8::internal::Isolate*, v8::internal::(anonymous namespace)::InvokeParams const&)+2952)
4. #03 pc 000000000159ae24 /system/lib64/ndk/libjsvm.so(v8::internal::Execution::Call(v8::internal::Isolate*, v8::internal::Handle<v8::internal::Object>, v8::internal::Handle<v8::internal::Object>, int, v8::internal::Handle<v8::internal::Object>*)+96)
5. #04 pc 0000000001432154 /system/lib64/ndk/libjsvm.so(v8::Function::Call(v8::Local<v8::Context>, v8::Local<v8::Value>, int, v8::Local<v8::Value>*)+384)
6. #05 pc 0000000000c6e3e0 /system/lib64/ndk/libjsvm.so(OH_JSVM_CallFunction+348)
7. ........
8. #24 pc 0000000000c77df8 /system/lib64/ndk/libjsvm.so(JSVM_Env__::CallFinalizer(void (*)(JSVM_Env__*, void*, void*), void*, void*)+96)
9. #25 pc 0000000000c65f5c /system/lib64/ndk/libjsvm.so(non-virtual thunk to v8impl::Reference::Finalize()+108)
10. #26 pc 0000000000c65fdc /system/lib64/ndk/libjsvm.so(v8impl::Reference::WeakCallback(v8::WeakCallbackInfo<v8impl::Reference> const&)+76)
```

**原因分析**

目前JSVM注册的Finalizer方法中禁止执行JS代码，在崩溃调用栈中，Finalizer方法调用了OH\_JSVM\_CallFunction执行了JS代码。

**解决措施**

在Finalizer中，仅清理与JS对象生命周期绑定的对象，不调用JSVM API。 若要在JS对象生命周期结束后执行一段JS代码，可在Finalizer方法中将相关代码的执行加入到外层事件循环队列中，等待下次事件循环时调用，从而实现时序上的顺序。
