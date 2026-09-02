---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-agent-framework-2
title: 智能体卡片变量问题
breadcrumb: FAQ > AI功能开发 > 计算平台 > 智能体框架（Agent Framework） > 智能体卡片变量问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:55:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:625ec2a0ad191f84e405e062e5954eb12b79773aaf0a8bff007229c09fc0924b
---

## 问题现象

1. 聚合链接怎么配，作用是啥？
2. 聚合变量作用是啥，怎么配？
3. 两个有啥区别？

## 解决方案

1. 聚合链接配置可参考：[通过聚合链接按指定方式跳转至应用](../harmonyos-guides/applinking-cross-platform.md)。聚合链接可用于实现在HarmonyOS系统的设备上点击链接后，按照指定的方式进行跳转。当用户打开链接时，聚合链接会引导用户跳转到HarmonyOS平台预览页、应用市场详情页、自定义网址、深度链接地址等页面。
2. 聚合变量是卡片中存储跳转目标信息的数据结构，定义了跳转所需的参数（如应用包名、服务名称、深度链接等）。其中：
   * webURL为点击整个卡片需要实际跳转的H5链接，要求为https地址。deepLink是对App的跳转。appLink是集成App Linking服务生成的，可查看[通过App Linking应用链接拉起指定应用](../harmonyos-guides/app-linking-startupapp.md)。
   * executeIntent是意图框架，具体可参考：[接入方案](../harmonyos-guides/intents-habit-rec-access-programme.md)。executeIntentReserves是备用意图框架，当主意图（executeIntent）执行失败或需降级处理时，系统会自动尝试按顺序执行executeIntentReserves中的备用意图。
3. 当变量类型为Array或者Object时，可以在内部填入聚合链接。当变量为Object(聚合链接)，需要填入聚合变量。
