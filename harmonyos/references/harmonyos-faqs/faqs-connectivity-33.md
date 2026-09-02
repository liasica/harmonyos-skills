---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-33
title: socket.sppReadAsync循环读取异常
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > socket.sppReadAsync循环读取异常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:38+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:98ec2ac876bc72b584cfdd7a021b7da2310080dd922b23ca1677b2f07a242ebc
---

## 问题现象

蓝牙spp连接成功后，调用socket.sppReadAsync，循环读取设备数据，只会成功读取一次，而后出现异常。问题代码如下：

```screen
import { socket } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';
let clientNumber = -1; // 入参clientNumber由sppAccept或sppConnect接口获取。
let buffer = new ArrayBuffer(1024);
let data = new Uint8Array(buffer);
let flag = 1;
while (flag) {
  try {
    socket.sppReadAsync(clientNumber).then((outBuffer: ArrayBuffer) => {
      buffer = outBuffer;
      if (buffer != null) {
        console.info(`sppRead success, data = ${JSON.stringify(buffer)}`);
      } else {
        console.error('sppRead error, data is null');
      }
    });
  } catch (err) {
    flag = 0;
    console.error(`startSppRead errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
  }
}
```

## 背景知识

* [socket.sppReadAsync](../harmonyos-references/js-apis-bluetooth-socket.md#socketsppreadasync18)通过socket读取对端所发送数据的异步接口，该接口支持断开连接时spp操作异常错误返回。
* 异步函数同时访问同一个变量时，执行顺序不可预测，数据竞争不一致导致访问冲突；
* [errorManager.on('unhandledRejection')](../harmonyos-references/js-apis-app-ability-errormanager.md#errormanageronunhandledrejection12)注册被拒绝promise监听器。注册后可以捕获到当前线程中未被捕获到的promise rejection。

## 问题定位

返回错误码401表示参数错误，删除while循环，就不会报错401，由此可得是多次调用导致的入参错误问题。socket.sppReadAsync是异步函数，在未等待执行结果后同时调用异步函数，并将同一个变量作为入参，导致数据资源存在竞争，导致入参异常。

## 分析结论

在执行异步函数时，应避免同时使用同一变量作为入参，否则可能存在资源访问异常情况，应该在异步函数执行完成后使用同一变量。

## 修改建议

socket.sppReadAsync该接口为异步接口，需要等异步回调结果返回后才能进行下一次调用。具体代码参考官方接口[socket.sppReadAsync](../harmonyos-references/js-apis-bluetooth-socket.md#socketsppreadasync18)示例代码。

## 常见FAQ

Q：在经典蓝牙中，应用该如何感知蓝牙是否已经断连？

A：调用sppReadAsync方法来监听spp蓝牙是否断开连接，如果spp蓝牙断开的话，接口会返回2901054错误。

## 总结

在异步函数调用中，应该充分考虑入参是否存在资源竞争关系，是否存在明显的执行逻辑顺序。
