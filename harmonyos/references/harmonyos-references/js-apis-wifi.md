---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifi
title: @ohos.wifi (WLAN)
breadcrumb: API参考 > 系统 > 网络 > Connectivity Kit（短距通信服务） > 已停止维护的接口 > @ohos.wifi (WLAN)
category: harmonyos-references
scraped_at: 2026-04-28T08:08:10+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:42ec39838b49147dfbfae6f4a4ac82d952d4725a16a16cfe3ef8326bc27ddfa9
---

该模块主要提供WLAN基础功能、P2P（peer-to-peer）功能和WLAN消息通知的相应服务，让应用可以通过WLAN和其他设备互联互通。

说明

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API Version 9 开始，该接口不再维护，推荐使用[@ohos.wifiManager (WLAN)](js-apis-wifimanager.md)等相关接口。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import wifi from '@ohos.wifi';
```

## wifi.isWifiActive(deprecated)

PhonePC/2in1TabletTVWearable

isWifiActive(): boolean

查询WLAN是否已使能。

说明

从API version 6开始支持，从API version 9开始废弃。建议使用[wifiManager.isWifiActive](js-apis-wifimanager.md#wifimanageriswifiactive)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true:已使能， false:未使能。 |

**示例：**

```
1. import wifi from '@ohos.wifi';

3. try {
4. let isWifiActive = wifi.isWifiActive();
5. console.info("isWifiActive:" + isWifiActive);
6. }catch(error){
7. console.error("failed:" + JSON.stringify(error));
8. }
```

## wifi.scan(deprecated)

PhonePC/2in1TabletTVWearable

scan(): boolean

启动WLAN扫描。

说明

从API version 6开始支持，从API version 9开始废弃。建议使用[wifiManager.scan](js-apis-wifimanager.md#wifimanagerscandeprecated)替代。

**需要权限：** ohos.permission.SET\_WIFI\_INFO 和 ohos.permission.LOCATION

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true:扫描操作执行成功， false:扫描操作执行失败。 |

**示例：**

```
1. import wifi from '@ohos.wifi';

3. try {
4. wifi.scan();
5. }catch(error){
6. console.error("failed:" + JSON.stringify(error));
7. }
```

## wifi.getScanInfos(deprecated)

PhonePC/2in1TabletTVWearable

getScanInfos(): Promise<Array<WifiScanInfo>>

获取扫描结果，使用Promise异步回调。

说明

从API version 6开始支持，从API version 9开始废弃。建议使用[wifiManager.getScanInfos](js-apis-wifimanager.md#wifimanagergetscaninfolist10)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO 和 (ohos.permission.GET\_WIFI\_PEERS\_MAC 或 ohos.permission.LOCATION)

ohos.permission.GET\_WIFI\_PEERS\_MAC权限仅系统应用可申请。

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise< Array<[WifiScanInfo](js-apis-wifi.md#wifiscaninfodeprecated)> > | Promise对象。返回扫描到的热点列表。 |

## wifi.getScanInfos(deprecated)

PhonePC/2in1TabletTVWearable

getScanInfos(callback: AsyncCallback<Array<WifiScanInfo>>): void

获取扫描结果，使用callback异步回调。

说明

从API version 6开始支持，从API version 9开始废弃。建议使用[wifiManager.getScanInfos](js-apis-wifimanager.md#wifimanagergetscaninfolist10)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO 和 (ohos.permission.GET\_WIFI\_PEERS\_MAC 或 ohos.permission.LOCATION)

ohos.permission.GET\_WIFI\_PEERS\_MAC权限仅系统应用可申请。

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback< Array<[WifiScanInfo](js-apis-wifi.md#wifiscaninfodeprecated)>> | 是 | 回调函数。当成功时，err为0，data为扫描到的热点；否则err为非0值，data为空。 |

**示例：**

```
1. import wifi from '@ohos.wifi';

3. wifi.getScanInfos().then(result => {
4. let len = result.length;
5. console.info("wifi received scan info: " + len);
6. for (let i = 0; i < len; ++i) {
7. console.info("ssid: " + result[i].ssid);
8. console.info("bssid: " + result[i].bssid);
9. console.info("capabilities: " + result[i].capabilities);
10. console.info("securityType: " + result[i].securityType);
11. console.info("rssi: " + result[i].rssi);
12. console.info("band: " + result[i].band);
13. console.info("frequency: " + result[i].frequency);
14. console.info("channelWidth: " + result[i].channelWidth);
15. console.info("timestamp: " + result[i].timestamp);
16. }
17. });
```

## WifiScanInfo(deprecated)

PhonePC/2in1TabletTVWearable

WLAN热点信息。

说明

从API version 6开始支持，从API version 9开始废弃。建议使用[WifiScanInfo](js-apis-wifimanager.md#wifiscaninfo)替代。

**系统能力：** SystemCapability.Communication.WiFi.STA

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| ssid | string | 否 | 否 | 热点的SSID，最大长度为32字节，编码格式为UTF-8。 |
| bssid | string | 否 | 否 | 热点的BSSID，例如：00:11:22:33:44:55。 |
| capabilities | string | 否 | 否 | 热点能力。 |
| securityType | [WifiSecurityType](js-apis-wifi.md#wifisecuritytypedeprecated) | 否 | 否 | WLAN加密类型。 |
| rssi | number | 否 | 否 | 热点的信号强度(dBm)。 |
| band | number | 否 | 否 | WLAN接入点的频段。1表示2.4GHZ；2表示5GHZ。 |
| frequency | number | 否 | 否 | WLAN接入点的频率。 |
| channelWidth | number | 否 | 否 | WLAN接入点的带宽。 |
| timestamp | number | 否 | 否 | 时间戳。 |

## WifiSecurityType(deprecated)

PhonePC/2in1TabletTVWearable

表示加密类型的枚举。

说明

从API version 6开始支持，从API version 9开始废弃。建议使用[WifiSecurityType](js-apis-wifimanager.md#wifisecuritytype)替代。

**系统能力：** SystemCapability.Communication.WiFi.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WIFI\_SEC\_TYPE\_INVALID | 0 | 无效加密类型。 |
| WIFI\_SEC\_TYPE\_OPEN | 1 | 开放加密类型。 |
| WIFI\_SEC\_TYPE\_WEP | 2 | Wired Equivalent Privacy (WEP)加密类型。 |
| WIFI\_SEC\_TYPE\_PSK | 3 | Pre-shared key (PSK)加密类型。 |
| WIFI\_SEC\_TYPE\_SAE | 4 | Simultaneous Authentication of Equals (SAE)加密类型。 |

## WifiDeviceConfig(deprecated)

PhonePC/2in1TabletTVWearable

WLAN配置信息。

说明

从API version 6开始支持，从API version 9开始废弃。建议使用[WifiDeviceConfig](js-apis-wifimanager.md#wifideviceconfig)替代。

**系统能力：** SystemCapability.Communication.WiFi.STA

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| ssid | string | 否 | 否 | 热点的SSID，最大长度为32字节，编码格式为UTF-8。 |
| bssid | string | 否 | 否 | 热点的BSSID，例如：00:11:22:33:44:55。 |
| preSharedKey | string | 否 | 否 | 热点的密钥，最大长度为64字节。 |
| isHiddenSsid | boolean | 否 | 否 | 是否是隐藏网络。true:是隐藏网络，false:不是隐藏网络。 |
| securityType | [WifiSecurityType](js-apis-wifi.md#wifisecuritytypedeprecated) | 否 | 否 | 加密类型。 |

## wifi.addUntrustedConfig(deprecated)

PhonePC/2in1TabletTVWearable

addUntrustedConfig(config: WifiDeviceConfig): Promise<boolean>

添加不可信网络配置，使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.addCandidateConfig](js-apis-wifimanager.md#wifimanageraddcandidateconfig)替代。

**需要权限：** ohos.permission.SET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [WifiDeviceConfig](js-apis-wifi.md#wifideviceconfigdeprecated) | 是 | WLAN配置信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。表示操作结果，true: 成功， false: 失败。 |

**示例：**

```
1. import wifi from '@ohos.wifi';

