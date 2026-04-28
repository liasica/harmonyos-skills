---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/statusbar-extension-guide
title: 应用接入状态栏
breadcrumb: 指南 > 系统 > 基础功能 > Desktop Extension Kit（桌面拓展服务） > 应用接入状态栏
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8f7172aee36d87cda24ca612b22cb88666d035eacf0ece875b33b77e112395d9
---

应用接入状态栏之后，状态栏会显示应用自定义的图标，图标提供左键显示自定义弹窗以及右键显示菜单的功能；应用退出时，状态栏图标会随着应用进程的销毁而消失。

从6.0.2(22)版本开始支持更新状态栏图标hover时显示内容。

## 接口说明

以下列出应用接入状态栏的相关API，具体API说明详见[接口文档](../harmonyos-references/statusbar-extension-manager.md)。

说明

DeskTop Extension Kit（桌面拓展服务）相关API仅在2in1设备上生效。

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

## 开发步骤

1. 导入相关模块。

   ```
   1. import { statusBarManager, StatusBarViewExtensionAbility } from '@kit.DeskTopExtensionKit';
   2. import { UIExtensionContentSession, Want } from '@kit.AbilityKit';
   3. import { image } from '@kit.ImageKit';
   4. import { resourceManager } from '@kit.LocalizationKit';
   5. import { emitter } from '@kit.BasicServicesKit';
   ```
2. 新建一个MyStatusBarViewAbility.ets文件（例如在entry/src/main/ets/statusbarviewextensionability文件夹下），同时新建一个StatusBarPage的页面（例如在entry/src/main/ets/pages目录下），该页面用于在状态栏图标的左键业务弹窗中显示，然后构建自定义的StatusBarViewExtensionAbility。

   ```
   1. let TAG = 'MyStatusBarViewExtAbility';
   2. export default class MyStatusBarViewAbility extends StatusBarViewExtensionAbility {
   3. onCreate() {
   4. console.info(TAG, `onCreate`);
   5. }

   7. onSessionCreate(want: Want, session: UIExtensionContentSession) {
   8. console.info(TAG, `onSessionCreate, want: ${want.abilityName}`);
   9. // pages/StatusBarPage为状态栏图标左键业务弹窗显示的页面
   10. session.loadContent('pages/StatusBarPage');
   11. }

   13. onForeground() {
   14. console.info(TAG, `onForeground`);
   15. }

   17. onBackground() {
   18. console.info(TAG, `onBackground`);
   19. }

   21. onSessionDestroy(session: UIExtensionContentSession) {
   22. console.info(TAG, `onSessionDestroy`);
   23. }

   25. onDestroy() {
   26. console.info(TAG, `onDestroy`);
   27. }
   28. }
   ```
3. 在MyStatusBarViewAbility所在模块下的module.json5文件中配置状态栏扩展Ability的信息。

   ```
   1. "extensionAbilities": [
   2. {
   3. "name": "MyStatusBarViewAbility",
   4. "icon": "$media:startIcon",
   5. "description": "statusBar",
   6. "type": "statusBarView",
   7. "exported": true,
   8. // 此处为MyStatusBarViewAbility类所在的文件路径
   9. "srcEntry": "./ets/statusbarviewextensionability/MyStatusBarViewAbility.ets"
   10. }
   11. ]
   ```
4. 在对应模块的rawfile文件夹（例如entry/src/main/resources/rawfile）下预置两张24[vp](../harmonyos-references/ts-pixel-units.md) \* 24vp尺寸的图片（例如本示例中testWhite.png和testBlack.png两张图片），在页面组件内(如：index.ets)配置应用接入状态栏显示的图标信息。

   ```
   1. let context: Context | undefined = this.getUIContext().getHostContext();
   2. if (!context) {
   3. console.error('getHostContext failed');
   4. return;
   5. }
   6. // 获取resourceManager资源管理器
   7. const resourceMgr: resourceManager.ResourceManager = context.resourceManager;

   9. // 创建white pixelMap，需在资源rawfile文件夹中预置testWhite.png图片，图片大小为24vp * 24vp
   10. const whiteFileData = resourceMgr.getRawFileContentSync('testWhite.png');
   11. const whiteBuffer = whiteFileData.buffer;
   12. const whiteImageSource = image.createImageSource(whiteBuffer);
   13. let whitePixelMap = await whiteImageSource.createPixelMap();

   15. // 创建black pixelMap，需在资源rawfile文件夹中预置testBlack.png图片，图片大小为24vp * 24vp
   16. const blackFileData = resourceMgr.getRawFileContentSync('testBlack.png');
   17. const blackBuffer = blackFileData.buffer;
   18. const blackImageSource = image.createImageSource(blackBuffer);
   19. let blackPixelMap = await blackImageSource.createPixelMap();

   21. // 构建图标信息
   22. let icon: statusBarManager.StatusBarIcon = {
   23. white: whitePixelMap,
   24. black: blackPixelMap
   25. }
   ```
