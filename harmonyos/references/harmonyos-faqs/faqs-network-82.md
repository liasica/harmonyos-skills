---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-82
title: 如何解决使用TcpSocket接收到的数据被截断的问题
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 如何解决使用TcpSocket接收到的数据被截断的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:36+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fa1166a73249b8bdb375fa1a9241fbc422c76ca264493223f4ea410bf3a8f6a5
---

## 问题现象

使用[TcpSocket](../harmonyos-references/js-apis-socket.md)接收到的数据被截断。

## 背景知识

TCP是面向字节流的协议，是无边界的。由于没有边界，当发送端按顺序将字节发送到网络中时，接收方无法确定这些字节属于哪个包。所以在TCP数据传输过程中，有可能会发生粘包、拆包（半包）现象。

* 正常传输数据包：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/sxlU0n25T0y5NR9nFQgATg/zh-cn_image_0000002628770212.png "点击放大")
* TCP粘包：

  是指发送方发送的若干数据，在接收方的缓冲区里被组合到一起后读取，后面数据包的头部“粘着”前面数据包的尾部，当单个包比较小时，多个包可能会被合并成一个数据包，所以称为粘包。

  粘包示意图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/kqk42HNPStOpq7nugkV3lg/zh-cn_image_0000002658969537.png "点击放大")
* TCP拆包：

  是指一个比较大的数据包，在接收方缓冲区被拆分成多个数据包来读取，这些多个数据包组合起来才是正确的数据包。

  拆包和粘包示意图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/7H1pJfL1RTa1DZFnxjqVbQ/zh-cn_image_0000002628610326.png "点击放大")

## 问题定位

使用代码模拟场景，发送一个长度很长的包，会出现截断现象；发送一个长度较短的包，会出现两次发送的包粘连成一个数据包。

## 分析结论

使用TcpSocket传输数据时，服务端同时发送了3个数据包A、B、C给客户端，由于B包数据过大，导致B包被截断，并且被截断的部分拼接到了C包的前面，从而客户端无法正常读取数据。

## 修改建议

* **方案一**：使用固定的标识符作为数据包的结尾。

  可以在每次发送数据时，在数据的末尾添加固定的标识符，比如\r\n。

  ```ts
  msg += '\r\n';
  try {
    await this.tcp.send({
      data: msg
    });
  } catch (error) {
    console.error(`send failed. ${index}`);
  }
  ```

  这样当解析对端传过来的数据时，首先把所有收到的数据都复制到接收缓冲区中，然后遍历缓冲区查找结束标志，找到后就把结束标志以前的部分作为完整数据包提取出来使用，剩余的部分复制到缓冲区首部进行下一次遍历，直到找不到结束标志为止。

  ```ts
  client.on('message', (value: socket.SocketMessageInfo) => {
    // 把接收到的数据复制到缓冲区有效数据尾部
    let copyCount = buffer.from(value.message).copy(this.receivedDataBuf, this.receivedDataLen);
    // 缓冲区已使用长度加上本次接收的数据长度
    this.receivedDataLen += copyCount;
    // 缓冲区数据中数据包结束标志的位置
    let endFlagPos = this.receivedDataBuf.subarray(0, this.receivedDataLen).indexOf(this.packetEndFlag);
    let textDecoder = util.TextDecoder.create('utf-8');
    while (endFlagPos > -1) {
      // 把数据包结束标志前面的数据转换为字符串
      let msgArray = new Uint8Array(this.receivedDataBuf.subarray(0, endFlagPos).buffer);
      let msg = textDecoder.decodeToString(msgArray);
      this.receivedMsg.push(msg);
      // 剩余的未解析数据
      let leaveBufData = this.receivedDataBuf.subarray(endFlagPos + 2, this.receivedDataLen);
      // 剩余的未解析数据移动到缓冲区头部
      for (let pos = 0; pos < leaveBufData.length; pos++) {
        this.receivedDataBuf.writeUInt8(leaveBufData.readUInt8(pos), pos);
      }
      // 重新设置缓冲区已使用长度
      this.receivedDataLen = leaveBufData.length;
      // 开始查找下一个数据包结束标志
      endFlagPos = this.receivedDataBuf.subarray(0, this.receivedDataLen).indexOf(this.packetEndFlag);
    }
  });
  ```

