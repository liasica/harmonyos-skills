---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-vision-5
title: 活体检测动作个数常见问题
breadcrumb: FAQ > AI功能开发 > 机器学习 > 场景化视觉（Vision） > 活体检测动作个数常见问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:59+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:c60a03974bb8e2dd2b06789ebeebdef090ac4d346aaa611e997a42c156e174d8
---

## 问题现象

使用活体检测时，应用希望用户仅检测一次动作就可以完成活体检测，但是[ActionsNumber](../harmonyos-references/vision-interactive-liveness.md#actionsnumber)显示随机一个动作和两个动作暂未支持，请问这个功能什么时候能支持？是否支持指定动作的检测？

## 解决方案

活体检测能实时捕捉人脸或者通过眨眼、张嘴、摇头、点头等组合动作，验证用户是否为真实活体操作。为了增强活体检测的安全性，对动作数量进行了优化，当调用静默活体和动作活体的动作数量少于三个时，系统将自动升级至包含三个随机动作的模式，从而提升防攻击能力。关于后续是否支持低于三个动作请以官网信息ActionsNumber为准。

活体检测支持的检测动作有眨眼、张嘴、点头、注视、向左摇头、向右摇头等动作，当前仅支持随机3个或4个动作的组合，若开放指定动作将有被安全攻击的风险。
