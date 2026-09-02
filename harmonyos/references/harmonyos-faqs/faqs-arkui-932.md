---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-932
title: 被动获焦场景下，如何控制RichEditor不拉起软键盘
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 被动获焦场景下，如何控制RichEditor不拉起软键盘
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:22+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cbc52b86d2aa55ed9ad4714a3b7ccfa6b2b139c401c4cd3ebc1361e7f0e77674
---

## 问题现象

有一个UI，上方为Text，Text有bindMenu，点击会弹出Menu；下方为RichEditor，点击会弹出键盘。当RichEditor中处理输入态时、键盘处于弹出状态，点击Text弹出Menu，RichEditor中失焦、键盘消失。Menu消失后，RichEditor又获焦，键盘又弹出，怎样让键盘不再弹出？

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/-Kl-5b2ASYGxvRKth2dWTg/zh-cn_image_0000002658799613.gif "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/qNplX4J_RRCCBHenZ_RofQ/zh-cn_image_0000002628560254.gif "点击放大")

## 背景知识

* [焦点控制](../harmonyos-references/ts-universal-attributes-focus.md)：自定义组件的走焦效果，可设置组件是否走焦和具体的走焦顺序。
* [焦点事件](../harmonyos-references/ts-universal-focus-event.md)：焦点事件指页面焦点在可获焦组件间移动时触发的事件，组件可使用焦点事件来处理相关逻辑。
* [requestFocus](../harmonyos-references/ts-universal-attributes-focus.md#requestfocus9)：方法语句中可使用的全局接口，调用此接口可以主动让焦点在下一帧渲染时转移至参数指定的组件上。
* [enableKeyboardOnFocus](../harmonyos-references/ts-basic-components-richeditor.md#enablekeyboardonfocus12)：设置RichEditor通过点击以外的方式获焦时，是否主动拉起软键盘。

## 解决方案

* **方案一**：使用enableKeyboardOnFocus属性设置RichEditor通过点击以外的方式获焦时，不拉起软键盘（推荐方案）。

  ```ts
  @Entry
  @Component
  struct Index {
    message: string = 'Operation';
    controller: RichEditorController = new RichEditorController();
    options: RichEditorOptions = { controller: this.controller };

    build() {
      Column() {
        Text(this.message)
          .fontSize($r('app.float.page_text_font_size'))
          .fontWeight(FontWeight.Bold)
          .margin({ top: 20, bottom: 20 })
          .bindMenu(this.MyMenu)
          .id('TextComponent')

        RichEditor(this.options)
          .height(200)
          .borderWidth(2)
          .borderColor(Color.Black)
          .width('99%')
          .margin({ top: 20, bottom: 20 })
          .enableKeyboardOnFocus(false)
          .onReady(() => {
            this.controller.addTextSpan('创建RichEditor组件。', {
              style: {
                fontColor: Color.Black,
                fontSize: 15
              }
            });
          })
      }
      .height('100%')
      .width('100%')
    }

    @Builder
    MyMenu() {
      Menu() {
        MenuItem({ content: '复制', labelInfo: 'Ctrl+C' });
        MenuItem({ content: '粘贴', labelInfo: 'Ctrl+V' });
      }
    }
  }
  ```
* **方案二**：使用onFocus、onBlur、onClick组合事件，定义变量richEditorClick属性，业务逻辑为：onClick事件中设置richEditorClick为true，onBlur事件中设置richEditorClick为false，onFocus事件中根据richEditorClick值判断是否清除焦点。

  ```ts
  @Entry
  @Component
  struct Scene2 {
    message: string = 'Operation';
    @State richEditorClick: boolean = false;
    controller: RichEditorController = new RichEditorController();
    options: RichEditorOptions = { controller: this.controller };

    build() {
      Column() {
        Text(this.message)
          .fontSize($r('app.float.page_text_font_size'))
          .fontWeight(FontWeight.Bold)
          .margin({top: 20, bottom: 20})
          .bindMenu(this.MyMenu)
          .id('Operation')

        RichEditor(this.options)
          .height(200)
          .borderWidth(2)
          .borderColor(Color.Black)
          .width('99%')
          .margin({top: 20, bottom: 20})
          .onFocus(() => {
            console.info(`RichEditor focus`);
            if (!this.richEditorClick) {
              this.getUIContext().getFocusController().clearFocus();
              // 部分组件可以使用该方法，如：Button组件支持，Text组件不支持
            }
          })
          .onBlur(() => {
            console.info(`RichEditor blur`);
            this.richEditorClick = false;
          })
          .onClick(() => {
            console.info(`RichEditor click`);
            this.richEditorClick = true;
          })
          .onReady(() => {
            this.controller.addTextSpan('创建RichEditor组件。', {
              style: {
                fontColor: Color.Black,
                fontSize: 15
              }
            });
          })
      }
      .height('100%')
      .width('100%')
    }

    @Builder
    MyMenu() {
      Menu() {
        MenuItem({ content: '复制', labelInfo: 'Ctrl+C' });
        MenuItem({ content: '粘贴', labelInfo: 'Ctrl+V' });
      }
    }
  }
  ```
* **方案三**：在其他组件失焦时，主动选择一个组件作为焦点组件（使用requestFocus接口）。

  ```ts
  @Entry
  @Component
  struct Scene3 {
    message: string = 'Operation';
    controller: RichEditorController = new RichEditorController();
    options: RichEditorOptions = { controller: this.controller };

    build() {
      Column() {
        Button(this.message)
          .fontSize($r('app.float.page_text_font_size'))
          .fontWeight(FontWeight.Bold)
          .margin({top: 20, bottom: 20})
          .bindMenu(this.MyMenu)
          .id('Operation')

        RichEditor(this.options)
          .height(200)
          .borderWidth(2)
          .borderColor(Color.Black)
          .width('99%')
          .margin({top: 20, bottom: 20})
          .onReady(() => {
            this.controller.addTextSpan('创建RichEditor组件。', {
              style: {
                fontColor: Color.Black,
                fontSize: 15
              }
            });
          })
      }
      .height('100%')
      .width('100%')
    }

    @Builder
    MyMenu() {
      Menu() {
        MenuItem({ content: '复制', labelInfo: 'Ctrl+C' })
        MenuItem({ content: '粘贴', labelInfo: 'Ctrl+V' })
      }
      .onBlur(() => {
        // 部分组件可以使用该方法，如：Button组件支持，Text组件不支持
        this.getUIContext().getFocusController().requestFocus('Operation');
      })
    }
  }
  ```

## 常见FAQ

Q：为什么不能通过设置[defaultFocus](../harmonyos-references/ts-universal-attributes-focus.md#defaultfocus9)属性为false，在其他组件失焦时，使RichEditor组件不再获取焦点？

A：defaultFocus仅在初次创建的页面第一次进入时生效。

## 总结

RichEditor组件获焦时软键盘不主动弹起，有以下方式：

* 目标组件不获焦，其他组件失焦后，主动选择一个组件获焦。
* 通过[onFocus](../harmonyos-references/ts-universal-focus-event.md#onfocus)/[onBlur](../harmonyos-references/ts-universal-focus-event.md#onblur)组合，被动获焦时清除焦点或将焦点转移到其他组件。
* 设置被动获焦后不主动拉起软键盘，如通过enableKeyboardOnFocus属性设置RichEditor组件点击以外的方式获焦时，不拉起软键盘。
