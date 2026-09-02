---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-31
title: 当连接指定wifi时，第一次会有概率性连接失败，这是什么原因呢
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 当连接指定wifi时，第一次会有概率性连接失败，这是什么原因呢
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:38+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8b1dbeee9e17522e5b708f896013221eaeb95dba3ec5bbd35eed8e95eeecb159
---

## 问题现象

在连接指定wifi时，第一次连接会有概率性失败，但最终都能连接上。

## 背景知识

* [WLAN](../harmonyos-references/js-apis-wifimanager.md)模块主要提供WLAN基础功能（无线接入、无线加密、无线漫游等）、P2P（peer-to-peer）服务的基础功能和WLAN消息通知的相应服务，让应用可以通过WLAN和其他设备互联互通。
* [Wi-Fi扫描](../harmonyos-guides/scan-development-guide.md)是指设备（如手机、电脑、路由器等）搜索周围可用Wi-Fi网络的过程。通过扫描，设备可以获取附近网络的基本信息（如网络名称、信号强度、加密方式等），从而实现连接、管理或分析周围网络。

## 问题定位

查看日志，搜索Call wifi func:日志的打印情况，确认Call wifi func: GetScanInfoList (start)之前是否有打印Call wifi func: StartScan (start)日志，如果没有，说明没有主动开启wifi扫描，而是在直接获取扫描结果，获取不到扫描结果会触发系统自动开启扫描，因此会出现第一次概率性连接失败，最终能连上的情况。此时，需要先调用[wifiManager.startScan](../harmonyos-references/js-apis-wifimanager.md#wifimanagerstartscan21)启动WLAN扫描，通过on('wifiScanStateChange')订阅扫描状态变更事件，触发扫描成功回调函数。

## 分析结论

开发者因未调用wifiManager.startScan接口进行wifi扫描，而是直接获取扫描结果，导致连接失败。

## 修改建议

在调用[wifiManager.getScanInfoList](../harmonyos-references/js-apis-wifimanager.md#wifimanagergetscaninfolist10)获取扫描结果前，先调用wifiManager.startScan启动WLAN扫描。