3. try {
4. let config:wifi.WifiDeviceConfig = {
5. ssid : "****",
6. bssid:  "****",
7. preSharedKey: "****",
8. isHiddenSsid: false,
9. securityType: 0,
10. creatorUid: 0,
11. disableReason: 0,
12. netId: 0,
13. randomMacType: 0,
14. randomMacAddr:  "****",
15. ipType: 0,
16. staticIp: {
17. ipAddress: 0,
18. gateway: 0,
19. dnsServers: [],
20. domains: []
21. }
22. }
23. wifi.addUntrustedConfig(config).then(result => {
24. console.info("result:" + JSON.stringify(result));
25. });
26. }catch(error){
27. console.error("failed:" + JSON.stringify(error));
28. }
```

## wifi.addUntrustedConfig(deprecated)

PhonePC/2in1TabletTVWearable

addUntrustedConfig(config: WifiDeviceConfig, callback: AsyncCallback<boolean>): void

添加不可信网络配置，使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.addCandidateConfig](js-apis-wifimanager.md#wifimanageraddcandidateconfig-1)替代。

**需要权限：** ohos.permission.SET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [WifiDeviceConfig](js-apis-wifi.md#wifideviceconfigdeprecated) | 是 | WLAN配置信息。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当操作成功时，err为0，data表示操作结果，true: 成功， false: 失败。如果error为非0，表示处理出现错误。 |

**示例：**

```
1. import wifi from '@ohos.wifi';

3. try {
4. let config:wifi.WifiDeviceConfig = {
5. ssid : "****",
6. bssid:  "****",
7. preSharedKey: "****",
8. isHiddenSsid: false,
9. securityType: 0,
10. creatorUid: 0,
11. disableReason: 0,
12. netId: 0,
13. randomMacType: 0,
14. randomMacAddr:  "****",
15. ipType: 0,
16. staticIp: {
17. ipAddress: 0,
18. gateway: 0,
19. dnsServers: [],
20. domains: []
21. }
22. }
23. wifi.addUntrustedConfig(config,(error,result) => {
24. console.info("result:" + JSON.stringify(result));
25. });
26. }catch(error){
27. console.error("failed:" + JSON.stringify(error));
28. }
```

## wifi.removeUntrustedConfig(deprecated)

PhonePC/2in1TabletTVWearable

removeUntrustedConfig(config: WifiDeviceConfig): Promise<boolean>

移除不可信网络配置，使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.removeCandidateConfig](js-apis-wifimanager.md#wifimanagerremovecandidateconfig)替代。

**需要权限：** ohos.permission.SET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [WifiDeviceConfig](js-apis-wifi.md#wifideviceconfigdeprecated) | 是 | WLAN配置信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。表示操作结果，true: 成功， false: 失败。 |

**示例：**

```
1. import wifi from '@ohos.wifi';

3. try {
4. let config:wifi.WifiDeviceConfig = {
5. ssid : "****",
6. bssid:  "****",
7. preSharedKey: "****",
8. isHiddenSsid: false,
9. securityType: 0,
10. creatorUid: 0,
11. disableReason: 0,
12. netId: 0,
13. randomMacType: 0,
14. randomMacAddr:  "****",
15. ipType: 0,
16. staticIp: {
17. ipAddress: 0,
18. gateway: 0,
19. dnsServers: [],
20. domains: []
21. }
22. }
23. wifi.removeUntrustedConfig(config).then(result => {
24. console.info("result:" + JSON.stringify(result));
25. });
26. }catch(error){
27. console.error("failed:" + JSON.stringify(error));
28. }
```

## wifi.removeUntrustedConfig(deprecated)

PhonePC/2in1TabletTVWearable

removeUntrustedConfig(config: WifiDeviceConfig, callback: AsyncCallback<boolean>): void

移除不可信网络配置，使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.removeCandidateConfig](js-apis-wifimanager.md#wifimanagerremovecandidateconfig-1)替代。

**需要权限：** ohos.permission.SET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [WifiDeviceConfig](js-apis-wifi.md#wifideviceconfigdeprecated) | 是 | WLAN配置信息。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当操作成功时，err为0，data表示操作结果，true: 成功， false: 失败。如果error为非0，表示处理出现错误。 |

**示例：**

```
1. import wifi from '@ohos.wifi';

