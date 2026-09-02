---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-49
title: 应用沙箱路径及访问URI的大小写分段规则是什么？
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 应用沙箱路径及访问URI的大小写分段规则是什么？
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:aa7f686b660df0481de5f260e1089942c1df09a6097370a147d06c6907a912ce
---

**问题描述**

应用沙箱路径及访问URI的大小写分段规则是什么？

**解决措施**

在应用沙箱路径和URI中，常用目录名和文件名的大小写敏感规则如下表：

一、大小写不敏感目录

| path | URI | 当前目录及子目录是否不敏感 |
| --- | --- | --- |
| /storage/Users/currentUser/Download | file://docs/storage/Users/currentUser/Download | 是 |
| /storage/Users/currentUser/Documents | file://docs/storage/Users/currentUser/Documents | 是 |
| /storage/Users/currentUser/Desktop | file://docs/storage/Users/currentUser/Desktop | 是 |
| /data/storage/el2/distributedfiles/<bundleName> | file://<bundleName>/data/storage/el2/distributedfiles/<bundleName> | 是 |
| /data/storage/el2/cloud/<bundleName> | file://<bundleName>/data/storage/el2/distributedfiles/<bundleName> | 是 |

二、大小写敏感目录

| path | URI | 当前目录及子目录是否敏感 |
| --- | --- | --- |
| /storage/Users/currentUser | file://docs//storage/Users/currentUser | 是 |
| /data/storage/el1/base | file://<bundleName>/data/storage/el1/base | 是 |
| /data/storage/el1/database | file://<bundleName>/data/storage/el1/database | 是 |
| /data/storage/el2/base | file://<bundleName>/data/storage/el2/base | 是 |
| /data/storage/el2/cloud | file://<bundleName>/data/storage/el2/cloud | 否 |
| /data/storage/el2/database | file://<bundleName>/data/storage/el2/database | 是 |

**例1**：/storage/Users/currentUser/Download/AAA/BBB目录大小写分段规则如下。

| 目录层级 | 是否大小写敏感 |
| --- | --- |
| storage | 敏感 |
| Users | 敏感 |
| currentUser | 敏感 |
| Download | 不敏感 |
| AAA | 不敏感 |
| BBB | 不敏感 |
