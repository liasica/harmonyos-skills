---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/serviceability-lifecycle
title: ServiceAbility的生命周期
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > FA模型开发指导 > FA模型应用组件 > ServiceAbility组件开发指导 > ServiceAbility的生命周期
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:59+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:0ad7ea13248cf43d92093f938b8678675794ac007a0c8e66cad299b0b361bdc8
---

开发者可以根据业务场景实现service.js/service.ets中的生命周期相关接口。ServiceAbility生命周期接口说明见下表。

**表1** ServiceAbility生命周期接口说明

| 接口名 | 描述 |
| --- | --- |
| onStart(): void | 该方法在创建ServiceAbility的时候调用，用于Service的初始化，在ServiceAbility的整个生命周期只会调用一次。 |
| onCommand(want: Want, startId: number): void | 在Service创建完成之后调用，该方法在客户端每次启动该Service时都会调用，开发者可以在该方法中做一些调用统计、初始化类的操作。 |
| onConnect(want: Want): rpc.RemoteObject | 在连接ServiceAbility时调用。 |
| onDisconnect(want: Want): void | 在与已连接的ServiceAbility断开连接时调用。 |
| onStop(): void | 在ServiceAbility销毁时调用。开发者应通过实现此方法来清理资源，如关闭线程、注册的侦听器等。 |
