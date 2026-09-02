---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-sharing
title: "@ohos.net.sharing (网络共享管理)"
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > ArkTS API > @ohos.net.sharing (网络共享管理)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:55+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0808967871eff9095ba0d8f23b61d56e449231351c401cdae9ca503fe0620a0a
---

网络共享管理模块用于将设备网络连接共享给其他连接设备。

**说明** 

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```js
import { sharing } from '@kit.NetworkKit';
```

## NetHandle

type NetHandle = connection.NetHandle

数据网络的句柄。在调用NetHandle的方法之前，需要先获取NetHandle对象。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 类型 | 说明 |
| --- | --- |
| [connection.NetHandle](js-apis-net-connection.md#nethandle) | 网络链路信息。 |
