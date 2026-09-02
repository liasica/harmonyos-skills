---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-699
title: 已经登录过，但是点击评论依然提示需要登录
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 已经登录过，但是点击评论依然提示需要登录
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:02+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2ee5a72653fdda573edef730153dc364a02791d9eb6dd0f71fc08dc66de22b0e
---

## 问题现象

已经登录过应用，在评论时依然提示需要登录。

## 背景知识

1. [PersistentStorage](../harmonyos-guides/arkts-persiststorage.md)：PersistentStorage提供状态变量持久化的能力，但是需要注意，其持久化和读回UI的能力都需要依赖[AppStorage](../harmonyos-guides/arkts-appstorage.md)。
2. [静默登录](../architecture-guides/silent_login-0000002292499361.md)：初次登录后后续不再显示登录页面。

## 问题定位

1. 检查应用是否使用了静默登录。
   * 检查在EntryAbility.ets中是否进行静默登录选项初始化。

     ```screen
     // 在EntryAbility.ets中进行静默登录选项初始化
     PersistentStorage.persistProp('isRemembered', false);
     ```
   * 检查在登录页是否进行状态更新：

     ```screen
     Button($r('app.string.login')).onClick(async () => {
       let index: number = this.accountList.findIndex(v => v.userName === this.userName);
       if (index > -1) {
         // 数据库存在用户信息，检验密码是否正确
       } else {
         // 数据库中不存在用户信息，进行注册
       }
     });
     // 登录页进行状态更新
     Checkbox({ name: 'checkbox', group: 'checkboxGroup' }).onChange(() => {
       this.isRemembered = !this.isRemembered;
     });
     ```
2. 检查登录状态是否同步到评论组件。

   ```screen
   @Component
   struct Review {
     // 同步登录状态
     @StorageLink('isLogin') isLogin: boolean = false;
     dialogController: CustomDialogController | null = new CustomDialogController({
       builder: CustomDialogTest({
         isLogin: this.isLogin
       }),
       alignment: DialogAlignment.Bottom,
     })

     build() {
       Button('点击评论').onClick((event: ClickEvent) => {
         // 根据登录状态判断是否要弹窗
         if (this.isLogin) {
           // 已登录，进行评论操作
           this.dialogController?.open();
           console.info('登录成功:', this.isLogin);
         } else {
           this.dialogController?.open();
           console.info('请先登录:', this.isLogin);
         }
       })
     }
   }
   ```

## 分析结论

1. 未使用静默登录。
2. 相关组件未同步登录状态。

## 修改建议

1. 使用静默登录，参考[静默登录示例代码](../architecture-guides/silent_login-0000002292499361.md#section9361334121520)。
2. 同步登录状态。

   ```screen
   @Entry
   @Component
   struct LoginPage {
     @StorageLink('isLogin') isLogin: boolean = false;
     pageInfo: NavPathStack = new NavPathStack();

     build() {
       Scroll() {
         Navigation(this.pageInfo) {
           Column() {
             Column({ space: 5 }) {
               Row() {
                 Checkbox()
                   .select(this.isLogin)
                   .onChange((value) => {
                     if (value) {
                       this.isLogin = true;
                     } else {
                       this.isLogin = false;
                     }
                   });
                 Text('点击改变登录状态');
               }
               .width('100%')
               .height('90%')
               .justifyContent(FlexAlign.Center);
             };

             Column() {
               Row({ space: 5 }) {
                 Button('点击登录')
                   .width('40%')
                   .onClick(() => {
                     // 保存登录状态
                     this.getUIContext().getPromptAction().showToast({ message: '已登录' });
                     AppStorage.setOrCreate('isLogin', true);
                     // 持久化操作可在EntryAbility中进行
                     PersistentStorage.persistProp('isLogin', true);
                   });
                 Review();
               };
             }
             .width('100%')
             .layoutWeight(1)
             .justifyContent(FlexAlign.End);
           }
           .border({ color: '#f1f3f5' })
           ;
         }
         .mode(NavigationMode.Stack)
         .hideToolBar(true)
         .hideTitleBar(true)
         .onAppear(() => {
           console.info('组件挂载');
         });
       };
     }
   }

   @Component
   struct Review {
     // 同步登录状态
     @StorageLink('isLogin') isLogin: boolean = false;

     build() {
       Button('点击评论')
         .width('40%')
         .onClick(() => {
           // 根据登录状态判断是否要弹窗
           if (this.isLogin) {
             // 已登录，进行评论操作
             this.getUIContext().getPromptAction().showToast({ message: `登录状态：${this.isLogin}` });
             console.info('登录成功:', this.isLogin);
           } else {
             this.getUIContext().getPromptAction().showToast({ message: `登录状态：${this.isLogin}` });
             console.info('请先登录:', this.isLogin);
           }
         });
     }
   }
   ```

   效果图如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/w5epPleST0ShDRVXMpi2xw/zh-cn_image_0000002658914203.png "点击放大")
