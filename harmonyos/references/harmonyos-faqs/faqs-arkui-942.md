---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-942
title: 关闭ComponentContent创建的弹窗未触发aboutToDisappear生命周期回调
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 关闭ComponentContent创建的弹窗未触发aboutToDisappear生命周期回调
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:22+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:8427b96d008b4737ce0cf85307d49dfb271564cb7bfbf75f16831a8128f393cb
---

## 问题现象

* 场景一：通过uiContext.getPromptAction().openCustomDialog()打开弹窗时aboutToAppear()会触发，但是uiContext.getPromptAction().closeCustomDialog()关闭弹窗时aboutToDisappear()未触发。

  错误代码如下：

  index：

  ```ts
  @Entry
  @Component
  struct CustomDialogCloseDemo {
    @State setTimeOut: number = 0;

    build() {
      Row() {
        Column({ space: 20 }) {
          Button('打开自定义弹窗')
            .fontSize(20)
            .onClick(async () => {
              const uiContext = this.getUIContext();
              const componentContent = new ComponentContent(this.getUIContext(), wrapBuilder(customDialogBuilder));
              uiContext.getPromptAction().openCustomDialog(componentContent, {
                onWillDismiss: () => {
                  uiContext.getPromptAction().closeCustomDialog(componentContent).then(() => {
                  });
                }
              });
              this.setTimeOut = setTimeout(() => {
                uiContext.getPromptAction().closeCustomDialog(componentContent).then(() => {
                });
              }, 2000);
            });
        }
        .width('100%');
      }
      .height('100%');
    }
  }
  ```

  customDialogComponent：

  ```ts
  @Builder
  export function customDialogBuilder() {
    customDialogComponent();
  }

  @Component
  struct customDialogComponent {
    aboutToAppear(): void {
      console.info('测试弹窗打开');
    }

    aboutToDisappear(): void {
      console.info('测试弹窗关闭');
    }

    build() {
      Column({ space: 30 }) {
        Text('弹窗页面')
          .fontColor(Color.White)
          .height('100%')
          .fontSize(30);
      }
      .justifyContent(FlexAlign.Center)
      .alignItems(HorizontalAlign.Center)
      .height(150)
      .width('90%')
      .justifyContent(FlexAlign.SpaceBetween)
      .backgroundColor('rgba(148, 148, 148, 1.00)');
    }
  }
  ```
* 场景二：通过uiContext.openBindSheet()打开半模态页面时aboutToAppear()会触发，但是uiContext.closeBindSheet()关闭半模态页面时aboutToDisappear()未触发。

  错误代码如下：

  ```ts
  import { FrameNode, ComponentContent } from "@kit.ArkUI";
  import { BusinessError } from '@kit.BasicServicesKit';

  class Params {
    text: string = "";

    constructor(text: string) {
      this.text = text;
    }
  }

  let contentNode: ComponentContent<Params>;
  let gUIContext: UIContext;

  @Builder
  function buildText() {
    buildTextComponent()
  }

  @Component
  struct buildTextComponent {
    aboutToAppear(): void {
      console.info('测试半模态打开')
    }

    aboutToDisappear(): void {
      console.info('测试半模态关闭')
    }

    build() {
      Column() {
        Text('')
        Button('Update BindSheet')
          .fontSize(20)
          .onClick(() => {
            gUIContext.updateBindSheet(contentNode, {
              backgroundColor: Color.Pink,
            }, true)
              .then(() => {
                console.info('updateBindSheet success');
              })
              .catch((err: BusinessError) => {
                console.error(`updateBindSheet error: ${err.code} ${err.message}`);
              })
          })

        Button('Close BindSheet')
          .fontSize(20)
          .onClick(() => {
            gUIContext.closeBindSheet(contentNode)
              .then(() => {
                console.info('closeBindSheet success');
              })
              .catch((err: BusinessError) => {
                console.error(`closeBindSheet error: ${err.code} ${err.message}`);
              })
          })
      }
    }
  }

  @Entry
  @Component
  struct UIContextBindSheet {
    @State message: string = 'BindSheet';

    aboutToAppear() {
      gUIContext = this.getUIContext();
      contentNode = new ComponentContent(this.getUIContext(), wrapBuilder(buildText));
    }

    build() {
      RelativeContainer() {
        Column() {
          Button('Open BindSheet')
            .fontSize(20)
            .onClick(() => {
              let uiContext = this.getUIContext();
              let uniqueId = this.getUniqueId();
              let frameNode: FrameNode | null = uiContext.getFrameNodeByUniqueId(uniqueId);
              let targetId = frameNode?.getFirstChild()?.getUniqueId();
              uiContext.openBindSheet(contentNode, {
                height: SheetSize.MEDIUM,
                backgroundColor: Color.Green,
                title: { title: "Title", subtitle: "subtitle" }
              }, targetId)
                .then(() => {
                  console.info('openBindSheet success');
                })
                .catch((err: BusinessError) => {
                  console.error(`openBindSheet error: ${err.code} ${err.message}`);
                })
            })
        }
      }
      .height('100%')
      .width('100%')
    }
  }
  ```

