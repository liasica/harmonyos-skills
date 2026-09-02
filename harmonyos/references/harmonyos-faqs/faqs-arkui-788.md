---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-788
title: 设置密码时，可输入的长度与提示长度不符
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 设置密码时，可输入的长度与提示长度不符
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:03+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cfc727377da1394bcdce5a3d4ad49c9a0e48b0df8c77318d87fb10b120c30c85
---

## 问题现象

设置密码时提示6~20位，但是实际在输入11位后就无法继续输入了。

## 背景知识

* [maxLength](../harmonyos-references/ts-basic-components-textinput.md#maxlength)：设置文本的最大输入字符数。
* [inputFilter](../harmonyos-references/ts-basic-components-textinput.md#inputfilter8)：通过正则表达式设置输入过滤器。匹配表达式的输入允许显示，不匹配的输入将被过滤。仅支持单个字符匹配，不支持字符串匹配。

## 问题定位

1. 定位到登录注册部分，查到输入密码的TextInput。
2. 查看对密码长度的校验规则，找到maxLength关键词是否为提示的最大值。

## 分析结论

maxLength设置的最大值只有11，导致密码最大值与提示的长度不同。

## 修改建议

通过设置maxLength来限制密码长度，并在onChange事件中判断键入的密码长度，小于6位提示用户密码长度过短。可参考以下代码：

```ts
@Entry
@Component
struct TextInputDemo {
  @State password: string = '';
  @State state: boolean = false;

  build() {
    Column({ space: 20 }) {
      Text(`当前输入密码长度：${this.password.length}`);

      TextInput({ text: this.password })
        .width('80%')
        .type(InputType.Password)
        .showPasswordIcon(false)
        .inputFilter('[0-9A-Za-z]')
        .maxLength(20)
        .onChange((v) => {
          this.password = v;
          console.info(`输入字符为：${this.password},长度：${this.password.length}`);
          if (this.password.length >= 6) {
            this.state = true;
          } else {
            this.state = false;
          }
        });

      if (!this.state) {
        Text('请输入6-20位密码，包含大小写字母和数字')
          .fontColor(Color.Red);
      }
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%');
  }
}
```
