---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1048
title: RichEditor实现撤销和重做功能
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > RichEditor实现撤销和重做功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:26+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:21ca1e07a22d89de2798fa57453a621dd0a094f415e7661a1b1b1bf2d66a1d99
---

## 问题现象

如何实现RichEditor撤销和重做的功能。

## 背景知识

富文本编辑器[RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)，是支持图文混排和文本交互式编辑的组件

撤销和重做：撤销指的是回退上一步操作，重做指的是恢复上一步撤销的操作。

## 解决方案

要实现编辑器撤销和重做的功能，本质上是要在做输入操作时记录包括内容、光标位置等信息，从而可以在撤销和重做的时候可以恢复原状。因此需要对输入操作进行改造，基于输入命令二次封装，增加undo函数撤销输入的内容同时恢复光标位置，同时我们还需要用栈来记录历史的操作信息。下面是一些核心的步骤：

1. 抽象EditorCommand类，封装了execute方法以及undo方法。
2. 实现InsertTextCommand输入文本类，execute方法内执行controller.addTextSpan输入内容，同时记录光标位置。
3. 实现一个EditorHistoryManager类，内部维护撤销栈undoStack和重做栈redoStack，每次编辑器正常输入时会往undoStack插入一个EditorCommand实例，并执行实例的execute方法输入内容，同时清空redoStack。
4. 当执行撤销时，将undoStack栈从顶部依次弹出实例；同时执行每个实例的undo方法让内容还原以及使光标恢复，并将弹出的元素推入redoStack。
5. 当执行重做时，将redoStack栈从顶部依次弹出实例；同时执行每个实例的redo方法让内容还原以及使光标恢复，并将弹出的元素推入undoStack。

具体代码如下：

```ts
// 1. 抽象命令基类
export abstract class EditorCommand {
  abstract execute(controller: RichEditorController);
  abstract undo(controller: RichEditorController);
}

// 2. 插入文本命令类
export class InsertTextCommand extends EditorCommand {
  private text: string;
  private prevOffset: number | null = 0;
  private curOffset: number | null = 0;
  private options: RichEditorTextSpanOptions;

  constructor(text: string, options: RichEditorTextSpanOptions) {
    super();
    this.text = text;
    this.options = JSON.parse(JSON.stringify(options));
  }

  execute(controller: RichEditorController) {
    // 移动到插入位置并插入文本
    this.prevOffset = controller.getCaretOffset();
    this.options.offset = this.prevOffset;
    controller.addTextSpan(this.text, this.options);
    this.curOffset = controller.getCaretOffset();
  }

  undo(controller: RichEditorController) {
    // 计算要删除的范围
    const start = this.prevOffset;
    const end = this.curOffset;
    // 删除插入的文本
    controller.deleteSpans({ start: start, end: end });
    // 恢复原始光标位置
    controller.setCaretOffset(start);
  }
}

// 历史输入管理类
@ObservedV2
export class EditorHistoryManager {
  @Trace private undoStack: EditorCommand[] = [];
  @Trace private redoStack: EditorCommand[] = [];
  private maxHistorySize: number = 100;
  private controller: RichEditorController;

  constructor(controller: RichEditorController) {
    this.controller = controller;
  }

  @Computed
  get canUndo(): boolean {
    return this.undoStack.length > 0;
  }

  @Computed
  get canRedo(): boolean {
    return this.redoStack.length > 0;
  }

  // 执行新命令
  executeCommand(command: EditorCommand) {
    command.execute(this.controller);
    this.undoStack.push(command);
    // 清空重做栈
    this.redoStack = [];
    // 控制历史记录大小
    this.trimHistory();
  }

  undo() {
    if (this.undoStack.length === 0) {
      return;
    }
    const command = this.undoStack.pop()!;
    command.undo(this.controller);
    this.redoStack.push(command);
  }

  redo() {
    if (this.redoStack.length === 0) {
      return;
    }
    const command = this.redoStack.pop()!;
    command.execute(this.controller);
    this.undoStack.push(command);
  }

  clearHistory(): void {
    this.undoStack = [];
    this.redoStack = [];
  }

  private trimHistory(): void {
    if (this.undoStack.length > this.maxHistorySize) {
      this.undoStack.shift();
    }
  }
}

@Entry
@Component
struct Index {
  private message: string = 'Hello World';
  private editorOptions: RichEditorOptions = { controller: new RichEditorController() };
  private historyManager: EditorHistoryManager = new EditorHistoryManager(this.editorOptions.controller);

  build() {
    Column() {
      Row({ space: 10 }) {
        Button('前进').width(100).onClick(() => {
          this.historyManager.redo();
        }).enabled(this.historyManager.canRedo)
        Button('回退').width(100).onClick(() => {
          this.historyManager.undo();
        }).enabled(this.historyManager.canUndo)
      }
      .width('100%')
      .height(100)
      .justifyContent(FlexAlign.Center)

      RichEditor(this.editorOptions)
        .placeholder(this.message)
        .height('100%')
        .caretColor(Color.Orange)
        .aboutToIMEInput((value) => {
          let command = new InsertTextCommand(value.insertValue, {});
          this.historyManager?.executeCommand(command);
          return false;
        })
        .layoutWeight(1)
    }
    .height('100%')
    .width('100%')
  }
}
```

## 总结

通过封装输入命令，以及维护undo撤销栈和redo重做栈，我们就可以实现编辑器的撤销和重做。
