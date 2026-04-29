---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-events-drag-event
title: 支持统一拖拽
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 添加交互响应 > 支持统一拖拽
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:004eb7d4e68dd6eb31721576c7d7500907b5c795dbfe911424b61b5cf06e0dd5
---

统一拖拽提供了一种通过鼠标或手势触屏传递数据的机制，即从一个组件位置拖出（drag）数据并将其拖入（drop）到另一个组件位置，以触发响应。在这一过程中，拖出方提供数据，而拖入方负责接收和处理数据。这一操作使用户能够便捷地移动、复制或删除指定内容。

## 基本概念

* 拖拽操作：在可响应拖出的组件上长按并滑动以触发拖拽行为，当用户释放手指或鼠标时，拖拽操作即告结束。
* 拖拽背景（背板）：用户拖动数据时的形象化表示。开发者可以通过[onDragStart](../harmonyos-references/ts-universal-events-drag-drop.md#ondragstart)的[CustomBuilder](../harmonyos-references/ts-types.md#custombuilder8)或[DragItemInfo](../harmonyos-references/ts-universal-events-drag-drop.md#dragiteminfo)进行设置，也可以通过[dragPreview](../harmonyos-references/ts-universal-attributes-drag-drop.md#dragpreview11)通用属性进行自定义。
* 拖拽内容：被拖动的数据，使用UDMF统一API [UnifiedData](../harmonyos-references/js-apis-data-unifieddatachannel.md#unifieddata) 进行封装，确保数据的一致性和安全性。
* 拖出对象：触发拖拽操作并提供数据的组件，通常具有响应拖拽的特性。
* 拖入目标：可接收并处理拖动数据的组件，能够根据拖入的数据执行相应的操作。
* 拖拽点：鼠标或手指与屏幕的接触位置，用于判断是否进入组件范围。判定依据是接触点是否位于组件的范围内。

## 拖拽方式

拖拽方式包含手势拖拽和鼠标拖拽，有助于开发者理解回调事件触发的时机。

### ​手势拖拽

在手势长按触发拖拽的场景中，ArkUI在发起拖拽前会校验当前组件是否具备拖拽功能。若为默认支持拖出能力的组件（[Search](../harmonyos-references/ts-basic-components-search.md)、[TextInput](../harmonyos-references/ts-basic-components-textinput.md)、[TextArea](../harmonyos-references/ts-basic-components-textarea.md)、[RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)、[Text](../harmonyos-references/ts-basic-components-text.md)、[Image](../harmonyos-references/ts-basic-components-image.md)、[Hyperlink](../harmonyos-references/ts-container-hyperlink.md)），需要判断是否设置了[draggable](../harmonyos-references/ts-universal-attributes-drag-drop.md#draggable)为true。其他组件则需额外确认是否已设置[onDragStart](../harmonyos-references/ts-universal-events-drag-drop.md#ondragstart)回调函数。在满足上述条件后，长按时间达到或超过500ms即可触发拖拽，而长按800ms时，系统开始执行预览图的浮起动效。若与Menu功能结合使用，并在[bindMenu](../harmonyos-references/ts-universal-attributes-menu.md#bindmenu11)中通过isShow控制其显示与隐藏，建议避免在用户操作800ms后才控制菜单显示，此举可能引发非预期的行为。

手势拖拽（手指/手写笔）触发拖拽流程：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/I9gmL4BuTme8LW0yq0AMyg/zh-cn_image_0000002589324323.png?HW-CC-KV=V1&HW-CC-Date=20260429T052806Z&HW-CC-Expire=86400&HW-CC-Sign=8ADA7BCE61A1B752C12970042165EDBD124172BD82B1FA7472199D5EEAB80A64)

### ​鼠标拖拽

鼠标拖拽操作遵循即拖即走的模式，当鼠标左键在可拖拽的组件上按下并移动超过1vp时，即可触发拖拽功能。鼠标拖拽的其他流程与手势拖拽流程相似，可参考[手势拖拽](arkts-common-events-drag-event.md#手势拖拽)。

## 拖拽回调

当前不仅支持应用内部的拖拽，还支持跨应用的拖拽操作。为了帮助开发者更好地感知拖拽状态并调整系统默认的拖拽行为，ArkUI提供了多个回调事件，具体详情如下：

| **回调事件** | **说明** |
| --- | --- |
| [onDragStart](../harmonyos-references/ts-universal-events-drag-drop.md#ondragstart) | 拖出的组件产生拖出动作时，该回调触发。  该回调可以感知拖拽行为的发起，开发者可以在onDragStart方法中设置拖拽过程中传递的数据，并自定义拖拽的背板图像。建议开发者采用pixelmap的方式来返回背板图像，避免使用customBuilder，因为后者可能会带来额外的性能开销。 |
| [onDragEnter](../harmonyos-references/ts-universal-events-drag-drop.md#ondragenter) | 当拖拽操作的拖拽点进入组件的范围时，如果该组件监听了[onDrop](../harmonyos-references/ts-universal-events-drag-drop.md#ondrop)事件，此回调将会被触发。 |
| [onDragMove](../harmonyos-references/ts-universal-events-drag-drop.md#ondragmove) | 当拖拽点在组件范围内移动时，如果该组件监听了onDrop事件，此回调将会被触发。  在这一过程中，可以通过调用[DragEvent](../harmonyos-references/ts-universal-events-drag-drop.md#dragevent7)中的setResult方法来影响系统在部分场景下的外观表现：  1. 设置DragResult.DROP\_ENABLED，组件允许落入。  2. 设置DragResult.DROP\_DISABLED，组件不允许落入。 |
| [onDragLeave](../harmonyos-references/ts-universal-events-drag-drop.md#ondragleave) | 当拖拽点移出组件范围时，如果该组件监听了onDrop事件，此回调将会被触发。  在以下两种情况下，系统默认不会触发onDragLeave事件：  1. 父组件移动到子组件。  2. 目标组件与当前组件布局有重叠。  API version 12开始可通过[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)中的[setDragEventStrictReportingEnabled](../harmonyos-references/arkts-apis-uicontext-dragcontroller.md#setdrageventstrictreportingenabled12)方法严格触发onDragLeave事件。 |
| [onDrop](../harmonyos-references/ts-universal-events-drag-drop.md#ondrop) | 当用户在组件范围内释放拖拽操作时，此回调会被触发。开发者需在此回调中通过DragEvent的setResult方法来设置拖拽结果，否则在拖出方组件的onDragEnd方法中，通过getResult方法获取的将只是默认的处理结果DragResult.DRAG\_FAILED。  此回调是开发者干预系统默认拖入处理行为的关键点，系统会优先执行开发者定义的onDrop回调。通过在onDrop回调中调用setResult方法，开发者可以告知系统如何处理被拖拽的数据。  1. 设置 DragResult.DRAG\_SUCCESSFUL，数据完全由开发者自己处理，系统不进行处理。  2. 设置DragResult.DRAG\_FAILED，数据不再由系统继续处理。  3. 设置DragResult.DRAG\_CANCELED，系统也不需要进行数据处理。  4. 设置DragResult.DROP\_ENABLED或DragResult.DROP\_DISABLED会被忽略，等同于设置DragResult.DRAG\_SUCCESSFUL。 |
| [onDragEnd](../harmonyos-references/ts-universal-events-drag-drop.md#ondragend10) | 当用户释放拖拽时，拖拽活动终止，发起拖出动作的组件将触发该回调函数。 |
| [onPreDrag](../harmonyos-references/ts-universal-events-drag-drop.md#onpredrag12) | 当触发拖拽事件的不同阶段时，绑定此事件的组件会触发该回调函数。  开发者可利用此方法，在拖拽开始前的不同阶段，根据[PreDragStatus](../harmonyos-references/ts-universal-events-drag-drop.md#predragstatus12枚举说明)枚举准备相应数据。  1. ACTION\_DETECTING\_STATUS：拖拽手势启动阶段。按下50ms时触发。  2. READY\_TO\_TRIGGER\_DRAG\_ACTION：拖拽准备完成，可发起拖拽阶段。按下500ms时触发。  3. PREVIEW\_LIFT\_STARTED：拖拽浮起动效发起阶段。按下800ms时触发。  4. PREVIEW\_LIFT\_FINISHED：拖拽浮起动效结束阶段。浮起动效完全结束时触发。  5. PREVIEW\_LANDING\_STARTED：拖拽落回动效发起阶段。落回动效发起时触发。  6. PREVIEW\_LANDING\_FINISHED：拖拽落回动效结束阶段。落回动效结束时触发。  7. ACTION\_CANCELED\_BEFORE\_DRAG：拖拽浮起落位动效中断。已满足READY\_TO\_TRIGGER\_DRAG\_ACTION状态后，未达到动效阶段，手指抬起时触发。  8. PREPARING\_FOR\_DRAG\_DETECTION18+：拖拽准备完成，可发起拖拽阶段。按下350ms时触发。 |
| [onDragSpringLoading](../harmonyos-references/ts-universal-events-drag-drop.md#ondragspringloading20) | 当拖拽对象悬停在绑定此事件的组件上时，触发回调通知。此时只有一个目标可以成为响应方，并且子组件始终具有更高的响应优先级。  开发者可以通过[SpringLoadingContext](../harmonyos-references/js-apis-arkui-dragcontroller.md#springloadingcontext20)配置回调的上下文信息，包括当前悬停检测的状态、一次悬停检测中的回调通知次数、拖拽信息和配置信息等。  从API version 20开始，支持调用该接口。 |

## 拖拽事件

拖拽回调函数可以接收[DragEvent](../harmonyos-references/ts-universal-events-drag-drop.md#dragevent7)对象。通过该对象发出拖拽事件，其中包含了拖拽行为的详细信息，以及拖出时组件向系统提供的数据等。

通过[DragEvent](../harmonyos-references/ts-universal-events-drag-drop.md#dragevent7)支持的get方法可以获取拖拽行为的详细信息。下表展示了在相应的拖拽回调中，这些get方法是否能够返回有效数据。

| 回调事件 | onDragStart | onDragEnter | onDragMove | onDragLeave | onDrop | onDragEnd |
| --- | --- | --- | --- | --- | --- | --- |
| getData | — | — | — | — | 支持 | — |
| getSummary | — | 支持 | 支持 | 支持 | 支持 | — |
| getResult | — | — | — | — | — | 支持 |
| getPreviewRect | — | — | — | — | 支持 | — |
| getVelocity/X/Y | — | 支持 | 支持 | 支持 | 支持 | — |
| getWindowX/Y | 支持 | 支持 | 支持 | 支持 | 支持 | — |
| getDisplayX/Y | 支持 | 支持 | 支持 | 支持 | 支持 | — |
| getX/Y | 支持 | 支持 | 支持 | 支持 | 支持 | — |
| getModifierKeyState | 支持 | 支持 | 支持 | 支持 | 支持 | 支持 |
| startDataLoading | — | — | — | — | 支持 | — |
| getDisplayId | 支持 | 支持 | 支持 | 支持 | 支持 | — |
| getDragSource | 支持 | 支持 | 支持 | 支持 | 支持 | 支持 |
| isRemote | 支持 | 支持 | 支持 | 支持 | 支持 | 支持 |
| getGlobalDisplayX/Y | 支持 | 支持 | 支持 | 支持 | 支持 | — |
| behavior | — | — | — | — | — | 支持 |

[DragEvent](../harmonyos-references/ts-universal-events-drag-drop.md#dragevent7)支持相关set方法向系统传递信息，这些信息部分会影响系统对UI或数据的处理方式。下表列出了set方法应该在回调的哪个阶段执行才会被系统接收并处理。

| 回调事件 | onDragStart | onDragEnter | onDragMove | onDragLeave | onDrop |
| --- | --- | --- | --- | --- | --- |
| useCustomDropAnimation | — | — | — | — | 支持 |
| setData | 支持 | — | — | — | — |
| setResult | 支持，可通过set failed或cancel来阻止拖拽发起 | 支持，不作为最终结果传递给onDragEnd | 支持，不作为最终结果传递给onDragEnd | 支持，不作为最终结果传递给onDragEnd | 支持，作为最终结果传递给onDragEnd |
| setDataLoadParams | 支持 | — | — | — | — |
| behavior | — | 支持 | 支持 | 支持 | 支持 |

## 拖拽背板图

在拖拽移动过程中显示的背板图并非组件本身，而是表示用户拖动的数据，开发者可将其设定为任意可显示的图像。具体而言，onDragStart回调中返回的customBuilder或pixelmap可以用于设置拖拽移动过程中的背板图，而浮起图则默认采用组件本身的截图。dragpreview属性中设定的customBuilder或pixelmap可以用于配置浮起和拖拽过程的背板图。若开发者未配置背板图，系统将自动采用组件本身的截图作为拖拽和浮起时的背板图。

拖拽背板图当前支持设置透明度、圆角、阴影和模糊，具体用法见[拖拽控制](../harmonyos-references/ts-universal-attributes-drag-drop.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/g5u7O9LFS1a-zgH5en0VVw/zh-cn_image_0000002589244263.png?HW-CC-KV=V1&HW-CC-Date=20260429T052806Z&HW-CC-Expire=86400&HW-CC-Sign=FD8397028E294891FC0BE0B44A2C4187B0F8C6DBAC6830E82AD1F123991C368E)

**约束限制：**

* 对于容器组件，如果内部内容通过position、offset等接口使得绘制区域超出了容器组件范围，则系统截图无法截取到范围之外的内容。此种情况下，如果一定要浮起，即拖拽背板能够包含范围之外的内容，则可考虑通过扩大容器范围或自定义方式实现。
* 不论是使用自定义builder或是系统默认截图方式，截图都暂时无法应用[scale](../harmonyos-references/ts-universal-attributes-transformation.md#scale)、[rotate](../harmonyos-references/ts-universal-attributes-transformation.md#rotate)等图形变换效果。

## 使用拖拽能力

### 通用拖拽适配

如下以[Image](../harmonyos-references/ts-basic-components-image.md)组件为例，介绍组件拖拽开发的基本步骤，以及开发中需要注意的事项。

1. 组件使能拖拽。

   设置draggable属性为true，并配置onDragStart回调函数。在回调函数中，可通过UDMF（用户数据管理框架）设置拖拽的数据，并返回自定义的拖拽背景图像。

   ```
   1. import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';
   ```

   [DefaultDrag.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/drag/DefaultDrag.ets#L17-L19)

   ```
   1. // 请将$r('app.media.app_icon')替换为实际资源文件
   2. Image($r('app.media.app_icon'))
   3. .width(100)
   4. .height(100)
   5. .draggable(true)
   6. // ...
   7. .onDragStart((event) => {
   8. let data: unifiedDataChannel.Image = new unifiedDataChannel.Image();
   9. // 'resources/base/media/app_icon.png'需要替换为开发者所需的图像资源文件
   10. data.imageUri = 'resources/base/media/app_icon.png';
   11. let unifiedData = new unifiedDataChannel.UnifiedData(data);
   12. event.setData(unifiedData);

   14. let dragItemInfo: DragItemInfo = {
   15. pixelMap: this.pixmap,
   16. extraInfo: 'this is extraInfo',
   17. };
   18. // onDragStart回调函数中返回自定义拖拽背板图
   19. return dragItemInfo;
   20. })
   ```

   [DefaultDrag.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/drag/DefaultDrag.ets#L116-L148)

   手势场景触发的拖拽功能依赖于底层绑定的长按手势。如果开发者在可拖拽组件上也绑定了长按手势，这将与底层的长按手势产生冲突，进而导致拖拽操作失败。为解决此类问题，可以采用并行手势的方案，具体如下：

   ```
   1. .parallelGesture(LongPressGesture().onAction(() => {
   2. this.getUIContext()
   3. .getPromptAction()
   4. .showToast({ duration: 100, message: 'Long press gesture trigger' });
   5. }))
   ```

   [DefaultDrag.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/drag/DefaultDrag.ets#L126-L132)
2. 自定义拖拽背板图。

   可以通过在长按50ms时触发的回调中设置[onPreDrag](../harmonyos-references/ts-universal-events-drag-drop.md#onpredrag12)回调函数，来提前准备自定义拖拽背板图的pixmap。

   ```
   1. .onPreDrag((preDragStatus: PreDragStatus) => {
   2. if (preDragStatus == PreDragStatus.ACTION_DETECTING_STATUS) {
   3. this.getComponentSnapshot();
   4. }
   5. })
   ```

   [DefaultDrag.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/drag/DefaultDrag.ets#L150-L156)

   pixmap的生成可以调用[this.getUIContext().getComponentSnapshot().createFromBuilder()](../harmonyos-references/arkts-apis-uicontext-componentsnapshot.md#createfrombuilder12)来实现。

   ```
   1. import { hilog } from '@kit.PerformanceAnalysisKit';

   3. const DOMAIN = 0x0000;
   4. const TAG = 'DefaultDragError: ';
   ```

   [DefaultDrag.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/drag/DefaultDrag.ets#L24-L29)

   ```
   1. @Builder
   2. pixelMapBuilder() {
   3. Column() {
   4. // 请将$r('app.media.startIcon')替换为实际资源文件
   5. Image($r('app.media.startIcon'))
   6. .width(120)
   7. .height(120)
   8. // ...
   9. }
   10. }

   12. // ...
   13. // 调用componentSnapshot中的createFromBuilder接口截取自定义builder的截图
   14. private getComponentSnapshot(): void {
   15. this.getUIContext().getComponentSnapshot().createFromBuilder(() => {
   16. this.pixelMapBuilder();
   17. },
   18. (error: Error, pixmap: image.PixelMap) => {
   19. if (error) {
   20. hilog.error(DOMAIN, TAG, '%{public}s', JSON.stringify(error));
   21. return;
   22. }
   23. this.pixmap = pixmap;
   24. });
   25. }
   ```

   [DefaultDrag.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/drag/DefaultDrag.ets#L40-L101)
3. 若开发者需确保触发[onDragLeave](../harmonyos-references/ts-universal-events-drag-drop.md#ondragleave)事件，应通过调用[setDragEventStrictReportingEnabled](../harmonyos-references/arkts-apis-uicontext-dragcontroller.md#setdrageventstrictreportingenabled12)方法进行设置。

   ```
   1. import { UIAbility } from '@kit.AbilityKit';
   2. import { window, UIContext } from '@kit.ArkUI';

   4. export default class EntryAbility extends UIAbility {
   5. // ···
   6. onWindowStageCreate(windowStage: window.WindowStage): void {
   7. windowStage.loadContent('pages/Index', (err, data) => {
   8. if (err.code) {
   9. return;
   10. }
   11. windowStage.getMainWindow((err, data) => {
   12. if (err.code) {
   13. return;
   14. }
   15. let windowClass: window.Window = data;
   16. let uiContext: UIContext = windowClass.getUIContext();
   17. uiContext.getDragController().setDragEventStrictReportingEnabled(true);
   18. });
   19. });
   20. }
   21. // ···
   22. }
   ```

   [EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/entryability/EntryAbility.ets#L18-L65)
4. 拖拽过程显示角标样式。

   通过设置[allowDrop](../harmonyos-references/ts-universal-attributes-drag-drop.md#allowdrop)来定义接收的数据类型，这将影响角标显示。当拖拽的数据符合定义的允许落入的数据类型时，角标会显示加号。当拖拽的数据类型不在允许范围内时，可强制设置为显示禁用角标。若未设置allowDrop，则角标不会显示加号。以下代码示例表示仅接收UnifiedData中定义的HYPERLINK和PLAIN\_TEXT类型数据，其他类型数据将被禁止落入。

   ```
   1. .allowDrop([uniformTypeDescriptor.UniformDataType.HYPERLINK,
   2. uniformTypeDescriptor.UniformDataType.PLAIN_TEXT])
   ```

   [DefaultDrag.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/drag/DefaultDrag.ets#L190-L193)

   在实现onDrop回调的情况下，还可以在onDragMove中设置[DragResult](../harmonyos-references/ts-universal-events-drag-drop.md#dragresult10枚举说明)为DROP\_ENABLED，并将[DragBehavior](../harmonyos-references/ts-universal-events-drag-drop.md#dragbehavior10)设置为COPY或MOVE，以此来控制角标中的加号是否显示。当设置为COPY时，角标显示加号；设置为MOVE时，角标不显示加号。

   ```
   1. .onDragMove((event) => {
   2. event.setResult(DragResult.DROP_ENABLED)
   3. event.dragBehavior = DragBehavior.COPY
   4. })
   ```

   [DefaultDrag.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/drag/DefaultDrag.ets#L184-L189)
5. 拖拽数据的接收。

   需要设置onDrop回调函数，并在回调函数中处理拖拽数据，显式设置拖拽结果。

   ```
   1. .onDrop((dragEvent?: DragEvent) => {
   2. // 获取拖拽数据
   3. this.getDataFromUdmf((dragEvent as DragEvent), (event: DragEvent) => {
   4. let records: unifiedDataChannel.UnifiedRecord[] = event.getData().getRecords();
   5. let rect: Rectangle = event.getPreviewRect();
   6. this.imageWidth = Number(rect.width);
   7. this.imageHeight = Number(rect.height);
   8. this.targetImage = (records[0] as unifiedDataChannel.Image).imageUri;
   9. this.imgState = Visibility.None;
   10. // 显式设置result为successful，则将该值传递给拖出方的onDragEnd
   11. event.setResult(DragResult.DRAG_SUCCESSFUL);
   12. })
   13. })
   ```

   [DefaultDrag.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/drag/DefaultDrag.ets#L197-L211)

   数据的传递是通过UDMF实现的，在数据较大时可能存在时延，因此在首次获取数据失败时建议加1500ms的延迟重试机制。

   ```
   1. getDataFromUdmfRetry(event: DragEvent, callback: (data: DragEvent) => void) {
   2. try {
   3. let data: UnifiedData = event.getData();
   4. if (!data) {
   5. return false;
   6. }
   7. let records: unifiedDataChannel.UnifiedRecord[] = data.getRecords();
   8. if (!records || records.length <= 0) {
   9. return false;
   10. }
   11. callback(event);
   12. return true;
   13. } catch (e) {
   14. hilog.error(DOMAIN, TAG, `${(e as BusinessError).code}, message: ${(e as BusinessError).message}`);
   15. return false;
   16. }
   17. }

   19. getDataFromUdmf(event: DragEvent, callback: (data: DragEvent) => void) {
   20. if (this.getDataFromUdmfRetry(event, callback)) {
   21. return;
   22. }
   23. setTimeout(() => {
   24. this.getDataFromUdmfRetry(event, callback);
   25. }, 1500);
   26. }
   ```

   [DefaultDrag.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/drag/DefaultDrag.ets#L57-L85)
6. 拖拽发起方可以通过设置onDragEnd回调感知拖拽结果。

   ```
   1. .onDragEnd((event) => {
   2. // onDragEnd里取到的result值在接收方onDrop设置
   3. if (event.getResult() === DragResult.DRAG_SUCCESSFUL) {
   4. this.getUIContext().getPromptAction().showToast({ duration: 100, message: 'Drag Success' });
   5. } else if (event.getResult() === DragResult.DRAG_FAILED) {
   6. this.getUIContext().getPromptAction().showToast({ duration: 100, message: 'Drag failed' });
   7. }
   8. })
   ```

   [DefaultDrag.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/drag/DefaultDrag.ets#L157-L168)

**完整示例：**

```
1. import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { image } from '@kit.ImageKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. const DOMAIN = 0x0000;
7. const TAG = 'DefaultDragError: ';

9. @Entry
10. @Component
11. export struct DefaultDrag {
12. @State targetImage: string = '';
13. @State imageWidth: number = 100;
14. @State imageHeight: number = 100;
15. @State imgState: Visibility = Visibility.Visible;
16. @State pixmap: image.PixelMap | undefined = undefined;

18. @Builder
19. pixelMapBuilder() {
20. Column() {
21. // 请将$r('app.media.startIcon')替换为实际资源文件
22. Image($r('app.media.startIcon'))
23. .width(120)
24. .height(120)
25. // ...
26. }
27. }

29. getDataFromUdmfRetry(event: DragEvent, callback: (data: DragEvent) => void) {
30. try {
31. let data: UnifiedData = event.getData();
32. if (!data) {
33. return false;
34. }
35. let records: unifiedDataChannel.UnifiedRecord[] = data.getRecords();
36. if (!records || records.length <= 0) {
37. return false;
38. }
39. callback(event);
40. return true;
41. } catch (e) {
42. hilog.error(DOMAIN, TAG, `${(e as BusinessError).code}, message: ${(e as BusinessError).message}`);
43. return false;
44. }
45. }

47. getDataFromUdmf(event: DragEvent, callback: (data: DragEvent) => void) {
48. if (this.getDataFromUdmfRetry(event, callback)) {
49. return;
50. }
51. setTimeout(() => {
52. this.getDataFromUdmfRetry(event, callback);
53. }, 1500);
54. }

56. // 调用componentSnapshot中的createFromBuilder接口截取自定义builder的截图
57. private getComponentSnapshot(): void {
58. this.getUIContext().getComponentSnapshot().createFromBuilder(() => {
59. this.pixelMapBuilder();
60. },
61. (error: Error, pixmap: image.PixelMap) => {
62. if (error) {
63. hilog.error(DOMAIN, TAG, '%{public}s', JSON.stringify(error));
64. return;
65. }
66. this.pixmap = pixmap;
67. });
68. }

70. build() {
71. // ...
72. Row() {
73. Column() {
74. Text('start Drag')
75. .fontSize(18)
76. .width('100%')
77. .height(40)
78. .margin(10)
79. .backgroundColor('#008888')
80. Row() {
81. // 请将$r('app.media.app_icon')替换为实际资源文件
82. Image($r('app.media.app_icon'))
83. .width(100)
84. .height(100)
85. .draggable(true)
86. .margin({ left: 15 })
87. .visibility(this.imgState)
88. // 绑定平行手势，可同时触发应用自定义长按手势
89. .parallelGesture(LongPressGesture().onAction(() => {
90. this.getUIContext()
91. .getPromptAction()
92. .showToast({ duration: 100, message: 'Long press gesture trigger' });
93. }))
94. .onDragStart((event) => {
95. let data: unifiedDataChannel.Image = new unifiedDataChannel.Image();
96. // 'resources/base/media/app_icon.png'需要替换为开发者所需的图像资源文件
97. data.imageUri = 'resources/base/media/app_icon.png';
98. let unifiedData = new unifiedDataChannel.UnifiedData(data);
99. event.setData(unifiedData);

101. let dragItemInfo: DragItemInfo = {
102. pixelMap: this.pixmap,
103. extraInfo: 'this is extraInfo',
104. };
105. // onDragStart回调函数中返回自定义拖拽背板图
106. return dragItemInfo;
107. })
108. // 提前准备拖拽自定义背板图
109. .onPreDrag((preDragStatus: PreDragStatus) => {
110. if (preDragStatus == PreDragStatus.ACTION_DETECTING_STATUS) {
111. this.getComponentSnapshot();
112. }
113. })
114. .onDragEnd((event) => {
115. // onDragEnd里取到的result值在接收方onDrop设置
116. if (event.getResult() === DragResult.DRAG_SUCCESSFUL) {
117. this.getUIContext().getPromptAction().showToast({ duration: 100, message: 'Drag Success' });
118. } else if (event.getResult() === DragResult.DRAG_FAILED) {
119. this.getUIContext().getPromptAction().showToast({ duration: 100, message: 'Drag failed' });
120. }
121. })
122. }

124. Text('Drag Target Area')
125. .fontSize(20)
126. .width('100%')
127. .height(40)
128. .margin(10)
129. .backgroundColor('#008888')
130. Row() {
131. Image(this.targetImage)
132. .width(this.imageWidth)
133. .height(this.imageHeight)
134. .draggable(true)
135. .margin({ left: 15 })
136. .border({ color: Color.Black, width: 1 })// 控制角标显示类型为MOVE，即不显示角标
137. .onDragMove((event) => {
138. event.setResult(DragResult.DROP_ENABLED);
139. event.dragBehavior = DragBehavior.COPY;
140. })
141. .allowDrop([uniformTypeDescriptor.UniformDataType.HYPERLINK,
142. uniformTypeDescriptor.UniformDataType.PLAIN_TEXT])
143. .allowDrop([uniformTypeDescriptor.UniformDataType.IMAGE])
144. .onDrop((dragEvent?: DragEvent) => {
145. // 获取拖拽数据
146. this.getDataFromUdmf((dragEvent as DragEvent), (event: DragEvent) => {
147. let records: unifiedDataChannel.UnifiedRecord[] = event.getData().getRecords();
148. let rect: Rectangle = event.getPreviewRect();
149. this.imageWidth = Number(rect.width);
150. this.imageHeight = Number(rect.height);
151. this.targetImage = (records[0] as unifiedDataChannel.Image).imageUri;
152. this.imgState = Visibility.None;
153. // 显式设置result为successful，则将该值传递给拖出方的onDragEnd
154. event.setResult(DragResult.DRAG_SUCCESSFUL);
155. });
156. })
157. }
158. }
159. .width('100%')
160. .height('100%')
161. }
162. .height('100%')
163. }

165. // ...
166. }
```

[DefaultDrag.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/drag/DefaultDrag.ets#L16-L233)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/3lQU6BPsQVGJHFGVocIYEA/zh-cn_image_0000002558764456.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052806Z&HW-CC-Expire=86400&HW-CC-Sign=DCF75C40A2BE3ECD8A305BEF133222D58AEA5875023D6B3E2EB31FC9F7276ABD)

### 多选拖拽适配

从API version 12开始，[Grid](../harmonyos-references/ts-container-grid.md)组件和[List](../harmonyos-references/ts-container-list.md)组件中的GridItem和ListItem组件支持多选与拖拽功能。目前，仅支持onDragStart的触发方式。

以下以Grid为例，详细介绍实现多选拖拽的基本步骤，以及在开发过程中需要注意的事项。

1. 组件多选拖拽使能。

   创建GridItem子组件并绑定onDragStart回调函数。同时设置GridItem组件的状态为可选中。

   ```
   1. Grid() {
   2. ForEach(this.numbers, (idx: number) => {
   3. GridItem() {
   4. Column()
   5. .backgroundColor(Color.Blue)
   6. .width(50)
   7. .height(50)
   8. .opacity(1.0)
   9. .id('grid' + idx)
   10. }
   11. // ···
   12. .onDragStart(() => {
   13. })
   14. .selectable(true)
   15. // ···
   16. }, (idx: string) => idx)
   17. }
   ```

   [GridEts.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/grid/GridEts.ets#L118-L247)

   多选拖拽功能默认处于关闭状态。若要启用此功能，需在[dragPreviewOptions](../harmonyos-references/ts-universal-attributes-drag-drop.md#dragpreviewoptions11)接口的DragInteractionOptions参数中，将isMultiSelectionEnabled设置为true，以表明当前组件支持多选。此外，DragInteractionOptions还包含defaultAnimationBeforeLifting参数，用于控制组件浮起前的默认效果。将该参数设置为true，组件在浮起前将展示一个默认的缩小动画效果。

   ```
   1. .dragPreviewOptions({ numberBadge: this.numberBadge },
   2. { isMultiSelectionEnabled: true, defaultAnimationBeforeLifting: true })
   ```

   [GridEts.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/grid/GridEts.ets#L267-L270)

   为了确保选中状态，应将GridItem子组件的selected属性设置为true。例如，可以通过调用[onClick](../harmonyos-references/ts-universal-events-click.md#onclick)来设置特定组件为选中状态。

   ```
   1. .selected(this.isSelectedGrid[idx])
   2. // ···
   3. .onClick(() => {
   4. this.isSelectedGrid[idx] = !this.isSelectedGrid[idx];
   5. // ···
   6. })
   ```

   [GridEts.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/grid/GridEts.ets#L150-L210)
2. 优化多选拖拽性能。

   在多选拖拽操作中，当多选触发聚拢动画效果时，系统会截取当前屏幕内显示的选中组件图像。如果选中组件数量过多，可能会造成较高的性能消耗。为了优化性能，多选拖拽功能支持从dragPreview中获取截图，用以实现聚拢动画效果，从而有效节省系统资源。

   ```
   1. .dragPreview({
   2. pixelMap: this.pixmap
   3. })
   ```

   [GridEts.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/grid/GridEts.ets#L135-L247)

   截图的获取可以在选中组件时通过调用[this.getUIContext().getComponentSnapshot().get()](../harmonyos-references/arkts-apis-uicontext-componentsnapshot.md#get12)方法获取。以下示例通过获取组件对应id的方法进行截图。

   ```
   1. @State previewData: DragItemInfo[] = [];
   2. @State isSelectedGrid: boolean[] = [];
   3. // ...
   4. .onClick(() => {
   5. this.isSelectedGrid[idx] = !this.isSelectedGrid[idx];
   6. if (this.isSelectedGrid[idx]) {
   7. // ...
   8. let gridItemName = 'grid' + idx;
   9. // 选中状态下提前调用componentSnapshot中的get接口获取pixmap
   10. this.getUIContext().getComponentSnapshot().get(gridItemName, (error: Error, pixmap: image.PixelMap) => {
   11. this.pixmap = pixmap;
   12. this.previewData[idx] = {
   13. pixelMap: this.pixmap
   14. };
   15. });
   16. } else {
   17. // ...
   18. }
   19. })
   ```

   [GridEts.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/grid/GridEts.ets#L29-L302)
3. 多选显示效果。

   通过[stateStyles](../harmonyos-references/ts-universal-attributes-polymorphic-style.md#statestyles)可以设置选中态和非选中态的显示效果，方便区分。

   ```
   1. @Styles
   2. normalStyles(): void {
   3. .opacity(1.0);
   4. }

   6. @Styles
   7. selectStyles(): void {
   8. .opacity(0.4);
   9. }

   11. // ...
   12. .stateStyles({
   13. normal: this.normalStyles,
   14. selected: this.selectStyles
   15. })
   ```

   [GridEts.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/grid/GridEts.ets#L41-L303)
4. 适配数量角标。

   多选拖拽的数量角标当前需要应用使用dragPreviewOptions中的numberBadge参数设置，开发者需要根据当前选中的节点数量来设置数量角标。

   ```
   1. @State numberBadge: number = 0;
   2. // ...
   3. .onClick(() => {
   4. this.isSelectedGrid[idx] = !this.isSelectedGrid[idx];
   5. if (this.isSelectedGrid[idx]) {
   6. // ...
   7. this.numberBadge++;
   8. // ...
   9. } else {
   10. this.numberBadge--;
   11. // ...
   12. }
   13. })
   14. // 多选场景右上角数量角标需要应用设置numberBadge参数
   15. .dragPreviewOptions({ numberBadge: this.numberBadge })
   ```

   [GridEts.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/grid/GridEts.ets#L33-L304)

**完整示例：**

```
1. import { image } from '@kit.ImageKit';

3. @Entry
4. @Component
5. struct GridEts {
6. @State pixmap: image.PixelMap | undefined = undefined;
7. @State numbers: number[] = [];
8. @State isSelectedGrid: boolean[] = [];
9. @State previewData: DragItemInfo[] = [];
10. @State numberBadge: number = 0;

12. @Styles
13. normalStyles(): void {
14. .opacity(1.0)
15. }

17. @Styles
18. selectStyles(): void {
19. .opacity(0.4)
20. }

22. onPageShow(): void {
23. let i: number = 0;
24. for(i = 0; i < 100; i++) {
25. this.numbers.push(i);
26. this.isSelectedGrid.push(false);
27. this.previewData.push({});
28. }
29. }

31. @Builder
32. RandomBuilder(idx: number) {
33. Column()
34. .backgroundColor(Color.Blue)
35. .width(50)
36. .height(50)
37. .opacity(1.0)
38. }

40. build() {
41. Column({ space: 5 }) {
42. Grid() {
43. ForEach(this.numbers, (idx: number) => {
44. GridItem() {
45. Column()
46. .backgroundColor(Color.Blue)
47. .width(50)
48. .height(50)
49. .opacity(1.0)
50. .id('grid' + idx)
51. }
52. .dragPreview(this.previewData[idx])
53. .selectable(true)
54. .selected(this.isSelectedGrid[idx])
55. // 设置多选显示效果
56. .stateStyles({
57. normal: this.normalStyles,
58. selected: this.selectStyles
59. })
60. .onClick(() => {
61. this.isSelectedGrid[idx] = !this.isSelectedGrid[idx]
62. if (this.isSelectedGrid[idx]) {
63. this.numberBadge++;
64. let gridItemName = 'grid' + idx;
65. // 选中状态下提前调用componentSnapshot中的get接口获取pixmap
66. this.getUIContext().getComponentSnapshot().get(gridItemName, (error: Error, pixmap: image.PixelMap) => {
67. this.pixmap = pixmap;
68. this.previewData[idx] = {
69. pixelMap: this.pixmap
70. }
71. })
72. } else {
73. this.numberBadge--;
74. }
75. })
76. // 使能多选拖拽，右上角数量角标需要应用设置numberBadge参数
77. .dragPreviewOptions({ numberBadge: this.numberBadge },
78. { isMultiSelectionEnabled: true, defaultAnimationBeforeLifting: true })
79. .onDragStart(() => {
80. })
81. }, (idx: string) => idx)
82. }
83. .columnsTemplate('1fr 1fr 1fr 1fr 1fr')
84. .columnsGap(5)
85. .rowsGap(10)
86. .backgroundColor(0xFAEEE0)
87. }.width('100%').margin({ top: 5 })
88. }
89. }
```

[GridExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/grid/GridExample.ets#L15-L106)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/xJ65UXaITReTPYScVbJ8-Q/zh-cn_image_0000002558604800.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052806Z&HW-CC-Expire=86400&HW-CC-Sign=5C408DFFBCD89BCEA3F5ADB0CF7F48CCB1F191A46FCB6EE138445EF306D97E87)

### 适配自定义落位动效

当开发者需要实现自定义落位动效时，可以禁用系统的默认动效。从API version 18开始，ArkUI提供了[executeDropAnimation](../harmonyos-references/ts-universal-events-drag-drop.md#executedropanimation18)接口，用于自定义落位动效。以下以Image组件为例，详细介绍使用[executeDropAnimation](../harmonyos-references/ts-universal-events-drag-drop.md#executedropanimation18)接口的基本步骤，以及开发过程中需要注意的事项。

1. 组件拖拽设置。

   设置draggable为true，并配置onDragStart、onDragEnd等回调函数。

   ```
   1. // 请将$r('app.media.app_icon')替换为实际资源文件
   2. Image($r('app.media.app_icon'))
   3. .width(100)
   4. .height(100)
   5. .draggable(true)
   6. .margin({ left: 15, top: 40 })
   7. .visibility(this.imgState)
   8. .onDragStart((event) => {
   9. })
   10. .onDragEnd((event) => {
   11. // ...
   12. })
   ```

   [DropAnimationExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/drop/DropAnimationExample.ets#L55-L74)
2. 设置自定义动效。

   自定义落位动效通过[animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)接口设置动画相关的参数来实现。例如，可以改变组件的大小。

   ```
   1. customDropAnimation =
   2. () => {
   3. this.getUIContext().animateTo({ duration: 1000, curve: Curve.EaseOut, playMode: PlayMode.Normal }, () => {
   4. this.imageWidth = 200;
   5. this.imageHeight = 200;
   6. this.imgState = Visibility.None;
   7. })
   8. }
   ```

   [DropAnimationExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/drop/DropAnimationExample.ets#L38-L48)
3. 拖拽落位适配动效。

   设置onDrop回调函数，接收拖拽数据。拖拽落位动效通过[executeDropAnimation](../harmonyos-references/ts-universal-events-drag-drop.md#executedropanimation18)函数执行，设置[useCustomDropAnimation](../harmonyos-references/ts-universal-events-drag-drop.md#dragevent7)为true禁用系统默认动效。

   ```
   1. Column() {
   2. Image(this.targetImage)
   3. .width(this.imageWidth)
   4. .height(this.imageHeight)
   5. }
   6. .draggable(true)
   7. .margin({ left: 15 })
   8. .border({ color: Color.Black, width: 1 })
   9. .allowDrop([uniformTypeDescriptor.UniformDataType.IMAGE])
   10. .onDrop((dragEvent: DragEvent) => {
   11. let records: Array<unifiedDataChannel.UnifiedRecord> = dragEvent.getData().getRecords();
   12. let rect: Rectangle = dragEvent.getPreviewRect();
   13. this.imageWidth = Number(rect.width);
   14. this.imageHeight = Number(rect.height);
   15. this.targetImage = (records[0] as unifiedDataChannel.Image).imageUri;
   16. dragEvent.useCustomDropAnimation = true;
   17. dragEvent.executeDropAnimation(this.customDropAnimation)
   18. })
   ```

   [DropAnimationExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/drop/DropAnimationExample.ets#L87-L106)

**完整示例：**

```
1. import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. // ...
5. const DOMAIN = 0x0000;
6. const TAG = 'DropAnimationExampleTag';

8. @Entry
9. @Component
10. export struct DropAnimationExample {
11. // ...
12. @State targetImage: string = '';
13. @State imageWidth: number = 100;
14. @State imageHeight: number = 100;
15. @State imgState: Visibility = Visibility.Visible;
16. customDropAnimation =
17. () => {
18. this.getUIContext().animateTo({ duration: 1000, curve: Curve.EaseOut, playMode: PlayMode.Normal }, () => {
19. this.imageWidth = 200;
20. this.imageHeight = 200;
21. this.imgState = Visibility.None;
22. });
23. };

25. build() {
26. // ...
27. Row() {
28. Column() {
29. // 请将$r('app.media.app_icon')替换为实际资源文件
30. Image($r('app.media.app_icon'))
31. .width(100)
32. .height(100)
33. .draggable(true)
34. .margin({ left: 15, top: 40 })
35. .visibility(this.imgState)
36. .onDragStart((event) => {
37. })
38. .onDragEnd((event) => {
39. if (event.getResult() === DragResult.DRAG_SUCCESSFUL) {
40. hilog.info(DOMAIN, TAG, '%{public}s', 'Drag Success');
41. } else if (event.getResult() === DragResult.DRAG_FAILED) {
42. hilog.info(DOMAIN, TAG, '%{public}s', 'Drag failed');
43. }
44. })

46. }.width('45%')
47. .height('100%')

49. Column() {
50. Text('Drag Target Area')
51. .fontSize(20)
52. .width(180)
53. .height(40)
54. .textAlign(TextAlign.Center)
55. .margin(10)
56. .backgroundColor('rgb(240,250,255)')
57. Column() {
58. Image(this.targetImage)
59. .width(this.imageWidth)
60. .height(this.imageHeight)
61. }
62. .draggable(true)
63. .margin({ left: 15 })
64. .border({ color: Color.Black, width: 1 })
65. .allowDrop([uniformTypeDescriptor.UniformDataType.IMAGE])
66. .onDrop((dragEvent: DragEvent) => {
67. let records: Array<unifiedDataChannel.UnifiedRecord> = dragEvent.getData().getRecords();
68. let rect: Rectangle = dragEvent.getPreviewRect();
69. this.imageWidth = Number(rect.width);
70. this.imageHeight = Number(rect.height);
71. this.targetImage = (records[0] as unifiedDataChannel.Image).imageUri;
72. dragEvent.useCustomDropAnimation = true;
73. dragEvent.executeDropAnimation(this.customDropAnimation);
74. })
75. .width(this.imageWidth)
76. .height(this.imageHeight)
77. }.width('45%')
78. .height('100%')
79. .margin({ left: '5%' })
80. }
81. .height('100%')
82. // ...
83. }
84. }
```

[DropAnimationExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/drop/DropAnimationExample.ets#L16-L129)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/yutmWfPYRPOX7mNkqd1krQ/zh-cn_image_0000002589324325.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052806Z&HW-CC-Expire=86400&HW-CC-Sign=D0E0A99E50304A263B545F3295775F4793B06EDD4691B90C1F45E6553F4CC941)

### 处理大批量数据

当多选拖拽的数量较多或者拖拽数据量较大时，在拖拽过程中统一处理数据可能会影响拖拽功能的体验。以下以Grid组件为例，详细介绍在大批量数据拖拽过程中数据的推荐处理方式，以及在开发中需要注意的事项。本示例中使用的主动阻塞拖拽能力从API version 18开始支持。

1. 组件多选拖拽设置。

   创建GridItem子组件，并设置其状态为可选中。再设置多选拖拽功能isMultiSelectionEnabled为true，最后设置选中状态用作区分是否选中。

   ```
   1. Grid() {
   2. ForEach(this.numbers, (idx: number) => {
   3. GridItem() {
   4. Column()
   5. .backgroundColor(Color.Blue)
   6. .width(50)
   7. .height(50)
   8. .opacity(1.0)
   9. .id('grid' + idx)
   10. }
   11. .dragPreview(this.previewData[idx])
   12. .dragPreviewOptions({ numberBadge: this.numberBadge },
   13. { isMultiSelectionEnabled: true, defaultAnimationBeforeLifting: true })
   14. .selectable(true)
   15. .selected(this.isSelectedGrid[idx])
   16. .stateStyles({
   17. normal: this.normalStyles,
   18. selected: this.selectStyles
   19. })
   20. .onClick(() => {
   21. this.isSelectedGrid[idx] = !this.isSelectedGrid[idx];
   22. })
   23. }, (idx: string) => idx)
   24. }
   ```

   [GridEts.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/grid/GridEts.ets#L255-L285)

   多选拖拽的数据数量过多可能影响拖拽的体验，推荐多选拖拽最大多选数量为500。

   ```
   1. onPageShow(): void {
   2. let i: number = 0;
   3. for (i = 0; i < 500; i++) {
   4. this.numbers.push(i);
   5. this.isSelectedGrid.push(false);
   6. this.previewData.push({});
   7. }
   8. }
   ```

   [GridExamples.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/grid/GridExamples.ets#L43-L53)
2. 多选拖拽选中时添加数据。

   当数据量较大时，建议在选择数据时通过[addRecord](../harmonyos-references/js-apis-data-unifieddatachannel.md#addrecord)添加数据记录，以避免在拖拽过程中集中添加数据而导致显著的性能消耗。

   ```
   1. .onClick(() => {
   2. this.isSelectedGrid[idx] = !this.isSelectedGrid[idx];
   3. if (this.isSelectedGrid[idx]) {
   4. let data: UDC.Image = new UDC.Image();
   5. // '/resource/image.jpeg'需要替换为开发者所需的图像资源文件
   6. data.uri = '/resource/image.jpeg';
   7. if (!this.unifiedData) {
   8. this.unifiedData = new UDC.UnifiedData(data);
   9. }
   10. this.unifiedData.addRecord(data);
   11. this.numberBadge++;
   12. let gridItemName = 'grid' + idx;
   13. // 选中状态下提前调用componentSnapshot中的get接口获取pixmap
   14. this.getUIContext().getComponentSnapshot().get(gridItemName, (error: Error, pixmap: image.PixelMap) => {
   15. this.pixmap = pixmap;
   16. this.previewData[idx] = {
   17. pixelMap: this.pixmap
   18. }
   19. })
   20. } else {
   21. this.numberBadge--;
   22. for (let i = 0; i < this.isSelectedGrid.length; i++) {
   23. if (this.isSelectedGrid[i] === true) {
   24. let data: UDC.Image = new UDC.Image();
   25. // '/resource/image.jpeg'需要替换为开发者所需的图像资源文件
   26. data.uri = '/resource/image.jpeg';
   27. if (!this.unifiedData) {
   28. this.unifiedData = new UDC.UnifiedData(data);
   29. }
   30. this.unifiedData.addRecord(data);
   31. }
   32. }
   33. }
   34. })
   ```

   [GridExamples.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/grid/GridExamples.ets#L121-L156)
3. 拖拽数据提前准备。

   在onPreDrag中可以提前接收到准备发起拖拽的信号。若数据量较大，此时可以事先准备数据。

   ```
   1. .onPreDrag((status: PreDragStatus) => {
   2. if (status == PreDragStatus.PREPARING_FOR_DRAG_DETECTION) {
   3. this.loadData();
   4. }
   5. })
   ```

   [GridExamples.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/grid/GridExamples.ets#L158-L164)
4. 数据准备未完成时设置主动阻塞拖拽。

   在发起拖拽时，应判断数据是否已准备完成。若数据未准备完成，则需向系统发出[WAITING](../harmonyos-references/js-apis-arkui-dragcontroller.md#dragstartrequeststatus18)信号。此时，若手指做出移动手势，背板图将停留在原地，直至应用发出READY信号或超出主动阻塞的最大限制时间（5s）。若数据已准备完成，则可直接将数据设置到[dragEvent](../harmonyos-references/ts-universal-events-drag-drop.md#dragevent7)中。此外，在使用主动阻塞功能时，需保存当前的dragEvent，并在数据准备完成时进行数据设置；在非主动阻塞场景下，不建议保存当前的dragEvent。

   ```
   1. .onDragStart((event: DragEvent) => {
   2. this.dragEvent = event;
   3. if (this.finished == false) {
   4. this.getUIContext()
   5. .getDragController()
   6. .notifyDragStartRequest(dragController.DragStartRequestStatus.WAITING);
   7. } else {
   8. event.setData(this.unifiedData);
   9. }
   10. })
   ```

   [GridExamples.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/grid/GridExamples.ets#L177-L164)

**完整示例：**

```
1. import { image } from '@kit.ImageKit';
2. import { unifiedDataChannel as UDC } from '@kit.ArkData';
3. import { dragController } from '@kit.ArkUI';

5. @Entry
6. @Component
7. struct GridEts {
8. @State pixmap: image.PixelMap | undefined = undefined;
9. @State numbers: number[] = [];
10. @State isSelectedGrid: boolean[] = [];
11. @State previewData: DragItemInfo[] = [];
12. @State numberBadge: number = 0;
13. unifiedData: UnifiedData | undefined = undefined;
14. timeout: number = 1;
15. finished: boolean = false;
16. dragEvent: DragEvent | undefined;

18. @Styles
19. normalStyles(): void{
20. .opacity(1.0);
21. }

23. @Styles
24. selectStyles(): void{
25. .opacity(0.4);
26. }

28. onPageShow(): void {
29. let i: number = 0;
30. for (i = 0; i < 500; i++) {
31. this.numbers.push(i);
32. this.isSelectedGrid.push(false);
33. this.previewData.push({});
34. }
35. }

37. loadData() {
38. this.timeout = setTimeout(() => {
39. // 数据准备完成后的状态
40. if (this.dragEvent) {
41. this.dragEvent.setData(this.unifiedData);
42. }
43. this.getUIContext().getDragController().notifyDragStartRequest(dragController.DragStartRequestStatus.READY);
44. this.finished = true;
45. }, 4000);
46. }

48. @Builder
49. RandomBuilder(idx: number) {
50. Column()
51. .backgroundColor(Color.Blue)
52. .width(50)
53. .height(50)
54. .opacity(1.0)
55. }

57. build() {
58. Column({ space: 5 }) {
59. // 请将$r('app.string.Select_All')替换为实际资源文件，在本示例中该资源文件的value值为"全选"
60. Button($r('app.string.Select_All'))
61. .onClick(() => {
62. for (let i = 0; i < this.isSelectedGrid.length; i++) {
63. if (this.isSelectedGrid[i] === false) {
64. this.numberBadge++;
65. this.isSelectedGrid[i] = true;
66. let data: UDC.Image = new UDC.Image();
67. // '/resource/image.jpeg'需要替换为开发者所需的图像资源文件
68. data.uri = '/resource/image.jpeg';
69. if (!this.unifiedData) {
70. this.unifiedData = new UDC.UnifiedData(data);
71. }
72. this.unifiedData.addRecord(data);
73. let gridItemName = 'grid' + i;
74. // 选中状态下提前调用componentSnapshot中的get接口获取pixmap
75. this.getUIContext().getComponentSnapshot().get(gridItemName, (error: Error, pixmap: image.PixelMap) => {
76. this.pixmap = pixmap;
77. this.previewData[i] = {
78. pixelMap: this.pixmap
79. };
80. });
81. }
82. }
83. })
84. Grid() {
85. ForEach(this.numbers, (idx: number) => {
86. GridItem() {
87. Column()
88. .backgroundColor(Color.Blue)
89. .width(50)
90. .height(50)
91. .opacity(1.0)
92. .id('grid' + idx)
93. }
94. .dragPreview(this.previewData[idx])
95. .dragPreviewOptions({ numberBadge: this.numberBadge },
96. { isMultiSelectionEnabled: true, defaultAnimationBeforeLifting: true })
97. .selectable(true)
98. .selected(this.isSelectedGrid[idx])
99. // 设置多选显示效果
100. .stateStyles({
101. normal: this.normalStyles,
102. selected: this.selectStyles
103. })
104. .onClick(() => {
105. this.isSelectedGrid[idx] = !this.isSelectedGrid[idx];
106. if (this.isSelectedGrid[idx]) {
107. let data: UDC.Image = new UDC.Image();
108. // '/resource/image.jpeg'需要替换为开发者所需的图像资源文件
109. data.uri = '/resource/image.jpeg';
110. if (!this.unifiedData) {
111. this.unifiedData = new UDC.UnifiedData(data);
112. }
113. this.unifiedData.addRecord(data);
114. this.numberBadge++;
115. let gridItemName = 'grid' + idx;
116. // 选中状态下提前调用componentSnapshot中的get接口获取pixmap
117. this.getUIContext().getComponentSnapshot().get(gridItemName, (error: Error, pixmap: image.PixelMap) => {
118. this.pixmap = pixmap;
119. this.previewData[idx] = {
120. pixelMap: this.pixmap
121. };
122. });
123. } else {
124. this.numberBadge--;
125. for (let i = 0; i < this.isSelectedGrid.length; i++) {
126. if (this.isSelectedGrid[i] === true) {
127. let data: UDC.Image = new UDC.Image();
128. // '/resource/image.jpeg'需要替换为开发者所需的图像资源文件
129. data.uri = '/resource/image.jpeg';
130. if (!this.unifiedData) {
131. this.unifiedData = new UDC.UnifiedData(data);
132. }
133. this.unifiedData.addRecord(data);
134. }
135. }
136. }
137. })
138. // ...
139. .onPreDrag((status: PreDragStatus) => {
140. // 1.长按时通知，350ms回调
141. if (status == PreDragStatus.PREPARING_FOR_DRAG_DETECTION) {
142. // 2.用户按住一段时间，还没有松手，有可能会拖拽，此时可准备数据
143. this.loadData();
144. } else if (status == PreDragStatus.ACTION_CANCELED_BEFORE_DRAG) {
145. // 3.用户停止拖拽交互，取消数据准备(模拟方法：定时器取消)
146. clearTimeout(this.timeout);
147. }
148. })
149. // >=500ms,移动超过10vp触发
150. .onDragStart((event: DragEvent) => {
151. this.dragEvent = event;
152. if (this.finished == false) {
153. this.getUIContext()
154. .getDragController()
155. .notifyDragStartRequest(dragController.DragStartRequestStatus.WAITING);
156. } else {
157. event.setData(this.unifiedData);
158. }
159. })
160. .onDragEnd(() => {
161. this.finished = false;
162. })
163. .dragPreviewOptions({ numberBadge: this.numberBadge },
164. { isMultiSelectionEnabled: true, defaultAnimationBeforeLifting: true })
165. }, (idx: string) => idx)
166. }
167. .columnsTemplate('1fr 1fr 1fr 1fr 1fr')
168. .columnsGap(5)
169. .rowsGap(10)
170. .backgroundColor(0xFAEEE0)
171. }.width('100%').margin({ top: 5 })
172. }
173. }
```

[GridExamples.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/grid/GridExamples.ets#L15-L204)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/w6DNWb2yTjOZm1K19GNBqw/zh-cn_image_0000002589244265.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052806Z&HW-CC-Expire=86400&HW-CC-Sign=4D8CB317E68CDDF0DC9D83B1B5739C92B1EC11ACC0734C4E16F940A5D430E39B)

## 支持悬停检测

Spring Loading，即拖拽悬停检测（又叫弹簧加载）是拖拽操作的一项增强功能，允许用户在拖动过程中通过悬停在目标上自动触发视图跳转，提供了使用的便利性。建议在所有支持页面切换的区域均实现该功能。

该能力从API version 20开始支持。

以下为常见的适合支持该功能的场景：

* 在文件管理器中，拖动文件并悬停在文件夹上时，文件夹可以自动打开。
* 在桌面启动器中，拖动文件并悬停在应用程序图标上时，应用程序可以自动打开。

除了实现视图切换跳转功能，该能力也可用于特定视图的激活。例如，在用户将一段文本拖拽至按钮上停留后，可激活一个文本输入框。用户随后可将所拖拽文本移动至该输入框上方释放，触发搜索结果展示，实现单手高效完成整个操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/fBenqTh8RXuJ_o137W9xUg/zh-cn_image_0000002558764458.png?HW-CC-KV=V1&HW-CC-Date=20260429T052806Z&HW-CC-Expire=86400&HW-CC-Sign=5AB87910B2A09ECE3F88071116EDE612BE62C28B073B1722B506AF79306759F9)

### 触发原理

要实现这些能力，需要在组件上注册onDragSpringLoading接口，并传入一个用于处理拖拽悬停触发通知的回调。使用该接口后，该组件将如同注册了onDrop接口的组件一样，成为一个可拖入目标，并且遵循与onDrop相同的命中检测规则，即：在悬停位置下方，仅有一个组件可以接收拖拽事件响应，并且总是首个被检测到的组件。

Spring Loading的整个过程包含三个阶段：悬停检测 -> 回调通知 -> 结束。在结束之前，如果用户重新开始移动，会自动中断Spring Loading，并通知应用取消。如果在悬停检测期间移动，且尚未进入Spring Loading状态，则不会触发取消通知。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/8cgcXXcGSaGOc7OGGiI-1w/zh-cn_image_0000002558604802.png?HW-CC-KV=V1&HW-CC-Date=20260429T052806Z&HW-CC-Expire=86400&HW-CC-Sign=A8CFE3E47BB42789CF27CB77D99F5A9BEB8EB534A872F2E21D799A1D86602ADC)

应用通过回调接收当前的状态，动态改变UI显示，从而达到用户提醒的效果。

| 状态 | 含义 | 建议处理方式 |
| --- | --- | --- |
| BEGIN | 用户已经在本组件上方悬停不动维持了一段时间，开始进入 Spring Loading 状态 | 修改背景色或改变组件尺寸，强化提醒用户继续保持悬停不动。 |
| UPDATE | 用户继续维持不动，系统周期性下发刷新通知，默认3次 | 通过通知中携带的sequence是否为奇偶数，来决定是否重置UI显示，以此达到周期性变化的提醒效果。 |
| END | 用户已保持悬停不动足够多的时间，整个Spring Loading检测与触发完整结束 | 进行页面跳转或视图切换。 |
| CANCEL | 悬停进入BEGIN状态后，用户重新移动或其他情况打断了悬停检测，无法再进行整个Spring Loading状态的触发 | 重置和恢复UI显示，取消视图切换相关的状态和逻辑。 |

说明

1. 在同一个组件内持续保持不动，整个Spring Loading仅会触发一轮，不会重复触发，直到拖离当前组件后再重新进入。
2. 同一个组件上即可以实现Spring Loading，也可以实现onDrop/onDragEnter等拖拽事件。

### 触发自定义

可以自定义修改Spring Loading检测参数，动态决定是否继续触发。

1. 触发参数自定义

[onDragSpringLoading](../harmonyos-references/ts-universal-events-drag-drop.md#ondragspringloading20)接口还提供了一个可选参数configuration供应用自定义静止检测时长以及触发间隔与次数等配置，可以通过此参数来个性化定义Spring Loading触发条件。但绝大数多情况下，不需要进行修改，使用系统默认配置即可。

configuration参数必须在检测开始前准备就绪。系统一旦启动Spring Loading检测过程，将不再从该参数读取配置。然而，可以通过回调中传入的context对象中的updateCon figuration方法动态更新配置。此动态更新仅对当前触发有效，不会影响通过configuration的配置。

推荐使用默认配置，或通过onDragSpringLoading接口的configuration配置固定参数。在绝大多数情况下，无需在Spring Loading过程中动态修改这些检测参数。但若需针对不同的拖拽数据类型提供不同的用户提示效果，则可考虑使用此功能。

说明

不要设置过长的时间间隔和过多的触发次数，这对于用户提醒通常没有意义。

2.动态终止

当系统检测到用户悬停足够时长，回调onDragSpringLoading接口设置到回调函数时，有机会决定即将出现的Spring Loading通知是否继续，这发生在需要观察用户拖拽的数据类型并与自身业务逻辑结合的情况下。

以下是一段伪代码示例：

```
1. .onDragSpringLoading((context: DragSpringLoadingContext)=>{
2. // 检查当前的状态
3. if (context.state == DragSpringLoadingState.BEGIN) {
4. // 检查用户所拖拽的数据类型是否自己能够处理的
5. boolean isICanHandle = false;
6. let dataSummary = context?.dragInfos?.dataSummary;
7. if (dataSummary != undefined) {
8. for (const [type, size] of dataSummary) {
9. if (type === "general.plain-text") { // 只能处理纯文本类型
10. isICanHandle = true;
11. break;
12. }
13. }
14. }
15. // 如果数据无法处理，直接终止Spring Loading
16. if (!isICanHandle) {
17. context.abort();
18. return;
19. }
20. }
21. })
```

3.禁用Spring Loading

如果不再需要该组件上响应任何Spring Loading事件，则可以通过传递null给onDragSpringLoading来明确关闭响应。

```
1. .onDragSpringLoading(null)
```

[SpringLoading.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/springloading/SpringLoading.ets#L190-L192)

### 实现示例

下面通过实现搜索设备的简单示例来展示如何通过onDragSpringLoading实现提醒和视图切换。

1.准备一些组件

为了简化示例，准备一个可拖出文字的组件以供用户拖出待搜索的文字，并添加一个按钮控件，用于响应Spring Loading来进一步激活视图。被激活的视图通过bindSheet实现，内部配置有一个输入框控件用于接收拖拽文本，以及一个文本组件用于展示搜索结果。

```
1. build() {
2. Column() {
3. // ...
4. Column() {
5. // 请将$r('app.string.DoubleClick_Text')替换为实际资源文件，在本示例中该资源文件的value值为"双击文字选择后拖出: \n     DeviceName"
6. Text($r('app.string.DoubleClick_Text'))
7. .fontSize(30)
8. .copyOption(CopyOptions.InApp) // 开启copyOption之后，文本组件即可支持选择内容进行拖拽
9. }.padding({ bottom: 30 })

11. // 请将$r('app.string.Search_Device')替换为实际资源文件，在本示例中该资源文件的value值为"搜索设备"
12. Button($r('app.string.Search_Device'))
13. .width('80%')
14. .height('80vp')
15. .fontSize(30)
16. .bindSheet($$this.isShowSheet, this.SheetBuilder(), {
17. detents: [SheetSize.MEDIUM, SheetSize.LARGE, 600],
18. preferType: SheetType.BOTTOM,
19. // 请将$r('app.string.Search_Device')替换为实际资源文件，在本示例中该资源文件的value值为"搜索设备"
20. title: { title: $r('app.string.Search_Device') },
21. })
22. // ...
23. }.width('100%').height('100%')
24. .justifyContent(FlexAlign.Center)
25. }
```

[SpringLoading.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/springloading/SpringLoading.ets#L151-L212)

2.实现SheetBuilder

实现半模态弹框的UI界面。

```
1. @Builder
2. SheetBuilder() {
3. Column() {
4. // 输入框
5. // 请将$r('app.string.Push_Here')替换为实际资源文件，在本示例中该资源文件的value值为"拖入此处"
6. TextInput({ placeholder: $r('app.string.Push_Here') })
7. .width('80%')
8. .borderWidth(1)
9. .borderColor(Color.Black)
10. // ...
11. .onChange((value: string) => {
12. if (value.length == 0) {
13. this.isSearchDone = false;
14. return;
15. }
16. // 此处简化处理，直接显示固定搜索结果
17. this.isSearchDone = true;
18. })
19. if (this.isSearchDone) {
20. Text(this.searchResult).fontSize(20)
21. // ...
22. }
23. }.width('100%').height('100%')
24. }
```

[SpringLoading.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/springloading/SpringLoading.ets#L37-L68)

3.为Button控件添加进入和离开的响应

为了达到提醒效果，为目标组件也增加onDragEnter和onDragLeave的处理。当用户拖拽文字进入到组件范围时，变化背景色，以提醒用户在此处停留。

```
1. .onDragEnter(() => {
2. // 当用户拖拽进入按钮范围，即提醒用户，此处是可以处理数据的
3. this.buttonBackgroundColor = this.reminderColor
4. })
5. .onDragLeave(() => {
6. // 当用户拖拽离开按钮范围，恢复UI
7. this.buttonBackgroundColor = this.normalColor
8. })
```

[SpringLoading.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/springloading/SpringLoading.ets#L180-L189)

4.实现Spring Loading响应

实现一个Spring Loading的响应函数，处理所有状态，如下：

```
1. handleSpringLoading(context: SpringLoadingContext) {
2. // BEGIN 状态时检查拖拽数据类型
3. if (context.state == dragController.DragSpringLoadingState.BEGIN) {
4. // ···
5. // 进行必要判断，决定是否要终止触发
6. return;
7. }
8. if (context.state == dragController.DragSpringLoadingState.UPDATE) {
9. // ···
10. // 刷新提醒
11. return;
12. }
13. // 处理Spring Loading结束，触发视图切换
14. if (context.state == dragController.DragSpringLoadingState.END) {
15. // ···
16. // 视图激活或跳转
17. return;
18. }
19. // 处理CANCEL状态，复原UI
20. if (context.state == dragController.DragSpringLoadingState.CANCEL) {
21. // ···
22. // 恢复状态与UI
23. return;
24. }
25. }
```

[SpringLoading.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/springloading/SpringLoading.ets#L99-L150)

**完整示例：**

```
1. import { dragController } from '@kit.ArkUI';
2. import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';

4. // ...

6. @Entry
7. @ComponentV2
8. export struct SpringLoadingPage {
9. context1 = this.getUIContext().getHostContext();
10. @Local isShowSheet: boolean = false;
11. // 请将$r('app.string.Select_Result')替换为实际资源文件，在本示例中该资源文件的value值为"搜索结果：\n  设备 1\n  设备 2\n  设备 3\n  ... ..."
12. private searchResult: string = this.context1?.resourceManager.getStringSync($r('app.string.Select_Result').id)!;
13. @Local isSearchDone: boolean = false;
14. private reminderColor: Color = Color.Green;
15. private normalColor: Color = Color.Blue;
16. @Local buttonBackgroundColor: Color = this.normalColor;

18. @Builder
19. SheetBuilder() {
20. Column() {
21. // 输入框
22. // 请将$r('app.string.Push_Here')替换为实际资源文件，在本示例中该资源文件的value值为"拖入此处"
23. TextInput({ placeholder: $r('app.string.Push_Here') })
24. .width('80%')
25. .borderWidth(1)
26. .borderColor(Color.Black)
27. .padding({ bottom: 5 })
28. .onChange((value: string) => {
29. if (value.length == 0) {
30. this.isSearchDone = false;
31. return;
32. }
33. // 此处简化处理，直接显示固定搜索结果
34. this.isSearchDone = true;
35. })
36. if (this.isSearchDone) {
37. Text(this.searchResult).fontSize(20)
38. .textAlign(TextAlign.Start)
39. .width('80%')
40. }
41. }.width('100%').height('100%')
42. }

44. // 检查拖拽数据类型是否包含所希望的plain-text
45. checkDataType(dataSummary: unifiedDataChannel.Summary | undefined): boolean {
46. let summary = dataSummary?.summary;
47. if (summary == undefined) {
48. return false;
49. }

51. let dataSummaryObjStr: string = JSON.stringify(summary);
52. let dataSummaryArray: Array<Array<string>> = JSON.parse(dataSummaryObjStr);
53. let isDataTypeMatched: boolean = false;
54. dataSummaryArray.forEach((record: Array<string>) => {
55. if (record[0] == 'general.plain-text') {
56. isDataTypeMatched = true;
57. }
58. });
59. return isDataTypeMatched;
60. }

62. // 处理BEGIN状态
63. handleBeginState(context: SpringLoadingContext): boolean {
64. // 检查用户所拖拽的数据类型是否自己能够处理的
65. if (this.checkDataType(context?.dragInfos?.dataSummary)) {
66. return true;
67. }
68. // 如果数据无法处理，直接终止Spring Loading
69. context.abort();
70. return false;
71. }

73. // Spring Loading处理入口
74. handleSpringLoading(context: SpringLoadingContext) {
75. // BEGIN 状态时检查拖拽数据类型
76. if (context.state == dragController.DragSpringLoadingState.BEGIN) {
77. if (this.handleBeginState(context)) {
78. // 我们已经在onDragEnter时刷新了提醒色，进入Spring Loading状态时，恢复UI，提醒用户继续保持不动
79. this.buttonBackgroundColor = this.normalColor;
80. }
81. // ...
82. return;
83. }
84. if (context.state == dragController.DragSpringLoadingState.UPDATE) {
85. // 奇数次UPDATE通知刷新提醒UI，偶数次复原UI
86. if (context.currentNotifySequence % 2 != 0) {
87. this.buttonBackgroundColor = this.reminderColor;
88. } else {
89. this.buttonBackgroundColor = this.normalColor;
90. }
91. // ...
92. return;
93. }
94. // 处理Spring Loading结束，触发视图切换
95. if (context.state == dragController.DragSpringLoadingState.END) {
96. this.isShowSheet = true;
97. // ...
98. return;
99. }
100. // 处理CANCEL状态，复原UI
101. if (context.state == dragController.DragSpringLoadingState.CANCEL) {
102. this.buttonBackgroundColor = this.normalColor;
103. // ...
104. return;
105. }
106. }

108. build() {
109. Column() {
110. // ...
111. Column() {
112. // 请将$r('app.string.DoubleClick_Text')替换为实际资源文件，在本示例中该资源文件的value值为"双击文字选择后拖出: \n     DeviceName"
113. Text($r('app.string.DoubleClick_Text'))
114. .fontSize(30)
115. .copyOption(CopyOptions.InApp) // 开启copyOption之后，文本组件即可支持选择内容进行拖拽
116. }.padding({ bottom: 30 })

118. // 请将$r('app.string.Search_Device')替换为实际资源文件，在本示例中该资源文件的value值为"搜索设备"
119. Button($r('app.string.Search_Device'))
120. .width('80%')
121. .height('80vp')
122. .fontSize(30)
123. .bindSheet($$this.isShowSheet, this.SheetBuilder(), {
124. detents: [SheetSize.MEDIUM, SheetSize.LARGE, 600],
125. preferType: SheetType.BOTTOM,
126. // 请将$r('app.string.Search_Device')替换为实际资源文件，在本示例中该资源文件的value值为"搜索设备"
127. title: { title: $r('app.string.Search_Device') },
128. })
129. .allowDrop([uniformTypeDescriptor.UniformDataType.PLAIN_TEXT])
130. .backgroundColor(this.buttonBackgroundColor)
131. .onDragEnter(() => {
132. // 当用户拖拽进入按钮范围，即提醒用户，此处是可以处理数据的
133. this.buttonBackgroundColor = this.reminderColor;
134. })
135. .onDragLeave(() => {
136. // 当用户拖拽离开按钮范围，恢复UI
137. this.buttonBackgroundColor = this.normalColor;
138. })
139. .onDragSpringLoading(null)
140. .onDragSpringLoading((context: SpringLoadingContext) => {
141. this.handleSpringLoading(context);
142. })
143. // ...
144. }.width('100%').height('100%')
145. .justifyContent(FlexAlign.Center)
146. }

148. }
```

[SpringLoading.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/springloading/SpringLoading.ets#L16-L215)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/h6aE8WepS5SgM7fi8-jJiw/zh-cn_image_0000002589324327.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052806Z&HW-CC-Expire=86400&HW-CC-Sign=057A27F06B6B4FD9745A7A824B06FC8058DC8278D199FA0728F59A5B9F152866)

## 示例代码

* [拖拽框架开发实践](https://gitcode.com/HarmonyOS_Samples/DragFramework)