3. try {
4. let config:wifi.WifiDeviceConfig = {
5. ssid : "****",
6. bssid:  "****",
7. preSharedKey: "****",
8. isHiddenSsid: false,
9. securityType: 0,
10. creatorUid: 0,
11. disableReason: 0,
12. netId: 0,
13. randomMacType: 0,
14. randomMacAddr:  "****",
15. ipType: 0,
16. staticIp: {
17. ipAddress: 0,
18. gateway: 0,
19. dnsServers: [],
20. domains: []
21. }
22. }
23. wifi.removeUntrustedConfig(config,(error,result) => {
24. console.info("result:" + JSON.stringify(result));
25. });
26. }catch(error){
27. console.error("failed:" + JSON.stringify(error));
28. }
```

## wifi.getSignalLevel(deprecated)

PhonePC/2in1TabletTVWearable

getSignalLevel(rssi: number, band: number): number

查询WLAN信号强度。

说明

从API version 6开始支持，从API version 9开始废弃。建议使用[wifiManager.getSignalLevel](js-apis-wifimanager.md#wifimanagergetsignallevel)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rssi | number | 是 | 热点的信号强度(dBm)。 |
| band | number | 是 | WLAN接入点的频段。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 信号强度，取值范围为[0, 4]。 |

**示例：**

```
1. import wifi from '@ohos.wifi';

3. try {
4. let rssi = 0;
5. let band = 0;
6. let level = wifi.getSignalLevel(rssi,band);
7. console.info("level:" + JSON.stringify(level));
8. }catch(error){
9. console.error("failed:" + JSON.stringify(error));
10. }
```

## wifi.getLinkedInfo(deprecated)

PhonePC/2in1TabletTVWearable

getLinkedInfo(): Promise<WifiLinkedInfo>

获取WLAN连接信息。使用Promise异步回调。

说明

从API version 6开始支持，从API version 9开始废弃。建议使用[wifiManager.getLinkedInfo](js-apis-wifimanager.md#wifimanagergetlinkedinfo)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[WifiLinkedInfo](js-apis-wifi.md#wifilinkedinfodeprecated)> | Promise对象。表示WLAN连接信息。 |

## wifi.getLinkedInfo(deprecated)

PhonePC/2in1TabletTVWearable

getLinkedInfo(callback: AsyncCallback<WifiLinkedInfo>): void

获取WLAN连接信息。使用callback异步回调。

说明

从API version 6开始支持，从API version 9开始废弃。建议使用[wifiManager.getLinkedInfo](js-apis-wifimanager.md#wifimanagergetlinkedinfo-1)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[WifiLinkedInfo](js-apis-wifi.md#wifilinkedinfodeprecated)> | 是 | 回调函数。当获取成功时，err为0，data表示WLAN连接信息。如果error为非0，表示处理出现错误。 |

**示例：**

```
1. import wifi from '@ohos.wifi';

3. wifi.getLinkedInfo((err, data:wifi.WifiLinkedInfo) => {
4. if (err) {
5. console.error("get linked info error");
6. return;
7. }
8. console.info("get wifi linked info: " + JSON.stringify(data));
9. });

11. wifi.getLinkedInfo().then(data => {
12. console.info("get wifi linked info: " + JSON.stringify(data));
13. }).catch((error:number) => {
14. console.info("get linked info error");
15. });
```

## WifiLinkedInfo(deprecated)

PhonePC/2in1TabletTVWearable

提供WLAN连接的相关信息。

说明

从API version 6开始支持，从API version 9开始废弃。建议使用[WifiLinkedInfo](js-apis-wifimanager.md#wifilinkedinfo)替代。

**系统能力：** SystemCapability.Communication.WiFi.STA

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| ssid | string | 否 | 否 | 热点的SSID，最大长度为32字节，编码格式为UTF-8。 |
| bssid | string | 否 | 否 | 热点的BSSID，例如：00:11:22:33:44:55。 |
| rssi | number | 否 | 否 | 热点的信号强度(dBm)。 |
| band | number | 否 | 否 | WLAN接入点的频段。1表示2.4GHZ；2表示5GHZ。 |
| linkSpeed | number | 否 | 否 | WLAN接入点的速度，单位Mbps。 |
| frequency | number | 否 | 否 | WLAN接入点的频率。 |
| isHidden | boolean | 否 | 否 | WLAN接入点是否是隐藏网络。true:是隐藏网络，false:不是隐藏网络。 |
| isRestricted | boolean | 否 | 否 | WLAN接入点是否限制数据量。true: 限制，false:不限制。 |
| macAddress | string | 否 | 否 | 设备的MAC地址。 |
| ipAddress | number | 否 | 否 | WLAN连接的IP地址。 |
| connState | [ConnState](js-apis-wifi.md#connstatedeprecated) | 否 | 否 | WLAN连接状态。 |

## ConnState(deprecated)

PhonePC/2in1TabletTVWearable

表示WLAN连接状态的枚举。

说明

从API version 6开始支持，从API version 9开始废弃。建议使用[ConnState](js-apis-wifimanager.md#connstate)替代。

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

## wifi.isConnected(deprecated)

PhonePC/2in1TabletTVWearable

isConnected(): boolean

查询WLAN是否已连接。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.isConnected](js-apis-wifimanager.md#wifimanagerisconnected)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true:已连接， false:未连接。 |

## wifi.isFeatureSupported(deprecated)

PhonePC/2in1TabletTVWearable

isFeatureSupported(featureId: number): boolean

判断设备是否支持相关WLAN特性。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.isFeatureSupported](js-apis-wifimanager.md#wifimanagerisfeaturesupported)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| featureId | number | 是 | 特性ID值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true:支持， false:不支持。 |

**示例：**

```
1. import wifi from '@ohos.wifi';

