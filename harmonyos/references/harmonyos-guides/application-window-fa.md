---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-window-fa
title: 管理应用窗口（FA模型）
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 管理应用窗口（FA模型）
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:41+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:0a7992a7748d10681eaa69aeb4b140c80376562224cea5746cc12859e375d0c3
---

## 基本概念

窗口沉浸式能力：指对状态栏、导航栏等系统窗口进行控制，减少状态栏导航栏等系统界面的突兀感，从而使用户获得最佳体验的能力。

沉浸式能力只在应用主窗口作为全屏窗口时生效。通常情况下，应用子窗口（弹窗、悬浮窗口等辅助窗口）和处于自由窗口下的应用主窗口无法使用沉浸式能力。

说明

当前沉浸式界面开发仅支持窗口级别的配置，暂不支持Page级别的配置。若有Page级别切换的需要，可以在页面生命周期开始，例如onPageShow中设置沉浸模式，然后在页面退出，例如onPageHide中恢复默认设置来实现。

## 场景介绍

在FA模型下，管理应用窗口的典型场景有：

* 设置应用子窗口属性及目标页面
* 体验窗口沉浸式能力

以下分别介绍具体开发方式。

## 接口说明

上述场景涉及的常用接口如下表所示。更多API说明请参见[API参考](../harmonyos-references/arkts-apis-window.md)。

| 实例名 | 接口名 | 描述 |
| --- | --- | --- |
| window静态方法 | createWindow(config: Configuration, callback: AsyncCallback<Window>): void | 创建子窗口。  -config：创建窗口时的参数。 |
| window静态方法 | findWindow(name: string): Window | 查找name所对应的窗口。 |
| Window | setUIContent(path: string, callback: AsyncCallback<void>): void | 根据当前工程中某个页面的路径为窗口加载具体的页面内容。  其中path为要加载到窗口中的页面内容的路径，在FA模型下该路径需添加到工程的config.json文件中。 |
| Window | moveWindowTo(x: number, y: number, callback: AsyncCallback<void>): void | 移动当前窗口位置。 |
| Window | setWindowBrightness(brightness: number, callback: AsyncCallback<void>): void | 设置屏幕亮度值。 |
| Window | resize(width: number, height: number, callback: AsyncCallback<void>): void | 改变当前窗口大小。 |
| Window | setWindowLayoutFullScreen(isLayoutFullScreen: boolean): Promise<void> | 设置主窗口或子窗口的布局是否为沉浸式布局。true表示沉浸式布局；false表示非沉浸式布局。 |
| Window | setWindowSystemBarEnable(names: Array<'status'|'navigation'>): Promise<void> | 设置主窗口状态栏、底部导航（根据用户设置，可表现为导航条或三键导航栏）的可见模式，状态栏和底部导航通过status控制、navigation参数无效果。  例如，该参数设置为['status', 'navigation']，则全部显示；设置为[]，则不显示。 |
| Window | setWindowSystemBarProperties(systemBarProperties: SystemBarProperties): Promise<void> | 设置窗口内导航栏、状态栏属性。  systemBarProperties：导航栏、状态栏的属性集合。 |
| Window | showWindow(callback: AsyncCallback<void>): void | 显示当前窗口。 |
| Window | on(type: 'touchOutside', callback: Callback<void>): void | 开启本窗口区域外的点击事件的监听。 |
| Window | destroyWindow(callback: AsyncCallback<void>): void | 销毁当前窗口。 |

## 设置应用子窗口

开发者可以按需创建应用子窗口，如弹窗等，并对其进行属性设置等操作。

说明

以下几种场景不建议使用子窗口，建议优先考虑使用控件[overlay](../harmonyos-references/ts-universal-attributes-overlay.md)能力实现。

* 移动设备（手机、在非自由模式下的平板设备）场景下子窗口不能超出处于悬浮窗、分屏状态的主窗口范围，与控件一致。
* 分屏窗口与自由窗口模式下，主窗口位置大小发生改变时控件实时跟随变化能力优于子窗口。
* 部分设备平台下根据实际的系统配置限制，子窗只有系统默认的动效和圆角阴影，应用无法设置，自由度低。

### 开发步骤

