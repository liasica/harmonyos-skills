---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-784
title: attach设置软键盘属性inputAttribute不生效
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > attach设置软键盘属性inputAttribute不生效
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:03+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:07a75d1b6ec224f9635d544fa6dde03a44573ec41c26ddd7f0e8758681a59399
---

## 问题现象

inputAttribute属性用于设置enter键的功能类型，enterKeyType:5表示"下一步"。TextInput使用attach方法唤起的软键盘，设置的inputAttribute属性初次生效，enter键的功能为"下一步"，关闭键盘后再拉起键盘，inputAttribute属性失效，enter键的功能为"完成"。

问题代码示例参考如下：

```screen
onFocus(() => {
  let textConfig: inputMethod.TextConfig = {
    inputAttribute: {
      textInputType: 0,
      enterKeyType: 5
    }
  };
  let inputMethodController = inputMethod.getController()
  inputMethodController.attach(true, textConfig, () => {
  });
})
```

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/fT21AMxITBWIHP2sOIpAaw/zh-cn_image_0000002658916947.gif "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/_TRTnWHNTN-bvrgtezPGmg/zh-cn_image_0000002628397738.gif "点击放大")

## 背景知识

* [attach](../harmonyos-references/js-apis-inputmethod.md#attach10)：自绘控件绑定输入法。使用callback异步回调。
* [updateAttribute](../harmonyos-references/js-apis-inputmethod.md#updateattribute10)：更新编辑框属性信息。使用callback异步回调。当编辑框属性信息更新成功时，err为undefined；否则为错误对象。

## 解决方案

使用updateAttribute方法设置inputAttribute属性。

```screen
import { inputMethod } from '@kit.IMEKit';

@Entry
@Component
struct CustomPopup {
  @State message: string = '';

  build() {
    Column() {
      TextInput({ text: this.message, placeholder: '请输入正确内容' })
        .onChange((value: string) => {
          this.message = value;
        })
        .focusable(true)
        .margin({ top: 100, left: 10, right: 10 })
        .onFocus(() => {
          let inputAttribute: inputMethod.InputAttribute = { textInputType: 0, enterKeyType: 5 };
          let inputMethodController = inputMethod.getController();
          inputMethodController.updateAttribute(inputAttribute, () => {
          });
        });
    }
    .width('100%')
    .height('100%');
  }
}
```
