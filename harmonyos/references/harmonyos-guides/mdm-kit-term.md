---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-term
title: MDM Kit术语
breadcrumb: 指南 > 系统 > 基础功能 > MDM Kit（企业设备管理服务） > MDM Kit术语
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:37+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:02182ec37851f2749fb5b85852ed3592e5be1ddb9c2a089aa5c98c3aea3c2612
---

## B

### Bring Your Own Device (BYOD)；自带设备办公

企业允许员工携带自己的平板或智能手机等移动终端设备到公司，并使用这些设备接入公司办公环境。适用于员工日常办公或外来访客携带设备访问工厂、实验室等场景。

### BYOD Device Admin (BDA)；BYOD设备管理员

MDM应用在BYOD场景下激活的Admin角色，可以对设备进行一些如禁用拍照、录音等简单管控。

## C

### Corporate-Owned, Personally-Enabled (COPE)；企业派发设备办公

企业统一购买笔记本电脑、平板电脑、智能手机等设备并分发给员工使用的管理模式。设备所有权归属企业，企业可对这类设备实施全面管控。

## D

### Device Admin (DA)；普通设备管理员

MDM应用激活为DA的Admin角色，可对设备进行管控但无法管理其他DA应用，适用于企业设备办公场景。

## E

### Enterprise Device Manager (EDM)；企业设备管理

企业设备管理框架中的核心底座服务，负责管理Admin组件的生命周期（创建、保活、启停）以及管控接口的权限校验与策略冲突处理。

### EnterpriseAdminExtensionAbility；企业设备管理扩展能力

企业设备管理扩展能力（EnterpriseAdminExtensionAbility）组件是MDM应用必备组件。开发者为企业开发MDM应用时，需继承EnterpriseAdminExtensionAbility，在EnterpriseAdminExtensionAbility实例中实现MDM业务逻辑，EnterpriseAdminExtensionAbility实现了系统管理状态变化通知功能，并定义了管理应用激活、去激活、应用安装、卸载事件等回调接口。当MDM应用的企业设备管理扩展能力被激活后，此企业设备管理扩展能力会被保活，当重启、切换用户后会自动启动。企业设备管理扩展能力激活后的MDM应用无法被卸载。

### Enterprise Mobility Management (EMM)；企业移动管理

为企业提供移动设备管理全套软件、解决方案和服务的业务领域。EMM厂商指专门提供此类产品与服务的公司。

## M

### MDM应用

又称企业MDM应用，指集成了MDM（Mobile Device Management，移动设备管理）管理功能的应用，能够集中管理、监控和保护企业内的移动设备（如智能手机、平板电脑、笔记本电脑等）。它允许IT管理员远程配置设备、强制执行安全策略、部署应用程序，并确保企业数据的安全。

### Mobile Device Management (MDM)；移动设备管理

狭义的MDM指手机、平板这类移动办公类终端设备的管理，广义的MDM泛指企业终端设备管理，包括PC、大屏、穿戴设备。

## S

### Super Device Admin (SDA)；超级设备管理员

MDM应用激活为SDA的Admin角色，可以对设备进行管控以及管理其他的DA应用（包括激活、解除激活DA应用），适用于企业设备办公。
