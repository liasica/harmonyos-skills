---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/filemanagerservice-arkts-extensionability
title: "@hms.filemanagement.FileManagerExtensionAbility (文件管理扩展能力)"
breadcrumb: API参考 > 应用服务 > File Manager Service Kit（文件管理服务） > ArkTS API > @hms.filemanagement.FileManagerExtensionAbility (文件管理扩展能力)
category: harmonyos-references
scraped_at: 2026-11-12T09:57:15+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:5b876760e8eb97ee10b4ed8e2d291399799cf8cc68c017e6382b304ac33b1d59
---

FileManagerExtensionAbility提供以下能力：在打开文件管理应用进入文件目录时，展示三方应用自定义的动态文件角标；在文件管理应用内单击右键时，展示三方应用自定义菜单。继承自[ExtensionAbility](../doccenter-references/api/js-apis-app-ability-extensionability.md)

**起始版本：** 26.0.1

## 导入模块

```typescript
import { FileManagerExtensionAbility } from '@kit.FileManagerServiceKit';
```

## 属性

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.FileManagement.FileManagerService.Extension

**起始版本：** 26.0.1

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [FileManagerExtensionContext](filemanagerservice-arkts-extensioncontext.md) | 否 | 否 | FileManagerExtensionAbility上下文环境，继承自ExtensionContext。 |

## onCreate

onCreate(want: Want): void

FileManagerExtensionAbility创建时回调。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.FileManagement.FileManagerService.Extension

**起始版本：** 26.0.1

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 创建Extension的Want信息。 |

**示例：**

```typescript
import { fileManagerService } from '@kit.FileManagerServiceKit';
import { FileManagerExtensionAbility } from '@kit.FileManagerServiceKit';

export default class MyExtensionAbility extends FileManagerExtensionAbility {

    onCreate(want: Want): void {
        console.info("MyExtensionAbility onCreate");
    }
}
```

## onDestroy

onDestroy(): void

FileManagerExtensionAbility销毁前回调。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.FileManagement.FileManagerService.Extension

**起始版本：** 26.0.1

**示例：**

```typescript
import { fileManagerService } from '@kit.FileManagerServiceKit';
import { FileManagerExtensionAbility } from '@kit.FileManagerServiceKit';

export default class MyExtensionAbility extends FileManagerExtensionAbility {

  onDestroy(): void {
    console.info("MyExtensionAbility onDestroy");
  }
}
```

## onObserveDir

onObserveDir(params: ObserveDirectoryParams): void

文件管理应用进入指定目录时回调。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.FileManagement.FileManagerService.Extension

