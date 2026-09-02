---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-kit-new-00001
title: VPN流程问题排查指南
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > VPN流程问题排查指南
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-07-15
content_hash: sha256:f8a83341c46edbed21baf9629b576b72a9a1184d1494261c5ed9aadf1ca2930a
---

## 问题现象

VPN从启动到销毁过程中，可能出现的异常场景有哪些，针对这些异常如何进行排查？

## 背景知识

VPN，即虚拟专用网络（Virtual Private Network），是在公用网络上建立专用网络的一种技术。HarmonyOS为开发者提供了用于创建VPN的API解决方案。当前提供三方VPN能力主要用于创建虚拟网卡及配置VPN路由信息，连接隧道过程及内部连接的协议需要应用内部自行实现。

## 解决方案

**阶段一：StartVpnExtensionAbility拉起VPN Extension进程**

**场景1：VPN Extension权限校验失败**

| 项目 | 内容 |
| --- | --- |
| **现象** | StartVpnExtensionAbility返回权限错误 |
| **错误码** | NETMANAGER\_EXT\_ERR\_PERMISSION\_DENIED(201) |
| **关键日志** | "query datebase fail." / "not allowed to start ability with different bundle name" |
| **排查方向** | 1. 检查调用方bundleName与VPN Extension的bundleName是否一致 2. 确认VPN应用是否通过了VPN权限弹窗授权 |

**场景2：EDM策略禁止VPN**

| 项目 | 内容 |
| --- | --- |
| **现象** | StartVpnExtensionAbility返回权限错误，企业策略禁用VPN |
| **错误码** | NETMANAGER\_EXT\_ERR\_PERMISSION\_DENIED(201) |
| **关键日志** | ```screen "persist.edm.vpn_disable disallowed setting up vpn" ``` |
| **排查方向** | 1. 检查系统属性: hdc shell param get persist.edm.vpn\_disable，若为true则被EDM策略禁用 2. 联系设备管理员解除VPN禁用策略 |

**场景3：AbilityManagerClient启动Extension失败**

| 项目 | 内容 |
| --- | --- |
| **现象** | StartVpnExtensionAbility返回错误，VPN Extension进程未被拉起 |
| **错误码** | NETMANAGER\_EXT\_ERR\_INTERNAL(2200003) |
| **关键日志** | "ConnectAbilityWithExtensionType failed" / "AbilityManagerClient is nullptr" |
| **排查方向** | 1. 检查VPN Extension的module.json中type是否配置为"vpn" 2. 检查VPN Extension进程是否已存在 3. 系统内部调用出现错误 |

**场景4：VPN权限弹窗用户拒绝**

| 项目 | 内容 |
| --- | --- |
| **现象** | VPN弹窗显示后用户点击拒绝，VPN Extension被停止 |
| **关键日志** | "VPN permission not authorized, show VPN dialog for bundleName" / "Failed to show VPN dialog" / "ShowVpnDialog: waiting for user authorization" |
| **排查方向** | 1. 确认VPN权限弹窗是否正常显示 2. 用户拒绝后VPN Extension Ability会被自动StopVpnExtensionAbility |

**场景5：VPN Service代理获取失败**

| 项目 | 内容 |
| --- | --- |
| **现象** | StartVpnExtensionAbility调用直接返回错误，VPN Extension进程未被拉起 |
| **错误码** | NETMANAGER\_EXT\_ERR\_GET\_PROXY\_FAIL(2200208) |
| **关键日志** | "StartVpnExtensionAbility proxy is nullptr" / "get SystemAbilityManager failed" / "get Remote vpn service failed" / "get Remote service proxy failed" |
| **排查方向** | 1. 系统内部调用出现错误 |

**阶段二：create创建VPN**

**场景1：VPN已存在，禁止重复创建**

| 项目 | 内容 |
| --- | --- |
| **现象** | create返回失败，VPN已存在 |
| **错误码** | NETWORKVPN\_ERROR\_VPN\_EXIST(2203002) |
| **关键日志** | "forbit setup, vpn exist already" / "vpn exist already, please execute destory first" / "vpn using by other user" |
| **排查方向** | 1. 检查当前是否已有VPN连接 2. 如有旧VPN先执行destroy再重新create 3. 检查是否系统VPN正在运行 |

**场景2：权限校验失败**

