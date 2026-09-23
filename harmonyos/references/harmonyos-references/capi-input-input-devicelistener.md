---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-devicelistener
title: Input_DeviceListener
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > C API > 结构体 > Input_DeviceListener
category: harmonyos-references
scraped_at: 2026-09-24T06:54:07+08:00
doc_updated_at: 2026-09-23
content_hash: sha256:1552dab3a685bd4c87bc33e741e49aac9d84e7d2029f9c2657f48968eaf5b66a
---

```c
typedef struct Input_DeviceListener {...} Input_DeviceListener
```

## 概述

定义一个结构体用于监听设备热插拔，该功能适用于需要实时响应输入设备连接和断开场景的应用程序，如游戏、音乐播放器等。通过监听设备热插拔事件，应用程序可以及时更新输入状态，提升用户体验，避免因设备断开导致的异常情况。

**起始版本：** 13

**相关模块：** [input](capi-input.md)

**所在头文件：** [oh\_input\_manager.h](capi-oh-input-manager-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Input\_DeviceAddedCallback](capi-oh-input-manager-h.md#input_deviceaddedcallback) deviceAddedCallback | 定义一个回调函数，用于接收设备热插事件。 |
| [Input\_DeviceRemovedCallback](capi-oh-input-manager-h.md#input_deviceremovedcallback) deviceRemovedCallback | 定义一个回调函数，用于接收设备热拔事件。 |