3. try {
4. let featureId = 0;
5. let ret = wifi.isFeatureSupported(featureId);
6. console.info("isFeatureSupported:" + ret);
7. }catch(error){
8. console.error("failed:" + JSON.stringify(error));
9. }
```

## wifi.getIpInfo(deprecated)

PhonePC/2in1TabletTVWearable

getIpInfo(): IpInfo

获取IP信息。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.getIpInfo](js-apis-wifimanager.md#wifimanagergetipinfo)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IpInfo](js-apis-wifi.md#ipinfodeprecated) | IP信息。 |

**示例：**

```
1. import wifi from '@ohos.wifi';

3. try {
4. let info = wifi.getIpInfo();
5. console.info("info:" + JSON.stringify(info));
6. }catch(error){
7. console.error("failed:" + JSON.stringify(error));
8. }
```

## IpInfo(deprecated)

PhonePC/2in1TabletTVWearable

IP信息。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.getIpInfo](js-apis-wifimanager.md#wifimanagergetipinfo)替代。

**系统能力：** SystemCapability.Communication.WiFi.AP.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| ipAddress | number | 否 | 否 | IP地址。 |
| gateway | number | 否 | 否 | 网关。 |
| netmask | number | 否 | 否 | 掩码。 |
| primaryDns | number | 否 | 否 | 主DNS服务器IP地址。 |
| secondDns | number | 否 | 否 | 备DNS服务器IP地址。 |
| serverIp | number | 否 | 否 | DHCP服务端IP地址。 |
| leaseDuration | number | 否 | 否 | IP地址租用时长。 |

## wifi.getCountryCode(deprecated)

PhonePC/2in1TabletTVWearable

getCountryCode(): string

获取国家码信息。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.getCountryCode](js-apis-wifimanager.md#wifimanagergetcountrycode)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 国家码。 |

**示例：**

```
1. import wifi from '@ohos.wifi';

3. try {
4. let code = wifi.getCountryCode();
5. console.info("code:" + code);
6. }catch(error){
7. console.error("failed:" + JSON.stringify(error));
8. }
```

## wifi.getP2pLinkedInfo(deprecated)

PhonePC/2in1TabletTVWearable

getP2pLinkedInfo(): Promise<WifiP2pLinkedInfo>

获取P2P连接信息。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.getP2pLinkedInfo](js-apis-wifimanager.md#wifimanagergetp2plinkedinfo)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[WifiP2pLinkedInfo](js-apis-wifi.md#wifip2plinkedinfodeprecated)> | Promise对象。表示P2P连接信息。 |

## WifiP2pLinkedInfo(deprecated)

PhonePC/2in1TabletTVWearable

提供WLAN连接的相关信息。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[WifiP2pLinkedInfo](js-apis-wifimanager.md#wifip2plinkedinfo)替代。

**系统能力：** SystemCapability.Communication.WiFi.P2P

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| connectState | [P2pConnectState](js-apis-wifi.md#p2pconnectstatedeprecated) | 否 | 否 | P2P连接状态。 |
| isGroupOwner | boolean | 否 | 否 | 是否是群主。true:是群主，false:不是群主。 |
| groupOwnerAddr | string | 否 | 否 | 群组MAC地址。 |

## P2pConnectState(deprecated)

PhonePC/2in1TabletTVWearable

表示P2P连接状态的枚举。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[P2pConnectState](js-apis-wifimanager.md#p2pconnectstate)替代。

**系统能力：** SystemCapability.Communication.WiFi.P2P

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DISCONNECTED | 0 | 断开状态。 |
| CONNECTED | 1 | 连接状态。 |

## wifi.getP2pLinkedInfo(deprecated)

PhonePC/2in1TabletTVWearable

getP2pLinkedInfo(callback: AsyncCallback<WifiP2pLinkedInfo>): void

获取P2P连接信息。使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.getP2pLinkedInfo](js-apis-wifimanager.md#wifimanagergetp2plinkedinfo-1)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[WifiP2pLinkedInfo](js-apis-wifi.md#wifip2plinkedinfodeprecated)> | 是 | 回调函数。当操作成功时，err为0，data表示P2P连接信息。如果error为非0，表示处理出现错误。 |

**示例：**

```
1. import wifi from '@ohos.wifi';

3. wifi.getP2pLinkedInfo((err, data:wifi.WifiP2pLinkedInfo) => {
4. if (err) {
5. console.error("get p2p linked info error");
6. return;
7. }
8. console.info("get wifi p2p linked info: " + JSON.stringify(data));
9. });

11. wifi.getP2pLinkedInfo().then(data => {
12. console.info("get wifi p2p linked info: " + JSON.stringify(data));
13. });
```

## wifi.getCurrentGroup(deprecated)

PhonePC/2in1TabletTVWearable

getCurrentGroup(): Promise<WifiP2pGroupInfo>

获取P2P当前组信息。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.getCurrentGroup](js-apis-wifimanager.md#wifimanagergetcurrentgroup)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO 和 ohos.permission.LOCATION

**系统能力：** SystemCapability.Communication.WiFi.P2P

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[WifiP2pGroupInfo](js-apis-wifi.md#wifip2pgroupinfodeprecated)> | Promise对象。表示当前组信息。 |

## wifi.getCurrentGroup(deprecated)

PhonePC/2in1TabletTVWearable

getCurrentGroup(callback: AsyncCallback<WifiP2pGroupInfo>): void

获取P2P当前组信息。使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.getCurrentGroup](js-apis-wifimanager.md#wifimanagergetcurrentgroup-1)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO 和 ohos.permission.LOCATION

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[WifiP2pGroupInfo](js-apis-wifi.md#wifip2pgroupinfodeprecated)> | 是 | 回调函数。当操作成功时，err为0，data表示当前组信息。如果error为非0，表示处理出现错误。 |

**示例：**

```
1. import wifi from '@ohos.wifi';

3. wifi.getCurrentGroup((err, data:wifi.WifiP2pGroupInfo) => {
4. if (err) {
5. console.error("get current P2P group error");
6. return;
7. }
8. console.info("get current P2P group: " + JSON.stringify(data));
9. });

