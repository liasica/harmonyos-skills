---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket
title: Socket错误码
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > 错误码 > Socket错误码
category: harmonyos-references
scraped_at: 2026-09-18T06:49:59+08:00
doc_updated_at: 2026-09-17
content_hash: sha256:656b9e701ef2d43ef4b0247e88ba77057b89fabe4a9f91d69d4190cb9b221e94
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码](errorcode-universal.md)说明文档。

Socket错误码映射关系：2301000 + [内核错误码](errorcode-kernel.md)。

Socket server错误码映射关系：2303100 + [内核错误码](errorcode-kernel.md)。

**连接断开场景错误码说明：**

* 服务端主动断开：对端正常关闭时TCPSocket/TLSSocket均触发close事件，无错误码；对端异常断开（连接重置）时，TCPSocket的send()或message/error事件返回2301104，TLSSocket返回2303505（TLS系统调用错误）。
* 客户端主动断开：本地close()后，TCPSocket继续调用send()、getState()等接口返回2301009，继续send()返回2301032或2301108。
* 蜂窝原因断开：TCPSocket.connect()/send()时底层蜂窝网络断开，返回2301100、2301101或2301113，弱网超时返回2301110。
* 应用内部原因断开：TCPSocket本地close()后误操作返回2301009、2301032或2301108；对未建立连接的socket调用TCPSocketServer.send()等接口返回2303207。

## 2301001 操作不允许

**错误信息**

Operation not permitted.

**错误描述**

操作不允许。

**可能原因**

非法操作。

**处理步骤**

检查操作步骤。

## 2301002 文件不存在

**错误信息**

No such file or directory.

**错误描述**

文件不存在。

**可能原因**

文件不存在。

**处理步骤**

检查文件名或文件路径。

## 2301003 进程不存在

**错误信息**

No such process.

**错误描述**

进程不存在。

**可能原因**

进程不存在。

**处理步骤**

排查进程信息。

## 2301004 系统调用中断

**错误信息**

Interrupted system call.

**错误描述**

系统调用中断。

**可能原因**

系统调用中断。

**处理步骤**

排查系统调用。

**TCP/UDP 错误码说明：**

TCP/UDP Socket其余错误码映射形式为：2301000 + Linux系统内核错误码errno，关键信息请参考Linux系统内核错误码。

## 2300002 系统内部错误

**错误信息**

System internal error.

**错误描述**

系统内部错误。

**可能原因**

1.内存异常。

2.空指针。

**处理步骤**

1.检查内存空间是否充足，清理内存后重试。

2.系统异常，请稍后重试或重启设备。

## 2301206 SOCKS5连接代理服务器失败

**错误信息**

Socks5 failed to connect to the proxy server.

**错误描述**

SOCKS5客户端连接代理服务器失败。

**可能原因**

代理服务器地址有误。

**处理步骤**

排查代理服务器地址是否正确。

## 2301207 SOCKS5认证用户名或密码无效

**错误信息**

Socks5 username or password is invalid.

**错误描述**

SOCKS5使用用户名密码认证方式时，用户名或者密码无效。

**可能原因**

用户名密码有误。

**处理步骤**

排查用户名密码是否设置准确。

## 2301208 SOCKS5连接远程服务器失败

**错误信息**

Socks5 failed to connect to the remote server.

**错误描述**

SOCKS5代理连接远程服务器失败。

**可能原因**

远程服务器网络问题。

**处理步骤**

排查远程服务器网络状况。

## 2301209 SOCKS5协商认证方式失败

**错误信息**

Socks5 failed to negotiate the authentication method.

**错误描述**

SOCKS5协商认证方式失败。

**可能原因**

代理服务器不支持客户端提供的认证方式。

**处理步骤**

排查代理服务器是否支持客户端提供的认证方式。

## 2301210 SOCKS5发送消息失败

**错误信息**

Socks5 failed to send the message.

**错误描述**

SOCKS5因系统调用错误，发送消息失败。

**可能原因**

内存溢出、参数无效等，关键信息请参考日志中Linux系统内核错误码。

**处理步骤**

尝试新建socket，再次发起连接。

## 2301211 SOCKS5接收消息失败

**错误信息**

Socks5 failed to receive the message.

**错误描述**

SOCKS5因系统调用错误，接收消息失败。

**可能原因**

内存溢出、参数无效等，关键信息请参考日志中Linux系统内核错误码。

**处理步骤**

尝试新建socket，再次发起连接。

## 2301212 SOCKS5消息序列化失败

**错误信息**

Socks5 serialization error.

**错误描述**

SOCKS5消息序列化失败。

**可能原因**

用户名密码过长，代理服务器、远端服务器地址和协议类型不匹配。

**处理步骤**

