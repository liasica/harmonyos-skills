---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/passwordvault-quick-adaptation
title: 快速适配
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6f26f03f652c1034b89307a643d6f4e8de432087c35cd062ccf2b5a8f687b75d
---

密码自动填充服务依托ArkUI [TextInput 组件](../harmonyos-references/ts-basic-components-textinput.md)为开发者提供的一系列登录场景相关控件，密码保险箱帮助开发者快速集成自动填充等功能，仅需在界面上使用ArkUI标准控件，开发者即可通过密码保险箱的便捷登录，让用户快速上手应用功能。

## 约束与限制

应用需要使用ArkUI组件[TextInput](../harmonyos-references/ts-basic-components-textinput.md)作为输入框，并指定输入框类型（InputType），才能使用系统密码自动填充服务。不同输入框类型与使用场景的对应关系如下表所示。

**表1** 输入框类型说明

| InputType名称 | 描述 | 使用场景 |
| --- | --- | --- |
| USER\_NAME | 用户名输入模式。 | 用于登录、注册等场景的用户名输入。 |
| Password | 密码输入模式。支持输入数字、字母、下划线、空格、特殊字符。  密码显示小眼睛图标并且默认会将文字变成圆点。 | 用于登录、注册等场景的密码输入。 |
| NUMBER\_PASSWORD | 数字密码输入模式。仅支持输入数字。  密码显示小眼睛图标并且默认会将文字变成圆点。 | 用于登录、注册等场景的密码输入。 |
| NEW\_PASSWORD | 新密码输入模式。 | 用于注册、修改密码等场景的新密码输入。 |

说明

本文档中类型描述为Password的类型，均可用NUMBER\_PASSWORD类型替代。

## 快速适配指导

当应用具备账号密码登录的场景时，只需要将充当用户名的TextInput输入框的type属性设置为InputType.USER\_NAME，将密码TextInput输入框的type属性设置为InputType.Password，即可使用密码保险箱的填充和保存功能。

在应用的账号密码注册页除设置用户名输入框外，将新密码TextInput输入框的type属性设置为InputType.NEW\_PASSWORD，即可使用强密码填充功能。如果应用对密码强度有特殊要求，根据[为应用添加自动生成高强度密码的建议](passwordvault-custom-strong-password-rules.md)适配即可。

代码示例：

```
1. TextInput({ placeholder: '用户名' })
2. .opacity(0.6)
3. .type(InputType.USER_NAME)
4. .placeholderColor(0x182431)
5. .width('100%')
6. .placeholderFont({ size: 16, weight: FontWeight.Regular })
7. .margin({ top: 32, bottom: 8 })
```
