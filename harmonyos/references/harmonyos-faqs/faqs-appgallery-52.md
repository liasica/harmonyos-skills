---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-52
title: 应用市场新版本app推送机制
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 应用市场新版本app推送机制
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6b55bb737a69591d4b73210361dee004ca5f2e7bc5fb8188b4c8716385885f83
---

## 问题现象

应用市场有更新且应用没有启动就会更新，这个更新检测是拉还是推，如果是推，推送机制是什么？

## 解决方案

应用市场会根据设备网络情况、电量等因素，在闲时给开了自动更新的设备进行应用更新。通过任务机制触发拉取更新，并非对所有设备同时主动推送更新。
