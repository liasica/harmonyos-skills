---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-picker
title: @ohos.file.picker (选择器)
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > ArkTS API > @ohos.file.picker (选择器)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:43+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:85edb5fab48c93940f767c1c2f805bcb0f5206a2685d06478cfbccd1f1795b9e
---

选择器(Picker)是一个封装DocumentViewPicker、AudioViewPicker、PhotoViewPicker的API模块，具有选择与保存的能力。应用可以选择使用以下API来实现文件的选择和保存的功能。该类接口，需要应用在界面UIAbility中调用，否则无法拉起FilePicker应用、AudioPicker应用或PhotoPicker应用。

调用本模块接口返回的URI数组，URI中的中文及非数字字母的特殊字符会被编码为对应的ASCII码并拼接到URI中。

说明

该模块接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 导入模块

PhonePC/2in1TabletTV

```
1. import  { picker } from '@kit.CoreFileKit';
```

## DocumentViewPicker

PhonePC/2in1TabletTV

文件选择器对象，用来支撑选择和保存各种格式文档。在使用前，需要先创建DocumentViewPicker实例。

**系统能力**：SystemCapability.FileManagement.UserFileService

### constructor12+

PhonePC/2in1TabletTV

constructor(context: Context)

创建DocumentViewPicker对象，推荐使用该构造函数，获取context参考[getHostContext](arkts-apis-uicontext-uicontext.md#gethostcontext12)。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文（仅支持UIAbilityContext）。Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import  { picker } from '@kit.CoreFileKit';
3. @Entry
4. @Component
5. struct Index {
6. @State message: string = 'hello World';

8. build() {
9. Row() {
10. Column() {
11. Text(this.message)
12. .fontSize(50)
13. .fontWeight(FontWeight.Bold)
14. .onClick(()=>{
15. let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // 请确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
16. let documentPicker = new picker.DocumentViewPicker(context);
17. })
18. }
19. .width('100%')
20. }
21. .height('100%')
22. }
23. }
```

### constructor12+

PhonePC/2in1TabletTV

constructor()

创建DocumentViewPicker对象，不推荐使用该构造函数，会出现概率性失败问题。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

**示例：**

```
1. let documentPicker = new picker.DocumentViewPicker(); // 不推荐使用无参构造，会出现概率性拉起失败问题
```

### constructor13+

PhonePC/2in1TabletTV

constructor(context: Context, window: window.Window)

应用自行创建窗口中，可用通过该构造函数创建DocumentViewPicker对象。一般场景推荐使用constructor(context: Context)方法创建DocumentViewPicker对象。

说明

从API version 19开始，2in1和Tablet设备支持该方法。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文（仅支持UIAbilityContext）。Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| window | [window.Window](arkts-apis-window-window.md) | 是 | 应用创建的窗口实例。 |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { picker } from '@kit.CoreFileKit';
3. import { window } from '@kit.ArkUI';
4. @Entry
5. @Component
6. struct Index {
7. @State message: string = 'hello World';

9. build() {
10. Row() {
11. Column() {
12. Text(this.message)
13. .fontSize(50)
14. .fontWeight(FontWeight.Bold)
15. .onClick(()=>{
16. let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // 请确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
17. let windowClass: window.Window | undefined = undefined;
18. windowClass = window.findWindow('test'); // 请确保window已创建，此处的'test'为window创建时的name参数
19. let documentPicker = new picker.DocumentViewPicker(context, windowClass);
20. })
21. }
22. .width('100%')
23. }
24. .height('100%')
25. }
26. }
```

### select

PhonePC/2in1TabletTV

select(option?: DocumentSelectOptions): Promise<Array<string>>

通过选择模式拉起documentPicker界面，用户可以选择一个或多个文件。使用Promise异步回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| option | [DocumentSelectOptions](js-apis-file-picker.md#documentselectoptions) | 否 | documentPicker选择选项。若无此参数，则默认拉起documentPicker主界面。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象。返回documentPicker选择后的结果集。  **注意**：此接口返回的URI数组的具体使用方式参见用户文件URI介绍中的[文档类uri的使用方式](../harmonyos-guides/user-file-uri-intro.md#文档类uri的使用方式)。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';
3. import  { picker } from '@kit.CoreFileKit';
4. async function example07(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
5. try {
6. let documentSelectOptions = new picker.DocumentSelectOptions();
7. let documentPicker = new picker.DocumentViewPicker(context);
8. documentPicker.select(documentSelectOptions).then((documentSelectResult: Array<string>) => {
9. console.info('DocumentViewPicker.select successfully, documentSelectResult uri: ' + JSON.stringify(documentSelectResult));
10. }).catch((err: BusinessError) => {
11. console.error(`DocumentViewPicker.select failed with err, code is: ${err.code}, message is: ${err.message}`);
12. });
13. } catch (error) {
14. let err: BusinessError = error as BusinessError;
15. console.error(`DocumentViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
16. }
17. }
```

### select

PhonePC/2in1TabletTV

select(option: DocumentSelectOptions, callback: AsyncCallback<Array<string>>): void

通过选择模式拉起documentPicker界面，用户可以选择一个或多个文件。使用callback异步回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| option | [DocumentSelectOptions](js-apis-file-picker.md#documentselectoptions) | 是 | documentPicker选择选项。 |
| callback | AsyncCallback<Array<string>> | 是 | callback 返回documentPicker选择后的结果集。  **注意**：此接口返回的URI数组的具体使用方式参见用户文件URI介绍中的[文档类uri的使用方式](../harmonyos-guides/user-file-uri-intro.md#文档类uri的使用方式)。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';
3. import  { picker } from '@kit.CoreFileKit';
4. async function example08(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
5. try {
6. let documentSelectOptions = new picker.DocumentSelectOptions();
7. let documentPicker = new picker.DocumentViewPicker(context);
8. documentPicker.select(documentSelectOptions, (err: BusinessError, documentSelectResult: Array<string>) => {
9. if (err) {
10. console.error(`DocumentViewPicker.select failed with err, code is: ${err.code}, message is: ${err.message}`);
11. return;
12. }
13. console.info('DocumentViewPicker.select successfully, documentSelectResult uri: ' + JSON.stringify(documentSelectResult));
14. });
15. } catch (error) {
16. let err: BusinessError = error as BusinessError;
17. console.error(`DocumentViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
18. }
19. }
```

### select

PhonePC/2in1TabletTV

select(callback: AsyncCallback<Array<string>>): void

通过选择模式拉起documentPicker界面，用户可以选择一个或多个文件。使用callback异步回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<string>> | 是 | callback 返回documentPicker选择后的结果集。  **注意**：此接口返回的URI数组的具体使用方式参见用户文件URI介绍中的[文档类uri的使用方式](../harmonyos-guides/user-file-uri-intro.md#文档类uri的使用方式)。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';
3. import  { picker } from '@kit.CoreFileKit';
4. async function example09(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
5. try {
6. let documentPicker = new picker.DocumentViewPicker(context);
7. documentPicker.select((err: BusinessError, documentSelectResult: Array<string>) => {
8. if (err) {
9. console.error(`DocumentViewPicker.select failed with err, code is: ${err.code}, message is: ${err.message}`);
10. return;
11. }
12. console.info('DocumentViewPicker.select successfully, documentSelectResult uri: ' + JSON.stringify(documentSelectResult));
13. });
14. } catch (error) {
15. let err: BusinessError = error as BusinessError;
16. console.error(`DocumentViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
17. }
18. }
```

### save

PhonePC/2in1TabletTV

save(option?: DocumentSaveOptions): Promise<Array<string>>

通过保存模式拉起documentPicker界面，用户可以保存一个或多个文件。使用Promise异步回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| option | [DocumentSaveOptions](js-apis-file-picker.md#documentsaveoptions) | 否 | documentPicker保存选项。若无此参数，则拉起documentPicker界面后需用户自行输入保存的文件名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象。返回documentPicker保存后的结果集。  **注意**：此接口返回的URI数组的具体使用方式参见用户文件URI介绍中的[文档类uri的使用方式](../harmonyos-guides/user-file-uri-intro.md#文档类uri的使用方式)。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';
3. import  { picker } from '@kit.CoreFileKit';
4. async function example10(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
5. try {
6. let documentSaveOptions = new picker.DocumentSaveOptions();
7. documentSaveOptions.newFileNames = ['DocumentViewPicker01.txt'];
8. let documentPicker = new picker.DocumentViewPicker(context);
9. documentPicker.save(documentSaveOptions).then((documentSaveResult: Array<string>) => {
10. console.info('DocumentViewPicker.save successfully, documentSaveResult uri: ' + JSON.stringify(documentSaveResult));
11. }).catch((err: BusinessError) => {
12. console.error(`DocumentViewPicker.save failed with err, code is: ${err.code}, message is: ${err.message}`);
13. });
14. } catch (error) {
15. let err: BusinessError = error as BusinessError;
16. console.error(`DocumentViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
17. }
18. }
```

### save

PhonePC/2in1TabletTV

save(option: DocumentSaveOptions, callback: AsyncCallback<Array<string>>): void

通过保存模式拉起documentPicker界面，用户可以保存一个或多个文件。使用callback异步回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| option | [DocumentSaveOptions](js-apis-file-picker.md#documentsaveoptions) | 是 | documentPicker保存选项。 |
| callback | AsyncCallback<Array<string>> | 是 | callback 返回documentPicker保存后的结果集。  **注意**：此接口返回的URI数组的具体使用方式参见用户文件URI介绍中的[文档类uri的使用方式](../harmonyos-guides/user-file-uri-intro.md#文档类uri的使用方式)。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';
3. import  { picker } from '@kit.CoreFileKit';
4. async function example11(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
5. try {
6. let documentSaveOptions = new picker.DocumentSaveOptions();
7. documentSaveOptions.newFileNames = ['DocumentViewPicker02.txt'];
8. let documentPicker = new picker.DocumentViewPicker(context);
9. documentPicker.save(documentSaveOptions, (err: BusinessError, documentSaveResult: Array<string>) => {
10. if (err) {
11. console.error(`DocumentViewPicker.save failed with err, code is: ${err.code}, message is: ${err.message}`);
12. return;
13. }
14. console.info('DocumentViewPicker.save successfully, documentSaveResult uri: ' + JSON.stringify(documentSaveResult));
15. });
16. } catch (error) {
17. let err: BusinessError = error as BusinessError;
18. console.error(`DocumentViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
19. }
20. }
```

### save

PhonePC/2in1TabletTV

save(callback: AsyncCallback<Array<string>>): void

通过保存模式拉起documentPicker界面，用户可以保存一个或多个文件。使用callback异步回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<string>> | 是 | callback 返回documentPicker保存后的结果集。  **注意**：此接口返回的URI数组的具体使用方式参见用户文件URI介绍中的[文档类uri的使用方式](../harmonyos-guides/user-file-uri-intro.md#文档类uri的使用方式)。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';
3. import  { picker } from '@kit.CoreFileKit';
4. async function example12(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
5. try {
6. let documentPicker = new picker.DocumentViewPicker(context);
7. documentPicker.save((err: BusinessError, documentSaveResult: Array<string>) => {
8. if (err) {
9. console.error(`DocumentViewPicker.save failed with err, code is: ${err.code}, message is: ${err.message}`);
10. return;
11. }
12. console.info('DocumentViewPicker.save successfully, documentSaveResult uri: ' + JSON.stringify(documentSaveResult));
13. });
14. } catch (error) {
15. let err: BusinessError = error as BusinessError;
16. console.error(`DocumentViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
17. }
18. }
```

### getSelectedIndex14+

PC/2in1

getSelectedIndex(): number

获取保存成功后的文件后缀类型的下标。

该方法只在调用 [save()](js-apis-file-picker.md#save)时使用生效，其他场景下不适用。

该方法需要配置参数[DocumentSaveOptions.fileSuffixChoices](js-apis-file-picker.md#documentsaveoptions)。

该方法返回的是所选后缀类型的下标(number)。所选的后缀类型是开发者所传的参数[DocumentSaveOptions.fileSuffixChoices](js-apis-file-picker.md#documentsaveoptions)里的某个后缀类型。如果没有传参，并且调用了getSelectedIndex()方法，返回值为-1。

**元服务API**：从API version 14开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService.FolderSelection

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回所选后缀类型在[DocumentSaveOptions.fileSuffixChoices](js-apis-file-picker.md#documentsaveoptions)里的下标(number)。默认返回-1。 |

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';
3. import  { picker } from '@kit.CoreFileKit';
4. async function exampleIndex(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
5. try {
6. let documentSaveOptions = new picker.DocumentSaveOptions();
7. // 保存文件的名字
8. documentSaveOptions.newFileNames = ['DocumentViewPicker01'];
9. // 保存文件的后缀类型
10. documentSaveOptions.fileSuffixChoices = ['txt', 'mp4', 'pdf'];
11. let documentPicker = new picker.DocumentViewPicker(context);
12. documentPicker.save(documentSaveOptions).then((documentSaveResult: Array<string>) => {
13. if (documentSaveOptions.fileSuffixChoices != undefined && documentSaveResult != undefined) {
14. // 获取保存文件的后缀类型的下标
15. let index = documentPicker.getSelectedIndex();
16. // 获取保存文件的后缀类型。
17. let selectedsuffix = documentSaveOptions.fileSuffixChoices[index];
18. console.info ('DocumentViewPicker.save selectedsuffix is ' + selectedsuffix);
19. }
20. console.info('DocumentViewPicker.save successfully, documentSaveResult uri: ' + JSON.stringify(documentSaveResult));
21. }).catch((err: BusinessError) => {
22. console.error(`DocumentViewPicker.save failed with err, code is: ${err.code}, message is: ${err.message}`);
23. });
24. } catch (error) {
25. let err: BusinessError = error as BusinessError;
26. console.error(`DocumentViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
27. }
28. }
```

## AudioViewPicker

PhonePC/2in1TabletTV

音频选择器对象，用来支撑选择和保存音频类文件等用户场景。在使用前，需要先创建AudioViewPicker实例。

**系统能力**：SystemCapability.FileManagement.UserFileService

### constructor12+

PhonePC/2in1TabletTV

constructor(context: Context)

创建AudioViewPicker对象，推荐使用该构造函数，获取context参考[getHostContext](arkts-apis-uicontext-uicontext.md#gethostcontext12)。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文（仅支持UIAbilityContext）。Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import  { picker } from '@kit.CoreFileKit';
3. @Entry
4. @Component
5. struct Index {
6. @State message: string = 'hello World';

8. build() {
9. Row() {
10. Column() {
11. Text(this.message)
12. .fontSize(50)
13. .fontWeight(FontWeight.Bold)
14. .onClick(()=>{
15. let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // 请确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
16. let audioPicker = new picker.AudioViewPicker(context);
17. })
18. }
19. .width('100%')
20. }
21. .height('100%')
22. }
23. }
```

### constructor12+

PhonePC/2in1TabletTV

constructor()

创建AudioViewPicker对象，不推荐使用该构造函数，会出现概率性失败问题。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

**示例：**

```
1. let audioPicker = new picker.AudioViewPicker(); // 不推荐使用无参构造，会出现概率性拉起失败问题
```

### select

PhonePC/2in1TabletTV

select(option?: AudioSelectOptions): Promise<Array<string>>

通过选择模式拉起audioPicker界面，用户可以选择一个或多个音频文件。使用Promise异步回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| option | [AudioSelectOptions](js-apis-file-picker.md#audioselectoptions) | 否 | audioPicker音频选择选项。若无此参数，则默认拉起audioPicker主界面。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象。返回audioPicker选择音频后的结果集。  **注意**： 此接口返回的URI数组的具体使用方式参见用户文件URI介绍中的[媒体类uri的使用方式](../harmonyos-guides/user-file-uri-intro.md#媒体文件uri介绍)。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';
3. import  { picker } from '@kit.CoreFileKit';
4. async function example13(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
5. try {
6. let audioSelectOptions = new picker.AudioSelectOptions();
7. let audioPicker = new picker.AudioViewPicker(context);
8. audioPicker.select(audioSelectOptions).then((audioSelectResult: Array<string>) => {
9. console.info('AudioViewPicker.select successfully, audioSelectResult uri: ' + JSON.stringify(audioSelectResult));
10. }).catch((err: BusinessError) => {
11. console.error(`AudioViewPicker.select failed with err, code is: ${err.code}, message is: ${err.message}`);
12. });
13. } catch (error) {
14. let err: BusinessError = error as BusinessError;
15. console.error(`AudioViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
16. }
17. }
```

### select

PhonePC/2in1TabletTV

select(option: AudioSelectOptions, callback: AsyncCallback<Array<string>>): void

通过选择模式拉起audioPicker界面，用户可以选择一个或多个音频文件。使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| option | [AudioSelectOptions](js-apis-file-picker.md#audioselectoptions) | 是 | audioPicker音频选择选项。 |
| callback | AsyncCallback<Array<string>> | 是 | callback 返回audioPicker选择音频后的结果集。  **注意**： 此接口返回的URI数组的具体使用方式参见用户文件URI介绍中的[媒体类uri的使用方式](../harmonyos-guides/user-file-uri-intro.md#媒体文件uri介绍)。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';
3. import  { picker } from '@kit.CoreFileKit';
4. async function example14(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
5. try {
6. let audioSelectOptions = new picker.AudioSelectOptions();
7. let audioPicker = new picker.AudioViewPicker(context);
8. audioPicker.select(audioSelectOptions, (err: BusinessError, audioSelectResult: Array<string>) => {
9. if (err) {
10. console.error(`AudioViewPicker.select failed with err, code is: ${err.code}, message is: ${err.message}`);
11. return;
12. }
13. console.info('AudioViewPicker.select successfully, audioSelectResult uri: ' + JSON.stringify(audioSelectResult));
14. });
15. } catch (error) {
16. let err: BusinessError = error as BusinessError;
17. console.error(`AudioViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
18. }
19. }
```

### select

PhonePC/2in1TabletTV

select(callback: AsyncCallback<Array<string>>): void

通过选择模式拉起audioPicker界面，用户可以选择一个或多个音频文件。使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<string>> | 是 | callback 返回audioPicker选择音频后的结果集。  **注意**： 此接口返回的URI数组的具体使用方式参见用户文件URI介绍中的[媒体类uri的使用方式](../harmonyos-guides/user-file-uri-intro.md#媒体文件uri介绍)。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';
3. import  { picker } from '@kit.CoreFileKit';
4. async function example15(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
5. try {
6. let audioPicker = new picker.AudioViewPicker(context);
7. audioPicker.select((err: BusinessError, audioSelectResult: Array<string>) => {
8. if (err) {
9. console.error(`AudioViewPicker.select failed with err, code is: ${err.code}, message is: ${err.message}`);
10. return;
11. }
12. console.info('AudioViewPicker.select successfully, audioSelectResult uri: ' + JSON.stringify(audioSelectResult));
13. });
14. } catch (error) {
15. let err: BusinessError = error as BusinessError;
16. console.error(`AudioViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
17. }
18. }
```

### save

PhonePC/2in1TabletTV

save(option?: AudioSaveOptions): Promise<Array<string>>

通过保存模式拉起audioPicker界面（目前拉起的是documentPicker，audioPicker在规划中），用户可以保存一个或多个音频文件。使用Promise异步回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| option | [AudioSaveOptions](js-apis-file-picker.md#audiosaveoptions) | 否 | audioPicker保存音频文件选项。若无此参数，则拉起audioPicker界面后需用户自行输入保存的文件名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象。返回audioPicker保存音频文件后的结果集。  **注意**： 此接口返回的URI数组的具体使用方式参见用户文件URI介绍中的[文档类uri的使用方式](../harmonyos-guides/user-file-uri-intro.md#文档类uri的使用方式)。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';
3. import  { picker } from '@kit.CoreFileKit';
4. async function example16(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
5. try {
6. let audioSaveOptions = new picker.AudioSaveOptions();
7. audioSaveOptions.newFileNames = ['AudioViewPicker01.mp3'];
8. let audioPicker = new picker.AudioViewPicker(context);
9. audioPicker.save(audioSaveOptions).then((audioSaveResult: Array<string>) => {
10. console.info('AudioViewPicker.save successfully, audioSaveResult uri: ' + JSON.stringify(audioSaveResult))
11. }).catch((err: BusinessError) => {
12. console.error(`AudioViewPicker.save failed with err, code is: ${err.code}, message is: ${err.message}`);
13. });
14. } catch (error) {
15. let err: BusinessError = error as BusinessError;
16. console.error(`AudioViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
17. }
18. }
```

### save

PhonePC/2in1TabletTV

save(option: AudioSaveOptions, callback: AsyncCallback<Array<string>>): void

通过保存模式拉起audioPicker界面（目前拉起的是documentPicker，audioPicker在规划中），用户可以保存一个或多个音频文件。使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| option | [AudioSaveOptions](js-apis-file-picker.md#audiosaveoptions) | 是 | audioPicker保存音频文件选项。 |
| callback | AsyncCallback<Array<string>> | 是 | callback 返回audioPicker保存音频文件后的结果集。  **注意**： 此接口返回的URI数组的具体使用方式参见用户文件URI介绍中的[文档类uri的使用方式](../harmonyos-guides/user-file-uri-intro.md#文档类uri的使用方式)。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';
3. import  { picker } from '@kit.CoreFileKit';
4. async function example17(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
5. try {
6. let audioSaveOptions = new picker.AudioSaveOptions();
7. audioSaveOptions.newFileNames = ['AudioViewPicker02.mp3'];
8. let audioPicker = new picker.AudioViewPicker(context);
9. audioPicker.save(audioSaveOptions, (err: BusinessError, audioSaveResult: Array<string>) => {
10. if (err) {
11. console.error(`AudioViewPicker.save failed with err, code is: ${err.code}, message is: ${err.message}`);
12. return;
13. }
14. console.info('AudioViewPicker.save successfully, audioSaveResult uri: ' + JSON.stringify(audioSaveResult));
15. });
16. } catch (error) {
17. let err: BusinessError = error as BusinessError;
18. console.error(`AudioViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
19. }
20. }
```

### save

PhonePC/2in1TabletTV

save(callback: AsyncCallback<Array<string>>): void

通过保存模式拉起audioPicker界面（目前拉起的是documentPicker，audioPicker在规划中），用户可以保存一个或多个音频文件。使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<string>> | 是 | callback 返回audioPicker保存音频文件后的结果集。  **注意**： 此接口返回的URI数组的具体使用方式参见用户文件URI介绍中的[文档类uri的使用方式](../harmonyos-guides/user-file-uri-intro.md#文档类uri的使用方式)。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';
3. import  { picker } from '@kit.CoreFileKit';
4. async function example18(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
5. try {
6. let audioPicker = new picker.AudioViewPicker(context);
7. audioPicker.save((err: BusinessError, audioSaveResult: Array<string>) => {
8. if (err) {
9. console.error(`AudioViewPicker.save failed with err, code is: ${err.code}, message is: ${err.message}`);
10. return;
11. }
12. console.info('AudioViewPicker.save successfully, audioSaveResult uri: ' + JSON.stringify(audioSaveResult));
13. });
14. } catch (error) {
15. let err: BusinessError = error as BusinessError;
16. console.error(`AudioViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
17. }
18. }
```

## DocumentSelectMode11+

PC/2in1

枚举，picker选择的文档类型。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService.FolderSelection

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FILE | 0 | 文件类型（默认类型）。 |
| FOLDER | 1 | 文件夹类型。 |
| MIXED | 2 | 文件和文件夹混合类型。 |

## DocumentSelectOptions

PhonePC/2in1TabletTV

文档选择选项。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| maxSelectNumber10+ | number | 否 | 是 | 选择文件最大个数。  API version 20及之前的版本，单次文件选择的最大数量上限为500个，默认值也为500。目录选择功能仅对具备该系统能力的设备开放，且单次最多可选择1个目录。  API version 21及之后的版本取消文件选择数量的限制。受系统能力限制，选择文件数量过大可能会出现功能异常或处理性能较差等情况，建议单次选择文件个数不超过1万个。  API version 23及之后的版本取消目录选择数量的限制。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。  **系统能力**：SystemCapability.FileManagement.UserFileService |
| defaultFilePathUri10+ | string | 否 | 是 | 指定选择的文件或者目录的URI。默认为空（效果为拉起最近打开页）。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。  **系统能力**：SystemCapability.FileManagement.UserFileService |
| fileSuffixFilters10+ | Array<string> | 否 | 是 | 选择文件的后缀类型。传入字符串数组，每一项代表一个后缀选项，每一项内部用"|"分为两部分，第一部分为描述，第二部分为过滤后缀。没有"|"则没有描述，该项整体是一个过滤后缀。每项过滤后缀可以存在多个后缀名，则每一个后缀名之间用英文逗号进行分隔，传入数组长度不能超过100，例如：['图片(.png, .jpg)|.png,.jpg', '文档|.txt', '视频|.mp4', '.pdf']。  默认不过滤，即显示所有文件。此外2in1设备支持通配符方式['所有文件(\*.\*)|.\*']（说明：从API version 17开始，手机支持该配置），表示为显示所有文件。  仅对具有该系统能力的设备开放。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。  **系统能力**：SystemCapability.FileManagement.UserFileService |
| selectMode11+ | [DocumentSelectMode](js-apis-file-picker.md#documentselectmode11) | 否 | 是 | Picker选择的文档类型，默认值是FILE(文件类型)。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。  **系统能力**：SystemCapability.FileManagement.UserFileService.FolderSelection |
| authMode12+ | boolean | 否 | 是 | 拉起授权Picker，默认为false（非授权模式）。当authMode为true时为授权模式，defaultFilePathUri必填，表明待授权URI。  **设备行为差异**：该参数在2in1设备中可正常使用，在其他设备中无效果。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。  **系统能力**：SystemCapability.FileManagement.UserFileService.FolderSelection |
| multiAuthMode15+ | boolean | 否 | 是 | 支持批量授权模式，默认为false（非批量授权模式）。当multiAuthMode为true时为批量授权模式。当multiAuthMode为true时，只有multiUriArray参数生效，其他参数不生效。  **设备行为差异**：该参数在Phone设备中可正常使用，在其他设备中无效果。  **元服务API**：从API version 15开始，该接口支持在元服务中使用。  **系统能力**：SystemCapability.FileManagement.UserFileService |
| multiUriArray15+ | Array<string> | 否 | 是 | 传入需要批量授权的URI数组（仅支持文件，文件夹不生效）。配合multiAuthMode使用。当multiAuthMode为false时，配置该参数不生效。默认为空（效果为拉起批量授权页面后展示的文件为空）。  **设备行为差异**：该参数在Phone设备中可正常使用，在其他设备中无效果。  **元服务API**：从API version 15开始，该接口支持在元服务中使用。  **系统能力**：SystemCapability.FileManagement.UserFileService |
| mergeMode15+ | [MergeTypeMode](js-apis-file-picker.md#mergetypemode15) | 否 | 是 | 开启聚合视图模式，支持拉起文件管理应用的聚合视图。默认为DEFAULT，表示该参数不生效，非聚合视图。当该参数置为非DEFAULT时，其他参数不生效。  **设备行为差异**：该参数在Phone设备中可正常使用，在其他设备中无效果。  **元服务API**：从API version 15开始，该接口支持在元服务中使用。  **系统能力**：SystemCapability.FileManagement.UserFileService |
| isEncryptionSupported19+ | boolean | 否 | 是 | 是否支持加密（仅支持文件，文件夹不生效），默认为false。该参数为true时，在Picker界面可以选择对文件进行加密。  **元服务API**：从API version 19开始，该接口支持在元服务中使用。  **系统能力**：SystemCapability.FileManagement.UserFileService |

## DocumentPickerMode12+

PhonePC/2in1TabletTV

枚举，picker保存的模式。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 标准模式。 |
| DOWNLOAD | 1 | 下载模式。  **注意**： DOWNLOAD模式创建的目录仅用于保存文件，目录之间无访问隔离，不建议保存应用敏感数据。 |

## MergeTypeMode15+

PhonePC/2in1TabletTV

枚举，文件聚合类型。

**元服务API**：从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

**设备行为差异**：该接口在Phone设备中可正常调用，在其他设备中无效果。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 默认模式，表示该参数不生效。 |
| AUDIO | 1 | 音频文件模式。 |
| VIDEO | 2 | 视频文件模式。 |
| DOCUMENT | 3 | 文档文件模式。 |
| PICTURE | 4 | 图片文件模式。 |

## DocumentSaveOptions

PhonePC/2in1TabletTV

文档保存选项。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| newFileNames | Array<string> | 否 | 是 | 拉起documentPicker进行保存的文件名。若无此参数，则默认需要用户自行输入。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。  **系统能力**：SystemCapability.FileManagement.UserFileService |
| defaultFilePathUri10+ | string | 否 | 是 | 指定保存的文件或者目录的URI。默认为空。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。  **系统能力**：SystemCapability.FileManagement.UserFileService |
| fileSuffixChoices10+ | Array<string> | 否 | 是 | 保存文件的后缀类型。传入字符串数组，每一项代表一个后缀选项，每一项内部用"|"分为两部分，第一部分为描述，第二部分为要保存的后缀。没有"|"则没有描述，该项整体是一个保存的后缀。默认没有后缀类型。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。  **系统能力**：SystemCapability.FileManagement.UserFileService |
| pickerMode12+ | [DocumentPickerMode](js-apis-file-picker.md#documentpickermode12) | 否 | 是 | 拉起picker的类型, 默认为DEFAULT。当pickerMode设置为DOWNLOAD时，用户配置的参数newFileNames、defaultFilePathUri和fileSuffixChoices将不会生效。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。  **系统能力**：SystemCapability.FileManagement.UserFileService |
| autoCreateEmptyFile23+ | boolean | 否 | 是 | 保存文件时，由应用决定是否预置空文件。默认为true，Picker会预置空文件并且返回文件的URI数组。false不预置空文件，只会返回文件的URI数组。  **模型约束**：此接口仅可在Stage模型下使用。  **系统能力**：SystemCapability.FileManagement.UserFileService.FolderSelection |

## AudioSelectOptions

PhonePC/2in1TabletTV

音频选择选项。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| maxSelectNumber12+ | number | 否 | 是 | 选择文件最大个数，默认值为1，上限为500个，有效值范围1-500。 |

## AudioSaveOptions

PhonePC/2in1TabletTV

音频保存选项。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| newFileNames | Array<string> | 否 | 是 | 拉起audioPicker进行保存音频资源的文件名。若无此参数，则默认需要用户自行输入。 |

## PhotoViewPicker(deprecated)

PhonePC/2in1TabletTV

图库选择器对象，用来支撑选择图片/视频和保存图片/视频等用户场景。选择文件推荐使用[PhotoAccessHelper的PhotoViewPicker](arkts-apis-photoaccesshelper-photoviewpicker.md)。在使用前，需要先创建PhotoViewPicker实例。

说明

从API version 9开始支持，从API version 12开始废弃。建议使用[photoAccessHelper.PhotoViewPicker](arkts-apis-photoaccesshelper-photoviewpicker.md)替代。

**系统能力**：SystemCapability.FileManagement.UserFileService

### constructor(deprecated)

PhonePC/2in1TabletTV

constructor(context: Context)

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文（仅支持UIAbilityContext）。Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |

创建PhotoViewPicker对象，推荐使用该构造函数，获取context参考[getHostContext](arkts-apis-uicontext-uicontext.md#gethostcontext12)。

说明

从API version 12开始支持，从API version 18开始废弃。建议使用[photoAccessHelper.PhotoViewPicker](arkts-apis-photoaccesshelper-photoviewpicker.md)替代。

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import  { picker } from '@kit.CoreFileKit';
3. @Entry
4. @Component
5. struct Index {
6. @State message: string = 'hello World';

8. build() {
9. Row() {
10. Column() {
11. Text(this.message)
12. .fontSize(50)
13. .fontWeight(FontWeight.Bold)
14. .onClick(()=>{
15. let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // 请确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
16. let photoPicker = new picker.PhotoViewPicker(context);
17. })
18. }
19. .width('100%')
20. }
21. .height('100%')
22. }
23. }
```

### constructor(deprecated)

PhonePC/2in1TabletTV

constructor()

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

创建PhotoViewPicker对象，不推荐使用该构造函数，会出现概率性失败问题。

说明

从API version 12开始支持，从API version 18开始废弃。建议使用[photoAccessHelper.PhotoViewPicker](arkts-apis-photoaccesshelper-photoviewpicker.md)替代。

**示例：**

```
1. let photoPicker = new picker.PhotoViewPicker(); // 不推荐使用无参构造，会出现概率性拉起失败问题
```

### select(deprecated)

PhonePC/2in1TabletTV

select(option?: PhotoSelectOptions): Promise<PhotoSelectResult>

通过选择模式拉起photoPicker界面，用户可以选择一个或多个图片/视频。接口采用Promise异步返回形式，传入可选参数PhotoSelectOptions对象，返回PhotoSelectResult对象。

说明

从API version 9开始支持，从API version 12开始废弃。建议使用[photoAccessHelper.PhotoViewPicker#select](arkts-apis-photoaccesshelper-photoviewpicker.md#select)替代。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| option | [PhotoSelectOptions](js-apis-file-picker.md#photoselectoptionsdeprecated) | 否 | photoPicker选择选项。若无此参数，则默认选择媒体文件类型为图片和视频类型。选择媒体文件数量的默认最大值为50。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PhotoSelectResult](js-apis-file-picker.md#photoselectresultdeprecated)> | Promise对象。返回photoPicker选择后的结果集。  **注意**：此接口返回的PhotoSelectResult对象中的photoUris只能通过临时授权的方式调用接口[photoAccessHelper.getAssets](arkts-apis-photoaccesshelper-photoaccesshelper.md#getassets)去使用，具体使用方式参见用户文件URI介绍中的[媒体文件URI的使用方式](../harmonyos-guides/user-file-uri-intro.md#媒体文件uri的使用方式)。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';
3. import  { picker } from '@kit.CoreFileKit';
4. async function example01(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
5. try {
6. let photoSelectOptions = new picker.PhotoSelectOptions();
7. photoSelectOptions.MIMEType = picker.PhotoViewMIMETypes.IMAGE_TYPE;
8. photoSelectOptions.maxSelectNumber = 5;
9. let photoPicker = new picker.PhotoViewPicker(context);
10. photoPicker.select(photoSelectOptions).then((photoSelectResult: picker.PhotoSelectResult) => {
11. console.info('PhotoViewPicker.select successfully, photoSelectResult uri: ' + JSON.stringify(photoSelectResult));
12. }).catch((err: BusinessError) => {
13. console.error('PhotoViewPicker.select failed with err: ' + JSON.stringify(err));
14. });
15. } catch (error) {
16. let err: BusinessError = error as BusinessError;
17. console.error('PhotoViewPicker failed with err: ' + JSON.stringify(err));
18. }
19. }
```

### select(deprecated)

PhonePC/2in1TabletTV

select(option: PhotoSelectOptions, callback: AsyncCallback<PhotoSelectResult>): void

通过选择模式拉起photoPicker界面，用户可以选择一个或多个图片/视频。接口采用callback异步返回形式，传入参数PhotoSelectOptions对象，返回PhotoSelectResult对象。

说明

从API version 9开始支持，从API version 12开始废弃。建议使用[photoAccessHelper.PhotoViewPicker#select](arkts-apis-photoaccesshelper-photoviewpicker.md#select-1)替代。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| option | [PhotoSelectOptions](js-apis-file-picker.md#photoselectoptionsdeprecated) | 是 | photoPicker选择选项。 |
| callback | AsyncCallback<[PhotoSelectResult](js-apis-file-picker.md#photoselectresultdeprecated)> | 是 | callback返回photoPicker选择后的结果集。  **注意**：此接口返回的PhotoSelectResult对象中的photoUris只能通过临时授权的方式调用接口[photoAccessHelper.getAssets](arkts-apis-photoaccesshelper-photoaccesshelper.md#getassets)去使用，具体使用方式参见用户文件URI介绍中的[媒体文件URI的使用方式](../harmonyos-guides/user-file-uri-intro.md#媒体文件uri的使用方式)。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';
3. import  { picker } from '@kit.CoreFileKit';
4. async function example02(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
5. try {
6. let photoSelectOptions = new picker.PhotoSelectOptions();
7. photoSelectOptions.MIMEType = picker.PhotoViewMIMETypes.IMAGE_TYPE;
8. photoSelectOptions.maxSelectNumber = 5;
9. let photoPicker = new picker.PhotoViewPicker(context);
10. photoPicker.select(photoSelectOptions, (err: BusinessError, photoSelectResult: picker.PhotoSelectResult) => {
11. if (err) {
12. console.error('PhotoViewPicker.select failed with err: ' + JSON.stringify(err));
13. return;
14. }
15. console.info('PhotoViewPicker.select successfully, photoSelectResult uri: ' + JSON.stringify(photoSelectResult));
16. });
17. } catch (error) {
18. let err: BusinessError = error as BusinessError;
19. console.error('PhotoViewPicker failed with err: ' + JSON.stringify(err));
20. }
21. }
```

### select(deprecated)

PhonePC/2in1TabletTV

select(callback: AsyncCallback<PhotoSelectResult>): void

通过选择模式拉起photoPicker界面，用户可以选择一个或多个图片/视频。接口采用callback异步返回形式，返回PhotoSelectResult对象。

说明

从API version 9开始支持，从API version 12开始废弃。建议使用[photoAccessHelper.PhotoViewPicker#select](arkts-apis-photoaccesshelper-photoviewpicker.md#select-2)替代。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[PhotoSelectResult](js-apis-file-picker.md#photoselectresultdeprecated)> | 是 | callback返回photoPicker选择后的结果集。  **注意**：此接口返回的PhotoSelectResult对象中的photoUris只能通过临时授权的方式调用接口[photoAccessHelper.getAssets](arkts-apis-photoaccesshelper-photoaccesshelper.md#getassets)去使用，具体使用方式参见用户文件URI介绍中的[媒体文件URI的使用方式](../harmonyos-guides/user-file-uri-intro.md#媒体文件uri的使用方式)。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';
3. import  { picker } from '@kit.CoreFileKit';
4. async function example03(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
5. try {
6. let photoPicker = new picker.PhotoViewPicker(context);
7. photoPicker.select((err: BusinessError, photoSelectResult: picker.PhotoSelectResult) => {
8. if (err) {
9. console.error('PhotoViewPicker.select failed with err: ' + JSON.stringify(err));
10. return;
11. }
12. console.info('PhotoViewPicker.select successfully, photoSelectResult uri: ' + JSON.stringify(photoSelectResult));
13. });
14. } catch (error) {
15. let err: BusinessError = error as BusinessError;
16. console.error('PhotoViewPicker failed with err: ' + JSON.stringify(err));
17. }
18. }
```

### save(deprecated)

PhonePC/2in1TabletTV

save(option?: PhotoSaveOptions): Promise<Array<string>>

通过保存模式拉起photoPicker界面，用户可以保存一个或多个图片/视频。接口采用Promise异步返回形式，传入可选参数PhotoSaveOptions对象，返回保存文件的uri数组。

说明

从API version 9开始支持，从API version 12开始废弃。建议使用[SaveButton](ts-security-components-savebutton.md)替代。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| option | [PhotoSaveOptions](js-apis-file-picker.md#photosaveoptionsdeprecated) | 否 | photoPicker保存图片或视频文件选项。若无此参数，则拉起photoPicker界面后需用户自行输入保存的文件名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象。返回photoPicker保存图片或视频文件后的结果集。  **注意**：此接口会将文件保存在文件管理器，而不是图库。返回的uri数组的具体使用方式参见用户文件uri介绍中的[文档类uri的使用方式](../harmonyos-guides/user-file-uri-intro.md#文档类uri的使用方式)。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';
3. import  { picker } from '@kit.CoreFileKit';
4. async function example04(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
5. try {
6. let photoSaveOptions = new picker.PhotoSaveOptions();
7. photoSaveOptions.newFileNames = ['PhotoViewPicker01.jpg', 'PhotoViewPicker01.mp4'];
8. let photoPicker = new picker.PhotoViewPicker(context);
9. photoPicker.save(photoSaveOptions).then((photoSaveResult: Array<string>) => {
10. console.info('PhotoViewPicker.save successfully, photoSaveResult uri: ' + JSON.stringify(photoSaveResult));
11. }).catch((err: BusinessError) => {
12. console.error('PhotoViewPicker.save failed with err: ' + JSON.stringify(err));
13. });
14. } catch (error) {
15. let err: BusinessError = error as BusinessError;
16. console.error('PhotoViewPicker failed with err: ' + JSON.stringify(err));
17. }
18. }
```

### save(deprecated)

PhonePC/2in1TabletTV

save(option: PhotoSaveOptions, callback: AsyncCallback<Array<string>>): void

通过保存模式拉起photoPicker界面，用户可以保存一个或多个图片/视频。接口采用callback异步返回形式，传入参数PhotoSaveOptions对象，返回保存文件的uri数组。

说明

从API version 9开始支持，从API version 12开始废弃。建议使用[SaveButton](ts-security-components-savebutton.md)替代。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| option | [PhotoSaveOptions](js-apis-file-picker.md#photosaveoptionsdeprecated) | 是 | photoPicker保存图片或视频文件选项。 |
| callback | AsyncCallback<Array<string>> | 是 | callback 返回photoPicker保存图片或视频文件后的结果集。  **注意**：此接口会将文件保存在文件管理器，而不是图库。返回的uri数组的具体使用方式参见用户文件uri介绍中的[文档类uri的使用方式](../harmonyos-guides/user-file-uri-intro.md#文档类uri的使用方式)。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';
3. import  { picker } from '@kit.CoreFileKit';
4. async function example05(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
5. try {
6. let photoSaveOptions = new picker.PhotoSaveOptions();
7. photoSaveOptions.newFileNames = ['PhotoViewPicker02.jpg','PhotoViewPicker02.mp4'];
8. let photoPicker = new picker.PhotoViewPicker(context);
9. photoPicker.save(photoSaveOptions, (err: BusinessError, photoSaveResult: Array<string>) => {
10. if (err) {
11. console.error('PhotoViewPicker.save failed with err: ' + JSON.stringify(err));
12. return;
13. }
14. console.info('PhotoViewPicker.save successfully, photoSaveResult uri: ' + JSON.stringify(photoSaveResult));
15. });
16. } catch (error) {
17. let err: BusinessError = error as BusinessError;
18. console.error('PhotoViewPicker failed with err: ' + JSON.stringify(err));
19. }
20. }
```

### save(deprecated)

PhonePC/2in1TabletTV

save(callback: AsyncCallback<Array<string>>): void

通过保存模式拉起photoPicker界面，用户可以保存一个或多个图片/视频。接口采用callback异步返回形式，返回保存文件的uri数组。

说明

从API version 9开始支持，从API version 12开始废弃。建议使用[SaveButton](ts-security-components-savebutton.md)替代。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<string>> | 是 | callback 返回photoPicker保存图片或视频文件后的结果集。  **注意**：此接口会将文件保存在文件管理器，而不是图库。返回的uri数组的具体使用方式参见用户文件uri介绍中的[文档类uri的使用方式](../harmonyos-guides/user-file-uri-intro.md#文档类uri的使用方式)。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';
3. import  { picker } from '@kit.CoreFileKit';
4. async function example06(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
5. try {
6. let photoPicker = new picker.PhotoViewPicker(context);
7. photoPicker.save((err: BusinessError, photoSaveResult: Array<string>) => {
8. if (err) {
9. console.error('PhotoViewPicker.save failed with err: ' + JSON.stringify(err));
10. return;
11. }
12. console.info('PhotoViewPicker.save successfully, photoSaveResult uri: ' + JSON.stringify(photoSaveResult));
13. });
14. } catch (error) {
15. let err: BusinessError = error as BusinessError;
16. console.error('PhotoViewPicker failed with err: ' + JSON.stringify(err));
17. }
18. }
```

## PhotoViewMIMETypes(deprecated)

PhonePC/2in1TabletTV

枚举，可选择的媒体文件类型。

说明

从API version 9开始支持，从API version 12开始废弃。建议使用[photoAccessHelper.PhotoViewMIMETypes](arkts-apis-photoaccesshelper-e.md#photoviewmimetypes)替代。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

| 名称 | 值 | 说明 |
| --- | --- | --- |
| IMAGE\_TYPE | 'image/\*' | 图片类型。  **说明**：从API version 9开始支持，从API version 18开始废弃。 |
| VIDEO\_TYPE | 'video/\*' | 视频类型。  **说明**：从API version 9开始支持，从API version 18开始废弃。 |
| IMAGE\_VIDEO\_TYPE | '\*/\*' | 图片和视频类型。  **说明**：从API version 9开始支持，从API version 18开始废弃。 |

## PhotoSelectOptions(deprecated)

PhonePC/2in1TabletTV

图库选择选项。

说明

从API version 9开始支持，从API version 12开始废弃。建议使用[photoAccessHelper.PhotoSelectOptions](arkts-apis-photoaccesshelper-class.md#photoselectoptions)替代。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| MIMEType | [PhotoViewMIMETypes](js-apis-file-picker.md#photoviewmimetypesdeprecated) | 否 | 是 | 可选择的媒体文件类型。若无此参数，则默认为图片和视频类型。  **说明**：从API version 9开始支持，从API version 18开始废弃。 |
| maxSelectNumber | number | 否 | 是 | 选择媒体文件数量的最大值，默认值为50，最大值为500。  **说明**：从API version 9开始支持，从API version 18开始废弃。 |

## PhotoSelectResult(deprecated)

PhonePC/2in1TabletTV

返回图库选择后的结果集。

说明

从API version 9开始支持，从API version 12开始废弃。建议使用[photoAccessHelper.PhotoSelectResult](arkts-apis-photoaccesshelper-class.md#photoselectresult)替代。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.UserFileService

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| photoUris | Array<string> | 否 | 否 | 返回图库选择后的媒体文件的URI数组。此URI数组只能通过临时授权的方式调用接口[photoAccessHelper.getAssets](arkts-apis-photoaccesshelper-photoaccesshelper.md#getassets)去使用，具体使用方式参见用户文件URI介绍中的[媒体文件URI的使用方式](../harmonyos-guides/user-file-uri-intro.md#媒体文件uri的使用方式)。  **说明**：从API version 9开始支持，从API version 18开始废弃。 |
| isOriginalPhoto | boolean | 否 | 否 | 返回图库选择后的媒体文件是否为原图。true为原图；false不是原图。  **说明**：从API version 9开始支持，从API version 18开始废弃。 |

## PhotoSaveOptions(deprecated)

PhonePC/2in1TabletTV

图片或视频的保存选项。

说明

从API version 9开始支持，从API version 12开始废弃。建议使用[SaveButtonOptions](ts-security-components-savebutton.md#savebuttonoptions)替代。

**系统能力**：SystemCapability.FileManagement.UserFileService

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| newFileNames | Array<string> | 否 | 是 | 拉起photoPicker进行保存图片或视频资源的文件名。若无此参数，则默认需要用户自行输入。  **说明**：从API version 9开始支持，从API version 18开始废弃。 |
