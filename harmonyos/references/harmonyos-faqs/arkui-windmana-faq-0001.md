---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-windmana-faq-0001
title: 如何设置禁止分屏
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 常见问题 > 如何设置禁止分屏
category: harmonyos-faqs
scraped_at: 2026-10-15T07:14:27+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:483569862903552d91b0f39d52ba590840c6a9c71bed28d9e59c30097caf37ac
---

**Q：如何设置禁止分屏？**

**A**：在应用开发阶段设置时，通过在module.json5配置文件中[abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)下的supportWindowMode属性设置fullscreen字段，设置后应用将强制全屏运行，无法进入分屏模式。
