---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-53
title: 使用productViewManager.loadProduct拉起的应用商店页如何在其他地方监听
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 使用productViewManager.loadProduct拉起的应用商店页如何在其他地方监听
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:51+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:10ff71a00bfd1fca50d41a8653ad62a7df103d011acc9ab7a8c4657de4b40290
---

## 问题现象

使用productViewManager.loadProduct拉起的应用商店页，通过uiObserver监听、window监听、UIContext.uiObserver监听，均无法收到page变化回调、window变化回调等回调，如何实现监听？

## 背景知识

* [productViewManager (应用市场推荐)](../harmonyos-references/store-productviewmanager.md)：提供展示应用/元服务详情页、应用内快捷方式加桌的能力。
* [使用Emitter进行线程间通信](../harmonyos-guides/itc-with-emitter.md)：Emitter是一种作用在进程内的事件处理机制，为应用程序提供订阅事件、发布事件、取消事件订阅的能力。

## 解决方案

[productViewManager.loadProduct](../harmonyos-references/store-productviewmanager.md#productviewmanagerloadproduct)接口用于展示应用详情页，下载安装目标应用。使用Callback回调，在加载应用详情页面时作为入参用于接收加载过程中的状态变化，包括以下三种状态：

* onError：回调函数，接收应用详情页加载失败的错误码；
* onAppear：回调函数，当应用详情页成功打开时回调该方法；
* onDisappear：回调函数，当应用详情页关闭时回调该方法。

当其他地方需要监听通过productViewManager.loadProduct接口拉起的应用详情页的状态变化时，可以[使用Emitter进行线程间通信](../harmonyos-guides/itc-with-emitter.md)配合实现。

* 例如，当通过productViewManager.loadProduct拉起应用详情页面，触发onAppear回调，在该回调中，调用[emitter.emit](../harmonyos-references/js-apis-emitter.md#emitteremit)发送指定的事件，在其他地方通过[emitter.on](../harmonyos-references/js-apis-emitter.md#emitteron)监听获取到应用详情页面拉起的事件。
