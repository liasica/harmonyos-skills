---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-17
title: 调用wifiManager.connectToCandidateConfig弹出Wi-Fi连接确认弹框后，如何判断用户点了连接还是取消
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 调用wifiManager.connectToCandidateConfig弹出Wi-Fi连接确认弹框后，如何判断用户点了连接还是取消
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:38+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:86eb041c2db1fa278cb0cc0f8863ebe457a6b9fb458f6f6567075fe382a0eb43
---

## 问题现象

调用wifiManager.connectToCandidateConfig接口后，会出现一个系统弹框提示用户是否连接候选WLAN，如何监听用户点了连接还是取消。

## 背景知识

* [wifiManager](../harmonyos-references/js-apis-wifimanager.md)模块主要提供WLAN基础功能（无线接入、无线加密、无线漫游等）、P2P（peer-to-peer）服务的基础功能和WLAN消息通知的相应服务，让应用可以通过WLAN和其他设备互联互通。
* [wifiManager.connectToCandidateConfig](../harmonyos-references/js-apis-wifimanager.md#wifimanagerconnecttocandidateconfig)接口支持应用连接到自己添加的候选网络。

## 解决方案

API20提供最新的API接口[wifiManager.connectToCandidateConfigWithUserAction](../harmonyos-references/js-apis-wifimanager.md#wifimanagerconnecttocandidateconfigwithuseraction20)，应用使用该接口连接到自己添加的候选网络时，会提示用户是否信任并建立连接，并使用Promise异步回调用户响应结果。

权限说明：应用需要在“src/main/module.json5”的requestPermissions层级中添加允许应用配置Wi-Fi设备权限[ohos.permission.SET\_WIFI\_INFO](../harmonyos-guides/permissions-for-all.md#ohospermissionset_wifi_info)。
