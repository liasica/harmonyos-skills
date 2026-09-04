---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/passwordvault-update-acc-password
title: 账号密码更新
breadcrumb: 指南 > 系统 > 安全 > 密码自动填充服务 > 应用接入密码保险箱 > 自动保存 > 账号密码更新
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:17+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:77092299fb142dcc5beb59880ce22b29db68e3ea6170e98e73f8ab1cbcc720b9
---

应用界面触发账号密码自动保存时，若密码保险箱中已存在同应用下与本次使用账号相同的账号，则弹出密码更新提示框，用户点击更新按钮，即可更新密码保险箱内对应账号的密码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/FYH0TMNdRxiHdLqrWD04YQ/zh-cn_image_0000002712244496.png)

应用触发修改密码或使用已经保存过的账号手动登录时，均会触发密码更新功能。

登录的布局介绍请参考[账号密码登录](passwordvault-save-acc-password.md#账号密码登录)，以下仅介绍修改账号密码的标准适配场景。

**触发条件及注意事项同[账号密码保存](passwordvault-save-acc-password.md)功能。**

## 修改账号密码

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/Gwxg7estTJq5UvDIzTZvqQ/zh-cn_image_0000002742003449.png)

示例代码如下：

```ts
@Entry
@Component
struct RegisterExample {
  pathInfos: NavPathStack = new NavPathStack();
  @State ReserveAccount: string = '';
  @State ReservePassword: string = '';
  @State enableAutoFill: boolean = true;

  onBackPress() {
    // 当非成功登录、返回等页面跳转时，将enableAutoFill设置为false，密码保险箱将不启用自动填充功能
    this.enableAutoFill = false;
    return false;
  }

  @Builder
  PageMap(name: string) {
    if (name === 'register_result_page') {
      RegisterResultPage()
    }
  }

  build() {
    Navigation(this.pathInfos) {
      Column() {
        Text("修改密码")
          .commonTitleStyles()

        TextInput({ placeholder: '用户名' })
          .commonInputStyles()
          .type(InputType.USER_NAME) // 账号框使用USER_NAME属性
          .onChange((value: string) => {
            this.ReserveAccount = value;
          })

        TextInput({ placeholder: '密码' })
          .showPasswordIcon(true)
          .commonInputStyles()
          .type(InputType.Password)
          .onChange((value: string) => {
            this.ReservePassword = value;
          })

        TextInput({ placeholder: '新密码' })
          .showPasswordIcon(true)
          .commonInputStyles()
          .type(InputType.NEW_PASSWORD) // 密码框使用NEW_PASSWORD属性，可以触发生成强密码。
          .enableAutoFill(this.enableAutoFill)
          .passwordRules('begin:[upper],special:[yes],len:[maxlen:32,minlen:12]')
          .onChange((value: string) => {
            this.ReservePassword = value;
          })

        Button('页面跳转')
          .commonButtonStyles()
          .enabled((this.ReserveAccount !== '') && (this.ReservePassword !== ''))
          .onClick(() => {
            this.pathInfos.pushPathByName('register_result_page', null)
          })

        Button('页面跳转（跳转前关闭autofill）')
          .commonButtonStyles()
          .enabled((this.ReserveAccount !== '') && (this.ReservePassword !== ''))
          .onClick(() => {
            this.enableAutoFill = false;
            this.pathInfos.pushPathByName('register_result_page', null)
          })
      }
    }
    .navDestination(this.PageMap)
    .height('100%')
    .width('100%')
  }
}

@Component
struct RegisterResultPage {
  pathInfos: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Column() {
        Text("Result Page").commonTitleStyles()
      }.width('100%').height('100%')
    }.title("Result Page")
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
  .margin({ top: 24, bottom: 16 })
}

@Extend(TextInput)
function commonInputStyles() {
  .placeholderColor(0x182431)
  .width('100%')
  .opacity(0.6)
  .placeholderFont({ size: 16, weight: FontWeight.Regular })
  .margin({ top: 16 })
}

@Extend(Button)
function commonButtonStyles() {
  .width('100%')
  .height(40)
  .borderRadius(20)
  .margin({ top: 24 })
}
```
