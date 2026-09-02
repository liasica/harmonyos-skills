---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-framework-tablet-1
title: 平板弹窗被遮挡
breadcrumb: FAQ > 应用框架开发 > 平板 > 常见问题 > 平板弹窗被遮挡
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:31+08:00
doc_updated_at: 2026-07-02
content_hash: sha256:4b014d1510272b0ceb8f28c9839764da9517411accdf2454b7c7cbd675daeed2
---

## 问题现象

在横屏模式下打开应用，点击“已有账号登录”后，登录弹窗从底部弹出，未居中显示，且无法点击弹窗中的内容。切换为竖屏模式后，同样点击“已有账号登录”，弹窗底部内容被截断，信息显示不完整。

## 背景知识

关于[弹窗](../harmonyos-guides/arkts-dialog-overview.md)，根据用户交互操作场景，可分为模态弹窗和非模态弹窗两种类型，其区别在于用户是否必须对其做出响应。

* 模态弹窗为强交互形式，会中断用户当前的操作流程，要求用户必须做出响应才能继续其他操作，通常用于需要向用户传达重要信息的场景；
* 非模态弹窗，为弱交互形式，不会影响用户当前操作行为，用户可以不对其进行回应，通常都有时间限制，出现一段时间后会自动消失。一般用于告诉用户信息内容外还需要用户进行功能操作的场景。

## 问题定位