1. 创建/获取子窗口对象。

   * 可以通过window.createWindow接口创建子窗口。

     非[自由窗口](window-terminology.md#自由窗口)状态下，子窗口创建后默认是[沉浸式布局](window-terminology.md#沉浸式布局)。

     自由窗口状态下，子窗口参数[decorEnabled](../harmonyos-references/arkts-apis-window-i.md#configuration9)为false时，子窗口创建后为沉浸式布局；子窗口参数decorEnabled为true，子窗口创建后为非沉浸式布局。
   * 也可以通过window.findWindow接口来查找已经创建的窗口从而得到子窗口。

   ```
   1. import { window } from '@kit.ArkUI';
   2. import { BusinessError } from '@kit.BasicServicesKit';

   4. let windowClass: window.Window | null = null;
   5. // 方式一：创建子窗口。
   6. let config: window.Configuration = { name: "subWindow", windowType: window.WindowType.TYPE_APP };
   7. window.createWindow(config, (err: BusinessError, data) => {
   8. let errCode: number = err.code;
   9. if (errCode) {
   10. console.error(`Failed to create the subWindow. Code:${err.code}, message:${err.message}`);
   11. return;
   12. }
   13. console.info('Succeeded in creating subWindow. Data: ' + JSON.stringify(data));
   14. windowClass = data;
   15. if (!windowClass) {
   16. console.error('windowClass is null');
   17. return;
   18. }
   19. });
   20. // 方式二：查找得到子窗口。
   21. try {
   22. windowClass = window.findWindow('subWindow');
   23. } catch (exception) {
   24. console.error('Failed to find the Window. Cause: ' + JSON.stringify(exception));
   25. }
   ```
2. 设置子窗口属性。

   子窗口创建成功后，可以改变其大小、位置等，还可以根据应用需要设置窗口背景色、亮度等属性。

   ```
   1. // 移动子窗口位置。
   2. windowClass.moveWindowTo(300, 300, (err: BusinessError) => {
   3. let errCode: number = err.code;
   4. if (errCode) {
   5. console.error('Failed to move the window. Cause:' + JSON.stringify(err));
   6. return;
   7. }
   8. console.info('Succeeded in moving the window.');
   9. });
   10. // 改变子窗口大小。
   11. windowClass.resize(500, 500, (err: BusinessError) => {
   12. let errCode: number = err.code;
   13. if (errCode) {
   14. console.error('Failed to change the window size. Cause:' + JSON.stringify(err));
   15. return;
   16. }
   17. console.info('Succeeded in changing the window size.');
   18. });
   ```
3. 加载显示子窗口的具体内容。

   使用setUIContent和showWindow接口加载显示子窗口的具体内容。

   ```
   1. // 为子窗口加载对应的目标页面。
   2. windowClass.setUIContent("pages/page2", (err: BusinessError) => {
   3. let errCode: number = err.code;
   4. if (errCode) {
   5. console.error('Failed to load the content. Cause: ' + JSON.stringify(err));
   6. return;
   7. }
   8. console.info('Succeeded in loading the content.');
   9. if (!windowClass) {
   10. console.error('windowClass is null');
   11. return;
   12. }
   13. // 显示子窗口。
   14. windowClass.showWindow((err: BusinessError) => {
   15. let errCode: number = err.code;
   16. if (errCode) {
   17. console.error('Failed to show the window. Cause: ' + JSON.stringify(err));
   18. return;
   19. }
   20. console.info('Succeeded in showing the window.');
   21. });
   22. });
   ```
4. 销毁子窗口。

   当不再需要某些子窗口时，可根据场景的具体实现逻辑，使用destroyWindow接口销毁子窗口。

   ```
   1. // 销毁子窗口。当不再需要某些子窗口时，可根据场景的具体实现逻辑，使用destroy接口销毁子窗口。
   2. windowClass.destroyWindow((err: BusinessError) => {
   3. let errCode: number = err.code;
   4. if (errCode) {
   5. console.error('Failed to destroy the subwindow. Cause:' + JSON.stringify(err));
   6. return;
   7. }
   8. console.info('Succeeded in destroying the subwindow.');
   9. });
   ```

## 体验窗口沉浸式能力

在看视频、玩游戏等场景下，用户往往希望隐藏状态栏、导航栏等不必要的系统窗口，从而获得更佳的沉浸式体验。此时可以借助窗口沉浸式能力（窗口沉浸式能力都是针对应用主窗口而言的），达到预期效果。从API version 10开始，沉浸式窗口默认配置为全屏大小并由组件模块控制布局，状态栏、导航栏背景颜色为透明，文字颜色为黑色；应用窗口调用setWindowLayoutFullScreen接口，设置为true表示由组件模块控制忽略状态栏、导航栏的沉浸式全屏布局，设置为false表示由组件模块控制避让状态栏、导航栏的非沉浸式全屏布局。

### 开发步骤

1. 获取主窗口对象。

   说明

   沉浸式能力需要在成功获取应用主窗口对象的前提下进行。

   确保应用内最后显示的窗口为主窗口，然后再使用window.getLastWindow接口来获取得到主窗口。

   ```
   1. import { window } from '@kit.ArkUI';
   2. import { BusinessError } from '@kit.BasicServicesKit';

   4. let mainWindowClass: window.Window | null = null;

   6. // 获取主窗口。
   7. class BaseContext {
   8. stageMode: boolean = false;
   9. }

   11. let context: BaseContext = { stageMode: false };
   12. window.getLastWindow(context, (err: BusinessError, data) => {
   13. let errCode: number = err.code;
   14. if (errCode) {
   15. console.error('Failed to get the mainWindow. Cause: ' + JSON.stringify(err));
   16. return;
   17. }
   18. console.info('Succeeded in getting mainWindow. Data: ' + JSON.stringify(data));
   19. mainWindowClass = data;
   20. if (!mainWindowClass) {
   21. console.error('mainWindowClass is null');
   22. return;
   23. }
   24. });
   ```
2. 实现沉浸式效果。有以下两种方式：

   * 方式一：应用主窗口为全屏窗口时，调用setWindowSystemBarEnable接口，设置导航栏、状态栏不显示，从而达到沉浸式效果。
   * 方式二：调用setWindowLayoutFullScreen接口，设置应用主窗口为全屏布局；然后调用setWindowSystemBarProperties接口，设置导航栏、状态栏的透明度、背景/文字颜色以及高亮图标等属性，使之保持与主窗口显示协调一致，从而达到沉浸式效果。

   ```
   1. // 实现沉浸式效果。方式一：设置导航栏、状态栏不显示。
   2. let names: Array<'status' | 'navigation'> = [];
   3. mainWindowClass.setWindowSystemBarEnable(names)
   4. .then(() => {
   5. console.info('Succeeded in setting the system bar to be visible.');
   6. })
   7. .catch((err: BusinessError) => {
   8. console.error('Failed to set the system bar to be visible. Cause:' + JSON.stringify(err));
   9. });
   10. // 实现沉浸式效果。
   11. // 方式二：设置窗口为全屏布局，配合设置状态栏、导航栏的透明度、背景/文字颜色及高亮图标等属性，与主窗口显示保持协调一致。
   12. let isLayoutFullScreen: boolean = true;
   13. mainWindowClass.setWindowLayoutFullScreen(isLayoutFullScreen)
   14. .then(() => {
   15. console.info('Succeeded in setting the window layout to full-screen mode.');
   16. })
   17. .catch((err: BusinessError) => {
   18. console.error('Failed to set the window layout to full-screen mode. Cause:' + JSON.stringify(err));
   19. });
   20. let sysBarProps: window.SystemBarProperties = {
   21. statusBarColor: '#ff00ff',
   22. navigationBarColor: '#00ff00',
   23. // 以下两个属性从API Version8开始支持。
   24. statusBarContentColor: '#ffffff',
   25. navigationBarContentColor: '#ffffff'
   26. };
   27. mainWindowClass.setWindowSystemBarProperties(sysBarProps)
   28. .then(() => {
   29. console.info('Succeeded in setting the system bar properties.');
   30. })
   31. .catch((err: BusinessError) => {
   32. console.error('Failed to set the system bar properties. Cause: ' + JSON.stringify(err));
   33. });
   ```
3. 加载显示沉浸式窗口的具体内容。

   使用setUIContent和showWindow接口加载显示沉浸式窗口的具体内容。

   ```
   1. // 为沉浸式窗口加载对应的目标页面。
   2. mainWindowClass.setUIContent("pages/page3", (err: BusinessError) => {
   3. let errCode: number = err.code;
   4. if (errCode) {
   5. console.error('Failed to load the content. Cause: ' + JSON.stringify(err));
   6. return;
   7. }
   8. console.info('Succeeded in loading the content.');
   9. if (!mainWindowClass) {
   10. console.error('mainWindowClass is null');
   11. return;
   12. }
   13. // 显示沉浸式窗口。
   14. mainWindowClass.showWindow((err: BusinessError) => {
   15. let errCode: number = err.code;
   16. if (errCode) {
   17. console.error('Failed to show the window. Cause: ' + JSON.stringify(err));
   18. return;
   19. }
   20. console.info('Succeeded in showing the window.');
   21. });
   22. });
   ```
