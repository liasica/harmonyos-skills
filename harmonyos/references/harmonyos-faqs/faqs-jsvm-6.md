---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-jsvm-6
title: 如何解决Finalizer方法中执行JS代码崩溃问题
breadcrumb: FAQ > 应用框架开发 > NDK开发 > JSVM > 如何解决Finalizer方法中执行JS代码崩溃问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:a6d64c57f1ada50adeacd7b47f1e170a8d8c3f23573cfbd85d34be6ccf984ffa
---

**问题现象**

崩溃的调用栈如下：

```text
#00 pc 0000000001d2cfa8 /system/lib64/ndk/libjsvm.so(v8::base::OS::Abort()+28)
#01 pc 0000000001d21bfc /system/lib64/ndk/libjsvm.so(V8_Fatal(char const*, ...)+384)
#02 pc 000000000159ba30 /system/lib64/ndk/libjsvm.so(v8::internal::(anonymous namespace)::Invoke(v8::internal::Isolate*, v8::internal::(anonymous namespace)::InvokeParams const&)+2952)
#03 pc 000000000159ae24 /system/lib64/ndk/libjsvm.so(v8::internal::Execution::Call(v8::internal::Isolate*, v8::internal::Handle<v8::internal::Object>, v8::internal::Handle<v8::internal::Object>, int, v8::internal::Handle<v8::internal::Object>*)+96)
#04 pc 0000000001432154 /system/lib64/ndk/libjsvm.so(v8::Function::Call(v8::Local<v8::Context>, v8::Local<v8::Value>, int, v8::Local<v8::Value>*)+384)
#05 pc 0000000000c6e3e0 /system/lib64/ndk/libjsvm.so(OH_JSVM_CallFunction+348)
........
#24 pc 0000000000c77df8 /system/lib64/ndk/libjsvm.so(JSVM_Env__::CallFinalizer(void (*)(JSVM_Env__*, void*, void*), void*, void*)+96)
#25 pc 0000000000c65f5c /system/lib64/ndk/libjsvm.so(non-virtual thunk to v8impl::Reference::Finalize()+108)
#26 pc 0000000000c65fdc /system/lib64/ndk/libjsvm.so(v8impl::Reference::WeakCallback(v8::WeakCallbackInfo<v8impl::Reference> const&)+76)
```

**原因分析**

目前JSVM注册的Finalizer方法中禁止执行JS代码，在崩溃调用栈中，Finalizer方法调用了OH\_JSVM\_CallFunction执行了JS代码。

**解决措施**

在Finalizer中，仅清理与JS对象生命周期绑定的对象，不调用JSVM API。 若要在JS对象生命周期结束后执行一段JS代码，可在Finalizer方法中将相关代码的执行加入到外层事件循环队列中，等待下次事件循环时调用，从而实现时序上的顺序。
