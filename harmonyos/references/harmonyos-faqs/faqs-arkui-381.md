---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-381
title: onAreaChange回调事件和windowStatusChange回调事件两者有什么关系，时序是怎样的
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > onAreaChange回调事件和windowStatusChange回调事件两者有什么关系，时序是怎样的
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:38+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:3326050532ecdd9e8a659b354b52fa1f4a2b7a156d20390c00bd84803e6a8a7e
---

onAreaChange是组件的回调事件，在组件布局的位置或者宽高发生变化时回调，即布局变化可能由父容器调整等非窗口状态因素触发。而windowStatusChange是窗口的回调事件，在窗口状态变化时回调，即窗口状态变化可能由系统事件等非组件布局因素触发。二者描述的对象不同，触发顺序没有必然关系，如调整窗口大小时可能同时触发windowStatusChange和组件的onAreaChange，但两者由不同机制驱动，当用户调整窗口大小时，通常先触发windowStatusChange事件，随后由于布局变化触发组件的onAreaChange事件。
