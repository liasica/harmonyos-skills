---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-introduction
title: Enterprise Space Kit简介
breadcrumb: 指南 > 应用服务 > Enterprise Space Kit（企业数字空间服务） > Enterprise Space Kit简介
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:54+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:cee2f04ed08eed6698f01b8dca052d1495c377ebc9cf2b0f9faebb6033e0b021
---

Enterprise Space Kit（企业数字空间服务）为企业[MDM](mdm-kit.md)应用提供[企业数字空间](enterprisespace-introduction.md#企业数字空间基础特性)的空间管控、空间互传管控等API，助力企业依托MDM应用实现集中管理与远程配置，确保企业数字空间适配企业业务场景，同时满足数据传输安全管控要求。

## 企业数字空间基础特性

企业数字空间是擎云系列企业版核心特性之一，在同一物理终端上划分出互不干扰的“个人空间”与“企业空间”，企业空间统一管控工作数据，守护企业数据安全；个人空间处理对外工作、个人事务等，平衡了企业数据安全与员工办公效率这一对长期存在的矛盾。

**空间互传：** 企业数字空间专属应用，支持跨空间文件共享。企业可自主管控数据流转，保障数据安全，实现高效共创。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/B3ZepNOuRzuveyVbVoQJRA/zh-cn_image_0000002736434051.gif)

**空间切换：** 通过四指横滑、快捷键等多种便捷方式在两个空间之间丝滑切换，切换时身份、网络、数据整体切换。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/Rl9Y6xk3TdKyPrLXjWntHQ/zh-cn_image_0000002706834900.gif)

**空间开启：** 企业可通过HEM或MDM开启企业数字空间。HEM开启的具体操作步骤请参考[PC企业版配置](https://developer.huawei.com/business/cn/doc/HEM/hem_user-guide_add-reseller_management-devices-ot-0000002307766441#section1177603005511)。

## 场景介绍

Enterprise Space Kit提供以下功能，满足在企业数字空间的开发需求：

* [文件外发管控](enterprisespace-file-transfer-control.md)：提供设置审批信息、获取审批信息、配置空间互传单双通策略的能力。
* [工作空间管理](enterprisespace-lifecycle-management.md)：提供开启双空间功能并创建、查询、删除工作空间等能力。
* [工作空间配置](enterprisespace-workspace-configuration.md)：提供设置工作空间信息、资料照片、本地名称、状态栏图标等能力。
* [空间事件订阅](enterprisespace-event-subscription.md)：提供订阅和取消订阅空间事件的能力。
* [进程访问限制](enterprisespace-process-access-restriction.md)：提供设置系统服务进程不可访问后台用户数据，获取、新增和删除不可访问后台用户数据的系统服务进程列表等能力。
* [深度冻结策略](enterprisespace-lockdown-exemptionapps.md)：提供设置和查询深度冻结豁免名单的能力。
* [企业账号认证](enterprisespace-workspace-authentication.md)：提供企业认证和获取企业应用令牌的能力。
* [跨空间消息提醒](enterprisespace-cross-space-notification.md)：提供配置跨空间消息提醒的能力。

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
