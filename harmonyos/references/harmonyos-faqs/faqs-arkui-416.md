---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-416
title: Watch开发，ArcSwiper实现右滑退出
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Watch开发，ArcSwiper实现右滑退出
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:50+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:4c86ea2135bcdd185dd6b8e739e3d8f7e35cd7ee6d4e1ce0e959748169054013
---

通过[onGestureRecognizerJudgeBegin()](../harmonyos-references/ts-gesture-blocking-enhancement.md#ongesturerecognizerjudgebegin13)函数识别滑动位置，该函数通过比较触摸起始坐标与移动坐标的差值来判断滑动方向，示例代码参考：[示例](../harmonyos-references/ts-container-arcswiper.md#示例)。
