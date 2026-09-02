---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/statusbar-extension-guide
title: 应用接入状态栏
breadcrumb: 指南 > 系统 > 基础功能 > Desktop Extension Kit（桌面拓展服务） > 应用接入状态栏
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:36+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:2349db481bb8669cd1467c23ebd29217dcaa5e3970fc92b08c874ab21f761a74
---

应用接入状态栏之后，状态栏会显示应用自定义的图标，图标提供左键显示自定义弹窗、右键显示菜单以及hover状态回调的功能；应用退出时，状态栏图标会随着应用进程的销毁而消失。

* 从API版本26.0.0开始，新增检查设备状态是否支持状态栏图标接入能力，以及图标悬浮（hover）状态回调能力。
* 从6.1.1(24)版本开始，右键菜单获得增强，菜单项支持分别设置默认图标与选中图标，并支持独立更新单个一级菜单项或二级菜单项的内容。
* 从6.0.2(22)版本开始，支持自定义状态栏图标在鼠标悬浮（hover）时显示的内容。

## 接口说明

以下列出应用接入状态栏的相关API，具体API说明详见[接口文档](../harmonyos-references/statusbar-extension-manager.md)。

**说明** 

Desktop Extension Kit（桌面拓展服务）相关API仅在PC/2in1设备上生效。

**表1** 应用接入状态栏相关功能接口介绍

