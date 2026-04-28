---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/file-processing-apps-startup
title: 拉起文件处理类应用（startAbility）
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Stage模型开发指导 > 应用间跳转 > 拉起指定类型的应用 > 拉起文件处理类应用（startAbility）
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:52+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d8a40263c7eaf887b5e03e96c7c73aec673561fec3ac83f5eb0e9bedb7fdac2d
---

## 使用场景

开发者可以通过调用[startAbility](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)接口，由系统从已安装的应用中寻找符合要求的应用，打开特定文件。

例如，在浏览器应用中下载PDF文件，可以调用此接口选择文件处理应用打开此PDF文件。开发者需要在请求中设置待打开文件的URI路径（[uri](file-processing-apps-startup.md#接口关键参数说明)）、文件格式（[type](file-processing-apps-startup.md#接口关键参数说明)）等字段，以便系统能够识别，直接拉起文件打开应用或弹出一个选择框，让用户选择合适的应用来打开文件，效果示意如下图所示。

图1 效果示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/p9ztY9vFTZiA2eWefYK3bA/zh-cn_image_0000002552797860.jpeg?HW-CC-KV=V1&HW-CC-Date=20260427T233751Z&HW-CC-Expire=86400&HW-CC-Sign=AC74538E1494F949EF230AC67C946EBA19546BCA1755E0F7007DF7BBD6108B43)

## 接口关键参数说明

开发者通过调用[startAbility](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)接口即可实现由已安装的垂域应用来打开文件。

表1 startAbility请求中[want](../harmonyos-references/js-apis-app-ability-want.md)相关参数说明

