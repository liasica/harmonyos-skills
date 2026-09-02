---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-146
title: RCP远场通信是否支持流式返回请求数据
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > RCP远场通信是否支持流式返回请求数据
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:31095f0ec131e7187db1455c82f8f12c81e189978d71d1c2b15c3a46b8142174
---

## 问题现象

RCP怎么接收流式传输的数据，一直不断返回数据。

## 解决方案

* 使用官网[实现同步读写流](../harmonyos-guides/remote-communication-syncstreamreq.md)允许客户端与服务器之间以流的形式进行数据交互，而无需等待所有数据准备完毕，能显著提升用户体验。流式传输适用于大文件的上传下载、直播、实时数据更新等场景。
* 还可使用[session.fetch](../harmonyos-references/remote-communication-rcp.md#fetch)接口，在入参request对象的headers里面设置请求头内容，content字段里面设置请求体内容，流式响应在destination字段里设置为Stream对象即可进行处理。具体实现可参考[示例代码](https://gitee.com/harmonyos_samples/RcpFileTransfer/blob/master/entry/src/main/ets/service/FileRequest.ets)。
