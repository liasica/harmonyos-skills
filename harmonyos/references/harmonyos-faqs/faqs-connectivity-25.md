---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-25
title: 连接无网Wi-Fi时弹窗及无法访问外网问题如何解决
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 连接无网Wi-Fi时弹窗及无法访问外网问题如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:38+08:00
doc_updated_at: 2026-07-22
content_hash: sha256:5fb108e5f92d02c10daf2dd753628c991c8eb57f89fa1acdd4cb10870588b904
---

## 问题现象

使用[connectToCandidateConfig](../harmonyos-references/js-apis-wifimanager.md#wifimanagerconnecttocandidateconfig)接口连接外设热点时，如果外设热点无法访问外部网络（如ap配网时），此时会提示"当前WLAN不可上网，是否继续使用此WLAN"弹窗。如果点击不使用，则有一定的概率出现指令下发失败现象，请问如何屏蔽此场景下的弹窗？另外，当应用直连设备并通过设备Wi-Fi连接时，该Wi-Fi无法连接外网，用户选择继续使用后，应用无法连接外网导致不能使用，是否有切换网络的API或解决方案？

## 背景知识

"当前WLAN不可上网，是否继续使用此WLAN"弹窗中的业务逻辑如下：

* 点击使用后，会默认所有网络的主链路为Wi-Fi，导致无法正常使用网络发起请求。
* 点击不使用后，虽然Wi-Fi一样会保持连接，但网络主链路会切换到蜂窝网络。

## 解决方案

此类弹窗属于系统弹窗，不支持应用屏蔽。由于弹窗中的操作不影响用户Wi-Fi网络的实际连接，只会决定其网络连接是默认走蜂窝网络，还是Wi-Fi网络。因此，并不会对用户的使用有影响。

另外，对于连接不可上网Wi-Fi后应用无法访问外网的问题，请升级到7.0(26.0.0)版本，该版本支持连接不可上网Wi-Fi时，允许应用拉起访问网络。

## 常见FAQ

Q：手动连接无网Wi-Fi，不会弹出"当前WLAN不可上网，是否继续使用此WLAN"弹窗。

A：该弹框只在首次连接弹出，不会重复弹出。只有将Wi-Fi删除后重新连接，该弹框才会再次弹出。

Q：连接无网Wi-Fi，系统一段时间后会自动断开，并且重新连接一个可以访问外网的Wi-Fi。

A：从API13开始，连接无网Wi-Fi后，系统将保持连接当前Wi-Fi，不再会自动断开当前Wi-Fi，重新连接其他可用Wi-Fi。

Q：调用[connectToCandidateConfigWithUserAction](../harmonyos-references/js-apis-wifimanager.md#wifimanagerconnecttocandidateconfigwithuseraction20)方法时报错Property 'connectToCandidateConfigWithUserAction' does not exist on type 'typeof wifiManager'原因。

A：[connectToCandidateConfigWithUserAction](../harmonyos-references/js-apis-wifimanager.md#wifimanagerconnecttocandidateconfigwithuseraction20)方法是在API20才开始支持的，低于API20无法使用该方法。

Q：是否有类似其他平台ConnectivityManager.requestNetwork的切换网络API？

A：当前不提供单独切换网络的API。连接不可上网Wi-Fi时应用无法访问外网的问题，已在7.0(26.0.0)版本中支持允许应用拉起访问网络，请升级到该版本验证。
