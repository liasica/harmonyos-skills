---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/permissions-for-enterprise-apps
title: 企业类应用可用权限
breadcrumb: 指南 > 系统 > 安全 > 程序访问控制 > 应用权限管控 > 应用权限列表 > 企业类应用可用权限
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:17+08:00
doc_updated_at: 2026-09-04
content_hash: sha256:0e2a474e71d27b2cf76aa3eb15b02765802ad68139d42096155d6559a74cce88
---

以下权限面向企业类应用开放。

企业类应用包括企业应用和企业MDM应用。

**企业应用：**

* 企业应用定义：

  指企业内部自研应用或者采购的三方应用，由于信息安全、网络保护等原因，无法上架华为应用市场，只能在企业内部通过企业私有应用商店或者本地离线安装等方式进行分发安装。
* 企业应用发布开发指导：

  [申请企业应用发布证书](../app/agc-help-enterprise-cert-0000002248177978.md)、[申请企业应用发布Profile](../app/agc-help-enterprise-profile-0000002248181282.md)
* 企业应用支持格式：

  支持.hap，.app，需要为单个应用包体。

  如果包含多个hap、hsp文件，需[打包为.app格式](packing-tool.md#app打包指令)，且需要在工程级build-profile.json5文件中，将packOptions的[appWithSignedPkg](ide-hvigor-build-profile-app.md#section03812484215)属性配置为true，保证APP里的HAP/HSP包均被签名。
* 企业应用安装方式：

  1. 通过上架企业私有应用商店（企业MDM应用）在企业内部进行统一分发安装。
  2. 在搭载鸿蒙电脑专业版、企业版的PC/2in1设备上，[开启离线应用安装开关](https://developer.huawei.com/business/cn/doc/HEM/hem-kuaisukaitong-hemchangyongdingzhiosnext-0000002524002086#section104506073517)后本地直接安装。
  3. 设备注册纳管到华为HEM平台，在首次开机时通过[HEM平台批量部署](https://developer.huawei.com/business/cn/doc/HEM/hem-kuaisukaitong-hemchangyongdingzhiosnext-0000002524002086#section104506073517)。
  4. 企业应用无法上架华为应用市场进行公开或非公开发布。

**注意** 

1. 企业应用仅支持在搭载了[鸿蒙电脑专业版](https://qingyun.huawei.com/harmonyos-computer/harmonyos-enterprise/)、[企业版的“擎云”系列](https://qingyun.huawei.com/products-and-solutions/)设备上分发安装。
2. HarmonyOS系统以应用包名作为应用的唯一标识，不同的发布证书代表不同的应用版本，需创建不同的应用包名。

* **企业MDM应用：**

  介绍请参考[仅MDM应用可用权限](permissions-for-mdm-apps.md)中的MDM应用介绍。

企业类应用可参考[声明权限](declare-permissions.md)，申请以下权限。

**注意** 

以下权限不支持自动签名，因此在调试和发布阶段，均需参照[手动签名](ide-signing-manual.md)的步骤，完成手动签名。

## ohos.permission.SET\_FILE\_GUARD\_POLICY

允许应用下发文件管控策略。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：10

**变更信息**：API 10-14时，其权限级别为system\_core，仅面向MDM应用开放；从API 14开始，权限级别变更为system\_basic，开放范围变更为企业普通应用。

## ohos.permission.FILE\_GUARD\_MANAGER

允许应用进行公共目录扫描及设置文件扩展属性。

当前扩展属性包括文件密级、文件标签。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：10

**变更信息**：API 10-14时，其权限级别为system\_core，仅面向MDM应用开放；从API 14开始，权限级别变更为system\_basic，开放范围变更为企业普通应用。

## ohos.permission.FILE\_GUARD\_FILE\_WRITE

允许企业应用修改文件。

获取该权限后，应用可以获取用户数据中指定文件的写权限，并修改文件。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：20

## ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS

允许应用跨系统本地账号交互。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：7

**变更信息**：API 7-13该权限仅向系统应用开放；从API 14开始，开放范围从系统应用变更为企业普通应用。

## ohos.permission.GET\_LOCAL\_ACCOUNT\_IDENTIFIERS

允许应用查询指定或所有本地账号的身份标识（如名称、ID）。

获取该权限后，应用可查询系统中指定或所有本地账号的身份标识。基于获取的身份标识，应用可进一步访问或管理目标本地账号。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：General

**起始版本**：26.0.0

## ohos.permission.GET\_RUNNING\_INFO

允许应用获取运行态信息。

可获取其他应用的运行态信息，包括Ability、Extension、Application的信息。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：7

**变更信息**：API 7-13该权限仅向系统应用开放；从API 14开始，开放范围从系统应用变更为企业普通应用。

## ohos.permission.RUNNING\_STATE\_OBSERVER

允许应用监听应用状态。

获取该权限后，可注册应用状态监听器。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：7

**变更信息**：API 7-13该权限仅向系统应用开放；从API 14开始，开放范围从系统应用变更为企业普通应用。

## ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED

允许查询应用的基本信息和其他敏感信息。

如应用包名、版本等信息。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：7

**变更信息**：API 7-13该权限仅向系统应用开放；从API 14开始，开放范围从系统应用变更为企业普通应用。

## ohos.permission.GET\_WIFI\_CONFIG

允许应用获取Wi-Fi的配置信息。

该权限允许应用获取SSID、PSK、加密方式等Wi-Fi配置的相关信息。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：Phone | PC/2in1 | Tablet | TV | Wearable | Car

**起始版本**：8

**变更信息**：API 8-14该权限仅向系统应用开放；从API 15开始，开放范围从系统应用变更为企业普通应用。

## ohos.permission.SET\_WIFI\_CONFIG

允许应用配置Wi-Fi信息。

该权限允许应用添加、删除Wi-Fi，以及修改Wi-Fi的配置信息。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：Phone | PC/2in1 | Tablet | TV | Wearable | Car

**起始版本**：8

**变更信息**：API 8-14该权限仅向系统应用开放；从API 15开始，开放范围变更为企业普通应用。

## ohos.permission.GET\_DOMAIN\_ACCOUNTS

允许应用查询域账号信息。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：10

**变更信息**：API 10-13该权限仅向系统应用开放；从API 14开始，开放范围变更为企业普通应用。

## ohos.permission.QUERY\_AUDIT\_EVENT

允许企业安全类应用查询安全审计事件。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：12

**变更信息**：API 12-13该权限仅面向MDM应用开放；从API 14开始，开放范围从MDM应用变更为企业普通应用。

## ohos.permission.KILL\_APP\_PROCESSES

允许系统应用结束其他应用进程。

获取权限后，可终止其他正在运行中的应用，允许它在必要时对系统中的进程进行管理和控制。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：12

**变更信息**：API 7-13该权限仅向系统应用开放；从API 14开始，开放范围从系统应用变更为企业普通应用。

## ohos.permission.MANAGE\_ENTERPRISE\_WIFI\_CONNECTION

允许应用管理Wi-Fi的连接。

获取该权限后，可执行开启/关闭、连接、断开Wi-Fi等操作。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**是否支持证书授权**：true

**起始版本**：15

## ohos.permission.ACCESS\_ENTERPRISE\_USER\_TRUSTED\_CERT

允许应用管理企业设备的用户CA证书。

在企业设备上企业应用使用私有的CA证书认证企业服务器时，该权限用于允许企业应用把私有CA证书安装到企业设备上，并对安装的CA证书进行管理操作。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：18

## ohos.permission.MANAGE\_NET\_FIREWALL

允许系统应用配置防火墙规则。

当前仅2in1设备应用可申请此权限。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：12

**变更信息**：API 12-14该权限仅向系统应用开放；从API 15开始，开放范围变更为企业普通应用。

## ohos.permission.GET\_NET\_FIREWALL

允许系统应用查询防火墙规则和查询防火墙拦截记录。

当前仅2in1设备应用可申请此权限。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：12

**变更信息**：API 12-14该权限仅向系统应用开放；从API 15开始，开放范围变更为企业普通应用。

## ohos.permission.GET\_DOMAIN\_ACCOUNT\_SERVER\_CONFIGS

允许应用获取域账号服务器配置。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：18

## ohos.permission.MANAGE\_DOMAIN\_ACCOUNT\_SERVER\_CONFIGS

允许应用管理域账号服务器配置。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：18

## ohos.permission.MANAGE\_DOMAIN\_ACCOUNTS

允许应用管理域账号。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：18

## ohos.permission.GET\_SIGNATURE\_INFO

允许应用获取应用包的签名信息。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：18

## ohos.permission.VISIBLE\_WINDOW\_INFO

允许应用获取当前屏幕的可见窗口信息。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：18

## ohos.permission.kernel.AUTH\_AUDIT\_EVENT

允许企业安全应用阻断安全审计事件。

企业安全应用申请此权限后，可以阻断安全审计事件。这些事件包括文件创建、文件打开和文件删除等。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：20

## ohos.permission.SUPPORT\_APP\_SERVICE\_EXTENSION

允许应用作为AppServiceExtension被拉起。

获取此权限后，应用可作为AppServiceExtension被同应用或同在"appidentifierAllowList"配置中的应用拉起或连接。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：20

## ohos.permission.ENTERPRISE\_MANAGE\_EAP

允许企业网络安全软件在EAP报文中新增私有信息。

获取此权限后，允许企业网络安全软件获取802.1x报文并新增信息，完成定制化认证需求。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：20

## ohos.permission.SUPPORT\_INSTALL\_ON\_U1

允许企业普通应用安装在特定用户下。

特定用户是支持应用单例运行的用户。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：20

## ohos.permission.QUERY\_LOCAL\_WORKSPACES

允许企业普通应用查询工作空间和不允许删除的空间列表。

获取此权限后，可查询工作空间的基本信息，以及哪些空间已被设置成不可删除。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：20

## ohos.permission.SET\_NET\_EXT\_ATTRIBUTE

允许应用设置网络扩展属性。

获取该权限后，应用可以通过API为网络设置扩展属性以标识网络是内部网络还是外部网络。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：20

## ohos.permission.MANAGE\_ANTIVIRUS

允许企业应用管理防病毒软件。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：20

## ohos.permission.REGISTER\_ANTIVIRUS

允许企业防病毒软件向系统注册、更新基本信息。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：20

## ohos.permission.CALL\_TPM\_CMD

允许应用调用TPM（Trusted Platform Module）命令。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：20

## ohos.permission.ENTERPRISE\_WORKSPACES\_EVENT\_SUBSCRIBE

允许企业应用订阅企业数字空间相关事件。

获取此权限后，可以通过spaceManager.subscribeEvent和spaceManager.unsubscribeEvent，订阅和取消订阅企业数字空间相关事件。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：20

## ohos.permission.SCAN\_REMEDIATE\_VIRUS

允许应用执行病毒扫描和处置操作。

此权限仅面向杀毒软件开放申请。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：24

## ohos.permission.sec.ACCESS\_UDID

允许应用获取UDID。

UDID（Unified Device ID）是设备的唯一标识。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：7

**变更信息**：API 7-19该权限仅向系统应用开放；从API 20开始，开放范围从系统应用变更为企业普通应用。

## ohos.permission.ENTERPRISE\_MANAGE\_PRINT

允许企业应用调用打印管理接口。

获取该权限后，应用可更新打印状态及打印机信息。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：24

## ohos.permission.DLP\_POLICY\_MANAGER

允许企业普通应用通过数据防泄露能力管理透明加解密策略。

获取该权限后，应用可管理透明加解密策略，如指定其他应用的文件操作需透明加解密、指定对应的加解密算法等。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：26.0.0

## ohos.permission.SUPPORT\_CROSS\_APP\_EMBED\_FOR\_OA

允许应用跨应用拉起EmbeddedUIExtension。

\*\*可申请此权限的特殊场景与功能： \*\*

* 应用为浏览器类应用，且具有NPAPI插件功能。
* 应用为流版签应用，且需要跨应用界面嵌入办公软件中的文档、表格、演示文件。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：26.0.0

## ohos.permission.SUPPORT\_NP\_PLUGIN\_FOR\_WEB

允许应用释放插件库。

\*\*可申请此权限的特殊场景与功能： \*\*

应用为具有浏览器NPAPI插件的应用。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：26.0.0

## ohos.permission.kernel.LOAD\_CERTSIGN\_LIBRARY\_FOR\_WEB

允许应用加载二进制证书签名的插件库。

\*\*可申请此权限的特殊场景与功能： \*\*

应用为具有NPAPI插件功能的浏览器类应用，且需要加载文档类NPAPI插件。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：26.0.0

## ohos.permission.ENTERPRISE\_GET\_INSTALLED\_BUNDLE\_LIST

允许企业普通应用获取已安装全量应用列表。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：26.0.0

## ohos.permission.kernel.TRAFFIC\_FILTER

允许应用在网络流量路径内检查数据包并决定是否放行，以及将网络流量重定向到本地端口。

获取该权限后，应用可以：

1. 以内联方式接入网络流量处理路径，对经过设备或系统的网络数据包进行实时检查、分析和策略判断。应用可以基于数据包的源地址、目标地址、端口、协议类型等，决定是否允许该流量继续传输、阻断连接、丢弃数据包、修改数据包，或执行告警、记录日志等安全处置操作。
2. 将特定网络流量重定向到本地指定端口，由本地安全代理、代理服务、检测引擎或策略执行组件进行进一步处理。例如，可用于恶意流量检测、入侵防护、数据防泄露、访问控制、威胁分析、内容过滤、企业合规审计等场景。

\*\*可申请此权限的特殊场景与功能： \*\*

应用需要为企业安全应用，提供企业数据防泄漏、企业网络管控等能力。

**申请后AGC的审核时长：** 预计3个工作日内反馈审核结果。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：26.0.0