| 项目 | 内容 |
| --- | --- |
| **现象** | create返回权限错误 |
| **错误码** | NETMANAGER\_EXT\_ERR\_PERMISSION\_DENIED(201) |
| **关键日志** | "forbid setup, CheckVpnPermission" / "forbid setup, CheckCurrentAccountType" / "is not system call" / "Permission denied" |
| **排查方向** | 1. 检查VPN权限是否已授予 2. 检查EDM策略persist.edm.vpn\_disable 3. 确认当前用户是活跃用户 |

**场景3：用户类型不允许（访客/非活跃用户）**

| 项目 | 内容 |
| --- | --- |
| **现象** | create返回拒绝创建VPN |
| **错误码** | NETWORKVPN\_ERROR\_REFUSE\_CREATE\_VPN(2203001) |
| **关键日志** | "The guest user cannot execute the VPN interface." / "GetOsAccountType error" |
| **排查方向** | 1. 确认当前用户不是访客用户 2. 确认当前用户是活跃用户 3. 检查多用户场景下是否在正确的用户下操作 |

**场景4：系统创建VPN网络失败**

| 项目 | 内容 |
| --- | --- |
| **现象** | create返回内部错误 |
| **错误码** | NETMANAGER\_EXT\_ERR\_INTERNAL(2200003) |
| **关键日志** | "VpnConnect vpnConfig\_ is nullptr" / "SetUpVpn param config is nullptr" / "SetUpVpn SerializeFromVpnConfig fail" / "SetUpVpn register internal callback fail." / "vpn netManager RegisterNetSupplier error." / "vpn UpdateNetSupplierInfo error" / "vpn UpdateNetSupplierInfo netSupplierInfo\_ is nullptr" / "linkInfo is nullptr" |
| **排查方向** | 1. 系统内部调用出现错误 |

**场景5：VPN TUN FD获取失败**

| 项目 | 内容 |
| --- | --- |
| **现象** | TUN文件描述符无效，无法读写VPN数据 |
| **错误码** | NETMANAGER\_EXT\_ERR\_INTERNAL(2200003) / NETWORKVPN\_ERROR\_INVALID\_FD(2203004) |
| **关键日志** | "Invalid socket file discriptor" / tunFd <= 0 |
| **排查方向** | 1. 系统内部调用出现错误 |

**场景6：分布式调制解调器共享VPN冲突**

| 项目 | 内容 |
| --- | --- |
| **现象** | create返回内部错误 |
| **错误码** | NETMANAGER\_EXT\_ERR\_INTERNAL(2200003) |
| **关键日志** | ```screen "forbit setup, distributed modem is sharing vpn." ``` |
| **排查方向** | 1. 等待分布式VPN共享结束 2. 检查分布式VPN的连接状态 |

**场景7：多VPN IP地址冲突**

| 项目 | 内容 |
| --- | --- |
| **现象** | create返回内部错误 |
| **错误码** | NETMANAGER\_EXT\_ERR\_INTERNAL(2200003) |
| **关键日志** | "forbid setup, multi tun check ip address is same" / "ipsec check ip address is same error." |
| **排查方向** | 1. 检查新VPN的localAddress是否与已有VPN冲突 2. 调整VPN配置中的localAddress |

**阶段三：VPN网卡创建与路由配置**

**场景1：/dev/tun设备打开失败**

| 项目 | 内容 |
| --- | --- |
| **现象** | VPN网卡未创建 |
| **关键日志** | "open virtual device failed:" / "tun set iff error:" |
| **排查方向** | 1. 系统内部调用出现错误 |

**场景2：VPN地址配置失败**

| 项目 | 内容 |
| --- | --- |
| **现象** | VPN网卡无IP地址 |
| **关键日志** | "invalid IP address:" / "if\_nametoindex failed" / "Invalid prefix length" / "AddAttr failed" / "ioctl set ipv4 address failed" / "ioctl set ip mask failed" |
| **排查方向** | 1. 检查VpnConfig中IP地址格式 2. 检查prefix length(IPv4:0-32, IPv6:0-128) |

**场景3：VPN网卡UP失败**

| 项目 | 内容 |
| --- | --- |
| **现象** | 网卡处于DOWN状态 |
| **关键日志** | "set iff up failed" / "create SOCK\_DGRAM ip failed" |
| **排查方向** | 1. 系统内部调用出现错误 |

