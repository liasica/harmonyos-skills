---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-752
title: PersistentStorage持久化数据无法删除
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > PersistentStorage持久化数据无法删除
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:03+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:73b41921ed89808fe26f61e5c2eaa7aec036c8496eff00a36e11b5a3f15904d8
---

## 问题现象

当用户登录时，会使用PersistentStorage进行部分数据的存储，当用户退出登录或切换账号时需要清除该数据，如何正确的删除数据？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/SNj4Fj5AQjK7ceRJBoI-9w/zh-cn_image_0000002658794737.png "点击放大")

## 背景知识

* [PersistentStorage](../harmonyos-guides/arkts-persiststorage.md)用于实现持久化数据存储的模块。它提供了在设备本地持久化存储和读取数据的功能，适用于需要保存用户数据、应用状态、配置信息等场景。
* [AppStorage](../harmonyos-guides/arkts-appstorage.md)：PersistentStorage提供状态变量持久化的能力，但是其持久化和读回UI的能力都需要依赖AppStorage。

## 解决方案

1. 可以使用[deleteProp](../harmonyos-references/ts-state-management.md#deleteprop10)将key对应的属性从PersistentStorage中删除，需要注意的是这样删除的是持久化中的用户数据，应用中的数据依旧存在，需要用户退出应用重新进入才能看出删除的效果。如果在应用不退出的前提删除数据。

   ```ts
   PersistentStorage.persistProp('P', '123');

   @Entry
   @Component
   struct TestCase6 {
     build() {
       Row() {
         Column() {
           Button('删除').onClick(() => {
             PersistentStorage.deleteProp('P');
             AppStorage.delete('P');
             this.getUIContext().getPromptAction().showToast({ message: '已删除持久化中的数据' });
             console.info('删除持久化数据P');
           })
           Button('查看').onClick(() => {
             let appData: undefined | string = AppStorage.get('P');
             console.info('输出：appData', appData);
           })
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```
2. 如果当前有页面使用@StorageLink的属性，AppStorage.delete就无法删除。可以改成AppStorage.link的形式，删除应用数据前可以取消订阅。

   ```ts
   PersistentStorage.persistProp('id', '123456');

   @Entry
   @Component
   struct Test {
     linkToId: SubscribedAbstractProperty<string> = AppStorage.link('id');
     @State uid: string | undefined = this.linkToId.get();

     build() {
       Column({ space: 5 }) {
         Text(`应用中当前id的值：${this.uid}`)
         Button('删除本地持久化的数据')
           .onClick(() => {
             // 删除持久化的数据后，应用中的数据还存在，需要退出应用才能看到效果
             PersistentStorage.deleteProp('id');
             this.uid = AppStorage.get('id');
             this.getUIContext().getPromptAction().showToast({ message: '已删除持久化中的数据' });
           })
         Button('取消linkToId')
           .onClick(() => {
             this.linkToId.aboutToBeDeleted();
           })
         Button('删除应用中的状态变量')
           .onClick(() => {
             // 如果没有订阅者，则删除成功
             let flag = AppStorage.delete('id');
             this.uid = AppStorage.get('id');
             if (flag) {
               this.getUIContext().getPromptAction().showToast({ message: '删除应用状态变量成功' });
             } else {
               this.getUIContext().getPromptAction().showToast({ message: '删除应用状态变量失败' });
             }
           })
       }
       .height('100%')
       .width('100%')
     }
   }
   ```
