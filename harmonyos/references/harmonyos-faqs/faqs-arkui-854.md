---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-854
title: 点击左边的各项功能模块，软键盘都会自动拉起又退出
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 点击左边的各项功能模块，软键盘都会自动拉起又退出
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:04+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:745182a50e6aa98e38b792e3ffd3fd75950b96570f5f2a70db482338a4721f60
---

## 问题现象

应用内某tab页面，点击左边的各项功能模块tab，右边会跳转对应的页面，软键盘都会自动拉起又退出。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/Xw_OAjMnQTKH7PWSOS0fZw/zh-cn_image_0000002628398644.png "点击放大")

## 背景知识

* [NavDestination](../harmonyos-references/ts-basic-components-navdestination.md#子组件)：作为子页面的根容器，用于显示Navigation的内容区。
  + [onWillShow](../harmonyos-references/ts-basic-components-navdestination.md#onwillshow12)：当该Destination显示之前触发此回调。
  + [onWillHide](../harmonyos-references/ts-basic-components-navdestination.md#onwillhide12)：当该Destination隐藏之前触发此回调。
* 焦点控制：自定义组件的走焦效果，可设置组件是否走焦和具体的走焦顺序，tab键或者方向键切换焦点。
  + [focusable](../harmonyos-references/ts-universal-attributes-focus.md#focusable)：设置当前组件是否可以获焦。
  + [defaultFocus](../harmonyos-references/ts-universal-attributes-focus.md#defaultfocus9)：设置当前组件是否为当前层级页面上的默认焦点。

## 问题定位

切换左边不同的模块，导致键盘拉起又自动退出，从现象来看推测可能是页面组件获取焦点然后又失去焦点导致的。

1. 分析日志，可以看到NavDestination页面跳转时，新页面展示，旧页面失去焦点，旧页面的键盘也随之关闭。

   ```txt
   AceFocus: [dict][(100000:100000:scope)] Focus view: NavDestination/2179 shown
   AceFocus: [dict][(100000:100000:scope)] Focus view: NavDestination/2117 lost focus
   AceNavigation: [dict][(100000:100000:scope)] GridEditor lifecycle change to onWillHide state.
   AceNavigation: [dict][(100000:100000:scope)] GridEditor lifecycle change to onWillShow state.
   AceKeyboard: [dict][(100000:100000:scope)] PageChange CloseKeyboard FrameNode notNeedSoftKeyboard.
   AceKeyboard: [dict][(100000:100000:scope)] PageChange CloseKeyboard SoftKeyboard Closes Successfully.
   ```
2. 接着根据"rich editor in focus"可知跳转新页面后，RichEditor组件获取焦点，并拉起键盘。

   ```txt
   AceFocus: [dict][(100000:100000:scope)] Request focus on focus view:NavDestination/2179.
   AceRichText: [dict][(100000:100000:scope)] rich editor in focus
   AceRichText: [dict][(100000:100000:scope)] HandleFocusEvent/2202
   AceKeyboard: [dict][(100000:100000:scope)] isScrollableChild_: 1
   AceRichText: [dict][(100000:100000:scope)] onFocus, requestKeyboard-1, windowMode=1
   AceRichText: [dict][(100000:100000:scope)] request keyboard, opts-0, 1, 1
   inputMethod/ImsaKit: [dict]line: 253, function: Attach,isShowKeyboard 1.
   ```
3. 然后从"OnFocusNodeChange"看出焦点发生变化，"NavDestination/2179"和"RichEditor/2202"在获取焦点时产生冲突，而"new isKeyboardEnableShow: false"说明键盘最后退出了。

   ```txt
   AceFocus: [dict][(100000:100000:scope)] FocusSwitch end, RichEditor/secure field onBlur, RichEditor/secure field onFocus, start: 2, end: 1, update: 2
   AceKeyboard: [dict][(100000:100000:scope)] current focus node info : (RichEditor/2202).
   AceRichText: [dict][(100000:100000:scope)] OnFocusNodeChange/2202, reason=0, blockKbInFloating-0
   AceFocus: [dict][(100000:100000:scope)] Focus view: NavDestination/2179 is first shown.
   AceFocus: [dict][(100000:100000:scope)] Request focus on default focus: RichEditor/2202 return: 1.
   CONCUR: [dict]report subFocus pid 4860 start
   WINDOW: SCBKeyboardSession --> old isKeyboardEnableShow: true, new isKeyboardEnableShow: false
   SCB: SCBKeyboardManager --> keyboard is not foreground, not need modify keyboard layer.
   inputMethod/ImsaKit: [dict]line: 645, function: operator(),OnInputStart task end!
   ```

## 分析结论

NavDestination页面跳转时，不同页面和组件对获取焦点处理不当，导致的键盘反复拉起、退出。

## 修改建议

建议在onWillShow、onWillHide等生命周期函数中控制焦点状态，优化不同页面和组件获取和失去焦点的逻辑，避免键盘反复拉起、退出，提升用户体验。示例代码如下：

```ts
@Entry
@Component
struct PageSwitchDemo {
  @Provide('pageInfos') pageInfos: NavPathStack = new NavPathStack();

  @Builder
  pageMap(name: string) {
    if (name === 'TestPage') {
      TestPage();
    }
  }

  build() {
    Column() {
      Navigation(this.pageInfos) {
        Column() {
          Button('TestPage1')
            .onClick(() => {
              this.pageInfos.pushPath({ name: 'TestPage', param: 'TestPage1' });
            })
            .margin({ bottom: 16 });
          Button('TestPage2')
            .onClick(() => {
              this.pageInfos.pushPath({ name: 'TestPage', param: 'TestPage2' });
            });
        }
        .padding(10)
      }
      .navDestination(this.pageMap)
      .mode(NavigationMode.Split);
    }
    .height('100%')
    .width('100%');
  }
}

@Component
struct TestPage {
  @State name: string = 'NA';
  @Consume('pageInfos') pageInfos: NavPathStack;
  @State isEnableFocus: boolean = false;
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };

  build() {
    NavDestination() {
      Column() {
        Column() {
          RichEditor(this.options)
            .onReady(() => {
              this.controller.addTextSpan('test text string.', {
                style: {
                  fontColor: Color.Black,
                  fontSize: 15
                }
              });
            })
            .defaultFocus(true)
            .focusable(this.isEnableFocus)
        }.width('100%');
      }.height('100%');
    }
    .onReady((context: NavDestinationContext) => {
      this.name = context.pathInfo.param as string;
    })
    .title(this.name)
    .onWillShow(() => {
      this.isEnableFocus = true;
    })
    .onWillHide(() => {
      this.isEnableFocus = false;
    });
  }
}
```

更多关于焦点的内容可以参考官网的[焦点事件](../harmonyos-guides/arkts-common-events-focus-event.md#基础概念与规范)、[焦点控制](../harmonyos-references/ts-universal-attributes-focus.md)。
