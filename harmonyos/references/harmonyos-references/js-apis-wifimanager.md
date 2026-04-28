---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager
title: @ohos.wifiManager (WLAN)
breadcrumb: API参考 > 系统 > 网络 > Connectivity Kit（短距通信服务） > ArkTS API > @ohos.wifiManager (WLAN)
category: harmonyos-references
scraped_at: 2026-04-28T08:08:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f80d2c6f7fe96f7c64c3207bb3b1360019d0f2b92914c7851edcd422f5bf5610
---

该模块主要提供WLAN基础功能（无线接入、无线加密、无线漫游等）、P2P（peer-to-peer）服务的基础功能和WLAN消息通知的相应服务，让应用可以通过WLAN和其他设备互联互通。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { wifiManager } from '@kit.ConnectivityKit';
```

## wifiManager.isWifiActive

PhonePC/2in1TabletTVWearable

isWifiActive(): boolean

查询WLAN开关是否已使能。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true:已使能， false:未使能。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. try {
4. let isWifiActive = wifiManager.isWifiActive();
5. console.info("isWifiActive:" + isWifiActive);
6. }catch(error){
7. console.error("failed:" + JSON.stringify(error));
8. }
```

## wifiManager.enableWifi15+

PhonePC/2in1TabletTVWearable

enableWifi(): void

启动WLAN。

**需要权限：** ohos.permission.SET\_WIFI\_INFO 和 (ohos.permission.MANAGE\_WIFI\_CONNECTION 仅系统应用可用 或 ohos.permission.MANAGE\_ENTERPRISE\_WIFI\_CONNECTION 仅企业应用可用)

**系统能力：** SystemCapability.Communication.WiFi.STA

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |
| 2501003 | Operation failed because the service is being closed. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. try {
4. wifiManager.enableWifi();
5. }catch(error){
6. console.error("failed:" + JSON.stringify(error));
7. }
```

## wifiManager.disableWifi20+

PhonePC/2in1TabletTVWearable

disableWifi(): void

关闭WLAN。

**需要权限：** ohos.permission.SET\_WIFI\_INFO 和 (ohos.permission.MANAGE\_WIFI\_CONNECTION 仅系统应用可用 或 ohos.permission.MANAGE\_ENTERPRISE\_WIFI\_CONNECTION 仅企业应用可用)

**系统能力：** SystemCapability.Communication.WiFi.STA

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |
| 2501004 | Operation failed because the service is being opened. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. try {
4. wifiManager.disableWifi();
5. }catch(error){
6. console.error(`disableWifi failed. ${error.message}`);
7. }
```

## wifiManager.scan(deprecated)

PhonePC/2in1TabletTVWearable

scan(): void

启动WLAN扫描，使用前先使能WLAN。

说明

