---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/widget-development-fa
title: JS卡片开发指导（FA模型）
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > JS卡片开发 > JS卡片开发指导（FA模型）
category: harmonyos-guides
scraped_at: 2026-04-29T13:30:06+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:cfa20b133b368b788d7af9e1355fb939babc08bc8a557035ca89dee8ac42189d
---

FA模型从API version 7开始支持，已经不再主推。该应用模型通过导出匿名对象、固定入口文件的方式指定应用组件，开发者无法进行派生，不利于扩展能力。建议使用新的Stage模型进行开发。

## 接口说明

FormAbility生命周期接口如下：

| 接口名 | 描述 |
| --- | --- |
| onCreate(want: Want): formBindingData.FormBindingData | 卡片提供方接收创建卡片的通知接口。 |
| onCastToNormal(formId: string): void | 卡片提供方接收临时卡片转常态卡片的通知接口。 |
| onUpdate(formId: string): void | 卡片提供方接收更新卡片的通知接口。 |
| onVisibilityChange(newStatus: Record<string, number>): void | 卡片提供方接收修改可见性的通知接口。 |
| onEvent(formId: string, message: string): void | 卡片提供方接收处理卡片事件的通知接口。 |
| onDestroy(formId: string): void | 卡片提供方接收销毁卡片的通知接口。 |
| onAcquireFormState?(want: Want): formInfo.FormState | 卡片提供方接收查询卡片状态的通知接口。 |
| onShare?(formId: string): {[key: string]: any} | 卡片提供方接收卡片分享的通知接口。 |
| onShareForm?(formId: string): Record<string, Object> | 卡片提供方接收卡片分享的通知接口。推荐使用该接口替代onShare接口。如果实现了该接口，onShare将不再被回调。 |

FormProvider类有如下API接口，具体的API介绍详见[@ohos.app.form.formProvider (formProvider)](../harmonyos-references/js-apis-app-form-formprovider.md)。

| 接口名 | 描述 |
| --- | --- |
| setFormNextRefreshTime(formId: string, minute: number, callback: AsyncCallback<void>): void; | 设置指定卡片的下一次更新时间，使用callback异步回调。 |
| setFormNextRefreshTime(formId: string, minute: number): Promise<void>; | 设置指定卡片的下一次更新时间，以promise方式返回。 |
| updateForm(formId: string, formBindingData: formBindingData.FormBindingData,callback: AsyncCallback<void>): void; | 更新指定的卡片，使用callback异步回调。 |
| updateForm(formId: string, formBindingData: FormBindingData): Promise<void>; | 更新指定的卡片，以promise方式返回。 |

FormBindingData类有如下API接口，具体的API介绍详见[@ohos.app.form.formBindingData (卡片数据绑定类)](../harmonyos-references/js-apis-app-form-formbindingdata.md)。

| 接口名 | 描述 |
| --- | --- |
| createFormBindingData(obj?: Object | string): FormBindingData | 创建一个FormBindingData对象。 |

## 开发步骤

FA卡片开发，即基于[FA模型](fa-model-development-overview.md)的卡片提供方开发，主要涉及如下关键步骤：

