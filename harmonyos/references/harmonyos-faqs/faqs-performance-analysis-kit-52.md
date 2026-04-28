---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-52
title: 如何通过hdc命令唤醒设备和查看屏幕状态
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何通过hdc命令唤醒设备和查看屏幕状态
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:22+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:4d0abf61914f5a9d76957e8698e23499b4b5c99889e4108be2d70c4a2bca2f1e
---

唤醒设备：hdc shell power-shell wakeup。

查看屏幕状态：hdc shell hidumper -s 3301 -a

查询手机IMEI：首先，进入fastboot模式（hdc target boot bootloader），然后使用fastboot命令查询（fastboot oem get-psid）。