* **方案二**：在每个数据包的头部定义数据包的长度。

  通过将数据包的总长度声明在数据包的首部，例如前2位字节为固定的包长度，使用小端的16位无符号整数表示，后面是包内容：

  ```ts
  let msg = index.toString();
  let textEncoder = new util.TextEncoder();
  let encodeValue = textEncoder.encodeInto(msg);
  let sendBuf = buffer.alloc(2 + encodeValue.byteLength);
  // 写入固定包头中的长度信息
  sendBuf.writeUInt16LE(encodeValue.byteLength);
  // 写入固定包头中的长度信息
  sendBuf.write(msg, 2);
  try {
    await this.tcp.send({
      data: sendBuf.buffer
    });
  } catch (error) {
    console.error(`send failed. ${index}`);
  }
  ```

  接收方在读取数据时，就可以先读取前2位字节获取数据包的长度，然后再往后读取这个长度的字节流，就是一个完整的数据包。

  ```ts
  client.on('message', (value: socket.SocketMessageInfo) => {
    // 把接收到的数据复制到缓冲区有效数据尾部
    let copyCount = buffer.from(value.message).copy(this.receivedDataBuf, this.receivedDataLen);
    this.receivedDataLen += copyCount;
    // 至少写入了3个字节才需要解析
    if (this.receivedDataLen < 3) {
      return;
    }
    // 当前数据包长度
    let packLen = this.receivedDataBuf.readUInt16LE();
    let textDecoder = util.TextDecoder.create('utf-8');
    // 当前数据包长度加上固定包体的2字节，如果小于等于缓冲区已使用长度，就可以解析
    while ((packLen + 2) <= this.receivedDataLen) {
      // 把可变包体中的数据转换为字符串
      let msgArray = new Uint8Array(this.receivedDataBuf.subarray(2, packLen + 2).buffer);
      let msg = textDecoder.decodeToString(msgArray);
      this.receivedMsg.push(msg);
      // 剩余的未解析数据
      let leaveBufData = this.receivedDataBuf.subarray(packLen + 2, this.receivedDataLen);
      // 剩余的未解析数据移动到缓冲区头部
      for (let pos = 0; pos < leaveBufData.length; pos++) {
        this.receivedDataBuf.writeUInt8(leaveBufData.readUInt8(pos), pos);
      }
      // 重新设置缓冲区已使用长度
      this.receivedDataLen = leaveBufData.length;
      // 至少写入了3个字节才需要解析，否则跳出循环
      if (this.receivedDataLen < 3) {
        break;
      }
      // 开始查找下一个固定包头中的可变包体长度
      packLen = this.receivedDataBuf.readUInt16LE();
    }
  });
  ```

实现TcpSocket通信，首先需要申请[ohos.permission.INTERNET](../harmonyos-guides/permissions-for-all.md#ohospermissioninternet)权限，完整示例参考如下：

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer, util } from '@kit.ArkTS';

@Entry
@Component
struct SocketCommunication {
  private tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
  private tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
  @State receivedMsg: string[] = [];
  // 数据包结束标志
  packetEndFlag: string = '\r\n';
  // 最大缓存长度
  maxBufSize: number = 1024 * 8;
  // 接收数据缓冲区
  receivedDataBuf: buffer.Buffer = buffer.alloc(this.maxBufSize);
  // 缓冲区已使用长度
  receivedDataLen: number = 0;

