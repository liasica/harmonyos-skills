---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-battery-usage-event
title: 24h功耗器件分解统计事件介绍
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 24h功耗器件分解统计事件 > 24h功耗器件分解统计事件介绍
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b0a3216ef5c5efa0af07605d64c6ae37aa44d9a0da8c57695809e54e6b699e10
---

## 简介

24h功耗器件分解统计事件用于统计应用在一天内的耗电统计信息，包含前后台使用时长以及耗电分解信息，每日0点统计应用耗电数据并上报。

如需了解如何使用HiAppEvent提供订阅24h功耗器件分解统计事件，请参考以下文档。目前仅提供ArkTS接口。

* [订阅24h功耗器件分解统计事件（ArkTS）](hiappevent-watcher-battery-usage-arkts.md)

说明

24h功耗器件分解统计事件不支持在[应用分身场景](app-clone.md)或[元服务场景](agc-harmonyos-create-faproject.md)使用HiAppEvent进行订阅，从API version 22开始支持在[输入法应用场景](inputmethod-application-guide.md)下使用HiAppEvent进行订阅。

## 检测原理

24h功耗器件分解统计是由系统hiview进程的功耗维测统计服务（XPower）实现相应的能力，它实现的基本过程如下：

1. 器件功耗建模：依据不同器件（屏幕、WIFI、Audio、蓝牙、Modem、CPU等）的耗电特征，建立器件的耗电模型，例如：屏幕的耗电与屏幕亮度、刷新帧率、显示内容等相关。
2. 在设备运行过程中，XPower实时采集各器件的耗电特性相关的状态数据，并依据器件耗电模型估算器件的耗电。
3. 器件的耗电关联到使用资源的应用，当多个应用使用某项器件时，XPower会将器件的耗电分摊到这些应用上，但不一定是均分。
4. 每日零点，XPower统计应用在24h的所有器件上的耗电信息，通过本事件上报给应用。

## 事件字段说明

params字段说明

24h功耗器件分解统计事件信息中params属性的详细描述如下：

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| time | number | 事件生成时间，单位为ms。 |
| bundle\_version | string | 应用版本。 |
| bundle\_name | string | 应用名称。 |
| begin\_time | number | 采集开始时间，单位为ms。 |
| end\_time | number | 采集结束时间，单位为ms。 |
| foreground\_usage | Array<number> | 每小时前台使用时长，单位为ms。 |
| background\_usage | Array<number> | 每小时后台使用时长，单位为ms。 |
| cpu\_foreground\_energy | Array<number> | 每小时CPU器件前台耗电量预估值，单位为mAs。 |
| cpu\_background\_energy | Array<number> | 每小时CPU器件后台耗电量预估值，单位为mAs。 |
| gpu\_foreground\_energy | Array<number> | 每小时GPU器件前台耗电量预估值，单位为mAs。 |
| gpu\_background\_energy | Array<number> | 每小时GPU器件后台耗电量预估值，单位为mAs。 |
| ddr\_foreground\_energy | Array<number> | 每小时DDR器件前台耗电量预估值，单位为mAs。 |
| ddr\_background\_energy | Array<number> | 每小时DDR器件后台耗电量预估值，单位为mAs。 |
| display\_foreground\_energy | Array<number> | 每小时display器件前台耗电量预估值，单位为mAs。 |
| display\_background\_energy | Array<number> | 每小时display器件后台耗电量预估值，单位为mAs。 |
| audio\_foreground\_energy | Array<number> | 每小时audio器件前台耗电量预估值，单位为mAs。 |
| audio\_background\_energy | Array<number> | 每小时audio器件后台耗电量预估值，单位为mAs。 |
| modem\_foreground\_energy | Array<number> | 每小时modem器件前台耗电量预估值，单位为mAs。 |
| modem\_background\_energy | Array<number> | 每小时modem器件后台耗电量预估值，单位为mAs。 |
| rom\_foreground\_energy | Array<number> | 每小时rom器件前台耗电量预估值，单位为mAs。 |
| rom\_background\_energy | Array<number> | 每小时rom器件后台耗电量预估值，单位为mAs。 |
| wifi\_foreground\_energy | Array<number> | 每小时wifi器件前台耗电量预估值，单位为mAs。 |
| wifi\_background\_energy | Array<number> | 每小时wifi器件后台耗电量预估值，单位为mAs。 |
| sensor\_foreground\_energy | Array<number> | 每小时sensor器件前台耗电量预估值，单位为mAs。  说明：从API version 22开始，支持该属性。 |
| sensor\_background\_energy | Array<number> | 每小时sensor器件后台耗电量预估值，单位为mAs。  说明：从API version 22开始，支持该属性。 |
| gps\_foreground\_energy | Array<number> | 每小时gps器件前台耗电量预估值，单位为mAs。  说明：从API version 22开始，支持该属性。 |
| gps\_background\_energy | Array<number> | 每小时gps器件后台耗电量预估值，单位为mAs。  说明：从API version 22开始，支持该属性。 |
| others\_foreground\_energy | Array<number> | 每小时其他器件前台耗电量预估值，单位为mAs。 |
| others\_background\_energy | Array<number> | 每小时其他器件后台耗电量预估值，单位为mAs。 |
