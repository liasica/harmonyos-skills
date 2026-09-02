---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-39
title: 蓝牙写入数据回调成功，无回复确认信息
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 蓝牙写入数据回调成功，无回复确认信息
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:38+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:48ad5091676cb9c659d0bf1940c8848434795f97498d296327e185296837fd34
---

## 问题现象

蓝牙回调提示已经发送成功，但设备没有回复确认信息，排查了设备和特征没有问题。相关核心代码如下：

this.connectDevice.writeCharacteristicValue(characteristic, ble.GattWriteType.WRITE\_NO\_RESPONSE, this.writeCharacteristicValueCallBack);

## 解决方案

[writeCharacteristicValue](../harmonyos-references/js-apis-bluetooth-ble.md#writecharacteristicvalue)方法的writeType参数指定写入特征值的方式：

* WRITE：写入特征值后，对端蓝牙设备需要回复确认；
* WRITE\_NO\_RESPONSE：写入特征值后，对端蓝牙设备不需要回复。

将ble.GattWriteType.WRITE\_NO\_RESPONSE，改成ble.GattWriteType.WRITE即可。
