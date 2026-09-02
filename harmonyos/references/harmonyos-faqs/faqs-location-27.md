---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-location-27
title: 位置服务支持范围和能力说明
breadcrumb: FAQ > 应用服务开发 > 位置服务（Location Kit） > 位置服务支持范围和能力说明
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:50+08:00
doc_updated_at: 2026-09-02
content_hash: sha256:b7b39f66a1c278f8e7be38a6bf220128ac7e16be4f442c0648a41721c194dc5e
---

## 问题现象

[Location Kit位置服务](../harmonyos-guides/location-kit-intro.md)为应用提供实时准确的设备位置信息，满足丰富位置使用场景。

本文介绍位置服务的相关能力范围和特殊场景说明。

## 解决方案

1. 位置服务支持的国家/地区。

   仅Wearable穿戴设备支持[海外国家/地区](../harmonyos-guides/location-kit-appendix.md#支持的国家地区)，其他设备类型仅支持中国境内（不包含中国香港、中国澳门、中国台湾），如果非穿戴设备在海外/地区使用可能会导致位置信息异常。
2. 除基础位置信息能力外，支持哪些开放能力？
   * 审内高精度定位：普通场景下，设备在室内时，使用网络定位，精度较低。开通室内高精度定位能力后，在国内指定的建筑室内，可实现高精度定位，并且可识别设备所在楼层。
   * 位置语音：开通位置语音能力后，通过单次定位[getCurrentLocation](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetcurrentlocation)、持续定位[geoLocationManager.on('locationChange')](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanageronlocationchange)接口获取位置信息时，可以返回当前位置附近的POI信息。也可以通过[geoLocationManager.getPoiInfo](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetpoiinfo20)接口直接获取当前位置附近的POI信息。
   * Beacon围栏后台唤醒：Beacon围栏是指通过蓝牙Beacon设备和手机应用配合，实现"虚拟围栏"的功能。当用户靠近或离开某个特定的Beacon设备时，手机应用会收到通知。支持应用在后台或者不在线时进出围栏拉起应用。接口API见[geoLocationManager.addBeaconFence](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanageraddbeaconfence20)。
   * 获取蓝牙扫描信息：开通该能力后，应用可以扫描获取设备周边的蓝牙设备信息。接口API见[geoLocationManager.on('bluetoothScanResultChange')](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanageronbluetoothscanresultchange16)。

   以上能力需要在AppGallery Connect开通，开通指导见[申请开放能力权限指导](../harmonyos-guides/location-apply-open-capability.md)。
3. 位置服务可以获取的位置信息。

   经度、纬度、海拔高度、设备移动速度、设备移动方向、当前位置附近的POI信息、附加信息（设备所在楼层等）。
4. 位置服务可以获取的GNSS卫星状态信息。

   卫星个数、每个卫星的ID、载波噪声功率谱密度比、卫星高度角、卫星方位角、载波频率、卫星星座类型。
5. 个人数据处理说明。

   定位服务在处理个人数据后立即删除，不会保存和共享用户的个人数据。
6. 上报位置信息的时间间隔。

   GNSS定位时默认和最短上报时间间隔为1秒，网络定位时默认和最短上报时间间隔为20秒。在室内时默认使用网络定位。
7. 持续定位interval参数与功耗的关系。

   持续定位订阅未关闭时，GNSS模块处于持续工作状态，以1秒一次的固定频率尝试获取位置数据。无论[ContinuousLocationRequest](../harmonyos-references/js-apis-geolocationmanager.md#continuouslocationrequest12)中的interval设为5还是30，GNSS硬件的功耗消耗是相同的。位置服务会同时使用GNSS定位和网络定位技术，以便在室内和户外场景下均可以获取到位置结果，对设备的硬件资源消耗较大，功耗也较大。如果不主动结束定位可能导致设备功耗高、耗电快，建议在不需要获取定位信息时及时结束定位。更多指导参考[获取设备的位置信息开发指导](../harmonyos-guides/location-guidelines.md)。
8. 后台地理围栏功能及限制说明。

   若需要在后台实现地理围栏功能，需要申请[后台围栏唤醒权限](../harmonyos-guides/location-apply-open-capability.md#围栏后台唤醒)。使用Location Kit提供的地理围栏可以完成近场服务中"位置感知"这一环节，当设备进入或离开特定区域时触发回调，应用可以在回调中执行自定义逻辑，例如发送通知、拉起页面等。但无法配置卡片实现一步直达目标页面。
