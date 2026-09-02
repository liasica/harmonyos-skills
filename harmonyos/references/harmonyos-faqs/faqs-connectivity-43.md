---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-43
title: BLE蓝牙重连异常
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > BLE蓝牙重连异常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:39+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:aed37e33a0db7d8c9a2448b119522232f0f031eb3220a7f331ec9de303310d52
---

## 问题现象

代码里实现有连接设备流程和重新连接流程，正常连接流程和重连的流程代码逻辑一致，正常连接流程，通信是没有问题的，但是重连通信一直报BussinessError 2900099：Operation failed这个错误。

## 背景知识

[getServices](../harmonyos-references/js-apis-bluetooth-ble.md#getservices)：client获取server端支持的所有服务能力，即服务发现流程。使用Callback异步回调。

应用调用该方法后，才能调用其他读写特征值、描述符等其他方法，且需确保server支持的服务能力中包含需要操作的特征值或描述符。并且这些方法，都需要在异步回调结果返回后，才能调用下一次读取或者写入操作，包含接口如下所示：

* [readCharacteristicValue](../harmonyos-references/js-apis-bluetooth-ble.md#readcharacteristicvalue).
* [readDescriptorValue](../harmonyos-references/js-apis-bluetooth-ble.md#readdescriptorvalue).
* [writeCharacteristicValue](../harmonyos-references/js-apis-bluetooth-ble.md#writecharacteristicvalue).
* [writeDescriptorValue](../harmonyos-references/js-apis-bluetooth-ble.md#writedescriptorvalue).
* [setCharacteristicChangeNotification](../harmonyos-references/js-apis-bluetooth-ble.md#setcharacteristicchangenotification).
* [setCharacteristicChangeIndication](../harmonyos-references/js-apis-bluetooth-ble.md#setcharacteristicchangeindication).

## 问题定位

分析hilog日志，从日志发现在重新连接流程时，有方法调用不合理的情况：

1. setCharacteristicChangeNotification和getServices一直在循环调用，且getServices在setCharacteristicChangeNotification之后调用，而正常流程是先调用getServices之后才能调用setCharacteristicChangeNotification。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/y4xxYOZyTueIsNOTfHQOww/zh-cn_image_0000002658972619.png "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/P7K8QV6XTVK9H2MMj9gZWg/zh-cn_image_0000002628613410.png "点击放大")
2. writeCharacteristicValue没有在setCharacteristicChangeNotification异步回调回来之后再调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/FDXvqRBKS--LV7I5NYrScw/zh-cn_image_0000002658852667.png "点击放大")

## 分析结论

1. 从日志分析是setCharacteristicChangeNotification和getServices/writeCharacteristicValue这两个接口存在调用阻塞，没有在异步回调回来之后再调用，导致报错2900099，需要排查方法调用是否存在问题。
2. setCharacteristicChangeNotification和getServices一直在循环调用，可能是每次重连GATT设备时都重新创建gattClient对象，未调用[close](../harmonyos-references/js-apis-bluetooth-ble.md#close-1)销毁之前创建的gattClient对象，导致调用方法多次重复订阅。

## 修改建议

排查问题代码，发现是代码中的重新连接流程有问题，会在每次重连GATT设备时都重新创建gattClient对象，而之前创建的gattClient对象未调用close销毁。可以考虑如下修改建议：

* 在重连时重用gattClient对象，连接断开时，使用现有的gattClient对象进行重连。
* 如果需要重新创建gattClient对象，需要将之前创建的gattClient对象调用close销毁。
* 在适当的时候如应用退出或不再需要连接时，调用close方法释放资源。
