---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/enterprisespace-spacemanager
title: "@hms.enterpriseSpaceService.spaceManager(空间管理)"
breadcrumb: API参考 > 应用服务 > Enterprise Space Kit（企业数字空间服务） > ArkTS API > @hms.enterpriseSpaceService.spaceManager(空间管理)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:62b9853a40be7fb5ad65d4bd3948e278d14f2e2f7112adcc6069bf2f17729d31
---

空间管理服务提供统一的空间管理能力，包括创建工作空间、移除工作空间、订阅空间事件等功能，满足用户空间使用和企业对空间的管理诉求。

**起始版本：** 6.0.0(20)

## 导入模块

```typescript
import { spaceManager } from '@kit.EnterpriseSpaceKit';
```

## spaceManager

空间管理服务的实例，提供统一的空间管理能力。

**起始版本：** 6.0.0(20)

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

### CreateWorkspaceParams

创建工作空间参数。

**起始版本：** 6.0.0(20)

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| shortName | string | 否 | 否 | 工作空间的本地简称，默认值与[WorkspaceInfo](enterprisespace-spacemanager.md#workspaceinfo)下的localName一致。 |

### WorkspaceDomainInfo

工作空间域账号信息。

**起始版本：** 6.0.0(20)

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| domain | string | 否 | 否 | 域名，仅在工作空间认证后有值，例如“xx.com”，否则其值为空。 |
| workspaceName | string | 否 | 否 | 工作空间域账号名称，仅在工作空间认证后有值，否则其值为空。 |
| accountId | string | 否 | 是 | 域账号标识符，仅在工作空间认证后有值，否则其值为空。其创建空间时，由系统自动生成的字符串，在[setWorkspaceInfo](enterprisespace-spacemanager.md#setworkspaceinfo)中可设置为空。 |
| isAuthenticated | boolean | 否 | 是 | 工作空间是否已鉴权。  - true：已鉴权  - false：未鉴权  默认值为false。 |
| serverConfigId | string | 否 | 是 | 工作空间所属域的服务器配置标识符。由创建空间时系统自动生成的，仅在工作空间认证后有值，例如“xx:test.com”，否则其值为空。 |
| enterpriseWorkspaceName | string | 否 | 是 | 工作空间名称，企业设备在某个空间下的标签属性，默认值为空。例如，该名称在企业空间为“XXX”。  **起始版本**：6.0.2(22) |

### WorkspaceInfo

工作空间信息。

**起始版本：** 6.0.0(20)

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| workspaceId | number | 否 | 否 | 工作空间ID。首个空间ID为100，后续创建的工作空间ID逐一递增，例如101、102。 |
| localName | string | 否 | 否 | 工作空间的本地账号名称，例如，“test”。 |
| shortName | string | 否 | 是 | 工作空间的本地简称，默认值与localName一致。 |
| isUnlocked | boolean | 否 | 否 | 工作空间是否处于解锁状态。  - true：解锁状态  - false：锁屏状态  默认值为false。 |
| photo | string | 否 | 否 | 工作空间的资料照片，是由本地照片的Base64格式拼接成的JSON字符串。“type”为照片类型，当前仅支持值为0；“defaultImg”为由照片转为Base64格式的字符串。例如，拼接后字符串为“{"type":0,"defaultImg":"data:image/png;base64,iVBO\*\*\*\*\*\*Jggg==}”。 |
| createTime | number | 否 | 否 | 工作空间的创建时间，系统生成的10位数字组成的时间戳，单位：s。 |
| lastLoginTime | number | 否 | 否 | 工作空间的最后登录时间，通常为系统生成的10位数字组成的时间戳，单位：s。 |
| serialNumber | number | 否 | 否 | 通常为由9位数字组成的工作空间序列号。 |
| isActivated | boolean | 否 | 否 | 工作空间是否处于激活状态。  - true：激活状态  - false：未激活状态  默认值为false。 |
| isCreateCompleted | boolean | 否 | 否 | 工作空间创建是否完成。  - true：创建工作空间已完成状态  - false：创建工作空间未完成状态  默认值为true。 |
| isAllowedToBeDeleted | boolean | 否 | 否 | 工作空间是否允许被删除。  - true：允许被删除  - false：不允许被删除  默认值为true。 |
| domainInfo | [WorkspaceDomainInfo](enterprisespace-spacemanager.md#workspacedomaininfo) | 否 | 否 | 工作空间域信息，具体可参见[WorkspaceDomainInfo](enterprisespace-spacemanager.md#workspacedomaininfo)。 |

### ProcessConfigInfo

进程无法访问的路径信息。

**起始版本：** 6.0.1(21)

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| processName | string | 否 | 否 | 系统服务进程的名称。 |
| disallowPaths | string[] | 否 | 否 | 不可访问的路径列表，列表只能包含如下列表的子集：['/data/service','/data/app','/storage','/mnt'] |

### WorkspaceType

工作空间类型的枚举。

**起始版本：** 6.0.0(20)

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ADMIN | 0 | 管理员工作空间，具有管理其他工作空间的权限。 |

### QueryType

工作空间查询类型的枚举。

**起始版本：** 6.0.0(20)

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ALL | 0 | 查询所有的工作空间。 |
| NON\_DELETABLE | 1 | 查询不允许被删除的工作空间。 |

### EventType

订阅事件类型的枚举。

**起始版本：** 6.0.0(20)

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EVENT\_WORKSPACE\_SWITCHED | 0 | 工作空间切换事件。 |

### UserDataEnum

工作空间类型的枚举。

**起始版本：** 6.0.1(21)

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ENTERPRISE | 0 | 表示企业空间。 |
| PERSONAL | 1 | 表示个人空间。 |

### EventData

工作空间事件信息。

**起始版本：** 6.0.0(20)

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| event | [EventType](enterprisespace-spacemanager.md#eventtype) | 否 | 否 | 事件类型，取值可参见[EventType](enterprisespace-spacemanager.md#eventtype)。 |
| currentWorkspaceId | number | 否 | 是 | 当前工作空间ID，例如101、102。 |

### LockdownModePolicy

锁定模式策略类型的枚举，包括后台应用冻结和公共目录加解密等安全加固功能，提供开关，关闭或者效率模式。

**起始版本：** 6.0.2(22)

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OFF | 0 | 关闭。关闭后不支持后台应用冻结和公共数据目录加解密。 |
| EFFICIENT | 1 | 效率模式。支持后台应用冻结和公共数据目录加解密。 |

### SpaceGuidePolicy

个人空间创建引导页展示策略的枚举。

**起始版本：** 6.1.0(23)

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SHOW | 0 | 展示个人空间创建页引导页。 |
| HIDE | 1 | 隐藏个人空间创建页引导页。 |

### AuthResult

企业认证结果。

**起始版本：** 6.1.0(23)

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| result | number | 否 | 否 | 认证结果，0代表成功，其他代表失败。 |
| workspaceId | number | 否 | 否 | 当前调用方的工作空间ID。 |

### StatusBarIcon

状态栏中的工作空间图标。

**起始版本：** 6.1.0(23)

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| white | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | 否 | 深色背景下图标，样式设计[参考设计规范](../design-guides/statusbar-0000002319710910.md#section13803824112416)。 |
| black | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | 否 | 浅色背景下图标，样式设计[参考设计规范](../design-guides/statusbar-0000002319710910.md#section13803824112416)。 |

### NotificationVisibilitySwitch

跨空间通知内容可见性的状态枚举。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NOTIFICATION\_HIDDEN | 0 | 隐藏跨空间消息提醒。 |
| NOTIFICATION\_VISIBLE | 1 | 展示跨空间消息提醒。 |

### NotificationSwitch

跨空间通知的开关状态枚举。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ON | 0 | 开启跨空间消息提醒。 |
| OFF | 1 | 关闭跨空间消息提醒。 |

### NotificationVisibilityControl

跨空间通知内容可见性的控制类型枚举。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ALLOW\_CHANGE | 0 | 允许修改跨空间消息提醒可见性开关状态。 |
| DISALLOW\_CHANGE | 1 | 不允许修改跨空间消息提醒可见性开关状态。 |

### NotificationConfig

应用跨空间通知的配置信息。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| workspaceId | number | 否 | 否 | 工作空间ID。首个空间ID为100，后续创建的工作空间ID逐一递增，例如101、102。取值应为[100,10736]内的整数。 |
| appIdentifier | string | 否 | 否 | 应用的唯一标识。详情信息可参考[什么是appIdentifier](../harmonyos-guides/common-problem-of-application.md#什么是appidentifier)。 |
| notificationState | [NotificationSwitch](enterprisespace-spacemanager.md#notificationswitch) | 否 | 否 | 跨空间消息提醒开关状态，取值可参见[NotificationSwitch](enterprisespace-spacemanager.md#notificationswitch)。 |
| visibilityState | [NotificationVisibilitySwitch](enterprisespace-spacemanager.md#notificationvisibilityswitch) | 否 | 是 | 跨空间消息提醒可见性开关状态，取值可参见[NotificationVisibilitySwitch](enterprisespace-spacemanager.md#notificationvisibilityswitch)。默认值为NOTIFICATION\_HIDDEN。 |
| allowVisibilityChange | [NotificationVisibilityControl](enterprisespace-spacemanager.md#notificationvisibilitycontrol) | 否 | 是 | 跨空间消息提醒可见性控制开关状态，取值可参见[NotificationVisibilityControl](enterprisespace-spacemanager.md#notificationvisibilitycontrol)。默认值为ALLOW\_CHANGE。 |

### createWorkspace

createWorkspace(localName: string, workspaceType: WorkspaceType, params?: CreateWorkspaceParams): Promise<WorkspaceInfo>

创建工作空间。使用Promise异步回调。

**说明** 

从6.1.0(23)开始，在创建工作空间时，增加如下校验：

* 最多可创建2个工作空间。
* 企业管理员设置禁止添加账号或者关闭全盘解密后，无法创建工作空间。

**起始版本：** 6.0.0(20)

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES或ohos.permission.MANAGE\_LOCAL\_WORKSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localName | string | 是 | 工作空间的本地账号名称，例如，“testWorkspace”。 |
| workspaceType | [WorkspaceType](enterprisespace-spacemanager.md#workspacetype) | 是 | 工作空间的类型。 |
| params | [CreateWorkspaceParams](enterprisespace-spacemanager.md#createworkspaceparams) | 否 | 创建工作空间配置，具体可参见[CreateWorkspaceParams](enterprisespace-spacemanager.md#createworkspaceparams)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[WorkspaceInfo](enterprisespace-spacemanager.md#workspaceinfo)> | Promise对象，返回工作空间信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-space.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 801 | The device type not supported.  适用版本：26.0.0+ |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. |
| 1020400003 | Invalid workspace. |
| 1020400007 | Enterprise workspace not enabled. |
| 1020400011 | Account creation is not permitted.  适用版本：6.1.0(23)+ |
| 1020400012 | Full disk encryption is not enabled.  适用版本：6.1.0(23)+ |

**示例：**

```typescript
import { spaceManager } from '@kit.EnterpriseSpaceKit';

const localName: string = 'testWorkspace';
const workspaceType: spaceManager.WorkspaceType = spaceManager.WorkspaceType.ADMIN;
const params: spaceManager.CreateWorkspaceParams = {
  shortName: 'test'
};
const workspaceInfo: spaceManager.WorkspaceInfo = await spaceManager.createWorkspace(localName, workspaceType, params);
console.info(`Succeeded in creating workspace. workspaceInfo: ${JSON.stringify(workspaceInfo)}`);
```

### enableWorkspace

enableWorkspace(enable: boolean): Promise<void>

使能双空间特性。双空间分别为企业空间和个人空间，企业空间为完全受企业管控的通用办公空间，个人空间为因工作需要对外交流、作业、开源开发等用途的空间。使用Promise异步回调。

**说明** 

从6.1.0(23)开始，使能双空间特性时，增加以下校验：

* 当前工作空间个数不超过2个。
* 企业管理员设置关闭全盘解密后，无法使能双空间特性。

**起始版本：** 6.0.0(20)

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES或ohos.permission.MANAGE\_LOCAL\_WORKSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 双空间特性是否启用。参数的默认值为false。  - true：支持双空间特性  - false：不支持双空间特性 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-space.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 801 | The device type not supported.  适用版本：26.0.0+ |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. |
| 1020400003 | Invalid workspace.  适用版本：6.1.0(23)+ |
| 1020400012 | Full disk encryption is not enabled.  适用版本：6.1.0(23)+ |

**示例：**

```typescript
import { spaceManager } from '@kit.EnterpriseSpaceKit';

const enable: boolean = true;
await spaceManager.enableWorkspace(enable);
console.info(`Succeeded in enabling workspace.`);
```

### queryWorkspace

queryWorkspace(queryFlag: QueryType): Promise<WorkspaceInfo[]>

查询工作空间。使用Promise异步回调。

**起始版本：** 6.0.0(20)

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.QUERY\_LOCAL\_WORKSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| queryFlag | [QueryType](enterprisespace-spacemanager.md#querytype) | 是 | 工作空间类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[WorkspaceInfo](enterprisespace-spacemanager.md#workspaceinfo)[]> | Promise对象，返回工作空间信息列表。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-space.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 801 | The device type not supported.  适用版本：26.0.0+ |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. |

**示例：**

```typescript
import { spaceManager } from '@kit.EnterpriseSpaceKit';

const queryFlag: spaceManager.QueryType = spaceManager.QueryType.ALL;
const spaces: spaceManager.WorkspaceInfo[] = await spaceManager.queryWorkspace(queryFlag);
console.info(`Succeeded in querying workspace. spaces: ${JSON.stringify(spaces)}`);
```

### removeWorkspace

removeWorkspace(workspaceId: number): Promise<void>

移除工作空间。使用Promise异步回调。

**说明** 

工作空间ID为100的首空间不支持移除，其余空间可正常移除。

**起始版本：** 6.0.0(20)

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES或ohos.permission.MANAGE\_LOCAL\_WORKSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| workspaceId | number | 是 | 工作空间ID。首个空间ID为100，后续创建的工作空间ID逐一递增，例如101、102。取值应为[100,10736]内的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-space.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 801 | The device type not supported.  适用版本：26.0.0+ |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. |
| 1020400003 | Invalid workspace. |
| 1020400007 | Enterprise workspace not enabled. |

**示例：**

```typescript
import { spaceManager } from '@kit.EnterpriseSpaceKit';

const workspaceId: number = 101; // 已经创建的工作空间ID。
await spaceManager.removeWorkspace(workspaceId);
console.info(`Succeeded in removing workspace.`);
```

### setWorkspaceInfo

setWorkspaceInfo(workspaceId: number, domainInfo: WorkspaceDomainInfo): Promise<void>

设置工作空间域信息。使用Promise异步回调。

**起始版本：** 6.0.0(20)

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES或ohos.permission.MANAGE\_LOCAL\_WORKSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| workspaceId | number | 是 | 工作空间ID。首个空间ID为100，后续创建的工作空间ID逐一递增，例如101、102。取值应为[100,10736]内的整数。 |
| domainInfo | [WorkspaceDomainInfo](enterprisespace-spacemanager.md#workspacedomaininfo) | 是 | 工作空间域信息，具体可参见[WorkspaceDomainInfo](enterprisespace-spacemanager.md#workspacedomaininfo)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-space.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 801 | The device type not supported.  适用版本：26.0.0+ |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. |
| 1020400003 | Invalid workspace. |
| 1020400007 | Enterprise workspace not enabled. |

**示例：**

```typescript
import { spaceManager } from '@kit.EnterpriseSpaceKit';

const workspaceId: number = 100;
const domainInfo: spaceManager.WorkspaceDomainInfo = {
  domain: 'test1',
  workspaceName: 'test2',
  accountId: 'test3',
  isAuthenticated: false,
  serverConfigId: 'test4',
  enterpriseWorkspaceName: 'default'
};

await spaceManager.setWorkspaceInfo(workspaceId, domainInfo);
console.info(`Succeeded in setting workspace info.`);
```

### setWorkspaceProfilePhoto

setWorkspaceProfilePhoto(workspaceId: number, photo: string): Promise<void>

设置工作空间资料照片。使用Promise异步回调。

**起始版本：** 6.0.0(20)

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| workspaceId | number | 是 | 工作空间ID。首个空间ID为100，后续创建的工作空间ID逐一递增，例如101、102。取值应为[100,10736]内的整数。 |
| photo | string | 是 | 设置的工作空间的资料照片，是由本地照片的Base64格式拼接成的JSON字符串。“type”为照片类型，当前仅支持值为0；“defaultImg”为由照片转为Base64格式的字符串。例如，拼接后字符串为“{"type":0,"defaultImg":"data:image/png;base64,iVBO\*\*\*\*\*\*Jggg==}”。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-space.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 801 | The device type not supported.  适用版本：26.0.0+ |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. |
| 1020400003 | Invalid workspace. |
| 1020400007 | Enterprise workspace not enabled. |

**示例：**

```typescript
import { spaceManager } from '@kit.EnterpriseSpaceKit';

const workspaceId: number = 100;
const photo: string = '{"type":0,"defaultImg":"data:image/png;base64,iVBO******Jggg==}';
try {
  await spaceManager.setWorkspaceProfilePhoto(workspaceId, photo);
  console.info(`Succeeded in setting workspace profile photo.`);
} catch (err) {
  console.error(`Failed to set workspace profile photo. Code: ${err.code}, message: ${err.message}`);
}
```

### subscribeEvent

subscribeEvent(eventId: EventType[], callback: AsyncCallback<EventData>): number

订阅空间事件。使用callback异步回调。

**起始版本：** 6.0.0(20)

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_WORKSPACES\_EVENT\_SUBSCRIBE

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | [EventType](enterprisespace-spacemanager.md#eventtype)[] | 是 | 订阅的空间事件类型列表。 |
| callback | AsyncCallback<[EventData](enterprisespace-spacemanager.md#eventdata)> | 是 | 回调函数，当订阅空间事件成功，err为undefined，data为获取到的工作空间事件信息[EventData](enterprisespace-spacemanager.md#eventdata)；否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 订阅ID，用于在取消空间事件中使用。首个返回的订阅ID为1，后续返回的订阅ID逐一递增，例如2、3。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-space.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 801 | The device type not supported.  适用版本：26.0.0+ |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. |
| 1020400006 | Session disconnected. |
| 1020400007 | Enterprise workspace not enabled. |

**示例：**

```typescript
import { spaceManager } from '@kit.EnterpriseSpaceKit';
import { BusinessError } from '@kit.BasicServicesKit';

const subscribeId = spaceManager.subscribeEvent([spaceManager.EventType.EVENT_WORKSPACE_SWITCHED],
  (error: BusinessError, data: spaceManager.EventData) => {
    if (error) {
      console.error(`error info:${error?.code}, err message:${error?.message}`);
    } else {
      console.info(`event: ${data.event}, currentWorkSpaceId: ${data.currentWorkspaceId}`);
    }
  });
console.info(`Succeeded in subscribing event. subscribeId: ${subscribeId}`);
```

### unsubscribeEvent

unsubscribeEvent(subscribeId: number): void

取消订阅空间事件。

**起始版本：** 6.0.0(20)

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_WORKSPACES\_EVENT\_SUBSCRIBE

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| subscribeId | number | 是 | 由订阅空间事件得到的订阅ID，用于取消订阅对应的空间事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-space.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 801 | The device type not supported.  适用版本：26.0.0+ |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. |
| 1020400007 | Enterprise workspace not enabled. |

**示例：**

```typescript
import { spaceManager } from '@kit.EnterpriseSpaceKit';

const subscribeId: number = 10; // 由订阅空间事件得到的订阅ID。
spaceManager.unsubscribeEvent(subscribeId);
console.info(`Succeeded in unsubscribing event.`);
```

### setRestrictedAccessBackgroundUserdata

setRestrictedAccessBackgroundUserdata(userData: UserDataEnum, enable: boolean): Promise<void>

设置系统服务进程不可访问后台用户数据的功能。使用Promise异步回调。

**起始版本：** 6.0.1(21)

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userData | [UserDataEnum](enterprisespace-spacemanager.md#userdataenum) | 是 | 表示工作空间类型。 |
| enable | boolean | 是 | 表示是否开启管控。默认值为true。  - true：表示开启管控，此时系统服务进程不可访问后台用户的数据  - false：表示关闭管控，此时系统服务进程可正常访问后台用户的数据 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-space.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 801 | The device type not supported.  适用版本：26.0.0+ |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. |
| 1020400007 | Enterprise workspace not enabled. |

**示例：**

```typescript
import { spaceManager } from '@kit.EnterpriseSpaceKit';

const userData: spaceManager.UserDataEnum = spaceManager.UserDataEnum.ENTERPRISE;
const enable: boolean = false;
await spaceManager.setRestrictedAccessBackgroundUserdata(userData, enable);
console.info(`Succeeded in setting restricted access background user data.`);
```

### getRestrictedAccessBackgroundUserdataStatus

getRestrictedAccessBackgroundUserdataStatus(userData: UserDataEnum): Promise<boolean>

获取系统服务进程不可访问的后台用户数据状态。后台用户数据主要包含如下目录['/data/service','/data/app','/storage','/mnt']下特定路径下的用户数据。使用Promise异步回调。

**起始版本：** 6.0.1(21)

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userData | [UserDataEnum](enterprisespace-spacemanager.md#userdataenum) | 是 | 表示工作空间类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，表示系统服务进程访问后台用户数据是否管控。  - true：表示开启管控，此时系统服务进程不可访问后台用户的数据  - false：表示关闭管控，此时系统服务进程可正常访问后台用户的数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-space.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 801 | The device type not supported.  适用版本：26.0.0+ |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. |
| 1020400007 | Enterprise workspace not enabled. |

**示例：**

```typescript
import { spaceManager } from '@kit.EnterpriseSpaceKit';

const userData: spaceManager.UserDataEnum = spaceManager.UserDataEnum.ENTERPRISE;
const status: boolean = await spaceManager.getRestrictedAccessBackgroundUserdataStatus(userData);
console.info(`Succeeded in getting restricted access background user data status. status: ${status}`);
```

### getRestrictedAccessBackgroundUserdataProcessList

getRestrictedAccessBackgroundUserdataProcessList(userData: UserDataEnum): Promise<ProcessConfigInfo[]>

获取不可访问后台用户数据的系统服务进程列表。使用Promise异步回调。

**起始版本：** 6.0.1(21)

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userData | [UserDataEnum](enterprisespace-spacemanager.md#userdataenum) | 是 | 表示工作空间类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ProcessConfigInfo](enterprisespace-spacemanager.md#processconfiginfo)[]> | Promise对象，返回当前配置的管控信息列表。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-space.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 801 | The device type not supported.  适用版本：26.0.0+ |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. |
| 1020400007 | Enterprise workspace not enabled. |

**示例：**

```typescript
import { spaceManager } from '@kit.EnterpriseSpaceKit';

const userData: spaceManager.UserDataEnum = spaceManager.UserDataEnum.ENTERPRISE;
try {
  const processConfigInfos: spaceManager.ProcessConfigInfo[] = await spaceManager.getRestrictedAccessBackgroundUserdataProcessList(userData);
  console.info(`Succeeded in getting restricted access background user data process list. processConfigInfos: ${JSON.stringify(processConfigInfos)}`);
} catch (err) {
  console.error(`Failed to get restricted access background user data process list. Code: ${err.code}, message: ${err.message}`);
}
```

### addRestrictedAccessBackgroundUserdataProcessList

addRestrictedAccessBackgroundUserdataProcessList(userData: UserDataEnum, processName: string, disallowPaths?: string[]): Promise<void>

新增系统服务进程不可访问后台用户数据路径列表。使用Promise异步回调。

**起始版本：** 6.0.1(21)

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userData | [UserDataEnum](enterprisespace-spacemanager.md#userdataenum) | 是 | 表示工作空间类型。 |
| processName | string | 是 | 表示系统服务进程的名称。 |
| disallowPaths | string[] | 否 | 表示配置的不可访问的路径。  - 当不传该参数时，默认值为['/data/service','/data/app','/storage','/mnt']  - 当传该参数时，其值只能是['/data/service','/data/app','/storage','/mnt']列表的子集 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-space.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 801 | The device type not supported.  适用版本：26.0.0+ |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. |
| 1020400007 | Enterprise workspace not enabled. |

**示例：**

```typescript
import { spaceManager } from '@kit.EnterpriseSpaceKit';

const userData: spaceManager.UserDataEnum = spaceManager.UserDataEnum.ENTERPRISE;
const processName: string = 'testSa'; // 系统实际服务进程的名称。
const disallowPaths: string[] = ['/data/service', '/data/app'];
try {
  await spaceManager.addRestrictedAccessBackgroundUserdataProcessList(userData, processName, disallowPaths);
  console.info(`Succeeded in adding restricted access background user data process list.`);
} catch (err) {
  console.error(`Failed to add restricted access background user data process list. Code: ${err.code}, message: ${err.message}`);
}
```

### deleteRestrictedAccessBackgroundUserdataProcessList

deleteRestrictedAccessBackgroundUserdataProcessList(userData: UserDataEnum, processName: string): Promise<void>

删除系统服务进程不可访问后台用户数据路径列表。使用Promise异步回调。

**起始版本：** 6.0.1(21)

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userData | [UserDataEnum](enterprisespace-spacemanager.md#userdataenum) | 是 | 表示工作空间类型，其值参考[UserDataEnum](enterprisespace-spacemanager.md#userdataenum)枚举值。 |
| processName | string | 是 | 表示系统服务进程的名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-space.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 801 | The device type not supported.  适用版本：26.0.0+ |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. |
| 1020400007 | Enterprise workspace not enabled. |

**示例：**

```typescript
import { spaceManager } from '@kit.EnterpriseSpaceKit';

const userData: spaceManager.UserDataEnum = spaceManager.UserDataEnum.ENTERPRISE;
const processName: string = 'testSa'; // 系统实际服务进程的名称。
try {
  await spaceManager.deleteRestrictedAccessBackgroundUserdataProcessList(userData, processName);
  console.info(`Succeeded in deleting restricted access background user data process list.`);
} catch (err) {
  console.error(`Failed to delete restricted access background user data process list. Code: ${err.code}, message: ${err.message}`);
}
```

### setWorkspacePolicy

setWorkspacePolicy(key: string, value: number, workspaceId?: number): Promise<void>

设置工作空间策略。使用Promise异步回调。

**起始版本：** 6.0.2(22)

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES或ohos.permission.MANAGE\_LOCAL\_WORKSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 表示策略名称。从6.0.2(22)版本开始支持深度冻结策略“lockdown”，从6.1.0(23)版本开始支持个人空间创建引导页展示策略“spaceguide”。 |
| value | number | 是 | 表示策略状态。当key为“lockdown”时，取值可参见[LockdownModePolicy](enterprisespace-spacemanager.md#lockdownmodepolicy)枚举值；当key为“spaceguide”时，取值可参见[SpaceGuidePolicy](enterprisespace-spacemanager.md#spaceguidepolicy)枚举值。 |
| workspaceId | number | 否 | 工作空间ID。首个空间ID为100，后续创建的工作空间ID逐一递增，例如101、102。如果未设置，则默认使用调用者所在的工作空间ID。取值应为[100,10736]内的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-space.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 801 | The device type not supported.  适用版本：26.0.0+ |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```typescript
import { spaceManager } from '@kit.EnterpriseSpaceKit';

const key: string = 'lockdown';
const value: spaceManager.LockdownModePolicy = spaceManager.LockdownModePolicy.OFF;
const workspaceId: number = 100;
await spaceManager.setWorkspacePolicy(key, value, workspaceId);
console.info(`Succeeded in setting workspace policy.`);
```

### getWorkspacePolicy

getWorkspacePolicy(key: string, workspaceId?: number): Promise<number>

查询工作空间策略。使用Promise异步回调。

**起始版本：** 6.0.2(22)

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.QUERY\_LOCAL\_WORKSPACES或ohos.permission.MANAGE\_LOCAL\_WORKSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 表示策略名称。从6.0.2(22)版本开始支持深度冻结策略“lockdown”，从6.1.0(23)版本开始支持个人空间创建引导页展示策略“spaceguide”。 |
| workspaceId | number | 否 | 工作空间ID。首个空间ID为100，后续创建的工作空间ID逐一递增，例如101、102。如果未设置，则默认使用调用者所在的工作空间ID。取值应为[100,10736]内的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回策略状态，根据传入的key查看[LockdownModePolicy](enterprisespace-spacemanager.md#lockdownmodepolicy)或者[SpaceGuidePolicy](enterprisespace-spacemanager.md#spaceguidepolicy)的枚举值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-space.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 801 | The device type not supported.  适用版本：26.0.0+ |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1020400005 | Configuration not set. |

**示例：**

```typescript
import { spaceManager } from '@kit.EnterpriseSpaceKit';

const key: string = 'lockdown';
const workspaceId: number = 100;
const value: number = await spaceManager.getWorkspacePolicy(key, workspaceId);
console.info(`Succeeded in getting workspace policy. value: ${value}`);
```

### setLockdownExemptionApps

setLockdownExemptionApps(appIds: string[], workspaceId?: number): Promise<void>

设置深度冻结豁免名单。设置的豁免应用在后台空间可正常运行，不会被冻结。使用Promise异步回调。

**起始版本：** 6.0.2(22)

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appIds | string[] | 是 | 表示属于深度冻结豁免名单的应用ID数组。列表，例如“['com.example.test1\_BN\*\*\*\*\*\*\*\*\*\*\*\*', 'com.example.test2\_BN\*\*\*\*\*\*\*\*\*\*\*\*']”。详情信息可参考[什么是appId](../harmonyos-guides/common-problem-of-application.md#什么是appid)。 |
| workspaceId | number | 否 | 表示工作空间ID。首个空间ID为100，后续创建的工作空间ID逐一递增，例如101、102。如果未设置，则默认使用调用者所在的工作空间ID。取值应为[100,10736]内的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-space.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 801 | The device type not supported.  适用版本：26.0.0+ |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1020400007 | Enterprise workspace not enabled. |

**示例：**

```typescript
import { spaceManager } from '@kit.EnterpriseSpaceKit';

const workspaceId: number = 100;
const appIds = [
  'com.example.test1_BN************',
  'com.example.test2_BN************'
];
await spaceManager.setLockdownExemptionApps(appIds, workspaceId);
console.info(`Succeeded in setting lockdown exemption apps.`);
```

### getLockdownExemptionApps

getLockdownExemptionApps(workspaceId?: number): Promise<string[]>

查询深度冻结豁免名单。使用Promise异步回调。

**起始版本：** 6.0.2(22)

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.QUERY\_LOCAL\_WORKSPACES或ohos.permission.MANAGE\_LOCAL\_WORKSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| workspaceId | number | 否 | 工作空间ID。首个空间ID为100，后续创建的工作空间ID逐一递增，例如101、102。如果未设置，则默认使用调用者所在的工作空间ID。取值应为[100,10736]内的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string[]> | Promise对象，返回深度冻结豁免名单。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-space.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 801 | The device type not supported.  适用版本：26.0.0+ |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1020400007 | Enterprise workspace not enabled. |

**示例：**

```typescript
import { spaceManager } from '@kit.EnterpriseSpaceKit';

const workspaceId: number = 100;
const apps: string[] = await spaceManager.getLockdownExemptionApps(workspaceId);
console.info(`Succeeded in getting lockdown exemption apps. apps: ${JSON.stringify(apps)}`);
```

### authenticate

authenticate(enterpriseAuthInfo: WorkspaceDomainInfo, credential: Uint8Array): Promise<AuthResult>

企业账号认证。使用Promise异步回调。

**起始版本：** 6.1.0(23)

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enterpriseAuthInfo | [WorkspaceDomainInfo](enterprisespace-spacemanager.md#workspacedomaininfo) | 是 | 工作空间域信息，具体可参见[WorkspaceDomainInfo](enterprisespace-spacemanager.md#workspacedomaininfo)。 |
| credential | Uint8Array | 是 | 企业用户登录凭证（如密码），需由用户传入。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AuthResult](enterprisespace-spacemanager.md#authresult)> | Promise对象，返回企业账号认证结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-space.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 801 | The device type not supported.  适用版本：26.0.0+ |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1020400004 | Authentication failed. |
| 1020400008 | Invalid account name or password. |
| 1020400009 | The account is locked. |
| 1020400010 | Enterprise authentication server unreachable. |

**示例：**

```typescript
import { spaceManager } from '@kit.EnterpriseSpaceKit';

try {
  const enterpriseAuthInfo: spaceManager.WorkspaceDomainInfo = {
    domain: 'testDomain',
    workspaceName: 'testAccountName',
    serverConfigId: 'testServerConfigId'
  };
  const credential = new Uint8Array([0, 0, 0, 0, 0, 0, 0, 0])
  const authResult: spaceManager.AuthResult = await spaceManager.authenticate(enterpriseAuthInfo, credential);
  console.info(`Succeeded in authenticating. authResult: ${JSON.stringify(authResult)}`);
} catch (err) {
  console.error(`Failed to authenticate. Code: ${err.code}, message: ${err.message}`);
}
```

### getAccessToken

getAccessToken(businessParams: Record<string, string>): Promise<Uint8Array>

获取企业应用访问令牌。使用Promise异步回调。

**起始版本：** 6.1.0(23)

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| businessParams | Record<string, string> | 是 | 业务参数，由业务方根据请求协议自定义。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | Promise对象，返回访问令牌，可用于企业应用的免密登录。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-space.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 801 | The device type not supported.  适用版本：26.0.0+ |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1020400003 | Invalid workspace. |
| 1020400004 | Authentication failed. |
| 1020400010 | Enterprise authentication server unreachable. |

**示例：**

```typescript
import { spaceManager } from '@kit.EnterpriseSpaceKit';

try {
  const params: Record<string, string> = {
    'clientId': 'test1'
  };
  const result: Uint8Array = await spaceManager.getAccessToken(params);
  console.info(`Succeeded in getting access token. result: ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get access token. Code: ${err.code}, message: ${err.message}`);
}
```

### setWorkspaceStatusBarIcon

setWorkspaceStatusBarIcon(icon: StatusBarIcon, workspaceId?: number): Promise<void>

根据工作空间ID设置工作空间状态栏图标。使用Promise异步回调。

该接口仅供企业安全管控类MDM应用申请权限后使用，可修改状态栏图标的工作空间受限于当前MDM应用所在工作空间。若MDM应用安装在系统预制用户下，可修改其他工作空间状态栏图标，否则仅能修改当前MDM应用所在工作空间的状态栏图标。

**起始版本：** 6.1.0(23)

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| icon | [StatusBarIcon](enterprisespace-spacemanager.md#statusbaricon) | 是 | 设置的工作空间的状态栏图标。 |
| workspaceId | number | 否 | 工作空间ID。首个空间ID为100，后续创建的工作空间ID逐一递增，例如101、102。如果未设置，则默认使用调用者所在的工作空间ID。取值应为[100,10736]内的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-space.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 801 | The device type not supported.  适用版本：26.0.0+ |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1020400003 | Invalid workspace. |

**示例：**

```typescript
import { spaceManager } from '@kit.EnterpriseSpaceKit';
import { resourceManager } from '@kit.LocalizationKit';
import { image } from '@kit.ImageKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  async test() {
    const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    const resourceMgr: resourceManager.ResourceManager = context.resourceManager;

    // 创建white pixelMap，需在资源rawfile文件夹中预置CustomWhite.jpg图片
    const whiteFileData = await resourceMgr.getRawFd('CustomWhite.jpg');
    const whiteImageSource: image.ImageSource = image.createImageSource(whiteFileData);
    const whitePixelMap: image.PixelMap = await whiteImageSource.createPixelMap();

    // 创建black pixelMap，需在资源rawfile文件夹中预置CustomBlack.jpg图片
    const blackFileData = await resourceMgr.getRawFd('CustomBlack.jpg');
    const blackImageSource: image.ImageSource = image.createImageSource(blackFileData);
    const blackPixelMap: image.PixelMap = await blackImageSource.createPixelMap();

    // 构建图标信息
    const icon: spaceManager.StatusBarIcon = {
      white: whitePixelMap,
      black: blackPixelMap
    };
    const workspaceId: number = 100;
    try {
      await spaceManager.setWorkspaceStatusBarIcon(icon, workspaceId);
      console.info(`Succeeded in setting workspace status bar icon.`);
    } catch (err) {
      console.error(`Failed to set workspace status bar icon. Code: ${err.code}, message: ${err.message}`);
    }
  }

  build() {
  }
}
```

### setWorkspaceLocalName

setWorkspaceLocalName(localName: string, workspaceId?: number): Promise<void>

根据工作空间ID设置工作空间本地名称。使用Promise异步回调。

该接口仅供企业安全管控类MDM应用申请权限后使用，可修改本地名称的工作空间受限于当前MDM应用所在工作空间。若MDM应用安装在系统预制用户下，可修改其他工作空间本地名称，否则仅能修改当前MDM应用所在工作空间的本地名称。

**起始版本：** 6.1.0(23)

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localName | string | 是 | 设置的工作空间的本地名称。 |
| workspaceId | number | 否 | 工作空间ID。首个空间ID为100，后续创建的工作空间ID逐一递增，例如101、102。如果未设置，则默认使用调用者所在的工作空间ID。取值应为[100,10736]内的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-space.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 801 | The device type not supported.  适用版本：26.0.0+ |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```typescript
import { spaceManager } from '@kit.EnterpriseSpaceKit';
 
const localName: string = 'localName';
const workspaceId: number = 100;
await spaceManager.setWorkspaceLocalName(localName, workspaceId);
console.info(`Succeeded in setting workspace local name.`);
```

### isEnterpriseWorkspaceEnabled

isEnterpriseWorkspaceEnabled(): Promise<boolean>

查询设备是否开启企业数字空间特性。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.QUERY\_LOCAL\_WORKSPACES或ohos.permission.MANAGE\_LOCAL\_WORKSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回true表示当前设备已开启企业数字空间特性；返回false表示当前设备未开启企业数字空间特性。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-space.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 801 | The device type not supported. |
| 1020400001 | System service exception. |

**示例：**

```typescript
import { spaceManager } from '@kit.EnterpriseSpaceKit';

const status = await spaceManager.isEnterpriseWorkspaceEnabled();
console.info(`Succeeded in getting space enable. status: ${status}`);
```

### isEnterpriseWorkspace

isEnterpriseWorkspace(workspaceId?: number): Promise<boolean>

查询工作空间是否为企业空间。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.QUERY\_LOCAL\_WORKSPACES或ohos.permission.MANAGE\_LOCAL\_WORKSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| workspaceId | number | 否 | 工作空间ID。首个空间ID为100，后续创建的工作空间ID逐一递增，例如101、102。如果未设置，则默认使用应用所在的工作空间ID。取值应为[100,10736]内的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回true表示该工作空间是企业空间；返回false表示该工作空间是个人空间。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-space.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 801 | The device type not supported. |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1020400003 | Invalid workspace. |
| 1020400007 | Enterprise workspace not enabled. |

**示例：**

```typescript
import { spaceManager } from '@kit.EnterpriseSpaceKit';

const workspaceId: number = 100;
const isEnterprise = await spaceManager.isEnterpriseWorkspace(workspaceId);
console.info(`Succeeded in getting enterprise space. isEnterprise: ${isEnterprise}`);
```

### switchWorkspace

switchWorkspace(workspaceId?: number): Promise<void>

切换工作空间。使用Promise异步回调。

该接口仅供企业安全管控类MDM应用申请权限后使用，并且存在两个空间的情况下允许调用。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| workspaceId | number | 否 | 目标工作空间ID，如果未设置，则默认切换到另一个工作空间。取值应为[100,10736]内的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-space.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 801 | The device type not supported. |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1020400003 | Invalid workspace. |
| 1020400007 | Enterprise workspace not enabled. |

**示例：**

```typescript
import { spaceManager } from '@kit.EnterpriseSpaceKit';

const workspaceId: number = 101; // 已经创建的工作空间ID。
await spaceManager.switchWorkspace(workspaceId);
console.info(`Succeeded in switching workspace.`);
```

### setNotificationConfig

setNotificationConfig(configs: NotificationConfig[]): Promise<void>

设置跨空间消息提醒配置。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| configs | [NotificationConfig](enterprisespace-spacemanager.md#notificationconfig)[] | 是 | 跨空间消息提醒配置列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-space.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 801 | The device type not supported. |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1020400007 | Enterprise workspace not enabled. |
| 1020400014 | Configuration quantity exceeds the limit. |

**示例：**

```typescript
import { spaceManager } from '@kit.EnterpriseSpaceKit';

const configs: spaceManager.NotificationConfig[] = [
  {
    workspaceId: 100,
    appIdentifier: '691867************',
    notificationState: spaceManager.NotificationSwitch.ON,
    visibilityState: spaceManager.NotificationVisibilitySwitch.NOTIFICATION_VISIBLE,
    allowVisibilityChange: spaceManager.NotificationVisibilityControl.ALLOW_CHANGE
  }
];
await spaceManager.setNotificationConfig(configs);
console.info(`Succeeded in setting notification config.`);
```

### getNotificationConfig

getNotificationConfig(): Promise<NotificationConfig[]>

获取跨空间消息提醒配置。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.QUERY\_LOCAL\_WORKSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[NotificationConfig](enterprisespace-spacemanager.md#notificationconfig)[]> | Promise对象，返回跨空间消息提醒配置列表。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-space.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 801 | The device type not supported. |
| 1020400001 | System service exception. |
| 1020400005 | Configuration not set. |
| 1020400007 | Enterprise workspace not enabled. |

**示例：**

```typescript
import { spaceManager } from '@kit.EnterpriseSpaceKit';

const configs: spaceManager.NotificationConfig[] = await spaceManager.getNotificationConfig();
console.info(`Succeeded in getting notification config. configs: ${JSON.stringify(configs)}`);
```
