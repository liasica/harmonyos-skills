---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-4
title: 设备连接Wi-Fi后，如何获取当前设备的IP地址
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 设备连接Wi-Fi后，如何获取当前设备的IP地址
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:38+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:98929ba0f9bb7a46c3e7ce1ee5e79854943514be757afc7e62b3f1dace7a00a9
---

使用wifiManager模块获取ipInfo，然后转换为IP常用格式，注意wifiManager.getIpInfo()接口需要权限ohos.permission.GET\_WIFI\_INFO。

参考代码如下：

```typescript
import { wifiManager } from '@kit.ConnectivityKit';

let ipAddress = wifiManager.getIpInfo().ipAddress;
let ip = (ipAddress >>> 24) + "." + (ipAddress >> 16 & 0xFF) + "." + (ipAddress >> 8 & 0xFF) + "." + (ipAddress & 0xFF);
```