  build() {
    Column({ space: 20 }) {
      Button('init TCP Server')
        .fontSize(24)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          let listenAddr: socket.NetAddress = {
            address: 'localhost',
            port: 9588,
            family: 1
          };
          this.tcpServer.listen(listenAddr, (err: BusinessError) => {
            if (err) {
              console.error('listen fail', JSON.stringify(err));
              return;
            }
            console.info('listen success');
            this.getUIContext().getPromptAction().showToast({ message: 'listen success' });
          });
        });
      Button('方案一：固定标识符作为尾部')
        .fontSize(24)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          this.tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
            console.info('client connected');
            client.on('close', () => {
              console.info('on close success');
            });
            client.on('message', (value: socket.SocketMessageInfo) => {
              // 把接收到的数据复制到缓冲区有效数据尾部
              let copyCount = buffer.from(value.message).copy(this.receivedDataBuf, this.receivedDataLen);
              // 缓冲区已使用长度加上本次接收的数据长度
              this.receivedDataLen += copyCount;
              // 缓冲区数据中数据包结束标志的位置
              let endFlagPos = this.receivedDataBuf.subarray(0, this.receivedDataLen).indexOf(this.packetEndFlag);
              let textDecoder = util.TextDecoder.create('utf-8');
              while (endFlagPos > -1) {
                // 把数据包结束标志前面的数据转换为字符串
                let msgArray = new Uint8Array(this.receivedDataBuf.subarray(0, endFlagPos).buffer);
                let msg = textDecoder.decodeToString(msgArray);
                this.receivedMsg.push(msg);
                // 剩余的未解析数据
                let leaveBufData = this.receivedDataBuf.subarray(endFlagPos + 2, this.receivedDataLen);
                // 剩余的未解析数据移动到缓冲区头部
                for (let pos = 0; pos < leaveBufData.length; pos++) {
                  this.receivedDataBuf.writeUInt8(leaveBufData.readUInt8(pos), pos);
                }
                // 重新设置缓冲区已使用长度
                this.receivedDataLen = leaveBufData.length;
                // 开始查找下一个数据包结束标志
                endFlagPos = this.receivedDataBuf.subarray(0, this.receivedDataLen).indexOf(this.packetEndFlag);
              }
            });
          });

          let netAddress: socket.NetAddress = {
            address: 'localhost',
            port: 9588
          };
          let tcpConnectOptions: socket.TCPConnectOptions = {
            address: netAddress,
            timeout: 6000
          };
          this.tcp.connect(tcpConnectOptions, async () => {
            console.info('connect success');
            for (let index = 0; index < 100; index++) {
              let msg = index.toString();
              msg += '\r\n';
              try {
                await this.tcp.send({
                  data: msg
                });
              } catch (error) {
                console.error(`send failed. ${index}`);
              }
            }
          });
        });
      Button('方案二：头部标识长度')
        .fontSize(24)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          this.tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
            console.info('client connected');
            client.on('close', () => {
              console.info('on close success');
            });
            client.on('message', (value: socket.SocketMessageInfo) => {
              // 把接收到的数据复制到缓冲区有效数据尾部
              let copyCount = buffer.from(value.message).copy(this.receivedDataBuf, this.receivedDataLen);
              this.receivedDataLen += copyCount;
              // 至少写入了3个字节才需要解析
              if (this.receivedDataLen < 3) {
                return;
              }
              // 当前数据包长度
              let packLen = this.receivedDataBuf.readUInt16LE();
              let textDecoder = util.TextDecoder.create('utf-8');
              // 当前数据包长度加上固定包体的2字节，如果小于等于缓冲区已使用长度，就可以解析
              while ((packLen + 2) <= this.receivedDataLen) {
                // 把可变包体中的数据转换为字符串
                let msgArray = new Uint8Array(this.receivedDataBuf.subarray(2, packLen + 2).buffer);
                let msg = textDecoder.decodeToString(msgArray);
                this.receivedMsg.push(msg);
                // 剩余的未解析数据
                let leaveBufData = this.receivedDataBuf.subarray(packLen + 2, this.receivedDataLen);
                // 剩余的未解析数据移动到缓冲区头部
                for (let pos = 0; pos < leaveBufData.length; pos++) {
                  this.receivedDataBuf.writeUInt8(leaveBufData.readUInt8(pos), pos);
                }
                // 重新设置缓冲区已使用长度
                this.receivedDataLen = leaveBufData.length;
                // 至少写入了3个字节才需要解析，否则跳出循环
                if (this.receivedDataLen < 3) {
                  break;
                }
                // 开始查找下一个固定包头中的可变包体长度
                packLen = this.receivedDataBuf.readUInt16LE();
              }
            });
          });

          let netAddress: socket.NetAddress = {
            address: 'localhost',
            port: 9588
          };
          let tcpConnectOptions: socket.TCPConnectOptions = {
            address: netAddress,
            timeout: 6000
          };
          this.tcp.connect(tcpConnectOptions, async () => {
            for (let index = 0; index < 100; index++) {
              let msg = index.toString();
              let textEncoder = new util.TextEncoder();
              let encodeValue = textEncoder.encodeInto(msg);
              let sendBuf = buffer.alloc(2 + encodeValue.byteLength);
              // 写入固定包头中的长度信息
              sendBuf.writeUInt16LE(encodeValue.byteLength);
              // 写入固定包头中的长度信息
              sendBuf.write(msg, 2);
              try {
                await this.tcp.send({
                  data: sendBuf.buffer
                });
              } catch (error) {
                console.error(`send failed. ${index}`);
              }
            }
          });
        });
      Column() {
        Scroll() {
          Column() {
            ForEach(this.receivedMsg, (item: string) => {
              Text(item)
                .textAlign(TextAlign.Center)
                .width('100%')
                .fontSize(24);
            });
          };
        };
      }
      .border({ width: 1 })
      .width('90%')
      .height('75%');
    }
    .margin({ top: 20 })
    .height('100%')
    .width('100%');
  }
}
```

## 常见FAQ

Q：TcpSocket发送的文件流比较大的时候，有什么好的处理方法？

A：可以修改sendBufferSize增大发送缓冲区大小和延长socketTimeout超时时间。
