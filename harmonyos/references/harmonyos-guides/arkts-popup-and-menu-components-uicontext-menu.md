---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-popup-and-menu-components-uicontext-menu
title: 不依赖UI组件的全局菜单 (openMenu)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用弹窗 > 菜单 > 不依赖UI组件的全局菜单 (openMenu)
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5d6454d35b6cb251bd71a0ef11d4a9a5cc65c494418c65a5cf43da49a0a3a0e0
---

[菜单控制 (Menu)](arkts-popup-and-menu-components-menu.md)在使用时依赖绑定UI组件，否则无法使用。从API version 18开始，可以通过使用全局接口[openMenu](../harmonyos-references/arkts-apis-uicontext-promptaction.md#openmenu18)的方式，在无UI组件的场景下直接或封装使用，例如在事件回调中使用或封装后对外提供能力。

## 弹出菜单

通过[openMenu](../harmonyos-references/arkts-apis-uicontext-promptaction.md#openmenu18)可以弹出菜单。

```
1. this.getUIContext().getPromptAction()
2. .openMenu(this.contentNode, { id: targetId }, {
3. enableArrow: true
4. })
5. .then(() => {
6. hilog.info(0xFF00, 'globalOpenMenu', 'openMenu success');
7. })
8. .catch((err: BusinessError) => {
9. hilog.error(0xFF00, 'globalOpenMenu', 'openMenu error: ' + err.code + ' ' + err.message);
10. });
```

[GlobalOpenMenu.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/Menu/globalmenusindependentofuicomponents/GlobalOpenMenu.ets#L108-L119)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/g-JzsiPUReCVyNVvx-mPtw/zh-cn_image_0000002589244215.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052756Z&HW-CC-Expire=86400&HW-CC-Sign=24696FA408E81DB65C4505A9081AA2518B9AD2BFD757AAE971402E54BE082726)

### 创建ComponentContent

通过调用openMenu接口弹出菜单，需要定义ComponentContent，以提供自定义弹出框的内容。详细规格可参考[ComponentContent](../harmonyos-references/js-apis-arkui-componentcontent.md)说明。

```
1. private contentNode: ComponentContent<Object> =
2. new ComponentContent(this.getUIContext(), wrapBuilder(buildText), this.message);
```

[GlobalOpenMenu.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/Menu/globalmenusindependentofuicomponents/GlobalOpenMenu.ets#L96-L99)

如果在wrapBuilder中包含其他组件（例如：[Popup](../harmonyos-references/ohos-arkui-advanced-popup.md)、[Chip](../harmonyos-references/ohos-arkui-advanced-chip.md)组件），则应在创建ComponentContent时设置[nestingBuilderSupported](../harmonyos-references/js-apis-arkui-buildernode.md#buildoptions12)属性为true。

```
1. @Builder
2. export function buildText(params: Params) {
3. Popup({
4. // 类型设置图标内容
5. icon: {
6. // 请将$r('app.media.app_icon')替换为实际资源文件
7. image: $r('app.media.app_icon'),
8. width: 32,
9. height: 32,
10. fillColor: Color.White,
11. borderRadius: 10
12. } as PopupIconOptions,
13. // 设置文字内容
14. title: {
15. text: `This is a Popup title 1`,
16. fontSize: 20,
17. fontColor: Color.Black,
18. fontWeight: FontWeight.Normal
19. } as PopupTextOptions,
20. // 设置文字内容
21. message: {
22. text: `This is a Popup message 1`,
23. fontSize: 15,
24. fontColor: Color.Black
25. } as PopupTextOptions,
26. // 设置按钮内容
27. buttons: [{
28. text: 'confirm',
29. action: () => {
30. hilog.info(0xFF00, 'globalOpenMenu', 'confirm button click');
31. },
32. fontSize: 15,
33. fontColor: Color.Black,
34. },
35. {
36. text: 'cancel',
37. action: () => {
38. hilog.info(0xFF00, 'globalOpenMenu', 'cancel button click');
39. },
40. fontSize: 15,
41. fontColor: Color.Black
42. },] as [PopupButtonOptions?, PopupButtonOptions?]
43. })
44. }

46. let contentNode: ComponentContent<Object> =
47. new ComponentContent(uiContext, wrapBuilder(buildText), message, { nestingBuilderSupported: true });
```

[GlobalOpenMenu.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/Menu/globalmenusindependentofuicomponents/GlobalOpenMenu.ets#L39-L88)

### 绑定组件信息

通过调用openMenu接口弹出菜单，需要提供绑定组件的信息[TargetInfo](../harmonyos-references/arkts-apis-uicontext-i.md#targetinfo18)。若未传入有效的target，菜单将无法弹出。

目前有两种设置target的方式。

* target的id属性设置为number类型，此时需要将id设置为对应组件的UniqueID，组件的UniqueID由系统保证唯一性。

  ```
  1. let frameNode: FrameNode | null = this.getUIContext().getFrameNodeByUniqueId(this.getUniqueId());
  2. let targetId = frameNode?.getChild(0)?.getUniqueId();
  ```

  [GlobalOpenMenu.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/Menu/globalmenusindependentofuicomponents/GlobalOpenMenu.ets#L156-L159)
* target的id属性设置为string类型，此时需要将id设置为对应组件的通用属性[id](../harmonyos-references/ts-universal-attributes-component-id.md#id)值。当无法保证id的唯一性时，如多团队开发或者复用自定义组件，可以通过设置componentId属性明确指定此id的范围来精确指定target，此时componentId属性可以设置为对应组件的父组件或者所在自定义组件的UniqueID。

  ```
  1. build() {
  2. NavDestination() {
  3. Column() {
  4. Row() {
  5. Button('button1')
  6. .id(this.targetIdString)
  7. }

  9. Row() {
  10. Button('button2')
  11. .id(this.targetIdString)
  12. }

  14. Button('openMenu')
  15. .onClick(() => {
  16. let frameNode: FrameNode | null = this.uiContext.getFrameNodeByUniqueId(this.getUniqueId());
  17. let componentId = frameNode?.getChild(1)?.getChild(0)?.getChild(1)?.getUniqueId();
  18. if (componentId == undefined) {
  19. this.componentId = 0;
  20. } else {
  21. this.componentId = componentId;
  22. }
  23. this.promptAction.openMenu(this.contentNode, { id: this.targetIdString, componentId: this.componentId }, {
  24. enableArrow: true
  25. })
  26. .then(() => {
  27. hilog.info(0x0000, 'openMenuWithTargetIdString', 'openMenu success');
  28. })
  29. .catch((err: BusinessError) => {
  30. hilog.error(0x0000, 'openMenuWithTargetIdString', 'openMenu error: ' + err.code + ' ' + err.message);
  31. });
  32. })
  33. }
  34. }
  35. }
  ```

  [OpenMenuWithTargetIdString.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/Menu/globalmenusindependentofuicomponents/OpenMenuWithTargetIdString.ets#L46-L82)

### 设置弹出菜单样式

通过调用openMenu接口弹出菜单，可以设置[MenuOptions](../harmonyos-references/ts-universal-attributes-menu.md#menuoptions10)中的属性调整菜单样式。title属性不生效。preview参数仅支持设置[MenuPreviewMode](../harmonyos-references/ts-universal-attributes-menu.md#menupreviewmode11)类型。

```
1. private options: MenuOptions = { enableArrow: true, placement: Placement.Bottom };
```

[GlobalOpenMenu.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/Menu/globalmenusindependentofuicomponents/GlobalOpenMenu.ets#L100-L103)

## 更新菜单样式

从API version 18开始，通过[updateMenu](../harmonyos-references/arkts-apis-uicontext-promptaction.md#updatemenu18)可以更新菜单的样式。支持全量更新和增量更新其菜单样式，不支持更新[MenuOptions](../harmonyos-references/ts-universal-attributes-menu.md#menuoptions10)中的showInSubWindow、preview、previewAnimationOptions、transition、onAppear、aboutToAppear、onDisappear、aboutToDisappear、onWillAppear、onDidAppear、onWillDisappear和onDidDisappear属性。

```
1. this.getUIContext().getPromptAction()
2. .updateMenu(this.contentNode, {
3. enableArrow: false
4. }, true)
5. .then(() => {
6. hilog.info(0xFF00, 'globalOpenMenu', 'updateMenu success');
7. })
8. .catch((err: BusinessError) => {
9. hilog.error(0xFF00, 'globalOpenMenu', 'updateMenu error: ' + err.code + ' ' + err.message);
10. });
```

[GlobalOpenMenu.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/Menu/globalmenusindependentofuicomponents/GlobalOpenMenu.ets#L123-L134)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/QKO8ixNPQ-C7-vWBLzCd0w/zh-cn_image_0000002589244215.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052756Z&HW-CC-Expire=86400&HW-CC-Sign=CDC532C17768EE5987BE454D46F5F75F94872F92C271DEF7FAEC0C5943E912E4)

## 关闭菜单

从API version 18开始，通过调用[closeMenu](../harmonyos-references/arkts-apis-uicontext-promptaction.md#closemenu18)可以关闭菜单。

```
1. this.getUIContext().getPromptAction()
2. .closeMenu(this.contentNode)
3. .then(() => {
4. hilog.info(0xFF00, 'globalOpenMenu', 'closeMenu success');
5. })
6. .catch((err: BusinessError) => {
7. hilog.error(0xFF00, 'globalOpenMenu', 'closeMenu error: ' + err.code + ' ' + err.message);
8. });
```

[GlobalOpenMenu.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/Menu/globalmenusindependentofuicomponents/GlobalOpenMenu.ets#L138-L147)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/kZAZw4zSTl2_6vvIcl7usA/zh-cn_image_0000002589244215.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052756Z&HW-CC-Expire=86400&HW-CC-Sign=18F3B21506DEA033D983DE00E3EDF345D72210FCC6240E1F2970EFBF1C07A046)

说明

由于[updateMenu](../harmonyos-references/arkts-apis-uicontext-promptaction.md#updatemenu18)和[closeMenu](../harmonyos-references/arkts-apis-uicontext-promptaction.md#closemenu18)依赖content来更新或者关闭指定的菜单，开发者需自行维护传入的content。

## 在HAR包中使用全局菜单

可以通过[HAR](har-package.md)包封装一个Menu，从而对外提供菜单的弹出、更新和关闭能力。

具体调用方式参考[在HAR包中使用全局气泡提示](arkts-popup-and-menu-components-uicontext-popup.md#在har包中使用全局气泡提示)。
