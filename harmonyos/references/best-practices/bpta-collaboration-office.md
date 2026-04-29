---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-collaboration-office
title: 办公编辑全场景协同最佳实践
breadcrumb: 最佳实践 > 自由流转 > 典型全场景协同开发案例 > 办公编辑全场景协同最佳实践
category: best-practices
scraped_at: 2026-04-29T14:12:54+08:00
doc_updated_at: 2026-04-01
content_hash: sha256:9cbb92848c1e4adf843e43401557f8610681eb54efe62b4cbe4bdb30a88e284d
---

## 概述

全场景协同是鸿蒙（HarmonyOS）分布式能力的核心，通过整合多设备资源实现跨终端无缝体验。在办公编辑场景中，用户常需要在多台设备间协同操作，例如插入其他设备中的图片、将其他设备用作扩展屏以同时编辑多个文档，或在不同设备间切换。应用可通过接入全场景协同能力，帮助用户实现多设备协同工作，从而减少因设备切换带来的效率损耗与专注力分散，让用户更聚焦于任务本身，而非设备间的数据传输与切换过程。

本文主要面向办公场景的开发者/产品经理，提供场景范例和开发指导， 在开始前，建议对ArkTS项目有基础了解，若想调试开发本项目代码建议有两台以上设备，目前全场景的能力暂不支持模拟器调试。

