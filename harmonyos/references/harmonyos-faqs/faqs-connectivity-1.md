---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-1
title: 三方应用如何获取蓝牙mac地址
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 三方应用如何获取蓝牙mac地址
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:38+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ea0f96ddc2306666f396826f8a6069d1bb1703e2590d60bc6d3465319a0c020f
---

调用connection.startBluetoothDiscovery()接口，使用蓝牙扫描功能，在扫描结果中即可获取蓝牙MAC地址。需要权限：ohos.permission.ACCESS\_BLUETOOTH。参考代码如下：

```screen
import { connection } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

function onReceiveEvent(data: Array<string>) { // data is a collection of Bluetooth device addresses
  console.info('bluetooth device find = '+ JSON.stringify(data));
}

try {
  connection.on('bluetoothDeviceFind', onReceiveEvent);
  connection.startBluetoothDiscovery();
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

**参考链接**

[发现蓝牙设备](../harmonyos-references/js-apis-bluetooth-connection.md#connectiononbluetoothdevicefind)
