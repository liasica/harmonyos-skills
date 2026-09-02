---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-131
title: DNS域名解析错误
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > DNS域名解析错误
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-07-09
content_hash: sha256:eda405a3da11c96bda2773fb71a4b71a3325896c67c8ab0b7a953b729133c392
---

## 问题现象

* 网络正常情况下，跳转页面提示加载失败、返回1007900006错误码等现象。
* 使用connection.addCustomDnsRule添加自定义DNS解析规则后，依旧走的原来的地址，自定义DNS规则未生效。

## 背景知识

* 当存在连接复用\自定义DNS规则\本地DNS缓存时，请求按如下顺序依次执行：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/biNUqo4ySwuNHuo1A5IOWQ/zh-cn_image_0000002663721703.png "点击放大")
* [wireshark](https://github.com/wireshark/wireshark)：一款强大的网络协议分析工具，用于捕获和分析网络数据包，帮助用户深入理解和调试网络通信问题。
* [WebNetErrorList](../harmonyos-references/arkts-apis-neterrorlist.md#webneterrorlist)：ArkWeb的网络协议栈错误列表，其中ERR\_NAME\_NOT\_RESOLVED表示域名无法解析。
* [1007900006 域名解析失败](../harmonyos-references/errorcode-remote-communication.md#section1007900006-域名解析失败)：服务器的域名无法解析。

## 问题定位

通常DNS问题参考如下方式定位：

1. **检查网络连通性**，通过浏览器访问域名或在终端执行hdc shell ping [域名]检查网络连接情况。在通畅的网络下，使用默认DNS服务器，终端返回域名解析结果，丢包率0%：

   ```txt
   > hdc shell ping developer.huawei.com
   Ping developer.huawei.com (183.61.***.**): 56(84) bytes.
   64 bytes from 183.61.***.**: icmp_seq=1 ttl=47 time=26 ms
   64 bytes from 183.61.***.**: icmp_seq=2 ttl=47 time=28 ms
   64 bytes from 183.61.***.**: icmp_seq=3 ttl=47 time=25 ms

   --- 183.61.***.** ping statistics ---
   3 packets transmitted, 3 received, 0% packet loss
   round-trip min/avg/max = 25/26/28 ms
   ```
2. **查看hilog日志**，分析报错信息有1007900006、Couldn't resolve host name、ERR\_NAME\_NOT\_RESOLVED报错。
   1. RCP请求分析示例如下：
      * dnsStatus：DNS结果的状态，1表示有IP地址，2表示只拿到了CNAME，3代表非法报文。
      * dnsFromNetsys：DNS查询的结果是否来自网络系统缓存，0代表从DNS服务器获取，1代表从缓存中获取。
      * tryDns：尝试连接的DNS服务器。
      * recvDns：收到响应的DNS服务器。

        ```txt
        [RCP]  {"code":1007900006,"data":"Couldn't resolve host name","extendInfo":{"httpPhase":"100000","dnsDur":"0.00",   "tcpDur":"0.00","tlsDur":"0.00","sndDur":"0.00","rcvDur":"0.00","totDur":"32.61","redDur":"0.00","osErr":"11", "sptIP6":"1","proxyType":"none","uptProxyMs":"0","proxyCode":"0","lastOsIn":"20:10:28.562","lastOsOut":"never",  "sock":"-1","dnsFromNetsys":"0","tryDns":"202.96.***.**","connDns":"1","recvDns":"202.96.***.**,202.96.***.**",   "dnsStatus":"3"}}
        ```

        如上面日志代表DNS解析失败，向DNS服务器202.96.\*\*\*.\*\*请求解析结果，但是未正常解析IP地址，返回了其他非法报文。
   2. ArkWeb网络请求错误日志示例如下：

      ```txt
      getaddrinfo_ext: 234: reportdnsresult: -2 in process 30114
      ...
      getErrorInfo:ERR_NAME_NOT_RESOLVED
      getErrorCode:-105
      ```
3. **查看网络数据包**，判断DNS解析请求数据包是否发出，使用dns.qry.name contains [域名]过滤pcap日志。
   * 正常情况下，同时存在DNS请求及响应数据包：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/8YEh5D9BSJGUKBeOwvCUzQ/zh-cn_image_0000002663802523.png "点击放大")
   * 若请求时间点存在DNS query数据包，没有query response响应包，ICMP返回Destination unreachable，需要检查DNS服务器是否可达。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/5lVYdd2_QUm3SJIWjpBVAQ/zh-cn_image_0000002663722461.png "点击放大")
   * 若请求时间点存在DNS query数据包，响应返回No such name [域名]，需要检查域名是否拼写正确，或更换DNS服务器。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/tXQHbI0-SAiusp8PHoqHdA/zh-cn_image_0000002633443396.png "点击放大")
4. **检查是否存在连接复用**：对于HTTP/2版本，强制启用连接复用；HTTP/1.1版本中，header的Connection: keep-alive代表启用连接复用，默认开启，客户端可通过设置Connection: close显示关闭连接复用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/MYhcRTpsQmyL5QG7ODRUPw/zh-cn_image_0000002633603292.png "点击放大")

## 分析结论

* 域名解析配置错误或URL拼写错误。
* 自定义DNS规则优先级高于netsys缓存，同时连接复用会影响DNS过程。连接复用基于域名进行匹配，如果已经有指向相同域名的连接可以复用，那么HTTP请求会直接复用已有连接，导致自定义规则不生效。

## 修改建议

* 正确配置域名解析或拼写正确的URL。
  1. 正确配置域名解析：
     + 正确配置交换机/路由器网关。
     + 正确配置DNS代理/DNS防火墙。
     + 在域名解析服务商，正确配置域名的解析设置。
  2. 拼写正确且可达的URL地址。
* 在设置自定义DNS规则时，需要避免连接复用，尽量在启用自定义DNS规则后，再执行HTTP请求。
