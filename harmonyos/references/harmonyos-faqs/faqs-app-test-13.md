---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-13
title: 录制成功但回放效果不符合预期
breadcrumb: FAQ > DevEco Studio > 应用测试 > 录制成功但回放效果不符合预期
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:20+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:39c5d1408729efecc1833def89ed9862195a2272ff12407b7af304086f690de7
---

**问题现象**

录制成功但回放效果不符合预期，未按照录制时的操作正确回放。

**可能原因**

1. 录制时或回放过程中手机、电脑存在息屏锁屏。
2. 录制时的工程与回放时的工程包名一致但源码不一致，导致组件布局出现偏差。

**解决措施**

1. 目前录制回放功能不支持手机端的任何息屏操作，电脑端Windows系统支持锁屏后回放，但Mac系统不支持锁屏后回放。请在实际使用时，确保手机处于解锁亮屏状态，否则会影响回放功能的体验。
2. 请确保录制和回放时工程的包名、源码保持一致。
