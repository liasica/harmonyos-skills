---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/reader-progress
title: 阅读进度通知
breadcrumb: 指南 > 应用服务 > Reader Kit（阅读服务） > 书籍内容交互 > 阅读进度通知
category: harmonyos-guides
scraped_at: 2026-10-15T07:05:40+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:f6d6eb8b8ef91276bec26f1d40b670d29dbf061097cee9c49eabadbd41e2a532
---

当页面展示时，会通过页面展示回调接口返回页面渲染信息。页面渲染信息提供用于阅读进度跳转的domPos及resourceIndex属性，开发者可将属性缓存到数据库当中，用于阅读进度的恢复。

## 接口说明

阅读进度通知涉及2个接口，具体介绍如下表所示。

| 接口名 | 描述 |
| --- | --- |
| [on('pageShow')](../harmonyos-references/reader-read-core.md#onpageshow) | 注册页面展示的通知服务，该通知在页面排版成功展示后触发。 |
| [off('pageShow')](../harmonyos-references/reader-read-core.md#offpageshow) | 注销章节内容分页展示结果回调，可在页面销毁时调用。 |

## 开发准备

在进行阅读进度通知监听之前，请先确保已经“[构建阅读器](reader-read-page.md)”。

## 开发步骤

1. 通过ReaderComponentController组件控制器监听页面展示回调。

   当排版引擎渲染完页面后会回调on('pageShow')接口，将页面渲染信息进行返回。通过页面渲染信息的domPos及resourceIndex属性，可标识当前阅读进度。

   开发者可在on('pageShow')接口回调中将阅读进度实时保存到数据库当中，防止用户异常退出阅读器时的进度丢失。当用户下次继续阅读时，可将保存domPos及resourceIndex属性传入到[startPlay](../harmonyos-references/reader-read-core.md#startplay)接口中，用于阅读进度的恢复。

   ```typescript
   // 保存页面展示回调函数引用，用于注销时使用
   private onPageShowCallback = (data: readerCore.PageDataInfo): void => {
     // 开发者可在此保存内容分页排版数据，利用data.resourceIndex及data.startDomPos数据调用startPlay接口继续阅读
     hilog.info(0x0000, 'ReaderLog', 'pageshow: data is: ' + JSON.stringify(data));
   }

   aboutToAppear(): void {
     this.setOnPageShowListener();
   }

   private setOnPageShowListener(): void {
     this.readerComponentController.on('pageShow', this.onPageShowCallback);
   }
   ```
2. 页面销毁时，需要调用注销页面展示接口，需传入原注册的回调函数引用。

   ```typescript
   aboutToDisappear(): void {
     this.readerComponentController.off('pageShow', this.onPageShowCallback);
   }
   ```
