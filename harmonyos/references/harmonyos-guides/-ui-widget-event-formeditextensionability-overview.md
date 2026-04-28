---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/-ui-widget-event-formeditextensionability-overview
title: ArkTS卡片编辑概述
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > ArkTS卡片提供方开发指导 > ArkTS卡片编辑 > ArkTS卡片编辑概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:32+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:9721345f307c586dd0a212fc8fcea5a618477cf687e2a6bf60f86335efe1806a
---

ArkTS卡片提供卡片页面编辑能力，支持实现用户自定义卡片内容的功能，例如：编辑联系人卡片、修改卡片中展示的联系人、编辑天气卡片等。

卡片页面编辑分为半模态卡片编辑和全屏卡片编辑两种方式，从API version 18开始，支持半模态卡片编辑。

## 半模态卡片编辑

下面给出一个示例，介绍半模态卡片编辑的使用步骤。

### 实现原理

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/H4NJuo0NSsShT4McumBCCA/zh-cn_image_0000002552958298.png?HW-CC-KV=V1&HW-CC-Date=20260427T234130Z&HW-CC-Expire=86400&HW-CC-Sign=A567790AE73C2C1E3DEB90001B5149CF2D34C242613DB4C5AAF99B6ED2D69E56)

1. 长按卡片弹出菜单，此时桌面通过[formConfigAbility](arkts-ui-widget-configuration.md#配置文件字段说明)字段判断卡片是否支持卡片编辑能力来决定是否显示编辑按钮。
2. 点击“编辑”菜单项，桌面通过formConfigAbility中的字段拉起对应的页面，进入一级编辑页。一级编辑页的编辑区域有限，用于比较简单的编辑布局。
   * 预览区：灰色区域为预览区，用于呈现卡片编辑后的效果。预览区的布局是由桌面决定的。
   * 编辑区：白色区域为编辑区，为应用自定义布局区域，用来实现卡片编辑的布局。卡片编辑区的布局由应用继承[FormEditExtensionAbility](../harmonyos-references/js-apis-app-form-formeditextensionability.md)后绘制而成，可用于简单的编辑布局。
   * FormEditDemo：该字段为卡片宿主应用的应用名称，通过[app.json5](app-configuration-file.md#配置文件标签)配置文件中的label字段配置。
   * widget：该字段为卡片名称，通过卡片form\_config.json配置文件中的[name](arkts-ui-widget-configuration.md#配置文件字段说明)字段配置。
   * “完成”按钮：编辑完成之后，点击按钮可退出半模态卡片编辑页面。
3. 在卡片编辑区，点击“切换到：上海”按钮后，卡片提供方可以通过[updateForm](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderupdateform)接口更新卡片信息，并在预览区显示。
4. 在卡片编辑区，点击“进入二级编辑页”按钮，此时卡片通过FormEditExtensionContext提供的[startSecondPage](../harmonyos-references/js-apis-inner-application-formeditextensioncontext.md#startsecondpage)方法，将卡片提供方的二级编辑页信息传递给桌面，桌面拉起对应页面，即进入二级编辑页。二级编辑页主要有用于实现复杂的编辑布局，是否需要二级编辑页请开发者根据实际需求添加。
5. 编辑完成之后退出编辑页。

### 开发步骤

1. [创建卡片](arkts-ui-widget-creation.md)。
2. 新增EntryFormEditAbility文件，用于实现[FormEditExtensionAbility](../harmonyos-references/js-apis-app-form-formeditextensionability.md)的半模态编辑组件，并在form\_config.json文件中配置[formConfigAbility](arkts-ui-widget-configuration.md#配置文件字段说明)字段。

   * 半模态一级编辑页Ability的实现。

   ```
   1. // entry/src/main/ets/entryformeditability/EntryFormEditAbility.ets
   2. import { FormEditExtensionAbility } from '@kit.FormKit';
   3. import { UIExtensionContentSession, Want } from '@kit.AbilityKit';
   4. import { ExtensionEvent } from '../model/ExtensionEvent';

   6. const TAG: string = 'FormEditDemo[EntryFormEditAbility] -->';
   7. let storage: LocalStorage = ExtensionEvent.getStorage();

   9. export default class EntryFormEditAbility extends FormEditExtensionAbility {
   10. onCreate() {
   11. console.info(`${TAG} onCreate`);
   12. }

   14. onForeground(): void {
   15. console.info(`${TAG} EntryFormEditAbility onForeground.....`);
   16. }

   18. onBackground(): void {
   19. console.info(`${TAG} EntryFormEditAbility onBackground......`);
   20. }

   22. onDestroy(): void {
   23. console.info(`${TAG} EntryFormEditAbility onDestroy......`);
   24. }

   26. onSessionCreate(want: Want, session: UIExtensionContentSession) {
   27. // 获取被编辑卡片的卡片ID和预览卡片的卡片ID，通过storage同步到一级编辑页中
   28. const formId: string | undefined = want.parameters?.cardId as string;
   29. const previewFormId: string | undefined = want.parameters?.previewCardId as string;

   31. if (formId) {
   32. console.info(`${TAG} form id is ${formId}`);
   33. storage.setOrCreate('formId', formId);
   34. }
   35. if (previewFormId) {
   36. console.info(`${TAG} preview form id is ${previewFormId}`);
   37. storage.setOrCreate('previewFormId', previewFormId);
   38. }
   39. let extensionEvent: ExtensionEvent = new ExtensionEvent();
   40. extensionEvent.setStartSecondPage((): void => this.startSecondPage());
   41. storage.setOrCreate('extensionEvent', extensionEvent);
   42. storage.setOrCreate('context', this.context);
   43. try {
   44. // 拉起一级编辑页
   45. session.loadContent('pages/FormEditExtension', storage);
   46. } catch (e) {
   47. console.error(`${TAG} EntryFormEditAbility loadContent err, Code: ${e.code}, Message: ${e.message}`);
   48. }
   49. }

   51. onSessionDestroy(session: UIExtensionContentSession) {
   52. console.info(`${TAG} onSessionDestroy`);
   53. }

   55. private startSecondPage() {
   56. const bundleName: string = this.context.extensionAbilityInfo.bundleName;
   57. const secPageAbilityName: string = 'FormEditSecPageAbility';
   58. console.info(`${TAG} startSecondPage. bundleName: ${bundleName}, secPageAbilityName: ${secPageAbilityName}.`);
   59. try {
   60. // 拉起二级编辑页
   61. this.context.startSecondPage({
   62. bundleName: bundleName,
   63. parameters: {
   64. 'secPageAbilityName': secPageAbilityName
   65. }
   66. });
   67. console.info(`${TAG} startSecondPage success!`);
   68. } catch (err) {
   69. console.error(`${TAG} startSecondPage failed, Code: ${err.code}, Message: ${err.message}`);
   70. }
   71. }
   72. };
   ```

   * 半模态二级编辑页Ability的实现。

   ```
   1. // entry/src/main/ets/entryformeditability/FormEditSecPageAbility.ets
   2. import { FormEditExtensionAbility } from '@kit.FormKit';
   3. import { UIExtensionContentSession, Want } from '@kit.AbilityKit';
   4. import { ExtensionEvent } from '../model/ExtensionEvent';

   6. const TAG = 'FormEditExtensionAbility';

   8. export default class FormEditSecPageAbility extends FormEditExtensionAbility {
   9. public storage: LocalStorage = new LocalStorage();

   11. onCreate() {
   12. console.info(TAG, `Ability onCreate`);
   13. }

   15. onForeground(): void {
   16. console.info(TAG, `Ability onForeground`);
   17. }

   19. onBackground(): void {
   20. console.info(TAG, `Ability onBackground`);
   21. }

   23. onDestroy(): void {
   24. console.info(TAG, `Ability onDestroy`);
   25. }

   27. onSessionCreate(want: Want, session: UIExtensionContentSession) {
   28. let extensionEvent: ExtensionEvent = new ExtensionEvent();
   29. this.storage.setOrCreate('extensionEvent', extensionEvent);
   30. this.storage.setOrCreate('session', session);

   32. try {
   33. session.loadContent('pages/FormEditSecPage', this.storage);
   34. console.info(TAG, `loadContent first edit page success`);
   35. } catch (e) {
   36. console.error(TAG, `EntryFormEditAbility loadContent err, want: ${e?.message}`);
   37. }
   38. }

   40. onSessionDestroy(session: UIExtensionContentSession) {
   41. console.info(TAG, `onSessionDestroy`);
   42. }
   43. }
   ```

   * 新增EntryFormEditAbility需要在module.json5配置，配置如下。

   ```
   1. // entry/src/main/module.json5
   2. {
   3. "module": {
   4. // ...
   5. "extensionAbilities": [
   6. {
   7. // 一级编辑页
   8. "name": "EntryFormEditAbility",
   9. "srcEntry": "./ets/entryformeditability/EntryFormEditAbility.ets",
   10. "type": "formEdit"
   11. },
   12. {
   13. // 二级编辑页
   14. "name": "FormEditSecPageAbility",
   15. "srcEntry": "./ets/entryformeditability/FormEditSecPageAbility.ets",
   16. "type": "formEdit"
   17. }
   18. ]
   19. }
   20. }
   ```

   * 卡片form\_config.json文件实现。

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
   10. "formConfigAbility": "ability://EntryFormEditAbility",
   11. "isDynamic": true,
   12. "isDefault": true,
   13. "updateEnabled": false,
   14. "scheduledUpdateTime": "10:30",
   15. "multiScheduledUpdateTime": "11:30,16:30",
   16. "updateDuration": 1,
   17. "defaultDimension": "1*2",
   18. "supportDimensions": [
   19. "1*2",
   20. "2*2",
   21. "2*4",
   22. "4*4",
   23. "6*4"
   24. ]
   25. }
   26. ]
   27. }
   ```
3. 实现一级编辑页布局，通过[updateForm](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderupdateform)接口去刷新被编辑卡片的信息和预览卡片信息，通过[startSecondPage](../harmonyos-references/js-apis-inner-application-formeditextensioncontext.md#startsecondpage)方法去拉起二级编辑页。

   * 一级编辑页布局实现如下。

   ```
   1. // entry/src/main/ets/pages/FormEditExtension.ets
   2. import { common, UIExtensionContentSession } from '@kit.AbilityKit';
   3. import { preferences } from '@kit.ArkData';
   4. import { formBindingData, formProvider } from '@kit.FormKit';
   5. import { BusinessError } from '@kit.BasicServicesKit';
   6. import { ExtensionEvent } from '../model/ExtensionEvent';
   7. import { PreferencesUtil } from '../common/PreferencesUtil';
   8. import { FormData } from '../common/CommonData';

   10. const TAG: string = 'FormEditDemo[Extension] -->';
   11. let storage: LocalStorage = ExtensionEvent.getStorage();

   13. @Entry(storage)
   14. @Component
   15. struct FormEditExtension {
   16. @State message1: string = '北京';
   17. @State message2: string = '上海';
   18. private formId: string = storage.get('formId') as string;
   19. private previewFormId: string = storage.get('previewFormId') as string;
   20. private session: UIExtensionContentSession =
   21. storage.get<UIExtensionContentSession>('session') as UIExtensionContentSession;
   22. private extensionEvent: ExtensionEvent = storage.get<ExtensionEvent>('extensionEvent') as ExtensionEvent;
   23. // 在API version 22以前，需要通过import LiveFormExtensionContext from 'application/LiveFormExtensionContext';
   24. // 导入LiveFormExtensionContext。该导入方式在DevEco Studio中标红，但不影响编译运行。
   25. // 可以直接使用LiveFormExtensionContext。在API version 22及以后，支持通过import { common } from '@kit.AbilityKit';
   26. // 导入LiveFormExtensionContext。并通过common.LiveFormExtensionContext的方式使用。
   27. private context: common.FormEditExtensionContext | undefined =
   28. storage.get<common.FormEditExtensionContext>('context');

   30. updateForm(message: string) {
   31. if (!this.formId && !this.previewFormId) {
   32. return;
   33. }
   34. if (this.context) {
   35. let util = PreferencesUtil.getInstance();
   36. let preferences = util.getPreferences(this.context) as preferences.Preferences;
   37. util.preferencesPut(preferences, this.formId, new FormData(this.formId, message));
   38. }
   39. let param: Record<string, string> = {
   40. 'message': message
   41. }
   42. let obj: formBindingData.FormBindingData = formBindingData.createFormBindingData(param);
   43. try {
   44. // 刷新被编辑卡片的信息
   45. formProvider.updateForm(this.formId, obj, (error: BusinessError) => {
   46. if (error) {
   47. console.error(TAG, `callback error, code: ${error.code}, message: ${error.message})`);
   48. return;
   49. }
   50. console.info(TAG, `formProvider updateForm success`);
   51. });
   52. } catch (error) {
   53. console.error(TAG, `catch error, Code: ${error.code}, Message: ${error.message}`);
   54. }
   55. if (!this.previewFormId) {
   56. console.error(TAG, 'previewFormId is empty');
   57. return;
   58. }
   59. try {
   60. // 刷新预览卡片的信息
   61. formProvider.updateForm(this.previewFormId, obj, (error: BusinessError) => {
   62. if (error) {
   63. console.error(TAG, `callback error, code: ${error.code}, message: ${error.message})`);
   64. return;
   65. }
   66. console.info(TAG, `formProvider updateForm success`);
   67. });
   68. } catch (error) {
   69. console.error(TAG, `catch error, Code: ${error.code}, Message: ${error.message}`);
   70. }
   71. }

   73. onPageShow() {
   74. console.info(`${TAG} onPageShow. extensionEvent`);
   75. }

   77. build() {
   78. Row() {
   79. Column() {
   80. Button($r('app.string.button_one'))
   81. .width('80%')
   82. .type(ButtonType.Capsule)
   83. .margin({
   84. top: 20
   85. })
   86. .onClick(() => {
   87. console.info(`${TAG} Button1 onClick ${storage.get('message')}`);
   88. this.updateForm(this.message1);
   89. storage.setOrCreate('message', this.message1);
   90. })
   91. Button($r('app.string.button_two'))
   92. .width('80%')
   93. .type(ButtonType.Capsule)
   94. .margin({
   95. top: 20
   96. })
   97. .onClick(() => {
   98. console.info(`${TAG} Button2 onClick`);
   99. this.updateForm(this.message2);
   100. storage.setOrCreate('message', this.message2);
   101. })
   102. Button($r('app.string.button_three'))
   103. .width('80%')
   104. .type(ButtonType.Capsule)
   105. .margin({
   106. top: 20
   107. })
   108. .onClick(async () => {
   109. console.info(`${TAG} Button onClick`);
   110. // 拉起二级编辑页
   111. this.extensionEvent?.startFormEditSecondPage();
   112. })
   113. }
   114. }
   115. .justifyContent(FlexAlign.Center)
   116. .width('100%')
   117. }
   118. }
   ```

   * 新增FormEditSecPage.ets文件用来实现二级编辑页布局。

   ```
   1. // entry/src/main/ets/pages/FormEditSecPage.ets
   2. @Entry
   3. @Component
   4. struct FormEditSecPage {
   5. @State message: string | ResourceStr = $r('app.string.button_three');

   7. build() {
   8. RelativeContainer() {
   9. Text(this.message)
   10. .id('HelloWorld')
   11. .fontSize($r('app.float.page_text_font_size'))
   12. .fontWeight(FontWeight.Bold)
   13. .alignRules({
   14. center: { anchor: '__container__', align: VerticalAlign.Center },
   15. middle: { anchor: '__container__', align: HorizontalAlign.Center }
   16. })
   17. .onClick(() => {
   18. this.message = 'Welcome';
   19. })
   20. }
   21. .height('100%')
   22. .width('100%')
   23. }
   24. }
   ```

   * 加载布局文件。

     ```
     1. // entry/src/main/resources/base/profile/main_pages.json
     2. {
     3. "src": [
     4. "pages/Index",
     5. "pages/FormEditExtension",
     6. "pages/FormEditSecPage"
     7. ]
     8. }
     ```
   * 新增ExtensionEvent文件，封装[startSecondPage](../harmonyos-references/js-apis-inner-application-formeditextensioncontext.md#startsecondpage)方法到startFormEditSecondPage中，供业务使用。

   ```
   1. // entry/src/main/ets/model/ExtensionEvent.ets
   2. const TAG: string = 'FormEditDemo[ExtensionEvent] -->';
   3. const LOCAL: Record<string, string> = { 'formId': '', 'previewFormId': '', 'message': '' };

   5. export class ExtensionEvent {
   6. private static storage = new LocalStorage(LOCAL);

   8. public static getStorage(): LocalStorage {
   9. return ExtensionEvent.storage;
   10. }

   12. public setStartSecondPage(startSecondPage: () => void) {
   13. console.info(`${TAG} setStartSecondPage`);
   14. this.startSecondPage = startSecondPage;
   15. }

   17. public async startFormEditSecondPage() {
   18. console.info(`${TAG} startFormEditSecondPage call`);
   19. this.startSecondPage();
   20. }

   22. private startSecondPage: () => void = (): void => {
   23. console.info(`${TAG} startSecondPage is empty!`);
   24. };
   25. }
   ```
4. 卡片信息持久化。每次进入卡片编辑页，预览卡片都需要与被编辑卡片保持一致，所以需要持久化卡片信息。

   * 新增PreferencesUtil文件，主要是来封装[Preferences](data-persistence-by-preferences.md)首选项，供业务做持久化数据使用。

   ```
   1. // entry/src/main/ets/common/PreferencesUtil.ets
   2. import { preferences } from '@kit.ArkData';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { FormData } from './CommonData';

   6. const TAG: string = 'PreferencesUtil';
   7. const MY_STORE: string = 'myStore';

   9. export class PreferencesUtil {
   10. private static preferencesUtil: PreferencesUtil;

   12. public static getInstance(): PreferencesUtil {
   13. if (!PreferencesUtil.preferencesUtil) {
   14. PreferencesUtil.preferencesUtil = new PreferencesUtil();
   15. }
   16. return PreferencesUtil.preferencesUtil;
   17. }

   19. getPreferences(context: Context): preferences.Preferences | undefined {
   20. try {
   21. preferences.removePreferencesFromCacheSync(context, MY_STORE);
   22. return preferences.getPreferencesSync(context, { name: MY_STORE });
   23. } catch (error) {
   24. let err = error as BusinessError;
   25. console.error(TAG, `getPreferences failed, error code=${err.code}, message=${err.message}`);
   26. return undefined;
   27. }
   28. }

   30. preferencesFlush(preferences: preferences.Preferences) {
   31. preferences.flush((err) => {
   32. if (err) {
   33. console.error(TAG, `Failed to flush. Code:${err.code}, message:${err.message}`);
   34. }
   35. })
   36. }

   38. preferencesPut(preferences: preferences.Preferences, formID: string, value: FormData): void {
   39. try {
   40. preferences.putSync(formID, value);
   41. this.preferencesFlush(preferences);
   42. } catch (error) {
   43. let err = error as BusinessError;
   44. console.error(TAG, `preferencesPut failed, error code=${err.code}, message=${err.message}`);
   45. }
   46. }

   48. removePreferencesFromCache(context: Context): void {
   49. preferences.removePreferencesFromCache(context, MY_STORE).catch((err: BusinessError) => {
   50. console.error(TAG, `removePreferencesFromCache failed, error code=${err.code}, message=${err.message}`);
   51. });
   52. }

   54. getValue(preferences: preferences.Preferences, formID: string): FormData | undefined {
   55. if (preferences === null) {
   56. console.error(TAG, `preferences is null`);
   57. return undefined;
   58. }
   59. try {
   60. return preferences.getSync(formID, new FormData('')) as FormData;
   61. } catch (error) {
   62. let err = error as BusinessError;
   63. console.error(TAG, `getSync failed, error code=${err.code}, message=${err.message}`);
   64. return undefined;
   65. }
   66. }

   68. removeFormId(context: Context, formId: string) {
   69. try {
   70. let preferences = this.getPreferences(context);
   71. if (!preferences) {
   72. console.error(TAG, `preferences is null`);
   73. return;
   74. }
   75. if (preferences.hasSync(formId)) {
   76. preferences.deleteSync(formId);
   77. this.preferencesFlush(preferences);
   78. }
   79. } catch (error) {
   80. console.error(TAG, `Failed to get preferences. Code:${error.code}, message:${error.message}`);
   81. }
   82. }
   83. }
   ```

   * 为确保预览卡片和被编辑卡片信息同步，新建卡片时，在onAddForm回调函数中需要判断'ohos.extra.param.key.edit\_form\_id'字段是否携带了卡片ID。如果携带了卡片ID，则就是预览卡片则需要从数据库获取被编辑卡片的信息。

   ```
   1. // entry/src/main/ets/entryformability/WidgetCard.ets
   2. import { formBindingData, FormExtensionAbility, formInfo } from '@kit.FormKit';
   3. import { Want } from '@kit.AbilityKit';
   4. import { PreferencesUtil } from '../common/PreferencesUtil';
   5. import { FormData } from '../common/CommonData';

   7. export default class EntryFormAbility extends FormExtensionAbility {
   8. onAddForm(want: Want) {
   9. let editFormId: string = '';
   10. let formId: string = '';
   11. // 初始化首选项数据库
   12. let util = PreferencesUtil.getInstance();
   13. let preferences = util.getPreferences(this.context);
   14. if (want.parameters) {
   15. formId = want.parameters[formInfo.FormParam.IDENTITY_KEY] as string;
   16. editFormId = want.parameters['ohos.extra.param.key.edit_form_id'] as string;
   17. }
   18. // 如果是编辑页面的预览卡片需要在创建时把编辑的卡片信息更新到预览卡片上
   19. if (editFormId && preferences) {
   20. let formData: FormData = util.getValue(preferences, editFormId) as FormData;
   21. return formBindingData.createFormBindingData({
   22. 'message': formData.text
   23. });
   24. }

   26. return formBindingData.createFormBindingData('');
   27. }

   29. onCastToNormalForm(formId: string) {
   30. }

   32. onUpdateForm(formId: string) {
   33. }

   35. onFormEvent(formId: string, message: string) {
   36. }

   38. onRemoveForm(formId: string) {
   39. }

   41. onAcquireFormState(want: Want) {
   42. return formInfo.FormState.READY;
   43. }
   44. }
   ```

   * 卡片布局文件如下。

   ```
   1. // entry/src/main/ets/widget/pages/WidgetCard.ets
   2. let storage: LocalStorage = new LocalStorage();

   4. @Entry(storage)
   5. @Component
   6. struct WidgetCard {
   7. @LocalStorageProp('message') title: string = 'Hello World';
   8. readonly actionType: string = 'router';
   9. readonly abilityName: string = 'EntryAbility';
   10. readonly message: string = 'add detail';
   11. readonly fullWidthPercent: string = '100%';
   12. readonly fullHeightPercent: string = '100%';

   14. build() {
   15. Row() {
   16. Column() {
   17. Text(this.title)
   18. .fontSize($r('app.float.font_size'))
   19. .fontWeight(FontWeight.Medium)
   20. .fontColor($r('sys.color.font'))
   21. }
   22. .width(this.fullWidthPercent)
   23. }
   24. .height(this.fullHeightPercent)
   25. .backgroundColor($r('sys.color.comp_background_primary'))
   26. .onClick(() => {
   27. postCardAction(this, {
   28. action: this.actionType,
   29. abilityName: this.abilityName,
   30. params: {
   31. message: this.message
   32. }
   33. });
   34. })
   35. }
   36. }
   ```

   * 新增CommonData.ets文件，用来定义卡片数据结构。

   ```
   1. // entry/src/main/ets/common/CommonData.ets
   2. export class FormData {
   3. public formId: string = '';
   4. public text: string = 'Hello World';

   6. constructor(formId: string, text?: string) {
   7. this.formId = formId;
   8. this.text = text ? text : 'Hello World';
   9. }
   10. }
   ```
5. 资源文件如下。

   ```
   1. // entry/src/main/resources/base/element/string.json
   2. {
   3. "string": [
   4. // ...
   5. {
   6. "name": "button_one",
   7. "value": "切换到：北京"
   8. },
   9. {
   10. "name": "button_two",
   11. "value": "切换到：上海"
   12. },
   13. {
   14. "name": "button_three",
   15. "value": "进入编辑二级页"
   16. }
   17. ]
   18. }
   ```
6. 运行效果如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/dxdqTbx5QvSqZhpmsmqx-g/zh-cn_image_0000002583478299.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234130Z&HW-CC-Expire=86400&HW-CC-Sign=F779DC7ED75642DBF159A754AFC2AF1A1293B5BFD51632ECE1B7F353DE800796)

## 全屏卡片编辑

### 实现原理

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/zx-AeiGLSn-9bi_SNdX8vg/zh-cn_image_0000002552798650.png?HW-CC-KV=V1&HW-CC-Date=20260427T234130Z&HW-CC-Expire=86400&HW-CC-Sign=2148ABDC3BA4D679EB98460C7B666CA2428CD4E49B7D79A777FCE1CD2C2FABB7)

1. 长按卡片弹出菜单。桌面通过[formConfigAbility](arkts-ui-widget-configuration.md#配置文件字段说明)字段判断卡片是否支持卡片编辑能力来决定是否显示编辑按钮。
2. 点击“编辑”菜单项进入全屏编辑页。桌面通过formConfigAbility字段的信息拉起卡片编辑页。
3. 点击“切换到：上海”按钮编辑卡片内容。提供方通过[updateForm](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderupdateform)接口去更新编辑卡片的信息。

### 开发步骤

下面给出示例，实现如下功能：长按卡片弹出编辑菜单，点击“编辑”菜单项进入全屏编辑页，修改卡片内容。

1. [创建卡片](arkts-ui-widget-creation.md)。
2. 开发者需要新增EntryEditAbility.ets文件，继承[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)组件，实现[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)和[onNewWant](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)回调函数。卡片使用方会通过[Want](../harmonyos-references/js-apis-app-ability-want.md)的parameters字段把被编辑的卡片ID带进来。并且需要再form\_config.json文件中配置[formConfigAbility](arkts-ui-widget-configuration.md#配置文件字段说明)字段。

   * 实现编辑页面的Ability。

   ```
   1. // entry/src/main/ets/entryability/EntryEditAbility.ets
   2. import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   4. import { window } from '@kit.ArkUI';
   5. import { PreferencesUtil } from '../common/PreferencesUtil';
   6. import { preferences } from '@kit.ArkData';

   8. const DOMAIN = 0x0000;

   10. export default class EntryEditAbility extends UIAbility {
   11. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
   12. const formId: string = want.parameters?.formId as string;
   13. hilog.info(DOMAIN, 'testTag', 'onCreate form id is' + formId)
   14. if (formId) {
   15. // 存储被编辑的卡片ID，后续编辑卡片会用
   16. let util = PreferencesUtil.getInstance();
   17. let preferences = util.getPreferences(this.context) as preferences.Preferences;
   18. util.preferencesPut(preferences, formId);
   19. }
   20. try {
   21. this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
   22. } catch (err) {
   23. hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Code:${err.code}, message:${err.message}');
   24. }
   25. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
   26. }

   28. onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam) {
   29. // 热启动编辑页时刷新被编辑的卡片ID
   30. const formId: string = want.parameters?.formId as string;
   31. hilog.info(DOMAIN, 'testTag', 'onNewWant form id is' + formId)
   32. if (formId) {
   33. // 初始化首选项数据库
   34. let util = PreferencesUtil.getInstance();
   35. let preferences = util.getPreferences(this.context) as preferences.Preferences;
   36. util.preferencesPut(preferences, formId);
   37. }
   38. }

   40. onDestroy(): void {
   41. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
   42. }

   44. onWindowStageCreate(windowStage: window.WindowStage): void {
   45. // Main window is created, set main page for this ability
   46. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

   48. windowStage.loadContent('pages/FormEditIndex', (err) => {
   49. if (err.code) {
   50. hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Code:${err.code}, message:${err.message}');
   51. return;
   52. }
   53. hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
   54. });
   55. AppStorage.setOrCreate('windowStage', this.context);
   56. }

   58. onWindowStageDestroy(): void {
   59. // Main window is destroyed, release UI related resources
   60. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
   61. }

   63. onForeground(): void {
   64. // Ability has brought to foreground
   65. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
   66. }

   68. onBackground(): void {
   69. // Ability has back to background
   70. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
   71. }
   72. }
   ```

   * 新增EntryEditAbility需要在module.json5配置，配置如下。

   ```
   1. "abilities": [
   2. // ...
   3. {
   4. "name": "FormEditAbility",
   5. "srcEntry": "./ets/entryability/EntryEditAbility.ets",
   6. "description": "$string:EntryAbility_desc",
   7. "icon": "$media:layered_image",
   8. "label": "$string:EntryAbility_label",
   9. "startWindowIcon": "$media:startIcon",
   10. "startWindowBackground": "$color:start_window_background",
   11. "exported": true,
   12. }
   13. ],
   ```

   * 卡片form\_config.json文件实现。

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
   10. "isDynamic": true,
   11. "isDefault": true,
   12. "updateEnabled": false,
   13. "formConfigAbility": "ability://FormEditAbility",
   14. "scheduledUpdateTime": "10:30",
   15. "updateDuration": 1,
   16. "defaultDimension": "2*2",
   17. "supportDimensions": [
   18. "2*2"
   19. ]
   20. }
   21. ]
   22. }
   ```
