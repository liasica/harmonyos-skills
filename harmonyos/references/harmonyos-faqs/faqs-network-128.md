---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-128
title: 如何在使用移动流量时进行相应提示
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 如何在使用移动流量时进行相应提示
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0302101e9b06e3fd0c290860208761233d798943f94ff5dd675534652432d1e3
---

## 问题现象

用户切换网络至移动流量时，应用应进行相应提示，然而应用未进行提示。

## 背景知识

* [on('netCapabilitiesChange')](../harmonyos-references/js-apis-net-connection.md#onnetcapabilitieschange)可订阅网络能力变化事件。
* 设备从Wi-Fi到移动数据会触发netLost事件（Wi-Fi丢失）之后触发netAvailable事件（移动数据可用）、netCapabilitiesChange事件和netConnectionPropertiesChange事件。
* [connection.getNetCapabilities](../harmonyos-references/js-apis-net-connection.md#connectiongetnetcapabilities)可获取netHandle对应网络的能力信息，使用callback方式作为异步方法。

## 解决方案

使用getNetCapabilities获取进入页面时的网络类型，并使用on('netCapabilitiesChange')监听网络类型变化。关键内容如下：

```ts
aboutToAppear(): void {
  // 获取页面创建时的网络类型
  connection.getDefaultNet()
    .then((netHandle: connection.NetHandle) => {
      if (netHandle.netId === 0) {
        // 当前没有已连接的网络时，netHandle的netId为0，属于异常场景。
        return;
      }
      connection.getNetCapabilities(netHandle, (error: BusinessError, data: connection.NetCapabilities) => {
        if (error) {
          return;
        }
        if (data.bearerTypes.length > 0) {
          let netType = data.bearerTypes[0]; // 获取网络类型
          // 使用流量
          if (netType === connection.NetBearType.BEARER_CELLULAR) {
            this.showDialog = true;
          } else {
            this.change = true;
          }
        }
      });
    })
    .catch((error: BusinessError) => {
      console.error(`Failed to get default net. Code:${error.code}, message:${error.message}`);
    });

  // 监听网络类型切换
  this.netCon.on('netCapabilitiesChange', (data: connection.NetCapabilityInfo) => {
    if (data.netCap.bearerTypes.length > 0) {
      let netType = data.netCap.bearerTypes[0]; // 获取当前网络类型
      // 当前网络为数据流量时进行提示
      if (netType === connection.NetBearType.BEARER_CELLULAR && this.change) {
        this.showDialog = true;
      }
    }
  });

  // 使用register接口注册网络状态变化事件。
  this.netCon.register((error: BusinessError) => {
    console.error(JSON.stringify(error));
  });
}
```

完整示例如下：

```ts
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

@CustomDialog
struct CustomDialogExample {
  @Consume('net') netState: string;
  controller?: CustomDialogController;

  build() {
    Column() {
      Text(this.netState)
        .fontSize(16)
        .textAlign(TextAlign.Center);

      Row() {
        Button('取消')
          .fontSize(16)
          .fontColor('#0A59F7')
          .backgroundColor(Color.Transparent)
          .width(120)
          .height(40)
          .borderRadius('50%');
        Button('确认')
          .fontSize(16)
          .backgroundColor('#0A59F7')
          .fontColor(Color.White)
          .width(120)
          .height(40)
          .borderRadius('50%');
      }
      .margin({ top: 20 })
      .width('100%')
      .justifyContent(FlexAlign.SpaceAround);
    }
    .padding(20);
  }
}

@Entry
@Component
struct NetworkDemo {
  @Provide('net') netState: string = '';
  @State change: boolean = false; // 是否使用流量
  @State @Watch('myShow') showDialog: boolean = false;
  private netCon: connection.NetConnection = connection.createNetConnection();
  dialogControllerConfirm: CustomDialogController = new CustomDialogController({
    builder: CustomDialogExample(),
    width: 300,
    cornerRadius: 40,
    onWillDisappear: () => {
      this.showDialog = false;
    }
  });

  myShow() {
    if (this.showDialog) {
      this.netState = '正在使用数据流量播放，请注意流量消耗。';
      this.dialogControllerConfirm.open();
    }
  }

  aboutToAppear(): void {
    // 获取页面创建时的网络类型
    connection.getDefaultNet()
      .then((netHandle: connection.NetHandle) => {
        if (netHandle.netId === 0) {
          // 当前没有已连接的网络时，netHandle的netId为0，属于异常场景。
          return;
        }
        connection.getNetCapabilities(netHandle, (error: BusinessError, data: connection.NetCapabilities) => {
          if (error) {
            return;
          }
          if (data.bearerTypes.length > 0) {
            let netType = data.bearerTypes[0]; // 获取网络类型
            // 使用流量
            if (netType === connection.NetBearType.BEARER_CELLULAR) {
              this.showDialog = true;
            } else {
              this.change = true;
            }
          }
        });
      })
      .catch((error: BusinessError) => {
        console.error(`Failed to get default net. Code:${error.code}, message:${error.message}`);
      });

    // 监听网络类型切换
    this.netCon.on('netCapabilitiesChange', (data: connection.NetCapabilityInfo) => {
      if (data.netCap.bearerTypes.length > 0) {
        let netType = data.netCap.bearerTypes[0]; // 获取当前网络类型
        // 当前网络为数据流量时进行提示
        if (netType === connection.NetBearType.BEARER_CELLULAR && this.change) {
          this.showDialog = true;
        }
      }
    });

    // 使用register接口注册网络状态变化事件。
    this.netCon.register((error: BusinessError) => {
      console.error(JSON.stringify(error));
    });
  }

  aboutToDisappear(): void {
    this.netCon.unregister((error: BusinessError) => {
      console.error(JSON.stringify(error));
    });
  }

  build() {
    Column()
      .height('100%')
      .width('100%');
  }
}
```
