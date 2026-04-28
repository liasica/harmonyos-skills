---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-467
title: Swiper左滑为什么会显示空白
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Swiper左滑为什么会显示空白
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:02+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:7747b6a6a2bc09cb4f19386e93eb03b6b71da6d0a72fe9d7b310e685a067f5d4
---

由于[cachedCount](../harmonyos-references/ts-container-swiper.md#cachedcount15)的isShown设为true，预加载节点进行绘制，当缓存数大于swiper实际包含的子组件数量时，会把空白内容渲染在右节点树，导致左滑时出现空白，把cachedCount的isShown设为false可以解决该问题。
