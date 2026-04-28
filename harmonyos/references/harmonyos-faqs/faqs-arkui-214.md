---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-214
title: 如何设置沉浸式状态栏
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何设置沉浸式状态栏
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:56+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:19d44fee61861526e1d3e22bd1365c1c2e412b51ceac1a966405428d7a383d0b
---

1. 获取应用主窗口。通过getMainWindow接口获取应用主窗口。
2. 实现沉浸式效果。有以下两种方式：
   * 方式一：调用setWindowSystemBarEnable接口，设置导航栏、状态栏不显示，从而达到沉浸式效果。
   * 方式二：调用setWindowLayoutFullScreen接口，设置应用主窗口为全屏布局；然后调用setWindowSystemBarProperties接口，设置导航栏、状态栏的透明度、背景/文字颜色以及高亮图标等属性，使之保持与主窗口显示协调一致，从而达到沉浸式效果。
3. 加载显示沉浸式窗口的具体内容。通过loadContent接口加载沉浸式窗口的具体内容。

   ```
   1. import { UIAbility } from '@kit.AbilityKit';
   2. import { window } from '@kit.ArkUI';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   6. export default class EntryAbility extends UIAbility {
   7. onWindowStageCreate(windowStage: window.WindowStage) {
   8. // 1.Get the main window of the application.
   9. let windowClass: window.Window | undefined = undefined;
   10. windowStage.getMainWindow((err: BusinessError, data) => {
   11. if (err.code) {
   12. console.error('Failed to obtain the main window. Cause: ' + JSON.stringify(err));
   13. return;
   14. }
   15. windowClass = data;
   16. console.info('Succeeded in obtaining the main window. Data: ' + JSON.stringify(data));

   19. // 2.Realize immersive effects. Method 1: Set the navigation bar and status bar to not display.
   20. let names = [];
   21. windowClass.setWindowSystemBarEnable(names).then(() => {
   22. console.info('Succeeded in setting the system bar to be visible.');
   23. }).catch((err: BusinessError) => {
   24. console.error('Failed to setting the system bar to be visible. Cause: ' + JSON.stringify(err));
   25. });
   26. // 2.Realize immersive effects. Method 2: Set the window to a full screen layout, and coordinate with the transparency, background/text color, and highlighted icons of the navigation bar and status bar to maintain consistency with the main window display.
   27. let isLayoutFullScreen = true;
   28. windowClass.setWindowLayoutFullScreen(isLayoutFullScreen).then(() => {
   29. console.info('Succeeded in setting the window layout to full-screen mode.');
   30. }).catch((err: BusinessError) => {
   31. console.error('Failed to setting the window layout. Cause: ' + JSON.stringify(err));
   32. });
   33. let sysBarProps: window.SystemBarProperties = {
   34. statusBarColor: '#ff00ff',
   35. navigationBarColor: '#00ff00',
   36. // The following two attributes are supported starting from API Version 8
   37. statusBarContentColor: '#ffffff',
   38. navigationBarContentColor: '#ffffff'
   39. };
   40. windowClass.setWindowSystemBarProperties(sysBarProps).then(() => {
   41. console.info('Succeeded in setting the system bar properties.');
   42. }).catch((err: BusinessError) => {
   43. console.error('Failed to setting the system bar properties. Cause: ' + JSON.stringify(err));
   44. });
   45. })
   46. // 3.Load the corresponding target page for the immersive window.
   47. windowStage.loadContent("pages/page2", (err) => {
   48. if (err.code) {
   49. console.error('Failed to load the content. Cause:' + JSON.stringify(err));
   50. return;
   51. }
   52. console.info('Succeeded in loading the content.');
   53. });
   54. }
   55. };
   ```

   [EntryAbilityImmersiveStatusBar.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/EntryAbilityImmersiveStatusBar.ets#L21-L75)
