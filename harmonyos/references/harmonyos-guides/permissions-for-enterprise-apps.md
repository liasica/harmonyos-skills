---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/permissions-for-enterprise-apps
title: 企业类应用可用权限
breadcrumb: 指南 > 系统 > 安全 > 程序访问控制 > 应用权限管控 > 应用权限列表 > 企业类应用可用权限
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:03+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:54074e661b8d641f7d8583dfa0192d89ea2463866c1b234646f25696ef60a0f1
---

以下权限面向企业类应用开放。

企业类应用包括企业普通应用和MDM（Mobile Device Management）设备管理应用。

企业类应用有以下特征：

* 仅在企业定制设备上运行，不会在普通消费者设备上运行。
* 分发类型分别为enterprise\_normal（企业普通应用）和enterprise\_mdm（MDM应用）。
* 不会上架华为应用市场。

企业类应用可参考[声明权限](declare-permissions.md)，申请以下权限。

注意

以下权限不支持自动签名，因此在调试和发布阶段，均需参照[手动签名](ide-signing.md#section297715173233)的步骤，完成手动签名。

## ohos.permission.SET\_FILE\_GUARD\_POLICY

允许应用下发文件管控策略。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：10

**变更信息**：API 10-14时，其权限级别为system\_core，仅面向MDM应用开放；从API 14开始，权限级别变更为system\_basic，开放范围变更为企业普通应用。

## ohos.permission.FILE\_GUARD\_MANAGER

允许应用进行公共目录扫描及设置文件扩展属性。

当前扩展属性包括文件密级、文件标签。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：10

**变更信息**：API 10-14时，其权限级别为system\_core，仅面向MDM应用开放；从API 14开始，权限级别变更为system\_basic，开放范围变更为企业普通应用。

## ohos.permission.FILE\_GUARD\_FILE\_WRITE

允许企业应用修改文件。

获取该权限后，应用可以获取用户数据中指定文件的写权限，并修改文件。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：20

## ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS

允许应用跨系统本地账号交互。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：7

**变更信息**：API 7-13该权限仅向系统应用开放；从API 14开始，开放范围从系统应用变更为企业普通应用。

## ohos.permission.GET\_RUNNING\_INFO

允许应用获取运行态信息。

可获取其他应用的运行态信息，包括Ability、Extension、Application的信息。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：7

**变更信息**：API 7-13该权限仅向系统应用开放；从API 14开始，开放范围从系统应用变更为企业普通应用。

## ohos.permission.RUNNING\_STATE\_OBSERVER

允许应用监听应用状态。

获取该权限后，可注册应用状态监听器。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：7

**变更信息**：API 7-13该权限仅向系统应用开放；从API 14开始，开放范围从系统应用变更为企业普通应用。

## ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED

允许查询应用的基本信息和其他敏感信息。

如应用包名，版本等信息。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：7

**变更信息**：API 7-13该权限仅向系统应用开放；从API 14开始，开放范围从系统应用变更为企业普通应用。

## ohos.permission.GET\_WIFI\_CONFIG

允许应用获取Wi-Fi的配置信息。

该权限允许应用获取SSID、PSK、加密方式等Wi-Fi配置的相关信息。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：8

**变更信息**：API 8-14该权限仅向系统应用开放；从API 15开始，开放范围从系统应用变更为企业普通应用。

## ohos.permission.SET\_WIFI\_CONFIG

允许应用配置Wi-Fi信息。

该权限允许应用添加、删除Wi-Fi，以及修改Wi-Fi的配置信息。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：8

**变更信息**：API 8-14该权限仅向系统应用开放；从API 15开始，开放范围变更为企业普通应用。

## ohos.permission.GET\_DOMAIN\_ACCOUNTS

允许应用查询域账号信息。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：10

**变更信息**：API 10-13该权限仅向系统应用开放；从API 14开始，开放范围变更为企业普通应用。

## ohos.permission.QUERY\_AUDIT\_EVENT

允许企业安全类应用查询安全审计事件。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：12

**变更信息**：API 12-13该权限仅面向MDM应用开放；从API 14开始，开放范围从MDM应用变更为企业普通应用。

## ohos.permission.KILL\_APP\_PROCESSES

允许系统应用结束其他应用进程。

获取权限后，可终止其他正在运行中的应用，允许它在必要时对系统中的进程进行管理和控制。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：12

**变更信息**：API 7-13该权限仅向系统应用开放；从API 14开始，开放范围从系统应用变更为企业普通应用。

## ohos.permission.MANAGE\_ENTERPRISE\_WIFI\_CONNECTION

允许应用管理Wi-Fi的连接。

获取该权限后，可执行开启/关闭、连接、断开Wi-Fi等操作。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**ACL使能**：true

**起始版本**：15

## ohos.permission.ACCESS\_ENTERPRISE\_USER\_TRUSTED\_CERT

允许应用管理企业设备的用户CA证书。

在企业设备上企业应用使用私有的CA证书认证企业服务器时，该权限用于允许企业应用把私有CA证书安装到企业设备上，并对安装的CA证书进行管理操作。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：18

## ohos.permission.MANAGE\_NET\_FIREWALL

允许系统应用配置防火墙规则。

当前仅2in1设备应用可申请此权限。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：12

**变更信息**：API 12-14该权限仅向系统应用开放；从API 15开始，开放范围变更为企业普通应用。

## ohos.permission.GET\_NET\_FIREWALL

允许系统应用查询防火墙规则和查询防火墙拦截记录。

当前仅2in1设备应用可申请此权限。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：12

**变更信息**：API 12-14该权限仅向系统应用开放；从API 15开始，开放范围变更为企业普通应用。

## ohos.permission.GET\_DOMAIN\_ACCOUNT\_SERVER\_CONFIGS

允许应用获取域账号服务器配置。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：18

## ohos.permission.MANAGE\_DOMAIN\_ACCOUNT\_SERVER\_CONFIGS

允许应用管理域账号服务器配置。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：18

## ohos.permission.MANAGE\_DOMAIN\_ACCOUNTS

允许应用管理域账号。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：18

## ohos.permission.GET\_SIGNATURE\_INFO

允许应用获取应用包的签名信息。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：18

## ohos.permission.VISIBLE\_WINDOW\_INFO

允许应用获取当前屏幕的可见窗口信息。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：18

## ohos.permission.kernel.AUTH\_AUDIT\_EVENT

允许企业安全应用阻断安全审计事件。

企业安全应用申请此权限后，可以阻断安全审计事件。这些事件包括文件创建，文件打开和文件删除等。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：20

## ohos.permission.SUPPORT\_APP\_SERVICE\_EXTENSION

允许应用作为AppServiceExtension被拉起。

获取此权限后，应用可作为AppServiceExtension被同应用或同在"appidentifierAllowList"配置中的应用拉起或连接。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：20

## ohos.permission.ENTERPRISE\_MANAGE\_EAP

允许企业网络安全软件在EAP报文中新增私有信息。

获取此权限后，允许企业网络安全软件获取802.1x报文并新增信息，完成定制化认证需求。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：20

## ohos.permission.SUPPORT\_INSTALL\_ON\_U1

允许企业普通应用安装在特定用户下。

特定用户是支持应用单例运行的用户。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：20

## ohos.permission.QUERY\_LOCAL\_WORKSPACES

允许企业普通应用查询工作空间和不允许删除的空间列表。

获取此权限后，可查询工作空间的基本信息，以及哪些空间已被设置成不可删除。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：20

## ohos.permission.SET\_NET\_EXT\_ATTRIBUTE

允许应用设置网络扩展属性。

获取该权限后，应用可以通过API为网络设置扩展属性以标识网络是内部网络还是外部网络。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：20

## ohos.permission.MANAGE\_ANTIVIRUS

允许企业应用管理防病毒软件。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：20

## ohos.permission.REGISTER\_ANTIVIRUS

允许企业防病毒软件向系统注册、更新基本信息。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：20

## ohos.permission.CALL\_TPM\_CMD

允许应用调用TPM（Trusted Platform Module）命令。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：20

## ohos.permission.ENTERPRISE\_WORKSPACES\_EVENT\_SUBSCRIBE

允许企业应用订阅企业数字空间相关事件。

获取此权限后，可以通过spaceManager.subscribeEvent和spaceManager.unsubscribeEvent，订阅和取消订阅企业数字空间相关事件。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：20

## ohos.permission.sec.ACCESS\_UDID

允许应用获取UDID。

UDID（Unified Device ID）是设备的唯一标识。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：7

**变更信息**：API 7-19该权限仅向系统应用开放；从API 20开始，开放范围从系统应用变更为企业普通应用。