| 参数名称 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示待打开文件的URI路径，一般配合type使用。  uri格式为：file://bundleName/path  - file：文件URI的标志。  - bundleName：该文件资源的属主。  - path：文件资源在应用沙箱中的路径。 |
| type | string | 否 | 表示打开文件的类型，推荐使用[UTD类型](uniform-data-type-descriptors.md)，比如：'general.plain-text'、'general.image'。目前也可以兼容使用[MIME type类型](https://www.iana.org/assignments/media-types/media-types.xhtml?utm_source=ld246.com)，如：'text/xml' 、 'image/\*'等。  **说明：**  1. type为可选字段，如果不传type，系统会尝试根据uri后缀名判断文件类型进行匹配；如果传入type，必须确保与uri的文件类型一致，否则会导致无法匹配到合适的应用。文件后缀与文件类型的映射关系参见[Uniform Type Descriptor(UTD)预置列表](uniform-data-type-list.md)。  2. 不支持传\*/\*。 |
| parameters | Record<string, Object> | 否 | 表示由系统定义，由开发者按需赋值的自定义参数，文件打开场景请参考表2。 |
| flags | number | 否 | 表示处理方式，文件打开场景请参考表3。 |
| action | string | 是 | 表示要执行的通用操作。文件打开场景固定值：'ohos.want.action.viewData' ，表示查看数据的操作。 |

**表2** [parameters](../harmonyos-references/js-apis-app-ability-wantconstant.md#params)相关参数说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| ability.params.stream | string | 指示携带的文件URI要授权给目标方，用于待打开的文件存在其他文件依赖的场景。例如打开本地html文件依赖本地其余资源文件的场景等。对应的value必须是string类型的文件URI数组。文件URI的获取参考表1中uri参数。 |
| ohos.ability.params.showDefaultPicker | boolean | 表示是否强制展示文件打开方式的选择弹框，缺省为false。  - false：表示由系统策略或默认应用设置决定直接拉起文件打开应用还是展示弹框。  - true：表示始终展示弹框。 |
| showCaller | boolean | 表示调用方本身作为目标方应用匹配成功时，是否在打开文件的应用选择弹框中展示，缺省为false。  - false：不展示。  - true：展示。 |

**表3** [flags](../harmonyos-references/js-apis-app-ability-wantconstant.md#flags)相关参数说明

| 参数名称 | 值 | 说明 |
| --- | --- | --- |
| FLAG\_AUTH\_READ\_URI\_PERMISSION | 0x00000001 | 指对URI执行读取操作的授权。 |
| FLAG\_AUTH\_WRITE\_URI\_PERMISSION | 0x00000002 | 指对URI执行写入操作的授权。 |

## 接入步骤

### 调用方接入步骤

1. 导入相关模块。

   ```
   1. // xxx.ets
   2. import { fileUri } from '@kit.CoreFileKit';
   3. import { UIAbility, Want, common, wantConstant } from '@kit.AbilityKit';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   5. import { window } from '@kit.ArkUI';
   ```
2. 获取[应用文件路径](application-context-stage.md#获取应用文件路径)。

   ```
   1. // xxx.ets
   2. // 假设应用bundleName值为com.example.demo
   3. export default class EntryAbility extends UIAbility {
   4. onWindowStageCreate(windowStage: window.WindowStage) {
   5. // 获取文件沙箱路径
   6. let filePath = this.context.filesDir + '/test1.txt';
   7. // 将沙箱路径转换为uri
   8. let uri = fileUri.getUriFromPath(filePath);
   9. // 获取的uri为"file://com.example.demo/data/storage/el2/base/files/test.txt"
   10. }
   11. // ...
   12. }
   ```
3. 构造请求数据。

   ```
   1. // xxx.ets
   2. export default class EntryAbility extends UIAbility {
   3. onWindowStageCreate(windowStage: window.WindowStage) {
   4. // 获取文件沙箱路径
   5. let filePath = this.context.filesDir + '/test.txt';
   6. // 将沙箱路径转换为uri
   7. let uri = fileUri.getUriFromPath(filePath);
   8. // 构造请求数据
   9. let want: Want = {
   10. action: 'ohos.want.action.viewData', // 表示查看数据的操作，文件打开场景固定为此值
   11. uri: uri,
   12. type: 'general.plain-text', // 表示待打开文件的类型
   13. // 配置被分享文件的读写权限，例如对文件打开应用进行读写授权
   14. flags: wantConstant.Flags.FLAG_AUTH_WRITE_URI_PERMISSION | wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION
   15. };
   16. }
   17. // ...
   18. }
   ```
4. 调用接口启动。

   ```
   1. // xxx.ets
   2. export default class EntryAbility extends UIAbility {
   3. onWindowStageCreate(windowStage: window.WindowStage) {
   4. // 获取文件沙箱路径
   5. let filePath = this.context.filesDir + '/test.txt';
   6. // 将沙箱路径转换为uri
   7. let uri = fileUri.getUriFromPath(filePath);
   8. // 构造请求数据
   9. let want: Want = {
   10. action: 'ohos.want.action.viewData', // 表示查看数据的操作，文件打开场景固定为此值
   11. uri: uri,
   12. type: 'general.plain-text', // 表示待打开文件的类型
   13. // 配置被分享文件的读写权限，例如对文件打开应用进行读写授权
   14. flags: wantConstant.Flags.FLAG_AUTH_WRITE_URI_PERMISSION | wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION
   15. };
   16. // 调用接口启动
   17. this.context.startAbility(want)
   18. .then(() => {
   19. console.info('Succeed to invoke startAbility.');
   20. })
   21. .catch((err: BusinessError) => {
   22. console.error(`Failed to invoke startAbility, code: ${err.code}, message: ${err.message}`);
   23. });
   24. }
   25. // ...
   26. }
   ```

### 目标方接入步骤

1. 声明文件打开能力。

   支持打开文件的应用需要在[module.json5](module-configuration-file.md)配置文件中声明文件打开能力。其中uris字段表示接收URI的类型，其中scheme固定为file。type字段表示支持打开的文件类型（参见[UTD类型](uniform-data-type-descriptors.md)（推荐）或[MIME type类型](https://www.iana.org/assignments/media-types/media-types.xhtml?utm_source=ld246.com)），如下举例中类型为txt文件。

   ```
   1. {
   2. "module": {
   3. // ...
   4. "abilities": [
   5. {
   6. // ...
   7. "skills": [
   8. {
   9. "actions": [
   10. "ohos.want.action.viewData" // 必填，声明数据处理能力
   11. ],
   12. "uris": [
   13. {
   14. // 允许打开uri中以file://协议开头标识的本地文件
   15. "scheme": "file", // 必填，声明协议类型为文件
   16. "type": "general.plain-text", // 必填，表示支持打开的文件类型
   17. "linkFeature": "FileOpen" // 必填且大小写敏感，表示此URI的功能为文件打开
   18. }
   19. // ...
   20. ]
   21. // ...
   22. }
   23. ]
   24. }
   25. ]
   26. }
   27. }
   ```
2. 应用处理待打开文件。

   声明了文件打开的应用在被拉起后，获取传入的[Want](../harmonyos-references/js-apis-app-ability-want.md)参数信息，从中获取待打开文件的URI，在打开文件并获取对应的file对象后，可对文件进行读写操作。

   ```
   1. // xxx.ets
   2. import { fileIo } from '@kit.CoreFileKit';
   3. import { Want, AbilityConstant, UIAbility } from '@kit.AbilityKit';
   4. import { BusinessError } from '@kit.BasicServicesKit';

   6. export default class EntryAbility extends UIAbility {
   7. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
   8. // 从want信息中获取uri字段
   9. let uri = want.uri;
   10. if (uri == null || uri == undefined) {
   11. console.info('uri is invalid');
   12. return;
   13. }
   14. try {
   15. // 根据待打开文件的URI进行相应操作。例如同步读写的方式打开URI获取file对象
   16. let file = fileIo.openSync(uri, fileIo.OpenMode.READ_WRITE);
   17. console.info('Succeed to open file.');
   18. } catch (err) {
   19. let error: BusinessError = err as BusinessError;
   20. console.error(`Failed to open file openSync, code: ${error.code}, message: ${error.message}`);
   21. }
   22. }
   23. }
   ```
