---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1501
title: 输入框组件自动获焦问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 输入框组件自动获焦问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7415fcf4e46d2dab8993c096405dc49a970cc6d2931caf2d6d53733220b68acc
---

## 问题现象

输入框组件在获焦时会弹出软键盘，这时可以优化操作路径，使得用户可以快速输入，但也有可能干扰用户操作，被跳焦打断体验。如何控制输入框组件是否自动获焦以适应不同场景？

## 背景知识

* [defaultFocus](../harmonyos-references/ts-universal-attributes-focus.md#defaultfocus9)：可以设置当前组件是否为当前层级页面上的默认焦点。
* [requestFocus](../harmonyos-references/ts-universal-attributes-focus.md#requestfocus9)：调用此接口可以主动让焦点在下一帧渲染时转移至参数指定的组件上。
* [clearFocus](../harmonyos-references/arkts-apis-uicontext-focuscontroller.md#clearfocus12)：清除焦点，将焦点强制转移到页面根容器节点，焦点链路上其他节点失焦。
* [visibility](../harmonyos-references/ts-universal-attributes-visibility.md#visibility)：控制组件的显示或隐藏。当未设置visibility时，组件默认为显示。

## 解决方案

* 场景一：defaultFocus属性仅在组件初次创建且页面首次进入时生效。因此适用场景是当弹窗弹出或者页面跳转时，通过defaultFocus属性使弹窗或新页面中的输入框组件成为默认焦点。

  ```screen
  @CustomDialog
  @Component
  struct CustomDialogForSolutionOne {
    @Link textValue: string;
    controller?: CustomDialogController;

    build() {
      Column({ space: 20 }) {
        Text('自定义弹窗').fontSize(20);
        TextInput({ placeholder: '', text: this.textValue })
          .height(50)
          .width('90%')
          .onChange((value: string) => {
            this.textValue = value;
          })
            // 弹窗显示时通过defaultFocus设置默认焦点
          .defaultFocus(true);
      }
      .justifyContent(FlexAlign.Center)
      .borderRadius(20)
      .padding(16)
      .backgroundColor(Color.White);
    }
  }

  @Entry
  @Component
  struct CustomDialogDemo {
    @State textValue: string = '';
    solutionOneController: CustomDialogController | null = new CustomDialogController({
      builder: CustomDialogForSolutionOne({
        textValue: this.textValue,
      }),
      autoCancel: true,
      alignment: DialogAlignment.Bottom,
      customStyle: true,
    });

    // 在自定义组件即将析构销毁时将dialogController置空
    aboutToDisappear() {
      // 将dialogController置空
      this.solutionOneController = null;
    }

    build() {
      Column({ space: 20 }) {
        Button('defaultFocus默认焦点')
          .backgroundColor('#0A59F7')
          .type(ButtonType.ROUNDED_RECTANGLE)
          .onClick(() => {
            if (this.solutionOneController != null) {
              this.solutionOneController.open();
            }
          });
      }
      .justifyContent(FlexAlign.Center)
      .height('100%')
      .width('100%');
    }
  }
  ```

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/531aO5ffSDi1Ana8rDtUKg/zh-cn_image_0000002628766424.png "点击放大")
* 场景二：当输入框通过动态渲染的方式出现在当前弹窗或者页面中时，无法通过设置defaultFocus使成默认焦点，这时可以通过调用requestFocus方法将焦点转移至输入框上。例如，在当前页面中通过visibility属性使输入框出现时，需要通过requestFocus方法使输入框组件获焦。

  ```screen
  @Entry
  @Component
  struct SearchFocus {
    @State @Watch('search') flag: boolean = false;
    @State changeValue: string = '';
    @State submitValue: string = '';
    @State backColor: string | Color = '';
    @State isFocus: string = '';

    search() {
      console.info(`flag: ${this.flag}`);
      try {
        focusControl.requestFocus('search');
      } catch (error) {
        console.error(`error: ${error}`);
      }
    }

    build() {
      Column({ space: 15 }) {
        Row() {
          SearchComponent({
            changeValue: this.changeValue,
            submitValue: this.submitValue,
            backColor: this.backColor,
            isFocus: this.isFocus
          })
            .visibility(this.flag ? Visibility.Visible : Visibility.Hidden);
        }
        .width('100%')
        .height(80)
        .justifyContent(FlexAlign.Center);

        Text(this.isFocus);
        Row() {
          Button('打开search')
            .onClick(() => {
              this.flag = true;
            });
          Button('关闭search')
            .onClick(() => {
              this.flag = false;
              this.getUIContext().getFocusController().clearFocus();
            });
        }
        .width('100%')
        .justifyContent(FlexAlign.SpaceAround);
      }
      .width('100%')
      .height('100%');
    }
  }

  @Component
  struct SearchComponent {
    @Link changeValue: string;
    @Link submitValue: string;
    @Link backColor: string | Color;
    @Link isFocus: string;

    build() {
      Search({ placeholder: '请输入' })
        .searchButton('搜索')
        .width('90%')
        .height(40)
        .backgroundColor(this.backColor)
        .placeholderColor('#ccc')
        .onSubmit((value: string) => {
          this.submitValue = value;
        })
        .onChange((value) => {
          this.changeValue = value;
        })
        .onFocus(() => {
          this.backColor = '#f1f3f5';
          this.isFocus = '已获焦';
          console.info(`onFocus已获焦`);
        })
        .onBlur(() => {
          this.backColor = Color.Blue;
          this.isFocus = '未获焦';
          console.info(`onBlur未获焦`);
        })
        .id('search')
        .margin(20);
    }
  }
  ```

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/hxL9pJVMQ6agyv19A8bpdA/zh-cn_image_0000002658965759.png "点击放大")
* 场景三：为防止自动获焦导致打断用户体验，可以通过clearFocus方法清除焦点。例如：在页面中的TextInput获焦时打开一个弹窗，此时焦点会转移到弹窗上，弹窗关闭时，焦点会尝试转移到上一个获取焦点的组件（即TextInput），导致软键盘再次弹出。为避免这种跳焦效果，可以在点击弹窗按钮时调用clearFocus方法清除焦点。

  关闭弹窗后的跳焦现象：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/dHGlVFCZQ0OdfuskiDKYag/zh-cn_image_0000002628606548.png "点击放大")

  ```screen
  @Entry
  @Component
  struct TextInputFocusExample {
    controller: TextInputController = new TextInputController();
    dialogController: CustomDialogController = new CustomDialogController({
      builder: CustomDialogFocusExample({
        cancel: () => {
          this.onCancel();
        },
        confirm: () => {
          this.onAccept();
        },
      }),
    });

    onCancel() {
    }

    onAccept() {
    }

    build() {
      Column() {
        TextInput({ placeholder: '请输入用户名', controller: this.controller })
          .height(40)
          .margin(20)
          .fontSize(14)
          .width('90%')
          .onFocus(() => {
            console.info('TextInput获焦');
          })
          .onBlur(() => {
            console.info('TextInput失焦');
          });
        Button('弹出Dialog')
          .backgroundColor('#0a59f7')
          .id('Button')
          .onClick(() => {
            try {
              this.getUIContext().getFocusController().clearFocus();
            } catch (error) {
              console.error(`error: ${error}`);
            }
            this.dialogController.open();
          })
          .width('30%');
      }
      .width('100%')
      .height('100%');
    }
  }

  @CustomDialog
  struct CustomDialogFocusExample {
    cancel?: () => void;
    confirm?: () => void;
    controller: CustomDialogController;

    build() {
      Column() {
        Text('我是内容').fontSize(20).margin({ top: 10, bottom: 10 });
        Flex({ justifyContent: FlexAlign.SpaceAround }) {
          Button('关闭')
            .onClick(() => {
              this.controller.close();
              if (this.cancel) {
                this.cancel();
              }
            })
            .backgroundColor(Color.White)
            .fontColor(Color.Black);
          Button('确定')
            .onClick(() => {
              this.controller.close();
              if (this.confirm) {
                this.confirm();
              }
            })
            .backgroundColor('#0a59f7')
            .fontColor(Color.White);
        }
        .margin({ bottom: 10 });
      };
    }
  }
  ```

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/eAdHfhr8R_2Ozf4OxaUEJw/zh-cn_image_0000002658845797.png "点击放大")
