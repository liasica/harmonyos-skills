---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-reader-2
title: Reader Kit中PageDataInfo的startDomPos或endDomPos值的含义是什么
breadcrumb: FAQ > 应用服务开发 > 电子书阅读服务（Reader Kit） > Reader Kit中PageDataInfo的startDomPos或endDomPos值的含义是什么
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:94d3fcc5900363886b777b5503c34b3963b75f82560768d62e54e1fd2dfed40c
---

## 问题现象

获取到PageDataInfo中的startDomPos，其中数字及符号的含义是什么？

## 解决方案

domPos可以简单理解为某个元素在DOM树中的位置，也就是根节点如何到该元素的路径。

完整的domPos格式如下：

章节标识=子节点索引=子孙节点索引#文字索引;@;进度。
