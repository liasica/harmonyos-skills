---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-sensor-service-3
title: 关闭系统设置，使用vibrator模块设置的振动规则会失效
breadcrumb: FAQ > 系统开发 > 硬件 > 传感器（Sensor Service） > 关闭系统设置，使用vibrator模块设置的振动规则会失效
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cc88736d8913cb5f3311cb44745ef486cf5ab5957aa098c8c469488c7c7f5daa
---

## 问题现象

HarmonyOS关闭系统设置振动，使用@ohos.vibrator模块设置的振动规则会失效，与其他平台表现不一致，其他平台即使关闭之后也能响应的。

## 背景知识

* HarmonyOS系统中，振动功能可以通过[@ohos.vibrator (振动)](../harmonyos-references/js-apis-vibrator.md)模块进行控制，其中[startVibration()](../harmonyos-references/js-apis-vibrator.md#vibratorstartvibration9)接口用于根据指定的振动效果和振动属性触发马达振动。
* [usage](../harmonyos-references/js-apis-vibrator.md#usage9)：马达振动的使用场景。
* 设备振动功能由两种开关控制：
  + 三态开关：

    位置：设置-->声音与振动-->响铃--振动--静音（或者控制中心面板上的响铃--振动--静音）。

    功能：这是一种多状态开关，允许用户选择设备的声音和振动模式。具体来说，它可以设置为响铃模式（设备发出声音）、振动模式（设备在接收通知时振动）或静音模式（设备既不发声也不振动）。
  + 触感开关：

    位置：设置-->声音与振动-->系统触感反馈。

    功能：此开关主要用于控制系统的触感反馈，决定是否在操作界面时通过振动给予用户物理上的反馈。
* 硬件限制：需要使用真机验证，模拟器不具备物理振动功能。

## 解决方案

振动功能在不同的使用场景[usage](../harmonyos-references/js-apis-vibrator.md#usage9)下，有不同的管控规则。请严格按照管控规则，否则会导致与预期效果不一致的问题。代码示例参考[vibrator.startVibration](../harmonyos-references/js-apis-vibrator.md#vibratorstartvibration9)中的“3.按照指定时长触发马达振动”。

## 常见FAQ

Q：系统静音模式下调用startVibration，设备未振动。

A：检查startVibration接口中的usage参数值具体是什么。明确振动使用场景，usage参数值为unknown、touch、media、physicalFeedback、simulateReality时，受触感开关管控。在触感开关开启时，即使系统处于静音模式，也会振动。

Q：输入法类型应用不受系统触感开关控制，为什么？

A：输入法应用通常会自行管理振动反馈规则，所以为了用户体验，不受系统触感反馈开关管控。
