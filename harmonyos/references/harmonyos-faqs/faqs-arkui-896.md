---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-896
title: 如何解决切换输入框导致输入法重复拉起问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决切换输入框导致输入法重复拉起问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:05+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f568364aafcda0670e2a62ec3b6488ea0bb16c79763b4eafbb9aec379e9d81f2
---

## 问题现象

在面对多组输入框场景时如用户名、密码、验证码，点击输入法键盘上的下一步跳转至下一个输入框，输入法会先隐藏再弹起，影响使用体验，如何解决该问题？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/bBcbj2tITSOrJcPl_HOkPQ/zh-cn_image_0000002658918871.png "点击放大")

## 背景知识

TextInput中，按下输入法回车键会触发[onSubmit()](../harmonyos-references/ts-basic-components-textinput.md#onsubmit)回调。onSubmit()回调函数一共有两个入参：[EnterKeyType](../harmonyos-references/ts-basic-components-textinput.md#enterkeytype枚举说明)和[SubmitEvent](../harmonyos-references/ts-basic-components-textinput.md#submitevent11)。其中EnterKeyType决定回车键的类型如next、done等，SubmitEvent则是用户提交事件，只有[keepEditableState()](../harmonyos-references/ts-basic-components-textinput.md#keepeditablestate11)方法。

## 问题定位

1. 查看是否调用了focusControl.requestFocus方法导致TextInput组件失焦。
2. 查看是否调用了keepEditableState()方法避免输入法键盘关闭。

## 分析结论

输入法隐藏再弹起是因为执行[focusControl.requestFocus](../harmonyos-references/ts-universal-attributes-focus.md#requestfocus9)方法时焦点转移到其他组件产生暂时失焦。

## 修改建议

* 通过给TextInput组件的onSubmit()方法里添加可选入参SubmitEvent，并在onSubmit()中添加SubmitEvent.keepEditableState()方法，可以阻止输入法在失焦情况下关闭，实现输入法键盘在切换编辑栏时保持状态不关闭。
* 但是遇到最后一个输入框时使用keepEditableState()方法会导致输入法键盘无法通过回车键关闭。所以可在该方法外面嵌套一层对于EnterKeyType判断，若EnterKeyType为next则执行keepEditableState()方法，若EnterKeyType为done则不执行。

```screen
@Entry
@Component
struct TextInputExample {
  private keyNo: number = 1;

  build() {
    Column({ space: 10 }) {
      TextInput({ placeholder: 'please input' })
        .id('code1')
        .enterKeyType(EnterKeyType.Next)
        .onSubmit((enterKey: EnterKeyType, event: SubmitEvent) => {
          let nextKeyNo: number = this.keyNo + 1;
          let nextKeyStr: string = 'code' + nextKeyNo;
          this.getUIContext()
            .getFocusController()
            .requestFocus(nextKeyStr); // focusControl.requestFocus()调用此接口可以主动让焦点转移至指定id的组件
          if (enterKey == EnterKeyType.Next) {
            event.keepEditableState(); // 如果回车键类型为Next则保持输入框不隐藏
          };
        })
      TextInput({ placeholder: 'please input' })
        .id('code2')
        .enterKeyType(EnterKeyType.Next)
        .onSubmit((enterKey: EnterKeyType, event: SubmitEvent) => {
          let nextKeyNo: number = this.keyNo + 2;
          let nextKeyStr: string = 'code' + nextKeyNo;
          this.getUIContext()
            .getFocusController()
            .requestFocus(nextKeyStr); // focusControl.requestFocus()调用此接口可以主动让焦点转移至指定id的组件
          if (enterKey == EnterKeyType.Next) {
            event.keepEditableState(); // 如果回车键类型为Next则保持输入框不隐藏
          };
        })
      TextInput({ placeholder: 'please input' })
        .id('code3')
        .enterKeyType(EnterKeyType.Next)
        .onSubmit((enterKey: EnterKeyType, event: SubmitEvent) => {
          if (enterKey == EnterKeyType.Next) {
            event.keepEditableState(); // 如果回车键类型为Next则保持输入框不隐藏
          };
        })
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
    .padding(15)
  }
}
```
