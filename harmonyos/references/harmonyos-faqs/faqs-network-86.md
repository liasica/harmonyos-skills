---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-86
title: Socket通信时，如何根据使用场景正确转换数据类型
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > Socket通信时，如何根据使用场景正确转换数据类型
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:854134e4b15eb0de5feffb9530b9401a46f14755740ef740a443bde24a824080
---

## 问题现象

使用WebSocket、TCPSocket、TLSSocket、UDPSocket发送数据时，如何根据使用场景正确转换数据类型。

## 知识背景

* Socket进行数据传输，支持TCPSocket、UDPSocket、WebSocket和TLSSocket，仅可发送string或ArrayBuffer类型的数据，详情请参考[Socket连接](../harmonyos-references/js-apis-socket.md)。
* ArrayBuffer是ArkTS TypedArray的底层数据结构，TypedArray支持Int8Array、Uint8Array、Int16Array、Uint16Array等，详情请参考[ArrayBuffer](../harmonyos-references/arkts-apis-arkts-collections-arraybuffer.md)。

## 解决方案

Socket数据传输仅支持string或ArrayBuffer数据类型，与服务器进行交互时，有以下五种场景：

* **场景一**：

  客户端发送普通字符串数据，且服务端接收普通字符串，可直接调用[send](../harmonyos-references/js-apis-socket.md#send)接口发送。
* **场景二**：

  客户端发送普通字符串数据，但服务端需要接收二进制数据。可在Socket发送前将字符串转为Unicode，最后转换为ArrayBuffer类型数据。

  ```ts
  function strToArrayBuffer(str: string) {
    let buf = new ArrayBuffer(str.length * 2);
    let bufView = new Uint16Array(buf);
    for (let i = 0, strLen = str.length; i < strLen; i++) {
      bufView[i] = str.charCodeAt(i);
    }
    console.info(`bufView ${bufView}`);
    return bufView.buffer;
  }

  let inputValue = 'This is a plain string';
  strToArrayBuffer(inputValue);
  ```
* **场景三**：

  客户端发送十六进制字符串数据如[FA AF 11 C5 FE FF...]，服务端需要接收8位有符号整数数值如[-6, -81, 17, -59, 3, -1...]，可在Socket发送前将十六进制字符转成8位有符号整数（元素取值范围-128至127）。

  ```ts
  function strToInt8ArrayBuffer(str: string) {
    const arr = str.split(' ').map(hex => {
      let num = parseInt(hex, 16);
      return num > 127 ? num - 256 : num;
    });
    const typedArray = new Int8Array(arr);
    console.info(`typedArray ${typedArray}`);
    return typedArray.buffer;
  }

  let hexString = 'FA AF 11 C5 FE FF FF FF FF FF FF F0 53 C8 B9 25 E1 A7 67 46 68 94 1D 72 BC';
  strToInt8ArrayBuffer(hexString);
  ```

  **说明** 

  若其他平台十六进制字符转8位二进制流数据给服务端正常，HarmonyOS端十六进制字符转8位二进制流数据给服务端解析异常时，请排查服务端需要的8位整数数据类型，需要8位有符号整数且取值范围为-128至127时，请参考该场景的转换方法。
* **场景四**：

  客户端发送十六进制字符串数据如[FA AF 11 C5 FE FF...]，服务端需要接收8位无符号整数数值如[250, 175, 17, 197, 254, 255...]，可在Socket发送前将十六进制字符转成8位无符号整数（元素取值范围0至255）。

  ```ts
  function strToUint8ArrayBuffer(str: string) {
    const arr = str.split(' ').map(hex => {
      let num = parseInt(hex, 16);
      return num;
    });
    const typedArray = new Uint8Array(arr);
    console.info(`typedArray ${typedArray}`);
    return typedArray.buffer;
  }

  let hexValue = 'FA AF 11 C5 FE FF FF FF FF FF FF F0 53 C8 B9 25 E1 A7 67 46 68 94 1D 72 BC';
  strToUint8ArrayBuffer(hexValue);
  ```

  **说明** 

  若其他平台十六进制字符转8位二进制流数据给服务端正常，HarmonyOS端十六进制字符转8位二进制流服务端解析异常时，请排查服务端需要的8位整数数据类型，需要8位无符号整数且取值范围为0至255时，请参考该场景的转换方法。
* **场景五**：

  客户端需要发送复合类型的数据，如对象、数组等，可在Socket发送前使用JSON.stringify()转为string类型，若服务端接收普通字符串请参考场景一，若服务端接收二进制流数据请参考场景二。

完整示例参考如下：

```ts
function strToArrayBuffer(str: string) {
  let buf = new ArrayBuffer(str.length * 2);
  let bufView = new Uint16Array(buf);
  for (let i = 0, strLen = str.length; i < strLen; i++) {
    bufView[i] = str.charCodeAt(i);
  }
  console.info(`bufView ${bufView}`);
  return bufView.buffer;
}

let inputValue = 'This is a plain string';
strToArrayBuffer(inputValue);

function strToInt8ArrayBuffer(str: string) {
  const arr = str.split(' ').map(hex => {
    let num = parseInt(hex, 16);
    return num > 127 ? num - 256 : num;
  });
  const typedArray = new Int8Array(arr);
  console.info(`typedArray ${typedArray}`);
  return typedArray.buffer;
}

let hexString = 'FA AF 11 C5 FE FF FF FF FF FF FF F0 53 C8 B9 25 E1 A7 67 46 68 94 1D 72 BC';
strToInt8ArrayBuffer(hexString);

function strToUint8ArrayBuffer(str: string) {
  const arr = str.split(' ').map(hex => {
    let num = parseInt(hex, 16);
    return num;
  });
  const typedArray = new Uint8Array(arr);
  console.info(`typedArray ${typedArray}`);
  return typedArray.buffer;
}

let hexValue = 'FA AF 11 C5 FE FF FF FF FF FF FF F0 53 C8 B9 25 E1 A7 67 46 68 94 1D 72 BC';
strToUint8ArrayBuffer(hexValue);

@Entry
@ComponentV2
struct SocketTest {
  build() {
    Column() {
      Button('普通字符串转buffer').onClick(() => {
        strToArrayBuffer(inputValue);
      });
      Button('16进制字符转Int8ArrayBuffer').onClick(() => {
        strToInt8ArrayBuffer(hexString);
      });
      Button('16进制字符转Uint8ArrayBuffer').onClick(() => {
        strToUint8ArrayBuffer(hexValue);
      });
    }
    .width('100%')
    .height('100%');
  }
}
```

## 常见FAQ

Q：同时启动多个tcp server去监听同样的端口，都可以成功，这种情况不应该抛出端口占用的异常吗？

A：目前如果遇到指定端口被占用的情况，tcpsocketserver的listen会自动绑定一个新的随机端口。

应用可以通过[getLocalAddress](../harmonyos-references/js-apis-socket.md#getlocaladdress12-1)获取监听的端口，判断是否与指定的一致。
