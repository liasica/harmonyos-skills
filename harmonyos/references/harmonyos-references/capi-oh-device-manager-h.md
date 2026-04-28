---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-device-manager-h
title: oh_device_manager.h
breadcrumb: API参考 > 系统 > 网络 > Distributed Service Kit（分布式管理服务） > C API > 头文件 > oh_device_manager.h
category: harmonyos-references
scraped_at: 2026-04-28T08:08:15+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:519b4c6cad0e1a62e9d1f1999d27cf60846d215aff1ea2adb9ac0501b8270366
---

## 概述

PhonePC/2in1TabletTVWearable

提供访问可信设备和本地设备信息的接口。

**引用文件：** <distributedhardware/device\_manager/oh\_device\_manager.h>

**库：** libdevicemanager\_ndk.so

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**起始版本：** 20

**相关模块：** [DeviceManager](capi-devicemanager.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [int32\_t OH\_DeviceManager\_GetLocalDeviceName(char \*\*localDeviceName, unsigned int &len)](capi-oh-device-manager-h.md#oh_devicemanager_getlocaldevicename) | 获取本地设备显示名。  设备显示名称涉及用户的隐私数据，需要应用提供相关隐私声明，声明设备显示名的用途。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_DeviceManager\_GetLocalDeviceName()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_DeviceManager_GetLocalDeviceName(char **localDeviceName, unsigned int &len)
```

**描述**

获取本地设备显示名。

设备显示名称涉及用户的隐私数据，需要应用提供相关隐私声明，声明设备显示名的用途。

**需要权限：** ohos.permission.READ\_LOCAL\_DEVICE\_NAME

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char \*\*localDeviceName | 表示本地设备显示名字符串的地址指针。使用后需要手动释放空间资源。应用具备 ohos.permission.READ\_LOCAL\_DEVICE\_NAME 权限，返回设备显示名称；否则返回设备默认名称。 |
| unsigned int &len | 表示本地设备显示名字符串的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的错误码。错误码定义详见[DeviceManager\_ErrorCode](capi-oh-device-manager-err-code-h.md#devicemanager_errorcode)。  返回[ERR\_OK](capi-oh-device-manager-err-code-h.md#devicemanager_errorcode)，表示执行成功。  返回[DM\_ERR\_FAILED](capi-oh-device-manager-err-code-h.md#devicemanager_errorcode)，表示函数执行失败。  返回[DM\_ERR\_OBTAIN\_SERVICE](capi-oh-device-manager-err-code-h.md#devicemanager_errorcode)，表示获取设备管理服务失败。  返回[DM\_ERR\_OBTAIN\_BUNDLE\_NAME](capi-oh-device-manager-err-code-h.md#devicemanager_errorcode)，表示获取bundleName失败。  返回[ERR\_INVALID\_PARAMETER](capi-oh-device-manager-err-code-h.md#devicemanager_errorcode)，表示参数localDeviceName是空指针或者\*localDeviceName是非空指针。 |

**示例：**

```
1. #include "napi/native_api.h"
2. #include "hilog/log.h"
3. #include <distributedhardware/device_manager/oh_device_manager.h>
4. #include <distributedhardware/device_manager/oh_device_manager_err_code.h>
5. static napi_value GetDeviceName(napi_env env, napi_callback_info info) {
6. napi_value result = nullptr;
7. napi_create_object(env, &result);
8. char *localDeviceName = nullptr; // 声明空字符串，不需要提前分配地址，接口内部会分配
9. unsigned int len = 0;
10. // 将空字符串的地址传给接口
11. int32_t ret = OH_DeviceManager_GetLocalDeviceName(&localDeviceName, len);
12. if (ret != ERR_OK) {
13. OH_LOG_ERROR(LOG_APP, "ret:%{public}d", ret);
14. }

16. napi_value code = nullptr;
17. napi_create_int32(env, ret, &code);
18. napi_set_named_property(env, result, "code", code);

20. if (ret == ERR_OK && localDeviceName != nullptr) {
21. napi_value deviceName = nullptr;
22. napi_create_string_utf8(env, localDeviceName, NAPI_AUTO_LENGTH, &deviceName);
23. napi_set_named_property(env, result, "deviceName", deviceName);
24. delete[] localDeviceName; // 释放内存

26. napi_value deviceNameLen = nullptr;
27. napi_create_int32(env, len, &deviceNameLen);
28. napi_set_named_property(env, result, "deviceNameLen", deviceNameLen);
29. }
30. return result;
31. }
```
