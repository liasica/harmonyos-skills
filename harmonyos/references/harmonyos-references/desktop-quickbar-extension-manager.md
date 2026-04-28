---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/desktop-quickbar-extension-manager
title: quickBarManager（快捷栏管理服务）
breadcrumb: API参考 > 系统 > 基础功能 > Desktop Extension Kit（桌面拓展服务） > ArkTS API > quickBarManager（快捷栏管理服务）
category: harmonyos-references
scraped_at: 2026-04-28T08:10:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4ae80df3d1b5e5fd0f5bcb36504c816b99ebbf7a767f1cbee93d91993806c74a
---

本模块为应用提供接入快捷栏能力。应用可以通过接入相应的API，可自定义应用在快捷栏右键菜单。

**起始版本：** 6.0.2(22)

## 导入模块

PC/2in1

```
1. import { quickBarManager } from '@kit.DeskTopExtensionKit';
```

## quickBarManager.QuickTaskInfo

PC/2in1

快捷栏菜单任务的详细参数。

**系统能力：** SystemCapability.PCService.QuickBarManager

**起始版本：** 6.0.2(22)

| **名称** | **类型** | **只读** | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| taskName | string | 否 | 否 | 快捷栏图标菜单任务的任务名称。  字符串长度范围：[1, 512]，且内容不为空。 |
| abilityName | string | 否 | 否 | 点击菜单任务拉起的应用的Ability名称。  字符串长度范围：[1, 512]，且内容不为空。 |
| moduleName | string | 否 | 是 | 点击菜单项任务拉起的应用的Ability所在的模块名称。  字符串长度范围：[1, 512]，且内容不为空。  默认值：''。 |
| taskIcon | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | 是 | 快捷栏图标菜单任务的图片信息，支持JPEG、PNG、GIF、WebP、BMP、SVG、ICO、DNG等图片类型。  默认值：undefined。  **说明：** 建议使用512vp \* 512vp大小的图片，若不传入图片信息，则使用应用图标作为任务图标。 |
| taskDetail | string | 否 | 是 | 快捷栏图标菜单任务的描述信息。  默认值：''。 |
| parameters | [ParameterItem](desktop-quickbar-extension-manager.md#quickbarmanagerparameteritem)[] | 否 | 是 | 快捷栏图标菜单任务的自定义参数。  数组大小范围：小于等于64。  默认值：undefined。 |

## quickBarManager.QuickTask

PC/2in1

应用的快捷栏菜单任务的信息。

**系统能力：** SystemCapability.PCService.QuickBarManager

**起始版本：** 6.0.2(22)

| **名称** | **类型** | **只读** | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| taskId | number | 是 | 否 | 快捷栏图标菜单任务的任务Id。 |
| categoryId | number | 是 | 否 | 快捷栏图标菜单分组的分组Id。 |
| taskInfo | [QuickTaskInfo](desktop-quickbar-extension-manager.md#quickbarmanagerquicktaskinfo) | 否 | 否 | 接入快捷栏的任务信息。 |

## quickBarManager.ParameterItem

PC/2in1

快捷栏菜单任务的自定义参数，表示WantParams，由开发者自行决定传入的键值对。

**系统能力：** SystemCapability.PCService.QuickBarManager

**起始版本：** 6.0.2(22)

| **名称** | **类型** | **只读** | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| key | string | 否 | 否 | 自定义参数的key值。  字符串长度范围：[1, 512]，且内容不为空。 |
| value | string | 否 | 否 | 自定义参数的value值。  字符串长度范围：[1, 512]，且内容不为空。 |

## quickBarManager.CustomCategory

PC/2in1

应用的快捷栏菜单分组的信息。

**系统能力：** SystemCapability.PCService.QuickBarManager

**起始版本：** 6.0.2(22)

| **名称** | **类型** | **只读** | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| categoryId | number | 是 | 否 | 快捷栏图标菜单分组的分组Id。 |
| categoryName | string | 否 | 否 | 快捷栏图标菜单分组的分组名称。  字符串长度范围：[1, 512]，且内容不为空。 |

## quickBarManager.QuickBarGroup

PC/2in1

快捷栏分组信息。

**系统能力：** SystemCapability.PCService.QuickBarManager

**起始版本：** 6.1.0(23)

| **名称** | **类型** | **只读** | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| groupKey | string | 否 | 否 | 快捷栏分组名称。  字符串长度范围：[1, 512]，且内容不为空。 |
| groupIcon | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | 否 | 快捷栏分组图标信息，图标类型支持JPEG、PNG、GIF、WebP、BMP、SVG、ICO、DNG。 |

## quickBarManager.addCustomCategory

PC/2in1

addCustomCategory(context: common.Context, categoryName: string): Promise<CustomCategory>

添加快捷栏分组。添加一个分组后才可以往分组里添加任务，最多可以添加三个分组。

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
| Promise<[CustomCategory](desktop-quickbar-extension-manager.md#quickbarmanagercustomcategory)> | Promise对象，返回菜单分组信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](statusbar-extension-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1020210001 | Maximum number of categories reached. |
| 1020210002 | Duplicate category name. |
| 1020210008 | The string length exceeds the threshold. |

**示例：**

```
1. import { quickBarManager } from '@kit.DeskTopExtensionKit';

3. /**
4. * 可以通过自定义组件的内置方法获取Context信息
5. * 具体方法：this.getUIContext().getHostContext();
6. */
7. async function addCustomCategory(context: Context) {
8. if (context === undefined) {
9. return;
10. }
11. try {
12. const res = await quickBarManager.addCustomCategory(context, '最近任务');
13. console.info(`customCategory info: ${JSON.stringify(res)}`);
14. } catch (error) {
15. console.error(`addCustomCategory failed. error code: ${error.code}, error message: ${error.message}`);
16. }
17. }
```

## quickBarManager.addQuickTask

PC/2in1

addQuickTask(context: common.Context, categoryId: number, taskInfo: QuickTaskInfo): Promise<QuickTask>

添加快捷栏任务。打开应用图标在快捷栏的右键菜单，即可看到添加后对应的菜单项。

**系统能力：** SystemCapability.PCService.QuickBarManager

**起始版本：** 6.0.2(22)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。 |
| categoryId | number | 是 | 快捷栏图标菜单分组的分组Id。 |
| taskInfo | [QuickTaskInfo](desktop-quickbar-extension-manager.md#quickbarmanagerquicktaskinfo) | 是 | 快捷栏图标菜单任务的详细信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[QuickTask](desktop-quickbar-extension-manager.md#quickbarmanagerquicktask)> | Promise对象，返回菜单任务信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](statusbar-extension-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1020210003 | Category not found. |
| 1020210008 | The string length exceeds the threshold. |
| 1020210009 | Invalid parameter. |

**示例：**

```
1. import { quickBarManager } from '@kit.DeskTopExtensionKit';
2. import { resourceManager } from '@kit.LocalizationKit';
3. import { image } from '@kit.ImageKit';

5. /**
6. * 可以通过自定义组件的内置方法获取Context信息
7. * 具体方法：this.getUIContext().getHostContext();
8. */
9. async function addQuickTask(context: Context) {
10. if (context === undefined) {
11. return;
12. }
13. // 获取resourceManager资源管理器
14. const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
15. // 创建任务的pixelMap，需在资源rawfile文件夹中预置testImage.png图片
16. const whiteFileData = resourceMgr.getRawFileContentSync('testImage.png');
17. const whiteImageSource = image.createImageSource(whiteFileData.buffer);
18. const imagePixelMap = await whiteImageSource.createPixelMap();
19. // 构建parameters信息
20. let parameters: quickBarManager.ParameterItem = {
21. key: 'testKey',
22. value: 'testValue'
23. }
24. // 构建QuickTaskInfo信息
25. let task: quickBarManager.QuickTaskInfo = {
26. taskName: '测试任务名称',
27. abilityName: 'TestAbility1',
28. moduleName: 'entry',
29. // 参数可选
30. taskIcon: imagePixelMap,
31. // 参数可选
32. taskDetail: '任务的描述',
33. parameters: [parameters]
34. }
35. try {
36. // 获取所有的分组信息，将任务添加到想要的分组中
37. const categoryList = await quickBarManager.getCustomCategories(context);
38. // 选择添加任务到第一个分组中
39. let res = await quickBarManager.addQuickTask(context, categoryList[0].categoryId, task);
40. console.info(`quickTask info: ${JSON.stringify(res)}`);
41. } catch (error) {
42. console.error(`addQuickTask failed. error code: ${error.code}, error message: ${error.message}`);
43. }
44. }
```

## quickBarManager.getCustomCategories

PC/2in1

getCustomCategories(context: common.Context): Promise<CustomCategory[]>

获取在快捷栏定义的所有分组。

**系统能力：** SystemCapability.PCService.QuickBarManager

**起始版本：** 6.0.2(22)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[CustomCategory](desktop-quickbar-extension-manager.md#quickbarmanagercustomcategory)[]> | Promise对象，返回所有菜单分组信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](statusbar-extension-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1020210003 | Category not found. |

**示例：**

```
1. import { quickBarManager } from '@kit.DeskTopExtensionKit';

3. /**
4. * 可以通过自定义组件的内置方法获取Context信息
5. * 具体方法：this.getUIContext().getHostContext();
6. */
7. async function getCustomCategories(context: Context) {
8. if (context === undefined) {
9. return;
10. }
11. try {
12. const res = await quickBarManager.getCustomCategories(context);
13. console.info(`customCategoryList info: ${JSON.stringify(res)}`);
14. } catch (error) {
15. console.error(`getCustomCategories failed. error code: ${error.code}, error message: ${error.message}`);
16. }
17. }
```

## quickBarManager.getTasksFromCategory

PC/2in1

getTasksFromCategory(context: common.Context, categoryId: number): Promise<QuickTask[]>

获取某个快捷栏分组下的所有任务信息。

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
| Promise<[QuickTask](desktop-quickbar-extension-manager.md#quickbarmanagerquicktask)[]> | Promise对象，返回一个分组下的所有任务信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](statusbar-extension-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1020210003 | Category not found. |
| 1020210004 | Quick task not found. |

**示例：**

```
1. import { quickBarManager } from '@kit.DeskTopExtensionKit';

3. /**
4. * 可以通过自定义组件的内置方法获取Context信息
5. * 具体方法：this.getUIContext().getHostContext();
6. */
7. async function getTasksFromCategory(context: Context) {
8. if (context === undefined) {
9. return;
10. }
11. try {
12. // 获取所有的分组信息，用于获取分组下所有的任务
13. const category = await quickBarManager.getCustomCategories(context);
14. // 选择获取第一个分组下的所有任务
15. const res = await quickBarManager.getTasksFromCategory(context, category[0].categoryId)
16. console.info(`quickTaskList info: ${JSON.stringify(res)}`);
17. } catch (error) {
18. console.error(`getTasksFromCategory failed. error code: ${error.code}, error message: ${error.message}`);
19. }
20. }
```

## quickBarManager.updateCustomCategory

PC/2in1

updateCustomCategory(context: common.Context, category: CustomCategory): Promise<void>

更新快捷栏分组。

**系统能力：** SystemCapability.PCService.QuickBarManager

**起始版本：** 6.0.2(22)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。 |
| category | [CustomCategory](desktop-quickbar-extension-manager.md#quickbarmanagercustomcategory) | 是 | 快捷栏图标的菜单分组信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](statusbar-extension-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1020210002 | Duplicate category name. |
| 1020210003 | Category not found. |
| 1020210008 | The string length exceeds the threshold |

**示例：**

```
1. import { quickBarManager } from '@kit.DeskTopExtensionKit';

3. /**
4. * 可以通过自定义组件的内置方法获取Context信息
5. * 具体方法：this.getUIContext().getHostContext();
6. */
7. async function updateCustomCategory(context: Context) {
8. if (context === undefined) {
9. return;
10. }
11. const category: quickBarManager.CustomCategory = {
12. categoryId: 1,
13. categoryName: 'demo'
14. }
15. try {
16. await quickBarManager.updateCustomCategory(context, category);
17. } catch (error) {
18. console.error(`updateCustomCategory failed. error code: ${error.code}, error message: ${error.message}`);
19. }
20. }
```

## quickBarManager.updateQuickTask

PC/2in1

updateQuickTask(context: common.Context, task: QuickTask): Promise<void>

更新快捷栏任务。

**系统能力：** SystemCapability.PCService.QuickBarManager

**起始版本：** 6.0.2(22)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。 |
| task | [QuickTask](desktop-quickbar-extension-manager.md#quickbarmanagerquicktask) | 是 | 快捷栏图标的菜单任务信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](statusbar-extension-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1020210004 | Quick task not found. |
| 1020210008 | The string length exceeds the threshold |
| 1020210009 | Invalid parameter. |

**示例：**

```
1. import { quickBarManager } from '@kit.DeskTopExtensionKit';
2. import { resourceManager } from '@kit.LocalizationKit';
3. import { image } from '@kit.ImageKit';

5. /**
6. * 可以通过自定义组件的内置方法获取Context信息
7. * 具体方法：this.getUIContext().getHostContext();
8. */
9. async function updateQuickTask(context: Context) {
10. if (context === undefined) {
11. return;
12. }
13. // 获取resourceManager资源管理器
14. const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
15. // 创建任务的pixelMap，需在资源rawfile文件夹中预置testUpdateImage.png图片
16. const fileData = resourceMgr.getRawFileContentSync('testUpdateImage.png');
17. const imageSource = image.createImageSource(fileData.buffer);
18. const imagePixelMap = await imageSource.createPixelMap();
19. // 构建parameters
20. let parameters: quickBarManager.ParameterItem = {
21. key: 'testKey',
22. value: 'testValue'
23. }
24. let taskInfo: quickBarManager.QuickTaskInfo = {
25. taskName: 'newTaskName',
26. abilityName: 'newEntryAbility',
27. moduleName: 'newModuleName',
28. // 参数可选
29. taskIcon: imagePixelMap,
30. // 参数可选
31. taskDetail: '任务的描述',
32. // 参数可选
33. parameters: [parameters]
34. }

36. const task: quickBarManager.QuickTask = {
37. taskId: 1,
38. categoryId: 1,
39. taskInfo: taskInfo
40. }

42. try {
43. await quickBarManager.updateQuickTask(context,task);
44. } catch (error) {
45. console.error(`updateQuickTask failed. error code: ${error.code}, error message: ${error.message}`);
46. }
47. }
```

## quickBarManager.deleteQuickTask

PC/2in1

deleteQuickTask(context: common.Context, taskId: number): Promise<void>

删除快捷栏任务。

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

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](statusbar-extension-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1020210004 | Quick task not found. |

**示例：**

```
1. import { quickBarManager } from '@kit.DeskTopExtensionKit';

3. /**
4. * 可以通过自定义组件的内置方法获取Context信息
5. * 具体方法：this.getUIContext().getHostContext();
6. */
7. async function deleteQuickTask(context: Context) {
8. if (context === undefined) {
9. return;
10. }
11. try {
12. // 删除任务id为1的任务
13. await quickBarManager.deleteQuickTask(context, 1);
14. } catch (error) {
15. console.error(`deleteQuickTask failed. error code: ${error.code}, error message: ${error.message}`);
16. }
17. }
```

## quickBarManager.deleteCustomCategory

PC/2in1

deleteCustomCategory(context: common.Context, categoryId: number): Promise<void>

删除快捷栏分组，其下的所有任务也会随着一起删除。

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

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](statusbar-extension-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1020210003 | Category not found. |

**示例：**

```
1. import { quickBarManager } from '@kit.DeskTopExtensionKit';

3. /**
4. * 可以通过自定义组件的内置方法获取Context信息
5. * 具体方法：this.getUIContext().getHostContext();
6. */
7. async function deleteCustomCategory(context: Context) {
8. if (context === undefined) {
9. return;
10. }
11. try {
12. // 删除分组id为1的分组
13. await quickBarManager.deleteCustomCategory(context, 1);
14. } catch (error) {
15. console.error(`deleteCustomCategory failed. error code: ${error.code}, error message: ${error.message}`);
16. }
17. }
```

## quickBarManager.addQuickBarGroup

PC/2in1

addQuickBarGroup(context: common.Context, group: QuickBarGroup): Promise<void>

增加快捷栏分组。

**系统能力：** SystemCapability.PCService.QuickBarManager

**起始版本：** 6.1.0(23)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。 |
| group | [QuickBarGroup](desktop-quickbar-extension-manager.md#quickbarmanagerquickbargroup) | 是 | 快捷栏分组信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回值的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](statusbar-extension-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1020210005 | Group already exists. |
| 1020210008 | The string length exceeds the threshold. |

**示例：**

```
1. import { quickBarManager } from '@kit.DeskTopExtensionKit';
2. import { image } from '@kit.ImageKit';
3. import { resourceManager } from '@kit.LocalizationKit';

5. // 获取资源管理器
6. const resourceMgr: resourceManager.ResourceManager = getContext().resourceManager;
7. // 从rawfile目录中获取图片
8. const whiteFileData = resourceMgr.getRawFileContentSync('icon.png');
9. const whiteImageSource = image.createImageSource(whiteFileData.buffer);
10. const imagePixelMap = await whiteImageSource.createPixelMap();
11. try {
12. // 增加分组
13. await quickBarManager.addQuickBarGroup(getContext(), {
14. groupKey: 'group_one', // 分组名
15. groupIcon: imagePixelMap // 分组图标
16. });
17. } catch (error) {
18. console.error(`error code: ${error.code}, error message: ${error.message}`);
19. }
```

## quickBarManager.deleteQuickBarGroup

PC/2in1

deleteQuickBarGroup(context: common.Context, groupKey: string): Promise<void>

增加快捷栏分组。

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
| Promise<void> | 无返回值的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](statusbar-extension-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1020210006 | Group not found. |

**示例：**

```
1. import { quickBarManager } from '@kit.DeskTopExtensionKit';

3. try {
4. // 删除分组名为group_one的分组
5. await quickBarManager.deleteQuickBarGroup(getContext(), 'group_one');
6. } catch (error) {
7. console.error(`error code: ${error.code}, error message: ${error.message}`);
8. }
```

## quickBarManager.getQuickBarGroups

PC/2in1

getQuickBarGroups(context: common.Context): Promise<QuickBarGroup[]>

获取所有分组信息。

**系统能力：** SystemCapability.PCService.QuickBarManager

**起始版本：** 6.1.0(23)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[QuickBarGroup](desktop-quickbar-extension-manager.md#quickbarmanagerquickbargroup)[]> | Promise对象，返回所有分组信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](statusbar-extension-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1020210006 | Group not found. |

**示例：**

```
1. import { quickBarManager } from '@kit.DeskTopExtensionKit';

3. try {
4. // 获取所有分组
5. const groups = await quickBarManager.getQuickBarGroups(getContext());
6. } catch (error) {
7. console.error(`error code: ${error.code}, error message: ${error.message}`);
8. }
```

## quickBarManager.setWindowToGroup

PC/2in1

setWindowToGroup(context: common.Context, windowid: string, groupKey?: string): Promise<void>

设置分组信息。

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
| Promise<void> | 无返回值的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](statusbar-extension-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1020210006 | Group not found. |
| 1020210007 | Window not found. |

**示例：**

```
1. import { quickBarManager } from '@kit.DeskTopExtensionKit';

3. try {
4. // 将id为80的窗口，增加到分组名为 group_one 的分组
5. await quickBarManager.setWindowToGroup(getContext(), '80', 'group_one');
6. } catch (error) {
7. console.error(`deleteCustomCategory failed. error code: ${error.code}, error message: ${error.message}`);
8. }
```
