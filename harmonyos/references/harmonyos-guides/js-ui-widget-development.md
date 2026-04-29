---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/js-ui-widget-development
title: JS卡片开发指导（Stage模型）
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > JS卡片开发 > JS卡片开发指导（Stage模型）
category: harmonyos-guides
scraped_at: 2026-04-29T13:30:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1148482c73bfcf656b0a54badd9eb54f6cbe7d666e935b97c34562a17a4b923c
---

Stage模型是从API version 9开始支持，目前主推且会长期演进的模型。该模型采用面向对象的方式，将应用组件以类接口的形式开放给开发者，可以进行派生，利于扩展能力。

## 接口说明

FormExtensionAbility类拥有如下API接口，具体的API介绍详见[@ohos.app.form.FormExtensionAbility (FormExtensionAbility)](../harmonyos-references/js-apis-app-form-formextensionability.md)。

| 接口名 | 描述 |
| --- | --- |
| onAddForm(want: Want): formBindingData.FormBindingData | 卡片提供方接收创建卡片的通知接口。 |
| onCastToNormalForm(formId: string): void | 卡片提供方接收临时卡片转常态卡片的通知接口。 |
| onUpdateForm(formId: string, wantParams?: Record<string, Object>): void | 卡片提供方接收更新卡片的通知接口。 |
| onChangeFormVisibility(newStatus: Record<string, number>): void | 卡片提供方接收修改可见性的通知接口。 |
| onFormEvent(formId: string, message: string): void | 卡片提供方接收处理卡片事件的通知接口。 |
| onRemoveForm(formId: string): void | 卡片提供方接收销毁卡片的通知接口。 |
| onConfigurationUpdate(newConfig: Configuration): void | 当系统配置更新时调用。 |

formProvider类部分API接口如下，具体的API介绍详见[@ohos.app.form.formProvider (formProvider)](../harmonyos-references/js-apis-app-form-formprovider.md)。

| 接口名 | 描述 |
| --- | --- |
| setFormNextRefreshTime(formId: string, minute: number, callback: AsyncCallback<void>): void | 设置指定卡片的下一次更新时间，使用callback异步回调。 |
| setFormNextRefreshTime(formId: string, minute: number): Promise<void> | 设置指定卡片的下一次更新时间，使用Promise异步回调。 |
| updateForm(formId: string, formBindingData: formBindingData.FormBindingData, callback: AsyncCallback<void>): void | 更新指定的卡片，使用callback异步回调。 |
| updateForm(formId: string, formBindingData: formBindingData.FormBindingData): Promise<void> | 更新指定的卡片，使用Promise异步回调。 |

formBindingData类部分API接口如下，具体的API介绍详见[@ohos.app.form.formBindingData (卡片数据绑定类)](../harmonyos-references/js-apis-app-form-formbindingdata.md)。

| 接口名 | 描述 |
| --- | --- |
| createFormBindingData(obj?: Object | string): FormBindingData | 创建一个FormBindingData对象。 |

## 开发步骤

Stage卡片开发，即基于[Stage模型](stage-model-development-overview.md)的卡片提供方开发，主要涉及如下关键步骤：

