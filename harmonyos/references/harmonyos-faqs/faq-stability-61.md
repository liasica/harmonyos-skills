---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-61
title: 使用PersistenceV2.globalConnect获取持久化数据时应用闪退
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 使用PersistenceV2.globalConnect获取持久化数据时应用闪退
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:86dffc03149e8fc8296821f90b3b0c5457ee378e30c755922bdb9cf7e81adfa6
---

## 问题现象

使用PersistenceV2持久化UI数据，应用第一次启动正常，更新持久化数据后退出应用，同时关闭后台，二次启动应用时闪退，报jscrash异常，代码崩溃在使用PersistenceV2.globalConnect获取持久化数据的地方，错误日志如下：

```log
Error message:For 'User' key: Error: The type of target 'object' mismatches the type of source 'string'
        Stacktrace:
        at errorHelper (/usr1/hmos_for_system/src/increment/sourcecode/out/generic_generic_arm_64only/general_all_phone_standard/obj/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/stateMgmt.js:15971:1)
        at getValueFromDisk (/usr1/hmos_for_system/src/increment/sourcecode/out/generic_generic_arm_64only/general_all_phone_standard/obj/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/stateMgmt.js:15794:1)
        at globalConnect (/usr1/hmos_for_system/src/increment/sourcecode/out/generic_generic_arm_64only/general_all_phone_standard/obj/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/stateMgmt.js:15590:1)
        at globalConnect (../../../foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/jsStateManagement.js:114:1)
        at Index entry (entry/src/main/ets/pages/main.ets:6:37)
        at anonymous entry (entry|entry|1.0.0|src/main/ets/pages/Main.ts:66:26)
```

问题代码示例参考如下：

```ts
import { PersistenceV2, Type } from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Local user: User = PersistenceV2.globalConnect({ type: User, defaultCreator: () => new User() })!;
  build() {
    Column({ space: 20 }) {
      Text('获取新数据')
        .width('25%')
        .borderRadius(10)
        .onClick(() => {
          this.getNewAddressAndName();
        })
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%')
  }
  private async getNewAddressAndName() {
    this.user.config!.address = 'www.example.com';
    this.user.config!.name = '';
    console.info(`user.config!.address: ${this.user.config!.address}`)
  }
}

@ObservedV2
export class Config {
  @Trace
  public address: Resource | string | undefined;

  @Trace
  public name: Resource | string | undefined;
}

@ObservedV2
export class User {
  constructor() {
    const config = new Config();
    config.address = $r('app.media.default');
    config.name = '华为用户';
    this.config = config;
  }

  @Type(Config)
  @Trace
  public config: Config;
}
```

## 背景知识

[PersistenceV2](../harmonyos-guides/arkts-new-persistencev2.md)：为了增强状态管理框架对持久化存储UI的能力，开发者可以使用PersistenceV2存储持久化的数据。PersistenceV2是应用程序中的可选单例对象。

此对象的作用是持久化存储UI相关的数据，以确保这些属性在应用程序重新启动时的值与应用程序关闭时的值相同。PersistenceV2提供状态变量持久化能力，开发者可以通过[connect](../harmonyos-references/js-apis-statemanagement.md#connect)或者[globalConnect](../harmonyos-references/js-apis-statemanagement.md#globalconnect18)绑定同一个key，在状态变量变化和应用冷启动时，实现持久化能力。

## 问题定位

1. 根据错误信息"The type mismatches when use the key 'User' in storage"可以判断错误是User类型不匹配问题导致的。
2. 由于User是自己定义的一个类，需要排查User类中各成员变量是否存在类型不匹配的情况，逐一排查User类中各成员变量的类型，发现address成员是联合类型：private address: Resource | string | undefined。
3. 排查address成员在代码中的赋值逻辑，发现初始化的时候赋的是Resource类型值：

   ```ts
   config.address = $r('app.media.default')；
   ```

   后续运行过程中又被赋了string类型值：

   ```ts
   config.address = 'www.example.com';
   ```
4. PersistenceV2存储数据的时候会记录某个变量首次存储时的类型，但会存储最新的变量值，因为address变量首次赋值的Resource类型，因此PersistenceV2会认为address变量为Resource类型，但后续address变量有被赋了string类型值，导致应用二次启动获取持久化数据反序列化的过程中类型不匹配，从而导致应用闪退。

## 分析结论

使用PersistenceV2存储持久化的数据时，被持久化的对象不建议使用联合类型，避免应用运行过程中给联合类型的对象赋了不同类型的值而导致反序列化失败。

## 修改建议

将User中的address成员改成string类型，不再使用联合类型，应用运行过程中该成员只用于存储string类型的值。

```ts
import { PersistenceV2, Type } from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Local user: User = PersistenceV2.globalConnect({ type: User, defaultCreator: () => new User() })!;

  build() {
    Column({ space: 20 }) {
      Text('获取新数据')
        .width('25%')
        .borderRadius(10)
        .onClick(() => {
          this.getNewAddressAndName();
        });
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%');
  }

  private async getNewAddressAndName() {
    this.user.config!.address = 'www.example.com';
    this.user.config!.name = '';
    console.info(`user.config!.address: ${this.user.config!.address}`);
  }
}

@ObservedV2
export class Config {
  @Trace
  public address: string = '';
  @Trace
  public name: string = '';
}

@ObservedV2
export class User {
  constructor() {
    const config = new Config();
    config.address = 'init address';
    config.name = 'name test';
    this.config = config;
  }

  @Type(Config)
  @Trace
  public config: Config;
}
```
