---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-362
title: 如何实现折叠屏折叠态不适配旋转，展示态适配旋转
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现折叠屏折叠态不适配旋转，展示态适配旋转
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:33+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:af5d915519db84614ee1b7a3d282252d2ee430f1ce11ab636a8c2aa3b056072a
---

1. 在module.json5添加属性"orientation": "unspecified"。

   ```
   1. // module.json5
   2. {
   3. "module": {
   4. "abilities": [
   5. {
   6. "name": "EntryAbility",
   7. "orientation":"unspecified"  // Unspecified orientation mode, determined by the system
   8. }
   9. ]
   10. }
   11. }
   ```

   [Rotation.json5](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/Rotation.json5#L6-L16)
2. 在EntryAbility.ets的onWindowStageCreate方法中设置监听。如果设备处于完全展开状态，设置跟随系统方向，包括竖屏、横屏、反向竖屏和反向横屏。如果设备处于完全折叠状态，设置固定竖屏。

   ```
   1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { display, window } from '@kit.ArkUI';
   4. import { BusinessError } from '@kit.BasicServicesKit';

   6. export default class EntryAbility extends UIAbility {
   7. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
   8. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
   9. }

   11. onDestroy(): void {
   12. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
   13. }

   15. onWindowStageCreate(windowStage: window.WindowStage): void {
   16. // Main window is created, set main page for this ability
   17. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

   20. windowStage.loadContent('pages/Index', (err) => {
   21. if (err.code) {
   22. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
   23. return;
   24. }
   25. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
   26. });

   28. windowStage.getMainWindow().then((windowObj) => {
   29. // Set orientation based on fold status: auto-rotation when expanded, portrait when folded
   30. let orientation = display.getFoldStatus() === display.FoldStatus.FOLD_STATUS_EXPANDED ?
   31. window.Orientation.AUTO_ROTATION : window.Orientation.PORTRAIT;
   32. windowObj?.setPreferredOrientation(orientation);

   34. // Monitor the unfolded or folded state of the foldable screen
   35. display.on('foldStatusChange', (foldStatus: display.FoldStatus) => {
   36. orientation = foldStatus === display.FoldStatus.FOLD_STATUS_EXPANDED ? window.Orientation.AUTO_ROTATION :
   37. window.Orientation.PORTRAIT;
   38. try {
   39. windowObj?.setPreferredOrientation(orientation, (err: BusinessError) => {
   40. if (err.code) {
   41. console.error(`Failed to set window orientation. Cause code: ${err.code}, message: ${err.message}`);
   42. return;
   43. }
   44. console.info('Succeeded in setting window orientation.');
   45. });
   46. } catch (exception) {
   47. console.error(`Failed to set window orientation. Cause code: ${exception.code}, message: ${exception.message}`);
   48. }
   49. })
   50. });
   51. }

   53. onWindowStageDestroy(): void {
   54. // Main window is destroyed, release UI related resources
   55. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
   56. }

   58. onForeground(): void {
   59. // Ability has brought to foreground
   60. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
   61. }

   63. onBackground(): void {
   64. // Ability has back to background
   65. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
   66. }
   67. }
   ```

   [EntryAbilityDisplayAdaptationRotation.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/EntryAbilityDisplayAdaptationRotation.ets#L21-L88)
