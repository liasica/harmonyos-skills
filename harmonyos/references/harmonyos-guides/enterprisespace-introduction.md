---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-introduction
title: Enterprise Space Kit简介
breadcrumb: 指南 > 应用服务 > Enterprise Space Kit（企业数字空间服务） > Enterprise Space Kit简介
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:53+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7fa0982a369822a47c1b9209cc41f24bd2de391a74b09d68f6244d9bca06e783
---

Enterprise Space Kit（企业数字空间服务）为企业[MDM](mdm-kit.md)应用提供空间管控、空间互传管控API，用于企业空间灵活配置管理、空间互传文件发送策略管控。企业MDM应用可以通过集中管理、远程配置来保障空间满足企业业务需求及数据传输安全诉求。它广泛应用于政府机构、大型科技企业、央国企、商业银行等“一机两用”、“一企多网”场景，以确保企业员工高效易用，企业管理简单易管，企业数据安全隔离。

## 场景介绍

* 提供企业安全管控类[MDM](mdm-kit.md)应用设置空间数据外发审批信息、获取审批内容的能力，便于企业根据自身安全管控要求管理并审批空间文件外发事件。其中审批信息可包含文件信息、文件状态、文件发送对象、文件发送时间等信息。
* 提供统一的空间管理能力、下发空间管理策略，包括创建工作空间、移除工作空间、订阅空间事件等能力，便于企业根据自身业务需求配置管理。

## 约束与限制

### 支持的国家和地区

当前仅支持在中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）提供服务。

### 支持的设备

当前设备类型仅支持PC/2in1，支持的设备详见下表。

| 设备类型 | 产品型号 |
| --- | --- |
| PC/2in1 | 华为擎云系列 |

### 访问限制

在企业数字空间服务使能后，经过空间切换，处于后台的空间，其[公共目录](ide-device-file-explorer.md#section975311314172)数据可能无法访问。

## 模拟器支持情况

本Kit暂不支持模拟器。
