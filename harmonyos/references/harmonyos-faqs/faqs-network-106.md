---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-106
title: WIFI环境下无法检测出IPv6地址
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > WIFI环境下无法检测出IPv6地址
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3e4aea03c0abe5aade17d7178f36d6a494ff8518f0a0d73c6cf187a765c5b715
---

## 问题现象

在WIFI环境下，WIFI设置页面显示已经分配了IPv6相关的地址，但是使用测试网站无法检测出IPv6地址。

## 背景知识

* 获取网络的连接信息：[getConnectionPropertiesSync](../harmonyos-references/js-apis-net-connection.md#connectiongetconnectionpropertiessync10)接口。
* 网络地址[NetAddress](../harmonyos-references/js-apis-net-connection.md#netaddress)中的属性family=2代表IPv6，family=1代表IPv4。
* 公网IPv6是全球唯一地址，由ISP分配，可直接通过互联网访问（例如以2001或240x开头的地址）。
* 本地IPv6包括链路本地地址（如FE80开头），仅在局域网内有效，无法从外部互联网直接访问；常用于设备间内部通信。
* 一台设备可同时拥有多个IPv6地址：包括至少一个本地IPv6（用于局域网通信）和一个公网IPv6（用于外部访问）。例如，电脑可能通过路由器获取公网IPv6用于上网，同时使用FE80地址与本地打印机通信。
* 公网IPv6由ISP动态或静态分配，而本地IPv6由设备自动生成或路由器分配（如通过SLAAC协议）。访问外部服务时，数据需通过公网IPv6路由；本地IPv6仅限内部网络传输，提升效率。
* 公网IPv6支持全球路由和DNS记录，本地IPv6不可路由至公网且无DNS映射。
* 公网地址可被外部访问，本地地址仅限局域网内响应。

## 问题定位

* HarmonyOS具备IPv6的能力，无法检测出IPv6地址需要检查公网上的IPv6分配。
* 有本地IPv6地址，但是没有公网IPv6，通常无法通过IPv6的网络检测。
* 使用NetAddress类获取当前网络的地址信息。
* 在浏览器中输入在线IPv6测试网址查询当前网络连接信息。

## 分析结论

基于以上定位，使用NetAddress类获取当前网络的地址信息，可以使用NetAddress类的family属性判定IP地址的版本，family属性的值为1表示IPv4，为2表示IPv6。

## 修改建议

* 使用NetAddress类获取当前网络的地址信息，NetAddress类的family属性用于指定IP地址的版本，family属性的值为1表示IPv4，为2表示IPv6。参考代码如下：

  ```ts
  import { connection } from '@kit.NetworkKit';

  @Entry
  @Component
  struct Index {
    @State message: string = 'Wifi点击';

    build() {
      RelativeContainer() {
        Button(this.message)
          .id('click')
          .fontSize($r('app.float.page_text_font_size'))
          .fontWeight(FontWeight.Bold)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onClick(() => {
            this.message = 'Welcome';
            this.getNetwork();
          })
      }
      .height('100%')
      .width('100%')
    }

    getNetwork() {
      try {
        let netHandle = connection.getDefaultNetSync();
        let connectionproperties = connection.getConnectionPropertiesSync(netHandle);
        if (connectionproperties !== undefined) {
          let arr_linkAddresses = connectionproperties.linkAddresses;
          if (arr_linkAddresses !== undefined && arr_linkAddresses instanceof Array && arr_linkAddresses.length > 0) {
            for (let i = 0; i < arr_linkAddresses.length; i++) {
              let address: connection.NetAddress = arr_linkAddresses[i].address;
              if (address !== undefined) {
                console.warn('log debug : address = ', `${address}`);
                if (address.family === 1) {
                  console.warn('log debug : address is ipv4');
                } else if (address.family === 2) {
                  console.warn('log debug : address is ipv6');
                }
              }
            }
          }
        }
      } catch (e) {
        console.error(`Get exception: ${e}`);
      }
    }
  }
  ```
* 使用浏览器访问在线网址测试。

## 常见FAQ

Q：手机和电脑连接同一WIFI网络，使用各自的浏览器访问“XXXXIPv6”测试网址，电脑IPv6检测是正常的，但是手机识别不到IPv6地址。这是什么原因？

A：部分手机设备仅支持通过SLAAC无状态地址分配获取IPv6地址。若路由器设置为DHCPv6有状态地址分配模式，手机将无法获取有效IPv6地址，而Windows电脑则支持两种模式。可采用以下方式排查：

* 登录路由器后台，将IPv6地址分配模式改为SLAAC+无状态DHCPv6（或关闭有状态模式）。
* 更换其他手机测试，排除单设备故障，使用其他平台设备连接同一WIFI检测IPv6地址是否正常。