排查用户名密码长度是否过长，代理服务器、远端服务器的地址和协议类型是否匹配。

## 2301213 SOCKS5消息反序列化失败

**错误信息**

Socks5 deserialization error.

**错误描述**

SOCKS5消息反序列化失败。

**可能原因**

服务器响应数据包长度不符合协议。

**处理步骤**

排查服务器响应数据包。

## 2303104 中断系统调用

**错误信息**

Interrupted system call.

**错误描述**

中断系统调用。

**可能原因**

调用connect时，可能会导致阻塞时间过长，所以系统产生中断信号，返回EINTR错误。

**处理步骤**

尝试重新走网络连接流程。

## 2303109 错误文件编号

**错误信息**

Bad file number.

**错误描述**

在本地关闭的套接字上进行操作将返回该错误。

**可能原因**

socket fd可能被关闭了，所以发生参数无效的错误。

**处理步骤**

检查socket是否被意外关闭。

## 2301009 错误文件描述符

**错误信息**

Bad file descriptor.

**错误描述**

文件描述符无效或已关闭。

**可能原因**

1. Socket已被关闭或销毁。
2. Socket未正确创建。
3. 在已关闭的Socket上执行操作。
4. Socket fd被意外关闭，日志提示poll to send failed, socket is .\*, errno is 9或fcntl F\_GETFL error, errno is .\*，其中 .\* 为通配符。

**处理步骤**

1. 检查Socket是否被意外关闭。
2. 确保在调用其他方法前Socket已正确创建并处于有效状态。
3. 若Socket已关闭，请重新创建Socket实例。

## 2301013 权限不足

**错误信息**

Insufficient permissions.

**错误描述**

权限不足，操作被拒绝。

**可能原因**

1. 应用缺少必要的网络权限配置（如ohos.permission.INTERNET）。
2. 系统权限限制，如访问特定端口需要特殊权限。

**处理步骤**

1. 检查module.json5中是否配置了必要的网络权限（如ohos.permission.INTERNET）。
2. 确认操作是否符合权限要求。可通过日志关键词"Permission denied"定位该错误。

## 2301032 连接已断开仍发送数据

**错误信息**

Broken pipe.

**错误描述**

向已断开连接发送数据，连接的另一端（服务端或本地）已关闭。

**可能原因**

1. 服务端主动关闭连接后，本地仍调用send发送数据（errno为32，EPIPE）。
2. 本地主动关闭连接后，仍调用send发送数据。

**处理步骤**

1. 结合断开时机判断：服务端先关闭则为服务端主动断开；本地先关闭则为客户端主动断开。
2. 停止发送，重新建立连接后再发送数据。

## 2301100 网络已关闭

**错误信息**

Network is down.

**错误描述**

网络已关闭，连接断开。

**可能原因**

1. 蜂窝网络断开、无网络信号或开启飞行模式（errno为100，ENETDOWN）。
2. 网络服务未启动或已停止。

**处理步骤**

1. 判断为蜂窝/网络原因导致的断开，非应用内部原因。
2. 检查网络连接状态，恢复网络后重新建立连接。

## 2301101 网络不可达

**错误信息**

Network is unreachable.

**错误描述**

网络不可达，连接断开。

**可能原因**

1. 蜂窝数据网络不可用或未开启（errno为101，ENETUNREACH）。
2. 网络路由异常或网关不可达。

**处理步骤**

1. 判断为蜂窝/网络原因导致的断开。
2. 检查网络连接状态，恢复网络后重新建立连接。

## 2301104 连接被对端重置

**错误信息**

Connection reset by peer.

**错误描述**

连接被对端重置，通常表示服务端主动断开连接。

**可能原因**

1. 服务端主动断开连接并发送RST（errno为104，ECONNRESET）。
2. 服务端进程异常退出，或连接被服务端超时回收。

**处理步骤**

1. 判断为服务端主动断开。
2. 确认服务端运行状态，重新建立连接。

## 2301108 连接已关闭仍发送数据

**错误信息**

Cannot send after transport endpoint shutdown.

**错误描述**

本地已关闭连接后仍发送数据。

**可能原因**

本地主动调用close或shutdown后继续调用send（errno为108，ESHUTDOWN）。

**处理步骤**

1. 判断为客户端主动断开后的误操作。
2. 检查代码流程，确认关闭连接后不再发送数据。

## 2301110 连接超时

**错误信息**

Connection timed out.

**错误描述**

连接超时，通常由弱网或蜂窝网络问题导致。

**可能原因**

1. 弱网或蜂窝网络信号差，数据无法在超时时间内送达（errno为110，ETIMEDOUT）。
2. 长时间无数据交互，连接被网络设备回收。

**处理步骤**

