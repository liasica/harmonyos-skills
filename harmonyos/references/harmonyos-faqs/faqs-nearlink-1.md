---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-nearlink-1
title: 星闪API外设设备名称获取方式
breadcrumb: FAQ > 系统开发 > 网络 > 星闪（NearLink） > 星闪API外设设备名称获取方式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:39+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:ef50229dd7f864362ffe90312dab64e843a24205606c4560e2ab42d64e5db69c
---

## 问题现象

1. [ScanResults](../harmonyos-references/nearlink-scan.md#scanresults)中的[deviceName](../harmonyos-references/nearlink-scan.md#scanresults)是通过读取广播包中哪个部分定义的内容？
2. 如果对端设备更新了广播包中的数据，手机里扫描获取的[ScanResults](../harmonyos-references/nearlink-scan.md#scanresults)中的[deviceName](../harmonyos-references/nearlink-scan.md#scanresults)一定会更新吗？是否会存在缓存上次扫描的结果？

## 解决方案

1. [ScanResults](../harmonyos-references/nearlink-scan.md#scanresults)（扫描结果）的[deviceName](../harmonyos-references/nearlink-scan.md#scanresults)（扫描到的设备名称）通过读取广播包中类型为0x0B（设备完整本地名称）或者0x0A（设备缩写本地名称）的数据，获得设备名称。
2. 扫描方根据扫描结果中类型为0x0A或0x0B的数据获取对端设备名，对端广播数据中携带的设备名更新后，扫描方获取的[ScanResults](../harmonyos-references/nearlink-scan.md#scanresults)中的[deviceName](../harmonyos-references/nearlink-scan.md#scanresults)就会更新。注意点：如果广播方设备在广播过程中发生设备名变化，广播数据中携带的设备名可能不会及时更新，重新发起星闪广播后才会更新广播数据。因为设备调用[startAdvertising](../harmonyos-references/nearlink-advertising.md#startadvertising)发起广播的时候会获取一次设备本地名称，如果设备正在发广播时设备名发生了变化，这时广播中携带的还是之前的设备名。此时[stopAdvertising](../harmonyos-references/nearlink-advertising.md#stopadvertising)再重新[startAdvertising](../harmonyos-references/nearlink-advertising.md#startadvertising)，才会携带新的设备名。
