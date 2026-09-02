---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ime-5
title: 如何关闭安全键盘
breadcrumb: FAQ > 应用框架开发 > 输入法框架 > 输入法开发（IME） > 如何关闭安全键盘
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2271b59c85bf713458b555adb88eb1e1098f7b481d5b39c852c6490840cb8da8
---

## 问题现象

自动化测试，如何关闭安全键盘（输入密码），当前输入密码弹起安全键盘，导致视频流黑屏。

## 解决方案

背景：安全键盘运行在可信执行环境中，提供数据隔离和防篡改功能。

导致黑屏原因：为保证数据安全，键盘弹出会强制占用图形资源关闭视频流（导致黑屏）。

如为了自动化测试，建议如下：

1. 开发者通过预置输入值方式避开组件获取焦点弹出安全键盘。
2. 也可以通过全局动态配置键盘来规避安全键盘（debug环境使用普通键盘，release环境使用安全键盘）。
