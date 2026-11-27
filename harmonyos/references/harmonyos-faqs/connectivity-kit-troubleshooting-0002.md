---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/connectivity-kit-troubleshooting-0002
title: BLE蓝牙扫描与广播问题排查与解决
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 故障排查 > BLE蓝牙扫描与广播问题排查与解决
category: harmonyos-faqs
scraped_at: 2026-11-27T10:51:23+08:00
doc_updated_at: 2026-11-26
content_hash: sha256:6bc171d848b85caf49c5261126d1990451518c70fb974ea5229a45404b4a6008
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/GGwvdKiNRMWtkifIi8Z5bA/zh-cn_image_0000002796000526.png?HW-CC-KV=V1&HW-CC-Date=20261127T025123Z&HW-CC-Expire=31536000000&HW-CC-Sign=DF202EDFF50CDC20162853AFF3912674039D298BA8D90220C8E7857EA6F76599 "点击放大")

### 分析结论

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/2cC3liFCRLSDcslfNgKyVA/zh-cn_image_0000002824640503.png?HW-CC-KV=V1&HW-CC-Date=20261127T025123Z&HW-CC-Expire=31536000000&HW-CC-Sign=1A74EBAEFC558310A1D8A98E5861ED60B5C8CE9773BBEB7ADD50D2A031F45737 "点击放大")

