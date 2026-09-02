---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-28
title: ohpm-repo获取最近下载量失败
breadcrumb: FAQ > DevEco Studio > 命令行工具 > ohpm-repo获取最近下载量失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:58+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ee98a424f0d3967ad0930eae96abf342563707bc49a2171c4f6aa5659792d24a
---

## 问题现象

ohpm-repo的5.0.7升级到5.0.8后，私仓报错获取最近一周包下载量数据失败, 所有ohpm包都无法下载。

## 背景知识

ohpm-repo私仓工具的概念、相关命令和如何部署可参考：[ohpm-repo私仓搭建工具](../harmonyos-guides/ide-ohpm-repo.md)。

## 问题定位

1. 查看服务器日志，[运行日志](../harmonyos-guides/ide-ohpm-repo-log.md#zh-cn_topic_0000001745217286_运行日志---runlog)和[错误运行日志](../harmonyos-guides/ide-ohpm-repo-log.md#section165144485914)均可，[日志具体路径](../harmonyos-guides/ide-ohpm-repo-log.md#zh-cn_topic_0000001745217286_日志存储路径)。查阅日志可以看到有“写入下载量文件失败”（该文件是ohpm-repo运行过程产生的用户信息，运行状态等数据存储配置，支持本地磁盘存储和mysql存储）。
2. 开发者的下载量是记录在本地的json文件中（db的type为filedb，默认路径为./db），查看json文件，发现json文件格式错误，最终导致写入文件失败，表现出获取下载量数据失败以及无法下载ohpm包。

## 分析结论

写入下载量的json文件格式错误，把json文件数据清空，设置为空数组，重新写入运行即恢复正常。

## 修改建议

对于企业单位，推荐使用数据库这种严格校验的方式存储，而不是使用json格式文件存储。改变db存储方式由本地磁盘filedb（此案例用本地json文件）转为mysql存储可以参考：[数据迁移](../harmonyos-guides/ide-ohpm-repo-data-migration.md)。
