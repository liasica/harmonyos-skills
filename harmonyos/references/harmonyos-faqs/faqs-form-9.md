---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-form-9
title: 卡片组件的圆角显示异常
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 卡片开发（Form） > 卡片组件的圆角显示异常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:eca1717b2ba6c81bb9fdcef87c01bef1d0c599584e74c76a6ce8b7d9932bae50
---

## 问题现象

在桌面添加应用的卡片组件，卡片四角有细微的白色边缘。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/uH0VCJV-SH6B38WkvhJwhA/zh-cn_image_0000002628631576.png "点击放大")

## 背景知识

* 使用图片资源时，应考虑图片的长宽和像素密度，卡片尺寸可参考[尺寸与基础参数](../design-guides/system-features-service-widget-0000002087671904.md#section250mcpsimp)，如下图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/ViJh1OXbSfmsHnGWyym62Q/zh-cn_image_0000002658870853.png "点击放大")
* 为了避免对内容造成影响，可以在设计工具里使用1x2、2x2宫格18vp，2x4、4x4宫格22vp圆角预览效果。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/svxRMpplQrOV-71OnWOSeA/zh-cn_image_0000002628791478.png "点击放大")

## 问题定位

全局搜索Widget，查看卡片内容组件的圆角弧度的设置。该2\*2大小的卡片的圆角弧度设置为22vp而不是18vp。

```ts
struct WidgetCard {
  @LocalStorageProp('formId') formId: string = '';
  @LocalStorageProp('batterySOCInfo') batterySOCInfo: number = 0;

  build() {
    Stack() {
      Row({ space: 8 }) {
        Image($r('app.media.myposter')) // $r('app.media.myposter')需要替换为开发者需要的图片资源文件
          .width('100%')
          .height('100%')
          .objectFit(ImageFit.Fill)
          .borderRadius(22) // 与卡片圆角弧度不一致
      }
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.Center)
    }
    .align(Alignment.TopEnd)
    .backgroundColor(Color.White)
    .backgroundColor('rgba(255, 255, 255, 0.43)');
  }
}
```

## 分析结论

卡片内容组件的圆角弧度与对应卡片规格的圆角弧度不一致，则为卡片内容组件的圆角弧度设置错误，组件未填充满卡片导致卡片圆角有异常白色。

## 修改建议

修改内容组件的圆角弧度，使之与对应卡片规格的圆角弧度一致。

src/main/ets/entryability/EntryAbility.ets：

```ts
import { ConfigurationConstant, UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { JSON } from '@kit.ArkTS';

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  onCreate(): void {
    this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_LIGHT);
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
  }

  onDestroy(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    // 沉浸式
    // 1. 设置窗口全屏
    let isLayoutFullScreen = true;
    let windowClass: window.Window = windowStage.getMainWindowSync(); // 获取应用主窗口
    windowClass.setWindowLayoutFullScreen(isLayoutFullScreen).then(() => {
      hilog.info(0x0000, 'testTag', 'Succeeded in setting the window layout to full-screen mode.');
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag',
        'Failed to set the window layout to full-screen mode. Cause:' + JSON.stringify(err));
    });
    let type = window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR; // 以导航条避让为例
    let avoidArea = windowClass.getWindowAvoidArea(type);
    let bottomRectHeight = avoidArea.bottomRect.height; // 获取到导航条区域的高度
    AppStorage.setOrCreate('bottomRectHeight', bottomRectHeight);

    type = window.AvoidAreaType.TYPE_SYSTEM; // 以状态栏避让为例
    avoidArea = windowClass.getWindowAvoidArea(type);
    let topRectHeight = avoidArea.topRect.height; // 获取状态栏区域高度
    AppStorage.setOrCreate('topRectHeight', topRectHeight);
    // 3. 注册监听函数，动态获取避让区域数据
    windowClass.on('avoidAreaChange', (data) => {
      if (data.type === window.AvoidAreaType.TYPE_SYSTEM) {
        let topRectHeight = data.area.topRect.height;
        AppStorage.setOrCreate('topRectHeight', topRectHeight);
      } else if (data.type === window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR) {
        let bottomRectHeight = data.area.bottomRect.height;
        AppStorage.setOrCreate('bottomRectHeight', bottomRectHeight);
      }
    });

    windowStage.loadContent('pages/DeviceInfoPage', (err) => {
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
};
```

