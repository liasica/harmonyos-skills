---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/network-kit-troubleshooting-0003
title: Socket访问IPv6报错问题定位
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 故障排查 > Socket访问IPv6报错问题定位
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:13+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:0c1f0653c0ffe1db2a11e4ca6fe234d3c0f309079cf63571e8c2f8f33e8f321b
---

## 问题现象

socket访问IPv6失败，会报错：{"code":2301097,"message":"Address family not supported by protocol"}。

## 定位过程

排查目标地址信息[NetAddress](../harmonyos-references/js-apis-socket.md#netaddress)中参数配置是否有误。

## 分析结论

根据报错信息Address family not supported by protocol和代码示例可知，问题出在地址信息配置上面。由于NetAddress中family参数默认为IPv4，如果不重新配置family参数，使用的将会是IPv4网络。

## 修改建议

将NetAddress中family参数设置为2，用以支持访问IPv6网络，代码示例如下：

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct TlsSocketBind {
  // tlsSocket实例
  @State tls: socket.TLSSocket = socket.constructTLSSocketInstance();

  // 绑定tls
  bind() {
    // 网络协议类型，可选类型：
    // - 1：IPv4。默认为1。
    // - 2：IPv6。地址为IPV6类型，该字段必须被显式指定为2。
    // - 3：Domain。地址为Domain类型，该字段必须被显式指定为3。
    let bindAddr: socket.NetAddress = {
      address: '::1', // address需要根据实际地址进行填写
      port: 8080,
      family: 2
    };
    this.tls.bind(bindAddr, (err: BusinessError) => {
      if (err) {
        console.info('绑定失败', JSON.stringify(err));
        return;
      }
      console.info('绑定成功');
    });
  }

  build() {
    Column() {
      Button('开始绑定tls').onClick(() => {
        // 开始绑定tls
        this.bind();
      });
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.SpaceAround);
  }
}
```
