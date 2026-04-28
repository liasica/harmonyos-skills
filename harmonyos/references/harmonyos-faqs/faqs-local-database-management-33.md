---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-33
title: 如何获知数据存储沙箱路径
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 如何获知数据存储沙箱路径
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:18+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:0b6d68951db729d2077f1c207223cc3e3e66fd90a9ab1ac98c3f35b8c3a261d0
---

关系型数据库：

"/data/app/el2/100/database/(bundleName)/entry/rdb/"下的.db文件

键值型数据库：

"/data/app/el2/100/database/(bundleName)/entry/kvdb/<系统默认生成文件名>/single\_ver/main/"路径下的.db文件

首选项：

"data/app/el2/100/base/(bundleName)/haps/entry/preferences"路径下的文件

应用持久化存储路径：

"/data/app/el2/100/base/(bundleName)/haps/<模块名>/files/persistent\_storage"

通过[获取应用文件路径](../harmonyos-guides/application-context-stage.md#获取应用文件路径)获取kvStore、Rdb路径前缀databaseDir和preferences路径前缀preferencesDir，后面自行拼接。