src/main/ets/entryformability/EntryFormAbility.ets：

```ts
import { formBindingData, FormExtensionAbility, formInfo } from '@kit.FormKit';
import { PreferencesUtil } from '../common/utils/PreferencesUtil';

export default class EntryFormAbility extends FormExtensionAbility {
  onAddForm(): formBindingData.FormBindingData {
    return formBindingData.createFormBindingData('');
  }

  async onRemoveForm(formId: string): Promise<void> {
    PreferencesUtil.getInstance().removeFormId(this.context, formId);
  }

  onAcquireFormState() {
    return formInfo.FormState.READY;
  }
};
```

src/main/ets/Pages/DeviceInfoPage.ets：

```ts
@Entry
@Component
struct DeviceInfoPage {
  build() {
    Navigation() {
      Stack() {
        Text('Hello World')
          .fontSize(16)
      }
      .height('100%')
      .width('100%')
    }
    .hideTitleBar(true)
    .height('100%')
    .width('100%')
  }
}
```

src/main/ets/widget/WidgetCard.ets：

```ts
let localStorage = new LocalStorage();

@Entry(localStorage)
@Component
export struct WidgetCard {

  build() {
    Stack() {
      Row({ space: 8 }) {
        Image($r('app.media.myposter')) // $r('app.media.myposter')需要替换为开发者需要的图片资源文件
          .width('100%')
          .height('100%')
          .objectFit(ImageFit.Fill)
          .borderRadius(16) // 与卡片圆角弧度不一致
      }
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.Center)
    }
    .align(Alignment.TopEnd)
    .backgroundColor(Color.White)
    .backgroundColor('rgba(255, 255, 255, 0.43)');
  }
}
```

src/main/ets/common/utils/Logger.ets:

```ts
import { hilog } from '@kit.PerformanceAnalysisKit';

class Logger {
  private domain: number;
  private prefix: string;
  private format: string = '%{public}s, %{public}s';

  /**
   * Constructor.
   *
   * @param Prefix Identifies the log tag.
   * @param domain Domain Indicates the service domain, which is a hexadecimal integer ranging from 0x0 to 0xFFFFF.
   */
  constructor(prefix: string) {
    this.prefix = prefix;
    this.domain = 0xFF00;
  }

  debug(...args: string[]): void {
    hilog.debug(this.domain, this.prefix, this.format, args);
  }

  info(...args: string[]): void {
    hilog.info(this.domain, this.prefix, this.format, args);
  }

  warn(...args: string[]): void {
    hilog.warn(this.domain, this.prefix, this.format, args);
  }

  error(...args: string[]): void {
    hilog.error(this.domain, this.prefix, this.format, args);
  }
}

export default new Logger('DeviceInfoCard');
```

src/main/ets/common/utils/PreferencesUtil.ets:

