---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/faqs-permissions-debug
title: 抓包/调试权限常见问题
breadcrumb: 指南 > 系统 > 安全 > 程序访问控制 > 应用权限管控 > 程序访问控制常见问题 > 抓包/调试权限常见问题
category: harmonyos-guides
scraped_at: 2026-11-12T09:51:30+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:e158011486f4008b1f8ac39bc3ba51750039057fb83ab06d371b304c08f8ad70
---

## ohos.permission.kernel.NET\_RAW权限使用说明

**约束与限制：**

* 仅支持在PC/2in1设备上申请使用。
* 在PC/2in1设备上，二进制程序可以申请ohos.permission.kernel.NET\_RAW权限进行网络抓包，使用时需要sudo提权使权限生效。

**使用说明：**

以[tcpdump工具](https://gitcode.host/OpenHarmonyToolkitsPlaza/tcpdump)为例，使用[二进制签名工具](binary-sign-tool.md)签名时在module.json文件中配置ohos.permission.kernel.NET\_RAW权限。

```json
{
    "requestPermissions": [
        {
            "name": "ohos.permission.kernel.NET_RAW"
        }
    ]
}
```

在hishell终端中使用sudo提权执行携带ohos.permission.kernel.NET\_RAW权限的tcpdump，认证成功后可以进行下述操作：

* 支持通过PF\_PACKET协议族创建PACKET类型套接字，在数据链路层直接捕获原始网络帧。
* 支持通过NETLINK\_ROUTE和NETLINK\_GENERIC类型的netlink套接字与内核通信，可以查询和管理网络接口。

```shell
# 示例
sudo ./tcpdump
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

```json
{
    "requestPermissions": [
        {
            "name": "ohos.permission.kernel.DEBUGGER"
        }
    ]
}
```

在hishell终端中，使用携带ohos.permission.kernel.DEBUGGER权限的lldb工具，以ATTACH模式附加到调试证书签名的debug\_bin进行调试。

```shell
# 示例：
# 确认UID一致
UID            PID  PPID C STIME TTY          TIME CMD
20020109     50262 32365 0 17:29:41 ?     00:00:00 lldb
20020109     52219 50262 0 17:31:15 ?     00:00:00 lldb-server
20020109     57631 13564 0 17:31:15 ?     00:00:00 debug_bin

# 附加到目标进程
(lldb) process attach --name debug_bin
```

## ohos.permission.kernel.ALLOW\_DEBUG使用说明

**约束与限制：**

* 仅支持在PC/2in1设备上申请使用。
* 在PC/2in1设备上，二进制程序或应用申请ohos.permission.kernel.ALLOW\_DEBUG权限后，可作为被调试方，支持被同UID且具备ohos.permission.kernel.DEBUGGER权限的二进制程序或应用调试。

  此外，Deveco Studio在使用真机设备调试时，如果PC/2in1设备上的应用使用了release签名并且配置了ohos.permission.kernel.ALLOW\_DEBUG权限，也支持被attach调试。

**使用说明：**

以DevEco Studio真机设备调试PC应用为例，在应用的module.json5文件中配置ohos.permission.kernel.ALLOW\_DEBUG权限。

```json5
{
    "requestPermissions": [
        {
            "name": "ohos.permission.kernel.ALLOW_DEBUG"
        }
    ]
}
```

在DecEco Studio调试器的进程列表中可以查看到携带ohos.permission.kernel.ALLOW\_DEBUG权限的发布应用进程，选择目标进程后即可进行附加并调试，具体可参考[应用调试](ide-debug-app.md)。

## ohos.privilege.operate\_raw\_net\_packets使用说明

**约束与限制：**

* 仅支持在PC/2in1设备上申请使用。
* 仅支持应用程序使用，不适用于二进制程序。
* 允许应用在授权后直接操作本机网络数据包的收发，包括创建原始套接字、访问数据链路层、开启混杂模式监听网络流量，以及构造自定义网络报文。这些能力可用于网络诊断、协议分析、性能测试和自定义协议实现。

**使用说明：**

应用在需要操作原始网络数据包前，通过osAccount提供的授权管理接口申请ohos.privilege.operate\_raw\_net\_packets特权。应用处于前台时，系统会以弹窗方式向设备使用者申请授权（若此前已存在有效授权，则直接复用，不再重复弹窗）；设备使用者同意授权后，应用即可获得操作原始网络数据包的能力。有关该特权的详细定义（包括授权策略），请参见[系统账号特权列表](../harmonyos-references/appendix-osaccount-authorization-privileges.md)。

```ts
// 示例
import { osAccount } from '@kit.BasicServicesKit';

let authManager: osAccount.AuthorizationManager = osAccount.getAuthorizationManager();
let privilege: string = 'ohos.privilege.operate_raw_net_packets';
let authOpt: osAccount.AcquireAuthorizationOptions = {
  isReuseNeeded: true,
  isInteractionAllowed: true
};
let authResult: osAccount.AcquireAuthorizationResult = await authManager.acquireAuthorization(privilege, authOpt);
if (authResult.resultCode === osAccount.AuthorizationResultCode.AUTHORIZATION_SUCCESS) {
  // 授权成功，可执行原始网络数据包相关操作
}
```

授权成功后，应用可以进行下述操作：

* 支持通过创建原始套接字，直接操作本机网络数据包的收发。
* 支持访问数据链路层，并开启混杂模式监听网络流量。
* 支持构造自定义网络报文，可用于网络诊断、协议分析、性能测试和自定义协议实现。
