---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/os-new-feature-504
title: 新增和增强特性
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.4(16) > OS平台能力 > 新增和增强特性
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:21+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:7add4c6704f40d03dbfc1998af220cc05998eb53cd07d3f5e88663d926454aba
---

## Ability Kit

新增一批C API函数，用于获取应用级别沙箱内文件目录。（[API参考](../harmonyos-references/capi-application-context-h.md)）

## ArkUI

* 文本组件新增支持设置文本选择菜单显示在独立窗口。（[API参考](../harmonyos-references/arkts-apis-uicontext-textmenucontroller.md)）
* 窗口管理新增支持创建虚拟屏幕。（[API参考](../harmonyos-references/js-apis-display.md#displaycreatevirtualscreen16)）

## ArkGraphics 2D

新增一批C API函数和枚举，用于支持直接绘制到屏幕buffer的GPU渲染能力。（[API参考](../harmonyos-references/capi-drawing-surface-h.md#oh_drawing_surfacecreateonscreen)）

## ArkWeb

新增支持以固定宽高设置同层渲染的元素。（[API参考](../harmonyos-references/arkts-basic-components-web-attributes.md#nativeembedoptions16)）

## Connectivity Kit

* 新增支持获取对端蓝牙设备的名称。（[API参考](../harmonyos-references/js-apis-bluetooth-connection.md#connectiongetremotedevicename16)）
* 新增支持连接远端设备所有允许连接的profiles。（[API参考](../harmonyos-references/js-apis-bluetooth-connection.md#connectionconnectallowedprofiles16-1)）
* 新增支持持久化存储所获取的对端设备的MAC地址。（[API参考](../harmonyos-references/js-apis-bluetooth-access.md#accessaddpersistentdeviceid16)）

## Input Kit

新增支持设置处于前台的应用操作指定按键的回调。（[API参考](../harmonyos-references/js-apis-inputconsumer.md#inputconsumeronkeypressed16)）

## Location Kit

新增支持订阅蓝牙扫描信息上报用于定位。（[API参考](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanageronbluetoothscanresultchange16)）

## Media Library Kit

新增文件位置的枚举定义，用于标记文件处于本地或云端。（[API参考](../harmonyos-references/arkts-apis-photoaccesshelper-e.md#positiontype16)）

## Network Kit

新增支持获取TLSSocket的文件描述符。（[API参考](../harmonyos-references/js-apis-socket.md#getsocketfd16)）

## Reader Kit

新增Reader Kit，支持多种格式电子书的解析、排版、阅读交互能力。（[指南](../harmonyos-guides/reader-introduction.md)、[API参考](../harmonyos-references/reader-read-core.md)）
