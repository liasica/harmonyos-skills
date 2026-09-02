---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/serviceinteraction-dev-guides
title: 碰一碰实现设备间交互
breadcrumb: 指南 > 系统 > 网络 > Service Collaboration Kit（协同服务） > 碰一碰实现设备间交互
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:35+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:0eaf5ca8ca0fa21ce0c78d0c5f66ff154d0c2226374afa8fb8548dc7ba71ab45
---

## 概述

从API版本26.0.0开始，新增碰一碰能力，提供顶端触碰方式，实现设备间的快速连接并进行数据交互。

在日常使用中，用户经常需要在两台设备之间快速传输数据或协同操作。例如，在聚会时想要交换名片、在游戏中想要邀请好友加入、在购物时想要分享商品信息等。传统的方式通常需要通过蓝牙配对、扫码添加好友等繁琐步骤，操作复杂且耗时。

碰一碰提供了一种简单直观的解决方案：用户只需将两台设备轻轻一碰，即可快速建立连接并进行数据传输。这种方式无需复杂的配对过程，操作简单自然，大大提升了用户体验。

## 实现原理

碰一碰基于设备的近场通信能力，通过顶端碰的方式触发连接建立。当两台设备相碰时会自动识别并建立连接，然后通过回调机制通知应用。应用可以通过Connection对象发送消息，并通过回调接收消息。

## 约束与限制

### 设备限制

设备需要打开WLAN和蓝牙开关。

### 权限限制

