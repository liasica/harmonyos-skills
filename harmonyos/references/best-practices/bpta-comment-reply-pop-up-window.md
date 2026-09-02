---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-comment-reply-pop-up-window
title: 评论回复弹窗
breadcrumb: 最佳实践 > 布局与弹窗 > 评论回复弹窗
category: best-practices
scraped_at: 2026-09-02T15:03:16+08:00
doc_updated_at: 2026-07-22
content_hash: sha256:952f6043c44e32e2e48f261ae679155da0e58b2827d86c3fffa0af91ebb19837
---

## 概述

评论回复模块在图文和视频应用中被广泛使用，包含编辑区域、好友列表、常用表情列表和表情面板（见下图），它允许用户进行输入文字、表情、@好友、选择图片等操作。该模块一般以弹窗的形式展现给用户，通常在图文、视频界面中直接弹出，或者在评论列表上层弹出，本文将从评论列表上层弹出这种相对复杂的场景出发，重点对以下几个方面进行介绍，为开发者提供评论回复弹窗模块开发的最佳实践。

* 弹窗组件的选型以及最终方案的实现
* 软键盘和表情面板切换的适配
* 编辑区域主要细节功能的实现

**图1** 效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/iXaHck9QTSe9x717Yjlhbw/zh-cn_image_0000002229337549.png "点击放大")

为方便阅读，下面表格对本文常出现的模块名称进行说明：

| 模块名称 | 对应图1中序号 |
| --- | --- |
| 评论列表 | 1 |
| 好友列表 | 2 |
| 编辑区域 | 3 |
| 常用表情列表 | 4 |
| 软键盘 | 5 |
| 表情面板 | 6 |

参考资料

* [组件导航（Navigation）](../harmonyos-guides/arkts-navigation-navigation.md)
* [支持图文混排和文本交互式编辑的组件（RichEditor）](../harmonyos-references/ts-basic-components-richeditor.md)
* [自定义弹窗（CustomDialog）](../harmonyos-references/ts-methods-custom-dialog-box.md)
* [半模态转场（.bindSheet）](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)

## 实现原理

### 弹窗组件选型

通过对[CustomDialog自定义弹窗](../harmonyos-references/ts-methods-custom-dialog-box.md)、[bindSheet半模态弹窗](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)、Navigation Dialog（即[页面显示类型](../harmonyos-guides/arkts-navigation-navdestination.md#页面显示类型)中的弹窗类型）三种弹窗方案进行尝试，发现自定义弹窗和半模态弹窗有一定规格限制，会产生一些无法避免的问题，最终选用Navigation Dialog（即[页面显示类型](../harmonyos-guides/arkts-navigation-navdestination.md#页面显示类型)中的弹窗类型）方案实现评论模块弹窗。以下对三种方案优劣势进行一个详细的说明。

* [CustomDialog自定义弹窗](../harmonyos-references/ts-methods-custom-dialog-box.md)

  方案优势：

  1. 现成封装好的组件，无需开发者实现弹窗相关的交互逻辑。
  2. 自定义弹窗默认避让软键盘，评论模块无需计算高度，调用时直接被软键盘抬起即可。

  方案劣势：

  1. 由于自定义弹窗完全避让软键盘，且该行为无法配置。在点击表情按钮时，展示表情面板，此过程评论模块高度发生变化，到软键盘完全收起的过程中，表情面板仍然处于软键盘上方，评论模块会被短暂顶起。
  2. 软键盘动画不能自定义配置或获取，无法配合动画能力抵消顶起操作。

  [PromptAction.openCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialog12)与自定义弹窗呈现效果相同，不再赘述。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/9ZVhWiBqTlyf92g-Q57p0g/zh-cn_image_0000002193852164.gif "点击放大")
* [bindSheet半模态弹窗](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)

  方案优势：

  1. 现成封装好的组件，无需开发者实现弹窗相关的交互逻辑。
  2. 可解决CustomDialog中评论模块被顶起的问题。

  方案劣势：

  1. 设置高度自适应后，bindSheet内部的Scroll依然生效，在bindSheet内部可滚动。
  2. 设置dragBar为false时，bindSheet依然可以上下拖动，松手后回到原位，但此过程会暴露软键盘下方的表情面板区域。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/Xi8-wM5XRzSg0z61eWz5vA/zh-cn_image_0000002194011744.gif "点击放大")
