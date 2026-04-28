---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-want
title: @ohos.app.ability.Want (Want)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 通用能力的接口(推荐) > @ohos.app.ability.Want (Want)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fa82a42c13d49154ff28483a9ffa49bc626d820eda81ac57c5cb971f4fcb2d0c
---

Want是对象间信息传递的载体，可以用于应用组件间的信息传递。

其典型应用场景之一是，当UIAbilityA启动UIAbilityB、并需要传入一些数据时，可使用Want作为载体。例如在startAbility接口的入参want中，可以通过abilityName指定启动的目标Ability，也可以通过parameters等字段携带其他数据。

说明

本模块首批接口从API version 9 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 约束限制

PhonePC/2in1TabletTVWearable

受IPC通信的限制，启动Ability时传入的Want字段需满足如下要求。

* API version 23开始，Want字段中支持传递的最大数据为200KB。
* API version 22及之前，Want字段中支持传递的最大数据为100KB。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { Want } from '@kit.AbilityKit';
```

## Want

PhonePC/2in1TabletTVWearable

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityBase

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 是 | 设备ID。在应用启动场景中表示被拉起方的设备ID，如果未设置该字段，则表示指定当前设备。 |
| bundleName | string | 否 | 是 | 应用包名。在应用启动场景中表示被拉起方的应用包名。 |
| moduleName | string | 否 | 是 | 应用模块名。在应用启动场景中表示被拉起方的应用模块名。  **说明：**  若待启动的Ability所属的模块为[HAR](../harmonyos-guides/har-package.md)，则moduleName需为依赖该HAR的[HAP](../harmonyos-guides/hap-package.md)/[HSP](../harmonyos-guides/in-app-hsp.md)的moduleName。 |
| abilityName | string | 否 | 是 | 应用的Ability组件名。在应用启动场景中表示被拉起方的Ability组件名。如果在Want中该字段同时指定了BundleName和AbilityName，则Want可以直接匹配到指定的Ability。AbilityName需要在一个应用的范围内保证唯一。 |
| action | string | 否 | 是 | 表示要执行的通用操作（如：查看、分享、应用详情）。在隐式Want中，开发者可以定义该字段，配合uri或parameters来表示对数据执行的操作。隐式Want定义及匹配规则请参见[显式Want与隐式Want匹配规则](../harmonyos-guides/explicit-implicit-want-mappings.md)。 |
| entities | Array<string> | 否 | 是 | 表示目标Ability额外的类别信息（如：浏览器、视频播放器）。在隐式Want中是对action字段的补充。在隐式Want中，开发者可以定义该字段，来过滤匹配Ability类型。 |
| uri | string | 否 | 是 | 统一资源标识符，一般在应用启动场景中配合type使用，指明待处理的数据类型。如果在Want中指定了uri，则Want将匹配指定的Uri信息，包括scheme、schemeSpecificPart、authority和path信息。 |
| type | string | 否 | 是 | 表示MIME type类型描述，打开文件的类型，主要用于文件管理器打开文件。比如：'text/xml' 、 'image/\*'等，MIME定义请参见[Media Types](https://www.iana.org/assignments/media-types/media-types.xhtml?utm_source=ld246.com)。 |
| parameters | Record<string, Object> | 否 | 是 | 表示WantParams描述。  一、以下Key均由系统赋值，开发者手动修改也不会生效，系统在数据传递时会自动修改为实际值。  - ohos.aafwk.param.callerPid：表示拉起方的pid，值为字符串类型。  - ohos.aafwk.param.callerBundleName：表示拉起方的BundleName，值为字符串类型。  - ohos.aafwk.param.callerAbilityName：表示拉起方的AbilityName，值为字符串类型。  - ohos.aafwk.param.callerNativeName：表示native调用时拉起方的进程名，值为字符串类型。  - ohos.aafwk.param.callerAppId：表示拉起应用的AppId信息，值为字符串类型。  - ohos.aafwk.param.callerAppIdentifier：表示拉起应用的AppIdentifier信息，值为字符串类型。  - ohos.aafwk.param.callerToken：表示拉起方的token，值为字符串类型。  - ohos.aafwk.param.callerUid：表示[BundleInfo](js-apis-bundlemanager-bundleinfo.md#bundleinfo-1)中的uid，应用包里应用程序的uid，值为数值类型。  - ohos.param.callerAppCloneIndex：表示拉起方应用的分身索引，值为数值类型。  - component.startup.newRules：表示是否启用新的管控规则，值为布尔类型。  - moduleName：表示被拉起方的moduleName，值为字符串类型。  - ohos.ability.params.abilityRecoveryRestart：表示当前Ability是否发生了故障恢复重启，值为布尔类型。  - ohos.extra.param.key.showMode：表示拉起元服务的展示模式，值为枚举类型[wantConstant.ShowMode](js-apis-app-ability-wantconstant.md#showmode12)。  **说明**：  在跨端场景中，以下三个字段不生效，不可用于身份或权限校验：ohos.aafwk.param.callerPid、ohos.aafwk.param.callerToken、ohos.aafwk.param.callerUid。  二、提供了一些由系统定义、开发者按需赋值的Key。具体的key值与对应说明详见[wantConstant.Params](js-apis-app-ability-wantconstant.md#params)。  三、除了上述情况，应用间还可以相互约定传入的键值对。  **说明**：  want的Params操作的常量的具体信息请参考[wantConstant](js-apis-app-ability-wantconstant.md)。  需注意，WantParams支持传输的最大数据量遵循[Want约束限制](js-apis-app-ability-want.md#约束限制)。当数据量超过该限制时，请使用[WriteRawDataBuffer](js-apis-rpc.md#writerawdatabuffer11)或[uri](js-apis-uri.md)的方式进行数据传输。  parameters的Value值仅支持基本数据类型：String、Number、Boolean、Object、undefined和null，不支持传递Object内部的function。 |
| flags | number | 否 | 是 | 表示处理Want的方式。值为枚举类型[Flags](js-apis-app-ability-wantconstant.md#flags)，默认传数字。  例如取值为0x00000001（即wantConstant.Flags.FLAG\_AUTH\_READ\_URI\_PERMISSION）表示临时授予接收方读取该URI指向的数据的权限。 |
| fds15+ | Record<string, number> | 是 | 是 | 表示文件描述符，在启动场景中拉起方写入的FD，会设置到该参数中。  **元服务API**：从API version 15开始，该接口支持在元服务中使用。 |

**示例：**

* 基础用法：在UIAbility对象中调用，示例中的context的获取方式请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

  ```
  1. import { UIAbility, Want } from '@kit.AbilityKit';
  2. import { window } from '@kit.ArkUI';
  3. import { BusinessError } from '@kit.BasicServicesKit';

  5. export default class EntryAbility extends UIAbility {
  6. onWindowStageCreate(windowStage: window.WindowStage): void {
  7. let want: Want = {
  8. deviceId: '', // deviceId为空表示本设备
  9. bundleName: 'com.example.myapplication',
  10. abilityName: 'FuncAbility',
  11. moduleName: 'entry' // moduleName非必选
  12. };

  14. this.context.startAbility(want, (err: BusinessError) => {
  15. if (err.code) {
  16. // 显式拉起Ability，通过bundleName、abilityName和moduleName可以唯一确定一个Ability
  17. console.error(`Failed to startAbility. Code: ${err.code}, message: ${err.message}`);
  18. }
  19. });
  20. }
  21. }
  ```
* 目前支持的数据类型有：字符串、数字、布尔、对象、数组和文件描述符等。

  + 字符串（String）

    ```
    1. import { UIAbility, Want } from '@kit.AbilityKit';
    2. import { window } from '@kit.ArkUI';
    3. import { BusinessError } from '@kit.BasicServicesKit';

    5. export default class EntryAbility extends UIAbility {
    6. onWindowStageCreate(windowStage: window.WindowStage): void {
    7. let want: Want = {
    8. bundleName: 'com.example.myapplication',
    9. abilityName: 'FuncAbility',
    10. parameters: {
    11. keyForString: 'str',
    12. },
    13. };

    15. this.context.startAbility(want, (err: BusinessError) => {
    16. if (err.code) {
    17. console.error(`Failed to startAbility. Code: ${err.code}, message: ${err.message}`);
    18. }
    19. });
    20. }
    21. }
    ```
  + 数字（Number）

    ```
    1. import { UIAbility, Want } from '@kit.AbilityKit';
    2. import { window } from '@kit.ArkUI';
    3. import { BusinessError } from '@kit.BasicServicesKit';

    5. export default class EntryAbility extends UIAbility {
    6. onWindowStageCreate(windowStage: window.WindowStage): void {
    7. let want: Want = {
    8. bundleName: 'com.example.myapplication',
    9. abilityName: 'FuncAbility',
    10. parameters: {
    11. keyForInt: 100,
    12. keyForDouble: 99.99,
    13. },
    14. };

    16. this.context.startAbility(want, (err: BusinessError) => {
    17. if (err.code) {
    18. console.error(`Failed to startAbility. Code: ${err.code}, message: ${err.message}`);
    19. }
    20. });
    21. }
    22. }
    ```
  + 布尔（Boolean）

    ```
    1. import { UIAbility, Want } from '@kit.AbilityKit';
    2. import { window } from '@kit.ArkUI';
    3. import { BusinessError } from '@kit.BasicServicesKit';

    5. export default class EntryAbility extends UIAbility {
    6. onWindowStageCreate(windowStage: window.WindowStage): void {
    7. let want: Want = {
    8. bundleName: 'com.example.myapplication',
    9. abilityName: 'FuncAbility',
    10. parameters: {
    11. keyForBool: true,
    12. },
    13. };

    15. this.context.startAbility(want, (err: BusinessError) => {
    16. if (err.code) {
    17. console.error(`Failed to startAbility. Code: ${err.code}, message: ${err.message}`);
    18. }
    19. });
    20. }
    21. }
    ```
  + 对象（Object）

    ```
    1. import { UIAbility, Want } from '@kit.AbilityKit';
    2. import { window } from '@kit.ArkUI';
    3. import { BusinessError } from '@kit.BasicServicesKit';

    5. export default class EntryAbility extends UIAbility {
    6. onWindowStageCreate(windowStage: window.WindowStage): void {
    7. let want: Want = {
    8. bundleName: 'com.example.myapplication',
    9. abilityName: 'FuncAbility',
    10. parameters: {
    11. keyForObject: {
    12. keyForObjectString: 'str',
    13. keyForObjectInt: -200,
    14. keyForObjectDouble: 35.5,
    15. keyForObjectBool: false,
    16. },
    17. },
    18. };

    20. this.context.startAbility(want, (err: BusinessError) => {
    21. if (err.code) {
    22. console.error(`Failed to startAbility. Code: ${err.code}, message: ${err.message}`);
    23. }
    24. });
    25. }
    26. }
    ```
  + 数组（Array）

    ```
    1. import { UIAbility, Want } from '@kit.AbilityKit';
    2. import { window } from '@kit.ArkUI';
    3. import { BusinessError } from '@kit.BasicServicesKit';

    5. export default class EntryAbility extends UIAbility {
    6. onWindowStageCreate(windowStage: window.WindowStage): void {
    7. let want: Want = {
    8. bundleName: 'com.example.myapplication',
    9. abilityName: 'FuncAbility',
    10. parameters: {
    11. keyForArrayString: ['str1', 'str2', 'str3'],
    12. keyForArrayInt: [100, 200, 300, 400],
    13. keyForArrayDouble: [0.1, 0.2],
    14. keyForArrayObject: [{ obj1: 'aaa' }, { obj2: 100 }],
    15. },
    16. };

    18. this.context.startAbility(want, (err: BusinessError) => {
    19. if (err.code) {
    20. console.error(`Failed to startAbility. Code: ${err.code}, message: ${err.message}`);
    21. }
    22. });
    23. }
    24. }
    ```
  + 文件描述符（FD）

    ```
    1. import { UIAbility, Want } from '@kit.AbilityKit';
    2. import { window } from '@kit.ArkUI';
    3. import { BusinessError } from '@kit.BasicServicesKit';
    4. import { fileIo } from '@kit.CoreFileKit';

    6. export default class EntryAbility extends UIAbility {
    7. onWindowStageCreate(windowStage: window.WindowStage): void {
    8. let fd: number = 0;

    10. try {
    11. fd = fileIo.openSync('/data/storage/el2/base/haps/pic.png').fd;
    12. } catch (err) {
    13. let code = (err as BusinessError).code;
    14. let message = (err as BusinessError).message;
    15. console.error(`Failed to openSync. Code: ${code}, message: ${message}`);
    16. }
    17. let want: Want = {
    18. deviceId: '', // deviceId为空表示本设备
    19. bundleName: 'com.example.myapplication',
    20. abilityName: 'FuncAbility',
    21. moduleName: 'entry', // moduleName非必选
    22. parameters: {
    23. 'keyFd': { 'type': 'FD', 'value': fd } // {'type':'FD', 'value':fd}是固定用法，用于表示该数据是FD
    24. }
    25. };

    27. this.context.startAbility(want, (err: BusinessError) => {
    28. if (err.code) {
    29. console.error(`Failed to startAbility. Code: ${err.code}, message: ${err.message}`);
    30. }
    31. });
    32. }
    33. }
    ```
  + parameters参数用法：parameters携带开发者自定义参数，由UIAbilityA传递给UIAbilityB，并在UIAbilityB中进行获取。

    ```
    1. // (1) UIAbilityA通过startAbility启动UIAbilityB
    2. import { UIAbility, Want } from '@kit.AbilityKit';
    3. import { window } from '@kit.ArkUI';
    4. import { BusinessError } from '@kit.BasicServicesKit';

    6. export default class EntryAbility extends UIAbility {
    7. onWindowStageCreate(windowStage: window.WindowStage): void {
    8. let want: Want = {
    9. bundleName: 'com.example.myapplication',
    10. abilityName: 'UIAbilityB',
    11. parameters: {
    12. developerParameters: 'parameters',
    13. },
    14. };

    16. this.context.startAbility(want, (err: BusinessError) => {
    17. if (err.code) {
    18. console.error(`Failed to startAbility. Code: ${err.code}, message: ${err.message}`);
    19. }
    20. });
    21. }
    22. }
    ```

    ```
    1. // (2) 以UIAbilityB实例首次启动为例，会进入到UIAbilityB的onCreate生命周期
    2. import { UIAbility, Want, AbilityConstant } from '@kit.AbilityKit';

    4. class UIAbilityB extends UIAbility {
    5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    6. console.info(`onCreate, want parameters: ${want.parameters?.developerParameters}`);
    7. }
    8. }
    ```
  + parameters参数中[wantConstant](js-apis-app-ability-wantconstant.md)的Key的使用方法。

    ```
    1. import { UIAbility, Want, wantConstant } from '@kit.AbilityKit';
    2. import { window } from '@kit.ArkUI';
    3. import { BusinessError } from '@kit.BasicServicesKit';

    5. export default class EntryAbility extends UIAbility {
    6. onWindowStageCreate(windowStage: window.WindowStage): void {
    7. let want: Want = {
    8. bundleName: 'com.example.myapplication',
    9. abilityName: 'FuncAbility',
    10. parameters: {
    11. [wantConstant.Params.CONTENT_TITLE_KEY]: 'contentTitle',
    12. },
    13. };

    15. this.context.startAbility(want, (err: BusinessError) => {
    16. if (err.code) {
    17. console.error(`Failed to startAbility. Code: ${err.code}, message: ${err.message}`);
    18. }
    19. });
    20. }
    21. }
    ```
  + parameters参数中获取拉起方的信息。

    详见[获取UIAbility拉起方的信息](../harmonyos-guides/uiability-usage.md#获取uiability拉起方的信息)。