3. 新增FormEditIndex.ets文件实现全屏编辑页布局，通过[updateForm](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderupdateform)接口去刷新被编辑卡片的信息。

   ```
   1. // entry/src/main/ets/pages/FormEditIndex.ets
   2. import { formBindingData, formProvider } from '@kit.FormKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { PreferencesUtil } from '../common/PreferencesUtil';
   5. import { preferences } from '@kit.ArkData';

   7. const TAG: string = 'FormEdit -->';

   9. @Entry
   10. @Component
   11. struct FormEditIndex {
   12. @State message: string = 'Hello World';
   13. @State message1: string = '北京';
   14. @State message2: string = '上海';

   16. updateForm(message: string) {
   17. // 通过数据库获取当前需要编辑的卡片ID
   18. let util = PreferencesUtil.getInstance();
   19. let preferences = util.getPreferences(this.getUIContext().getHostContext() as Context) as preferences.Preferences;
   20. let formId: string = util.getValue(preferences) as string;
   21. if (!formId) {
   22. return;
   23. }
   24. console.info(TAG, `doy: formId: ${formId}, message: ${message}`)
   25. let param: Record<string, string> = {
   26. 'message': message
   27. }
   28. let obj: formBindingData.FormBindingData = formBindingData.createFormBindingData(param);
   29. try {
   30. formProvider.updateForm(formId, obj, (error: BusinessError) => {
   31. if (error) {
   32. console.error(TAG, `callback error, code: ${error.code}, message: ${error.message})`);
   33. return;
   34. }
   35. console.info(TAG, `formProvider updateForm success`);
   36. });
   37. } catch (error) {
   38. console.error(TAG, `catch error, Code:${error.code}, message:${error.message}`);
   39. }
   40. }

   42. build() {
   43. Row() {
   44. Column() {
   45. Button($r('app.string.button_one'))
   46. .width('80%')
   47. .type(ButtonType.Capsule)
   48. .margin({
   49. top: 20
   50. })
   51. .onClick(() => {
   52. this.updateForm(this.message1);
   53. })
   54. Button($r('app.string.button_two'))
   55. .width('80%')
   56. .type(ButtonType.Capsule)
   57. .margin({
   58. top: 20
   59. })
   60. .onClick(() => {
   61. this.updateForm(this.message2);
   62. })
   63. }
   64. }
   65. .justifyContent(FlexAlign.Center)
   66. .width('100%')
   67. }
   68. }
   ```

   * 加载全屏编辑页布局文件。

   ```
   1. // entry/src/main/resources/base/profile/main_pages.json
   2. {
   3. "src": [
   4. "pages/Index",
   5. "pages/FormEditIndex"
   6. ]
   7. }
   ```

   * 卡片布局文件如下。

   ```
   1. // entry/src/main/ets/widget/pages/WidgetCard.ets
   2. @Entry
   3. @Component
   4. struct WidgetCard {
   5. @LocalStorageProp('message') title: string = 'Hello World';
   6. readonly actionType: string = 'router';
   7. readonly abilityName: string = 'EntryAbility';
   8. readonly message: string = 'add detail';
   9. readonly fullWidthPercent: string = '100%';
   10. readonly fullHeightPercent: string = '100%';

   12. build() {
   13. Row() {
   14. Column() {
   15. Text(this.title)
   16. .fontSize($r('app.float.font_size'))
   17. .fontWeight(FontWeight.Medium)
   18. .fontColor($r('sys.color.font'))
   19. }
   20. .width(this.fullWidthPercent)
   21. }
   22. .height(this.fullHeightPercent)
   23. .backgroundColor($r('sys.color.comp_background_primary'))
   24. .onClick(() => {
   25. postCardAction(this, {
   26. action: this.actionType,
   27. abilityName: this.abilityName,
   28. params: {
   29. message: this.message
   30. }
   31. });
   32. })
   33. }
   34. }
   ```
