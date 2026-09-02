---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-109
title: 使用connection.setAppHttpProxy设置代理后如何取消代理
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 使用connection.setAppHttpProxy设置代理后如何取消代理
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-07-22
content_hash: sha256:8f6b9eb965c2124dec0152f10189019d3c388b4934c84dc1f61db35775e6982e
---

## 问题现象

在使用connection.setAppHttpProxy设置代理后，如何才能取消代理？没有在官方文档中看到可以取消代理的接口。

## 背景知识

* [connection.setAppHttpProxy](../harmonyos-references/js-apis-net-connection.md#connectionsetapphttpproxy11)设置应用级http代理配置信息。
* [connection.getDefaultHttpProxy](../harmonyos-references/js-apis-net-connection.md#connectiongetdefaulthttpproxy10)获取网络默认的代理配置信息。如果设置了全局代理，则会返回全局代理配置信息。如果进程使用setAppNet绑定到指定[NetHandle](../harmonyos-references/js-apis-net-connection.md#nethandle)对应的网络，则返回[NetHandle](../harmonyos-references/js-apis-net-connection.md#nethandle)对应网络的代理配置信息。在其它情况下，将返回默认网络的代理配置信息。

## 解决方案

* 方案一：使用[connection.setAppHttpProxy](../harmonyos-references/js-apis-net-connection.md#connectionsetapphttpproxy11)设置空代理配置：通过将host设为空字符串、port设为0，并将exclusionList置为空列表。
* 方案二：通过[connection.getDefaultHttpProxy](../harmonyos-references/js-apis-net-connection.md#connectiongetdefaulthttpproxy10)获取到默认网络的代理配置信息，然后通过[connection.setAppHttpProxy](../harmonyos-references/js-apis-net-connection.md#connectionsetapphttpproxy11)重新设置为默认配置。

## 常见FAQ

Q：如何获取设备当前的代理列表？

A：通过[connection.getDefaultHttpProxy](../harmonyos-references/js-apis-net-connection.md#connectiongetdefaulthttpproxy10)在回调中可以看到当前的代理信息。

Q：如何检测Wi-Fi代理并阻止？

A：[connection.getDefaultHttpProxy](../harmonyos-references/js-apis-net-connection.md#connectiongetdefaulthttpproxy10)可以获取网络默认的代理配置信息。当用户开启代理时，可以通过此API获取到的代理信息来判断是否开启代理，并弹出[警告弹窗](../harmonyos-references/ts-methods-alert-dialog-box.md)阻止继续使用。

Q：为何无论[connection.setAppHttpProxy](../harmonyos-references/js-apis-net-connection.md#connectionsetapphttpproxy11)接口设置的域名是否正确，都会返回成功？

A：connection.setAppHttpProxy接口仅负责将代理配置写入系统，不会验证代理服务器的可用性。即使域名错误或服务器不可用，只要参数格式合法（如域名非空、端口为1-65535），都会返回成功。因此，需要应用自己校验域名的正确性。

Q：是否支持使用参数 { host: '', port: 0, exclusionList: ['\*'] } 来达到禁用代理的效果？为何设置该参数后再去获取，得到的参数为 { host: '', port: 0, exclusionList: [] }？

A：set的参数用get接口拿到的会保持原样，get函数会拿到set函数设置的值。只有启用有效代理会对用户网络产生影响，设置空代理配置（如host为空、port为0）不会对用户网络产生任何影响。具体可参考[connection.setAppHttpProxy](../harmonyos-references/js-apis-net-connection.md#connectionsetapphttpproxy11)与[connection.getDefaultHttpProxy](../harmonyos-references/js-apis-net-connection.md#connectiongetdefaulthttpproxy10)接口说明。