目前，在商务办公应用中，集成Web编辑页面已成为主流方案。然而，这一架构下应用侧与Web侧如何通信，正是全场景协同能力接入时面临的主要难点。本文将以集成Web编辑页面的应用为基础，介绍如何[插入其他设备的图文](bpta-collaboration-office.md#section94919784915)、[切换设备继续编辑](bpta-collaboration-office.md#section1099115610472)、[分享协作](bpta-collaboration-office.md#section1739891118221)，具体目录如下：

* [用户体验](bpta-collaboration-office.md#section11739191313401)：通过图文形式介绍应用按照本文建议接入后的具体体验提升，以及用户使用时的约束限制。
* [插入其他设备的图文](bpta-collaboration-office.md#section94919784915)：在办公编辑时，若需要来源于其他设备的图文数据，本章介绍应用如何通过不同方式快速获取其他设备的数据。
* [切换设备继续编辑](bpta-collaboration-office.md#section1099115610472)：随着使用场景的变化，例如上班路上通过手机编辑文档，到公司之后需要通过PC继续编辑时，适宜的办公设备亦会相应切换。本章介绍应用如何实现设备的快速切换编辑。
* [分享协作](bpta-collaboration-office.md#section1739891118221) ：办公编辑业务往往涉及多人协同，本章介绍应用如何实现通过设备间的互动快速邀请其他用户编辑文档。
* [示例代码](bpta-collaboration-office.md#section149086232359)：开发者可以下载安装，配合本文一起使用，也可自行调试和参考开发。

说明

若应用不涉及Web页面集成，也可参考本文提供的体验设计及代码示例，将应用侧与Web交互步骤改为应用自身数据的获取与写入流程。

## 用户体验

### 体验

|  | 特性 | 特性体验 | 体验视频 |
| --- | --- | --- | --- |
| 插入其他设备图文 | 跨设备互通插入图片 | 1、用户使用平板/PC打开应用。  2、点击应用跨设备互通按钮。  3、弹窗选择设备拍照/图库。  4、用其他设备拍照/选择插入的图片。  5、插入图片到文档中。 | Video Player is loading. Play Video Play Current Time 0:00  Loaded: 4.69%    0:00  Duration 0:12  Mute  1x Playback Rate * 2x * 1.8x * 1.5x * 1.2x * 1x, selected Fullscreen  This is a modal window.  Beginning of dialog window. Escape will cancel and close the window.  TextColorWhiteBlackRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-TransparentText BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-TransparentTransparentCaption Area BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityTransparentSemi-TransparentOpaque  Font Size50%75%100%125%150%175%200%300%400%Text Edge StyleNoneRaisedDepressedUniformDrop shadowFont FamilyProportional Sans-SerifMonospace Sans-SerifProportional SerifMonospace SerifCasualScriptSmall Caps  Reset restore all settings to the default valuesDone Close Modal Dialog End of dialog window. |
| 插入其他设备图文 | 碰一碰文件/图片插入 | 1、用户在PC上打开应用。  2、通过手机碰PC窗口触发，手机向PC传输图片/文件。  3、文档接收文件，图片直接展示，文件形成链接。 | Video Player is loading. Play Video Play Current Time 0:00  Loaded: 8.12%    0:00  Duration 0:08  Mute  1x Playback Rate * 2x * 1.8x * 1.5x * 1.2x * 1x, selected Fullscreen  This is a modal window.  Beginning of dialog window. Escape will cancel and close the window.  TextColorWhiteBlackRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-TransparentText BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-TransparentTransparentCaption Area BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityTransparentSemi-TransparentOpaque  Font Size50%75%100%125%150%175%200%300%400%Text Edge StyleNoneRaisedDepressedUniformDrop shadowFont FamilyProportional Sans-SerifMonospace Sans-SerifProportional SerifMonospace SerifCasualScriptSmall Caps  Reset restore all settings to the default valuesDone Close Modal Dialog End of dialog window. |
| 插入其他设备图文 | 跨设备剪贴板 | 1、用户使用两台/多台设备（至少包含一台PC），均打开键鼠穿越，选择共享的设备。  2、复制图文。  3、粘贴选中图文到另一台设备的应用，图文正常落入。 | Video Player is loading. Play Video Play Current Time 0:00  Loaded: 12.24%    0:00  Duration 0:09  Mute  1x Playback Rate * 2x * 1.8x * 1.5x * 1.2x * 1x, selected Fullscreen  This is a modal window.  Beginning of dialog window. Escape will cancel and close the window.  TextColorWhiteBlackRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-TransparentText BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-TransparentTransparentCaption Area BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityTransparentSemi-TransparentOpaque  Font Size50%75%100%125%150%175%200%300%400%Text Edge StyleNoneRaisedDepressedUniformDrop shadowFont FamilyProportional Sans-SerifMonospace Sans-SerifProportional SerifMonospace SerifCasualScriptSmall Caps  Reset restore all settings to the default valuesDone Close Modal Dialog End of dialog window. |
| 插入其他设备图文 | 跨设备拖拽 | 1、用户使用两台/多台设备，均打开键鼠穿越，并链接鼠标。  2、拖拽图文到另一台设备的应用窗口。  3、图文正常落入。 | Video Player is loading. Play Video Play Current Time 0:00  Loaded: 10.93%    0:00  Duration 0:07  Mute  1x Playback Rate * 2x * 1.8x * 1.5x * 1.2x * 1x, selected Fullscreen  This is a modal window.  Beginning of dialog window. Escape will cancel and close the window.  TextColorWhiteBlackRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-TransparentText BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-TransparentTransparentCaption Area BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityTransparentSemi-TransparentOpaque  Font Size50%75%100%125%150%175%200%300%400%Text Edge StyleNoneRaisedDepressedUniformDrop shadowFont FamilyProportional Sans-SerifMonospace Sans-SerifProportional SerifMonospace SerifCasualScriptSmall Caps  Reset restore all settings to the default valuesDone Close Modal Dialog End of dialog window. |
| 切换设备继续编辑 | 应用接续 | 1、应用在源端设备打开，想切换到对端设备继续编辑。  2、点击对端设备docker栏应用图标。  3、对端设备正常打开文档。 | Video Player is loading. Play Video Play Current Time 0:00  Loaded: 20.29%    0:00  Duration 0:03  Mute  1x Playback Rate * 2x * 1.8x * 1.5x * 1.2x * 1x, selected Fullscreen  This is a modal window.  Beginning of dialog window. Escape will cancel and close the window.  TextColorWhiteBlackRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-TransparentText BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-TransparentTransparentCaption Area BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityTransparentSemi-TransparentOpaque  Font Size50%75%100%125%150%175%200%300%400%Text Edge StyleNoneRaisedDepressedUniformDrop shadowFont FamilyProportional Sans-SerifMonospace Sans-SerifProportional SerifMonospace SerifCasualScriptSmall Caps  Reset restore all settings to the default valuesDone Close Modal Dialog End of dialog window. |
| 分享协作 | 碰一碰邀请协同 | 1、用户A打开应用。  2、A的设备和B的设备之间相碰。  3、用户B的设备打开文档。 | Video Player is loading. Play Video Play Current Time 0:00  Loaded: 13.72%    0:00  Duration 0:09  Mute  1x Playback Rate * 2x * 1.8x * 1.5x * 1.2x * 1x, selected Fullscreen  This is a modal window.  Beginning of dialog window. Escape will cancel and close the window.  TextColorWhiteBlackRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-TransparentText BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-TransparentTransparentCaption Area BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityTransparentSemi-TransparentOpaque  Font Size50%75%100%125%150%175%200%300%400%Text Edge StyleNoneRaisedDepressedUniformDrop shadowFont FamilyProportional Sans-SerifMonospace Sans-SerifProportional SerifMonospace SerifCasualScriptSmall Caps  Reset restore all settings to the default valuesDone Close Modal Dialog End of dialog window. |
| 分享协作 | 隔空传送邀请协同 | 1、用户A打开应用。  2、用户A做隔空传送手势到用户B的设备，手势见[场景介绍](../harmonyos-guides/gestures-share-overview.md#section1936087195916)。  3、用户B的设备打开文档。 | Video Player is loading. Play Video Play Current Time 0:00  Loaded: 4.78%    0:00  Duration 0:09  Mute  1x Playback Rate * 2x * 1.8x * 1.5x * 1.2x * 1x, selected Fullscreen  This is a modal window.  Beginning of dialog window. Escape will cancel and close the window.  TextColorWhiteBlackRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-TransparentText BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-TransparentTransparentCaption Area BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityTransparentSemi-TransparentOpaque  Font Size50%75%100%125%150%175%200%300%400%Text Edge StyleNoneRaisedDepressedUniformDrop shadowFont FamilyProportional Sans-SerifMonospace Sans-SerifProportional SerifMonospace SerifCasualScriptSmall Caps  Reset restore all settings to the default valuesDone Close Modal Dialog End of dialog window. |

### 使用限制

|  | 特性 | 设备版本 | 设备类型（垂域常见设备手机、平板、PC） | 双端登录同一华为账号 | 双端打开WLAN 和蓝牙开关 | 设置配置 | 其他限制 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 插入其他设备图文 | 跨设备互通插入图片 | HarmonyOS NEXT Developer Preview0以上 | * 本端设备：平板或PC设备。 * 远端设备：具有相机能力的手机或平板设备。 | √ | √（条件允许时，建议双端设备接入同一个局域网，可提升唤醒相机的速度。） | 设置中开启“多设备协同 > **跨设备互通**”功能 | PC设备可以调用平板和手机，平板可以调用手机，同类型设备不可调用。 |
| 碰一碰文件/图片插入 | 手机和pc均6.0及以上，手机nova畅想系列不支持 | * 发起端设备：手机或折叠手机直板态 * 接收端设备：PC设备 | √ | × | 双端在设置中开启“多设备协同 > 华为分享 > 更多华为分享设置 > **启用华为分享服务**”功能 | * 需要PC打开应用窗口 * 对碰一碰的角度、手机壳厚度限制见[使用约束](../harmonyos-guides/knock-share-pc-phones-overview.md#section484625701614)。 |
| 跨设备剪贴板 | HarmonyOS NEXT Developer Preview0及以上 | 手机、平板、PC | √ | √ | 双端在设置中开启“多设备协同 > **跨设备剪贴板**”功能 | / |
| 跨设备拖拽 | HarmonyOS NEXT Developer Preview0 | 需要平板、PC设备提供键鼠，可从手机拖拽（手机不支持） | √ | √ | 双端在设置中开启“多设备协同 > **键鼠穿越**”功能 | / |
| 切换设备继续编辑 | 应用接续 | HarmonyOS NEXT Developer Preview0以上 | 手机、平板、PC | √ | √ | 双端在设置中开启“多设备协同 > **接续**”功能 | / |
| 分享协作 | 碰一碰邀请协同 | 5.0及以上，nova畅想系列不支持 | 手机或折叠手机直板态 | × | √ | 双端在设置中开启“多设备协同 > 华为分享 > 更多华为分享设置 > **启用华为分享服务**”功能 | 手机和pc也可以进行链接分享，但双端需要登录同一个华为账号，且手机和pc版本均需6.0及以上。 |
| 隔空传送邀请协同 | [HarmonyOS 6.0.0 Beta1](../harmonyos-releases/overview-600.md#section1836613212578)及以上版本 | 均支持 | × | × | 双端在设置中开启“多设备协同 > 华为分享 > 更多华为分享设置 > **启用华为分享服务**”功能 | 设备型号限制见[隔空传送支持的机型和版本说明](https://consumer.huawei.com/cn/support/content/zh-cn16074833/?source=weknow)。 |

## 插入其他设备的图文

随着个人设备数量的增加，用户在某一设备上操作时，常需从其他设备获取图片或文字。鸿蒙系统提供了多种方式，简化用户操作，降低开发成本，实现设备间的数据直接传输，减少设备间的界限。本章节介绍如何通过不同方式快速获取其他设备的数据。

### 跨设备互通插入图片

跨设备互通提供跨设备的相机、扫描和图库访问功能，平板或PC设备能够调用手机的相机、扫描和图库功能，用户可借此功能快速向文档添加来自其他设备的图片。

**实现原理**

通过同层渲染在Web页面中嵌入按钮，点击后调用[createCollaborationServiceMenuItems()](../harmonyos-references/servicecollaboration-collaborationservice.md#section1633482912443)创建设备选择菜单。使用对端设备执行操作（如拍照）后，通过[CollaborationServiceStateDialog.onState()](../harmonyos-references/servicecollaboration-collaborationservice.md#section33027582114)回调返回数据（Buffer或URI）。应用根据数据类型上传到服务器，再通过[runJavaScript()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascript)将图片插入Web编辑器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/XXr5ssqWTuWR2gXqThRxeA/zh-cn_image_0000002556898911.png?HW-CC-KV=V1&HW-CC-Date=20260429T061246Z&HW-CC-Expire=86400&HW-CC-Sign=90C6F3D718AE0C93C99862BE3C1FCA02DCE71C58E565B53FC4CAD313E4102AAE "点击放大")

**开发步骤**

1. web页面同层渲染。
   1. 在Web页面中标记需要同层渲染的HTML标签，在本案例中，使用object标签进行渲染，也可选择embed标签，可参考[Web网页的同层渲染标签](../harmonyos-guides/web-same-layer.md#web网页的同层渲染标签)。

      ```
      1. <object type="test" id="crossDeviceEmbed" class="crossDevice-btn" title="Cross-Device Share"></object>
      ```
   2. 应用侧使用[enableNativeEmbedMode()](../harmonyos-references/arkts-basic-components-web-attributes.md#enablenativeembedmode11)开启同层渲染，并使用[registerNativeEmbedRule()](../harmonyos-references/arkts-basic-components-web-attributes.md#registernativeembedrule12)注册object标签，第二个参数'test'，需要与a步骤中HTML标签中的type值相同。

      ```
      1. Web({
      2. src: `${this.viewModel.SERVER_URL}/edit.html?docId=${encodeURIComponent(this.getSafeDocIdForUrl())}`,
      3. controller: this.viewModel.controller
      4. })
      5. // ...
      6. .enableNativeEmbedMode(true)
      7. .registerNativeEmbedRule('object', 'test')
      ```

      [EditPage.ets](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/master/entry/src/main/ets/view/EditPage.ets#L140-L166)
   3. 创建自定义组件，该ArkTS组件将会被渲染进Web页面中。

      创建[Component](../atomic-ascf/custom-components-component.md)，封装Button按钮，并为按钮增加[onClick()](../harmonyos-references/ts-universal-events-click.md#onclick12)点击事件以响应用户手势，通过[bindContextMenu()](../harmonyos-references/ts-universal-attributes-menu.md#bindcontextmenu12)绑定菜单，第一个参数为显隐控制，响应点击事件。

      ```
      1. @Component
      2. struct CrossDeviceComponent {
      3. // Whether cross-device relay is active.
      4. @State isCrossDevice: boolean = false;
      5. // Builder params (position, size, onClick).
      6. @Prop param: CrossDeviceEmbedParams;

      8. build() {
      9. Button() {
      10. // ...
      11. }
      12. // ...
      13. .onClick(() => {
      14. this.isCrossDevice = true;
      15. })
      16. .bindContextMenu(this.isCrossDevice, crossDeviceMenu(), {
      17. aboutToDisappear: () => {
      18. this.isCrossDevice = false;
      19. }
      20. })
      21. }
      22. }
      ```

      [EditViewModel.ets](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/master/entry/src/main/ets/viewmodel/EditViewModel.ets#L434-L487)

      将[Component](../atomic-ascf/custom-components-component.md)封装为[Builder](../harmonyos-guides/arkts-builder.md)，以便后续调用。

      ```
      1. /**
      2. * Builder for cross-device button content in native embed.
      3. */
      4. @Builder
      5. export function CrossDeviceEmbedBuilder(params: CrossDeviceEmbedParams) {
      6. CrossDeviceComponent({ param: params })
      7. }
      ```

      [EditViewModel.ets](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/master/entry/src/main/ets/viewmodel/EditViewModel.ets#L424-L430)
   4. 创建节点控制器[NodeController](../harmonyos-references/js-apis-arkui-nodecontroller.md)，用于实现自定义节点的创建、显示、更新等操作的管理，并负责将自定义节点挂载到[NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md)上。
      * 重写[makeNode()](../harmonyos-references/js-apis-arkui-nodecontroller.md#makenode)方法，创建UI节点：检查销毁状态，已销毁则返回null；如果根节点已存在，直接返回对应的FrameNode，否则创建新的BuilderNode并构建跨设备嵌入UI。
      * 定义updateNode()，更新节点参数，调用根节点的update方法。
      * 定义getEmbedId()，返回嵌入标识符。
      * 定义setDestroy()，设置销毁状态，销毁时会清空根节点。
      * 定义postEvent()，处理触摸事件，转发给根节点处理。

        ```
        1. export class CrossDeviceNodeController extends NodeController {
        2. // Builder node for cross-device button UI.
        3. private rootNode: BuilderNode<CrossDeviceEmbedParams[]> | undefined | null = null;
        4. // Embed id from Web.
        5. private embedId: string = '';
        6. // Surface id for native embed.
        7. private surfaceId: string = '';
        8. // Render type (display/texture).
        9. private renderType: NodeRenderType = NodeRenderType.RENDER_TYPE_DISPLAY;
        10. // Node width in vp.
        11. private width: number = 0;
        12. // Node height in vp.
        13. private height: number = 0;
        14. // Whether controller is destroyed.
        15. private isDestroy: boolean = false;

        17. setRenderOption(params: NodeControllerParams): void {
        18. this.surfaceId = params.surfaceId;
        19. this.renderType = params.renderType;
        20. this.embedId = params.embedId;
        21. this.width = params.width;
        22. this.height = params.height;
        23. }

        25. makeNode(uiContext: UIContext): FrameNode | null {
        26. if (this.isDestroy) {
        27. return null;
        28. }
        29. if (this.rootNode) {
        30. return this.rootNode.getFrameNode();
        31. }
        32. this.rootNode = new BuilderNode(uiContext, {
        33. surfaceId: this.surfaceId,
        34. type: this.renderType
        35. });
        36. if (!this.rootNode) {
        37. return null;
        38. }
        39. this.rootNode.build(wrapBuilder(CrossDeviceEmbedBuilder), {
        40. width: this.width,
        41. height: this.height,
        42. });
        43. return this.rootNode.getFrameNode();
        44. }

        46. updateNode(arg: CrossDeviceEmbedParams): void {
        47. this.rootNode?.update(arg);
        48. }

        50. getEmbedId(): string {
        51. return this.embedId;
        52. }

        54. setDestroy(isDestroy: boolean): void {
        55. this.isDestroy = isDestroy;
        56. if (this.isDestroy) {
        57. this.rootNode = null;
        58. }
        59. }

        61. postEvent(event: TouchEvent | undefined): boolean {
        62. return (this.rootNode?.postTouchEvent(event) as boolean) ?? false;
        63. }
        64. }
        ```

        [EditViewModel.ets](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/master/entry/src/main/ets/viewmodel/EditViewModel.ets#L507-L570)
   5. 监听同层渲染的生命周期变化。

      开启该功能后，当网页中存在同层渲染支持的标签时，ArkWeb内核会触发回调函数。开发者则需要调用[onNativeEmbedLifecycleChange()](../harmonyos-references/arkts-basic-components-web-events.md#onnativeembedlifecyclechange11)来监听同层渲染标签的生命周期变化。Web的同层渲染标签创建、更新、销毁时，同层渲染组件也应创建、更新、销毁。

      ```
      1. Web({
      2. src: `${this.viewModel.SERVER_URL}/edit.html?docId=${encodeURIComponent(this.getSafeDocIdForUrl())}`,
      3. controller: this.viewModel.controller
      4. })
      5. // ...
      6. .onNativeEmbedLifecycleChange((embed: NativeEmbedDataInfo) => {
      7. const componentId = embed.info?.id?.toString() ?? '';
      8. const uiContext = this.getUIContext();
      9. if (embed.status === NativeEmbedStatus.CREATE) {
      10. this.viewModel.embedLifecycleCreate(embed, uiContext, componentId);
      11. this.componentIdArr = [...this.componentIdArr, componentId];
      12. } else if (embed.status === NativeEmbedStatus.UPDATE) {
      13. this.viewModel.embedLifecycleUpdate(embed, uiContext, componentId, this.isCrossDevice)
      14. } else if (embed.status === NativeEmbedStatus.DESTROY) {
      15. hilog.info(Constant.HILOG_DOMAIN, LOG_TAG, `NativeEmbed destroy: ${componentId}`);
      16. this.viewModel.embedLifecycleDestroy(componentId);
      17. this.componentIdArr = this.componentIdArr.filter((id: string) => id !== componentId);
      18. }
      19. })
      ```

      [EditPage.ets](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/master/entry/src/main/ets/view/EditPage.ets#L141-L195)

      组件创建：

      ```
      1. embedLifecycleCreate(embed: NativeEmbedDataInfo, uiContext: UIContext, componentId: string) {
      2. const params: NodeControllerParams = {
      3. surfaceId: embed.surfaceId as string,
      4. type: embed.info?.type as string,
      5. renderType: NodeRenderType.RENDER_TYPE_TEXTURE,
      6. embedId: embed.embedId as string,
      7. width: uiContext.px2vp(embed.info?.width ?? 0),
      8. height: uiContext.px2vp(embed.info?.height ?? 0),
      9. };
      10. const nodeController = new CrossDeviceNodeController();
      11. nodeController.setRenderOption(params);
      12. nodeController.setDestroy(false);
      13. this.nodeControllerMap.set(componentId, nodeController);
      14. this.widthMap.set(componentId, params.width);
      15. this.heightMap.set(componentId, params.height);
      16. let edges: Edges = {
      17. left: `${embed.info?.position?.x as number }px`,
      18. top: `${embed.info?.position?.y  as number }px`
      19. };
      20. this.positionMap.set(componentId, edges);
      21. }
      ```

      [EditViewModel.ets](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/master/entry/src/main/ets/viewmodel/EditViewModel.ets#L335-L355)

      组件更新：

      ```
      1. embedLifecycleUpdate(embed: NativeEmbedDataInfo, uiContext: UIContext, componentId: string, isCrossDevice: boolean) {
      2. const nodeController = this.nodeControllerMap.get(componentId);
      3. let edges: Edges = {
      4. left: `${embed.info?.position?.x  as number }px`,
      5. top: `${embed.info?.position?.y  as number }px`
      6. };
      7. this.positionMap.set(componentId, edges);
      8. const width = uiContext.px2vp(embed.info?.width ?? 0);
      9. const height = uiContext.px2vp(embed.info?.height ?? 0);
      10. this.widthMap.set(componentId, width);
      11. this.heightMap.set(componentId, height);
      12. nodeController?.updateNode({ width: width, height: height, crossButtonX: edges.left,
      13. crossButtonY: edges.top, isCrossDevice: isCrossDevice ,onClick: () => {} });
      14. }
      ```

      [EditViewModel.ets](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/master/entry/src/main/ets/viewmodel/EditViewModel.ets#L359-L372)

      组件销毁：

      ```
      1. embedLifecycleUpdate(embed: NativeEmbedDataInfo, uiContext: UIContext, componentId: string, isCrossDevice: boolean) {
      2. const nodeController = this.nodeControllerMap.get(componentId);
      3. let edges: Edges = {
      4. left: `${embed.info?.position?.x  as number }px`,
      5. top: `${embed.info?.position?.y  as number }px`
      6. };
      7. this.positionMap.set(componentId, edges);
      8. const width = uiContext.px2vp(embed.info?.width ?? 0);
      9. const height = uiContext.px2vp(embed.info?.height ?? 0);
      10. this.widthMap.set(componentId, width);
      11. this.heightMap.set(componentId, height);
      12. nodeController?.updateNode({ width: width, height: height, crossButtonX: edges.left,
      13. crossButtonY: edges.top, isCrossDevice: isCrossDevice ,onClick: () => {} });
      14. }
      ```

      [EditViewModel.ets](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/master/entry/src/main/ets/viewmodel/EditViewModel.ets#L359-L372)
2. 跨设备服务互通菜单实现
   1. 构建列表选择器。[createCollaborationServiceMenuItems()](../harmonyos-references/servicecollaboration-collaborationservice.md#section149271552154711)组件是设备列表选择器，需要在[Menu](../harmonyos-references/ts-basic-components-menu.md)组件内调用。用于显示组网内具有对应能力的设备列表。

      ```
      1. @Builder
      2. function crossDeviceMenu() {
      3. Menu() {
      4. // Add cross-device menu items, supporting up to 5 images.
      5. createCollaborationServiceMenuItems([CollaborationServiceFilter.ALL], 5)
      6. }
      7. }
      ```

      [EditViewModel.ets](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/master/entry/src/main/ets/viewmodel/EditViewModel.ets#L494-L500)
   2. 在页面中弹窗提示对端应用状态，并实现[onState()](../harmonyos-references/servicecollaboration-collaborationservice.md#section33027582114)方法作为数据接收回调。该方法接收三个参数：stateCode表示操作完成状态，bufferType表示回传的数据类型，buffer为回传的数据内容。在回调中调用应用封装的webViewHelper.doInsertPicture() 方法，将数据传递至Web端。

      ```
      1. // Cross-device communication state dialog component.
      2. CollaborationServiceStateDialog({
      3. onState: (stateCode: number, bufferType: string, buffer: ArrayBuffer): void => {
      4. this.webViewHelper.doInsertPicture(stateCode, bufferType, buffer);
      5. }
      6. })
      ```

      [EditPage.ets](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/master/entry/src/main/ets/view/EditPage.ets#L368-L373)
3. web的图片插入
   1. 实现doInsertPicture()，最终将文件进行封装为WebFileData，使用[runJavaScript()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascript)执行web端的函数。

      ```
      1. /**
      2. * Process image data returned from remote device
      3. * @param stateCode Completion status code
      4. * @param bufferType Returned data type
      5. * @param buffer Returned image data
      6. */
      7. public doInsertPicture(stateCode: number, bufferType: string, buffer: ArrayBuffer): void {
      8. // ...
      9. this.viewModel.handleCrossDeviceImage(buffer, `cross-device-image-${Date.now()}.jpg`, 'image/jpeg')
      10. .then(() => {
      11. // Show success message.
      12. this.showToast('Image added to editor');
      13. })
      14. // ...
      15. }
      ```

      [WebViewHelper.ets](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/master/entry/src/main/ets/utils/WebViewHelper.ets#L75-L106)

      ```
      1. public async handleCrossDeviceImage(buffer: ArrayBuffer, fileName: string, mimeType: string): Promise<void> {
      2. // ...
      3. const serverFilePath = await this.fileUploadUtil.uploadBufferToServer(buffer, fileName, mimeType);
      4. const webFileData: WebFileData = {
      5. uri: serverFilePath,
      6. mimeType: mimeType,
      7. fileName: fileName,
      8. title: fileName
      9. };
      10. hilog.info(Constant.HILOG_DOMAIN, LOG_TAG, 'Sending cross-device image to Web page, server path: %{public}s',
      11. serverFilePath);
      12. await this.controller.runJavaScript(`receiveFileToEditor(${JSON.stringify(webFileData)})`);
      13. // ...
      14. }
      ```

      [EditViewModel.ets](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/master/entry/src/main/ets/viewmodel/EditViewModel.ets#L170-L198)
   2. 图片注入前端页面，该步骤开发时由具体业务实现和原有的编辑器代码框架决定。前端网页获取arkts传递的uri参数，用于页面展示。

      ```
      1. function registerReceiveFileToEditor() {
      2. window.receiveFileToEditor = function (fileData) {
      3. const parsedData = parseNativeFileData(fileData);
      4. if (!parsedData) {
      5. return;
      6. }
      7. ensureEditModeForNativeInsert();
      8. const editor = document.getElementById('editor');
      9. if (editor) {
      10. applyDropPositionIfSaved(editor);
      11. }
      12. const displayFileName = getDisplayFileNameFromParsedData(parsedData);
      13. const fileType = inferNativeFileType(parsedData);
      14. handleNativeFileByType(parsedData, fileType, displayFileName);
      15. };
      16. }
      ```

      [script-harmonyos.js](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/b6aca07fcec9a58b919523c103a577cf5c57c554/WebEditor/public/js/script-harmonyos.js#L389-L404)

### 跨设备拖拽

拖拽能力允许用户自由的拖拽图文到其他窗口，在适配拖拽后，鸿蒙也自动支持跨设备拖拽。

**实现原理**

拖拽落入：

在WebView的 [onDrop()](../harmonyos-references/ts-universal-events-drag-drop.md#ondrop) 事件中，首先通过 [dragEvent.getData()](../harmonyos-references/ts-universal-events-drag-drop.md#getdata10)获取[UnifiedData](../harmonyos-references/ts-universal-events-drag-drop.md#unifieddata10) 对象。处理时遵循以下优先级：

1. 优先处理 HTML 类型数据：若存在，则解析 HTML，提取其中的图片，并按顺序插入文本和图片。
2. 若无 HTML 数据，则根据数据类型分别处理：
   * -- 文本：直接插入；
   * -- 图片、文件、视频：先上传，再插入；
   * -- 超链接：直接插入

   拖拽落入时序图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/PePa4HhVQwCeqi4Te3R53w/zh-cn_image_0000002525619066.png?HW-CC-KV=V1&HW-CC-Date=20260429T061246Z&HW-CC-Expire=86400&HW-CC-Sign=75554D175A055B64F8B8E8A0F03AAAA3F3FA44160D03AADAF63640C26B212B0E "点击放大")

拖拽拖出：

系统支持，无需适配。

**开发步骤**

1. web落入
   1. 自定义落入，使用[onDrop()](../harmonyos-references/ts-universal-events-drag-drop.md#ondrop)接口进行监听，当Web组件监听到拖拽落入时，将会触发此监听，应用应当处理拖拽数据。

      ```
      1. Web({
      2. src: `${this.viewModel.SERVER_URL}/edit.html?docId=${encodeURIComponent(this.getSafeDocIdForUrl())}`,
      3. controller: this.viewModel.controller
      4. })
      5. // ...
      6. .onDrop((dragEvent?: DragEvent) => {
      7. hilog.info(Constant.HILOG_DOMAIN, LOG_TAG, 'Drag completed, start processing drag data.');
      8. this.isDraggingOver = false;
      9. if (dragEvent) {
      10. try {
      11. this.viewModel.processDragData(dragEvent)
      12. .then(() => {
      13. hilog.info(Constant.HILOG_DOMAIN, LOG_TAG, 'Successfully processed drag data.');
      14. })
      15. .catch((error: BusinessError) => {
      16. hilog.error(Constant.HILOG_DOMAIN, LOG_TAG, 'Failed to process drag data: %{public}d %{public}s',
      17. error.code, error.message);
      18. });
      19. } catch (error) {
      20. const err = error as BusinessError;
      21. hilog.error(Constant.HILOG_DOMAIN, LOG_TAG,
      22. 'Failed to process drag event: %{public}d %{public}s', err.code,err.message);
      23. }
      24. }
      25. })
      ```

      [EditPage.ets](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/master/entry/src/main/ets/view/EditPage.ets#L142-L218)
   2. 数据处理

      异步处理拖拽数据，当存在HTML数据时，优先处理HTML类型；无HTML数据时，支持文本、图片、文件、超链接、视频等多种数据类型，不同的类型使用不同的处理方式。

      ```
      1. public async processDragData(dragEvent: DragEvent): Promise<void> {
      2. try {
      3. const unifiedData = dragEvent.getData();
      4. const records: unifiedDataChannel.UnifiedRecord[] = unifiedData.getRecords();

      6. // ...
      7. let processedCount = 0;
      8. const totalCount = records.length;

      10. // Check if there is any HTML type data.
      11. const hasHtmlData = records.some(record =>
      12. record.getType() === uniformTypeDescriptor.UniformDataType.HTML
      13. );
      14. // ...

      16. for (const record of records) {
      17. const recordType = record.getType();

      19. try {
      20. if (hasHtmlData) {
      21. // If there is HTML data, only process HTML type.
      22. if (recordType === uniformTypeDescriptor.UniformDataType.HTML) {
      23. hilog.info(Constant.HILOG_DOMAIN, LOG_TAG, 'Processing HTML type drag data (has HTML data)');
      24. await this.processHtmlDrag(record as unifiedDataChannel.HTML);
      25. processedCount++;
      26. } else {
      27. // For other types, just log and do not process.
      28. hilog.info(Constant.HILOG_DOMAIN, LOG_TAG,
      29. `Skipping non-HTML drag data type when HTML exists: ${recordType}`);
      30. }
      31. } else {
      32. // If no HTML data, process all types as before.
      33. hilog.info(Constant.HILOG_DOMAIN, LOG_TAG, `Processing non-HTML drag data type: ${recordType}`);

      35. if (recordType === uniformTypeDescriptor.UniformDataType.TEXT ||
      36. recordType === uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) {
      37. // Process text drag.
      38. await this.processTextDrag(record as unifiedDataChannel.PlainText);
      39. processedCount++;
      40. } else if (recordType === uniformTypeDescriptor.UniformDataType.IMAGE) {
      41. // Process image drag.
      42. await this.processImageDrag(record as unifiedDataChannel.Image);
      43. processedCount++;
      44. } else if (recordType === uniformTypeDescriptor.UniformDataType.FILE) {
      45. // Process file drag.
      46. await this.processFileDrag(record as unifiedDataChannel.File);
      47. processedCount++;
      48. } else if (recordType === uniformTypeDescriptor.UniformDataType.HYPERLINK) {
      49. let hyperLinkUds =
      50. record.getEntry(uniformTypeDescriptor.UniformDataType.HYPERLINK) as uniformDataStruct.Hyperlink;
      51. if (hyperLinkUds) {
      52. let url = hyperLinkUds.url;
      53. let text = hyperLinkUds.description ?? url;
      54. hilog.info(Constant.HILOG_DOMAIN, LOG_TAG, `Received hyperlink drag: url=${url}, text=${text}`);
      55. await this.processHyperlinkDrag(url, text);
      56. processedCount++;
      57. }
      58. } else if (recordType === uniformTypeDescriptor.UniformDataType.VIDEO) {
      59. const fileUriUds =
      60. record.getEntry(uniformTypeDescriptor.UniformDataType.FILE_URI) as uniformDataStruct.FileUri;
      61. if (fileUriUds) {
      62. let uri = fileUriUds.oriUri;
      63. hilog.info(Constant.HILOG_DOMAIN, LOG_TAG, `Received video drag: uri=${uri}`);
      64. await this.processVideoDrag(uri);
      65. processedCount++;
      66. }
      67. } else {
      68. hilog.warn(Constant.HILOG_DOMAIN, LOG_TAG, `Unsupported drag data type: ${recordType}`);
      69. }
      70. }
      71. } catch (recordError) {
      72. // ...
      73. }
      74. }
      75. // ...
      76. } catch (error) {
      77. // ...
      78. }
      79. }
      ```

      [DragDropModel.ets](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/master/entry/src/main/ets/model/DragDropModel.ets#L66-L160)

      数据处理，以图片拖拽为例。先通过uploadFileToServer()将本地图片URI上传到服务器，再通过[runJavaScript()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascript)注入方式将文件信息传递给前端编辑器。

      ```
      1. private async processImageDrag(imageRecord: unifiedDataChannel.Image): Promise<void> {
      2. const imageUri = imageRecord.imageUri;
      3. // ...
      4. try {
      5. // Generate unique file name.
      6. const fileName = `drag-image-${Date.now()}.jpg`;
      7. const mimeType = 'image/jpeg';

      9. // Upload image to server using URI.
      10. const serverFilePath = await this.fileUploadUtil.uploadFileToServer(imageUri, fileName, mimeType);
      11. hilog.info(Constant.HILOG_DOMAIN, LOG_TAG, `Image uploaded to server: ${serverFilePath}`);

      13. // Send the image URL to the web editor.
      14. const fileInfo: FileInfo = {
      15. uri: serverFilePath,
      16. mimeType: mimeType,
      17. fileName: fileName,
      18. title: fileName
      19. };
      20. await this.controller.runJavaScript(`receiveFileToEditor(${JSON.stringify(fileInfo)})`);
      21. } catch (error) {
      22. // ...
      23. }
      24. }
      ```

      [DragDropModel.ets](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/master/entry/src/main/ets/model/DragDropModel.ets#L193-L226)
2. web拖出

   ArkWeb目前支持以下四种数据格式。应用按照H5标准设置这些格式的拖拽数据，即可将内容拖拽到其他应用中。

   | 数据格式 | 说明 |
   | --- | --- |
   | text/plain | 文本 |
   | text/uri-list | 链接 |
   | text/html | HTML格式 |
   | Files | 文件 |

   说明

   手机不支持web内容拖出。

### 跨设备剪贴板

**实现原理**

首先获取剪贴板权限，通过[onContextMenuShow()](../harmonyos-references/arkts-basic-components-web-events.md#oncontextmenushow9)显示上下文菜单，使用[getSystemPasteboard().hasDataSync()](../harmonyos-references/js-apis-pasteboard.md#hasdatasync11)检查剪贴板是否有数据。用户点击粘贴后调用[result.paste()](../harmonyos-references/arkts-basic-components-web-webcontextmenuresult.md#paste9)，系统自动将剪贴板内容插入WebView。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/z4aLhA3pSXacZ_4P83RZ_w/zh-cn_image_0000002556778943.png?HW-CC-KV=V1&HW-CC-Date=20260429T061246Z&HW-CC-Expire=86400&HW-CC-Sign=DF1A29946085603FE0CBB5A86F2AC867AD46DE9B59D71DFC0A884C325895BFFE "点击放大")

**开发步骤**

1. 复制数据

   复制与粘贴的常用快捷键系统默认已经适配，开发不需要适配，PC端Web组件左键/长按需要适配弹窗。
2. 粘贴数据
   1. 授权获取，通过[checkAccessTokenSync()](../harmonyos-references/js-apis-abilityaccessctrl.md#checkaccesstokensync10)检测是否由剪贴板权限。

      ```
      1. // Use synchronous method to get application bundle info.
      2. const bundleInfo: bundleManager.BundleInfo =
      3. bundleManager.getBundleInfoForSelfSync(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
      4. const appInfo: bundleManager.ApplicationInfo = bundleInfo.appInfo;
      5. tokenId = appInfo.accessTokenId;

      7. // Use synchronous method to check permission.
      8. const permissionStatus = atManager.checkAccessTokenSync(tokenId, 'ohos.permission.READ_PASTEBOARD');
      9. hasPermission = permissionStatus === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED;
      ```

      [PermissionUtil.ets](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/master/entry/src/main/ets/utils/PermissionUtil.ets#L47-L55)

      通过[requestPermissionsFromUser()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)获取授权。

      ```
      1. const requestResult =
      2. await atManager.requestPermissionsFromUser(context, ['ohos.permission.READ_PASTEBOARD']);
      ```

      [PermissionUtil.ets](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/master/entry/src/main/ets/utils/PermissionUtil.ets#L71-L72)
   2. 获取上下文菜单。

      创建弹出[Menu](../harmonyos-references/ts-basic-components-menu.md)，是以垂直列表形式显示的菜单，会垂直展示[MenuItem](../harmonyos-references/ts-basic-components-menuitem.md)子组件。

      ```
      1. @Builder
      2. MenuBuilder() {
      3. Menu() {
      4. MenuItem({
      5. symbolStartIcon: new SymbolGlyphModifier($r('sys.symbol.plus_square_on_square')),
      6. content: $r('app.string.copy'),
      7. labelInfo: $r('app.string.copy_info')
      8. })
      9. // ...
      10. .onClick(() => {
      11. this.result?.copy();
      12. this.showMenu = false;
      13. })
      14. MenuItem({
      15. symbolStartIcon: new SymbolGlyphModifier($r('sys.symbol.plus_square_dashed_on_square')),
      16. content: $r('app.string.paste'),
      17. labelInfo: $r('app.string.paste_info')
      18. })
      19. // ...
      20. .onClick(() => {
      21. this.result?.paste();
      22. this.showMenu = false;
      23. })
      24. MenuItem({
      25. symbolStartIcon: new SymbolGlyphModifier($r('sys.symbol.checkmark_square_on_square')),
      26. content: $r('app.string.select_all'),
      27. labelInfo: $r('app.string.select_all_info')
      28. })
      29. // ...
      30. .onClick(() => {
      31. this.result?.selectAll();
      32. this.showMenu = false;
      33. })
      34. }
      35. // ...
      36. }
      ```

      [EditPage.ets](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/master/entry/src/main/ets/view/EditPage.ets#L87-L133)

      Web组件绑定[onContextMenuShow()](../harmonyos-references/arkts-basic-components-web-events.md#oncontextmenushow9)回调，其中param为[WebContextMenuParam](../harmonyos-references/arkts-basic-components-web-webcontextmenuparam.md)类型，包含点击位置对应HTML元素信息和位置信息，result为[WebContextMenuResult](../harmonyos-references/arkts-basic-components-web-webcontextmenuresult.md)类型，提供常见的菜单能力。回调返回false表示触发的自定义菜单无效，以允许自定义显示上下文菜单，通过bindPopup()绑定展示。

      ```
      1. Web({
      2. src: `${this.viewModel.SERVER_URL}/edit.html?docId=${encodeURIComponent(this.getSafeDocIdForUrl())}`,
      3. controller: this.viewModel.controller
      4. })
      5. // ...
      6. .onContextMenuShow((event) => {
      7. if (this.deviceType === 'phone') {
      8. return false;
      9. }
      10. this.result = event.result;
      11. const flags = event.param.getEditStateFlags();
      12. this.canCopy = (flags & ContextMenuEditStateFlags.CAN_COPY) !== 0;
      13. this.canPaste = false;
      14. try {
      15. let hasData = pasteboard.getSystemPasteboard().hasDataSync();
      16. this.canPaste = (flags & ContextMenuEditStateFlags.CAN_PASTE) !== 0 && hasData;
      17. } catch (error) {
      18. const err = error as BusinessError;
      19. hilog.error(Constant.HILOG_DOMAIN, LOG_TAG, `Failed to check clipboard data: ${err.code} ${err.message}`);
      20. }
      21. this.showMenu = true;
      22. this.offsetX = Math.max(this.getUIContext().px2vp(event?.param.x() ?? 0) - 0, 0);
      23. this.offsetY = Math.max(this.getUIContext().px2vp(event?.param.y() ?? 0) - 0, 0);
      24. return true;
      25. })
      26. .bindPopup(this.showMenu,
      27. {
      28. builder: this.MenuBuilder(),
      29. enableArrow: false,
      30. placement: Placement.LeftTop,
      31. offset: { x: this.offsetX, y: this.offsetY },
      32. mask: false,
      33. onStateChange: async (e) => {
      34. let result = false;
      35. if (e.isVisible) {
      36. result = await PermissionUtil.checkAndRequestPasteboardPermission(this.context);
      37. }
      38. if (!result || !e.isVisible) {
      39. this.showMenu = false;
      40. try {
      41. this.result?.closeContextMenu();
      42. } catch (error) {
      43. const err = error as BusinessError;
      44. hilog.error(Constant.HILOG_DOMAIN, LOG_TAG,
      45. `Failed to close context menu: ${err.code} ${err.message}`);
      46. }
      47. }
      48. }
      49. })
      ```

      [EditPage.ets](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/master/entry/src/main/ets/view/EditPage.ets#L143-L335)

### 碰一碰文件/图片插入

**实现原理**

编辑页加载时注册[on('dataReceive')](../harmonyos-references/share-harmony-share.md#section1365282783615)监听，支持指定MEDIA和FILE类型。PC端通过碰一碰发送文件后触发回调，调用[receiveTarget.receive()](../harmonyos-references/share-harmony-share.md#section1923918121115)接收数据。解析[SharedData.getRecords()](../harmonyos-references/share-system-share.md#section14943101911111)获取文件URI，上传到服务器后通过[runJavaScript()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascript)插入编辑器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/OtRv2IC6Rr-EvJdDxp1bug/zh-cn_image_0000002525779028.png?HW-CC-KV=V1&HW-CC-Date=20260429T061246Z&HW-CC-Expire=86400&HW-CC-Sign=99C31C44CA5A7CD8156F0245DA471F85026F6C62D2F15E6E57ECF3E0FCA69C4C "点击放大")

**开发步骤**

1. 使用[canIUse()](../harmonyos-references/js-apis-syscap.md#caniuse)判断是否可以使用接口。

   ```
   1. if (!canIUse('SystemCapability.Collaboration.HarmonyShare')) {
   2. hilog.error(Constant.HILOG_DOMAIN, LOG_TAG, 'Device does not support HarmonyShare functionality');
   3. return;
   4. }
   ```

   [KnockShareModel.ets](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/master/entry/src/main/ets/model/KnockShareModel.ets#L244-L247)
2. 注册监听事件[on('dataReceive')](../harmonyos-references/share-harmony-share.md#section1365282783615)实现应用沙箱接收文件。该方法需要传入当前应用的窗口ID，并且需要传入capabilities属性，以表示当前应用支持接收的文件标准化数据类型及其最大接收数量，该属性不能传入空数组。

   ```
   1. // Use correct dataReceive event listening, implemented according to example structure.
   2. harmonyShare.on('dataReceive', {
   3. windowId: mainWindowID,
   4. capabilities: [
   5. {
   6. 'utd': uniformTypeDescriptor.UniformDataType.MEDIA,
   7. 'maxSupportedCount': 5
   8. },
   9. {
   10. 'utd': uniformTypeDescriptor.UniformDataType.FILE,
   11. 'maxSupportedCount': 5
   12. }
   13. ]
   14. }, (receiveTarget: harmonyShare.ReceivableTarget) => {
   15. hilog.info(Constant.HILOG_DOMAIN, LOG_TAG,
   16. `Received dataReceive event, receiveTarget: ${JSON.stringify(receiveTarget)}`);

   18. if (!this.context) {
   19. return;
   20. }

   22. receiveTarget.receive(fileUri.getUriFromPath(this.context.filesDir), {
   23. onDataReceived: (shareData: systemShare.SharedData) => {
   24. hilog.info(Constant.HILOG_DOMAIN, LOG_TAG,
   25. `Received shared data, shareData: ${JSON.stringify(shareData)}`);

   27. let shareRecords = shareData.getRecords();
   28. shareRecords.forEach((record: systemShare.SharedRecord) => {
   29. if (!record.uri) {
   30. return;
   31. }

   33. // Extract file name from uri (decode for correct display e.g. Chinese).
   34. const rawName = record.uri.split('/').pop() || 'Unknown file';
   35. let fileName: string;
   36. try {
   37. fileName = decodeURIComponent(rawName);
   38. } catch {
   39. fileName = rawName;
   40. }

   42. // Determine MIME type based on file name extension, not relying on record.mimeType.
   43. let mimeType = 'application/octet-stream'; // Default MIME type.
   44. const ext = fileName.split('.').pop()?.toLowerCase() || '';

   46. const mimeTypes = Constant.KNOCK_MIME_TYPES;

   48. // Get corresponding MIME type from mapping table.
   49. if (mimeTypes[ext]) {
   50. mimeType = mimeTypes[ext];
   51. }

   53. // Build fileData object suitable for web.
   54. const fileData: FileData = {
   55. data: record.uri,
   56. mimeType: mimeType,
   57. title: record.title || fileName,
   58. description: record.description || '',
   59. content: record.content,
   60. fileName: fileName,
   61. dataType: 'uri'
   62. };

   64. hilog.info(Constant.HILOG_DOMAIN, LOG_TAG, `Parsed file data: ${JSON.stringify(fileData)}`);
   65. // Call callback function, pass file data to application layer.
   66. callback(fileData);
   67. });
   68. },
   69. onResult(resultCode: number) {
   70. if (resultCode === 0) {
   71. hilog.info(Constant.HILOG_DOMAIN, LOG_TAG, 'File received successfully');
   72. } else {
   73. hilog.error(Constant.HILOG_DOMAIN, LOG_TAG, `Failed to receive file, result code: ${resultCode}`);
   74. }
   75. }
   76. });
   ```

   [KnockShareModel.ets](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/master/entry/src/main/ets/model/KnockShareModel.ets#L271-L346)
3. 将沙箱图片上传到web侧。

   ```
   1. public async sendFileToWeb(fileData: FileData): Promise<void> {
   2. if (fileData && fileData.data) {
   3. try {
   4. // ...
   5. const serverFilePath = await this.fileUploadUtil.uploadFileToServer(fileData.data, fileData.fileName,
   6. fileData.mimeType);
   7. const webFileData: WebFileData = {
   8. uri: serverFilePath,
   9. mimeType: fileData.mimeType,
   10. fileName: fileData.fileName,
   11. title: fileData.title
   12. };
   13. // ...
   14. } catch (error) {
   15. // ...
   16. }
   17. }
   18. }
   ```

   [EditViewModel.ets](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/master/entry/src/main/ets/viewmodel/EditViewModel.ets#L131-L163)

## 切换设备继续编辑

### 应用接续

**实现原理**

源端在[onContinue()](../harmonyos-references/js-apis-app-ability-uiability.md#oncontinue)中获取当前WebView的URL并保存到wantParam.webUrl，系统传输到目标设备。目标设备在[onCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)/[onNewWant()](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)中检测launchReason.CONTINUATION，从want.parameters获取URL，设置给continuationUrl静态变量。页面加载时检查continuationUrl，若为编辑页则调用loadUrl加载接续URL。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/ms5pY2F_T_eDeF_WXDE35Q/zh-cn_image_0000002556898917.png?HW-CC-KV=V1&HW-CC-Date=20260429T061246Z&HW-CC-Expire=86400&HW-CC-Sign=EC6D99224FB5765F447C249D7A310D9F3DE2FFD800FB82D61B74E0AA435EBCC6 "点击放大")

**开发步骤**

1. 开启应用接续能力。

   说明

   若应用需要接续的不同设备存在于多个hap打包中，可参考[支持同应用中不同Ability跨端迁移](../harmonyos-guides/app-continuation-guide.md#section71450211617)进行配置，以支持不同hap包之间的应用接续。

   ```
   1. {
   2. "module": {
   3. // ...
   4. "abilities": [
   5. {
   6. // ...
   7. "continuable": true,
   8. // ...
   9. }
   10. ],
   11. // ...
   12. }
   13. }
   ```

   [module.json5](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/master/entry/src/main/module.json5#L2-L106)
2. 在源端UIAbility中实现[onContinue()](../harmonyos-references/js-apis-app-ability-uiability.md#oncontinue)接口，这里需要保存迁移数据（网页地址）到want.param中。

   说明

   若需要接续的数据大于100KB或需要文件接续时，[使用分布式数据对象迁移数据](../harmonyos-guides/app-continuation-guide.md#section14877369451)。

   ```
   1. onContinue(wantParam: Record<string, Object>): AbilityConstant.OnContinueResult |
   2. Promise<AbilityConstant.OnContinueResult> {
   3. // ...
   4. // Get current edit page ViewModel (Web controller lives there).
   5. const viewModel = EditViewModel.getInstance();

   7. if (viewModel) {
   8. const currentUrl = viewModel.controller.getUrl();
   9. wantParam.webUrl = currentUrl;
   10. } else {
   11. hilog.warn(Constant.HILOG_DOMAIN, LOG_TAG, 'No current EditViewModel instance available.');
   12. }
   13. // ...
   14. return AbilityConstant.OnContinueResult.AGREE;
   15. }
   ```

   [EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L129-L151)
3. 实现在[onCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)与[onNewWant()](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)生命周期中恢复数据。

   ```
   1. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
   2. // ...
   3. // Check if it's launched from continuation - use launchParam.launchReason.
   4. if (launchParam.launchReason === AbilityConstant.LaunchReason.CONTINUATION) {
   5. // When restoring from continuation, get the saved Web browsing progress data.
   6. this.restoreWebProgress(want);
   7. }
   8. // ...
   9. }
   ```

   [EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L31-L55)

   ```
   1. onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
   2. // ...
   3. // Check if it's launched from continuation - use launchParam.launchReason.
   4. if (launchParam.launchReason === AbilityConstant.LaunchReason.CONTINUATION) {
   5. // When restoring from continuation, get the saved Web browsing progress data.
   6. this.restoreWebProgress(want);
   7. }
   8. // ...
   9. }
   ```

   [EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L63-L78)

   ```
   1. restoreWebProgress(want: Want): void {
   2. try {
   3. // Get saved webUrl.
   4. const webUrl = want.parameters?.webUrl;
   5. if (webUrl && typeof webUrl === 'string') {
   6. // Save continuation URL to static variable, handled by page's aboutToAppear.
   7. IndexViewModel.getInstance().continuationUrl = webUrl;
   8. hilog.info(Constant.HILOG_DOMAIN, LOG_TAG, 'Saved continuation URL: %{public}s.', webUrl);
   9. } else {
   10. hilog.warn(Constant.HILOG_DOMAIN, LOG_TAG, 'No webUrl found in want parameters.');
   11. }
   12. } catch (error) {
   13. const err = error as BusinessError;
   14. hilog.error(Constant.HILOG_DOMAIN, LOG_TAG, 'Failed to restore web progress. Cause: %{public}s.', err.message);
   15. }
   16. try {
   17. this.context.restoreWindowStage(new LocalStorage());
   18. } catch (error) {
   19. const err = error as BusinessError;
   20. hilog.error(Constant.HILOG_DOMAIN, LOG_TAG,
   21. 'Failed to restore window stage. Cause: %{public}s.', JSON.stringify(err));
   22. }
   23. }
   ```

   [EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L173-L195)

## 分享协作

### 碰一碰邀请协同

**实现原理**

初始化时注册[on('knockShare')](../harmonyos-references/share-harmony-share.md#section1215414133214)事件监听。用户触发分享时保存当前文档URL和docId。设备碰一碰或执行手势后触发事件，优先使用预保存缩略图，创建SharedData对象（类型为HYPERLINK）并调用[SharableTarget.share()](../harmonyos-references/share-harmony-share.md#section1862171812120)分享链接。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/JHMSuLxEQ0KNSUKJzz3IMA/zh-cn_image_0000002525619068.png?HW-CC-KV=V1&HW-CC-Date=20260429T061246Z&HW-CC-Expire=86400&HW-CC-Sign=D1D3D193508C09335952E9A3C1C87DA504D60267672FB73D349BF5A4BA6543B0 "点击放大")

**开发步骤**

1. 配置App Linking服务。App Linking的配置和使用开发者可以参考[使用App Linking实现应用间跳转](../harmonyos-guides/app-linking-startup.md)。

   ```
   1. {
   2. "module": {
   3. // ...
   4. "abilities": [
   5. {
   6. // ...
   7. "exported": true,
   8. // ...
   9. "skills": [
   10. {
   11. "entities": [
   12. "entity.system.home",
   13. // entities must contain "entity.system.browsable"
   14. "entity.system.browsable"
   15. ],
   16. "actions": [
   17. "ohos.want.action.home",
   18. // Actions must contain "ohos.want.action.viewData"
   19. "ohos.want.action.viewData"
   20. ],
   21. "uris": [
   22. {
   23. // The scheme must be configured as https
   24. "scheme": "https",
   25. // The host must be configured as the associated domain name
   26. "host": "www.example.com",
   27. "path": ""
   28. }
   29. ],
   30. // domainVerify must be set to true
   31. "domainVerify": true
   32. }
   33. ]
   34. }
   35. ],
   36. // ...
   37. }
   38. }
   ```

   [module.json5](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/master/entry/src/main/module.json5#L3-L107)
2. 注册碰一碰事件的监听[on('knockShare')](../harmonyos-references/share-harmony-share.md#section1215414133214)和取消监听[off('knockShare')](../harmonyos-references/share-harmony-share.md#section18498201183311)。

   说明

   建议进入页面时，在aboutToAppear()和onPageShow()回调中注册监听；离开页面（包括应用退至后台等情况）时，建议在onPageHide()方法中及时取消监听，避免资源浪费和异常触发。

   注册监听和取消监听的时机非常重要，如果设置错误将无法触发碰一碰功能或者触发后无法正常分享。

   ```
   1. if (canIUse('SystemCapability.Collaboration.HarmonyShare')) {
   2. window.getLastWindow(this.context).then((windowData) => {
   3. try {
   4. this.windowId = windowData.getWindowProperties().id;
   5. // Listen for knock-to-share events.
   6. harmonyShare.on('knockShare', { windowId: this.windowId }, (target) => {
   7. this.handleKnockShare(target);
   8. });
   9. hilog.info(Constant.HILOG_DOMAIN, LOG_TAG, 'Knock-to-share listening started');
   10. } catch (err) {
   11. let error = err as BusinessError;
   12. hilog.error(Constant.HILOG_DOMAIN, LOG_TAG,
   13. `Failed to start knock-to-share listening: ${error.code} ${error.message}`);
   14. }
   15. }).catch((error: BusinessError) => {
   16. hilog.error(Constant.HILOG_DOMAIN, LOG_TAG, `Failed to get window: ${error.code} ${error.message}`);
   17. });
   18. } else {
   19. hilog.info(Constant.HILOG_DOMAIN, LOG_TAG, 'Device does not support HarmonyShare functionality');
   20. }
   ```

   [KnockShareModel.ets](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/master/entry/src/main/ets/model/KnockShareModel.ets#L107-L126)

   ```
   1. if (canIUse('SystemCapability.Collaboration.HarmonyShare') && this.windowId > 0) {
   2. try {
   3. harmonyShare.off('knockShare', { windowId: this.windowId });
   4. hilog.info(Constant.HILOG_DOMAIN, LOG_TAG, 'Knock-to-share listening stopped');
   5. } catch (err) {
   6. let error = err as BusinessError;
   7. hilog.error(Constant.HILOG_DOMAIN, LOG_TAG,
   8. `Failed to stop knock-to-share listening: ${error.code} ${error.message}`);
   9. }
   10. }
   ```

   [KnockShareModel.ets](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/master/entry/src/main/ets/model/KnockShareModel.ets#L135-L144)
3. 加载预览图和发起分享。

   先使用预保存的预览图进行分享，同时通过预览图延迟更新的能力获取页面截图作为预览图，当完成截图后，调用[sharableTarget.updateShareData()](../harmonyos-references/share-harmony-share.md#section18386290710)刷新预览图。

   ```
   1. let thumbnailUri: string | undefined;
   2. const docIdSafe = this.docIdToShare && CommonUtil.isSafeDocIdForPath(this.docIdToShare);
   3. const thumbnailPath = (this.context && docIdSafe) ?
   4. `${this.context.tempDir}/thumbnails/${this.docIdToShare}.jpeg` : '';
   5. if (thumbnailPath && fileIo.accessSync(thumbnailPath)) {
   6. thumbnailUri = fileUri.getUriFromPath(thumbnailPath);
   7. hilog.info(Constant.HILOG_DOMAIN, LOG_TAG, `Using pre-saved thumbnail: ${thumbnailUri}`);
   8. } else if (this.context && this.uiContext) {
   9. // Fallback: capture component snapshot for thumbnail.
   10. const timestamp = new Date().getTime();
   11. const sandboxPath = `${this.context.tempDir}/snapshots/snapshot_${timestamp}.jpeg`;
   12. CommonUtil.captureComponentSnapshot(Constant.COMPONENT_ID_EDIT, this.uiContext, sandboxPath);
   13. thumbnailUri = fileUri.getUriFromPath(sandboxPath);
   14. setTimeout(() => {
   15. try {
   16. hilog.info(Constant.HILOG_DOMAIN, LOG_TAG, 'Link updateShareData thumbnailUri');
   17. target.updateShareData({
   18. thumbnailUri: thumbnailUri
   19. });
   20. } catch (error) {
   21. const err = error as BusinessError;
   22. hilog.error(Constant.HILOG_DOMAIN, LOG_TAG,
   23. `updateShareData thumbnailUri failed: ${err.code} ${err.message}`);
   24. }
   25. }, 3000);
   26. hilog.info(Constant.HILOG_DOMAIN, LOG_TAG, `Component snapshot captured: ${thumbnailUri}`);
   27. }
   ```

   [KnockShareModel.ets](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/master/entry/src/main/ets/model/KnockShareModel.ets#L160-L186)

   调用[sharableTarget.share()](../harmonyos-references/share-harmony-share.md#section1862171812120)方法发起分享，并设置分享卡片的信息，包括数据类型（utd）、content（数据内容）、标题（title）、描述（description）和缩略图URI（thumbnailUri）。这些参数将用于生成特定的卡片模板。

   ```
   1. // Create link share data.
   2. const shareData: systemShare.SharedData = new systemShare.SharedData({
   3. // Set share data type to link.
   4. utd: uniformTypeDescriptor.UniformDataType.HYPERLINK,
   5. // Share document link.
   6. content: this.linkToShare,
   7. title: 'Online Editor Document',
   8. thumbnailUri: thumbnailUri,
   9. description: Constant.SHARE_DEFAULT_DESCRIPTION
   10. });
   11. // Initiate sharing.
   12. target.share(shareData)
   13. .then(() => {
   14. hilog.info(Constant.HILOG_DOMAIN, LOG_TAG, 'Link shared successfully');
   15. })
   16. .catch((error: BusinessError) => {
   17. hilog.error(Constant.HILOG_DOMAIN, LOG_TAG,
   18. `Failed to share link. Error code: ${error.code}, error message: ${error.message}`);
   19. });
   ```

   [KnockShareModel.ets](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/master/entry/src/main/ets/model/KnockShareModel.ets#L189-L207)
4. （对端已安装应用）对端在[onCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)与[onNewWant()](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)生命周期中获取链接，并进行跳转。

   ```
   1. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
   2. // ...
   3. this.getShareData(want);
   4. }

   6. onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
   7. // ...
   8. this.getShareData(want);
   9. }
   ```

   [EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L32-L79)

   ```
   1. private getShareData(want: Want) {
   2. let uri = want?.uri;
   3. if (uri && typeof uri === 'string') {
   4. // Only accept continuation URLs that point to our own server and edit page.
   5. if (this.isSafeContinuationUrl(uri)) {
   6. IndexViewModel.getInstance().continuationUrl = uri;
   7. hilog.info(Constant.HILOG_DOMAIN, LOG_TAG, 'Saved safe continuation URL from share: %{public}s.', uri);
   8. } else {
   9. hilog.warn(Constant.HILOG_DOMAIN, LOG_TAG,
   10. 'Rejected unsafe continuation URL from share (potential XSS or external site): %{public}s.', uri);
   11. }
   12. }
   13. }
   ```

   [EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L202-L214)
5. （对端未安装应用）为提升用户未安装应用时的体验，可配置[通过直达应用市场能力跳转至应用市场下载详情页](../harmonyos-guides/applinking-direct-to-ag.md)功能，引导用户下载安装应用。配置完成后，当对端收到源端分享的App Linking链接时，若设备未安装目标应用，系统将直接跳转至应用市场的应用详情页，支持一键下载安装。

   同时，需要实现[通过延迟链接跳转至应用详情页](../harmonyos-guides/applinking-deferredlink.md)功能，确保安装后首次启动可直达内容。安装完应用之后，开发者可以在用户首次打开应用时，使用延迟链接，直接跳转到视频播放页面，这一流程不仅优化了用户体验，还有助于提升链接的转化率。

### 隔空传送邀请协同

**实现原理**

初始化时注册[on('gesturesShare')](../harmonyos-references/share-harmony-share.md#section199317814132)事件监听。用户触发分享时保存当前文档URL和docId。设 备检测到隔空手势后触发事件，构建[SharedRecord](../harmonyos-references/share-system-share.md#section20696483813)对象，并调用[SharableTarget.share()](../harmonyos-references/share-harmony-share.md#section1862171812120)分享链接。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/dmOmVLDYTzmIa6_ebWmA8w/zh-cn_image_0000002556778947.png?HW-CC-KV=V1&HW-CC-Date=20260429T061246Z&HW-CC-Expire=86400&HW-CC-Sign=5F523FC91B7B8F16A5D6D9F4D699EDAAA8805F2772D91A4E9573242EE271838D "点击放大")

**开发步骤**

1. 使用[on('gesturesShare')](../harmonyos-references/share-harmony-share.md#section199317814132)监听，使用[off('gesturesShare')](../harmonyos-references/share-harmony-share.md#section1699538101317)方法取消监听。

   说明

   建议进入页面时，aboutToAppear()和onPageShow()回调中注册监听；离开页面（包括应用退至后台等情况）时，比如在onPageHide()方法中及时取消监听，避免资源浪费和异常触发。

   注册监听和取消监听的时机非常重要，如果设置错误将无法触发碰一碰功能或者触发后无法正常分享。

   ```
   1. if (canIUse('SystemCapability.Collaboration.HarmonyShare')) {
   2. window.getLastWindow(this.context).then((windowData) => {
   3. // ...
   4. harmonyShare.on('gesturesShare', { windowId: this.windowId }, (target) => {
   5. this.handleGestureShare(target);
   6. });
   7. // ...
   8. }).catch((error: BusinessError) => {
   9. // ...
   10. });
   11. } else {
   12. // ...

   14. }
   ```

   [GesturesShareModel.ets](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/master/entry/src/main/ets/model/GesturesShareModel.ets#L89-L124)

   ```
   1. if (canIUse('SystemCapability.Collaboration.HarmonyShare')) {
   2. // ...
   3. harmonyShare.off('gesturesShare', { windowId: this.windowId });
   4. // ...
   5. }
   ```

   [GesturesShareModel.ets](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/master/entry/src/main/ets/model/GesturesShareModel.ets#L133-L146)
2. 调用[sharableTarget.share()](../harmonyos-references/share-harmony-share.md#section1862171812120)方法发起分享，并设置分享卡片的信息，包括数据类型（utd）、content（数据内容）、标题（title）、描述（description）和缩略图URI（thumbnailUri）。这些参数将用于生成特定的卡片模板。

   ```
   1. private handleGestureShare(target: harmonyShare.SharableTarget): void {
   2. // ...
   3. let shareData: systemShare.SharedData = new systemShare.SharedData({
   4. // Set share data type to link.
   5. utd: uniformTypeDescriptor.UniformDataType.HYPERLINK,
   6. content: this.linkToShare,
   7. title: 'Online Editor Document',
   8. thumbnailUri: this.getThumbnailUri(),
   9. description: Constant.SHARE_DEFAULT_DESCRIPTION
   10. });

   12. target.share(shareData).then(() => {
   13. hilog.info(Constant.HILOG_DOMAIN, LOG_TAG, 'Link shared successfully.');
   14. if (this.shareCallback) {
   15. this.shareCallback('link', this.linkToShare);
   16. }
   17. }).catch((error: BusinessError) => {
   18. hilog.error(
   19. Constant.HILOG_DOMAIN,
   20. LOG_TAG,
   21. `Failed to share link. Error code: ${error.code}, Error message: ${error.message}.`
   22. );
   23. });
   24. // ...
   25. }
   ```

   [GesturesShareModel.ets](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration/blob/master/entry/src/main/ets/model/GesturesShareModel.ets#L155-L195)
3. 对端拉起和引导下载，和碰一碰邀请协同[第4步](bpta-collaboration-office.md#li616744215363)和[第5步](bpta-collaboration-office.md#li474162221318)相同。

## 示例代码

* [基于ArkWeb和自由流转实现办公编辑协同](https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration)
