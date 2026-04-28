---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-preloading-resources
title: 资源提前加载
breadcrumb: 最佳实践 > 性能 > 性能优化 > 资源提前加载
category: best-practices
scraped_at: 2026-04-28T08:22:27+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:4a477b1e91e0ee14a6491a60bd8a344da05854f8991edab709e457fdfc222889
---

## 网络请求优化

在附带网络请求的页面跳转场景中，完成时延过长的绝大多数原因都是网络HTTP请求时间过长。由于网络请求受操作系统和外部环境制约，业务代码难以直接优化请求速度。因此应尽可能地[提前发起网络请求](bpta-click-to-complete-delay-analysis.md#section375382219020)。

## Web组件的预连接、预加载、预渲染

当遇到Web页面加载慢的场景，可以使用Web组件的预连接、预加载、预渲染能力，在应用空闲时间提前进行Web引擎初始化和页面加载，提升下一页面的启动和响应速度，具体原理与案例请参阅[Web组件开发性能提升指导](bpta-web-develop-optimization.md#section128761465256)。

## 预下载优化Image白块

为了减少白块的出现，开发者可以预下载网络图片，通过应用沙箱提前缓存。图片下载和解码应在组件创建前完成，当Image组件加载时，直接从应用沙箱中获取缓存数据。非首次请求时，系统会判断应用沙箱中是否存在资源，如果存在，则直接从缓存中获取，避免重复下载，从而减少Image加载大型网络图片时的白屏或白块显示时间，提升用户体验。具体原理与案例请参阅[Image白块解决问题指导](bpta-image-white-lump-solution.md)。