11. wifi.getCurrentGroup().then(data => {
12. console.info("get current P2P group: " + JSON.stringify(data));
13. });
```

## wifi.getP2pPeerDevices(deprecated)

PhonePC/2in1TabletTVWearable

getP2pPeerDevices(): Promise<WifiP2pDevice[]>

获取P2P对端设备列表信息。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.getP2pPeerDevices](js-apis-wifimanager.md#wifimanagergetp2ppeerdevices)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO 和 ohos.permission.LOCATION

**系统能力：** SystemCapability.Communication.WiFi.P2P

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[WifiP2pDevice[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifi#wifip2pdevicedeprecated)> | Promise对象。表示对端设备列表信息。 |

## wifi.getP2pPeerDevices(deprecated)

PhonePC/2in1TabletTVWearable

getP2pPeerDevices(callback: AsyncCallback<WifiP2pDevice[]>): void

获取P2P对端设备列表信息。使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.getP2pPeerDevices](js-apis-wifimanager.md#wifimanagergetp2ppeerdevices-1)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO 和 ohos.permission.LOCATION

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[WifiP2pDevice[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifi#wifip2pdevicedeprecated)> | 是 | 回调函数。当操作成功时，err为0，data表示对端设备列表信息。如果error为非0，表示处理出现错误。 |

**示例：**

```
1. import wifi from '@ohos.wifi';

3. wifi.getP2pPeerDevices((err, data:wifi.WifiP2pDevice) => {
4. if (err) {
5. console.error("get P2P peer devices error");
6. return;
7. }
8. console.info("get P2P peer devices: " + JSON.stringify(data));
9. });

11. wifi.getP2pPeerDevices().then(data => {
12. console.info("get P2P peer devices: " + JSON.stringify(data));
13. });
```

## WifiP2pDevice(deprecated)

PhonePC/2in1TabletTVWearable

表示P2P设备信息。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[WifiP2pDevice](js-apis-wifimanager.md#wifip2pdevice)替代。

**系统能力：** SystemCapability.Communication.WiFi.P2P

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceName | string | 否 | 否 | 设备名称。 |
| deviceAddress | string | 否 | 否 | 设备MAC地址。 |
| primaryDeviceType | string | 否 | 否 | 主设备类型。 |
| deviceStatus | [P2pDeviceStatus](js-apis-wifi.md#p2pdevicestatusdeprecated) | 否 | 否 | 设备状态。 |
| groupCapabilitys | number | 否 | 否 | 群组能力。 |

## P2pDeviceStatus(deprecated)

PhonePC/2in1TabletTVWearable

表示设备状态的枚举。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[P2pDeviceStatus](js-apis-wifimanager.md#p2pdevicestatus)替代。

**系统能力：** SystemCapability.Communication.WiFi.P2P

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CONNECTED | 0 | 连接状态。 |
| INVITED | 1 | 邀请状态。 |
| FAILED | 2 | 失败状态。 |
| AVAILABLE | 3 | 可用状态。 |
| UNAVAILABLE | 4 | 不可用状态。 |

## wifi.createGroup(deprecated)

PhonePC/2in1TabletTVWearable

createGroup(config: WifiP2PConfig): boolean

创建群组。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.createGroup](js-apis-wifimanager.md#wifimanagercreategroup)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [WifiP2PConfig](js-apis-wifi.md#wifip2pconfigdeprecated) | 是 | 群组配置信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true:创建群组操作执行成功， false:创建群组操作执行失败。 |

**示例：**

```
1. import wifi from '@ohos.wifi';

3. try {
4. let config:wifi.WifiP2PConfig = {
5. deviceAddress: "****",
6. netId: 0,
7. passphrase: "*****",
8. groupName: "****",
9. goBand: 0
10. }
11. wifi.createGroup(config);

13. }catch(error){
14. console.error("failed:" + JSON.stringify(error));
15. }
```

## WifiP2PConfig(deprecated)

PhonePC/2in1TabletTVWearable

表示P2P配置信息。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[WifiP2PConfig](js-apis-wifimanager.md#wifip2pconfig)替代。

**系统能力：** SystemCapability.Communication.WiFi.P2P

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceAddress | string | 否 | 否 | 设备地址。 |
| netId | number | 否 | 否 | 网络ID。创建群组时-1表示创建临时组，-2表示创建永久组。 |
| passphrase | string | 否 | 否 | 群组密钥。 |
| groupName | string | 否 | 否 | 群组名称。 |
| goBand | [GroupOwnerBand](js-apis-wifi.md#groupownerbanddeprecated) | 否 | 否 | 群组带宽。 |

## GroupOwnerBand(deprecated)

PhonePC/2in1TabletTVWearable

表示群组带宽的枚举。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[GroupOwnerBand](js-apis-wifimanager.md#groupownerband)替代。

**系统能力：** SystemCapability.Communication.WiFi.P2P

| 名称 | 值 | 说明 |
| --- | --- | --- |
| GO\_BAND\_AUTO | 0 | 自动模式。 |
| GO\_BAND\_2GHZ | 1 | 2GHZ。 |
| GO\_BAND\_5GHZ | 2 | 5GHZ。 |

## wifi.removeGroup(deprecated)

PhonePC/2in1TabletTVWearable

removeGroup(): boolean

移除群组。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.removeGroup](js-apis-wifimanager.md#wifimanagerremovegroup)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true:操作执行成功， false:操作执行失败。 |

**示例：**

```
1. import wifi from '@ohos.wifi';

3. try {
4. wifi.removeGroup();
5. }catch(error){
6. console.error("failed:" + JSON.stringify(error));
7. }
```

## wifi.p2pConnect(deprecated)

PhonePC/2in1TabletTVWearable

p2pConnect(config: WifiP2PConfig): boolean

执行P2P连接。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.p2pConnect](js-apis-wifimanager.md#wifimanagerp2pconnect)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO 和 ohos.permission.LOCATION

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [WifiP2PConfig](js-apis-wifi.md#wifip2pconfigdeprecated) | 是 | 连接配置信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true:操作执行成功， false:操作执行失败。 |

**示例：**

```
1. import wifi from '@ohos.wifi';

