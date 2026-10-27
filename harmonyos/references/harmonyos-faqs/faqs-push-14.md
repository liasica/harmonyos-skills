---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-push-14
title: 自助分析结果显示“未查询到消息处理”
breadcrumb: FAQ > 应用服务开发 > 消息推送服务（Push Kit） > 自助分析结果显示“未查询到消息处理”
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:43+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:3d6d827ee3e83b5f7bad7a4c55782467e9f3f0dacd7dc5d7842d51667746b05d
---

## 问题现象

在HarmonyOS 开发者中心平台，按查询路径：“应用管理 -> 推广运营 -> 增长运营 -> 推送服务 -> 自助分析（Beta）”，在自助分析里面输入requestId和token，分析结果显示“未查询到消息处理”，可能是什么原因造成的。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/hHRG8sftR0yoO6qWxITwWw/zh-cn_image_0000002628394546.png "点击放大")

## 解决方案

* **步骤一**、使用自助分析前请先确认Push云侧REST API接口已发送推送消息成功返回响应码为[80000000-成功](../harmonyos-references/push-scenariozed-api-response.md#section80000000-成功)。
* **步骤二**、确认REST API接口已发送推送消息成功，仍无法查询到消息结果，可以排查以下两个方面：
  + 检查输入正确：requestId为发送消息后得到的请求标识（见[响应参数](../harmonyos-references/push-scenariozed-api-response.md#response-body)），同时请确保输入的是最新有效的token（见请求体参数说明-[target](../harmonyos-references/push-scenariozed-api-request-param.md#target)）。
  + 时间跨度超过3天的消息无法查询，请输入3天内的requestId和token。
