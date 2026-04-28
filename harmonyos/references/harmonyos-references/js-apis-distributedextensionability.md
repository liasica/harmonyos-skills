---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributedextensionability
title: @ohos.application.DistributedExtensionAbility (协同Extension)
breadcrumb: API参考 > 系统 > 网络 > Distributed Service Kit（分布式管理服务） > ArkTS API > @ohos.application.DistributedExtensionAbility (协同Extension)
category: harmonyos-references
scraped_at: 2026-04-28T08:08:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4ac4e1fc60fc520bfda94cb8b7bb47c5deff994fea6f5ba69920ca85e8e23509
---

DistributedExtensionAbility模块提供分布式相关扩展能力，提供分布式创建、销毁、连接的生命周期回调。

说明

本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { DistributedExtensionAbility} from '@kit.DistributedServiceKit';
```

## DistributedExtensionAbility

PhonePC/2in1TabletTVWearable

### 属性

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | DistributedExtensionContext | 否 | 否 | DistributedExtension的上下文环境，继承自ExtensionContext。 |

### onCreate

PhonePC/2in1TabletTVWearable

onCreate(want: Want): void

Extension生命周期回调，在创建时回调，执行初始化业务逻辑操作。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 当前Extension相关的Want类型信息，包括ability名称、bundle名称等。 |

**示例：**

```
1. import { Want } from '@kit.AbilityKit';
2. import { DistributedExtensionAbility } from '@kit.DistributedServiceKit';

4. export default class DistributedExtension extends DistributedExtensionAbility {
5. onCreate(want: Want) {
6. console.info(`DistributedExtension Create ok`);
7. console.info(`DistributedExtension on Create want: ${JSON.stringify(want)}`);
8. console.info(`DistributedExtension Create end`);
9. }
10. }
```

### onCollaborate

PhonePC/2in1TabletTVWearable

onCollaborate(wantParam: Record <string, Object>) : AbilityConstant.CollaborateResult

多设备协作场景下返回协作结果的回调。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wantParam | Record <string, Object> | 是 | want相关参数，仅支持key值取"ohos.extra.param.key.supportCollaborateIndex"。通过该key值可以获取到调用方传输的数据并进行相应的处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AbilityConstant.CollaborateResult](js-apis-app-ability-abilityconstant.md#collaborateresult18) | 协同方应用是否接受协同。 |

**示例**

```
1. import { abilityConnectionManager, DistributedExtensionAbility } from '@kit.DistributedServiceKit';
2. import { AbilityConstant } from '@kit.AbilityKit';

4. export default class DistributedExtension extends DistributedExtensionAbility {
5. onCollaborate(wantParam: Record<string, Object>) {
6. console.info(`DistributedExtension onCollabRequest Accept to the result of Ability collaborate`);
7. let sessionId = -1;
8. const collaborationValues = wantParam["CollaborationValues"] as abilityConnectionManager.CollaborationValues;
9. if (collaborationValues == undefined) {
10. return sessionId;
11. }
12. console.info(`onCollab, collaborationValues: ${JSON.stringify(collaborationValues)}`);
13. return AbilityConstant.CollaborateResult.ACCEPT;
14. }
15. }
```

### onDestroy

PhonePC/2in1TabletTVWearable

onDestroy(): void

Extension生命周期回调，在销毁时回调，执行资源清理等操作。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**示例：**

```
1. import { DistributedExtensionAbility } from '@kit.DistributedServiceKit';

3. export default class DistributedExtension extends DistributedExtensionAbility {
4. onDestroy() {
5. console.info('DistributedExtension onDestroy ok');
6. }
7. }
```
