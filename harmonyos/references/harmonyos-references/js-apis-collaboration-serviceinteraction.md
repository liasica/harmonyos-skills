---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-collaboration-serviceinteraction
title: "@hms.collaboration.serviceInteraction (碰一碰)"
breadcrumb: API参考 > 系统 > 网络 > Service Collaboration Kit（协同服务） > ArkTS API > @hms.collaboration.serviceInteraction (碰一碰)
category: harmonyos-references
scraped_at: 2026-09-05T06:19:09+08:00
doc_updated_at: 2026-09-04
content_hash: sha256:5f34c3472b1eb9440272d50635a5ae6486c3de9623f8fb93311c7368798766c8
---

本模块提供碰一碰能力，包括设备间通过顶端碰的方式触发连接、传递信息、断开连接等。

**起始版本：** 26.0.0

## 导入模块

```typescript
import { serviceInteraction } from '@kit.ServiceCollaborationKit';
```

## TriggerType

枚举类型，表示触发碰一碰的方式。

**系统能力：** SystemCapability.Collaboration.Connection

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**起始版本：** 26.0.0

| 名称 | 值 | 说明 |
| --- | --- | --- |
| KNOCK | 'knock' | 设备间通过顶端碰的方式触发碰一碰。 |

## CollaborationConfig

注册碰一碰回调方法的参数配置。

