---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/externaldevice-faqs
title: 常见问题
breadcrumb: 指南 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > 常见问题
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:37+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:729c900189b6a0222904f384f2cce7f96d0a9d8b38168bea0aef451802ac9b9c
---

## 编译或运行时无法找到头文件

### 问题现象

编译或运行时提示“usb/usb\_ddk\_api.h not found”、“hid/hid\_ddk\_api.h not found” 等。

### 解决措施

* 编译时报错：请确认HarmonyOS版本，是否为最新版本。
* 运行时报错：请确认设备SDK版本为API11及以上。

## 安装HAP时提示版本不匹配

### 问题现象

安装HAP时提示 “compileSdkVersion and releaseType of the app do not match the apiVersion and releaseType on the device”。

### 解决措施

请根据[参考信息](externaldevice-faqs.md#参考信息)提供的对应关系，检查设备SDK的API版本是否匹配。

### 参考信息

| 接口类型 | 支持的最小API |
| --- | --- |
| 应用开发接口（ArkTS接口） | API10 |
| USB DDK接口 | API10 |
| HID DDK接口 | API11 |

## 安装HAP时提示解析本地so文件失败

### 问题现象

安装HAP时提示"code:9568347 error: install parse native so failed"。

### 解决措施

根据应用调试中[安装HAP时提示“code:9568347 error: install parse native so failed”错误，或者运行时候提示“TypeError：Cannot read property xxx of undefined”错误](../harmonyos-faqs-V5/faqs-app-debugging-14-V5.md)提供的解决方法，在build-profile.json5中的buildOption/externalNativeOptions内手动配置abiFilters的值。

## 使用基于缓冲区发送数据的DDK接口时，未按照指定的offset和bufferLength发送

### 问题现象

以[OH\_Usb\_SendPipeRequest](../harmonyos-references/capi-usb-ddk-api-h.md#oh_usb_sendpiperequest)为例，使用此类基于缓冲区发送数据的接口时，对参数[UsbDeviceMemMap](../harmonyos-references/capi-usbddk-usbdevicememmap.md)的offset、bufferLength字段做了赋值，但是实际传输的数据内容是按照size大小将整个缓冲区的数据发送。

### 解决措施

此类接口的实现是按照size大小将整个缓冲区用于传输。因此在发送特定部分的数据时，需要按需申请相应大小的缓冲区、并填充对应的数据以发起传输。可以参考以下代码块的实现。注：

* 此类接口计划进行优化改造，后续版本中会提供基于offset和bufferLength传输的能力。
* 性能开销：创建和销毁缓冲区接口的性能开销很小，通常在0.1毫秒以内、可忽略不计。

```cpp
/**
 * 假定此处 data 已经填充了有效数据；deviceId是对应外设ID；pipe是要传输的管道信息
 * 场景预设：需传输 data 中索引从0x10开始的、长度为32的数据
 */
uint8_t *data = new uint8_t [128];

/** 创建数据缓冲区 */
UsbDeviceMemMap *devMmap;
OH_Usb_CreateDeviceMemMap(deviceId, 32, &devMmap);

/** 只拷贝要传输的部分数据到缓冲区 */
memcpy(devMmap->address, data + 0x10, 32);

/** 发起数据传输 */
OH_Usb_SendPipeRequest(pipe, devMmap);

/** 使用完毕后，需销毁数据缓冲区以回收资源 */
OH_Usb_DestroyDeviceMemMap(devMmap);
```

## 在子进程或非驱动Ability中调用DDK的C-API失败

### 问题现象

在驱动Ability创建的子进程或者非驱动Ability进程中调用Driver Development Kit的C-API，返回异常错误。

### 解决措施

Driver Development Kit提供的C-API仅支持在DriverExtension进程中使用，如果在其他进程中需要实现外设的管理和通信，建议使用[@ohos.usbManager (USB管理)](../harmonyos-references/js-apis-usbmanager.md)、libusb三方库等提供的接口。

## 多个驱动Ability配置了同一型号外设的情况下，插入该外设只会拉起一个驱动Ability

### 问题现象

在多个驱动Ability的“vids”、“pids”列表中都配置了一个型号的外设，但是接入该外设时，只能绑定并拉起一个驱动Ability。

### 解决措施

驱动Ability的设计初衷是支持厂商为单个或多个型号的外设开发一个驱动应用，规格上不支持为同一外设同时部署多个驱动Ability的场景。若确实存在该诉求（例如：上游需要封装USB功能实现，并分发给下游多个应用），可以使用USB系统服务提供的[@ohos.usbManager (USB管理)](../harmonyos-references/js-apis-usbmanager.md)、libusb三方库等实现封装。
