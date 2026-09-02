---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputeventclient
title: 输入事件注入错误码
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > 错误码 > 输入事件注入错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:02:09+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e1169d579413c280c2a80cde150703afa1067f02d9f2758c27d621ed46fabcde
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码](errorcode-universal.md)。

## 3800001 输入服务异常

**错误信息**

Input service exception.

**错误描述**

当调用输入事件注入相关接口时，如果输入服务内部发生异常，会产生此错误码。

**可能原因**

1. 内存分配失败。
2. 线程繁忙。
3. 服务运行异常。
4. 其他非预期错误。

**处理步骤**

建议稍后重试。如果问题持续存在，请检查系统资源使用情况。

## 4300001 状态错误

**错误信息**

状态错误，根据具体接口和场景有以下不同情况。

**错误描述**

该错误码在不同接口中表示不同的状态错误：

* **pressKey 接口**：The key is already pressed and is not the most recently pressed key, or the number of pressed keys exceeds 5.

  当调用键盘控制器的pressKey接口时，如果按键已被按下且不是最近按下的按键，或已按下的按键数超过了5个，会产生此错误码。

  **可能原因**：按键已经被按下且不是最近按下的按键，或已按下的按键数超过了5个。

  **处理步骤**：确保按键在抬起状态下才能被按下；如果按键已被按下，确保它是最近按下的按键；确保同时按下的按键数量不超过5个。
* **releaseKey 接口**：The key is not pressed.

  当调用键盘控制器的releaseKey接口时，如果按键未被按下，会产生此错误码。

  **可能原因**：尝试抬起一个未被按下的按键。

  **处理步骤**：确保只抬起已经被按下的按键。
* **pressButton 接口**：The mouse button is already pressed.

  当调用鼠标控制器的pressButton接口时，如果鼠标按键已被按下，会产生此错误码。

  **可能原因**：鼠标按键已经处于按下状态。

  **处理步骤**：确保鼠标按键在抬起状态下才能被按下。
* **releaseButton 接口**：The mouse button is not pressed.

  当调用鼠标控制器的releaseButton接口时，如果鼠标按键未被按下，会产生此错误码。

  **可能原因**：尝试抬起一个未被按下的鼠标按键。

  **处理步骤**：确保只抬起已经被按下的鼠标按键。
* **beginAxis 接口**：The axis event is in progress.

  当调用鼠标控制器的beginAxis接口时，如果已有轴事件正在进行中，会产生此错误码。

  **可能原因**：已经有一个轴事件序列正在进行，尚未结束。

  **处理步骤**：确保在开始新的轴事件序列之前，先结束当前正在进行的轴事件序列。
* **updateAxis/endAxis 接口**：The axis event is not in progress.

  当调用鼠标控制器的updateAxis或endAxis接口时，如果没有轴事件正在进行中，会产生此错误码。

  **可能原因**：尝试更新或结束一个未开始的轴事件序列。

  **处理步骤**：确保在调用updateAxis或endAxis之前，先调用beginAxis开始轴事件序列。
* **touchDown 接口**：触点正在接触屏幕，或者触点ID不在有效范围[0, 9]内。

  当调用触控控制器的touchDown接口时，如果触点已接触屏幕或触点ID不在有效范围[0, 9]内，会产生此错误码。

  **可能原因**：触点已经处于按下状态，或触点ID不在有效范围[0, 9]内。

  **处理步骤**：调用touchDown前，请确保对应触点尚未接触屏幕，且触点ID在有效范围[0, 9]内。
* **touchMove/touchUp 接口**：触点未接触屏幕，或者触点ID不在有效范围[0, 9]内。

  当调用触控控制器的touchMove或touchUp接口时，如果触点尚未接触屏幕或触点ID不在有效范围[0, 9]内，会产生此错误码。

  **可能原因**：触点尚未处于按下状态，或触点ID不在有效范围[0, 9]内。

  **处理步骤**：调用touchMove或touchUp前，请先调用touchDown使对应触点接触屏幕，并确保触点ID在有效范围[0, 9]内。

## 4300002 显示器不存在

**错误信息**

The display does not exist.

**错误描述**

当调用鼠标控制器的moveTo接口或触控控制器的touchDown接口时，如果指定的显示器不存在，会产生此错误码。

**可能原因**

指定的displayId对应的显示器不存在。

**处理步骤**

使用有效的显示器ID，可以通过显示管理接口查询可用的显示器列表。
