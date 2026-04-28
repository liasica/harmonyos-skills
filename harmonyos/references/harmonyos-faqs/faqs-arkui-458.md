---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-458
title: FrameNode的性能为什么不如声明式
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > FrameNode的性能为什么不如声明式
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:01+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:cbb74c3e3b111eb864ecf9a111681e94fc2a2963071fab55575ea0fe9fa62832
---

FrameNode的属性设置流程比ArkTS要长，原因是：ArkTS采用声明式UI范式，在编译期生成完整的属性配置；FrameNode作为命令式UI节点，需要运行时动态应用属性变更，ArkTS是对组件的所有属性一次性完成设置，而FrameNode则是对节点的每个属性逐个进行设置，每次属性设置都需要跨语言通信，这是性能差异的主要来源。如果需要动态更改组件树或复用组件，建议仅设置或更改必要的属性以优化性能。
