---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-mdm-4
title: 如何设置升级策略
breadcrumb: FAQ > 系统开发 > 基础功能 > 企业设备管理（MDM） > 如何设置升级策略
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:22+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:3de8669155fa91f83b270ea7d669516a3996da68d9b24d8a02d6182956862129
---

## 问题现象

MDM应用中如何禁止用户主动去更新系统，其他的升级策略还有哪些。

## 背景知识

[systemManager.setOtaUpdatePolicy](../harmonyos-references/js-apis-enterprise-systemmanager.md#systemmanagersetotaupdatepolicy)：设置升级策略。此接口仅可在Stage模型下使用，并需要[ohos.permission.ENTERPRISE\_MANAGE\_SYSTEM](../harmonyos-guides/permissions-for-mdm-apps.md#ohospermissionenterprise_manage_system)权限。

## 解决方案

MDM Kit提供了企业设备管理[systemManager.setOtaUpdatePolicy](../harmonyos-references/js-apis-enterprise-systemmanager.md#systemmanagersetotaupdatepolicy)接口可以设置升级策略，接口第二个参数policy为[OtaUpdatePolicy](../harmonyos-references/js-apis-enterprise-systemmanager.md#otaupdatepolicy)类型，将OtaUpdatePolicy中的升级策略类型[PolicyType](../harmonyos-references/js-apis-enterprise-systemmanager.md#policytype)设置为PROHIBIT可实现禁止升级策略。

除了可设置禁止升级策略，还提供其他四种升级策略：

* 默认升级策略。周期提示用户，用户确认后升级。
* 强制升级策略。需指定最晚升级时间参数，具体行为如下：
  + 到达最晚升级时间前：
    - 距离该时间48小时前：按照默认提醒策略与内容提醒。
    - 距离该时间48小时内：按照默认提醒策略同时弹框和通知提醒，通知不可移除；内容修改成“您的单位要求此设备在YYYY/MM/DD之前更新至x.x.x(C00XXXXXXSD)。”；忽略自动下载开关，自动下载条件满足后即开始下载。
  + 到达最晚升级时间后：忽略自动下载以及夜间升级开关。按照默认提醒策略同时弹框和通知提醒，通知不可移除；内容修改成“您的单位要求此设备在YYYY/MM/DD之前更新至x.x.x(C00XXXXXXSD)。”；忽略自动下载开关，自动下载条件满足后即开始下载；忽略夜间升级开关，夜间升级条件满足后即夜间安装。
* 指定时间窗口升级策略。需指定时间窗口参数（installStartTime、installEndTime），时间窗口必须大于5分钟，具体行为如下：
  + 配置时间窗口[A，B]，获取窗口中的随机升级时间C，到达时间后满足空闲条件，自动升级。
  + 到达时间后不满足空闲条件且B-C大于半小时，在C和B之间重新生成随机时间D，到达D后若满足空闲条件则自动升级，若仍不满足空闲条件则24小时后再检测，窗口任务推迟到下一个[A，B]窗口。
  + 到达时间后不满足空闲条件且B-C小于或等于半小时，24小时后再检测，窗口任务推迟到下一个[A，B]窗口。
* 延迟升级策略。延迟指定时间后进入DEFAULT模式，周期提示用户升级。

使用升级策略接口中，常见注意事项如下：

* 内网升级场景下，需要先调用[systemManager.notifyUpdatePackages](../harmonyos-references/js-apis-enterprise-systemmanager.md#systemmanagernotifyupdatepackages)接口通知系统更新包，再调用该接口设置升级策略。
* [OtaUpdatePolicy](../harmonyos-references/js-apis-enterprise-systemmanager.md#otaupdatepolicy)中的version参数是指待升级软件的版本号，并不是OS系统版本号。
