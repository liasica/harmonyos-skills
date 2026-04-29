---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-intro
title: MDM Kit简介
breadcrumb: 指南 > 系统 > 基础功能 > MDM Kit（企业设备管理服务） > MDM Kit简介
category: harmonyos-guides
scraped_at: 2026-04-29T13:33:26+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:9811cf192b0096e6442f04b984dfc0e9c518e8272a62f00b1f7a1a8fe2a6d18f
---

## 业务介绍

MDM Kit（企业设备管理服务）为企业MDM（Mobile Device Management）应用提供设备管理API，用于管理并保护公司设备上的数据和应用程序。[MDM应用](mdm-kit-term.md#mdm应用设备管理应用)可以通过集中管理、远程配置和监控来保障设备和数据的安全性和稳定性。它广泛应用于企业和政府机构，以确保员工和客户使用的设备和数据受到保护，实现企业高效管理、安全使用设备。

## 场景介绍

* 企业派发设备场景（COPE）：指企业统一购买笔记本电脑、平板电脑、智能手机等设备，并将这些设备分发给企业员工使用，这类设备的所属权属于企业，企业对这类设备进行统一管理。
* 自带设备办公场景（BYOD）：指一些企业允许员工携带自己的平板或智能手机到公司，并将这些设备接入办公环境，用于企业办公或者外来访客携带设备访问工厂、实验室等场景。

## 实现原理

框架层和服务层提供了enterprise\_device\_management部件和enterprise\_device\_management\_ext部件，enterprise\_device\_management部件提供了设备管理应用程序框架和基本设备管理能力，enterprise\_device\_management\_ext部件为HarmonyOS NEXT设备提供扩展的企业设备管理能力。设备管理应用通过[EnterpriseAdminExtensionAbility](mdm-kit-admin.md)来调用MDM Kit中的接口，实现管理设备的意图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/zPJ62dKmTPi6iWdRyDBeMg/zh-cn_image_0000002558764960.png?HW-CC-KV=V1&HW-CC-Date=20260429T053325Z&HW-CC-Expire=86400&HW-CC-Sign=D584C1C6DF793632EDBF9EA4EF5880711BBC8DACEC0538B3921014B662FB76DB)

## 约束与限制

* SDK版本为5.0.0（API 12）及以上。
* 仅支持Stage模型。
* 仅支持HarmonyOS NEXT设备。

## 模拟器支持情况

本Kit支持模拟器。

模拟器与真机存在通用差异，详情请参见“[模拟器与真机的差异](ide-emulator-specification.md#section1227613205203)”。
