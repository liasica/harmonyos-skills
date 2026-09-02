---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-51
title: ArkTS侧如何释放绑定的C++侧对象
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > ArkTS侧如何释放绑定的C++侧对象
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:973b51b6c6595ee8807dcd5ad567de9d8036cae156132b4e22696f8d1d31115b
---

**问题现象**

在Java中，垃圾回收机制可以自动回收对象。对于ArkTS对象内部创建并绑定的C++对象，可以通过类似Java的`finalize`方法实现自动内存回收，而无需开发者主动调用。

**解决措施**

ArkTS无法直接回收C++对象。在ArkTS侧业务完成后，可以通过接口向Native侧发送信号，在Native侧释放对象。具体方式如下：

在使用 napi\_wrap 绑定 ArkTS 对象与 C++ 对象时，通过定义回调函数来销毁 C++ 对象，该回调函数作为接口的第四个参数。绑定完成后，当 ArkTS 对象被回收时，会自动触发回调函数，销毁对应的 C++ 对象。

具体接口使用示例如下：

```cpp
napi_wrap(
    env, ArkTSDemo, CDemo,
    // Define a callback function for ArkTS object recycling to destroy C++objects and prevent memory leaks
    [](napi_env env, void *finalize_data, void *finalize_hint) {
        MyDemo *cDemo = (MyDemo *)finalize_data;
        delete cDemo;
        cDemo = nullptr;
    },
    nullptr, nullptr);
```
