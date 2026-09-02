---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-130
title: 通过链接跳转到应用市场提示不支持在当前设备安装
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 通过链接跳转到应用市场提示不支持在当前设备安装
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-07-31
content_hash: sha256:9108bd7851f38ad52c395781b9d04d05b2150a44da065e58ab610fd8186dd555
---

## 问题现象

点击链接跳转至应用市场后，提示“不支持在当前设备安装”，无法完成应用的下载和安装操作。

## 背景知识

* [隐式Want](../harmonyos-guides/want-overview.md#want的类型)：在启动目标应用组件时，调用方传入的Want参数中未指定abilityName，称为隐式Want。
* [拉起系统应用](../harmonyos-guides/system-app-startup.md)AppGallery Kit提供了[loadProduct()](../harmonyos-references/store-productviewmanager.md#productviewmanagerloadproduct)接口，支持直接跳转应用详情页；也可以通过startAbility()隐式拉起应用市场详情页。详见[应用详情页展示](../harmonyos-guides/appgallery-productview-loadproduct.md)。
* [DeepLinking](../harmonyos-guides/deep-linking-startup.md)：采用Deep Linking进行跳转时，系统会根据接口中传入的uri信息，在本地已安装的应用中寻找到符合条件的应用并进行拉起。当匹配到多个应用时，会拉起应用选择框。

  ```ts
  store: // appgallery.huawei.com/app/detail?id=+bundleName
  ```

* 为兼容旧链接，可以在appId前拼接大写的C。如下所示：

  ```ts
  // 比如123456是实际的appid。前面拼接上大写的C
  store: // appgallery.huawei.com/app/detail?id=C123456
  ```

## 问题定位

参考以下代码结构，排查传入uri等参数是否正确，跳转应用市场uri常见错误id前未加大写C。

```ts
import { Want } from '@kit.AbilityKit';

let wantInfo: Want = {
  action: 'ohos.want.action.search',
  entities: [ 'entity.system.browsable' ],
  uri: 'store: // appgallery.huawei.com/app/detail?id=Cxxxxxxx',
  type: 'text/plain',
};
```

## 分析结论

uri参数错误，bundleName传参错误或者在使用旧链接方式的时候id前未加大写C。

## 修改建议

参考以下Demo正确实现链接跳转下载应用功能：

```ts
import Want from '@ohos.app.ability.Want';
import common from '@ohos.app.ability.common';

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('点击跳转到应用市场详情页面')
          .margin({top: 50})
          .onClick(()=>{
            const want: Want = {
              // 隐式指定action为ohos.want.action.appdetail
              action: 'ohos.want.action.appdetail',
              // bundleName为需要拉起写评论页的应用包名
              uri: 'store://appgallery.huawei.com/app/detail?id=com.huawei.hmos.vmall'
            };
            const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
            context.startAbility(want).then(()=>{
              // 拉起成功
            }).catch(()=>{
              // 拉起失败
            });
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
