---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-443
title: Scroll内容区的高度小于组件高度，是否无法滑动
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Scroll内容区的高度小于组件高度，是否无法滑动
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:56+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:64b4697f7f797f7d374422199b16f0f7b93ebdfc2d2fc707b12c5ca0951997e0
---

[scroll](../harmonyos-references/ts-container-scroll.md)组件可以通过[scrollable](../harmonyos-references/ts-container-scroll.md#scrollable)接口设置滚动方向，默认情况下(alwaysEnabled为false)，当内容尺寸不大于容器尺寸时无法滚动，当滚动方向设置为Vertical时，需要内容的高度大于scroll组件的高度才可以滚动；当滚动方向设置为Horizontal时，需要内容的宽度大于scroll组件的宽度才可以滚动。此外，如果将Scroll的[EdgeEffect](../harmonyos-references/ts-container-scroll.md#edgeeffect)的alwaysEnabled属性设置为true时，内容小于组件大小也可以滚动。

**参考链接**

[EdgeEffectOptions对象](../harmonyos-references/ts-container-scrollable-common.md#nestedscrolloptions10对象说明)

[设置alwaysEnabled属性为true示例代码](../harmonyos-references/ts-container-scroll.md#示例8单边边缘效果)
