---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-remote-communication
title: API错误码
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > API错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3a8b89c483351cd18e17fae4076bcd5b53f25d8a38542c4a9a6ef8566685812e
---

**说明** 

* 以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码](errorcode-universal.md)。
* 1007900000 ~ 1007900200：1007900000 + curl错误码。curl错误码可参考：[curl错误码](https://curl.se/libcurl/c/libcurl-errors.html)。
* 1007900201 ~ 1007900999：RCP特有错误码保留段。
* 1007910000 ~ 1007910999：URPC特有错误码保留段。

## 1007900001 不支持的协议

**错误信息**

Unsupported protocol.

**错误描述**

服务器不支持该协议版本。

**可能原因**

传入的协议版本，服务器不支持。

**处理步骤**

请检查传入的协议版本是否合理，排查服务器实现。

## 1007900002 初始化失败

**错误信息**

Failed initialization

**错误描述**

初始化失败。

**可能原因**

可能是因为内存分配失败。

**处理步骤**

释放清理内存，确保有充足的可用内存空间。

## 1007900003 URL格式错误

**错误信息**

URL using bad/illegal format or missing URL.

**错误描述**

URL格式错误。

**可能原因**

可能传入的url格式不正确。

**处理步骤**

检查传入的url格式是否正确。

## 1007900005 代理服务器域名解析失败

**错误信息**

Couldn't resolve proxy name.

**错误描述**

代理服务器的域名无法解析。

**可能原因**

服务器的URL不正确。

**处理步骤**

排查代理服务器的URL是否正确。

## 1007900006 域名解析失败

**错误信息**

Couldn't resolve host name.

**错误描述**

服务器的域名无法解析。

**可能原因**

1. 传入的服务器的URL不正确。
2. 网络不通畅。
3. 系统内部异常。
4. DNS服务器异常。

**处理步骤**

1. 请检查输入的服务器的URL是否合理。
2. 请检查网络连接情况。
3. 采集故障扩展信息字段或者日志，查看DNS相关字段：[dnsSockE](remote-communication-error-field.md#dnssocke)、[dnsCloseE](remote-communication-error-field.md#dnsclosee)、[dnsConnE](remote-communication-error-field.md#dnsconne)、[dnsRecvE](remote-communication-error-field.md#dnsrecve)、[dnsSendE](remote-communication-error-field.md#dnssende)，以上有字段不为0，表明系统内部报错，建议排查应用管控是否有拦截、网络是否正常可用。
4. 采集故障扩展信息字段或者日志，检验如下关键字段：

   * [connDns](remote-communication-error-field.md#conndns)：若全"0"，表示Wi-Fi/蜂窝下发送请求至不可用的服务器，全部DNS服务器连接失败，DNS请求无法发送。
   * [tryDns](remote-communication-error-field.md#trydns)：若为空表示当前无可用的DNS服务器。
   * [recvDns](remote-communication-error-field.md#recvdns)：若[connDns](remote-communication-error-field.md#conndns)的DNS服务器与[recvDns](remote-communication-error-field.md#recvdns)中的DNS服务器若无法对应，表示有服务器没有返回DNS结果。
   * [dnsStatus](remote-communication-error-field.md#dnsstatus)：1表示有IP地址，请求正常；2表示只拿到了CNAME，CNAME应该进行递归查询或者使用备份服务器重试；3表示非法报文。

   出现以上情况，建议查看Wi-Fi或蜂窝网络是否正常可用，网络管理的DNS服务器是否异常。

## 1007900007 无法连接到服务器

**错误信息**

Couldn't connect to server.

**错误描述**

服务器无法连接。

**可能原因**

网络断开。

**处理步骤**

检查网络连接。

## 1007900008 服务器返回非法数据

**错误信息**

Weird server reply.

**错误描述**

服务器返回非法数据。

**可能原因**

服务器出错，返回了非HTTP格式的数据。

**处理步骤**

排查服务器实现。

## 1007900009 拒绝对远程资源的访问

**错误信息**

Access denied to remote resource.

**错误描述**

拒绝对远程资源的访问。

**可能原因**

指定的内容被服务器拒绝访问。

**处理步骤**

排查请求内容。

## 1007900016 HTTP2帧层错误

**错误信息**

Error in the HTTP2 framing layer.

**错误描述**

HTTP2层级的错误。

**可能原因**

服务器不支持HTTP2。

**处理步骤**

抓包分析、排查服务器是否支持HTTP2。

## 1007900018 服务器返回数据不完整

**错误信息**

Transferred a partial file.

**错误描述**

服务器返回的数据不完整。

**可能原因**

可能与服务器实现有关。

**处理步骤**

排查服务器实现。

## 1007900023 写入接收到的数据到磁盘/应用程序失败

**错误信息**

Failed writing received data to disk/application.

**错误描述**

写入接收到的数据到磁盘/应用程序失败。

**可能原因**

下载数据量超过最大值。

**处理步骤**

当请求数据量超大时推荐使用[OnDataReceive](remote-communication-rcp.md#ondatareceive)。

## 1007900025 上传失败

**错误信息**

Upload failed (at start/before it took off).

**错误描述**

上传失败。

**可能原因**

文件过大或者网络问题。对于FTP，服务器通常会拒绝STOR命令。错误缓冲区通常包含服务器的解释。

**处理步骤**

排查文件大小及网络状况。

## 1007900026 从文件/应用程序中打开/读取本地数据失败

**错误信息**

Failed to open/read local data from file/application.

**错误描述**

从文件/应用程序中打开/读取本地数据失败。

**可能原因**

应用没有读文件权限。

**处理步骤**

排查应用权限。

## 1007900027 内存不足

**错误信息**

Out of memory.

**错误描述**

内存不足。

**可能原因**

内存不足。

**处理步骤**

排查系统内存。

## 1007900028 操作超时

**错误信息**

Timeout was reached.

**错误描述**

操作超时。

**可能原因**

根据超时所处的不同阶段，可将其划分为以下四类：

1. 参考[httpPhase字段说明](remote-communication-error-field.md#httpphase)，若dns开始阶段为1且其余阶段均为0，则判定为DNS阶段超时。DNS阶段超时可能由以下原因导致：

   * DNS服务器异常，例如蜂窝网络或Wi-Fi连接故障。
   * 服务器不支持IPv6或IPv4，导致查询无响应。
2. 参考[httpPhase字段说明](remote-communication-error-field.md#httpphase)，若tcp开始阶段是1，tls开始阶段是0，则判定为TCP阶段超时。TCP阶段超时可能由以下原因导致：

   * SYN报文发送超时。
   * 网络切换、网络断开导致的系统内部异常。
   * 代理信息错误，可能是系统代理获取失败或者调用方的代理配置错误。
3. 参考[httpPhase字段说明](remote-communication-error-field.md#httpphase)，若tls开始阶段是1，snd开始阶段是0，则判定为TLS阶段超时。TLS阶段超时可能由TLS握手过程中TCP流产生异常导致。
4. 参考[httpPhase字段说明](remote-communication-error-field.md#httpphase)，若snd开始阶段是1，rcv开始阶段是0，则判定发送阶段超时。若rcv开始阶段是1，bdy开始阶段是0，则判定响应头接收阶段超时。若rcv开始阶段是1，bdy开始阶段也是1，则判定响应体接收阶段超时。传输阶段超时可能由以下原因导致：

   * [lastOsIn](remote-communication-error-field.md#lastosin)：表示最近一次系统内部通知RCP有数据到达的时间。如果[lastOsIn](remote-communication-error-field.md#lastosin)不存在或值为8:0:0.0，意味着系统内部接收缓冲区为空，RCP目前未接收到数据。[lastOsIn](remote-communication-error-field.md#lastosin)与超时发生时间之间的差异接近[cfgTransferMs](remote-communication-error-field.md#cfgtransferms)，则表示长时间未能从系统内部接收数据，从而导致超时。
   * [lastOsOut](remote-communication-error-field.md#lastosout)：表示最近一次系统内部通知RCP成功发送数据的时间。如果[lastOsOut](remote-communication-error-field.md#lastosout)不存在，则表明RCP面临系统内部发送缓冲区满的情况，无法发送数据。同时，[lastOsIn](remote-communication-error-field.md#lastosin)与[lastOsOut](remote-communication-error-field.md#lastosout)之间的差异接近[cfgTransferMs](remote-communication-error-field.md#cfgtransferms)，则表示从发送数据到接收响应的时间过长，导致超时。

**处理步骤**

建议请检查网络连接，切换至更稳定的网络环境，并排查服务端是否存在阻塞情况。如果连续多次遇到1007900028错误码，建议把Session关闭后，重新创建Session。

## 1007900035 SSL连接错误

**错误信息**

SSL connect error.

**错误描述**

SSL连接错误。

**可能原因**

根据系统内部是否发生错误，可划分为以下两种情况：

1. 系统内部报错，故障扩展信息字段/日志中，[sslConnE](remote-communication-error-field.md#sslconne)字段非0。可能的原因是TLS握手过程中出现TCP流异常（如网络切换或中断）导致。
2. 系统内部无报错，故障扩展信息字段/日志中，[sslConnE](remote-communication-error-field.md#sslconne)字段为0。可能的原因是TLS握手过程中TCP流正常，但是云侧拒绝TLS连接导致。

**处理步骤**

如果TLS连接失败，请检客户端的TLS相关配置（[SecurityConfiguration](remote-communication-rcp.md#securityconfiguration)中的tlsOptions和tlsRange属性）是否与服务端匹配，例如客户端与服务端的TLS版本是否匹配。

## 1007900037 无法读取文件

**错误信息**

Couldn't read a file:// file.

**错误描述**

无法读取文件。

**可能原因**

1、文件路径错误或文件不存在。

2、文件权限不足。

3、路径格式不正确。

**处理步骤**

1、检查对应路径文件是否存在。

2、应用程序是否有对此路径文件的操作权限。

3、使用的文件路径格式是否正确。

## 1007900042 操作被应用程序回调中止

**错误信息**

Operation was aborted by an application callback.

**错误描述**

操作被应用程序回调中止。

**可能原因**

回调函数中存在异常逻辑处理，如：死循环、异常中断、耗时较长的同步操作等。

**处理步骤**

检查所有回调函数，确保没有冗余的处理逻辑。

## 1007900045 本地连接端绑定失败

**错误信息**

Failed binding local connection end.

**错误描述**

本地连接端绑定失败。

**可能原因**

指定的网络接口、IP不存在或不可用。

**处理步骤**

检查网络接口、IP是否存在或是否被占用。

## 1007900047 重定向次数达到最大值

**错误信息**

Number of redirects hit maximum amount.

**错误描述**

重定向次数达到最大值。

**可能原因**

重定向次数过多。

**处理步骤**

排查服务器实现。

## 1007900049 提供了格式不正确的选项

**错误信息**

Malformed option provided in a setopt.

**错误描述**

提供了格式不正确的选项。

**可能原因**

可能是因为[StaticDnsRule](remote-communication-rcp.md#staticdnsrule)或者[DynamicDnsRule](remote-communication-rcp.md#dynamicdnsrule)传入的IP地址格式不正确。

**处理步骤**

确认[StaticDnsRule](remote-communication-rcp.md#staticdnsrule)或者[DynamicDnsRule](remote-communication-rcp.md#dynamicdnsrule)传入参数格式是否正确可用。

## 1007900052 服务器没有返回内容

**错误信息**

Server returned nothing (no headers, no data).

**错误描述**

服务器没有返回内容。

**可能原因**

与服务器实现有关。

**处理步骤**

排查服务器实现。

## 1007900055 发送网络数据失败

**错误信息**

Failed sending data to the peer.

**错误描述**

无法向对端发送数据，发送网络数据失败。

**可能原因**

网络问题。

**处理步骤**

排查网络。

## 1007900056 接收网络数据失败

**错误信息**

Failure when receiving data from the peer.

**错误描述**

无法从对端收到数据，接收网络数据失败。

**可能原因**

网络问题。

**处理步骤**

排查网络问题。

## 1007900058 本地SSL证书错误

**错误信息**

Problem with the local SSL certificate.

**错误描述**

本地SSL证书错误。

**可能原因**

SSL证书格式有错误。

**处理步骤**

检查SSL证书格式。

## 1007900059 无法使用指定的密码

**错误信息**

Couldn't use specified SSL cipher.

**错误描述**

无法使用指定的密码。

**可能原因**

client和sever协商的加密算法系统不支持。

**处理步骤**

抓包分析协商的算法。

## 1007900060 远程服务器SSL证书或SSH秘钥不正确

**错误信息**

SSL peer certificate or SSH remote key was not OK.

**错误描述**

远程服务器SSL证书或SSH秘钥错误或者无效。

**可能原因**

1. 无法校验服务器身份，有可能是证书过期了。
2. 证书自身异常。
3. 调用方设置的CA异常。

**处理步骤**

1. 检查证书有效性。常见的异常原因：证书是自签名证书、访问了Portal（门户认证）网站等。
2. 查看访问的服务器的证书颁发者信息。

   * 浏览器访问目标服务器地址，进入证书查看界面，在证书的详细信息中，查看“颁发者” 字段的颁发者名称信息，检查颁发者是否是受信任的机构。
   * 采集故障扩展信息字段或者日志，查看关键字段[issuers](remote-communication-error-field.md#issuers)，通过IssuerName判断证书颁发者是否是对应服务器返回。
3. 采集故障扩展信息字段或者日志，查看如下关键字信息：

   * [tstGlbUsr](remote-communication-error-field.md#tstglbusr)、[tstCurUsr](remote-communication-error-field.md#tstcurusr)：参考[网络连接安全配置](../harmonyos-guides/network-connection-security-configuration.md)信任CA证书。
   * [caFun](remote-communication-error-field.md#cafun)：若使用了自定义回调函数，请查看回调函数的逻辑正确性。
   * [selfCaPath](remote-communication-error-field.md#selfcapath)：若使用了自定义CA文件夹，请分析排查自定义CA文件夹下的证书与服务器证书是否匹配。
   * [selfCaFile](remote-communication-error-field.md#selfcafile)：若使用了自定义证书文件，请分析排查自定义证书文件。
   * [selfCaBlob](remote-communication-error-field.md#selfcablob)：若使用了自定义证书内容，请分析排查自定义证书内容。

## 1007900061 无法识别或错误的HTTP编码格式

**错误信息**

Unrecognized or bad HTTP Content or Transfer-Encoding.

**错误描述**

无法识别或错误的HTTP编码格式。

**可能原因**

HTTP编码格式不正确。

**处理步骤**

排查服务器实现，目前仅支持gzip编码。

## 1007900063 超出最大文件大小

**错误信息**

Maximum file size exceeded.

**错误描述**

超出最大文件大小。

**可能原因**

content-length的值与文件的实际大小不一致。

**处理步骤**

排查服务器实现。

## 1007900065 发送失败，因为数据流回退操作失败

**错误信息**

Send failed since rewinding of the data stream failed.

**错误描述**

发送失败，因为数据流回退操作失败。

**可能原因**

网络异常导致的数据重传。

**处理步骤**

检查网络状态是否正常。

## 1007900070 服务器磁盘空间不足

**错误信息**

Disk full or allocation exceeded.

**错误描述**

服务器磁盘空间不足。

**可能原因**

服务器磁盘已满。

**处理步骤**

检查服务器磁盘空间。

## 1007900073 服务器返回文件已存在

**错误信息**

Remote file already exists.

**错误描述**

服务器返回文件已存在。

**可能原因**

上传文件的时候，服务器返回文件已经存在。

**处理步骤**

排查服务器。

## 1007900077 SSL CA证书不存在或没有访问权限

**错误信息**

Problem with the SSL CA cert (path? access rights?).

**错误描述**

SSL CA证书不存在或没有访问权限。

**可能原因**

证书不存在或者没有访问权限。

**处理步骤**

检查证书是否存在或者有没有访问权限。

## 1007900078 URL请求的文件不存在

**错误信息**

Remote file not found.

**错误描述**

URL请求的文件不存在。

**可能原因**

URL请求的文件不存在。

**处理步骤**

检查URL请求的文件是否存在。

## 1007900089 已达到最大连接数限制

**错误信息**

The max connection limit is reached.

**错误描述**

已达到最大连接数限制。

**可能原因**

session连接数量已达到最大值，当前没有可用的连接。

**处理步骤**

控制同时发起的请求并发数量，请求完成后及时关闭使用的连接。

## 1007900090 SSL公钥与固定的公钥不匹配

**错误信息**

SSL public key does not match pinned public key.

**错误描述**

SSL公钥与固定的公钥不匹配。

**可能原因**

1、服务器证书被更换后与客户端证书不再匹配。

2、客户端公钥格式错误。

**处理步骤**

1、确保公钥格式正确。

2、确保客户端与服务端使用的公钥一致。

## 1007900092 HTTP/2 框架层中的流错误

**错误信息**

Stream error in the HTTP/2 framing layer.

**错误描述**

HTTP/2 框架层中的流错误。

**可能原因**

1、HTTP/2 流被服务器主动关闭。

2、代理服务器或防火墙错误的拦截或修改。

**处理步骤**

1、检查服务器关闭HTTP/2流的原因。

2、检查代理或防火墙的拦截规则。

## 1007900094 身份校验失败

**错误信息**

An authentication function returned an error.

**错误描述**

身份校验失败。

**可能原因**

传入的校验身份的字段与服务器不匹配。

**处理步骤**

排查传入的校验身份的字段是否与服务器匹配。

## 1007900095 HTTP/3错误

**错误信息**

HTTP/3 error.

**错误描述**

HTTP/3错误。

**可能原因**

服务器或网络不支持HTTP/3协议。

**处理步骤**

1、使用更低版本的HTTP协议发起请求。

2、要求服务端升级HTTP协议。

## 1007900097 代理握手错误

**错误信息**

proxy handshake error.

**错误描述**

代理握手错误。

**可能原因**

1、代理服务器地址或端口配置错误。

2、代理认证失败。

3、代理服务器拒绝连接。

**处理步骤**

1、检查代理服务器配置是否正确。

2、确保代理可用。

3、检查代理服务器日志，确认错误原因。

## 1007900100 数据长度超过允许的范围

**错误信息**

A value or data field grew larger than allowed.

**错误描述**

数据长度超过允许的范围。

**可能原因**

请求的数据或上传的内容过大，超出了客户端或服务器的限制。

**处理步骤**

1、使用流式数据传输接口。

2、检查上传或下载的数据是否在服务端允许的范围内。

## 1007900999 内部错误

**错误信息**

Internal Error.

**错误描述**

内部错误。

**可能原因**

通常意味着在系统中发生了一些未知的错误，导致无法完成请求。

**处理步骤**

如果遇到此错误，请尝试重新启动应用程序或联系技术支持以获取帮助。

## 1007900998 所请求的方法不被支持

**错误信息**

Method not supported.

**错误描述**

方法不被支持。

**可能原因**

使用一个不被支持的API 方法或协议。

**处理步骤**

检查代码或应用程序，确保使用的方法和协议是正确的。

## 1007900997 无效的内容类型

**错误信息**

Invalid content type.

**错误描述**

内容类型无效。

**可能原因**

使用不受支持的数据格式或内容类型进行请求。

**处理步骤**

确保请求的是正确的内容类型，并使用支持的数据格式进行请求。

## 1007900996 代理类型不支持

**错误信息**

Proxy type not supported.

**错误描述**

代理类型不支持。

**可能原因**

使用不受支持的代理类型。

**处理步骤**

换一种代理类型或者禁用代理，然后重新连接。

## 1007900995 获取系统代理失败

**错误信息**

Get system proxy failed.

**错误描述**

获取到的系统代理失败。

**可能原因**

没有正确配置代理设置或代理设置不正确导致的。

**处理步骤**

检查网络设置，确保代理设置正确。

## 1007900994 会话数达到限制

**错误信息**

Sessions number reached limit.

**错误描述**

会话数达到限制。

**可能原因**

session创建数量过多导致，自5.1.0(18)版本开始最多可创建1024个session实例。

**处理步骤**

减少创建的session数量，不超过1024个。

## 1007900993 会话已关闭

**错误信息**

Session is closed.

**错误描述**

会话已关闭。

**可能原因**

应用程序在尝试使用已经关闭的会话或会话已过期的情况下执行某些操作。

**处理步骤**

在应用程序中重新打开会话或创建新的会话，以便继续执行所需的操作。

## 1007900992 请求已被取消

**错误信息**

Request is canceled.

**错误描述**

该请求已被取消。

**可能原因**

由于请求超时，网络连接中断等原因导致的。

**处理步骤**

尝试重新发起请求，并确保网络连接稳定。

## 1007900991 服务器返回的响应内容不符合预期的格式或规范

**错误信息**

The response is invalid.

**错误描述**

服务器返回的响应内容不符合预期的格式或规范，导致客户端无法正确解析或处理该响应

**可能原因**

客户端请求的参数或格式不符合服务器的预期，导致服务器返回错误的响应。

**处理步骤**

验证客户端发送的请求是否正确，确保所有必要的参数都已正确设置，并且请求的格式符合服务器的要求。

## 1007900990 内存不足

**错误信息**

Out of memory.

**错误描述**

系统无法分配出内存。

**可能原因**

当前系统内存不足、应用占用过多内存、应用存在内存泄漏等原因。

**处理步骤**

排查应用或系统的内存占用情况，也可尝试重启应用或系统。

## 1007900988 文件打开错误

**错误信息**

Cannot open file.

**错误描述**

文件打开错误。

**可能原因**

当前应用没有对此路径文件进行读写的权限。

**处理步骤**

检查应用是否有对此路径文件进行读写的权限。

## 1007900987 创建目录时发生错误

**错误信息**

Cannot create directory.

**错误描述**

创建目录时发生错误。

**可能原因**

当前应用没有对此路径进行创建目录的权限。

**处理步骤**

检查应用是否有对此路径进行创建目录的权限。

## 1007900986 建立蜂窝链接超时

**错误信息**

Cannot establish cellular link.

**错误描述**

通过使用[PathPreference](remote-communication-rcp.md#pathpreference)的'cellular'模式拉起蜂窝数据连接时，因为条件不满足而导致激活蜂窝超时。

**可能原因**

用户开启飞行模式或SIM卡去激活等无法激活蜂窝数据场景。

**处理步骤**

检查网络情况，确保满足蜂窝激活条件。

## 1007900985 文件系统IO错误。

**错误信息**

File system IO error.

**错误描述**

文件操作失败。

**可能原因**

文件创建、访问或者删除失败场景。

**处理步骤**

检查是否具备文件路径访问权限、文件路径是否合法等原因。

## 1007900401 接口参数错误

**错误信息**

Parameter error.

**错误描述**

参数非法。

**可能原因**

入参数据不符合接口规范要求。

**处理步骤**

检查入参数据，确保符合业务逻辑。

## 1007900201 禁止明文传输

**错误信息**

Plaintext transmission is forbidden.

**错误描述**

禁止明文传输。

**可能原因**

禁止了 Remote Communication Kit 的 HTTP 明文传输。

**处理步骤**

检查 network\_config.json 中关于HTTP明文传输的相关配置是否符合业务需求。

## 1007910001 请求数据传输错误

**错误信息**

Urpc some error.

**错误描述**

URPC数据传输过程发生错误。

**可能原因**

参见URPC的日志。

**处理步骤**

排查URPC日志确认具体错误原因。

## 1007910002 请求超时

**错误信息**

Timeout was reached.

**错误描述**

URPC请求超出开发者配置的[UrpcConnectConfiguration](remote-communication-urpcapi.md#urpcconnectconfiguration)时长。

**可能原因**

1. 请求侧请求发送失败，底层发送队列阻塞。
2. 服务侧发生异常，未正常回复response。

**处理步骤**

1. 原因1重试请求发送。
2. 原因2重启服务端。

## 1007910003 请求被取消

**错误信息**

Request is cancel.

**错误描述**

URPC请求被取消。

**可能原因**

某次发送的URPC请求因调用的资源被清理而被取消。

**处理步骤**

排查业务流程是否存在请求未发送完毕就清理资源。

## 1007910004 连接断开

**错误信息**

Urpc disconnect.

**错误描述**

URPC连接断开。

**可能原因**

网络原因导致网络断开。

**处理步骤**

排查网络情况。

## 1007910005 请求数量达到上限

**错误信息**

Limit of request number.

**错误描述**

URPC请求数目达到服务端请求处理上限。

**可能原因**

开发者发送大量请求且未对其相应进行处理。

**处理步骤**

排查请求侧实现。

## 1007910006 请求大小达到上限

**错误信息**

Limit of request size.

**错误描述**

URPC请求大小达到系统内存上限。

**可能原因**

开发者发送的请求大小超出上限。

**处理步骤**

排查请求侧实现。

## 1007910008 恢复发送失败

**错误信息**

Resume transmit error.

**错误描述**

断点续传的请求，恢复发送失败。

**可能原因**

触发断点续传时，发送链路异常。

**处理步骤**

排查请求侧日志。

## 1007910099 取消时Stub查询失败

**错误信息**

Urpc stub not found.

**错误描述**

在调用cancel方法时，未查询到Stub。

**可能原因**

Stub提前触发销毁了。

**处理步骤**

排查[UrpcStub](remote-communication-urpcapi.md#urpcstub)类的声明和使用是否正确。

## 10079100997 数据反序列化失败

**错误信息**

Deserialize failed.

**错误描述**

数据反序列化失败。

**可能原因**

数据内容错误，与预期的序列化后的数据不符。

**处理步骤**

根据日志，排查服务侧数据发送状况。

## 10079100998 远程调用方法错误

**错误信息**

Function name error.

**错误描述**

请求侧的方法名指定错误。

**可能原因**

请求侧的方法名指定错误。

**处理步骤**

排查请求侧方法名。

## 10079100999 URPC Stub查询失败

**错误信息**

Urpc stub not found.

**错误描述**

未正确使用Urpcstub。

**可能原因**

stub使用错误。

**处理步骤**

排查[UrpcStub](remote-communication-urpcapi.md#urpcstub)类的声明和使用是否正确。
