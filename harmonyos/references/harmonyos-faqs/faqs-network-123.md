---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-123
title: 目标IP是公司内网，请求失败，异常信息：Couldn't connect to server
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 目标IP是公司内网，请求失败，异常信息：Couldn't connect to server
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7315db97f97dfa9eb7e49015cf878b098a62a70a7a70f9d69a572f1a0e0aeef2
---

## 问题现象

使用真机调试应用，请求公司内网IP，连接失败，异常信息：Couldn't connect to server。

## 背景知识

* 若请求发送或接收的数据量较少，可使用[request](../harmonyos-references/js-apis-http.md#request)，若是大文件的上传或者下载，且关注数据发送和接收进度，可使用HTTP请求流式传输[requestInStream](../harmonyos-references/js-apis-http.md#requestinstream10)。
* [Remote Communication Kit](../harmonyos-guides/remote-communication-introduction.md)提供请求网络数据的功能，当前包含“HTTP请求能力”和“URPC（Unified Remote Procedure Call）高性能rpc通信库”等能力。
* 权限[ohos.permission.INTERNET](../harmonyos-guides/permissions-for-all.md#ohospermissioninternet)：允许使用Internet网络。

## 问题定位

* 检查手机是否能成功请求到普通外网地址，确认可以；确认结果说明已声明“ohos.permission.INTERNET”权限。
* 在与手机连接的电脑上请求相同的IP地址是否可以请求成功，确认可以；确认结果说明请求IP地址正确、可达。
* 检查手机是否可以请求公司其他内网地址，确认另一内网地址请求成功；确认结果说明请求代码正确。
* 检查手机WiFi与电脑是否同一局域网网段，尝试电脑开启热点，手机连接电脑热点再请求公司内网连接，请求成功。

## 分析结论

手机WiFi与请求IP不在同一局域网，导致无路由转发请求到目标IP。

## 修改建议

使用电脑开启的热点，确保连接的WiFi与请求目标URL在同一网段。

## 总结

想要通过连接公司WiFi请求公司内网地址成功，需要确保连接的WiFi与请求目标URL在同一网段。