4. 新增PreferencesUtil文件，主要是来封装[Preferences](data-persistence-by-preferences.md)首选项，供业务做持久化数据使用。

   ```
   1. // entry/src/main/ets/common/PreferencesUtil.ets
   2. import { preferences } from '@kit.ArkData';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. const TAG: string = 'PreferencesUtil';
   6. const MY_STORE: string = 'myStore';
   7. const key: string = 'formID';

   9. export class PreferencesUtil {
   10. private static preferencesUtil: PreferencesUtil;

   12. public static getInstance(): PreferencesUtil {
   13. if (!PreferencesUtil.preferencesUtil) {
   14. PreferencesUtil.preferencesUtil = new PreferencesUtil();
   15. }
   16. return PreferencesUtil.preferencesUtil;
   17. }

   19. getPreferences(context: Context): preferences.Preferences | undefined {
   20. try {
   21. preferences.removePreferencesFromCacheSync(context, MY_STORE);
   22. return preferences.getPreferencesSync(context, { name: MY_STORE });
   23. } catch (error) {
   24. let err = error as BusinessError;
   25. console.error(TAG, `getPreferences failed, error code=${err.code}, message=${err.message}`);
   26. return undefined;
   27. }
   28. }

   30. preferencesFlush(preferences: preferences.Preferences) {
   31. preferences.flushSync();
   32. }

   34. preferencesPut(preferences: preferences.Preferences, formID: string): void {
   35. try {
   36. preferences.putSync(key, formID);
   37. preferences.flushSync();
   38. } catch (error) {
   39. let err = error as BusinessError;
   40. console.error(TAG, `preferencesPut failed, error code=${err.code}, message=${err.message}`);
   41. }
   42. }

   44. removePreferencesFromCache(context: Context): void {
   45. preferences.removePreferencesFromCache(context, MY_STORE).catch((err: BusinessError) => {
   46. console.error(TAG, `removePreferencesFromCache failed, error code=${err.code}, message=${err.message}`);
   47. });
   48. }

   50. getValue(preferences: preferences.Preferences): string | undefined {
   51. if (preferences === null) {
   52. console.error(TAG, `preferences is null`);
   53. return undefined;
   54. }
   55. try {
   56. return preferences.getSync(key, '') as string
   57. } catch (error) {
   58. let err = error as BusinessError;
   59. console.error(TAG, `getSync failed, error code=${err.code}, message=${err.message}`);
   60. return undefined;
   61. }
   62. }

   64. removeFormId(context: Context) {
   65. try {
   66. let preferences = this.getPreferences(context);
   67. if (!preferences) {
   68. console.error(TAG, `preferences is null`);
   69. return;
   70. }
   71. if (preferences.hasSync(key)) {
   72. preferences.deleteSync(key);
   73. preferences.flushSync();
   74. console.info(TAG, `deleteSync done.`)
   75. }
   76. } catch (error) {
   77. console.error(TAG, `Failed to get preferences. Code:${error.code}, message:${error.message}`);
   78. }
   79. }
   80. }
   ```
5. 资源文件如下。

   ```
   1. // entry/src/main/resources/base/element/string.json
   2. {
   3. "string": [
   4. // ...
   5. {
   6. "name": "button_one",
   7. "value": "切换到：北京"
   8. },
   9. {
   10. "name": "button_two",
   11. "value": "切换到：上海"
   12. }
   13. ]
   14. }
   ```
6. 运行效果如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/8B4mOT2HS76hz-q-tvpr6w/zh-cn_image_0000002583438345.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234130Z&HW-CC-Expire=86400&HW-CC-Sign=DDAD879B382799727C79E46D4D30B398E1005D8167803942DFE121FF88DBBAE7)