* [实现卡片生命周期接口](widget-development-fa.md#实现卡片生命周期接口)：开发FormAbility生命周期回调函数。
* [配置卡片配置文件](widget-development-fa.md#配置卡片配置文件)：配置应用配置文件config.json。
* [卡片信息的持久化](widget-development-fa.md#卡片信息的持久化)：对卡片信息进行持久化管理。
* [卡片数据交互](widget-development-fa.md#卡片数据交互)：通过updateForm()更新卡片显示的信息。
* [开发卡片页面](widget-development-fa.md#开发卡片页面)：使用HML+CSS+JSON开发JS卡片页面。
* [开发卡片事件](widget-development-fa.md#开发卡片事件)：为卡片添加router事件和message事件。

### 实现卡片生命周期接口

创建FA模型的卡片，需实现卡片的生命周期接口。先参考[DevEco Studio开发服务卡片指南](ide-service-widget.md)生成服务卡片模板。

1. 在form.ts中，导入相关模块

   ```
   1. import type featureAbility from '@ohos.ability.featureAbility';
   2. import type Want from '@ohos.app.ability.Want';
   3. import formBindingData from '@ohos.app.form.formBindingData';
   4. import formInfo from '@ohos.app.form.formInfo';
   5. import formProvider from '@ohos.app.form.formProvider';
   6. import dataPreferences from '@ohos.data.preferences';
   7. import hilog from '@ohos.hilog';
   ```
2. 在form.ts中，实现卡片生命周期接口

   ```
   1. const TAG: string = '[Sample_FAModelAbilityDevelop]';
   2. const domain: number = 0xFF00;

   4. const DATA_STORAGE_PATH: string = 'form_store';
   5. let storeFormInfo = async (formId: string, formName: string, tempFlag: boolean, context: featureAbility.Context): Promise<void> => {
   6. // 此处仅对卡片ID：formId，卡片名：formName和是否为临时卡片：tempFlag进行了持久化
   7. let formInfo: Record<string, string | number | boolean> = {
   8. 'formName': 'formName',
   9. 'tempFlag': 'tempFlag',
   10. 'updateCount': 0
   11. };
   12. try {
   13. const storage = await dataPreferences.getPreferences(context, DATA_STORAGE_PATH);
   14. // put form info
   15. await storage.put(formId, JSON.stringify(formInfo));
   16. hilog.info(domain, TAG, `storeFormInfo, put form info successfully, formId: ${formId}`);
   17. await storage.flush();
   18. } catch (err) {
   19. hilog.error(domain, TAG, `failed to storeFormInfo, err: ${JSON.stringify(err as Error)}`);
   20. }
   21. };

   23. let deleteFormInfo = async (formId: string, context: featureAbility.Context) => {
   24. try {
   25. const storage = await dataPreferences.getPreferences(context, DATA_STORAGE_PATH);
   26. // del form info
   27. await storage.delete(formId);
   28. hilog.info(domain, TAG, `deleteFormInfo, del form info successfully, formId: ${formId}`);
   29. await storage.flush();
   30. } catch (err) {
   31. hilog.error(domain, TAG, `failed to deleteFormInfo, err: ${JSON.stringify(err)}`);
   32. }
   33. }

   35. class LifeCycle {
   36. onCreate: (want: Want) => formBindingData.FormBindingData = (want) => ({ data: '' });
   37. onCastToNormal: (formId: string) => void = (formId) => {
   38. };
   39. onUpdate: (formId: string) => void = (formId) => {
   40. };
   41. onVisibilityChange: (newStatus: Record<string, number>) => void = (newStatus) => {
   42. let obj: Record<string, number> = {
   43. 'test': 1
   44. };
   45. return obj;
   46. };
   47. onEvent: (formId: string, message: string) => void = (formId, message) => {
   48. };
   49. onDestroy: (formId: string) => void = (formId) => {
   50. };
   51. onAcquireFormState?: (want: Want) => formInfo.FormState = (want) => (0);
   52. onShareForm?: (formId: string) => Record<string, Object> = (formId) => {
   53. let obj: Record<string, number> = {
   54. 'test': 1
   55. };
   56. return obj;
   57. };
   58. }

   60. let obj: LifeCycle = {
   61. onCreate(want: Want) {
   62. hilog.info(domain, TAG, 'FormAbility onCreate');
   63. if (want.parameters) {
   64. let formId = String(want.parameters['ohos.extra.param.key.form_identity']);
   65. let formName = String(want.parameters['ohos.extra.param.key.form_name']);
   66. let tempFlag = Boolean(want.parameters['ohos.extra.param.key.form_temporary']);
   67. // 将创建的卡片信息持久化，以便在下次获取/更新该卡片实例时进行使用
   68. // 此接口请根据实际情况实现，具体请参考：FormExtAbility Stage模型卡片实例
   69. hilog.info(domain, TAG, 'FormAbility onCreate' + formId);
   70. storeFormInfo(formId, formName, tempFlag, this.context);
   71. }

   73. // 使用方创建卡片时触发，提供方需要返回卡片数据绑定类
   74. let obj: Record<string, string> = {
   75. 'title': 'titleOnCreate',
   76. 'detail': 'detailOnCreate'
   77. };
   78. let formData: formBindingData.FormBindingData = formBindingData.createFormBindingData(obj);
   79. return formData;
   80. },
   81. onCastToNormal(formId: string) {
   82. // 使用方将临时卡片转换为常态卡片触发，提供方需要做相应的处理，当前卡片使用方不存在临时卡片场景
   83. hilog.info(domain, TAG, 'FormAbility onCastToNormal');
   84. },
   85. onUpdate(formId: string) {
   86. // 若卡片支持定时更新/定点更新/卡片使用方主动请求更新功能，则提供方需要重写该方法以支持数据更新
   87. hilog.info(domain, TAG, 'FormAbility onUpdate');
   88. let obj: Record<string, string> = {
   89. 'title': 'titleOnUpdate',
   90. 'detail': 'detailOnUpdate'
   91. };
   92. let formData: formBindingData.FormBindingData = formBindingData.createFormBindingData(obj);
   93. // 调用updateForm接口去更新对应的卡片，仅更新入参中携带的数据信息，其他信息保持不变
   94. formProvider.updateForm(formId, formData).catch((error: Error) => {
   95. hilog.error(domain, TAG, 'FormAbility updateForm, error:' + JSON.stringify(error));
   96. });
   97. },
   98. onVisibilityChange(newStatus: Record<string, number>) {
   99. // 使用方发起可见或者不可见通知触发，提供方需要做相应的处理，仅系统应用生效
   100. hilog.info(domain, TAG, 'FormAbility onVisibilityChange');
   101. },
   102. onEvent(formId: string, message: string) {
   103. // 若卡片支持触发事件，则需要重写该方法并实现对事件的触发
   104. let obj: Record<string, string> = {
   105. 'title': 'titleOnEvent',
   106. 'detail': 'detailOnEvent'
   107. };
   108. let formData: formBindingData.FormBindingData = formBindingData.createFormBindingData(obj);
   109. // 调用updateForm接口去更新对应的卡片，仅更新入参中携带的数据信息，其他信息保持不变
   110. formProvider.updateForm(formId, formData).catch((error: Error) => {
   111. hilog.error(domain, TAG, 'FormAbility updateForm, error:' + JSON.stringify(error));
   112. });
   113. hilog.info(domain, TAG, 'FormAbility onEvent');
   114. },
   115. onDestroy(formId: string) {
   116. // 删除卡片实例数据
   117. hilog.info(domain, TAG, 'FormAbility onDestroy');
   118. // 删除之前持久化的卡片实例数据
   119. // 此接口请根据实际情况实现，具体请参考：FormExtAbility Stage模型卡片实例
   120. deleteFormInfo(formId, this.context);
   121. },
   122. onAcquireFormState(want: Want) {
   123. hilog.info(domain, TAG, 'FormAbility onAcquireFormState');
   124. return formInfo.FormState.READY;
   125. }
   126. };

   128. export default obj;
   ```

说明

FormAbility不能常驻后台，即在卡片生命周期回调函数中无法处理长时间的任务。

### 配置卡片配置文件

卡片需要在应用配置文件config.json中进行配置。

* JS模块，用于对应卡片的JS相关资源，内部字段结构说明：

  | 属性名称 | 含义 | 数据类型 | 是否可缺省 |
  | --- | --- | --- | --- |
  | name | 表示JS Component的名字。该标签不可缺省，默认值为default。 | 字符串 | 否 |
  | pages | 表示JS Component的页面用于列举JS Component中每个页面的路由信息[页面路径+页面名称]。该标签不可缺省，取值为数组，数组第一个元素代表JS FA首页。 | 数组 | 否 |
  | window | 用于定义与显示窗口相关的配置。 | 对象 | 可缺省，缺省值参考[window标签](arkts-ui-widget-configuration.md#window标签)表格。 |
  | type | 表示JS应用的类型。取值范围如下：  normal：标识该JS Component为应用实例。  form：标识该JS Component为卡片实例。 | 字符串 | 可缺省，缺省值为“normal” 。 |
  | mode | 定义JS组件的开发模式。 | 对象 | 可缺省，缺省值为空。 |

  配置示例如下：

  ```
  1. "js": [
  2. // ...
  3. {
  4. "name": "widget",
  5. "pages": [
  6. "pages/index/index"
  7. ],
  8. "window": {
  9. "designWidth": 720,
  10. "autoDesignWidth": true
  11. },
  12. "type": "form"
  13. }
  14. ]
  ```
* abilities模块，用于对应卡片的FormAbility，内部字段结构说明：

  | 属性名称 | 含义 | 数据类型 | 是否可缺省 |
  | --- | --- | --- | --- |
  | name | 表示卡片的类名。字符串最大长度为127字节。 | 字符串 | 否 |
  | description | 表示卡片的描述。取值可以是描述性内容，也可以是对描述性内容的资源索引，以支持多语言。字符串最大长度为255字节。 | 字符串 | 可缺省，缺省为空。 |
  | isDefault | 表示该卡片是否为默认卡片，每个Ability有且只有一个默认卡片。  true：默认卡片。  false：非默认卡片。 | 布尔值 | 否 |
  | type | 表示卡片的类型。取值范围如下：  JS：JS卡片。 | 字符串 | 否 |
  | colorMode(deprecated) | 表示卡片的主题样式，取值范围如下：  auto：自适应。  dark：深色主题。  light：浅色主题。  **说明：**  从API version 20开始，该接口废弃，卡片主题样式统一跟随系统的颜色模式。 | 字符串 | 可缺省，缺省值为“auto”。 |
  | supportDimensions | 表示卡片支持的外观规格，取值范围：  1 \* 2：表示1行2列的二宫格。  2 \* 2：表示2行2列的四宫格。  2 \* 4：表示2行4列的八宫格。  4 \* 4：表示4行4列的十六宫格。 | 字符串数组 | 否 |
  | defaultDimension | 表示卡片的默认外观规格，取值必须在该卡片supportDimensions配置的列表中。 | 字符串 | 否 |
  | updateEnabled | 表示卡片是否支持周期性刷新，取值范围：  true：表示支持周期性刷新，可以在定时刷新（updateDuration）和定点刷新（scheduledUpdateTime）两种方式任选其一，优先选择定时刷新。  false：表示不支持周期性刷新。 | 布尔类型 | 否 |
  | scheduledUpdateTime | 表示卡片的定点刷新的时刻，采用24小时制，精确到分钟。  updateDuration参数优先级高于scheduledUpdateTime，两者同时配置时，以updateDuration配置的刷新时间为准。 | 字符串 | 可缺省，缺省值为“0:0”，缺省时不进行定点刷新。 |
  | updateDuration | 表示卡片定时刷新的更新周期，单位为30分钟，取值为自然数。  当取值为0时，表示该参数不生效。  当取值为正整数N时，表示刷新周期为30\*N分钟。  updateDuration参数优先级高于scheduledUpdateTime，两者同时配置时，以updateDuration配置的刷新时间为准。 | 数值 | 可缺省，缺省值为0。 |
  | formConfigAbility | 表示卡片的配置跳转链接，采用URI格式。 | 字符串 | 可缺省，缺省值为空。 |
  | formVisibleNotify | 标识是否允许卡片使用卡片可见性通知。 | 字符串 | 可缺省，缺省值为空。 |
  | jsComponentName | 表示JS卡片的Component名称。字符串最大长度为127字节。 | 字符串 | 否 |
  | metaData | 表示卡片的自定义信息，包含customizeData数组标签。 | 对象 | 可缺省，缺省值为空。 |
  | customizeData | 表示自定义的卡片信息。 | 对象数组 | 可缺省，缺省值为空。 |

  配置示例如下：

  ```
  1. "abilities": [
  2. // ...
  3. {
  4. "name": ".FormAbility",
  5. "srcPath": "FormAbility",
  6. "description": "$string:FormAbility_desc",
  7. "icon": "$media:icon",
  8. "label": "$string:FormAbility_label",
  9. "type": "service",
  10. "formsEnabled": true,
  11. "srcLanguage": "ets",
  12. "forms": [
  13. {
  14. "jsComponentName": "widget",
  15. "isDefault": true,
  16. "scheduledUpdateTime": "10:30",
  17. "defaultDimension": "2*2",
  18. "name": "widget",
  19. "description": "This is a service widget.",
  20. "type": "JS",
  21. "formVisibleNotify": true,
  22. "supportDimensions": [
  23. "2*2"
  24. ],
  25. "updateEnabled": true,
  26. "updateDuration": 1
  27. }
  28. ]
  29. },
  30. // ...
  31. ]
  ```

### 卡片信息的持久化

因大部分卡片提供方都不是常驻服务，只有在需要使用时才会被拉起获取卡片信息，且卡片管理服务支持对卡片进行多实例管理，卡片ID对应实例ID，因此若卡片提供方支持对卡片数据进行配置，则需要对卡片的业务数据按照卡片ID进行持久化管理，以便在后续获取、更新以及拉起时能获取到正确的卡片业务数据。且需要适配onDestroy卡片删除通知接口，在其中实现卡片实例数据的删除。

```
1. const TAG: string = '[Sample_FAModelAbilityDevelop]';
2. const domain: number = 0xFF00;

4. const DATA_STORAGE_PATH: string = 'form_store';
5. let storeFormInfo = async (formId: string, formName: string, tempFlag: boolean, context: featureAbility.Context): Promise<void> => {
6. // 此处仅对卡片ID：formId，卡片名：formName和是否为临时卡片：tempFlag进行了持久化
7. let formInfo: Record<string, string | number | boolean> = {
8. 'formName': 'formName',
9. 'tempFlag': 'tempFlag',
10. 'updateCount': 0
11. };
12. try {
13. const storage = await dataPreferences.getPreferences(context, DATA_STORAGE_PATH);
14. // put form info
15. await storage.put(formId, JSON.stringify(formInfo));
16. hilog.info(domain, TAG, `storeFormInfo, put form info successfully, formId: ${formId}`);
17. await storage.flush();
18. } catch (err) {
19. hilog.error(domain, TAG, `failed to storeFormInfo, err: ${JSON.stringify(err as Error)}`);
20. }
21. };

23. let deleteFormInfo = async (formId: string, context: featureAbility.Context) => {
24. try {
25. const storage = await dataPreferences.getPreferences(context, DATA_STORAGE_PATH);
26. // del form info
27. await storage.delete(formId);
28. hilog.info(domain, TAG, `deleteFormInfo, del form info successfully, formId: ${formId}`);
29. await storage.flush();
30. } catch (err) {
31. hilog.error(domain, TAG, `failed to deleteFormInfo, err: ${JSON.stringify(err)}`);
32. }
33. }

35. // ...
36. onCreate(want: Want) {
37. hilog.info(domain, TAG, 'FormAbility onCreate');
38. if (want.parameters) {
39. let formId = String(want.parameters['ohos.extra.param.key.form_identity']);
40. let formName = String(want.parameters['ohos.extra.param.key.form_name']);
41. let tempFlag = Boolean(want.parameters['ohos.extra.param.key.form_temporary']);
42. // 将创建的卡片信息持久化，以便在下次获取/更新该卡片实例时进行使用
43. // 此接口请根据实际情况实现，具体请参考：FormExtAbility Stage模型卡片实例
44. hilog.info(domain, TAG, 'FormAbility onCreate' + formId);
45. storeFormInfo(formId, formName, tempFlag, this.context);
46. }

48. // 使用方创建卡片时触发，提供方需要返回卡片数据绑定类
49. let obj: Record<string, string> = {
50. 'title': 'titleOnCreate',
51. 'detail': 'detailOnCreate'
52. };
53. let formData: formBindingData.FormBindingData = formBindingData.createFormBindingData(obj);
54. return formData;
55. },
56. // ...

58. let deleteFormInfo = async (formId: string, context: featureAbility.Context): Promise<void> => {
59. try {
60. const storage = await dataPreferences.getPreferences(context, DATA_STORAGE_PATH);
61. // del form info
62. await storage.delete(formId);
63. hilog.info(domain, TAG, `deleteFormInfo, del form info successfully, formId: ${formId}`);
64. await storage.flush();
65. } catch (err) {
66. hilog.error(domain, TAG, `failed to deleteFormInfo, err: ${JSON.stringify(err)}`);
67. }
68. };

70. // ...
71. // 适配onDestroy卡片删除通知接口，在其中实现卡片实例数据的删除。
72. onDestroy(formId: string) {
73. // 删除卡片实例数据
74. hilog.info(domain, TAG, 'FormAbility onDestroy');
75. // 删除之前持久化的卡片实例数据
76. // 此接口请根据实际情况实现，具体请参考：FormExtAbility Stage模型卡片实例
77. deleteFormInfo(formId, this.context);
78. }
79. // ...
```

具体的持久化方法可以参考[应用数据持久化概述](app-data-persistence-overview.md)。

需要注意的是，卡片使用方在请求卡片时传递给提供方应用的Want数据中存在临时标记字段，表示此次请求的卡片是否为临时卡片：

* 常态卡片：卡片使用方会持久化的卡片。如添加到桌面的卡片。
* 临时卡片：卡片使用方不会持久化的卡片。当前卡片使用方不存在临时卡片场景。

临时卡片转常态卡片：上划卡片应用后，此时会显示的卡片为临时卡片；点击卡片上的“图钉”按钮后添加到桌面，此时卡片转为常态卡片。

由于临时卡片的数据具有非持久化的特殊性，某些场景例如卡片服务框架死亡重启，此时临时卡片数据在卡片管理服务中已经删除，且对应的卡片ID不会通知到提供方，所以卡片提供方需要自己负责清理长时间未删除的临时卡片数据。同时对应的卡片使用方可能会将之前请求的临时卡片转换为常态卡片。如果转换成功，卡片提供方也需要对对应的临时卡片ID进行处理，把卡片提供方记录的临时卡片数据转换为常态卡片数据，防止提供方在清理长时间未删除的临时卡片时，把已经转换为常态卡片的临时卡片信息删除，导致卡片信息丢失。

### 卡片数据交互

当卡片应用需要更新数据时（如触发了定时更新或定点更新），卡片应用获取最新数据，并调用updateForm()接口更新主动触发卡片的更新。

```
1. const TAG: string = '[Sample_FAModelAbilityDevelop]';
2. const domain: number = 0xFF00;

4. onUpdate(formId: string) {
5. // 若卡片支持定时更新/定点更新/卡片使用方主动请求更新功能，则提供方需要重写该方法以支持数据更新
6. hilog.info(domain, TAG, 'FormAbility onUpdate');
7. let obj: Record<string, string> = {
8. 'title': 'titleOnUpdate',
9. 'detail': 'detailOnUpdate'
10. };
11. let formData: formBindingData.FormBindingData = formBindingData.createFormBindingData(obj);
12. // 调用updateForm接口去更新对应的卡片，仅更新入参中携带的数据信息，其他信息保持不变
13. formProvider.updateForm(formId, formData).catch((error: Error) => {
14. hilog.error(domain, TAG, 'FormAbility updateForm, error:' + JSON.stringify(error));
15. });
16. }
```

### 开发卡片页面

开发者可以使用类Web范式（HML+CSS+JSON）开发JS卡片页面。生成如下卡片页面，可以这样配置卡片页面文件：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/qm5i1TLNQkOVzy8Yks9cZQ/zh-cn_image_0000002589244619.png?HW-CC-KV=V1&HW-CC-Date=20260429T053004Z&HW-CC-Expire=86400&HW-CC-Sign=E9044159D5AB46AB5C7838B61930A89FBBF98D1867BE8E0788E39FEEEFAC7AA2)

说明

FA模型当前仅支持JS扩展的类Web开发范式来实现卡片的UI。

* HML：使用类Web范式的组件描述卡片的页面信息。

  ```
  1. <div class="container">
  2. <stack>
  3. <div class="container-img">
  4. <image src="/common/widget.png" class="bg-img"></image>
  5. <image src="/common/rect.png" class="bottom-img"></image>
  6. </div>
  7. <div class="container-inner">
  8. <text class="title" onclick="routerEvent">{{title}}</text>
  9. <text class="detail_text" onclick="messageEvent">{{detail}}</text>
  10. </div>
  11. </stack>
  12. </div>
  ```
* CSS：HML中类Web范式组件的样式信息。

  ```
  1. .container {
  2. flex-direction: column;
  3. justify-content: center;
  4. align-items: center;
  5. }

  7. .bg-img {
  8. flex-shrink: 0;
  9. height: 100%;
  10. z-index: 1;
  11. }

  13. .bottom-img {
  14. position: absolute;
  15. width: 150px;
  16. height: 56px;
  17. top: 63%;
  18. background-color: rgba(216, 216, 216, 0.15);
  19. filter: blur(20px);
  20. z-index: 2;
  21. }

  23. .container-inner {
  24. flex-direction: column;
  25. justify-content: flex-end;
  26. align-items: flex-start;
  27. height: 100%;
  28. width: 100%;
  29. padding: 12px;
  30. }

  32. .title {
  33. font-family: HarmonyHeiTi-Medium;
  34. font-size: 14px;
  35. color: rgba(255,255,255,0.90);
  36. letter-spacing: 0.6px;
  37. }

  39. .detail_text {
  40. font-family: HarmonyHeiTi;
  41. font-size: 12px;
  42. color: rgba(255,255,255,0.60);
  43. letter-spacing: 0.51px;
  44. text-overflow: ellipsis;
  45. max-lines: 1;
  46. margin-top: 6px;
  47. }
  ```
* JSON：卡片页面中的数据和事件交互。

  ```
  1. {
  2. "data": {
  3. "title": "TitleDefault",
  4. "detail": "TextDefault"
  5. },
  6. "actions": {
  7. "routerEvent": {
  8. "action": "router",
  9. "abilityName": "com.samples.famodelabilitydevelop.MainAbility",
  10. "params": {
  11. "message": "add detail"
  12. }
  13. },
  14. "messageEvent": {
  15. "action": "message",
  16. "params": {
  17. "message": "add detail"
  18. }
  19. }
  20. }
  21. }
  ```

### 开发卡片事件

卡片支持为组件设置交互事件(action)，包括router事件和message事件，其中router事件用于Ability跳转，message事件用于卡片开发人员自定义点击事件。关键步骤说明如下：

1. 在hml中为组件设置onclick属性，其值对应到json文件的actions字段中。
2. 如何设置router事件：

   * action属性值为"router"；
   * abilityName为跳转目标的Ability名（支持跳转FA模型的PageAbility组件和Stage模型的UIAbility组件），如目前DevEco创建的FA模型的UIAbility默认名为com.example.entry.EntryAbility；
   * params为传递给跳转目标Ability的自定义参数，可以按需填写。其值可以在目标Ability启动时的want中的parameters里获取。如FA模型EntryAbility的onCreate生命周期里可以通过featureAbility.getWant()获取到want，然后在其parameters字段下获取到配置的参数；
3. 如何设置message事件：

   * action属性值为"message"；
   * params为message事件的用户自定义参数，可以按需填写。其值可以在卡片生命周期函数onEvent中的message里获取；

示例如下：

* hml文件

  ```
  1. <div class="container">
  2. <stack>
  3. <div class="container-img">
  4. <image src="/common/widget.png" class="bg-img"></image>
  5. <image src="/common/rect.png" class="bottom-img"></image>
  6. </div>
  7. <div class="container-inner">
  8. <text class="title" onclick="routerEvent">{{title}}</text>
  9. <text class="detail_text" onclick="messageEvent">{{detail}}</text>
  10. </div>
  11. </stack>
  12. </div>
  ```
* css文件

  ```
  1. .container {
  2. flex-direction: column;
  3. justify-content: center;
  4. align-items: center;
  5. }

  7. .bg-img {
  8. flex-shrink: 0;
  9. height: 100%;
  10. z-index: 1;
  11. }

  13. .bottom-img {
  14. position: absolute;
  15. width: 150px;
  16. height: 56px;
  17. top: 63%;
  18. background-color: rgba(216, 216, 216, 0.15);
  19. filter: blur(20px);
  20. z-index: 2;
  21. }

  23. .container-inner {
  24. flex-direction: column;
  25. justify-content: flex-end;
  26. align-items: flex-start;
  27. height: 100%;
  28. width: 100%;
  29. padding: 12px;
  30. }

  32. .title {
  33. font-family: HarmonyHeiTi-Medium;
  34. font-size: 14px;
  35. color: rgba(255,255,255,0.90);
  36. letter-spacing: 0.6px;
  37. }

  39. .detail_text {
  40. font-family: HarmonyHeiTi;
  41. font-size: 12px;
  42. color: rgba(255,255,255,0.60);
  43. letter-spacing: 0.51px;
  44. text-overflow: ellipsis;
  45. max-lines: 1;
  46. margin-top: 6px;
  47. }
  ```
* json文件

  ```
  1. {
  2. "data": {
  3. "title": "TitleDefault",
  4. "detail": "TextDefault"
  5. },
  6. "actions": {
  7. "routerEvent": {
  8. "action": "router",
  9. "abilityName": "com.samples.famodelabilitydevelop.MainAbility",
  10. "params": {
  11. "message": "add detail"
  12. }
  13. },
  14. "messageEvent": {
  15. "action": "message",
  16. "params": {
  17. "message": "add detail"
  18. }
  19. }
  20. }
  21. }
  ```
