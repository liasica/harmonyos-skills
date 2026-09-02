---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-cloudfoundation-11
title: 关于云数据库访问限制的问题
breadcrumb: FAQ > 应用服务开发 > 云开发服务（Cloud Foundation Kit） > 关于云数据库访问限制的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e123e5e7fc274f68b03471a6f26d8b98c3dbee2bac8278798bd330aada27c579
---

## 问题现象

* **问题1**：如果满足某个查询条件的数据为2000条，且限制返回的数量为30条，以时间降序方式排序，返回的数据是哪30条数据？
* **问题2**：连接后台云数据库有连接池概念吗？如果多个用户同时访问云数据库，会不会连接池不够而导致排队，或者由于用户太多导致连不上？

## 背景知识

* 云数据库使用限制的[数据查询、写入、删除和事务](../AppGallery-connect-Guides/agc-clouddb-restrictions-0000001127557973.md#section107781227114511)中说明端侧每次查询云侧数据，查询结果中包含的数据条数上限为1000条。
* 云数据库使用限制的[数据库、对象类型和对象](../AppGallery-connect-Guides/agc-clouddb-restrictions-0000001127557973.md#section17493131914454)中说明单应用云侧连接数的上限为200000个。

## 解决方案

* **问题1**：如果满足查询条件的数据条数大于每次查询的数据条数，最终返回的30条数据是2000条满足查询条件数据中最新的30条数据。
* **问题2**：连接后台云数据库是有连接池的概念的，但是连接池是存在于HarmonyOS内部服务器和数据库之间，不存在于开发者用户和服务器之间，所以不会出现多个用户同时访问云数据库时，因为连接池不够而导致排队，或者由于用户太多导致连不上的情况。