5. 配置状态栏左键点击弹窗相关信息。

   ```
   1. // 构建左键业务弹窗信息
   2. let operation: statusBarManager.QuickOperation = {
   3. // 此处abilityName为上述配置的module.json5中配置的自定义StatusBarViewExtensionAbility名称
   4. abilityName: "MyStatusBarViewAbility",
   5. title: "测试Demo",
   6. height: 300,
   7. // 可缺省
   8. moduleName: 'entry'
   9. };
   ```
6. （可选）配置状态栏右键菜单内容信息，可在状态栏图标的右键菜单中增加自定义菜单选项。

   ```
   1. // 构建右键菜单项内容
   2. let subMenus: Array<statusBarManager.StatusBarSubMenuItem> = [];
   3. let subMenuItemAction: statusBarManager.StatusBarMenuAction = {
   4. abilityName: "EntryAbility"
   5. }
   6. let subMenu: statusBarManager.StatusBarSubMenuItem = {
   7. subTitle: "子菜单项",
   8. menuAction: subMenuItemAction
   9. }
   10. subMenus.push(subMenu);

   12. let statusBarMenuItems: Array<statusBarManager.StatusBarMenuItem> = [];
   13. let menuItem: statusBarManager.StatusBarMenuItem = {
   14. title: "一级菜单项",
   15. // 一级menuAction和subMenu两项不可都缺省
   16. subMenu: subMenus
   17. };
   18. statusBarMenuItems.push(menuItem);

   20. let statusBarGroupMenus: Array<statusBarManager.StatusBarGroupMenu> = [];
   21. statusBarGroupMenus.push(statusBarMenuItems);
   ```
7. 整合配置信息，接入状态栏，显示应用图标。

   ```
   1. // 构建添加到状态栏的图标详细信息
   2. let item: statusBarManager.StatusBarItem = {
   3. icons: icon,
   4. quickOperation: operation,
   5. // 该参数可选
   6. statusBarGroupMenu: statusBarGroupMenus
   7. };

   9. try {
   10. statusBarManager.addToStatusBar(context, item);
   11. } catch (error) {
   12. console.error(`addToStatusBar failed. error code: ${error.code}, error message: ${error.message}`);
   13. }
   ```
