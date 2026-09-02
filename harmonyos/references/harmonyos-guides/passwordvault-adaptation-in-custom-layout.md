---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/passwordvault-adaptation-in-custom-layout
title: 自定义布局下的适配建议
breadcrumb: 指南 > 系统 > 安全 > 密码自动填充服务 > 应用接入密码保险箱 > 自定义布局下的适配建议
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:59+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:52b2d867b41b628afc0fc57c929d681c48917959d9377a853a984b15fe2a6acd
---

## 登录

应用在设置“登录”页面时，需要“用户名/账号名”、“密码”在同一个界面，具体可参照[账号密码保存-登录](passwordvault-save-acc-password.md#账号密码登录)、[账号密码填充-登录](passwordvault-autofill-acc-password.md#登录)中的介绍。

## 注册

应用在设置“注册”页面时，需要“用户名/账号名”、“新密码”在同一个界面，具体可参照[账号密码保存-注册](passwordvault-save-acc-password.md#账号密码注册)、[强密码填充-注册](passwordvault-autofill-strong-password.md#注册)中的介绍。

## 修改密码

应用在设置“修改密码”页面时，需要“用户名/账号名”、“旧密码”、“新密码”在同一个界面，具体可参照[账号密码更新-修改账号密码](passwordvault-update-acc-password.md#修改账号密码)、[账号密码填充-修改密码](passwordvault-autofill-acc-password.md#修改密码)中的介绍。

## 登录、注册失败

当应用成功登录或注册后，应将账号密码保存至密码保险箱。若登录或注册未成功，通过页面路由（router）跳转返回时，建议应用将enableAutofill属性设置为false，以避免保存错误信息。

示例代码如下：

```ts
@Entry
@Component
struct LoginExample {
  pathInfos: NavPathStack = new NavPathStack();
  @State ReserveAccount: string = '';
  @State ReservePassword: string = '';
  // 保存填充功能初始值：true
  @State enableAutoFill: boolean = true;

  onBackPress() {
    // 当非成功登录、返回等页面跳转时，将enableAutoFill设置为false，密码保险箱将不启用自动填充功能
    this.enableAutoFill = false;
    return false;
  }

  @Builder
  PageMap(name: string) {
    if (name === 'home_page') {
      HomePage()
    }
  }

  build() {
    Navigation(this.pathInfos) {
      Column({ space: 16 }) {
        Text("账户登录")
          .commonTitleStyles()

        TextInput({ placeholder: '账号' })
          .commonInputStyles()
          .type(InputType.USER_NAME)// 账号框使用USER_NAME属性
          .enableAutoFill(this.enableAutoFill)// 保存填充功能属性
          .onChange((value: string) => {
            this.ReserveAccount = value;
          })

        TextInput({ placeholder: '密码' })
          .commonInputStyles()
          .showPasswordIcon(true)
          .type(InputType.Password)// 密码框使用Password属性
          .enableAutoFill(this.enableAutoFill)// 保存填充功能属性
          .onChange((value: string) => {
            this.ReservePassword = value;
          })

        Button('登录', { type: ButtonType.Capsule, stateEffect: false })
          .borderRadius(20)
          .width('100%')
          .height(40)
          .enabled((this.ReserveAccount !== '') && (this.ReservePassword !== ''))
          .onClick(() => {
            // 成功登录时页面跳转将enableAutoFill设置为true，密码保险箱使能
            this.enableAutoFill = true;
            this.pathInfos.pushPathByName('home_page', null)
          })
      }
      .padding(16)
    }
    .navDestination(this.PageMap)
    .height('100%')
    .width('100%')
  }
}

@Component
struct HomePage {
  pathInfos: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Column() {
        Text("Home Page").commonTitleStyles()
      }.width('100%').height('100%')
    }.title("Home Page")
    .onReady((context: NavDestinationContext) => {
      this.pathInfos = context.pathStack;
    })
  }
}

@Extend(Text)
function commonTitleStyles() {
  .fontSize(24)
  .fontColor('#000000')
  .fontWeight(FontWeight.Medium)
  .margin({ top: 18 })
}

@Extend(TextInput)
function commonInputStyles() {
  .placeholderColor(0x182431)
  .width('100%')
  .opacity(0.6)
  .placeholderFont({ size: 16, weight: FontWeight.Regular })
}
```

## 将导致功能受限的布局

除上述典型场景外，以下界面布局对密码保险箱功能的使用存在限制：

| 实现场景 | 布局情况 | 账号密码填充 | 强密码填充 | 自动保存 |
| --- | --- | --- | --- | --- |
| 登录 | 用户名、密码不在同一界面 | 不支持 | 不支持 | 不支持 |
| 登录 | 验证码登录 | 不支持 | 不支持 | 不支持 |
| 注册 | 用户名、密码不在同一界面 | 不支持 | 不支持 | 不支持 |
| 修改密码 | 界面只有用户名、新密码 | 不支持 | 支持 | 支持 |
| 修改密码 | 界面只有旧密码、新密码 | 不支持 | 不支持 | 不支持 |
| 修改密码 | 界面只有新密码 | 不支持 | 不支持 | 不支持 |
