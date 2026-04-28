---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-device-manager-err-code-h
title: oh_device_manager_err_code.h
breadcrumb: API参考 > 系统 > 网络 > Distributed Service Kit（分布式管理服务） > C API > 头文件 > oh_device_manager_err_code.h
category: harmonyos-references
scraped_at: 2026-04-28T08:08:16+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:6105d1fc7aebe367383e616082994e7534d882a177b9e56da73bb17378f79de7
---

## 概述

PhonePC/2in1TabletTVWearable

声明设备管理模块错误码信息。

**引用文件：** <distributedhardware/device\_manager/oh\_device\_manager\_err\_code.h>

**库：** libdevicemanager\_ndk.so

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**起始版本：** 20

**相关模块：** [DeviceManager](capi-devicemanager.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [DeviceManager\_ErrorCode](capi-oh-device-manager-err-code-h.md#devicemanager_errorcode) | DeviceManager\_ErrorCode | 分布式设备管理错误码信息。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### DeviceManager\_ErrorCode

PhonePC/2in1TabletTVWearable

```
1. enum DeviceManager_ErrorCode
```

**描述**

分布式设备管理错误码信息。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| ERR\_OK = 0 | 执行成功。 |
| ERR\_PERMISSION\_ERROR = 201 | 权限校验失败。 |
| ERR\_INVALID\_PARAMETER = 401 | 非法参数。 |
| DM\_ERR\_FAILED = 11600101 | 函数执行失败。 |
| DM\_ERR\_OBTAIN\_SERVICE = 11600102 | 获取设备管理服务失败。 |
| DM\_ERR\_OBTAIN\_BUNDLE\_NAME = 11600109 | 获取bundleName失败。 |