3. let recvP2pConnectionChangeFunc = (result:wifi.WifiP2pLinkedInfo) => {
4. console.info("p2p connection change receive event: " + JSON.stringify(result));
5. wifi.getP2pLinkedInfo((err, data:wifi.WifiP2pLinkedInfo) => {
6. if (err) {
7. console.error('failed to get getP2pLinkedInfo: ' + JSON.stringify(err));
8. return;
9. }
10. console.info("get getP2pLinkedInfo: " + JSON.stringify(data));
11. });
12. }
13. wifi.on("p2pConnectionChange", recvP2pConnectionChangeFunc);

15. let recvP2pDeviceChangeFunc = (result:wifi.WifiP2pDevice) => {
16. console.info("p2p device change receive event: " + JSON.stringify(result));
17. }
18. wifi.on("p2pDeviceChange", recvP2pDeviceChangeFunc);

20. let recvP2pPeerDeviceChangeFunc = (result:wifi.WifiP2pDevice[]) => {
21. console.info("p2p peer device change receive event: " + JSON.stringify(result));
22. wifi.getP2pPeerDevices((err, data:wifi.WifiP2pDevice[]) => {
23. if (err) {
24. console.error('failed to get peer devices: ' + JSON.stringify(err));
25. return;
26. }
27. console.info("get peer devices: " + JSON.stringify(data));
28. let len = data.length;
29. for (let i = 0; i < len; ++i) {
30. if (data[i].deviceName === "my_test_device") {
31. console.info("p2p connect to test device: " + data[i].deviceAddress);
32. let config:wifi.WifiP2PConfig = {
33. deviceAddress:data[i].deviceAddress,
34. netId:-2,
35. passphrase:"",
36. groupName:"",
37. goBand:0,
38. }
39. wifi.p2pConnect(config);
40. }
41. }
42. });
43. }
44. wifi.on("p2pPeerDeviceChange", recvP2pPeerDeviceChangeFunc);

46. let recvP2pPersistentGroupChangeFunc = () => {
47. console.info("p2p persistent group change receive event");

49. wifi.getCurrentGroup((err, data:wifi.WifiP2pGroupInfo) => {
50. if (err) {
51. console.error('failed to get current group: ' + JSON.stringify(err));
52. return;
53. }
54. console.info("get current group: " + JSON.stringify(data));
55. });
56. }
57. wifi.on("p2pPersistentGroupChange", recvP2pPersistentGroupChangeFunc);

59. setTimeout(() => {wifi.off("p2pConnectionChange", recvP2pConnectionChangeFunc);}, 125 * 1000);
60. setTimeout(() => {wifi.off("p2pDeviceChange", recvP2pDeviceChangeFunc);}, 125 * 1000);
61. setTimeout(() => {wifi.off("p2pPeerDeviceChange", recvP2pPeerDeviceChangeFunc);}, 125 * 1000);
62. setTimeout(() => {wifi.off("p2pPersistentGroupChange", recvP2pPersistentGroupChangeFunc);}, 125 * 1000);
63. console.info("start discover devices -> " + wifi.startDiscoverDevices());
```

## wifi.p2pCancelConnect(deprecated)

PhonePC/2in1TabletTVWearable

p2pCancelConnect(): boolean

取消P2P连接。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.p2pCancelConnect](js-apis-wifimanager.md#wifimanagerp2pcancelconnect)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true:操作执行成功， false:操作执行失败。 |

**示例：**

```
1. import wifi from '@ohos.wifi';

3. try {
4. wifi.p2pCancelConnect();
5. }catch(error){
6. console.error("failed:" + JSON.stringify(error));
7. }
```

## wifi.startDiscoverDevices(deprecated)

PhonePC/2in1TabletTVWearable

startDiscoverDevices(): boolean

开始发现设备。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.startDiscoverDevices](js-apis-wifimanager.md#wifimanagerstartdiscoverdevices)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO 和 ohos.permission.LOCATION

**系统能力：** SystemCapability.Communication.WiFi.P2P

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true:操作执行成功， false:操作执行失败。 |

**示例：**

```
1. import wifi from '@ohos.wifi';

3. try {
4. wifi.startDiscoverDevices();
5. }catch(error){
6. console.error("failed:" + JSON.stringify(error));
7. }
```

## wifi.stopDiscoverDevices(deprecated)

PhonePC/2in1TabletTVWearable

stopDiscoverDevices(): boolean

停止发现设备。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.stopDiscoverDevices](js-apis-wifimanager.md#wifimanagerstopdiscoverdevices)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true:操作执行成功 false:操作执行失败。 |

**示例：**

```
1. import wifi from '@ohos.wifi';

3. try {
4. wifi.stopDiscoverDevices();
5. }catch(error){
6. console.error("failed:" + JSON.stringify(error));
7. }
```

## WifiP2pGroupInfo(deprecated)

PhonePC/2in1TabletTVWearable

表示P2P群组相关信息。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[WifiP2pGroupInfo](js-apis-wifimanager.md#wifip2pgroupinfo)替代。

**系统能力：** SystemCapability.Communication.WiFi.P2P

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isP2pGo | boolean | 否 | 否 | 是否是群主。true:是群主，false:不是群主。 |
| ownerInfo | [WifiP2pDevice](js-apis-wifi.md#wifip2pdevicedeprecated) | 否 | 否 | 群组的设备信息。 |
| passphrase | string | 否 | 否 | 群组密钥。 |
| interface | string | 否 | 否 | 接口名称。 |
| groupName | string | 否 | 否 | 群组名称。 |
| networkId | number | 否 | 否 | 网络ID。 |
| frequency | number | 否 | 否 | 群组的频率。 |
| clientDevices | [WifiP2pDevice[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifi#wifip2pdevicedeprecated) | 否 | 否 | 接入的设备列表信息。 |
| goIpAddress | string | 否 | 否 | 群组IP地址。 |

## wifi.on('wifiStateChange')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'wifiStateChange', callback: Callback<number>): void

注册WLAN状态改变事件。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.on](js-apis-wifimanager.md#wifimanageronwifistatechange)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"wifiStateChange"字符串。 |
| callback | Callback<number> | 是 | 状态改变回调函数。 |

**状态改变事件的枚举：**

| 枚举值 | 说明 |
| --- | --- |
| 0 | 未激活。 |
| 1 | 已激活。 |
| 2 | 激活中。 |
| 3 | 去激活中。 |

## wifi.off('wifiStateChange')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'wifiStateChange', callback?: Callback<number>): void

取消注册WLAN状态改变事件。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.off](js-apis-wifimanager.md#wifimanageroffwifistatechange)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"wifiStateChange"字符串。 |
| callback | Callback<number> | 否 | 状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。 |

**示例：**

```
1. import wifi from '@ohos.wifi';

