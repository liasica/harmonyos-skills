---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-completionhandler
title: "@ohos.app.ability.CompletionHandler (拉起应用结果的操作类)"
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.CompletionHandler (拉起应用结果的操作类)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:32+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5d8d71014b7c5c0219ed87fb36ef0b2e877404348d6a4355600a00f5f505c8df
---

CompletionHandler作为[StartOptions](js-apis-app-ability-startoptions.md#startoptions)和[OpenLinkOptions](js-apis-app-ability-openlinkoptions.md#openlinkoptions)的可选参数，用于处理拉起应用请求的结果。

**说明** 

* 本模块首批接口从API version 20 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## 约束限制

当前支持使用该模块的接口包括：

* [startAbility](js-apis-inner-application-uiabilitycontext.md#startability-2)
* [startAbilityForResult](js-apis-inner-application-uiabilitycontext.md#startabilityforresult-2)
* [openLink](js-apis-inner-application-uiabilitycontext.md#openlink12)

## 导入模块

```ts
import { CompletionHandler } from '@kit.AbilityKit';
```

## CompletionHandler

CompletionHandler提供了[onRequestSuccess](js-apis-app-ability-completionhandler.md#onrequestsuccess)和[onRequestFailure](js-apis-app-ability-completionhandler.md#onrequestfailure)两个回调函数，分别处理拉起应用成功和失败时的结果。

### onRequestSuccess

onRequestSuccess(elementName: ElementName, message: string): void

拉起应用成功时的回调函数，用于接收并处理拉起应用成功后的结果信息。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elementName | [ElementName](js-apis-bundlemanager-elementname.md) | 是 | ElementName信息用于标识被拉起应用。通常，ElementName仅包含abilityName和bundleName。moduleName和deviceId信息是否存在取决于调用方是否传入。shortName和uri为空。 |
| message | string | 是 | 成功拉起应用时的信息。该信息采用JSON格式，样式如下：  {  "errMsg": "Succeeded."  } |

**示例：**

参见[CompletionHandler使用](js-apis-app-ability-completionhandler.md#completionhandler使用)。

### onRequestFailure

onRequestFailure(elementName: ElementName, message: string): void

拉起应用失败时的回调函数，用于接收并处理拉起应用失败后的错误信息。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elementName | [ElementName](js-apis-bundlemanager-elementname.md) | 是 | ElementName信息用于标识被拉起应用。  - 通常，ElementName仅包含abilityName和bundleName。moduleName和deviceId信息是否存在取决于调用方是否传入。shortName和uri为空。  - 隐式启动失败时，无法获取ElementName信息。 |
| message | string | 是 | 拉起应用失败时的信息。该信息采用JSON格式，样式如下：  {  "errMsg": "xxx"  }  其中，"xxx"的取值说明如下：  Failed to call <api-name>：表示调用接口出错。其中，<api-name>为具体的接口名，比如startAbility。  User refused redirection：表示用户关闭了应用跳转弹框。  User closed the implicit startup picker：表示用户关闭了隐式启动时的应用选择弹框。  User closed the app clone picker：表示用户关闭了分身应用选择弹框。  Free installation failed：表示免安装失败。 |

**示例：**

参见[CompletionHandler使用](js-apis-app-ability-completionhandler.md#completionhandler使用)。

### CompletionHandler使用

```ts
import { UIAbility, Want, StartOptions, CompletionHandler, bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      deviceId: '',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };

    let completionHandler: CompletionHandler = {
      onRequestSuccess: (elementName: bundleManager.ElementName, message: string): void => {
        console.info(`${elementName.bundleName}-${elementName.moduleName}-${elementName.abilityName} start succeeded: ${message}`);
      },
      onRequestFailure: (elementName: bundleManager.ElementName, message: string): void => {
        console.error(`${elementName.bundleName}-${elementName.moduleName}-${elementName.abilityName} start failed: ${message}`);
      }
    };

    let options: StartOptions = {
      completionHandler: completionHandler
    };

    try {
      this.context.startAbility(want, options, (err: BusinessError) => {
        if (err.code) {
          // 处理业务逻辑错误
          console.error(`startAbility failed, code is ${err.code}, message is ${err.message}`);
          return;
        }
        // 执行正常业务
        console.info('startAbility succeed');
      });
    } catch (err) {
      // 处理入参错误异常
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`startAbility failed, code is ${code}, message is ${message}`);
    }
  }
}
```