1. 判断为网络原因（蜂窝/弱网）导致的断开。
2. 检查网络质量，恢复网络后重新建立连接。

## 2301113 主机不可达

**错误信息**

No route to host.

**错误描述**

目标主机不可达。

**可能原因**

1. 蜂窝网络无法路由到目标主机（errno为113，EHOSTUNREACH）。
2. 目标服务器已下线或IP地址变更。

**处理步骤**

1. 判断为网络原因（蜂窝/路由）导致的断开。
2. 检查目标主机可达性与网络状态。

## 2301115 连接正在进行或连接失败

**错误信息**

Operation now in progress.

**错误描述**

TCP异步连接正在进行，或连接超时/失败时框架返回的兼容错误码。

**可能原因**

1. TCP异步连接正在进行中（errno为115，EINPROGRESS），尚未返回最终连接结果。
2. 调用TCPSocket.connect时连接超时或失败，框架统一返回EINPROGRESS（兼容处理）。
3. 调用LocalSocket.connect连接超时或失败时，也可能返回该错误码。

**处理步骤**

1. 若连接仍在进行，等待connect回调或'connect'事件后再执行后续操作。
2. 若已超时，检查网络连接状态及对端服务状态，重新发起连接。

## 2301011 操作将阻塞

**错误信息**

Operation would block.

**错误描述**

操作可能会阻塞。

**可能原因**

1. 在非阻塞Socket上执行了会阻塞的操作（errno为11，EAGAIN）。
2. Socket发送缓冲区已满，或当前资源暂时不可用。

**处理步骤**

1. 等待Socket可写后重试。
2. 检查Socket状态和资源占用情况。

## 2301022 参数无效

**错误信息**

Invalid argument.

**错误描述**

参数无效。

**可能原因**

1. 传入的参数不合法（errno为22，EINVAL）。
2. 传入的IP地址、端口或Socket选项取值不正确。

**处理步骤**

1. 检查传入参数的取值和格式是否正确。
2. 参考接口参数说明重新设置参数。

## 2301088 非套接字的套接字操作

**错误信息**

Not a socket.

**错误描述**

对非Socket文件描述符执行了Socket操作。

**可能原因**

1. Socket未正确创建或已被销毁（errno为88，ENOTSOCK）。
2. 在已关闭的Socket上执行了操作。

**处理步骤**

1. 检查Socket是否正确创建且未被关闭。
2. 重新创建Socket后再执行操作。

## 2301098 网络地址已被使用

**错误信息**

Address already in use.

**错误描述**

网络地址已被使用。

**可能原因**

1. 绑定的本地地址已被其他Socket占用（errno为98，EADDRINUSE）。
2. 端口未释放，仍处于TIME\_WAIT状态。

**处理步骤**

1. 更换绑定的地址或端口。
2. 等待端口释放或关闭占用端口的连接。

## 2301099 不能分配请求的地址

**错误信息**

Cannot assign requested address.

**错误描述**

不能分配请求的地址。

**可能原因**

1. 绑定的IP地址不属于本机（errno为99，EADDRNOTAVAIL）。
2. 指定的本地地址无效或不可用。

**处理步骤**

1. 检查绑定的IP地址是否为本机地址。
2. 更换为可用的本地地址。

## 2301111 连接被拒绝

**错误信息**

Connection refused.

**错误描述**

连接被拒绝。

**可能原因**

1. 目标地址没有进程在监听（errno为111，ECONNREFUSED）。
2. 目标服务端未启动，或防火墙拒绝了连接请求。

**处理步骤**

1. 确认目标服务端已启动并监听对应端口。
2. 检查网络防火墙或安全策略配置。

## 2303111 资源暂时不可用，请重试

**错误信息**

Resource temporarily unavailable. Try again.

**错误描述**

系统资源暂时不可用，尝试再次调用。

**可能原因**

系统资源繁忙。

**处理步骤**

重新调用接口。

## 2303188 非套接字的套接字操作

**错误信息**

Socket operation on non-socket.

**错误描述**

参数socket未指定一个套接字描述符。

**可能原因**

参数不是套接字类型的描述符。

**处理步骤**

检查代码描述符的获取是否正确。

## 2303191 socket协议类型错误

**错误信息**

Incorrect socket protocol type.

**错误描述**

参数设置的协议类型错误。

**可能原因**

标识了协议的Socket函数在不支持的socket上进行操作，如Internet UDP协议不能被标识为SOCK\_STREAM socket类型。

**处理步骤**

检查参数设置是否符合协议类型。

## 2303198 网络地址已被使用

**错误信息**

Address already in use.

**错误描述**

地址已被使用。

**可能原因**

如果应用程序试图将套接字绑定到已用于现有套接字的IP地址/端口，或未正确关闭的套接字，或仍在关闭过程中的套接字，则会发生此错误。

