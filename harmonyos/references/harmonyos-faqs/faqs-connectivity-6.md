---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-6
title: 如何解决存在较大量的蓝牙设备时-低功耗蓝牙连接效率低问题
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 如何解决存在较大量的蓝牙设备时-低功耗蓝牙连接效率低问题
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:16+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:24fa6351894441e0b288c43afbcb57a3d16658c3355dc1a0aabe2423fc86e092
---

## 问题现象

存在较大量的蓝牙设备时（车库场景），低功耗蓝牙连接效率低。

## 背景知识

[低功耗蓝牙](../harmonyos-guides/bluetooth-ble.md)是从蓝牙4.0起支持的协议，与[传统蓝牙](../harmonyos-guides/bluetooth-br.md)相比，功耗极低、传输速度更快，但传输数据量较小。常用在对续航要求较高且只需小数据量传输的各种智能电子产品中，比如智能穿戴设备、智能家电、传感器等，应用场景广泛。

* 当存在大量蓝牙设备时，广播信道中会充斥大量扫描报文，并且会占据空口资源，导致连接效率低；扫描端使用ScanFilter过滤参数，扫描端设备链路层只处理位于过滤参数白名单中的设备的广播数据，减少扫描报文的发送，减少空口压力，同时减少扫描设备内部控制器和主机间的交互通信，降低芯片功耗，提高连接效率。
* 可根据不同的场景选择合适的扫描模式[ScanDuty](../harmonyos-references/js-apis-bluetooth-ble.md#scanduty)，如需提高扫描发现效率，可以选择SCAN\_MODE\_LOW\_LATENCY扫描模式。

## 解决方案

* **方案一**：

  在BLE扫描距离范围内扫描时，可以通过扫描过滤参数[ScanFilter](../harmonyos-references/js-apis-bluetooth-ble.md#scanfilter)来过滤出目标设备，如设备的随机MAC地址、设备名称、serviceUUID等，可以快速找到目标设备。如果已经连接过，可以将随机MAC地址或deviceName保存起来，下次可以直接用保存的信息去过滤扫描。

  **说明** 

  该随机MAC在如下情况会改变：已配对设备取消配对后重新扫描或蓝牙服务下电时，该随机地址会变更，若和该设备地址配对成功后，该地址不会变更，参考[ble.getConnectedBLEDevices](../harmonyos-references/js-apis-bluetooth-ble.md#blegetconnectedbledevices)。

  使用name过滤发起BLE扫描的代码。

  ```ts
  // 开始扫描
  async startScan(): Promise<void> {
    let grantStatus: boolean = await this.checkPermissionGrant('ohos.permission.ACCESS_BLUETOOTH') ===
    abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED;
    if (!grantStatus) {
      this.promptAction.showToast({
        message: '请先申请蓝牙权限',
        duration: 2000
      });
      return;
    }

    if (this.isScanning) {
      return;
    }

    try {
      // 清空之前的结果
      this.deviceList = [];

      let scanFilter: ble.ScanFilter = {
        name: 'XXXXXXXX'
      };
      // Setting Scan Parameters
      let scanOptions: ble.ScanOptions = {
        interval: 100,
        dutyMode: ble.ScanDuty.SCAN_MODE_LOW_LATENCY,
        matchMode: ble.MatchMode.MATCH_MODE_AGGRESSIVE
      };

      ble.on('BLEDeviceFind', (data) => {
        console.info('testTag', `scan result = ${data[0].deviceId}`);
        console.info('BLEScannerDemo: 扫描结果:', JSON.stringify(data));
        this.scanCallback(data);
      });

      // 开始扫描
      await ble.startBLEScan([scanFilter], scanOptions);
      console.info('BLEScannerDemo: 开始扫描');

      this.isScanning = true;
      this.promptAction.showToast({
        message: '开始扫描BLE设备',
        duration: 2000
      });

      console.info('BLE扫描已启动');

      // 30秒后自动停止扫描（节省电量）
      setTimeout(() => {
        if (this.isScanning) {
          this.stopScan();
        }
      }, 30000);

    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error('开始扫描失败:', err.code, err.message);
      this.promptAction.showToast({
        message: `扫描失败: ${err.message}`,
        duration: 3000
      });
    }
  }
  ```

  **说明** 

  使用蓝牙能力时，需要在module.json5中添加ohos.permission.ACCESS\_BLUETOOTH权限。

  完整示例参考如下：

  ```ts
  import { ble } from '@kit.ConnectivityKit';
  import { BusinessError } from '@kit.BasicServicesKit';
  import { abilityAccessCtrl, common, Permissions } from '@kit.AbilityKit';
  import { PromptAction } from '@kit.ArkUI';
  import { JSON } from '@kit.ArkTS';
  import { bundleManager } from '@kit.AbilityKit';

  // BLE设备信息接口
  interface BLEDeviceInfo {
    deviceId: string;
    deviceName: string;
    rssi: number;
    manufactureData?: ArrayBuffer;
    serviceUuids?: Array<string>;
  }

  @Entry
  @Component
  struct BLEScannerDemo {
    // 扫描状态
    @State isScanning: boolean = false;
    // 扫描结果列表
    @State deviceList: Array<BLEDeviceInfo> = [];
    // 权限状态
    context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    uiContext: UIContext = this.getUIContext();
    promptAction: PromptAction = this.uiContext.getPromptAction();

    // BLE扫描回调
    scanCallback(data: Array<ble.ScanResult>) {
      // 扫描到设备时触发
      data.forEach(device => {
        console.info(`发现设备: ${device.deviceId}, RSSI: ${device.rssi}`);

        // 检查是否已存在该设备
        const existingIndex = this.deviceList.findIndex(item => item.deviceId === device.deviceId);

        if (existingIndex !== -1) {
          // 更新已有设备信息
          this.deviceList[existingIndex] = {
            deviceId: device.deviceId,
            deviceName: device.deviceName || '未知设备',
            rssi: device.rssi,

          };
        } else {
          // 添加新设备
          const newDevice: BLEDeviceInfo = {
            deviceId: device.deviceId,
            deviceName: device.deviceName || '未知设备',
            rssi: device.rssi,
          };
          this.deviceList.push(newDevice);
        }

        // 触发UI更新
        this.deviceList = [...this.deviceList];

      });

    }

    // 页面显示时初始化
    aboutToAppear(): void {
      const atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
      atManager.requestPermissionsFromUser(this.context, ['ohos.permission.ACCESS_BLUETOOTH'], (err: BusinessError) => {
        if (err) {
          console.error('权限申请失败');
        } else {
          console.info('权限申请成功');
        }
      });
    }

    //校验权限
    async checkPermissionGrant(permission: Permissions): Promise<abilityAccessCtrl.GrantStatus> {
      let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
      let grantStatus: abilityAccessCtrl.GrantStatus = abilityAccessCtrl.GrantStatus.PERMISSION_DENIED;

      // 获取应用程序的accessTokenID。
      let tokenId: number = 0;
      try {
        let bundleInfo: bundleManager.BundleInfo =
          await bundleManager.getBundleInfoForSelf(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
        let appInfo: bundleManager.ApplicationInfo = bundleInfo.appInfo;
        tokenId = appInfo.accessTokenId;
      } catch (error) {
        const err: BusinessError = error as BusinessError;
        console.error(`Failed to get bundle info for self, code: ${err.code}, message: ${err.message}`);
      }

      // 校验应用是否被授予权限。
      try {
        grantStatus = await atManager.checkAccessToken(tokenId, permission);
      } catch (error) {
        const err: BusinessError = error as BusinessError;
        console.error(`Failed to check access token, code: ${err.code}, message: ${err.message}`);
      }

      return grantStatus;
    }

    // 开始扫描
    async startScan(): Promise<void> {
      let grantStatus: boolean = await this.checkPermissionGrant('ohos.permission.ACCESS_BLUETOOTH') ===
      abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED;
      if (!grantStatus) {
        this.promptAction.showToast({
          message: '请先申请蓝牙权限',
          duration: 2000
        });
        return;
      }

      if (this.isScanning) {
        return;
      }

      try {
        // 清空之前的结果
        this.deviceList = [];

        let scanFilter: ble.ScanFilter = {
          name: 'XXXXXXXX'
        };
        // Setting Scan Parameters
        let scanOptions: ble.ScanOptions = {
          interval: 100,
          dutyMode: ble.ScanDuty.SCAN_MODE_LOW_LATENCY,
          matchMode: ble.MatchMode.MATCH_MODE_AGGRESSIVE
        };

        ble.on('BLEDeviceFind', (data) => {
          console.info('testTag', `scan result = ${data[0].deviceId}`);
          console.info('BLEScannerDemo: 扫描结果:', JSON.stringify(data));
          this.scanCallback(data);
        });

        // 开始扫描
        await ble.startBLEScan([scanFilter], scanOptions);
        console.info('BLEScannerDemo: 开始扫描');

        this.isScanning = true;
        this.promptAction.showToast({
          message: '开始扫描BLE设备',
          duration: 2000
        });

        console.info('BLE扫描已启动');

        // 30秒后自动停止扫描（节省电量）
        setTimeout(() => {
          if (this.isScanning) {
            this.stopScan();
          }
        }, 30000);

      } catch (error) {
        const err: BusinessError = error as BusinessError;
        console.error('开始扫描失败:', err.code, err.message);
        this.promptAction.showToast({
          message: `扫描失败: ${err.message}`,
          duration: 3000
        });
      }
    }

    // 停止扫描
    async stopScan(): Promise<void> {
      if (!this.isScanning) {
        return;
      }

      try {

        await ble.stopBLEScan();
        this.isScanning = false;
        console.info('BLEScannerDemo: 停止扫描');
        this.promptAction.showToast({
          message: `扫描结束，发现 ${this.deviceList.length} 个设备`,
          duration: 3000
        });
        console.info('BLE扫描已停止');
        ble.off('BLEDeviceFind');
      } catch (error) {
        const err: BusinessError = error as BusinessError;
        console.error('停止扫描失败:', err.code, err.message);
        this.promptAction.showToast({
          message: `停止扫描失败: ${err.message}`,
          duration: 3000
        });
      }
    }

    // 清空结果
    clearResults(): void {
      this.deviceList = [];
      this.promptAction.showToast({
        message: '已清空扫描结果',
        duration: 2000
      });
    }

    // 格式化设备信息用于显示
    formatDeviceInfo(device: BLEDeviceInfo): string {
      let info = `名称: ${device.deviceName}\n`;
      info += `ID: ${device.deviceId}\n`;
      info += `信号强度: ${device.rssi} dBm`;

      if (device.serviceUuids && device.serviceUuids.length > 0) {
        info += `\n服务UUID: ${device.serviceUuids.length} 个`;
      }

      return info;
    }

    build() {
      Column({ space: 20 }) {
        // 标题
        Text('BLE设备扫描器')
          .fontSize(24)
          .fontWeight(FontWeight.Bold)
          .margin({ top: 20 })

        // 扫描状态显示
        Row({ space: 10 }) {
          Text('扫描状态:')
            .fontSize(16)
          Text(this.isScanning ? '扫描中...' : '已停止')
            .fontSize(16)
            .fontColor(this.isScanning ? Color.Green : Color.Gray)
        }
        .margin({ top: 10 })

        // 控制按钮
        Row({ space: 20 }) {
          Button(this.isScanning ? '停止扫描' : '开始扫描')
            .backgroundColor(this.isScanning ? Color.Orange : Color.Blue)
            .fontColor(Color.White)
            .padding(10)
            .borderRadius(8)
            .onClick(() => {
              if (this.isScanning) {
                this.stopScan();
              } else {
                this.startScan();
              }
            })

          Button('清空结果')
            .backgroundColor(Color.Gray)
            .fontColor(Color.White)
            .padding(10)
            .borderRadius(8)
            .onClick(() => this.clearResults())
            .enabled(this.deviceList.length > 0 && !this.isScanning)
        }
        .margin({ top: 20 })

        // 设备数量统计
        Text(`发现设备: ${this.deviceList.length} 个`)
          .fontSize(16)
          .fontColor(Color.Blue)
          .margin({ top: 10 })

        // 设备列表
        if (this.deviceList.length > 0) {
          List({ space: 10 }) {
            ForEach(this.deviceList, (device: BLEDeviceInfo) => {
              ListItem() {
                Column({ space: 8 }) {
                  // 设备名称和信号强度
                  Row() {
                    Text(device.deviceName)
                      .fontSize(18)
                      .fontWeight(FontWeight.Bold)
                      .layoutWeight(1)

                    // 信号强度指示
                    Text(`${device.rssi} dBm`)
                      .fontSize(14)
                      .fontColor(this.getRSSIColor(device.rssi))
                  }
                  .width('100%')

                  // 设备ID
                  Text(`ID: ${device.deviceId}`)
                    .fontSize(12)
                    .fontColor(Color.Gray)
                    .width('100%')
                    .textOverflow({ overflow: TextOverflow.Ellipsis })

                  // 附加信息
                  if (device.manufactureData || device.serviceUuids) {
                    Text(this.getAdditionalInfo(device))
                      .fontSize(12)
                      .fontColor(Color.Green)
                      .width('100%')
                  }
                }
                .padding(12)
                .backgroundColor(Color.White)
                .borderRadius(8)
                .shadow({
                  radius: 2,
                  color: Color.Gray,
                  offsetX: 1,
                  offsetY: 1
                })
                .margin({ top: 5, bottom: 5 })
              }
            }, (device: BLEDeviceInfo) => device.deviceId)
          }
          .width('100%')
          .height('60%')
          .margin({ top: 10 })
          .divider({
            strokeWidth: 1,
            color: Color.Gray,
            startMargin: 10,
            endMargin: 10
          })
        } else {
          // 空状态提示
          Column({ space: 20 }) {

            Text(this.isScanning ? '正在搜索附近的BLE设备...' : '点击"开始扫描"搜索BLE设备')
              .fontSize(16)
              .fontColor(Color.Gray)
              .textAlign(TextAlign.Center)
          }
          .height('60%')
          .justifyContent(FlexAlign.Center)
          .margin({ top: 40 })
        }
      }
      .width('100%')
      .height('100%')
      .padding(16)
      .backgroundColor(Color.White)
    }

    // 根据RSSI值获取颜色
    private getRSSIColor(rssi: number): ResourceColor {
      if (rssi >= -50) {
        return Color.Green;
      }
      if (rssi >= -70) {
        return Color.Blue;
      }
      if (rssi >= -85) {
        return Color.Orange;
      }
      return Color.Red;
    }

    // 获取附加信息
    private getAdditionalInfo(device: BLEDeviceInfo): string {
      const info: string[] = [];

      if (device.manufactureData) {
        info.push('有制造商数据');
      }

      if (device.serviceUuids && device.serviceUuids.length > 0) {
        info.push(`${device.serviceUuids.length}个服务`);
      }

      return info.join(' | ');
    }

    // 页面销毁时停止扫描
    aboutToDisappear(): void {
      if (this.isScanning) {
        this.stopScan();
      }
    }
  }
  ```
* **方案二**：

  [ble.startBLEScan](../harmonyos-references/js-apis-bluetooth-ble.md#blestartblescan)发起BLE扫描流程时，可以选择SCAN\_MODE\_LOW\_LATENCY扫描模式，减少蓝牙扫描的时间，提高扫描发现效率。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/tpGVTuDFStK00MWXdT-YLQ/zh-cn_image_0000002658851753.png "点击放大")

## 总结

1. 低功耗蓝牙建连过程，对端BLE设备发广播的强度，本端设备和对端BLE设备的距离都可能造成蓝牙连接失败，需要保持在连接范围内。
2. 首次蓝牙连接后，可保存MAC地址或设备名等信息作为ScanFilter参数，提高连接效率。

## 常见FAQ

Q：ScanFilter指的是结果中被过滤掉（不包含）的部分，还是过滤出（仅包含）的意思？

A：是过滤出（仅包含）的意思。

Q：蓝牙扫描怎么取消过滤条件？

A：将startBLEScan过滤条件传入为null。
