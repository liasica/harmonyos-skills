---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-46
title: 如何选用业务需要的摄像头
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 如何选用业务需要的摄像头
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c6af9ff75719293b77f558739a4bbe403cb08ae29e8081a5ff9853126f2398e5
---

## 问题现象

使用[getSupportedCameras](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedcameras)接口获取摄像头设备时，获得的后置摄像头有且仅有一个广角的，无法指定其他类型的后置摄像头。

另外，如何获取USB相机、分布式相机等外部相机？

## 解决方案

1. 如何获取相机设备？
   * [getSupportedCameras](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedcameras)：可通过该接口获取到当前设备能支持的相机设备列表，开发者可根据自己业务需要通过参数去筛选合适的相机设备，起流拍摄。从API23开始，该接口无法查询到分布式相机。
   * [getCameraDevices](../harmonyos-references/arkts-apis-camera-cameramanager.md#getcameradevices23)：开发者可通过参数限定直接查询业务需要的相机设备列表。从API23开始，有需要分布式相机的开发者可使用该接口，通过指定ConnectionType为CAMERA\_CONNECTION\_REMOTE来查找分布式相机设备。
   * [getCameraDevice](../harmonyos-references/arkts-apis-camera-cameramanager.md#getcameradevice18)：该接口从API18开始开放，开发者可以通过接口查找指定相机设备。
2. 如何筛选合适的相机设备？

   可以通过[CameraPosition](../harmonyos-references/arkts-apis-camera-e.md#cameraposition)（相机位置，前置/后置）和[ConnectionType](../harmonyos-references/arkts-apis-camera-e.md#connectiontype)（连接方式，内置/USB连接/分布式摄像头）两个参数来筛选业务需要的相机设备，然后起流拍摄。

   例如在自拍场景，可以选取CameraPosition为CameraPosition.CAMERA\_POSITION\_FRONT的相机设备初始化资源、起流拍摄。如果需要使用USB/分布式相机，则可以通过ConnectionType参数选取指定的相机设备。
3. 其他补充说明：
   * 如何获取物理摄像头？

     对于内置相机来说，当前还不支持直接获取物理摄像头，只能获取逻辑摄像头。一台设备上可能存在多个内置物理摄像头，但是通过接口最多只能查询到两个逻辑摄像头，即前置和后置摄像头，无法显式指定具体使用哪颗后置摄像头。
   * 如何使用USB相机/分布式相机起流拍摄？

     以选择USB相机为例，在getSupportedCameras接口返回的设备列表中选择ConnectionType为CAMERA\_CONNECTION\_USB\_PLUGIN的设备初始化相机资源，然后起流拍摄即可。后续的初始化资源、起流拍摄的过程与使用内置相机的流程完全一致，可参考：[拍照实践(ArkTS)](../harmonyos-guides/camera-shooting-case.md)。

     API23之后，如想使用分布式相机，需要通过getCameraDevices接口去查找相机设备，将接口入参connectType指定为ConnectionType.CAMERA\_CONNECTION\_REMOTE即可。后续初始化、起流拍摄的流程也与内置相机流程一致。

     如果接口返回的设备列表中不存在CAMERA\_CONNECTION\_USB\_PLUGIN/CAMERA\_CONNECTION\_REMOTE的设备，则说明当前设备不支持对应的外接USB相机或分布式相机设备。
   * 如何理解getCameraDevice接口的入参type？

     目前getCameraDevice/getCameraDevices两个接口的type/types参数只能指定为CameraType.CAMERA\_TYPE\_DEFAULT，无法通过该参数定向查找广角/超广角/长焦/带景深信息的相机设备。
   * PC上探测到外接设备之后，能否通过外接设备的商品传播名去选择设备？

     外接设备分为两种，即USB连接的相机（CAMERA\_CONNECTION\_USB\_PLUGIN）和分布式相机（CAMERA\_CONNECTION\_REMOTE）。USB连接的相机可以通过cameraId字段拿到相机的商品传播名，分布式相机则可以通过hostDeviceName字段获取对应相机设备的传播名。

     需要注意的是，分布式相机是指在同一个无线组网环境中的相机设备，可能是另一台手机或者平板设备。另外，非分布式相机的hostDeviceName字段为空。

## 总结

上述三个接口优缺点对比情况如下表：

| 接口 | 优点 | 缺点 | 推荐应用场景 |
| --- | --- | --- | --- |
| [getSupportedCameras](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedcameras) | 可以查询所有非分布式相机设备 | 无法查询分布式相机；需从列表中手动筛选设备 | 所有不涉及分布式相机的场景 |
| [getCameraDevice](../harmonyos-references/arkts-apis-camera-cameramanager.md#getcameradevice18) | 可以根据参数查询特定相机设备 | 感知不到全部设备 | 仅适用于特定场景（如自拍场景，指定查询前置摄像头，查询不到直接退出） |
| [getCameraDevices](../harmonyos-references/arkts-apis-camera-cameramanager.md#getcameradevices23) | 可以根据参数查询特定相机设备列表；可查询到分布式相机 | 感知不到全部设备；需从列表中手动筛选设备 | 同getCameraDevice，尤其是分布式相机应用场景 |
