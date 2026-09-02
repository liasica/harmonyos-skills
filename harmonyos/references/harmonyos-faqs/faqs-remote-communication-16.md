---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-remote-communication-16
title: RCP响应结果解析及常见问题定位思路
breadcrumb: FAQ > 系统开发 > 网络 > 远场通信（Remote Communication） > RCP响应结果解析及常见问题定位思路
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:38+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:ff9ce7acc55b6515fa67c24f175997dadcfd811906b4173c13ed83fbe53834c3
---

## 问题现象

[Remote Communication Kit](../harmonyos-references/remote-communication-api.md)构建了一种场景化HTTP通信能力，HTTP请求失败是网络通信中常见问题，请求失败后通常会使用日志打印的方式用于问题分析定位，常见的日志打印示例如下所示，那么如何能根据日志信息高效定位网络请求失败问题？

```txt
Rcp {"code":errCode,"data":"errInfo xxx","extendInfo":{"httpPhase":"111100","dnsDur":"76.30","tcpDur":"30.96","tlsDur":"55.88","sndDur":"0.17","rcvDur":"0.00","totDur":"195.18","redDur":"0.00","sptIP6":"0","proxyType":"none","srcAddr":"192.168.**.**","srcPort":"54842","dstAddr":"218.77.***.*","dstPort":"443","sock":"168"}}
```

## 背景知识