| 接口名 | 描述 |
| --- | --- |
| [addToStatusBar](../harmonyos-references/statusbar-extension-manager.md#statusbarmanageraddtostatusbar)(context: common.Context, statusBarItem: StatusBarItem): void | 添加应用图标到状态栏。 |
| [removeFromStatusBar](../harmonyos-references/statusbar-extension-manager.md#statusbarmanagerremovefromstatusbar)(context: common.Context): void | 移除状态栏的应用图标。 |
| [updateQuickOperationHeight](../harmonyos-references/statusbar-extension-manager.md#statusbarmanagerupdatequickoperationheight)(context: common.Context, height: number): void | 更新状态栏图标左键弹窗应用定制区域的高度。 |
| [updateStatusBarMenu](../harmonyos-references/statusbar-extension-manager.md#statusbarmanagerupdatestatusbarmenu)(context: common.Context, statusBarGroupMenus: StatusBarGroupMenu[]): void | 更新接入状态栏图标的右键菜单内容。 |
| [updateStatusBarIcon](../harmonyos-references/statusbar-extension-manager.md#statusbarmanagerupdatestatusbaricon)(context: common.Context, statusBarIcon: StatusBarIcon): void | 更新状态栏图标。 |
| [updateStatusBarHoverTips](../harmonyos-references/statusbar-extension-manager.md#statusbarmanagerupdatestatusbarhovertips)(context: common.Context, hoverTips: string): Promise<void> | 更新状态栏图标hover时显示内容。 |
| [on](../harmonyos-references/statusbar-extension-manager.md#statusbarmanageronstatusbariconclick)(type: 'statusBarIconClick', callback: Callback<emitter.EventData>): void | 监听状态栏图标点击事件。 |
| [off](../harmonyos-references/statusbar-extension-manager.md#statusbarmanageroffstatusbariconclick)(type: 'statusBarIconClick', callback?: Callback<emitter.EventData>): void | 注销状态栏图标点击事件。 |
| [on](../harmonyos-references/statusbar-extension-manager.md#statusbarmanageronrightmenuclick)(type: 'rightMenuClick', callback: Callback<emitter.EventData>): void | 监听状态栏右键菜单点击事件。 |
| [off](../harmonyos-references/statusbar-extension-manager.md#statusbarmanageroffrightmenuclick)(type: 'rightMenuClick', callback?: Callback<emitter.EventData>): void | 注销状态栏右键菜单点击事件。 |
| [updateStatusBarMenuItem](../harmonyos-references/statusbar-extension-manager.md#statusbarmanagerupdatestatusbarmenuitem)(context: common.Context, item: StatusBarMenuItem): Promise<void> | 更新单个一级菜单项内容。 |
| [updateStatusBarSubMenuItem](../harmonyos-references/statusbar-extension-manager.md#statusbarmanagerupdatestatusbarsubmenuitem)(context: common.Context, item: StatusBarSubMenuItem): Promise<void> | 更新菜单项的单个二级菜单项内容。 |
| [isStatusBarCapabilitySupported](../harmonyos-references/statusbar-extension-manager.md#statusbarmanagerisstatusbarcapabilitysupported)(context: common.Context): Promise<boolean> | 检查是否支持状态栏能力。使用promise异步回调。 |
| [onIconHover](../harmonyos-references/statusbar-extension-manager.md#statusbarmanageroniconhover)(callback: Callback<emitter.EventData>): void | 监听状态栏图标悬浮（hover）事件。使用callback异步回调。 |
| [offIconHover](../harmonyos-references/statusbar-extension-manager.md#statusbarmanagerofficonhover)(callback?: Callback<emitter.EventData>): void | 注销状态栏图标悬浮（hover）事件。使用callback异步回调。 |

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { emitter } from '@kit.BasicServicesKit';
   import { statusBarManager } from '@kit.DeskTopExtensionKit';
   import { image } from '@kit.ImageKit';
   import { resourceManager } from '@kit.LocalizationKit';
   ```
2. 新建一个MyStatusBarViewAbility.ets文件（例如在entry/src/main/ets/statusbarviewextensionability文件夹下），同时新建一个StatusBarPage的页面（例如在entry/src/main/ets/pages目录下），该页面用于在状态栏图标的左键业务弹窗中显示，然后构建自定义的StatusBarViewExtensionAbility。

   ```typescript
   import { UIExtensionContentSession, Want } from '@kit.AbilityKit';
   import { StatusBarViewExtensionAbility } from '@kit.DeskTopExtensionKit';

   let TAG = 'MyStatusBarViewAbility';

   export default class MyStatusBarViewAbility extends StatusBarViewExtensionAbility {
     // 当StatusBarViewExtensionAbility组件实例完成创建时，系统会触发该回调。
     onCreate() {
       console.info(TAG, 'onCreate');
     }

     // 当UIExtensionContentSession实例创建完成后，系统会触发该回调。
     onSessionCreate(want: Want, session: UIExtensionContentSession) {
       console.info(TAG, `onSessionCreate, want: ${want.abilityName}`);
       // pages/StatusBarPage为状态栏图标左键业务弹窗显示的页面
       session.loadContent('pages/StatusBarPage');
     }

     // 当StatusBarViewExtensionAbility组件首次启动到前台或者从后台转入到前台时，系统触发该回调。
     onForeground() {
       console.info(TAG, 'onForeground');
     }

     // 当StatusBarViewExtensionAbility组件从前台转入到后台时，系统触发该回调。
     onBackground() {
       console.info(TAG, 'onBackground');
     }

     // 当UIExtensionContentSession实例销毁后，系统触发该回调。
     onSessionDestroy(session: UIExtensionContentSession) {
       console.info(TAG, 'onSessionDestroy');
     }

     // 当StatusBarViewExtensionAbility组件被销毁时，系统触发该回调。
     onDestroy() {
       console.info(TAG, 'onDestroy');
     }
   }
   ```
3. 在MyStatusBarViewAbility所在模块下的module.json5文件中配置状态栏扩展Ability的信息。

   ```json5
   "extensionAbilities": [
       {
           "name": "MyStatusBarViewAbility",
           "icon": "$media:startIcon",
           "description": "statusBar",
           "type": "statusBarView",
           "exported": true,
           // 此处为MyStatusBarViewAbility类所在的文件路径
           "srcEntry": "./ets/statusbarviewextensionability/MyStatusBarViewAbility.ets"
       }
   ],
   ```
4. 在对应模块的rawfile文件夹（例如entry/src/main/resources/rawfile）下预置两张24[vp](../harmonyos-references/ts-pixel-units.md) \* 24vp尺寸的图片（例如本示例中testWhite.svg和testBlack.svg两张图片），在页面组件内(如：index.ets)配置应用接入状态栏显示的图标信息。

   ```typescript
   /**
    * 可以通过自定义组件的内置方法获取Context信息
    * 具体方法：this.getUIContext().getHostContext();
    */
   if (!context) {
     console.error('getHostContext failed');
     return;
   }
   // 获取resourceManager资源管理器
   const resourceMgr: resourceManager.ResourceManager = context.resourceManager;

   // 创建white pixelMap，需在资源rawfile文件夹中预置testWhite.svg图片，图片大小为24vp * 24vp
   const whiteFileData = resourceMgr.getRawFileContentSync('testWhite.svg');
   const whiteBuffer = whiteFileData.buffer;
   const whiteImageSource = image.createImageSource(whiteBuffer);
   let whitePixelMap = await whiteImageSource.createPixelMap();

   // 创建black pixelMap，需在资源rawfile文件夹中预置testBlack.svg图片，图片大小为24vp * 24vp
   const blackFileData = resourceMgr.getRawFileContentSync('testBlack.svg');
   const blackBuffer = blackFileData.buffer;
   const blackImageSource = image.createImageSource(blackBuffer);
   let blackPixelMap = await blackImageSource.createPixelMap();

   // 构建图标信息
   let icon: statusBarManager.StatusBarIcon = {
     white: whitePixelMap,
     black: blackPixelMap
   }
   ```
5. 配置状态栏左键点击弹窗相关信息。

   ```typescript
   // 构建左键业务弹窗信息
   let operation: statusBarManager.QuickOperation = {
     abilityName: 'MyStatusBarViewAbility',
     title: 'TestDemo',
     height: 300,
     // 可缺省
     moduleName: 'entry'
   };
   ```
6. （可选）配置状态栏右键菜单内容信息，可在状态栏图标的右键菜单中增加自定义菜单选项。无论是否配置右键菜单，系统均会自动生成一个“退出”的菜单选项，该选项不支持应用自定义。若应用具备语言切换功能，该项的语言将遵循系统设置，而非应用内的语言设置。

   ```typescript
   // 构建右键菜单项内容
   let subMenus: statusBarManager.StatusBarSubMenuItem[] = [];
   let subMenuItemAction: statusBarManager.StatusBarMenuAction = {
     abilityName: 'EntryAbility'
   }
   let subMenu: statusBarManager.StatusBarSubMenuItem = {
     subTitle: '子菜单项',
     menuAction: subMenuItemAction
   }
   subMenus.push(subMenu);

   let statusBarMenuItems: statusBarManager.StatusBarMenuItem[] = [];
   let menuItem: statusBarManager.StatusBarMenuItem = {
     title: '一级菜单项',
     // 一级menuAction和subMenu两项不可都缺省
     subMenu: subMenus
   };
   statusBarMenuItems.push(menuItem);

   let statusBarGroupMenus: statusBarManager.StatusBarGroupMenu[] = [];
   statusBarGroupMenus.push(statusBarMenuItems);
   ```
7. 整合配置信息，调用[isStatusBarCapabilitySupported](../harmonyos-references/statusbar-extension-manager.md#statusbarmanagerisstatusbarcapabilitysupported)判断当前设备状态是否支持图标接入状态栏的能力，如果设备状态支持，则调用[addToStatusBar](../harmonyos-references/statusbar-extension-manager.md#statusbarmanageraddtostatusbar)将图标接入状态栏，显示应用图标；如果不支持，则调用addToStatusBar后，界面上无效果。

   ```typescript
   // 构建添加到状态栏的图标详细信息
   let item: statusBarManager.StatusBarItem = {
     icons: icon,
     quickOperation: operation,
     statusBarGroupMenu: statusBarGroupMenus,
     // 初始化时可以自定义hover时显示内容
     hoverTips: 'appName'
   };

   try {
     statusBarManager.addToStatusBar(context, item);
   } catch (error) {
     console.error(`addToStatusBar failed. error code: ${error.code}, error message: ${error.message}`);
   }
   ```
8. （可选）应用接入状态栏之后，可以通过[updateStatusBarMenu](../harmonyos-references/statusbar-extension-manager.md#statusbarmanagerupdatestatusbarmenu)接口更新状态栏的右键菜单。

   ```typescript
   /**
    * 可以通过自定义组件的内置方法获取Context信息
    * 具体方法：this.getUIContext().getHostContext();
    */
   function updateStatusBarMenuExample(context: Context) {
     // 构建右键菜单项内容
     let subMenus: statusBarManager.StatusBarSubMenuItem[] = [];
     let subMenuItemAction: statusBarManager.StatusBarMenuAction = {
       abilityName: 'EntryAbility'
     }
     let subMenu: statusBarManager.StatusBarSubMenuItem = {
       subTitle: '二级菜单项',
       menuAction: subMenuItemAction,
       menuCode: '00'
     }
     subMenus.push(subMenu);

     let statusBarMenuItems: statusBarManager.StatusBarMenuItem[] = [];
     let menuItem: statusBarManager.StatusBarMenuItem = {
       title: '一级菜单项',
       menuCode: '0',
       // 一级menuAction和subMenu两项不可都缺省
       subMenu: subMenus
     };
     statusBarMenuItems.push(menuItem);

     let statusBarGroupMenus: statusBarManager.StatusBarGroupMenu[] = [];
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
9. （可选）应用接入状态栏之后，可以通过[updateQuickOperationHeight](../harmonyos-references/statusbar-extension-manager.md#statusbarmanagerupdatequickoperationheight)接口更新状态栏图标左键业务弹窗的高度。

   ```typescript
   /**
    * 可以通过自定义组件的内置方法获取Context信息
    * 具体方法：this.getUIContext().getHostContext();
    */
   function updateQuickOperationHeightExample(context: Context) {
     if (!context) {
       console.error('getHostContext failed');
       return;
     }
     let height = 200;
     statusBarManager.updateQuickOperationHeight(context, height);
   }
   ```
10. （可选）应用接入状态栏之后，可以通过[updateStatusBarIcon](../harmonyos-references/statusbar-extension-manager.md#statusbarmanagerupdatestatusbaricon)接口将状态栏中对应的应用图标进行更改。

    ```typescript
    /**
     * 可以通过自定义组件的内置方法获取Context信息
     * 具体方法：this.getUIContext().getHostContext();
     */
    async function updateStatusBarIconExample(context: Context) {
      if (!context) {
        console.error('getHostContext failed');
        return;
      }
      // 获取resourceManager资源管理器
      const resourceMgr: resourceManager.ResourceManager = context.resourceManager;

      // 创建white pixelMap，需在资源rawfile文件夹中预置testWhite.svg图片，图片大小为24vp * 24vp
      const whiteFileData = resourceMgr.getRawFileContentSync('testWhite.svg');
      const whiteBuffer = whiteFileData.buffer;
      const whiteImageSource = image.createImageSource(whiteBuffer);
      let whitePixelMap = await whiteImageSource.createPixelMap();

      // 创建black pixelMap，需在资源rawfile文件夹中预置testBlack.svg图片，图片大小为24vp * 24vp
      const blackFileData = resourceMgr.getRawFileContentSync('testBlack.svg');
      const blackBuffer = blackFileData.buffer;
      const blackImageSource = image.createImageSource(blackBuffer);
      let blackPixelMap = await blackImageSource.createPixelMap();

      // 构建图标信息
      let icons: statusBarManager.StatusBarIcon = {
        white: whitePixelMap,
        black: blackPixelMap
      }
      statusBarManager.updateStatusBarIcon(context, icons);
    }
    ```
11. （可选）应用接入状态栏之后，且未指定图标[QuickOperation](../harmonyos-references/statusbar-extension-manager.md#quickoperation)的abilityName可以通过[on](../harmonyos-references/statusbar-extension-manager.md#statusbarmanageronstatusbariconclick)/[off](../harmonyos-references/statusbar-extension-manager.md#statusbarmanageroffstatusbariconclick)接口自定义状态栏图标左键业务。

    ```typescript
    function listenerLeftClickByOnOff() {
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

      // 注销状态栏图标点击事件,调用on之后最终需要调用off接口
      statusBarManager.off('statusBarIconClick', onStatusBarIconClick);
    }
    ```
12. （可选）应用接入状态栏之后，调用[updateStatusBarMenu](../harmonyos-references/statusbar-extension-manager.md#statusbarmanagerupdatestatusbarmenu)接口，指定菜单[StatusBarMenuAction](../harmonyos-references/statusbar-extension-manager.md#statusbarmenuaction)的notifyOnly使能和menuCode菜单项标识，可以通过[on](../harmonyos-references/statusbar-extension-manager.md#statusbarmanageronstatusbariconclick)/[off](../harmonyos-references/statusbar-extension-manager.md#statusbarmanageroffstatusbariconclick)接口自定义状态栏图标右键菜单点击业务。

    ```typescript
    function listenerRightClickByOnOff() {
      let onRightMenuClick = (eventData: emitter.EventData) => {
        // 自定义图标右键菜单点击业务
        let data = eventData.data;
        if (data) {
          let menuCode = data['menuCode'] as string;
          // 处理点击菜单项业务
        }
      }

      // 监听状态栏图标右键菜单点击事件
      statusBarManager.on('rightMenuClick', onRightMenuClick);

      // 注销状态栏图标右键菜单点击事件,调用on之后最终需要调用off接口
      statusBarManager.off('rightMenuClick', onRightMenuClick);
    }
    ```
13. （可选）应用接入状态栏之后，调用[updateStatusBarHoverTips](../harmonyos-references/statusbar-extension-manager.md#statusbarmanagerupdatestatusbarhovertips)接口可以自定义图标hover时的显示内容。

    ```typescript
    /**
     * 可以通过自定义组件的内置方法获取Context信息
     * 具体方法：this.getUIContext().getHostContext();
     */
    async function updateStatusBarHoverTipsExample(context: Context) {
      if (!context) {
        console.error('getHostContext failed');
        return;
      }
      let hoverTips: string = 'hoverTips';
      try {
        await statusBarManager.updateStatusBarHoverTips(context, hoverTips);
      } catch (error) {
        console.error(`updateStatusBarHoverTips ${error.message} ${error.code}`)
      }
    }
    ```
14. （可选）对于已接入状态栏的应用，如果存在菜单项并且某个一级菜单项已设置menuCode属性，则可调用[updateStatusBarMenuItem](../harmonyos-references/statusbar-extension-manager.md#statusbarmanagerupdatestatusbarmenuitem)接口，通过指定的menuCode来更新对应一级菜单项的内容。

    ```typescript
    /**
     * 可以通过自定义组件的内置方法获取Context信息
     * 具体方法：this.getUIContext().getHostContext();
     */
    async function updateStatusBarMenuItemExample(context: Context) {
      if (!context) {
        console.error('getHostContext failed');
        return;
      }
      // 获取resourceManager资源管理器
      const resourceMgr: resourceManager.ResourceManager = context.resourceManager;

      // 创建white pixelMap，需在资源rawfile文件夹中预置testWhite.svg图片，图片大小为24vp * 24vp
      const whiteFileData = resourceMgr.getRawFileContentSync('testWhite.svg');
      const whiteBuffer = whiteFileData.buffer;
      const whiteImageSource = image.createImageSource(whiteBuffer);
      let whitePixelMap = await whiteImageSource.createPixelMap();

      // 创建black pixelMap，需在资源rawfile文件夹中预置testBlack.svg图片，图片大小为24vp * 24vp
      const blackFileData = resourceMgr.getRawFileContentSync('testBlack.svg');
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
        title: 'menuItem after',
        // 当前的menuCode需要已经存在于已有的一级菜单中
        menuCode: '0',
        // 一级菜单项的menuAction和subMenu两项不可同时缺省
        menuAction: menuAction,
        // 支持设置图标及当前菜单项是否选中
        options: menuItemOptions
      }

      try {
        updateStatusBarMenuExample(context);
        await statusBarManager.updateStatusBarMenuItem(context, menuItemTmp);
      } catch (error) {
        console.error(`updateStatusBarMenuItem failed. error code: ${error?.code}, error message: ${error?.message}`);
      }
    }
    ```
15. （可选）对于已接入状态栏的应用，若其一级菜单项包含二级菜单，且二级菜单项已设置menuCode属性，则可调用[updateStatusBarSubMenuItem](../harmonyos-references/statusbar-extension-manager.md#statusbarmanagerupdatestatusbarsubmenuitem)接口，通过指定的menuCode来更新对应二级菜单项的内容。

    ```typescript
    /**
     * 可以通过自定义组件的内置方法获取Context信息
     * 具体方法：this.getUIContext().getHostContext();
     */
    async function updateStatusBarSubMenuItemExample(context: Context) {
      if (!context) {
        console.error('getHostContext failed');
        return;
      }
      // 获取resourceManager资源管理器
      const resourceMgr: resourceManager.ResourceManager = context.resourceManager;

      // 创建white pixelMap，需在资源rawfile文件夹中预置testWhite.svg图片，图片大小为24vp * 24vp
      const whiteFileData = resourceMgr.getRawFileContentSync('testWhite.svg');
      const whiteBuffer = whiteFileData.buffer;
      const whiteImageSource = image.createImageSource(whiteBuffer);
      let whitePixelMap = await whiteImageSource.createPixelMap();

      // 创建black pixelMap，需在资源rawfile文件夹中预置testBlack.svg图片，图片大小为24vp * 24vp
      const blackFileData = resourceMgr.getRawFileContentSync('testBlack.svg');
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
        // 支持设置图标及当前菜单项是否选中
        options: subMenuItemOptions
      }
      try {
        updateStatusBarMenuExample(context);
        await statusBarManager.updateStatusBarSubMenuItem(context, subMenuItemTmp);
      } catch (error) {
        console.error(`updateStatusBarSubMenuItem failed. error code: ${error?.code}, error message: ${error?.message}`);
      }
    }
    ```
16. （可选）应用接入状态栏之后，可以通过[onIconHover](../harmonyos-references/statusbar-extension-manager.md#statusbarmanageroniconhover)/[offIconHover](../harmonyos-references/statusbar-extension-manager.md#statusbarmanagerofficonhover)接口自定义状态栏图标悬浮（hover）业务。

    ```typescript
    let onIconHoverChange = (eventData: emitter.EventData) => {
      let data = eventData.data;
      if (data) {
        let isHovered = data['isHovered'] as boolean;
        // 处理图标悬浮业务
      }
    };

    // 监听状态栏图标悬浮事件
    statusBarManager.onIconHover(onIconHoverChange);

    // 取消事件回调处理函数
    statusBarManager.offIconHover(onIconHoverChange);
    ```

## 完整示例代码

完整示例代码请参见[状态栏开放服务](https://gitcode.com/HarmonyOS_Samples/DesktopExtensionKit-samplecode)。
