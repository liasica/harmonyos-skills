---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1200
title: 如何解决点击Select下拉菜单会导致TextInput失焦的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决点击Select下拉菜单会导致TextInput失焦的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:07+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:21eee18a2dd4e9b485aa909d9154ce3355fd1f926adfdbea75f297db1f870383
---

## 问题现象

TextInput获焦时点击Select弹出菜单选项，此时TextInput会失焦，导致软键盘收起，希望弹出菜单选项时TextInput不会失焦，如何实现？

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/-5yS45Q4RRubfsIgLLWyYw/zh-cn_image_0000002658832829.png "点击放大")

问题代码示例如下：

```ts
@Entry
@Component
struct SelectExample {
  @State text: string = 'Select';
  @State value: string = '';
  @State index: number = 2;
  controller: TextInputController = new TextInputController();

  build() {
    Column() {
      Blank().layoutWeight(1).width('100%');
      Row({ space: 16 }) {
        Select([{ value: '选项1' },
          { value: '选项2' },
          { value: '选项3' }])
          .selected(this.index)
          .value(this.text)
          .font({ size: 16, weight: 500 })
          .fontColor('#182431')
          .onSelect((index: number, text?: string | undefined) => {
            this.index = index;
            if (text) {
              this.text = text;
            }
          })
          .avoidance(AvoidanceMode.COVER_TARGET)
          .onFocus(() => {
            console.info(`Select获焦`);
          })
          .onBlur(() => {
            console.info(`Select失焦`);
          });

        TextInput({ text: this.value!!, placeholder: 'input your word...', controller: this.controller })
          .placeholderColor(Color.Grey)
          .placeholderFont({ size: 14, weight: 400 })
          .caretColor(Color.Blue)
          .layoutWeight(1)
          .id('TextInput')
          .onFocus(() => {
            console.info(`TextInput获焦`);
          })
          .onBlur(() => {
            console.info(`TextInput失焦`);
          })
          .inputFilter('[a-z]', (e) => {
            console.info(JSON.stringify(e));
          });
      }
      .padding({ left: 16, right: 16 })
      .width('100%');
    };
  }
}
```

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/0u1GmR2MSJugyB5JzhXhWQ/zh-cn_image_0000002628593588.png "点击放大")

## 背景知识

* [TextInput](../harmonyos-references/ts-basic-components-textinput.md)是单行文本输入框组件，当TextInput获焦时，会弹出软键盘并显示编辑光标。
* [Select](../harmonyos-references/ts-basic-components-select.md)提供下拉选择菜单。
* 组件获焦时会触发[onFocus](../harmonyos-references/ts-universal-focus-event.md#onfocus)回调，失焦时会触发[onBlur](../harmonyos-references/ts-universal-focus-event.md#onblur)回调。

## 问题定位

运行时发现在TextInput获焦时点击Select，TextInput会触发onBlur事件，但Select不会触发onFocus事件。

## 分析结论

上述运行结果说明焦点并没有从TextInput组件转移到Select组件上，而Select弹出的菜单选项相当于一个弹窗，焦点是从页面转移到了菜单弹窗上。

## 修改建议

自定义一个完全属于页面这个层级的自定义Select，防止焦点转移到弹窗这个层级，导致TextInput失焦。

```ts
@Entry
@Component
struct SelectExample {
  @State text: string = 'Select';
  controller: TextInputController = new TextInputController();
  @State selectVisibility: Visibility = Visibility.None;

  build() {
    Column() {
      Blank().layoutWeight(1).width('100%');

      Column() {
        Row() {
          Text('选项1');
        }
        .justifyContent(FlexAlign.Start)
        .width(120)
        .onClick(() => {
          this.text = '选项1';
        });

        Blank().height(5);
        Divider().width(120).color(Color.Black);
        Blank().height(5);

        Row() {
          Text('选项2');
        }
        .justifyContent(FlexAlign.Start)
        .width(120)
        .onClick(() => {
          this.text = '选项2';
        });

        Blank().height(5);
        Divider().width(120).color(Color.Black);
        Blank().height(5);

        Row() {
          Text('选项3');
        }
        .justifyContent(FlexAlign.Start)
        .width(120)
        .onClick(() => {
          this.text = '选项3';
        });

        Blank().height(5);
      }
      .shadow({
        radius: 60,
        color: 'rgba(0, 0, 0, 0.2)',
        offsetX: 0,
        offsetY: 0
      })
      .padding(5)
      .borderRadius(20)
      .width(150)
      .margin({ left: 16 })
      .visibility(this.selectVisibility);

      Blank().height(5);

      Row({ space: 16 }) {
        Blank().width(0);
        Row() {
          Text(this.text);
          Text('▼');
        }
        .borderRadius(20)
        .backgroundColor('#F1F3F5')
        .height(40)
        .width(80)
        .justifyContent(FlexAlign.SpaceEvenly)
        .onClick(() => {
          if (this.selectVisibility === Visibility.None) {
            this.selectVisibility = Visibility.Visible;
          } else if (this.selectVisibility === Visibility.Visible) {
            this.selectVisibility = Visibility.None;
          }
        });

        TextInput({ placeholder: 'input your word...', controller: this.controller })
          .placeholderColor(Color.Grey)
          .placeholderFont({ size: 14, weight: 400 })
          .caretColor(Color.Blue)
          .layoutWeight(1)
          .id('TextInput')
          .inputFilter('[a-z]', (e) => {
            console.info(JSON.stringify(e));
          })
          .onFocus(() => {
            console.info(`TextInput获焦`);
          })
          .onBlur(() => {
            console.info(`TextInput失焦`);
          });
        Blank().width(0);
      }.width('100%');
    }
    .alignItems(HorizontalAlign.Start);
  }
}
```