1. **HTTPS请求过程**

   一次完整的HTTPS请求过程如下图所示，包括构造网络请求、DNS解析、TCP握手、TLS握手、发送HTTP请求、服务器处理并生成响应、客户端接收响应数据、TCP四次挥手。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/lGnwAQLoRoyA-SIHpHcH0Q/zh-cn_image_0000002661541099.png "点击放大")
   1. **构造网络请求**

      RCP模块中[Request](../harmonyos-references/remote-communication-rcp.md#request)的参数包含请求地址、请求方法、请求头、请求内容、请求cookie等，通过请求参数的设置来构造网络请求。
   2. **DNS解析**

      DNS（Domain Name System，域名系统）是将域名转换为IP地址。DNS解析的基本原理是通过分布式的层级结构，将域名逐层解析为IP地址。这个过程涉及多个DNS服务器的协同工作，其解析步骤如上图所示。
   3. **TCP握手**

      TCP（传输控制协议）通过三次握手（Three-way Handshake）在客户端和服务器之间建立可靠的连接。其主要目的是确认双方的接收和发送能力均正常。
   4. **TLS握手**

      TLS握手是HTTPS建立安全连接的核心过程，其目标是在客户端和服务器之间建立共享的会话密钥，并验证双方的身份。详细步骤如上图所示。
   5. **发送HTTP请求**

      客户端将HTTP请求（如GET/index.html用会话密钥加密（对称加密，如AES）），通过已建立的TCP连接发送给服务器。
   6. **服务器处理并生成响应**

      服务器用相同的会话密钥解密，处理请求后，将响应数据（如HTML页面）加密后返回。
   7. **客户端接收响应数据**

      客户端收到响应数据后，解密响应数据。
   8. **TCP四次挥手**

      通信完成后，TCP四次挥手断开TCP连接，具体过程为客户端发送请求关闭连接，服务器发送确认收到关闭请求，服务器发送消息告知客户端数据发送完成，客户端发送消息确认关闭释放连接。

## 问题定位

1. **确认请求进行到哪个阶段。**

   关键字段httpPhase，httpPhase是6位由1或者0组成的数字，如11，按位表示当前执行到的阶段，当前将HTTP执行拆分为dns、tcp、tls、send、rcv、body共6个阶段，每个阶段开始执行时将对应位置置1。

   * dns：DNS开始。
   * tcp：DNS结束，TCP握手开始。
   * tls：TCP握手结束，TLS握手开始。
   * snd：TLS握手结束，请求发送开始。
   * rcv：请求发送结束，响应头接收开始。
   * bdy：响应头接收结束，响应体接收开始。

   下表是httpPhase所有可能的值与含义。

   | dns | tcp | tls | snd | rcv | bdy | httpPhase值 | 含义 |
   | --- | --- | --- | --- | --- | --- | --- | --- |
   | 1 | 1 | 1 | 1 | 1 | 1 | 111111 | HTTPS进行到接收响应体阶段 |
   | 1 | 1 | 1 | 1 | 1 | 0 | 111110 | HTTPS进行到接收响应头阶段 |
   | 1 | 1 | 1 | 1 | 0 | 0 | 111100 | HTTPS进行到发送请求阶段 |
   | 1 | 1 | 1 | 0 | 0 | 0 | 111000 | HTTPS进行到TLS阶段 |
   | 1 | 1 | 0 | 0 | 0 | 0 | 110000 | HTTPS进行到TCP阶段 |
   | 1 | 0 | 0 | 0 | 0 | 0 | 100000 | HTTPS进行到DNS阶段 |

   当出现DNS来自缓存，而非来自查询时，会出现DNS位为0的情况，如下所示。

   | dns | tcp | tls | snd | rcv | bdy | httpPhase值 | 含义 |
   | --- | --- | --- | --- | --- | --- | --- | --- |
   | 0 | 1 | 1 | 1 | 1 | 1 | 011111 | （DNS来自缓存）HTTPS进行到接收响应体阶段 |
   | 0 | 1 | 1 | 1 | 1 | 0 | 011110 | （DNS来自缓存）HTTPS进行到接收响应头阶段 |
   | 0 | 1 | 1 | 1 | 0 | 0 | 011100 | （DNS来自缓存）HTTPS进行到发送请求阶段 |
   | 0 | 1 | 1 | 0 | 0 | 0 | 011000 | （DNS来自缓存）HTTPS进行到TLS阶段 |
   | 0 | 1 | 0 | 0 | 0 | 0 | 010000 | （DNS来自缓存）HTTPS进行到TCP阶段 |

   当出现链接复用时，会出现tcp、tls为0的情况，如下所示。

   | dns | tcp | tls | snd | rcv | bdy | httpPhase值 | 含义 |
   | --- | --- | --- | --- | --- | --- | --- | --- |
   | 0 | 0 | 0 | 1 | 1 | 1 | 000111 | （连接复用）HTTPS进行到接收响应体阶段 |
   | 0 | 0 | 0 | 1 | 1 | 0 | 000110 | （连接复用）HTTPS进行到接收响应头阶段 |
   | 0 | 0 | 0 | 1 | 0 | 0 | 000100 | （连接复用）HTTPS进行到发送请求阶段 |
   | 1 | 0 | 0 | 1 | 1 | 1 | 100111 | （连接复用）HTTPS进行到接收响应体阶段 |
   | 1 | 0 | 0 | 1 | 1 | 0 | 100110 | （连接复用）HTTPS进行到接收响应头阶段 |
   | 1 | 0 | 0 | 1 | 0 | 0 | 100100 | （连接复用）HTTPS进行到发送请求阶段 |
2. **使用extendInfo和错误码字段进一步定位不同网络请求阶段问题错误**。
   1. **构造网络请求阶段典型问题场景如下：**
      * [401 参数错误](../harmonyos-references/errorcode-universal.md#section401-参数检查失败)：[rcp.createSession](../harmonyos-references/remote-communication-rcp.md#createsession)或者对应请求方法[fetch](../harmonyos-references/remote-communication-rcp.md#fetch)、[get](../harmonyos-references/remote-communication-rcp.md#get)、[post](../harmonyos-references/remote-communication-rcp.md#post)、[put](../harmonyos-references/remote-communication-rcp.md#put)等方法入参传入非法。
      * [201 权限被拒绝](../harmonyos-references/errorcode-universal.md#section201-权限校验失败)：使用RCP模块需要申请ohos.permission.INTERNET，若启用蜂窝网络路径偏好（cellular模式），需额外申请ohos.permission.GET\_NETWORK\_INFO。
      * [1007900994 会话数达到限制](../harmonyos-references/errorcode-remote-communication.md#section1007900994-会话数达到限制)：session创建数量超过系统规格上限。
   2. **DNS解析阶段解析失败典型问题场景如下：**

      | 故障 | 日志定位 | 典型场景问题 | 排查方法 |
      | --- | --- | --- | --- |
      | DNS服务器异常 | connDns为连接的DNS服务器列表，字段全为"0"，表示所有服务器连接失败，tryDns为尝试连接的服务器列表。 | 网络不通 | 其他设备连接同一网络环境后确认是否可以成功DNS服务器 |
      | DNS服务器无响应 | connDns的DNS服务器与recvDns中的DNS服务器无法对应，表示有服务器没有返回DNS结果。 | 网络管理给的DNS服务器不响应 | 排查DNS服务器配置，生成响应处理逻辑 |
      | DNS结果响应异常 | dnsStatus为1表示有IP地址，2表示只拿到CNAME，3表示非法报文。 | 2在重定向场景无异常，3表示域名解析为非法IP地址 | 排查域名是否正确，DNS自定义规则是否正确 |
   3. **TCP握手失败典型问题场景如下：**

      | 故障 | 日志定位 | 典型场景问题 | 排查方法 |
      | --- | --- | --- | --- |
      | TCP握手失败 | tryConnIp和tryConnPort分别为尝试连接的IP地址和端口。osErr为socket上发生的错误码与POSIX错误码一致。 | 目标IP网络不通或者服务器异常 | ping目标IP地址及其端口，排查目标服务器网络连通性 |
   4. **TLS握手失败典型问题场景如下：**

      | 故障 | 日志定位 | 典型场景问题 | 排查方法 |
      | --- | --- | --- | --- |
      | TCP流异常 | sslConnE非0。 | 网络切换、中断 | 查询osErr错误码分析原因 |
      | 拒绝TLS连接 | sslConnE为0，ciphers为调用方设置的加密套件或者默认的加密套件，minTlsVersion和maxTlsVersion调用方设置的最小和最大TLS版本或者默认的最小和最大TLS版本。 | 证书的版本以及加密套件不匹配 | 检查证书的版本以及加密套件等 |
   5. **发送HTTP请求数据到服务器，服务器返回数据到客户端，整个传输阶段超时典型问题场景如下：**

      | 故障 | 日志定位 | 典型场景问题 | 排查方法 |
      | --- | --- | --- | --- |
      | 传输超时 | dlSpeed下载速率，ulSpeed上传速率，lastPollinTime最近一次RCP尝试接收数据的时间，lastOsPollinTime最近一次内核通知RCP有数据的时间，lastPolloutTime最近一次RCP尝试发数据的时间，lastOsPolloutTime最近一次内核通知RCP有数据的时间。 | 弱网环境导致丢包重传乱序等问题 | 检查是否为弱网环境，尝试设置增加超时时间检查是否可以解决问题 |
      | rcp接收服务器响应流写入文件时响应超时 | transferMs参数数据传输默认值为60000，传输文件超过60S后报错Timeout was reached，响应超时。 | 参数值未满足写入文件所需的时间 | 配置HTTP请求的transferMs参数值,允许开发者定义连接和传输数据所允许的最长时间 |

## 分析结论

RCP网络请求问题首先通过日志判断在哪个请求阶段失效，针对不同的网络请求阶段，通过不同的日志拓展字段综合分析典型问题场景。但是也要结合实际的网络场景通过抓包进行补充分析。

## 修改建议

通过上述的定位分析，可以针对性修改请求参数，DNS服务器配置，目标服务器配置，路由网络环境配置等。