3. let recvPowerNotifyFunc = (result:number) => {
4. console.info("Receive power state change event: " + result);
5. }

7. // Register event
8. wifi.on("wifiStateChange", recvPowerNotifyFunc);

10. // Unregister event
11. wifi.off("wifiStateChange", recvPowerNotifyFunc);
```

## wifi.on('wifiConnectionChange')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'wifiConnectionChange', callback: Callback<number>): void

注册WLAN连接状态改变事件。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.on](js-apis-wifimanager.md#wifimanageronwificonnectionchange)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

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

## wifi.off('wifiConnectionChange')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'wifiConnectionChange', callback?: Callback<number>): void

取消注册WLAN连接状态改变事件。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.off](js-apis-wifimanager.md#wifimanageroffwificonnectionchange)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"wifiConnectionChange"字符串。 |
| callback | Callback<number> | 否 | 连接状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。 |

**示例：**

```
1. import wifi from '@ohos.wifi';

3. let recvWifiConnectionChangeFunc = (result:number) => {
4. console.info("Receive wifi connection change event: " + result);
5. }

7. // Register event
8. wifi.on("wifiConnectionChange", recvWifiConnectionChangeFunc);

10. // Unregister event
11. wifi.off("wifiConnectionChange", recvWifiConnectionChangeFunc);
```

## wifi.on('wifiScanStateChange')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'wifiScanStateChange', callback: Callback<number>): void

注册扫描状态改变事件。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.on](js-apis-wifimanager.md#wifimanageronwifiscanstatechange)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

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

## wifi.off('wifiScanStateChange')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'wifiScanStateChange', callback?: Callback<number>): void

取消注册扫描状态改变事件。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.off](js-apis-wifimanager.md#wifimanageroffwifiscanstatechange)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"wifiScanStateChange"字符串。 |
| callback | Callback<number> | 否 | 状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。 |

**示例：**

```
1. import wifi from '@ohos.wifi';

3. let recvWifiScanStateChangeFunc = (result:number) => {
4. console.info("Receive Wifi scan state change event: " + result);
5. }

7. // Register event
8. wifi.on("wifiScanStateChange", recvWifiScanStateChangeFunc);

10. // Unregister event
11. wifi.off("wifiScanStateChange", recvWifiScanStateChangeFunc);
```

## wifi.on('wifiRssiChange')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'wifiRssiChange', callback: Callback<number>): void

注册RSSI状态改变事件。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.on](js-apis-wifimanager.md#wifimanageronwifirssichange)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"wifiRssiChange"字符串。 |
| callback | Callback<number> | 是 | 状态改变回调函数，返回以dBm为单位的RSSI值。 |

## wifi.off('wifiRssiChange')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'wifiRssiChange', callback?: Callback<number>): void

取消注册RSSI状态改变事件。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.off](js-apis-wifimanager.md#wifimanageroffwifirssichange)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"wifiRssiChange"字符串。 |
| callback | Callback<number> | 否 | 状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。 |

**示例：**

```
1. import wifi from '@ohos.wifi';

3. let recvWifiRssiChangeFunc = (result:number) => {
4. console.info("Receive wifi rssi change event: " + result);
5. }

7. // Register event
8. wifi.on("wifiRssiChange", recvWifiRssiChangeFunc);

10. // Unregister event
11. wifi.off("wifiRssiChange", recvWifiRssiChangeFunc);
```

## wifi.on('hotspotStateChange')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'hotspotStateChange', callback: Callback<number>): void

注册热点状态改变事件。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.on](js-apis-wifimanager.md#wifimanageronhotspotstatechange)替代。

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

**示例：**

```
1. import wifi from '@ohos.wifi';

3. let recvHotspotStateChangeFunc = (result:number) => {
4. console.info("Receive hotspot state change event: " + result);
5. }

7. // Register event
8. wifi.on("hotspotStateChange", recvHotspotStateChangeFunc);

10. // Unregister event
11. wifi.off("hotspotStateChange", recvHotspotStateChangeFunc);
```

## wifi.off('hotspotStateChange')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'hotspotStateChange', callback?: Callback<number>): void

取消注册热点状态改变事件。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.off](js-apis-wifimanager.md#wifimanageroffhotspotstatechange)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.AP.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"hotspotStateChange"字符串。 |
| callback | Callback<number> | 否 | 状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。 |

## wifi.on('p2pStateChange')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'p2pStateChange', callback: Callback<number>): void

注册P2P开关状态改变事件。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.on](js-apis-wifimanager.md#wifimanageronp2pstatechange)替代。

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

## wifi.off('p2pStateChange')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'p2pStateChange', callback?: Callback<number>): void

取消注册P2P开关状态改变事件。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.off](js-apis-wifimanager.md#wifimanageroffp2pstatechange)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"p2pStateChange"字符串。 |
| callback | Callback<number> | 否 | 状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。 |

**示例：**

```
1. import wifi from '@ohos.wifi';

3. let recvP2pStateChangeFunc = (result:number) => {
4. console.info("Receive p2p state change event: " + result);
5. }

7. // Register event
8. wifi.on("p2pStateChange", recvP2pStateChangeFunc);

10. // Unregister event
11. wifi.off("p2pStateChange", recvP2pStateChangeFunc);
```

## wifi.on('p2pConnectionChange')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'p2pConnectionChange', callback: Callback<WifiP2pLinkedInfo>): void

注册P2P连接状态改变事件。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.on](js-apis-wifimanager.md#wifimanageronp2pconnectionchange)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"p2pConnectionChange"字符串。 |
| callback | Callback<[WifiP2pLinkedInfo](js-apis-wifi.md#wifip2plinkedinfodeprecated)> | 是 | 状态改变回调函数。 |

## wifi.off('p2pConnectionChange')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'p2pConnectionChange', callback?: Callback<WifiP2pLinkedInfo>): void

取消注册P2P连接状态改变事件。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.off](js-apis-wifimanager.md#wifimanageroffp2pconnectionchange)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"p2pConnectionChange"字符串。 |
| callback | Callback<[WifiP2pLinkedInfo](js-apis-wifi.md#wifip2plinkedinfodeprecated)> | 否 | 状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。 |

**示例：**

```
1. import wifi from '@ohos.wifi';

