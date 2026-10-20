---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/connectivity-kit-troubleshooting-0002
title: BLE蓝牙扫描与广播问题排查
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 故障排查 > BLE蓝牙扫描与广播问题排查
category: harmonyos-faqs
scraped_at: 2026-10-21T07:12:02+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:34772adb0d98a218cfd929e8db26e5caba179264c0b9346dbc477c1c90db1187
---

## BLE蓝牙无法搜索到对端设备

### 问题现象

1. 使用[低功耗蓝牙（Bluetooth Low Energy，BLE）](../harmonyos-references/js-apis-bluetooth-ble.md)开启扫描，不添加过滤条件时，可以搜索到指定的对端设备，添加自定义过滤条件后，无法搜索到指定的对端设备。
2. 蓝牙搜索过程中，部分蓝牙设备通过[serviceUuid](../harmonyos-references/js-apis-bluetooth-ble.md#servicedata)无法扫描到对应设备。

### 定位过程

1. 检查代码中过滤条件使用是否有误或扫描结果返回是否做了特殊处理，存在开发者可能将真实mac地址作为[scanFilter](../harmonyos-references/js-apis-bluetooth-ble.md#scanfilter)过滤条件及BLE设备发现上报事件回调中使用真实mac地址作为判断条件的情况。
2. 存在部分设备厂商可能没有将serviceUuid放入广播包里的情况。

### 分析结论

1. 基于信息安全考虑，BLE蓝牙底层对真实mac地址做了特殊处理，生成的是虚拟mac地址。因此，若代码中使用真实mac地址作为过滤条件，无法筛选出设备。
2. 部分设备厂商没有把serviceUuid放入广播包中，导致搜索异常。

### 修改建议

* 可根据官方API文档中的过滤条件设置其他过滤参数，以实现扫描出指定设备的能力。如：serviceUuid、[manufactureId](../harmonyos-references/js-apis-bluetooth-ble.md#manufacturedata)、name等过滤参数。所有过滤参数只支持完全匹配，不支持模糊匹配。
* 可以不使用过滤条件，查询出所有设备后对全部设备进行代码手动过滤。

## 如何分析BLE广播信息

### 问题现象

如何通过广播包的报文数据内容，排查蓝牙扫描设备信息获取故障问题，如扫描蓝牙设备名称为空、扫描不到目标广播包等场景？

### 定位过程

对日志进行联合分析，通过时间戳对齐hilog应用事件与HCI底层事件。根据hilog日志中开启广播[ble.startAdvertising](../harmonyos-references/js-apis-bluetooth-ble.md#blestartadvertising)的时间为11:32:26.209，找到HCI日志中对应的开启广播命令，并从右侧的详情页分析广播具体的字段以及内容。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/Sg3fh8DpSTuDWauzFA1Mag/zh-cn_image_0000002768121552.png "点击放大")

### 分析结论

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/FGX1qb_4RbehrGhrn42EbQ/zh-cn_image_0000002797401523.png "点击放大")

左侧代码可以参考[ble.startAdvertising](../harmonyos-references/js-apis-bluetooth-ble.md#blestartadvertising)中的示例，从图中的对应关系可以分析BLE广播报文数据内容[AdvertiseData](../harmonyos-references/js-apis-bluetooth-ble.md#advertisedata)，其中可以关注以下四点：

1. 当前只支持传统广播，因此报文最大长度为31个字节。因此需要关注Advertising Data Length字段，避免因为广播数据过长导致启动广播失败。
2. manufacturerData字段为自定义厂商数据，格式为厂商ID+自定义数据，通过此字段可以排查自定义厂商的数据是否符合预期。
3. 服务数据内容serviceData的原始UUID为00001999-0000-1000-8000-00805f9b34fb，广播包中则表现为0x1999。这是因为广播数据优化逻辑，检测到UUID符合蓝牙SIG标准基地址，会自动优化为16位格式以减少数据包大小。通过此字段可以排查服务数据内容是否符合预期。
4. 通过Local Name字段可以排查广播是否携带设备名称。

### 修改建议

广播包中的字段信息，如果在扫描侧配置的过滤条件[ScanFilter](../harmonyos-references/js-apis-bluetooth-ble.md#scanfilter)比如manufactureData、serviceData以及设备名称等信息与广播报文数据内容不匹配，会导致无法扫描出目标广播包，因此需要结合广播报文数据内容进行排查。
