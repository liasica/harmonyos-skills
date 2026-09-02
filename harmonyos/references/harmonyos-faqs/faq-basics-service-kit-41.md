---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-41
title: request.agent是否可以不发送结果通知
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > request.agent是否可以不发送结果通知
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:39+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:63ef80d8b2b8d3be74654f03335662a219bc4806f972153353f17b76ef00c040
---

## 问题现象

request.agent.create创建并开始下载任务，关闭app，为什么下载任务会继续下载不会停止？完成下载时，手机推送中心会有成功的通知，是否可以不发送该通知？尝试设置gauge参数，但无法达到预期效果。

## 背景知识

* @ohos.request模块在上传/下载任务的配置信息[config](../harmonyos-references/js-apis-request.md#requestagentconfig10)设置中有参数[mode](../harmonyos-references/js-apis-request.md#requestagentmode10)可设置前台任务（FOREGROUND）或后台任务（BACKGROUND），默认为后台任务，当应用切换到后台时，后台任务不会影响，可正常进行。
* [gauge参数](../harmonyos-references/js-apis-request.md#requestagentconfig10)用于控制后台任务的过程进度通知策略，仅应用于后台任务，默认值为false。
  + false：代表仅完成或失败的通知。
  + true：发出每个进度已完成或失败的通知。

## 解决方案

[mode](../harmonyos-references/js-apis-request.md#requestagentmode10)设置为前台任务时，在终止app或应用切后台一段时间后会失败/暂停，不会立即停止。

前台任务不显示在通知栏，对于后台任务默认会显示在通知栏，设置[gauge](../harmonyos-references/js-apis-request.md#requestagentconfig10)仅可控制后台任务的过程进度通知策略，但任务完成和失败时一定会显示，保证用户知道最后任务结果，及时做出相关处理。
