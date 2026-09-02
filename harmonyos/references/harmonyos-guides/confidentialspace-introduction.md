---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/confidentialspace-introduction
title: Confidential Space Kit简介
breadcrumb: 指南 > 系统 > 安全 > Confidential Space Kit（机密空间服务） > Confidential Space Kit简介
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:28+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:c029b3055cc42a88e64327615f5fe05b4860cfe0f5b2eedc7690d00d20834feb
---

Confidential Space Kit（机密空间服务）提供了在机密空间内部运行数据应用、处理隐私数据的能力，支持应用与系统、应用与应用在空间内安全地共享数据，防止隐私信息外泄。

## 场景介绍

Confidential Space Kit为应用提供了在对外隔离的计算环境中运行数据应用的系统能力。数据应用是机密空间内的一个独立程序，可以使用应用从空间外发送的数据，也可以使用系统或其他应用引入空间的数据，但是从空间向外发送的数据量被严格管控，从而避免用户隐私泄漏。应用开发者可以自行编写程序逻辑，放入机密空间内部计算，将计算后的信息传回空间外应用。本Kit可服务于风控、反诈等涉及多方用户数据的场景中，增强用户安全或用户体验。

## 约束与限制

### 支持的国家/地区

只支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

### 支持的设备

Phone、Tablet、PC/2in1。

## 模拟器支持情况

本Kit暂不支持模拟器。
