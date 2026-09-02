---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-113
title: 移动数据关闭再打开后，如何监听IPv6已激活
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 移动数据关闭再打开后，如何监听IPv6已激活
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f869b94c19a7cad9993564d24463e53cff18a8a624c9fc21ca071fd98293c957
---

## 问题现象

使用移动网络，初次连接IPv6地址连接成功。关闭再打开移动数据开关后，再次连接IPv6地址，此时连接失败。在订阅网络事件netAvailable时打印连接信息时，发现初次连接，linkAddresses中包含IPv6地址。关闭再打开移动数据开关，此时打印linkAddresses中没有IPv6地址。

问题代码如下：

```ts
let conn = connection.createNetConnection();
conn.register((error: BusinessError) => {});
conn.on('netAvailable', ((netHandle: connection.NetHandle) => {
  let properties = connection.getConnectionPropertiesSync(netHandle);
  if (properties && properties.linkAddresses) {
    console.info(LOG_TAG, JSON.stringify(properties.linkAddresses))
  }
  // 连接socket
  this.connect()
}));
```

日志打印：

```txt
03-27 11:10:24.179   A03D00/com.exa...pv6test/JSAPP  apppool               I     ipv6_test [{"address":{"address":"10.74.xxx.6","family":1,"port":0},"prefixLength":32},{"address":{"address":"2409:8915:xxxx:xxxx:8e49","family":2,"port":0},"prefixLength":128}]
03-27 11:10:24.227   A03D00/com.exa...pv6test/JSAPP  com.example.ipv6test  I     ipv6_test socket connect result:true
03-27 11:10:30.012   A03D00/com.exa...pv6test/JSAPP  com.example.ipv6test  I     ipv6_test [{"address":{"address":"10.103.xxx.203","family":1,"port":0},"prefixLength":32}]
03-27 11:10:30.015   A03D00/com.exa...pv6test/JSAPP  com.example.ipv6test  I     ipv6_test tcp connect error:{"code":2301101,"message":"Network unreachable"}
03-27 11:10:30.015   A03D00/com.exa...pv6test/JSAPP  com.example.ipv6test  I     ipv6_test socket connect result:false
```

## 背景知识

