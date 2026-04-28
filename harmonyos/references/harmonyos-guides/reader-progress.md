---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/reader-progress
title: 阅读进度通知
breadcrumb: 指南 > 应用服务 > Reader Kit（阅读服务） > 书籍内容交互 > 阅读进度通知
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b0cb437c2ecf42e578e8305837c86e949acc4ea7e9a30407222ddee879ba27bf
---

当页面展示时，会通过页面展示回调接口返回页面渲染信息。页面渲染信息提供用于阅读进度跳转的domPos及resourceIndex属性，开发者可将属性缓存到数据库当中，用于阅读进度的恢复。

## 接口说明

阅读进度通知涉及2个接口，具体介绍如下表所示。

| 接口名 | 描述 |
| --- | --- |
| [on('pageShow')](../harmonyos-references/reader-read-core.md#onpageshow) | 注册章节内容分页展示结果回调。 |
| [off('pageShow')](../harmonyos-references/reader-read-core.md#offpageshow) | 注销章节内容分页展示结果回调，可在页面销毁时调用。 |

## 开发准备

在进行阅读进度通知监听之前，请先确保已经“[构建阅读器](reader-read-page.md)”。

## 开发步骤

1. 通过ReaderComponentController组件控制器监听页面展示回调。

   当排版引擎渲染完页面后会回调on('pageShow')接口，将页面渲染信息进行返回。通过页面渲染信息的domPos及resourceIndex属性，可标识当前阅读进度。

   开发者可在on('pageShow')接口回调中将阅读进度实时保存到数据库当中，防止用户异常退出阅读器时的进度丢失。当用户下次继续阅读时，可将保存domPos及resourceIndex属性传入到[startPlay](../harmonyos-references/reader-read-core.md#startplay)接口中，用于阅读进度的恢复。

   ```
   1. aboutToAppear(): void {
   2. this.setOnPageShowListener();
   3. }

   5. private async setOnPageShowListener(){
   6. try {
   7. this.readerComponentController.on('pageShow', (data: readerCore.PageDataInfo): void => {
   8. // 开发者可在此保存内容分页排版数据，利用data.resourceIndex及data.startDomPos数据调用startPlay接口继续阅读
   9. hilog.info(0x0000, 'testTag', 'pageshow: data is: ' + JSON.stringify(data));
   10. });
   11. } catch (err) {
   12. hilog.error(0x0000, 'testTag', `failed to init, Code is ${err.code}, message is ${err.message}`);
   13. }
   14. }
   ```
2. 页面销毁时，需要调用注销页面展示接口。

   ```
   1. aboutToDisappear(): void {
   2. this.readerComponentController.off('pageShow');
   3. }
   ```
