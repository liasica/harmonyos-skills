---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-869
title: 搜索建议需要点击两次才会消失
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 搜索建议需要点击两次才会消失
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:04+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ac9f0cddae467856ef51e52664601fbddf206fc5fb26b23194f4d07252181a52
---

## 问题现象

在搜索框组件中，当用户输入内容触发搜索建议时，下拉列表需要点击两次才会消失。正常情况下，点击一次即可关闭下拉列表。该问题导致用户体验不一致，且不符合常规交互预期。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/3GwFiTBkSXq5BUYBnT95rA/zh-cn_image_0000002658798187.png "点击放大")

## 背景知识

* [onClick](../harmonyos-references/ts-universal-events-click.md#onclick12)点击动作触发该回调。
* [TextInput](../harmonyos-references/ts-basic-components-textinput.md)单行文本输入框组件。

## 问题定位

检查搜索建议点击事件回调函数，确认回调函数是否通过代码逻辑区分自动填充与手动输入，一般可通过标志位进行区分，标志位是一个变量，用于标记程序的某种状态或条件，控制代码的执行逻辑。比如在下方代码中，注释位置未使用标志位来区分自动填充与手动输入。

```ts
List() {
  ForEach(this.filteredSuggestions, (item: string) => {
    ListItem() {
      Text(item)
        .width('100%')
        .height(50)
        .fontSize(18)
        .textAlign(TextAlign.Start)
        .padding({ left: 15 })
    }
    .onClick(() => {
       // 未设置标志位，表示本次填充为自动填充
      this.controller.deleteText();
      this.controller.addText(item);
      this.controller.caretPosition(item.length);
    })
  }, (item: string) => item)
}
.width('90%')
.border({ width: 1, color: '#e0e0e0' })
.borderRadius(8)
.shadow({ radius: 6, color: '#20000000', offsetX: 2, offsetY: 4 })
.margin({ top: 5 })
```

## 分析结论

点击搜索建议，自动填充进搜索框后，仍将该自动填充判断为用户输入，再次对该输入进行了匹配搜索，因此展示了同样的搜索建议。

## 修改建议

在点击搜索建议后，在注释位置设置标志位，表示本次填充为自动填充：

```ts
@Entry
@Component
struct Input {
  private controller: TextInputController = new TextInputController();
  @State inputText: string = '';
  @State filteredSuggestions: string[] = [];
  @State showSuggestions: boolean = false;
  private isProgrammaticChange: boolean = false;

  private suggestions: string[] = ['Apple', 'Banana', 'Cherry'];

  build() {
    Column() {
      TextInput({ controller: this.controller , placeholder:'请输入水果名称'})
        .width('90%')
        .height(40)
        .onChange((value: string) => {
          if (this.isProgrammaticChange) {
            this.isProgrammaticChange = false;
            return;
          }

          this.inputText = value;
          if (value.length > 0) {
            this.filterSuggestions();
          } else {
            this.showSuggestions = false;
          }
        })

      if (this.showSuggestions && this.filteredSuggestions.length > 0) {
        List() {
          ForEach(this.filteredSuggestions, (item: string) => {
            ListItem() {
              Text(item)
                .fontSize(16)
                .padding(10)
            }
            .onClick(() => {
              this.isProgrammaticChange = true;
              this.controller.deleteText();
              this.controller.addText(item);
              this.controller.caretPosition(item.length);
              this.showSuggestions = false;
            })
          })
        }
        .width('90%')
        .border({ width: 1, color: '#ccc' })
        .backgroundColor(Color.White)
      }
    }
    .width('100%')
    .padding(20)
  }

  private filterSuggestions() {
    const input = this.inputText.toLowerCase();
    this.filteredSuggestions = this.suggestions.filter(item =>
    item.toLowerCase().startsWith(input)
    );
    this.showSuggestions = this.filteredSuggestions.length > 0;
  }
}
```
