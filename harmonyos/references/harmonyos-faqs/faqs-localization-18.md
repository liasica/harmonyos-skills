---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-localization-18
title: 如何实现在程序运行时动态添加并使用多语言资源
breadcrumb: FAQ > 应用框架开发 > 无障碍和本地化 > 本地化开发（Localization） > 如何实现在程序运行时动态添加并使用多语言资源
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:31+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0237755658de535776bd1cc1397be5f1de9d13a9f878cee180b7f240b6a15a93
---

## 问题现象

有的程序中使用的部分多语言国际化文本是动态从云端获取的，此时该如何保存到程序中并使用，同时可以保证程序中的文本跟随系统语言的变化而变化。

## 背景知识

* 通过applicationContext[订阅环境变量变化](../harmonyos-guides/subscribe-system-environment-variable-changes.md)，可以在程序中监测系统语言的变化。
* AppStorage提供了[应用全局的UI状态存储](../harmonyos-guides/arkts-appstorage.md)，可以在整个应用范围内更新相关UI的变化。

## 解决方案

1. 由于resource文件夹中的多语言资源属于静态资源，在打包后无法在其中增加或减少相关多语言资源，所以这里自行实现一个I18n模块以管理动态增加的多语言资源。
2. 解决思路：实现一个I18n单例类功能模块，用来管理程序中动态增加的语言包，并把当前语言使用的语言包放到AppStorage中供其他页面使用。通过applicationContext订阅环境变量变化，监听系统语言的变化，发生变化时通过I18n模块将使用的语言包替换为新的语言包，即可达到显示文本跟随系统语言变化的效果。

* 以下是一个简单实现，其中语言包的存储方式和单例实现逻辑可根据需要修改，代码示例如下：

  ```ts
  // i18n功能模块
  export type LanguagePack = Record<string, string>;

  export class MyI18n {
    private static instance: MyI18n;
    private currentLanguage: string;
    private languagePacks: Record<string, LanguagePack> = {};

    private set appLanguagePacks(pack: Record<string, string>) {
      AppStorage.setOrCreate('LanguagePack', pack);
    }

    get appLanguagePacks() {
      return AppStorage.get('LanguagePack') as Record<string, string>;
    }

    // 私有构造函数，防止外部直接实例化
    private constructor(defaultLanguage: string) {
      this.currentLanguage = defaultLanguage;
      this.languagePacks[defaultLanguage] = {};
      this.appLanguagePacks = this.languagePacks[defaultLanguage];
    }

    // 静态方法，用于获取单例实例
    public static getInstance(defaultLanguage: string = 'en'): MyI18n {
      if (!MyI18n.instance) {
        MyI18n.instance = new MyI18n(defaultLanguage);
      }
      return MyI18n.instance;
    }

    // 加载语言包
    loadLanguagePack(language: string, pack: LanguagePack) {
      this.languagePacks[language] = pack;
      if (this.currentLanguage === language) {
        this.appLanguagePacks = this.languagePacks[language];
      }
    }

    // 设置当前语言
    setLanguage(language: string) {
      if (this.languagePacks[language]) {
        this.currentLanguage = language;
        this.appLanguagePacks = this.languagePacks[language];
      } else {
        console.warn(`Language pack for ${language} is not loaded.`);
      }
    }

    // 获取当前语言
    getCurrentLanguage() {
      return this.currentLanguage;
    }

    updateLanguagePack(language: string, newLanguagePack: LanguagePack) {
      const tempPack = this.languagePacks[language] ?? {};
      for (let key of Object.keys(newLanguagePack)) {
        tempPack[key] = newLanguagePack[key];
      }
      this.languagePacks[language] = tempPack;
      if (this.currentLanguage === language) {
        this.appLanguagePacks = this.languagePacks[language];
      }
    }
  }
  ```
* 设置系统语言变化监听：

  ```ts
  import { ConfigurationConstant, EnvironmentCallback, UIAbility } from '@kit.AbilityKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';
  import { window } from '@kit.ArkUI';
  import { MyI18n } from '../commons/I18n';

  const DOMAIN = 0x0000;

  export default class EntryAbility extends UIAbility {
    onCreate(): void {
      try {
        this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_LIGHT);
      } catch (err) {
        hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
      }
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
    }

    onWindowStageCreate(windowStage: window.WindowStage): void {
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

      windowStage.loadContent('pages/Index', (err) => {
        if (err.code) {
          hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
          return;
        }
        hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
      });

      this.subscribeConfigurationUpdate();
    }

    subscribeConfigurationUpdate() {
      let systemLanguage: string | undefined = this.context.config.language; // 获取系统当前语言

      // 1.获取ApplicationContext
      let applicationContext = this.context.getApplicationContext();
      MyI18n.getInstance(systemLanguage);
      // 2.通过applicationContext订阅环境变量变化
      let environmentCallback: EnvironmentCallback = {
        onConfigurationUpdated(newConfig) {
          const appLanguage = MyI18n.getInstance().getCurrentLanguage();
          if (appLanguage !== newConfig.language && newConfig.language) {
            MyI18n.getInstance().setLanguage(newConfig.language);
          }
        },
        onMemoryLevel(level) {
          console.info(`onMemoryLevel level: ${level}`);
        }
      };

      applicationContext.on('environment', environmentCallback);
    }
  };
  ```
* 页面中模拟动态获取多语言资源以及使用语言包显示:

  ```ts
  import { LanguagePack, MyI18n } from '../commons/I18n';

  interface LanguageMap {
    zh_CN: string;
    en: string;
  }

  function mockApi(): Promise<Record<string, LanguageMap>> {
    return new Promise((resolve) => {
      resolve({
        'name': {
          zh_CN: '中文',
          en: '英文'
        }
      });
    });
  }

  @Entry
  @Component
  struct Index {
    @StorageProp('LanguagePack') languagePack: Record<string, string> = {};

    aboutToAppear(): void {
      mockApi().then((languageResource: Record<string, LanguageMap>) => {
        const newZhPack: LanguagePack = {};
        const newEnPack: LanguagePack = {};
        Object.keys(languageResource).forEach((key) => {
          newZhPack[key] = languageResource[key].zh_CN;
          newEnPack[key] = languageResource[key].en;
        });
        MyI18n.getInstance().updateLanguagePack('zh-Hans-CN', newZhPack);
        MyI18n.getInstance().updateLanguagePack('en-Latn-CN', newEnPack);
      });
    }

    build() {
      RelativeContainer() {
        Text(this.languagePack['name'])
          .fontSize($r('app.float.page_text_font_size'))
          .fontWeight(FontWeight.Bold)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          });
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

运行示例：

当系统语言为中文时，显示的是中文的字段：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/DXOTpCDnSFGvydyRDmmyOA/zh-cn_image_0000002659022315.png "点击放大") ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/tCUTiewPQFectiaRmAMPwA/zh-cn_image_0000002659062369.png "点击放大")

当系统语言为英文时，显示的是英文对应的字段：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/0Fw0k_q-R4m0SaN_koFTTw/zh-cn_image_0000002628822998.png "点击放大") ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/KYCLzKLPRNC4VNdeGrvVlA/zh-cn_image_0000002628663110.png "点击放大")

动图效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/X_JnN9YhRRqcKYqqBy1Yjg/zh-cn_image_0000002659022317.png "点击放大")