* [on('netAvailable')](../harmonyos-references/js-apis-net-connection.md#onnetavailable)：订阅网络可用事件，当网络可用时触发该事件。
* [on('netConnectionPropertiesChange')](../harmonyos-references/js-apis-net-connection.md#onnetconnectionpropertieschange)：订阅网络连接信息变化事件，当网络连接信息变化时，如从无网络到有网络、从WiFi切换到蜂窝时，会触发该事件。打开网络，关闭网络，再打开网络的操作，是网络连接信息的变化，使用netConnectionPropertiesChange可以更加直观的监听网络。

## 解决方案

1. netAvailable表示当前有网络可用，但是不保证此时IPv4和IPv6都已就绪。
2. 当移动网络重启时，IPv4先激活，IPv6后激活。IPv4激活后就会触发netAvailable事件，因此使用IPv6前，请确认已分配有效的IPv6地址，否则连接会失败。
3. 使用netConnectionPropertiesChange事件，并判断IPv6是否激活，然后再连接。

   **说明** 

   需确保当前的IPv6链路可用。

   核心代码如下：

   ```ts
   conn.on('netConnectionPropertiesChange', ((date: connection.NetConnectionPropertyInfo) => {
     for (let i = 0; i < date.connectionProperties.linkAddresses.length; i++) {
       console.info(LOG_TAG, JSON.stringify(date.connectionProperties.linkAddresses));
       if (date.connectionProperties.linkAddresses[i].address.family === 2) {
         this.flag = true;
         this.connect();
         break;
       } else {
         this.flag = false;
       }
     }
   }));
   ```

   日志打印：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/5siwOP6TQoGkIKuufJbNVQ/zh-cn_image_0000002628610904.png "点击放大")

完整样例参考：

```ts
import { socket } from '@kit.NetworkKit';
import { connection } from '@kit.NetworkKit';

const LOG_TAG = 'hm-->';

@Entry
@Component
struct Index {
  flag: boolean = false;

  /**
   * connect
   */
  connect() {
    // 需替换有效的IPv6地址
    let address = '2409:8C3C:0904:x::x:xx';
    let port = 8206;
    // 创建相应协议的Socket对象
    let tcpSocket = new TcpSocket();
    tcpSocket.createSocket();
    // 连接服务器ip
    tcpSocket.connectSocket(address, port).then(res => {
      console.info(LOG_TAG, 'socket connect result:', res);
    }).catch((rej: Error) => {
      console.info(LOG_TAG, 'socket connect error:', rej);
    });
  }

  aboutToAppear(): void {
    let conn = connection.createNetConnection();
    conn.register(() => {
    });
    conn.on('netConnectionPropertiesChange', ((date: connection.NetConnectionPropertyInfo) => {
      for (let i = 0; i < date.connectionProperties.linkAddresses.length; i++) {
        console.info(LOG_TAG, JSON.stringify(date.connectionProperties.linkAddresses));
        if (date.connectionProperties.linkAddresses[i].address.family === 2) {
          this.flag = true;
          this.connect();
          break;
        } else {
          this.flag = false;
        }
      }
    }));
  }

  build() {
    Column() {
      Button('连接tcpSocket')
        .onClick(() => {
          if (this.flag) {
            this.connect();
          }
        })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}

class TcpSocket implements BaseSocket {
  private tcpSocket: socket.TCPSocket | null = null;

  /**
   * 创建Socket
   */
  async createSocket(): Promise<boolean> {
    try {
      if (this.tcpSocket) {
        this.tcpSocket.close();
        this.tcpSocket = null;
      }
      this.tcpSocket = socket.constructTCPSocketInstance();
      return true;
    } catch (e) {
      console.info(LOG_TAG, 'create socket error', e);
    }
    return false;
  }

  /**
   * 连接Socket
   */
  async connectSocket(address: string, port: number): Promise<boolean> {
    try {
      if (!this.tcpSocket) {
        return false;
      }

      if (await this.isConnected()) {
        return true;
      }
      //ipv4和ipv6类型设置
      let familyValue = 1;
      if (this.isValidIPv6Format(address)) {
        familyValue = 2;
      }
      await this.tcpSocket.connect({
        address: {
          address: address,
          port: port,
          family: familyValue
        },
        timeout: 6000,
      });
      await this.tcpSocket.setExtraOptions({
        keepAlive: true,
        receiveBufferSize: 1024 * 34,
        sendBufferSize: 1024 * 8,
        socketTimeout: 6000
      });
      return true;
    } catch (e) {
      console.info(LOG_TAG, 'tcp connect error', e);
    }
    return false;
  };

  /**
   * 判断是否连接
   */
  async isConnected(): Promise<boolean> {
    if (!this.tcpSocket) {
      return false;
    }
    ;

    try {
      let state: socket.SocketStateBase = await this.tcpSocket.getState();
      if (state.isConnected) {
        return true;
      }
    } catch (e) {
    }
    return false;
  };

  /**
   * 判断是否是IPv6
   */
  private isValidIPv6Format(ip: string): boolean {
    const IPv4Segment = '(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])';
    const IPv4Address = `(${IPv4Segment}[.]){3}${IPv4Segment}`;
    const IPv6Segment = '(?:[0-9a-fA-F]{1,4})';
    const ipRegex = new RegExp('^(' +
      `(?:${IPv6Segment}:){7}(?:${IPv6Segment}|:)|` +
      `(?:${IPv6Segment}:){6}(?:${IPv4Address}|:${IPv6Segment}|:)|` +
      `(?:${IPv6Segment}:){5}(?::${IPv4Address}|(:${IPv6Segment}){1,2}|:)|` +
      `(?:${IPv6Segment}:){4}(?:(:${IPv6Segment}){0,1}:${IPv4Address}|(:${IPv6Segment}){1,3}|:)|` +
      `(?:${IPv6Segment}:){3}(?:(:${IPv6Segment}){0,2}:${IPv4Address}|(:${IPv6Segment}){1,4}|:)|` +
      `(?:${IPv6Segment}:){2}(?:(:${IPv6Segment}){0,3}:${IPv4Address}|(:${IPv6Segment}){1,5}|:)|` +
      `(?:${IPv6Segment}:){1}(?:(:${IPv6Segment}){0,4}:${IPv4Address}|(:${IPv6Segment}){1,6}|:)|` +
      `(?::((?::${IPv6Segment}){0,5}:${IPv4Address}|(?::${IPv6Segment}){1,7}|:))` +
      ')(%[0-9a-zA-Z.]{1,})?$');
    let flag = ipRegex.test(ip);
    return flag;
  };
}

/**
 * Socket协议类型
 */
export enum SocketType {
  TCP,
  TLS
}
;

/**
 * 实现统一的接口(tcp/tls)
 */
export interface BaseSocket {
  createSocket(localIp: string, port: number): Promise<boolean>;

  connectSocket(address: string, port: number): Promise<boolean>;
}
```
