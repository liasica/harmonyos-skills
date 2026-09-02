---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1014
title: 如何解决TextInput组件密码模式下图标不能修改的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决TextInput组件密码模式下图标不能修改的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:05+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0849cb0ca8b4a2fb0837709f80920c468b168d40a577192990816d30bec3c032
---

## 问题现象

TextInput密码输入模式（Password）下系统控制密码显隐的PasswordIcon图标的位置、大小、颜色无法更改，而应用某些定制化场景下需要更改PasswordIcon位置、大小、颜色等。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/nsRFbOwTSDqcBXwDCsrkEA/zh-cn_image_0000002658923997.png "点击放大")

## 背景知识

[TextInput](../harmonyos-references/ts-basic-components-textinput.md)为单行文本输入框组件。可以通过[InputType](../harmonyos-references/ts-basic-components-textinput.md#inputtype枚举说明)设置输入框类型，常见的类型有：Normal、Password、Email、Number、PhoneNumber等。在TextInput输入类型为Password时，输入的字符会表现为点（·），在[showPasswordIcon](../harmonyos-references/ts-basic-components-textinput.md#showpasswordicon9)设置为true时，行尾会有一个小眼睛图标，点击可控制密码的显隐。

## 解决方案

当前的规格不支持更改icon图标的大小及位置，许多APP均是使用的此规格，由于并不阻塞功能的开发，此场景可以通过实现一个自定义组件，来完成行尾密码图标位置、大小、颜色的修改。自定义组件由TextInput和Image组成，使用Stack容器作为父容器。需要注意的是需要将TextInput自带的PasswordIcon设置为不显示，然后将需要替换的图标放入到Image组件中即可，此时即可随意更改位置、大小、颜色。具体代码细节如下：

```ts
@Component
struct ModifyTextInputPasswordModeIconExample {
  // TextInput行尾图标宽度
  iconWidth: number = 40;
  // TextInput行尾图标宽度
  iconHeight: number = 40;
  // TextInput组件高度
  textInputHeight: number = 56;
  // TextInput输入内容
  @State text: string = '';
  // 密码是否可见
  @State passwordState: boolean = true;
  // TextInput行尾图标图片
  @State icon: Resource = $r('app.media.ic_public_password_visible');
  // TextInputController
  controller: TextInputController = new TextInputController();

  build() {
    Column() {
      Flex({ direction: FlexDirection.Row }) {
        Stack() {
          TextInput({ text: this.text, controller: this.controller })
            .type(InputType.Password)
            .placeholderFont({ size: 16, weight: 400 })
            .showPasswordIcon(false) // 此处需将自带的行尾小眼睛图标设置成不显示
            .showPassword(this.passwordState)
            .width('100%')
            .height(this.textInputHeight)
            .backgroundColor('#E8E7E7')
            .onChange((value: string) => {
              this.text = value;
            });
          // 使用Image组件自定义实现行尾图标
          Image(this.icon)
            .margin({
              left: 290
            })
            .width(this.iconWidth)
            .height(this.iconHeight)
            .onClick(() => {
              // 点击行尾图标改变状态和icon
              this.passwordState = !this.passwordState;
              this.icon = $r(this.passwordState ? 'app.media.ic_public_password_visible' :
                'app.media.ic_public_password_invisible'
              );
            });
        };
      };
    }
    .width('100%')
    .height('100%');
  }
}

@Entry
@Component
struct ModifyTextInputPasswordModeIcon {
  build() {
    Column() {
      // icon宽高20vp
      ModifyTextInputPasswordModeIconExample({ iconWidth: 20, iconHeight: 20 })
        .height('50vp');
      Blank();
      // icon宽高30vp
      ModifyTextInputPasswordModeIconExample({ iconWidth: 30, iconHeight: 30 })
        .height('50vp');
      Blank();
      // icon宽高40vp
      ModifyTextInputPasswordModeIconExample({ iconWidth: 40, iconHeight: 40 })
        .height('50vp');
      Blank();
      // icon宽高50vp
      ModifyTextInputPasswordModeIconExample({ iconWidth: 50, iconHeight: 50 })
        .height('50vp');
    }
    .height('50%')
    .width('100%')
    .margin({ top: 50 })
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center);
  }
}
```

## 常见FAQ

Q：TextInput模式为Password的情况下，输入框右边的小眼睛如何设置能不显示？

A：设置[showPasswordIcon](../harmonyos-references/ts-basic-components-textinput.md#showpasswordicon9)为false。

Q：TextInput右侧默认的icon如何设置自定义图片？

A：使用[PasswordIcon](../harmonyos-references/ts-basic-components-textinput.md#passwordicon10)属性即可。

## 总结

对于TextInput其他输入类型，均可采用此方法来实现自定义组件，以满足更多的定制化要求，此处不再一一举例，参考上述代码实现即可。甚至如果想定制一个TextInput的输入类型，也可以参考此方法去实现。