```ts
import { preferences } from '@kit.ArkData';
import Logger from './Logger';

const TAG: string = 'PreferencesUtil';
const MY_STORE: string = 'myStore';

export class PreferencesUtil {
  private static preferencesUtil: PreferencesUtil;

  public static getInstance(): PreferencesUtil {
    if (!PreferencesUtil.preferencesUtil) {
      PreferencesUtil.preferencesUtil = new PreferencesUtil();
    }
    return PreferencesUtil.preferencesUtil;
  }

  getPreferences(context: Context): preferences.Preferences {
    preferences.removePreferencesFromCacheSync(context, MY_STORE);
    return preferences.getPreferencesSync(context, { name: MY_STORE });
  }

  preferencesFlush(preferences: preferences.Preferences) {
    preferences.flush((err) => {
      if (err) {
        Logger.error(TAG, `Failed to flush. Code:${err.code}, message:${err.message}`);
      }
    });
  }

  preferencesPut(preferences: preferences.Preferences, key: string, value: preferences.ValueType): void {
    preferences.putSync(key, value);
    this.preferencesFlush(preferences);
  }

  removePreferencesFromCache(context: Context): void {
    preferences.removePreferencesFromCache(context, MY_STORE);
  }

  getFormIds(preferences: preferences.Preferences): Array<string> {
    if (preferences === null) {
      Logger.error(TAG, `preferences is null`);
      return [];
    }
    return preferences.getSync('formIdList', ['']) as Array<string>;
  }

  addFormId(preferences: preferences.Preferences, formId: string): void {
    try {
      if (preferences.hasSync('formIdList')) {
        let formIds = this.getFormIds(preferences);
        if (formIds.indexOf(formId) === -1) {
          formIds.push(formId);
          this.preferencesPut(preferences, 'formIdList', formIds);
        }
      } else {
        this.preferencesPut(preferences, 'formIdList', [formId]);
      }
      this.preferencesFlush(preferences);
    } catch (error) {
      Logger.error(TAG, `Failed to check the key 'formIds'. Code:${error.code}, message:${error.message}`);
    }
  }

  removeFormId(context: Context, formId: string) {
    try {
      let preferences = this.getPreferences(context);
      if (preferences === null) {
        Logger.error(TAG, `preferences is null`);
        return;
      }
      if (preferences.hasSync('formIdList')) {
        let formIds = this.getFormIds(preferences);
        let index = formIds.indexOf(formId);
        if (index !== -1) {
          formIds.splice(index, 1);
        }
        this.preferencesPut(preferences, 'formIdList', formIds);
        if (preferences.hasSync(`${formId}_show_index`)) {
          preferences.deleteSync(`${formId}_show_index`);
        }
        this.preferencesFlush(preferences);
      }
    } catch (error) {
      Logger.error(TAG, `Failed to get preferences. Code:${error.code}, message:${error.message}`);
    }
  }
}
```

src/main/module.json5：

```json
{
  "module": {
    "name": "entry",
    "type": "entry",
    "description": "$string:module_desc",
    "mainElement": "EntryAbility",
    "deviceTypes": [
      "phone",
      "tablet",
      "2in1"
    ],
    "requestPermissions": [
      {
        "name": "ohos.permission.KEEP_BACKGROUND_RUNNING",
        "reason": "$string:reason_keep_background_running",
        "usedScene": {
          "abilities": [
            "EntryAbility"
          ],
          "when": "always"
        }
      }
    ],
    "deliveryWithInstall": true,
    "installationFree": false,
    "pages": "$profile:main_pages",
    "abilities": [
      {
        "name": "EntryAbility",
        "srcEntry": "./ets/entryability/EntryAbility.ets",
        "description": "$string:EntryAbility_desc",
        "icon": "$media:layered_image",
        "label": "$string:EntryAbility_label",
        "startWindowIcon": "$media:startIcon",
        "startWindowBackground": "$color:start_window_background",
        "exported": true,
        "skills": [
          {
            "entities": [
              "entity.system.home"
            ],
            "actions": [
              "action.system.home"
            ]
          }
        ]
      }
    ],
    "extensionAbilities": [
      {
        "name": "EntryBackupAbility",
        "srcEntry": "./ets/entrybackupability/EntryBackupAbility.ets",
        "type": "backup",
        "exported": false,
        "metadata": [
          {
            "name": "ohos.extension.backup",
            "resource": "$profile:backup_config"
          }
        ],
      },
      {
        "name": "EntryFormAbility",
        "srcEntry": "./ets/entryformability/EntryFormAbility.ets",
        "label": "$string:EntryFormAbility_label",
        "description": "$string:EntryFormAbility_desc",
        "type": "form",
        "metadata": [
          {
            "name": "ohos.extension.form",
            "resource": "$profile:form_config"
          }
        ]
      }
    ]
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/N_q6pgueQ4ixNOfHkt2r7A/zh-cn_image_0000002658990793.png "点击放大")
