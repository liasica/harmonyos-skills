---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-deviceinfo
title: @ohos.enterprise.deviceInfo（设备信息管理）
breadcrumb: API参考 > 系统 > 基础功能 > MDM Kit（企业设备管理服务） > ArkTS API > @ohos.enterprise.deviceInfo（设备信息管理）
category: harmonyos-references
scraped_at: 2026-04-28T08:10:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:91f847a12cc644958da6845b6636d1a2ac37dee37d489d217d84ffd572ceebfb
---

本模块提供企业设备信息管理能力，包括获取设备序列号、设备名称等。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../harmonyos-guides/mdm-kit-guide.md)。

## 导入模块

PhonePC/2in1Tablet

```
1. import { deviceInfo } from '@kit.MDMKit';
```

## deviceInfo.getDeviceInfo

PhonePC/2in1Tablet

getDeviceInfo(admin: Want, label: string): string

获取设备信息。

**需要权限：** ohos.permission.ENTERPRISE\_GET\_DEVICE\_INFO

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| label | string | 是 | 支持获取的设备信息标签。  - deviceName：设备名称。  - deviceSerial：设备序列号。  - simInfo：SIM卡信息。  - disk：硬盘信息。  - memory：内存信息，当前仅支持PC/2in1设备使用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回label对应的参数值。  当label为simInfo时，返回值为表示SIM卡信息的JSON字符串。例如：[{"slotId": 0, "MEID": "", "IMSI": "", "ICCID": "", "IMEI": "", "NUMBER": ""}, {"slotId": 1, "MEID": "", "IMSI": "", "ICCID": "", "IMEI": "", "NUMBER": ""}]，其中：slotId:0表示卡槽1，slotId:1表示卡槽2。 NUMBER：从API version 23开始支持，表示手机号码，格式为包含国家码的E.164国际标准格式（如 +8612345678901）。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { deviceInfo } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };

10. try {
11. // 需根据实际情况进行替换
12. let result: string = deviceInfo.getDeviceInfo(wantTemp, 'deviceName');
13. console.info(`Succeeded in getting device name, result : ${result}`);
14. } catch (err) {
15. console.error(`Failed to get device name. Code: ${err.code}, message: ${err.message}`);
16. }
```
