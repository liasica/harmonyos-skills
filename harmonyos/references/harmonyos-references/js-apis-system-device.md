---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-device
title: @system.device (设备信息)
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 已停止维护的接口 > @system.device (设备信息)
category: harmonyos-references
scraped_at: 2026-04-28T08:09:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1fc1050131551bbee18af5134c092d0c13ae370cae9e80b82f1efa816bdc5d42
---

本模块提供当前设备的信息。

说明

* 模块维护策略

  - 对于Lite Wearable设备类型，该模块长期维护，正常使用。

  - 对于支持该模块的其他设备类型，该模块从API Version 6开始不再维护，推荐使用新接口[@ohos.deviceInfo](js-apis-device-info.md)进行设备信息查询。
* 本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

WearableLite Wearable

```
1. import device from '@system.device';
```

## device.getInfo(deprecated)

WearableLite Wearable

getInfo(options?: GetDeviceOptions): void

获取当前设备的信息。

说明

在首页的onShow生命周期之前不建议调用device.getInfo接口。

**系统能力：** SystemCapability.Startup.SystemInfo.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [GetDeviceOptions](js-apis-system-device.md#getdeviceoptionsdeprecated) | 否 | 定义设备信息获取的参数选项。 |

## GetDeviceOptions(deprecated)

WearableLite Wearable

定义设备信息获取的参数选项。

**系统能力：** SystemCapability.Startup.SystemInfo.Lite

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | (data: DeviceResponse) => void | 否 | 接口调用成功的回调函数。 data为成功返回的设备信息，具体参考[DeviceResponse](js-apis-system-device.md#deviceresponsedeprecated)。 |
| fail | (data: any,code:number)=> void | 否 | 接口调用失败的回调函数。 code为失败返回的错误码。  code:200，表示返回结果中存在无法获得的信息。 |
| complete | () => void | 否 | 接口调用结束的回调函数。 |

## DeviceResponse(deprecated)

WearableLite Wearable

设备信息。

**系统能力：** SystemCapability.Startup.SystemInfo.Lite

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| brand | string | 品牌。 |
| manufacturer | string | 生产商。 |
| model | string | 型号。 |
| product | string | 代号。 |
| language4+ | string | 系统语言。 |
| region4+ | string | 系统地区。 |
| windowWidth | number | 可使用的窗口宽度。 |
| windowHeight | number | 可使用的窗口高度。 |
| screenDensity4+ | number | 屏幕密度。 |
| screenShape4+ | string | 屏幕形状。可取值：  - rect：方形屏；  - circle：圆形屏。 |
| apiVersion4+ | number | 系统API版本号。 |
| deviceType4+ | string | 设备类型。 |

**示例：**

```
1. export default class Page {
2. getInfo() {
3. interface DeviceData {
4. brand: string;
5. }

7. try {
8. device.getInfo({
9. success: (data: DeviceData) => {
10. console.info('Device information obtained successfully. Device brand:' + data.brand);
11. },
12. fail: (data: string, code: number) => {
13. console.info('Failed to obtain device information. Error code:' + code + '; Error information: ' + data);
14. },
15. });
16. } catch (error) {
17. console.error('Device information API is not supported');
18. }
19. }
20. }
```
