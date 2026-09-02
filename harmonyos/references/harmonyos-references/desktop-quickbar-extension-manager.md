---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/desktop-quickbar-extension-manager
title: quickBarManager（快捷栏管理服务）
breadcrumb: API参考 > 系统 > 基础功能 > Desktop Extension Kit（桌面拓展服务） > ArkTS API > quickBarManager（快捷栏管理服务）
category: harmonyos-references
scraped_at: 2026-09-02T14:52:32+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9a2039b1905f63c2567cc6329f3e37255258e1111d9ad3be0df9a4ed6c4b5083
---

本模块为应用提供接入快捷栏能力。应用可以通过接入相应的API，可自定义应用在快捷栏右键菜单。

**起始版本：** 6.0.2(22)

## 导入模块

```typescript
import { quickBarManager } from '@kit.DeskTopExtensionKit';
```

## QuickTaskInfo

快捷栏菜单任务的详细参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.QuickBarManager

**起始版本：** 6.0.2(22)

| **名称** | **类型** | **只读** | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| taskName | string | 否 | 否 | 快捷栏图标菜单任务的任务名称。  字符串长度范围：[1, 512]，且内容不为空。 |
| abilityName | string | 否 | 否 | 点击菜单任务拉起的应用的Ability名称。  字符串长度范围：[1, 512]，且内容不为空。 |
| moduleName | string | 否 | 是 | 点击菜单项任务拉起的应用的Ability所在的模块名称。  字符串长度范围：[1, 512]，且内容不为空。  默认值：''。 |
| taskIcon | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | 是 | 快捷栏图标菜单任务的图片信息，支持JPEG、PNG、GIF、WebP、BMP、SVG、ICO、DNG等图片类型。  默认值：undefined。  **说明：** 建议使用512vp \* 512vp大小的图片，若不传入图片信息，则使用应用图标作为任务图标。 |
| taskDetail | string | 否 | 是 | 快捷栏图标菜单任务的描述信息。  字符串长度范围：[1, 512]，且内容不为空。  默认值：''。 |
| parameters | [ParameterItem](desktop-quickbar-extension-manager.md#parameteritem)[] | 否 | 是 | 快捷栏图标菜单任务的自定义参数。  数组大小范围：小于等于64。  默认值：undefined。 |

## QuickTask

应用的快捷栏菜单任务的信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.QuickBarManager

**起始版本：** 6.0.2(22)

| **名称** | **类型** | **只读** | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| taskId | number | 是 | 否 | 快捷栏图标菜单任务的任务Id。 |
| categoryId | number | 是 | 否 | 快捷栏图标菜单分组的分组Id。 |
| taskInfo | [QuickTaskInfo](desktop-quickbar-extension-manager.md#quicktaskinfo) | 否 | 否 | 接入快捷栏的任务信息。 |

## ParameterItem

快捷栏菜单任务的自定义参数，表示WantParams，由开发者自行决定传入的键值对。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.QuickBarManager

**起始版本：** 6.0.2(22)

| **名称** | **类型** | **只读** | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| key | string | 否 | 否 | 自定义参数的key值。  字符串长度范围：[1, 512]，且内容不为空。 |
| value | string | 否 | 否 | 自定义参数的value值。  字符串长度范围：[1, 512]，且内容不为空。 |

## CustomCategory

应用的快捷栏菜单分组的信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.QuickBarManager

**起始版本：** 6.0.2(22)

| **名称** | **类型** | **只读** | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| categoryId | number | 是 | 否 | 快捷栏图标菜单分组的分组Id。 |
| categoryName | string | 否 | 否 | 快捷栏图标菜单分组的分组名称。  字符串长度范围：[1, 512]，且内容不为空。 |

## QuickBarGroup

快捷栏分组信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.QuickBarManager

**起始版本：** 6.1.0(23)

| **名称** | **类型** | **只读** | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| groupKey | string | 否 | 否 | 快捷栏分组名称。  字符串长度范围：[1, 512]，且内容不为空。 |
| groupIcon | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | 否 | 快捷栏分组图标信息，图标类型支持JPEG、PNG、GIF、WebP、BMP、SVG、ICO、DNG。 |

## quickBarManager.addCustomCategory

addCustomCategory(context: common.Context, categoryName: string): Promise<CustomCategory>

添加快捷栏分组。添加一个分组后才可以往分组里添加任务，最多可以添加三个分组。使用promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.QuickBarManager

**起始版本：** 6.0.2(22)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。 |
| categoryName | string | 是 | 快捷栏图标菜单分组的分组名称。  字符串长度范围：[1, 512]，且内容不为空。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[CustomCategory](desktop-quickbar-extension-manager.md#customcategory)> | Promise对象，返回菜单分组信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-statusbar-extension.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1020210001 | Maximum number of categories reached. |
| 1020210002 | Duplicate category name. |
| 1020210008 | The string length exceeds the threshold. |

**示例：**

```typescript
import { quickBarManager } from '@kit.DeskTopExtensionKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function addCustomCategory(context: Context) {
  if (context === undefined) {
    return;
  }
  try {
    const res = await quickBarManager.addCustomCategory(context, '最近任务');
    console.info(`customCategory info: ${JSON.stringify(res)}`);
  } catch (error) {
    console.error(`addCustomCategory failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

## quickBarManager.addQuickTask

addQuickTask(context: common.Context, categoryId: number, taskInfo: QuickTaskInfo): Promise<QuickTask>

添加快捷栏任务。打开应用图标在快捷栏的右键菜单，即可看到添加后对应的菜单项。使用promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.QuickBarManager

**起始版本：** 6.0.2(22)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。 |
| categoryId | number | 是 | 快捷栏图标菜单分组的分组Id。 |
| taskInfo | [QuickTaskInfo](desktop-quickbar-extension-manager.md#quicktaskinfo) | 是 | 快捷栏图标菜单任务的详细信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[QuickTask](desktop-quickbar-extension-manager.md#quicktask)> | Promise对象，返回菜单任务信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-statusbar-extension.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1020210003 | Category not found. |
| 1020210008 | The string length exceeds the threshold. |
| 1020210009 | Invalid parameter. |

**示例：**

```typescript
import { quickBarManager } from '@kit.DeskTopExtensionKit';
import { resourceManager } from '@kit.LocalizationKit';
import { image } from '@kit.ImageKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function addQuickTask(context: Context) {
  if (context === undefined) {
    return;
  }
  // 获取resourceManager资源管理器
  const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
  // 创建任务的pixelMap，需在资源rawfile文件夹中预置testImage.png图片
  const whiteFileData = resourceMgr.getRawFileContentSync('testImage.png');
  const whiteImageSource = image.createImageSource(whiteFileData.buffer);
  const imagePixelMap = await whiteImageSource.createPixelMap();
  // 构建parameters信息
  let parameters: quickBarManager.ParameterItem = {
    key: 'testKey',
    value: 'testValue'
  }
  // 构建QuickTaskInfo信息
  let task: quickBarManager.QuickTaskInfo = {
    taskName: '测试任务名称',
    abilityName: 'TestAbility1',
    moduleName: 'entry',
    // 参数可选
    taskIcon: imagePixelMap,
    // 参数可选
    taskDetail: '任务的描述',
    parameters: [parameters]
  }
  try {
    // 获取所有的分组信息，将任务添加到想要的分组中
    const categoryList = await quickBarManager.getCustomCategories(context);
    // 选择添加任务到第一个分组中
    let res = await quickBarManager.addQuickTask(context, categoryList[0].categoryId, task);
    console.info(`quickTask info: ${JSON.stringify(res)}`);
  } catch (error) {
    console.error(`addQuickTask failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

## quickBarManager.getCustomCategories

getCustomCategories(context: common.Context): Promise<CustomCategory[]>

获取在快捷栏定义的所有分组。使用promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.QuickBarManager

**起始版本：** 6.0.2(22)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[CustomCategory](desktop-quickbar-extension-manager.md#customcategory)[]> | Promise对象，返回所有菜单分组信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-statusbar-extension.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1020210003 | Category not found. |

**示例：**

```typescript
import { quickBarManager } from '@kit.DeskTopExtensionKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function getCustomCategories(context: Context) {
  if (context === undefined) {
    return;
  }
  try {
    const res = await quickBarManager.getCustomCategories(context);
    console.info(`customCategoryList info: ${JSON.stringify(res)}`);
  } catch (error) {
    console.error(`getCustomCategories failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

## quickBarManager.getTasksFromCategory

getTasksFromCategory(context: common.Context, categoryId: number): Promise<QuickTask[]>

获取某个快捷栏分组下的所有任务信息。使用promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.QuickBarManager

**起始版本：** 6.0.2(22)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。 |
| categoryId | number | 是 | 快捷栏图标菜单分组的分组Id。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[QuickTask](desktop-quickbar-extension-manager.md#quicktask)[]> | Promise对象，返回一个分组下的所有任务信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-statusbar-extension.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1020210003 | Category not found. |
| 1020210004 | Quick task not found. |

**示例：**

```typescript
import { quickBarManager } from '@kit.DeskTopExtensionKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function getTasksFromCategory(context: Context) {
  if (context === undefined) {
    return;
  }
  try {
    // 获取所有的分组信息，用于获取分组下所有的任务
    const category = await quickBarManager.getCustomCategories(context);
    // 选择获取第一个分组下的所有任务
    const res = await quickBarManager.getTasksFromCategory(context, category[0].categoryId)
    console.info(`quickTaskList info: ${JSON.stringify(res)}`);
  } catch (error) {
    console.error(`getTasksFromCategory failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

## quickBarManager.updateCustomCategory

updateCustomCategory(context: common.Context, category: CustomCategory): Promise<void>

更新快捷栏分组。使用promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.QuickBarManager

**起始版本：** 6.0.2(22)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。 |
| category | [CustomCategory](desktop-quickbar-extension-manager.md#customcategory) | 是 | 快捷栏图标的菜单分组信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回值。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-statusbar-extension.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1020210002 | Duplicate category name. |
| 1020210003 | Category not found. |
| 1020210008 | The string length exceeds the threshold. |

**示例：**

```typescript
import { quickBarManager } from '@kit.DeskTopExtensionKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function updateCustomCategory(context: Context) {
  if (context === undefined) {
    return;
  }
  const category: quickBarManager.CustomCategory = {
    categoryId: 1,
    categoryName: 'demo'
  }
  try {
    await quickBarManager.updateCustomCategory(context, category);
  } catch (error) {
    console.error(`updateCustomCategory failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

## quickBarManager.updateQuickTask

updateQuickTask(context: common.Context, task: QuickTask): Promise<void>

更新快捷栏任务。使用promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.QuickBarManager

**起始版本：** 6.0.2(22)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。 |
| task | [QuickTask](desktop-quickbar-extension-manager.md#quicktask) | 是 | 快捷栏图标的菜单任务信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回值。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-statusbar-extension.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1020210004 | Quick task not found. |
| 1020210008 | The string length exceeds the threshold. |
| 1020210009 | Invalid parameter. |

**示例：**

```typescript
import { quickBarManager } from '@kit.DeskTopExtensionKit';
import { resourceManager } from '@kit.LocalizationKit';
import { image } from '@kit.ImageKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function updateQuickTask(context: Context) {
  if (context === undefined) {
    return;
  }
  // 获取resourceManager资源管理器
  const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
  // 创建任务的pixelMap，需在资源rawfile文件夹中预置testUpdateImage.png图片
  const fileData = resourceMgr.getRawFileContentSync('testUpdateImage.png');
  const imageSource = image.createImageSource(fileData.buffer);
  const imagePixelMap = await imageSource.createPixelMap();
  // 构建parameters
  let parameters: quickBarManager.ParameterItem = {
    key: 'testKey',
    value: 'testValue'
  }
  let taskInfo: quickBarManager.QuickTaskInfo = {
    taskName: 'newTaskName',
    abilityName: 'newEntryAbility',
    moduleName: 'newModuleName',
    // 参数可选
    taskIcon: imagePixelMap,
    // 参数可选
    taskDetail: '任务的描述',
    // 参数可选
    parameters: [parameters]
  }

  const task: quickBarManager.QuickTask = {
    taskId: 1,
    categoryId: 1,
    taskInfo: taskInfo
  }

  try {
    await quickBarManager.updateQuickTask(context,task);
  } catch (error) {
    console.error(`updateQuickTask failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

## quickBarManager.deleteQuickTask

deleteQuickTask(context: common.Context, taskId: number): Promise<void>

删除快捷栏任务。使用promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.QuickBarManager

**起始版本：** 6.0.2(22)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。 |
| taskId | number | 是 | 快捷栏图标的菜单任务的Id。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回值。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-statusbar-extension.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1020210004 | Quick task not found. |

**示例：**

```typescript
import { quickBarManager } from '@kit.DeskTopExtensionKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function deleteQuickTask(context: Context) {
  if (context === undefined) {
    return;
  }
  try {
    // 删除任务id为1的任务
    await quickBarManager.deleteQuickTask(context, 1);
  } catch (error) {
    console.error(`deleteQuickTask failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

## quickBarManager.deleteCustomCategory

deleteCustomCategory(context: common.Context, categoryId: number): Promise<void>

删除快捷栏分组，其下的所有任务也会随着一起删除。使用promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.QuickBarManager

**起始版本：** 6.0.2(22)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。 |
| categoryId | number | 是 | 快捷栏图标菜单分组的分组Id。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回值。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-statusbar-extension.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1020210003 | Category not found. |

**示例：**

```typescript
import { quickBarManager } from '@kit.DeskTopExtensionKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function deleteCustomCategory(context: Context) {
  if (context === undefined) {
    return;
  }
  try {
    // 删除分组id为1的分组
    await quickBarManager.deleteCustomCategory(context, 1);
  } catch (error) {
    console.error(`deleteCustomCategory failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

## quickBarManager.addQuickBarGroup

addQuickBarGroup(context: common.Context, group: QuickBarGroup): Promise<void>

增加快捷栏分组。增加分组后才能设置分组的窗口信息。使用promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.QuickBarManager

**起始版本：** 6.1.0(23)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。 |
| group | [QuickBarGroup](desktop-quickbar-extension-manager.md#quickbargroup) | 是 | 快捷栏分组信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回值。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-statusbar-extension.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1020210005 | Group already exists. |
| 1020210008 | The string length exceeds the threshold. |

**示例：**

```typescript
import { quickBarManager } from '@kit.DeskTopExtensionKit';
import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';

// 获取资源管理器
const context: Context | undefined = this.getUIContext().getHostContext();
if (!context) {
  console.error('context is null');
  return;
}
const resourceMgr: resourceManager.ResourceManager = context!.resourceManager;

// 从rawfile目录中获取图片
const whiteFileData = resourceMgr.getRawFileContentSync('icon.png');
const whiteImageSource = image.createImageSource(whiteFileData.buffer);
const imagePixelMap = await whiteImageSource.createPixelMap();
try {
  // 增加分组
  await quickBarManager.addQuickBarGroup(context, {
    groupKey: 'group_one', // 分组名
    groupIcon: imagePixelMap // 分组图标
  });
} catch (error) {
  console.error(`error code: ${error.code}, error message: ${error.message}`);
}
```

## quickBarManager.deleteQuickBarGroup

deleteQuickBarGroup(context: common.Context, groupKey: string): Promise<void>

删除快捷栏分组。使用promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.QuickBarManager

**起始版本：** 6.1.0(23)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。 |
| groupKey | string | 是 | 分组名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回值。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-statusbar-extension.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1020210006 | Group not found. |

**示例：**

```typescript
import { quickBarManager } from '@kit.DeskTopExtensionKit';

const context: Context | undefined = this.getUIContext().getHostContext();
if (!context) {
  console.error('context is null');
  return;
}

try {
  // 删除分组名为group_one的分组
  await quickBarManager.deleteQuickBarGroup(context, 'group_one');
} catch (error) {
  console.error(`error code: ${error.code}, error message: ${error.message}`);
}
```

## quickBarManager.getQuickBarGroups

getQuickBarGroups(context: common.Context): Promise<QuickBarGroup[]>

获取所有分组信息。使用promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.QuickBarManager

**起始版本：** 6.1.0(23)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[QuickBarGroup](desktop-quickbar-extension-manager.md#quickbargroup)[]> | Promise对象，返回所有分组信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-statusbar-extension.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1020210006 | Group not found. |

**示例：**

```typescript
import { quickBarManager } from '@kit.DeskTopExtensionKit';

const context: Context | undefined = this.getUIContext().getHostContext();
if (!context) {
  console.error('context is null');
  return;
}

try {
  // 获取所有分组
  const groups = await quickBarManager.getQuickBarGroups(context);
} catch (error) {
  console.error(`error code: ${error.code}, error message: ${error.message}`);
}
```

## quickBarManager.setWindowToGroup

setWindowToGroup(context: common.Context, windowid: string, groupKey?: string): Promise<void>

设置分组的窗口信息。使用promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.QuickBarManager

**起始版本：** 6.1.0(23)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。 |
| windowid | string | 是 | 窗口id。 |
| groupKey | string | 否 | 分组名称。缺省时，窗口将从分组中删除，此窗口不属于任何分组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回值。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-statusbar-extension.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1020210006 | Group not found. |
| 1020210007 | Window not found. |

**示例：**

```typescript
import { quickBarManager } from '@kit.DeskTopExtensionKit';

const context: Context | undefined = this.getUIContext().getHostContext();
if (!context) {
  console.error('context is null');
  return;
}

try {
  // 将id为80的窗口，增加到分组名为 group_one 的分组
  await quickBarManager.setWindowToGroup(context, '80', 'group_one');
} catch (error) {
  console.error(`setWindowToGroup failed. error code: ${error.code}, error message: ${error.message}`);
}
```

## ProgressState

快捷栏进度状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.QuickBarManager

**起始版本：** 26.0.0

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NO\_PROGRESS | 0 | 无进度状态。 |
| NORMAL | 1 | 正常状态。 |
| PAUSED | 2 | 暂停状态。 |
| ERROR | 3 | 错误状态。 |

## quickBarManager.setQuickBarCombineIcon

setQuickBarCombineIcon(context: common.Context, combineIcon: image.PixelMap): Promise<void>

设置快捷栏融合图标。使用promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.SET\_ABILITY\_INSTANCE\_INFO

**系统能力：** SystemCapability.PCService.QuickBarManager

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。 |
| combineIcon | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 快捷栏图标信息，支持JPEG、PNG、GIF、WebP、BMP、SVG、ICO、DNG等图片类型。  **说明：** 建议使用512vp \* 512vp大小的图片。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-statusbar-extension.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 1020210009 | Invalid parameter. |
| 1020210010 | Quick bar icon not found. |
| 1020210011 | The API is called too frequently. |

**示例：**

```typescript
import { quickBarManager } from '@kit.DeskTopExtensionKit';
import { resourceManager } from '@kit.LocalizationKit';
import { image } from '@kit.ImageKit';

const context: Context | undefined = this.getUIContext().getHostContext();
if (context === undefined) {
  return;
}
// 获取resourceManager资源管理器
const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
// 创建图标的pixelMap，需在资源rawfile文件夹中预置icon.png图片
const fileData = resourceMgr.getRawFileContentSync('icon.png');
const imageSource = image.createImageSource(fileData.buffer);
const imagePixelMap = await imageSource.createPixelMap();

try {
  await quickBarManager.setQuickBarCombineIcon(context, imagePixelMap);
  console.info('setQuickBarCombineIcon success');
} catch (error) {
  console.error(`setQuickBarCombineIcon failed. error code: ${error.code}, error message: ${error.message}`);
}
```

## quickBarManager.setQuickBarLayeredIcon

setQuickBarLayeredIcon(context: common.Context, foregroundIcon: image.PixelMap, backgroundIcon: image.PixelMap): Promise<void>

设置快捷栏分层图标。使用promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.SET\_ABILITY\_INSTANCE\_INFO

**系统能力：** SystemCapability.PCService.QuickBarManager

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。 |
| foregroundIcon | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 快捷栏前景图标信息，支持JPEG、PNG、GIF、WebP、BMP、SVG、ICO、DNG等图片类型。  **说明：** 建议使用512vp \* 512vp大小的图片。 |
| backgroundIcon | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 快捷栏背景图标信息，支持JPEG、PNG、GIF、WebP、BMP、SVG、ICO、DNG等图片类型。  **说明：** 建议使用512vp \* 512vp大小的图片。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-statusbar-extension.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 1020210009 | Invalid parameter. |
| 1020210010 | Quick bar icon not found. |
| 1020210011 | The API is called too frequently. |

**示例：**

```typescript
import { quickBarManager } from '@kit.DeskTopExtensionKit';
import { resourceManager } from '@kit.LocalizationKit';
import { image } from '@kit.ImageKit';

const context: Context | undefined = this.getUIContext().getHostContext();
if (context === undefined) {
  return;
}
// 获取resourceManager资源管理器
const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
// 创建前景图的pixelMap，需在资源rawfile文件夹中预置foreground.png图片
const foregroundFileData = resourceMgr.getRawFileContentSync('foreground.png');
const foregroundImageSource = image.createImageSource(foregroundFileData.buffer);
const foregroundPixelMap = await foregroundImageSource.createPixelMap();

// 创建背景图的pixelMap，需在资源rawfile文件夹中预置background.png图片
const backgroundFileData = resourceMgr.getRawFileContentSync('background.png');
const backgroundImageSource = image.createImageSource(backgroundFileData.buffer);
const backgroundPixelMap = await backgroundImageSource.createPixelMap();

try {
  await quickBarManager.setQuickBarLayeredIcon(context, foregroundPixelMap, backgroundPixelMap);
  console.info('setQuickBarLayeredIcon success');
} catch (error) {
  console.error(`setQuickBarLayeredIcon failed. error code: ${error.code}, error message: ${error.message}`);
}
```

## quickBarManager.setProgressState

setProgressState(context: common.Context, state: ProgressState): Promise<void>

在快捷栏图标上设置进度条状态。使用promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.SET\_ABILITY\_INSTANCE\_INFO

**系统能力：** SystemCapability.PCService.QuickBarManager

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。 |
| state | [ProgressState](desktop-quickbar-extension-manager.md#progressstate) | 是 | 快捷栏图标上显示的进度状态。  取值范围如下：  - NO\_PROGRESS (0)：无进度状态。  - NORMAL (1)：正常状态。  - PAUSED (2)：暂停状态。  - ERROR (3)：错误状态。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-statusbar-extension.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 1020210009 | Invalid parameter. |
| 1020210010 | Quick bar icon not found. |
| 1020210011 | The API is called too frequently. |

**示例：**

```typescript
import { quickBarManager } from '@kit.DeskTopExtensionKit';

const context: Context | undefined = this.getUIContext().getHostContext();
if (context === undefined) {
  return;
}

try {
  // 设置进度状态为NORMAL
  await quickBarManager.setProgressState(context, quickBarManager.ProgressState.NORMAL);
  console.info('setProgressState success');
} catch (error) {
  console.error(`setProgressState failed. error code: ${error.code}, error message: ${error.message}`);
}
```

## quickBarManager.setProgressValue

setProgressValue(context: common.Context, completed: number, total: number): Promise<void>

在快捷栏图标上设置进度条。使用promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.SET\_ABILITY\_INSTANCE\_INFO

**系统能力：** SystemCapability.PCService.QuickBarManager

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。 |
| completed | number | 是 | 已完成的进度值。  取值范围：[0, 100]，且小于等于total的值。 |
| total | number | 是 | 总进度值。  取值范围：(0, 100]，且大于等于completed的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-statusbar-extension.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 1020210009 | Invalid parameter. |
| 1020210010 | Quick bar icon not found. |
| 1020210011 | The API is called too frequently. |

**示例：**

```typescript
import { quickBarManager } from '@kit.DeskTopExtensionKit';

const context: Context | undefined = this.getUIContext().getHostContext();
if (context === undefined) {
  return;
}

const completed: number = 50;
const total: number = 100;

try {
  await quickBarManager.setProgressValue(context, completed, total);
  console.info('setProgressValue success');
} catch (error) {
  console.error(`setProgressValue failed. error code: ${error.code}, error message: ${error.message}`);
}
```

## quickBarManager.isQuickBarCapabilitySupported

isQuickBarCapabilitySupported(context: common.Context): Promise<boolean>

检查是否支持快捷栏功能。使用promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.QuickBarManager

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回**true**表示支持快捷栏功能，返回**false**表示不支持。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-statusbar-extension.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1020210011 | The API is called too frequently. |

**示例：**

```typescript
import { quickBarManager } from '@kit.DeskTopExtensionKit';

const context: Context | undefined = this.getUIContext().getHostContext();
if (context === undefined) {
  return;
}

try {
  const isSupported: boolean = await quickBarManager.isQuickBarCapabilitySupported(context);
  console.info(`isQuickBarCapabilitySupported result: ${isSupported}`);
} catch (error) {
  console.error(`isQuickBarCapabilitySupported failed. error code: ${error.code}, error message: ${error.message}`);
}
```