**处理步骤**

尝试其他地址。

## 2303199 不能分配请求的地址

**错误信息**

Cannot assign requested address.

**错误描述**

请求的地址在其上下文中无效。

**可能原因**

当远程地址或端口对远程计算机无效时，可能发生该问题。

**处理步骤**

检查地址或端口是否正确。

## 2303200 网络已关闭

**错误信息**

Network is down.

**错误描述**

网络已关闭。

**可能原因**

网络服务未启动或已停止。

**处理步骤**

检查网络连接。

## 2303207 套接字未连接

**错误信息**

Socket is not connected.

**错误描述**

对未建立连接的套接字执行了需要连接的操作。

**可能原因**

1. 在连接建立成功前执行了发送等操作（errno为107，ENOTCONN）。
2. 连接已断开，但仍在套接字上执行操作。

**处理步骤**

1. 先建立连接，再执行相关操作。
2. 检查连接状态，必要时重新发起连接。

## 2303210 连接超时

**错误信息**

Connection timed out.

**错误描述**

长时间不能和远程服务器建立连接。

**可能原因**

这种情况一般发生在服务器主机崩溃。

**处理步骤**

本地无法处理此问题，需确认远程服务器是否出现故障。

## 2303501 SSL为空

**错误信息**

SSL is null.

**错误描述**

SSL对象为空。

**可能原因**

1. [TLSSocket.connect](js-apis-socket.md#connect9)方法未调用。
2. [TLSSocket.connect](js-apis-socket.md#connect9)方法执行失败。
3. SSL连接未成功建立。
4. TLSSocket未正确绑定（未调用bind方法），日志提示"tlsSocket is null"。

**处理步骤**

1. 确保在调用其他方法前先成功调用[TLSSocket.connect](js-apis-socket.md#connect9)方法。
2. 检查connect方法的执行结果，确认连接已成功建立。
3. 若connect失败，请排查失败原因后重新尝试连接。

## 2303502 TLS读取错误

**错误信息**

An error occurred when reading data on the TLS socket.

**错误描述**

在TLS套接字上读取数据时发生错误。

**可能原因**

底层socket阻塞。

**处理步骤**

重新执行接收数据的操作。

## 2303503 TLS写入错误

**错误信息**

An error occurred when writing data on the TLS socket.

**错误描述**

在TLS套接字上写入数据时发生错误。

**可能原因**

发送端缓冲区已满时，底层套接字发送将给出EWOULDBLOCK错误，这意味着服务器没有读取从客户端发送的消息。

**处理步骤**

需检查服务器状态并进行修复。

## 2303504 查找x509时出错

**错误信息**

An error occurred when verifying the X.509 certificate.

**错误描述**

认证x509证书发生错误，操作未完成。

**可能原因**

本地证书和服务器证书不匹配。

**处理步骤**

检查本地CA根证书和服务器证书是否匹配。

## 2303505 TLS系统调用错误

**错误信息**

An error occurred in the TLS system call.

**错误描述**

TLS系统调用发生不可恢复的致命I/O错误。

**可能原因**

1. 网络问题导致通信失败。
2. 底层Socket异常。
3. TLS握手过程中发生错误。
4. Socket在TLS操作过程中被关闭，日志提示poll to recv failed, socket is .\*, errno is .\*或recv fail, socket:.\*, errno:.\*，其中 .\* 为通配符。常见errno值参考：errno=9（EBADF，无效文件描述符）、errno=104（ECONNRESET，连接被重置）、errno=110（ETIMEDOUT，连接超时）、errno=111（ECONNREFUSED，连接被拒绝）。

**处理步骤**

1. 请参阅日志中的内核通用错误码errno以了解详细信息。
2. 检查网络连接状态。
3. 尝试重新建立TLS连接。

## 2303506 关闭TLS连接失败

**错误信息**

Failed to close the TLS connection.

**错误描述**

关闭TLS连接失败。

**可能原因**

协议中出现关闭警报时，即连接已完全关闭时，才会返回此结果代码。

**处理步骤**

尝试重新发起连接。

## 2303601 Socket文件描述符无效

**错误信息**

Invalid socket FD.

**错误描述**

Socket文件描述符无效。

**可能原因**

1. Socket未正确创建或已被关闭。
2. 在已销毁的Socket上执行了操作。

**处理步骤**

1. 检查Socket是否有效。
2. 重新创建Socket后再执行操作。

## 2303602 套接字未连接

**错误信息**

Socket is not connected.

**错误描述**

套接字未连接。

**可能原因**

1. 在连接建立前执行了需要连接的操作。
2. 连接已被关闭后继续操作。

**处理步骤**

1. 先建立连接再执行操作。
2. 检查连接状态，重新发起连接。
