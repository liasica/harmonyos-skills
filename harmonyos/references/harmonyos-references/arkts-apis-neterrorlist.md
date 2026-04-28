---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-neterrorlist
title: @ohos.web.netErrorList (ArkWeb网络协议栈错误列表)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.netErrorList (ArkWeb网络协议栈错误列表)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:12+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b6eac359f4be97a5b419b23bd42a3761027b927c1ec732184bcfb55dfb3f10c3
---

ArkWeb的网络协议栈错误列表。

ArkWeb网络协议栈错误码直接映射Chromium错误码[net\_error\_list.h](https://chromium.googlesource.com/chromium/src.git/+/refs/heads/main/net/base/net_error_list.h)。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { WebNetErrorList } from '@kit.ArkWeb';
```

## WebNetErrorList

PhonePC/2in1TabletTVWearable

ArkWeb的网络协议栈错误列表

**系统能力**：SystemCapability.Web.Webview.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NET\_OK | 0 | 访问正常。 |
| ERR\_IO\_PENDING | -1 | 异步IO操作尚未完成。 |
| ERR\_FAILED | -2 | 一般性的错误。 |
| ERR\_ABORTED | -3 | 操作已被中止。 |
| ERR\_INVALID\_ARGUMENT | -4 | 参数无效。 |
| ERR\_INVALID\_HANDLE | -5 | 文件描述符的句柄是无效的。 |
| ERR\_FILE\_NOT\_FOUND | -6 | 文件未找到。 |
| ERR\_TIMED\_OUT | -7 | 操作超时。 |
| ERR\_FILE\_TOO\_LARGE | -8 | 文件过大。 |
| ERR\_UNEXPECTED | -9 | 遇到了一个未被预期或未被特定处理的问题。 |
| ERR\_ACCESS\_DENIED | -10 | 访问除了网络以外的资源被拒绝。 |
| ERR\_NOT\_IMPLEMENTED | -11 | 功能未实现，导致操作失败。 |
| ERR\_INSUFFICIENT\_RESOURCES | -12 | 系统或程序执行所需的资源不足。 |
| ERR\_OUT\_OF\_MEMORY | -13 | 内存溢出。 |
| ERR\_UPLOAD\_FILE\_CHANGED | -14 | 上传文件失败因为文件的修改时间不符合预期。 |
| ERR\_SOCKET\_NOT\_CONNECTED | -15 | 长连接断开。 |
| ERR\_FILE\_EXISTS | -16 | 文件已存在。 |
| ERR\_FILE\_PATH\_TOO\_LONG | -17 | 文件路径或者文件名过长。 |
| ERR\_FILE\_NO\_SPACE | -18 | 磁盘没有足够空间。 |
| ERR\_FILE\_VIRUS\_INFECTED | -19 | 文件包含病毒。 |
| ERR\_BLOCKED\_BY\_CLIENT | -20 | 客户端已阻止该请求。 |
| ERR\_NETWORK\_CHANGED | -21 | 网络发生变化。 |
| ERR\_BLOCKED\_BY\_ADMINISTRATOR | -22 | 被管理员阻止。 |
| ERR\_SOCKET\_CONNECTED | -23 | socket已经处于连接状态。 |
| ERR\_UPLOAD\_STREAM\_REWIND\_NOT\_SUPPORTED | -25 | 上传重传不支持。 |
| ERR\_CONTEXT\_SHUT\_DOWN | -26 | 因为上下文已关闭导致请求失败。 |
| ERR\_BLOCKED\_BY\_RESPONSE | -27 | 请求失败，因为响应不满足要求（例如“X-Frame-Options”和“Content Security Policy”检查以及“Cross Origin Resource Policy”）。 |
| ERR\_CLEARTEXT\_NOT\_PERMITTED | -29 | 该请求被系统策略阻止，不允许部分或全部明文请求。 |
| ERR\_BLOCKED\_BY\_CSP | -30 | 请求被内容安全策略阻止。 |
| ERR\_H2\_OR\_QUIC\_REQUIRED | -31 | 由于没有H/2或QUIC会话，请求被阻止。 |
| ERR\_BLOCKED\_BY\_ORB | -32 | 请求被 CORB 或 ORB 阻止。 |
| ERR\_CONNECTION\_CLOSED | -100 | 连接已关闭（对应于TCP FIN）。 |
| ERR\_CONNECTION\_RESET | -101 | 连接被重置（对应于TCP RST）。 |
| ERR\_CONNECTION\_REFUSED | -102 | 连接被拒绝。 |
| ERR\_CONNECTION\_ABORTED | -103 | 由于未接收到发送数据的ACK，连接超时。这可能包括一个未得到ACK的FIN数据包。 |
| ERR\_CONNECTION\_FAILED | -104 | 连接失败。 |
| ERR\_NAME\_NOT\_RESOLVED | -105 | 域名无法解析。 |
| ERR\_INTERNET\_DISCONNECTED | -106 | 网络断开连接。 |
| ERR\_SSL\_PROTOCOL\_ERROR | -107 | SSL 协议错误。 |
| ERR\_ADDRESS\_INVALID | -108 | IP地址或端口号无效（例如，无法连接到IP地址0或端口0）。 |
| ERR\_ADDRESS\_UNREACHABLE | -109 | 无法访问IP地址。这通常意味着没有到指定主机或网络的路由。 |
| ERR\_SSL\_CLIENT\_AUTH\_CERT\_NEEDED | -110 | 服务器指定需要客户端提供SSL证书来校验身份。 |
| ERR\_TUNNEL\_CONNECTION\_FAILED | -111 | 无法建立通过代理的隧道连接。 |
| ERR\_NO\_SSL\_VERSIONS\_ENABLED | -112 | 不支持SSL协议的任何版本。 |
| ERR\_SSL\_VERSION\_OR\_CIPHER\_MISMATCH | -113 | 客户端和服务器不支持通用的SSL协议版本或密码套件。 |
| ERR\_SSL\_RENEGOTIATION\_REQUESTED | -114 | 服务器请求重新协商（rehandshake）。 |
| ERR\_PROXY\_AUTH\_UNSUPPORTED | -115 | 代理请求身份验证（隧道连接使用不支持的方法）。 |
| ERR\_BAD\_SSL\_CLIENT\_AUTH\_CERT | -117 | SSL 客户端证书错误。 |
| ERR\_CONNECTION\_TIMED\_OUT | -118 | 连接超时。 |
| ERR\_HOST\_RESOLVER\_QUEUE\_TOO\_LARGE | -119 | 挂起的DNS解析太多，因此队列中的请求被中止。 |
| ERR\_SOCKS\_CONNECTION\_FAILED | -120 | 无法为目标主机建立与 SOCKS 代理服务器的连接。 |
| ERR\_SOCKS\_CONNECTION\_HOST\_UNREACHABLE | -121 | 域名不可达。 |
| ERR\_ALPN\_NEGOTIATION\_FAILED | -122 | 协商备用协议的请求失败。 |
| ERR\_SSL\_NO\_RENEGOTIATION | -123 | 对方发送了SSL no\_renegotiation警报消息。 |
| ERR\_WINSOCK\_UNEXPECTED\_WRITTEN\_BYTES | -124 | Winsock有时会报告写入的数据多于传递的数据。这可能是由于LSP损坏。 |
| ERR\_SSL\_DECOMPRESSION\_FAILURE\_ALERT | -125 | SSL对等端向本端发送了致命的解压失败警报。当对等方错误地认为它支持DEFLATE压缩时，通常会发生这种情况。 |
| ERR\_SSL\_BAD\_RECORD\_MAC\_ALERT | -126 | SSL对等端向本端发送了致命的bad\_record\_mac警报。一个对DELEGATE支持有问题的服务器可能发生这个情况。 |
| ERR\_PROXY\_AUTH\_REQUESTED | -127 | 代理请求身份验证（用于隧道建立）。 |
| ERR\_PROXY\_CONNECTION\_FAILED | -130 | 无法创建到代理服务器的连接。域名解析或连接套接字时出错。请注意，这不包括HTTP代理的实际“CONNECT”方法期间的故障。 |
| ERR\_MANDATORY\_PROXY\_CONFIGURATION\_FAILED | -131 | 无法使用强制代理配置。目前，这意味着无法获取、解析或执行强制的PAC脚本。 |
| ERR\_PRECONNECT\_MAX\_SOCKET\_LIMIT | -133 | 在预连接时，已经达到了套接字池的最大套接字限制。因此不需要尝试预连接更多的套接字。 |
| ERR\_SSL\_CLIENT\_AUTH\_PRIVATE\_KEY\_ACCESS\_DENIED | -134 | 使用SSL客户端证书私钥的权限被拒绝。 |
| ERR\_SSL\_CLIENT\_AUTH\_CERT\_NO\_PRIVATE\_KEY | -135 | SSL客户端证书没有私钥。 |
| ERR\_PROXY\_CERTIFICATE\_INVALID | -136 | HTTPS 代理提供的证书无效。 |
| ERR\_NAME\_RESOLUTION\_FAILED | -137 | 域名解析时出错（DNS）。 |
| ERR\_NETWORK\_ACCESS\_DENIED | -138 | 网络被禁用。 |
| ERR\_TEMPORARILY\_THROTTLED | -139 | 因节流而取消了此请求以避免DDOS。 |
| ERR\_HTTPS\_PROXY\_TUNNEL\_RESPONSE\_REDIRECT | -140 | 通过HTTPS代理创建SSL隧道连接的请求收到302（响应正文可能包括请求失败原因的描述）。 |
| ERR\_SSL\_CLIENT\_AUTH\_SIGNATURE\_FAILED | -141 | 无法使用客户端证书的私钥对SSL客户端身份验证握手的CertificateVerify数据进行签名。 |
| ERR\_MSG\_TOO\_BIG | -142 | 消息太大，无法传输。（例如，超过大小阈值的UDP消息）。 |
| ERR\_WS\_PROTOCOL\_ERROR | -145 | Websocket协议错误。表示由于帧格式错误或其他协议冲突，正在终止连接。 |
| ERR\_ADDRESS\_IN\_USE | -147 | 尝试绑定已在使用的地址时返回。 |
| ERR\_SSL\_HANDSHAKE\_NOT\_COMPLETED | -148 | 由于SSL握手尚未完成，操作失败。 |
| ERR\_SSL\_BAD\_PEER\_PUBLIC\_KEY | -149 | SSL 公钥错误。 |
| ERR\_SSL\_PINNED\_KEY\_NOT\_IN\_CERT\_CHAIN | -150 | 收到的证书与内置域名指定的公钥不匹配。 |
| ERR\_CLIENT\_AUTH\_CERT\_TYPE\_UNSUPPORTED | -151 | 服务器对客户端证书的请求不包含本机支持的任何类型。 |
| ERR\_SSL\_DECRYPT\_ERROR\_ALERT | -153 | SSL对等端向本端发送了致命的decrypt\_error警报。当对等方无法正确验证签名（在CertificateVerify或ServerKeyExchange中）或验证Finished消息时，通常会发生这种情况。 |
| ERR\_WS\_THROTTLE\_QUEUE\_TOO\_LARGE | -154 | 挂起的WebSocketJob实例太多，因此没有将新Job推送到队列中。 |
| ERR\_SSL\_SERVER\_CERT\_CHANGED | -156 | SSL服务器证书在重新协商中更改。 |
| ERR\_SSL\_UNRECOGNIZED\_NAME\_ALERT | -159 | SSL服务器向本端发送了致命的未识别名称警报。 |
| ERR\_SOCKET\_SET\_RECEIVE\_BUFFER\_SIZE\_ERROR | -160 | 未能按请求设置套接字的接收缓冲区大小。 |
| ERR\_SOCKET\_SET\_SEND\_BUFFER\_SIZE\_ERROR | -161 | 未能按请求设置套接字的发送缓冲区大小。 |
| ERR\_SOCKET\_RECEIVE\_BUFFER\_SIZE\_UNCHANGEABLE | -162 | 尽管setsockopt返回了成功的代码，但未能按请求设置套接字的接收缓冲区大小。 |
| ERR\_SOCKET\_SEND\_BUFFER\_SIZE\_UNCHANGEABLE | -163 | 尽管setsockopt返回了成功的代码，但未能按请求设置套接字的发送缓冲区大小。 |
| ERR\_SSL\_CLIENT\_AUTH\_CERT\_BAD\_FORMAT | -164 | 无法将客户端证书从平台存储导入SSL库。 |
| ERR\_ICANN\_NAME\_COLLISION | -166 | 将主机名解析为包含IPv4地址“127.0.53.53”的IP地址列表。这是ICANN建议的一个特殊IP地址，用于表示存在名称冲突，并提醒管理员注意潜在问题。 |
| ERR\_SSL\_SERVER\_CERT\_BAD\_FORMAT | -167 | SSL服务器提供了一个无法解码的证书。这不是证书错误代码，因为没有X509Certificate对象可用。此错误是致命的。 |
| ERR\_CT\_STH\_PARSING\_FAILED | -168 | Certificate Transparency：解析signed tree head失败。 |
| ERR\_CT\_STH\_INCOMPLETE | -169 | Certificate Transparency: 解析signed tree head成功，但是缺少了一些信息。 |
| ERR\_UNABLE\_TO\_REUSE\_CONNECTION\_FOR\_PROXY\_AUTH | -170 | 在使用AuthController生成凭据之前，尝试重新使用连接发送代理身份验证凭据失败。调用方应使用新连接重新使用控制器。 |
| ERR\_CT\_CONSISTENCY\_PROOF\_PARSING\_FAILED | -171 | Certificate Transparency: 一致性验证解析失败。 |
| ERR\_SSL\_OBSOLETE\_CIPHER | -172 | SSL服务器需要一个不受支持的密码套件，该套件已被删除。此错误将在密码套件删除后立即在一个或两个版本的回退中临时发出信号，之后回退将被删除。 |
| ERR\_WS\_UPGRADE | -173 | 当WebSocket握手成功完成并且连接已升级时，URLRequest将被取消，并返回此错误代码。 |
| ERR\_READ\_IF\_READY\_NOT\_IMPLEMENTED | -174 | 套接字ReadIfReady支持未实现。 |
| ERR\_NO\_BUFFER\_SPACE | -176 | 没有可用的套接字缓冲区空间。 |
| ERR\_SSL\_CLIENT\_AUTH\_NO\_COMMON\_ALGORITHMS | -177 | 在本端的客户端证书私钥和服务器的首选项之间没有共同的签名算法。 |
| ERR\_EARLY\_DATA\_REJECTED | -178 | TLS 1.3 early data 被服务器拒绝。这将在从套接字返回任何数据之前接收。应在禁用early data的情况下重试请求。 |
| ERR\_WRONG\_VERSION\_ON\_EARLY\_DATA | -179 | TLS 1.3 early data 版本错误。 |
| ERR\_TLS13\_DOWNGRADE\_DETECTED | -180 | TLS 1.3已启用，但已协商更低的版本，服务器返回一个值，表示它支持TLS 1.3。这是TLS 1.3中安全检查的一部分，但也可能表明用户使用了一个有问题的TLS-terminating代理。 |
| ERR\_SSL\_KEY\_USAGE\_INCOMPATIBLE | -181 | 服务器的证书具有与协商的TLS密钥交换方法不兼容的keyUsage扩展。 |
| ERR\_INVALID\_ECH\_CONFIG\_LIST | -182 | 无法解析通过DNS获取的ECHConfigList。 |
| ERR\_ECH\_NOT\_NEGOTIATED | -183 | ECH已启用，但服务器无法解密加密的ClientHello。 |
| ERR\_ECH\_FALLBACK\_CERTIFICATE\_INVALID | -184 | ECH已启用，服务器无法解密加密的ClientHello，并且没有提供对公用名称有效的证书。 |
| ERR\_CERT\_COMMON\_NAME\_INVALID | -200 | 服务器响应时使用的证书的公用名称与主机名不匹配。这可能意味着：1.攻击者已将本端的流量重定向到他们的服务器，并提供了他们知道私钥的证书。2.服务器配置错误，使用错误的证书进行响应。3.用户在无线网络上，并被重定向到网络的登录页面。4.操作系统使用了DNS搜索后缀，服务器在地址栏中没有缩写名称的证书。 |
| ERR\_CERT\_DATE\_INVALID | -201 | 证书已过期。这可能意味着：1.攻击者正在出示一个旧证书，他们已设法获得该证书的私钥。2.服务器配置错误，没有提供有效的证书。3.设备的时钟错了。 |
| ERR\_CERT\_AUTHORITY\_INVALID | -202 | 未信任的证书签发机构。这可能意味着：1.攻击者用真实证书代替了包含其公钥并由其表亲签名的证书。2.服务器操作员拥有来自本端不知道但应该信任的CA的合法证书。3.服务器提供了一个自签名证书，无法抵御主动攻击者。 |
| ERR\_CERT\_CONTAINS\_ERRORS | -203 | 证书中包含错误。 |
| ERR\_CERT\_NO\_REVOCATION\_MECHANISM | -204 | 证书无撤销机制，实际上，此证书不能被吊销。 |
| ERR\_CERT\_UNABLE\_TO\_CHECK\_REVOCATION | -205 | 此网站的安全证书的吊销信息不可用。这可能意味着：1.一个攻击者破坏了证书中的私钥，并阻止了本端发现证书已被吊销的尝试。2.证书未被吊销，但吊销服务器正忙或不可用。 |
| ERR\_CERT\_REVOKED | -206 | 证书已撤销。本端有能力忽略这个错误，但这可能不是本端应该做的事情。 |
| ERR\_CERT\_INVALID | -207 | 证书非法。 |
| ERR\_CERT\_WEAK\_SIGNATURE\_ALGORITHM | -208 | 服务器以使用弱签名算法签名的证书作为响应。 |
| ERR\_CERT\_NON\_UNIQUE\_NAME | -210 | 证书中指定的域名不是唯一的。 |
| ERR\_CERT\_WEAK\_KEY | -211 | 服务器以包含弱密钥（例如，RSA密钥太小）的证书作为响应。 |
| ERR\_CERT\_NAME\_CONSTRAINT\_VIOLATION | -212 | 违反证书名称约束。 |
| ERR\_CERT\_VALIDITY\_TOO\_LONG | -213 | 证书有效期过长。 |
| ERR\_CERTIFICATE\_TRANSPARENCY\_REQUIRED | -214 | 此连接需要Certificate Transparency，但服务器未提供符合策略的CT信息。 |
| ERR\_CERT\_SYMANTEC\_LEGACY | -215 | 该证书链接到不再受信任的旧赛门铁克根目录。 |
| ERR\_CERT\_KNOWN\_INTERCEPTION\_BLOCKED | -217 | 已知该证书被设备所有者以外的实体用于拦截。 |
| ERR\_SSL\_OBSOLETE\_VERSION\_OR\_CIPHER | -218 | 连接使用过时版本的 SSL/TLS 或密码。 |
| ERR\_CERT\_END | -219 | 紧跟在上一个证书错误代码之后的值。 |
| ERR\_INVALID\_URL | -300 | 非法URL。 |
| ERR\_DISALLOWED\_URL\_SCHEME | -301 | 不允许使用的URL scheme。 |
| ERR\_UNKNOWN\_URL\_SCHEME | -302 | 未知 scheme。 |
| ERR\_INVALID\_REDIRECT | -303 | 试图加载URL导致重定向到无效的URL。 |
| ERR\_TOO\_MANY\_REDIRECTS | -310 | 重定向过多。 |
| ERR\_UNSAFE\_REDIRECT | -311 | 不安全的重定向。 |
| ERR\_UNSAFE\_PORT | -312 | 不安全的端口。 |
| ERR\_INVALID\_RESPONSE | -320 | 非法返回。 |
| ERR\_INVALID\_CHUNKED\_ENCODING | -321 | 分块传输编码错误。 |
| ERR\_METHOD\_UNSUPPORTED | -322 | 方法不支持。 |
| ERR\_UNEXPECTED\_PROXY\_AUTH | -323 | 意外的代理身份验证。 |
| ERR\_EMPTY\_RESPONSE | -324 | 空返回错误。 |
| ERR\_RESPONSE\_HEADERS\_TOO\_BIG | -325 | 返回体中 headers 太大。 |
| ERR\_PAC\_SCRIPT\_FAILED | -327 | pac 脚本错误。 |
| ERR\_REQUEST\_RANGE\_NOT\_SATISFIABLE | -328 | 请求范围不可满足。 |
| ERR\_MALFORMED\_IDENTITY | -329 | 用于身份验证的标识无效。 |
| ERR\_CONTENT\_DECODING\_FAILED | -330 | 响应正文的内容解码失败。 |
| ERR\_NETWORK\_IO\_SUSPENDED | -331 | 操作无法完成，因为所有网络IO都已挂起。 |
| ERR\_SYN\_REPLY\_NOT\_RECEIVED | -332 | 在流上未接收到SYN\_REPLY的情况下接收到的FLIP数据。 |
| ERR\_ENCODING\_CONVERSION\_FAILED | -333 | 将响应转换为目标编码失败。 |
| ERR\_UNRECOGNIZED\_FTP\_DIRECTORY\_LISTING\_FORMAT | -334 | 无法识别的 ftp 目录列表格式。 |
| ERR\_NO\_SUPPORTED\_PROXIES | -336 | 没有支持的代理。 |
| ERR\_HTTP2\_PROTOCOL\_ERROR | -337 | HTTP/2协议错误。 |
| ERR\_INVALID\_AUTH\_CREDENTIALS | -338 | 无效的身份验证凭据。 |
| ERR\_UNSUPPORTED\_AUTH\_SCHEME | -339 | 不支持的身份验证方案。 |
| ERR\_ENCODING\_DETECTION\_FAILED | -340 | 编码检测失败。 |
| ERR\_MISSING\_AUTH\_CREDENTIALS | -341 | 缺少身份验证凭据。 |
| ERR\_UNEXPECTED\_SECURITY\_LIBRARY\_STATUS | -342 | 意外的安全库状态。 |
| ERR\_MISCONFIGURED\_AUTH\_ENVIRONMENT | -343 | 配置错误的身份验证环境。 |
| ERR\_UNDOCUMENTED\_SECURITY\_LIBRARY\_STATUS | -344 | 取消文档安全库状态。 |
| ERR\_RESPONSE\_BODY\_TOO\_BIG\_TO\_DRAIN | -345 | 响应体太大。 |
| ERR\_RESPONSE\_HEADERS\_MULTIPLE\_CONTENT\_LENGTH | -346 | 响应 headers 多个内容长度。 |
| ERR\_INCOMPLETE\_HTTP2\_HEADERS | -347 | 不完整的 HTTP/2 headers。 |
| ERR\_PAC\_NOT\_IN\_DHCP | -348 | pac 不在 dhcp 中。 |
| ERR\_RESPONSE\_HEADERS\_MULTIPLE\_CONTENT\_DISPOSITION | -349 | 响应标头多重内容处置。 |
| ERR\_RESPONSE\_HEADERS\_MULTIPLE\_LOCATION | -350 | 多个位置的响应标头。 |
| ERR\_HTTP2\_SERVER\_REFUSED\_STREAM | -351 | HTTP/2 服务器拒绝流。 |
| ERR\_HTTP2\_PING\_FAILED | -352 | HTTP/2 ping 失败。 |
| ERR\_CONTENT\_LENGTH\_MISMATCH | -354 | 当连接关闭时，HTTP 响应主体传输的字节数少于 Content-Length 头中公布的字节数。 |
| ERR\_INCOMPLETE\_CHUNKED\_ENCODING | -355 | HTTP 响应体使用分块编码传输，但在连接关闭时从未发送终止零长度块。 |
| ERR\_QUIC\_PROTOCOL\_ERROR | -356 | 存在QUIC协议错误。 |
| ERR\_RESPONSE\_HEADERS\_TRUNCATED | -357 | HTTP 头部信息被文件结束符（EOF）截断。 |
| ERR\_QUIC\_HANDSHAKE\_FAILED | -358 | QUIC 加密握手失败。这意味着服务器无法读取发送的任何请求，因此它们可能会被重新发送。 |
| ERR\_HTTP2\_INADEQUATE\_TRANSPORT\_SECURITY | -360 | 传输安全性不适合HTTP/2版本。 |
| ERR\_HTTP2\_FLOW\_CONTROL\_ERROR | -361 | 对等方违反了HTTP/2流控制。 |
| ERR\_HTTP2\_FRAME\_SIZE\_ERROR | -362 | 对等方发送了大小不正确的HTTP/2帧。 |
| ERR\_HTTP2\_COMPRESSION\_ERROR | -363 | 压缩HTTP/2 头部信息的解码或编码失败。 |
| ERR\_PROXY\_AUTH\_REQUESTED\_WITH\_NO\_CONNECTION | -364 | 请求的代理身份验证没有有效的客户端套接字句柄。 |
| ERR\_HTTP\_1\_1\_REQUIRED | -365 | 在 HTTP/2 会话中收到 HTTP\_1\_1\_REQUIRED 错误代码。 |
| ERR\_PROXY\_HTTP\_1\_1\_REQUIRED | -366 | 在通过 HTTP/2 会话代理时收到 HTTP\_1\_1\_REQUIRED 错误代码。 |
| ERR\_PAC\_SCRIPT\_TERMINATED | -367 | PAC 脚本已终止并必须重新加载。 |
| ERR\_INVALID\_HTTP\_RESPONSE | -370 | 服务器应返回 HTTP/1.x 响应，但未返回。而不是将其视为 HTTP/0.9，返回此错误。 |
| ERR\_CONTENT\_DECODING\_INIT\_FAILED | -371 | 内容解码初始化失败。 |
| ERR\_HTTP2\_RST\_STREAM\_NO\_ERROR\_RECEIVED | -372 | 收到带有 NO\_ERROR 错误代码的 HTTP/2 RST\_STREAM 帧。此错误应由 HTTP/2 代码内部处理，而不应超过 SpdyStream 层。 |
| ERR\_HTTP2\_PUSHED\_STREAM\_NOT\_AVAILABLE | -373 | 请求声明的推送流不再可用。 |
| ERR\_HTTP2\_CLAIMED\_PUSHED\_STREAM\_RESET\_BY\_SERVER | -374 | 已声明推送的流，随后服务器将其重置。发生这种情况时，应该重试请求。 |
| ERR\_TOO\_MANY\_RETRIES | -375 | 由于身份验证或证书无效，HTTP事务重试次数过多。 |
| ERR\_HTTP2\_STREAM\_CLOSED | -376 | 在已关闭的流上收到一个 HTTP/2 帧。 |
| ERR\_HTTP2\_CLIENT\_REFUSED\_STREAM | -377 | 客户端拒绝了一个 HTTP/2 流。 |
| ERR\_HTTP2\_PUSHED\_RESPONSE\_DOES\_NOT\_MATCH | -378 | 基于匹配的 URL 和请求头，一个 HTTP/2 推送的流被请求所接收，但是推送的响应头并不匹配请求。 |
| ERR\_HTTP\_RESPONSE\_CODE\_FAILURE | -379 | 服务器返回了non-2xx的HTTP响应代码。 |
| ERR\_QUIC\_UNKNOWN\_CERT\_ROOT | -380 | 在 QUIC 连接上展示的证书未链接到已知根证书，并且连接到的原始服务器不在允许未知根证书的域名列表中。 |
| ERR\_QUIC\_GOAWAY\_REQUEST\_CAN\_BE\_RETRIED | -381 | 已接收到一个 GOAWAY 帧，表明请求未得到处理，因此可以安全地在不同的连接上重试。 |
| ERR\_TOO\_MANY\_ACCEPT\_CH\_RESTARTS | -382 | ACCEPT\_CH 重启已被触发太多次。 |
| ERR\_INCONSISTENT\_IP\_ADDRESS\_SPACE | -383 | 在相同的请求期间，远程端点的 IP 地址空间与先前观察到的值不同。任何受影响的请求的缓存条目都应被标记为无效。 |
| ERR\_CACHED\_IP\_ADDRESS\_SPACE\_BLOCKED\_BY\_LOCAL\_NETWORK\_ACCESS\_POLICY | -384 | 缓存的远程端点的 IP 地址空间被本地网络访问检查所阻止。 |
| ERR\_CACHE\_MISS | -400 | 缓存中没有请求的条目。 |
| ERR\_CACHE\_READ\_FAILURE | -401 | 无法从磁盘缓存中读取。 |
| ERR\_CACHE\_WRITE\_FAILURE | -402 | 无法写入磁盘缓存。 |
| ERR\_CACHE\_OPERATION\_UNSUPPORTED | -403 | 此条目不支持此操作。 |
| ERR\_CACHE\_OPEN\_FAILURE | -404 | 磁盘缓存无法打开此条目。 |
| ERR\_CACHE\_CREATE\_FAILURE | -405 | 磁盘缓存无法创建此条目。 |
| ERR\_CACHE\_RACE | -406 | 多个事务正在竞相创建磁盘缓存条目。 |
| ERR\_CACHE\_CHECKSUM\_READ\_FAILURE | -407 | 缓存无法读取条目上的校验和记录。 |
| ERR\_CACHE\_CHECKSUM\_MISMATCH | -408 | 缓存发现一个具有无效校验和的条目。 |
| ERR\_CACHE\_LOCK\_TIMEOUT | -409 | HTTP缓存的内部错误代码。 |
| ERR\_CACHE\_AUTH\_FAILURE\_AFTER\_READ | -410 | 在事务读取某些数据后收到质询，但凭据不可用。 |
| ERR\_CACHE\_ENTRY\_NOT\_SUITABLE | -411 | HTTP缓存的内部不完全错误代码 |
| ERR\_CACHE\_DOOM\_FAILURE | -412 | 磁盘缓存无法删除此条目。 |
| ERR\_CACHE\_OPEN\_OR\_CREATE\_FAILURE | -413 | 磁盘缓存无法打开或创建此条目。 |
| ERR\_INSECURE\_RESPONSE | -501 | 服务器的响应不安全（例如，存在证书错误）。 |
| ERR\_NO\_PRIVATE\_KEY\_FOR\_CERT | -502 | 尝试导入客户端证书失败，因为用户的密钥数据库缺少相应的私钥。 |
| ERR\_ADD\_USER\_CERT\_FAILED | -503 | 向操作系统证书数据库添加证书时发生错误。 |
| ERR\_INVALID\_SIGNED\_EXCHANGE | -504 | 处理已签名的交换时发生错误。 |
| ERR\_INVALID\_WEB\_BUNDLE | -505 | 处理Web Bundle源时发生错误。 |
| ERR\_TRUST\_TOKEN\_OPERATION\_FAILED | -506 | 执行Trust Tokens协议操作的请求失败（原因包括：预置条件失败、内部错误、不良响应）。 |
| ERR\_TRUST\_TOKEN\_OPERATION\_SUCCESS\_WITHOUT\_SENDING\_REQUEST | -507 | 在处理一个与Trust Tokens协议相关的操作执行请求时，系统能够执行该请求中的Trust Tokens操作，但并没有将请求发送到其指定的目的地。 |
| ERR\_FTP\_FAILED | -601 | FTP控制连接命令失败的通用错误。 |
| ERR\_FTP\_SERVICE\_UNAVAILABLE | -602 | 服务器目前无法满足请求。这是一个临时错误。FTP响应代码421。 |
| ERR\_FTP\_TRANSFER\_ABORTED | -603 | 服务器已中止传输。FTP响应代码426。 |
| ERR\_FTP\_FILE\_BUSY | -604 | 文件正在使用中，或在打开文件时发生了一些其他临时错误条件。FTP响应代码450。 |
| ERR\_FTP\_SYNTAX\_ERROR | -605 | 由于语法错误，服务器拒绝了本端的命令。FTP响应代码500、501。 |
| ERR\_FTP\_COMMAND\_UNSUPPORTED | -606 | 服务器不支持本端发出的命令。FTP响应代码502、504。 |
| ERR\_FTP\_BAD\_COMMAND\_SEQUENCE | -607 | 服务器拒绝了本端的命令，因为本端没有按照正确的顺序发出命令。FTP响应代码503。 |
| ERR\_PKCS12\_IMPORT\_BAD\_PASSWORD | -701 | 由于密码不正确，PKCS #12 导入失败。 |
| ERR\_PKCS12\_IMPORT\_FAILED | -702 | 由于其他错误，PKCS #12 导入失败。 |
| ERR\_IMPORT\_CA\_CERT\_NOT\_CA | -703 | CA导入失败-不是CA证书。 |
| ERR\_IMPORT\_CERT\_ALREADY\_EXISTS | -704 | 导入失败-数据库中已存在证书。 |
| ERR\_IMPORT\_CA\_CERT\_FAILED | -705 | 由于其他错误，CA导入失败。 |
| ERR\_IMPORT\_SERVER\_CERT\_FAILED | -706 | 由于某些内部错误，服务器证书导入失败。 |
| ERR\_PKCS12\_IMPORT\_INVALID\_MAC | -707 | PKCS #12 导入失败，因为 MAC（消息认证码）无效。 |
| ERR\_PKCS12\_IMPORT\_INVALID\_FILE | -708 | PKCS #12 导入失败，因为文件无效或已损坏。 |
| ERR\_PKCS12\_IMPORT\_UNSUPPORTED | -709 | 由于不支持的特性，PKCS #12 导入失败。 |
| ERR\_KEY\_GENERATION\_FAILED | -710 | 密钥生成失败。 |
| ERR\_PRIVATE\_KEY\_EXPORT\_FAILED | -712 | 无法导出私钥。 |
| ERR\_SELF\_SIGNED\_CERT\_GENERATION\_FAILED | -713 | 自签名证书生成失败。 |
| ERR\_CERT\_DATABASE\_CHANGED | -714 | 证书数据库已发生某种更改。 |
| ERR\_CERT\_VERIFIER\_CHANGED | -716 | 证书验证配置已发生某种更改。 |
| ERR\_DNS\_MALFORMED\_RESPONSE | -800 | DNS解析程序收到格式错误的响应。 |
| ERR\_DNS\_SERVER\_REQUIRES\_TCP | -801 | DNS服务器需要TCP。 |
| ERR\_DNS\_SERVER\_FAILED | -802 | DNS服务器失败。对于以下所有错误情况，都会返回此错误。1-格式错误-名称服务器无法解释查询。2-服务器故障-名称服务器由于自身问题无法处理这个查询。3-未实现-名称服务器不支持请求的查询类型。4-拒绝-名称服务器出于策略原因拒绝执行指定的操作。 |
| ERR\_DNS\_TIMED\_OUT | -803 | DNS事务超时。 |
| ERR\_DNS\_CACHE\_MISS | -804 | 对于只查询本地源的查找，在缓存或其他本地源中未找到该条目。 |
| ERR\_DNS\_SEARCH\_EMPTY | -805 | 后缀搜索列表规则阻止了给定主机名的解析。 |
| ERR\_DNS\_SORT\_ERROR | -806 | 未能根据RFC3484对地址进行排序。 |
| ERR\_DNS\_SECURE\_RESOLVER\_HOSTNAME\_RESOLUTION\_FAILED | -808 | 未能解析DNS-over-HTTPS服务器的主机名。 |
| ERR\_DNS\_NAME\_HTTPS\_ONLY | -809 | DNS已识别请求因不安全的连接（http/ws）而被禁止。应用程序应该像处理HTTP重定向一样处理这个错误，将连接重定向到安全的https或wss。 |
| ERR\_DNS\_REQUEST\_CANCELED | -810 | 与此任务相关的所有 DNS 请求已被取消。 |
| ERR\_DNS\_NO\_MATCHING\_SUPPORTED\_ALPN | -811 | HTTPS记录的主机名解析预期未能使用受支持协议的ALPN值进行解析。 |
