---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-477
title: 组件内转场(transition)新增内容动画生效，但删除内容动画不生效的可能原因是什么
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 组件内转场(transition)新增内容动画生效，但删除内容动画不生效的可能原因是什么
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:06+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:4a068c627cd0a31b49d33b230db6f6a4bc9cf1a18225223340a0eca92aa73f52
---

**问题描述**

当为List等组件设置组件内转场动画时，data数组size变化时展示对应的新增或删除动画，但删除动画未生效，可能是什么原因？

**解决措施**

检查组件是否设置了clip裁剪属性为true且未设置高度。例如给ListItem设置transition动画时，List组件默认的clip裁剪属性为true，若List未设置高度，则会根据子组件自动调整，删除item后，List的高度会减小，但未给List设置动画，由于未对List高度变化设置动画过渡，且clip裁剪区域同步缩小，即List的clip为true且有裁剪效果，因此被裁剪的删除动画不可见。

**参考链接**

[clip](../harmonyos-references/ts-universal-attributes-sharp-clipping.md#clip12)
