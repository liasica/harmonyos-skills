---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-36
title: BLE蓝牙客户端连接后无法接收服务端广播数据
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > BLE蓝牙客户端连接后无法接收服务端广播数据
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:38+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3771428958330d2cc6f8f6604491363bf86de4d486abfd83e81314123027e449
---

## 问题现象

BLE蓝牙服务端和客户端连接成功后，客户端收到服务端约30次数据后停止接收。

## 背景知识

* 低功耗蓝牙（Bluetooth Low Energy, BLE）是从蓝牙4.0开始支持的技术。相比于传统蓝牙，BLE在保障一定的传输速率情况下，具备更低功耗的特点，广泛使用于续航要求较高的蓝牙设备中。其最高传输速率可达1Mbps，通信范围通常为10米左右。相比于传统蓝牙，BLE以其低功耗的特点，广泛应用于穿戴设备、智能家居和物联网传感器等领域。
* [notifyCharacteristicChanged](../harmonyos-references/js-apis-bluetooth-ble.md#notifycharacteristicchanged)：server端发送特征值变化通知或者指示给client端。
* [on('descriptorWrite')](../harmonyos-references/js-apis-bluetooth-ble.md#ondescriptorwrite)：server端订阅client的描述符写请求事件，server端收到该事件后需要根据DescriptorWriteRequest里的needRsp决定是否调用sendResponse接口回复client。

## 问题定位

定位思路：

先排查服务端是否正常广播数据，以下日志表示服务端广播日志正常打印：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/YpGZFVAPSuu2hw9I4MkQ9g/zh-cn_image_0000002658972595.png "点击放大")

再排查客户端是否正常接收数据，发现客户端BLECharacteristicChanges事件回调日志打印到第30次后结束打印。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/-TkfzhE6SiC9cIm-O4X7-Q/zh-cn_image_0000002628613382.png "点击放大")

蓝牙中的Hilog日志显示客户端NotifyCallback同样只执行30次。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/RgZ-vWOpS-KaD7lIiS-RuA/zh-cn_image_0000002658852645.png "点击放大")

翻看BLE蓝牙服务端文档发现，当服务端收到写入描述符请求时，根据写入请求[DescriptorWriteRequest](../harmonyos-references/js-apis-bluetooth-ble.md#descriptorwriterequest)的needRsp判断是否需要调用[sendResponse](../harmonyos-references/js-apis-bluetooth-ble.md#sendresponse)进行回复。根据文档说明可知，服务端需要订阅客户端的描述符写请求事件，即server.on('descriptorWrite')，当客户端发起写入描述符请求事件[descriptorWrite](../harmonyos-references/js-apis-bluetooth-ble.md#ondescriptorwrite)时，可通过在服务端监听descriptorWrite事件，并在回调中回复客户端。

## 分析结论

根据分析以上定位过程可知，造成客户端无法接收服务端广播数据的原因是服务端没有监听客户端发起写入描述符请求事件[descriptorWrite](../harmonyos-references/js-apis-bluetooth-ble.md#ondescriptorwrite)。

## 修改建议

服务端在数据传输阶段[监听descriptorWrite事件](../harmonyos-references/js-apis-bluetooth-ble.md#ondescriptorwrite)。

验证结果可以看出客户端的BLECharacteristicChange回调函数已经持续执行超过30次。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/arX58XaZQP2FKokzCGhEMw/zh-cn_image_0000002628773282.png "点击放大")

## 总结

通过订阅描述符读取或写入事件请参考[on('descriptorRead')](../harmonyos-references/js-apis-bluetooth-ble.md#ondescriptorread)和[on('descriptorWrite')](../harmonyos-references/js-apis-bluetooth-ble.md#ondescriptorwrite)。

收到读取描述符请求时，需要调用[sendResponse](../harmonyos-references/js-apis-bluetooth-ble.md#sendresponse)进行回复对应描述符的数据内容。

收到写入描述符请求时，可保存客户端写入的描述符数据内容。根据写入请求DescriptorWriteRequest的needRsp判断是否需要调用sendResponse进行回复。