* Navigation Dialog

  方案优势：

  1. 可解决上述两种方案中存在的问题。
  2. 基于Navigation路由形式，以进出路由栈的方式打开或关闭弹窗，可以实现弹窗与UI界面解耦。

  方案劣势：

  1. 弹窗遮罩层以及点击遮罩关闭弹窗的逻辑需要手动实现。

**注意** 

Navigation Dialog（即[页面显示类型](../harmonyos-guides/arkts-navigation-navdestination.md#页面显示类型)中的弹窗类型）在z轴的层级较低，评论模块如果基于该方案实现，那么在其他使用了CustomDialog、bindSheet的弹窗模块（例如评论列表）中调用评论模块，评论模块会在其他弹窗模块下层，所以其他弹窗模块也需要一同改为Navigation Dialog（即[页面显示类型](../harmonyos-guides/arkts-navigation-navdestination.md#页面显示类型)中的弹窗类型）实现，通过路由栈进行弹窗层级的控制。

### 编辑区域组件及方法选型

编辑区域支持输入文字、表情、@好友等内容。目前支持图文混排和文本交互式编辑的组件，[RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)是不二的选择。针对添加表情，可使用[RichEditorController.addImageSpan](../harmonyos-references/ts-basic-components-richeditor.md#addimagespan)方法实现。@好友可使用[RichEditorController.addTextSpan](../harmonyos-references/ts-basic-components-richeditor.md#addtextspan)和[RichEditorController.addBuilderSpan](../harmonyos-references/ts-basic-components-richeditor.md#addbuilderspan11)两种方法实现，通过以下对两种方法的分析对比，最终选择addBuilderSpan实现@好友功能。

**说明** 

为了方便表述，下文对通过addTextSpan、addImageSpan、addBuilderSpan方法添加到编辑区域的内容分别命名为textSpan、imageSpan、builderSpan。

* 使用addTextSpan实现@好友
  1. 在textSpan前后通过软键盘输入的文字会自动与之合并成一个textSpan，而@好友具有特殊样式和逻辑，需要对前后文字进行分割，这些细节需要手动处理。
  2. @好友作为一个整体，光标不能在中间点击，删除需要整体删除，使用textSpan需要手动处理这些细节。
  3. 获取编辑区域内容时，可以获取到textSpan中的文字（好友昵称），但是如果想获取到该好友的其他信息，仅用好友昵称去关联显然不是一种可靠的方案。
* 使用addBuilderSpan实现@好友
  1. builderSpan不会和前后文字合并。
  2. builderSpan默认作为一个整体，对光标点击以及删除逻辑不需要另外处理。
  3. 获取编辑区域内容时，无法获取到builderSpan中的内容，需要手动对添加或删除的builderSpan信息进行维护，自己维护的同时自然也能与好友的其他信息进行关联。

## 关键场景实现

### 弹窗显示

在视频页面点击消息按钮，弹出评论列表页面弹窗。在评论列表页点击写评论按钮，弹出评论模块弹窗。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/ialRzNAfTga8tVEvJxDVcA/zh-cn_image_0000002229337541.gif "点击放大")

基于Navigation的弹窗方案，Navigation的mode属性需要设置为NavigationMode.Stack。弹窗需要全屏显示，Navigation则需要添加在最外层组件上。

```typescript
// features/home/src/main/ets/view/Home.ets
build() {
  Navigation(this.navDialogPageInfos) {
    // ...
  }
  .hideTitleBar(true)
  .mode(NavigationMode.Stack)
  .navDestination(this.NavDialogPageMap)
}
```

弹窗模块需要用NavDestination包裹，设置NavDestination的mode属性为NavDestinationMode.DIALOG弹窗类型，设置[expandSafeArea](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#expandsafearea)属性为[SafeAreaType.KEYBOARD]扩展安全区域，不避让软键盘，以解决[CustomDialog自定义弹窗](../harmonyos-references/ts-methods-custom-dialog-box.md)的问题。并在弹窗内容下层通过Stack添加遮罩，点击可关闭弹窗，考虑到多个弹窗模块要进行相同的处理，将弹窗模块封装为组件，评论列表和评论模块调用该组件则无需关注弹窗相关的交互，只需关注弹窗中需要展示的内容即可。

```typescript
// features/home/src/main/ets/view/NavigationDialog.ets
@Component
export struct NavigationDialog {
  @Consume navDialogPageInfos: NavPathStack;
  @Prop alignContent: Alignment = Alignment.Bottom;
  @Prop maskBackgroundColor: ResourceColor

  @Builder
  DefaultContentBuilder() {}

  @BuilderParam
  contentBuilderParam: () => void = this.DefaultContentBuilder

  onClose = () => {
    this.navDialogPageInfos.pop();
  }

  build() {
    NavDestination() {
      Stack() {
        Column()
          .height('100%')
          .width('100%')
          .backgroundColor(this.maskBackgroundColor)
          .onClick(this.onClose)
        this.contentBuilderParam()
      }
      .height('100%')
      .alignContent(this.alignContent)
    }
    .mode(NavDestinationMode.DIALOG)
    .hideTitleBar(true)
    .expandSafeArea([SafeAreaType.KEYBOARD])
  }
}
```

各个弹窗模块的弹出和关闭通过路由的进栈出栈控制，弹窗的层级关系通过路由进栈的顺序来控制。

### 软键盘和表情面板切换适配

点击编辑区域表情按钮，软键盘切换为表情面板，表情按钮图标变成键盘图标。再次点击，表情面板切换回软键盘，按钮图标由键盘变回表情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/bzFBe31tTS2xvUTymq1AAw/zh-cn_image_0000002193852160.gif "点击放大")

本文选择自定义键盘来控制软键盘和表情面板的切换。通过设置[RichEditor.customKeyboard](../harmonyos-references/ts-basic-components-richeditor.md#customkeyboard)为表情面板组件的构建函数EmojiKeyboard，来展示表情面板，设置该属性为undefined，则展示默认软键盘。通过这种方式在软键盘与表情面板切换时也无需手动进行richEditor焦点的处理。

```typescript
// features/home/src/main/ets/view/CommentKeyboard.ets
RichEditor({ controller: this.richEditorController })
  .customKeyboard(this.isEmojiKeyboardVisible ? this.EmojiKeyboard() : undefined)
  // ...
```

为保证切换软键盘和表情面板时，评论模块整体高度不发生改变，则需要获取软键盘高度对表情面板高度进行计算和手动设置。有可能软键盘高度被手动更改，所以需要通过[keyboardHeightChange](../harmonyos-references/arkts-apis-window-window.md#onkeyboardheightchange7)事件对软键盘高度进行监听，当高度大于0时，更新记录软键盘高度的状态变量。注意在组件销毁前取消对应的监听事件。

```typescript
aboutToAppear(): void {
  window.getLastWindow(this.getUIContext().getHostContext()).then(win => {
    this.addKeyboardHeightListener(win);
  }).catch((err: BusinessError) => {
    Logger.error(TAG,
      `getLastWindow Failed. Code:${err.code}, message:${err.message}`);
  });
}

aboutToDisappear(): void {
  window.getLastWindow(this.getUIContext().getHostContext()).then(win => {
    this.removeKeyboardHeightListener(win);
  }).catch((err: BusinessError) => {
    Logger.error(TAG,
      `getLastWindow Failed. Code:${err.code}, message:${err.message}`);
  });
}

getResourceString(resource: Resource): string {
  try {
    return this.getUIContext().getHostContext()!.resourceManager.getStringSync(resource.id);
  } catch (exception) {
    Logger.error(TAG,
      `getLastWindow Failed. Code:${exception.code}, message:${exception.message}`);
    return '';
  }
}

addKeyboardHeightListener(win: window.Window) {
  win.on('keyboardHeightChange', height => {
    Logger.info(TAG, 'keyboard height has changed', this.getUIContext().px2vp(height));
    if (height !== 0) {
      this.keyboardHeight = this.getUIContext().px2vp(height);
      return;
    }
    // ...
  });
}

removeKeyboardHeightListener(win: window.Window) {
  win.off('keyboardHeightChange');
}
```

如图1效果图所示，对比软键盘显示界面和表情面板显示界面可知，表情面板的高度 = 常用表情列表的高度 + 软键盘的高度。由于弹窗不避让软键盘和自定义键盘，在切换到软键盘时，需要一个占位元素来将软键盘上方区域顶起，且高度为软键盘的高度。同理，切换到表情面板时，需要将占位元素的高度设置为表情面板的高度（即常用表情列表的高度 + 软键盘的高度）。

评论弹窗模块高度适配代码：

```typescript
// features/home/src/main/ets/view/CommentKeyboard.ets
build() {
  NavigationDialog({ maskBackgroundColor: 'rgba(0, 0, 0, 0.1)' }) {
    Column() {
      this.AtFriendList()
      this.ToolBar()
      Divider()
      if (!this.isEmojiKeyboardVisible) {
        this.FrequentEmojiList()
      }
      Column()
        .height(
          this.isEmojiKeyboardVisible ?
            this.keyboardHeight + this.frequentEmojiListHeight :
            this.keyboardHeight
        )
    }
    .backgroundColor(Color.White)
  }
}
```

表情面板高度适配代码：

```typescript
// features/home/src/main/ets/view/CommentKeyboard.ets
@Builder
EmojiKeyboard() {
  Grid() {
    ForEach(this.getEmojiIcons(), (icon: Resource) => {
      GridItem() {
        Image(icon)
          .width(45)
          .onClick(() => {
            this.onEmojiClick(icon)
          })
      }
    })
  }
  .width('100%')
  .height(this.keyboardHeight + this.frequentEmojiListHeight)
  // ...
}
```

### 编辑区功能

编辑区通常包括输入文字、表情、@好友、选择图片功能，本节通过效果图展示结合代码讲解的方式对上述功能开发做相应介绍。

* 添加表情

  在软键盘上方常用表情列表点击表情图片，或者切换到表情面板点击表情图片，会在编辑区域光标后方添加对应的表情内容。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/I_dzSaTMTwOxBaaRNqDixg/zh-cn_image_0000002194011748.gif "点击放大")

  在表情面板或常用表情列表中点击表情时可通过[RichEditorController.addImageSpan](../harmonyos-references/ts-basic-components-richeditor.md#addimagespan)在编辑区域进行添加图片表情，注意需要设置offset属性为当前光标位置，当前光标的位置可通过[RichEditorController.getCaretOffset](../harmonyos-references/ts-basic-components-richeditor.md#getcaretoffset10)获取。这样使得表情在当前光标后添加，否则默认在内容的最后方添加，后文类似的添加操作都遵循此规则。

  ```typescript
  // features/home/src/main/ets/view/CommentKeyboard.ets
  onEmojiClick: (icon: Resource) => void = icon => {
    this.richEditorController.addImageSpan(icon, {
      offset: this.richEditorController.getCaretOffset(),
      imageStyle: { size: [20, 20] }
    });
    // ...
  }
  ```

* @好友

  点击编辑区域@按钮，或在软键盘输入@符号，会展示好友列表。点击好友列表中好友头像，会在编辑区域添加@好友内容。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/GXNh8bmYQ7C9hfe830tgGA/zh-cn_image_0000002229452041.gif "点击放大")

  点击@按钮时，通过[RichEditorController.addTextSpan](../harmonyos-references/ts-basic-components-richeditor.md#addtextspan)添加@符号，并显示好友列表。同时需要监听[RichEditor.aboutToIMEInput](../harmonyos-references/ts-basic-components-richeditor.md#abouttoimeinput)事件 ，该事件在输入内容前触发回调，在回调中获取要输入的内容，如果输入的内容为@，则相当于点击了@按钮的效果，这样统一了点击@按钮和键盘输入@的逻辑，方便后续一些细节的处理。

  ```typescript
  // features/home/src/main/ets/view/CommentKeyboard.ets
  onAtButtonClick: (event?: ClickEvent) => void = event => {
    const controller = this.richEditorController;
    this.isAtFriendListVisible = true;
    controller.addTextSpan('@', { offset: controller.getCaretOffset() });
  }
  ```

  在好友列表中点击好友头像时，通过[RichEditorController.getSpans](../harmonyos-references/ts-basic-components-richeditor.md#getspans)可以获取光标前一个span的内容，若光标前一个span是内容为@的textSpan，则先删除，然后通过[RichEditorController.addBuilderSpan](../harmonyos-references/ts-basic-components-richeditor.md#addbuilderspan11)将“@[好友昵称]”以指定的样式作为一个整体添加到编辑区域中。

  ```typescript
  // features/home/src/main/ets/view/CommentKeyboard.ets
  onAtFriendClick: (friend: User) => void = friend => {
    const controller = this.richEditorController;
    const offset = controller.getCaretOffset();
    const range: RichEditorRange = { start: offset - 1, end: offset };
    const span = controller.getSpans(range);
    if (offset !== 0 && (span[0] as RichEditorTextSpanResult).value === '@') {
      controller.deleteSpans(range);
    }
    controller.addBuilderSpan(() => this.AtSpan(friend.nickname), {
      offset: controller.getCaretOffset()
    });
    this.setBuilderSpans(controller, friend);
  }

  @Builder
  AtSpan(nickname: string) {
    Text(`@${nickname}`)
      .fontColor(0xFF133667)
      .maxLines(1)
      .textOverflow({ overflow: TextOverflow.Ellipsis })
  }
  ```

* 删除内容

  点击软键盘删除按钮，如果要编辑区域光标前删除的内容是builderSpan（@好友）且没有被选中，则进行选中，否则直接删除光标前的内容。选中内容会作为整体删除。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/xf4UPEYMS96YAIHMxP5p1w/zh-cn_image_0000002229452037.gif "点击放大")

  监听[RichEditor.aboutToDelete](../harmonyos-references/ts-basic-components-richeditor.md#abouttodelete)事件，可通过回调中返回false阻止编辑区域默认的删除行为。在第一次删除builderSpan（@好友）的时候，先使用[RichEditorController.setSelection](../harmonyos-references/ts-basic-components-richeditor.md#setselection11)对整体进行选中，再次点击删除键时选中内容在RichEditor中会默认被整体删除。

  ```typescript
  // features/home/src/main/ets/view/CommentKeyboard.ets
  aboutToDelete: (value: RichEditorDeleteValue) => boolean = value => {
    const controller = this.richEditorController;
    const span = value.richEditorDeleteSpans[0];
    if (span && this.isBuilderSpan(span)) {
      if (this.hasSelection(controller)) {
        this.deleteBuilderSpan();
        return true;
      }
      controller.setSelection(value.offset, value.offset + 1);
      return false;
    }
    return true;
  }
  ```

* 内容获取与展示

  在编辑区域输入文字、表情、@好友内容，点击发送按钮，获取编辑区域内容，并弹窗展示内容以及@好友中好友的相关信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/chuDKZb_S9SwtUnRGM4N8g/zh-cn_image_0000002229337545.png "点击放大")

  可以通过[RichEditorController.getSpans](../harmonyos-references/ts-basic-components-richeditor.md#getspans)来获取编辑区域所有的内容，获取到的内容在getSpans方法的返回值中表现为[RichEditorTextSpanResult](../harmonyos-references/ts-basic-components-richeditor.md#richeditortextspanresult)和[RichEditorImageSpanResult](../harmonyos-references/ts-basic-components-richeditor.md#richeditorimagespanresult)两种类型。上文中提到过文字、图片表情、@好友三种内容与这两种类型的对应关系如下表：

  | 本文中的定义 | 对应编辑区域内容 | 添加方式 | getSpans方法返回值中对应的类型 |
  | --- | --- | --- | --- |
  | textSpan | 连续的文字 | 键盘输入或[RichEditorController.addTextSpan](../harmonyos-references/ts-basic-components-richeditor.md#addtextspan) | [RichEditorTextSpanResult](../harmonyos-references/ts-basic-components-richeditor.md#richeditortextspanresult) |
  | imageSpan | 图片表情 | [RichEditorController.addImageSpan](../harmonyos-references/ts-basic-components-richeditor.md#addimagespan) | [RichEditorImageSpanResult](../harmonyos-references/ts-basic-components-richeditor.md#richeditorimagespanresult) |
  | builderSpan | @[好友昵称] | [RichEditorController.addBuilderSpan](../harmonyos-references/ts-basic-components-richeditor.md#addbuilderspan11) | [RichEditorImageSpanResult](../harmonyos-references/ts-basic-components-richeditor.md#richeditorimagespanresult) |

  textSpan可通过RichEditorTextSpanResult.value获取文字内容。imageSpan可通过RichEditorImageSpanResult.valueResourceStr获取图片资源。但是builderSpan在RichEditorImageSpanResult中获取不到任何相关的内容信息，所以在点击好友头像添加@好友内容时需要手动将这些builderSpan进行维护。

  ```typescript
  // features/home/src/main/ets/view/CommentKeyboard.ets
  onAtFriendClick: (friend: User) => void = friend => {
    // ...
    this.setBuilderSpans(controller, friend);
  }
  ```

  实际开发中编辑区域不同类型的内容往往需要一种统一的数据结构来表达，方便传输和存储。该数据结构需要不仅能对编辑区域内容进行记录，也需要有携带一些额外信息的能力，比如携带@好友相关的用户信息。本文定义为RichEditorSpan。（实际开发中需要的属性字段根据需求灵活调整）。

  ```typescript
  // features/home/src/main/ets/view/CommentKeyboard.ets
  export interface RichEditorSpan {
    value?: string
    resourceValue?: ResourceStr
    type: 'text' | 'image' | 'builder'
    data?: User | ImageInfo
  }
  ```

  使用RichEditorSpan[]类型的数组builderSpans来维护@好友时的builderSpan，需要注意的是要保证每个builderSpan在数组中的顺序要与实际内容中出现的顺序一致。在添加builderSpan时，通过计算当前光标位置前面builderSpan的个数，来确定添加到builderSpans数组中的位置，并把需要携带的好友信息放入data属性中。

  ```typescript
  setBuilderSpans(controller: RichEditorController, friend: User) {
    const builderSpan: RichEditorSpan = {
      value: `@${friend.nickname}`,
      data: friend,
      type: 'builder'
    };
    const range: RichEditorRange = { end: controller.getCaretOffset() };
    const index = this.getBuilderSpanCount(controller, range) - 1;
    this.builderSpans.splice(index, 0, builderSpan);
  }

  getBuilderSpanCount(controller: RichEditorController, range: RichEditorRange) {
    return controller.getSpans(range).reduce((count: number, span) => {
      return this.isBuilderSpan(span) ? count + 1 : count;
    }, 0);
  }
  ```

  发送评论时，将获取到的内容用RichEditorSpan[]类型的数组richEditorSpans进行统一地表达。通过getSpans获取所有内容，如果是textSpan，通过value属性取出文字内容，设置RichEditorSpan.type为text，如果是imageSpan，通过valueResourceStr属性获取图片资源，设置RichEditorSpan.type为image。如果是builderSpan，按顺序从数组builderSpans中获取，并将他们按顺序添加到richEditorSpans中。

  ```typescript
  // features/home/src/main/ets/view/CommentKeyboard.ets
  onSendComment: () => void = () => {
    let builderSpanIndex = 0;
    let richEditorSpan: RichEditorSpan;
    const richEditorSpans: RichEditorSpan[] = [];
    this.richEditorController.getSpans().forEach((span, index) => {
      const textSpan = span as RichEditorTextSpanResult;
      const imageSpan = span as RichEditorImageSpanResult;
      if (textSpan.value) {
        richEditorSpan = { value: textSpan.value, type: 'text' };
      } else if (this.isBuilderSpan(span)) {
        richEditorSpan = this.builderSpans[builderSpanIndex];
        builderSpanIndex += 1;
      } else {
        richEditorSpan = { resourceValue: imageSpan.valueResourceStr, type: 'image' };
      }
      richEditorSpans.push(richEditorSpan);
    });
    // ...
  }
  ```

  最终生成的richEditorSpans数据格式如下：

  ```json
  [
    {
      "value": "@朋友1",
      "data": {
        "id": "0",
        "avatar": {
          "id": 16777268,
          "type": 20000,
          "params": [],
          "bundleName": "com.example.commentreply",
          "moduleName": "default"
        },
        "nickname": "朋友1"
      },
      "type": "builder"
    },
    {
      "value": "Hello",
      "type": "text"
    },
    {
      "resourceValue": "resource:///emoji_3.png",
      "type": "image"
    }
  ]
  ```

  当需要展示评论内容时，只需要对richEditorSpans进行遍历，根据type属性，分别对文字、表情、@好友进行展示逻辑的处理。具体展示形式开发者根据实际需求确定。

  ```typescript
  // features/home/src/main/ets/view/CommentSendDialog.ets
  Column() {
    Text($r('app.string.send_title'))
      .margin({ bottom: 20 })
    Flex({ wrap: FlexWrap.Wrap }) {
      ForEach(this.getComment(), (richEditorSpan: RichEditorSpan) => {
        if (richEditorSpan.type === 'text') {
          Text(richEditorSpan.value)
        } else if (richEditorSpan.type === 'image') {
          Image(richEditorSpan.resourceValue)
            .width(20)
        } else {
          Text(`${richEditorSpan.value}(`)
            .fontColor(0xFF133667)
          Text(`id：${(richEditorSpan.data as User).id}; avatar：`)
          Image((richEditorSpan.data as User).avatar)
            .width(20)
          Text(')')
        }
      }, (richEditorSpan: RichEditorSpan) => JSON.stringify(richEditorSpan))
    }
  }
  ```
* 选择图片

  点击图片按钮拉起系统相册，选择本地图片进行上传。该功能使用场景相对独立，本文不详细介绍。开发者需要进一步了解详情，可参考以下sample。

  + [选择并查看文档和媒体文件](https://gitcode.com/harmonyos_samples/picker)
  + [文件管理](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_NEXT-FilesManger)
  + [发布图片评论](https://gitcode.com/harmonyos_samples/image-comment)

## 示例代码

* [实现评论回复弹窗模块](https://gitcode.com/harmonyos_samples/CommentReply)
