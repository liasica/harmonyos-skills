---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-network-resources
title: 网络资源低功耗建议
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 前台任务低功耗 > 前台资源合理使用 > 网络资源低功耗建议
category: best-practices
scraped_at: 2026-09-02T14:53:45+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:a3cb4aa723a7119714ddeda4ef693ea7761957350fa8f8663b5de7fc89259b71
---

## 建议

应用资源预缓存时，建议不要提前下载过多资源，以免SOC功耗和Wi-Fi功耗劣化。以小视频播放场景为例，如果提前加载前后视频片源数量过多，会导致功耗增加。

## 开发步骤

提前下载视频资源可使用有prefetch前缀的预加载接口。例如，网页加载资源使用的示例如下：

```typescript
// Load web resources in advance
this.webviewController.prefetchPage('url');
```

在小视频场景中，也有类似的预加载接口，用于加载当前片源的后续片源。建议预加载的片源数量不超过5个以优化功耗。
