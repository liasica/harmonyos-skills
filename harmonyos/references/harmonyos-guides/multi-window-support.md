---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-window-support
title: 应用声明支持智慧多窗
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 智慧多窗应用开发指南 > 应用适配智慧多窗 > 应用声明支持智慧多窗
category: harmonyos-guides
scraped_at: 2026-04-29T13:29:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:08bc5977ec94c80f3c467cdb61bf1922ac64d3dbe65bbb923fd535863216dcc3
---

当应用需要智慧多窗的能力时，可以通过在[module.json5配置文件](module-configuration-file.md)中对应标签添加相关字段声明支持。

## 声明支持悬浮窗

开发者可以通过在module.json5配置文件中[abilities标签](module-configuration-file.md#abilities标签)下的**supportWindowMode**属性增加“**floating**”字段或使用缺省值以声明应用支持悬浮窗。

说明

supportWindowMode缺省值为["fullscreen", "split", "floating"]。

**supportWindowMode**属性主要标识当前UIAbility所支持的窗口模式，支持的字段及含义如下表所示。

| 字段 | 说明 |
| --- | --- |
| fullscreen | 窗口支持全屏显示。 |
| split | 窗口支持分屏显示。 |
| floating | 窗口支持悬浮窗显示。 |

在应用声明支持智慧多窗后，还可根据业务场景的需要配置是否支持横向悬浮窗或上下分屏模式。

当应用需要支持横向悬浮窗时，开发者可以通过在module.json5配置文件中**abilities**标签下的**preferMultiWindowOrientation**属性增加“**landscape**”或者“**landscape\_auto**”配合API以声明应用支持横向悬浮窗或上下分屏模式。

**preferMultiWindowOrientation**属性主要标识当前UIAbility组件多窗布局方向，支持的字段及含义如下表所示。

| 配置值 | 说明 | 效果 |
| --- | --- | --- |
| portrait | 多窗布局方向为竖向。建议竖向游戏类应用配置。 | **手机**  手势触发悬浮窗：竖向悬浮窗  手势触发分屏：不支持  分屏样式切换：不涉及  **折叠屏手机展开态**  手势触发悬浮窗：竖向悬浮窗  手势触发分屏：形成左右分屏  分屏样式切换：不支持样式切换 |
| landscape | 多窗布局方向为横向，配置后支持横向悬浮窗和上下分屏。建议横向游戏类应用配置。 | **手机**  手势触发悬浮窗：横向悬浮窗  手势触发分屏：不支持  分屏样式切换：不涉及  **折叠屏手机展开态**  手势触发悬浮窗：横向悬浮窗  手势触发分屏：形成上下分屏  分屏样式切换：不支持样式切换 |
| landscape\_auto | 多窗布局动态可变为横向，需要配合API（[enableLandscapeMultiWindow](../harmonyos-references/arkts-apis-window-window.md#enablelandscapemultiwindow12) / [disableLandscapeMultiWindow](../harmonyos-references/arkts-apis-window-window.md#disablelandscapemultiwindow12)）使用。建议视频类应用配置。 | **系统识别应用为横向全屏播放：**  **手机**  手势触发悬浮窗：横向悬浮窗  手势触发分屏：形成上下分屏  分屏样式切换：不涉及  **折叠屏手机展开态**  手势触发悬浮窗：横向悬浮窗  手势触发分屏：形成上下分屏  分屏样式切换：支持样式切换  **系统识别应用为非横向全屏播放：** 同配置为default |
| default | 缺省值，参数不配置时默认为default。  建议其他应用类配置。 | **折叠屏手机折叠态 & 手机**  手势触发悬浮窗：竖向悬浮窗  手势触发分屏：形成上下分屏  分屏样式切换：不涉及  **折叠屏手机展开态**  手势触发悬浮窗：竖向悬浮窗  手势触发分屏：形成左右分屏  分屏样式切换：支持样式切换 |

## 声明支持分屏

开发者可以通过在module.json5配置文件中[abilities标签](module-configuration-file.md#abilities标签)下的**supportWindowMode**属性增加“**split**”字段或使用缺省值以声明应用支持分屏。

说明

supportWindowMode缺省值为["fullscreen", "split", "floating"]。

**supportWindowMode**属性主要标识当前UIAbility所支持的窗口模式，支持的字段及含义如下表所示。

| 字段 | 说明 |
| --- | --- |
| fullscreen | 窗口支持全屏显示。 |
| split | 窗口支持分屏显示。 |
| floating | 窗口支持悬浮窗显示。 |

## 应用内分屏

应用内分屏功能允许[声明支持分屏](multi-window-support.md#声明支持分屏)的应用在全屏显示模式下，通过调用startAbility方法启动UIAbility并形成分屏。该功能能够增强应用的多任务处理能力，提升用户的操作体验。

此处以点击按钮启动分屏为例，主要步骤和示例如下所示：

1. 在应用中获取UIAbilityContext 对象，这是启动分屏所必需的上下文对象，用于后续调用startAbility接口。

   ```
   1. this.hostContext = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
   ```
2. 调用startAbility接口启动UIAbility，形成分屏。调用startAbility接口时，设置StartOptions对象，需要指定窗口模式[windowMode](../harmonyos-references/js-apis-app-ability-abilityconstant.md#windowmode12)（需设置为WINDOW\_MODE\_SPLIT\_PRIMARY或者WINDOW\_MODE\_SPLIT\_SECONDARY），并可根据需要设置其他StartOptions属性或startAbility参数，如Want对象。

   ```
   1. // 创建StartOptions并设置为主窗口模式
   2. let option: StartOptions = { windowMode: AbilityConstant.WindowMode.WINDOW_MODE_SPLIT_PRIMARY };
   3. let want: Want = { bundleName: 'com.example.startsplitdemo', abilityName: 'EntryAbility1', moduleName: '' };
   4. this.hostContext?.startAbility(want, option);
   ```
3. 若继续执行上述步骤，可继续启动其他UIAbility窗口，呈现左右分屏或替换一侧的分屏窗口。

完整示例如下：

使用DevEco Studio新建Ability，创建EntryAbility1和EntryAbility2，对应文中组成分屏的两个窗口页面，加载页面为默认页面Index.ets。

```
1. // Index.ets
2. import { AbilityConstant, common, StartOptions, Want } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. @Entry
7. @Component
8. struct Index {
9. @State name: string = '';
10. private hostContext: common.UIAbilityContext | null = null;

12. aboutToAppear(): void {
13. this.hostContext = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
14. this.name = this.hostContext.abilityInfo.name;
15. }

17. build() {
18. Column({ space: 20 }) {
19. Text(this.name)

21. Button() {
22. Text('启动应用内分屏')
23. }
24. .height(40)
25. .onClick(() => {
26. // 指定拉起的分屏窗口的应用信息
27. let want: Want = { bundleName: 'com.example.startsplitdemo', abilityName: 'EntryAbility1', moduleName: '' };
28. // 创建StartOptions并设置窗口模式为分屏模式，左侧分屏
29. let option: StartOptions = { windowMode: AbilityConstant.WindowMode.WINDOW_MODE_SPLIT_PRIMARY };
30. this.hostContext?.startAbility(want, option);
31. })

33. Button() {
34. Text('启动另一分屏窗口')
35. }
36. .height(40)
37. .onClick(() => {
38. let want: Want = { bundleName: 'com.example.startsplitdemo', abilityName: 'EntryAbility2', moduleName: '' };
39. // 指定启动EntryAbility2的窗口模式，右侧分屏
40. let option: StartOptions = { windowMode: AbilityConstant.WindowMode.WINDOW_MODE_SPLIT_SECONDARY };
41. this.hostContext?.startAbility(want, option, (error: BusinessError) => {
42. if (error.code) {
43. return;
44. }
45. hilog.info(0x0000, 'testTag', '启动分屏成功');
46. });
47. })
48. }
49. .padding(20)
50. .height('100%')
51. .width('100%')
52. }
53. }
```

图1 启动左侧分屏

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/5KB-v2PSR8yJqos4ClDdkg/zh-cn_image_0000002589244495.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052906Z&HW-CC-Expire=86400&HW-CC-Sign=E69A56475E4DBA81BBFBC27CFD6571338E61B80E61476EB5A1A9A2711FCFF6C2)

图2 启动右侧分屏

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/28nyTG_3SZKxL5kZs2JveQ/zh-cn_image_0000002558764688.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052906Z&HW-CC-Expire=86400&HW-CC-Sign=BCAFF6A04DEF83AAC94CDA8BEC8209CCC21F27EA252F35C0288375C226BBDE67)

## 应用内多窗

从HarmonyOS 6.0.0版本开始，新增支持应用内多窗。应用内多窗功能支持应用拉起分屏或全景多窗，方便用户进行多任务处理。

当应用开发者需要使用应用内多窗图标时，可以使用高级组件[MultiWindowEntryInAPP](../harmonyos-references/ui-design-multiwindowentryinapp-api.md)实现该功能。
