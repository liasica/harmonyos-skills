---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/faqs-permissions-debug
title: 抓包/调试权限常见问题
breadcrumb: 指南 > 系统 > 安全 > 程序访问控制 > 应用权限管控 > 抓包/调试权限常见问题
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:04+08:00
doc_updated_at: 2026-04-13
content_hash: sha256:7e7add062b11efb7035eb2b6594d1dd43f8d5a28f6bb71b09cba182f94fb13d3
---

## ohos.permission.kernel.NET\_RAW权限使用说明

**约束与限制：**

* 仅支持在PC/2in1设备上申请使用。
* 在PC/2in1设备上，二进制程序可以申请ohos.permission.kernel.NET\_RAW权限进行网络抓包，使用时需要sudo提权使权限生效。

**使用说明：**

以[tcpdump工具](https://gitcode.host/OpenHarmonyToolkitsPlaza/tcpdump)为例，使用[二进制签名工具](binary-sign-tool.md)签名时在module.json文件中配置ohos.permission.kernel.NET\_RAW权限。

```
1. {
2. "requestPermissions": [
3. {
4. "name": "ohos.permission.kernel.NET_RAW"
5. }
6. ]
7. }
```

在hishell终端中使用sudo提权执行携带ohos.permission.kernel.NET\_RAW权限的tcpdump，认证成功后可以进行下述操作：

* 支持通过PF\_PACKET协议族创建PACKET类型套接字，在数据链路层直接捕获原始网络帧。
* 支持通过NETLINK\_ROUTE和NETLINK\_GENERIC类型的netlink套接字与内核通信，可以查询和管理网络接口。

```
1. # 示例
2. sudo ./tcpdump
```

## ohos.permission.kernel.DEBUGGER权限使用说明

**约束与限制：**

* 仅支持在PC/2in1设备上申请使用。
* 仅允许调试同UID进程。
* 在PC/2in1设备上，二进制程序或应用申请ohos.permission.kernel.DEBUGGER权限后，可作为调试方，调试与其具有相同UID的以下内容：

  1. 自签名的二进制程序。
  2. 调试证书签名的应用/二进制程序。
  3. 由发布证书签名且具备 ohos.permission.kernel.ALLOW\_DEBUG 权限的应用/二进制程序。

**使用说明：**

以[lldb高性能调试器](debug-lldb.md)为例，使用[二进制签名工具](binary-sign-tool.md)签名时在module.json文件中配置ohos.permission.kernel.DEBUGGER权限。

```
1. {
2. "requestPermissions": [
3. {
4. "name": "ohos.permission.kernel.DEBUGGER"
5. }
6. ]
7. }
```

在hishell终端中，使用携带ohos.permission.kernel.DEBUGGER权限的lldb工具，以ATTACH模式附加到调试证书签名的debug\_bin进行调试。

```
1. # 示例：
2. # 确认UID一致
3. UID            PID  PPID C STIME TTY          TIME CMD
4. 20020109     50262 32365 0 17:29:41 ?     00:00:00 lldb
5. 20020109     52219 50262 0 17:31:15 ?     00:00:00 lldb-server
6. 20020109     57631 13564 0 17:31:15 ?     00:00:00 debug_bin

8. # 附加到目标进程
9. (lldb) process attach --name debug_bin
```

## ohos.permission.kernel.ALLOW\_DEBUG使用说明

**约束与限制：**

* 仅支持在PC/2in1设备上申请使用。
* 在PC/2in1设备上，二进制程序或应用申请ohos.permission.kernel.ALLOW\_DEBUG权限后，可作为被调试方，支持被同UID且具备ohos.permission.kernel.DEBUGGER权限的二进制程序或应用调试。

  此外，Deveco Studio在使用真机设备调试时，如果PC/2in1设备上的应用使用了release签名并且配置了ohos.permission.kernel.ALLOW\_DEBUG权限，也支持被attach调试。

**使用说明：**

以DevEco Studio真机设备调试PC应用为例，在应用的module.json5文件中配置ohos.permission.kernel.ALLOW\_DEBUG权限。

```
1. {
2. "requestPermissions": [
3. {
4. "name": "ohos.permission.kernel.ALLOW_DEBUG"
5. }
6. ]
7. }
```

在DecEco Studio调试器的进程列表中可以查看到携带ohos.permission.kernel.ALLOW\_DEBUG权限的发布应用进程，选择目标进程后即可进行附加并调试，具体可参考[应用调试](ide-debug-app.md)。
