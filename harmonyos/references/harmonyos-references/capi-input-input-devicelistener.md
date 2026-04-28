---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-devicelistener
title: Input_DeviceListener
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > C API > 结构体 > Input_DeviceListener
category: harmonyos-references
scraped_at: 2026-04-28T08:10:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:69b95b5722432c81ab16e9d0a9fb0fd16bff2e3f6672fb114971775accc80284
---

```
1. typedef struct Input_DeviceListener {...} Input_DeviceListener
```

## 概述

PhonePC/2in1TabletTVWearable

定义一个结构体用于监听设备热插拔。

**起始版本：** 13

**相关模块：** [input](capi-input.md)

**所在头文件：** [oh\_input\_manager.h](capi-oh-input-manager-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Input\_DeviceAddedCallback](capi-input-input-devicelistener.md#input_deviceaddedcallback) deviceAddedCallback | 定义一个回调函数，用于接收设备热插事件。 |
| [Input\_DeviceRemovedCallback](capi-input-input-devicelistener.md#input_deviceremovedcallback) deviceRemovedCallback | 定义一个回调函数，用于接收设备热拔事件。 |

### 成员函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*Input\_DeviceAddedCallback)(int32\_t deviceId)](capi-input-input-devicelistener.md#input_deviceaddedcallback) | Input\_DeviceAddedCallback() | 回调函数，用于接收输入设备的热插事件。 |
| [typedef void (\*Input\_DeviceRemovedCallback)(int32\_t deviceId)](capi-input-input-devicelistener.md#input_deviceremovedcallback) | Input\_DeviceRemovedCallback() | 回调函数，用于接收输入设备的热拔事件。 |

## 成员函数说明

PhonePC/2in1TabletTVWearable

### Input\_DeviceAddedCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*Input_DeviceAddedCallback)(int32_t deviceId)
```

**描述**

回调函数，用于接收输入设备的热插事件。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t deviceId | 输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。 |

### Input\_DeviceRemovedCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*Input_DeviceRemovedCallback)(int32_t deviceId)
```

**描述**

回调函数，用于接收输入设备的热拔事件。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t deviceId | 输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。 |
