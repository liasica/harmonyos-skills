---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-account-20
title: 华为账号怎么切换到未成年人模式
breadcrumb: FAQ > 应用服务开发 > 华为账号服务（Account Kit） > 华为账号怎么切换到未成年人模式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:ba8d3552b32d993166979d9b4676aff3f493d0c79407b3433328e5bf7331ccfd
---

## 问题现象

应用使用华为账号登录后怎么切换到未成年人模式？

## 背景知识

本材料中的未成年人指在中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）未满十八周岁的公民。系统开启未成年人模式后可以对手机使用时长、应用安装下载、应用打开、内容访问等行为进行限制。如开启未成年人模式后亮屏时长限制在2小时内，超过两小时后手机锁定。并可以设置手机允许访问的网站或禁止访问的网站等。

## 解决方案

* 未成年人模式的开关属于系统能力，应用内开启未成年人模式需要通过调用[leadToTurnOnMinorsMode](../harmonyos-references/account-api-minorsprotection.md#leadtoturnonminorsmode)接口拉起开启未成年人模式页面，引导用户开启未成年人模式。
* 应用通过订阅系统未成年人模式开启广播事件[COMMON\_EVENT\_MINORSMODE\_ON](../harmonyos-references/commoneventmanager-definitions.md#common_event_minorsmode_on12)和系统未成年人模式关闭广播事件[COMMON\_EVENT\_MINORSMODE\_OFF](../harmonyos-references/commoneventmanager-definitions.md#common_event_minorsmode_off12)来实现应用内未成年人模式的切换。在EntryAbility的onCreate()生命周期函数中订阅未成年人模式开启/关闭事件。

  ```ts
  import { ConfigurationConstant, UIAbility} from '@kit.AbilityKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';
  import { window } from '@kit.ArkUI';
  import { minorsProtection } from '@kit.AccountKit';
  import { commonEventManager } from '@kit.BasicServicesKit';

  const DOMAIN = 0x00000;

  function dealCommonEventAllError(error: BusinessError): void {
    hilog.error(0x0000, 'testTag', `Failed to subscribe. Code: ${error.code}, message: ${error.message}`);
  }

  function registerMinorsmode() {
    const subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
      events: [commonEventManager.Support.COMMON_EVENT_MINORSMODE_ON,
        commonEventManager.Support.COMMON_EVENT_MINORSMODE_OFF]
    };
    let subscriber: commonEventManager.CommonEventSubscriber;
    // 创建订阅者
    commonEventManager.createSubscriber(subscribeInfo)
      .then((commonEventSubscriber: commonEventManager.CommonEventSubscriber) => {
        // 这里获取到commonEventSubscriber对象需要暂存，用于后续事件回调。不可直接使用，否则会出现事件回调不生效的情况
        subscriber = commonEventSubscriber;
        // 订阅公共事件
        commonEventManager.subscribe(subscriber,
          (error: BusinessError, data: commonEventManager.CommonEventData) => {
            queryMinorsmode();
            if (error) {
              dealCommonEventAllError(error);
              return;
            }
            if (data.event === commonEventManager.Support.COMMON_EVENT_MINORSMODE_ON) {
              AppStorage.setOrCreate('YouthMode', true);
              // 订阅到开启事件，可以调用获取年龄段的接口，根据年龄段刷新内容展示，同时如开发者有缓存年龄段或未成年人模式开启状态，则需要刷新缓存
              return;
            }
            if (data.event === commonEventManager.Support.COMMON_EVENT_MINORSMODE_OFF) {
              AppStorage.setOrCreate('YouthMode', false);
              // 订阅到关闭事件，关闭当前应用的未成年人模式，刷新应用内容展示，取消年龄限制，如开发者有缓存未成年人模式开启状态，则需要刷新缓存
              return;
            }
            ;
          });
      })
      .catch((error: BusinessError) => {
        dealCommonEventAllError(error);
      });
  }

  function queryMinorsmode() {
    const minorsProtectionInfo: minorsProtection.MinorsProtectionInfo =
      minorsProtection.getMinorsProtectionInfoSync();
    // 获取未成年人模式开启状态
    const minorsProtectionMode: boolean = minorsProtectionInfo.minorsProtectionMode;
    // 如开发者有频繁使用到未成年人模式开启状态，这里则需缓存未成年人模式开启状态
    hilog.info(0x0000, 'testTag',
      `Succeeded in getting minorsProtectionMode is: ${minorsProtectionMode.valueOf()}`);
    // 未成年人模式已开启，获取年龄段信息
    if (minorsProtectionMode) {
      AppStorage.setOrCreate('YouthMode', true);
      const ageGroup: minorsProtection.AgeGroup | undefined = minorsProtectionInfo.ageGroup;
      if (ageGroup) {
        hilog.info(0x0000, 'testTag', `Succeeded in getting lowerAge is: ${ageGroup.lowerAge}`);

        hilog.info(0x0000, 'testTag', `Succeeded in getting upperAge is: ${ageGroup.upperAge}`);
        AppStorage.setOrCreate('lowerAge', ageGroup.lowerAge);
        AppStorage.setOrCreate('upperAge', ageGroup.upperAge);
        // 根据年龄段刷新内容展示。如开发者有频繁使用到年龄段信息，这里则需缓存年龄段信息
      }
    } else {
      AppStorage.setOrCreate('YouthMode', false);
      AppStorage.setOrCreate('lowerAge', 0);
      AppStorage.setOrCreate('upperAge', 0);
      // 未成年人模式未开启，应用需跟随系统未成年人模式，展示内容不做限制
    }
  }

  export default class EntryAbility extends UIAbility {
    onCreate(): void {
      if (canIUse('SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection')) {
        try {
          if (minorsProtection.supportMinorsMode()) {
            registerMinorsmode();
            queryMinorsmode();
          } else {
            hilog.info(0x0000, 'testTag',
              'The current device environment does not support the youth mode, please check the current device environment.');
          }
        } catch (error) {
          hilog.error(0x0000, 'testTag',
            `Failed to invoke supportMinorsMode or getMinorsProtectionInfoSync. errCode: ${error.code},
        errMessage: ${error.message}`);
        }
      } else {
        hilog.info(0x0000, 'testTag',
          'The current device does not support the invoking of the getMinorsProtectionInfoSync interface.');
      }
      try {
        this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
      } catch (err) {
        hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
      }
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
    }

    onDestroy(): void {
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
    }

    onWindowStageCreate(windowStage: window.WindowStage): void {
      // Main window is created, set main page for this ability
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

      windowStage.loadContent('pages/Index', (err) => {
        if (err.code) {
          hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
          return;
        }
        hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
      });
    }

    onWindowStageDestroy(): void {
      // Main window is destroyed, release UI related resources
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
    }

    onForeground(): void {
      // Ability has brought to foreground
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
    }

    onBackground(): void {
      // Ability has back to background
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
    }
  }
  ```
* 应用内用户需要关闭未成年人模式时，可以通过[leadToTurnOffMinorsMode](../harmonyos-references/account-api-minorsprotection.md#leadtoturnonminorsmode)拉起系统未成年人模式页面引导用户关闭系统未成年人模式，也可以调用系统接口[verifyMinorsProtectionCredential](../harmonyos-references/account-api-minorsprotection.md#verifyminorsprotectioncredential)通过用户验证后关闭应用的未成年人模式，相比关闭系统未成年人模式更灵活更快捷。

  ```ts
  import { minorsProtection } from '@kit.AccountKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';

  @Entry
  @Component
  struct Index {
    @StorageLink('YouthMode') YouthMode: boolean = false;
    @StorageLink('lowerAge') lowerAge: string = '0';
    @StorageLink('upperAge') upperAge: string = '0';

    build() {
      Column() {
        Row() {
          Text('用户状态:')
            .fontSize($r('app.float.page_text_font_size'))
            .fontWeight(FontWeight.Bold)
          Text((this.YouthMode == false) ? '成年人' : '未成年人')
            .fontSize($r('app.float.page_text_font_size'))
            .fontWeight(FontWeight.Bold)
        }.margin({ bottom: '20vp' })

        if (this.YouthMode == true) {
          Row() {
            Text('年龄段:')
              .fontSize($r('app.float.page_text_font_size'))
              .fontWeight(FontWeight.Bold)
            Text(this.lowerAge + '~' + this.upperAge)
              .fontSize($r('app.float.page_text_font_size'))
              .fontWeight(FontWeight.Bold)
          }.margin({ bottom: '20vp' })
        }
        if (this.YouthMode == false) {
          Button('开启未成年人模式').onClick(() => {
            minorsProtection.leadToTurnOnMinorsMode(this.getUIContext().getHostContext())
              .then(() => {
                // 接口调用完成，如需显示弹窗，请在此处处理
              })
              .catch((error: BusinessError<Object>) => {
                dealError(error);
              });
          })
        }
        if (this.YouthMode == true) {
          Button('关闭未成年人模式').onClick(() => {
            minorsProtection.leadToTurnOffMinorsMode(this.getUIContext().getHostContext())
              .then(() => {
                // 接口调用完成，如需显示弹窗，请在此处处理
              })
              .catch((error: BusinessError<Object>) => {
                dealError(error);
              });
          })
        }

      }
      .height('100%')
      .width('100%')
    }
  }

  function dealError(error: BusinessError<Object>): void {
    hilog.error(0x0000, 'testTag', `Failed to changeMinorsMode. Code: ${error.code}, message: ${error.message}`);
  }
  ```

## 常见FAQ

Q：开启未成年人模式后DevEco Studio无法发现手机设备。

A：未成年人模式开启后，开发者选项中的USB调试会被自动关闭，需要输入未成年人模式密码重新开启。
