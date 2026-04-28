---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/permissions-for-mdm-apps
title: 仅MDM应用可用权限
breadcrumb: 指南 > 系统 > 安全 > 程序访问控制 > 应用权限管控 > 应用权限列表 > 仅MDM应用可用权限
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:04+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3ba02cc637b46e645dffdd2b7b12b34dd7b871bf88b8a38b92871695b2303854
---

以下权限仅对MDM（Mobile Device Management）设备管理应用开放。MDM应用的详细介绍，请参考[MDM Kit简介](mdm-kit-intro.md)。

注意

以下权限不支持自动签名，因此在调试和发布阶段，均需参照[手动签名](ide-signing.md#section297715173233)的步骤，完成手动签名。

## ohos.permission.ENTERPRISE\_GET\_DEVICE\_INFO

允许应用激活设备管理应用。

包括读取设备ID、读取设备硬盘序列号，读取OS版本、读取机器名。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：10

## ohos.permission.ENTERPRISE\_GET\_NETWORK\_INFO

允许设备管理应用查询网络信息。

包括查询网卡设置、IP地址、MAC地址，网卡启用状态。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：10

## ohos.permission.ENTERPRISE\_INSTALL\_BUNDLE

允许设备管理应用安装和卸载包。

**权限级别**：system\_core

**授权方式**：系统授权（system\_grant）

**起始版本**：10

## ohos.permission.ENTERPRISE\_MANAGE\_SET\_APP\_RUNNING\_POLICY

允许设备管理应用设置应用运行管理策略。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：10

## ohos.permission.ENTERPRISE\_RESET\_DEVICE

允许设备管理应用恢复设备出厂设置。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：10

## ohos.permission.ENTERPRISE\_SET\_ACCOUNT\_POLICY

允许设备管理应用设置账户管理策略。

比如新增账号。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：10

## ohos.permission.ENTERPRISE\_SET\_BUNDLE\_INSTALL\_POLICY

允许设备管理应用设置包安装管理策略。

比如设置包安装白名单。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：10

## ohos.permission.ENTERPRISE\_SET\_DATETIME

允许设备管理应用设置系统时间。

包括设置系统时间值，禁止用户修改系统时间策略。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：9

## ohos.permission.ENTERPRISE\_SET\_NETWORK

允许设备管理应用设置网络信息。

包括禁用、开启网卡。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：10

## ohos.permission.ENTERPRISE\_SET\_WIFI

允许设备管理应用设置和查询WiFi信息。

可设置和查询WiFi禁用，设置WiFi连接。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：10

## ohos.permission.ENTERPRISE\_SUBSCRIBE\_MANAGED\_EVENT

允许设备管理应用订阅管理事件。

比如应用安装事件、应用卸载事件和系统更新事件等。订阅成功后，事件触发时会通知MDM应用。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：9

## ohos.permission.ENTERPRISE\_RESTRICT\_POLICY

允许设备管理员下发和获取限制类策略。

比如禁用HDC，禁用直连打印服务等。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：10

## ohos.permission.ENTERPRISE\_SET\_SCREENOFF\_TIME

允许设备管理员设置系统休眠时间。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：10

## ohos.permission.ENTERPRISE\_MANAGE\_USB

允许设备管理员管理USB。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：10

## ohos.permission.ENTERPRISE\_MANAGE\_NETWORK

允许设备管理员管理网络。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：10

## ohos.permission.ENTERPRISE\_MANAGE\_CERTIFICATE

允许设备管理员管理证书。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：10

## ohos.permission.ENTERPRISE\_GET\_SETTINGS

允许设备管理员查询“设置”应用数据。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：10

## ohos.permission.ENTERPRISE\_SET\_BROWSER\_POLICY

允许设备设置/取消浏览器策略。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：10

## ohos.permission.SET\_ENTERPRISE\_INFO

允许设备管理应用设置企业信息。

企业设备管理器激活后可设置企业组织信息，包括企业名称和描述信息，用于system UI展示设备被所属管理信息。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：9

## ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

允许设备设置安全管理策略。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：11

## ohos.permission.ENTERPRISE\_MANAGE\_BLUETOOTH

允许设备管理应用设置和查询蓝牙信息。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：11

## ohos.permission.ENTERPRISE\_MANAGE\_SYSTEM

允许设备管理系统设置参数策略。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：11

## ohos.permission.ENTERPRISE\_MANAGE\_WIFI

允许设备管理应用设置和查询WIFI信息。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：11

## ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS

允许设备管理应用管理限制策略。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：11

## ohos.permission.ENTERPRISE\_MANAGE\_APPLICATION

允许设备管理应用管理应用策略。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：11

## ohos.permission.ENTERPRISE\_MANAGE\_LOCATION

允许设备管理应用设置和查询位置信息。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：11

## ohos.permission.ENTERPRISE\_REBOOT

允许设备管理应用进行关机重启操作。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：11

## ohos.permission.ENTERPRISE\_LOCK\_DEVICE

允许设备管理应用锁定设备。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：11

## ohos.permission.ENTERPRISE\_MANAGE\_SETTINGS

允许设备管理应用管理设置。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：11

## ohos.permission.ENTERPRISE\_OPERATE\_DEVICE

允许设备管理应用操作设备。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：12

## ohos.permission.ENTERPRISE\_ADMIN\_MANAGE

允许应用管理设备管理应用。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：12

## ohos.permission.ENTERPRISE\_RECOVERY\_KEY

允许应用管理企业级恢复密钥。

**权限级别**：system\_core

**授权方式**：系统授权（system\_grant）

**起始版本**：13

## ohos.permission.ENTERPRISE\_MANAGE\_DELEGATED\_POLICY

允许设备管理应用委托其他应用设置设备管控策略。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：14

## ohos.permission.ENTERPRISE\_GET\_ALL\_BUNDLE\_INFO

允许设备管理应用获取设备所有应用信息。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：Phone | PC/2in1 | Tablet

**起始版本**：20

## ohos.permission.ENTERPRISE\_SET\_USER\_RESTRICTION

允许设备管理应用限制用户修改系统设置。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：Phone | PC/2in1 | Tablet

**起始版本**：20

## ohos.permission.ENTERPRISE\_MANAGE\_APN

允许设备管理应用管理设备APN策略。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：Phone | PC/2in1 | Tablet

**起始版本**：20

## ohos.permission.ENTERPRISE\_MANAGE\_TELEPHONY

允许设备管理应用管理设备通话策略。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：Phone | PC/2in1 | Tablet

**起始版本**：20

## ohos.permission.ENTERPRISE\_SET\_KIOSK

允许设备管理应用设置Kiosk模式。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：Phone | PC/2in1 | Tablet

**起始版本**：20

## ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES

允许企业应用启用、创建、删除工作空间。

获取此权限后，应用可以设置空间切换免密登录时间、用户照片、不允许删除的空间列表等。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：20

## ohos.permission.ENTERPRISE\_FILE\_TRANSFER\_AUDIT\_POLICY\_MANAGEMENT

允许MDM应用管理文件传输的策略和审计信息。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：20

## ohos.permission.ENTERPRISE\_SET\_WALLPAPER

允许设备管理应用设置壁纸。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：Phone | PC/2in1 | Tablet

**起始版本**：20

## ohos.permission.MANAGE\_PREINSTALLED\_ANTIVIRUS

允许MDM应用管理系统预装的防病毒软件。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：20

## ohos.permission.ENTERPRISE\_MANAGE\_USER\_GRANT\_PERMISSION

允许设备管理应用（MDM）设置user\_grant类权限策略。

获取该权限后，MDM应用可设置被管理应用user\_grant类权限策略，策略支持静默授予，拒绝授予以及默认（即不影响应用申请）。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：Phone | PC/2in1 | Tablet

**起始版本**：20

## ohos.permission.ENTERPRISE\_DATA\_IDENTIFY\_FILE

允许MDM应用识别文件敏感内容。

**权限级别**：system\_core

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：21

## ohos.permission.ENTERPRISE\_ACCESS\_DLP\_FILE

允许设备管理应用（MDM）生成、解密DLP文件，查询DLP文件策略。

**权限级别**：system\_core

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：20

**变更信息**：在API20，该权限面向系统应用开放；从API 21开始，面向MDM应用开放。

## ohos.permission.ENTERPRISE\_MANAGE\_DEVICE\_ADMIN

允许应用管理其他设备管理应用。

获取该权限后，超级设备管理应用可管理其他设备管理应用。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：Phone | PC/2in1 | Tablet

**起始版本**：23

## ohos.permission.ENTERPRISE\_START\_ABILITIES

允许设备管理应用访问其他组件。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：Phone | PC/2in1 | Tablet

**起始版本**：23

## ohos.permission.ENTERPRISE\_READ\_LOG

允许MDM应用收集系统日志。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：Phone | PC/2in1 | Tablet

**起始版本**：23

## ohos.permission.ENTERPRISE\_DEACTIVATE\_DEVICE\_ADMIN

允许已激活的MDM应用解除自身的激活状态。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：Phone | PC/2in1 | Tablet

**起始版本**：23
