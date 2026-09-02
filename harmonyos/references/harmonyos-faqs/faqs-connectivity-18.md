---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-18
title: 如何实现WLAN随机MAC地址获取
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 如何实现WLAN随机MAC地址获取
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:38+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2de2121bfdf051b76354c4c236fe4dda71d7938ed71aeeb8b63329e0385e123c
---

## 问题现象

网络连接成功后，如何获取设备的MAC地址？

## 背景知识

1. 设备连接到WLAN网络或接入点时会使用MAC地址。由于这些MAC地址未经加密即被传输，因此可能会被捕获并用于跟踪用户的位置。随机分配MAC地址功能通过在连接到WLAN网络时使用随机分配的MAC地址，可以加强用户隐私保护。在HarmonyOS中可以通过[getLinkedInfo](../harmonyos-references/js-apis-wifimanager.md#wifimanagergetlinkedinfo)获取MAC地址。
2. 需要权限：ohos.permission.GET\_WIFI\_INFO。
3. 当macType是1时，获取macAddress还需申请[ohos.permission.GET\_WIFI\_LOCAL\_MAC](../harmonyos-guides/restricted-permissions.md#ohospermissionget_wifi_local_mac)权限（API8-15仅面向系统应用开放。从API 16开始，在PC/2in1设备上面向普通应用开放，在其余设备上仍仅面向系统应用开放），无该权限时，macAddress返回随机MAC地址。可申请此权限的特殊场景与功能包括：
   * 证券交易：应用内进行证券交易，如股票、期货、债券交易等。适用设备：PC/2in1。
   * 网银交易及身份认证：应用内提供网上银行服务（如账户查询、转账汇款等），或为网银用户提供身份认证及签名验签工具。适用设备：PC/2in1。
   * 视频类应用，适用设备：TV。

## 解决方案

开发前需要在module.json5文件中的requestPermissions字段添加{"name": "ohos.permission.GET\_WIFI\_INFO"}申请权限，当macType是1时，获取macAddress还需申请ohos.permission.GET\_WIFI\_LOCAL\_MAC权限。

使用Promise异步回调，通过macAddress属性获取MAC地址信息。

```ts
import wifiManager from '@ohos.wifiManager';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button("点击获取当前连接的Wi-Fi信息")
        .onClick(() => {
          wifiManager.getLinkedInfo().then(data => {
            console.info(`get wifi linked info: ${JSON.stringify(data.macAddress)}`);
          }).catch((error: Error) => {
            console.error(`get linked failed: ${JSON.stringify(error)}`);
          });
        })
    }
  }
}
```

成功获取到WLAN随机MAC，输出结果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/wReieo7eT1KKn0rgroWDhA/zh-cn_image_0000002628772524.png "点击放大")

## 常见FAQ

Q：通过wifiManager.getLinkedInfo获取的随机MAC地址(即macType=0)，对于不同网络环境，MAC地址会改变吗？

A：macType为0时，随机MAC在同一网络下macAddress不会改变，切换不同网络，macAddress是会发生变化的。
