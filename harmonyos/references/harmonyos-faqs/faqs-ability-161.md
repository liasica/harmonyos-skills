---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-161
title: 如何集成多个SDK解决不同abilityStage之间的冲突
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何集成多个SDK解决不同abilityStage之间的冲突
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8746b2d9f392234f1a0a41b1143ae1f06577346035055e508efba5f293a0bb9a
---

## 问题现象

应用集成多个SDK，不同的SDK均需要添加abilityStage工程文件。第一个SDK需要创建entry/src/main/ets/abilityStage/OneAbilityStage.ets，第二个SDK需要创建entry/src/main/ets/abilityStage/TwoAbilityStage.ets，而在模块的module.json5文件中添加srcEntry路径时，只能填入一个路径，如何解决该问题？

## 背景知识

[AbilityStage](../harmonyos-references/js-apis-app-ability-abilitystage.md)是一个[Module级别](../harmonyos-guides/application-package-overview.md#应用的多module设计机制)的组件管理器，用于进行Module级别的资源预加载、线程创建等初始化操作，以及维护Module下的应用状态。

## 解决方案

由于AbilityStage与Module一一对应，即一个Module拥有一个AbilityStage。因此，无法在模块的module.json5文件中配置多个srcEntry，即指向abilityStage文件的地址。如果项目中集成多个SDK均需要配置abilityStage工程文件，可以将不同SDK的abilityStage工程文件合并成一个。如果在合并过程中存在命名冲突的问题，可以在导入函数时，通过重命名的方法来解决。示例代码如下：

模仿OneSDK提供的方法：

```screen
export function preInit(str: string) {
  console.info('strOne' + str);
}
```

模仿TwoSDK提供的方法：

```screen
export function preInit(str: string) {
  console.info('strTwo' + str);
}
```

使用方合并采用的方法：

```screen
import AbilityStage from '@ohos.app.ability.AbilityStage';
import { preInit as preInitOne } from './OneAnalytics';
import { preInit as preInitTwo } from './TwoAnalytics';

export default class MyAbilityStage extends AbilityStage {
  onCreate() {
    preInitOne('One');
    preInitTwo('Two');
  }
};
```