**系统能力：** SystemCapability.Collaboration.Connection

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| triggerType | [TriggerType](js-apis-collaboration-serviceinteraction.md#triggertype) | 否 | 否 | 触发碰一碰的方式。目前仅支持'knock'方式。 |
| windowId | number | 否 | 否 | 应用窗口ID。多窗口注册时使用的窗口ID，用于区分不同窗口的回调注册。通过[this.getUIContext().getWindowId()](arkts-apis-uicontext-uicontext.md#getwindowid23)获取。 |
| appLinking | string | 否 | 是 | 应用链接。用于在碰一碰后跳转到指定应用页面的链接，格式为URL。 |
| timeOut | number | 否 | 是 | 超时时间。在无数据传输后自动断开连接的时间，值为整数，默认值为20。单位：秒。 |

## Connection

设备间建链的链接管理对象，用于管理连接、发送消息和断开连接。

**系统能力：** SystemCapability.Collaboration.Connection

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| connectId | number | 否 | 否 | 设备间建链对应的链接ID。唯一标识一个连接会话，用于区分不同的连接设备。 |

### sendMessage

sendMessage(data: ArrayBuffer): Promise<void>

向连接中的对端设备传递信息。使用Promise异步回调。

**系统能力：** SystemCapability.Collaboration.Connection

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.KNOCK\_COLLABORATION

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | ArrayBuffer | 是 | 需要向对端传递的信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[错误码](errorcode-servicecollaboration.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The permissions check failed. |
| 1028501001 | IPC communication exception. |
| 1028501002 | Invalid parameter. |

**示例：**

参考[示例](js-apis-collaboration-serviceinteraction.md#示例)。

### disconnect

disconnect(): Promise<void>

断开与对端设备的连接。使用Promise异步回调。

**系统能力：** SystemCapability.Collaboration.Connection

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.KNOCK\_COLLABORATION

**起始版本：** 26.0.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[错误码](errorcode-servicecollaboration.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The permissions check failed. |
| 1028501001 | IPC communication exception. |

**示例：**

参考[示例](js-apis-collaboration-serviceinteraction.md#示例)。

## ServiceInteractionCallback

注册碰一碰回调方法所需的回调对象。

**系统能力：** SystemCapability.Collaboration.Connection

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**起始版本：** 26.0.0

### onDeviceConnect

onDeviceConnect(connection: Connection): void

连接对端设备成功。

**系统能力：** SystemCapability.Collaboration.Connection

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| connection | [Connection](js-apis-collaboration-serviceinteraction.md#connection) | 是 | 设备间建链的链接管理对象。包含连接ID和操作方法，可用于发送消息和断开连接。 |

**示例：**

参考[示例](js-apis-collaboration-serviceinteraction.md#示例)。

### onDeviceDisconnect

onDeviceDisconnect(connection: Connection, retCode: number): void;

对端设备断开连接时触发的回调。当连接断开时，系统会调用此方法。

**系统能力：** SystemCapability.Collaboration.Connection

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| connection | [Connection](js-apis-collaboration-serviceinteraction.md#connection) | 是 | 设备间建链的链接管理对象。包含连接ID和操作方法，可用于发送消息和断开连接。 |
| retCode | number | 是 | 连接对端设备的状态码，表示断开连接的原因。值为整数，0表示正常断开，非0表示异常断开。 |

**示例：**

参考[示例](js-apis-collaboration-serviceinteraction.md#示例)。

### onMessageReceive

onMessageReceive(connection: Connection, data: ArrayBuffer): void

收到对端发送信息时触发的回调。当对端设备通过Connection对象发送消息时，本端会收到此回调。

**系统能力：** SystemCapability.Collaboration.Connection

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| connection | [Connection](js-apis-collaboration-serviceinteraction.md#connection) | 是 | 设备间建链的链接管理对象。包含连接ID和操作方法，可用于发送消息和断开连接。 |
| data | ArrayBuffer | 是 | 本端收到的对端发送信息。 |

**示例：**

参考[示例](js-apis-collaboration-serviceinteraction.md#示例)。

### onConnectFail

onConnectFail(retCode: number): void

连接对端设备失败时触发的回调。当设备间通过碰一碰方式尝试建立连接失败时，系统会调用此方法。

**系统能力：** SystemCapability.Collaboration.Connection

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| retCode | number | 是 | 连接对端设备的状态码，表示连接失败的原因。值为整数，非0表示连接失败。 |

**示例：**

参考[示例](js-apis-collaboration-serviceinteraction.md#示例)。

## onServiceInteraction

onServiceInteraction(config: CollaborationConfig, callbacks: ServiceInteractionCallback): void

注册碰一碰回调方法，注册成功后，当设备间通过碰一碰方式触发连接时，系统会调用相应的回调方法。

**系统能力：** SystemCapability.Collaboration.Connection

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.KNOCK\_COLLABORATION

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [CollaborationConfig](js-apis-collaboration-serviceinteraction.md#collaborationconfig) | 是 | 注册碰一碰回调方法的参数。包含触发方式、窗口ID、应用链接和超时时间等配置。 |
| callbacks | [ServiceInteractionCallback](js-apis-collaboration-serviceinteraction.md#serviceinteractioncallback) | 是 | 注册碰一碰回调方法所需的回调对象。包含设备连接、断开、消息接收和连接失败的回调方法。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[错误码](errorcode-servicecollaboration.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The permissions check failed. |
| 1028501001 | IPC communication exception. |
| 1028501002 | Invalid parameter. |

**示例：**

参考[示例](js-apis-collaboration-serviceinteraction.md#示例)。

## offServiceInteraction

offServiceInteraction(config: CollaborationConfig, callbacks?: ServiceInteractionCallback): void

取消注册碰一碰回调方法。调用此方法后，将不再收到设备连接、断开、消息接收等事件回调。

**系统能力：** SystemCapability.Collaboration.Connection

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.KNOCK\_COLLABORATION

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [CollaborationConfig](js-apis-collaboration-serviceinteraction.md#collaborationconfig) | 是 | 注册碰一碰回调方法的参数。包含触发方式、窗口ID、应用链接和超时时间等配置。 |
| callbacks | [ServiceInteractionCallback](js-apis-collaboration-serviceinteraction.md#serviceinteractioncallback) | 否 | 解注册碰一碰回调方法所需的回调对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[错误码](errorcode-servicecollaboration.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The permissions check failed. |
| 1028501001 | IPC communication exception. |
| 1028501002 | Invalid parameter. |

**示例：**

参考[示例](js-apis-collaboration-serviceinteraction.md#示例)。

## 示例

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
   * 1. 注册监听（只注册一次）
   *
   * 重要：此回调可能会被多次调用，每次设备相碰都会触发
   * 每次调用返回一个新的Connection对象
   */
  private registerServiceInteraction(): void {
    const config: serviceInteraction.CollaborationConfig = {
      triggerType: serviceInteraction.TriggerType.KNOCK,
      windowId: this.windowId,
      appLinking: this.appLinking
    };

    // 2. 处理回调：统一入口处理所有连接事件
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
   * 3. 多Connection处理：添加新连接
   *
   * 每次设备相碰都会调用此方法，创建一个新的ConnectionInfo
   */
  private addConnection(connection: serviceInteraction.Connection): void {
    // 检查是否已存在相同connectionId的连接
    const exists = this.connectionList.some(
      item => item.connection.connectId === connection.connectId
    );

    if (exists) {
      hilog.info(0, 'MEMOMOCK', '连接已存在，connectionId: ' + connection.connectId);
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

    hilog.info(0, 'MEMOMOCK', '新连接成功，connectionId: ' + connection.connectId +
      '，当前连接数: ' + this.connectionList.length);
  }

  /**
   * 处理断开连接（通过connectionId识别连接）
   */
  private onDisconnected(connection: serviceInteraction.Connection, retCode: number): void {
    const index = this.connectionList.findIndex(
      item => item.connection.connectId === connection.connectId
    );

    if (index > -1) {
      this.connectionList.splice(index, 1);
      hilog.info(0, 'MEMOMOCK', '连接已断开，connectionId: ' + connection.connectId + '，retCode: ' + retCode);
    }

    this.updateConnectionStatus();
  }

  /**
   * 处理消息接收（通过connectionId识别连接）
   */
  private onMessageReceived(connection: serviceInteraction.Connection, data: ArrayBuffer): void {
    const connectionInfo = this.connectionList.find(
      item => item.connection === connection
    );

    const deviceName = connectionInfo ? connectionInfo.deviceName : '未知设备';
    hilog.info(0, 'MEMOMOCK', '收到消息，设备: ' + deviceName + '，connectionId: ' + connection.connectId);
    let decoder = util.TextDecoder.create('utf-8');
    let str = decoder.decodeToString(new Uint8Array(data));
    hilog.info(0, 'MEMOMOCK', 'data: ' + data + '，str: ' + str);
    this.receivedMessage = str;
  }

  /**
   * 更新连接状态
   */
  private updateConnectionStatus(): void {
    this.connectionStatus = this.connectionList.length > 0
      ? '已连接 ' + this.connectionList.length + ' 台设备'
      : '未连接';
  }

  /**
   * 断开所有连接
   */
  private disconnectAll(): void {
    this.connectionList.forEach(item => {
      item.connection.disconnect();
    });
    this.connectionList = [];
    this.updateConnectionStatus();
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
        Button('给已连接设备发送消息').onClick(() => {
          this.connectionList.forEach((connnection) => {
            let textEncoder: util.TextEncoder = new util.TextEncoder();
            let uint8Array = new Uint8Array(textEncoder.encodeInto(this.sendMessage).length);
            textEncoder.encodeIntoUint8Array(this.sendMessage, uint8Array);
            try {
              connnection.connection.sendMessage(uint8Array.buffer);
            } catch (error) {
              hilog.error(0, 'MEMOMOCK', '发送消息失败，message：' + error.message);
            }
          })
        })

        Button('断连').onClick(() => {
          this.connectionList.forEach((connnection) => {
            try {
              connnection.connection.disconnect();
            } catch (error) {
              hilog.error(0, 'MEMOMOCK', '断开连接失败，message：' + error.message);
            }
          })
        })
      }

      if(this.receivedMessage != '' && this.connectionList.length > 0){
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
