---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-restrictions
title: "@ohos.enterprise.restrictions（限制类策略）"
breadcrumb: API参考 > 系统 > 基础功能 > MDM Kit（企业设备管理服务） > ArkTS API > @ohos.enterprise.restrictions（限制类策略）
category: harmonyos-references
scraped_at: 2026-09-02T15:02:11+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:e81be54a3782ce93cc588c1278faf731f62b10cf53b3987a89e83b717f345793
---

本模块提供设置通用限制类策略能力。可以全局禁用和解除禁用蓝牙、HDC、USB、Wi-Fi、蜂窝数据、相机、麦克风等特性。

**使用场景**：

* 企业设备管理场景下，管理员需要对员工设备进行功能限制，防止数据泄露或非授权使用。
* BYOD（Bring Your Own Device）场景下，企业空间需要限制设备功能以符合企业安全策略。
* 设备安全管控场景下，需要禁用特定功能以保护企业敏感信息。

**能解决的问题**：

* 防止员工通过蓝牙、USB等方式传输企业敏感数据。
* 限制设备调试能力（HDC）以提升设备安全性。
* 控制网络访问能力（Wi-Fi、蜂窝数据等）以符合企业网络策略。
* 管理设备多媒体能力（相机、麦克风等）以保护隐私和企业机密。

**带来的收益**：

* 提升企业设备安全性，降低数据泄露风险。
* 满足企业合规要求，符合安全审计标准。
* 实现精细化的设备功能管控，平衡安全与使用体验。

**说明** 

本模块首批接口从API version 12 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../harmonyos-guides/mdm-kit-guide.md)。

## 导入模块

```ts
import { restrictions } from '@kit.MDMKit';
```

## restrictions.setDisallowedPolicy(deprecated)

setDisallowedPolicy(admin: Want, feature: string, disallow: boolean): void

设置禁用/启用某特性。

**说明** 

本接口为设备级禁用策略，影响设备所有用户。如需针对特定用户设置禁用策略，请使用[setDisallowedPolicyForAccount](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicyforaccountdeprecated)接口。

**起始版本：** 12

**废弃版本：** 26.0.0

**替代接口：** [restrictions.setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy24)

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS 或者 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS15+ 或者 ohos.permission.ENTERPRISE\_MANAGE\_NETWORK（设置不同特性所需权限不同，具体请参考表1）

- 从API version 20开始，支持申请ohos.permission.ENTERPRISE\_MANAGE\_NETWORK权限。

- 从API version 15开始，支持申请ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS权限。

