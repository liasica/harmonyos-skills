---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/external-log
title: external_log日志介绍
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 故障检测 > 通用日志 > external_log日志 > external_log日志介绍
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:45+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:ff893b890c9b038921eef4c6e3485d115326677c1783096d948a03ab00c9abe0
---

## 简介

从API版本26.0.1开始提供了external\_log日志管理者注册接口，确保故障日志沙箱目录容量达到阈值时通知应用清理删除external\_log文件。

external\_log是应用沙箱内的故障日志文件路径，当应用通过HiAppEvent订阅系统事件后，若对应系统事件被触发，系统参数对象params中将包含external\_log字段，开发者可依据该路径读取故障日志文件内容。

同一系统事件支持多个订阅者，每个订阅者获取的external\_log路径均不同，以确保各订阅者间的操作相互不影响，最多支持前100个订阅者获取独立的日志路径，超出此数量的订阅者将复用相同的日志路径。

目前提供ArkTS和C/C++两种接口注册external\_log日志管理者，按需选择。

* [external\_log日志清理（ArkTS）](external-log-arkts.md)
* [external\_log日志清理（C/C++）](external-log-ndk.md)

## 实现原理

应用通过订阅系统事件来获取对应系统事件发生时的external\_log故障日志文件内容，其实现原理如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/lM8iUETPTl2pNhyfMl_QIA/zh-cn_image_0000002817506973.png?HW-CC-KV=V1&HW-CC-Date=20261114T004605Z&HW-CC-Expire=31536000000&HW-CC-Sign=6D55BD7052D673DC758FFCF69C7921AC36EB5855A5B073492F1FDE5764544904)

详细步骤如下：

1. 应用运行过程中发生对应系统事件，DFX系统故障感知模块触发故障日志采集。
2. DFX系统将生成的external\_log写入应用沙箱目录。
3. HiAppEvent监视到应用沙箱目录有新生成故障日志。
4. HiAppEvent将external\_log字段写入系统事件的事件参数对象params中，随回调一同返回给应用观察者。
5. 应用开发者通过external\_log字段获取故障日志文件内容。

## 日志规格

external\_log目录包含/data/storage/el2/log/hiappevent、/data/storage/el2/log/watchdog、/data/storage/el2/log/resourcelimit。

日志规格可参考[系统事件故障日志目录规格](hiappevent-intro.md#系统事件故障日志目录规格)。

沙箱故障日志目录阈值：

1. /data/storage/el2/log/hiappevent/ 目录达到4MB时通知应用清理删除external\_log文件。
2. /data/storage/el2/log/resourcelimit/ 目录达到1500MB时通知应用清理删除external\_log文件。

## 约束与限制

external\_log日志管理者只允许被注册一次，已注册成功重复注册返回失败。

注册不会持久化，应用启动不会继承上一次的注册状态，需要重新注册。
