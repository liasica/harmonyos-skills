---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-14
title: 如何主动关闭CPU访问窗口缓冲区数据降低功耗
breadcrumb: FAQ > 图形开发 > 2D图形（ArkGraphics 2D） > 如何主动关闭CPU访问窗口缓冲区数据降低功耗
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:46+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8c3cee16c5364e15082b760a2440766836c9156a843875bb6aeb8d27c0218604
---

当前操作系统的窗口缓冲区默认使用CPU访问，这具有良好的兼容性，但GPU访问窗口缓冲区的能效更高，而使用CPU访问的能效开销较大。如果开发者确定应用不需要CPU访问，可以手动关闭该功能，以提高应用的能效。

## 问题现象

自绘制应用在生产缓冲区内容时，默认使用CPU访问能力。由于CPU访问缓冲区效率较低，性能开销较大。

## 解决措施

如果确认应用不需要使用CPU访问窗口缓冲区数据，可以在首次获取窗口句柄（OnSurfaceCreatedCB）时关闭CPU访问能力，由硬件平台选择最佳的图像格式，以提高能效并降低功耗。

在首次获取窗口句柄（OnSurfaceCreatedCB）时，调用OH\_NativeWindow\_NativeWindowHandleOpt(…, SET\_USAGE, …)方法设置缓冲区USAGE的值，关闭CPU访问能力。系统将选择更高效的方法（如GPU）访问缓冲区。参考代码如下：

```cpp
void OnSurfaceCreatedCB(OH_NativeXComponent *component, void *window) {    
    uint64_t usage = 0;
    int32_t ret = OH_NativeWindow_NativeWindowHandleOpt((OHNativeWindow*)window, GET_USAGE, &usage);
    usage &= ~NATIVEBUFFER_USAGE_CPU_READ;
    int32_t ret2 = OH_NativeWindow_NativeWindowHandleOpt((OHNativeWindow*)window, SET_USAGE, usage);
}
```

对于大型游戏等高负载场景，关闭CPU访问可提高能效约30%。
