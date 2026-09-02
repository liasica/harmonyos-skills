---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-hotspot-accelerate
title: 热点加速错误码
breadcrumb: API参考 > 系统 > 基础功能 > Linx Kit（灵犀加速库） > C API > 错误码 > 热点加速错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:02:11+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:ecb7928bea09b0910c84a8c77acf6e4ad63ca61165198e0bc35ee39a03f1a7e3
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 501 资源被其他线程占用

**错误信息**

Resource occupied by another thread.

**错误描述**

当前资源正在被其他线程使用，无法完成操作。

**可能原因**

1. 同一个热点加速上下文被多个线程同时操作。
2. 前一个异步操作尚未完成就进行了新的调用。

**处理步骤**

1. 确保同一上下文只在一个线程中使用。
2. 等待前一个操作完成后再进行新的操作。

## 1026800001 API 未正确初始化

**错误信息**

API not initialized properly.

**错误描述**

在使用热点加速API之前，需要先调用初始化接口。

**可能原因**

1. 未调用初始化接口就使用了其他API。
2. 初始化接口调用失败。

**处理步骤**

1. 确保在使用其他热点加速API之前先调用初始化接口。
2. 检查初始化接口的返回值，确保初始化成功。

## 1026800002 无效的上下文索引

**错误信息**

Invalid context index.

**错误描述**

传入的上下文索引无效。

**可能原因**

1. 传入的上下文索引超出了有效范围。
2. 上下文已经被销毁或失效。

**处理步骤**

1. 检查传入的上下文索引是否在有效范围内。
2. 确保上下文仍然有效且未被销毁。
