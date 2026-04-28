---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-aspect-implements-aop
title: 基于Aspect插件库实现切面编程
breadcrumb: 最佳实践 > 应用框架 > ArkTS语言 > 基于Aspect插件库实现切面编程
category: best-practices
scraped_at: 2026-04-28T08:20:06+08:00
doc_updated_at: 2026-03-27
content_hash: sha256:3e092f23ada2f1935354df66855e1fd77005af7850eeaabd4c8324097f25ab0d
---

## 概述

[Aspect](https://gitcode.com/OpenHarmony-ApplicationTPC/aspect)是面向HarmonyOS应用工程的AOP（面向切面编程）插件库，允许开发者在不修改业务核心代码的情况下，对代码进行增强。在实际开发中，开发者可以使用Aspect来模块化实现生命周期函数插桩、事件监听、API调用替换等通用功能。本文主要以实际开发中的各项场景为例，介绍Aspect插件的最佳实践。如需了解如何安装配置与快速上手，可参考[Aspect快速开始](https://gitcode.com/OpenHarmony-ApplicationTPC/aspect/blob/master/README.md)。

Aspect插件库底层对[AbcKit方舟字节码工具库](https://gitcode.com/openharmony/arkcompiler_runtime_core/blob/master/libabckit/README_zh.md)进行了封装，帮助开发者减少对字节码查找和修改细节内容的关注，提高插桩开发效率。其主要功能特性包括：

* 装饰器标记：使用装饰器标记自定义切面类和切面方法，配置插桩任务，实现字节码插桩。
* 方法定义点插桩：支持方法定义点的前置和后置插桩。
* API调用点插桩：支持API调用点的前置、后置和替换插桩。
* UI组件交互事件插桩：支持UI组件交互事件回调函数的前置和后置插桩。
* API异步回调插桩：支持API异步回调函数的前置、后置和替换插桩。

在开始之前，建议了解HarmonyOS应用开发基础并准备好HarmonyOS开发环境和项目工程。

本文主要内容如下：

* [开发流程](bpta-aspect-implements-aop.md#section2075611281159)：介绍所有场景通用的开发流程。
* [不同场景的切面类开发](bpta-aspect-implements-aop.md#section7558828115214)：通过实际开发中的场景，介绍Aspect插件的基本使用方法。
  + [ArkUI组件生命周期函数埋点](bpta-aspect-implements-aop.md#section111420155615)
  + [隐私API调用监控](bpta-aspect-implements-aop.md#section102491613819)
  + [API调用点替换增强](bpta-aspect-implements-aop.md#section246912551823)
  + [API Promise.then回调函数替换](bpta-aspect-implements-aop.md#section132056262411)

## 开发流程

开发者要使用Aspect插件对HarmonyOS工程进行插桩，需要进行编写切面类和注册切面类两个步骤。其中切面类的编写会因场景不同而略有差异，本文将在[不同应用场景的切面类开发](bpta-aspect-implements-aop.md#section7558828115214)中详细介绍。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/nRjqFhLnRPC8YaiDFE39sw/zh-cn_image_0000002563843797.png?HW-CC-KV=V1&HW-CC-Date=20260428T002004Z&HW-CC-Expire=86400&HW-CC-Sign=74E91B3CE755DD7295826365C9E1C0C53C085EEE62F091D7856BD92C9B2F2A54 "点击放大")

### 编写切面类

切面类可以写在工程源码的模块里，也可以写在另外创建的自定义模块里。此处的切面类选择写在自定义MyAspect模块里。

```
1. .
2. ├──entry/src/main/ets                 // entry模块
3. │  └──...
4. ├──MyAspect/src/main/ets              // MyAspect模块
5. │  ├──aop
6. │  │  ├──call
7. │  │  │  └──MyCallAspect.ets          // 切面类
8. │  │  ├──callback
9. │  │  │  └──MyCallbackAspect.ets      // 切面类
10. │  │  ├──definition
11. │  │  │  └──MyDefinitionAspect.ets    // 切面类
12. │  │  └──eventcallback
13. │  │     └──MyEventCallbackAspect.ets // 切面类
14. │  └──AspectRegistryUtil.ets
15. ├──aspect.json
16. ├──...
17. └──README.md
```

### 注册切面类

切面类编写完成后，需要进行注册才可以生效，原因是源码在编译构建过程中，如果文件（这里为声明的切面类）未被引用，编译器的优化操作会导致字节码中不包含该文件内容。

注册流程如下：

1. 在切面类文件的同一个模块下，添加文件AspectRegistryUtil.ets。
2. 在AspectRegistryUtil.ets中定义一个函数aspectRegister()。
3. 在aspectRegister()中，使用AspectRegistry.register()注册切面类。

   ```
   1. // Step 1: Create file MyAspect/src/main/ets/AspectRegistryUtil.ets
   2. import { AspectRegistry } from '@hadss/aspect';
   3. import { MyCallAspect } from './aop/call/MyCallAspect';
   4. import { MyCallbackAspect } from './aop/callback/MyCallbackAspect';
   5. import { MyDefinitionAspect } from './aop/definition/MyDefinitionAspect';
   6. import { MyEventCallbackAspect } from './aop/eventcallback/MyEventCallbackAspect';

   8. // Step 2: Declare a function aspectRegister()
   9. export function aspectRegister(): void {
   10. // Step 3: Register Aspect classes
   11. AspectRegistry.register(MyDefinitionAspect);
   12. AspectRegistry.register(MyCallAspect);
   13. AspectRegistry.register(MyCallbackAspect);
   14. AspectRegistry.register(MyEventCallbackAspect);
   15. }
   ```

   [AspectRegistryUtil.ets](https://gitcode.com/HarmonyOS_Samples/aspect/blob/master/MyAspect/src/main/ets/AspectRegistryUtil.ets#L17-L31)
4. 在目标模块的EntryAbility.ets中引入aspectRegister()，并在onCreate()中调用。

   这里主要是确保编译构建时未被引用的切面类能够编译进字节码文件中。

   ```
   1. import { aspectRegister } from 'myaspect'; // Step 4: import aspectRegister

   3. const TAG: string = '[EntryAbility]';

   5. export default class EntryAbility extends UIAbility {
   6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
   7. aspectRegister(); // Step 4: call aspectRegister
   ```

   [EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/aspect/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L21-L27)
5. 在项目根目录配置aspect.json，如果文件不存在需要手动创建。

   ```
   1. {ProjectRootDir}
   2. .
   3. ├── ...
   4. ├── build-profile.json5
   5. ├── oh-package.json5
   6. └── aspect.json
   ```

   其中key值对应插桩目标模块名（通常未entry或hsp模块），value值对应切面类路径的列表。

   ```
   1. // aspect.json
   2. {
   3. "entry": [
   4. "MyAspect/src/main/ets/components"
   5. ]
   6. }
   ```

## 不同应用场景的切面类开发

### ArkUI组件生命周期函数埋点

**场景描述**

开发者可以在目标方法的定义点插入切面类方法的调用。例如，此处将对自定义组件CompA的生命周期函数aboutToAppear()方法进行前置插桩。插桩后，相当于在aboutToAppear()方法体首行前插入了MyDefinitionAspect.addBefore(joinPoint)的调用语句。

以下是定义点ArkTS源码示例：

```
1. @Component
2. struct CompA {
3. @StorageLink('logList') logList: string[] = [];

5. aboutToAppear(): void {
6. // Aspect will insert here: MyDefinitionAspect.addBefore(joinPoint)
7. this.logList.push(ResourceUtil.getFormatString(this.getUIContext(), $r('app.string.card_definition_aboutToAppear'),
8. TimeUtil.getNowWithHMS()));
9. }

11. build() {
12. Column() {
13. Button(`CompA`)
14. .stateStyles({
15. normal: {
16. .backgroundColor($r('sys.color.comp_background_tertiary'))
17. .fontColor($r('sys.color.font_emphasize'))
18. }
19. })
20. .attributeModifier(new ButtonStyles())
21. }
22. }
23. }
```

[DefinitionBefore.ets](https://gitcode.com/HarmonyOS_Samples/aspect/blob/master/entry/src/main/ets/pages/definition/DefinitionBefore.ets#L80-L102)

**开发步骤**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/AHppVmevQQGdouhcRGiu1Q/zh-cn_image_0000002532723966.png?HW-CC-KV=V1&HW-CC-Date=20260428T002004Z&HW-CC-Expire=86400&HW-CC-Sign=026B2AE096B070F4AF70D37B1F2C850E2502351A09428DD34330A8642F1A9E80 "点击放大")

1. 定义类MyDefinitionAspect，添加装饰器@Aspect将其标记为切面类。
2. 在切面类MyDefinitionAspect中定义方法addBefore()，使用@Before将其标记为前置插桩切面函数。
3. 配置装饰器的入参，以便在目标API方法体首行插入切面逻辑。

   装饰器入参配置：

   * insertType: InsertType.DEFINITION：指定切面插入类型为定义点。
   * scan：配置定义点的扫描范围，指定模块、路径、类和指定方法。

   代码如下：

   ```
   1. @Aspect
   2. export class MyDefinitionAspect {
   3. public static logListLink: SubscribedAbstractProperty<string[]> = AppStorage.link('logList');

   5. @Before({
   6. insertType: InsertType.DEFINITION,
   7. scan: {
   8. module: 'entry',
   9. path: 'src/main/ets/pages/definition/DefinitionBefore',
   10. className: 'CompA',
   11. methodName: 'aboutToAppear'
   12. }
   13. })
   14. static addBefore(joinPoint: JoinPoint): void {
   15. let logList: string[] = AppStorage.get<Array<string>>('logList') ?? [];
   16. logList.push(ResourceUtil.getFormatStringWithoutContext($r('app.string.card_definition_before'),
   17. TimeUtil.getNowWithHMS()));
   18. logList.push(ResourceUtil.getFormatStringWithoutContext($r('app.string.card_location_params_list'),
   19. joinPoint?.className ?? '', joinPoint.moduleName ?? ''));
   20. MyDefinitionAspect.logListLink = AppStorage.link('logList');
   21. MyDefinitionAspect.logListLink.set(logList);
   22. }
   ```

   [MyDefinitionAspect.ets](https://gitcode.com/HarmonyOS_Samples/aspect/blob/master/MyAspect/src/main/ets/aop/definition/MyDefinitionAspect.ets#L20-L42)

### 隐私API调用监控

**场景描述**

开发者可以在目标API的调用点插入切面类方法的调用。例如，此处将对隐私API geoLocationManager.getCurrentLocation()的调用点进行前置插桩，以监控位置信息的调用情况。插桩后，相当于在调用该方法的代码行之前插入了MyCallAspect.addBefore(joinPoint)。

以下是调用点ArkTS源码示例：

```
1. getLocation(): void {
2. const request: geoLocationManager.SingleLocationRequest = {
3. locatingPriority: geoLocationManager.LocatingPriority.PRIORITY_LOCATING_SPEED,
4. locatingTimeoutMs: CommonConstants.LOCATING_TIMEOUT_MS
5. };
6. this.logList.push(ResourceUtil.getFormatString(this.getUIContext(), $r('app.string.card_location_start'),
7. TimeUtil.getNowWithHMS()));
8. // Aspect will insert here: MyCallAspect.addBefore(joinPoint)
9. geoLocationManager.getCurrentLocation(request).then((location: geoLocationManager.Location) => {
10. this.longitude = location.longitude;
11. this.latitude = location.latitude;
12. this.logList.push(ResourceUtil.getFormatString(this.getUIContext(), $r('app.string.card_location_then'),
13. TimeUtil.getNowWithHMS()));
14. }).catch((err: BusinessError) => {
15. Logger.error(TAG, `getLocation failed, code: ${err.code}, message: ${err.message}`);
16. LocationErrorUtil.locationFailedAlert(this.getUIContext(), err.code);
17. });
```

[CallBefore.ets](https://gitcode.com/HarmonyOS_Samples/aspect/blob/master/entry/src/main/ets/pages/call/CallBefore.ets#L82-L98)

**开发步骤**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/uq52LC24QxeEeKrfUCqkoQ/zh-cn_image_0000002532883912.png?HW-CC-KV=V1&HW-CC-Date=20260428T002004Z&HW-CC-Expire=86400&HW-CC-Sign=D54517F6E64E5C49C1EC02FBD29E19E5488410EF2FB823C39889765DB7D998F3 "点击放大")

1. 定义类MyCallAspect，添加装饰器@Aspect将其标记为切面类。
2. 在切面类MyCallAspect中定义方法addBefore()，使用@Before将其标记为前置插桩切面方法。
3. 配置装饰器的入参，以便在目标API调用前插入切面逻辑。

   装饰器入参配置：

   * insertType: InsertType.CALL：指定切面插入类型为调用点。
   * scan：配置调用点的扫描范围，指定模块和路径。
   * api：配置目标API，包括模块、导入名称和方法名称。

   代码如下：

   ```
   1. @Aspect
   2. export class MyCallAspect {
   3. public static logListLink: SubscribedAbstractProperty<string[]> = AppStorage.link('logList');

   5. @Before({
   6. insertType: InsertType.CALL,
   7. scan: {
   8. module: 'entry',
   9. path: 'src/main/ets/pages/call/CallBefore',
   10. },
   11. api: {
   12. module: '@ohos:geoLocationManager',
   13. importName: 'geoLocationManager',
   14. functionName: 'getCurrentLocation',
   15. }
   16. })
   17. static addBefore(joinPoint: JoinPoint): void {
   18. let logList: string[] = AppStorage.get<Array<string>>('logList') ?? [];
   19. logList.push(ResourceUtil.getFormatStringWithoutContext($r('app.string.card_location_before'),
   20. TimeUtil.getNowWithHMS()));
   21. logList.push(ResourceUtil.getFormatStringWithoutContext($r('app.string.card_location_params_list'),
   22. joinPoint?.className ?? '', joinPoint.moduleName ?? ''));
   23. MyCallAspect.logListLink = AppStorage.link('logList');
   24. MyCallAspect.logListLink.set(logList);
   25. }
   ```

   [MyCallAspect.ets](https://gitcode.com/HarmonyOS_Samples/aspect/blob/master/MyAspect/src/main/ets/aop/call/MyCallAspect.ets#L21-L46)

### API调用点替换增强

**场景描述**

开发者可以在不修改业务代码的前提下，以原API调用点为切入点，将目标API替换为切面类方法。

示例中，对CallbackReplacePage类中的getLocation()方法里geoLocationManager.getCurrentLocation()的方法进行替换。替换后，相当于将geoLocationManager.getCurrentLocation()方法的代码换成MyCallAspect.replaceGetLocation()。

以下是调用点ArkTS源码示例：

```
1. getLocationAddress(): void {
2. this.logList.push(ResourceUtil.getFormatString(this.getUIContext(), $r('app.string.card_location_start'),
3. TimeUtil.getNowWithHMS()));
4. // Aspect will replace: entire statement geoLocationManager.getCurrentLocation with MyCallAspect.replaceGet(this.request)
5. geoLocationManager.getCurrentLocation(this.request).then((location: geoLocationManager.Location) => {
6. this.longitude = location.longitude;
7. this.latitude = location.latitude;
8. this.logList.push(ResourceUtil.getFormatString(this.getUIContext(), $r('app.string.card_location_then'),
9. TimeUtil.getNowWithHMS()));
10. }).catch((err: BusinessError) => {
11. Logger.error(TAG, `getLocationAddress failed, code: ${err.code}, message: ${err.message}`);
12. LocationErrorUtil.locationFailedAlert(this.getUIContext(), err.code);
13. });
14. this.logList.push(ResourceUtil.getFormatString(this.getUIContext(), $r('app.string.card_location_end'),
15. TimeUtil.getNowWithHMS()));
16. }
```

[CallReplace.ets](https://gitcode.com/HarmonyOS_Samples/aspect/blob/master/entry/src/main/ets/pages/call/CallReplace.ets#L86-L101)

**开发步骤**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/ibylmMZsQEuFFphK9t6Ryw/zh-cn_image_0000002563763873.png?HW-CC-KV=V1&HW-CC-Date=20260428T002004Z&HW-CC-Expire=86400&HW-CC-Sign=3277228D5DAE76BCB6A02D3DFEADA55EFDA07A3590BE0831351F79F469BC9852 "点击放大")

1. 定义类MyCallAspect，添加装饰器@Aspect将其标记为切面类。
2. 在切面类MyCallAspect中定义方法replaceGetLocation()，使用@Replace将其标记为替换插桩切面函数。

   注意

   切面类方法的参数和返回类型需要与目标方法保持一致。
3. 配置装饰器的入参，以便将目标API调用替换为切面方法。

   装饰器入参配置：

   * insertType: InsertType.CALL：指定切面插入类型为调用点。
   * scan：配置调用点的扫描范围，指定模块和路径。
   * api：配置目标API，包括模块、导入名称和方法名称。

   代码如下：

   ```
   1. @Replace({
   2. insertType: InsertType.CALL,
   3. scan: {
   4. module: 'entry',
   5. path: 'src/main/ets/pages/call/CallReplace',
   6. },
   7. api: {
   8. module: '@ohos:geoLocationManager',
   9. importName: 'geoLocationManager',
   10. functionName: 'getCurrentLocation',
   11. }
   12. })
   13. static async replaceGetLocation(request?: geoLocationManager.CurrentLocationRequest
   14. | geoLocationManager.SingleLocationRequest): Promise<geoLocationManager.Location> {
   15. let logList: string[] = AppStorage.get<Array<string>>('logList') ?? [];
   16. logList.push(ResourceUtil.getFormatStringWithoutContext($r('app.string.card_location_replace'),
   17. TimeUtil.getNowWithHMS(), 31.2304, 121.4737));
   18. // Return sample data
   19. return Promise.resolve({
   20. longitude: 121.4737,
   21. latitude: 31.2304,
   22. altitude: 5.0,
   23. accuracy: 10.0,
   24. timeStamp: new Date().getTime(),
   25. direction: 0,
   26. speed: 0
   27. } as geoLocationManager.Location);
   28. }
   ```

   [MyCallAspect.ets](https://gitcode.com/HarmonyOS_Samples/aspect/blob/master/MyAspect/src/main/ets/aop/call/MyCallAspect.ets#L71-L99)

### API Promise.then回调函数替换

**场景描述**

开发者可以将Promise对象异步调用的then()/catch()回调函数替换为切面类方法。例如，对geoLocationManager.getCurrentLocation().then()的回调函数进行替换插桩。插桩后，相当于该回调函数的代码逻辑替换为了MyCallbackAspect.getAddress()。

以下是ArkTS源码示例：

```
1. getLocation(): void {
2. // Aspect will replace: entire statement in getCurrentLocation.then() with MyCallbackAspect.getAddress(location)
3. geoLocationManager.getCurrentLocation(this.request).then((location: geoLocationManager.Location) => {
4. this.longitude = location.longitude;
5. this.latitude = location.latitude;
6. this.logList.push(ResourceUtil.getFormatString(this.getUIContext(), $r('app.string.card_location_get'),
7. TimeUtil.getNowWithHMS()));
8. }).catch((err: BusinessError) => {
9. Logger.error(TAG, `getLocationAddress failed, code: ${err.code}, message: ${err.message}`);
10. LocationErrorUtil.locationFailedAlert(this.getUIContext(), err.code);
11. });
12. }
```

[CallbackReplace.ets](https://gitcode.com/HarmonyOS_Samples/aspect/blob/master/entry/src/main/ets/pages/callback/CallbackReplace.ets#L81-L92)

**开发步骤**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/7Fn0GbJ2TsyOlB3d2V-1eg/zh-cn_image_0000002563843849.png?HW-CC-KV=V1&HW-CC-Date=20260428T002004Z&HW-CC-Expire=86400&HW-CC-Sign=5CF2F95143A69A38678D14AEA7CD34084C1BD1ADC431B32BB8D8C67117AC2DC4 "点击放大")

1. 定义类MyCallbackAspect，添加装饰器@Aspect将其标记为切面类。
2. 在切面类MyCallbackAspect中定义方法getAddress()，使用@Replace将其标记为替换插桩切面类方法。

   注意

   切面类方法的参数和返回类型需要与目标方法保持一致。
3. 配置装饰器的入参，以便将目标异步回调函数替换为切面类方法。

   装饰器入参配置：

   * insertType: InsertType.CALLBACK：指定切面插入类型为异步回调函数。
   * scan：配置异步回调函数的扫描范围，指定模块和路径。
   * api：配置目标API，包括模块、导入名称和方法名称。

   代码如下：

   ```
   1. @Replace({
   2. insertType: InsertType.CALLBACK,
   3. scan: {
   4. module: 'entry',
   5. path: 'src/main/ets/pages/callback/CallbackReplace',
   6. },
   7. api: {
   8. module: '@ohos:geoLocationManager',
   9. importName: 'geoLocationManager',
   10. functionName: 'getCurrentLocation.then',
   11. }
   12. })
   13. static getAddress(location: geoLocationManager.Location): void {
   14. let logList: string[] = AppStorage.get<Array<string>>('logList') ?? [];
   15. logList.push(ResourceUtil.getFormatStringWithoutContext($r('app.string.card_location_callback_replace'),
   16. TimeUtil.getNowWithHMS()));
   17. try {
   18. const reverseGeocodeRequest: geoLocationManager.ReverseGeoCodeRequest = {
   19. latitude: location.latitude,
   20. longitude: location.longitude,
   21. maxItems: 1
   22. };
   23. geoLocationManager.getAddressesFromLocation(reverseGeocodeRequest, (err, data) => {
   24. if (data) {
   25. const address: string = data[0]?.placeName || '';
   26. logList.push(ResourceUtil.getFormatStringWithoutContext($r('app.string.card_location_callback_replace_address'),
   27. address));
   28. } else {
   29. hilog.error(0xFF00, 'MyAspect',
   30. `getAddressesFromLocation failed, code: ${err?.code}, message: ${err?.message}`);
   31. }
   32. });
   33. } catch (error) {
   34. hilog.error(0xFF00, 'MyAspect', `getAddress failed, code: ${error.code}, message: ${error.message}`);
   35. }
   36. }
   ```

   [MyCallbackAspect.ets](https://gitcode.com/HarmonyOS_Samples/aspect/blob/master/MyAspect/src/main/ets/aop/callback/MyCallbackAspect.ets#L69-L104)

### UI组件事件监听

**场景描述**

开发者可以在基于ArkUI的组件（例如Button，Text）的事件回调函数（例如onClick()，onTouch()）内插入切面类方法的调用。

示例中，此处对EventCallbackBeforePage类的Button组件下onClick()事件进行前置插桩，相当于在onClick()回调函数首行插入了MyEventCallbackAspect.addBefore(JoinPoint)。

ArkTS源码如下所示：

```
1. Button($r('app.string.event_onclick'))
2. .attributeModifier(new ButtonStyles())
3. .onClick(() => {
4. // Aspect will insert here: MyEventCallbackAspect.addBefore(joinPoint)
5. this.logList.push(ResourceUtil.getFormatString(this.getUIContext(), $r('app.string.card_callback_click'),
6. TimeUtil.getNowWithHMS()));
7. });
```

[EventCallbackBefore.ets](https://gitcode.com/HarmonyOS_Samples/aspect/blob/master/entry/src/main/ets/pages/eventcallback/EventCallbackBefore.ets#L59-L65)

**开发步骤**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/bC3Z1CjiQWC-QBViKqZZaA/zh-cn_image_0000002532724012.png?HW-CC-KV=V1&HW-CC-Date=20260428T002004Z&HW-CC-Expire=86400&HW-CC-Sign=96498AE139B356A81B097F197DA0CE87FB5A98B435A8EFBA87B461CD20D2EF39 "点击放大")

1. 定义类MyEventCallbackAspect，添加装饰器@Aspect将其标记为切面类。
2. 在切面类MyEventCallbackAspect中定义方法addBefore()，使用@Before将其标记为前置插桩切面方法，其中切面方法就是实际监听的业务代码。
3. 配置装饰器的入参，以便在目标API调用前插入切面逻辑。

   装饰器入参配置：

   * insertType: InsertType.EVENT\_CALLBACK：指定切面插入类型为事件回调。
   * scan：配置调用点的扫描范围，指定模块和路径。
   * event：配置目标事件，包括组件名、事件名称。

   代码如下：

   ```
   1. @Before({
   2. insertType: InsertType.EVENT_CALLBACK,
   3. scan: {
   4. module: 'entry',
   5. path: 'src/main/ets/pages/eventcallback/EventCallbackBefore',
   6. },
   7. event: {
   8. component: 'Button',
   9. eventFunction: 'onClick',
   10. }
   11. })
   12. static addBefore(joinPoint: JoinPoint): void {
   13. let logList: string[] = AppStorage.get<Array<string>>('logList') ?? [];
   14. logList.push(ResourceUtil.getFormatStringWithoutContext($r('app.string.card_event_callback_before'),
   15. TimeUtil.getNowWithHMS()));
   16. logList.push(ResourceUtil.getFormatStringWithoutContext($r('app.string.card_location_params_list'),
   17. joinPoint?.className ?? '', joinPoint.moduleName ?? ''));
   18. MyEventCallbackAspect.logListLink = AppStorage.link('logList');
   19. MyEventCallbackAspect.logListLink.set(logList);
   20. }
   ```

   [MyEventCallbackAspect.ets](https://gitcode.com/HarmonyOS_Samples/aspect/blob/master/MyAspect/src/main/ets/aop/eventcallback/MyEventCallbackAspect.ets#L23-L42)

## 总结

本文主要介绍了开发者如何使用Aspect插件库，通过编写和注册切面类，实现不同场景下的字节码插桩。其核心在于根据不同场景的需要编写切面类、切面方法，并配置相应的装饰器入参。如需进一步了解如何使用Aspect插件库，可以参考以下文档：

* [装饰器使用指南](https://gitcode.com/OpenHarmony-ApplicationTPC/aspect/blob/master/docs/AnnotationGuide.md)
* [常见问题](https://gitcode.com/OpenHarmony-ApplicationTPC/aspect/blob/master/docs/FAQ.md)
* [获取切入点上下文信息](https://gitcode.com/OpenHarmony-ApplicationTPC/aspect/blob/master/docs/JoinPointGuide.md)
* [从源码构建插件](https://gitcode.com/OpenHarmony-ApplicationTPC/aspect/blob/master/docs/BuildFromSource_win.md)

## 示例代码

[基于Aspect插件库实现切面编程](https://gitcode.com/HarmonyOS_Samples/aspect/tree/master)