**起始版本：** 26.0.1

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [ObserveDirectoryParams](filemanagerservice-arkts-filemanagerservice.md#observedirectoryparams) | 是 | 进入目录参数，接收到用户打开文件目录。 |

**示例：**

```typescript
import { fileManagerService } from '@kit.FileManagerServiceKit';
import { FileManagerExtensionAbility } from '@kit.FileManagerServiceKit';

export default class MyExtensionAbility extends FileManagerExtensionAbility {

  onObserveDir(params: fileManagerService.ObserveDirectoryParams): void {
    console.info("MyExtensionAbility onObserveDir, param = " + JSON.stringify(params));
  }
}
```

## onStopObservingDir

onStopObservingDir(params: ObserveDirectoryParams): void

文件管理应用离开指定目录时回调。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.FileManagement.FileManagerService.Extension

**起始版本：** 26.0.1

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [ObserveDirectoryParams](filemanagerservice-arkts-filemanagerservice.md#observedirectoryparams) | 是 | 离开目录参数，接收到用户离开文件目录。 |

**示例：**

```typescript
import { fileManagerService } from '@kit.FileManagerServiceKit';
import { FileManagerExtensionAbility } from '@kit.FileManagerServiceKit';

export default class MyExtensionAbility extends FileManagerExtensionAbility {

  onStopObservingDir(params: fileManagerService.ObserveDirectoryParams): void {
    console.info("MyExtensionAbility onStopObservingDir, param = " + JSON.stringify(params));
  }
}
```

## onQueryBadges

onQueryBadges(params: QueryBadgesParams): Promise<QueryBadgesResult>

文件管理应用查询指定目录下文件的角标。文件管理器进入目录或刷新文件角标时回调，开发者在此回调中返回需要刷新的文件角标信息。使用Promise异步回调。

**说明** 

文件角标显示按应用安装顺序决策，仅问询当前设备上先安装的前15个注册文件扩展能力的应用；若同文件目录被多个文件扩展监听，则按此顺序查询，只显示第一个文件扩展类型应用isMemberOf为true的角标。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.FileManagement.FileManagerService.Extension

**起始版本：** 26.0.1

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [QueryBadgesParams](filemanagerservice-arkts-filemanagerservice.md#querybadgesparams) | 是 | 角标查询参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[QueryBadgesResult](filemanagerservice-arkts-filemanagerservice.md#querybadgesresult)> | Promise对象，返回角标查询结果。 |

**示例：**

```typescript
import { fileManagerService } from '@kit.FileManagerServiceKit';
import { FileManagerExtensionAbility } from '@kit.FileManagerServiceKit';

export default class MyExtensionAbility extends FileManagerExtensionAbility {

  onQueryBadges(params: fileManagerService.QueryBadgesParams): Promise<fileManagerService.QueryBadgesResult> {
    console.info("MyExtensionAbility onQueryBadges");
    const badges: fileManagerService.FileBadge[] = [];
    badges.push({ uri: "file://docs/storage/Users/currentUser/Documents/example.txt", icon: String($r('app.media.add').id) });
    badges.push({ uri: "file://docs/storage/Users/currentUser/Documents/readme.txt", icon: String($r('app.media.add').id) });
    const result: fileManagerService.QueryBadgesResult = { isMemberOf: true, badges };
    return Promise.resolve(result);
  }
}
```

## onQueryMenu

onQueryMenu(params: QueryMenuParams): Promise<MenuConfig[]>

右键单击菜单时查询扩展菜单配置。用户进入文件管理应用目录或桌面使用右键时调用，限制最多3级菜单。使用Promise异步回调。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.FileManagement.FileManagerService.Extension

**起始版本：** 26.0.1

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [QueryMenuParams](filemanagerservice-arkts-filemanagerservice.md#querymenuparams) | 是 | 菜单查询参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[MenuConfig](filemanagerservice-arkts-filemanagerservice.md#menuconfig)[]> | Promise对象，返回菜单配置列表。如果返回空数组，表示用户未选择文件。 |

**示例：**

```typescript
import { fileManagerService } from '@kit.FileManagerServiceKit';
import { FileManagerExtensionAbility } from '@kit.FileManagerServiceKit';

export default class MyExtensionAbility extends FileManagerExtensionAbility {

  onQueryMenu(params: fileManagerService.QueryMenuParams): Promise<fileManagerService.MenuConfig[]> {
    console.info("MyExtensionAbility onQueryMenu");
    let menu :fileManagerService.MenuConfig = {
      icon: String($r('app.media.add').id),
      description: "新建",
      menuId: 1,
      submenu: [],
    }
    return Promise.resolve([menu]);
  }
}
```

## onMenuAction

onMenuAction(params: MenuActionParams): Promise<void>

菜单项点击处理。当用户点击菜单时，选择应用FileManagerExtensionAbility进行点击后的动作。FileManagerExtensionAbility收到回调后可执行自定义动作。使用Promise异步回调。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.FileManagement.FileManagerService.Extension

**起始版本：** 26.0.1

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [MenuActionParams](filemanagerservice-arkts-filemanagerservice.md#menuactionparams) | 是 | 菜单点击参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```typescript
import { fileManagerService } from '@kit.FileManagerServiceKit';
import { FileManagerExtensionAbility } from '@kit.FileManagerServiceKit';

export default class MyExtensionAbility extends FileManagerExtensionAbility {

  onMenuAction(params: fileManagerService.MenuActionParams): Promise<void> {
    console.info("MyExtensionAbility onMenuAction");
    return Promise.resolve();
  }
}
```

## notifyBadgeChange

notifyBadgeChange(params: BadgeChangeNotify): void

推送角标变更至文件管理器。当文件角标发生变化（如文件状态更新）时调用，单次推送的数据量限制为200kb。文件管理器会监听指定目录下角标信息。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.FileManagement.FileManagerService.Extension

**起始版本：** 26.0.1

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [BadgeChangeNotify](filemanagerservice-arkts-filemanagerservice.md#badgechangenotify) | 是 | 角标变更通知参数。 |

**示例：**

```typescript
import { fileManagerService } from '@kit.FileManagerServiceKit';
import { FileManagerExtensionAbility } from '@kit.FileManagerServiceKit';

export default class MyExtensionAbility extends FileManagerExtensionAbility {

  // 开发者实现自定义方法决定通知文件管理需要更新文件角标
  sendFileStateChangeMsg() {
    this.notifyBadgeChange({
      badges: [
        { uri: 'file://docs/storage/Users/currentUser/Documents/example.txt', icon: String($r('app.media.add').id) }
      ]
    });
  }
}
```
