---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-2
title: 如何扫描Wi-Fi列表
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 如何扫描Wi-Fi列表
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:18+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f9d335b78fbdeae9d3126d43a5de937e69fd541ebe601b38a30de15538d6026e
---

使用wifiManager.getScanInfoList方法获取扫描Wi-Fi结果，需要权限：ohos.permission.GET\_WIFI\_INFO。参考代码如下：

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. try {
4. let scanInfoList = wifiManager.getScanInfoList();
5. console.info('scanInfoList:' + JSON.stringify(scanInfoList));
6. let len = scanInfoList.length;
7. console.log('wifi received scan info: ' + len);
8. if (len > 0) {
9. for (let i = 0; i < len; ++i) {
10. console.info('ssid: ' + scanInfoList[i].ssid);
11. console.info('bssid: ' + scanInfoList[i].bssid);
12. console.info('capabilities: ' + scanInfoList[i].capabilities);
13. console.info('securityType: ' + scanInfoList[i].securityType);
14. console.info('rssi: ' + scanInfoList[i].rssi);
15. console.info('band: ' + scanInfoList[i].band);
16. console.info('frequency: ' + scanInfoList[i].frequency);
17. console.info('channelWidth: ' + scanInfoList[i].channelWidth);
18. console.info('timestamp: ' + scanInfoList[i].timestamp);
19. }
20. }
21. } catch (error) {
22. console.error('failed:' + JSON.stringify(error));
23. }
```

[ScanWifiList.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ConnectivityKit/entry/src/main/ets/pages/ScanWifiList.ets#L21-L44)

**参考链接**

[wifiManager.getScanInfoList](../harmonyos-references/js-apis-wifimanager.md#wifimanagergetscaninfolist10)