* [创建卡片FormExtensionAbility](js-ui-widget-development.md#创建卡片formextensionability)：卡片生命周期回调函数FormExtensionAbility开发。
* [配置卡片配置文件](js-ui-widget-development.md#配置卡片配置文件)：配置应用配置文件module.json5和profile配置文件。
* [卡片信息的持久化](js-ui-widget-development.md#卡片信息的持久化)：对卡片信息进行持久化管理。
* [卡片数据交互](js-ui-widget-development.md#卡片数据交互)：通过updateForm更新卡片显示的信息。
* [开发卡片页面](js-ui-widget-development.md#开发卡片页面)：使用HML+CSS+JSON开发JS卡片页面。
* [开发卡片事件](js-ui-widget-development.md#开发卡片事件)：为卡片添加router事件和message事件。

### 创建卡片FormExtensionAbility

创建Stage模型的卡片，需实现FormExtensionAbility生命周期接口。先参考[DevEco Studio服务卡片开发指南](ide-service-widget.md)生成服务卡片模板。

1. 在JsCardFormAbility.ets中，导入相关模块。

   ```
   1. // entry/src/main/ets/jscardformability/JsCardFormAbility.ets
   2. import { common, Want } from '@kit.AbilityKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   4. import { formBindingData, FormExtensionAbility, formProvider } from '@kit.FormKit';
   5. import { BusinessError } from '@kit.BasicServicesKit';
   6. import { preferences } from '@kit.ArkData';
   ```
2. 在JsCardFormAbility.ets中，实现FormExtension生命周期接口。

   ```
   1. // entry/src/main/ets/jscardformability/JsCardFormAbility.ets
   2. const TAG: string = 'JsCardFormAbility';
   3. const DATA_STORAGE_PATH: string = '/data/storage/el2/base/haps/form_store';
   4. const DOMAIN_NUMBER: number = 0xFF00;
   5. let storeFormInfo =
   6. async (formId: string, formName: string, tempFlag: boolean, context: common.FormExtensionContext): Promise<void> => {
   7. // 此处仅对卡片ID：formId，卡片名：formName和是否为临时卡片：tempFlag进行了持久化
   8. let formInfo: Record<string, string | boolean | number> = {
   9. 'formName': formName,
   10. 'tempFlag': tempFlag,
   11. 'updateCount': 0
   12. };
   13. try {
   14. const storage: preferences.Preferences = await preferences.getPreferences(context, DATA_STORAGE_PATH);
   15. // put form info
   16. await storage.put(formId, JSON.stringify(formInfo));
   17. hilog.info(DOMAIN_NUMBER, TAG, `[EntryFormAbility] storeFormInfo, put form info successfully, formId: ${formId}`);
   18. await storage.flush();
   19. } catch (err) {
   20. hilog.error(DOMAIN_NUMBER, TAG, `[EntryFormAbility] failed to storeFormInfo,
   21. err: ${JSON.stringify(err as BusinessError)}`);
   22. }
   23. }
   24. let deleteFormInfo = async (formId: string, context: common.FormExtensionContext): Promise<void> => {
   25. try {
   26. const storage: preferences.Preferences = await preferences.getPreferences(context, DATA_STORAGE_PATH);
   27. // del form info
   28. await storage.delete(formId);
   29. hilog.info(DOMAIN_NUMBER, TAG, `[EntryFormAbility] deleteFormInfo, del form info successfully, formId: ${formId}`);
   30. await storage.flush();
   31. } catch (err) {
   32. hilog.error(DOMAIN_NUMBER, TAG, `[EntryFormAbility] failed to deleteFormInfo,
   33. err: ${JSON.stringify(err as BusinessError)}`);
   34. }
   35. };

   38. export default class JsCardFormAbility extends FormExtensionAbility {
   39. onAddForm(want: Want): formBindingData.FormBindingData {
   40. hilog.info(DOMAIN_NUMBER, TAG, '[JsCardFormAbility] onAddForm');

   42. if (want.parameters) {
   43. let formId = JSON.stringify(want.parameters['ohos.extra.param.key.form_identity']);
   44. let formName = JSON.stringify(want.parameters['ohos.extra.param.key.form_name']);
   45. let tempFlag = want.parameters['ohos.extra.param.key.form_temporary'] as boolean;
   46. // 将创建的卡片信息持久化，以便在下次获取/更新该卡片实例时进行使用
   47. storeFormInfo(formId, formName, tempFlag, this.context);
   48. }

   50. let obj: Record<string, string> = {
   51. 'title': 'titleOnCreate',
   52. 'detail': 'detailOnCreate'
   53. };
   54. let formData: formBindingData.FormBindingData = formBindingData.createFormBindingData(obj);
   55. return formData;
   56. }

   58. onRemoveForm(formId: string): void {
   59. // 删除卡片实例数据
   60. hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onRemoveForm');
   61. // 删除之前持久化的卡片实例数据
   62. deleteFormInfo(formId, this.context);
   63. }

   65. onUpdateForm(formId: string): void {
   66. // 若卡片支持定时更新/定点更新/卡片使用方主动请求更新功能，则卡片提供方需要重写该方法以支持数据更新
   67. hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onUpdateForm');
   68. let obj: Record<string, string> = {
   69. 'title': 'titleOnUpdate',
   70. 'detail': 'detailOnUpdate'
   71. };
   72. let formData: formBindingData.FormBindingData = formBindingData.createFormBindingData(obj);
   73. formProvider.updateForm(formId, formData).catch((error: BusinessError) => {
   74. hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] updateForm, error:' + JSON.stringify(error));
   75. });
   76. }

   78. onFormEvent(formId: string, message: string): void {
   79. // 若卡片支持触发事件，则需要重写该方法并实现对事件的触发
   80. hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onFormEvent');
   81. // 获取message事件中传递的detail参数
   82. let msg: Record<string, string> = JSON.parse(message);
   83. if (msg.detail === 'message detail') {
   84. // 执行业务逻辑，由用户自行实现
   85. hilog.info(DOMAIN_NUMBER, TAG, 'message info:' + msg.detail);
   86. }
   87. }

   89. }
   ```

说明

FormExtensionAbility不能常驻后台，即在卡片生命周期回调函数中无法处理长时间的任务。

### 配置卡片配置文件

1. 卡片需要在[module.json5配置文件](module-configuration-file.md)中的extensionAbilities标签下，配置ExtensionAbility相关信息。FormExtensionAbility需要填写metadata元信息标签，其中键名称为固定字符串"ohos.extension.form"，资源为卡片的具体配置信息的索引。

   配置示例如下：

   ```
   1. {
   2. "module": {
   3. // ...
   4. "extensionAbilities": [
   5. {
   6. "name": "JsCardFormAbility",
   7. "srcEntry": "./ets/jscardformability/JsCardFormAbility.ets",
   8. "description": "$string:JSCardFormAbility_desc",
   9. "label": "$string:JSCardFormAbility_label",
   10. "type": "form",
   11. "metadata": [
   12. {
   13. "name": "ohos.extension.form",
   14. "resource": "$profile:form_jscard_config"
   15. }
   16. ]
   17. }
   18. ]
   19. }
   20. }
   ```
2. 卡片的具体配置信息。在上述FormExtensionAbility的元信息（"metadata"配置项）中，可以指定卡片具体配置信息的资源索引。例如当resource指定为$profile:form\_jscard\_config时，会使用开发视图的resources/base/profile/目录下的form\_jscard\_config.json作为卡片profile配置文件。内部字段结构说明如下表所示。

   **表1** 卡片profile配置文件

   | 属性名称 | 含义 | 数据类型 | 是否可缺省 |
   | --- | --- | --- | --- |
   | name | 表示卡片的类名，字符串最大长度为127字节。 | 字符串 | 否 |
   | description | 表示卡片的描述。取值可以是描述性内容，也可以是对描述性内容的资源索引，以支持多语言。字符串最大长度为255字节。 | 字符串 | 可缺省，缺省为空。 |
   | src | 表示卡片对应的UI代码的完整路径。 | 字符串 | 否 |
   | window | 用于定义与显示窗口相关的配置。 | 对象 | 可缺省，缺省值参考[window标签](arkts-ui-widget-configuration.md#window标签)表格。 |
   | isDefault | 表示该卡片是否为默认卡片，每个UIAbility有且只有一个默认卡片。  - true：默认卡片。  - false：非默认卡片。 | 布尔值 | 否 |
   | colorMode(deprecated) | 表示卡片的主题样式，取值范围如下：  - auto：跟随系统的颜色模式值选取主题。  - dark：深色主题。  - light：浅色主题。  **说明：**  1. 从API version 12开始支持该配置项，从API version 20开始废弃该配置项，卡片主题样式统一跟随系统的颜色模式。 | 字符串 | 可缺省，缺省值为“auto”。 |
   | supportDimensions | 表示卡片支持的外观规格，取值范围：  - 1 \* 1：表示1行1列的一宫格。  - 1 \* 2：表示1行2列的二宫格。  - 2 \* 2：表示2行2列的四宫格。  - 2 \* 4：表示2行4列的八宫格。  - 2 \* 3：表示2行3列的六宫格。  - 3 \* 3：表示3行3列的九宫格。  - 4 \* 4：表示4行4列的十六宫格。  - 6 \* 4：表示6行4列的二十四宫格。  **说明**： 2 \* 3和 3 \* 3仅支持手表设备， 1 \* 1只支持在锁屏上使用。 | 字符串数组 | 否 |
   | defaultDimension | 表示卡片的默认外观规格，取值必须在该卡片supportDimensions配置的列表中。 | 字符串 | 否 |
   | updateEnabled | 表示卡片是否支持周期性刷新，取值范围：  - true：表示支持周期性刷新，可以在定时刷新（updateDuration）和定点刷新（scheduledUpdateTime）两种方式任选其一，优先选择定时刷新。  - false：表示不支持周期性刷新。 | 布尔类型 | 否 |
   | scheduledUpdateTime | 表示卡片的定点刷新的时刻，采用24小时制，精确到分钟。  updateDuration参数优先级高于scheduledUpdateTime，两者同时配置时，以updateDuration配置的刷新时间为准。 | 字符串 | 可缺省，缺省值为“0:0”，缺省时不进行定点刷新。 |
   | updateDuration | 表示卡片定时刷新的更新周期，单位为30分钟，取值为自然数。  当取值为0时，表示该参数不生效。  当取值为正整数N时，表示刷新周期为30\*N分钟。  updateDuration参数优先级高于scheduledUpdateTime，两者同时配置时，以updateDuration配置的刷新时间为准。 | 数值 | 可缺省，缺省值为0。 |
   | formConfigAbility | 表示卡片的配置跳转链接，采用URI格式。 | 字符串 | 可缺省，缺省值为空。 |
   | formVisibleNotify | 标识是否允许卡片使用卡片可见性通知。 | 字符串 | 可缺省，缺省值为空。 |
   | metaData | 表示卡片的自定义信息，包含customizeData数组标签。 | 对象 | 可缺省，缺省值为空。 |

   配置示例如下：

   ```
   1. {
   2. "forms": [
   3. {
   4. "name": "WidgetJS",
   5. "description": "$string:JSCardEntryAbility_desc",
   6. "src": "./js/WidgetJS/pages/index/index",
   7. "window": {
   8. "designWidth": 720,
   9. "autoDesignWidth": true
   10. },
   11. "isDefault": true,
   12. "updateEnabled": true,
   13. "scheduledUpdateTime": "10:30",
   14. "updateDuration": 1,
   15. "defaultDimension": "2*2",
   16. "supportDimensions": [
   17. "2*2"
   18. ]
   19. }
   20. ]
   21. }
   ```

### 卡片信息的持久化

因大部分卡片提供方都不是常驻服务，只有在需要使用时才会被拉起获取卡片信息，且卡片管理服务支持对卡片进行多实例管理，卡片ID对应实例ID，因此若卡片提供方支持对卡片数据进行配置，则需要对卡片的业务数据按照卡片ID进行持久化管理，以便在后续获取、更新以及拉起时能获取到正确的卡片业务数据。

代码导入请参考[创建卡片FormExtensionAbility](js-ui-widget-development.md#创建卡片formextensionability)中的导入模块。

```
1. // entry/src/main/ets/jscardformability/JsCardFormAbility.ets
2. const TAG: string = 'JsCardFormAbility';
3. const DATA_STORAGE_PATH: string = '/data/storage/el2/base/haps/form_store';
4. const DOMAIN_NUMBER: number = 0xFF00;
5. let storeFormInfo =
6. async (formId: string, formName: string, tempFlag: boolean, context: common.FormExtensionContext): Promise<void> => {
7. // 此处仅对卡片ID：formId，卡片名：formName和是否为临时卡片：tempFlag进行了持久化
8. let formInfo: Record<string, string | boolean | number> = {
9. 'formName': formName,
10. 'tempFlag': tempFlag,
11. 'updateCount': 0
12. };
13. try {
14. const storage: preferences.Preferences = await preferences.getPreferences(context, DATA_STORAGE_PATH);
15. // put form info
16. await storage.put(formId, JSON.stringify(formInfo));
17. hilog.info(DOMAIN_NUMBER, TAG, `[EntryFormAbility] storeFormInfo, put form info successfully, formId: ${formId}`);
18. await storage.flush();
19. } catch (err) {
20. hilog.error(DOMAIN_NUMBER, TAG, `[EntryFormAbility] failed to storeFormInfo,
21. err: ${JSON.stringify(err as BusinessError)}`);
22. }
23. }
24. // ...

26. export default class JsCardFormAbility extends FormExtensionAbility {
27. onAddForm(want: Want): formBindingData.FormBindingData {
28. hilog.info(DOMAIN_NUMBER, TAG, '[JsCardFormAbility] onAddForm');

30. if (want.parameters) {
31. let formId = JSON.stringify(want.parameters['ohos.extra.param.key.form_identity']);
32. let formName = JSON.stringify(want.parameters['ohos.extra.param.key.form_name']);
33. let tempFlag = want.parameters['ohos.extra.param.key.form_temporary'] as boolean;
34. // 将创建的卡片信息持久化，以便在下次获取/更新该卡片实例时进行使用
35. storeFormInfo(formId, formName, tempFlag, this.context);
36. }

38. let obj: Record<string, string> = {
39. 'title': 'titleOnCreate',
40. 'detail': 'detailOnCreate'
41. };
42. let formData: formBindingData.FormBindingData = formBindingData.createFormBindingData(obj);
43. return formData;
44. }

46. // ...
47. }
```

且需要适配onRemoveForm卡片删除通知接口，在其中实现卡片实例数据的删除。

```
1. // entry/src/main/ets/jscardformability/JsCardFormAbility.ets
2. const TAG: string = 'JsCardFormAbility';
3. const DATA_STORAGE_PATH: string = '/data/storage/el2/base/haps/form_store';
4. const DOMAIN_NUMBER: number = 0xFF00;
5. // ...
6. let deleteFormInfo = async (formId: string, context: common.FormExtensionContext): Promise<void> => {
7. try {
8. const storage: preferences.Preferences = await preferences.getPreferences(context, DATA_STORAGE_PATH);
9. // del form info
10. await storage.delete(formId);
11. hilog.info(DOMAIN_NUMBER, TAG, `[EntryFormAbility] deleteFormInfo, del form info successfully, formId: ${formId}`);
12. await storage.flush();
13. } catch (err) {
14. hilog.error(DOMAIN_NUMBER, TAG, `[EntryFormAbility] failed to deleteFormInfo,
15. err: ${JSON.stringify(err as BusinessError)}`);
16. }
17. };

20. export default class JsCardFormAbility extends FormExtensionAbility {
21. // ...
22. onRemoveForm(formId: string): void {
23. // 删除卡片实例数据
24. hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onRemoveForm');
25. // 删除之前持久化的卡片实例数据
26. deleteFormInfo(formId, this.context);
27. }

29. // ...
30. }
```

具体的持久化方法可以参考[轻量级数据存储开发指导](app-data-persistence-overview.md)。

需要注意的是，卡片使用方在请求卡片时传递给提供方应用的Want数据中存在临时标记字段，表示此次请求的卡片是否为临时卡片：

* 常态卡片：卡片使用方会持久化的卡片。
* 临时卡片：卡片使用方不会持久化的卡片，当前卡片使用方不存在临时卡片场景。

由于临时卡片的数据具有非持久化的特殊性，某些场景例如卡片服务框架死亡重启，此时临时卡片数据在卡片管理服务中已经删除，且对应的卡片ID不会通知到提供方，所以卡片提供方需要自己负责清理长时间未删除的临时卡片数据。同时对应的卡片使用方可能会将之前请求的临时卡片转换为常态卡片。如果转换成功，卡片提供方也需要对对应的临时卡片ID进行处理，把卡片提供方记录的临时卡片数据转换为常态卡片数据，防止提供方在清理长时间未删除的临时卡片时，把已经转换为常态卡片的临时卡片信息删除，导致卡片信息丢失。

### 卡片数据交互

当卡片应用需要更新数据时（如触发了定时更新或定点更新），卡片应用获取最新数据，并调用updateForm()接口主动触发卡片的更新。

代码导入请参考[创建卡片FormExtensionAbility](js-ui-widget-development.md#创建卡片formextensionability)中的导入模块。

```
1. // entry/src/main/ets/jscardformability/JsCardFormAbility.ets
2. const TAG: string = 'JsCardFormAbility';
3. // ...
4. const DOMAIN_NUMBER: number = 0xFF00;
5. // ...

7. export default class JsCardFormAbility extends FormExtensionAbility {
8. // ...
9. onUpdateForm(formId: string): void {
10. // 若卡片支持定时更新/定点更新/卡片使用方主动请求更新功能，则卡片提供方需要重写该方法以支持数据更新
11. hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onUpdateForm');
12. let obj: Record<string, string> = {
13. 'title': 'titleOnUpdate',
14. 'detail': 'detailOnUpdate'
15. };
16. let formData: formBindingData.FormBindingData = formBindingData.createFormBindingData(obj);
17. formProvider.updateForm(formId, formData).catch((error: BusinessError) => {
18. hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] updateForm, error:' + JSON.stringify(error));
19. });
20. }

22. // ...
23. }
```

### 开发卡片页面

开发者可以使用类Web范式（HML+CSS+JSON）开发JS卡片页面。生成如下卡片页面，可以这样配置卡片页面文件：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/K3f6fRK5T86RZreO9-NO2A/zh-cn_image_0000002589324681.png?HW-CC-KV=V1&HW-CC-Date=20260429T053001Z&HW-CC-Expire=86400&HW-CC-Sign=B368B03018D3FD4A479DBEB91D6B6AA57A1151ECFB9017DD4AD708E8D28BE60B)

* HML：使用类Web范式的组件描述卡片的页面信息。

  ```
  1. <div class="container">
  2. <stack>
  3. <div class="container-img">
  4. <image src="/common/widget.png" class="bg-img"></image>
  5. </div>
  6. <div class="container-inner">
  7. <text class="title">{{title}}</text>
  8. <text class="detail_text" onclick="routerEvent">{{detail}}</text>
  9. </div>
  10. </stack>
  11. </div>
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
  10. }

  12. .container-inner {
  13. flex-direction: column;
  14. justify-content: flex-end;
  15. align-items: flex-start;
  16. height: 100%;
  17. width: 100%;
  18. padding: 12px;
  19. }

  21. .title {
  22. font-size: 19px;
  23. font-weight: bold;
  24. color: white;
  25. text-overflow: ellipsis;
  26. max-lines: 1;
  27. }

  29. .detail_text {
  30. font-size: 16px;
  31. color: white;
  32. opacity: 0.66;
  33. text-overflow: ellipsis;
  34. max-lines: 1;
  35. margin-top: 6px;
  36. }
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
  9. "abilityName": "EntryAbility",
  10. "params": {
  11. "message": "add detail"
  12. }
  13. }
  14. }
  15. }
  ```

### 开发卡片事件

卡片支持为组件设置交互事件（action），包括router事件和message事件，其中router事件用于UIAbility跳转，message事件用于卡片开发人员自定义点击事件。

关键步骤说明如下：

1. 在HML中为组件设置onclick属性，其值对应到JSON文件的actions字段中。
2. 设置router事件：

   * action属性值为"router"。
   * abilityName为跳转目标的UIAbility名（支持跳转FA模型的PageAbility组件和Stage模型的UIAbility组件），如目前DevEco Studio创建的Stage模型的UIAbility默认名为EntryAbility。
   * params为传递给跳转目标UIAbility的自定义参数，可以按需填写。其值可以在目标UIAbility启动时的want中的parameters里获取。如Stage模型MainAbility的onCreate生命周期里的入参want的parameters字段下获取到配置的参数。
3. 设置message事件：

   * action属性值为"message"。
   * params为message事件的用户自定义参数，可以按需填写。其值可以在卡片生命周期函数onFormEvent()中的message里获取。

示例如下。

* HML文件

  ```
  1. <div class="container">
  2. <stack>
  3. <div class="container-img">
  4. <image src="/common/CardWebImg.png" class="bg-img"></image>
  5. <image src="/common/CardWebImgMatrix.png"
  6. class="bottom-img"/>
  7. </div>
  8. <div class="container-inner">
  9. <text class="title" onclick="routerEvent">{{ title }}</text>
  10. <text class="detail_text" onclick="messageEvent">{{ detail }}</text>
  11. </div>
  12. </stack>
  13. </div>
  ```
* CSS文件

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
  35. color: rgba(255, 255, 255, 0.90);
  36. letter-spacing: 0.6px;
  37. font-weight: 500;
  38. width: 100%;
  39. text-overflow: ellipsis;
  40. max-lines: 1;
  41. }

  43. .detail_text {
  44. font-family: HarmonyHeiTi;
  45. font-size: 12px;
  46. color: rgba(255, 255, 255, 0.60);
  47. letter-spacing: 0.51px;
  48. font-weight: 400;
  49. text-overflow: ellipsis;
  50. max-lines: 1;
  51. margin-top: 6px;
  52. width: 100%;
  53. }
  ```
* JSON文件

  ```
  1. {
  2. "data": {
  3. "title": "TitleDefault",
  4. "detail": "TextDefault"
  5. },
  6. "actions": {
  7. "routerEvent": {
  8. "action": "router",
  9. "abilityName": "JSCardEntryAbility",
  10. "params": {
  11. "info": "router info",
  12. "message": "router message"
  13. }
  14. },
  15. "messageEvent": {
  16. "action": "message",
  17. "params": {
  18. "detail": "message detail"
  19. }
  20. }
  21. }
  22. }
  ```

说明

"data"中JSON Value支持多级嵌套数据，在更新数据时，需要注意携带完整数据。

当前卡片显示07.18日Mr.Zhang的课程信息，示例如下。

```
1. "data": {
2. "Day": "07.18",
3. "teacher": {
4. "name": "Mr.Zhang",
5. "course": "Math"
6. }
7. }
```

当卡片内容需要更新为07.18日Mr.Li的课程信息时，需要传递待更新的完整数据，不能只传递单个数据项，如只传name或只传course，示例如下。

```
1. "teacher": {
2. "name": "Mr.Li",
3. "course": "English"
4. }
```

* 在UIAbility中接收router事件并获取参数

  ```
  1. // entry/src/main/ets/entryability/EntryAbility.ets
  2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
  3. import { hilog } from '@kit.PerformanceAnalysisKit';
  4. import { window } from '@kit.ArkUI';

  6. const TAG: string = 'EntryAbility';
  7. const DOMAIN_NUMBER: number = 0xFF00;
  8. // ...
  9. export default class EntryAbility extends UIAbility {
  10. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  11. if (want?.parameters?.params) {
  12. let params: Record<string, Object> = JSON.parse(JSON.stringify(want.parameters.params));
  13. // 获取router事件中传递的info参数
  14. if (params.info === 'router info') {
  15. // 执行业务逻辑，由用户自行实现
  16. hilog.info(DOMAIN_NUMBER, TAG, `router info: ${params.info}`);
  17. }
  18. // 获取router事件中传递的message参数
  19. if (params.message === 'router message') {
  20. // 执行业务逻辑，由用户自行实现
  21. hilog.info(DOMAIN_NUMBER, TAG, `router message: ${params.message}`);
  22. }
  23. }
  24. }

  26. // ...
  27. }
  ```
* 在FormExtensionAbility中接收message事件并获取参数，代码导入请参考[创建卡片FormExtensionAbility](js-ui-widget-development.md#创建卡片formextensionability)中的导入模块。

  ```
  1. // entry/src/main/ets/jscardformability/JsCardFormAbility.ets
  2. const TAG: string = 'JsCardFormAbility';
  3. // ...
  4. const DOMAIN_NUMBER: number = 0xFF00;
  5. // ...

  7. export default class JsCardFormAbility extends FormExtensionAbility {
  8. // ...
  9. onFormEvent(formId: string, message: string): void {
  10. // 若卡片支持触发事件，则需要重写该方法并实现对事件的触发
  11. hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onFormEvent');
  12. // 获取message事件中传递的detail参数
  13. let msg: Record<string, string> = JSON.parse(message);
  14. if (msg.detail === 'message detail') {
  15. // 执行业务逻辑，由用户自行实现
  16. hilog.info(DOMAIN_NUMBER, TAG, 'message info:' + msg.detail);
  17. }
  18. }

  20. }
  ```