- API version 14及之前的版本，需要申请ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS权限。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [从严管控](../harmonyos-guides/mdm-kit-multi-mdm.md#规则1从严管控)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| feature | string | 是 | 支持设置的特性清单参考表1。  **说明：** 从API version 15开始，应用申请权限ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS并通过[startAdminProvision](js-apis-enterprise-adminmanager.md#adminmanagerstartadminprovision15)激活为[BDA](../harmonyos-guides/mdm-kit-term.md#byod-device-admin-bdabyod设备管理员)，可以使用此接口设置以下特性：bluetooth、hdc、microphone、usb、wifi、tethering、camera、screenshot、screenRecord、nearLink、resetFactory，从API版本26.0.0开始，新增支持使用此接口设置mtpServer特性。 |
| disallow | boolean | 是 | true表示禁止使用，false表示允许使用。 |

**表1 支持设置的特性清单：**

| 特性 | 说明 | 需要权限 |
| --- | --- | --- |
| bluetooth | 设备蓝牙能力。当已经通过[addDisallowedBluetoothDevices](js-apis-enterprise-bluetoothmanager.md#bluetoothmanageradddisallowedbluetoothdevices20)接口或者[addAllowedBluetoothDevices](js-apis-enterprise-bluetoothmanager.md#bluetoothmanageraddallowedbluetoothdevices)接口设置了蓝牙设备禁用名单或者允许名单，再通过本接口禁用设备蓝牙能力，会优先生效禁用设备蓝牙能力。直到设备蓝牙能力启用后，禁止或允许名单才会生效。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS 或 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| modifyDateTime | 设备修改系统时间能力。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| printer | 设备打印能力，在API version 23之前仅支持PC/2in1设备使用，从API version 23开始支持PC/2in1、Phone、Tablet设备。本接口禁用了设备打印能力时，通过[setDisallowedPolicyForAccount](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicyforaccountdeprecated)接口开启某用户的打印能力，该用户下的打印能力仍然被禁用。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| hdc | 被其他设备通过hdc连接、调试的能力。设置禁用后，其他设备无法通过hdc连接、调试此设备。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS 或 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| microphone | 设备麦克风能力。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS 或 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| fingerprint | 设备指纹认证能力。当已经通过[setDisallowedPolicyForAccount](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicyforaccountdeprecated)设置了某用户禁用设备指纹认证能力时，再通过本接口启用设备指纹认证能力，会报策略冲突。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| usb | 设备USB能力。禁用后外接的USB设备无法使用，即在当前设备为HOST模式时，无法外接其他DEVICE设备。  以下四种情况再通过本接口禁用设备USB能力，会报策略冲突。  1）通过[addAllowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageraddallowedusbdevices)接口添加了USB设备可用名单。  2）通过[setUsbStorageDeviceAccessPolicy](js-apis-enterprise-usbmanager.md#usbmanagersetusbstoragedeviceaccesspolicy)接口设置了USB存储设备访问策略为只读/禁用。  3）通过[addDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageradddisallowedusbdevices14)接口添加了禁止使用的USB设备类型。  4）通过[setDisallowedPolicyForAccount](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicyforaccountdeprecated)接口禁用了某用户USB存储设备写入能力。  5）通过[setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicydeprecated)接口（feature参数传入usbSerial）禁用了USB转串口。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS 或 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| wifi | 设备Wi-Fi能力。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS 或 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| tethering14+ | 网络共享能力（设备已有网络共享给其他设备的能力，即共享热点能力）。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS 或 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| inactiveUserFreeze14+ | 非活跃用户运行能力。禁用后，非UIAbility进程一般不会被冻结，UIAbility申请短时任务、长时任务、延迟任务或能效资源等后台运行任务也不会被冻结。当前仅支持PC/2in1设备使用。企业空间场景下，系统切换到企业空间用户，个人空间用户属于非活跃用户。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| camera14+ | 设备相机能力。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS 或 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| mtpClient18+ | MTP客户端能力（包含读取和写入），当前仅支持PC/2in1设备使用。MTP（Media Transfer Protocol，媒体传输协议），该协议允许用户在移动设备上线性访问媒体文件。当已经通过[setDisallowedPolicyForAccount](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicyforaccountdeprecated)设置了某用户禁用MTP客户端写入能力时，再通过本接口禁用MTP客户端能力，会报策略冲突。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| mtpServer18+ | MTP服务端能力，当前仅支持手机、平板设备使用。 | API版本26.0.0之前：ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS，API版本26.0.0开始：ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS 或 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| sambaClient20+ | samba客户端能力，当前仅支持PC/2in1设备使用。samba是在Linux和UNIX系统上实现SMB协议的一个免费软件，由服务器及客户端程序构成。SMB（Server Message Block，信息服务块）是一种在局域网上共享文件和打印机的一种通信协议，它为局域网内的不同计算机之间提供文件及打印机等资源的共享服务。SMB协议是客户机/服务器型协议，客户机通过该协议可以访问服务器上的共享文件系统、打印机及其他资源。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| sambaServer20+ | samba服务端能力，当前仅支持PC/2in1设备使用。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| backupAndRestore20+ | 备份和恢复能力，禁用后设备的"设置--系统--备份和恢复"、"设置--云空间"置灰，当前仅支持手机、平板使用。如果要完全禁用设备的备份和恢复能力，建议同时调用[applicationManager.addDisallowedRunningBundlesSync](js-apis-enterprise-applicationmanager.md#applicationmanageradddisallowedrunningbundlessync)接口禁止具备备份和恢复能力的应用运行，如备份和恢复、手机助手、云空间应用。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| maintenanceMode20+ | 设备维修模式能力。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| mms20+ | multimedia messaging service，设备接收、发送彩信的能力，当前仅支持手机、平板设备使用。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| sms20+ | short messaging service，设备接收、发送短信的能力，当前仅支持手机、平板设备使用。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| mobileData20+ | 蜂窝数据能力，当前仅支持手机、平板设备使用。 | ohos.permission.ENTERPRISE\_MANAGE\_NETWORK |
| airplaneMode20+ | 飞行模式能力，当前仅支持手机、平板设备使用。 | ohos.permission.ENTERPRISE\_MANAGE\_NETWORK |
| vpn20+ | Virtual Private Network（虚拟专用网络），VPN能力。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| notification20+ | 设备通知能力。禁用后，由系统应用和第三方应用发出的通知将不会显示，而系统服务通知能力不受影响。当此设备已经通过[addAllowedNotificationBundles](js-apis-enterprise-applicationmanager.md#applicationmanageraddallowednotificationbundles)设置了应用通知允许名单之后，再通过此接口禁用设备通知能力，会抛出错误码9200010。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| nfc20+ | Near Field Communication（近距离无线通信），NFC能力，当前仅支持手机、平板设备使用。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| privateSpace20+ | 创建隐私空间能力，当前仅支持手机、平板使用。对已创建的隐私空间无效。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| telephoneCall20+ | 设备通话能力，禁用后电话无法呼入和呼出。当前仅支持手机、平板设备使用。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| appClone21+ | [应用分身能力](../harmonyos-guides/app-clone.md)，禁用后无法创建应用分身。对已创建的应用分身无效。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| externalStorageCard21+ | 外置存储能力，禁用后设备无法使用外置存储，并且当前已连接的外置存储会被卸载。如果外置存储卸载时有文件正在被使用，可能会导致卸载失败，返回9200013错误码。  外置存储禁用后重新启用，需要手动重新连接外置存储。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| randomMac21+ | Wi-Fi连接时使用随机MAC能力，设置禁用后，连接Wi-Fi仅能使用设备物理MAC。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| unmuteDevice22+ | 设备媒体播放声音能力，设置禁用后，设备媒体播放将静音，[蜂窝通话](../harmonyos-guides/audio-call-overview.md)能力不受影响。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| hdcRemote22+ | 设备通过hdc调试其他设备的能力，当前仅支持PC/2in1设备设置。设置禁用后，无法通过hdc调试手机、平板、PC、智能手表等设备。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| virtualService23+ | 设备虚拟化服务能力，即利用硬件资源的冗余，以虚拟化方式运行其他平台（如Linux、Windows）的能力。设置禁用设备虚拟化服务能力时，建议同时卸载与虚拟化服务相关的应用，并禁止其再次安装。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| usbSerial24+ | 设备USB转串口能力。禁用后外接的USB转串口设备无法使用。以下两种情况再通过本接口禁用设备USB转串口能力，会报策略冲突。  1）通过[addAllowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageraddallowedusbdevices)接口添加了USB设备可用名单。  2）通过[setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicydeprecated)接口（feature参数传入usb）禁用了USB设备。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| screenshot | 设备截屏能力。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS 或 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| screenRecord | 设备录屏能力。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS 或 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| diskRecoveryKey | 恢复密钥导出能力。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| nearLink | 设备星闪能力。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS 或 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| developerMode14+ | 开发者模式，重启后生效，当前仅支持PC/2in1设备使用。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| resetFactory18+ | 恢复出厂能力。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS 或 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| remoteDesk20+ | 远程桌面能力，可通过点击我的华为-服务-快捷服务-智能检测-右上角更多-远程服务，查看远程桌面功能，当前仅支持手机、平板、PC/2in1设备使用。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| remoteDiagnosis20+ | 远程诊断能力，可通过点击我的华为-服务-快捷服务-智能检测-右上角更多-诊断分析，查看远程诊断功能，当前仅支持手机、平板、PC/2in1设备使用。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| otaUpdate20+ | 公网环境下系统升级能力。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200013 | The enterprise management policy has been successfully set, but the function has not taken effect in real time.  适用版本：21+ |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ts
import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 参数需根据实际情况进行替换
  restrictions.setDisallowedPolicy(wantTemp, 'printer', true);
  console.info('Succeeded in setting printer disabled');
} catch (err) {
  console.error(`Failed to set printer disabled. Code is ${err.code}, message is ${err.message}`);
}
```

## restrictions.getDisallowedPolicy(deprecated)

getDisallowedPolicy(admin: Want | null, feature: string): boolean

查询某特性是否被禁用。

**起始版本：** 12

**废弃版本：** 26.0.0

**替代接口：** [restrictions.getDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionsgetdisallowedpolicy24)

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS 或者 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS15+ 或者 ohos.permission.ENTERPRISE\_MANAGE\_NETWORK（查询不同特性所需权限不同，具体请参考表2）

- 从API version 20开始，支持申请ohos.permission.ENTERPRISE\_MANAGE\_NETWORK权限。

- 从API version 15开始，支持申请ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS权限。

- API version 14及之前的版本，需要申请ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS权限。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | null | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。API version 20之前，调用本接口查询某特性是否被禁用。当设备存在多个MDM应用时，传入admin查询对应admin设置的策略。从API version 20开始，admin新增支持传入null，传入null时查询整机实际生效的策略。 |
| feature | string | 是 | 支持查询的特性清单参考下表2。  **说明：** 从API version 15开始，应用申请权限ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS并通过[startAdminProvision](js-apis-enterprise-adminmanager.md#adminmanagerstartadminprovision15)激活为[BDA](../harmonyos-guides/mdm-kit-term.md#byod-device-admin-bdabyod设备管理员)，可以使用此接口获取以下特性状态：bluetooth、hdc、microphone、usb、wifi、tethering、camera、screenshot、screenRecord、nearLink、resetFactory，从API版本26.0.0开始，新增支持使用此接口获取mtpServer特性状态。 |

**表2 支持查询的特性清单：**

| 特性 | 说明 | 需要权限 |
| --- | --- | --- |
| bluetooth | 设备蓝牙能力。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS 或 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| modifyDateTime | 设备修改系统时间能力。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| printer | 设备打印能力，在API version 23之前仅支持PC/2in1设备使用，从API version 23开始支持PC/2in1、Phone、Tablet设备。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| hdc | 被其他设备通过hdc连接、调试的能力。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS 或 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| microphone | 设备麦克风能力。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS 或 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| fingerprint | 设备指纹认证能力。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| usb | 设备USB能力。禁用后外接的USB设备无法使用，即在当前设备为HOST模式时，无法外接其他DEVICE设备。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS 或 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| wifi | 设备Wi-Fi能力。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS 或 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| tethering14+ | 网络共享能力（设备已有网络共享给其他设备的能力，即共享热点能力）。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS 或 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| inactiveUserFreeze14+ | 非活跃用户运行能力。禁用后，非UIAbility进程一般不会被冻结，UIAbility申请短时任务、长时任务、延迟任务或能效资源等后台运行任务也不会被冻结。当前仅支持PC/2in1设备使用。企业空间场景下，系统切换到企业空间用户，个人空间用户属于非活跃用户。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| camera14+ | 设备相机能力。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS 或 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| mtpClient18+ | MTP客户端能力（包含读取和写入），当前仅支持PC/2in1设备使用。MTP（Media Transfer Protocol，媒体传输协议），该协议允许用户在移动设备上线性访问媒体文件。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| mtpServer18+ | MTP服务端能力，当前仅支持手机、平板设备使用。 | API版本26.0.0之前：ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS，API版本26.0.0开始：ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS 或 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| sambaClient20+ | samba客户端能力，当前仅支持PC/2in1设备使用。samba是在Linux和UNIX系统上实现SMB协议的一个免费软件，由服务器及客户端程序构成。SMB（Server Message Block，信息服务块）是一种在局域网上共享文件和打印机的一种通信协议，它为局域网内的不同计算机之间提供文件及打印机等资源的共享服务。SMB协议是客户机/服务器型协议，客户机通过该协议可以访问服务器上的共享文件系统、打印机及其他资源。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| sambaServer20+ | samba服务端能力，当前仅支持PC/2in1设备使用。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| backupAndRestore20+ | 备份和恢复能力，禁用后设备的"设置--系统--备份和恢复"、"设置--云空间"置灰，当前仅支持手机、平板使用。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| maintenanceMode20+ | 设备维修模式能力。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| mms20+ | multimedia messaging service，设备接收、发送彩信的能力，当前仅支持手机、平板设备使用。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| sms20+ | short messaging service，设备接收、发送短信的能力，当前仅支持手机、平板设备使用。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| mobileData20+ | 蜂窝数据能力，当前仅支持手机、平板设备使用。 | ohos.permission.ENTERPRISE\_MANAGE\_NETWORK |
| airplaneMode20+ | 飞行模式能力，当前仅支持手机、平板设备使用。 | ohos.permission.ENTERPRISE\_MANAGE\_NETWORK |
| vpn20+ | Virtual Private Network（虚拟专用网络），VPN能力。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| notification20+ | 设备通知能力。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| nfc20+ | Near Field Communication（近距离无线通信），NFC能力，当前仅支持手机、平板设备使用。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| privateSpace20+ | 创建隐私空间能力，当前仅支持手机、平板使用。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| telephoneCall20+ | 设备通话能力，禁用后电话无法呼入和呼出。当前仅支持手机、平板设备使用。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| appClone21+ | [应用分身能力](../harmonyos-guides/app-clone.md)，禁用后无法创建应用分身。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| externalStorageCard21+ | 外置存储能力。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| randomMac21+ | Wi-Fi连接时使用随机MAC能力。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| unmuteDevice22+ | 设备媒体播放声音能力，设置禁用后，设备媒体播放将静音，[蜂窝通话](../harmonyos-guides/audio-call-overview.md)能力不受影响。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| hdcRemote22+ | 设备通过hdc调试其他设备的能力，当前仅支持PC/2in1设备设置。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| virtualService23+ | 设备虚拟化服务能力。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| usbSerial24+ | 设备USB转串口能力。禁用后外接的USB转串口设备无法使用。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| screenshot | 设备截屏能力。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS 或 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| screenRecord | 设备录屏能力。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS 或 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| diskRecoveryKey | 恢复密钥导出能力。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| nearLink | 设备星闪能力。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS 或 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| developerMode14+ | 开发者模式，重启后生效，当前仅支持PC/2in1设备使用。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| resetFactory18+ | 恢复出厂能力。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS 或 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| remoteDesk20+ | 远程桌面能力，可通过点击我的华为-服务-快捷服务-智能检测-右上角更多-远程服务，查看远程桌面功能，当前仅支持手机、平板、PC/2in1设备使用。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| remoteDiagnosis20+ | 远程诊断能力，可通过点击我的华为-服务-快捷服务-智能检测-右上角更多-诊断分析，查看远程诊断功能，当前仅支持手机、平板、PC/2in1设备使用。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| otaUpdate20+ | 公网环境下系统升级能力。 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示feature对应的某种特性被禁用，false表示feature对应的某种特性未被禁用。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ts
import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 参数需根据实际情况进行替换
  let result: boolean = restrictions.getDisallowedPolicy(wantTemp, 'printer');
  console.info(`Succeeded in querying whether the printing function is disabled. Disabled status: ${result}`);
} catch (err) {
  console.error(`Failed to get printer disabled status. Code is ${err.code}, message is ${err.message}`);
}
```

## restrictions.setDisallowedPolicyForAccount(deprecated)

setDisallowedPolicyForAccount(admin: Want, feature: string, disallow: boolean, accountId: number): void

设置禁用/启用指定用户的某特性。

**起始版本：** 14

**废弃版本：** 26.0.0

**替代接口：** [restrictions.setDisallowedPolicyForAccount](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicyforaccount)

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [从严管控](../harmonyos-guides/mdm-kit-multi-mdm.md#规则1从严管控)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| feature | string | 是 | feature名称。  - fingerprint：设备指纹认证能力，当前仅支持PC/2in1设备使用。使用此参数时有以下规则：  1. 通过[setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicydeprecated)接口禁用了设备指纹认证能力，再使用本接口传入此参数，会报策略冲突。  2. 通过本接口设置禁用/启用指定用户的设备指纹认证能力后，再通过[setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicydeprecated)接口禁用设备指纹认证能力时，后者会覆盖前者的策略。此后再通过[setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicydeprecated)接口启用设备指纹认证能力，则所有用户都允许使用设备指纹认证能力。  - print20+：设备打印能力，在API version 23之前仅支持PC/2in1设备使用，从API version 23开始支持PC/2in1、Phone、Tablet设备。如果使用本接口禁用了指定用户的设备打印能力，再通过[setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicydeprecated)接口启用设备打印能力，该用户下的设备打印能力仍然被禁用。  - mtpClient20+：MTP客户端能力（仅包含写入），当前仅支持PC/2in1设备使用。MTP（Media Transfer Protocol，媒体传输协议），该协议允许用户在移动设备上线性访问媒体文件。当已经通过[setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicydeprecated)接口禁用了设备MTP客户端能力时，再通过本接口禁用某用户MTP客户端写入能力，会报策略冲突。  - usbStorageDeviceWrite20+：USB存储设备写入能力，当前仅支持PC/2in1企业设备使用。  以下三种情况再通过本接口禁用某用户USB存储设备写入能力，会报策略冲突。  1）通过[setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicydeprecated)接口设置了设备USB能力禁用。  2）通过[setUsbStorageDeviceAccessPolicy](js-apis-enterprise-usbmanager.md#usbmanagersetusbstoragedeviceaccesspolicy)接口设置了USB存储设备访问策略为只读/禁用。  3）通过[addDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageradddisallowedusbdevices14)接口添加了存储类型的USB设备禁用。  - diskRecoveryKey20+：恢复[密钥导出](../harmonyos-guides/huks-export-key-arkts.md)能力，当前仅支持PC/2in1设备使用。  - sudo20+：superuser do，表示以超级用户执行，当前仅支持PC/2in1设备使用。禁用后企业空间或个人空间不能以超级用户执行。  - distributedTransmissionOutgoing20+：设备间分布式单向传输数据的能力（仅包含向其他设备传输数据）。当已经通过[setDisallowedPolicyForAccount](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicyforaccount)接口禁用了分布式服务，再通过本接口禁用设备间分布式单向传输数据的能力，会报策略冲突。  - openFileBoost23+：[文件打开加速](preview-arkts-openfileboost-api.md)，为应用提供文件打开加速状态感知能力。应用可以通过接入对应API，感知文件的加速状态，进而应用可以实现对已加速文件给出独特的UI（user interface）标识等功能，优化用户文件打开体验，当前仅支持PC/2in1设备使用。 |
| disallow | boolean | 是 | true表示禁用，false表示启用。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。  accountId可以通过[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200010 | A conflict policy has been configured. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ts
import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 参数需根据实际情况进行替换
  restrictions.setDisallowedPolicyForAccount(wantTemp, 'fingerprint', true, 100);
  console.info('Succeeded in setting fingerprint disabled');
} catch (err) {
  console.error(`Failed to set fingerprint disabled. Code is ${err.code}, message is ${err.message}`);
}
```

## restrictions.getDisallowedPolicyForAccount(deprecated)

getDisallowedPolicyForAccount(admin: Want | null, feature: string, accountId: number): boolean

获取指定用户的某特性状态。

**起始版本：** 14

**废弃版本：** 26.0.0

**替代接口：** [restrictions.getDisallowedPolicyForAccount](js-apis-enterprise-restrictions.md#restrictionsgetdisallowedpolicyforaccount)

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | null | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。API version 20之前，调用本接口获取指定用户的某特性状态。当设备存在多个MDM应用时，传入admin查询对应admin设置的策略。从API version 20开始，admin新增支持传入null，传入null时查询整机实际生效的策略。 |
| feature | string | 是 | feature名称。  - fingerprint：设备指纹认证能力，当前仅支持PC/2in1设备使用。使用此参数时有以下规则：当已经通过[setDisallowedPolicyForAccount](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicyforaccountdeprecated)接口设置禁用/启用指定用户的设备指纹认证能力后，再通过[setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicydeprecated)接口禁用设备指纹认证能力时，后者会覆盖前者的策略。即此时调用本接口结果为false。  - mtpClient20+：MTP客户端能力（仅包含写入），当前仅支持PC/2in1设备使用。MTP（Media Transfer Protocol，媒体传输协议），该协议允许用户在移动设备上线性访问媒体文件。  - usbStorageDeviceWrite20+：USB存储设备写入能力，当前仅支持PC/2in1企业设备使用。  - diskRecoveryKey20+：恢复[密钥导出](../harmonyos-guides/huks-export-key-arkts.md)能力，当前仅支持PC/2in1设备使用。  - sudo20+：superuser do，表示以超级用户执行，当前仅支持PC/2in1设备使用。禁用后企业空间或个人空间不能以超级用户执行。  - distributedTransmissionOutgoing20+：设备间单向传输数据的能力（仅包含向其他设备传输数据）。  - print20+：设备打印能力，在API version 23之前仅支持PC/2in1设备使用，从API version 23开始支持PC/2in1、Phone、Tablet设备。如果使用[setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicydeprecated)接口禁用了设备打印能力，再通过[setDisallowedPolicyForAccount](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicyforaccountdeprecated)接口启用某用户下的设备打印能力，通过本接口查询结果是该用户已启用打印能力，但实际打印能力已被禁用。  - openFileBoost23+：[文件打开加速](preview-arkts-openfileboost-api.md)，为应用提供文件打开加速状态感知能力。应用可以通过接入对应API，感知文件的加速状态，进而应用可以实现对已加速文件给出独特的UI（user interface）标识等功能，优化用户文件打开体验，当前仅支持PC/2in1设备使用。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。  accountId可以通过[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示参数feature对应的特性被禁用，false表示参数feature对应的特性未被禁用。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ts
import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 参数需根据实际情况进行替换
  let result: boolean = restrictions.getDisallowedPolicyForAccount(wantTemp, 'fingerprint', 100);
  console.info(`Succeeded in querying is the fingerprint function disabled : ${result}`);
} catch (err) {
  console.error(`Failed to set fingerprint disabled. Code is ${err.code}, message is ${err.message}`);
}
```

## restrictions.addDisallowedListForAccount14+

addDisallowedListForAccount(admin: Want, feature: string, list: Array<string>, accountId: number): void

为指定用户添加禁止使用某特性的应用名单。指定用户下，添加到名单中的应用不允许使用指定的特性能力。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| feature | string | 是 | feature名称。  - snapshotSkip：屏幕快照能力。 |
| list | Array<string> | 是 | 应用包名列表。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。  accountId可以通过[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let valueList:Array<string> = ["com.xx.aa.", "com.xx.bb"];
try {
  // 参数需根据实际情况进行替换
  restrictions.addDisallowedListForAccount(wantTemp, 'snapshotSkip', valueList, 100);
  console.info('Succeeded in adding disallowed snapshotSkip feature');
} catch (err) {
  console.error(`Failed to add disallowed snapshotSkip feature. Code is ${err.code}, message is ${err.message}`);
}
```

## restrictions.removeDisallowedListForAccount14+

removeDisallowedListForAccount(admin: Want, feature: string, list: Array<string>, accountId: number): void

为指定用户移除禁止使用某特性的应用名单。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| feature | string | 是 | feature名称。  - snapshotSkip：屏幕快照能力。 |
| list | Array<string> | 是 | 包名等内容的名单集合。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。  accountId可以通过[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let valueList:Array<string> = ["com.xx.aa.", "com.xx.bb"];
try {
  // 参数需根据实际情况进行替换
  restrictions.removeDisallowedListForAccount(wantTemp, 'snapshotSkip', valueList, 100);
  console.info('Succeeded in removing disallowed snapshotSkip feature');
} catch (err) {
  console.error(`Failed to remove disallowed snapshotSkip feature. Code is ${err.code}, message is ${err.message}`);
}
```

## restrictions.getDisallowedListForAccount14+

getDisallowedListForAccount(admin: Want, feature: string, accountId: number): Array<string>

获取指定用户禁止使用某特性的应用名单。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| feature | string | 是 | feature名称。  - snapshotSkip：屏幕快照能力。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。  accountId可以通过[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 用户已添加的禁用某特征的应用名单。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 参数需根据实际情况进行替换
  let result: Array<string> = restrictions.getDisallowedListForAccount(wantTemp, 'snapshotSkip', 100);
  console.info('Succeeded in querying disallowed list for account');
} catch (err) {
  console.error(`Failed to query disallowed list for account. Code is ${err.code}, message is ${err.message}`);
}
```

## restrictions.setUserRestriction(deprecated)

setUserRestriction(admin: Want, settingsItem: string, restricted: boolean): void

设置用户行为的限制规则。

**起始版本：** 20

**废弃版本：** 26.0.0

**替代接口：** [restrictions.setUserRestriction](js-apis-enterprise-restrictions.md#restrictionssetuserrestriction)

**需要权限：** ohos.permission.ENTERPRISE\_SET\_USER\_RESTRICTION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [从严管控](../harmonyos-guides/mdm-kit-multi-mdm.md#规则1从严管控)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| settingsItem | string | 是 | 行为名称，仅支持以下值，传入其他值会报错。  - setApn：APN设置，当前仅支持手机、平板使用。  - powerLongPress：长按电源键打开电源菜单，当前仅支持手机、平板使用。  - setEthernetIp：修改以太网IP地址，当前仅支持PC/2in1设备使用。  - setDeviceName：修改设备名称，当前仅支持PC/2in1设备、手机、平板使用。禁用后，PC/2in1设备的设置中以下设备名称无法修改，包括关于本机、蓝牙、多设备协同->星闪。手机、平板设备设置中的关于本机、蓝牙、个人热点的设备名称无法修改。  - setBiometricsAndScreenLock：修改锁屏密码，当前仅支持PC/2in1设备、手机、平板使用。 |
| restricted | boolean | 是 | 是否禁用行为。true表示禁用，false表示不禁用。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ts
import { Want } from '@kit.AbilityKit';
import { restrictions } from '@kit.MDMKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 参数需根据实际情况进行替换
  restrictions.setUserRestriction(wantTemp, 'setApn', true);
  console.info('Succeeded in restricting from setting apn');
} catch (err) {
  console.error(`Failed to restrict from setting apn. Code is ${err.code}, message is ${err.message}`);
}
```

## restrictions.getUserRestricted(deprecated)

getUserRestricted(admin: Want, settingsItem: string): boolean

获取设置项的禁用状态。

**起始版本：** 20

**废弃版本：** 26.0.0

**替代接口：** [restrictions.getUserRestricted](js-apis-enterprise-restrictions.md#restrictionsgetuserrestricted)

**需要权限：** ohos.permission.ENTERPRISE\_SET\_USER\_RESTRICTION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| settingsItem | string | 是 | 指定设置项。  - setEthernetIp：修改以太网IP地址，当前仅支持PC/2in1设备使用。  - setDeviceName：修改设备名称，当前仅支持PC/2in1设备、手机、平板使用。PC/2in1设备设置中关于本机、蓝牙、多设备协同->星闪中的设备名称。手机、平板设备设置中关于本机、蓝牙、个人热点的设备名称。  - setBiometricsAndScreenLock：修改锁屏密码，当前仅支持PC/2in1设备、手机、平板使用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回指定设置项的禁用状态，true表示已禁用，false表示未禁用。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ts
import { Want } from '@kit.AbilityKit';
import { restrictions } from '@kit.MDMKit';

let wantTemp: Want = {
  // 需根据实际情况替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 入参需根据实际情况替换
  let result: boolean = restrictions.getUserRestricted(wantTemp, 'setEthernetIp');
  console.info('Succeeded in getting user restricted');
} catch (err) {
  console.error(`Failed to get user restricted. Code is ${err.code}, message is ${err.message}`);
}
```

## restrictions.setUserRestrictionForAccount(deprecated)

setUserRestrictionForAccount(admin: Want, settingsItem: string, accountId: number, restricted: boolean): void

设置指定用户行为的限制规则。

**起始版本：** 23

**废弃版本：** 26.0.0

**替代接口：** [restrictions.setUserRestrictionForAccount](js-apis-enterprise-restrictions.md#restrictionssetuserrestrictionforaccount)

**需要权限：** ohos.permission.ENTERPRISE\_SET\_USER\_RESTRICTION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [从严管控](../harmonyos-guides/mdm-kit-multi-mdm.md#规则1从严管控)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| settingsItem | string | 是 | 行为名称。  - modifyWallpaper：修改壁纸，包含锁屏壁纸和桌面壁纸。在配置此特性之前，此设备必须通过[HEM商用部署](https://developer.huawei.com/business/cn/doc/HEM/hem_user-guide_add-reseller_management-resellerr-0000002469112100)。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。  accountId可以通过[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。 |
| restricted | boolean | 是 | 是否禁用行为。true表示禁用，false表示不禁用。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ts
import { Want } from '@kit.AbilityKit';
import { restrictions } from '@kit.MDMKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let userId = 100;
let settingsItem: string = "modifyWallpaper";
try {
  restrictions.setUserRestrictionForAccount(wantTemp, settingsItem, userId, true);
  console.info('Succeeded in restricting from setting modifyWallpaper');
} catch (err) {
  console.error(`Failed to restrict from setting modifyWallpaper. Code is ${err.code}, message is ${err.message}`);
}
```

## restrictions.getUserRestrictedForAccount(deprecated)

getUserRestrictedForAccount(admin: Want | null, settingsItem: string, accountId: number): boolean

获取指定用户设置项的禁用状态。

**起始版本：** 23

**废弃版本：** 26.0.0

**替代接口：** [restrictions.getUserRestrictedForAccount](js-apis-enterprise-restrictions.md#restrictionsgetuserrestrictedforaccount)

**需要权限：** ohos.permission.ENTERPRISE\_SET\_USER\_RESTRICTION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | null | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| settingsItem | string | 是 | 指定设置项。  - modifyWallpaper：修改壁纸，包含锁屏壁纸和桌面壁纸。在配置此特性之前，此设备必须通过[HEM商用部署](https://developer.huawei.com/business/cn/doc/HEM/hem_user-guide_add-reseller_management-resellerr-0000002469112100)。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。  accountId可以通过[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回指定设置项的禁用状态，true表示已禁用，false表示未禁用。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ts
import { Want } from '@kit.AbilityKit';
import { restrictions } from '@kit.MDMKit';

let wantTemp: Want = {
  // 需根据实际情况替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

// 需根据实际情况替换
let userId = 100;
let settingsItem: string = "modifyWallpaper";
try {
  let result: boolean = restrictions.getUserRestrictedForAccount(wantTemp, settingsItem, userId);
  console.info(`Succeeded in getting user restricted: ${result}`);
} catch (err) {
  console.error(`Failed to get user restricted. Code is ${err.code}, message is ${err.message}`);
}
```

## restrictions.setDisallowedPolicy24+

setDisallowedPolicy(admin: Want, feature: FeatureForDevice, disallow: boolean): void

设置禁用/启用指定设备特性，禁用后相关设备特性无法被使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS 或 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [从严管控](../harmonyos-guides/mdm-kit-multi-mdm.md#规则1从严管控)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| feature | [FeatureForDevice](js-apis-enterprise-restrictions.md#featurefordevice24) | 是 | 指定要禁用或允许的设备特性。  **说明：** 应用申请权限ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS并通过[startAdminProvision](js-apis-enterprise-adminmanager.md#adminmanagerstartadminprovision15)激活为[BDA](../harmonyos-guides/mdm-kit-term.md#byod-device-admin-bdabyod设备管理员)，可以使用此接口设置以下特性：[FeatureForDevice.WIFI\_P2P](js-apis-enterprise-restrictions.md#featurefordevice24)。 |
| disallow | boolean | 是 | true表示禁止使用，false表示允许使用。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200010 | A conflict policy has been configured. |
| 9200013 | The enterprise management policy has been successfully set, but the function has not taken effect in real time. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ts
import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  restrictions.setDisallowedPolicy(wantTemp, restrictions.FeatureForDevice.WIFI_P2P, true);
  console.info('Succeeded in setting Wi-Fi P2P disabled');
} catch (err) {
  console.error(`Failed to set Wi-Fi P2P disabled. Code is ${err.code}, message is ${err.message}`);
}
```

## restrictions.getDisallowedPolicy24+

getDisallowedPolicy(admin: Want | null, feature: FeatureForDevice): boolean

查询指定设备特性是否被禁用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS 或 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | null | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| feature | [FeatureForDevice](js-apis-enterprise-restrictions.md#featurefordevice24) | 是 | 指定要查询的设备特性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示feature对应的设备特性被禁用，false表示feature对应的设备特性未被禁用。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ts
import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let result: boolean = restrictions.getDisallowedPolicy(wantTemp, restrictions.FeatureForDevice.WIFI_P2P);
  console.info(`Succeeded in querying whether Wi-Fi P2P is disabled. Disabled status: ${result}`);
} catch (err) {
  console.error(`Failed to get Wi-Fi P2P disabled status. Code is ${err.code}, message is ${err.message}`);
}
```

## restrictions.setDisallowedPolicyForAccount

setDisallowedPolicyForAccount(admin: Want, feature: FeatureForAccount, disallow: boolean, accountId: number): void

设置禁用/启用指定用户的某特性。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [从严管控](../harmonyos-guides/mdm-kit-multi-mdm.md#规则1从严管控)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| feature | [FeatureForAccount](js-apis-enterprise-restrictions.md#featureforaccount) | 是 | 要禁用或允许的用户特性。  当feature值为SUPER\_HUB时，如果已经通过[addUserNonStopApps](js-apis-enterprise-applicationmanager.md#applicationmanageraddusernonstopapps22)接口将中转站添加到当前用户下不可关停的应用列表中，再调用本接口禁用中转站，会发生策略冲突，抛出9200010错误码。可以通过[removeUserNonStopApps](js-apis-enterprise-applicationmanager.md#applicationmanagerremoveusernonstopapps22)接口将中转站从当前用户下不可关停的应用列表中移除来解决冲突。  当feature值为DISTRIBUTED\_TRANSMISSION时，如果已经通过[setDisallowedPolicyForAccount](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicyforaccountdeprecated)接口禁用设备间分布式单向传输数据的能力，再调用本接口禁用分布式管理服务，会发生策略冲突，抛出9200010错误码。可以通过[setDisallowedPolicyForAccount](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicyforaccountdeprecated)接口取消禁用设备间分布式单向传输数据来解决冲突。 |
| disallow | boolean | 是 | true表示禁用，false表示启用。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。  accountId可以通过[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。  当feature值为SUPER\_HUB时，accountId仅支持传入当前用户的用户ID，不支持跨用户设置。否则会抛出9200012错误码。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200010 | A conflict policy has been configured. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ts
import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 参数需根据实际情况进行替换
  restrictions.setDisallowedPolicyForAccount(wantTemp, restrictions.FeatureForAccount.SUPER_HUB, true, 100);
  console.info('Succeeded in setting super hub disabled');
} catch (err) {
  console.error(`Failed to set super hub disabled. Code is ${err.code}, message is ${err.message}`);
}
```

## restrictions.getDisallowedPolicyForAccount

getDisallowedPolicyForAccount(admin: Want | null, feature: FeatureForAccount, accountId: number): boolean

获取指定用户的某特性状态。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | null | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。当设备存在多个MDM应用时，传入admin查询对应admin设置的策略。传入null时查询整机实际生效的策略。 |
| feature | [FeatureForAccount](js-apis-enterprise-restrictions.md#featureforaccount) | 是 | 指定要查询的用户特性。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。  accountId可以通过[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示参数feature对应的特性被禁用，false表示参数feature对应的特性未被禁用。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ts
import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 参数需根据实际情况进行替换
  let result: boolean = restrictions.getDisallowedPolicyForAccount(wantTemp,
    restrictions.FeatureForAccount.SUPER_HUB, 100);
  console.info(`Succeeded in querying whether the super hub is disabled: ${result}`);
} catch (err) {
  console.error(`Failed to get whether super hub is disabled. Code is ${err.code}, message is ${err.message}`);
}
```

## restrictions.setUserRestriction

setUserRestriction(admin: Want, settingsItem: SettingsForDevice, restricted: boolean): void

限制用户修改指定的设备设置项。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE\_SET\_USER\_RESTRICTION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| settingsItem | [SettingsForDevice](js-apis-enterprise-restrictions.md#settingsfordevice) | 是 | 指定要限制修改的设备设置项。 |
| restricted | boolean | 是 | true表示禁用，false表示不禁用。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ts
import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  restrictions.setUserRestriction(wantTemp, restrictions.SettingsForDevice.SET_APN, true);
  console.info('Succeeded in restricting from setting apn');
} catch (err) {
  console.error(`Failed to restrict from setting apn. Code is ${err.code}, message is ${err.message}`);
}
```

## restrictions.getUserRestricted

getUserRestricted(admin: Want | null, settingsItem: SettingsForDevice): boolean

获取指定设备设置项的禁用状态。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE\_SET\_USER\_RESTRICTION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | null | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。  当设备存在多个MDM应用时，传入Want时查询对应企业设备管理应用设置的策略，传入null时查询实际生效的策略。 |
| settingsItem | [SettingsForDevice](js-apis-enterprise-restrictions.md#settingsfordevice) | 是 | 指定要查询的设备设置项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回指定设备设置项的禁用状态，true表示已禁用，false表示未禁用。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ts
import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let result: boolean = restrictions.getUserRestricted(wantTemp, restrictions.SettingsForDevice.SET_APN);
  console.info(`Succeeded in getting user restricted: ${result}`);
} catch (err) {
  console.error(`Failed to get user restricted. Code is ${err.code}, message is ${err.message}`);
}
```

## restrictions.setUserRestrictionForAccount

setUserRestrictionForAccount(admin: Want, settingsItem: SettingsForAccount, accountId: number, restricted: boolean): void

限制指定用户修改指定的设置项。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE\_SET\_USER\_RESTRICTION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| settingsItem | [SettingsForAccount](js-apis-enterprise-restrictions.md#settingsforaccount) | 是 | 指定要限制修改的用户设置项。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。  accountId可以通过[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。 |
| restricted | boolean | 是 | true表示禁用，false表示不禁用。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ts
import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 参数需根据实际情况进行替换
  restrictions.setUserRestrictionForAccount(wantTemp, restrictions.SettingsForAccount.MODIFY_WALLPAPER, 100, true);
  console.info('Succeeded in restricting from setting modifyWallpaper');
} catch (err) {
  console.error(`Failed to restrict from setting modifyWallpaper. Code is ${err.code}, message is ${err.message}`);
}
```

## restrictions.getUserRestrictedForAccount

getUserRestrictedForAccount(admin: Want | null, settingsItem: SettingsForAccount, accountId: number): boolean

获取指定用户设置项的禁用状态。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE\_SET\_USER\_RESTRICTION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | null | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| settingsItem | [SettingsForAccount](js-apis-enterprise-restrictions.md#settingsforaccount) | 是 | 指定要查询的用户设置项。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。  accountId可以通过[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回指定用户设置项的禁用状态，true表示已禁用，false表示未禁用。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ts
import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 参数需根据实际情况进行替换
  let result: boolean = restrictions.getUserRestrictedForAccount(wantTemp, restrictions.SettingsForAccount.MODIFY_WALLPAPER, 100);
  console.info(`Succeeded in getting user restricted: ${result}`);
} catch (err) {
  console.error(`Failed to get user restricted. Code is ${err.code}, message is ${err.message}`);
}
```

## FeatureForDevice24+

设备特性枚举。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WIFI\_P2P | 0 | Wi-Fi P2P（点对点连接），允许设备在没有接入点的情况下直接相互连接。禁用后，设备无法通过Wi-Fi P2P进行点对点连接，影响文件传输、游戏联机、屏幕共享等需要直接Wi-Fi连接的应用功能。 |
| LOCAL\_INPUT | 2 | 本地输入（包含键盘、鼠标、触控板、触摸屏等）被禁用后，无法通过本地输入进行操作。重启设备可解除禁用。在息屏状态下禁用会导致屏幕无法唤醒，若禁用后屏幕自动息屏，同样会导致无法唤醒屏幕。  **起始版本：** 26.0.0 |
| TRAFFIC\_REDIRECTION | 5 | 网络流量重定向管控策略。禁用后，无法将TCP流量重定向到其它端口，取消禁用之后可恢复使用。当前仅支持PC/2in1设备使用。  **起始版本：** 26.0.0 |
| CORE\_DUMP | 6 | 创建文件转储。禁用后，无法通过任务管理器创建文件转储。当前仅支持PC/2in1设备使用。  **起始版本：** 26.0.0 |
| RS232 | 7 | RS-232串口管控策略。禁用后，无法通过RS-232串口传输数据。当前仅支持PC/2in1设备使用（部分设备不支持RS-232串口）。  **起始版本：** 26.0.0 |
| DISK\_ERASURE | 8 | 磁盘擦除能力。禁用后，"磁盘擦除"入口将被置灰。当前仅支持PC/2in1设备使用。  **起始版本：** 26.0.0 |
| BLUETOOTH | 9 | 设备蓝牙能力。当已经通过[addDisallowedBluetoothDevices](js-apis-enterprise-bluetoothmanager.md#bluetoothmanageradddisallowedbluetoothdevices20)接口或者[addAllowedBluetoothDevices](js-apis-enterprise-bluetoothmanager.md#bluetoothmanageraddallowedbluetoothdevices)接口设置了蓝牙设备禁用名单或者允许名单，再禁用设备蓝牙能力，会优先生效禁用设备蓝牙能力。直到设备蓝牙能力启用后，禁止或允许名单才会生效。  **起始版本：** 26.0.0 |
| MODIFY\_DATE\_TIME | 10 | 设备修改系统时间能力。  **起始版本：** 26.0.0 |
| PRINTER | 11 | 设备打印能力。禁用了设备打印能力时，通过[setDisallowedPolicyForAccount](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicyforaccount)接口开启某用户的打印能力，该用户下的打印能力仍然被禁用。  **起始版本：** 26.0.0 |
| HDC | 12 | 被其他设备通过hdc连接、调试的能力。设置禁用后，其他设备无法通过hdc连接、调试此设备。  **起始版本：** 26.0.0 |
| MICROPHONE | 13 | 设备麦克风能力。  **起始版本：** 26.0.0 |
| FINGERPRINT | 14 | 设备指纹认证能力。当已经通过[setDisallowedPolicyForAccount](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicyforaccount)设置了某用户禁用设备指纹认证能力时，再启用设备指纹认证能力，会报策略冲突。  **起始版本：** 26.0.0 |
| USB | 15 | 设备USB能力。禁用后外接的USB设备无法使用，即在当前设备为HOST模式时，无法外接其他DEVICE设备。  以下五种情况再禁用设备USB能力，会报策略冲突。  1）通过[addAllowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageraddallowedusbdevices)接口添加了USB设备可用名单。  2）通过[setUsbStorageDeviceAccessPolicy](js-apis-enterprise-usbmanager.md#usbmanagersetusbstoragedeviceaccesspolicy)接口设置了USB存储设备访问策略为只读/禁用。  3）通过[addDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageradddisallowedusbdevices14)接口添加了禁止使用的USB设备类型。  4）通过[setDisallowedPolicyForAccount](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicyforaccount)接口禁用了某用户USB存储设备写入能力。  5）禁用USB转串口（[USB\_SERIAL](js-apis-enterprise-restrictions.md#featurefordevice24)）。  **起始版本：** 26.0.0 |
| WIFI | 16 | 设备Wi-Fi能力。  **起始版本：** 26.0.0 |
| TETHERING | 17 | 网络共享能力（设备已有网络共享给其他设备的能力，即共享热点能力）。  **起始版本：** 26.0.0 |
| INACTIVE\_USER\_FREEZE | 18 | 非活跃用户运行能力。禁用后，非UIAbility进程一般不会被冻结，UIAbility申请短时任务、长时任务、延迟任务或能效资源等后台运行任务也不会被冻结。当前仅支持PC/2in1设备使用。企业空间场景下，系统切换到企业空间用户，个人空间用户属于非活跃用户。  **起始版本：** 26.0.0 |
| CAMERA | 19 | 设备相机能力。  **起始版本：** 26.0.0 |
| MTP\_CLIENT | 20 | MTP客户端能力（包含读取和写入），当前仅支持PC/2in1设备使用。MTP（Media Transfer Protocol，媒体传输协议），该协议允许用户在移动设备上线性访问媒体文件。当已经通过[setDisallowedPolicyForAccount](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicyforaccount)设置了某用户禁用MTP客户端写入能力时，再禁用MTP客户端能力，会报策略冲突。  **起始版本：** 26.0.0 |
| MTP\_SERVER | 21 | MTP服务端能力，当前仅支持手机、平板设备使用。  **起始版本：** 26.0.0 |
| SAMBA\_CLIENT | 22 | samba客户端能力，当前仅支持PC/2in1设备使用。samba是在Linux和UNIX系统上实现SMB协议的一个免费软件，由服务器及客户端程序构成。SMB（Server Message Block，信息服务块）是一种在局域网上共享文件和打印机的一种通信协议，它为局域网内的不同计算机之间提供文件及打印机等资源的共享服务。SMB协议是客户机/服务器型协议，客户机通过该协议可以访问服务器上的共享文件系统、打印机及其他资源。  **起始版本：** 26.0.0 |
| SAMBA\_SERVER | 23 | samba服务端能力，当前仅支持PC/2in1设备使用。  **起始版本：** 26.0.0 |
| BACKUP\_AND\_RESTORE | 24 | 备份和恢复能力，禁用后设备的"设置--系统--备份和恢复"、"设置--云空间"置灰，当前仅支持手机、平板使用。如果要完全禁用设备的备份和恢复能力，建议同时调用[applicationManager.addDisallowedRunningBundlesSync](js-apis-enterprise-applicationmanager.md#applicationmanageradddisallowedrunningbundlessync)接口禁止具备备份和恢复能力的应用运行，如备份和恢复、手机助手、云空间应用。  **起始版本：** 26.0.0 |
| MAINTENANCE\_MODE | 25 | 设备维修模式能力。  **起始版本：** 26.0.0 |
| MMS | 26 | multimedia messaging service，设备接收、发送彩信的能力，当前仅支持手机、平板设备使用。  **起始版本：** 26.0.0 |
| SMS | 27 | short messaging service，设备接收、发送短信的能力，当前仅支持手机、平板设备使用。  **起始版本：** 26.0.0 |
| MOBILE\_DATA | 28 | 蜂窝数据能力，当前仅支持手机、平板设备使用。  **起始版本：** 26.0.0 |
| AIRPLANE\_MODE | 29 | 飞行模式能力，当前仅支持手机、平板设备使用。  **起始版本：** 26.0.0 |
| VPN | 30 | Virtual Private Network（虚拟专用网络），VPN能力。  **起始版本：** 26.0.0 |
| NOTIFICATION | 31 | 设备通知能力。禁用后，由系统应用和第三方应用发出的通知将不会显示，而系统服务通知能力不受影响。当此设备已经通过[addAllowedNotificationBundles](js-apis-enterprise-applicationmanager.md#applicationmanageraddallowednotificationbundles)设置了应用通知允许名单之后，再禁用设备通知能力，会抛出错误码9200010。  **起始版本：** 26.0.0 |
| NFC | 32 | Near Field Communication（近距离无线通信），NFC能力，当前仅支持手机、平板设备使用。  **起始版本：** 26.0.0 |
| PRIVATE\_SPACE | 33 | 创建隐私空间能力，当前仅支持手机、平板使用。对已创建的隐私空间无效。  **起始版本：** 26.0.0 |
| TELEPHONE\_CALL | 34 | 设备通话能力，禁用后电话无法呼入和呼出。当前仅支持手机、平板设备使用。  **起始版本：** 26.0.0 |
| APP\_CLONE | 35 | [应用分身能力](../harmonyos-guides/app-clone.md)，禁用后无法创建应用分身。对已创建的应用分身无效。  **起始版本：** 26.0.0 |
| EXTERNAL\_STORAGE\_CARD | 36 | 外置存储能力，禁用后设备无法使用外置存储，并且当前已连接的外置存储会被卸载。如果外置存储卸载时有文件正在被使用，可能会导致卸载失败，返回9200013错误码。  外置存储禁用后重新启用，需要手动重新连接外置存储。  **起始版本：** 26.0.0 |
| RANDOM\_MAC | 37 | Wi-Fi连接时使用随机MAC能力，设置禁用后，连接Wi-Fi仅能使用设备物理MAC。  **起始版本：** 26.0.0 |
| UNMUTE\_DEVICE | 38 | 设备媒体播放声音能力，设置禁用后，设备媒体播放将静音，[蜂窝通话](../harmonyos-guides/audio-call-overview.md)能力不受影响。  **起始版本：** 26.0.0 |
| HDC\_REMOTE | 39 | 设备通过hdc调试其他设备的能力，当前仅支持PC/2in1设备设置。设置禁用后，无法通过hdc调试手机、平板、PC、智能手表等设备。  **起始版本：** 26.0.0 |
| VIRTUAL\_SERVICE | 40 | 设备虚拟化服务能力，即利用硬件资源的冗余，以虚拟化方式运行其他平台（如Linux、Windows）的能力。设置禁用设备虚拟化服务能力时，建议同时卸载与虚拟化服务相关的应用，并禁止其再次安装。  **起始版本：** 26.0.0 |
| USB\_SERIAL | 41 | 设备USB转串口能力。禁用后外接的USB转串口设备无法使用。以下两种情况再禁用设备USB转串口能力，会报策略冲突。  1）通过[addAllowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageraddallowedusbdevices)接口添加了USB设备可用名单。  2）禁用设备USB能力（[USB](js-apis-enterprise-restrictions.md#featurefordevice24)）。  **起始版本：** 26.0.0 |
| SCREEN\_SHOT | 42 | 截屏能力，禁用后无法进行截屏操作。  **起始版本：** 26.0.0 |
| SCREEN\_RECORD | 43 | 录屏能力，禁用后无法进行录屏操作。  **起始版本：** 26.0.0 |
| DISK\_RECOVERY\_KEY | 44 | 恢复[密钥导出](../harmonyos-guides/huks-export-key-arkts.md)能力，当前仅支持PC/2in1设备使用。  **起始版本：** 26.0.0 |
| NEAR\_LINK | 45 | 星闪（NearLink）能力。  **起始版本：** 26.0.0 |
| DEVELOPER\_MODE | 46 | 开发者模式，禁用后设备重启生效。  **起始版本：** 26.0.0 |
| RESET\_FACTORY | 47 | 恢复出厂设置能力。  **起始版本：** 26.0.0 |
| REMOTE\_DESK | 48 | 远程桌面能力。  **起始版本：** 26.0.0 |
| REMOTE\_DIAGNOSIS | 49 | 远程诊断能力。  **起始版本：** 26.0.0 |
| OTA\_UPDATE | 50 | 公网系统升级能力。  **起始版本：** 26.0.0 |

## FeatureForAccount

可为指定用户设置禁用/启用的特性的枚举。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MULTI\_WINDOW | 0 | 系统多窗口。当前仅支持手机、平板设备使用，禁用后无法使用系统多窗口功能（分屏、一键分屏、智慧多窗、悬浮窗口）。若系统多窗口功能已开启，本次使用不受影响，但关闭后将无法再次使用。 |
| DISTRIBUTED\_TRANSMISSION | 1 | [分布式管理服务](../harmonyos-guides/distributedservice-kit-intro.md#运作机制)。禁用后无法使用设备分布式管理服务中的发现、认证、查询、监听等功能。 |
| SUPER\_HUB | 2 | 中转站。当前仅支持手机、平板设备使用，禁用后无法使用中转站功能。若中转站已开启，本次使用不受影响，但关闭后将无法再次使用。 |
| FINGERPRINT | 3 | 设备指纹认证能力，当前仅支持PC/2in1设备使用。使用时有以下规则：  1. 禁用设备指纹认证能力（[FeatureForDevice.FINGERPRINT](js-apis-enterprise-restrictions.md#featurefordevice24)）后，再禁用某用户的设备指纹认证能力，会报策略冲突。  2. 禁用/启用指定用户的设备指纹认证能力后，再禁用设备指纹认证能力（[FeatureForDevice.FINGERPRINT](js-apis-enterprise-restrictions.md#featurefordevice24)）时，后者会覆盖前者的策略。此后再启用设备指纹认证能力（[FeatureForDevice.FINGERPRINT](js-apis-enterprise-restrictions.md#featurefordevice24)），则所有用户都允许使用设备指纹认证能力。 |
| PRINT | 4 | 设备打印能力。如果禁用了指定用户的设备打印能力，再启用设备打印能力（[FeatureForDevice.PRINTER](js-apis-enterprise-restrictions.md#featurefordevice24)），该用户下的设备打印能力仍然被禁用。 |
| MTP\_CLIENT | 5 | MTP客户端能力（仅包含写入），当前仅支持PC/2in1设备使用。MTP（Media Transfer Protocol，媒体传输协议），该协议允许用户在移动设备上线性访问媒体文件。当已禁用设备MTP客户端能力（[FeatureForDevice.MTP\_CLIENT](js-apis-enterprise-restrictions.md#featurefordevice24)）时，再禁用某用户MTP客户端写入能力，会报策略冲突。 |
| USB\_STORAGE\_DEVICE\_WRITE | 6 | USB存储设备写入能力，当前仅支持PC/2in1企业设备使用。  以下三种情况再禁用某用户USB存储设备写入能力，会报策略冲突。  1）已禁用设备USB能力（[FeatureForDevice.USB](js-apis-enterprise-restrictions.md#featurefordevice24)）。  2）通过[setUsbStorageDeviceAccessPolicy](js-apis-enterprise-usbmanager.md#usbmanagersetusbstoragedeviceaccesspolicy)接口设置了USB存储设备访问策略为只读/禁用。  3）通过[addDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageradddisallowedusbdevices14)接口添加了存储类型的USB设备禁用。 |
| DISK\_RECOVERY\_KEY | 7 | 恢复[密钥导出](../harmonyos-guides/huks-export-key-arkts.md)能力，当前仅支持PC/2in1设备使用。 |
| SUDO | 8 | superuser do，表示以超级用户执行，当前仅支持PC/2in1设备使用。禁用后企业空间或个人空间不能以超级用户执行。 |
| DISTRIBUTED\_TRANSMISSION\_OUTGOING | 9 | 设备间分布式单向传输数据的能力（仅包含向其他设备传输数据）。当已禁用分布式管理服务（[DISTRIBUTED\_TRANSMISSION](js-apis-enterprise-restrictions.md#featureforaccount)），再禁用设备间分布式单向传输数据的能力，会报策略冲突。 |
| OPEN\_FILE\_BOOST | 10 | [文件打开加速](preview-arkts-openfileboost-api.md)，为应用提供文件打开加速状态感知能力。应用可以通过接入对应API，感知文件的加速状态，进而应用可以实现对已加速文件给出独特的UI（user interface）标识等功能，优化用户文件打开体验，当前仅支持PC/2in1设备使用。 |

## SettingsForDevice

设备设置项枚举。

**起始版本：** 26.0.0

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SET\_APN | 0 | APN设置，当前仅支持手机、平板使用。 |
| POWER\_LONG\_PRESS | 1 | 长按电源键打开电源菜单，当前仅支持手机、平板使用。 |
| SET\_ETHERNET\_IP | 2 | 修改以太网IP地址，当前仅支持PC/2in1设备使用。 |
| SET\_DEVICE\_NAME | 3 | 修改设备名称，当前仅支持PC/2in1设备、手机、平板使用。禁用后，PC/2in1设备的设置中以下设备名称无法修改，包括关于本机、蓝牙、多设备协同->星闪。手机、平板设备设置中的关于本机、蓝牙、个人热点的设备名称无法修改。 |
| SET\_BIOMETRICS\_AND\_SCREEN\_LOCK | 4 | 修改锁屏密码，当前仅支持PC/2in1设备、手机、平板使用。 |

## SettingsForAccount

用户设置项枚举。

**起始版本：** 26.0.0

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MODIFY\_WALLPAPER | 0 | 修改壁纸，包含锁屏壁纸和桌面壁纸。 |
