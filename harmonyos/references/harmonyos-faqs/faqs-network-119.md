---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-119
title: 如何解决TCPSocket发送数据报错"send failed, socket is 72, errno is 32"
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 如何解决TCPSocket发送数据报错"send failed, socket is 72, errno is 32"
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:57b9db66aed4525b1c0427b448d5cc62078fbf82e9d725d6350db263b301f89c
---

## 问题现象

使用TCPSocket给打印机循环发送文件数据时中途报错：[socket\_exec.cpp:2654] send failed, socket is 72, errno is 32，但是使用Debug方式一步一步的执行可以发送成功，如何解决？

## 背景知识

应用使用TCP协议进行Socket通信需要了解以下流程：

1. import需要的Socket模块。
2. 创建一个TCPSocket连接，返回一个TCPSocket对象。
3. 订阅TCPSocket相关的订阅事件。
4. 绑定IP地址和端口，端口可以指定或由系统随机分配。
5. 连接到指定的IP地址和端口。
6. 发送数据。
7. Socket连接使用完毕后，主动关闭。

## 问题定位

* 通过TCPDump日志分析是否对端主动关闭连接。
* 检查是否循环发送数据量过大导致服务端处理不过来。

## 分析结论

通过抓取TCPDump日志进行分析，关键日志如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/bNIiE173QtqsKDeuOMP2Xw/zh-cn_image_0000002706380593.png "点击放大")

结论如下：

* 在非Debug方式下，打印机主动发了一个RST，服务端主动关闭连接。
* 客户端已经发了大量的包，打印机还在应答前面的包，服务端处理不过来了。

## 修改建议

* 减小每次发送的数据大小。
* 在每次发送完添加Sleep延时50毫秒避免数据堆积。

## 常见FAQ

Q：发送原始字节数组时报错"recv fail, errno: 0"如何处理？

A：该错误码表示服务器返回FIN主动关闭了连接。建议通过tcpdump抓包日志分析服务器关闭连接的具体原因，检查是否存在数据格式不匹配、发送频率过快或服务端处理超时等情况。
