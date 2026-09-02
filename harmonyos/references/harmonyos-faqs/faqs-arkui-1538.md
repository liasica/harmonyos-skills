---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1538
title: WrappedBuilder报参数类型不匹配的错误如何解决
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > WrappedBuilder报参数类型不匹配的错误如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:11+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5baebd92bb31d73602b6f9e1b935adf9fa6b1082967e0300c3b38e10f5c5910b
---

## 问题现象

使用WrappedBuilder维护UI时，遇到WrappedBuilder泛型报错如何处理？

报错提示如下：

```screen
Argument of type 'DialogCustomV2<T>' is not assignable to parameter of type 'MAPPER_VALUE'.
  The types of 'wrapped.builder' are incompatible between these types.
    Type '(args_0: T) => void' is not assignable to type '(args_0: BaseCustomDialogParam) => void'.
      Types of parameters 'args_0' and 'args_0' are incompatible.
        Type 'BaseCustomDialogParam' is not assignable to type 'T'.
          'BaseCustomDialogParam' is assignable to the constraint of type 'T', but 'T' could be instantiated with a different subtype of constraint 'BaseCustomDialogParam'.
```

解释：报错提示泛型参数类型不匹配，类型“DialogCustomV2<T>”不能分配给类型“DialogCustomV2<BaseCustomDialogParam>”。错误代码如下：

```screen
import { ComponentContent, UIContext } from '@kit.ArkUI';

// 定义基础接口
namespace Param {
  export interface BaseDialogParamV2 {
    alignment?: DialogAlignment
    mask?: boolean
    cornerRadius?: Dimension,
    autoCancel?: boolean,
    width?: Dimension,
    height?: Dimension,
  }

  export interface BaseCustomDialogParam {
    dialogFunc?: () => boolean;
  }
}

function simpleUUID(): string {
  return 'xxxxxxxxxxxx4xxxyxxxxxxxxxxxxxxx'.replace(/[xy]/g, (c) => {
    const r = Math.random() * 16 | 0;
    const v = c === 'x' ? r : (r & 0x3 | 0x8);
    return v.toString(16);
  });
}

// 定义泛型类DialogCustomV2
class DialogCustomV2<T extends Param.BaseCustomDialogParam> {
  uiContext: UIContext = new UIContext;
  wrapped: WrappedBuilder<[T]>;
  param: T;
  dialogParam: Param.BaseDialogParamV2;
  private _id: string;

  public get id(): string {
    return this._id;
  }

  constructor(wrapped: WrappedBuilder<[T]>, param: T, dialogParam?: Param.BaseDialogParamV2) {
    this.wrapped = wrapped;
    this.param = param;
    this.dialogParam = dialogParam ?? {};
    this._id = simpleUUID();
  }

  open() {
    let view = new ComponentContent(this.uiContext, this.wrapped, this.param);
    this.uiContext.getPromptAction().openCustomDialog(view, this.dialogParam);
  }
}

export function showCustomV2<T extends Param.BaseCustomDialogParam>(wrapped: WrappedBuilder<[T]>, param: T,
  dialogParam?: Param.BaseDialogParamV2) {
  const dialog: DialogCustomV2<T> = new DialogCustomV2<T>(wrapped, param, dialogParam);
  // 缓存弹窗映射
  type MAPPER_VALUE = DialogCustomV2<Param.BaseCustomDialogParam>;
  const MAPPER = new Map<string, MAPPER_VALUE>();
  // 弹框堆栈
  const STACK: Array<string> = [];
  MAPPER.set(dialog.id, dialog);
  STACK.push(dialog.id);
  dialog.open();
}

@Builder
function MyBuilder(param: Param.BaseCustomDialogParam) {
  Column() {
    Text('Hello from Dialog!')
      .fontSize(24)
      .fontWeight(FontWeight.Bold)
      .margin({ bottom: 20 });

    Button('点此执行自定义方法')
      .onClick(() => {
        if (param.dialogFunc) {
          const shouldClose = param.dialogFunc();
          if (shouldClose) {
            console.info('自定义方法被执行');
          }
        }
      })
      .margin({ top: 10 });
  }
  .backgroundColor(Color.White)
  .borderRadius(32)
  .padding(20)
  .alignItems(HorizontalAlign.Center);
}

let globalBuilder: WrappedBuilder<[Param.BaseCustomDialogParam]> = wrapBuilder(MyBuilder);

@Entry
@Component
struct TestPage {
  build() {
    Column() {
      Button('打开弹窗')
        .onClick(() => {
          // globalBuilder作为WrappedBuilder参数
          const param: Param.BaseCustomDialogParam = {
            dialogFunc: () => {
              // 这里可以加逻辑，比如提示、上报等
              console.info('这里可以执行自定义方法');
              // 返回true表示允许关闭
              return true;
            }
          };

          // 弹窗样式参数
          const dialogParam: Param.BaseDialogParamV2 = {
            width: 300,
            height: 200,
            cornerRadius: 16,
            mask: true,
            autoCancel: true,
            alignment: DialogAlignment.Center
          };

          // 调用showCustomV2，传入globalBuilder和参数
          showCustomV2(globalBuilder, param, dialogParam);
        });
    }
    .width('100%');
  }
}
```

## 背景知识

[wrapBuilder](../harmonyos-guides/arkts-wrapbuilder.md)作为全局@Builder的封装函数，返回一个WrappedBuilder对象，从而使得全局@Builder可以进行属性赋值和参数传递。

## 问题定位

查看报错部分代码：

