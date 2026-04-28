---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/enterprisespace-spacemanager
title: spaceManager (空间管理)
breadcrumb: API参考 > 应用服务 > Enterprise Space Kit（企业数字空间服务） > ArkTS API > spaceManager (空间管理)
category: harmonyos-references
scraped_at: 2026-04-28T08:16:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3a7e5620e31d98cd9ab475a8b01c11874b379f1c8af326958cd662e2daf09d62
---

空间管理服务提供统一的空间管理能力，包括创建工作空间、移除工作空间、订阅空间事件等功能，满足用户空间使用和企业对空间的管理诉求。

**起始版本：** 6.0.0(20)

## 导入模块

PC/2in1

```
1. import { spaceManager } from '@kit.EnterpriseSpaceKit';
```

## CreateWorkspaceParams

PC/2in1

创建工作空间参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| shortName | string | 否 | 否 | 工作空间的本地简称，其值与localName一致。 |

## WorkspaceDomainInfo

PC/2in1

工作空间域账号信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| domain | string | 否 | 否 | 域名，仅在企业空间有值，例如“xx.com”，在个人空间中，其值为空。 |
| workspaceName | string | 否 | 否 | 工作空间域账号名称，仅在企业空间中有效，而在个人空间中则为空。 |
| accountId | string | 否 | 是 | 域中的账号标识符，仅在企业空间中有效，而在个人空间中则为空。其创建空间时，由系统自动生成的字符串，在[setWorkspaceInfo](enterprisespace-spacemanager.md#setworkspaceinfo)中可设置为空。 |
| isAuthenticated | boolean | 否 | 是 | 工作空间是否已鉴权。  - true：已鉴权  - false：未鉴权  默认值为false。 |
| serverConfigId | string | 否 | 是 | 工作空间所属域的服务器配置标识符。由创建空间时系统自动生成的，仅在企业空间中有效，例如“xx:test.com”，而在个人空间中则为空。 |
| enterpriseWorkspaceName | string | 否 | 是 | 企业空间名称，企业设备在某个空间下的标签属性。例如，该名称在企业空间为“企业空间”，在个人空间为“个人空间”。  **起始版本**：6.0.2(22) |

## WorkspaceInfo

PC/2in1

工作空间信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| workspaceId | number | 否 | 否 | 工作空间ID。首个空间ID为100，后续创建的工作空间ID逐一递增，例如101、102。 |
| localName | string | 否 | 否 | 工作空间的本地账号名称，例如，“test”。 |
| shortName | string | 否 | 是 | 工作空间的本地简称，其值与localName一致。 |
| isUnlocked | boolean | 否 | 否 | 工作空间是否处于解锁状态。  - true：解锁状态  - false：锁屏状态  默认值为false。 |
| photo | string | 否 | 否 | 工作空间的资料照片，是由本地照片的Base64格式拼接成的JSON字符串。“type”为照片类型，当前仅支持值为0；“defaultImg”为由照片转为Base64格式的字符串。例如，拼接后字符串为“{"type":0,"defaultImg":"data:image/png;base64,iVBO\*\*\*\*\*\*Jggg==}”。 |
| createTime | number | 否 | 否 | 工作空间的创建时间戳，为系统生成的10位数字组成的时间戳。 |
| lastLoginTime | number | 否 | 否 | 工作空间的最后登录时间，通常为系统生成的10位数字组成的时间戳。 |
| serialNumber | number | 否 | 否 | 通常为由9位数字组成的工作空间序列号。 |
| isActivated | boolean | 否 | 否 | 工作空间是否处于激活状态。  - true：激活状态  - false：未激活状态  默认值为false。 |
| isCreateCompleted | boolean | 否 | 否 | 工作空间创建是否完成。  - true：创建工作空间已完成状态  - false：创建工作空间未完成状态  默认值为true。 |
| isAllowedToBeDeleted | boolean | 否 | 否 | 工作空间是否允许被删除。  - true：允许被删除  - false：不允许被删除  默认值为true。 |
| domainInfo | [WorkspaceDomainInfo](enterprisespace-spacemanager.md#workspacedomaininfo) | 否 | 否 | 工作空间域信息，具体可参见[WorkspaceDomainInfo](enterprisespace-spacemanager.md#workspacedomaininfo)。 |

## ProcessConfigInfo

PC/2in1

管控的系统服务进程以及其不可访问路径的配置信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**起始版本：** 6.0.1(21)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| processName | string | 否 | 否 | 系统服务进程的名称。 |
| disallowPaths | string[] | 否 | 否 | 不可访问的路径列表，列表只能包含如下列表的子集：['/data/service','/data/app','/storage','/mnt'] |

## WorkspaceType

PC/2in1

工作空间类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ADMIN | 0 | 管理员工作空间，具有管理其他工作空间的权限。 |

## QueryType

PC/2in1

查询的工作空间类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ALL | 0 | 查询所有的工作空间。 |
| NON\_DELETABLE | 1 | 查询不允许被删除的工作空间。 |

## EventType

PC/2in1

订阅事件类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EVENT\_WORKSPACE\_SWITCHED | 0 | 工作空间切换事件。 |

## UserDataEnum

PC/2in1

用户类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**起始版本：** 6.0.1(21)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ENTERPRISE | 0 | 表示企业用户。 |
| PERSONAL | 1 | 表示个人用户。 |

## EventData

PC/2in1

与空间事件相关的详细信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| event | [EventType](enterprisespace-spacemanager.md#eventtype) | 否 | 否 | 事件类型，取值可参见[EventType](enterprisespace-spacemanager.md#eventtype)。 |
| currentWorkspaceId | number | 否 | 是 | 当前工作空间ID。 |

## LockdownModePolicy

PC/2in1

锁定模式策略，包括后台应用冻结和公共目录加解密等安全加固功能，提供开关，关闭或者效率模式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**起始版本：** 6.0.2(22)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OFF | 0 | 关闭。关闭后不支持后台应用冻结和公共数据目录加解密。 |
| EFFICIENT | 1 | 效率模式。支持后台应用冻结和公共数据目录加解密。 |

## SpaceGuidePolicy

PC/2in1

个人空间创建引导页展示策略。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**起始版本：** 6.1.0(23)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SHOW | 0 | 展示个人空间创建页引导页。 |
| HIDE | 1 | 隐藏个人空间创建页引导页。 |

## AuthResult

PC/2in1

企业认证返回结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**起始版本：** 6.1.0(23)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| result | number | 否 | 否 | 认证结果，0代表成功，其他代表失败。 |
| workspaceId | number | 否 | 否 | 当前调用方的工作空间ID。 |

## StatusBarIcon

PC/2in1

状态栏图标。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**起始版本：** 6.1.0(23)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| white | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | 否 | 黑色背景下图标，样式设计[参考设计规范](../design-guides/statusbar-0000002319710910.md#section13803824112416)。 |
| black | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | 否 | 白色背景下图标，样式设计[参考设计规范](../design-guides/statusbar-0000002319710910.md#section13803824112416)。 |

## createWorkspace

PC/2in1

createWorkspace(localName: string, workspaceType: WorkspaceType, params?: CreateWorkspaceParams): Promise<WorkspaceInfo>

创建工作空间。使用Promise异步回调。

说明

从6.1.0(23)版本，在创建工作空间时，增加如下校验：

* 最多可创建2个工作空间。
* 企业管理员设置禁止添加账号或者关闭全盘解密后，无法创建工作空间。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES或ohos.permission.MANAGE\_LOCAL\_WORKSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localName | string | 是 | 工作空间的本地名称。 |
| workspaceType | [WorkspaceType](enterprisespace-spacemanager.md#workspacetype) | 是 | 工作空间的类型，取值可参见[WorkspaceType](enterprisespace-spacemanager.md#workspacetype)。 |
| params | [CreateWorkspaceParams](enterprisespace-spacemanager.md#createworkspaceparams) | 否 | 创建工作空间配置，具体可参见[CreateWorkspaceParams](enterprisespace-spacemanager.md#createworkspaceparams)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[WorkspaceInfo](enterprisespace-spacemanager.md#workspaceinfo)> | Promise对象，返回工作空间信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](enterprisespace-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. |
| 1020400003 | Invalid workspace. |
| 1020400007 | Enterprise workspace not enabled. |
| 1020400011 | Account creation is not permitted. |
| 1020400012 | Full disk encryption is not enabled. |

**示例：**

```
1. import { spaceManager } from '@kit.EnterpriseSpaceKit';

3. const localName: string = '111111';
4. const workspaceType: spaceManager.WorkspaceType = spaceManager.WorkspaceType.ADMIN;
5. const params: spaceManager.CreateWorkspaceParams = {
6. shortName: 'test'
7. };
8. try {
9. const workspaceInfo: spaceManager.WorkspaceInfo = await spaceManager.createWorkspace(localName, workspaceType, params);
10. console.info(`Succeeded in creating workspace, workspaceInfo:` + JSON.stringify(workspaceInfo));
11. } catch (err) {
12. console.error(`Failed to create workspace. Code: ${err.code}, message: ${err.message}`);
13. }
```

## enableWorkspace

PC/2in1

enableWorkspace(enable: boolean): Promise<void>

使能双空间特性。双空间分别为企业空间和个人空间，企业空间为完全受企业管控的通用办公空间，个人空间为因工作需要对外交流、作业、开源开发等用途的空间。使用Promise异步回调。

说明

从6.1.0(23)开始，使能双空间特性时，增加以下校验：

* 用户数量不超过2个。
* 企业管理员设置禁止关闭全盘解密后，无法使能双空间特性。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES或ohos.permission.MANAGE\_LOCAL\_WORKSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 双空间特性是否启用。默认值为false。  - true：支持双空间特性  - false：不支持双空间特性 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](enterprisespace-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. |
| 1020400003 | Invalid workspace. |
| 1020400012 | Full disk encryption is not enabled. |

**示例：**

```
1. import { spaceManager } from '@kit.EnterpriseSpaceKit';

3. const enable: boolean = true;
4. try {
5. await spaceManager.enableWorkspace(enable);
6. console.info('Succeeded in enabling workspace');
7. } catch (err) {
8. console.error(`Failed to enable workspace. Code: ${err.code}, message: ${err.message}`);
9. }
```

## queryWorkspace

PC/2in1

queryWorkspace(queryFlag: QueryType): Promise<WorkspaceInfo[]>

查询工作空间。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.QUERY\_LOCAL\_WORKSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| queryFlag | [QueryType](enterprisespace-spacemanager.md#querytype) | 是 | 工作空间类型，其取值可参见[QueryType](enterprisespace-spacemanager.md#querytype)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[WorkspaceInfo](enterprisespace-spacemanager.md#workspaceinfo)[]> | Promise对象，返回工作空间信息列表。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](enterprisespace-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. |

**示例：**

```
1. import { spaceManager } from '@kit.EnterpriseSpaceKit';

3. const queryFlag: spaceManager.QueryType = spaceManager.QueryType.ALL;
4. try {
5. const spaces: spaceManager.WorkspaceInfo[] = await spaceManager.queryWorkspace(queryFlag);
6. console.info(`Succeeded in querying workspace` + JSON.stringify(spaces));
7. } catch (err) {
8. console.error(`Failed to query workspace. Code: ${err.code}, message: ${err.message}`);
9. }
```

## removeWorkspace

PC/2in1

removeWorkspace(workspaceId: number): Promise<void>

移除工作空间。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES或ohos.permission.MANAGE\_LOCAL\_WORKSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| workspaceId | number | 是 | 工作空间ID。首个空间ID为100，后续创建的工作空间ID逐一递增，例如101、102。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](enterprisespace-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. |
| 1020400003 | Invalid workspace. |
| 1020400007 | Enterprise workspace not enabled. |

**示例：**

```
1. import { spaceManager } from '@kit.EnterpriseSpaceKit';

3. const workspaceId: number = 100;
4. try {
5. await spaceManager.removeWorkspace(workspaceId);
6. console.info('Succeeded in removing workspace');
7. } catch (err) {
8. console.error(`Failed to remove workspace. Code: ${err.code}, message: ${err.message}`);
9. }
```

## setWorkspaceInfo

PC/2in1

setWorkspaceInfo(workspaceId: number, domainInfo: WorkspaceDomainInfo): Promise<void>

设置工作空间域信息。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| workspaceId | number | 是 | 工作空间ID。首个空间ID为100，后续创建的工作空间ID逐一递增，例如101、102。 |
| domainInfo | [WorkspaceDomainInfo](enterprisespace-spacemanager.md#workspacedomaininfo) | 是 | 工作空间域信息，具体可参见[WorkspaceDomainInfo](enterprisespace-spacemanager.md#workspacedomaininfo)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](enterprisespace-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. |
| 1020400003 | Invalid workspace. |
| 1020400007 | Enterprise workspace not enabled. |

**示例：**

```
1. import { spaceManager } from '@kit.EnterpriseSpaceKit';

3. const workspaceId: number = 100;
4. const domainInfo: spaceManager.WorkspaceDomainInfo = {
5. domain: 'test1',
6. workspaceName: 'test2',
7. accountId: 'test3',
8. isAuthenticated: false,
9. serverConfigId: 'test4',
10. enterpriseWorkspaceName: 'default'
11. };

13. try {
14. await spaceManager.setWorkspaceInfo(workspaceId, domainInfo);
15. console.info('Succeeded in setting workspace info');
16. } catch (err) {
17. console.error(`Failed to set workspace info. Code: ${err.code}, message: ${err.message}`);
18. }
```

## setWorkspaceProfilePhoto

PC/2in1

setWorkspaceProfilePhoto(workspaceId: number, photo: string): Promise<void>

根据工作空间ID设置工作空间资料照片。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| workspaceId | number | 是 | 工作空间ID。首个空间ID为100，后续创建的工作空间ID逐一递增，例如101、102。 |
| photo | string | 是 | 设置的工作空间的资料照片，是由本地照片的Base64格式拼接成的JSON字符串。“type”为照片类型，当前仅支持值为0；“defaultImg”为由照片转为Base64格式的字符串。例如，拼接后字符串为“{"type":0,"defaultImg":"data:image/png;base64,iVBO\*\*\*\*\*\*Jggg==}”。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](enterprisespace-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. |
| 1020400003 | Invalid workspace. |
| 1020400007 | Enterprise workspace not enabled. |

**示例：**

```
1. import { spaceManager } from '@kit.EnterpriseSpaceKit';

3. const workspaceId: number = 100;
4. const photo: string = '{"type":0,"defaultImg":"data:image/png;base64,iVBO******Jggg==}';
5. try {
6. await spaceManager.setWorkspaceProfilePhoto(workspaceId, photo);
7. console.info('Succeeded in setting workspace profile photo');
8. } catch (err) {
9. console.error(`Failed to set workspace profile photo. Code: ${err.code}, message: ${err.message}`);
10. }
```

## subscribeEvent

PC/2in1

subscribeEvent(eventId: EventType[], callback: AsyncCallback<EventData>): number

订阅空间事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_WORKSPACES\_EVENT\_SUBSCRIBE

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | [EventType](enterprisespace-spacemanager.md#eventtype)[] | 是 | 订阅的空间事件类型列表。 |
| callback | AsyncCallback<[EventData](enterprisespace-spacemanager.md#eventdata)> | 是 | 回调函数，当订阅空间事件成功，[EventData](enterprisespace-spacemanager.md#eventdata)为与空间事件相关的详细信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 订阅ID，用于在取消空间事件中使用。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](enterprisespace-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. |
| 1020400006 | Session disconnected. |
| 1020400007 | Enterprise workspace not enabled. |

**示例：**

```
1. import { spaceManager } from '@kit.EnterpriseSpaceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. const subscribeId = spaceManager.subscribeEvent([spaceManager.EventType.EVENT_WORKSPACE_SWITCHED],
6. (error: BusinessError, data: spaceManager.EventData) => {
7. if (error) {
8. console.error(`error info:${error?.code}, err message:${error?.message}`);
9. } else {
10. console.info(`event: ${data.event},currentWorkSpaceId: ${data.currentWorkspaceId}`);
11. }
12. });
13. console.info(`Succeeded in subscribing event. subscribeId: ${subscribeId}`);
14. } catch (err) {
15. console.error(`Failed to subscribe event. Code: ${err.code}, message: ${err.message}`);
16. }
```

## unsubscribeEvent

PC/2in1

unsubscribeEvent(subscribeId: number): void

取消订阅空间事件。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_WORKSPACES\_EVENT\_SUBSCRIBE

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| subscribeId | number | 是 | 由订阅空间事件得到的订阅ID，用于取消订阅对应的空间事件。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](enterprisespace-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. |
| 1020400007 | Enterprise workspace not enabled. |

**示例：**

```
1. import { spaceManager } from '@kit.EnterpriseSpaceKit';

3. const subscribeId: number = 100;
4. try {
5. spaceManager.unsubscribeEvent(subscribeId);
6. console.info('Succeeded in unsubscribing event');
7. } catch (err) {
8. console.error(`Failed to unsubscribe event. Code: ${err.code}, message: ${err.message}`);
9. }
```

## setRestrictedAccessBackgroundUserdata

PC/2in1

setRestrictedAccessBackgroundUserdata(userData: UserDataEnum, enable: boolean): Promise<void>

设置系统服务进程不可访问后台用户数据的功能。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**起始版本：** 6.0.1(21)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userData | [UserDataEnum](enterprisespace-spacemanager.md#userdataenum) | 是 | 表示用户空间类型。 |
| enable | boolean | 是 | 表示是否开启管控。默认值为true。  - true：表示开启管控，此时系统服务进程不可访问后台用户的数据  - false：表示关闭管控，此时系统服务进程可正常访问后台用户的数据 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](enterprisespace-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. |
| 1020400007 | Enterprise workspace not enabled. |

**示例：**

```
1. import { spaceManager } from '@kit.EnterpriseSpaceKit';

3. const userData: spaceManager.UserDataEnum = spaceManager.UserDataEnum.ENTERPRISE;
4. const enable: boolean = false;
5. try {
6. await spaceManager.setRestrictedAccessBackgroundUserdata(userData, enable)
7. console.info(`Succeeded in setting restricted access background user data. userData: ${userData}, enable: ${enable}`);
8. } catch (err) {
9. console.error(`Failed to set restricted access background user data. Code: ${err.code}, message: ${err.message}`);
10. }
```

## getRestrictedAccessBackgroundUserdataStatus

PC/2in1

getRestrictedAccessBackgroundUserdataStatus(userData: UserDataEnum): Promise<boolean>

获取系统服务进程不可访问的后台用户数据状态。后台用户数据主要包含如下目录['/data/service','/data/app','/storage','/mnt']下特定路径下的用户数据。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**起始版本：** 6.0.1(21)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userData | [UserDataEnum](enterprisespace-spacemanager.md#userdataenum) | 是 | 表示用户空间类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，表示当前用户空间不可访问功能状态。  表示是否开启管控。  - true：表示开启管控，此时系统服务进程不可访问后台用户的数据  - false：表示关闭管控，此时系统服务进程可正常访问后台用户的数据 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](enterprisespace-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. |
| 1020400007 | Enterprise workspace not enabled. |

**示例：**

```
1. import { spaceManager } from '@kit.EnterpriseSpaceKit';

3. const userData: spaceManager.UserDataEnum = spaceManager.UserDataEnum.ENTERPRISE;
4. try {
5. const status: boolean = await spaceManager.getRestrictedAccessBackgroundUserdataStatus(userData);
6. console.info(`Succeeded in getting restricted access background user data status. status: ${status}`);
7. } catch (err) {
8. console.error(`Failed to get restricted access background user data status. Code: ${err.code}, message: ${err.message}`);
9. }
```

## getRestrictedAccessBackgroundUserdataProcessList

PC/2in1

getRestrictedAccessBackgroundUserdataProcessList(userData: UserDataEnum): Promise<ProcessConfigInfo[]>

获取不可访问后台用户数据的系统服务进程列表。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**起始版本：** 6.0.1(21)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userData | [UserDataEnum](enterprisespace-spacemanager.md#userdataenum) | 是 | 表示用户空间类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ProcessConfigInfo](enterprisespace-spacemanager.md#processconfiginfo)[]> | Promise对象，表示当前配置的管控信息列表。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](enterprisespace-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. |
| 1020400007 | Enterprise workspace not enabled. |

**示例：**

```
1. import { spaceManager } from '@kit.EnterpriseSpaceKit';

3. const userData: spaceManager.UserDataEnum = spaceManager.UserDataEnum.ENTERPRISE;
4. try {
5. const processConfigInfos: spaceManager.ProcessConfigInfo[] = await spaceManager.getRestrictedAccessBackgroundUserdataProcessList(userData);
6. console.info(`Succeeded in getting restricted access background user data process list. process config infos: ${JSON.stringify(processConfigInfos)}`);
7. } catch (err) {
8. console.error(`Failed to get restricted access background user data process list. Code: ${err.code}, message: ${err.message}`);
9. }
```

## addRestrictedAccessBackgroundUserdataProcessList

PC/2in1

addRestrictedAccessBackgroundUserdataProcessList(userData: UserDataEnum, processName: string, disallowPaths?: string[]): Promise<void>

新增系统服务进程不可访问后台用户数据路径列表。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**起始版本：** 6.0.1(21)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userData | [UserDataEnum](enterprisespace-spacemanager.md#userdataenum) | 是 | 表示用户空间类型。 |
| processName | string | 是 | 表示系统服务进程的名称。 |
| disallowPaths | string[] | 否 | 表示配置的不可访问的路径。  - 当不传该参数时，默认值为['/data/service','/data/app','/storage','/mnt']  - 当传该参数时，其值只能是['/data/service','/data/app','/storage','/mnt']列表的子集 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](enterprisespace-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. |
| 1020400007 | Enterprise workspace not enabled. |

**示例：**

```
1. import { spaceManager } from '@kit.EnterpriseSpaceKit';

3. const userData: spaceManager.UserDataEnum = spaceManager.UserDataEnum.ENTERPRISE;
4. const processName: string = 'testSa';
5. const disallowPaths: string[] = ['/data/service', '/data/app'];
6. try {
7. await spaceManager.addRestrictedAccessBackgroundUserdataProcessList(userData, processName, disallowPaths);
8. console.info(`Succeeded in adding restricted access background user data process list`);
9. } catch (err) {
10. console.error(`Failed to add restricted access background user data process list. Code: ${err.code}, message: ${err.message}`);
11. }
```

## deleteRestrictedAccessBackgroundUserdataProcessList

PC/2in1

deleteRestrictedAccessBackgroundUserdataProcessList(userData: UserDataEnum, processName: string): Promise<void>

删除系统服务进程不可访问后台用户数据路径列表。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**起始版本：** 6.0.1(21)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userData | [UserDataEnum](enterprisespace-spacemanager.md#userdataenum) | 是 | 表示用户空间类型，其值参考[UserDataEnum](enterprisespace-spacemanager.md#userdataenum)枚举值。 |
| processName | string | 是 | 表示系统服务进程的名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](enterprisespace-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. |
| 1020400007 | Enterprise workspace not enabled. |

**示例：**

```
1. import { spaceManager } from '@kit.EnterpriseSpaceKit';

3. const userData: spaceManager.UserDataEnum = spaceManager.UserDataEnum.ENTERPRISE;
4. const processName: string = 'testSa';
5. try {
6. await spaceManager.deleteRestrictedAccessBackgroundUserdataProcessList(userData, processName);
7. console.info(`Succeeded in deleting restricted access background user data process list`);
8. } catch (err) {
9. console.error(`Failed to delete restricted access background user data process list. Code: ${err.code}, message: ${err.message}`);
10. }
```

## setWorkspacePolicy

PC/2in1

setWorkspacePolicy(key: string, value: number, workspaceId?: number): Promise<void>

设置工作空间策略。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**起始版本：** 6.0.2(22)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 表示策略名称。从6.0.2(22)版本开始支持深度冻结策略“lockdown”，从6.1.0(23)版本开始支持个人空间创建引导页展示策略“spaceguide”。 |
| value | number | 是 | 表示策略状态。当key为“lockdown”时，取值可参见[LockdownModePolicy](enterprisespace-spacemanager.md#lockdownmodepolicy)枚举值；当key为“spaceguide”时，取值可参见[SpaceGuidePolicy](enterprisespace-spacemanager.md#spaceguidepolicy)枚举值。 |
| workspaceId | number | 否 | 工作空间ID。首个空间ID为100，后续创建的工作空间ID逐一递增，例如101、102。如果未设置，则默认使用调用者所在的工作空间ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](enterprisespace-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. |

**示例：**

```
1. import { spaceManager } from '@kit.EnterpriseSpaceKit';

3. const key: string = 'lockdown';
4. const value: spaceManager.LockdownModePolicy = spaceManager.LockdownModePolicy.OFF;
5. const workspaceId: number = 100;
6. try {
7. await spaceManager.setWorkspacePolicy(key, value, workspaceId);
8. console.info(`Succeeded in setting workspace policy.`);
9. } catch (err) {
10. console.error(`Failed to set workspace policy. Code: ${err.code}, message: ${err.message}`);
11. }
```

## getWorkspacePolicy

PC/2in1

getWorkspacePolicy(key: string, workspaceId?: number): Promise<number>

查询工作空间策略。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.QUERY\_LOCAL\_WORKSPACES或ohos.permission.MANAGE\_LOCAL\_WORKSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**起始版本：** 6.0.2(22)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 表示策略名称。从6.0.2(22)版本开始支持深度冻结策略“lockdown”，从6.1.0(23)版本开始支持个人空间创建引导页展示策略“spaceguide”。 |
| workspaceId | number | 否 | 工作空间ID。首个空间ID为100，后续创建的工作空间ID逐一递增，例如101、102。如果未设置，则默认使用调用者所在的工作空间ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，策略状态，根据传入的key查看[LockdownModePolicy](enterprisespace-spacemanager.md#lockdownmodepolicy)或者[SpaceGuidePolicy](enterprisespace-spacemanager.md#spaceguidepolicy)的枚举值。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](enterprisespace-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. |
| 1020400005 | Configuration not set. |

**示例：**

```
1. import { spaceManager } from '@kit.EnterpriseSpaceKit';

3. const key: string = 'lockdown';
4. const workspaceId: number = 100;
5. try {
6. const value: number = await spaceManager.getWorkspacePolicy(key, workspaceId);
7. console.info(`Succeeded in getting workspace policy. value: ${value}`);
8. } catch (err) {
9. console.error(`Failed to get workspace policy. Code: ${err.code}, message: ${err.message}`);
10. }
```

## setLockdownExemptionApps

PC/2in1

setLockdownExemptionApps(appIds: string[], workspaceId?: number): Promise<void>

设置深度冻结豁免名单。设置的豁免应用在后台空间可正常运行，不会被冻结。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**起始版本：** 6.0.2(22)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appIds | string[] | 是 | 表示属于深度冻结豁免名单的应用ID数组。列表，例如“[com.example.test1, com.example.test2]”。 |
| workspaceId | number | 否 | 表示属于豁免名单的空间ID。首个空间ID为100，后续创建的工作空间ID逐一递增，例如101、102。如果未设置，则默认使用调用者所在的工作空间ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](enterprisespace-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. |
| 1020400007 | Enterprise workspace not enabled. |

**示例：**

```
1. import { spaceManager } from '@kit.EnterpriseSpaceKit';

3. const workspaceId: number = 100;
4. const appIds = [
5. 'com.example.enterprisespacekit_samplecode_clientdemo_arkts1',
6. 'com.example.enterprisespacekit_samplecode_clientdemo_arkts2'
7. ];
8. try {
9. await spaceManager.setLockdownExemptionApps(appIds, workspaceId);
10. console.info(`Succeeded in setting lockdown exemption apps.`);
11. } catch (err) {
12. console.error(`Failed to set lockdown exemption apps. Code: ${err.code}, message: ${err.message}`);
13. }
```

## getLockdownExemptionApps

PC/2in1

getLockdownExemptionApps(workspaceId?: number): Promise<string[]>

查询深度冻结豁免名单。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.QUERY\_LOCAL\_WORKSPACES或ohos.permission.MANAGE\_LOCAL\_WORKSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**起始版本：** 6.0.2(22)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| workspaceId | number | 否 | 工作空间ID。首个空间ID为100，后续创建的工作空间ID逐一递增，例如101、102。如果未设置，则默认使用调用者所在的工作空间ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string[]> | Promise对象，表示深度冻结豁免名单。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](enterprisespace-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. |
| 1020400007 | Enterprise workspace not enabled. |

**示例：**

```
1. import { spaceManager } from '@kit.EnterpriseSpaceKit';

3. const workspaceId: number = 100;
4. try {
5. const apps: string[] = await spaceManager.getLockdownExemptionApps(workspaceId);
6. console.info(`Succeeded in getting lockdown exemption apps. apps:` + JSON.stringify(apps));
7. } catch (err) {
8. console.error(`Failed to get lockdown exemption apps. Code: ${err.code}, message: ${err.message}`);
9. }
```

## authenticate

PC/2in1

authenticate(enterpriseAuthInfo: WorkspaceDomainInfo, credential: Uint8Array): Promise<AuthResult>

企业账号认证。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**起始版本：** 6.1.0(23)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enterpriseAuthInfo | [WorkspaceDomainInfo](enterprisespace-spacemanager.md#workspacedomaininfo) | 是 | 工作空间域信息，具体可参见[WorkspaceDomainInfo](enterprisespace-spacemanager.md#workspacedomaininfo)。 |
| credential | Uint8Array | 是 | 企业用户登录凭证。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<AuthResult> | Promise对象，表示企业账号认证结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](enterprisespace-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. |
| 1020400004 | Authentication failed. |
| 1020400008 | Invalid account name or password. |
| 1020400009 | The account is locked. |
| 1020400010 | Enterprise authentication server unreachable. |

**示例：**

```
1. import { spaceManager } from '@kit.EnterpriseSpaceKit';

3. try {
4. const enterpriseAuthInfo: spaceManager.WorkspaceDomainInfo = {
5. domain: 'testDomain',
6. workspaceName: 'testAccountName',
7. serverConfigId: 'testServerConfigId'
8. };
9. const credential = new Uint8Array([0, 0, 0, 0, 0, 0, 0, 0])
10. const authResult: spaceManager.AuthResult = await spaceManager.authenticate(enterpriseAuthInfo, credential);
11. console.info(`Succeeded in authenticating. Auth result is: ` + JSON.stringify(authResult));
12. } catch (err) {
13. console.error(`Failed to authenticate. Code: ${err.code}, message: ${err.message}`);
14. }
```

## getAccessToken

PC/2in1

getAccessToken(businessParams: Record<string, string>): Promise<Uint8Array>

获取企业应用访问令牌。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**起始版本：** 6.1.0(23)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| businessParams | Record<string, string> | 是 | 业务参数，由业务方根据请求协议自定义。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | Promise对象，表示AccessToken。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](enterprisespace-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. |
| 1020400003 | Invalid workspace. |
| 1020400004 | Authentication failed. |
| 1020400010 | Enterprise authentication server unreachable. |

**示例：**

```
1. import { spaceManager } from '@kit.EnterpriseSpaceKit';

3. try {
4. const params: Record<string, string> = {
5. 'clientId': 'test1'
6. };
7. const result: Uint8Array = await spaceManager.getAccessToken(params);
8. console.info(`Succeeded in getting access token. Result is: ` + JSON.stringify(result));
9. } catch (err) {
10. console.error(`Failed to get access token. Code: ${err.code}, message: ${err.message}`);
11. }
```

## setWorkspaceStatusBarIcon

PC/2in1

setWorkspaceStatusBarIcon(statusBarIcon: StatusBarIcon, workspaceId?: number): Promise<void>

根据工作空间ID设置工作空间状态栏图标。使用Promise异步回调。

该接口仅供企业安全管控类MDM应用申请权限后使用，可修改状态栏图标的工作空间受限于当前MDM应用所在工作空间。若MDM应用安装在U0/U1工作空间下，可修改其他工作空间状态栏图标，否则仅能修改当前MDM应用所在工作空间的状态栏图标。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**起始版本：** 6.1.0(23)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| statusBarIcon | [StatusBarIcon](enterprisespace-spacemanager.md#statusbaricon) | 是 | 设置的工作空间的状态栏图标。 |
| workspaceId | number | 否 | 工作空间ID。首个空间ID为100，后续创建的工作空间ID逐一递增，例如101、102。 如果未设置，则默认使用调用者所在的工作空间ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](enterprisespace-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. |
| 1020400003 | Invalid workspace. |

**示例：**

```
1. import { spaceManager } from '@kit.EnterpriseSpaceKit';

3. const context: Context = getContext();
4. if (!context) {
5. console.error('getHostContext failed');
6. return;
7. }
8. const resourceMgr: resourceManager.ResourceManager = context.resourceManager;

10. // 创建white pixelMap，需在资源rawfile文件夹中预置HuaweiWhite.jpg图片
11. let whiteFileData = await resourceMgr.getRawFd('HuaweiWhite.jpg');
12. const whiteImageSource: image.ImageSource = image.createImageSource(whiteFileData);
13. const whitePixelMap: image.PixelMap = await whiteImageSource.createPixelMap();

15. // 创建black pixelMap，需在资源rawfile文件夹中预置HuaweiBlack.jpg图片
16. let blackFileData = await resourceMgr.getRawFd('HuaweiBlack.jpg');
17. const blackImageSource: image.ImageSource = image.createImageSource(blackFileData);
18. const blackPixelMap: image.PixelMap = await blackImageSource.createPixelMap();

20. // 构建图标信息
21. const icons: spaceManager.StatusBarIcon = {
22. white: whitePixelMap,
23. black: blackPixelMap
24. };
25. const workspaceId: number = 100;
26. try {
27. await spaceManager.setWorkspaceStatusBarIcon(icons, workspaceId);
28. console.info(TAG, `Succeeded in setting workspace status bar icon`);
29. } catch (err) {
30. console.error(`Failed to set workspace status bar icon. Code: ${err.code}, message: ${err.message}`);
31. }
```

## setWorkspaceLocalName

PC/2in1

setWorkspaceLocalName(localName: string, workspaceId?: number): Promise<void>

根据工作空间ID设置工作空间本地名称。使用Promise异步回调。

该接口仅供企业安全管控类MDM应用申请权限后使用，可修改本地名称的工作空间受限于当前MDM应用所在工作空间。若MDM应用安装在U0/U1工作空间下，可修改其他工作空间本地名称，否则仅能修改当前MDM应用所在工作空间的本地名称。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES

**系统能力：** SystemCapability.EnterpriseSpace.ServiceManage

**起始版本：** 6.1.0(23)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localName | string | 是 | 设置的工作空间的本地名称。 |
| workspaceId | number | 否 | 工作空间ID。首个空间ID为100，后续创建的工作空间ID逐一递增，例如101、102。 如果未设置，则默认使用调用者所在的工作空间ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](enterprisespace-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 1020400001 | System service exception. |
| 1020400002 | Parameter error. |

**示例：**

```
1. import { spaceManager } from '@kit.EnterpriseSpaceKit';

3. const localName: string = 'localName';
4. const workspaceId: number = 100;
5. try {
6. await spaceManager.setWorkspaceLocalName(localName, workspaceId);
7. console.info('Succeeded in setting workspace local name');
8. } catch (err) {
9. console.error(`Failed to set workspace local name. Code: ${err.code}, message: ${err.message}`);
10. }
```