需要申请权限[ohos.permission.KNOCK\_COLLABORATION](restricted-permissions.md#ohospermissionknock_collaboration)，该能力受限开放。权限申请方式请参见[申请使用受限权限](declare-permissions-in-acl.md)。

## 接口说明

碰一碰关键接口如下表所示。具体API说明详见[接口文档](../harmonyos-references/js-apis-collaboration-serviceinteraction.md)。

| 接口名 | 描述 |
| --- | --- |
| onServiceInteraction(config: CollaborationConfig, callbacks: ServiceInteractionCallback): void | 注册碰一碰回调方法。 |
| offServiceInteraction(config: CollaborationConfig, callbacks?: ServiceInteractionCallback): void | 取消注册碰一碰回调方法。 |
| Connection.sendMessage(data: ArrayBuffer): Promise<void> | 向连接中的对端设备传递信息。使用Promise异步回调。 |
| Connection.disconnect(): Promise<void> | 断开与对端设备的连接。使用Promise异步回调。 |

## 开发步骤

1. 导入serviceInteraction模块以及其他必要的工具模块。

   ```typescript
   import { serviceInteraction } from '@kit.ServiceCollaborationKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { util } from '@kit.ArkTS';
   ```
2. 创建[CollaborationConfig](../harmonyos-references/js-apis-collaboration-serviceinteraction.md#collaborationconfig)对象，配置触发类型、窗口ID等参数。

   ```typescript
   const config: serviceInteraction.CollaborationConfig = {
     triggerType: serviceInteraction.TriggerType.KNOCK,
     windowId: 1, // 此处示例传入1，具体开发场景可通过this.getUIContext().getWindowId(); 来获取windowId。
     appLinking: 'https://example.com/app',
     timeOut: 10 // 可选，默认值为20秒
   };
   ```
3. 通过[onServiceInteraction](../harmonyos-references/js-apis-collaboration-serviceinteraction.md#onserviceinteraction)接口注册回调方法，处理设备连接、断连、消息接收等事件。

   ```typescript
   const callback: serviceInteraction.ServiceInteractionCallback = {
     onDeviceConnect: (connection: serviceInteraction.Connection) => {
       // 设备连接成功
       hilog.info(0, 'MEMOMOCK', '设备连接成功，connectId: ' + connection.connectId);
     },
     onDeviceDisconnect: (connection: serviceInteraction.Connection, retCode: number) => {
       // 设备断开连接
       hilog.info(0, 'MEMOMOCK', '设备断开连接，connectId: ' + connection.connectId + '，retCode: ' + retCode);
     },
     onMessageReceive: (connection: serviceInteraction.Connection, data: ArrayBuffer) => {
       // 收到对端消息
       hilog.info(0, 'MEMOMOCK', '收到消息，connectId: ' + connection.connectId);
     },
     onConnectFail: (retCode: number) => {
       // 连接失败
       hilog.error(0, 'MEMOMOCK', '连接失败，retCode: ' + retCode);
     }
   };

   try {
     serviceInteraction.onServiceInteraction(config, callback);
     hilog.info(0, 'MEMOMOCK', '注册成功');
   } catch (error) {
     hilog.error(0, 'MEMOMOCK', '注册失败，message：' + error.message);
   }
   ```
4. 通过[Connection](../harmonyos-references/js-apis-collaboration-serviceinteraction.md#connection)对象的[sendMessage](../harmonyos-references/js-apis-collaboration-serviceinteraction.md#sendmessage)方法向对端设备发送消息。

   ```typescript
   // 发送消息
   const message: string = 'Hello from device A';
   const textEncoder: util.TextEncoder = new util.TextEncoder();
   const uint8Array = new Uint8Array(textEncoder.encodeInto(message).length);
   textEncoder.encodeIntoUint8Array(message, uint8Array);

   try {
     connection.sendMessage(uint8Array.buffer).then(() => {
       hilog.info(0, 'MEMOMOCK', '消息发送成功');
     }).catch((error: Error) => {
       hilog.error(0, 'MEMOMOCK', '消息发送失败: ' + error.message);
     });
   } catch (error) {
     hilog.error(0, 'MEMOMOCK', '发送失败，message：' + error.message);
   }
   ```
5. 通过[Connection](../harmonyos-references/js-apis-collaboration-serviceinteraction.md#connection)对象的[disconnect](../harmonyos-references/js-apis-collaboration-serviceinteraction.md#disconnect)方法断开与对端设备的连接。

   ```typescript
   try {
     connection.disconnect().then(() => {
       hilog.info(0, 'MEMOMOCK', '断开连接成功');
     }).catch((error: Error) => {
       hilog.error(0, 'MEMOMOCK', '断开连接失败: ' + error.message);
     });
   } catch (error) {
     hilog.error(0, 'MEMOMOCK', '断开失败，message：' + error.message);
   }
   ```
6. 通过[offServiceInteraction](../harmonyos-references/js-apis-collaboration-serviceinteraction.md#offserviceinteraction)接口取消注册回调方法，停止接收回调事件。

   ```typescript
   // 取消注册回调
   try {
     serviceInteraction.offServiceInteraction(config);
     hilog.info(0, 'MEMOMOCK', '取消注册成功');
   } catch (error) {
     hilog.error(0, 'MEMOMOCK', '取消注册失败，message：' + error.message);
   }
   ```

### 调测验证

开发完成后，可以通过以下步骤验证功能：

1. 准备两台设备，并确保WLAN和蓝牙开关已打开。
2. 在两台设备上分别运行应用。
3. 将两台设备顶端轻轻一碰，观察是否触发连接回调。
4. 检查连接状态是否正确显示。
5. 在一台设备上发送消息，观察另一台设备是否收到消息。
6. 断开连接，观察断开回调是否正确触发。
7. 检查hilog日志，确认所有操作是否正常执行。

### 完整示例

以下示例展示了如何使用碰一碰功能实现双端设备交互的场景，包括消息发送和接收功能。

```typescript
import { serviceInteraction } from '@kit.ServiceCollaborationKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';

/**
 * 连接信息封装
 */
interface ConnectionInfo {
  connection: serviceInteraction.Connection;
  deviceName: string;
}

/**
 * 核心流程：
 * 1. 注册监听：只注册一次onServiceInteraction
 * 2. 处理回调：每次设备相碰会触发回调，返回新的Connection
 * 3. 多Connection处理：使用connectionList管理多个连接，每个连接独立设置回调
 */
@Entry
@Component
struct LuckyCardExchangePage {
  @State connectionStatus: string = '未连接';
  @State connectionList: ConnectionInfo[] = [];
  @State windowId: number = 0;
  private appLinking: string = 'https://example.com/luckycard/exchange';
  @State sendMessage: string = '';
  @State receivedMessage: string = '';

  aboutToAppear() {
    this.windowId = this.getUIContext().getWindowId() as number;
    this.registerServiceInteraction();
  }

  aboutToDisappear() {
    this.unregisterServiceInteraction();
    this.disconnectAll();
  }

  /**
   * 注册碰一碰监听
   */
  private registerServiceInteraction(): void {
    const config: serviceInteraction.CollaborationConfig = {
      triggerType: serviceInteraction.TriggerType.KNOCK,
      windowId: this.windowId,
      appLinking: this.appLinking
    };

    const callback: serviceInteraction.ServiceInteractionCallback = {
      onDeviceConnect: (connection: serviceInteraction.Connection) => {
        this.addConnection(connection);
      },
      onDeviceDisconnect: (connection: serviceInteraction.Connection, retCode: number) => {
        this.onDisconnected(connection, retCode);
      },
      onMessageReceive: (connection: serviceInteraction.Connection, data: ArrayBuffer) => {
        this.onMessageReceived(connection, data);
      },
      onConnectFail: (retCode: number) => {
        hilog.info(0, 'MEMOMOCK', '连接失败, 错误码是：' + retCode);
      },
    };

    try {
      serviceInteraction.onServiceInteraction(config, callback);
    } catch (error) {
      hilog.error(0, 'MEMOMOCK', '注册失败，message：' + error.message);
    }
    hilog.info(0, 'MEMOMOCK', '已注册服务交互监听');
  }

  /**
   * 取消注册监听
   */
  private unregisterServiceInteraction(): void {
    const config: serviceInteraction.CollaborationConfig = {
      triggerType: serviceInteraction.TriggerType.KNOCK,
      windowId: this.windowId,
      appLinking: this.appLinking
    };

    try {
      serviceInteraction.offServiceInteraction(config);
    } catch (error) {
      hilog.error(0, 'MEMOMOCK', '取消注册失败，message：' + error.message);
    }
    hilog.info(0, 'MEMOMOCK', '已取消服务交互监听');
  }

  /**
   * 添加新连接
   */
  private addConnection(connection: serviceInteraction.Connection): void {
    // 检查是否已存在相同connectId的连接
    const exists = this.connectionList.some(
      item => item.connection.connectId === connection.connectId
    );

    if (exists) {
      hilog.info(0, 'MEMOMOCK', '连接已存在，connectId: ' + connection.connectId);
      return;
    }

    // 创建新的连接信息
    const connectionInfo: ConnectionInfo = {
      connection: connection,
      deviceName: '设备' + (this.connectionList.length + 1)
    };
    // 添加到连接列表
    this.connectionList.push(connectionInfo);
    this.updateConnectionStatus();

    hilog.info(0, 'MEMOMOCK', '新连接成功，connectId: ' + connection.connectId +
      '，当前连接数: ' + this.connectionList.length);
  }

  /**
   * 处理断开连接
   */
  private onDisconnected(connection: serviceInteraction.Connection, retCode: number): void {
    const index = this.connectionList.findIndex(
      item => item.connection.connectId === connection.connectId
    );

    if (index > -1) {
      this.connectionList.splice(index, 1);
      hilog.info(0, 'MEMOMOCK', '连接已断开，connectId: ' + connection.connectId + '，retCode: ' + retCode);
    }

    this.updateConnectionStatus();
  }

  /**
   * 处理消息接收
   */
  private onMessageReceived(connection: serviceInteraction.Connection, data: ArrayBuffer): void {
    const connectionInfo = this.connectionList.find(
      item => item.connection === connection
    );

    const deviceName = connectionInfo ? connectionInfo.deviceName : '未知设备';
    hilog.info(0, 'MEMOMOCK', '收到消息，设备: ' + deviceName + '，connectId: ' + connection.connectId);

    // 解码消息内容
    const decoder = util.TextDecoder.create('utf-8');
    const str = decoder.decodeToString(new Uint8Array(data));
    hilog.info(0, 'MEMOMOCK', 'data: ' + data + '，str: ' + str);

    // 保存接收到的消息
    this.receivedMessage = str;
  }

  /**
   * 发送消息
   */
  private sendToAllDevices(): void {
    if (this.connectionList.length === 0) {
      hilog.warn(0, 'MEMOMOCK', '没有已连接的设备');
      return;
    }

    this.connectionList.forEach((connection) => {
      let textEncoder: util.TextEncoder = new util.TextEncoder();
      let uint8Array = new Uint8Array(textEncoder.encodeInto(this.sendMessage).length);
      textEncoder.encodeIntoUint8Array(this.sendMessage, uint8Array);
      try {
        connection.connection.sendMessage(uint8Array.buffer);
      } catch (error) {
        hilog.error(0, 'MEMOMOCK', '发送失败，message：' + error.message);
      }
    });
  }

  /**
   * 断开所有连接
   */
  private disconnectAll(): void {
    this.connectionList.forEach((connection) => {
      try {
        connection.connection.disconnect();
      } catch (error) {
        hilog.error(0, 'MEMOMOCK', '断开失败，message：' + error.message);
      }
    });
    this.connectionList = [];
    this.updateConnectionStatus();
  }

  /**
   * 更新连接状态
   */
  private updateConnectionStatus(): void {
    this.connectionStatus = this.connectionList.length > 0
      ? '已连接 ' + this.connectionList.length + ' 台设备'
      : '未连接';
  }

  build() {
    Column() {
      Text('碰一碰协同')
        .fontSize(24)
        .fontWeight(FontWeight.Bold)
        .margin({ top: 40, bottom: 20 })

      Text('连接状态: ' + this.connectionStatus)
        .fontSize(16)
        .margin({ bottom: 20 })

      if (this.connectionList.length > 0) {
        Text('已连接设备:')
          .fontSize(14)
          .margin({ bottom: 10 })

        ForEach(this.connectionList, (item: ConnectionInfo) => {
          Text(item.deviceName + ' (ID: ' + item.connection.connectId + ')')
            .fontSize(14)
            .margin({ bottom: 5 })
        })
      }

      Text('使用说明: 将两台设备相碰即可建立连接')
        .fontSize(12)
        .fontColor(Color.Gray)
        .margin({ top: 20 })

      if (this.connectionList.length > 0) {
        TextInput()
          .margin({ top: 20, bottom: 20 })
          .onChange((value) => {
            this.sendMessage = value;
          })

        Button('给已连接设备发送消息')
          .onClick(() => {
            this.sendToAllDevices();
          })

        Button('断连')
          .margin({ top: 10 })
          .onClick(() => {
            this.disconnectAll();
          })
      }

      if (this.receivedMessage != '' && this.connectionList.length > 0) {
        TextArea({
          text: this.receivedMessage
        })
          .margin({ top: 20, bottom: 20 })
      }
    }
    .width('100%')
    .height('100%')
    .padding(20)
  }
}
```
