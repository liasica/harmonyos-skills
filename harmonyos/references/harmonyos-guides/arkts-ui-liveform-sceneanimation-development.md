---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-liveform-sceneanimation-development
title: 场景动效类型互动卡片开发指导
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > 互动卡片开发 > 场景动效类型互动卡片 > 场景动效类型互动卡片开发指导
category: harmonyos-guides
scraped_at: 2026-04-29T13:30:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1081a31c5686a8bdcba25a1b4aa722dabae0e8f7dc2599483bcc1dedfa5c1a61
---

本文档提供了场景动效类型互动卡片的开发指导，包括卡片非激活态和激活态UI界面开发、卡片配置文件开发。

## 接口说明

场景动效类型互动卡片关键接口如下表所示。

**表1** 主要接口

| 接口名 | 描述 |
| --- | --- |
| [onLiveFormCreate(liveFormInfo: LiveFormInfo, session: UIExtensionContentSession): void](../harmonyos-references/js-apis-app-form-liveformextensionability.md#onliveformcreate) | 互动卡片界面对象创建的回调函数。 |
| [onLiveFormDestroy(liveFormInfo: LiveFormInfo): void](../harmonyos-references/js-apis-app-form-liveformextensionability.md#onliveformdestroy) | 互动卡片界面对象销毁、资源清理的回调函数。 |
| [LiveFormExtensionContext](../harmonyos-references/js-apis-application-liveformextensioncontext.md) | LiveFormExtensionAbility的上下文，继承自ExtensionContext。 |
| [startAbilityByLiveForm(want: Want): Promise<void>](../harmonyos-references/js-apis-application-liveformextensioncontext.md#startabilitybyliveform) | 拉起互动卡片提供方（应用）的页面。 |
| [formProvider.requestOverflow(formId: string, overflowInfo: formInfo.OverflowInfo): Promise<void>](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderrequestoverflow20) | 卡片提供方发起互动卡片动效请求。 |
| [formProvider.cancelOverflow(formId: string): Promise<void>](../harmonyos-references/js-apis-app-form-formprovider.md#formprovidercanceloverflow20) | 卡片提供方发起取消互动卡片动效请求。 |
| [formProvider.getFormRect(formId: string): Promise<formInfo.Rect>](../harmonyos-references/js-apis-app-form-formprovider.md#formprovidergetformrect20) | 卡片提供方查询卡片位置、尺寸。 |

## 开发流程

### 卡片激活态UI开发

1. 创建互动卡片

   通过[LiveFormExtensionAbility](../harmonyos-references/js-apis-app-form-liveformextensionability.md)创建互动卡片，创建时加载互动卡片页面。

   ```
   1. // entry/src/main/ets/myliveformextensionability/MyLiveFormExtensionAbility.ets
   2. import { formInfo, LiveFormInfo, LiveFormExtensionAbility } from '@kit.FormKit';
   3. import { UIExtensionContentSession } from '@kit.AbilityKit';
   4. import { hilog } from '@kit.PerformanceAnalysisKit';

   6. const DOMAIN = 0x0000;

   8. export default class MyLiveFormExtensionAbility extends LiveFormExtensionAbility {
   9. onLiveFormCreate(liveFormInfo: LiveFormInfo, session: UIExtensionContentSession) {
   10. let storage: LocalStorage = new LocalStorage();
   11. storage.setOrCreate('context', this.context);
   12. storage.setOrCreate('session', session);
   13. let formId: string = liveFormInfo.formId;
   14. storage.setOrCreate('formId', formId);

   16. // 获取卡片圆角信息
   17. let borderRadius: number = liveFormInfo.borderRadius;
   18. storage.setOrCreate('borderRadius', borderRadius);

   20. // liveFormInfo.rect字段表示非激活态卡片组件相对激活态UI的位置和尺寸信息
   21. let formRect: formInfo.Rect = liveFormInfo.rect;
   22. storage.setOrCreate('formRect', formRect);
   23. hilog.info(DOMAIN, 'testTag', `MyLiveFormExtensionAbility onSessionCreate formId: ${formId}` +
   24. `, borderRadius: ${borderRadius}, formRectInfo: ${JSON.stringify(formRect)}`);

   26. // 加载互动页面
   27. session.loadContent('myliveformextensionability/pages/MyLiveFormPage', storage);
   28. }

   30. onLiveFormDestroy(liveFormInfo: LiveFormInfo) {
   31. hilog.info(DOMAIN, 'testTag', `MyLiveFormExtensionAbility onDestroy`);
   32. }
   33. };
   ```
2. 实现互动卡片页面

   ```
   1. // entry/src/main/ets/myliveformextensionability/pages/MyLiveFormPage.ets
   2. import { formInfo, formProvider } from '@kit.FormKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { common } from '@kit.AbilityKit';
   5. // Constants实现参考“互动卡片动效工具函数实现”小节
   6. import { Constants } from '../../common/Constants';
   7. import { hilog } from '@kit.PerformanceAnalysisKit';

   9. const ANIMATION_RECT_SIZE: number = 100;
   10. const END_SCALE: number = 1.5;
   11. const END_TRANSLATE: number = -300;
   12. const DOMAIN = 0x0000;

   14. @Entry
   15. @Component
   16. struct MyLiveFormPage {
   17. @State columnScale: number = 1.0;
   18. @State columnTranslate: number = 0.0;
   19. private uiContext: UIContext | undefined = undefined;
   20. private storageForMyLiveFormPage: LocalStorage | undefined = undefined;
   21. private formId: string | undefined = undefined;
   22. private formRect: formInfo.Rect | undefined = undefined;
   23. private formBorderRadius: number | undefined = undefined;
   24. private liveFormContext: common.LiveFormExtensionContext | undefined = undefined;

   26. aboutToAppear(): void {
   27. this.uiContext = this.getUIContext();
   28. if (!this.uiContext) {
   29. hilog.error(DOMAIN, 'testTag', 'no uiContext');
   30. return;
   31. }
   32. this.initParams();
   33. }

   35. private initParams(): void {
   36. this.storageForMyLiveFormPage = this.uiContext?.getSharedLocalStorage();
   37. this.formId = this.storageForMyLiveFormPage?.get<string>('formId');
   38. this.formRect = this.storageForMyLiveFormPage?.get<formInfo.Rect>('formRect');
   39. this.formBorderRadius = this.storageForMyLiveFormPage?.get<number>('borderRadius');
   40. this.liveFormContext = this.storageForMyLiveFormPage?.get<common.LiveFormExtensionContext>('context');
   41. }

   43. // 执行动效
   44. private runAnimation(): void {
   45. this.uiContext?.animateTo({
   46. duration: Constants.OVERFLOW_DURATION,
   47. curve: Curve.Ease
   48. }, () => {
   49. this.columnScale = END_SCALE;
   50. this.columnTranslate = END_TRANSLATE;
   51. });
   52. }

   54. private startAbilityByLiveForm(): void {
   55. try {
   56. // 请开发者替换为实际的want信息
   57. this.liveFormContext?.startAbilityByLiveForm({
   58. bundleName: 'com.samples.formlivedemo',
   59. abilityName: 'EntryAbility',
   60. })
   61. .then(() => {
   62. hilog.info(DOMAIN, 'testTag', 'startAbilityByLiveForm succeed');
   63. })
   64. .catch((err: BusinessError) => {
   65. hilog.error(DOMAIN, 'testTag',
   66. `startAbilityByLiveForm failed, code is ${err?.code}, message is ${err?.message}`);
   67. });
   68. } catch (e) {
   69. hilog.error(DOMAIN, 'testTag', `startAbilityByLiveForm failed, code is ${e?.code}, message is ${e?.message}`);
   70. }
   71. }

   73. build() {
   74. Stack({ alignContent: Alignment.TopStart }) {
   75. // 背景组件和普通卡片一样大
   76. Column()
   77. .width(this.formRect ? this.formRect.width : 0)
   78. .height(this.formRect ? this.formRect.height : 0)
   79. .offset({
   80. x: this.formRect ? this.formRect.left : 0,
   81. y: this.formRect ? this.formRect.top : 0,
   82. })
   83. .borderRadius(this.formBorderRadius ? this.formBorderRadius : 0)
   84. .backgroundColor('#2875F5')
   85. Stack() {
   86. this.buildContent();
   87. }
   88. .width('100%')
   89. .height('100%')
   90. }
   91. .width('100%')
   92. .height('100%')
   93. .onClick(() => {
   94. hilog.info(DOMAIN, 'testTag', 'MyLiveFormPage click to start ability');
   95. if (!this.liveFormContext) {
   96. hilog.info(DOMAIN, 'testTag', 'MyLiveFormPage liveFormContext is empty');
   97. return;
   98. }
   99. this.startAbilityByLiveForm();
   100. })
   101. }

   103. @Builder
   104. buildContent() {
   105. Stack()
   106. .width(ANIMATION_RECT_SIZE)
   107. .height(ANIMATION_RECT_SIZE)
   108. .backgroundColor(Color.White)
   109. .scale({
   110. x: this.columnScale,
   111. y: this.columnScale,
   112. })
   113. .translate({
   114. y: this.columnTranslate
   115. })
   116. .onAppear(() => {
   117. // 在页面出现时执行动效
   118. this.runAnimation();
   119. })
   120. // $r('app.string.button_cancel')需要在相应的资源文件string.json中定义
   121. Button($r('app.string.button_cancel'))
   122. .backgroundColor(Color.Grey)
   123. .onClick(() => {
   124. if (!this.formId) {
   125. hilog.info(DOMAIN, 'testTag', 'MyLiveFormPage formId is empty, cancel overflow failed');
   126. return;
   127. }
   128. hilog.info(DOMAIN, 'testTag', 'MyLiveFormPage cancel overflow animation');
   129. formProvider.cancelOverflow(this.formId);
   130. })
   131. }
   132. }
   ```
3. 互动卡片LiveFormExtensionAbility配置

   在module.json5配置文件中[extensionAbilities标签](module-configuration-file.md#extensionabilities标签)下配置LiveFormExtensionAbility。

   ```
   1. // entry/src/main/module.json5
   2. // ...
   3. "extensionAbilities": [
   4. // ...
   5. {
   6. "name": "MyLiveFormExtensionAbility",
   7. "srcEntry": "./ets/myliveformextensionability/MyLiveFormExtensionAbility.ets",
   8. "description": "MyLiveFormExtensionAbility",
   9. "type": "liveForm"
   10. }
   11. ],
   12. // ...
   ```

   在main\_pages.json文件中声明互动卡片页面。

   ```
   1. // entry/src/main/resources/base/profile/main_pages.json
   2. {
   3. "src": [
   4. "pages/Index",
   5. "myliveformextensionability/pages/MyLiveFormPage"
   6. ]
   7. }
   ```

### 卡片非激活态UI开发

1. 非激活态卡片页面实现

   非激活态卡片页面开发同普通卡片开发流程完全一致，在widgetCard.ets中完成。widgetCard.ets文件在卡片创建时自动生成，卡片创建流程可以参考[创建ArkTS卡片](arkts-ui-widget-creation.md)。在非激活态卡片页面实现点击卡片时，发起卡片动效请求。

   ```
   1. // entry/src/main/ets/widget/pages/WidgetCard.ets
   2. @Entry
   3. @Component
   4. struct WidgetCard {
   5. build() {
   6. Row() {
   7. Column() {
   8. // $r('app.string.liveform_click1')需要在相应的资源文件string.json中定义
   9. Text($r('app.string.liveform_click1'))
   10. // $r('app.float.font_size')需开发者根据实际情况替换相应的资源或值
   11. .fontSize($r('app.float.font_size'))
   12. .fontWeight(FontWeight.Medium)
   13. // $r('sys.color.font_primary')需开发者根据实际情况替换相应的资源或值
   14. .fontColor($r('sys.color.font_primary'))
   15. }
   16. .width('100%')
   17. }
   18. .height('100%')
   19. .onClick(() => {
   20. // 点击卡片时，选择向EntryFormAbility发送消息，并在其onFormEvent回调中调用formProvider.requestOverflow，请求卡片动效
   21. postCardAction(this, {
   22. action: 'message',
   23. abilityName: 'EntryFormAbility',
   24. params: {
   25. message: 'requestOverflow'
   26. }
   27. });
   28. })
   29. }
   30. }
   ```
2. form\_config.json配置

   在form\_config.json配置文件中新增sceneAnimationParams配置项。

   ```
   1. // entry/src/main/resources/base/profile/form_config.json
   2. {
   3. "forms": [
   4. {
   5. "name": "widget",
   6. "displayName": "$string:widget_display_name",
   7. "description": "$string:widget_desc",
   8. "src": "./ets/widget/pages/WidgetCard.ets",
   9. "uiSyntax": "arkts",
   10. "window": {
   11. "designWidth": 720,
   12. "autoDesignWidth": true
   13. },
   14. "colorMode": "auto",
   15. "isDefault": true,
   16. "updateEnabled": true,
   17. "scheduledUpdateTime": "10:30",
   18. "updateDuration": 1,
   19. "defaultDimension": "2*2",
   20. "supportDimensions": [
   21. "2*2"
   22. ],
   23. "formConfigAbility": "ability://EntryAbility",
   24. "dataProxyEnabled": false,
   25. "isDynamic": true,
   26. "transparencyEnabled": false,
   27. "metadata": [],
   28. "sceneAnimationParams": {
   29. "abilityName": "MyLiveFormExtensionAbility"
   30. }
   31. }
   32. ]
   33. }
   ```

### 互动卡片动效实现

1. 触发互动卡片动效

   互动卡片通过调用[formProvider.requestOverflow](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderrequestoverflow20)接口触发动效，调用时需要明确：（1）动效申请范围。（2）动效持续时间。（3）是否使用系统提供的默认切换动效。具体可参考[formInfo.OverflowInfo](../harmonyos-references/js-apis-app-form-forminfo.md#overflowinfo20)。其中，互动卡片可以通过调用[formProvider.getFormRect](../harmonyos-references/js-apis-app-form-formprovider.md#formprovidergetformrect20)接口获取卡片尺寸和在窗口内的位置信息。卡片提供方以此计算动效申请范围，单位为vp。计算规则具体请参考[互动卡片请求参数约束](arkts-ui-liveform-sceneanimation-overview.md#请求参数约束)。

   ```
   1. // entry/src/main/ets/entryformability/EntryFormAbility.ets
   2. import { FormExtensionAbility, formInfo, formProvider } from '@kit.FormKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. // Constants实现参考“互动卡片动效工具函数实现”小节
   5. import { Constants } from '../common/Constants';
   6. import { hilog } from '@kit.PerformanceAnalysisKit';

   8. const TAG: string = 'EntryFormAbility';
   9. const DOMAIN_NUMBER: number = 0xFF00;

   11. export default class EntryFormAbility extends FormExtensionAbility {
   12. async onFormEvent(formId: string, message: string) {
   13. let shortMessage: string = JSON.parse(message)['message'];

   15. // 当接收的message为requestOverflow，触发互动卡片动效
   16. if (shortMessage === 'requestOverflow') {
   17. let formRect: formInfo.Rect = await formProvider.getFormRect(formId);
   18. this.requestOverflow(formId, formRect.width, formRect.height);
   19. return;
   20. }
   21. }

   23. private requestOverflow(formId: string, formWidth: number, formHeight: number): void {
   24. if (formWidth <= 0 || formHeight <= 0) {
   25. hilog.info(DOMAIN_NUMBER, TAG, 'requestOverflow failed, form size is not correct.');
   26. return;
   27. }

   29. // 基于卡片自身尺寸信息，计算卡片动效渲染区域
   30. let left: number = -Constants.OVERFLOW_LEFT_RATIO * formWidth;
   31. let top: number = -Constants.OVERFLOW_TOP_RATIO * formHeight;
   32. let width: number = Constants.OVERFLOW_WIDTH_RATIO * formWidth;
   33. let height: number = Constants.OVERFLOW_HEIGHT_RATIO * formHeight;
   34. let duration: number = Constants.OVERFLOW_DURATION;

   36. // 发起互动卡片动效申请
   37. try {
   38. formProvider.requestOverflow(formId, {
   39. // 动效申请范围
   40. area: {
   41. left: left,
   42. top: top,
   43. width: width,
   44. height: height
   45. },
   46. // 动效持续时间
   47. duration: duration,
   48. // 指定是否使用系统提供的默认切换动效
   49. useDefaultAnimation: true,
   50. }).then(() => {
   51. hilog.info(DOMAIN_NUMBER, TAG, 'requestOverflow requestOverflow succeed');
   52. }).catch((error: BusinessError) => {
   53. hilog.info(DOMAIN_NUMBER, TAG, `requestOverflow requestOverflow catch error` + `,
   54. code: ${error.code}, message: ${error.message}`);
   55. })
   56. } catch (e) {
   57. hilog.info(DOMAIN_NUMBER, TAG, `requestOverflow call requestOverflow catch error` + `,
   58. code: ${e.code}, message: ${e.message}`);
   59. }
   60. }
   61. }
   ```
2. 互动卡片动效工具函数实现

   ```
   1. // entry/src/main/ets/common/Constants.ets
   2. // 动效相关常量的开发
   3. export class Constants {
   4. // 互动卡片动效超范围，左侧偏移百分比 = 偏移值/卡片宽度
   5. public static readonly OVERFLOW_LEFT_RATIO: number = 0.1;
   6. // 互动卡片动效超范围，上侧偏移百分比 = 偏移值/卡片高度
   7. public static readonly OVERFLOW_TOP_RATIO: number = 0.15;
   8. // 互动卡片动效超范围，宽度放大百分比
   9. public static readonly OVERFLOW_WIDTH_RATIO: number = 1.2;
   10. // 互动卡片动效超范围，高度放大百分比
   11. public static readonly OVERFLOW_HEIGHT_RATIO: number = 1.3;
   12. // 互动卡片动效超范围，动效时长
   13. public static readonly OVERFLOW_DURATION: number = 3500;
   14. }
   ```
3. 需要的资源文件string.json

   ```
   1. {
   2. "string": [
   3. // ...
   4. {
   5. "name": "liveform_click1",
   6. "value": "点击触发互动卡片动效"
   7. },
   8. {
   9. "name": "button_cancel",
   10. "value": "强制取消动效"
   11. }
   12. ]
   13. }
   ```

## 实现效果

以下是按照本文档代码示例开发而成的效果demo，demo执行动效时，点击按钮，将调用 [formProvider.cancelOverflow](../harmonyos-references/js-apis-app-form-formprovider.md#formprovidercanceloverflow20) 接口，打断当前破框动效，卡片切换为非激活态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/Dh9YjMH1TbOm-QwSB8VdWw/zh-cn_image_0000002589324679.gif?HW-CC-KV=V1&HW-CC-Date=20260429T053000Z&HW-CC-Expire=86400&HW-CC-Sign=BC044FDC72457917E9EDF0DD50C6930BF401366BAF1164ED0E4B59A9FEBDAC41)
