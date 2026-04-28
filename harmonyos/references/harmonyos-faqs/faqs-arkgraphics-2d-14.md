---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-14
title: 如何主动关闭CPU访问窗口缓冲区数据降低功耗
breadcrumb: FAQ > 图形开发 > 2D图形（ArkGraphics 2D） > 如何主动关闭CPU访问窗口缓冲区数据降低功耗
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:49+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f20f5725d7902ad3b80cb81f2b6a808a5f8d71d934496ed5c3112aaf4042d76a
---

当前操作系统的窗口缓冲区默认使用CPU访问，这具有良好的兼容性，但GPU访问窗口缓冲区的能效更高，而使用CPU访问的能效开销较大。如果开发者确定应用不需要CPU访问，可以手动关闭该功能，以提高应用的能效。

**问题现象**

自绘制应用在生产缓冲区内容时，默认使用CPU访问能力。由于CPU访问缓冲区效率较低，性能开销较大。

**解决措施**

如果确认应用不需要使用CPU访问窗口缓冲区数据，可以在首次获取窗口句柄（OnSurfaceCreatedCB）时关闭CPU访问能力，由硬件平台选择最佳的图像格式，以提高能效并降低功耗。

在首次获取窗口句柄（OnSurfaceCreatedCB）时，调用OH\_NativeWindow\_NativeWindowHandleOpt(…, SET\_USAGE, …)方法设置缓冲区USAGE的值，关闭CPU访问能力。系统将选择更高效的方法（如GPU）访问缓冲区。参考代码如下：

```
1. void OnSurfaceCreatedCB(OH_NativeXComponent *component, void *window) {
2. uint64_t usage = 0;
3. int32_t ret = OH_NativeWindow_NativeWindowHandleOpt((OHNativeWindow*)window, GET_USAGE, &usage);
4. usage &= ~NATIVEBUFFER_USAGE_CPU_READ;
5. int32_t ret2 = OH_NativeWindow_NativeWindowHandleOpt((OHNativeWindow*)window, SET_USAGE, usage);
6. }
```

[SurfaceCreatedCB.cpp](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/Arkgraphics2D/entry/src/main/ets/pages/SurfaceCreatedCB.cpp#L5-L10)

对于大型游戏等高负载场景，关闭CPU访问可提高能效约30%。
