---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-startup-overview
title: 拉起指定应用概述
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > 应用间跳转 > 拉起指定应用 > 拉起指定应用概述
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:10+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ad426a4f16628bbfce645911066a176100cc82f10b23aa83423e866b0681f9cf
---

本章节主要介绍如何通过应用链接跳转的方式拉起指定应用。

**说明** 

从API 12开始，已不再推荐三方应用使用指定Ability方式（即显式Want）拉起其他应用。关于如何从指定Ability方式切换到指定[应用链接](app-startup-overview.md#应用链接)方式，详见[显式Want跳转切换应用链接跳转适配指导](uiability-startup-adjust.md)。

## 应用链接

应用链接是指可以将用户引导至应用内特定位置或相关网页的URL，常见的格式如下。更多关于应用链接格式与字段含义的说明，详见[应用链接说明](app-uri-config.md)。

```txt
scheme://host[:port]/path
```

## 运作机制

1. 目标应用在配置文件中注册自己的URL，并对外提供URL。
2. 拉起方应用在跳转接口中传入目标应用的URL等信息。
3. 系统接收到URL等相关信息，会寻找对应匹配项，并跳转至目标应用。

## 应用链接分类

按照应用链接的scheme以及校验机制的不同，可以分为Deep Linking与App Linking两种方式。

* **Deep Linking**：是一种通过链接跳转至应用特定页面的技术，其特点是支持开发者定义任意形式的scheme。由于缺乏域名校验机制，容易被其他应用所仿冒。
* **App Linking**：其限定了scheme必须为https，同时通过增加域名校验机制，可以从已匹配到的应用中筛选过滤出目标应用，消除应用查询和定位中产生的歧义，直达受信的目标应用。

相比Deep Linking，App Linking具有更高的安全性和可靠性，用户体验更佳。推荐开发者将App Linking作为首选方案。

| 类型 | App Linking（推荐） | Deep Linking |
| --- | --- | --- |
| 实现方案 | 目标应用需要在module.json5中声明应用链接；同时需要向系统注册域名并通过域名认证。 | 目标应用需要在module.json5中声明应用链接。 |
| 链接格式 | scheme必须为https。 | scheme可以自定义。通常不为https、http、file，否则会拉起默认的系统浏览器。 |
| 是否可用于分享或直接在网页中访问 | 可以 | 不可以，需在代码中调用。 |
| 是否可以直接拉起目标应用 | 可以 | 可以，但不推荐使用，存在被仿冒风险。 |

Deep Linking与App Linking均可以使用[openLink()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#openlink12)接口实现，不同条件下的跳转效果如下。

**说明** 

该接口中的appLinkingOnly字段表示是否必须以App Linking的方式启动UIAbility，默认为false。appLinkingOnly为true一般只用于浏览器等应用。

| 应用链接类型 | App Linking（推荐） | Deep Linking |
| --- | --- | --- |
| appLinkingOnly为false且目标应用已安装 | 直接跳转打开目标应用。 | 跳转目标应用（如果有多个符合条件的应用时，展示应用选择弹框）。 |
| appLinkingOnly为false且目标应用未安装 | 跳转默认浏览器打开网页。 | 返回失败，系统不跳转，由应用自行处理；当前会展示“链接无法打开”弹框。 |
| appLinkingOnly为true且目标应用已安装 | 直接跳转打开目标应用。 | 返回失败，系统不跳转，由应用自行处理。 |
| appLinkingOnly为true且目标应用未安装 | 返回失败，系统不跳转由应用自行处理。 | 返回失败，系统不跳转，由应用自行处理。 |

通过App Linking方式拉起指定应用的示意图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/hAR_Rcu1RvCL1I3xve9dJw/zh-cn_image_0000002736432185.png)

通过Deep Linking方式拉起应用时，如果存在多个符合条件的应用，需要用户选择后方可跳转到指定应用。示意图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/5lXxE2kdR6yRdK2RCgr-Wg/zh-cn_image_0000002706833030.png)

## 常见问题

### 跨应用拉起UIAbility时，如何感知跳转弹框的用户选择结果

通过startAbility方式或Deep Linking方式拉起其他应用的UIAbility时，系统会弹出“是否允许跳转”的确认弹框，由用户进行选择。可通过[CompletionHandler](../harmonyos-references/js-apis-app-ability-completionhandler.md)感知用户的选择结果。

### 应用间跳转时如何取消“是否允许跳转”的确认弹框

