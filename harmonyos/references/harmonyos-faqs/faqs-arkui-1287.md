---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1287
title: 自定义键盘实现密码保险箱效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 自定义键盘实现密码保险箱效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:08+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8c2cc6699fdb31019fd049973998d5d4e31df14d3391198b9627fa13362b3c1f
---

## 问题现象

登录场景下，使用只能输入数字的自定义键盘，如何实现密码保险箱功能？

## 背景知识

[密码保险箱](../harmonyos-guides/passwordvault-save-acc-password.md)功能在应用的登录、注册、修改密码等场景具备自动保存用户名和密码的能力。触发条件及注意事项：

* 已设置锁屏密码，并且开启密码保险箱中“自动填充和保存”开关。
* 界面中TextInput输入框组件的enableAutoFill属性的值应为true（默认为true）。
* 密码保险箱的自动保存功能只适用用户名和密码保存场景，在界面中必须同时存在用户名和密码的TextInput输入框组件。即用户名输入框应设置type属性为InputType.USER\_NAME。
* 密码输入框应设置type属性为InputType.Password或InputType.NEW\_PASSWORD。具体类型请参考[InputType枚举说明](../harmonyos-references/ts-basic-components-textinput.md#inputtype枚举说明)。

## 解决方案

密码保险箱只能通过系统键盘来触发，可以将自定义键盘和系统键盘绑定，再将系统键盘隐藏，以此来实现。具体步骤如下：

1. 创建自定义数字键盘。

   ```ts
   // 自定义键盘组件
   @Builder
   CustomKeyboardBuilder() {
     Column() {
       Button('X').onClick(() => {
         // 关闭自定义键盘
         this.controller.stopEditing();
         this.getUIContext().getFocusController().clearFocus();
       });
       Grid() {
         ForEach([1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#'], (item: number | string) => {
           GridItem() {
             Button(item + '')
               .width(110)
               .backgroundColor('#ff567fd2')
               .onClick(() => {
                 this.reserveAccount += item;
               });
           };
         });
       }
       .maxCount(3)
       .columnsGap(10)
       .rowsGap(10)
       .padding(5);
     }.backgroundColor(Color.Gray)
     .padding(5);
   }
   ```
2. 用Stack布局将自定义键盘和系统键盘叠加绑定。

   ```ts
   import { BusinessError } from '@kit.BasicServicesKit';

   @Entry
   @Component
   struct LoginPage {
     @State reserveAccount: string = '';
     @State reservePassword: string = '';
     @State isShowUserName: boolean = true;
     controller: TextInputController = new TextInputController();

     @Styles
     TextInputStyle(){
       .opacity(0.6)
       .width('100%')
       .hitTestBehavior(HitTestMode.Default); // 绑定自定义键盘
     }

     build() {
       Column() {
         Text('账户登录')
           .fontSize(24)
           .fontColor($r('sys.color.black'))
           .fontWeight(FontWeight.Medium)
           .textAlign(TextAlign.Start)
           .width('100%')
           .margin({ top: 18, bottom: 32 });
         TextInput({ placeholder: '用户名(自定义键盘)', text: $$this.reserveAccount })
           .margin({ bottom: 8 })
           .type(InputType.USER_NAME)
           .placeholderColor(0x182431)
           .TextInputStyle()
           .placeholderFont({ size: 16, weight: FontWeight.Regular })
           .customKeyboard(this.CustomKeyboardBuilder());
         Stack() {
           TextInput({ placeholder: '用户名', text: $$this.reserveAccount })
             .type(InputType.PhoneNumber)
             .placeholderColor(0x182431)
             .showPasswordIcon(false)
             .placeholderFont({ size: 16, weight: FontWeight.Regular })
             .TextInputStyle()
             .id('phoneInput');
           TextInput({ placeholder: '用户名', text: $$this.reserveAccount })
             .type(InputType.USER_NAME)
             .placeholderColor(0x182431)
             .TextInputStyle()
             .placeholderFont({ size: 16, weight: FontWeight.Regular })
             .margin({ left: this.isShowUserName ? 0 : '100%' })
             .onFocus(() => {
               this.getUIContext().getFocusController().requestFocus('phoneInput');
               this.isShowUserName = false;
             })
             .id('usernameInput');
         }
         .margin({ bottom: 8 })
         .visibility(Visibility.Hidden); // 这行代码用于隐藏使用系统键盘的输入框
         TextInput({ placeholder: '密码' })
           .type(InputType.Password)
           .placeholderColor(0x182431)
           .TextInputStyle()
           .showPasswordIcon(true)
           .placeholderFont({ size: 16, weight: FontWeight.Regular })
           .onChange((value: string) => {
             this.reservePassword = value;
           })
           .margin({ bottom: 36 });
         Button('登录', { type: ButtonType.Capsule, stateEffect: false })
           .borderRadius(20)
           .width('100%')
           .height(40)
           .enabled((this.reserveAccount !== '') && (this.reservePassword !== ''))
           .onClick(() => {
             // 页面跳转时触发保存功能
             this.getUIContext()
               .getRouter()
               .pushUrl({
                 url: 'pages/Index',
               })
               .then(() => {
                 console.info('succeeded');
               })
               .catch((error: BusinessError) => {
                 console.error(`pushUrl failed, code is ${error.code}, message is ${error.message}`);
               });
           });
       }
       .padding({ left: 24, right: 24 })
       .height('100%')
       .width('100%');
     }

     // 自定义键盘组件
     @Builder
     CustomKeyboardBuilder() {
       Column() {
         Button('X').onClick(() => {
           // 关闭自定义键盘
           this.controller.stopEditing();
           this.getUIContext().getFocusController().clearFocus();
         });
         Grid() {
           ForEach([1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#'], (item: number | string) => {
             GridItem() {
               Button(item + '')
                 .width(110)
                 .backgroundColor('#ff567fd2')
                 .onClick(() => {
                   this.reserveAccount += item;
                 });
             };
           });
         }
         .maxCount(3)
         .columnsGap(10)
         .rowsGap(10)
         .padding(5);
       }.backgroundColor(Color.Gray)
       .padding(5);
     }

   }
   ```

## 常见FAQ

Q：金融类APP，不想让账号密码这种数据被密码保险箱保管起来，怎么限制密码保险箱的使用？

A：设置是否启用自动填充属性[enableAutoFill](../harmonyos-references/ts-basic-components-textinput.md#enableautofill11)为false。

Q：在使用Web组件实现登录页面，如何唤起密码保险箱保存账号密码？

A：可以参考[网页接入密码保险箱](../harmonyos-guides/arkweb-access-password-safe.md)。

Q：登录页面通过全屏模态转场bindContentCover展示，登录成功后并未触发密码保险箱特性。是否必须使用router才能触发此特性？或者是否可以主动触发保存用户密码？

A：页面跳转时触发保存功能，router和navigation都可以触发该特性。全屏模态转场的情况无法触发保存功能，当前没有主动触发保存的方案。

Q：密码保险箱功能的账号密码填充，触发条件写的是在点击用户名输入框或者密码输入框时触发自动填充弹窗，实际点击时无法弹出如何处理？

A：出现该问题的原因是TextInput组件需要是点击输入框获取焦点，不能是通过方法去获取的焦点。

Q：HarmonyOS系统上使用系统浏览器登录Web网站个人账号，如何设置会提示是否保存账号密码？

A：在系统浏览器->我的->设置->安全浏览->密码保险箱，设置密码之后，找到自动填充和保存，打开即可，然后在系统浏览器上重新登录Web网站个人账号后，就会出现保存账号和密码的提示。
