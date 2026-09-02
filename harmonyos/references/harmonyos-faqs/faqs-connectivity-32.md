---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-32
title: 连接过的蓝牙设备，重新连接失败
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 连接过的蓝牙设备，重新连接失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:38+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1b6f2a93d360ca929304a8b8d9f68d1a129d7ec46e7646accea448f5b49c4b1b
---

## 问题现象

蓝牙设备第一次连接成功，重启蓝牙之后，再次连接失败，需要删除设备重新扫描。

## 背景知识

基于信息安全考虑，通过蓝牙扫描获取到的设备地址为虚拟MAC地址。

* 若和该设备地址配对成功后，该地址不会变更。
* 若取消配对该设备或蓝牙关闭后，再次重新发起扫描，该虚拟地址会变更。

[access.addPersistentDeviceId](../harmonyos-references/js-apis-bluetooth-access.md#accessaddpersistentdeviceid16)：若应用想长期使用扫描获取到的虚拟随机地址，需要调用该接口持久化存储虚拟随机地址。

## 问题定位

1. 日志搜索bluetooth.\*device.\*not exist，看到如下日志，说明设备地址错误。

   ```shell
   E C00102/bluetooth_service/bt_chr_ue_manager: [10](PutDeviceProperties:283)device EF:8F:**:**:**:2B not exist, eventName: ACL_CONN_CMP
   ```
2. 代码搜索addPersistentDeviceId，检查应用是否将虚拟设备地址持久化。

## 分析结论

应用未将虚拟设备地址持久化，重新连接时设备地址已发生改变，无法连接。

## 修改建议

```ts
import { access, ble} from '@kit.ConnectivityKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { abilityAccessCtrl, common, Permissions } from '@kit.AbilityKit';

@Entry
@Component
struct BlePage {
  @StorageLink('availableDevices') availableDevices: Array<BluetoothDevice> = [];

  aboutToAppear(): void {
    const context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    reqPermissionFromUser(PERMISSION_LIST, context);
  }

  build() {
    Column() {
      if (this.availableDevices && this.availableDevices.length > 0 && this.availableDevices[0].deviceId) {
        List({ space: LIST_SPACE, initialIndex: 0 }) {
          ForEach(this.availableDevices as BluetoothDevice[], (item: BluetoothDevice, index: number) => {
            ListItem() {
              Item({
                bluetoothDevice: item as BluetoothDevice,
                index: index
              })
            }
            .width('100%')
            .height(76)
            .borderRadius(16)
            .backgroundColor(Color.White)
          })
        }
        .scrollBar(BarState.Auto)
        .width('100%')
        .height('100%')
        .layoutWeight(1)
        .padding({
          left: 16,
          top: 16,
          right: 16,
          bottom: 0
        })
      } else {
        EmptyPage({ img: $r('app.media.picture7'), message: 'No equipment'})
          .width('100%')
          .height('100%')
          .layoutWeight(1)
      }
      Row() {
        Button('Search Device')
          .id('btn_start_scan')
          .fontSize(16)
          .onClick(() => {
            bluetoothClientModel.startBLEScan();
          })
          .width('100%')
      }
      .width('100%')
      .padding({ left: 16, right: 16, bottom: 16})
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#F5F5F5')
  }
}

@Component
struct Item {
  @State bluetoothDevice: BluetoothDevice = {};
  private index: number = 0;

  build() {
    Row() {
      Column() {
        Text(this.bluetoothDevice.deviceName)
          .fontSize(16)
          .fontColor('#333333')
          .textAlign(TextAlign.Start)
          .width('100%')

        Text(this.bluetoothDevice.deviceId)
          .fontSize(14)
          .fontColor(Color.Black)
          .opacity(0.6)
          .margin({ top: 6 })
          .textAlign(TextAlign.Start)
          .width('100%')
      }
      .width('75%')
      .height('100%')
      .justifyContent(FlexAlign.Center)

      Button('持久化')
        .id(`btn_connect${this.index}`)
        .fontSize(16)
        .fontColor('#FF0A59F7')
        .backgroundColor(this.bluetoothDevice.connectionState === ConnectionState.STATE_CONNECTED ? '#00000000' :
          '#0D000000')
        .padding({ left: 16, right: 16 })
        .onClick(() => {
          bluetoothClientModel.persistenceDevice(this.bluetoothDevice.deviceId);
        })
    }
    .id(`list_item${this.index}`)
    .width('100%')
    .height('100%')
    .padding({
      left: 16,
      right: 16,
    })
    .justifyContent(FlexAlign.SpaceBetween)
  }
}

@Component
struct EmptyPage {
  private img: string | PixelMap | Resource = $r('app.media.picture7');
  private message: ResourceStr = 'no equipment';

  build() {
    Column() {
      Image(this.img)
        .width(120)
        .aspectRatio(1)

      Text(this.message)
        .fontSize(14)
        .fontColor(Color.Black)
        .opacity(0.9)
        .margin({ top: 8 })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center)
  }
}

const LIST_SPACE: number = 20;
const PERMISSION_LIST: Array<Permissions> = [
  'ohos.permission.ACCESS_BLUETOOTH'
];
const uiContext: UIContext | undefined = AppStorage.get('uiContext');

function reqPermissionFromUser(permissions: Array<Permissions>, context: common.UIAbilityContext): void {
  const atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
  atManager.requestPermissionsFromUser(context, permissions).then((data) => {
    Logger.info(`data:${JSON.stringify(data)}`);
  }).catch((err: BusinessError) => {
    Logger.error(`requestPermissionsFromUser fail: err = ${JSON.stringify(err)}`);
  });
}

class BluetoothClientModel {
  private mConnectBluetoothDevice: BluetoothDevice = {};
  private mAvailableDevices: BluetoothDevice[] = [];

  isBluetoothEnabled(): boolean {
    let state: access.BluetoothState = 0;
    try {
      state = access.getState();
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(0x0000, 'BluetoothClientModel',
        `isBluetoothEnabled failed. code=${err.code}, message=${err.message}`);
    }
    Logger.info(`isBluetoothEnabled: state = ${state}`);
    if (state === access.BluetoothState.STATE_ON || state === access.BluetoothState.STATE_TURNING_ON) {
      return true;
    }
    return false;
  }

  enableBluetooth() {
    try {
      this.onBTStateChange();
      access.enableBluetooth();
    } catch (err) {
      Logger.error(`enableBluetooth: err = ${JSON.stringify(err)}`);
    }
  }

  startBLEScan(): boolean {
    if (!this.isBluetoothEnabled()) {
      this.enableBluetooth();
      return false;
    }
    this.onBLEDeviceFind();
    const ret = this.startBLEScanInner();
    return ret;
  }

  // 持久化设备地址
  persistenceDevice(deviceId?: string) {
    if (deviceId) {
      access.addPersistentDeviceId(deviceId).then(() => {
        uiContext?.getPromptAction().showToast({
          message: '持久化成功',
          duration: 2000
        });
      }).catch((err: BusinessError) => {
        Logger.error(`addPersistentDeviceId: err = ${JSON.stringify(err)}`);
      });
    }
  }

  private onBTStateChange() {
    try {
      access.on('stateChange', (data: access.BluetoothState) => {
        if (data === access.BluetoothState.STATE_ON) {
          this.startBLEScan();
        } else if (data === access.BluetoothState.STATE_OFF) {
          this.mAvailableDevices = [];
          AppStorage.setOrCreate('availableDevices', this.mAvailableDevices);
        }
      });
    } catch (err) {
      Logger.error(`onBTSateChange: err = ${JSON.stringify(err)}`);
    }
  }

  private onBLEDeviceFind() {
    try {
      ble.on('BLEDeviceFind', (arr: Array<ble.ScanResult>) => {
        let deviceId: string = arr[0].deviceId;
        let deviceName: string = arr[0].deviceName;
        let device = this.mAvailableDevices.find((availableDevice => {
          return availableDevice.deviceId === deviceId;
        }));
        if (!device) {
          let data: ArrayBuffer = arr[0].data;
          deviceName = util.TextDecoder.create('utf-8', {
            ignoreBOM: true
          }).decodeToString(new Uint8Array(data), { stream: false });
          this.mAvailableDevices = [];
          this.mAvailableDevices.push(this.getDevice(deviceId, deviceName));
          AppStorage.setOrCreate('availableDevices', this.mAvailableDevices);
        }
      });
    } catch (err) {
      Logger.info(`onBLEDeviceFind: err = ${JSON.stringify(err)}`);
    }
  }

  private startBLEScanInner(): boolean {
    try {
      this.mAvailableDevices = [];
      if (this.mConnectBluetoothDevice.connectionState === ConnectionState.STATE_CONNECTED) {
        this.mAvailableDevices.push(this.mConnectBluetoothDevice);
      }
      AppStorage.setOrCreate('availableDevices', this.mAvailableDevices);
      ble.startBLEScan([{ serviceUuid: '0000180D-0000-1000-8000-00805F9B34FB' }]);
      return true;
    } catch (err) {
      Logger.error(`startBLEScanInner: err = ${JSON.stringify(err)}`);
    }
    return false;
  }

  private getDevice(deviceId: string, deviceName: string): BluetoothDevice {
    let device = new BluetoothDevice();
    device.deviceId = deviceId;
    device.deviceName = deviceName;
    return device;
  }
}

let bluetoothClientModel = new BluetoothClientModel();

class ConnectionState {
  static STATE_CONNECTED = 2;
  static STATE_DISCONNECTED = 4;
}

@Observed
class BluetoothDevice {
  deviceId?: string = '';
  deviceName?: string = '';
  connectionState?: number = ConnectionState.STATE_DISCONNECTED;
}

class Logger {
  private static domain: number = 0xFF00;
  private static prefix: string = 'BluetoothLowEnergy';
  private static format: string = '%{public}s';

  static info(...args: string[]): void {
    hilog.info(Logger.domain, Logger.prefix, Logger.format, args);
  }

  static error(...args: string[]): void {
    hilog.error(Logger.domain, Logger.prefix, Logger.format, args);
  }
}
```