通过[openLink](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#openlink12)或[startAbility](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)拉起其他应用时，为了防止应用的恶意跳转，系统会弹出“是否允许跳转”的确认弹框，由用户进行确认。不支持开发者取消该弹框。

**说明** 

“是否允许跳转”的确认弹框实际显示的提示语由系统定义，比如“xx想要拉起xx”，此处仅为举例。

### 应用间跳转时如何取消“暂无可用打开方式”弹框

当通过[openLink](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#openlink12)或[startAbility](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)隐式启动其他应用时，如果没有找到匹配的应用，系统会弹框提示“暂无可用打开方式”。

* openLink方式启动其他应用：API version 21版本之前，不支持取消弹框提示。从API version 21版本开始，可以将OpenLinkOptions中的hideFailureTipDialog字段设置为true，取消弹框提示。

  示例如下：

  ```ts
  import { common, OpenLinkOptions, wantConstant, CompletionHandler, bundleManager } from '@kit.AbilityKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';
  import { BusinessError } from '@kit.BasicServicesKit';

  const DOMAIN = 0xeeee;
  const TAG: string = '[openLinkDemo]';

  @Entry
  @Component
  struct Index {
    @State message: string = 'I am caller';

    build() {
      Row() {
        Column() {
          Text(this.message)
            .fontSize(50)
            .fontWeight(FontWeight.Bold)
          Button('start browser', { type: ButtonType.Capsule, stateEffect: true })
            .width('87%')
            .height('5%')
            .margin({ bottom: '12vp' })
            .onClick(() => {
              let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
              let link: string = 'https://www.example.com';
              let completionHandler: CompletionHandler = {
                onRequestSuccess: (elementName: bundleManager.ElementName, message: string): void => {
                  console.info(`${elementName.bundleName}-${elementName.moduleName}-${elementName.abilityName} start succeeded: ${message}`);
                },
                onRequestFailure: (elementName: bundleManager.ElementName, message: string): void => {
                  console.error(`${elementName.bundleName}-${elementName.moduleName}-${elementName.abilityName} start failed: ${message}`);
                }
              };
              let openLinkOptions: OpenLinkOptions = {
                appLinkingOnly: false,
                // hideFailureTipDialog字段需要在appLinkingOnly字段是false时才生效
                hideFailureTipDialog: true,
                parameters: {
                  [wantConstant.Params.CONTENT_TITLE_KEY]: 'contentTitle',
                  keyString: 'str',
                  keyNumber: 200,
                  keyBool: false,
                  keyObj: {
                    keyObjKey: 'objValue',
                  }
                },
                completionHandler: completionHandler
              };
              try {
                context.openLink(
                  link,
                  openLinkOptions,
                  (err, result) => {
                    hilog.error(DOMAIN, TAG, `openLink callback error.code: ${JSON.stringify(err)}`);
                    hilog.info(DOMAIN, TAG, `openLink callback result: ${JSON.stringify(result.resultCode)}`);
                    hilog.info(DOMAIN, TAG, `openLink callback result data: ${JSON.stringify(result.want)}`);
                  }
                ).then(() => {
                  hilog.info(DOMAIN, TAG, `open link success.`);
                }).catch((err: BusinessError) => {
                  hilog.error(DOMAIN, TAG, `open link failed, errCode: ${JSON.stringify(err.code)}`);
                });
              } catch (e) {
                hilog.error(DOMAIN, TAG, `open link failed, errCode: ${JSON.stringify(e.code)}`);
              }
            })
        }
        .width('100%')
      }
      .height('100%')
    }
  }
  ```
* startAbility隐式启动其他应用：可以通过将Want中的[flags字段](../harmonyos-references/js-apis-app-ability-wantconstant.md#flags)设置为FLAG\_START\_WITHOUT\_TIPS，取消弹框提示。

  示例如下：

  ```ts
  import { common, Want, wantConstant } from '@kit.AbilityKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';
  import { BusinessError } from '@kit.BasicServicesKit';

  const TAG: string = '[Page_UIAbilityComponentsInteractive]';
  const DOMAIN_NUMBER: number = 0xFF00;

  @Entry
  @Component
  struct Page_UIAbilityComponentsInteractive {
    private context = this.getUIContext().getHostContext() as common.   UIAbilityContext;

    build() {
      Column() {
        // ...
        List({ initialIndex: 0 }) {
          ListItem() {
            Row() {
              // ...
            }
            .onClick(() => {
              // context为UIAbility对象的成员
              let wantInfo: Want = {
                deviceId: '', // deviceId为空表示本设备
                action: 'xxxx', // 隐式启动
                flags: wantConstant.Flags.FLAG_START_WITHOUT_TIPS,
              };
              // context为调用方UIAbility的UIAbilityContext
              this.context.startAbility(wantInfo).then(() => {
                hilog.info(DOMAIN_NUMBER, TAG, 'startAbility success.');
              }).catch((error: BusinessError) => {
                hilog.error(DOMAIN_NUMBER, TAG, 'startAbility failed.');
              });
            })
          }
          // ...
        }
        // ...
      }
      // ...
    }
  }
  ```
