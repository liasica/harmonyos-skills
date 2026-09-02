---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1162
title: PersistenceV2持久化保存数据如何实现整体赋值
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > PersistenceV2持久化保存数据如何实现整体赋值
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:07+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f8791be07b519fb18378708020fc0ed978bf504cd1caabf4528c11fd38049208
---

## 问题现象

单个属性的赋值是可以保存成功的，但是整个model赋值保存会失败。如果用户的信息的字段较多，不能逐一对属性进行赋值，该如何实现整体赋值？

## 背景知识

* [PersistenceV2: 持久化储存UI状态](../harmonyos-guides/arkts-new-persistencev2.md)：PersistenceV2是应用程序中的可选单例对象。此对象的作用是持久化存储UI相关的数据，以确保这些属性在应用程序重新启动时的值与应用程序关闭时的值相同。

  PersistenceV2提供状态变量持久化能力，开发者可以通过connect或者globalConnect绑定同一个key，在状态变量变换和应用冷启动时，实现持久化能力。相关API使用可参考：[PersistenceV2](../harmonyos-references/js-apis-statemanagement.md#persistencev2)。
* [@ObservedV2装饰器和@Trace装饰器-类属性变化观测](../harmonyos-guides/arkts-new-observedv2-and-trace.md)：为了增强状态管理框架对类对象中属性的观测能力，开发者可以使用@ObservedV2装饰器和@Trace装饰器装饰类以及类中的属性。@ObservedV2和@Trace提供了对嵌套类对象属性变化直接观测的能力，是状态管理V2中相对核心的能力之一。
* 通过JSON.parse()转出来的对象只是普通的对象，不会被@Trace装饰。[PersistenceV2](../harmonyos-guides/arkts-new-persistencev2.md#使用限制)中只有@Trace的数据改变会触发自动持久化，普通数据的改变不会触发自动持久化。

## 解决方案

PersistenceV2实现持久化的方式是利用connect绑定一个key，返回一个对象，通过修改对象中的属性实现自动持久化存储数据。如果当前场景一次修改的值较多，逐一修改属性会导致多次[自动持久化](../harmonyos-guides/arkts-new-persistencev2.md#概述)，影响应用性能。直接用新值覆盖对象会导致新的值和之前持久化的数据失去联系，导致保存失效。这时可以先删除之前持久化的数据，再把新的值持久化到本地，实现整体赋值。

以下是实现步骤：

1. 首先利用JSON.parse(this.jsonStr)将JSON字符串转化为普通对象。
2. 使用PersistenceV2.remove删除之前持久化的数据。
3. 把新的值利用connect持久化到本地，通过构造器用新的值创建对象，且需要自动持久化（或者UI动态渲染）的属性要有@Trace装饰。
4. 可以实现整体赋值的效果，后续也可以对对象中单个属性值进行修改让UI渲染刷新。

完整示例参考如下：

```screen
import { JSON } from '@kit.ArkTS';
import { PersistenceV2, Type } from '@kit.ArkUI';

@Entry
@ComponentV2
struct PersistentPage {
  @Local jsonStr: string =
    `{
      "answerQuestion":false,
      "customerId":"930772319746404352",
      "firstLogin":false,
      "lastLoginDeviceName":"HUAWEI",
      "lastLoginIp":"192.168.61.37",
      "lastLoginTime":"2024-12-17 09:25:13",
      "msgValidate":false,
      "needWindow":false,
      "ticketString":"95ce6acb-f9a3-446f-8b32-81480bc8c01c",
      "userBaseInfo":{
        "id":930772319746404422,
        "idCard":"xxxxxxx",
        "laborUnionId":0,
        "lastLoginTime":1734398772793,
        "memberType":1,
        "mobile":"xxxx",
        "modelWorkerType":0,
        "nickName":"R202qMeZ2o",
        "openWalletBankCode":"102",
        "realName":"李四",
        "status":10101,
        "verifyStatus":true,
        "walletState":false
        }
      }`;
  @Local user: UserInfoModel =
    PersistenceV2.connect(UserInfoModel, 'LocalUserInfoModelKey', () => new UserInfoModel())!;

  aboutToAppear(): void {
    console.info(JSON.stringify(this.user));
  }

  build() {
    Column({ space: 15 }) {
      Text(`用户名:${this.user.userBaseInfo?.nickName}`)
        .margin({
          top: 40
        });
      Text(`真名:${this.user.userBaseInfo?.realName}`);
      Text(`是否登录:${this.user.isLogin}`);
      Text(`token:${this.user.ticketString}`);

      // 保存用户信息
      Button('登录').onClick(() => {
        const model = JSON.parse(this.jsonStr) as UserInfoModel;
        model.isLogin = true;
        // 重新持久化存储UI状态
        PersistenceV2.remove('LocalUserInfoModelKey');
        this.user = PersistenceV2.connect(UserInfoModel, 'LocalUserInfoModelKey', () => new UserInfoModel(model))!;
        console.info(JSON.stringify(this.user));
      });

      Button(`修改用户名:${this.user.userBaseInfo?.nickName}`)
        .onClick(() => {
          this.user.userBaseInfo!.nickName = '测试张三';
        });
      Button(`修改token:${this.user.ticketString}`)
        .onClick(() => {
          this.user.ticketString = 'xxxxxx';
        });
      Button(`退出登录:${this.user.isLogin}`)
        .onClick(() => {
          this.user.isLogin = false;
        });
    }
    .height('100%')
    .width('100%');
  }
}

@ObservedV2
export class UserBaseInfoModel {
  @Trace id?: number = 0;
  @Trace idCard?: string = '';
  @Trace laborUnionId?: number = 0;
  @Trace lastLoginTime?: number = 0;
  @Trace memberType?: number = 0;
  @Trace mobile?: string = '';
  @Trace modelWorkerType?: number = 0;
  @Trace nickName?: string = '';
  @Trace openWalletBankCode?: string = '';
  @Trace realName?: string = '';
  @Trace status?: number = 0;
  @Trace verifyStatus?: boolean = false;
  @Trace walletState?: boolean = false;

  constructor(baseInfo?: UserBaseInfoModel) {
    this.id = baseInfo?.id || 0;
    this.idCard = baseInfo?.idCard || '';
    this.laborUnionId = baseInfo?.laborUnionId || 0;
    this.lastLoginTime = baseInfo?.lastLoginTime || 0;
    this.memberType = baseInfo?.memberType || 0;
    this.mobile = baseInfo?.mobile || '';
    this.modelWorkerType = baseInfo?.modelWorkerType || 0;
    this.nickName = baseInfo?.nickName || '';
    this.openWalletBankCode = baseInfo?.openWalletBankCode || '';
    this.realName = baseInfo?.realName || '';
    this.status = baseInfo?.status || 0;
    this.verifyStatus = baseInfo?.verifyStatus || false;
    this.walletState = baseInfo?.walletState || false;
  }
}

@ObservedV2
export class UserInfoModel {
  @Trace answerQuestion?: boolean = false;
  @Trace customerId?: string = '';
  @Trace firstLogin?: boolean = false;
  @Trace lastLoginDeviceName?: string = '';
  @Trace lastLoginIp?: string = '';
  @Trace lastLoginTime?: string = '';
  @Trace msgValidate?: boolean = false;
  @Trace needWindow?: boolean = false;
  @Trace ticketString?: string = '';
  @Trace isLogin?: boolean = false;
  @Type(UserBaseInfoModel)
  @Trace userBaseInfo?: UserBaseInfoModel = new UserBaseInfoModel();

  constructor(user?: UserInfoModel) {
    this.answerQuestion = user?.answerQuestion || false;
    this.customerId = user?.customerId || '';
    this.firstLogin = user?.firstLogin || false;
    this.lastLoginDeviceName = user?.lastLoginDeviceName || '';
    this.lastLoginIp = user?.lastLoginIp || '';
    this.lastLoginTime = user?.lastLoginTime || '';
    this.needWindow = user?.needWindow || false;
    this.ticketString = user?.ticketString || 'aaa';
    this.isLogin = user?.isLogin || false;
    this.userBaseInfo = new UserBaseInfoModel(user?.userBaseInfo);
  }
}
```