3. let recvP2pConnectionChangeFunc = (result:wifi.WifiP2pLinkedInfo) => {
4. console.info("Receive p2p connection change event: " + result);
5. }

7. // Register event
8. wifi.on("p2pConnectionChange", recvP2pConnectionChangeFunc);

10. // Unregister event
11. wifi.off("p2pConnectionChange", recvP2pConnectionChangeFunc);
```

## wifi.on('p2pDeviceChange')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'p2pDeviceChange', callback: Callback<WifiP2pDevice>): void

注册P2P设备状态改变事件。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.on](js-apis-wifimanager.md#wifimanageronp2pdevicechange)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO 和 ohos.permission.LOCATION

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"p2pDeviceChange"字符串。 |
| callback | Callback<[WifiP2pDevice](js-apis-wifi.md#wifip2pdevicedeprecated)> | 是 | 状态改变回调函数。 |

## wifi.off('p2pDeviceChange')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'p2pDeviceChange', callback?: Callback<WifiP2pDevice>): void

取消注册P2P设备状态改变事件。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.off](js-apis-wifimanager.md#wifimanageroffp2pdevicechange)替代。

**需要权限：** ohos.permission.LOCATION

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"p2pDeviceChange"字符串。 |
| callback | Callback<[WifiP2pDevice](js-apis-wifi.md#wifip2pdevicedeprecated)> | 否 | 状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。 |

**示例：**

```
1. import wifi from '@ohos.wifi';

3. let recvP2pDeviceChangeFunc = (result:wifi.WifiP2pDevice) => {
4. console.info("Receive p2p device change event: " + result);
5. }

7. // Register event
8. wifi.on("p2pDeviceChange", recvP2pDeviceChangeFunc);

10. // Unregister event
11. wifi.off("p2pDeviceChange", recvP2pDeviceChangeFunc);
```

## wifi.on('p2pPeerDeviceChange')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'p2pPeerDeviceChange', callback: Callback<WifiP2pDevice[]>): void

注册P2P对端设备状态改变事件。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.on](js-apis-wifimanager.md#wifimanageronp2ppeerdevicechange)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO 和 ohos.permission.LOCATION

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"p2pPeerDeviceChange"字符串。 |
| callback | Callback<[WifiP2pDevice[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifi#wifip2pdevicedeprecated)> | 是 | 状态改变回调函数。 |

## wifi.off('p2pPeerDeviceChange')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'p2pPeerDeviceChange', callback?: Callback<WifiP2pDevice[]>): void

取消注册P2P对端设备状态改变事件。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.off](js-apis-wifimanager.md#wifimanageroffp2ppeerdevicechange)替代。

**需要权限：** ohos.permission.LOCATION

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"p2pPeerDeviceChange"字符串。 |
| callback | Callback<[WifiP2pDevice[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifi#wifip2pdevicedeprecated)> | 否 | 状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。 |

**示例：**

```
1. import wifi from '@ohos.wifi';

3. let recvP2pPeerDeviceChangeFunc = (result:wifi.WifiP2pDevice[]) => {
4. console.info("Receive p2p peer device change event: " + result);
5. }

7. // Register event
8. wifi.on("p2pPeerDeviceChange", recvP2pPeerDeviceChangeFunc);

10. // Unregister event
11. wifi.off("p2pPeerDeviceChange", recvP2pPeerDeviceChangeFunc);
```

## wifi.on('p2pPersistentGroupChange')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'p2pPersistentGroupChange', callback: Callback<void>): void

注册P2P永久组状态改变事件。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.on](js-apis-wifimanager.md#wifimanageronp2ppersistentgroupchange)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"p2pPersistentGroupChange"字符串。 |
| callback | Callback<void> | 是 | 状态改变回调函数。 |

## wifi.off('p2pPersistentGroupChange')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'p2pPersistentGroupChange', callback?: Callback<void>): void

取消注册P2P永久组状态改变事件。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.off](js-apis-wifimanager.md#wifimanageroffp2ppersistentgroupchange)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"p2pPersistentGroupChange"字符串。 |
| callback | Callback<void> | 否 | 状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。 |

**示例：**

```
1. import wifi from '@ohos.wifi';

3. let recvP2pPersistentGroupChangeFunc = (result:void) => {
4. console.info("Receive p2p persistent group change event: " + result);
5. }

7. // Register event
8. wifi.on("p2pPersistentGroupChange", recvP2pPersistentGroupChangeFunc);

10. // Unregister event
11. wifi.off("p2pPersistentGroupChange", recvP2pPersistentGroupChangeFunc);
```

## wifi.on('p2pDiscoveryChange')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'p2pDiscoveryChange', callback: Callback<number>): void

注册发现设备状态改变事件。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.on](js-apis-wifimanager.md#wifimanageronp2pdiscoverychange)替代。

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

## wifi.off('p2pDiscoveryChange')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'p2pDiscoveryChange', callback?: Callback<number>): void

取消注册发现设备状态改变事件。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.off](js-apis-wifimanager.md#wifimanageroffp2pdiscoverychange)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"p2pDiscoveryChange"字符串。 |
| callback | Callback<number> | 否 | 状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。 |

**示例：**

```
1. import wifi from '@ohos.wifi';

3. let recvP2pDiscoveryChangeFunc = (result:number) => {
4. console.info("Receive p2p discovery change event: " + result);
5. }

7. // Register event
8. wifi.on("p2pDiscoveryChange", recvP2pDiscoveryChangeFunc);

10. // Unregister event
11. wifi.off("p2pDiscoveryChange", recvP2pDiscoveryChangeFunc);
```
