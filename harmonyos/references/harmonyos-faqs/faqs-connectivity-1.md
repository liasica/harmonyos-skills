---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-1
title: 三方应用如何获取蓝牙MAC地址
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 三方应用如何获取蓝牙MAC地址
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:18+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:970855fd5ab2b2fcd8891cd7e170f4dd792fe84fa3b0df219847e2ad8b9c63a5
---

调用connection.startBluetoothDiscovery()接口，使用蓝牙扫描功能，在扫描结果中即可获取蓝牙MAC地址。需要权限：ohos.permission.ACCESS\_BLUETOOTH。参考代码如下：

```
1. import { connection } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function onReceiveEvent(data: Array<string>) { // data is a collection of Bluetooth device addresses
5. console.info('bluetooth device find = '+ JSON.stringify(data));
6. }

8. try {
9. connection.on('bluetoothDeviceFind', onReceiveEvent);
10. connection.startBluetoothDiscovery();
11. } catch (err) {
12. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
13. }
```

[GetBtMac.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ConnectivityKit/entry/src/main/ets/pages/GetBtMac.ets#L21-L34)

**参考链接**

[发现蓝牙设备](../harmonyos-references/js-apis-bluetooth-connection.md#connectiononbluetoothdevicefind)
