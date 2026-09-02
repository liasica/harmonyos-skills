---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-device-manager-h
title: oh_device_manager.h
breadcrumb: API参考 > 系统 > 网络 > Distributed Service Kit（分布式管理服务） > C API > 头文件 > oh_device_manager.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:fc942d4f55d5560f5b2f6030f096509240b2dc502f19962915c28f03fd713807
---

## 概述

提供访问可信设备和本地设备信息的接口。

**引用文件：** <distributedhardware/device\_manager/oh\_device\_manager.h>

**库：** libdevicemanager\_ndk.so

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**起始版本：** 20

**相关模块：** [DeviceManager](capi-devicemanager.md)

## 汇总

### 函数

| 名称 | 描述 |
| --- | --- |
| [int32\_t OH\_DeviceManager\_GetLocalDeviceName(char \*\*localDeviceName, unsigned int &len)](capi-oh-device-manager-h.md#oh_devicemanager_getlocaldevicename) | 获取本地设备显示名。  设备显示名称涉及用户的隐私数据，需要应用提供相关隐私声明，声明设备显示名的用途。 |
| [int32\_t OH\_DeviceManager\_GetLocalDeviceNameC(char \*\*localDeviceName, unsigned int \*len)](capi-oh-device-manager-h.md#oh_devicemanager_getlocaldevicenamec) | 获取本地设备显示名。  设备显示名称涉及用户的隐私数据，需要应用提供相关隐私声明，声明设备显示名的用途。 |

## 函数说明

### OH\_DeviceManager\_GetLocalDeviceName()

```c
int32_t OH_DeviceManager_GetLocalDeviceName(char **localDeviceName, unsigned int &len)
```

**描述**

获取本地设备显示名。

设备显示名称涉及用户的隐私数据，需要应用提供相关隐私声明，声明设备显示名的用途。

**需要权限：** ohos.permission.READ\_LOCAL\_DEVICE\_NAME

**起始版本：** 20

**废弃版本：** 26.0.0

**替代接口：** [OH\_DeviceManager\_GetLocalDeviceNameC](capi-oh-device-manager-h.md#oh_devicemanager_getlocaldevicenamec)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char \*\*localDeviceName | 表示本地设备显示名字符串的地址指针。使用后需要手动释放空间资源。应用具备ohos.permission.READ\_LOCAL\_DEVICE\_NAME权限，返回设备显示名称；否则返回设备默认名称。 |
| unsigned int &len | 表示本地设备显示名字符串的长度。单位：字节 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的错误码。错误码定义详见[DeviceManager\_ErrorCode](capi-oh-device-manager-err-code-h.md#devicemanager_errorcode)。  返回[ERR\_OK](capi-oh-device-manager-err-code-h.md#devicemanager_errorcode)，表示执行成功。  返回[DM\_ERR\_FAILED](capi-oh-device-manager-err-code-h.md#devicemanager_errorcode)，表示函数执行失败。  返回[DM\_ERR\_OBTAIN\_SERVICE](capi-oh-device-manager-err-code-h.md#devicemanager_errorcode)，表示获取设备管理服务失败。  返回[DM\_ERR\_OBTAIN\_BUNDLE\_NAME](capi-oh-device-manager-err-code-h.md#devicemanager_errorcode)，表示获取bundleName失败。  返回[ERR\_INVALID\_PARAMETER](capi-oh-device-manager-err-code-h.md#devicemanager_errorcode)，表示参数localDeviceName是空指针或者\*localDeviceName是非空指针。 |

### OH\_DeviceManager\_GetLocalDeviceNameC()

```c
int32_t OH_DeviceManager_GetLocalDeviceNameC(char **localDeviceName, unsigned int *len)
```

**描述**

获取本地设备显示名。

设备显示名称涉及用户的隐私数据，需要应用提供相关隐私声明，声明设备显示名的用途。

**需要权限：** ohos.permission.READ\_LOCAL\_DEVICE\_NAME

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char \*\*localDeviceName | 表示本地设备显示名字符串的地址指针。使用后需要手动释放空间资源。应用具备ohos.permission.READ\_LOCAL\_DEVICE\_NAME权限，返回设备显示名称；否则返回设备默认名称。 |
| unsigned int \*len | 表示本地设备显示名字符串长度的地址指针。使用后需要手动释放空间资源。单位：字节 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的错误码。错误码定义详见[DeviceManager\_ErrorCode](capi-oh-device-manager-err-code-h.md#devicemanager_errorcode)。  返回[ERR\_OK](capi-oh-device-manager-err-code-h.md#devicemanager_errorcode)，表示执行成功。  返回[DM\_ERR\_FAILED](capi-oh-device-manager-err-code-h.md#devicemanager_errorcode)，表示函数执行失败。  返回[DM\_ERR\_OBTAIN\_SERVICE](capi-oh-device-manager-err-code-h.md#devicemanager_errorcode)，表示获取设备管理服务失败。  返回[DM\_ERR\_OBTAIN\_BUNDLE\_NAME](capi-oh-device-manager-err-code-h.md#devicemanager_errorcode)，表示获取bundleName失败。  返回[ERR\_INVALID\_PARAMETER](capi-oh-device-manager-err-code-h.md#devicemanager_errorcode)，表示参数localDeviceName是空指针或者\*localDeviceName是非空指针或者len是空指针。 |
