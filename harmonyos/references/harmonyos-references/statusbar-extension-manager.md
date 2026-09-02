---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/statusbar-extension-manager
title: statusBarManager（状态栏管理服务）
breadcrumb: API参考 > 系统 > 基础功能 > Desktop Extension Kit（桌面拓展服务） > ArkTS API > statusBarManager（状态栏管理服务）
category: harmonyos-references
scraped_at: 2026-09-02T14:52:31+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:14b520417d3e506b2eb1d7ccf3dfb78f3b28c87ce4359164cb4ae29520930bfc
---

本模块为应用提供接入状态栏的能力。应用可以通过接入相应的API，可快速在状态栏显示应用及下拉面板，实现对应用的管理；用户可以通过直接操作状态栏图标完成一些应用操作。

**起始版本：** 5.0.0(12)

## 导入模块

```typescript
import { statusBarManager } from '@kit.DeskTopExtensionKit';
```

## StatusBarItem

状态栏图标详细参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.0(12)

| **名称** | **类型** | **只读** | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| icons | [StatusBarIcon](statusbar-extension-manager.md#statusbaricon) | 否 | 否 | 状态栏应用图标的图片信息。 |
| quickOperation | [QuickOperation](statusbar-extension-manager.md#quickoperation) | 否 | 否 | 状态栏应用图标的左键业务弹窗相关信息。 |
| statusBarGroupMenu | [StatusBarGroupMenu](statusbar-extension-manager.md#statusbargroupmenu)[] | 否 | 是 | 状态栏图标的右键分组菜单相关信息。  默认值：undefined。  **说明：** 当前所有分组下一级菜单项的总和不可超过20个。 |
| hoverTips | string | 否 | 是 | 状态栏图标hover时的显示信息。  取值范围：1~128。  **说明：** 如不配置该参数，则hover时显示内容默认取值为[QuickOperation](statusbar-extension-manager.md#quickoperation)中配置模块的[label](js-apis-bundlemanager-hapmoduleinfo.md#hapmoduleinfo-1)。  **起始版本：** 6.0.2(22) |

## StatusBarIcon

状态栏图标的图片信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.0(12)

| **名称** | **类型** | **只读** | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| white | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | 否 | 深色壁纸下展示的图标，建议采用纯白色图标，支持JPEG、PNG、GIF、WebP、BMP、SVG、ICO、DNG等图片类型。  **说明：** 建议使用24[vp](ts-pixel-units.md) \* 24vp的图片。 |
| black | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | 否 | 浅色壁纸下展示的图标，建议采用纯黑色图标，支持JPEG、PNG、GIF、WebP、BMP、SVG、ICO、DNG等图片类型。  **说明：** 建议使用24vp \* 24vp的图片。 |

## QuickOperation

状态栏图标左键业务弹窗的详细信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.0(12)

| **名称** | **类型** | **只读** | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| title | string | 否 | 否 | 状态栏图标的左键业务弹窗的标题。  取值范围：无限制，超长显示省略号。 |
| height | number | 否 | 否 | 状态栏图标的左键业务弹窗的自定义区域高度，单位：vp。  取值范围：大于0。 |
| abilityName | string | 否 | 否 | 状态栏图标左键业务弹窗的应用定制区域对应的自定义[StatusBarViewExtensionAbility](statusbar-extension-ability.md)的名称。  **说明：** 当传空字符串时，支持通过监听[statusBarIconClick](statusbar-extension-manager.md#statusbarmanageronstatusbariconclick)事件处理点击业务。 |
| moduleName | string | 否 | 是 | 状态栏图标左键业务弹窗的应用定制区域对应的自定义[StatusBarViewExtensionAbility](statusbar-extension-ability.md)所在的模块名称。  默认值：''。 |
| loadingStatus | boolean | 否 | 是 | 点击状态栏图标展开业务弹窗场景下是否加载动效。  默认值：false。  **说明：** loadingStatus为true时，打开弹窗时会显示加载动效；为false时，不会显示加载动效。  **起始版本：** 6.0.0(20) |

## StatusBarGroupMenu

type StatusBarGroupMenu = StatusBarMenuItem[]

状态栏图标右键菜单的分组菜单信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [StatusBarMenuItem](statusbar-extension-manager.md#statusbarmenuitem)[] | 菜单组的信息，可以包含多个一级菜单项。 |

## StatusBarMenuItem

状态栏图标右键菜单的一级菜单项信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.0(12)

| **名称** | **类型** | **只读** | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| title | string | 否 | 否 | 菜单项标题。  取值范围：无限制，超长显示省略号。 |
| menuAction | [StatusBarMenuAction](statusbar-extension-manager.md#statusbarmenuaction) | 否 | 是 | 菜单项行为信息。  默认值：undefined。  **说明：** 当前菜单行为仅支持打开应用内定义的UIAbility，且menuAction和subMenu两个参数不可同时缺省。 |
| subMenu | [StatusBarSubMenuItem](statusbar-extension-manager.md#statusbarsubmenuitem)[] | 否 | 是 | 一级菜单项的子菜单项。  默认值：undefined。  **说明：** 当前单个一级菜单项最多支持20个子菜单项。 |
| menuCode | string | 否 | 是 | 菜单项的唯一标识。  默认值: ''。  **说明：** 设置该属性后，需确保其值在菜单中全局唯一。若同时配置了menuAction的menuCode，该属性值将覆盖menuAction中的对应值。  **起始版本：** 6.1.1(24) |
| options | [StatusBarMenuItemOptions](statusbar-extension-manager.md#statusbarmenuitemoptions) | 否 | 是 | 菜单项的可选参数。  默认值：undefined。  **说明：** 支持配置菜单项的默认图标和选中图标。若菜单项包含二级菜单，其selected参数及selectedIcon配置将自动失效。  **起始版本：** 6.1.1(24) |

## StatusBarMenuAction

状态栏图标右键菜单的菜单项点击行为信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.0(12)

| **名称** | **类型** | **只读** | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| abilityName | string | 否 | 否 | 点击菜单项拉起的应用的Ability名称。  **说明：** 当前仅支持拉起UIAbility。 |
| moduleName | string | 否 | 是 | 点击菜单项拉起的应用的Ability所在的模块名称。  默认值：'' |
| notifyOnly | boolean | 否 | 是 | 图标右键菜单点击事件使能。  取值范围：  false：不使能，此时点击右键菜单无事件通知。  true：使能，此时点击右键菜单有事件通知。  默认值：false - 无右键菜单点击事件触发。  **说明：** 当使能和提供菜单menuCode时，支持通过监听[rightMenuClick](statusbar-extension-manager.md#statusbarmanageronrightmenuclick)事件处理图标右键菜单点击业务。  **起始版本：** 5.0.2(14) |
| menuCode(deprecated) | string | 否 | 是 | 图标右键菜单唯一标识。  默认值：''  **说明：** 需保证菜单标识的唯一性，用于区分不同菜单项。从5.0.2(14)开始支持，从6.1.1(24)开始废弃，建议使用[StatusBarMenuItem](statusbar-extension-manager.md#statusbarmenuitem)或者[StatusBarSubMenuItem](statusbar-extension-manager.md#statusbarsubmenuitem)的menuCode替代。如果同时设置StatusBarMenuItem或者StatusBarSubMenuItem的menuCode，该属性值会被覆盖。 |

## StatusBarSubMenuItem

状态栏图标右键菜单中的二级菜单项信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.0(12)

| **名称** | **类型** | **只读** | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| subTitle | string | 否 | 否 | 二级菜单项标题。  取值范围：无限制，超长显示省略号。 |
| menuAction | [StatusBarMenuAction](statusbar-extension-manager.md#statusbarmenuaction) | 否 | 否 | 菜单项行为信息。  **说明：** 当前菜单行为仅支持打开应用内定义的UIAbility。 |
| menuCode | string | 否 | 是 | 菜单项的唯一标识。  默认值: ''  **说明：** 设置该属性后，需确保其值在菜单中全局唯一。若同时配置了menuAction的menuCode，该属性值将覆盖menuAction中的对应值。  **起始版本：** 6.1.1(24) |
| options | [StatusBarMenuItemOptions](statusbar-extension-manager.md#statusbarmenuitemoptions) | 否 | 是 | 菜单项的可选参数。  默认值：undefined。  **说明：** 支持配置当前菜单项的默认显示图标、菜单项的选中态及选中时显示的图标。  **起始版本：** 6.1.1(24) |

## StatusBarItemIcon

菜单项中显示的图标，继承自[StatusBarIcon](statusbar-extension-manager.md#statusbaricon)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 6.1.1(24)

| **名称** | **类型** | **只读** | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| white | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | 否 | 系统深色模式下展示的图标，建议采用纯白色图标，支持JPEG、PNG、GIF、WebP、BMP、SVG、ICO、DNG等图片类型。  **说明：** 建议使用24vp \* 24vp的图片。 |
| black | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | 否 | 系统浅色模式下展示的图标，建议采用纯黑色图标，支持JPEG、PNG、GIF、WebP、BMP、SVG、ICO、DNG等图片类型。  **说明：** 建议使用24vp \* 24vp的图片。 |

## StatusBarMenuItemOptions

菜单项的可选参数，支持配置菜单项的默认显示图标、及选中时显示的图标。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 6.1.1(24)

| **名称** | **类型** | **只读** | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| icon | [StatusBarItemIcon](statusbar-extension-manager.md#statusbaritemicon) | 否 | 是 | 菜单项默认显示的图标。  默认值：undefined |
| selected | boolean | 否 | 是 | 菜单项是否选中。  默认值：false  **说明：** selected为true时，会显示选中图标，如果配置了selectedIcon，则会显示selectedIcon中配置的图标，否则会显示系统默认的选中图标；selected为false时，不会显示选中图标。 |
| selectedIcon | [StatusBarItemIcon](statusbar-extension-manager.md#statusbaritemicon) | 否 | 是 | 菜单项选中时显示的图标。  默认值：undefined |

## statusBarManager.addToStatusBar

addToStatusBar(context: common.Context, statusBarItem: StatusBarItem): void

应用接入状态栏方法，当前同一个应用仅支持添加一个图标，重复添加无效。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。  **说明：** 当前context仅支持传入Context的子类[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)、ServiceExtensionContext、[FormExtensionContext](js-apis-inner-application-formextensioncontext.md)。 |
| statusBarItem | [StatusBarItem](statusbar-extension-manager.md#statusbaritem) | 是 | 应用自定义接入状态栏的图标的详细信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-statusbar-extension.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1010710001 | The size of the pixelmap exceeds the limit. |
| 1010710002 | The number of menu items or submenu items exceeds the limit. |
| 1010710003 | The API is being called too frequently. |
| 1010710005 | The string length exceeds the threshold.  适用版本：6.0.2(22)+ |
| 1010710007 | The menuCode of the menu item is not unique.  适用版本：6.1.1(24)+ |
| 1010720001 | A menu item contains neither submenu nor menuAction. |

**示例：**

```typescript
import { statusBarManager } from '@kit.DeskTopExtensionKit';
import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function addToStatusBar(context: Context) {
  if (!context) {
    console.error('getHostContext failed');
    return;
  }
  // 获取resourceManager资源管理器
  const resourceMgr: resourceManager.ResourceManager = context.resourceManager;

  // 创建white pixelMap，需在资源rawfile文件夹中预置testWhite.png图片，图片大小为24vp * 24vp
  const whiteFileData = resourceMgr.getRawFileContentSync('testWhite.png');
  const whiteBuffer = whiteFileData.buffer;
  const whiteImageSource = image.createImageSource(whiteBuffer);
  let whitePixelMap = await whiteImageSource.createPixelMap();

  // 创建black pixelMap，需在资源rawfile文件夹中预置testBlack.png图片，图片大小为24vp * 24vp
  const blackFileData = resourceMgr.getRawFileContentSync('testBlack.png');
  const blackBuffer = blackFileData.buffer;
  const blackImageSource = image.createImageSource(blackBuffer);
  let blackPixelMap = await blackImageSource.createPixelMap();

  // 构建图标信息
  let icon: statusBarManager.StatusBarIcon = {
    white: whitePixelMap,
    black: blackPixelMap
  }

  // 构建右键菜单项内容
  let subMenus: Array<statusBarManager.StatusBarSubMenuItem> = [];
  let subMenuItemAction: statusBarManager.StatusBarMenuAction = {
    abilityName: 'EntryAbility'
  }
  let subMenu: statusBarManager.StatusBarSubMenuItem = {
    subTitle: '子菜单项',
    menuAction: subMenuItemAction
  }
  subMenus.push(subMenu);

  let statusBarMenuItems: Array<statusBarManager.StatusBarMenuItem> = [];
  let menuItem: statusBarManager.StatusBarMenuItem = {
    title: '一级菜单项',
    // 一级menuAction和subMenu两项不可都缺省
    subMenu: subMenus
  };
  statusBarMenuItems.push(menuItem);

  let statusBarGroupMenus: Array<statusBarManager.StatusBarGroupMenu> = [];
  statusBarGroupMenus.push(statusBarMenuItems);

  // 构建左键业务弹窗信息
  let operation: statusBarManager.QuickOperation = {
    abilityName: 'MyStatusBarViewAbility',
    title: '测试Demo',
    height: 300,
    // 可缺省
    moduleName: 'entry'
  };

  // 构建添加到状态栏的图标详细信息
  let item: statusBarManager.StatusBarItem = {
    icons: icon,
    quickOperation: operation,
    statusBarGroupMenu: statusBarGroupMenus
  };

  try {
    statusBarManager.addToStatusBar(context, item);
  } catch (error) {
    console.error(`addToStatusBar failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

## statusBarManager.addToStatusBar

addToStatusBar(context: common.Context, statusBarItem: StatusBarItem, callback: AsyncCallback<void>): void

应用接入状态栏方法，使用callback异步回调，当前同一个应用仅支持添加一个图标，重复添加无效。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。  **说明：** 当前context仅支持传入Context的子类[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)、ServiceExtensionContext、[FormExtensionContext](js-apis-inner-application-formextensioncontext.md)。 |
| statusBarItem | [StatusBarItem](statusbar-extension-manager.md#statusbaritem) | 是 | 应用自定义接入状态栏的图标的详细信息。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当添加图标到状态栏成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-statusbar-extension.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1010710001 | The size of the pixelmap exceeds the limit. |
| 1010710002 | The number of menu items or submenu items exceeds the limit. |
| 1010710003 | The API is being called too frequently. |
| 1010710005 | The string length exceeds the threshold.  适用版本：6.0.2(22)+ |
| 1010710007 | The menuCode of the menu item is not unique.  适用版本：6.1.1(24)+ |
| 1010720001 | A menu item contains neither submenu nor menuAction. |

**示例：**

```typescript
import { statusBarManager } from '@kit.DeskTopExtensionKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function addToStatusBar(context: Context) {
  if (!context) {
    console.error('getHostContext failed');
    return;
  }
  // 获取resourceManager资源管理器
  const resourceMgr: resourceManager.ResourceManager = context.resourceManager;

  // 创建white pixelMap，需在资源rawfile文件夹中预置testWhite.png图片，图片大小为24vp * 24vp
  const whiteFileData = resourceMgr.getRawFileContentSync('testWhite.png');
  const whiteBuffer = whiteFileData.buffer;
  const whiteImageSource = image.createImageSource(whiteBuffer);
  let whitePixelMap = await whiteImageSource.createPixelMap();

  // 创建black pixelMap，需在资源rawfile文件夹中预置testBlack.png图片，图片大小为24vp * 24vp
  const blackFileData = resourceMgr.getRawFileContentSync('testBlack.png');
  const blackBuffer = blackFileData.buffer;
  const blackImageSource = image.createImageSource(blackBuffer);
  let blackPixelMap = await blackImageSource.createPixelMap();

  // 构建图标信息
  let icon: statusBarManager.StatusBarIcon = {
    white: whitePixelMap,
    black: blackPixelMap
  }

  // 构建右键菜单项内容
  let subMenus: Array<statusBarManager.StatusBarSubMenuItem> = [];
  let subMenuItemAction: statusBarManager.StatusBarMenuAction = {
    abilityName: 'EntryAbility'
  }
  let subMenu: statusBarManager.StatusBarSubMenuItem = {
    subTitle: '子菜单项',
    menuAction: subMenuItemAction
  }
  subMenus.push(subMenu);

  let statusBarMenuItems: Array<statusBarManager.StatusBarMenuItem> = [];
  let menuItem: statusBarManager.StatusBarMenuItem = {
    title: '一级菜单项',
    // 一级menuAction和subMenu两项不可都缺省
    subMenu: subMenus
  };
  statusBarMenuItems.push(menuItem);

  let statusBarGroupMenus: Array<statusBarManager.StatusBarGroupMenu> = [];
  statusBarGroupMenus.push(statusBarMenuItems);

  // 构建左键业务弹窗信息
  let operation: statusBarManager.QuickOperation = {
    abilityName: 'MyStatusBarViewAbility',
    title: '测试Demo',
    height: 300,
    // 可缺省
    moduleName: 'entry'
  };

  // 构建添加到状态栏的图标详细信息
  let item: statusBarManager.StatusBarItem = {
    icons: icon,
    quickOperation: operation,
    statusBarGroupMenu: statusBarGroupMenus
  };

  try {
    statusBarManager.addToStatusBar(context, item, (error: BusinessError) => {
      if (error) {
        // ...
        return;
      }
      console.info('addToStatusBar success');
    });
  } catch (error) {
    console.error(`addToStatusBar failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

## statusBarManager.removeFromStatusBar

removeFromStatusBar(context: common.Context): void

应用移除状态栏对应图标方法。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。  **说明：** 当前context仅支持传入Context的子类[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)、ServiceExtensionContext、[FormExtensionContext](js-apis-inner-application-formextensioncontext.md)。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-statusbar-extension.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1010710003 | The API is being called too frequently. |
| 1010710004 | The icon cannot be deleted when no window is in the foreground. |

**示例：**

```typescript
import { statusBarManager } from '@kit.DeskTopExtensionKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
function removeFromStatusBar(context: Context) {
  if (!context) {
    console.error('getHostContext failed');
    return;
  }
  try {
    statusBarManager.removeFromStatusBar(context);
  } catch (error) {
    console.error(`removeFromStatusBar failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

## statusBarManager.removeFromStatusBar

removeFromStatusBar(context: common.Context, callback: AsyncCallback<void>): void

应用移除状态栏对应图标方法，使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。  **说明：** 当前context仅支持传入Context的子类[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)、ServiceExtensionContext、[FormExtensionContext](js-apis-inner-application-formextensioncontext.md)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当从状态栏移除图标成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-statusbar-extension.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1010710003 | The API is being called too frequently. |
| 1010710004 | The icon cannot be deleted when no window is in the foreground. |

**示例：**

```typescript
import { statusBarManager } from '@kit.DeskTopExtensionKit';
import { BusinessError } from '@kit.BasicServicesKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
function removeFromStatusBar(context: Context) {
  if (!context) {
    console.error('getHostContext failed');
    return;
  }
  try {
    statusBarManager.removeFromStatusBar(context, (error: BusinessError) => {
      if (error) {
        // ...
        return;
      }
      console.info('removeFromStatusBar success');
    });
  } catch (error) {
    console.error(`removeFromStatusBar failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

## statusBarManager.updateQuickOperationHeight

updateQuickOperationHeight(context: common.Context, height: number): void

应用更新状态栏图标的左键弹窗应用定制区域高度。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。  **说明：** 当前context仅支持传入Context的子类[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)、ServiceExtensionContext、[FormExtensionContext](js-apis-inner-application-formextensioncontext.md)。 |
| height | number | 是 | 状态栏图标左键的应用面板自定义区域高度，单位：vp。  取值范围：大于0。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-statusbar-extension.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1010710003 | The API is being called too frequently. |

**示例：**

```typescript
import { statusBarManager } from '@kit.DeskTopExtensionKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
function updateQuickOperationHeight(context: Context) {
  if (!context) {
    console.error('getHostContext failed');
    return;
  }
  let height = 200;
  try {
    statusBarManager.updateQuickOperationHeight(context, height);
  } catch (error) {
    console.error(`updateQuickOperationHeight failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

## statusBarManager.updateQuickOperationHeight

updateQuickOperationHeight(context: common.Context, height: number, callback: AsyncCallback<void>): void

应用更新状态栏图标的左键弹窗应用定制区域高度，使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。  **说明：** 当前context仅支持传入Context的子类[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)、ServiceExtensionContext、[FormExtensionContext](js-apis-inner-application-formextensioncontext.md)。 |
| height | number | 是 | 状态栏图标左键的应用面板自定义区域高度，单位：vp。  取值范围：大于0。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当更新状态栏图标的左键弹窗应用定制区域高度成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-statusbar-extension.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1010710003 | The API is being called too frequently. |

**示例：**

```typescript
import { statusBarManager } from '@kit.DeskTopExtensionKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
function updateQuickOperationHeight(context: Context) {
  if (!context) {
    console.error('getHostContext failed');
    return;
  }
  let height = 200;
  try {
    statusBarManager.updateQuickOperationHeight(context, height, (error) => {
      if (error) {
        // ...
        return;
      }
      console.info('updateQuickOperationHeight success');
    });
  } catch (error) {
    console.error(`updateQuickOperationHeight failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

## statusBarManager.updateStatusBarMenu

updateStatusBarMenu(context: common.Context, statusBarGroupMenus: StatusBarGroupMenu[]): void

应用更新状态栏图标的右键菜单内容。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。  **说明：** 当前context仅支持传入Context的子类[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)、ServiceExtensionContext、[FormExtensionContext](js-apis-inner-application-formextensioncontext.md)。 |
| statusBarGroupMenus | [StatusBarGroupMenu](statusbar-extension-manager.md#statusbargroupmenu)[] | 是 | 更新后的应用右键菜单栏相关信息。  **说明：** 当前所有分组下一级菜单项的总和不可超过20个。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-statusbar-extension.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1010710002 | The number of menu items or submenu items exceeds the limit. |
| 1010710003 | The API is being called too frequently. |
| 1010710007 | The menuCode of the menu item is not unique.  适用版本：6.1.1(24)+ |
| 1010720001 | A menu item contains neither submenu nor menuAction. |

**示例：**

```typescript
import { statusBarManager } from '@kit.DeskTopExtensionKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
function updateStatusBarMenu(context: Context) {
  // 构建右键菜单项内容
  let subMenus: Array<statusBarManager.StatusBarSubMenuItem> = [];
  let subMenuItemAction: statusBarManager.StatusBarMenuAction = {
    abilityName: 'EntryAbility'
  }
  let subMenu: statusBarManager.StatusBarSubMenuItem = {
    subTitle: '二级菜单项',
    menuAction: subMenuItemAction
  }
  subMenus.push(subMenu);
  let statusBarMenuItems: Array<statusBarManager.StatusBarMenuItem> = [];
  let menuItem: statusBarManager.StatusBarMenuItem = {
    title: '一级菜单项',
    // 一级menuAction和subMenu两项不可都缺省
    subMenu: subMenus
  };
  statusBarMenuItems.push(menuItem);
  let statusBarGroupMenus: Array<statusBarManager.StatusBarGroupMenu> = [];
  statusBarGroupMenus.push(statusBarMenuItems);
  if (!context) {
    console.error('getHostContext failed');
    return;
  }
  try {
    statusBarManager.updateStatusBarMenu(context, statusBarGroupMenus);
  } catch (error) {
    console.error(`updateStatusBarMenu failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

## statusBarManager.updateStatusBarMenu

updateStatusBarMenu(context: common.Context, statusBarGroupMenus: StatusBarGroupMenu[], callback: AsyncCallback<void>): void

应用更新状态栏图标的右键菜单内容，使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。  **说明：** 当前context仅支持传入Context的子类[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)、ServiceExtensionContext、[FormExtensionContext](js-apis-inner-application-formextensioncontext.md)。 |
| statusBarGroupMenus | [StatusBarGroupMenu](statusbar-extension-manager.md#statusbargroupmenu)[] | 是 | 更新后的应用右键菜单栏相关信息。  **说明：** 当前所有分组下一级菜单项的总和不可超过20个。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当更新状态栏图标的右键菜单内容成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-statusbar-extension.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1010710002 | The number of menu items or submenu items exceeds the limit. |
| 1010710003 | The API is being called too frequently. |
| 1010710007 | The menuCode of the menu item is not unique.  适用版本：6.1.1(24)+ |
| 1010720001 | A menu item contains neither submenu nor menuAction. |

**示例：**

```typescript
import { statusBarManager } from '@kit.DeskTopExtensionKit';
import { BusinessError } from '@kit.BasicServicesKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
function updateStatusBarMenu(context: Context) {
  // 构建右键菜单项内容
  let subMenus: Array<statusBarManager.StatusBarSubMenuItem> = [];
  let subMenuItemAction: statusBarManager.StatusBarMenuAction = {
    abilityName: 'EntryAbility'
  }
  let subMenu: statusBarManager.StatusBarSubMenuItem = {
    subTitle: '二级菜单项',
    menuAction: subMenuItemAction
  }
  subMenus.push(subMenu);
  let statusBarMenuItems: Array<statusBarManager.StatusBarMenuItem> = [];
  let menuItem: statusBarManager.StatusBarMenuItem = {
    title: '一级菜单项',
    // 一级menuAction和subMenu两项不可都缺省
    subMenu: subMenus
  };
  statusBarMenuItems.push(menuItem);
  let statusBarGroupMenus: Array<statusBarManager.StatusBarGroupMenu> = [];
  statusBarGroupMenus.push(statusBarMenuItems);
  if (!context) {
    console.error('getHostContext failed');
    return;
  }
  try {
    statusBarManager.updateStatusBarMenu(context, statusBarGroupMenus, (err: BusinessError) => {
      if (err) {
        // ...
        return;
      }
      console.info('updateStatusBarMenu success');
    });
  } catch (error) {
    console.error(`updateStatusBarMenu failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

## statusBarManager.updateStatusBarIcon

updateStatusBarIcon(context: common.Context, statusBarIcon: StatusBarIcon): void

应用更新接入状态栏的图标。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。  **说明：** 当前context仅支持传入Context的子类[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)、ServiceExtensionContext、[FormExtensionContext](js-apis-inner-application-formextensioncontext.md)。 |
| statusBarIcon | [StatusBarIcon](statusbar-extension-manager.md#statusbaricon) | 是 | 更新的图标。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-statusbar-extension.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1010710001 | The size of the pixelmap exceeds the limit. |
| 1010710003 | The API is being called too frequently. |

**示例：**

```typescript
import { statusBarManager } from '@kit.DeskTopExtensionKit';
import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function updateStatusBarIcon(context: Context) {
  if (!context) {
    console.error('getHostContext failed');
    return;
  }
  // 获取resourceManager资源管理器
  const resourceMgr: resourceManager.ResourceManager = context.resourceManager;

  // 创建white pixelMap，需在资源rawfile文件夹中预置testWhite.png图片，图片大小为24vp * 24vp
  const whiteFileData = resourceMgr.getRawFileContentSync('testWhite.png');
  const whiteBuffer = whiteFileData.buffer;
  const whiteImageSource = image.createImageSource(whiteBuffer);
  let whitePixelMap = await whiteImageSource.createPixelMap();

  // 创建black pixelMap，需在资源rawfile文件夹中预置testBlack.png图片，图片大小为24vp * 24vp
  const blackFileData = resourceMgr.getRawFileContentSync('testBlack.png');
  const blackBuffer = blackFileData.buffer;
  const blackImageSource = image.createImageSource(blackBuffer);
  let blackPixelMap = await blackImageSource.createPixelMap();

  // 构建图标信息
  let icons: statusBarManager.StatusBarIcon = {
    white: whitePixelMap,
    black: blackPixelMap
  }

  try {
    statusBarManager.updateStatusBarIcon(context, icons);
  } catch (error) {
    console.error(`updateStatusBarIcon failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

## statusBarManager.updateStatusBarIcon

updateStatusBarIcon(context: common.Context, statusBarIcon: StatusBarIcon, callback: AsyncCallback<void>): void

应用更新接入状态栏的图标，使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。  **说明：** 当前context仅支持传入Context的子类[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)、ServiceExtensionContext、[FormExtensionContext](js-apis-inner-application-formextensioncontext.md)。 |
| statusBarIcon | [StatusBarIcon](statusbar-extension-manager.md#statusbaricon) | 是 | 更新的图标。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当更新接入状态栏的图标成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-statusbar-extension.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1010710001 | The size of the pixelmap exceeds the limit. |
| 1010710003 | The API is being called too frequently. |

**示例：**

```typescript
import { statusBarManager } from '@kit.DeskTopExtensionKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function updateStatusBarIcon(context: Context) {
  if (!context) {
    console.error('getHostContext failed');
    return;
  }
  // 获取resourceManager资源管理器
  const resourceMgr: resourceManager.ResourceManager = context.resourceManager;

  // 创建white pixelMap，需在资源rawfile文件夹中预置testWhite.png图片，图片大小为24vp * 24vp
  const whiteFileData = resourceMgr.getRawFileContentSync('testWhite.png');
  const whiteBuffer = whiteFileData.buffer;
  const whiteImageSource = image.createImageSource(whiteBuffer);
  let whitePixelMap = await whiteImageSource.createPixelMap();

  // 创建black pixelMap，需在资源rawfile文件夹中预置testBlack.png图片，图片大小为24vp * 24vp
  const blackFileData = resourceMgr.getRawFileContentSync('testBlack.png');
  const blackBuffer = blackFileData.buffer;
  const blackImageSource = image.createImageSource(blackBuffer);
  let blackPixelMap = await blackImageSource.createPixelMap();

  // 构建图标信息
  let icons: statusBarManager.StatusBarIcon = {
    white: whitePixelMap,
    black: blackPixelMap
  }

  try {
    statusBarManager.updateStatusBarIcon(context, icons, (error: BusinessError) => {
      if (error) {
        // ...
        return;
      }
      console.info('updateStatusBarIcon success');
    });
  } catch (error) {
    console.error(`updateStatusBarIcon failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

## statusBarManager.on('statusBarIconClick')

on(type: 'statusBarIconClick', callback: Callback<emitter.EventData>): void

监听状态栏图标点击事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'statusBarIconClick'，当点击应用图标时，触发该事件。  **说明：** 当调用[addToStatusBar](statusbar-extension-manager.md#statusbarmanageraddtostatusbar)，入参[quickOperation](statusbar-extension-manager.md#quickoperation)未指定abilityName时，支持通过监听statusBarIconClick事件处理点击业务。 |
| callback | Callback<[emitter.EventData](js-apis-emitter.md#eventdata)> | 是 | 需要注册的回调函数，返回信息为图标点击相关信息。  当前仅支持返回iconClickType（点击事件类型）中的leftClick（左键）。 |

**示例：**

```typescript
import { emitter } from '@kit.BasicServicesKit';
import { statusBarManager } from '@kit.DeskTopExtensionKit';

function statusBarIconClickOnTest() {
  let onStatusBarIconClick = (eventData: emitter.EventData) => {
    // 自定义图标点击业务
    let data = eventData.data;
    if (data) {
      switch (data['iconClickType']) {
        case 'leftClick':
          // 自定义左键点击业务
          break;
        default:
          break;
      }
    }
  }

  // 监听状态栏图标点击事件
  statusBarManager.on('statusBarIconClick', onStatusBarIconClick);
}
```

## statusBarManager.off('statusBarIconClick')

off(type: 'statusBarIconClick', callback?: Callback<emitter.EventData>): void

注销状态栏图标点击事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消事件回调类型，支持的事件为'statusBarIconClick' |
| callback | Callback<[emitter.EventData](js-apis-emitter.md#eventdata)> | 否 | 取消该事件的回调处理函数。  默认值：undefined。  **说明：**  若不传入callback，会取消该事件的所有回调函数；  若传入callback，需要传入对应on方法相同的对象，否则会导致回调函数未成功注销，导致内存泄露。 |

**示例：**

```typescript
import { emitter } from '@kit.BasicServicesKit';
import { statusBarManager } from '@kit.DeskTopExtensionKit';

function statusBarIconClickOffTest() {
  let onStatusBarIconClick = (eventData: emitter.EventData) => {
    // 自定义图标点击业务
    let data = eventData.data;
    if (data) {
      switch (data['iconClickType']) {
        case 'leftClick':
          // 自定义左键点击业务
          break;
        default:
          break;
      }
    }
  }
  // 取消事件回调处理函数
  statusBarManager.off('statusBarIconClick', onStatusBarIconClick);

  // 注销事件监听
  statusBarManager.off('statusBarIconClick');
}
```

## statusBarManager.on('rightMenuClick')

on(type: 'rightMenuClick', callback: Callback<emitter.EventData>): void

监听状态栏图标右键菜单点击事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'rightMenuClick'，当点击应用图标右键菜单时，触发该事件。  **说明：** 当调用[updateStatusBarMenu](statusbar-extension-manager.md#statusbarmanagerupdatestatusbarmenu)，添加菜单项时，指定[menuAction](statusbar-extension-manager.md#statusbarmenuaction)的notifyOnly使能和菜单项menuCode时生效。 |
| callback | Callback<[emitter.EventData](js-apis-emitter.md#eventdata)> | 是 | 需要注册的回调函数，返回信息为图标右键菜单点击相关信息。  当前返回信息menuCode（点击菜单项唯一标识）。 |

**示例：**

```typescript
import { emitter } from '@kit.BasicServicesKit';
import { statusBarManager } from '@kit.DeskTopExtensionKit';

function rightMenuClickOnTest() {
  let onRightMenuClick = (eventData: emitter.EventData) => {
    // 自定义图标右键菜单点击业务
    let data = eventData.data;
    if (data) {
      let menuCode = data['menuCode'] as string;
      // 处理点击菜单项业务
    }
  }

  // 监听右键菜单点击事件
  statusBarManager.on('rightMenuClick', onRightMenuClick);
}
```

## statusBarManager.off('rightMenuClick')

off(type: 'rightMenuClick', callback?: Callback<emitter.EventData>): void

注销状态栏图标右键菜单点击事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消事件回调类型，支持的事件为'rightMenuClick'。 |
| callback | Callback<[emitter.EventData](js-apis-emitter.md#eventdata)> | 否 | 取消该事件的回调处理函数。  默认值：undefined。  **说明：**  若不传入callback，会取消该事件的所有回调函数；  若传入callback，需要传入对应on方法相同的对象，否则会导致回调函数未成功注销，导致内存泄露。 |

**示例：**

```typescript
import { emitter } from '@kit.BasicServicesKit';
import { statusBarManager } from '@kit.DeskTopExtensionKit';

function rightMenuClickOffTest() {
  let onRightMenuClick = (eventData: emitter.EventData) => {
    // 自定义图标右键菜单点击业务
    let data = eventData.data;
    if (data) {
      let menuCode = data['menuCode'] as string;
      // 处理点击菜单项业务
    }
  }

  // 取消事件回调处理函数
  statusBarManager.off('rightMenuClick', onRightMenuClick);

  // 注销事件监听
  statusBarManager.off('rightMenuClick');
}
```

## statusBarManager.updateStatusBarHoverTips

updateStatusBarHoverTips(context: common.Context, hoverTips: string): Promise<void>

更新状态栏图标hover时显示内容。使用promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 6.0.2(22)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。  **说明：** 当前context仅支持传入Context的子类[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)、ServiceExtensionContext、[FormExtensionContext](js-apis-inner-application-formextensioncontext.md)。 |
| hoverTips | string | 是 | 状态栏图标hover时的显示信息。  字符串长度范围：1~128。  **说明：** 超出取值范围会抛错误码1010710005。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-statusbar-extension.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1010710003 | The API is being called too frequently. |
| 1010710005 | The string length exceeds the threshold. |

**示例：**

```typescript
import { statusBarManager } from '@kit.DeskTopExtensionKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function updateStatusBarHoverTips(context: Context) {
  if (!context) {
    console.error('getHostContext failed');
    return;
  }
  let hoverTips: string = 'hoverTips';
  try {
    await statusBarManager.updateStatusBarHoverTips(context, hoverTips);
  } catch (error) {
    console.error(`updateStatusBarHoverTips failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

## statusBarManager.updateStatusBarMenuItem

updateStatusBarMenuItem(context: common.Context, item: StatusBarMenuItem): Promise<void>

更新单个一级菜单项的内容。使用promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 6.1.1(24)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。  **说明：** 当前context仅支持传入Context的子类[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)、ServiceExtensionContext、[FormExtensionContext](js-apis-inner-application-formextensioncontext.md)。 |
| item | [StatusBarMenuItem](statusbar-extension-manager.md#statusbarmenuitem) | 是 | 更新后的菜单项内容。  **说明：** item的menuCode属性值需要已经存在于当前的一级菜单项中（不能为''），会根据item的menuCode属性值作为唯一标识，匹配更新当前已经存在的一级菜单项内容。更新一级菜单时会同步更新该一级菜单下的所有二级菜单项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-statusbar-extension.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1010710002 | The number of menu items or submenu items exceeds the limit. |
| 1010710003 | The API is being called too frequently. |
| 1010710006 | Menu item not found. |
| 1010710007 | The menuCode of the menu item is not unique. |
| 1010720001 | A menu item contains neither submenu nor menuAction. |

**示例：**

```typescript
import { statusBarManager } from '@kit.DeskTopExtensionKit';
import { resourceManager } from '@kit.LocalizationKit';
import { image } from '@kit.ImageKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function updateStatusBarMenuItemTest(context: Context) {
  if (!context) {
    console.error('getHostContext failed');
    return;
  }
  // 获取resourceManager资源管理器
  const resourceMgr: resourceManager.ResourceManager = context.resourceManager;

  // 创建white pixelMap，需在资源rawfile文件夹中预置testWhite.png图片，图片大小为24vp * 24vp
  const whiteFileData = resourceMgr.getRawFileContentSync('testWhite.png');
  const whiteBuffer = whiteFileData.buffer;
  const whiteImageSource = image.createImageSource(whiteBuffer);
  let whitePixelMap = await whiteImageSource.createPixelMap();

  // 创建black pixelMap，需在资源rawfile文件夹中预置testBlack.png图片，图片大小为24vp * 24vp
  const blackFileData = resourceMgr.getRawFileContentSync('testBlack.png');
  const blackBuffer = blackFileData.buffer;
  const blackImageSource = image.createImageSource(blackBuffer);
  let blackPixelMap = await blackImageSource.createPixelMap();

  // 构建图标信息
  let icon: statusBarManager.StatusBarItemIcon = {
    white: whitePixelMap,
    black: blackPixelMap
  }
  let menuItemOptions: statusBarManager.StatusBarMenuItemOptions = {
    icon: icon,
    selected: true
  }
  let menuAction: statusBarManager.StatusBarMenuAction = {
    abilityName: 'EntryAbility'
  }
  let menuItemTmp: statusBarManager.StatusBarMenuItem = {
    title: 'menuItem',
    // 当前的menuCode需要已经存在于已有的一级菜单中
    menuCode: '0',
    // 一级菜单项的menuAction和subMenu两项不可同时缺省
    menuAction: menuAction,
    options: menuItemOptions
  }
  try {
    await statusBarManager.updateStatusBarMenuItem(context, menuItemTmp);
  } catch (e) {
    console.error(`updateStatusBarMenuItem failed. error code: ${e?.code}, error message: ${e?.message}`);
  }
}
```

## statusBarManager.updateStatusBarSubMenuItem

updateStatusBarSubMenuItem(context: common.Context, item: StatusBarSubMenuItem): Promise<void>

更新单个二级菜单项的内容。使用promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 6.1.1(24)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。  **说明：** 当前context仅支持传入Context的子类[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)、ServiceExtensionContext、[FormExtensionContext](js-apis-inner-application-formextensioncontext.md)。 |
| item | [StatusBarSubMenuItem](statusbar-extension-manager.md#statusbarsubmenuitem) | 是 | 更新后的菜单项内容。  **说明：** item的menuCode属性需要已经存在于当前的二级菜单项中（不能为''），会根据item的menuCode属性值作为唯一标识，匹配更新当前已经存在的二级菜单项内容。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-statusbar-extension.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1010710003 | The API is being called too frequently. |
| 1010710006 | Menu item not found. |

**示例：**

```typescript
import { statusBarManager } from '@kit.DeskTopExtensionKit';
import { resourceManager } from '@kit.LocalizationKit';
import { image } from '@kit.ImageKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function updateStatusBarSubMenuItemTest(context: Context) {
  if (!context) {
    console.error('getHostContext failed');
    return;
  }
  // 获取resourceManager资源管理器
  const resourceMgr: resourceManager.ResourceManager = context.resourceManager;

  // 创建white pixelMap，需在资源rawfile文件夹中预置testWhite.png图片，图片大小为24vp * 24vp
  const whiteFileData = resourceMgr.getRawFileContentSync('testWhite.png');
  const whiteBuffer = whiteFileData.buffer;
  const whiteImageSource = image.createImageSource(whiteBuffer);
  let whitePixelMap = await whiteImageSource.createPixelMap();

  // 创建black pixelMap，需在资源rawfile文件夹中预置testBlack.png图片，图片大小为24vp * 24vp
  const blackFileData = resourceMgr.getRawFileContentSync('testBlack.png');
  const blackBuffer = blackFileData.buffer;
  const blackImageSource = image.createImageSource(blackBuffer);
  let blackPixelMap = await blackImageSource.createPixelMap();

  // 构建图标信息
  let icon: statusBarManager.StatusBarItemIcon = {
    white: whitePixelMap,
    black: blackPixelMap
  }
  let subMenuItemOptions: statusBarManager.StatusBarMenuItemOptions = {
    icon: icon,
    selected: true
  }
  let menuAction: statusBarManager.StatusBarMenuAction = {
    abilityName: 'EntryAbility'
  }
  let subMenuItemTmp: statusBarManager.StatusBarSubMenuItem = {
    subTitle: 'menuItem',
    // 当前的menuCode需要存在于已有的二级菜单项中
    menuCode: '00',
    menuAction: menuAction,
    // 支持设置图标信息及当前菜单项是否选中
    options: subMenuItemOptions
  }
  try {
    await statusBarManager.updateStatusBarSubMenuItem(context, subMenuItemTmp);
  } catch (e) {
    console.error(`updateStatusBarSubMenuItem failed. error code: ${e?.code}, error message: ${e?.message}`);
  }
}
```

## statusBarManager.isStatusBarCapabilitySupported

isStatusBarCapabilitySupported(context: common.Context): Promise<boolean>

检查是否支持状态栏能力。使用promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文信息。  **说明：** 当前context仅支持传入Context的子类[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)、ServiceExtensionContext、[FormExtensionContext](js-apis-inner-application-formextensioncontext.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示支持状态栏能力；返回false表示不支持。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-statusbar-extension.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1010710003 | The API is being called too frequently. |

**示例：**

```typescript
import { statusBarManager } from '@kit.DeskTopExtensionKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function isStatusBarCapabilitySupportedTest(context: Context) {
  if (!context) {
    console.error('getHostContext failed');
    return;
  }
  try {
    let isSupported = await statusBarManager.isStatusBarCapabilitySupported(context);
    if (isSupported) {
      console.info('The status bar capability is supported.');
    } else {
      console.info('The status bar capability is not supported.');
    }
  } catch (error) {
    console.error(`isStatusBarCapabilitySupported failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

## statusBarManager.onIconHover

onIconHover(callback: Callback<emitter.EventData>): void

监听状态栏图标悬浮事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[emitter.EventData](js-apis-emitter.md#eventdata)> | 是 | 需要注册的回调函数，返回图标悬浮状态信息。 |

**示例：**

```typescript
import { emitter } from '@kit.BasicServicesKit';
import { statusBarManager } from '@kit.DeskTopExtensionKit';
 
function onIconHoverTest() {
  let onIconHoverChange = (eventData: emitter.EventData) => {
    let data = eventData.data;
    if (data) {
      let isHovered = data['isHovered'] as boolean;
      // 处理图标悬浮业务
    }
  };
 
  statusBarManager.onIconHover(onIconHoverChange);
}
```

## statusBarManager.offIconHover

offIconHover(callback?: Callback<emitter.EventData>): void

注销状态栏图标悬浮事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[emitter.EventData](js-apis-emitter.md#eventdata)> | 否 | 取消该事件的回调处理函数。  默认值：undefined。  **说明：**  若不传入callback，会取消该事件的所有回调函数。  若传入callback，需要传入对应[onIconHover](statusbar-extension-manager.md#statusbarmanageroniconhover)方法相同的对象，否则会导致回调函数未成功注销，导致内存泄露。 |

**示例：**

```typescript
import { emitter } from '@kit.BasicServicesKit';
import { statusBarManager } from '@kit.DeskTopExtensionKit';
 
function offIconHoverTest() {
  let onIconHoverChange = (eventData: emitter.EventData) => {
    let data = eventData.data;
    if (data) {
      let isHovered = data['isHovered'] as boolean;
      // 处理图标悬浮业务
    }
  };
 
  // 取消事件回调处理函数
  statusBarManager.offIconHover(onIconHoverChange);
 
  // 注销事件监听
  statusBarManager.offIconHover();
}
```