左侧代码可以参考[ble.startAdvertising](../harmonyos-references/js-apis-bluetooth-ble.md#blestartadvertising)中的示例，从图中的对应关系可以分析BLE广播报文数据内容[AdvertiseData](../harmonyos-references/js-apis-bluetooth-ble.md#advertisedata)，其中可以关注以下四点：

1. 当前只支持传统广播，因此报文最大长度为31个字节。因此需要关注Advertising Data Length字段，避免因为广播数据过长导致启动广播失败。
2. manufacturerData字段为自定义厂商数据，格式为厂商ID+自定义数据，通过此字段可以排查自定义厂商的数据是否符合预期。
3. 服务数据内容serviceData的原始UUID为00001999-0000-1000-8000-00805f9b34fb，广播包中则表现为0x1999。这是因为广播数据优化逻辑，检测到UUID符合蓝牙SIG标准基地址，会自动优化为16位格式以减少数据包大小。通过此字段可以排查服务数据内容是否符合预期。
4. 通过Local Name字段可以排查广播是否携带设备名称。

### 修改建议

广播包中的字段信息，如果在扫描侧配置的过滤条件[ScanFilter](../harmonyos-references/js-apis-bluetooth-ble.md#scanfilter)比如manufactureData、serviceData以及设备名称等信息与广播报文数据内容不匹配，会导致无法扫描出目标广播包，因此需要结合广播报文数据内容进行排查。

## BLE扫描不到设备问题定位

### 问题现象

蓝牙BLE扫描无法获取设备，如何定位是扫描端还是广播端的问题？

蓝牙BLE扫描涉及两端交互，对于扫描端与广播端都需要进行排查，可以通过上述方法进行排查，初步确认问题所在。

### 定位过程

假设当前是手机扫描与车钥匙广播的场景，可以通过以下方式排查：

在车钥匙旁边放一个其他的BLE设备，比如手表、手环或者BLE模组，在蓝牙设置界面能否扫到这个BLE设备和车钥匙。

1. 如果设置能扫描到BLE设备，扫描不到车钥匙，可判断为车钥匙广播端问题，需排查是否由于硬件原因未发出广播。
2. 如果设置能扫描到，应用扫描不到，可判断为应用的问题，参考以下步骤排查：
   * 是否正确设置ScanFilter的过滤条件，例如：参考[BLE扫描流程](../harmonyos-guides/ble-development-guide.md#完整示例)，为什么无法扫描到附近的BLE设备？
   * 是否正确设置广播端参数，例如：ble.on('BLEDeviceFind')订阅扫描结果，返回蓝牙名称deviceName为什么是空的？
   * 广播端携带的字段与扫描端过滤的字段是否一致，例如：蓝牙扫描ScanFilter过滤参数serviceUuid，无法扫描到目标设备，为什么过滤参数serviceSolicitationUuid就可以扫描到目标设备？

### 分析结论

1. 如果是硬件原因，需要联系硬件提供方分析具体原因。
2. 应用侧问题分析结论：
   * 示例中设置了ScanFilter过滤条件，所以扫描不到目标设备，过滤条件需要根据实际情况调整。
   * 对端设备发广播时没有把参数[AdvertiseData](../harmonyos-references/js-apis-bluetooth-ble.md#advertisedata)中includeDeviceName设置为true，携带设备名称。由于广播报文数据内容中没有设备名称，扫描到的设备上报就不会有设备名称。
   * serviceUuid一般是外围设备在广播包里携带，表明自己支持哪些服务。serviceSolicitationUuid一般是中央设备在广播包里携带，表明自己希望搜索到哪些服务，但也有设备厂商在外围设备广播包里携带，表明外围设备希望搜索到哪些服务。

### 修改建议

1. 如果是硬件原因，需要联系硬件提供方分析具体原因后修改。
2. 应用侧问题修改建议：
   * 如果需要扫描所有可发现的周边BLE设备，需要把startBLEScan第一个入参改为null，根据实际情况调整过滤条件。
   * 需要把参数AdvertiseData中includeDeviceName设置为true，在广播报文数据内容中携带设备名称，扫描到的设备上报才会有设备名称。
   * 由于当前问题的外围设备在广播报文数据内容中，携带的字段为希望搜索到的UUID服务，因此扫描端需要过滤参数serviceSolicitationUuid，根据广播端携带的字段过滤，两端需要保持一致。

## BLE广播设备名与UUID取舍

### 问题现象

BLE蓝牙广播，如果设置携带设备名就发不了13条serviceUuids数据，应该怎么在携带设备名称和发送13条serviceUuids数据之间做取舍？

问题代码如下：

```ts
import { ble } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';
BLE蓝牙广播，如果设置携带设备名就发不了13条serviceUuids数据，应该怎么在携带设备名称和发送13条serviceUuids数据之间做取舍？

const TAG: string = 'BleAdvertisingManager';

export class BleAdvertisingManager {
  private advHandle: number = 0xFF;

  // 1.定义广播状态上报事件
  onReceiveEvent = (data: ble.AdvertisingStateChangeInfo) => {
    AppStorage.setOrCreate('advertiserState', data.state);
  };

  // 2.首次启动广播
  public async startAdvertising() {
    // 2.1设置广播发送的参数
    let setting: ble.AdvertiseSetting = {
      interval: 160,
      txPower: 0,
      connectable: true,
    };
    // 2.2构造广播数据
    let manufactureValueBuffer = new Uint8Array();
    manufactureValueBuffer[0] = 1;
    manufactureValueBuffer[1] = 2;
    manufactureValueBuffer[2] = 3;
    manufactureValueBuffer[3] = 4;

    let serviceValueBuffer = new Uint8Array(4);
    serviceValueBuffer[0] = 5;
    serviceValueBuffer[1] = 6;
    serviceValueBuffer[2] = 7;
    serviceValueBuffer[3] = 8;
    let manufactureDataUnit: ble.ManufactureData = {
      manufactureId: 4567,
      manufactureValue: manufactureValueBuffer.buffer
    };
    let serviceDataUnit1: ble.ServiceData = {
      serviceUuid: "0000181A-0000-1000-8000-00805F9B34FB",
      serviceValue: serviceValueBuffer.buffer
    };
    let serviceDataUnit2: ble.ServiceData = {
      serviceUuid: "19991999-0000-1000-8000-00805f9b34fb",
      serviceValue: serviceValueBuffer.buffer
    };
    let advData: ble.AdvertiseData = {
      serviceUuids: [
        "000008F0-0000-1000-8000-00805F9B34FB",
        "00000810-0000-1000-8000-00805F9B34FB",
        "00009D13-0000-1000-8000-00805F9B34FB",
        "0000950E-0000-1000-8000-00805F9B34FB",
        "00004E2D-0000-1000-8000-00805F9B34FB",
        "000041F0-0000-1000-8000-00805F9B34FB",
        "00001DE1-0000-1000-8000-00805F9B34FB",
        "00007EB9-0000-1000-8000-00805F9B34FB",
        "0000F59C-0000-1000-8000-00805F9B34FB",
        "00002D98-0000-1000-8000-00805F9B34FB",
        "0000343D-0000-1000-8000-00805F9B34FB",
        "00002B0B-0000-1000-8000-00805F9B34FB",
        "00002D89-0000-1000-8000-00805F9B34FB"
        ],
      manufactureData: [],
      serviceData: [],
    };

    // 2.3构造广播启动完整参数AdvertisingParams
    let advertisingParams: ble.AdvertisingParams = {
      advertisingSettings: setting,
      advertisingData: advData, // 注意:广播报文长度不能超过31个字节
      advertisingResponse: advData, // 注意:广播报文长度不能超过31个字节
      duration: 0 // 可选参数，若参数大于0，则广播发送一段时间后会停止，但分配的广播资源还在，可重新启动发送
    }

    // 2.4首次启动广播，蓝牙子系统会分配相关资源，包括应用获取到的广播标识ID
    try {
      ble.on('advertisingStateChange', this.onReceiveEvent);
      this.advHandle = await ble.startAdvertising(advertisingParams);
    } catch (err) {
      console.error(TAG, 'err');
    }
  }
}
```

### 定位过程

根据问题代码中的serviceUuids可以发现，1条serviceUuid是2字节，13条就是26字节。如果广播要携带设备名，占用的字节数取决于设置界面的蓝牙名称的总长度，问题中的设备名"XXXX XXPro"占用10个字节，因此会超出最大长度（31个字节）限制，会导致启动广播失败。

### 分析结论

启动广播失败是因为超出了报文最大长度，serviceUuid可以在连接之后服务发现的时候获取，不一定要在广播的时候全都带上。

服务发现流程：[getServices](../harmonyos-references/js-apis-bluetooth-ble.md#getservices-1)，client获取server端支持的所有服务能力。获取返回的结构体[GattService](../harmonyos-references/js-apis-bluetooth-ble.md#gattservice)中会有所有的serviceUuid。

### 修改建议

如果一定要在广播时设置携带设备名，建议减少serviceUuid的条数，后续在服务发现流程获取serviceUuid。

## 被动扫描设备核心数据需放主动广播

### 问题现象

部分设备仅支持被动扫描，只能接收主动广播包（advertisingData）中的数据，无法获取扫描响应包（advertisingResponse）中的数据，导致设备发现和连接失败。

部分设备仅支持被动扫描，只能接收主动广播包（advertisingData）中的数据，无法获取扫描响应包（advertisingResponse）中的数据，导致设备发现和连接失败。

### 定位过程

被动扫描设备仅能接收主动广播包（advertisingData）中的数据，无法获取扫描响应包（advertisingResponse）中的数据。如果设备发现所依赖的核心信标数据（如厂商自定义数据或Service UUID）被放置在扫描响应包中，被动扫描设备将无法获取这些数据，导致设备发现失败。

### 分析结论

被动扫描设备无法发现设备的原因是核心数据被放置在扫描响应包中，而被动扫描模式下设备不会主动发送扫描请求，因此无法获取扫描响应包中的数据。需将核心数据迁移至主动广播包中，同时注意主动广播包长度不能超过31字节。

### 修改建议

将设备发现强依赖的核心数据（如厂商自定义数据或Service UUID）放置在主动广播包（advertisingData）中，将非核心数据放置在扫描响应包（advertisingResponse）中。同时需精简主动广播包中的数据，确保总长度不超过31字节。

```ts
import { ble } from '@kit.ConnectivityKit';

// 1. 广播基础设置
let setting: ble.AdvertiseSetting = {
  interval: 160,
  txPower: -7,
  connectable: true
};

// 2. 主动广播包（advertisingData）- 被动扫描设备唯一能接收的数据源
// 仅放置设备发现所必须的核心数据，注意总长度不能超过31字节
let coreData = new Uint8Array([0x01, 0x02]);
let advData: ble.AdvertiseData = {
  serviceUuids: ["0000xxxx-0000-1000-8000-00805f9b34fb"],
  manufactureData: [{
    manufactureId: 0x0001,
    manufactureValue: coreData.buffer
  }],
  serviceData: []
};

// 3. 扫描响应包（advertisingResponse）- 仅主动扫描设备才能获取
// 将非核心数据放置在此处
let extraData = new Uint8Array([0x11, 0x22, 0x33, 0x44, 0x55, 0x66]);
let advResponse: ble.AdvertiseData = {
  serviceUuids: [],
  manufactureData: [],
  serviceData: [{
    serviceUuid: "0000yyyy-0000-1000-8000-00805f9b34fb",
    serviceValue: extraData.buffer
  }]
};

// 4. 构造广播启动完整参数AdvertisingParams
let advertisingParams: ble.AdvertisingParams = {
  advertisingSettings: setting,
  advertisingData: advData,
  advertisingResponse: advResponse,
  duration: 0
};

// 5. 启动广播
async function startBleAdvertising() {
  try {
    let advHandle = await ble.startAdvertising(advertisingParams);
    console.info('BLE广播启动，核心数据已放置在advertisingData中');
  } catch (err) {
    console.error(`BLE广播启动失败: ${err.message}`);
  }
}
```
