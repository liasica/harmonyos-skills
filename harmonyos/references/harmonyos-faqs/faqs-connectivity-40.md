---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-40
title: 如何分析BLE广播信息
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 如何分析BLE广播信息
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:38+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c12eb7fe487250f09eda61d62dda77fdebbccf05aafbd274119982a848829686
---

## 问题现象

如何通过广播包的报文数据内容，排查蓝牙扫描设备信息获取故障问题，如扫描蓝牙设备名称为空、扫描不到目标广播包等场景？

## 背景知识

* 日志获取：
  1. 蓝牙HCI日志：hdc file recv /data/log/bt。
  2. [hilog](../harmonyos-guides/hilog.md)日志：hdc file recv /data/log/hilog。获取后使用[hilogtool](../harmonyos-guides/hilog-tool.md)工具进行解析，将其转换为明文hilog日志。
* 在BLE技术中，广播包是设备被发现和建立连接的核心载体，其设计兼顾了低功耗与信息传递效率。BLE广播发送时，可以通过[AdvertiseSetting](../harmonyos-references/js-apis-bluetooth-ble.md#advertisesetting)设置广播的发送参数，包括：
  1. 广播发送间隔interval，控制广播间隔时间，直接影响设备被发现的速度。
  2. 广播发送功率txPower，控制蓝牙信号发射功率强度，直接影响信号覆盖范围及功耗。
  3. 是否是可连接广播connectable，如果此处设置为不可连接广播，将直接影响后续的连接操作，导致无法进行连接。

## 问题定位

对日志进行联合分析，通过时间戳对齐hilog应用事件与HCI底层事件。根据hilog日志中开启广播[ble.startAdvertising](../harmonyos-references/js-apis-bluetooth-ble.md#blestartadvertising)的时间为11:32:26.209，找到HCI日志中对应的开启广播命令，并从右侧的详情页分析广播具体的字段以及内容。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/oaxcazIvQ7umMGp06TZK9Q/zh-cn_image_0000002658852665.png "点击放大")

## 分析结论

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/ImkC84s3QierC22xwaBQCQ/zh-cn_image_0000002628773304.png "点击放大")

左侧代码可以参考ble.startAdvertising中的示例，从图中的对应关系可以分析BLE广播报文数据内容[AdvertiseData](../harmonyos-references/js-apis-bluetooth-ble.md#advertisedata)，其中可以关注以下四点：

1. 当前只支持传统广播，因此报文最大长度为31个字节。因此需要关注Advertising Data Length字段，避免因为广播数据过长导致启动广播失败。
2. manufacturerData字段为自定义厂商数据，格式为厂商ID+自定义数据，通过此字段可以排查自定义厂商的数据是否符合预期。
3. 服务数据内容serviceData的原始UUID为00001999-0000-1000-8000-00805f9b34fb，广播包中则表现为0x1999。这是因为广播数据优化逻辑，检测到UUID符合蓝牙SIG标准基地址，会自动优化为16位格式以减少数据包大小。通过此字段可以排查服务数据内容是否符合预期。
4. 通过Local Name字段可以排查广播是否携带设备名称。

## 修改建议

广播包中的字段信息，如果在扫描侧配置的过滤条件[ScanFilter](../harmonyos-references/js-apis-bluetooth-ble.md#scanfilter)比如manufactureData、serviceData以及设备名称等信息与广播报文数据内容不匹配，会导致无法扫描出目标广播包，因此需要结合广播报文数据内容进行排查。

## 常见FAQ

Q：ScanFilter指的是结果中被过滤掉（不包含）的部分，还是过滤出（仅包含）的意思？

A：是过滤出（仅包含）的意思。

Q：为什么扫描到的设备deviceName是空的？

A：排查广播是否携带设备名称，如果广播包中的Local Name字段为空，那么扫描上报的数据中设备名称就为空。建议检查广播端AdvertiseData的includeDeviceName字段，是否携带了本机的设备名称作为广播名称。