## 背景知识

[ComponentContent](../harmonyos-references/js-apis-arkui-componentcontent.md#componentcontent-1)创建的[openCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialog12)弹窗的关闭过程不涉及页面的销毁，弹窗关闭时不会执行[aboutToDisappear()](../harmonyos-references/ts-custom-component-lifecycle.md#abouttodisappear)方法。同理，[openBindSheet](../harmonyos-references/arkts-apis-uicontext-uicontext.md#openbindsheet12)创建的半模态页面关闭过程也不涉及页面的销毁，关闭时同样不会执行[aboutToDisappear()](../harmonyos-references/ts-custom-component-lifecycle.md#abouttodisappear)方法。

## 解决方案

* 场景一：

  如果想在弹窗关闭后触发弹窗的aboutToDisappear()生命周期函数，可以在promptAction.closeCustomDialog()的异步方法回调里，调用ComponentContent的[dispose()](../harmonyos-references/js-apis-arkui-componentcontent.md#dispose)方法立即释放当前ComponentContent实例，解除节点之间的绑定关系即可触发aboutToDisappear()生命周期函数。

  对index代码做如下修改：

  ```ts
  import { ComponentContent } from '@kit.ArkUI';
  import { customDialogBuilder } from './customDialogComponent';

  @Entry
  @Component
  struct CustomDialogCloseDemo {
    @State setTimeOut: number = 0;

    build() {
      Row() {
        Column({ space: 20 }) {
          Button('打开自定义弹窗')
            .fontSize(20)
            .onClick(async () => {
              const uiContext = this.getUIContext();
              const componentContent = new ComponentContent(this.getUIContext(), wrapBuilder(customDialogBuilder));
              uiContext.getPromptAction().openCustomDialog(componentContent, {
                onWillDismiss: () => {
                  uiContext.getPromptAction().closeCustomDialog(componentContent).then(() => {
                    clearTimeout(this.setTimeOut);
                    componentContent.dispose();
                  });
                }
              });
              this.setTimeOut = setTimeout(() => {
                uiContext.getPromptAction().closeCustomDialog(componentContent).then(() => {
                  componentContent.dispose();
                });
              }, 2000);
            });
        }
        .width('100%');
      }
      .height('100%');
    }
  }
  ```

  customDialogComponent：

  ```ts
  @Builder
  export function customDialogBuilder() {
    customDialogComponent();
  }

  @Component
  struct customDialogComponent {
    aboutToAppear(): void {
      console.info('测试弹窗打开');
    }

    aboutToDisappear(): void {
      console.info('测试弹窗关闭');
    }

    build() {
      Column({ space: 30 }) {
        Text('弹窗页面')
          .fontColor(Color.White)
          .height('100%')
          .fontSize(30);
      }
      .justifyContent(FlexAlign.Center)
      .alignItems(HorizontalAlign.Center)
      .height(150)
      .width('90%')
      .justifyContent(FlexAlign.SpaceBetween)
      .backgroundColor('rgba(148, 148, 148, 1.00)');
    }
  }
  ```

  实现效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/C8p3alvZS1yAxp9E-KsP4w/zh-cn_image_0000002718888667.png "点击放大")
* 场景二：

  如果想在半模态页面关闭后触发aboutToDisappear()生命周期函数，可以在[closeBindSheet](../harmonyos-references/arkts-apis-uicontext-uicontext.md#closebindsheet12)的异步回调里，调用ComponentContent的[dispose()](../harmonyos-references/js-apis-arkui-componentcontent.md#dispose)方法立即释放当前ComponentContent实例，解除节点之间的绑定关系即可触发aboutToDisappear()生命周期函数。若需再次打开半模态页面，还需重新创建ComponentContent实例。

  修改后代码如下：

  ```ts
  import { FrameNode, ComponentContent } from "@kit.ArkUI";
  import { BusinessError } from '@kit.BasicServicesKit';

  class Params {
    text: string = "";

    constructor(text: string) {
      this.text = text;
    }
  }

  let contentNode: ComponentContent<Params>;
  let gUIContext: UIContext;

  @Builder
  function buildText() {
    buildTextComponent()
  }

  @Component
  struct buildTextComponent {
    aboutToAppear(): void {
      console.info('测试半模态打开')
    }

    aboutToDisappear(): void {
      console.info('测试半模态关闭')
    }

    build() {
      Column() {
        Text('')
        Button('Update BindSheet')
          .fontSize(20)
          .onClick(() => {
            gUIContext.updateBindSheet(contentNode, {
              backgroundColor: Color.Pink,
            }, true)
              .then(() => {
                console.info('updateBindSheet success');
              })
              .catch((err: BusinessError) => {
                console.error(`updateBindSheet error: ${err.code} ${err.message}`);
              })
          })

        Button('Close BindSheet')
          .fontSize(20)
          .onClick(() => {
            gUIContext.closeBindSheet(contentNode)
              .then(() => {
                console.info('closeBindSheet success');
                // 关闭后调用dispose释放ComponentContent，触发aboutToDisappear
                contentNode.dispose();
                // 重新创建ComponentContent以备下次打开
                contentNode = new ComponentContent(gUIContext, wrapBuilder(buildText));
              })
              .catch((err: BusinessError) => {
                console.error(`closeBindSheet error: ${err.code} ${err.message}`);
              })
          })
      }
    }
  }

  @Entry
  @Component
  struct UIContextBindSheet {
    @State message: string = 'BindSheet';

    aboutToAppear() {
      gUIContext = this.getUIContext();
      contentNode = new ComponentContent(this.getUIContext(), wrapBuilder(buildText));
    }

    build() {
      RelativeContainer() {
        Column() {
          Button('Open BindSheet')
            .fontSize(20)
            .onClick(() => {
              let uiContext = this.getUIContext();
              let uniqueId = this.getUniqueId();
              let frameNode: FrameNode | null = uiContext.getFrameNodeByUniqueId(uniqueId);
              let targetId = frameNode?.getFirstChild()?.getUniqueId();
              uiContext.openBindSheet(contentNode, {
                height: SheetSize.MEDIUM,
                backgroundColor: Color.Green,
                title: { title: "Title", subtitle: "subtitle" }
              }, targetId)
                .then(() => {
                  console.info('openBindSheet success');
                })
                .catch((err: BusinessError) => {
                  console.error(`openBindSheet error: ${err.code} ${err.message}`);
                })
            })
        }
      }
      .height('100%')
      .width('100%')
    }
  }
  ```