从 API version 9开始支持，从API version 10开始废弃。建议使用[wifiManager.startScan](js-apis-wifimanager.md#wifimanagerstartscan21)代替。

**需要权限：** ohos.permission.SET\_WIFI\_INFO、ohos.permission.LOCATION 和 ohos.permission.APPROXIMATELY\_LOCATION

**系统能力：** SystemCapability.Communication.WiFi.STA

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. try {
4. wifiManager.scan();
5. }catch(error){
6. console.error("failed:" + JSON.stringify(error));
7. }
```

## wifiManager.startScan21+

PhonePC/2in1TabletTVWearable

startScan(): void

启动WLAN扫描。

* 应用程序在前台运行时，两分钟内最多可扫描四次。
* 在后台运行时，三十分钟内最多可扫描一次。
* 通过[on('wifiScanStateChange')](js-apis-wifimanager.md#wifimanageronwifiscanstatechange)订阅扫描状态变更事件，监听扫描完成通知。

**需要权限：** ohos.permission.SET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. try {
4. wifiManager.startScan();
5. }catch(error){
6. console.error("failed:" + JSON.stringify(error));
7. }
```

## wifiManager.getScanResults(deprecated)

PhonePC/2in1TabletTVWearable

getScanResults(): Promise<Array<WifiScanInfo>>

获取扫描结果，使用Promise异步回调。

* 返回一个Promise对象，解析后得到一个包含多个WifiScanInfo对象的数组，每个对象表示一个WLAN网络的扫描信息。

说明

从 API version 9开始支持，从API version 10开始废弃。建议使用[wifiManager.getScanInfoList](js-apis-wifimanager.md#wifimanagergetscaninfolist10)代替。

**需要权限：** ohos.permission.GET\_WIFI\_INFO 和 (ohos.permission.GET\_WIFI\_PEERS\_MAC 或(ohos.permission.LOCATION 和 ohos.permission.APPROXIMATELY\_LOCATION))

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise< Array<[WifiScanInfo](js-apis-wifimanager.md#wifiscaninfo)> > | Promise对象。返回扫描到的热点列表。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

## wifiManager.getScanResults(deprecated)

PhonePC/2in1TabletTVWearable

getScanResults(callback: AsyncCallback<Array<WifiScanInfo>>): void

获取扫描结果，使用callback异步回调。

* 通过回调函数返回一个包含多个WifiScanInfo对象的数组，每个对象表示一个WLAN网络的扫描信息。

说明

从 API version 9开始支持，从API version 10开始废弃。建议使用[wifiManager.getScanInfoList](js-apis-wifimanager.md#wifimanagergetscaninfolist10)代替。

**需要权限：** ohos.permission.GET\_WIFI\_INFO 和 (ohos.permission.GET\_WIFI\_PEERS\_MAC 或 (ohos.permission.LOCATION 和 ohos.permission.APPROXIMATELY\_LOCATION))

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback< Array<[WifiScanInfo](js-apis-wifimanager.md#wifiscaninfo)>> | 是 | 回调函数。当成功时，err为0，data为扫描到的热点；否则err为非0值，data为空。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. wifiManager.getScanResults((err, result) => {
4. if (err) {
5. console.error("get scan info error");
6. return;
7. }

9. let len = result.length;
10. console.info("wifi received scan info: " + len);
11. for (let i = 0; i < len; ++i) {
12. console.info("ssid: " + result[i].ssid);
13. console.info("bssid: " + result[i].bssid);
14. console.info("capabilities: " + result[i].capabilities);
15. console.info("securityType: " + result[i].securityType);
16. console.info("rssi: " + result[i].rssi);
17. console.info("band: " + result[i].band);
18. console.info("frequency: " + result[i].frequency);
19. console.info("channelWidth: " + result[i].channelWidth);
20. console.info("timestamp: " + result[i].timestamp);
21. }
22. });

24. wifiManager.getScanResults().then(result => {
25. let len = result.length;
26. console.info("wifi received scan info: " + len);
27. for (let i = 0; i < len; ++i) {
28. console.info("ssid: " + result[i].ssid);
29. console.info("bssid: " + result[i].bssid);
30. console.info("capabilities: " + result[i].capabilities);
31. console.info("securityType: " + result[i].securityType);
32. console.info("rssi: " + result[i].rssi);
33. console.info("band: " + result[i].band);
34. console.info("frequency: " + result[i].frequency);
35. console.info("channelWidth: " + result[i].channelWidth);
36. console.info("timestamp: " + result[i].timestamp);
37. }
38. }).catch((err:number) => {
39. console.error("failed:" + JSON.stringify(err));
40. });
```

## wifiManager.getScanResultsSync(deprecated)

PhonePC/2in1TabletTVWearable

getScanResultsSync(): Array<[WifiScanInfo](js-apis-wifimanager.md#wifiscaninfo)>

获取扫描结果，使用同步方式返回一个包含多个WifiScanInfo对象的数组，每个对象表示一个WLAN网络的扫描信息。

说明

从 API version 9开始支持，从API version 10开始废弃。建议使用[wifiManager.getScanInfoList](js-apis-wifimanager.md#wifimanagergetscaninfolist10)代替。

**需要权限：** ohos.permission.GET\_WIFI\_INFO 和 (ohos.permission.GET\_WIFI\_PEERS\_MAC 或 (ohos.permission.LOCATION 和 ohos.permission.APPROXIMATELY\_LOCATION))

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[WifiScanInfo](js-apis-wifimanager.md#wifiscaninfo)> | 扫描结果数组。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. try {
4. let scanInfoList = wifiManager.getScanResultsSync();
5. console.info("scanInfoList:" + JSON.stringify(scanInfoList));
6. let len = scanInfoList.length;
7. console.info("wifi received scan info: " + len);
8. if(len > 0){
9. for (let i = 0; i < len; ++i) {
10. console.info("ssid: " + scanInfoList[i].ssid);
11. console.info("bssid: " + scanInfoList[i].bssid);
12. console.info("capabilities: " + scanInfoList[i].capabilities);
13. console.info("securityType: " + scanInfoList[i].securityType);
14. console.info("rssi: " + scanInfoList[i].rssi);
15. console.info("band: " + scanInfoList[i].band);
16. console.info("frequency: " + scanInfoList[i].frequency);
17. console.info("channelWidth: " + scanInfoList[i].channelWidth);
18. console.info("timestamp: " + scanInfoList[i].timestamp);
19. }
20. }
21. }catch(error){
22. console.error("failed:" + JSON.stringify(error));
23. }
```

## wifiManager.getScanInfoList10+

PhonePC/2in1TabletTVWearable

getScanInfoList(): Array<WifiScanInfo>

获取包含当前时间点前30s内的缓存扫描结果。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[WifiScanInfo](js-apis-wifimanager.md#wifiscaninfo)> | 返回扫描到的热点列表。如果应用申请了ohos.permission.GET\_WIFI\_PEERS\_MAC权限，则返回结果中的bssid为真实设备地址，否则为随机设备地址。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. try {
4. let scanInfoList = wifiManager.getScanInfoList();
5. console.info("scanInfoList:" + JSON.stringify(scanInfoList));
6. let len = scanInfoList.length;
7. console.info("wifi received scan info: " + len);
8. if(len > 0){
9. for (let i = 0; i < len; ++i) {
10. console.info("ssid: " + scanInfoList[i].ssid);
11. console.info("bssid: " + scanInfoList[i].bssid);
12. console.info("capabilities: " + scanInfoList[i].capabilities);
13. console.info("securityType: " + scanInfoList[i].securityType);
14. console.info("rssi: " + scanInfoList[i].rssi);
15. console.info("band: " + scanInfoList[i].band);
16. console.info("frequency: " + scanInfoList[i].frequency);
17. console.info("channelWidth: " + scanInfoList[i].channelWidth);
18. console.info("timestamp: " + scanInfoList[i].timestamp);
19. console.info("supportedWifiCategory: " + scanInfoList[i].supportedWifiCategory);
20. console.info("isHiLinkNetwork: " + scanInfoList[i].isHiLinkNetwork);
21. }
22. }
23. }catch(error){
24. console.error("failed:" + JSON.stringify(error));
25. }
```

## WifiScanInfo

PhonePC/2in1TabletTVWearable

WLAN热点信息。

**系统能力：** SystemCapability.Communication.WiFi.STA

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| ssid | string | 否 | 否 | 热点的SSID，最大长度为32字节，编码格式为UTF-8。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| bssid | string | 否 | 否 | 热点的BSSID，例如：00:11:22:33:44:55。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| bssidType10+ | [DeviceAddressType](js-apis-wifimanager.md#deviceaddresstype10) | 否 | 否 | 热点的BSSID类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| capabilities | string | 否 | 否 | 热点能力。 |
| securityType | [WifiSecurityType](js-apis-wifimanager.md#wifisecuritytype) | 否 | 否 | WLAN加密类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| rssi | number | 否 | 否 | 热点的信号强度(dBm)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| band | number | 否 | 否 | WLAN接入点的频段，1表示2.4GHZ；2表示5GHZ。 |
| frequency | number | 否 | 否 | WLAN接入点的频率。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| channelWidth | number | 否 | 否 | WLAN接入点的带宽，具体定义参见[WifiChannelWidth](js-apis-wifimanager.md#wifichannelwidth)。 |
| centerFrequency0 | number | 否 | 否 | 热点的中心频率。 |
| centerFrequency1 | number | 否 | 否 | 热点的中心频率。如果热点使用两个不重叠的WLAN信道，则返回两个中心频率，分别用centerFrequency0和centerFrequency1表示。 |
| infoElems | Array<[WifiInfoElem](js-apis-wifimanager.md#wifiinfoelem)> | 否 | 否 | 信息元素。 |
| timestamp | number | 否 | 否 | 时间戳。 |
| supportedWifiCategory12+ | [WifiCategory](js-apis-wifimanager.md#wificategory12) | 否 | 否 | 热点支持的最高Wi-Fi级别。 |
| isHiLinkNetwork12+ | boolean | 否 | 否 | 热点是否支持hiLink，true表示支持， false表示不支持。 |

## DeviceAddressType10+

PhonePC/2in1TabletTVWearable

WLAN设备地址（MAC/BSSID）类型。是标识WLAN设备或接入点的唯一地址。

在WLAN相关操作中，如连接指定的WLAN网络、获取设备信息等，需要使用DeviceAddressType类型的参数。

**系统能力：** SystemCapability.Communication.WiFi.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RANDOM\_DEVICE\_ADDRESS | 0 | 随机设备地址。 |
| REAL\_DEVICE\_ADDRESS | 1 | 真实设备地址。 |

## WifiSecurityType

PhonePC/2in1TabletTVWearable

表示加密类型的枚举。

**系统能力：** SystemCapability.Communication.WiFi.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WIFI\_SEC\_TYPE\_INVALID | 0 | 无效加密类型。 |
| WIFI\_SEC\_TYPE\_OPEN | 1 | 开放加密类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| WIFI\_SEC\_TYPE\_WEP | 2 | Wired Equivalent Privacy (WEP)加密类型。候选网络(添加网络配置信息)配置不支持该加密类型。 |
| WIFI\_SEC\_TYPE\_PSK | 3 | Pre-shared key (PSK)加密类型。 |
| WIFI\_SEC\_TYPE\_SAE | 4 | Simultaneous Authentication of Equals (SAE)加密类型。 |
| WIFI\_SEC\_TYPE\_EAP | 5 | EAP authentication (EAP)加密类型。 |
| WIFI\_SEC\_TYPE\_EAP\_SUITE\_B | 6 | Suite-B 192位加密类型。 |
| WIFI\_SEC\_TYPE\_OWE | 7 | Opportunistic Wireless Encryption (OWE)机会性无线加密类型。 |
| WIFI\_SEC\_TYPE\_WAPI\_CERT | 8 | WAPI-Cert加密类型。 |
| WIFI\_SEC\_TYPE\_WAPI\_PSK | 9 | WAPI-PSK加密类型。 |

## WifiBandType10+

PhonePC/2in1TabletTVWearable

表示WIFI频段类型的枚举。

**系统能力：** SystemCapability.Communication.WiFi.STA

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WIFI\_BAND\_NONE | 0 | 无效频段类型。 |
| WIFI\_BAND\_2G | 1 | 2.4G频段类型。 |
| WIFI\_BAND\_5G | 2 | 5G频段类型。 |
| WIFI\_BAND\_6G | 3 | 6G频段类型。 |
| WIFI\_BAND\_60G | 4 | 60G频段类型。 |

## WifiStandard10+

PhonePC/2in1TabletTVWearable

表示WIFI标准的枚举。

**系统能力：** SystemCapability.Communication.WiFi.STA

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WIFI\_STANDARD\_UNDEFINED | 0 | 无效WIFI标准类型。 |
| WIFI\_STANDARD\_11A | 1 | 802.11a WiFi标准类型。 |
| WIFI\_STANDARD\_11B | 2 | 802.11b WiFi标准类型。 |
| WIFI\_STANDARD\_11G | 3 | 802.11g WiFi标准类型。 |
| WIFI\_STANDARD\_11N | 4 | 802.11n WiFi标准类型。 |
| WIFI\_STANDARD\_11AC | 5 | 802.11ac WiFi标准类型。 |
| WIFI\_STANDARD\_11AX | 6 | 802.11ax WiFi标准类型。 |
| WIFI\_STANDARD\_11AD | 7 | 802.11ad WiFi标准类型。 |

## WifiInfoElem

PhonePC/2in1TabletTVWearable

WLAN热点信息。

**系统能力：** SystemCapability.Communication.WiFi.STA

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| eid | number | 否 | 否 | 元素ID。 |
| content | Uint8Array | 否 | 否 | 元素内容。 |

## WifiChannelWidth

PhonePC/2in1TabletTVWearable

表示带宽类型的枚举。

**系统能力：** SystemCapability.Communication.WiFi.STA

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WIDTH\_20MHZ | 0 | 20MHZ。 |
| WIDTH\_40MHZ | 1 | 40MHZ。 |
| WIDTH\_80MHZ | 2 | 80MHZ。 |
| WIDTH\_160MHZ | 3 | 160MHZ。 |
| WIDTH\_80MHZ\_PLUS | 4 | 80MHZ+。 |
| WIDTH\_INVALID | 5 | 无效值 |

## WifiDeviceConfig

PhonePC/2in1TabletTVWearable

WLAN配置信息。

**系统能力：** SystemCapability.Communication.WiFi.STA

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| ssid | string | 否 | 否 | 热点的SSID，最大长度为32字节，编码格式为UTF-8。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| bssid | string | 否 | 是 | 热点的BSSID，例如：00:11:22:33:44:55。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| bssidType10+ | [DeviceAddressType](js-apis-wifimanager.md#deviceaddresstype10) | 否 | 是 | 热点的BSSID类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| preSharedKey | string | 否 | 否 | 热点的密钥，最大长度为64字节。  当securityType为WIFI\_SEC\_TYPE\_OPEN时该字段需为空串，其他加密类型不能为空串。  当securityType为WIFI\_SEC\_TYPE\_WEP时，该字段长度只允许为5、10、13、26、16和32字节其中之一，并且当字段长度为偶数时，该字段必须为纯十六进制数字构成。  当securityType为WIFI\_SEC\_TYPE\_SAE时，该字段最小长度为1字节。  当securityType为WIFI\_SEC\_TYPE\_PSK时，该字段最小长度为8字节。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| isHiddenSsid | boolean | 否 | 是 | 是否是隐藏网络。true表示是隐藏网络，false表示不是隐藏网络。 |
| securityType | [WifiSecurityType](js-apis-wifimanager.md#wifisecuritytype) | 否 | 否 | 加密类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| netId22+ | number | 否 | 是 | 分配的网络ID。 |
| eapConfig10+ | [WifiEapConfig](js-apis-wifimanager.md#wifieapconfig10) | 否 | 是 | 可扩展身份验证协议配置。只有securityType为WIFI\_SEC\_TYPE\_EAP时需要填写。 |
| wapiConfig12+ | [WifiWapiConfig](js-apis-wifimanager.md#wifiwapiconfig12) | 否 | 是 | WAPI身份验证协议配置。只有securityType为WIFI\_SEC\_TYPE\_WAPI\_CERT或WIFI\_SEC\_TYPE\_WAPI\_PSK时需要填写。 |

## WifiEapConfig10+

PhonePC/2in1TabletTVWearable

可扩展身份验证协议配置信息。

* WifiEapConfig是一个用于配置WLAN网络EAP认证的类型。
* 包含EAP认证方式、第二阶段认证方式、身份信息、密码、证书等配置项。

**系统能力：** SystemCapability.Communication.WiFi.STA

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| eapMethod | [EapMethod](js-apis-wifimanager.md#eapmethod10) | 否 | 否 | EAP认证方式。 |
| phase2Method | [Phase2Method](js-apis-wifimanager.md#phase2method10) | 否 | 否 | 第二阶段认证方式。只有eapMethod为EAP\_PEAP或EAP\_TTLS时需要填写。 |
| identity | string | 否 | 否 | 身份信息。当eapMethod为EAP\_PEAP、EAP\_TLS或EAP\_PWD时，该字段不能为空串。 |
| anonymousIdentity | string | 否 | 否 | 匿名身份。暂未使用。 |
| password | string | 否 | 否 | 密码。当eapMethod为EAP\_PEAP或EAP\_PWD时，该字段不能为空串，最大长度为128字节。 |
| caCertAlias | string | 否 | 否 | CA证书别名。 |
| caPath | string | 否 | 否 | CA证书路径。 |
| clientCertAlias | string | 否 | 否 | 客户端证书别名。 |
| certEntry | Uint8Array | 否 | 否 | CA证书内容。当eapMethod为EAP\_TLS时，如果该字段为空，则clientCertAlias不能为空。 |
| certPassword | string | 否 | 否 | CA证书密码，最大长度为128字节。 |
| altSubjectMatch | string | 否 | 否 | 替代主题匹配。 |
| domainSuffixMatch | string | 否 | 否 | 域后缀匹配。 |
| realm | string | 否 | 否 | 通行证凭证的领域。 |
| plmn | string | 否 | 否 | 公共陆地移动网的直通凭证提供商。 |
| eapSubId | number | 否 | 否 | SIM卡的子ID。 |

## WifiWapiConfig12+

PhonePC/2in1TabletTVWearable

WAPI(Wireless LAN Authentication and Privacy Infrastructure) 身份验证协议配置。

当用户通过WAPI身份验证协议连接无线网时，可通过以下方式配置参数或者证书进行连接。

* 方式一:通过配置证书进行连接。WifiDeviceConfig中关键字段的配置如下:
  + preSharedKey无需传参;
  + securityType设置为WIFI\_SEC\_TYPE\_WAPI\_CERT;
  + 在wapiConfig中：
    - wapiAsCert传递AS证书的文本内容。
    - wapiUserCert传递用户证书的文本内容。
* 方式二:通过配置preSharedKey进行链接。WifiDeviceConfig中关键字段的配置如下:
  + preSharedKey传参为路由器上设置的密码;
  + securityType设置为WIFI\_SEC\_TYPE\_WAPI\_PSK。

**系统能力：** SystemCapability.Communication.WiFi.STA

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| wapiPskType | [WapiPskType](js-apis-wifimanager.md#wapipsktype12) | 否 | 否 | 加密类型。 |
| wapiAsCert | string | 否 | 否 | AS证书(Authentication Server Certificate，认证服务器证书)。 |
| wapiUserCert | string | 否 | 否 | 用户证书。 |

## WapiPskType12+

PhonePC/2in1TabletTVWearable

WAPI认证方式的枚举。

**系统能力：** SystemCapability.Communication.WiFi.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WAPI\_PSK\_ASCII | 0 | ASCII类型。 |
| WAPI\_PSK\_HEX | 1 | HEX类型。 |

## EapMethod10+

PhonePC/2in1TabletTVWearable

表示EAP认证方式的枚举。

**系统能力：** SystemCapability.Communication.WiFi.STA

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EAP\_NONE | 0 | 不指定。 |
| EAP\_PEAP | 1 | PEAP类型。 |
| EAP\_TLS | 2 | TLS类型。 |
| EAP\_TTLS | 3 | TTLS类型。 |
| EAP\_PWD | 4 | PWD类型。 |
| EAP\_SIM | 5 | SIM类型。 |
| EAP\_AKA | 6 | AKA类型。 |
| EAP\_AKA\_PRIME | 7 | AKA Prime类型。 |
| EAP\_UNAUTH\_TLS | 8 | UNAUTH TLS类型。 |

## Phase2Method10+

PhonePC/2in1TabletTVWearable

表示第二阶段认证方式的枚举。

**系统能力：** SystemCapability.Communication.WiFi.STA

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PHASE2\_NONE | 0 | 不指定。 |
| PHASE2\_PAP | 1 | PAP类型。 |
| PHASE2\_MSCHAP | 2 | MSCHAP类型。 |
| PHASE2\_MSCHAPV2 | 3 | MSCHAPV2类型。 |
| PHASE2\_GTC | 4 | GTC类型。 |
| PHASE2\_SIM | 5 | SIM类型。 |
| PHASE2\_AKA | 6 | AKA类型。 |
| PHASE2\_AKA\_PRIME | 7 | AKA Prime类型。 |

## WifiCategory12+

PhonePC/2in1TabletTVWearable

表示热点支持的最高WLAN类别。可以用于识别和区分不同WLAN技术标准的热点。

**系统能力：** SystemCapability.Communication.WiFi.STA

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 1 | Default。Wifi6以下的wifi类别。 |
| WIFI6 | 2 | Wifi6。 |
| WIFI6\_PLUS | 3 | Wifi6+。 |
| WIFI715+ | 4 | Wifi7。 |
| WIFI7\_PLUS15+ | 5 | Wifi7+。 |

## wifiManager.addCandidateConfig

PhonePC/2in1TabletTVWearable

addCandidateConfig(config: WifiDeviceConfig): Promise<number>

添加候选网络配置，使用Promise异步回调，使用前先使能WLAN。

* 通过传入[WifiDeviceConfig](js-apis-wifimanager.md#wifideviceconfig)对象，配置WLAN网络的详细信息，如SSID、密码、安全类型等。
* 返回一个Promise对象，解析后得到一个数字，表示配置的ID(用于区分、管理不同WLAN配置，其他相关API操作，错误处理调试等)。

**需要权限：** ohos.permission.SET\_WIFI\_INFO

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [WifiDeviceConfig](js-apis-wifimanager.md#wifideviceconfig) | 是 | WLAN配置信息。如果bssidType未指定值，则bssidType默认为随机设备地址类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。表示网络配置ID。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified.  2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. try {
4. let config:wifiManager.WifiDeviceConfig = {
5. ssid : "****",
6. preSharedKey : "****",
7. securityType : 0
8. }
9. wifiManager.addCandidateConfig(config).then(result => {
10. console.info("result:" + JSON.stringify(result));
11. }).catch((err:number) => {
12. console.error("failed:" + JSON.stringify(err));
13. });
14. }catch(error){
15. console.error("failed:" + JSON.stringify(error));
16. }
```

## wifiManager.addCandidateConfig

PhonePC/2in1TabletTVWearable

addCandidateConfig(config: WifiDeviceConfig, callback: AsyncCallback<number>): void

添加候选网络配置，使用callback异步回调。

* 将指定的WLAN设备配置添加为候选网络，添加后的网络在没有连接记录的情况下无法触发自动回连，可以通过 connectToCandidateConfig或connectToCandidateConfigWithUserAction 方法实现候选网络连接，页面确认连接成功后，可实现自动回连。
* 候选网络属于应用维度添加的网络配置，和系统网络配置是相互隔离的，在系统WLAN页面不可见。

**需要权限：** ohos.permission.SET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [WifiDeviceConfig](js-apis-wifimanager.md#wifideviceconfig) | 是 | WLAN配置信息。如果bssidType未指定值，则bssidType默认为随机设备地址类型。 |
| callback | AsyncCallback<number> | 是 | 回调函数。err为0时：操作成功，data为添加的网络配置ID，如果data值为-1，表示添加失败。  err为非0值时：操作出现错误。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified.  2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. try {
4. let config:wifiManager.WifiDeviceConfig = {
5. ssid : "****",
6. preSharedKey : "****",
7. securityType : 0
8. }
9. wifiManager.addCandidateConfig(config,(error,result) => {
10. console.info("result:" + JSON.stringify(result));
11. });
12. }catch(error){
13. console.error("failed:" + JSON.stringify(error));
14. }
```

## wifiManager.removeCandidateConfig

PhonePC/2in1TabletTVWearable

removeCandidateConfig(networkId: number): Promise<void>

移除候选网络配置，使用Promise异步回调。

* 从系统中删除指定网络ID的WLAN候选配置，清理不再需要的WLAN候选配置，释放系统资源。
* 只能移除通过[addCandidateConfig](js-apis-wifimanager.md#wifimanageraddcandidateconfig)添加的候选配置，移除后该候选网络将不再被系统自动连接。

**需要权限：** ohos.permission.SET\_WIFI\_INFO

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| networkId | number | 是 | 网络配置ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified.  2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |
| 2501001 | Wi-Fi STA disabled. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. try {
4. let networkId = 0;
5. wifiManager.removeCandidateConfig(networkId).then(result => {
6. console.info("result:" + JSON.stringify(result));
7. }).catch((err:number) => {
8. console.error("failed:" + JSON.stringify(err));
9. });
10. }catch(error){
11. console.error("failed:" + JSON.stringify(error));
12. }
```

## wifiManager.removeCandidateConfig

PhonePC/2in1TabletTVWearable

removeCandidateConfig(networkId: number, callback: AsyncCallback<void>): void

移除指定的候选网络配置，使用callback异步回调。

* 从系统中删除指定网络ID的WLAN候选配置，清理不再需要的WLAN候选配置，释放系统资源。
* 只能移除通过[addCandidateConfig](js-apis-wifimanager.md#wifimanageraddcandidateconfig)添加的候选配置，移除后该候选网络将不再被系统自动连接。

**需要权限：** ohos.permission.SET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| networkId | number | 是 | 网络配置ID。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当操作成功时，err为0。如果error为非0，表示处理出现错误。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified.  2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |
| 2501001 | Wi-Fi STA disabled. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. try {
4. let networkId = 0;
5. wifiManager.removeCandidateConfig(networkId,(error,result) => {
6. console.info("result:" + JSON.stringify(result));
7. });
8. }catch(error){
9. console.error("failed:" + JSON.stringify(error));
10. }
```

## wifiManager.removeDevice15+

PhonePC/2in1TabletTVWearable

removeDevice(id: number): void

移除网络配置。

* 通过网络配置ID删除已保存的WLAN网络配置信息。
* 移除后对应的网络配置将不再可用，设备也不会再自动连接该网络。

**需要权限：** ohos.permission.SET\_WIFI\_INFO 和 (ohos.permission.MANAGE\_WIFI\_CONNECTION 仅系统应用可用 或 ohos.permission.MANAGE\_ENTERPRISE\_WIFI\_CONNECTION 仅企业应用可用)

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 网络配置ID。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified.  2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |
| 2501001 | Wi-Fi STA disabled. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. try {
4. let id = 0;
5. wifiManager.removeDevice(id);
6. }catch(error){
7. console.error("failed:" + JSON.stringify(error));
8. }
```

## wifiManager.getCandidateConfigs

PhonePC/2in1TabletTVWearable

getCandidateConfigs(): Array<WifiDeviceConfig>

获取候选网络配置。

* 候选网络是指曾经连接过或者手动添加的网络配置。
* 该接口返回系统中所有已保存但当前未连接的WLAN网络配置。
* 用于展示可连接的网络列表或进行网络管理操作。

**需要权限：**

API 10起：ohos.permission.GET\_WIFI\_INFO

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[WifiDeviceConfig](js-apis-wifimanager.md#wifideviceconfig)> | 候选网络配置数组。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. try {
4. let configs = wifiManager.getCandidateConfigs();
5. console.info("configs:" + JSON.stringify(configs));
6. let len = configs.length;
7. console.info("result len: " + len);
8. if(len > 0){
9. for (let i = 0; i < len; ++i) {
10. console.info("ssid: " + configs[i].ssid);
11. console.info("bssid: " + configs[i].bssid);
12. }
13. }
14. }catch(error){
15. console.error("failed:" + JSON.stringify(error));
16. }
```

## wifiManager.connectToCandidateConfig

PhonePC/2in1TabletTVWearable

connectToCandidateConfig(networkId: number): void

应用使用该接口连接到自己添加的候选网络。

**需要权限：** ohos.permission.SET\_WIFI\_INFO

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| networkId | number | 是 | 候选网络配置的ID。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified.  2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |
| 2501001 | Wi-Fi STA disabled. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. try {
4. let networkId = 0; // 候选网络ID，在添加候选网络时生成
5. wifiManager.connectToCandidateConfig(networkId);
6. }catch(error){
7. console.error("failed:" + JSON.stringify(error));
8. }
```

## wifiManager.connectToCandidateConfigWithUserAction20+

PhonePC/2in1TabletTVWearable

connectToCandidateConfigWithUserAction(networkId: number): Promise<void>

该接口用于应用连接到用户添加的候选网络，并在连接时提示用户进行信任确认。使用Promise异步回调。

* 调用此接口时，系统将提示用户确认是否信任并连接到指定的候选网络。
* 用户确认是连接过程中的必要步骤，未获得用户信任确认前，连接操作不会执行。
* 建议在发起连接前先通过startScan接口触发一次WLAN扫描，通过[wifiManager.on('wifiScanStateChange')](js-apis-wifimanager.md#wifimanageronwifiscanstatechange)方法监听到扫描结果刷新后再连接，以提高连接成功率。

说明

调用[wifiManager.connectToCandidateConfig](js-apis-wifimanager.md#wifimanagerconnecttocandidateconfig)连接候选网络时，不会返回用户响应结果。

**需要权限：** ohos.permission.SET\_WIFI\_INFO

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| networkId | number | 是 | 候选网络配置的ID，ID不能小于0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |
| 2501001 | Wi-Fi STA disabled. |
| 2501005 | The user does not respond. |
| 2501006 | The user refused the action. |
| 2501007 | Parameter validation failed. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. try {
4. let networkId = 0; // 候选网络ID，在添加候选网络时生成
5. wifiManager.connectToCandidateConfigWithUserAction(networkId).then(result => {
6. console.info("result:" + JSON.stringify(result));
7. }).catch((err:number) => {
8. console.error("failed:" + JSON.stringify(err));
9. });
10. }catch(error){
11. console.error("failed:" + JSON.stringify(error));
12. }
```

## wifiManager.addDeviceConfig15+

PhonePC/2in1TabletTVWearable

addDeviceConfig(config: WifiDeviceConfig): Promise<number>

添加网络配置。使用Promise异步回调。

**需要权限：** ohos.permission.SET\_WIFI\_INFO 和 ohos.permission.SET\_WIFI\_CONFIG

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [WifiDeviceConfig](js-apis-wifimanager.md#wifideviceconfig) | 是 | WLAN配置信息。如果bssidType无指定值，则bssidType默认为随机设备地址类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。表示网络配置ID。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified.  2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |
| 2501001 | Wi-Fi STA disabled. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. try {
4. let config:wifiManager.WifiDeviceConfig = {
5. ssid : "****",
6. preSharedKey : "****",
7. securityType : 0
8. }
9. wifiManager.addDeviceConfig(config).then(result => {
10. console.info("result:" + JSON.stringify(result));
11. }).catch((err:number) => {
12. console.error("failed:" + JSON.stringify(err));
13. });
14. }catch(error){
15. console.error("failed:" + JSON.stringify(error));
16. }
```

## wifiManager.addDeviceConfig15+

PhonePC/2in1TabletTVWearable

addDeviceConfig(config: WifiDeviceConfig, callback: AsyncCallback<number>): void

添加网络配置。使用callback异步回调。

**需要权限：** ohos.permission.SET\_WIFI\_INFO 和 ohos.permission.SET\_WIFI\_CONFIG

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [WifiDeviceConfig](js-apis-wifimanager.md#wifideviceconfig) | 是 | WLAN配置信息。如果bssidType无指定值，则bssidType默认为随机设备地址类型。 |
| callback | AsyncCallback<number> | 是 | 回调函数。当操作成功时，err为0，data为添加的网络配置ID，如果data值为-1，表示添加失败。当操作错误，err为非0值。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified.  2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |
| 2501001 | Wi-Fi STA disabled. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. try {
4. let config:wifiManager.WifiDeviceConfig = {
5. ssid : "****",
6. preSharedKey : "****",
7. securityType : 0
8. }
9. wifiManager.addDeviceConfig(config,(error,result) => {
10. console.info("result:" + JSON.stringify(result));
11. });
12. }catch(error){
13. console.error("failed:" + JSON.stringify(error));
14. }
```

## wifiManager.getDeviceConfigs15+

PhonePC/2in1TabletTVWearable

getDeviceConfigs(): Array<WifiDeviceConfig>

获取网络配置。

**需要权限：** ohos.permission.GET\_WIFI\_INFO 和 ohos.permission.GET\_WIFI\_CONFIG

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[WifiDeviceConfig](js-apis-wifimanager.md#wifideviceconfig)> | 网络配置数组。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. try {
4. let configs = wifiManager.getDeviceConfigs();
5. console.info("configs:" + JSON.stringify(configs));
6. }catch(error){
7. console.error("failed:", error.code, error.message);
8. }
```

## wifiManager.connectToNetwork15+

PhonePC/2in1TabletTVWearable

connectToNetwork(networkId: number): void

应用使用该接口连接到热点。

**需要权限：** ohos.permission.MANAGE\_WIFI\_CONNECTION 仅系统应用可用 或 ohos.permission.MANAGE\_ENTERPRISE\_WIFI\_CONNECTION 仅企业应用可用

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| networkId | number | 是 | 候选网络配置的ID。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified.  2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |
| 2501001 | Wi-Fi STA disabled. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. try {
4. let networkId = 0;
5. wifiManager.connectToNetwork(networkId);
6. }catch(error){
7. console.error("failed:" + JSON.stringify(error));
8. }
```

## wifiManager.getSignalLevel

PhonePC/2in1TabletTVWearable

getSignalLevel(rssi: number, band: number): number

查询WLAN信号强度。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rssi | number | 是 | 热点的信号强度(dBm)。 |
| band | number | 是 | WLAN接入点的频段，1表示2.4GHZ；2表示5GHZ。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 信号强度，取值范围为[0, 4]。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. try {
4. let rssi = 0;
5. let band = 0;
6. let level = wifiManager.getSignalLevel(rssi,band);
7. console.info("level:" + JSON.stringify(level));
8. }catch(error){
9. console.error("failed:" + JSON.stringify(error));
10. }
```

## wifiManager.getLinkedInfo

PhonePC/2in1TabletTVWearable

getLinkedInfo(): Promise<WifiLinkedInfo>

获取WLAN连接信息。使用Promise异步回调。

**需要权限：** ohos.permission.GET\_WIFI\_INFO 。

当macType是1 - 设备MAC地址时，获取 macAddress 还需申请ohos.permission.GET\_WIFI\_LOCAL\_MAC权限（API8-15仅面向系统应用开放。从API 16开始，在PC/2in1设备上面向普通应用开放，在其余设备上仍仅面向系统应用开放），无该权限时，macAddress 返回随机MAC地址。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[WifiLinkedInfo](js-apis-wifimanager.md#wifilinkedinfo)> | Promise对象。表示WLAN连接信息。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |
| 2501001 | Wi-Fi STA disabled. |

## wifiManager.getLinkedInfo

PhonePC/2in1TabletTVWearable

getLinkedInfo(callback: AsyncCallback<WifiLinkedInfo>): void

获取WLAN连接信息。使用callback异步回调。

**需要权限：** ohos.permission.GET\_WIFI\_INFO 。

说明

* 当macType是1（设备MAC地址），获取macAddress还需申请ohos.permission.GET\_WIFI\_LOCAL\_MAC权限（API8-15仅面向系统应用开放。从API 16开始，在PC/2in1设备上面向普通应用开放，在其余设备上仍仅面向系统应用开放），无该权限时，macAddress返回为空。
* 如果应用申请了ohos.permission.GET\_WIFI\_PEERS\_MAC权限，则返回结果中的bssid为真实BSSID地址，否则为随机设备地址。

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[WifiLinkedInfo](js-apis-wifimanager.md#wifilinkedinfo)> | 是 | 回调函数。当获取成功时，err为0，data表示WLAN连接信息。如果err为非0，表示处理出现错误。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |
| 2501001 | Wi-Fi STA disabled. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. wifiManager.getLinkedInfo().then((data: wifiManager.WifiLinkedInfo) => {
4. console.info("get wifi linked info: " + JSON.stringify(data));
5. }).catch((error: Error) => {
6. console.error("get linked info error: ", error);
7. });
```

## wifiManager.getLinkedInfoSync18+

PhonePC/2in1TabletTVWearable

getLinkedInfoSync(): WifiLinkedInfo;

获取WLAN连接信息，使用同步方式返回结果。

**需要权限：** ohos.permission.GET\_WIFI\_INFO 。

说明

* 当macType是1（设备MAC地址），获取macAddress还需申请ohos.permission.GET\_WIFI\_LOCAL\_MAC权限（API8-15仅面向系统应用开放。从API 16开始，在PC/2in1设备上面向普通应用开放，在其余设备上仍仅面向系统应用开放），无该权限时，macAddress返回为空。
* 如果应用申请了ohos.permission.GET\_WIFI\_PEERS\_MAC权限，则返回结果中的bssid为真实BSSID地址，否则为随机设备地址。

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WifiLinkedInfo](js-apis-wifimanager.md#wifilinkedinfo) | 表示WLAN连接信息。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |
| 2501001 | Wi-Fi STA disabled. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';
2. try {
3. let linkInfo = wifiManager.getLinkedInfoSync();
4. console.info("get linked info:" + JSON.stringify(linkInfo));
5. } catch(error) {
6. console.error("get linked info failed:" + JSON.stringify(error));
7. }
```

## WifiLinkedInfo

PhonePC/2in1TabletTVWearable

提供WLAN连接的相关信息。

**系统能力：** SystemCapability.Communication.WiFi.STA

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| ssid | string | 否 | 否 | 热点的SSID（Service Set Identifier，服务集标识符），用于获取当前设备已连接的Wi-Fi热点的公开名称（即无线网络的名称），编码格式为UTF-8。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| bssid | string | 否 | 否 | 热点的BSSID（Basic Service Set Identifier，基本服务集标识符）即无线网络的MAC地址。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| rssi | number | 否 | 否 | 热点的信号强度(dBm)。  RSSI（Received Signal Strength Indicator，接收信号强度指示），其标准取值范围为-127dBm至0dBm。在正常使用场景下，常见有效范围为-100dBm（弱信号）至-30dBm（强信号），接近0dBm表示信号极强。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| band | number | 否 | 否 | WLAN接入点的频段，1表示2.4GHZ；2表示5GHZ。 |
| linkSpeed | number | 否 | 否 | WLAN接入点的上行速度，单位Mbps。 |
| rxLinkSpeed10+ | number | 否 | 否 | WLAN接入点的下行速度，单位Mbps。 |
| maxSupportedTxLinkSpeed10+ | number | 否 | 否 | 当前支持的最大上行速率，单位Mbps。 |
| maxSupportedRxLinkSpeed10+ | number | 否 | 否 | 当前支持的最大下行速率，单位Mbps。 |
| frequency | number | 否 | 否 | WLAN接入点的频率。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| isHidden | boolean | 否 | 否 | WLAN接入点是否是隐藏网络，true表示是隐藏网络，false表示不是隐藏网络。 |
| isRestricted | boolean | 否 | 否 | WLAN接入点是否限制数据量，true表示限制，false表示不限制。 |
| macType | number | 否 | 否 | MAC地址类型。0 - 随机MAC地址，1 - 设备MAC地址。 |
| macAddress | string | 否 | 否 | 设备的MAC地址。 |
| ipAddress | number | 否 | 否 | WLAN连接的IP地址。  1. IP地址在WiFi连接信息和"设置 > 关于本机 > 状态信息"中可以查看。  2. ipAddress值为number类型，需要转换为IP常用格式，具体请参考[IP格式转换](../harmonyos-faqs/faqs-connectivity-4.md)。 |
| connState | [ConnState](js-apis-wifimanager.md#connstate) | 否 | 否 | WLAN连接状态。 |
| channelWidth10+ | [WifiChannelWidth](js-apis-wifimanager.md#wifichannelwidth) | 否 | 否 | 当前连接热点的信道带宽。 |
| wifiStandard10+ | [WifiStandard](js-apis-wifimanager.md#wifistandard10) | 否 | 否 | 当前连接热点的Wi-Fi标准。 |
| supportedWifiCategory12+ | [WifiCategory](js-apis-wifimanager.md#wificategory12) | 否 | 否 | 热点支持的最高Wi-Fi级别。 |
| isHiLinkNetwork12+ | boolean | 否 | 否 | 热点是否支持hilink，true表示支持， false表示不支持。 |
| wifiLinkType18+ | [WifiLinkType](js-apis-wifimanager.md#wifilinktype18) | 否 | 是 | Wi-Fi7连接类型。 |

## WifiLinkType18+

PhonePC/2in1TabletTVWearable

枚举，Wi-Fi7连接类型。

**系统能力：** SystemCapability.Communication.WiFi.STA

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT\_LINK | 0 | 默认连接类型。 |
| WIFI7\_SINGLE\_LINK | 1 | Wi-Fi7单链连接。 |
| WIFI7\_MLSR | 2 | Wi-Fi7 MLSR（multi-link single-radio，多链路多天线）连接。 |
| WIFI7\_EMLSR | 3 | Wi-Fi7 EMLSR（enhanced multi-link single-radio，增强型多链路单天线）连接。 |
| WIFI7\_STR | 4 | Wi-Fi7 STR（Simultaneous Tx and Rx，同时发送和接收）连接。 |

## ConnState

PhonePC/2in1TabletTVWearable

表示WLAN连接状态的枚举。

**系统能力：** SystemCapability.Communication.WiFi.STA

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SCANNING | 0 | 设备正在搜索可用的AP。 |
| CONNECTING | 1 | 正在建立WLAN连接。 |
| AUTHENTICATING | 2 | WLAN连接正在认证中。 |
| OBTAINING\_IPADDR | 3 | 正在获取WLAN连接的IP地址。 |
| CONNECTED | 4 | WLAN连接已建立。 |
| DISCONNECTING | 5 | WLAN连接正在断开。 |
| DISCONNECTED | 6 | WLAN连接已断开。 |
| UNKNOWN | 7 | WLAN连接建立失败。 |

## wifiManager.isConnected

PhonePC/2in1TabletTVWearable

isConnected(): boolean

查询WLAN是否已连接。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true:已连接， false:未连接。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. try {
4. let ret = wifiManager.isConnected();
5. console.info("isConnected:" + ret);
6. }catch(error){
7. console.error("failed:" + JSON.stringify(error));
8. }
```

## wifiManager.disconnect15+

PhonePC/2in1TabletTVWearable

disconnect(): void

断开WLAN连接。

**需要权限：** ohos.permission.SET\_WIFI\_INFO 和 (ohos.permission.MANAGE\_WIFI\_CONNECTION 仅系统应用可用 或

ohos.permission.MANAGE\_ENTERPRISE\_WIFI\_CONNECTION 仅企业应用可用)

**系统能力：** SystemCapability.Communication.WiFi.STA

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |
| 2501001 | Wi-Fi STA disabled. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. try {
4. wifiManager.disconnect();
5. }catch(error){
6. console.error("failed:" + JSON.stringify(error));
7. }
```

## wifiManager.isFeatureSupported

PhonePC/2in1TabletTVWearable

isFeatureSupported(featureId: number): boolean

判断设备是否支持相关WLAN特性。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| featureId | number | 是 | 特性ID值。 |

**特性ID值枚举：**

| 枚举值 | 说明 |
| --- | --- |
| 0x0001 | 基础结构模式特性。 |
| 0x0002 | 5 GHz带宽特性。 |
| 0x0004 | GAS/ANQP特性。 |
| 0x0008 | Wifi-Direct特性。 |
| 0x0010 | Soft AP特性。 |
| 0x0040 | Wi-Fi AWare组网特性。 |
| 0x8000 | AP STA共存特性。 |
| 0x8000000 | WPA3-Personal SAE特性。 |
| 0x10000000 | WPA3-Enterprise Suite-B。 |
| 0x20000000 | 增强开放特性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true:支持， false:不支持。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified.  2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2401000 | Operation failed. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. try {
4. let featureId = 0;
5. let ret = wifiManager.isFeatureSupported(featureId);
6. console.info("isFeatureSupported:" + ret);
7. }catch(error){
8. console.error("failed:" + JSON.stringify(error));
9. }
```

## wifiManager.getDeviceMacAddress15+

PhonePC/2in1TabletTVWearable

getDeviceMacAddress(): string[]

获取设备的MAC地址。

**需要权限：** ohos.permission.GET\_WIFI\_LOCAL\_MAC 和 ohos.permission.GET\_WIFI\_INFO

API8-15 ohos.permission.GET\_WIFI\_LOCAL\_MAC权限仅向系统应用开放，从API16开始，在PC/2in1设备上面向普通应用开放，在其余设备上仍仅面向系统应用开放。

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] | MAC地址。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |
| 2501001 | Wi-Fi STA disabled. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. try {
4. let ret = wifiManager.getDeviceMacAddress();
5. console.info("deviceMacAddress:" + JSON.stringify(ret));
6. }catch(error){
7. console.error("failed:" + JSON.stringify(error));
8. }
```

## wifiManager.getIpInfo

PhonePC/2in1TabletTVWearable

getIpInfo(): IpInfo

获取IPV4信息。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IpInfo](js-apis-wifimanager.md#ipinfo) | IP信息。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. try {
4. let info = wifiManager.getIpInfo();
5. console.info("info:" + JSON.stringify(info));
6. }catch(error){
7. console.error("failed:" + JSON.stringify(error));
8. }
```

## IpInfo

PhonePC/2in1TabletTVWearable

IPV4信息。

**系统能力：** SystemCapability.Communication.WiFi.STA

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| ipAddress | number | 否 | 否 | IP地址。（ipAddress值为number类型，需要转换为IP常用格式，具体请参考[IP格式转换](../harmonyos-faqs/faqs-connectivity-4.md)）。 |
| gateway | number | 否 | 否 | 网关。 |
| netmask | number | 否 | 否 | 掩码。 |
| primaryDns | number | 否 | 否 | 主DNS服务器IP地址。 |
| secondDns | number | 否 | 否 | 备DNS服务器IP地址。 |
| serverIp | number | 否 | 否 | DHCP服务端IP地址。 |
| leaseDuration | number | 否 | 否 | IP地址租用时长，单位：秒。 |

## wifiManager.getIpv6Info10+

PhonePC/2in1TabletTVWearable

getIpv6Info(): Ipv6Info

获取IPV6信息。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Ipv6Info](js-apis-wifimanager.md#ipv6info10) | Ipv6信息。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. try {
4. let info = wifiManager.getIpv6Info();
5. console.info("info:" + JSON.stringify(info));
6. }catch(error){
7. console.error("failed:" + JSON.stringify(error));
8. }
```

## Ipv6Info10+

PhonePC/2in1TabletTVWearable

Ipv6信息。

**系统能力：** SystemCapability.Communication.WiFi.STA

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| linkIpv6Address | string | 否 | 否 | 链路Ipv6地址。 |
| globalIpv6Address | string | 否 | 否 | 全局Ipv6地址。 |
| randomGlobalIpv6Address | string | 否 | 否 | 随机全局Ipv6地址。 预留字段，暂不支持。 |
| uniqueIpv6Address12+ | string | 否 | 是 | 唯一本地Ipv6地址。 |
| randomUniqueIpv6Address12+ | string | 否 | 是 | 随机唯一本地Ipv6地址。 |
| gateway | string | 否 | 否 | 网关。 |
| netmask | string | 否 | 否 | 网络掩码。 |
| primaryDNS | string | 否 | 否 | 主DNS服务器Ipv6地址。 |
| secondDNS | string | 否 | 否 | 备DNS服务器Ipv6地址。 |

## wifiManager.getCountryCode

PhonePC/2in1TabletTVWearable

getCountryCode(): string

获取国家码信息。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 国家码。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2401000 | Operation failed. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. try {
4. let code = wifiManager.getCountryCode();
5. console.info("code:" + code);
6. }catch(error){
7. console.error("failed:" + JSON.stringify(error));
8. }
```

## wifiManager.isBandTypeSupported10+

PhonePC/2in1TabletTVWearable

isBandTypeSupported(bandType: WifiBandType): boolean

判断当前频段是否支持。

**需要权限：** ohos.permission.GET\_WIFI\_INFO。

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bandType | [WifiBandType](js-apis-wifimanager.md#wifibandtype10) | 是 | Wifi 频段类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true:支持， false:不支持。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. try {
4. let type = 0;
5. let isBandTypeSupported = wifiManager.isBandTypeSupported(type);
6. console.info("isBandTypeSupported:" + isBandTypeSupported);
7. }catch(error){
8. console.error("failed:" + JSON.stringify(error));
9. }
```

## wifiManager.isMeteredHotspot11+

PhonePC/2in1TabletTVWearable

isMeteredHotspot(): boolean

查询设备当前连接的wifi是否是手机热点。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true:是手机热点， false:不是手机热点。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |
| 2501001 | Wi-Fi STA disabled. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. try {
4. let isMeteredHotspot = wifiManager.isMeteredHotspot();
5. console.info("isMeteredHotspot:" + isMeteredHotspot);
6. }catch(error){
7. console.error("failed:" + JSON.stringify(error));
8. }
```

## wifiManager.isHotspotActive15+

PhonePC/2in1TabletTVWearable

isHotspotActive(): boolean

热点是否已使能。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.AP.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true:已使能， false:未使能。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2601000 | Operation failed. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. try {
4. let ret = wifiManager.isHotspotActive();
5. console.info("result:" + ret);
6. } catch(error) {
7. console.error("failed:" + JSON.stringify(error));
8. }
```

## wifiManager.getP2pLinkedInfo

PhonePC/2in1TabletTVWearable

getP2pLinkedInfo(): Promise<WifiP2pLinkedInfo>

获取P2P连接信息。使用Promise异步回调。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

获取 groupOwnerAddr 还需申请ohos.permission.GET\_WIFI\_LOCAL\_MAC权限（API8-15仅面向系统应用开放。从API 16开始，在PC/2in1设备上面向普通应用开放，在其余设备上仍仅面向系统应用开放），无该权限时，groupOwnerAddr 返回全零地址。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[WifiP2pLinkedInfo](js-apis-wifimanager.md#wifip2plinkedinfo)> | Promise对象。表示P2P连接信息。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |

## wifiManager.getP2pLinkedInfo

PhonePC/2in1TabletTVWearable

getP2pLinkedInfo(callback: AsyncCallback<WifiP2pLinkedInfo>): void

获取P2P连接信息。使用callback异步回调。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

获取 groupOwnerAddr 还需申请ohos.permission.GET\_WIFI\_LOCAL\_MAC权限（API8-15仅面向系统应用开放。从API 16开始，在PC/2in1设备上面向普通应用开放，在其余设备上仍仅面向系统应用开放），无该权限时，groupOwnerAddr 返回全零地址。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[WifiP2pLinkedInfo](js-apis-wifimanager.md#wifip2plinkedinfo)> | 是 | 回调函数。当操作成功时，err为0，data表示P2P连接信息。如果err为非0，表示处理出现错误。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |
| 2801001 | Wi-Fi STA disabled. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. wifiManager.getP2pLinkedInfo((err, data:wifiManager.WifiP2pLinkedInfo) => {
4. if (err) {
5. console.error("get p2p linked info error");
6. return;
7. }
8. console.info("get wifi p2p linked info: " + JSON.stringify(data));
9. });

11. wifiManager.getP2pLinkedInfo().then(data => {
12. console.info("get wifi p2p linked info: " + JSON.stringify(data));
13. });
```

## WifiP2pLinkedInfo

PhonePC/2in1TabletTVWearable

提供WLAN连接的相关信息。

**系统能力：** SystemCapability.Communication.WiFi.P2P

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| connectState | [P2pConnectState](js-apis-wifimanager.md#p2pconnectstate) | 否 | 否 | P2P连接状态。 |
| isGroupOwner | boolean | 否 | 否 | true表示是群主，false表示不是群主。 |
| groupOwnerAddr | string | 否 | 否 | 群组IP地址。 |

## P2pConnectState

PhonePC/2in1TabletTVWearable

表示P2P连接状态的枚举。

**系统能力：** SystemCapability.Communication.WiFi.P2P

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DISCONNECTED | 0 | 断开状态。 |
| CONNECTED | 1 | 连接状态。 |

## wifiManager.getCurrentGroup

PhonePC/2in1TabletTVWearable

getCurrentGroup(): Promise<WifiP2pGroupInfo>

获取P2P当前组信息。使用Promise异步回调。

**需要权限：**

API 10起：ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[WifiP2pGroupInfo](js-apis-wifimanager.md#wifip2pgroupinfo)> | Promise对象。表示当前组信息。如果应用申请了ohos.permission.GET\_WIFI\_PEERS\_MAC权限，则返回结果中的deviceAddress为真实设备地址，否则为随机设备地址。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |

## wifiManager.getCurrentGroup

PhonePC/2in1TabletTVWearable

getCurrentGroup(callback: AsyncCallback<WifiP2pGroupInfo>): void

获取P2P当前组信息。使用callback异步回调。

**需要权限：**

API 10起：ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[WifiP2pGroupInfo](js-apis-wifimanager.md#wifip2pgroupinfo)> | 是 | 回调函数。当操作成功时，err为0，data表示当前组信息。如果error为非0，表示处理出现错误。如果应用申请了ohos.permission.GET\_WIFI\_PEERS\_MAC权限，则返回结果中的deviceAddress为真实设备地址，否则为随机设备地址。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';
2. // p2p已经建组或者连接成功，才能正常获取到当前组信息
3. wifiManager.getCurrentGroup((err, data:wifiManager.WifiP2pGroupInfo) => {
4. if (err) {
5. console.error("get current P2P group error");
6. return;
7. }
8. console.info("get current P2P group: " + JSON.stringify(data));
9. });

11. wifiManager.getCurrentGroup().then(data => {
12. console.info("get current P2P group: " + JSON.stringify(data));
13. });
```

## wifiManager.getP2pPeerDevices

PhonePC/2in1TabletTVWearable

getP2pPeerDevices(): Promise<WifiP2pDevice[]>

获取P2P对端设备列表信息。使用Promise异步回调。

**需要权限：**

API 10起：ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[WifiP2pDevice[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifip2pdevice)> | Promise对象。表示对端设备列表信息。如果应用申请了ohos.permission.GET\_WIFI\_PEERS\_MAC权限，则返回结果中的deviceAddress为真实设备地址，否则为随机设备地址。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |

## wifiManager.getP2pPeerDevices

PhonePC/2in1TabletTVWearable

getP2pPeerDevices(callback: AsyncCallback<WifiP2pDevice[]>): void

获取P2P对端设备列表信息。使用callback异步回调。

**需要权限：**

API 10起：ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[WifiP2pDevice[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifip2pdevice)> | 是 | 回调函数。当操作成功时，err为0，data表示对端设备列表信息。如果err为非0，表示处理出现错误。如果应用申请了ohos.permission.GET\_WIFI\_PEERS\_MAC权限，则返回结果中的deviceAddress为真实设备地址，否则为随机设备地址。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |
| 2801001 | Wi-Fi STA disabled. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';
2. // p2p发现阶段完成，才能正常获取到对端设备列表信息
3. wifiManager.getP2pPeerDevices((err, data:wifiManager.WifiP2pDevice[]) => {
4. if (err) {
5. console.error("get P2P peer devices error");
6. return;
7. }
8. console.info("get P2P peer devices: " + JSON.stringify(data));
9. });

11. wifiManager.getP2pPeerDevices().then(data => {
12. console.info("get P2P peer devices: " + JSON.stringify(data));
13. });
```

## WifiP2pDevice

PhonePC/2in1TabletTVWearable

表示P2P设备信息。

**系统能力：** SystemCapability.Communication.WiFi.P2P

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceName | string | 否 | 否 | 设备名称。 |
| deviceAddress | string | 否 | 否 | 设备MAC地址。 |
| deviceAddressType10+ | [DeviceAddressType](js-apis-wifimanager.md#deviceaddresstype10) | 否 | 是 | 设备MAC地址类型。 |
| primaryDeviceType | string | 否 | 否 | 主设备类型。 |
| deviceStatus | [P2pDeviceStatus](js-apis-wifimanager.md#p2pdevicestatus) | 否 | 否 | 设备状态。 |
| groupCapabilities | number | 否 | 否 | 群组能力。 |

## P2pDeviceStatus

PhonePC/2in1TabletTVWearable

表示设备状态的枚举。

**系统能力：** SystemCapability.Communication.WiFi.P2P

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CONNECTED | 0 | 连接状态。 |
| INVITED | 1 | 邀请状态。 |
| FAILED | 2 | 失败状态。 |
| AVAILABLE | 3 | 可用状态。 |
| UNAVAILABLE | 4 | 不可用状态。 |

## wifiManager.getP2pLocalDevice

PhonePC/2in1TabletTVWearable

getP2pLocalDevice(): Promise<WifiP2pDevice>

获取P2P本端设备信息，使用Promise异步回调。

**需要权限：**

API 11起：ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[WifiP2pDevice](js-apis-wifimanager.md#wifip2pdevice)> | Promise对象。表示本端设备信息。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |

## wifiManager.getP2pLocalDevice

PhonePC/2in1TabletTVWearable

getP2pLocalDevice(callback: AsyncCallback<WifiP2pDevice>): void

获取P2P本端设备信息，使用callback异步回调。

**需要权限：**

API 11起：ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[WifiP2pDevice](js-apis-wifimanager.md#wifip2pdevice)> | 是 | 回调函数。当操作成功时，err为0，data表示本端设备信息。如果error为非0，表示处理出现错误。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |
| 2801001 | Wi-Fi STA disabled. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';
2. // p2p已经建组或者连接成功，才能正常获取到本端设备信息
3. wifiManager.getP2pLocalDevice((err, data:wifiManager.WifiP2pDevice) => {
4. if (err) {
5. console.error("get P2P local device error");
6. return;
7. }
8. console.info("get P2P local device: " + JSON.stringify(data));
9. });

11. wifiManager.getP2pLocalDevice().then(data => {
12. console.info("get P2P local device: " + JSON.stringify(data));
13. });
```

## wifiManager.createGroup

PhonePC/2in1TabletTVWearable

createGroup(config: WifiP2PConfig): void

创建群组。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [WifiP2PConfig](js-apis-wifimanager.md#wifip2pconfig) | 是 | 群组配置信息。如果DeviceAddressType未指定值，则DeviceAddressType默认为随机设备地址类型。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameters. Possible causes: 1. Incorrect parameter types.  2. Parameter verification failed. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |
| 2801001 | Wi-Fi STA disabled. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. try {
4. let config:wifiManager.WifiP2PConfig = {
5. deviceAddress: "****",
6. netId: 0,
7. passphrase: "*****",
8. groupName: "****",
9. goBand: 0
10. }
11. wifiManager.createGroup(config);

13. }catch(error){
14. console.error("failed:" + JSON.stringify(error));
15. }
```

## WifiP2PConfig

PhonePC/2in1TabletTVWearable

表示P2P配置信息。

**系统能力：** SystemCapability.Communication.WiFi.P2P

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceAddress | string | 否 | 否 | 设备地址。 |
| deviceAddressType10+ | [DeviceAddressType](js-apis-wifimanager.md#deviceaddresstype10) | 否 | 是 | 设备地址类型。 |
| netId | number | 否 | 否 | 网络ID。创建群组时-1表示创建临时组，-2表示创建永久组。 |
| passphrase | string | 否 | 否 | 群组密钥。 |
| groupName | string | 否 | 否 | 群组名称。 |
| goBand | [GroupOwnerBand](js-apis-wifimanager.md#groupownerband) | 否 | 否 | 群组带宽。 |
| goFreq23+ | number | 否 | 是 | 群组频率，若群组带宽和群组频率同时添加的情况下，当频率合法时（频率在2400MHz-2500MHz或者4900MHz-5900MHz范围内认为合法），以频率为准，否则以带宽为准。 |

## GroupOwnerBand

PhonePC/2in1TabletTVWearable

表示群组带宽的枚举。

**系统能力：** SystemCapability.Communication.WiFi.P2P

| 名称 | 值 | 说明 |
| --- | --- | --- |
| GO\_BAND\_AUTO | 0 | 自动模式。 |
| GO\_BAND\_2GHZ | 1 | 2.4GHZ。 |
| GO\_BAND\_5GHZ | 2 | 5GHZ。 |

## wifiManager.removeGroup

PhonePC/2in1TabletTVWearable

removeGroup(): void

移除群组。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |
| 2801001 | Wi-Fi STA disabled. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. try {
4. wifiManager.removeGroup();
5. }catch(error){
6. console.error("failed:" + JSON.stringify(error));
7. }
```

## wifiManager.p2pConnect

PhonePC/2in1TabletTVWearable

p2pConnect(config: WifiP2PConfig): void

执行P2P连接。

**需要权限：**

API 10起：ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [WifiP2PConfig](js-apis-wifimanager.md#wifip2pconfig) | 是 | 连接配置信息。如果DeviceAddressType未指定值，则DeviceAddressType默认为随机设备地址类型。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameters. Possible causes: 1. Incorrect parameter types.  2. Parameter verification failed. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |
| 2801001 | Wi-Fi STA disabled. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. let recvP2pConnectionChangeFunc = (result:wifiManager.WifiP2pLinkedInfo) => {
4. console.info("p2p connection change receive event: " + JSON.stringify(result));
5. wifiManager.getP2pLinkedInfo((err, data:wifiManager.WifiP2pLinkedInfo) => {
6. if (err) {
7. console.error('failed to get getP2pLinkedInfo: ' + JSON.stringify(err));
8. return;
9. }
10. console.info("get getP2pLinkedInfo: " + JSON.stringify(data));
11. });
12. }
13. wifiManager.on("p2pConnectionChange", recvP2pConnectionChangeFunc);

15. let recvP2pDeviceChangeFunc = (result:wifiManager.WifiP2pDevice) => {
16. console.info("p2p device change receive event: " + JSON.stringify(result));
17. }
18. wifiManager.on("p2pDeviceChange", recvP2pDeviceChangeFunc);

20. let recvP2pPeerDeviceChangeFunc = (result:wifiManager.WifiP2pDevice[]) => {
21. console.info("p2p peer device change receive event: " + JSON.stringify(result));
22. wifiManager.getP2pPeerDevices((err, data:wifiManager.WifiP2pDevice[]) => {
23. if (err) {
24. console.error('failed to get peer devices: ' + JSON.stringify(err));
25. return;
26. }
27. console.info("get peer devices: " + JSON.stringify(data));
28. let len = data.length;
29. for (let i = 0; i < len; ++i) {
30. if (data[i].deviceName === "my_test_device") {
31. console.info("p2p connect to test device: " + data[i].deviceAddress);
32. let config:wifiManager.WifiP2PConfig = {
33. deviceAddress:data[i].deviceAddress,
34. netId:-2,
35. passphrase:"",
36. groupName:"",
37. goBand:0,
38. }
39. wifiManager.p2pConnect(config);
40. }
41. }
42. });
43. }
44. wifiManager.on("p2pPeerDeviceChange", recvP2pPeerDeviceChangeFunc);

46. let recvP2pPersistentGroupChangeFunc = () => {
47. console.info("p2p persistent group change receive event");

49. wifiManager.getCurrentGroup((err, data:wifiManager.WifiP2pGroupInfo) => {
50. if (err) {
51. console.error('failed to get current group: ' + JSON.stringify(err));
52. return;
53. }
54. console.info("get current group: " + JSON.stringify(data));
55. });
56. }
57. wifiManager.on("p2pPersistentGroupChange", recvP2pPersistentGroupChangeFunc);

59. setTimeout(() => {wifiManager.off("p2pConnectionChange", recvP2pConnectionChangeFunc);}, 125 * 1000);
60. setTimeout(() =>  {wifiManager.off("p2pDeviceChange", recvP2pDeviceChangeFunc);}, 125 * 1000);
61. setTimeout(() =>  {wifiManager.off("p2pPeerDeviceChange", recvP2pPeerDeviceChangeFunc);}, 125 * 1000);
62. setTimeout(() =>  {wifiManager.off("p2pPersistentGroupChange", recvP2pPersistentGroupChangeFunc);}, 125 * 1000);
63. console.info("start discover devices -> " + wifiManager.startDiscoverDevices());
```

## wifiManager.p2pCancelConnect

PhonePC/2in1TabletTVWearable

p2pCancelConnect(): void

在P2P连接过程中，取消P2P连接。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |
| 2801001 | Wi-Fi STA disabled. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. try {
4. wifiManager.p2pCancelConnect();
5. }catch(error){
6. console.error("failed:" + JSON.stringify(error));
7. }
```

## wifiManager.startDiscoverDevices

PhonePC/2in1TabletTVWearable

startDiscoverDevices(): void

开始发现设备。

**需要权限：**

API 10起：ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |
| 2801001 | Wi-Fi STA disabled. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. try {
4. wifiManager.startDiscoverDevices();
5. }catch(error){
6. console.error("failed:" + JSON.stringify(error));
7. }
```

## wifiManager.stopDiscoverDevices

PhonePC/2in1TabletTVWearable

stopDiscoverDevices(): void

停止发现设备。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |
| 2801001 | Wi-Fi STA disabled. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. try {
4. wifiManager.stopDiscoverDevices();
5. }catch(error){
6. console.error("failed:" + JSON.stringify(error));
7. }
```

## wifiManager.getMultiLinkedInfo18+

PhonePC/2in1TabletTVWearable

getMultiLinkedInfo(): Array<WifiLinkedInfo>

获取MLO(Multi-Link Operation，多链路操作)WLAN连接信息。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

说明

* 当macType是1（设备MAC地址），获取macAddress还需申请ohos.permission.GET\_WIFI\_LOCAL\_MAC权限（API8-15仅面向系统应用开放。从API 16开始，在PC/2in1设备上面向普通应用开放，在其余设备上仍仅面向系统应用开放），无该权限时，macAddress返回为空。
* 如果应用申请了ohos.permission.GET\_WIFI\_PEERS\_MAC权限，则返回结果中的bssid为真实BSSID地址，否则为随机设备地址。

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[WifiLinkedInfo](js-apis-wifimanager.md#wifilinkedinfo)> | Wi-Fi连接信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |
| 2501001 | Wi-Fi STA disabled. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. try {
4. let linkedInfo = wifiManager.getMultiLinkedInfo();
5. console.info("linkedInfo:" + JSON.stringify(linkedInfo));
6. }catch(error){
7. console.error("failed:" + JSON.stringify(error));
8. }
```

## WifiP2pGroupInfo

PhonePC/2in1TabletTVWearable

表示P2P群组相关信息。

**系统能力：** SystemCapability.Communication.WiFi.P2P

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isP2pGo | boolean | 否 | 否 | 是否是群主。true表示是群主，false表示不是群主。 |
| ownerInfo | [WifiP2pDevice](js-apis-wifimanager.md#wifip2pdevice) | 否 | 否 | 群组的设备信息。 |
| passphrase | string | 否 | 否 | 群组密钥。 |
| interface | string | 否 | 否 | 接口名称。 |
| groupName | string | 否 | 否 | 群组名称。 |
| networkId | number | 否 | 否 | 网络ID。 |
| frequency | number | 否 | 否 | 群组的频率。 |
| clientDevices | [WifiP2pDevice[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifip2pdevice) | 否 | 否 | 接入的设备列表信息。 |
| goIpAddress | string | 否 | 否 | 群组IP地址。 |

## wifiManager.on('wifiStateChange')

PhonePC/2in1TabletTVWearable

on(type: 'wifiStateChange', callback: Callback<number>): void

注册WLAN状态改变事件，在业务退出时，要调用off(type: 'wifiStateChange', callback?: Callback<number>)接口去掉之前的注册回调。使用callback异步回调。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"wifiStateChange"字符串。 |
| callback | Callback<number> | 是 | 状态改变回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**状态改变事件的枚举：**

| 枚举值 | 说明 |
| --- | --- |
| 0 | 未激活。 |
| 1 | 已激活。 |
| 2 | 激活中。 |
| 3 | 去激活中。 |

## wifiManager.off('wifiStateChange')

PhonePC/2in1TabletTVWearable

off(type: 'wifiStateChange', callback?: Callback<number>): void

取消注册WLAN状态改变事件。使用callback异步回调。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"wifiStateChange"字符串。 |
| callback | Callback<number> | 否 | 状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. let recvPowerNotifyFunc = (result:number) => {
4. console.info("Receive power state change event: " + result);
5. }

7. // Register event
8. wifiManager.on("wifiStateChange", recvPowerNotifyFunc);

10. // Unregister event
11. wifiManager.off("wifiStateChange", recvPowerNotifyFunc);
```

## wifiManager.on('wifiConnectionChange')

PhonePC/2in1TabletTVWearable

on(type: 'wifiConnectionChange', callback: Callback<number>): void

注册WLAN连接状态改变事件，在业务退出时，要调用off(type: 'wifiConnectionChange', callback?: Callback<number>)接口去掉之前的注册回调。使用callback异步回调。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"wifiConnectionChange"字符串。 |
| callback | Callback<number> | 是 | 状态改变回调函数。 |

**连接状态改变事件的枚举：**

| 枚举值 | 说明 |
| --- | --- |
| 0 | 已断开。 |
| 1 | 已连接。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

## wifiManager.off('wifiConnectionChange')

PhonePC/2in1TabletTVWearable

off(type: 'wifiConnectionChange', callback?: Callback<number>): void

取消注册WLAN连接状态改变事件。使用callback异步回调。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"wifiConnectionChange"字符串。 |
| callback | Callback<number> | 否 | 连接状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. let recvWifiConnectionChangeFunc = (result:number) => {
4. console.info("Receive wifi connection change event: " + result);
5. }

7. // Register event
8. wifiManager.on("wifiConnectionChange", recvWifiConnectionChangeFunc);

10. // Unregister event
11. wifiManager.off("wifiConnectionChange", recvWifiConnectionChangeFunc);
```

## wifiManager.on('wifiScanStateChange')

PhonePC/2in1TabletTVWearable

on(type: 'wifiScanStateChange', callback: Callback<number>): void

注册扫描状态改变事件，在业务退出时，要调用off(type: 'wifiScanStateChange', callback?: Callback<number>)接口去掉之前的注册回调。使用callback异步回调。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"wifiScanStateChange"字符串。 |
| callback | Callback<number> | 是 | 状态改变回调函数。 |

**扫描状态改变事件的枚举：**

| 枚举值 | 说明 |
| --- | --- |
| 0 | 扫描失败。 |
| 1 | 扫描成功。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

## wifiManager.off('wifiScanStateChange')

PhonePC/2in1TabletTVWearable

off(type: 'wifiScanStateChange', callback?: Callback<number>): void

取消注册扫描状态改变事件。使用callback异步回调。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"wifiScanStateChange"字符串。 |
| callback | Callback<number> | 否 | 状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. let recvWifiScanStateChangeFunc = (result:number) => {
4. console.info("Receive Wifi scan state change event: " + result);
5. }

7. // Register event
8. wifiManager.on("wifiScanStateChange", recvWifiScanStateChangeFunc);

10. // Unregister event
11. wifiManager.off("wifiScanStateChange", recvWifiScanStateChangeFunc);
```

## wifiManager.on('wifiRssiChange')

PhonePC/2in1TabletTVWearable

on(type: 'wifiRssiChange', callback: Callback<number>): void

注册WLAN接收信号强度(RSSI)变化事件，在业务退出时，要调用off(type: 'wifiRssiChange', callback?: Callback<number>)接口去掉之前的注册回调。使用callback异步回调。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"wifiRssiChange"字符串。 |
| callback | Callback<number> | 是 | 状态改变回调函数，返回以dBm为单位的RSSI值。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

## wifiManager.off('wifiRssiChange')

PhonePC/2in1TabletTVWearable

off(type: 'wifiRssiChange', callback?: Callback<number>): void

取消注册WLAN接收信号强度(RSSI)变化事件。使用callback异步回调。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"wifiRssiChange"字符串。 |
| callback | Callback<number> | 否 | 状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. let recvWifiRssiChangeFunc = (result:number) => {
4. console.info("Receive wifi rssi change event: " + result);
5. }

7. // Register event
8. wifiManager.on("wifiRssiChange", recvWifiRssiChangeFunc);

10. // Unregister event
11. wifiManager.off("wifiRssiChange", recvWifiRssiChangeFunc);
```

## wifiManager.on('hotspotStateChange')

PhonePC/2in1TabletTVWearable

on(type: 'hotspotStateChange', callback: Callback<number>): void

注册热点状态改变事件，在业务退出时，要调用off(type: 'hotspotStateChange', callback?: Callback<number>)接口去掉之前的注册回调。使用callback异步回调。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.AP.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"hotspotStateChange"字符串。 |
| callback | Callback<number> | 是 | 状态改变回调函数。 |

**热点状态改变事件的枚举：**

| 枚举值 | 说明 |
| --- | --- |
| 0 | 未激活。 |
| 1 | 已激活。 |
| 2 | 激活中。 |
| 3 | 去激活中。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2601000 | Operation failed. |

## wifiManager.off('hotspotStateChange')

PhonePC/2in1TabletTVWearable

off(type: 'hotspotStateChange', callback?: Callback<number>): void

取消注册热点状态改变事件。使用callback异步回调。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.AP.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"hotspotStateChange"字符串。 |
| callback | Callback<number> | 否 | 状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2601000 | Operation failed. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. let recvHotspotStateChangeFunc = (result:number) => {
4. console.info("Receive hotspot state change event: " + result);
5. }

7. // Register event
8. wifiManager.on("hotspotStateChange", recvHotspotStateChangeFunc);

10. // Unregister event
11. wifiManager.off("hotspotStateChange", recvHotspotStateChangeFunc);
```

## wifiManager.on('p2pStateChange')

PhonePC/2in1TabletTVWearable

on(type: 'p2pStateChange', callback: Callback<number>): void

注册P2P开关状态改变事件，在业务退出时，要调用off(type: 'p2pStateChange', callback?: Callback<number>)接口去掉之前的注册回调。使用callback异步回调。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"p2pStateChange"字符串。 |
| callback | Callback<number> | 是 | 状态改变回调函数。 |

**P2P状态改变事件的枚举：**

| 枚举值 | 说明 |
| --- | --- |
| 1 | 空闲。 |
| 2 | 打开中。 |
| 3 | 已打开。 |
| 4 | 关闭中。 |
| 5 | 已关闭。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |

## wifiManager.off('p2pStateChange')

PhonePC/2in1TabletTVWearable

off(type: 'p2pStateChange', callback?: Callback<number>): void

取消注册P2P开关状态改变事件。使用callback异步回调。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"p2pStateChange"字符串。 |
| callback | Callback<number> | 否 | 状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. let recvP2pStateChangeFunc = (result:number) => {
4. console.info("Receive p2p state change event: " + result);
5. }

7. // Register event
8. wifiManager.on("p2pStateChange", recvP2pStateChangeFunc);

10. // Unregister event
11. wifiManager.off("p2pStateChange", recvP2pStateChangeFunc);
```

## wifiManager.on('p2pConnectionChange')

PhonePC/2in1TabletTVWearable

on(type: 'p2pConnectionChange', callback: Callback<WifiP2pLinkedInfo>): void

注册P2P连接状态改变事件，在业务退出时，要调用off(type: 'p2pConnectionChange', callback?: Callback<WifiP2pLinkedInfo>)接口去掉之前的注册回调。使用callback异步回调。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"p2pConnectionChange"字符串。 |
| callback | Callback<[WifiP2pLinkedInfo](js-apis-wifimanager.md#wifip2plinkedinfo)> | 是 | 状态改变回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |

## wifiManager.off('p2pConnectionChange')

PhonePC/2in1TabletTVWearable

off(type: 'p2pConnectionChange', callback?: Callback<WifiP2pLinkedInfo>): void

取消注册P2P连接状态改变事件。使用callback异步回调。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"p2pConnectionChange"字符串。 |
| callback | Callback<[WifiP2pLinkedInfo](js-apis-wifimanager.md#wifip2plinkedinfo)> | 否 | 状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. let recvP2pConnectionChangeFunc = (result:wifiManager.WifiP2pLinkedInfo) => {
4. console.info("Receive p2p connection change event: " + result);
5. }

7. // Register event
8. wifiManager.on("p2pConnectionChange", recvP2pConnectionChangeFunc);

10. // Unregister event
11. wifiManager.off("p2pConnectionChange", recvP2pConnectionChangeFunc);
```

## wifiManager.on('p2pDeviceChange')

PhonePC/2in1TabletTVWearable

on(type: 'p2pDeviceChange', callback: Callback<WifiP2pDevice>): void

注册P2P设备状态改变事件，在业务退出时，要调用off(type: 'p2pDeviceChange', callback?: Callback<WifiP2pDevice>)接口去掉之前的注册回调。使用callback异步回调。

**需要权限：**

API 10起：ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"p2pDeviceChange"字符串。 |
| callback | Callback<[WifiP2pDevice](js-apis-wifimanager.md#wifip2pdevice)> | 是 | 状态改变回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |

## wifiManager.off('p2pDeviceChange')

PhonePC/2in1TabletTVWearable

off(type: 'p2pDeviceChange', callback?: Callback<WifiP2pDevice>): void

取消注册P2P设备状态改变事件。使用callback异步回调。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"p2pDeviceChange"字符串。 |
| callback | Callback<[WifiP2pDevice](js-apis-wifimanager.md#wifip2pdevice)> | 否 | 状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. let recvP2pDeviceChangeFunc = (result:wifiManager.WifiP2pDevice) => {
4. console.info("Receive p2p device change event: " + result);
5. }

7. // Register event
8. wifiManager.on("p2pDeviceChange", recvP2pDeviceChangeFunc);

10. // Unregister event
11. wifiManager.off("p2pDeviceChange", recvP2pDeviceChangeFunc);
```

## wifiManager.on('p2pPeerDeviceChange')

PhonePC/2in1TabletTVWearable

on(type: 'p2pPeerDeviceChange', callback: Callback<WifiP2pDevice[]>): void

注册P2P对端设备状态改变事件，在业务退出时，要调用off(type: 'p2pPeerDeviceChange', callback?: Callback<WifiP2pDevice[]>)接口去掉之前的注册回调。使用callback异步回调。

**需要权限：**

API 10起：ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"p2pPeerDeviceChange"字符串。 |
| callback | Callback<[WifiP2pDevice[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifip2pdevice)> | 是 | 状态改变回调函数。如果应用申请了ohos.permission.GET\_WIFI\_PEERS\_MAC权限，则返回结果中的deviceAddress为真实设备地址，否则为随机设备地址。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |

## wifiManager.off('p2pPeerDeviceChange')

PhonePC/2in1TabletTVWearable

off(type: 'p2pPeerDeviceChange', callback?: Callback<WifiP2pDevice[]>): void

取消注册P2P对端设备状态改变事件。使用callback异步回调。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"p2pPeerDeviceChange"字符串。 |
| callback | Callback<[WifiP2pDevice[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifip2pdevice)> | 否 | 状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。如果应用申请了ohos.permission.GET\_WIFI\_PEERS\_MAC权限，则返回结果中的deviceAddress为真实设备地址，否则为随机设备地址。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. let recvP2pPeerDeviceChangeFunc = (result:wifiManager.WifiP2pDevice[]) => {
4. console.info("Receive p2p peer device change event: " + result);
5. }

7. // Register event
8. wifiManager.on("p2pPeerDeviceChange", recvP2pPeerDeviceChangeFunc);

10. // Unregister event
11. wifiManager.off("p2pPeerDeviceChange", recvP2pPeerDeviceChangeFunc);
```

## wifiManager.on('p2pPersistentGroupChange')

PhonePC/2in1TabletTVWearable

on(type: 'p2pPersistentGroupChange', callback: Callback<void>): void

注册P2P永久组状态改变事件，在业务退出时，要调用off(type: 'p2pPersistentGroupChange', callback?: Callback<void>)接口去掉之前的注册回调。使用callback异步回调。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"p2pPersistentGroupChange"字符串。 |
| callback | Callback<void> | 是 | 状态改变回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |

## wifiManager.off('p2pPersistentGroupChange')

PhonePC/2in1TabletTVWearable

off(type: 'p2pPersistentGroupChange', callback?: Callback<void>): void

取消注册P2P永久组状态改变事件。使用callback异步回调。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"p2pPersistentGroupChange"字符串。 |
| callback | Callback<void> | 否 | 状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. let recvP2pPersistentGroupChangeFunc = (result:void) => {
4. console.info("Receive p2p persistent group change event: " + result);
5. }

7. // Register event
8. wifiManager.on("p2pPersistentGroupChange", recvP2pPersistentGroupChangeFunc);

10. // Unregister event
11. wifiManager.off("p2pPersistentGroupChange", recvP2pPersistentGroupChangeFunc);
```

## wifiManager.on('p2pDiscoveryChange')

PhonePC/2in1TabletTVWearable

on(type: 'p2pDiscoveryChange', callback: Callback<number>): void

注册发现设备状态改变事件，在业务退出时，要调用off(type: 'p2pDiscoveryChange', callback?: Callback<number>)接口去掉之前的注册回调。使用callback异步回调。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"p2pDiscoveryChange"字符串。 |
| callback | Callback<number> | 是 | 状态改变回调函数。 |

**发现设备状态改变事件的枚举：**

| 枚举值 | 说明 |
| --- | --- |
| 0 | 初始状态。 |
| 1 | 发现成功。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |

## wifiManager.off('p2pDiscoveryChange')

PhonePC/2in1TabletTVWearable

off(type: 'p2pDiscoveryChange', callback?: Callback<number>): void

取消注册发现设备状态改变事件。使用callback异步回调。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"p2pDiscoveryChange"字符串。 |
| callback | Callback<number> | 否 | 状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |

**示例：**

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. let recvP2pDiscoveryChangeFunc = (result:number) => {
4. console.info("Receive p2p discovery change event: " + result);
5. }

7. // Register event
8. wifiManager.on("p2pDiscoveryChange", recvP2pDiscoveryChangeFunc);

10. // Unregister event
11. wifiManager.off("p2pDiscoveryChange", recvP2pDiscoveryChangeFunc);
```
