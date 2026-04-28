---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-rich-text-editor
title: 实现富文本编辑器
breadcrumb: 最佳实践 > 布局与弹窗 > 实现富文本编辑器
category: best-practices
scraped_at: 2026-04-28T08:19:54+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:1c67f8bbc8e9b09317a2cf4e00a5ae277d3abaa5c825b5321970da808845d343
---

## 概述

在移动应用开发中，富文本编辑器是社交、评论、笔记等场景的核心组件。ArkUI提供了[RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)组件，支持图文混排和交互式文本编辑。

本文旨在探讨如何使用[RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)组件，在内容发布场景中实现自定义表情、@好友、添加话题等功能，并提供示例代码详细拆解细节逻辑，如@好友如何被视为一个整体，编辑器中内容如何获取并归一化处理等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/goDXPTOLRAKJfIIjYVrQow/zh-cn_image_0000002428614480.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001949Z&HW-CC-Expire=86400&HW-CC-Sign=D67E846B61A20E15705E495232B46488698EDAE517CDB3C5B3B4DE9F586CF30C "点击放大")

## 实现原理

### RichEditor组件内容管理方式选型

[RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)组件提供两套内容管理接口，方式一使用[RichEditor(options: RichEditorStyledStringOptions)](../harmonyos-references/ts-basic-components-richeditor.md#richeditorstyledstringoptions12)接口创建基于属性字符串（[StyledString/MutableStyledString](../harmonyos-guides/arkts-styled-string.md)）进行内容管理的组件，方式二使用[RichEditor(value: RichEditorOptions)](../harmonyos-references/ts-basic-components-richeditor.md#richeditoroptions)接口创建基于Span进行内容管理的组件。在本文内容发布场景中需要频繁进行输入文字、添加表情、@好友、删除等操作，且无需复杂的样式操作，选择使用方式二基于Span进行内容管理更为合适。

* 方式一：基于属性字符串管理
  + 进行内容样式更新，更加灵活便捷。
  + 序列化困难，需手动提取属性存储，增加持久化逻辑复杂度。
  + 动态内容维护成本高，不适合频繁增删操作。
* 方式二：基于Span管理
  + 使用便捷，通过直接操作独立的Span来动态构建和修改内容。
  + 支持增量式操作，适合需要频繁交互、动态修改（如插入表情、@好友）的场景。

### 添加不同类型内容的方式选型

编辑区域支持输入文字、表情、@好友等内容。

* 使用系统键盘可输入文字，通过[RichEditorController.setTypingStyle()](../harmonyos-references/ts-basic-components-richeditor.md#settypingstyle11)方法可以设置默认的文本样式。
* 添加自定义表情图片可使用[RichEditorController.addImageSpan()](../harmonyos-references/ts-basic-components-richeditor.md#addimagespan)方法实现。
* @好友可使用[RichEditorController.addTextSpan()](../harmonyos-references/ts-basic-components-richeditor.md#addtextspan)和[RichEditorController.addBuilderSpan()](../harmonyos-references/ts-basic-components-richeditor.md#addbuilderspan11)两种方法实现。

  通过如下对比分析可知，使用addBuilderSpan()方法实现更为便捷，但是无法规避折行问题，具体实现可参考[评论回复弹窗](bpta-comment-reply-pop-up-window.md#section1318482323916)。本文使用addTextSpan()方法实现，提供@好友等自定义内容需要折行显示的开发指导。

  |  | 使用addBuilderSpan()方法 | 使用addTextSpan()方法 |
  | --- | --- | --- |
  | 内容长度 | 默认作为一个整体，长度视为一个文字 | 以文本形式添加，长度为文本长度 |
  | 光标与删除逻辑 | 默认作为一个整体，无需额外处理 | 需手动处理光标变化、删除规则 |
  | 折行与显示规则 | 长度超一行：光标高度随builderSpan高度自动调整  长度不超一行：无法折行，触达边界后自动换行 | 与普通文本逻辑一致，支持正常折行显示 |
  | 数据获取与维护 | 无法获取builderSpan中的内容 | 可获取textSpan内容，但额外携带数据需自行维护 |

说明

为了方便表述，对通过addTextSpan()方法和addBuilderSpan()方法添加到编辑区域的内容分别命名为textSpan和builderSpan。

### 维护输入内容

由上述选型可知，使用addTextSpan()方法实现@好友、添加话题等自定义内容时，需手动处理光标变化、删除内容和携带数据的逻辑。

需要定义一个数据结构能将自定义的textSpan维护起来，value用于存储显示的文字内容，spanRange记录内容在编辑区的起始位置和结束位置，以便查找，type用于区分不同类型（例如是@好友还是添加的话题）。data用于携带结构化数据，如好友id、头像等。

```
1. interface TextSpan {
2. value: string;
3. spanRange: [number, number];
4. type: string;
5. data: ESObject;
6. }
```

[EditorView.ets](https://gitcode.com/harmonyos_samples/content-publisher/blob/master/entry/src/main/ets/views/EditorView.ets#L21-L26)

通过维护一个textSpans数组记录所有自定义的textSpan，涉及编辑区域添加或删除内容的操作都需要去更新当前光标后所有textSpan的位置信息（spanRange字段）。

```
1. private textSpans: TextSpan[] = [];
2. // ...
3. // Update the textSpans range that come after the current offset
4. updateTextSpans(insertOffset: number, insertLength: number) {
5. this.textSpans.forEach(textSpan => {
6. if (textSpan.spanRange[0] >= insertOffset) {
7. textSpan.spanRange[0] += insertLength;
8. textSpan.spanRange[1] += insertLength;
9. }
10. })
11. }
```

[EditorView.ets](https://gitcode.com/harmonyos_samples/content-publisher/blob/master/entry/src/main/ets/views/EditorView.ets#L56-L78)

## 添加自定义表情

### 场景描述

点击下方表情按钮，系统键盘切换为表情面板。点击表情图标，会在编辑区域光标后方添加对应的表情内容。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/Ru9eypDITly82dh6RdAFog/zh-cn_image_0000002428774296.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001949Z&HW-CC-Expire=86400&HW-CC-Sign=7E5CAB1973232BF296169F66A072DDA3FAA1577B9BEF473EFF8B787475D79F4C "点击放大")

### 开发步骤

1. 使用[customKeyboard(value: CustomBuilder, options?: KeyboardOptions)](../harmonyos-references/ts-basic-components-richeditor.md#customkeyboard)属性给编辑区域绑定自定义键盘，通过状态变量isEmojiKeyboard控制系统键盘和自定义键盘（表情面板）的切换。并设置[KeyboardOptions](../harmonyos-references/ts-basic-components-richeditor.md#keyboardoptions12)参数中的supportAvoidance属性值为true，使自定义键盘也支持避让功能。

   ```
   1. @Link isEmojiKeyboard: boolean;
   2. // ...
   3. build() {
   4. RichEditor({
   5. controller: this.richEditorController
   6. })
   7. .customKeyboard(this.isEmojiKeyboard ? this.EmojiKeyboard() : undefined, {
   8. supportAvoidance: true
   9. })
   10. // ...
   11. }
   ```

   [EditorView.ets](https://gitcode.com/harmonyos_samples/content-publisher/blob/master/entry/src/main/ets/views/EditorView.ets#L59-L352)
2. 在表情面板中点击表情，可通过[addImageSpan()](../harmonyos-references/ts-basic-components-richeditor.md#addimagespan)方法在编辑区域添加表情图片，默认在内容最后方插入。

   通过设置offset属性为当前光标位置，使表情在正确位置插入。

   当前光标位置可通过[getCaretOffset()](../harmonyos-references/ts-basic-components-richeditor.md#getcaretoffset10)方法获取。后文类似的插入操作都遵循此规则。

   ```
   1. addImageSpan(value: ResourceStr) {
   2. const controller = this.richEditorController;
   3. const curOffset = controller.getCaretOffset();
   4. controller.addImageSpan(value, {
   5. offset: curOffset,
   6. imageStyle: {
   7. size: [16, 16]
   8. }
   9. });
   10. // Update the textSpans spanRange that come after the current offset
   11. this.updateTextSpans(curOffset, 1);
   12. }
   ```

   [EditorView.ets](https://gitcode.com/harmonyos_samples/content-publisher/blob/master/entry/src/main/ets/views/EditorView.ets#L96-L107)

## @好友

### 场景描述

点击下方工具栏@图标或使用系统键盘输入@字符，会跳转到好友列表页面，选择对应好友将自动跳转回编辑页面并在编辑区域添加对应的@好友内容。

添加话题、标题与@好友逻辑一致。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/eon0VozsSI2a5gFDoey7wA/zh-cn_image_0000002462252949.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001949Z&HW-CC-Expire=86400&HW-CC-Sign=B6578FE681AB868C66AB8DA729336F50AD26292F02E8E72C4736DA763D319661 "点击放大")

### 开发步骤

* **点击工具栏@图标跳转好友列表**

1. 点击下方工具栏@图标，跳转到好友列表页面，选择好友后，使用[addTextSpan()](../harmonyos-references/ts-basic-components-richeditor.md#addtextspan)方法将@好友作为文本内容添加到编辑区域。通过offset属性和style属性分别控制插入的位置和样式。可通过添加一个空字符和其他内容做视觉上的分割。

   ```
   1. addTextSpan(value: string, type: string, data: ESObject, style: RichEditorTextStyle) {
   2. // ...
   3. const controller = this.richEditorController;
   4. const curOffset = controller.getCaretOffset();
   5. controller.addTextSpan(value, {
   6. offset: curOffset,
   7. style
   8. });
   9. const splitChar = ' ';
   10. controller.addTextSpan(splitChar, {
   11. offset: controller.getCaretOffset()
   12. });
   13. // ...
   14. }
   ```

   [EditorView.ets](https://gitcode.com/harmonyos_samples/content-publisher/blob/master/entry/src/main/ets/views/EditorView.ets#L112-L143)
2. 维护自定义textSpan数据。更新在当前光标后面所有的自定义textSpan的位置信息，起始位置往后移动的距离为新添加内容的长度，并在textSpans数组中添加该自定义内容textSpan的信息。

   ```
   1. addTextSpan(value: string, type: string, data: ESObject, style: RichEditorTextStyle) {
   2. // ...
   3. this.updateTextSpans(curOffset, value.length + splitChar.length);
   4. this.textSpans.push({
   5. value,
   6. type,
   7. data,
   8. spanRange: [curOffset, curOffset + value.length],
   9. })
   10. }
   ```

   [EditorView.ets](https://gitcode.com/harmonyos_samples/content-publisher/blob/master/entry/src/main/ets/views/EditorView.ets#L113-L144)
3. 在编辑区域添加了@好友内容后，在其前后输入的文字会拥有@好友内容的样式，并与其合并成一个textSpan。

   在RichEditor组件[onReady()](../harmonyos-references/ts-basic-components-richeditor.md#onready)事件回调函数中，为键盘输入内容设置默认样式，这样就能与@好友等自定义textSpan内容隔离开。

   ```
   1. RichEditor({
   2. controller: this.richEditorController
   3. })
   4. // ...
   5. .onReady(() => {
   6. this.richEditorController.setTypingStyle({
   7. fontColor: Color.Black,
   8. })
   9. })
   ```

   [EditorView.ets](https://gitcode.com/harmonyos_samples/content-publisher/blob/master/entry/src/main/ets/views/EditorView.ets#L319-L341)

* **键盘输入@符号跳转好友列表**

1. 通过键盘输入@符号的方式跳转好友列表，键盘默认行为会先在编辑区添加@符号，在选择好友后需要先删除默认行为添加@符号，再将@好友作为整体通过addTextSpan()方法添加。

   通过状态变量isKeyboardTriggered标志是否为键盘输入触发。在[aboutToIMEInput()](../harmonyos-references/ts-basic-components-richeditor.md#abouttoimeinput)键盘输入事件的回调函数中，判断插入字符是@，则更新标志位为true，并跳转联系人页面。在添加@好友内容时如果是键盘输入触发，则删除光标前一个字符，并将标志位重置为false。

   ```
   1. @State isKeyboardTriggered: boolean = false;
   2. // ...
   3. deletePrevChar() {
   4. const controller = this.richEditorController;
   5. const offset = controller.getCaretOffset();
   6. const range: RichEditorRange = { start: offset - 1, end: offset };
   7. controller.deleteSpans(range);
   8. }
   9. // ...
   10. addTextSpan(value: string, type: string, data: ESObject, style: RichEditorTextStyle) {
   11. if (this.isKeyboardTriggered) {
   12. this.deletePrevChar()
   13. this.isKeyboardTriggered = false;
   14. }
   15. // ...
   16. }
   17. // ...
   18. aboutToIMEInput: (value: RichEditorInsertValue) => boolean = value => {
   19. if (value.insertValue === '@') {
   20. this.isKeyboardTriggered = true;
   21. this.getUIContext().getRouter().pushUrl({ url: 'pages/ContactListPage' });
   22. // ...
   23. }
   24. return true;
   25. }
   ```

   [EditorView.ets](https://gitcode.com/HarmonyOS_Samples/content-publisher/blob/master/entry/src/main/ets/views/EditorView.ets#L52-L181)
2. 后续步骤与[点击工具栏@图标跳转好友列表](bpta-rich-text-editor.md#li4151245711)方式的开发步骤中的1、2、3步一致。

## 处理光标位置

### 场景描述

光标不可落入@好友文本的内部。当用户点击或选中@好友这种自定义内容时，光标应自动跳转到内容的开始或结束位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/cFHtPrt2TTOFREBRV1Zfhw/zh-cn_image_0000002462133105.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001949Z&HW-CC-Expire=86400&HW-CC-Sign=C5B81032884A81ED44BAEBBAF8BF3512DAD6136C96F0526235939142DB6C7BF9 "点击放大")

### 开发步骤

1. 判断当前光标位置是否在自定义内容的textSpan中间，是则根据就近原则返回textSpan的起始位置或结束位置，否则返回当前光标位置。

   ```
   1. snapCaretToTextSpanBoundary(caretOffset: number, type?: 'start' | 'end') {
   2. const textSpan = this.textSpans.find(textSpan => {
   3. return caretOffset > textSpan.spanRange[0] && caretOffset < textSpan.spanRange[1];
   4. });
   5. if (!textSpan) return caretOffset;
   6. if (type === 'start') return textSpan.spanRange[0];
   7. if (type === 'end') return textSpan.spanRange[1];
   8. const disToStart = caretOffset - textSpan.spanRange[0];
   9. const disToEnd = textSpan.spanRange[1] - caretOffset;
   10. if (disToStart <= disToEnd) return textSpan.spanRange[0];
   11. return textSpan.spanRange[1];
   12. }
   ```

   [EditorView.ets](https://gitcode.com/harmonyos_samples/content-publisher/blob/master/entry/src/main/ets/views/EditorView.ets#L251-L262)
2. 当用户点击@好友内容时，在[onSelectionChange()](../harmonyos-references/ts-basic-components-richeditor.md#onselectionchange12)事件的回调函数中重新计算并使用[setCaretOffset()](../harmonyos-references/ts-basic-components-richeditor.md#setcaretoffset10)设置光标位置。

   ```
   1. onSelectionChange: (range: RichEditorRange) => void = range => {
   2. // When start and end values are the same, it indicates a cursor position change triggered by a click, with no selected area.
   3. if (range.start === range.end) {
   4. const targetCaretOffset = this.snapCaretToTextSpanBoundary(range.start!);
   5. this.richEditorController.setCaretOffset(targetCaretOffset);
   6. }
   7. }
   ```

   [EditorView.ets](https://gitcode.com/harmonyos_samples/content-publisher/blob/master/entry/src/main/ets/views/EditorView.ets#L232-L238)
3. 当选中内容发生变化时，在[onSelect()](../harmonyos-references/ts-basic-components-richeditor.md#onselect)事件的回调函数中获取选中内容的起始位置和结束位置。
   * 当它们处于同一个自定义内容的textSpan中间时，更新两个光标的位置到该textSpan的起始位置和结束为止。
   * 否则，更新两个光标的位置到各自就近的textSpan边缘。

   最后通过setSelection()方法设置计算后的选中区域。

   ```
   1. onSelect: (selection: RichEditorSelection) => void = richEditorSelection => {
   2. const caretStart = richEditorSelection.selection[0];
   3. const caretEnd = richEditorSelection.selection[1];
   4. // Determine if the selected content lies within a single textSpan.
   5. // If it does, adjust the selection range to the start and end of that textSpan.
   6. const textSpan = this.textSpans.find(textSpan => {
   7. return caretStart >= textSpan.spanRange[0] && caretEnd <= textSpan.spanRange[1];
   8. });
   9. if (textSpan) {
   10. this.richEditorController.setSelection(textSpan.spanRange[0], textSpan.spanRange[1]);
   11. return;
   12. }
   13. // Both values being -1 indicates clear selection operation.
   14. if (caretStart === -1 && caretEnd ===  -1) {
   15. return
   16. }
   17. const selectionStart = this.snapCaretToTextSpanBoundary(caretStart);
   18. const selectionEnd = this.snapCaretToTextSpanBoundary(caretEnd);
   19. this.richEditorController.setSelection(selectionStart, selectionEnd);
   20. }
   ```

   [EditorView.ets](https://gitcode.com/harmonyos_samples/content-publisher/blob/master/entry/src/main/ets/views/EditorView.ets#L209-L228)

## 删除内容

### 场景描述

点击软键盘删除按钮，光标前待删除的是@好友等自定义内容时，则作为整体删除。其余内容删除时无需额外处理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/kbpfCG_mQfubXybOZO5ymg/zh-cn_image_0000002428614484.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001949Z&HW-CC-Expire=86400&HW-CC-Sign=5DEFF299DD5725DD11B8F1FC77DDC4CD4D0D639F5780F177187841ADEAE14124 "点击放大")

### 开发步骤

1. 在[aboutToDelete()](../harmonyos-references/ts-basic-components-richeditor.md#abouttodelete)事件的回调函数中，获取将要删除内容的起始位置和结束位置。
2. 若起始位置在自定义的textSpan中间，则更新起始位置为该textSpan的起始位置。若结束位置在自定义的textSpan中间，则更新结束位置为该textSpan的结束位置。
3. 使用[deleteSpans()](../harmonyos-references/ts-basic-components-richeditor.md#deletespans)方法删除编辑区域中的内容。
4. 更新自行维护的textSpans数据，删除起始位置和结束位置中间所有的textSpan数据，并更新在删除内容后所有的自定义textSpan的位置信息。

```
1. aboutToDelete: (value: RichEditorDeleteValue) => boolean = deleteValue => {
2. // when enables pinyin preview on the screen,each input triggers the aboutToDelete Event.
3. // in this case,the default deletion logic is directly applied.
4. const previewText = this.richEditorController.getPreviewText().value;
5. if (previewText.length !== 0) {
6. return true;
7. }

9. const start = deleteValue.offset;
10. const end = start + deleteValue.length;
11. const snapStart = this.snapCaretToTextSpanBoundary(start, 'start');
12. const snapEnd = this.snapCaretToTextSpanBoundary(end, 'end');
13. this.richEditorController.deleteSpans({
14. start: snapStart,
15. end: snapEnd
16. });
17. // delete all textSpans in selection
18. this.textSpans = this.textSpans.filter(ts => {
19. const isInRange = ts.spanRange[0] >= snapStart && ts.spanRange[1] <= snapEnd
20. return !isInRange;
21. });
22. this.updateTextSpans(snapStart, snapStart - snapEnd);
23. return false;
24. }
```

[EditorView.ets](https://gitcode.com/harmonyos_samples/content-publisher/blob/master/entry/src/main/ets/views/EditorView.ets#L189-L212)

## 获取内容

### 场景描述

发布内容时，需要获取编辑区域的文本内容，同时还需要获取带有结构化信息（如好友的id）的数据，用于提交到服务器或持久化存储。

### 开发步骤

1. 实际开发中编辑区域不同类型的内容往往需要一种统一的数据结构来表达，方便传输和存储。这里定义为CustomSpan，其中value表示文本内容，resourceValue表示表情图片资源，type用于区分不同类型的textSpan，例如是@好友还是添加的话题，data用于存储携带的信息，例如好友id等。

   ```
   1. export interface CustomSpan {
   2. value?: string;
   3. resourceValue?: ResourceStr;
   4. type?: string;
   5. data?: ESObject;
   6. }
   ```

   [EditorView.ets](https://gitcode.com/harmonyos_samples/content-publisher/blob/master/entry/src/main/ets/views/EditorView.ets#L30-L35)
2. RichEditor组件提供[getSpans()](../harmonyos-references/ts-basic-components-richeditor.md#getspans)方法来获取内容，但是例如@好友中一些结构化信息仍需要根据位置信息去手动维护的[textSpans](bpta-rich-text-editor.md#section153701489425)数组中去查找。最后将[getSpans()](../harmonyos-references/ts-basic-components-richeditor.md#getspans)方法获取的[RichEditorTextSpanResult](../harmonyos-references/ts-basic-components-richeditor.md#richeditortextspanresult)和[RichEditorImageSpanResult](../harmonyos-references/ts-basic-components-richeditor.md#richeditorimagespanresult)转换成CustomSpan。

   ```
   1. getData(): CustomSpan[] {
   2. const customSpans = this.richEditorController.getSpans().map(span => {
   3. const textSpan = span as RichEditorTextSpanResult;
   4. const imageSpan = span as RichEditorImageSpanResult;
   5. // is imageSpan
   6. if (!textSpan.value) {
   7. return { resourceValue: imageSpan.valueResourceStr } as CustomSpan;
   8. }
   9. // is textSpan
   10. const customTextSpan = this.textSpans.find(customTextSpan => {
   11. return this.isTheSameRange(customTextSpan.spanRange, textSpan.spanPosition.spanRange);
   12. })
   13. if (!customTextSpan) {
   14. return { value: textSpan.value } as CustomSpan;
   15. }
   16. return {
   17. value: customTextSpan.value,
   18. type: customTextSpan.type,
   19. data: customTextSpan.data
   20. } as CustomSpan;
   21. });
   22. return customSpans;
   23. }
   ```

   [EditorView.ets](https://gitcode.com/harmonyos_samples/content-publisher/blob/master/entry/src/main/ets/views/EditorView.ets#L270-L292)
3. 图中内容通过getData()方法生成的数据序列化后的数据如下，如何与服务端交互或使用这些数据，根据业务需求调整即可。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/r_NR1F4QQMGPnsSUZXivdw/zh-cn_image_0000002428774300.png?HW-CC-KV=V1&HW-CC-Date=20260428T001949Z&HW-CC-Expire=86400&HW-CC-Sign=C8AB7F7DE58C81F2B12CFB4DE3F729F24F69ABB0BA3E3046B078FF77B705213C "点击放大")

   ```
   1. [{
   2. "value": "Hello"
   3. }, {
   4. "resourceValue": "resource:///emoji_3.png"
   5. }, {
   6. "value": "@阿飞",
   7. "type": "contact",
   8. "data": {
   9. "imgName": "app.media.ic_comm_pic1",
   10. "name": "阿飞"
   11. }
   12. }, {
   13. "value": " "
   14. }, {
   15. "value": "#众测主题赛#",
   16. "type": "topic",
   17. "data": {
   18. "topicId": "1",
   19. "title": "众测主题赛"
   20. }, {
   21. "value": " "
   22. }]
   ```

## 常见问题

### 使用addBuilderSpan自定义内容时，折行显示与光标异常

对折行显示有硬性需求可使用addTextSpan方式实现。参考[添加不同类型内容的方式选型](bpta-rich-text-editor.md#section0845456185414)。

### 发布内容时如何处理富文本数据

通过维护自定义textSpan数据的方式实现。参考[获取内容](bpta-rich-text-editor.md#section13583102185219)。

### 如何自定义选择菜单

通过[bindSelectionMenu](../harmonyos-references/ts-basic-components-richeditor.md#bindselectionmenu)属性对不同类型的Span绑定不同的菜单。参考[自定义选择菜单](../harmonyos-guides/arkts-common-components-richeditor.md#设置自定义选择菜单)。

## 示例代码

* [基于ArkUI实现内容发布器功能](https://gitcode.com/harmonyos_samples/content-publisher)
