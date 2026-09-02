---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1027
title: 如何实现想法标记功能
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现想法标记功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:26+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5a8ecb8c7a497b166000eb5330a138a15d029da169dbb0946714de371c439541
---

## 问题现象

想要实现类似于华为阅读应用的想法标记功能，具体要求如下：

1. 长按选择文本，弹出的菜单内包含想法按钮。
2. 点击想法按钮弹出想法输入框，当输入框为空时不能添加想法。
3. 点击添加想法后，输入框消失，选择的文本标记高亮。
4. 点击高亮部分可以显示对应的想法内容。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/ZUnIjI1OQ3eUGRKfINioDg/zh-cn_image_0000002658804085.png "点击放大")

## 背景知识

[Text](../harmonyos-references/ts-basic-components-text.md)是文本组件，用于展示用户视图，如显示文章的文字内容。该组件支持绑定自定义文本选择菜单，用户可根据需要选择不同功能。此外，还可以扩展自定义菜单，丰富可用选项，进一步提升用户体验。[Span](../harmonyos-references/ts-basic-components-span.md)则用于展示行内文本。

## 解决方案

由于[RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)组件不支持禁止文本编辑，所以主体的文本展示功能使用Text和Span组件实现。按照要求，可以将想法标记功能分为以下几点分别实现：

