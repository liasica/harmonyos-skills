---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1345
title: 登录页面手机号输入长度不对仍然可以点击登录
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 登录页面手机号输入长度不对仍然可以点击登录
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:08+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b93655b6abe06dd273873a19d0c93dd8251c25526227e7a22086ccd13b8b1ebd
---

## 问题现象

在应用登录页面，输入大于11位的手机号，仍然可以点击登录。

## 背景知识

[TextInput](../harmonyos-references/ts-basic-components-textinput.md)：单行文本输入框组件，用于用户输入。

## 问题定位

通过UIViewer查看页面布局，手机号输入框采用TextInput组件，最多可以输入15位长度，而不是手机号的标准长度11位，还可以输入“+”、“-”符号，说明没有对输入框做长度限制。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/1dmQwaorScKFDq4TAyFcEw/zh-cn_image_0000002628601516.png "点击放大")

## 分析结论

为了允许用户可以输入区号例如“+86-”，开发者设置的文本输入最大长度与标准手机号的长度不一致。

## 修改建议

* 将区号和手机号分开输入，避免造成用户误解；
* 通过TextInput组件的[type](../harmonyos-references/ts-basic-components-textinput.md#type)和[maxLength](../harmonyos-references/ts-basic-components-textinput.md#maxlength)来限制手机号输入格式。示例代码如下：

  ```screen
  const MAX_LENGTH: number = 11;

  @Entry
  @Component
  struct PasswordInput {
    @State phoneNumber: string = '';

    build() {
      Column() {
        TextInput({
          placeholder: '请输入手机号码'
        })
          .type(InputType.PhoneNumber)
          .maxLength(MAX_LENGTH)
          .onChange((data) => {
            this.phoneNumber = data;
          })
          .width('70%');
      }
      .justifyContent(FlexAlign.Center)
      .height('100%')
      .width('100%');
    }
  }
  ```
