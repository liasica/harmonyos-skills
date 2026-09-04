---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/modular-object-extension-overview
title: 模块化对象模型概述 (C/C++)
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > 基于ModularObjectExtensionAbility的模块化对象开发指导 (C/C++) > 模块化对象模型概述 (C/C++)
category: harmonyos-guides
scraped_at: 2026-09-05T06:13:48+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5c8707c5a3f69fe5a2464fc744f5eb624ec657dbd6c279d13ef47ab1779a4bac
---

模块化对象是一种跨应用的能力开放方式。应用通过ModularObjectExtensionAbility（相关C API定义见[modular\_object\_extension\_ability.h](../harmonyos-references/capi-modular-object-extension-ability-h.md)）组件将特定功能封装为独立的功能模块并对外暴露Proxy对象，其他应用获取Proxy对象后，即可跨进程调用这些能力。例如，文档编辑类应用可以提供文档处理能力，其他应用可调用该能力实现文档协同编辑；邮件类应用可以提供邮件发送能力，其他应用可调用该能力实现邮件群发等。

在基于ModularObjectExtensionAbility的开发中，可借助[Taihe](ability-terminology.md#taihe)工具根据接口定义自动生成Proxy/Stub代码及类型库元数据，屏蔽IPC底层细节；客户端也可通过ModularObjectDispatcher在运行时动态查询并调用远端接口。

## 基本概念

* 服务端：提供ModularObjectExtensionAbility组件的应用称为服务端。
* 客户端：连接并调用ModularObjectExtensionAbility组件的应用称为客户端。
* Stub对象：服务端创建的对象，用于接收并处理客户端发送的IPC请求，以及业务能力实现。
* Proxy对象：客户端持有的对象，用于向服务端发送IPC请求。客户端通过连接ModularObjectExtensionAbility组件获取该对象。

## 运行机制

1. 客户端连接服务端：客户端通过Connect接口发起连接请求，指定目标ModularObjectExtensionAbility的bundleName、moduleName和abilityName。每次连接服务端都会创建新的ModularObjectExtensionAbility实例。
2. 服务端返回Proxy对象：连接成功后，系统会加载服务端对应Ability的so库，并调用OnNativeExtensionCreate入口函数。然后系统会依次触发服务端的OnCreateFunc和OnConnectFunc回调，开发者在OnConnectFunc回调中返回Stub对象。系统将Stub转换为Proxy对象返回给客户端。
3. 客户端通过Proxy与服务端通信：客户端在OnConnectCallback回调中收到服务端返回的Proxy对象后，通过该对象与服务端通信。当不再需要通信时，客户端可以通过Disconnect断开连接。连接断开后，系统会依次触发服务端的OnDisconnectFunc回调和OnDestroyFunc回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/Tp9oUSOVQ-O4RSdb7zsA7Q/zh-cn_image_0000002712403258.png)

上述步骤中涉及的简写与完整接口名称的对应关系如下表所示：

| 简写 | 完整接口名称 |
| --- | --- |
| Connect | [OH\_AbilityRuntime\_ConnectModularObjectExtensionAbility](../harmonyos-references/capi-modular-object-extension-manager-h.md#oh_abilityruntime_connectmodularobjectextensionability) |
| Disconnect | [OH\_AbilityRuntime\_DisconnectModularObjectExtensionAbility](../harmonyos-references/capi-modular-object-extension-manager-h.md#oh_abilityruntime_disconnectmodularobjectextensionability) |
| OnNativeExtensionCreate | [OH\_AbilityRuntime\_OnNativeExtensionCreate](../harmonyos-references/capi-extension-ability-h.md#oh_abilityruntime_onnativeextensioncreate) |
| OnCreateFunc | [OH\_AbilityRuntime\_ModObjExtensionAbility\_OnCreateFunc](../harmonyos-references/capi-modular-object-extension-ability-h.md#oh_abilityruntime_modobjextensionability_oncreatefunc) |
| OnConnectFunc | [OH\_AbilityRuntime\_ModObjExtensionAbility\_OnConnectFunc](../harmonyos-references/capi-modular-object-extension-ability-h.md#oh_abilityruntime_modobjextensionability_onconnectfunc) |
| OnDisconnectFunc | [OH\_AbilityRuntime\_ModObjExtensionAbility\_OnDisconnectFunc](../harmonyos-references/capi-modular-object-extension-ability-h.md#oh_abilityruntime_modobjextensionability_ondisconnectfunc) |
| OnDestroyFunc | [OH\_AbilityRuntime\_ModObjExtensionAbility\_OnDestroyFunc](../harmonyos-references/capi-modular-object-extension-ability-h.md#oh_abilityruntime_modobjextensionability_ondestroyfunc) |
| OnConnectCallback | [OH\_AbilityRuntime\_ConnectOptions\_OnConnectCallback](../harmonyos-references/capi-connect-options-h.md#oh_abilityruntime_connectoptions_onconnectcallback) |
| Proxy | [OHIPCRemoteProxy](../harmonyos-references/capi-ohipcparcel-ohipcremoteproxy.md) |
| Stub | [OHIPCRemoteStub](../harmonyos-references/capi-ohipcparcel-ohipcremotestub.md) |