1. 选择菜单内添加自定义按钮：通过设置Text组件的[editMenuOptions](../harmonyos-references/ts-basic-components-text.md#editmenuoptions12)属性实现。
2. 点击想法按钮弹出想法输入框：[绑定半模态页面](../harmonyos-guides/arkts-sheet-page.md)，将输入框放在半模态页面内，点击按钮时打开。
3. 输入框为空时不能添加想法：通过[TextInput](../harmonyos-references/ts-basic-components-textinput.md)组件的[onChange()](../harmonyos-references/ts-basic-components-textinput.md#onchange)事件读取输入框的内容并记录，在添加想法时判断输入框内容是否为空，若为空则不做任何反应。
4. 将选择的文本标记高亮：参考[文本标记高亮显示](../architecture-guides/text_marker_ability-0000002283796046.md)。
5. 点击高亮部分显示对应想法：创建一个Map用来存储想法，以高亮的结束坐标为键，想法内容为值，点击高亮时读取Map值用于显示。

完整示例代码如下：

```ts
import { PromptAction } from '@kit.ArkUI';
import { JSON } from '@kit.ArkTS';

const TEXT_DATA = '文本内容'; // 展示的文本内容

@Entry
@Component
struct TextPage {
  promptAction: PromptAction = this.getUIContext().getPromptAction();
  @StorageProp('bottomRectHeight')
  bottomRectHeight: number = 0;
  @StorageProp('topRectHeight')
  topRectHeight: number = 0;
  @State markList: HighlightMark[] = []; // 高亮标记数据
  currentColor: number = 0; // 当前笔记颜色
  @State textLineHeight: Length = 26; // 行高
  @State textFontSize: Length = 17; // 字体大小
  originalText: string = TEXT_DATA; // 显示文本
  private selectionStart: number = -1; // 当前选中区间开头
  private selectionEnd: number = -1; // 当前选中区间结尾
  private controller: TextController = new TextController();
  @State isShowSheet: boolean = false; // 控制想法输入框的显隐
  @State ideaInput: string = ''; // 记录输入的想法
  onCreateMenu = (menuItems: Array<TextMenuItem>) => { // 自定义菜单内容
    let item1: TextMenuItem = {
      content: '想法',
      icon: $r('app.media.startIcon'),
      id: TextMenuItemId.of('IDEA'),
    };
    menuItems.unshift(item1);
    return menuItems;
  };
  onMenuItemClick = (menuItem: TextMenuItem) => { // 自定义点击菜单事件
    if (menuItem.id.equals(TextMenuItemId.of('IDEA'))) {
      this.isShowSheet = true; // 打开想法输入框
      return true;
    }
    return false;
  };
  @State editMenuOptions: EditMenuOptions = {
    onCreateMenu: this.onCreateMenu,
    onMenuItemClick: this.onMenuItemClick
  };
  ideaSet: Map<number, string> = new Map(); // 创建一个集合来保存所有想法

  // 初始化文本内容
  aboutToAppear(): void {
    this.markList = [{
      // 载入文本内容
      start: 0,
      end: this.originalText.length,
      color: Color.Transparent
    }];
  }

  // 标记选中区域高亮
  markHighlight(highlight: boolean) {
    if (this.selectionStart !== -1 && this.selectionEnd !== -1) {
      let leftMarks: HighlightMark[] = []; // 区域左侧的文本样式数据
      let rightMarks: HighlightMark[] = []; // 区域右侧的文本样式数据
      // 当前需要更改样式的区域
      let currentSelection: HighlightMark = {
        start: this.selectionStart,
        end: this.selectionEnd,
        color: highlight ? Color.Pink : Color.Transparent
      };

      this.markList.forEach((mark) => {
        // 如果既有样式区间开头在当前选中区域开头之前
        if (mark.start < currentSelection.start) {
          // 如果既有样式区间结尾在当前选中区域开头之前，即两个区间无交集
          if (mark.end < currentSelection.start) {
            leftMarks.push({
              start: mark.start,
              end: mark.end,
              color: mark.color
            });
          } else if (mark.color === currentSelection.color) {
            // 两个区间有交集且样式一致，合并入当前选中区域
            currentSelection.start = mark.start;
          } else {
            // 样式不一致，截断区间
            leftMarks.push({
              start: mark.start,
              end: currentSelection.start,
              color: mark.color
            });
          }
        }
        // 既有样式区间在当前选中区域末尾之后
        if (mark.end > currentSelection.end) {
          // 如果既有样式区间开头在当前选中区域开头之后，即两个区间无交集
          if (mark.start > currentSelection.end) {
            rightMarks.push({
              start: mark.start,
              end: mark.end,
              color: mark.color
            });
          } else if (mark.color === currentSelection.color) {
            // 两个区间有交集且样式一致，合并入当前选中区域
            currentSelection.end = mark.end;
          } else {
            // 样式不一致，截断区间
            rightMarks.push({
              start: currentSelection.end,
              end: mark.end,
              color: mark.color
            });
          }
        }
      });
      // 合并当前与左右文本样式数据
      this.markList = leftMarks.concat(currentSelection, rightMarks);
    }
  }

  // 文字预览区域
  @Builder
  TextViewer() {
    Scroll() {
      Text('', { controller: this.controller }) {
        ForEach(this.markList, (mark: HighlightMark) => {
          Span(this.originalText.substring(mark.start, mark.end))
            .textBackgroundStyle({ color: mark.color, radius: 0 })
            .lineHeight(this.textLineHeight)
            .fontSize(this.textFontSize)
            .onClick(() => { // 通过底色判断是否绑定想法
              if (mark.color != Color.Transparent) {
                this.promptAction.showToast({ message: this.ideaSet.get(mark.end) }); // 展示想法内容
              }
            })
        }, (mark: HighlightMark) => JSON.stringify(mark));
      }
      .editMenuOptions(this.editMenuOptions) // 绑定自定义菜单
      .padding(24)
      .copyOption(CopyOptions.InApp)
      .onTextSelectionChange((selectionStart: number, selectionEnd: number) => { // 记录光标选中区域
        this.selectionStart = selectionStart;
        this.selectionEnd = selectionEnd;
      });

    }
    .scrollBar(BarState.Off)
    .width('90%')
    .layoutWeight(1);
  }

  // 想法标题
  @Builder
  titleBuilder() {
    Column() {
      Text('请写下你的想法')
    }
    .width('100%')
    .justifyContent(FlexAlign.Center)
  }

  // 想法输入框
  @Builder
  SheetBuilder() {
    Column({ space: 30 }) {
      TextInput()
        .width('90%')
        .height('70%')
        .onChange((index: string) => {
          this.ideaInput = index; // 记录输入内容
        })

      Button('添加想法')
        .backgroundColor('#0A59F7')
        .opacity(this.ideaInput ? 1 : 0.4)
        .width('90%')
        .onClick(() => {
          if (this.ideaInput) { // 设置有内容时才可以点击
            this.markHighlight(true); // 标记高亮表示此处有想法
            this.ideaSet.set(this.selectionEnd, this.ideaInput); // 将想法放入集合
            this.ideaInput = ''; // 清空输入记录
            this.isShowSheet = false; // 关闭想法输入框
            this.controller.closeSelectionMenu(); // 关闭菜单
          }
        })
    }
    .width('100%')
    .height('100%')
  }

  build() {
    Column() {
      this.TextViewer();
    }
    .height('100%')
    .width('100%')
    .padding({
      top: this.getUIContext().px2vp(this.topRectHeight),
      bottom: this.getUIContext().px2vp(this.bottomRectHeight)
    })
    .bindSheet($$this.isShowSheet, this.SheetBuilder(), {
      detents: [SheetSize.MEDIUM, SheetSize.LARGE, 600],
      preferType: SheetType.BOTTOM,
      title: this.titleBuilder(),
      showClose: false,
      dragBar: false
    })
  }
}

interface HighlightMark { // 创建高亮文字类
  start: number; // 区间开头（含）
  end: number; // 区间结尾（不含）
  color: ResourceColor; // 高亮颜色，无高亮标记则为透明
}
```
