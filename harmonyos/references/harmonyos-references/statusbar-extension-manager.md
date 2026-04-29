---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/statusbar-extension-manager
title: statusBarManager（状态栏管理服务）
breadcrumb: API参考 > 系统 > 基础功能 > Desktop Extension Kit（桌面拓展服务） > ArkTS API > statusBarManager（状态栏管理服务）
category: harmonyos-references
scraped_at: 2026-04-29T14:00:43+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:f9e4036d1aae898357cfac38b0491c1fe914c19002f7abedcff9c9e6e02d25be
---

本模块为应用提供接入状态栏的能力。应用可以通过接入相应的API，可快速在状态栏显示应用及下拉面板，实现对应用的管理；用户可以通过直接操作状态栏图标完成一些应用操作。

**起始版本：** 5.0.0(12)

## 导入模块

PC/2in1

```
1. import { statusBarManager } from '@kit.DeskTopExtensionKit';
```

## statusBarManager.StatusBarItem

PC/2in1

状态栏图标详细参数。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.0(12)

| **名称** | **类型** | **只读** | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| icons | [StatusBarIcon](statusbar-extension-manager.md#statusbarmanagerstatusbaricon) | 否 | 否 | 状态栏应用图标的图片信息。 |
| quickOperation | [QuickOperation](statusbar-extension-manager.md#statusbarmanagerquickoperation) | 否 | 否 | 状态栏应用图标的左键业务弹窗相关信息。 |
| statusBarGroupMenu | [StatusBarGroupMenu](statusbar-extension-manager.md#statusbarmanagerstatusbargroupmenu)[] | 否 | 是 | 状态栏图标的右键分组菜单相关信息。  默认值：undefined。  **说明：** 当前所有分组下一级菜单项的总和不可超过20个。 |
| hoverTips | string | 否 | 是 | 状态栏图标hover时的显示信息。  取值范围：1~128。  **说明：** 如不配置该参数，则hover时显示内容默认取值为[statusBarManager.QuickOperation](statusbar-extension-manager.md#statusbarmanagerquickoperation)中配置模块的[label](js-apis-bundlemanager-hapmoduleinfo.md#hapmoduleinfo-1)。  **起始版本：** 6.0.2(22) |

## statusBarManager.StatusBarIcon

PC/2in1

状态栏图标的图片信息。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.0(12)

| **名称** | **类型** | **只读** | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| white | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | 否 | 深色壁纸下展示的图标，建议采用纯白色图标，支持JPEG、PNG、GIF、WebP、BMP、SVG、ICO、DNG等图片类型。  **说明：** 建议使用24[vp](ts-pixel-units.md) \* 24vp的图片。 |
| black | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | 否 | 浅色壁纸下展示的图标，建议采用纯黑色图标，支持JPEG、PNG、GIF、WebP、BMP、SVG、ICO、DNG等图片类型。  **说明：** 建议使用24vp \* 24vp的图片。 |

## statusBarManager.QuickOperation

PC/2in1

状态栏图标左键业务弹窗的详细信息。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.0(12)

| **名称** | **类型** | **只读** | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| title | string | 否 | 否 | 状态栏图标的左键业务弹窗的标题。  取值范围：无限制，超长显示省略号。 |
| height | number | 否 | 否 | 状态栏图标的左键业务弹窗的自定义区域高度，单位：vp。  取值范围：大于0。 |
| abilityName | string | 否 | 否 | 状态栏图标左键业务弹窗的应用定制区域对应的自定义[StatusBarViewExtensionAbility](statusbar-extension-ability.md)的名称。  **说明：** 当传空字符串时，支持通过监听[statusBarIconClick](statusbar-extension-manager.md#statusbarmanageronstatusbariconclick)事件处理点击业务。 |
| moduleName | string | 否 | 是 | 状态栏图标左键业务弹窗的应用定制区域对应的自定义[StatusBarViewExtensionAbility](statusbar-extension-ability.md)所在的模块名称。  默认值：''。 |
| loadingStatus | boolean | 否 | 是 | 点击状态栏图标展开二级菜单场景下是否加载动效。  默认值：false。  **起始版本：** 6.0.0(20) |

## statusBarManager.StatusBarGroupMenu

PC/2in1

type StatusBarGroupMenu = StatusBarMenuItem[]

状态栏图标右键菜单的分组菜单信息。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [StatusBarMenuItem](statusbar-extension-manager.md#statusbarmanagerstatusbarmenuitem)[] | 菜单组的信息，可以包含多个一级菜单项。 |

## statusBarManager.StatusBarMenuItem

PC/2in1

状态栏图标右键菜单的一级菜单项信息。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.0(12)

| **名称** | **类型** | **只读** | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| title | string | 否 | 否 | 菜单项标题。  取值范围：无限制，超长显示省略号。 |
| menuAction | [StatusBarMenuAction](statusbar-extension-manager.md#statusbarmanagerstatusbarmenuaction) | 否 | 是 | 菜单项行为信息。  默认值：undefined。  **说明：** 当前菜单行为仅支持打开应用内定义的UIAbility，且menuAction和subMenu两个参数不可同时缺省。 |
| subMenu | [StatusBarSubMenuItem](statusbar-extension-manager.md#statusbarmanagerstatusbarsubmenuitem)[] | 否 | 是 | 一级菜单项的子菜单项。  默认值：undefined。  **说明：** 当前单个一级菜单项最多支持20个子菜单项。 |

## statusBarManager.StatusBarMenuAction

PC/2in1

状态栏图标右键菜单的菜单项点击行为信息。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.0(12)

| **名称** | **类型** | **只读** | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| abilityName | string | 否 | 否 | 点击菜单项拉起的应用的Ability名称。  **说明：** 当前仅支持拉起UIAbility。 |
| moduleName | string | 否 | 是 | 点击菜单项拉起的应用的Ability所在的模块名称。  默认值：'' |
| notifyOnly | boolean | 否 | 是 | 图标右键菜单点击事件使能。  取值范围：  false：不使能，此时点击右键菜单无事件通知。  true：使能，此时点击右键菜单有事件通知。  默认值：false - 无右键菜单点击事件触发。  **说明：** 当使能和提供菜单menuCode时，支持通过监听[rightMenuClick](statusbar-extension-manager.md#statusbarmanageronrightmenuclick)事件处理图标右键菜单点击业务。  **起始版本：** 5.0.2(14) |
| menuCode | string | 否 | 是 | 图标右键菜单唯一标识。  默认值：''。  **说明：** 需保证菜单标识的唯一性，用于区分不同菜单项。  **起始版本：** 5.0.2(14) |

## statusBarManager.StatusBarSubMenuItem

PC/2in1

状态栏图标的右键菜单的二级菜单项信息

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.0(12)

| **名称** | **类型** | **只读** | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| subTitle | string | 否 | 否 | 二级菜单项标题。  取值范围：无限制，超长显示省略号。 |
| menuAction | [StatusBarMenuAction](statusbar-extension-manager.md#statusbarmanagerstatusbarmenuaction) | 否 | 否 | 菜单项行为信息。  **说明：** 当前菜单行为仅支持打开应用内定义的UIAbility。 |

## statusBarManager.addToStatusBar

PC/2in1

addToStatusBar(context: common.Context, statusBarItem: StatusBarItem): void

应用接入状态栏方法，当前同一个应用仅支持添加一个图标，重复添加无效。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。  **说明：** 当前context仅支持传入Context的子类UIAbilityContext、ServiceExtensionContext、FormExtensionContext。 |
| statusBarItem | [StatusBarItem](statusbar-extension-manager.md#statusbarmanagerstatusbaritem) | 是 | 应用自定义接入状态栏的图标的详细信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](statusbar-extension-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1010710001 | The size of the pixelmap exceeds the limit. |
| 1010710002 | The number of menu items or submenu items exceeds the limit. |
| 1010710003 | The API is being called too frequently. |
| 1010710005 | The string length exceeds the threshold. |
| 1010720001 | A menu item contains neither submenu nor menuAction. |

**示例：**

```
1. import { statusBarManager } from '@kit.DeskTopExtensionKit';
2. import { image } from '@kit.ImageKit';
3. import { resourceManager } from '@kit.LocalizationKit';

5. /**
6. * 可以通过自定义组件的内置方法获取Context信息
7. * 具体方法：this.getUIContext().getHostContext();
8. */
9. async function addToStatusBar(context: Context) {
10. if (!context) {
11. console.error('getHostContext failed');
12. return;
13. }
14. // 获取resourceManager资源管理器
15. const resourceMgr: resourceManager.ResourceManager = context.resourceManager;

17. // 创建white pixelMap，需在资源rawfile文件夹中预置testWhite.png图片，图片大小为24vp * 24vp
18. const whiteFileData = resourceMgr.getRawFileContentSync('testWhite.png');
19. const whiteBuffer = whiteFileData.buffer;
20. const whiteImageSource = image.createImageSource(whiteBuffer);
21. let whitePixelMap = await whiteImageSource.createPixelMap();

23. // 创建black pixelMap，需在资源rawfile文件夹中预置testBlack.png图片，图片大小为24vp * 24vp
24. const blackFileData = resourceMgr.getRawFileContentSync('testBlack.png');
25. const blackBuffer = blackFileData.buffer;
26. const blackImageSource = image.createImageSource(blackBuffer);
27. let blackPixelMap = await blackImageSource.createPixelMap();

29. // 构建图标信息
30. let icon: statusBarManager.StatusBarIcon = {
31. white: whitePixelMap,
32. black: blackPixelMap
33. }

35. // 构建右键菜单项内容
36. let subMenus: Array<statusBarManager.StatusBarSubMenuItem> = [];
37. let subMenuItemAction: statusBarManager.StatusBarMenuAction = {
38. abilityName: "EntryAbility"
39. }
40. let subMenu: statusBarManager.StatusBarSubMenuItem = {
41. subTitle: "子菜单项",
42. menuAction: subMenuItemAction
43. }
44. subMenus.push(subMenu);

46. let statusBarMenuItems: Array<statusBarManager.StatusBarMenuItem> = [];
47. let menuItem: statusBarManager.StatusBarMenuItem = {
48. title: "一级菜单项",
49. // 一级menuAction和subMenu两项不可都缺省
50. subMenu: subMenus
51. };
52. statusBarMenuItems.push(menuItem);

54. let statusBarGroupMenus: Array<statusBarManager.StatusBarGroupMenu> = [];
55. statusBarGroupMenus.push(statusBarMenuItems);

57. // 构建左键业务弹窗信息
58. let operation: statusBarManager.QuickOperation = {
59. abilityName: "MyStatusBarViewAbility",
60. title: "测试Demo",
61. height: 300,
62. // 可缺省
63. moduleName: 'entry'
64. };

66. // 构建添加到状态栏的图标详细信息
67. let item: statusBarManager.StatusBarItem = {
68. icons: icon,
69. quickOperation: operation,
70. statusBarGroupMenu: statusBarGroupMenus
71. };

73. try {
74. statusBarManager.addToStatusBar(context, item);
75. } catch (error) {
76. console.error(`addToStatusBar failed. error code: ${error.code}, error message: ${error.message}`);
77. }
78. }
```

## statusBarManager.addToStatusBar

PC/2in1

addToStatusBar(context: common.Context, statusBarItem: StatusBarItem, callback: AsyncCallback<void>): void

应用接入状态栏方法，使用callback异步回调，当前同一个应用仅支持添加一个图标，重复添加无效。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。  **说明：** 当前context仅支持传入Context的子类UIAbilityContext、ServiceExtensionContext、FormExtensionContext。 |
| statusBarItem | [StatusBarItem](statusbar-extension-manager.md#statusbarmanagerstatusbaritem) | 是 | 应用自定义接入状态栏的图标的详细信息。 |
| callback | AsyncCallback<void> | 是 | 表示应用添加图标到状态栏回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](statusbar-extension-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1010710001 | The size of the pixelmap exceeds the limit. |
| 1010710002 | The number of menu items or submenu items exceeds the limit. |
| 1010710003 | The API is being called too frequently. |
| 1010710005 | The string length exceeds the threshold. |
| 1010720001 | A menu item contains neither submenu nor menuAction. |

**示例：**

```
1. import { statusBarManager } from '@kit.DeskTopExtensionKit';
2. import { image } from '@kit.ImageKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { resourceManager } from '@kit.LocalizationKit';

6. /**
7. * 可以通过自定义组件的内置方法获取Context信息
8. * 具体方法：this.getUIContext().getHostContext();
9. */
10. async function addToStatusBar(context: Context) {
11. if (!context) {
12. console.error('getHostContext failed');
13. return;
14. }
15. // 获取resourceManager资源管理器
16. const resourceMgr: resourceManager.ResourceManager = context.resourceManager;

18. // 创建white pixelMap，需在资源rawfile文件夹中预置testWhite.png图片，图片大小为24vp * 24vp
19. const whiteFileData = resourceMgr.getRawFileContentSync('testWhite.png');
20. const whiteBuffer = whiteFileData.buffer;
21. const whiteImageSource = image.createImageSource(whiteBuffer);
22. let whitePixelMap = await whiteImageSource.createPixelMap();

24. // 创建black pixelMap，需在资源rawfile文件夹中预置testBlack.png图片，图片大小为24vp * 24vp
25. const blackFileData = resourceMgr.getRawFileContentSync('testBlack.png');
26. const blackBuffer = blackFileData.buffer;
27. const blackImageSource = image.createImageSource(blackBuffer);
28. let blackPixelMap = await blackImageSource.createPixelMap();

30. // 构建图标信息
31. let icon: statusBarManager.StatusBarIcon = {
32. white: whitePixelMap,
33. black: blackPixelMap
34. }

36. // 构建右键菜单项内容
37. let subMenus: Array<statusBarManager.StatusBarSubMenuItem> = [];
38. let subMenuItemAction: statusBarManager.StatusBarMenuAction = {
39. abilityName: "EntryAbility"
40. }
41. let subMenu: statusBarManager.StatusBarSubMenuItem = {
42. subTitle: "子菜单项",
43. menuAction: subMenuItemAction
44. }
45. subMenus.push(subMenu);

47. let statusBarMenuItems: Array<statusBarManager.StatusBarMenuItem> = [];
48. let menuItem: statusBarManager.StatusBarMenuItem = {
49. title: "一级菜单项",
50. // 一级menuAction和subMenu两项不可都缺省
51. subMenu: subMenus
52. };
53. statusBarMenuItems.push(menuItem);

55. let statusBarGroupMenus: Array<statusBarManager.StatusBarGroupMenu> = [];
56. statusBarGroupMenus.push(statusBarMenuItems);

58. // 构建左键业务弹窗信息
59. let operation: statusBarManager.QuickOperation = {
60. abilityName: "MyStatusBarViewAbility",
61. title: "测试Demo",
62. height: 300,
63. // 可缺省
64. moduleName: 'entry'
65. };

67. // 构建添加到状态栏的图标详细信息
68. let item: statusBarManager.StatusBarItem = {
69. icons: icon,
70. quickOperation: operation,
71. statusBarGroupMenu: statusBarGroupMenus
72. };

74. try {
75. statusBarManager.addToStatusBar(context, item, (error: BusinessError) => {
76. if (error) {
77. // ...
78. return;
79. }
80. console.info('addToStatusBar success');
81. });
82. } catch (error) {
83. console.error(`addToStatusBar failed. error code: ${error.code}, error message: ${error.message}`);
84. }
85. }
```

## statusBarManager.removeFromStatusBar

PC/2in1

removeFromStatusBar(context: common.Context): void

应用移除状态栏对应图标方法。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。  **说明：** 当前context仅支持传入Context的子类UIAbilityContext、ServiceExtensionContext、FormExtensionContext。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](statusbar-extension-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1010710003 | The API is being called too frequently. |
| 1010710004 | The icon cannot be deleted when no window is in the foreground. |

**示例：**

```
1. import { statusBarManager } from '@kit.DeskTopExtensionKit';

3. /**
4. * 可以通过自定义组件的内置方法获取Context信息
5. * 具体方法：this.getUIContext().getHostContext();
6. */
7. function removeFromStatusBar(context: Context) {
8. if (!context) {
9. console.error('getHostContext failed');
10. return;
11. }
12. try {
13. statusBarManager.removeFromStatusBar(context);
14. } catch (error) {
15. console.error(`removeFromStatusBar failed. error code: ${error.code}, error message: ${error.message}`);
16. }
17. }
```

## statusBarManager.removeFromStatusBar

PC/2in1

removeFromStatusBar(context: common.Context, callback: AsyncCallback<void>): void

应用移除状态栏对应图标方法，使用callback异步回调。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。  **说明：** 当前context仅支持传入Context的子类UIAbilityContext、ServiceExtensionContext、FormExtensionContext。 |
| callback | AsyncCallback<void> | 是 | 表示应用移除状态栏图标回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](statusbar-extension-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1010710003 | The API is being called too frequently. |
| 1010710004 | The icon cannot be deleted when no window is in the foreground. |

**示例：**

```
1. import { statusBarManager } from '@kit.DeskTopExtensionKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. /**
5. * 可以通过自定义组件的内置方法获取Context信息
6. * 具体方法：this.getUIContext().getHostContext();
7. */
8. function removeFromStatusBar(context: Context) {
9. if (!context) {
10. console.error('getHostContext failed');
11. return;
12. }
13. try {
14. statusBarManager.removeFromStatusBar(context, (error: BusinessError) => {
15. if (error) {
16. // ...
17. return;
18. }
19. console.info('removeFromStatusBar success');
20. });
21. } catch (error) {
22. console.error(`removeFromStatusBar failed. error code: ${error.code}, error message: ${error.message}`);
23. }
24. }
```

## statusBarManager.updateQuickOperationHeight

PC/2in1

updateQuickOperationHeight(context: common.Context, height: number): void

应用更新状态栏图标的左键弹窗应用定制区域高度。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。  **说明：** 当前context仅支持传入Context的子类UIAbilityContext、ServiceExtensionContext、FormExtensionContext。 |
| height | number | 是 | 状态栏图标左键的应用面板自定义区域高度，单位：vp。  取值范围：大于0。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](statusbar-extension-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1010710003 | The API is being called too frequently. |

**示例：**

```
1. import { statusBarManager } from '@kit.DeskTopExtensionKit';

3. /**
4. * 可以通过自定义组件的内置方法获取Context信息
5. * 具体方法：this.getUIContext().getHostContext();
6. */
7. function updateQuickOperationHeight(context: Context) {
8. if (!context) {
9. console.error('getHostContext failed');
10. return;
11. }
12. let height = 200;
13. try {
14. statusBarManager.updateQuickOperationHeight(context, height);
15. } catch (error) {
16. console.error(`updateQuickOperationHeight failed. error code: ${error.code}, error message: ${error.message}`);
17. }
18. }
```

## statusBarManager.updateQuickOperationHeight

PC/2in1

updateQuickOperationHeight(context: common.Context, height: number, callback: AsyncCallback<void>): void

应用更新状态栏图标的左键弹窗应用定制区域高度，使用callback异步回调。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。  **说明：** 当前context仅支持传入Context的子类UIAbilityContext、ServiceExtensionContext、FormExtensionContext。 |
| height | number | 是 | 状态栏图标左键的应用面板自定义区域高度，单位：vp。  取值范围：大于0。 |
| callback | AsyncCallback<void> | 是 | 表示应用更新状态栏图标的左键弹窗应用定制区域高度回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](statusbar-extension-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1010710003 | The API is being called too frequently. |

**示例：**

```
1. import { statusBarManager } from '@kit.DeskTopExtensionKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. /**
5. * 可以通过自定义组件的内置方法获取Context信息
6. * 具体方法：this.getUIContext().getHostContext();
7. */
8. function updateQuickOperationHeight(context: Context) {
9. if (!context) {
10. console.error('getHostContext failed');
11. return;
12. }
13. let height = 200;
14. try {
15. statusBarManager.updateQuickOperationHeight(context, height, (error) => {
16. if (error) {
17. // ...
18. return;
19. }
20. console.info('updateQuickOperationHeight success');
21. });
22. } catch (error) {
23. console.error(`updateQuickOperationHeight failed. error code: ${error.code}, error message: ${error.message}`);
24. }
25. }
```

## statusBarManager.updateStatusBarMenu

PC/2in1

updateStatusBarMenu(context: common.Context, statusBarGroupMenus: StatusBarGroupMenu[]): void

应用更新状态栏图标的右键菜单内容。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。  **说明：** 当前context仅支持传入Context的子类UIAbilityContext、ServiceExtensionContext、FormExtensionContext。 |
| statusBarGroupMenus | [StatusBarGroupMenu](statusbar-extension-manager.md#statusbarmanagerstatusbargroupmenu)[] | 是 | 更新后的应用右键菜单栏相关信息。  **说明：** 当前所有分组下一级菜单项的总和不可超过20个。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](statusbar-extension-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1010710002 | The number of menu items or submenu items exceeds the limit. |
| 1010710003 | The API is being called too frequently. |
| 1010720001 | A menu item contains neither submenu nor menuAction. |

**示例：**

```
1. import { statusBarManager } from '@kit.DeskTopExtensionKit';

3. /**
4. * 可以通过自定义组件的内置方法获取Context信息
5. * 具体方法：this.getUIContext().getHostContext();
6. */
7. function updateStatusBarMenu(context: Context) {
8. // 构建右键菜单项内容
9. let subMenus: Array<statusBarManager.StatusBarSubMenuItem> = [];
10. let subMenuItemAction: statusBarManager.StatusBarMenuAction = {
11. abilityName: "EntryAbility"
12. }
13. let subMenu: statusBarManager.StatusBarSubMenuItem = {
14. subTitle: "二级菜单项",
15. menuAction: subMenuItemAction
16. }
17. subMenus.push(subMenu);
18. let statusBarMenuItems: Array<statusBarManager.StatusBarMenuItem> = [];
19. let menuItem: statusBarManager.StatusBarMenuItem = {
20. title: "一级菜单项",
21. // 一级menuAction和subMenu两项不可都缺省
22. subMenu: subMenus
23. };
24. statusBarMenuItems.push(menuItem);
25. let statusBarGroupMenus: Array<statusBarManager.StatusBarGroupMenu> = [];
26. statusBarGroupMenus.push(statusBarMenuItems);
27. if (!context) {
28. console.error('getHostContext failed');
29. return;
30. }
31. try {
32. statusBarManager.updateStatusBarMenu(context, statusBarGroupMenus);
33. } catch (error) {
34. console.error(`updateStatusBarMenu failed. error code: ${error.code}, error message: ${error.message}`);
35. }
36. }
```

## statusBarManager.updateStatusBarMenu

PC/2in1

updateStatusBarMenu(context: common.Context, statusBarGroupMenus: StatusBarGroupMenu[], callback: AsyncCallback<void>): void

应用更新状态栏图标的右键菜单内容，使用callback异步回调。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。  **说明：** 当前context仅支持传入Context的子类UIAbilityContext、ServiceExtensionContext、FormExtensionContext。 |
| statusBarGroupMenus | [StatusBarGroupMenu](statusbar-extension-manager.md#statusbarmanagerstatusbargroupmenu)[] | 是 | 更新后的应用右键菜单栏相关信息。  **说明：** 当前所有分组下一级菜单项的总和不可超过20个。 |
| callback | AsyncCallback<void> | 是 | 表示应用更新状态栏图标的右键菜单内容回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](statusbar-extension-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1010710002 | The number of menu items or submenu items exceeds the limit. |
| 1010710003 | The API is being called too frequently. |
| 1010720001 | A menu item contains neither submenu nor menuAction. |

**示例：**

```
1. import { statusBarManager } from '@kit.DeskTopExtensionKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. /**
5. * 可以通过自定义组件的内置方法获取Context信息
6. * 具体方法：this.getUIContext().getHostContext();
7. */
8. function updateStatusBarMenu(context: Context) {
9. // 构建右键菜单项内容
10. let subMenus: Array<statusBarManager.StatusBarSubMenuItem> = [];
11. let subMenuItemAction: statusBarManager.StatusBarMenuAction = {
12. abilityName: "EntryAbility"
13. }
14. let subMenu: statusBarManager.StatusBarSubMenuItem = {
15. subTitle: "二级菜单项",
16. menuAction: subMenuItemAction
17. }
18. subMenus.push(subMenu);
19. let statusBarMenuItems: Array<statusBarManager.StatusBarMenuItem> = [];
20. let menuItem: statusBarManager.StatusBarMenuItem = {
21. title: "一级菜单项",
22. // 一级menuAction和subMenu两项不可都缺省
23. subMenu: subMenus
24. };
25. statusBarMenuItems.push(menuItem);
26. let statusBarGroupMenus: Array<statusBarManager.StatusBarGroupMenu> = [];
27. statusBarGroupMenus.push(statusBarMenuItems);
28. if (!context) {
29. console.error('getHostContext failed');
30. return;
31. }
32. try {
33. statusBarManager.updateStatusBarMenu(context, statusBarGroupMenus, (err: BusinessError) => {
34. if (err) {
35. // ...
36. return;
37. }
38. console.info('updateStatusBarMenu success');
39. });
40. } catch (error) {
41. console.error(`updateStatusBarMenu failed. error code: ${error.code}, error message: ${error.message}`);
42. }
43. }
```

## statusBarManager.updateStatusBarIcon

PC/2in1

updateStatusBarIcon(context: common.Context, statusBarIcon: StatusBarIcon): void

应用更新接入状态栏的图标。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。  **说明：** 当前context仅支持传入Context的子类UIAbilityContext、ServiceExtensionContext、FormExtensionContext。 |
| statusBarIcon | [StatusBarIcon](statusbar-extension-manager.md#statusbarmanagerstatusbaricon) | 是 | 更新的图标。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](statusbar-extension-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1010710001 | The size of the pixelmap exceeds the limit. |
| 1010710003 | The API is being called too frequently. |

**示例：**

```
1. import { statusBarManager } from '@kit.DeskTopExtensionKit';
2. import { image } from '@kit.ImageKit';
3. import { resourceManager } from '@kit.LocalizationKit';

5. /**
6. * 可以通过自定义组件的内置方法获取Context信息
7. * 具体方法：this.getUIContext().getHostContext();
8. */
9. async function updateStatusBarIcon(context: Context) {
10. if (!context) {
11. console.error('getHostContext failed');
12. return;
13. }
14. // 获取resourceManager资源管理器
15. const resourceMgr: resourceManager.ResourceManager = context.resourceManager;

17. // 创建white pixelMap，需在资源rawfile文件夹中预置testWhite.png图片，图片大小为24vp * 24vp
18. const whiteFileData = resourceMgr.getRawFileContentSync('testWhite.png');
19. const whiteBuffer = whiteFileData.buffer;
20. const whiteImageSource = image.createImageSource(whiteBuffer);
21. let whitePixelMap = await whiteImageSource.createPixelMap();

23. // 创建black pixelMap，需在资源rawfile文件夹中预置testBlack.png图片，图片大小为24vp * 24vp
24. const blackFileData = resourceMgr.getRawFileContentSync('testBlack.png');
25. const blackBuffer = blackFileData.buffer;
26. const blackImageSource = image.createImageSource(blackBuffer);
27. let blackPixelMap = await blackImageSource.createPixelMap();

29. // 构建图标信息
30. let icons: statusBarManager.StatusBarIcon = {
31. white: whitePixelMap,
32. black: blackPixelMap
33. }

35. try {
36. statusBarManager.updateStatusBarIcon(context, icons);
37. } catch (error) {
38. console.error(`updateStatusBarIcon failed. error code: ${error.code}, error message: ${error.message}`);
39. }
40. }
```

## statusBarManager.updateStatusBarIcon

PC/2in1

updateStatusBarIcon(context: common.Context, statusBarIcon: StatusBarIcon, callback: AsyncCallback<void>): void

应用更新接入状态栏的图标，使用callback异步回调。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。  **说明：** 当前context仅支持传入Context的子类UIAbilityContext、ServiceExtensionContext、FormExtensionContext。 |
| statusBarIcon | [StatusBarIcon](statusbar-extension-manager.md#statusbarmanagerstatusbaricon) | 是 | 更新的图标。 |
| callback | AsyncCallback<void> | 是 | 表示应用更新接入状态栏的图标回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](statusbar-extension-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1010710001 | The size of the pixelmap exceeds the limit. |
| 1010710003 | The API is being called too frequently. |

**示例：**

```
1. import { statusBarManager } from '@kit.DeskTopExtensionKit';
2. import { image } from '@kit.ImageKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { resourceManager } from '@kit.LocalizationKit';

6. /**
7. * 可以通过自定义组件的内置方法获取Context信息
8. * 具体方法：this.getUIContext().getHostContext();
9. */
10. async function updateStatusBarIcon(context: Context) {
11. if (!context) {
12. console.error('getHostContext failed');
13. return;
14. }
15. // 获取resourceManager资源管理器
16. const resourceMgr: resourceManager.ResourceManager = context.resourceManager;

18. // 创建white pixelMap，需在资源rawfile文件夹中预置testWhite.png图片，图片大小为24vp * 24vp
19. const whiteFileData = resourceMgr.getRawFileContentSync('testWhite.png');
20. const whiteBuffer = whiteFileData.buffer;
21. const whiteImageSource = image.createImageSource(whiteBuffer);
22. let whitePixelMap = await whiteImageSource.createPixelMap();

24. // 创建black pixelMap，需在资源rawfile文件夹中预置testBlack.png图片，图片大小为24vp * 24vp
25. const blackFileData = resourceMgr.getRawFileContentSync('testBlack.png');
26. const blackBuffer = blackFileData.buffer;
27. const blackImageSource = image.createImageSource(blackBuffer);
28. let blackPixelMap = await blackImageSource.createPixelMap();

30. // 构建图标信息
31. let icons: statusBarManager.StatusBarIcon = {
32. white: whitePixelMap,
33. black: blackPixelMap
34. }

36. try {
37. statusBarManager.updateStatusBarIcon(context, icons, (error: BusinessError) => {
38. if (error) {
39. // ...
40. return;
41. }
42. console.info('updateStatusBarIcon success');
43. });
44. } catch (error) {
45. console.error(`updateStatusBarIcon failed. error code: ${error.code}, error message: ${error.message}`);
46. }
47. }
```

## statusBarManager.on('statusBarIconClick')

PC/2in1

on(type: 'statusBarIconClick', callback: Callback<emitter.EventData>): void

监听状态栏图标点击事件。使用callback异步回调。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'statusBarIconClick'，当点击应用图标时，触发该事件。  **说明：** 当调用[addToStatusBar](statusbar-extension-manager.md#statusbarmanageraddtostatusbar)，入参[quickOperation](statusbar-extension-manager.md#statusbarmanagerquickoperation)未指定abilityName时，支持通过监听statusBarIconClick事件处理点击业务。 |
| callback | Callback<[emitter.EventData](js-apis-emitter.md#eventdata)> | 是 | 需要注册的回调函数，返回信息为图标点击相关信息。  当前仅支持返回iconClickType（点击事件类型）中的leftClick（左键）。 |

**示例：**

```
1. private onStatusBarIconClick = (eventData: emitter.EventData) => {
2. // 自定义图标点击业务
3. let data = eventData.data;
4. if (data) {
5. switch (data['iconClickType']) {
6. case 'leftClick':
7. // 自定义左键点击业务
8. break;
9. default:
10. break;
11. }
12. }
13. }

15. // 监听状态栏图标点击事件
16. statusBarManager.on('statusBarIconClick', this.onStatusBarIconClick);
```

## statusBarManager.off('statusBarIconClick')

PC/2in1

off(type: 'statusBarIconClick', callback?: Callback<emitter.EventData>): void

注销状态栏图标点击事件。使用callback异步回调。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消事件回调类型，支持的事件为'statusBarIconClick' |
| callback | Callback<[emitter.EventData](js-apis-emitter.md#eventdata)> | 否 | 取消该事件的回调处理函数。  默认值：undefined。  **说明：**  若不传入callback，会取消该事件的所有回调函数；  若传入callback，需要传入对应on方法相同的对象，否则会导致回调函数未成功注销，导致内存泄露。 |

**示例：**

```
1. private onStatusBarIconClick = (eventData: emitter.EventData) => {
2. // 自定义图标点击业务
3. let data = eventData.data;
4. if (data) {
5. switch (data['iconClickType']) {
6. case 'leftClick':
7. // 自定义左键点击业务
8. break;
9. default:
10. break;
11. }
12. }
13. }
14. // 取消事件回调处理函数
15. statusBarManager.off('statusBarIconClick', this.onStatusBarIconClick);

17. // 注销事件监听
18. statusBarManager.off('statusBarIconClick');
```

## statusBarManager.on('rightMenuClick')

PC/2in1

on(type: 'rightMenuClick', callback: Callback<emitter.EventData>): void

监听状态栏图标右键菜单点击事件。使用callback异步回调。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'rightMenuClick'，当点击应用图标右键菜单时，触发该事件。  **说明：** 当调用[updateStatusBarMenu](statusbar-extension-manager.md#statusbarmanagerupdatestatusbarmenu)，添加菜单项时，指定[menuAction](statusbar-extension-manager.md#statusbarmanagerstatusbarmenuaction)的notifyOnly使能和菜单项menuCode时生效。 |
| callback | Callback<[emitter.EventData](js-apis-emitter.md#eventdata)> | 是 | 需要注册的回调函数，返回信息为图标右键菜单点击相关信息。  当前返回信息menuCode（点击菜单项唯一标识）。 |

**示例：**

```
1. private onRightMenuClick = (eventData: emitter.EventData) => {
2. // 自定义图标右键菜单点击业务
3. let data = eventData.data;
4. if (data) {
5. let menuCode = data['menuCode'] as string;
6. // 处理点击菜单项业务
7. }
8. }

10. // 监听右键菜单点击事件
11. statusBarManager.on('rightMenuClick', this.onRightMenuClick);
```

## statusBarManager.off('rightMenuClick')

PC/2in1

off(type: 'rightMenuClick', callback?: Callback<emitter.EventData>): void

注销状态栏图标右键菜单点击事件。使用callback异步回调。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消事件回调类型，支持的事件为'rightMenuClick'。 |
| callback | Callback<[emitter.EventData](js-apis-emitter.md#eventdata)> | 否 | 取消该事件的回调处理函数。  默认值：undefined。  **说明：**  若不传入callback，会取消该事件的所有回调函数；  若传入callback，需要传入对应on方法相同的对象，否则会导致回调函数未成功注销，导致内存泄露。 |

**示例：**

```
1. private onRightMenuClick = (eventData: emitter.EventData) => {
2. // 自定义图标右键菜单点击业务
3. let data = eventData.data;
4. if (data) {
5. let menuCode = data['menuCode'] as string;
6. // 处理点击菜单项业务
7. }
8. }

10. // 取消事件回调处理函数
11. statusBarManager.off('rightMenuClick', this.onRightMenuClick);

13. // 注销事件监听
14. statusBarManager.off('rightMenuClick');
```

## statusBarManager.updateStatusBarHoverTips

PC/2in1

updateStatusBarHoverTips(context: common.Context, hoverTips: string): Promise<void>

更新状态栏图标hover时显示内容。使用promise异步回调。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 6.0.2(22)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。  **说明：** 当前context仅支持传入Context的子类UIAbilityContext、ServiceExtensionContext、FormExtensionContext。 |
| hoverTips | string | 是 | 状态栏图标hover时的显示信息。  字符串长度范围：1~128。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](statusbar-extension-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1010710003 | The API is being called too frequently. |
| 1010710005 | The string length exceeds the threshold. |

**示例：**

```
1. import { statusBarManager } from '@kit.DeskTopExtensionKit';

3. /**
4. * 可以通过自定义组件的内置方法获取Context信息
5. * 具体方法：this.getUIContext().getHostContext();
6. */
7. async function updateStatusBarHoverTips(context: Context) {
8. if (!context) {
9. console.error('getHostContext failed');
10. return;
11. }
12. let hoverTips: string = 'hoverTips';
13. try {
14. await statusBarManager.updateStatusBarHoverTips(context, hoverTips);
15. } catch (error) {
16. console.error(`updateStatusBarHoverTips failed. error code: ${error.code}, error message: ${error.message}`);
17. }
18. }
```
