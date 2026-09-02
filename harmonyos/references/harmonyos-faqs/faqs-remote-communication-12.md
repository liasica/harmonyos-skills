---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-remote-communication-12
title: 如何定位分析设置VPN服务器失败问题
breadcrumb: FAQ > 系统开发 > 网络 > 远场通信（Remote Communication） > 如何定位分析设置VPN服务器失败问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:16e1d24c1b96a2b28c6a42b97e53140638cf91ec3e4cd7cd2c95db8138d57c52
---

## 问题现象

设置VPN服务器时，出现“Timeout was reached”的提示信息，问题现象和错误日志如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/L64ZuG5ERQG1xwj2uPPUsA/zh-cn_image_0000002658851745.png "点击放大")

```shell
NETSTACK:  id=50, httpVer:2, errCode:1007900006, httpPhase:111110, dnsDur:197.44, tcpDur:89.70, tlsDur:78.84, sndDur:0.97, rcvDur:69.27, totDur:517.63, redDur:436.31, osErrno:11, sptIP6:0, proxyType:none, srcAddr:192.168.*.**, srcPort:36940, dstAddr:121.37.**.***, dstPort:443, sock:119, dnsRecvE:11, tryDns:2.0.*.**,2.0.*.***,2.0.*.**,2.0.*.**,2.0.*.**, connDns:1,1,1,1,1, recvDns:2.0.*.**,2.0.*.**,2.0.*.**,2.0.*.**, tcpConnE:115, tryConnV4:1, tryConnV6:0, dlSpeed:0, ulSpeed:0, dlSz:0, ulSz:0, reused:false, sockType:IpConnection, connectMs:60000, transferMs:60000, reqLen:0, respLen:no header recv, lastRcpIn:9:15:46.117, lastOsIn:9:15:46.117, lastRcpOut:9:15:45.983, lastOsOut:9:15:45.983, lastSslRecvSz:-1, lastSslSendSz:1660, totalSslRecvSz:761, totalSslSendSz:1733, lastEpollAct:5, headerOutSz:537, headerInSz:997, tstGlbUsr:0, tstCurUsr:0, selfCaPath:0, selfCaFile:1, selfCaBlob:0, 
JSAPP: Rcp {"code":1007900006,"data":"Couldn't resolve host name","extendInfo":{"httpPhase":"111110","dnsDur":"197.44","tcpDur":"89.70","tlsDur":"78.84","sndDur":"0.97","rcvDur":"69.27","totDur":"517.63","redDur":"436.31","sptIP6":"0","proxyType":"none","srcAddr":"192.168.*.**","srcPort":"36940","dstAddr":"121.37.**.***","dstPort":"443","sock":"119","dnsRecvE":"11","tryDns":"2.0.*.**,2.0.*.***,2.0.*.**,2.0.*.**,2.0.*.**","connDns":"1,1,1,1,1","recvDns":"2.0.*.**,2.0.*.**,2.0.*.**,2.0.*.**"}}
*
NK_CPP: [ERROR][OnLogMessage] SetSockOpt failed, errno:92, strerror:Protocol not available
```

## 背景知识

* VPN客户端与VPN服务端初次连接，主要包括6个阶段准备与初始化，建立传输层连接、协议握手与认证、安全隧道建立、网络配置、连接维护，如下图所示。准备与初始化包括客户端配置加载和DNS解析。传输层连接时基于TCP/UDP连接实现三次握手。协议握手与认证包括协议版本协商、身份验证。安全隧道建立包括密钥交换、加密通道建立。网络配置包括IP地址分配、路由配置、隧道接口创建。连接维护包括心跳与保活、连接就绪。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/W8TEcjIRRQ6Ph2ylFsAG-A/zh-cn_image_0000002628772380.png "点击放大")
* DNS解析通用过程如下图所示，第一优先级为使用本地缓存解析域名，其次是使用客户端配置本地DNS解析服务器查询，进一步依次查询根DNS服务器、NameServer服务器等。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/k2jMXwGvQZqzZSmhVfUaXg/zh-cn_image_0000002658971701.png "点击放大")

## 问题定位

1. 根据问题截图可知是客户端初次连接VPN服务器阶段的网络超时。
2. 根据报错日志为"Couldn't resolve host name"可知为DNS解析阶段无法解析域名导致的失败导致网络请求超时。
3. 根据日志中扩展字段tryDns和recvDns数量不匹配，但是connDns不为0，证明客户端与DNS服务器网络是连通的，并且DNS服务器的IP为"2.0.\*.\*\*"，证明只是没有收到正确的内部DNS服务器响应，从而导致DNS解析失败。
4. 进一步查看内核日志信息"strerror:Protocol not available"说明需要解析的域名信息不支持该通信协议。
5. 查看输入的VPN服务器地址为HTTP开头，为不支持的VPN通信协议。

## 分析结论

DNS服务器不能解析HTTP协议域名，导致DNS解析失败，最终导致连接VPN超时。

## 修改建议

客户端修改正确的VPN地址即可。