8. （可选）应用接入状态栏之后，可以通过[updateStatusBarMenu](../harmonyos-references/statusbar-extension-manager.md#statusbarmanagerupdatestatusbarmenu)接口更新状态栏的右键菜单。

   ```
   1. // 构建右键菜单项内容
   2. let subMenus: Array<statusBarManager.StatusBarSubMenuItem> = [];
   3. let subMenuItemAction: statusBarManager.StatusBarMenuAction = {
   4. abilityName: "EntryAbility"
   5. }
   6. let subMenu: statusBarManager.StatusBarSubMenuItem = {
   7. subTitle: "二级菜单项",
   8. menuAction: subMenuItemAction
   9. }
   10. subMenus.push(subMenu);

   12. let statusBarMenuItems: Array<statusBarManager.StatusBarMenuItem> = [];
   13. let menuItem: statusBarManager.StatusBarMenuItem = {
   14. title: "一级菜单项",
   15. // 一级menuAction和subMenu两项不可都缺省
   16. subMenu: subMenus
   17. };
   18. statusBarMenuItems.push(menuItem);

   20. let statusBarGroupMenus: Array<statusBarManager.StatusBarGroupMenu> = [];
   21. statusBarGroupMenus.push(statusBarMenuItems);

   23. let context: Context | undefined = this.getUIContext().getHostContext();
   24. if (!context) {
   25. console.error('getHostContext failed');
   26. return;
   27. }
   28. try {
   29. statusBarManager.updateStatusBarMenu(context, statusBarGroupMenus);
   30. } catch (error) {
   31. console.error(`updateStatusBarMenu failed. error code: ${error.code}, error message: ${error.message}`);
   32. }
   ```
9. （可选）应用接入状态栏之后，可以通过[updateQuickOperationHeight](../harmonyos-references/statusbar-extension-manager.md#statusbarmanagerupdatequickoperationheight)接口更新状态栏图标左键业务弹窗的高度。

   ```
   1. let context: Context | undefined = this.getUIContext().getHostContext();
   2. if (!context) {
   3. console.error('getHostContext failed');
   4. return;
   5. }
   6. let height = 200;
   7. statusBarManager.updateQuickOperationHeight(context, height);
   ```
10. （可选）应用接入状态栏之后，可以通过[updateStatusBarIcon](../harmonyos-references/statusbar-extension-manager.md#statusbarmanagerupdatestatusbaricon)接口将状态栏中对应的应用图标进行更改。

    ```
    1. let context: Context | undefined = this.getUIContext().getHostContext();
    2. if (!context) {
    3. console.error('getHostContext failed');
    4. return;
    5. }
    6. // 获取resourceManager资源管理器
    7. const resourceMgr: resourceManager.ResourceManager = context.resourceManager;

    9. // 创建white pixelMap，需在资源rawfile文件夹中预置testWhite.png图片，图片大小为24vp * 24vp
    10. const whiteFileData = resourceMgr.getRawFileContentSync('testWhite.png');
    11. const whiteBuffer = whiteFileData.buffer;
    12. const whiteImageSource = image.createImageSource(whiteBuffer);
    13. let whitePixelMap = await whiteImageSource.createPixelMap();

    15. // 创建black pixelMap，需在资源rawfile文件夹中预置testBlack.png图片，图片大小为24vp * 24vp
    16. const blackFileData = resourceMgr.getRawFileContentSync('testBlack.png');
    17. const blackBuffer = blackFileData.buffer;
    18. const blackImageSource = image.createImageSource(blackBuffer);
    19. let blackPixelMap = await blackImageSource.createPixelMap();

    21. // 构建图标信息
    22. let icons: statusBarManager.StatusBarIcon = {
    23. white: whitePixelMap,
    24. black: blackPixelMap
    25. }
    26. statusBarManager.updateStatusBarIcon(context, icons);
    ```
11. （可选）应用接入状态栏之后，且未指定图标[QuickOperation](../harmonyos-references/statusbar-extension-manager.md#statusbarmanagerquickoperation)的abilityName可以通过[on](../harmonyos-references/statusbar-extension-manager.md#statusbarmanageronstatusbariconclick)/[off](../harmonyos-references/statusbar-extension-manager.md#statusbarmanageroffstatusbariconclick)接口自定义状态栏图标左键业务。

    ```
    1. private onStatusBarIconClick = (eventData: emitter.EventData) => {
    2. // 自定义图标点击业务
    3. let data = eventData.data;
    4. if (data) {
    5. switch (data['iconClickType']) {
    6. case 'leftClickType':
    7. // 自定义左键点击业务
    8. break;
    9. default:
    10. break;
    11. }
    12. }
    13. }

    15. // 监听状态栏图标点击事件
    16. statusBarManager.on('statusBarIconClick', this.onStatusBarIconClick);

    18. // 注销状态栏图标点击事件
    19. statusBarManager.off('statusBarIconClick', this.onStatusBarIconClick);
    ```
12. （可选）应用接入状态栏之后，调用[updateStatusBarMenu](../harmonyos-references/statusbar-extension-manager.md#statusbarmanagerupdatestatusbarmenu)接口，指定菜单[StatusBarMenuAction](../harmonyos-references/statusbar-extension-manager.md#statusbarmanagerstatusbarmenuaction)的notifyOnly使能和menuCode菜单项标识，可以通过[on](../harmonyos-references/statusbar-extension-manager.md#statusbarmanageronstatusbariconclick)/[off](../harmonyos-references/statusbar-extension-manager.md#statusbarmanageroffstatusbariconclick)接口自定义状态栏图标右键菜单点击业务。

    ```
    1. private onRightMenuClick = (eventData: emitter.EventData) => {
    2. // 自定义图标右键菜单点击业务
    3. let data = eventData.data;
    4. if (data) {
    5. let menuCode = data['menuCode'] as string;
    6. // 处理点击菜单项业务
    7. }
    8. }

    10. // 监听状态栏图标右键菜单点击事件
    11. statusBarManager.on('rightMenuClick', this.onRightMenuClick);

    13. // 注销状态栏图标右键菜单点击事件
    14. statusBarManager.off('rightMenuClick', this.onRightMenuClick);
    ```
13. （可选）应用接入状态栏之后，调用[updateStatusBarHoverTips](../harmonyos-references/statusbar-extension-manager.md#statusbarmanagerupdatestatusbarhovertips)接口可以自定义图标hover时的显示内容。

    ```
    1. let context: Context | undefined = this.getUIContext().getHostContext();
    2. if (!context) {
    3. console.error('getHostContext failed');
    4. return;
    5. }
    6. let hoverTips: string = 'hoverTips';
    7. try {
    8. await statusBarManager.updateStatusBarHoverTips(context, hoverTips);
    9. } catch (err) {
    10. console.error(`updateStatusBarHoverTips ${err.message} ${err.code}`)
    11. }
    ```

## 完整示例代码

完整示例代码请参见[状态栏开放服务](https://gitcode.com/harmonyos_samples/status-bar-extension-kit-samplecode)。