```screen
export function showCustomV2<T extends Param.BaseCustomDialogParam>(wrapped: WrappedBuilder<[T]>, param: T,
  dialogParam?: Param.BaseDialogParamV2) {
  const dialog: DialogCustomV2<T> = new DialogCustomV2<T>(wrapped, param, dialogParam);
  // 缓存弹窗映射
  type MAPPER_VALUE = DialogCustomV2<Param.BaseCustomDialogParam>;
  const MAPPER = new Map<string, MAPPER_VALUE>();
  // 弹框堆栈
  const STACK: Array<string> = [];
  MAPPER.set(dialog.id, dialog);
  STACK.push(dialog.id);
  dialog.open();
}
```

查看DialogCustomV2的构造函数：

```screen
constructor(wrapped: WrappedBuilder<[T]>, param: T, dialogParam?: Param.BaseDialogParamV2) {
  this.wrapped = wrapped;
  this.param = param;
  this.dialogParam = dialogParam ?? {};
  this._id = simpleUUID();
}
```

可以看到，DialogCustomV2包含了一个WrappedBuilder类型的成员wrapped，而使用WrappedBuilder时需要指定一个明确的类型。

## 分析结论

上述代码是由于类型不匹配导致报错，虽然BaseCustomDialogParam能够满足T的约束条件，但是由于T是一个泛型类型，它可以被实例化为任何符合该约束的类型，这导致了类型不兼容的情况。目前WrappedBuilder不支持上述代码的用法。

## 修改建议

使用WrappedBuilder时为了确保类型安全和正确的功能实现，需要将DialogCustomV2中的T设置为实际要操作的数据类型的精确类型。在这个例子中，应该将DialogCustomV2<T>和wrapped: WrappedBuilder<[T]>中的T设置为BaseCustomDialogParam，而不是更宽泛的类型。

完整示例参考如下：

```screen
import { ComponentContent, UIContext } from '@kit.ArkUI';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

// 定义基础接口
namespace Param {
  export interface BaseDialogParamV2 {
    alignment?: DialogAlignment
    mask?: boolean
    cornerRadius?: Dimension,
    autoCancel?: boolean,
    width?: Dimension,
    height?: Dimension,
  }

  export interface BaseCustomDialogParam {
    dialogFunc?: () => boolean;
  }
}

function simpleUUID(): string {
  let rand = cryptoFramework.createRandom();
  let randData = rand.generateRandomSync(1);
  return 'xxxx'.replace(/[xy]/g, (str) => {
    const temp = randData.data[0] * 16 / 255 | 0;
    const value = str === 'x' ? temp : (temp & 0x3 | 0x8);
    return value.toString(16);
  });
}

// 定义泛型类DialogCustomV2
class DialogCustomV2<T extends Param.BaseCustomDialogParam> {
  uiContext: UIContext = new UIContext;
  wrapped: WrappedBuilder<[T]>;
  param: T;
  dialogParam: Param.BaseDialogParamV2;
  private _id: string;

  public get id(): string {
    return this._id;
  }

  constructor(wrapped: WrappedBuilder<[T]>, param: T, dialogParam?: Param.BaseDialogParamV2) {
    this.wrapped = wrapped;
    this.param = param;
    this.dialogParam = dialogParam ?? {};
    this._id = simpleUUID();
  }

  open() {
    let view = new ComponentContent(this.uiContext, this.wrapped, this.param);
    this.uiContext.getPromptAction().openCustomDialog(view, this.dialogParam);
  }
}

export function showCustomV2<T extends Param.BaseCustomDialogParam>(wrapped: WrappedBuilder<[Param.BaseCustomDialogParam]>,
  param: T,
  dialogParam?: Param.BaseDialogParamV2) {
  const dialog: DialogCustomV2<Param.BaseCustomDialogParam> =
    new DialogCustomV2<Param.BaseCustomDialogParam>(wrapped, param, dialogParam);
  // 缓存弹窗映射
  type MAPPER_VALUE = DialogCustomV2<Param.BaseCustomDialogParam>;
  const MAPPER = new Map<string, MAPPER_VALUE>();
  // 弹框堆栈
  const STACK: Array<string> = [];
  MAPPER.set(dialog.id, dialog);
  STACK.push(dialog.id);
  dialog.open();
}

@Builder
function MyBuilder(param: Param.BaseCustomDialogParam) {
  Column() {
    Text('Hello from Dialog!')
      .fontSize(24)
      .fontWeight(FontWeight.Bold)
      .margin({ bottom: 20 });

    Button('点此执行自定义方法')
      .onClick(() => {
        if (param.dialogFunc) {
          const shouldClose = param.dialogFunc();
          if (shouldClose) {
            console.info('自定义方法被执行');
          }
        }
      })
      .margin({ top: 10 });
  }
  .backgroundColor(Color.White)
  .borderRadius(32)
  .padding(20)
  .alignItems(HorizontalAlign.Center);
}

let globalBuilder: WrappedBuilder<[Param.BaseCustomDialogParam]> = wrapBuilder(MyBuilder);

@Entry
@Component
struct TestPage {
  build() {
    Column() {
      Button('打开弹窗')
        .onClick(() => {
          // globalBuilder作为WrappedBuilder参数
          const param: Param.BaseCustomDialogParam = {
            dialogFunc: () => {
              // 这里可以加逻辑，比如提示、上报等
              console.info('这里可以执行自定义方法');
              // 返回true表示允许关闭
              return true;
            }
          };

          // 弹窗样式参数
          const dialogParam: Param.BaseDialogParamV2 = {
            width: 300,
            height: 200,
            cornerRadius: 16,
            mask: true,
            autoCancel: true,
            alignment: DialogAlignment.Center
          };

          // 调用showCustomV2，传入globalBuilder和参数
          showCustomV2(globalBuilder, param, dialogParam);
        });
    }
    .width('100%');
  }
}
```
