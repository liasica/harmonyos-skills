---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-4
title: 设备连接Wi-Fi后，如何获取当前设备的IP地址
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 设备连接Wi-Fi后，如何获取当前设备的IP地址
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:19+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:fc6c21e424b92b824f09a3565599e090ec52e3b4d49bebdad794ef2ee51d8740
---

使用wifiManager模块获取ipInfo，然后转换为IP常用格式，注意wifiManager.getIpInfo()接口需要权限ohos.permission.GET\_WIFI\_INFO。

参考代码如下：

```
1. import { wifiManager } from '@kit.ConnectivityKit';

3. let ipAddress = wifiManager.getIpInfo().ipAddress;
4. let ip = (ipAddress >>> 24) + "." + (ipAddress >> 16 & 0xFF) + "." + (ipAddress >> 8 & 0xFF) + "." + (ipAddress & 0xFF);
```

[GetIpInfo.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ConnectivityKit/entry/src/main/ets/pages/GetIpInfo.ets#L21-L25)
