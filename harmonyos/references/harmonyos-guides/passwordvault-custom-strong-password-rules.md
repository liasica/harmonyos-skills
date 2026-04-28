---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/passwordvault-custom-strong-password-rules
title: 为应用添加自动生成高强度密码的建议
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:08+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:77f8fb31dfa5f9cda4d3070b5a1c28b8a1c42fb011df19cc3b74608f74a5444b
---

在本文档中介绍的强密码特指，在密码保险箱强密码填充场景中，推荐用户使用的较强密码。强密码中一定包含大写字母、小写字母、数字三种字符。且强密码的复杂度高，破解难度大。

当开发者没有指定密码规则，或是开发者指定的规则书写错误、不符合规范时，密码保险箱会根据[默认的规则](passwordvault-custom-strong-password-rules.md#默认强密码规则)生成符合开发者指定条件的强密码。开发者可以在允许的范围内指定强密码的规格，详见[开发者可自定义的强密码规则](passwordvault-custom-strong-password-rules.md#开发者可自定义的强密码规则)。

## 默认强密码规则

当开发者没有指定规则，或是指定的密码规则不符合规范时，将按照以下默认规则生成强密码。

* 以字母开头。
* 包含大小写字母和数字。
* 长度为16位。

## 开发者可自定义的强密码规则

开发者可以设置新密码输入框的passwordRules属性来指定强密码规则。

强密码中一定包含大写字母、小写字母、数字三种字符。开发者可以按照以下指导对强密码规格做一些限定。

强密码规则包含3个属性：

3个属性可以任意选择，书写时顺序不做限制，属性之间以英文“,”进行分隔，每个属性只能出现一次。

说明

各属性段请严格参照介绍进行书写，否则将导致指定规则不生效。

* **"begin"**

  表示生成的强密码首位的字符类型，可选值如下表所示。该字段可缺省，若填写了非下表中的指定值则按默认规则处理。

  | 取值 | 说明 |
  | --- | --- |
  | upper | 以大写字母开头。 |
  | lower | 以小写字母开头。 |
  | digit | 以数字开头。 |
  | 不填 | 不填时，将以任意字母或数字0-9开头。 |

  格式举例：

  ```
  1. begin:[upper]
  ```
* **"special"**

  表示生成的强密码是否可以包含特殊字符。需要包含特殊字符时，请将该字段设置为"yes"；如不需要，不填写"special"字段。

  当设置为"yes"时，生成的强密码中将包含至少一个特殊字符，特殊字符不会出现在强密码的首位。

  强密码中可能出现的特殊字符包括：!@#$%^&\*

  格式举例：

  ```
  1. special:[yes]
  ```
* **"len"**

  表示生成的强密码长度。密码保险箱允许设定的强密码长度最小12位，最大32位。

  强密码长度属性提供三个关键字用于描述长度。

  | 关键字 | 说明 |
  | --- | --- |
  | fixedlen | 固定长度 |
  | minlen | 最小长度 |
  | maxlen | 最大长度 |

  开发者可以根据以下方式指定强密码长度。如果开发者指定的密码长度数值不在有效范围[12, 32]内，将视为非法指定，系统将使用默认长度16位替代。

  1. 仅设置固定长度fixedlen，此时强密码长度为fixedlen设置值。

     ```
     1. len:[fixedlen:16]
     ```
  2. 仅设置最小长度minlen，此时强密码长度随机，最小长度为minlen设置值，最大为默认值32位。

     ```
     1. len:[minlen:15]
     ```
  3. 仅设置最大长度maxlen，此时强密码长度随机，最小长度为默认值12位，最大为maxlen设置值。

     ```
     1. len:[maxlen:28]
     ```
  4. 同时设置最大长度maxlen和最小长度minlen。设置时，minlen的值必须小于maxlen的值。此时强密码长度随机，最小长度为minlen设置值，最大为maxlen设置值。

     ```
     1. len:[minlen:13,maxlen:18]
     ```
  5. 若不指定len属性，强密码长度默认为16位。

### 自定义规则样例说明

正确的规则样例如下：

| 强密码规则样例 | 规则释义 |
| --- | --- |
| begin:[upper],special:[yes],len:[maxlen:32,minlen:12] | 以大写字母开头，包含大小写字母、数字、特殊字符，长度为12-32之间（包含12和32）的随机数值。 |
| begin:[lower],special:[yes],len:[minlen:14] | 以小写字母开头，包含大小写字母、数字、特殊字符，长度为14-32之间（包含14和32）的随机数值。 |
| begin:[digit],special:[yes],len:[fixedlen:15] | 以数字开头，包含大小写字母、数字、特殊字符，长度为15。 |
| begin:[upper] | 以大写字母开头，包含大小写字母、数字，长度为16。 |
| special:[yes] | 以任意字母或数字开头，包含大小写字母、数字、特殊字符，长度为16。 |
| len:[fixedlen:15] | 以任意字母或数字开头，包含大小写字母、数字，长度为15。 |
| begin:[upper],special:[yes] | 以大写字母开头，包含大小写字母、数字、特殊字符,长度为16。 |
| begin:[lower],len:[maxlen:25,minlen:12] | 以小写字母开头，包含大小写字母、数字，长度为12-25之间（包含12和25）的随机数值。 |
| special:[yes],len:[fixedlen:15] | 以任意字母或数字开头，包含大小写字母、数字、特殊字符，长度为15。 |

错误的规则用例如下：

| 强密码规则错误用例 | 错误原因 |
| --- | --- |
| begin:[uppper] | begin属性的取值upper拼写错误。 |
| began:[upper] | begin属性拼写错误。 |
| len:[15] | len属性语法错误，未使用三种长度关键词。 |
| len:[fixedlen:15,maxlen:18] | len属性语法错误，fixedlen与maxlen不可混用。 |
| len:[maxlen:15,minlen:18] | len属性参数值错误，maxlen的取值不能小于minlen。 |

### 示例

```
1. TextInput({ placeholder: '新密码' })
2. .enableAutoFill(true)
3. .type(InputType.NEW_PASSWORD)
4. .passwordRules('begin:[lower],special:[yes],len:[maxlen:32,minlen:12]')
5. .placeholderColor(0x182431)
6. .width('100%')
7. .opacity(0.6)
8. .showPasswordIcon(true)
9. .placeholderFont({ size: 16, weight: FontWeight.Regular })
10. .margin({ bottom: 36 })
```
