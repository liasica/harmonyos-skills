---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-device-security-9
title: 如何判断系统是否root
breadcrumb: FAQ > 系统开发 > 安全 > 设备安全服务（Device Security） > 如何判断系统是否root
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1779c48e36e9511308af4e217a1098481a3fab76e3d184ab63cbba08f2756472
---

## 问题现象

HarmonyOS如何防止应用在系统root的情况下进行敏感操作，如何检测手机是否root？

## 解决方案

* 方法一：手机root之后可以查看更多的系统信息，可以使用hdc命令根据是否能查看相关信息来确定手机是否root，比如：
  1. 运行hdc shell param get命令，如果只有几行信息打印说明没有root。
  2. 运行hdc shell param get const.product.devicetype查看设备类型，提示fail，说明没有root。
* 方法二：运行hdc shell，进入的命令行观察用户身份是普通用户（$）还是管理员用户（#），如果是#手机则被root过，如果是$手机没有被root过。
* 方法三：通过代码[检查系统完整性](../harmonyos-guides/devicesecurity-sysintegrity-check.md)，包含在线检测与本地检测。根据safetyDetect.checkSysIntegrity返回结果进行判断。basicIntegrity为false则表示系统完整性存在风险。当basicIntegrity为false且detail为jailbreak则表示设备被越狱。
