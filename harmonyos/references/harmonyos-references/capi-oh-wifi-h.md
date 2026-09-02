---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-wifi-h
title: oh_wifi.h
breadcrumb: API参考 > 系统 > 网络 > Connectivity Kit（短距通信服务） > C API > 头文件 > oh_wifi.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ca897efdbe41bfa154bcf38d33f06d896146082539893b1b7052a8e5a48af633
---

## 概述

定义查询WIFI开关状态、获取设备MAC地址和获取WIFI连接信息的接口。

**引用文件：** <ConnectivityKit/wifi/oh\_wifi.h>

**库：** libwifi\_ndk.so

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 13

**相关模块：** [Wifi](capi-wifi.md)

## 汇总

### 宏定义

| 名称 | 描述 |
| --- | --- |
| WIFI\_MAX\_SSID\_LEN 33 | [OH\_WifiLinkedInfo](capi-oh-wifi-h.md#oh_wifilinkedinfo) 成员变量ssid数组的长度（32 + \0）。  **起始版本：** 24 |
| WIFI\_MAC\_LEN 18 | [OH\_WifiLinkedInfo](capi-oh-wifi-h.md#oh_wifilinkedinfo) 成员变量macAddress数组和bssid数组的长度（17 + \0）。  **起始版本：** 24 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Wifi\_ResultCode](capi-oh-wifi-h.md#wifi_resultcode) | Wifi\_ResultCode | 定义WIFI接口返回值的错误码。 |
| [OH\_WifiConnState](capi-oh-wifi-h.md#oh_wificonnstate) | OH\_WifiConnState | 定义WIFI连接状态。 |
| [OH\_WifiChannelWidth](capi-oh-wifi-h.md#oh_wifichannelwidth) | OH\_WifiChannelWidth | 定义当前连接热点的信道带宽。 |
| [OH\_WifiStandard](capi-oh-wifi-h.md#oh_wifistandard) | OH\_WifiStandard | 当前连接热点的WIFI标准。 |
| [OH\_WifiCategory](capi-oh-wifi-h.md#oh_wificategory) | OH\_WifiCategory | 热点支持的最高WIFI级别。 |
| [OH\_WifiLinkType](capi-oh-wifi-h.md#oh_wifilinktype) | OH\_WifiLinkType | WIFI7连接类型。 |

### 结构体

| 名称 | 描述 |
| --- | --- |
| [OH\_WifiLinkedInfo](capi-oh-wifi-h.md#oh_wifilinkedinfo) | 提供WLAN连接的相关信息。可以获取当前设备已连接的WIFI热点的信息。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [Wifi\_ResultCode OH\_Wifi\_IsWifiEnabled(bool \*enabled)](capi-oh-wifi-h.md#oh_wifi_iswifienabled) | 查询WIFI开关是否开启。 |
| [Wifi\_ResultCode OH\_Wifi\_GetDeviceMacAddress(char \*macAddr, unsigned int \*macAddrLen)](capi-oh-wifi-h.md#oh_wifi_getdevicemacaddress) | 该接口用于获取设备真实MAC地址。 |
| [Wifi\_ResultCode OH\_Wifi\_GetLinkedInfo(OH\_WifiLinkedInfo \*info)](capi-oh-wifi-h.md#oh_wifi_getlinkedinfo) | 该接口用于获取WIFI连接信息。 |

## 枚举类型说明

### Wifi\_ResultCode

```c
enum Wifi_ResultCode
```

**描述**

定义WIFI接口返回值的错误码。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| WIFI\_SUCCESS = 0 | 操作成功。 |
| WIFI\_PERMISSION\_DENIED = 201 | 权限校验失败。 |
| WIFI\_INVALID\_PARAM = 401 | 参数错误。  可能原因：1.输入参数为空指针；2.参数数值超出定义范围。 |
| WIFI\_NOT\_SUPPORTED = 801 | 该功能不支持。由于设备能力有限，无法调用该函数。 |
| WIFI\_OPERATION\_FAILED = 2501000 | 操作失败。  可能原因：服务内部执行失败。 |
| WIFI\_STA\_DISABLED = 2501001 | STA服务未拉起。  可能原因：WIFI未打开。  **起始版本：** 21 |

### OH\_WifiConnState

```c
enum OH_WifiConnState
```

**描述**

WLAN连接状态。

**起始版本：** 24

| 枚举项 | 描述 |
| --- | --- |
| OH\_WIFI\_CONN\_SCANNING = 0 | 设备正在搜索可用的热点。 |
| OH\_WIFI\_CONN\_CONNECTING = 1 | 正在建立WLAN连接。 |
| OH\_WIFI\_CONN\_AUTHENTICATING = 2 | WLAN连接正在认证中。 |
| OH\_WIFI\_CONN\_OBTAINING\_IPADDR = 3 | 正在获取WLAN连接的IP地址。 |
| OH\_WIFI\_CONN\_CONNECTED = 4 | WLAN连接已建立。 |
| OH\_WIFI\_CONN\_DISCONNECTING = 5 | WLAN连接正在断开。 |
| OH\_WIFI\_CONN\_DISCONNECTED = 6 | WLAN连接已断开。 |
| OH\_WIFI\_CONN\_SPECIAL\_CONNECT = 7 | WLAN连接处于特殊状态。 |
| OH\_WIFI\_CONN\_UNKNOWN = 8 | WLAN连接建立失败。 |

### OH\_WifiChannelWidth

```c
enum OH_WifiChannelWidth
```

**描述**

WLAN信道带宽。

**起始版本：** 24

| 枚举项 | 描述 |
| --- | --- |
| OH\_WIFI\_WIDTH\_20MHZ = 0 | 20MHz信道带宽。 |
| OH\_WIFI\_WIDTH\_40MHZ = 1 | 40MHz信道带宽。 |
| OH\_WIFI\_WIDTH\_80MHZ = 2 | 80MHz信道带宽。 |
| OH\_WIFI\_WIDTH\_160MHZ = 3 | 160MHz信道带宽。 |
| OH\_WIFI\_WIDTH\_80MHZ\_PLUS = 4 | 双80MHz信道带宽。 |
| OH\_WIFI\_WIDTH\_INVALID = 5 | 无效的信道带宽。 |

### OH\_WifiStandard

```c
enum OH_WifiStandard
```

**描述**

WIFI标准枚举。

**起始版本：** 24

| 枚举项 | 描述 |
| --- | --- |
| OH\_WIFI\_STANDARD\_UNDEFINED = 0 | 无效的WIFI标准。 |
| OH\_WIFI\_STANDARD\_11A = 1 | 802.11a WIFI标准。 |
| OH\_WIFI\_STANDARD\_11B = 2 | 802.11b WIFI标准。 |
| OH\_WIFI\_STANDARD\_11G = 3 | 802.11g WIFI标准。 |
| OH\_WIFI\_STANDARD\_11N = 4 | 802.11n WIFI标准。 |
| OH\_WIFI\_STANDARD\_11AC = 5 | 802.11ac WIFI标准。 |
| OH\_WIFI\_STANDARD\_11AX = 6 | 802.11ax WIFI标准。 |
| OH\_WIFI\_STANDARD\_11AD = 7 | 802.11ad WIFI标准。 |

### OH\_WifiCategory

```c
enum OH_WifiCategory
```

**描述**

WIFI类别枚举。

**起始版本：** 24

| 枚举项 | 描述 |
| --- | --- |
| OH\_WIFI\_CATEGORY\_DEFAULT = 1 | 默认类别。 |
| OH\_WIFI\_CATEGORY\_WIFI6 = 2 | WIFI6类别。 |
| OH\_WIFI\_CATEGORY\_WIFI6\_PLUS = 3 | WIFI6+类别。 |
| OH\_WIFI\_CATEGORY\_WIFI7 = 4 | WIFI7类别。 |
| OH\_WIFI\_CATEGORY\_WIFI7\_PLUS = 5 | WIFI7+类别。 |

### OH\_WifiLinkType

```c
enum OH_WifiLinkType
```

**描述**

WIFI7连接类型。

**起始版本：** 24

| 枚举项 | 描述 |
| --- | --- |
| OH\_WIFI\_LINK\_DISCONNECT = -1 | 未连接。 |
| OH\_WIFI\_LINK\_DEFAULT\_LINK = 0 | 默认连接。 |
| OH\_WIFI\_LINK\_WIFI7\_SINGLE\_LINK = 1 | WIFI7单链连接。 |
| OH\_WIFI\_LINK\_WIFI7\_MLSR = 2 | WIFI7 MLSR（Multi-Link Single Radio，多链路单射频）。 |
| OH\_WIFI\_LINK\_WIFI7\_EMLSR = 3 | WIFI7 EMLSR（Enhanced Multi-Link Single Radio，增强型多链路单射频）。 |
| OH\_WIFI\_LINK\_WIFI7\_STR = 4 | WIFI7 STR（Simultaneous Transmit and Receive，同时发送与接收）。 |
| OH\_WIFI\_LINK\_WIFI7\_LEGACY = 5 | WIFI7 传统模式。 |

## 结构体说明

### OH\_WifiLinkedInfo

```c
struct OH_WifiLinkedInfo
```

**描述**

提供WLAN连接的相关信息。可以获取当前设备已连接的WIFI热点的信息。

**起始版本：** 24

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| ssid | char[] | 否 | 否 | 热点的SSID（Service Set Identifier，服务集标识符），用于获取当前设备已连接的WIFI热点的公开名称（即无线网络的名称），编码格式为UTF-8。  长度 WIFI\_MAX\_SSID\_LEN = 33。 |
| bssid | char[] | 否 | 否 | 热点的BSSID（Basic Service Set Identifier，基本服务集标识符）即无线网络的MAC地址。如果应用已请求 ohos.permission.GET\_WIFI\_PEERS\_MAC 权限，则返回的bssid为真实BSSID地址；否则为随机设备地址。  格式："AA:BB:CC:DD:EE:FF"  最大长度 WIFI\_MAC\_LEN = 18。 |
| rssi | int32\_t | 否 | 否 | 热点的信号强度(dBm)。RSSI（Received Signal Strength Indicator，接收信号强度指示）。 |
| band | int32\_t | 否 | 否 | WLAN接入点的频段，1表示2.4GHz；2表示5GHz。 |
| linkSpeed | int32\_t | 否 | 否 | WLAN接入点的上行速度单位Mbps。 |
| rxLinkSpeed | int32\_t | 否 | 否 | WLAN接入点的下行速度单位Mbps。 |
| maxSupportedTxLinkSpeed | int32\_t | 否 | 否 | 当前支持的最大上行速率单位Mbps。 |
| maxSupportedRxLinkSpeed | int32\_t | 否 | 否 | 当前支持的最大下行速率单位Mbps。 |
| frequency | int32\_t | 否 | 否 | WLAN接入点的频率，单位MHz。 |
| isHidden | bool | 否 | 否 | WLAN接入点是否是隐藏网络，true表示是隐藏网络，false表示不是隐藏网络。 |
| isRestricted | bool | 否 | 否 | WLAN接入点是否限制数据量，true表示限制，false表示不限制。 |
| macType | int32\_t | 否 | 否 | MAC地址类型。0 - 随机MAC地址，1 - 设备MAC地址。 |
| macAddress | char[] | 否 | 否 | 设备的MAC地址。当macType为1时需要申请ohos.permission.GET\_WIFI\_LOCAL\_MAC权限。  格式："AA:BB:CC:DD:EE:FF"  长度 WIFI\_MAC\_LEN = 18。 |
| ipAddress | uint32\_t | 否 | 否 | WLAN连接的IP地址。 |
| connState | [OH\_WifiConnState](capi-oh-wifi-h.md#oh_wificonnstate) | 否 | 否 | WLAN连接状态。详情见OH\_WifiConnState。 |
| channelWidth | [OH\_WifiChannelWidth](capi-oh-wifi-h.md#oh_wifichannelwidth) | 否 | 否 | 当前连接热点的信道带宽。详情见OH\_WifiChannelWidth。 |
| wifiStandard | [OH\_WifiStandard](capi-oh-wifi-h.md#oh_wifistandard) | 否 | 否 | 当前连接热点的WIFI标准。详情见OH\_WifiStandard。 |
| supportedWifiCategory | [OH\_WifiCategory](capi-oh-wifi-h.md#oh_wificategory) | 否 | 否 | 热点支持的最高WIFI级别。详情见OH\_WifiCategory。 |
| isHiLinkNetwork | bool | 否 | 否 | 热点是否支持hilink，true表示支持，false表示不支持。 |
| wifiLinkType | [OH\_WifiLinkType](capi-oh-wifi-h.md#oh_wifilinktype) | 否 | 是 | WIFI7连接类型。详情见OH\_WifiLinkType。 |

## 函数说明

### OH\_Wifi\_IsWifiEnabled()

```c
Wifi_ResultCode OH_Wifi_IsWifiEnabled(bool *enabled)
```

**描述**

查询WIFI开关是否开启。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| bool \*enabled | - bool类型的指针，用于接收WIFI开关状态值。  等于true表示WIFI开关开启，false表示WIFI开关关闭。  需要传入非空指针，否则会返回错误。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Wifi\_ResultCode](capi-oh-wifi-h.md#wifi_resultcode) | 返回操作结果，详细定义参见[Wifi\_ResultCode](capi-oh-wifi-h.md#wifi_resultcode)。  [WIFI\_SUCCESS](capi-oh-wifi-h.md#wifi_resultcode)查询WIFI开关状态成功。  [WIFI\_INVALID\_PARAM](capi-oh-wifi-h.md#wifi_resultcode)入参为空指针。  [WIFI\_OPERATION\_FAILED](capi-oh-wifi-h.md#wifi_resultcode) 服务内部执行错误。 |

### OH\_Wifi\_GetDeviceMacAddress()

```c
Wifi_ResultCode OH_Wifi_GetDeviceMacAddress(char *macAddr, unsigned int *macAddrLen)
```

**描述**

该接口用于获取设备真实MAC地址。

**需要权限：** ohos.permission.GET\_WIFI\_LOCAL\_MAC 和 ohos.permission.GET\_WIFI\_INFO

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char \*macAddr | 设备MAC地址的字符数组，以'\0'结尾。 |
| unsigned int \*macAddrLen | 为macAddr字符数组分配的内存大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Wifi\_ResultCode](capi-oh-wifi-h.md#wifi_resultcode) | 返回操作结果，详细定义参见[Wifi\_ResultCode](capi-oh-wifi-h.md#wifi_resultcode)。  [WIFI\_SUCCESS](capi-oh-wifi-h.md#wifi_resultcode) 成功获取设备MAC地址。  [WIFI\_PERMISSION\_DENIED](capi-oh-wifi-h.md#wifi_resultcode) 权限拒绝。  [WIFI\_NOT\_SUPPORTED](capi-oh-wifi-h.md#wifi_resultcode) 不支持该能力。  [WIFI\_INVALID\_PARAM](capi-oh-wifi-h.md#wifi_resultcode) 输入参数macAddr是空指针。  [WIFI\_OPERATION\_FAILED](capi-oh-wifi-h.md#wifi_resultcode) 内部执行失败。  [WIFI\_STA\_DISABLED](capi-oh-wifi-h.md#wifi_resultcode) WIFI STA模式未启用。 |

### OH\_Wifi\_GetLinkedInfo()

```c
Wifi_ResultCode OH_Wifi_GetLinkedInfo(OH_WifiLinkedInfo *info)
```

**描述**

该接口用于获取WIFI连接信息。

**说明** 

* 当macType是1（设备MAC地址），获取macAddress还需申请ohos.permission.GET\_WIFI\_LOCAL\_MAC权限（API version 8-15仅面向系统应用开放。从API version 16开始，在PC/2in1设备上面向普通应用开放，在其余设备上仍仅面向系统应用开放），无该权限时，macAddress返回为空。
* 如果应用申请了ohos.permission.GET\_WIFI\_PEERS\_MAC权限，则返回结果中的bssid为真实bssid地址，否则为随机设备地址。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_WifiLinkedInfo](capi-oh-wifi-h.md#oh_wifilinkedinfo) \*info | OH\_WifiLinkedInfo类型的结构体。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Wifi\_ResultCode](capi-oh-wifi-h.md#wifi_resultcode) | 返回操作结果，详细定义参见[Wifi\_ResultCode](capi-oh-wifi-h.md#wifi_resultcode)。  [WIFI\_SUCCESS](capi-oh-wifi-h.md#wifi_resultcode) 成功获取WIFI连接信息。  [WIFI\_PERMISSION\_DENIED](capi-oh-wifi-h.md#wifi_resultcode) 权限拒绝。  [WIFI\_NOT\_SUPPORTED](capi-oh-wifi-h.md#wifi_resultcode) 不支持获取连接信息。  [WIFI\_INVALID\_PARAM](capi-oh-wifi-h.md#wifi_resultcode) 输入参数info是空指针。  [WIFI\_OPERATION\_FAILED](capi-oh-wifi-h.md#wifi_resultcode) 内部执行失败。  [WIFI\_STA\_DISABLED](capi-oh-wifi-h.md#wifi_resultcode) WIFI STA模式未启用。 |