**场景4：VPN FD传递失败**

| 项目 | 内容 |
| --- | --- |
| **现象** | VPN Extension进程收不到TUN FD |
| **关键日志** | "memset\_s cmsgu.cmsg failed!" / "memset\_s message failed!" / "memcpy\_s cmsgu failed!" |
| **排查方向** | 1. 系统内部调用出现错误 |

**场景5：路由规则设置失败**

| 项目 | 内容 |
| --- | --- |
| **现象** | VPN路由规则未生效，流量未走VPN |
| **关键日志** | "invalid IP-rule priority" / "RouteManager cannot find interface" / "add route" |
| **排查方向** | 1. 检查路由配置中是否配置了正确的网卡名称与网关地址，IP格式是否正确 |

**阶段四：VPN生命周期管理**

**场景1：VPN Extension进程异常死亡**

| 项目 | 内容 |
| --- | --- |
| **现象** | VPN Extension进程crash或被kill，VPN连接断开 |
| **关键日志** | "vpn OnProcessDied" / "VPN HAP is OnProcessDied StopExtensionAbility" / "destroy vpn failed" / "OnProcessDied not vpn uid and pid" / "vpn OnRemoteDied" / "diedRemoted is null" / "system vpn client died" / "destroy vpn is VpnEvent" / "destroy vpn is failed" |
| **排查方向** | 1. 检查VPN Extension进程crash日志 2. 确认VPN资源是否被自动清理 |

**场景2：VPN应用卸载后VPN未清理**

| 项目 | 内容 |
| --- | --- |
| **现象** | VPN应用被卸载，但VPN连接和网卡仍存在 |
| **关键日志** | ```screen "COMMON_EVENT_PACKAGE_REMOVED, BundleName" ``` |
| **排查方向** | 1. 系统内部调用出现错误 |

**阶段五：DestroyVpn销毁VPN**

**场景1：非VPN创建者尝试销毁**

| 项目 | 内容 |
| --- | --- |
| **现象** | destroy返回操作失败 |
| **错误码** | NETMANAGER\_EXT\_ERR\_OPERATION\_FAILED(2200002) |
| **关键日志** | "not same vpn, can't destroy" / "DestroyVpn permission denied, caller uid" |
| **排查方向** | 1. 确认调用方UID与创建VPN的UID一致 2. 检查是否已创建VPN连接 |

**场景2：DestroyVpn内部失败**

| 项目 | 内容 |
| --- | --- |
| **现象** | destroy返回内部错误 |
| **错误码** | NETMANAGER\_EXT\_ERR\_INTERNAL(2200003) |
| **关键日志** | "destroy vpn is failed" / "destroy vpn failed" |
| **排查方向** | 1. 系统内部调用出现错误 |

**场景3：VPN路由表未清理**

| 项目 | 内容 |
| --- | --- |
| **现象** | Destroy后VPN路由规则残留 |
| **关键日志** | ```screen "Failed to remove interface" ``` |
| **排查方向** | 1. 系统内部调用出现错误 |

**阶段六：StopVpnExtensionAbility销毁VPN Extension进程**

**场景1：VPN Service SA代理获取失败**

| 项目 | 内容 |
| --- | --- |
| **现象** | StopVpnExtensionAbility调用直接返回错误 |
| **错误码** | NETMANAGER\_EXT\_ERR\_GET\_PROXY\_FAIL(2200208) |
| **关键日志** | ```screen "StopVpnExtensionAbility proxy is nullptr" ``` |
| **排查方向** | 1. 系统内部调用出现错误 |

**场景2：权限校验失败**

| 项目 | 内容 |
| --- | --- |
| **现象** | StopVpnExtensionAbility返回权限错误 |
| **错误码** | NETMANAGER\_EXT\_ERR\_PERMISSION\_DENIED(201) |
| **关键日志** | "StopVpnExtensionAbility permission check failed" / "not allowed to stop ability with different bundle name" |
| **排查方向** | 1. 确认调用方bundleName与VPN Extension一致 |

**场景3：AbilityManagerClient停止Extension失败**

| 项目 | 内容 |
| --- | --- |
| **现象** | Extension未被停止，VPN Extension进程仍在运行 |
| **关键日志** | ```screen "AbilityManagerClient is nullptr" ``` |
| **排查方向** | 1. 系统内部调用出现错误 |