* 排查自定义弹窗中[@Builder](../harmonyos-guides/arkts-builder.md)自定义构建函数修饰的自定义组件中是否设置的height属性，强制固定了弹窗的高度，导致自定义弹窗的内容被截断，显示不全。
* 排查自定义弹窗中[BaseDialogOptions](../harmonyos-references/js-apis-promptaction.md#basedialogoptions11)属性中是否传入并设置了offset属性强行给自定义弹窗设置了向下的偏移量，导致弹窗向下偏移被遮挡。

## 分析结论

* 自定义弹窗的自定义构建函数[@Builder](../harmonyos-guides/arkts-builder.md)修饰的自定义组件中设置了height属性，并且值被写死，导致自定义弹窗内容超出部分被截断。
* 自定义弹窗的选项属性[BaseDialogOptions](../harmonyos-references/js-apis-promptaction.md#basedialogoptions11)中传入了offset属性值，在Y轴方向上设置了偏移量，导致弹窗贴底被遮挡。

## 修改建议

由于[CustomDialog](../harmonyos-guides/arkts-common-components-custom-dialog.md)在使用上存在较多限制，不支持动态创建和动态刷新，在相对较复杂的应用场景中推荐使用UIContext中获取到的[PromptAction](../harmonyos-references/js-apis-promptaction.md)对象提供的[openCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialog12)接口来实现自定义弹出框。以下是基于[PromptAction](../harmonyos-references/js-apis-promptaction.md)封装的自定义弹窗实现横竖屏居中显示不遮挡的示例，具体实现步骤如下：

* 创建ComponentContent。ComponentContent用于定义自定义弹出框的内容。其中，wrapBuilder(buildText)封装自定义组件，new Params(this.message)是自定义组件的入参，可以缺省，也可以传入基础数据类型。

  ```ts
  private contentNode: ComponentContent<Object> =
    new ComponentContent(this.ctx, wrapBuilder(buildText));
  ```
* 打开自定义弹出框。通过调用openCustomDialog接口打开的弹出框默认customStyle为true，即弹出框的内容样式完全按照contentNode自定义样式显示。

  ```ts
  PromptActionClass.ctx.getPromptAction()
    .openCustomDialog(PromptActionClass.contentNode, PromptActionClass.options)
    .then(() => {
      console.info('OpenCustomDialog complete.');
    })
    .catch((error: BusinessError) => {
      let message = (error as BusinessError).message;
      let code = (error as BusinessError).code;
      console.error(`OpenCustomDialog args error code is ${code}, message is ${message}`);
    });
  ```
* 关闭自定义弹出框。由于closeCustomDialog接口需要传入待关闭弹出框对应的ComponentContent。因此，如果需要在弹出框中设置关闭方法，则可参考完整示例封装静态方法来实现。关闭弹出框之后若需要释放对应的ComponentContent，则需要调用ComponentContent的dispose方法。

  ```ts
  PromptActionClass.ctx.getPromptAction()
    .closeCustomDialog(PromptActionClass.contentNode)
    .then(() => {
      console.info('CloseCustomDialog complete.');
    })
    .catch((error: BusinessError) => {
      let message = (error as BusinessError).message;
      let code = (error as BusinessError).code;
      console.error(`CloseCustomDialog args error code is ${code}, message is ${message}`);
    });
  ```
* PromptAction的BaseDialogOptions选项中offset属性值在Y轴方向上设置偏移量为0。

  ```ts
  aboutToAppear(): void {
    PromptActionClass.setContext(this.ctx);
    PromptActionClass.setContentNode(this.contentNode);
    PromptActionClass.setOptions({ alignment: DialogAlignment.Center });
  }
  ```
* 自定义组件的height属性不设置或设置为auto，高度由内容撑开。

  ```ts
  @Builder
  function buildText() {
    Column() {
      Flex({ justifyContent: FlexAlign.SpaceBetween }) {
        Text('账号登录').fontSize(24).fontWeight(FontWeight.Bold);
        Image($r('app.media.close'))
          .width(32)
          .height(32)
          .onClick(() => {
            PromptActionClass.closeDialog();
          });
      }.padding({ bottom: 24 });

      Column() {
        TextInput({ placeholder: '邮箱' })
          .width('100%')
          .showUnderline(true);
        TextInput({ placeholder: '验证码' })
          .width('100%')
          .showUnderline(true);

        Row() {
          Checkbox({ name: 'checkbox2', group: 'checkboxGroup' })
            .select(false)
            .selectedColor(0x39a2db)
            .shape(CheckBoxShape.ROUNDED_SQUARE)
            .onChange((value: boolean) => {
              console.info('Checkbox2 change is' + value);
            });
          Text('我已阅读并同意《隐私政策》');
        }.padding({ top: 12, bottom: 12 });
      };

      Button('登录')
        .width('100%')
        .onClick(() => {
          PromptActionClass.closeDialog();
        });

      Column() {
        Text('其他账号登录').padding({ bottom: 12 });
        Row() {
          Image($r('app.media.huawei')).width(32).height(32).margin({ right: 12 });
        };
      }
      .padding({ top: 24 });
    }.backgroundColor('#FFF0F0F0')
    .padding(24)
    .width(480)
    .border({ radius: '10%' });
  }
  ```

完整示例如下：

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { ComponentContent, promptAction, UIContext } from '@kit.ArkUI';

export class PromptActionClass {
  static ctx: UIContext;
  static contentNode: ComponentContent<Object>;
  static options: promptAction.BaseDialogOptions;

  static setContext(context: UIContext) {
    PromptActionClass.ctx = context;
  }

  static setContentNode(node: ComponentContent<Object>) {
    PromptActionClass.contentNode = node;
  }

  static setOptions(options: promptAction.BaseDialogOptions) {
    PromptActionClass.options = options;
  }

  static openDialog() {
    if (PromptActionClass.contentNode !== null) {
      PromptActionClass.ctx.getPromptAction()
        .openCustomDialog(PromptActionClass.contentNode, PromptActionClass.options)
        .then(() => {
          console.info('OpenCustomDialog complete.');
        })
        .catch((error: BusinessError) => {
          let message = (error as BusinessError).message;
          let code = (error as BusinessError).code;
          console.error(`OpenCustomDialog args error code is ${code}, message is ${message}`);
        });
    }
  }

  static closeDialog() {
    if (PromptActionClass.contentNode !== null) {
      PromptActionClass.ctx.getPromptAction()
        .closeCustomDialog(PromptActionClass.contentNode)
        .then(() => {
          console.info('CloseCustomDialog complete.');
        })
        .catch((error: BusinessError) => {
          let message = (error as BusinessError).message;
          let code = (error as BusinessError).code;
          console.error(`CloseCustomDialog args error code is ${code}, message is ${message}`);
        });
    }
  }

  static updateDialog(options: promptAction.BaseDialogOptions) {
    if (PromptActionClass.contentNode !== null) {
      PromptActionClass.ctx.getPromptAction()
        .updateCustomDialog(PromptActionClass.contentNode, options)
        .then(() => {
          console.info('UpdateCustomDialog complete.');
        })
        .catch((error: BusinessError) => {
          let message = (error as BusinessError).message;
          let code = (error as BusinessError).code;
          console.error(`UpdateCustomDialog args error code is ${code}, message is ${message}`);
        });
    }
  }
}
```

```ts
// Index.ets
import { ComponentContent } from '@kit.ArkUI';
import { PromptActionClass } from './PromptActionView';

@Builder
function buildText() {
  Column() {
    Flex({ justifyContent: FlexAlign.SpaceBetween }) {
      Text('账号登录').fontSize(24).fontWeight(FontWeight.Bold);
      Image($r('app.media.close'))
        .width(32)
        .height(32)
        .onClick(() => {
          PromptActionClass.closeDialog();
        });
    }.padding({ bottom: 24 });

    Column() {
      TextInput({ placeholder: '邮箱' })
        .width('100%')
        .showUnderline(true);
      TextInput({ placeholder: '验证码' })
        .width('100%')
        .showUnderline(true);

      Row() {
        Checkbox({ name: 'checkbox2', group: 'checkboxGroup' })
          .select(false)
          .selectedColor(0x39a2db)
          .shape(CheckBoxShape.ROUNDED_SQUARE)
          .onChange((value: boolean) => {
            console.info('Checkbox2 change is' + value);
          });
        Text('我已阅读并同意《隐私政策》');
      }.padding({ top: 12, bottom: 12 });
    };

    Button('登录')
      .width('100%')
      .onClick(() => {
        PromptActionClass.closeDialog();
      });

    Column() {
      Text('其他账号登录').padding({ bottom: 12 });
      Row() {
        Image($r('app.media.huawei')).width(32).height(32).margin({ right: 12 });
      };
    }
    .padding({ top: 24 });
  }.backgroundColor('#FFF0F0F0')
  .padding(24)
  .width(480)
  .border({ radius: '10%' });
}

@Entry
@Component
struct Index {
  private ctx: UIContext = this.getUIContext();
  private contentNode: ComponentContent<Object> =
    new ComponentContent(this.ctx, wrapBuilder(buildText));

  aboutToAppear(): void {
    PromptActionClass.setContext(this.ctx);
    PromptActionClass.setContentNode(this.contentNode);
    PromptActionClass.setOptions({ alignment: DialogAlignment.Center });
  }

  build() {
    Column() {
      Button('已有账号登录')
        .margin({ bottom: 24 })
        .onClick(() => {
          PromptActionClass.openDialog();
        });
    }
    .justifyContent(FlexAlign.End)
    .width('100%')
    .height('100%');
  }
}
```
