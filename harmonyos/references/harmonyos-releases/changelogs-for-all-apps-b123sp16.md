---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-for-all-apps-b123sp16
title: OS平台API行为的变更
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.2(14) > OS平台能力 > OS平台行为变更说明 > OS平台API行为的变更
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c32a0bb26a32e5c20fe44442f574c556f3409b3e7e9335c21fd083ab9390b036
---

## Ability

### 包管理bundleManager/AbilityInfo中新增必选属性orientationId

**变更原因**

按照终端设备用户的使用习惯，应用应当能够根据设备类型配置默认的窗口旋转方式，应用在orientation配置资源引用，使用时根据资源ID orientationId解析具体配置。

**变更影响**

此变更涉及应用适配。

变更前：应用在构造AbilityInfo时编译无问题。

变更后：应用在构造AbilityInfo时需要添加必选参数orientationId。

**起始API Level**

9

**关键的接口/组件变更**

AbilityInfo.d.ts中新增必选属性orientationId。

**适配指导**

升级到API14后，如果应用在自己的业务中构造了AbilityInfo结构体，则需要在构造的AbilityInfo结构体中新增必选属性orientationId。

## ArkData

### 数据库插入长度为0的Uint8Array的数据，getRow、getValue 接口返回值发生变化

**变更原因**

当插入列类型是blob且数据为长度为0的Uint8Array时，数据库对应错误写入null值，导致使用getRow和getValue接口读取时，读取数值结果错误与插入数据不匹配。

**变更影响**

此变更涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.0.2(14)时生效。

变更前：在blob类型的列里插入长度为0的Uint8Array，调用getRow/getValue接口，获取到的值是null。

变更后：在blob类型的列里插入长度为0的Uint8Array，调用getRow/getValue接口，获取到的值是长度为0的Uint8Array。

**起始API Level**

| 接口名称 | 起始API Level |
| --- | --- |
| getRow | 11 |
| getValue | 12 |

**变更的接口/组件**

@ohos.data.relationalStore.d.ts中getRow接口。

@ohos.data.relationalStore.d.ts中getValue接口。

**适配指导**

变更后，接口的调用方式没有发生变化。开发者需要关注，在blob类型的列里插入长度为0的Uint8Array后，调用getRow或getValue获取到的值发生了变化。

```
1. import { relationalStore } from '@kit.ArkData';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { UIAbility } from '@kit.AbilityKit';
4. import { window } from '@kit.ArkUI';

6. const STORE_CONFIG: relationalStore.StoreConfig = {
7. name: "RdbTest.db",
8. securityLevel: relationalStore.SecurityLevel.S3
9. };
10. const CREATE_TABLE_TEST =
11. "CREATE TABLE IF NOT EXISTS EMPLOYEE (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL, age INTEGER, salary REAL, blobType BLOB)";

13. let store: relationalStore.RdbStore | undefined = undefined;
14. relationalStore.getRdbStore(this.context, STORE_CONFIG, (err: BusinessError, rdbStore: relationalStore.RdbStore) => {
15. store = rdbStore;
16. store.executeSql(CREATE_TABLE_TEST);
17. if (err) {
18. console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
19. return;
20. }
21. console.info('Get RdbStore successfully.');
22. })
23. //在ValuesBucket的blob类型插入长度为0的Uint8Array，并查询该数据。
24. let resultSet: relationalStore.ResultSet | undefined = undefined;
25. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
26. if (store != undefined) {
27. (store as relationalStore.RdbStore).query(predicates).then((result: relationalStore.ResultSet) => {
28. resultSet = result;
29. });
30. }
31. if (resultSet != undefined) {
32. //blobType是数据类型为blob的列名
33. const codes = (resultSet as relationalStore.ResultSet).getValue((resultSet as relationalStore.ResultSet).getColumnIndex("blobType"));
34. }
35. //变更前 codes为null。
36. //变更后 codes为长度为0的Uint8Array。

38. if (resultSet != undefined) {
39. const row = (resultSet as relationalStore.ResultSet).getRow();
40. }
41. //变更前 row.blobType为null。
42. //变更后 row.blobType为长度为0的Uint8Array。
```

### 关系型数据管理@ohos.data.relationalStore.d.ts中getRdbStore接口新增错误码14800020，用于业务侧进行恢复重建数据库

**变更原因**

根密钥和工作密钥不匹配时返回的错误码不正确，新增14800020错误码，此错误码用于业务侧进行恢复重建数据库。

**变更影响**

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.0.2(14)时生效。

变更前：在根密钥和工作密钥不匹配场景下，不会抛出错误码，业务侧无法恢复数据库。

变更后：在根密钥和工作密钥不匹配场景下，会抛出14800020错误码，此错误码可用于业务侧进行恢复重建数据库。

**起始API Level**

9

**变更的接口/组件**

@ohos.data.relationalStore.d.ts中如下接口：

1. function getRdbStore(context: Context, config: StoreConfig, callback: AsyncCallback<RdbStore>): void;
2. function getRdbStore(context: Context, config: StoreConfig): Promise<RdbStore>;

**适配指导**

异常处理：在调用getRdbStore方法后，检查返回的错误码。如果错误码为14800020，表示数据库根密钥与工作密钥不匹配，需要进行重新建库。

```
1. import { relationalStore } from '@kit.ArkData';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { UIAbility } from '@kit.AbilityKit';
4. import { window } from '@kit.ArkUI';

6. const STORE_CONFIG: relationalStore.StoreConfig = {
7. name: "RdbTest.db",
8. securityLevel: relationalStore.SecurityLevel.S3,
9. encrypt: true
10. };
11. const CREATE_TABLE_TEST =
12. "CREATE TABLE IF NOT EXISTS EMPLOYEE (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL, age INTEGER, salary REAL, blobType BLOB)";

14. let store: relationalStore.RdbStore | undefined = undefined;
15. relationalStore.getRdbStore(this.context, STORE_CONFIG, (err: BusinessError, rdbStore: relationalStore.RdbStore) => {
16. store = rdbStore;
17. store.executeSql(CREATE_TABLE_TEST);
18. if (err) {
19. console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
20. //业务侧需要进行数据库恢复。
21. //err.code为14800020业务侧需要进行数据库恢复。
22. return;
23. }
24. console.info('Get RdbStore successfully.');
25. })
```

## ArkTS

### 延迟加载（lazy import）影响异步任务执行时序变更为不影响异步任务执行时序

**变更原因**

延迟加载（lazy import）特性在测试过程中发现问题，使用lazy import的变量，会改变异步任务的运行时序。

**变更影响**

此变更涉及应用适配。

变更前： 使用lazy import的变量，会改变异步任务的运行时序。

变更后： 使用lazy import的变量，不会改变异步任务的运行时序。

**起始API Level**

12

**变更的接口/组件**

不涉及

**适配指导**

排查使用lazy import变量的场景，该功能的时序可能会发生改变。

例如：

```
1. // myLog.ets
2. export class MyLog {
3. static log(s:string) {
4. console.log(s);
5. }
6. }

8. // test.ets
9. import lazy { MyLog } from './myLog'

11. async function asyncFunc(f?:string): Promise<number> {
12. MyLog.log("asyncFunc start");
13. return new Promise(resolve => {
14. resolve(0);
15. });
16. }
17. export async function taskTest() {
18. MyLog.log("taskTest start");
19. asyncFunc().then((res) => {
20. MyLog.log("asyncFunc then");
21. });
22. MyLog.log("taskTest end");
23. }
```

【提示】修改之前，lazy import会影响异步任务的运行时序，该用例的输出为：

```
1. taskTest start
2. asyncFunc start
3. asyncFunc then
4. taskTest end
```

修复问题之后，该用例的输出为：

```
1. taskTest start
2. asyncFunc start
3. taskTest end
4. asyncFunc then
```

本变更修复该问题，使得lazy import不会影响异步任务运行时序。

### 执行幂运算（\*\*）当底数是1，指数是NaN或ToNumber之后是NaN的情况的返回值变更

**变更原因**

ArkTS执行幂运算时，当底数为1，指数为NaN或ToNumber之后是NaN，返回值为1，与ECMAScript® 2021 Language Specification描述不符。

**变更影响**

该变更为不兼容变更。

变更前： 执行幂运算，当底数为1，指数为NaN或ToNumber之后是NaN，返回值为1。

变更后： 执行幂运算，当底数为1，指数为NaN或ToNumber之后是NaN，返回值为NaN。

**起始API Level**

6

**变更的接口/组件**

不涉及

**适配指导**

排查是否对 \*\*（幂运算）有如下情况的使用

例如：

```
1. console.log((1 ** NaN).toString())
```

未变更前该用例输出为：

```
1. 1
```

变更后该用例输出为:

```
1. NaN
```

说明

对于类似 1 \*\* "test" 的用法，在ets文件中不能使用，但是可能在三方库中有使用，该行为同样会变化。

本变更修复该问题，\*\* （幂运算）对于底数是1，指数为NaN或ToNumber之后是NaN的情况会返回NaN。

### String.prototype.lastIndexOf接口查找空字符串行为变更

**变更原因**

String.prototype.lastIndexOf接口查找空字符串时返回值为-1，与ECMAScript® 2021 Language Specification描述不符。

**变更影响**

该变更为不兼容变更。

变更前：String.prototype.lastIndexOf接口查找字符串为空时返回值为-1。

变更后：String.prototype.lastIndexOf接口查找字符串为空时返回值为最后一个字符的位置加1。

**起始API Level**

6

**变更的接口/组件**

String.prototype.lastIndexOf

**适配指导**

排查是否有使用String.prototype.lastIndexOf接口查找空字符串的场景。

例如：

```
1. console.log("abcde".lastIndexOf("").toString())
```

未变更前该用例输出为：

```
1. -1
```

变更后该用例输出为:

```
1. 5
```

本变更修复该问题，String.prototype.lastIndexOf查找空串的结果是最后一个字符的位置加1。

## ArkUI

### ImageAttributeModifier支持new方式创建ColorFilter对象传入colorFilter接口变更

**变更原因**

ImageAttributeModifier不支持new方式创建ColorFilter对象传入colorFilter接口，修复后即可增加colorFilter接口的支持范围，并且ColorFilter在业务代码中传递更加便捷。

**变更影响**

此变更涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.0.2(14)时生效。

变更前：ImageAttributeModifier不支持new方式创建ColorFilter对象传入colorFilter接口。

变更后：ImageAttributeModifier支持new方式创建ColorFilter对象传入colorFilter接口。

**起始API Level**

9

**变更的接口/组件**

ImageAttributeModifier的colorFilter接口。

**适配指导**

已知bug修复，无需适配。使用ImageAttributeModifier的colorFilter接口时，已经支持new方式创建ColorFilter对象传入接口中。示例如下:

```
1. import { ImageModifier } from '@kit.ArkUI'

3. class SelfImageModifier extends ImageModifier {
4. applyNormalAttribute(instance: ImageAttribute): void {
5. let colorFilter = new ColorFilter([0.5, 0.5, 0.5, 0, 0.1, 0.2, 0.2, 0.2, 0, 0.1, 0.1, 0.1, 0.1, 0, 0.1, 0.8, 0.8, 0.8, 0, 0.3])
6. instance.colorFilter(colorFilter)
7. }
8. }

10. @Entry
11. @Component
12. struct ColorFilters {
13. @State modifier: ImageModifier = new SelfImageModifier()

15. build() {
16. Column() {
17. Image($r('app.media.startIcon'))
18. .width(100)
19. .height(100)
20. .attributeModifier(this.modifier)
21. }
22. .height('100%')
23. .width('100%')
24. }
25. }
```

### 轴事件分发机制变更

**变更原因**

轴事件分发错误，开发者如果改了组件z序，组件显示、隐藏后不能正确分发到挂载轴事件的XComponent组件上。

**变更影响**

此变更涉及应用适配。

通过OH\_NativeXComponent\_RegisterUIInputEventCallback接口注册监听回调，在轴事件触发此回调时，分发机制变更。

变更前：在多层级组件堆叠场景下，zIndex属性会影响兄弟组件响应轴事件的顺序。堆叠场景下，先绑定挂载轴事件且zIndex大的组件，然后绑定挂载轴事件且zIndex小的组件，轴事件无法正常分发给挂载轴事件且zIndex较大的组件，而会分发给挂载轴事件但zIndex较小的组件。

变更后：在多层级组件堆叠场景下，zIndex属性会影响兄弟组件响应轴事件的顺序。堆叠场景下，先绑定挂载轴事件且zIndex大的组件，然后绑定挂载轴事件且zIndex小的组件，轴事件可以正常分发给挂载轴事件且zIndex较大的组件，挂载轴事件但zIndex较小的组件无法收到事件。

**起始API Level**

11

**变更的接口/组件**

[OH\_NativeXComponent\_RegisterUIInputEventCallback](../harmonyos-references/capi-native-interface-xcomponent-h.md#oh_nativexcomponent_registeruiinputeventcallback)接口。

**适配指导**

默认行为变更，应注意变更后的行为是否对整体应用逻辑产生影响。

### List组件首次创建布局时，Scroller控制器的跳转方法优先级变更为高于initialIndex的优先级

**访问级别**

公开接口

**变更原因**

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.0.2(14)时生效。

initialIndex仅支持设定起始index，并默认将列表头部对齐，这使得开发者无法自定义对齐策略。scrollToIndex允许指定index与对齐方式，然而其效果会被initialIndex覆盖。因此，需要提升scrollToIndex的优先级，使其高于initialIndex。这样一来，在组件初次布局时，如果开发者希望设定起始index并同时指定对齐方式，即可通过使用scrollToIndex来达成目标。

**变更影响**

此变更涉及应用适配。

场景1：List设置initialIndex为0（默认也是0），并在首次布局前调用scrollToIndex(1)。

| 变更前 | 变更后 |
| --- | --- |
| List首次布局将从index为0的ListItem开始布局。 | List首次布局将从index为1的ListItem开始布局。 |

场景2：List设置initialIndex为0（默认也是0），并在首次布局前调用scrollEdge(Edge.Bottom)。

| 变更前 | 变更后 |
| --- | --- |
| List首次布局将展示在顶部，即index为0的ListItem处于顶部。 | List首次布局将展示在底部，即index为最大值的ListItem处于底部。 |

**起始API Level**

7

**变更的接口/组件**

List组件的initialIndex接口和Scroller控制器的跳转接口（scrollToIndex、scrollToItemInGroup和scrollEdge）。

**适配指导**

需要对使用List组件的页面进行排查，检查是否在onAppear或其他List组件首次布局之前的阶段，同时设置了initialIndex并调用了scrollToIndex,、scrollToItemInGroup或scrollEdge接口。在变更后，initialIndex的生效优先级将低于scrollToIndex、scrollToItemInGroup或scrollEdge的优先级。

### Image组件的borderRadius接口支持动态修改

**变更原因**

为了增强功能的灵活性，Image组件的borderRadius接口支持动态修改。动态修改可以实时更新borderRadius的值，灵活地调整图片的圆角效果。例如，可根据用户交互或状态变化即时改变圆角半径。

**变更影响**

此变更涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.0.2(14)时生效。

变更前：Image组件的borderRadius接口动态修改不生效。

变更后：Image组件的borderRadius接口动态修改生效。

| 变更前 | 变更后 |
| --- | --- |
|  |  |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. @State borderRadiusValue: number = 10;
6. build() {
7. Column() {
8. Text("BorderRadiusValue = " + this.borderRadiusValue)
9. .height(100)
10. .width(200)
11. .fontSize(FontWeight.Bold)
12. Image($r("app.media.sky"))
13. .height(300)
14. .width(300)
15. .borderRadius(this.borderRadiusValue)
16. Button("增加BorderRadius")
17. .onClick(()=>{
18. this.borderRadiusValue += 10
19. })
20. }
21. .height('100%')
22. .width('100%')
23. }
24. }
```

**起始API Level**

7

**变更的接口/组件**

Image组件的borderRadius接口。

**适配指导**

如果应用需要动态修改borderRadius接口，可以在运行时灵活调整圆角效果以响应用户交互或其他状态变化。

如果应用不需要动态修改borderRadius接口，例如：避免在运行时改变圆角效果。borderRadius接口的参数建议设置为固定值，例如：borderRadius('5px')。

### RichEditor（富文本）在光标处于文本起始位置情况时向前删除空文本onWillChange回调变更

**变更原因**

RichEditorController构造的富文本：光标位于文本起始位置时向前删除，触发onWillChange回调范围是[-1, -1]，不符合接口定义。

RichEditorStyledStringController构造的富文本：光标位于文本起始位置时向前删除，触发onWillChange回调范围是[0, 1]，不符合接口定义。

**变更影响**

此变更涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.0.2(14)时生效。

| 组件 | 变更前 | 变更后 |
| --- | --- | --- |
| RichEditorController构造的富文本 | 光标位于文本起始位置时向前删除，触发onWillChange回调范围是[-1, -1]。 | 光标位于文本起始位置时向前删除，触发onWillChange回调范围是[0, 0]。 |
| RichEditorStyledStringController构造的富文本 | 光标位于文本起始位置时向前删除，触发onWillChange回调范围是[0, 1]。 | 光标位于文本起始位置时向前删除，触发onWillChange回调范围是[0, 0]。 |

**起始API Level**

12

**变更的接口/组件**

RichEditor

**适配指导**

默认行为变更，应注意变更后的行为是否对整体应用逻辑产生影响。

### 修复zIndex接口会影响组件在3D变换中的透视效果的错误行为

**变更原因**

zIndex接口在3D变换场景与translateZ耦合，导致zIndex值的改变会影响3D变换时的透视效果。

**变更影响**

此变更涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.0.2(14)时生效。

变更前：开发者在3D变换中使用zIndex接口，zIndex接口的数值会影响近大远小的透视效果。

变更后：开发者在3D变换中使用zIndex接口，zIndex接口的数值不会影响近大远小的透视效果。

设置组件绕y轴旋转45度，同时设置zIndex值为200，变更前后效果如下：

| 变更前 | 变更后 |
| --- | --- |
|  |  |

**起始API Level**

7

**变更的接口/组件**

zIndex接口

**适配指导**

如仍需要实现变更前近大远小的透视效果，可以使用translate接口并设置z向平移实现近大远小的透视效果，示例代码如下：

```
1. @Entry
2. @Preview
3. @Component
4. struct zIndexTest {
5. build() {
6. Column() {
7. Stack() {
8. Column()
9. .backgroundColor("rgb(213, 213, 213)")
10. .width('600px')
11. .height('600px')
12. Column()
13. .backgroundColor("rgb(0, 74, 175)")
14. .width('600px')
15. .height('600px')
16. .rotate({
17. y: 1,
18. angle: 45
19. })
20. .translate({ x: 0, y: 0, z: 66 })    // 使用translate接口并设置Z向移动，实现3D变换中的近大远小透视效果
21. }.margin({ top: 80 })
22. }
23. .width('100%')
24. .height('100%')
25. }
26. }
```

实现效果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/EKVrQdbyStaUPKOkfzz38A/zh-cn_image_0000002300492512.png?HW-CC-KV=V1&HW-CC-Date=20260427T233543Z&HW-CC-Expire=86400&HW-CC-Sign=6F824A7B65D6A49B91D94C652ACBF6B2B47600E375877E78BD4D998236F8F330)

### 屏幕Display对象rotation和orientation属性变更

**变更原因**

手机、平板等不同设备，电子器件贴片方向具有差异，传感器自然方向与屏幕的物理方向具有偏差，导致平板上屏幕Display对象中的rotation和orientation的变化方向和手机不统一，给用户带来困扰，需要针对设备类型做特殊处理，影响使用。

**变更影响**

此变更涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.0.2(14)时生效。

变更后平板上获取屏幕的横竖屏状态时，方向会与更改前不同，与手机保持一致。

变更前后对比效果，如下图所示：

| 设备旋转方向 | 平板变更前 | 平板变更后 | 手机 |
| --- | --- | --- | --- |
|  | rotation: 1  orientation: 0 | rotation: 0  orientation: 0 | rotation: 0  orientation: 0 |
|  | rotation: 2  orientation: 3 | rotation: 1  orientation: 1 | rotation: 1  orientation: 1 |
|  | rotation: 3  orientation: 2 | rotation: 2  orientation: 2 | rotation: 2  orientation: 2 |
|  | rotation: 0  orientation: 1 | rotation: 3  orientation: 3 | rotation: 3  orientation: 3 |

**起始API Level**

7

**变更的接口/组件**

@ohos.display.d.ts文件中屏幕Display对象的rotation和orientation属性。

**适配指导**

平板上监听横竖屏状态变更：

业务方通过display.on('change')监听屏幕属性变化，从Display对象获取的rotation、orientation值。业务方如果在平板上判断rotation、orientation是否为某个横竖屏状态再处理相应业务，需要注意该值的变更。

以充电口朝下方向（此时rotation为0）为准，顺时针旋转0、90、180、270度，平板设备上对应的rotation和orientation对照表如下所示：

| 顺时针旋转角度 | rotation变更前 | rotation变更后 | orientation变更前 | orientation变更后 |
| --- | --- | --- | --- | --- |
| 0 | 1 | 0 | 0 | 0 |
| 90 | 2 | 1 | 3 | 1 |
| 180 | 3 | 2 | 2 | 2 |
| 270 | 0 | 3 | 1 | 3 |

### @ohos.arkui.uiExtension中uiExtension命名空间下新增properties必选属性

**变更原因**

[EmbeddedComponent](../harmonyos-references/ts-container-embedded-component.md)所在的应用窗口移动的场景下，无法获取该组件的大小和位置信息，不满足开发者业务诉求。

**变更影响**

此变更涉及应用适配。

变更前：uiExtension命名空间下的WindowProxy无必选属性properties。

变更后：uiExtension命名空间下的WindowProxy有必选属性properties。

**起始API Level**

14

**变更的接口/组件**

WindowProxy的properties属性

**适配指导**

升级到API14后，如果应用在自己的业务中实现WindowProxy这个Interface，则需要在自定义的实现中新增必选属性properties。

### Navigation的menus接口、NavDestination的title和menus接口支持Resource类型资源

**变更原因**

基础能力增强，Navigationd的menus接口、NavDestination的title和menus接口支持Resource类型资源。

**变更影响**

由于NavigationMenuItem变量类型变更为 string | Resource，不再与单一变量类型string相匹配，因此将NavigationMenuItem赋值给一个string类型变量，程序会编译报错。

```
1. const myIcon: NavigationMenuItem = { value: "图标", icon: "https://example.png"}
2. const myString: string = myIcon.value
```

**起始API Level**

9

**变更的接口/组件**

Navigation的menus接口、NavDestination的title和menus接口

**适配指导**

```
1. // navigation.ets
2. // 使用resource类型资源赋值给Navigation/NavDestination的title及menu接口
3. Navigation() {
4. // xxx
5. }
6. // $r('app.string.MyTestNavigationTitle')需要替换为开发者所需的资源文件
7. .title($r('app.string.MyTestNavigationTitle'))  // 可直接将resource类型资源传递给title接口
8. // menus内的item设置可直接支持resource类型资源
9. .menus([
10. {
11. // $r("app.string.MyTestMenuValue1")和$r("app.media.1")需要替换为开发者所需的资源文件
12. value: $r("app.string.MyTestMenuValue1"),
13. icon: $r("app.media.1")
14. },
15. {
16. // $r("app.string.MyTestMenuValue2")和$r("app.media.2")需要替换为开发者所需的资源文件
17. value: $r("app.string.MyTestMenuValue2"),
18. icon: $r("app.media.2")
19. },
20. {
21. // $r("app.string.MyTestMenuValue3")和$r("app.media.3")需要替换为开发者所需的资源文件
22. value: $r("app.string.MyTestMenuValue3"),
23. icon: $r("app.media.3")
24. }
25. ])
```

```
1. // navDestination.ets
2. // Navigation及NavDestination的CommonTitle类型，支持设置resource资源
3. // 需要替换为开发者所需的资源文件
4. @State commonTitle: NavDestinationCommonTitle = { main: $r('app.string.MyTestNavigationTitle'), sub: $r('app.string.MyTestNavigationTitle')}
5. NavDestination() {
6. // xxx
7. }
8. .menus([
9. {
10. // $r("app.string.MyTestMenuValue1")和$r("app.media.4")需要替换为开发者所需的资源文件
11. value: $r("app.string.MyTestMenuValue1"),
12. icon: $r("app.media.4")
13. },
14. {
15. // $r("app.string.MyTestMenuValue2")和$r("app.media.5")需要替换为开发者所需的资源文件
16. value: $r("app.string.MyTestMenuValue2"),
17. icon: $r("app.media.5")
18. },
19. {
20. // $r("app.string.MyTestMenuValue3")和$r("app.media.6")需要替换为开发者所需的资源文件
21. value: $r("app.string.MyTestMenuValue3"),
22. icon: $r("app.media.6")
23. }
24. ])
25. .title(this.commonTitle)
```

### 在PC/2in1设备上getWindowStatus和on('windowStatusChange')接口在窗口最大化状态返回值变更

**变更原因**

getWindowStatus和on('windowStatusChange')接口在最大化状态返回值为WindowStatusType::FULL\_SCREEN，与实际情况不符合。

应用无法直接通过这两个接口在PC/2in1设备上区分当前最大化和全屏状态，与接口功能设计不符合。

**变更影响**

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.0.2(14)时生效。

变更前：PC/2in1设备上调用getWindowStatus和on('windowStatusChange')接口，在最大化状态返回值为WindowStatusType::FULL\_SCREEN。

变更后：PC/2in1设备上调用getWindowStatus和on('windowStatusChange')接口，在最大化状态返回值为WindowStatusType::MAXIMIZE。

**起始API Level**

on('windowStatusChange')：11

getWindowStatus：12

**变更的接口/组件**

@ohos.window.d.ts

系统能力：SystemCapability.Window.SessionManager

接口：getWindowStatus、on('windowStatusChange')

**适配指导**

针对PC/2in1设备上想要区分当前窗口最大化状态和全屏状态的场景，在变更前后的实现方案分别如下：

* API version 13及之前的版本，可以在窗口状态为WindowStatusType::FULL\_SCREEN的情况下，再调用[getImmersiveModeEnabledState()](../harmonyos-references/arkts-apis-window-window.md#getimmersivemodeenabledstate12)接口进行进一步判断，到底是最大化状态还是全屏状态。若接口返回true则表示当前窗口为全屏状态，若接口返回false则表示当前窗口为最大化状态。
* API version 14及之后的版本，可以直接调用getWindowStatus、on('windowStatusChange')接口区分窗口最大化和全屏状态。

  不过需要注意返回值的变更和代码适配：若应用针对WindowStatusType::FULL\_SCREEN和WindowStatusType::MAXIMIZE状态的代码处理逻辑相同，则在对应的逻辑处理时，直接追加WindowStatusType::MAXIMIZE判断条件（条件或）即可；若应用针对WindowStatusType::FULL\_SCREEN和WindowStatusType::MAXIMIZE状态有不同的处理逻辑，则需要增加新的WindowStatusType::MAXIMIZE条件判断分支中进行窗口最大化状态相关逻辑的处理。

以下示例以on('windowStatusChange')接口为例，提供变更前后PC/2in1设备上区分当前窗口最大化状态和全屏状态的指导和适配示例：

API version 13及之前版本区分最大化状态示例：

```
1. // EntryAbility.ets
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. // ...
6. onWindowStageCreate(windowStage: window.WindowStage) {
7. console.info('onWindowStageCreate');
8. try {
9. let windowClass = windowStage.getMainWindowSync();
10. windowClass?.on("windowStatusChange", (windowStatusType: window.WindowStatusType) => {
11. if (windowStatusType == window.WindowStatusType.FULL_SCREEN) {
12. // isFullScreen 为true 表示全屏，为false 表示最大化
13. let isFullScreen: boolean = windowClass.getImmersiveModeEnabledState();
14. } else {
15. // ...
16. }
17. })
18. } catch (exception) {
19. console.error(`Failed to obtain the main window. Cause code: ${exception.code}, message: ${exception.message}`);
20. }
21. }
22. }
```

API version 14版本区分最大化状态示例：

```
1. // EntryAbility.ets
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. // ...
6. onWindowStageCreate(windowStage: window.WindowStage) {
7. console.info('onWindowStageCreate');
8. try {
9. let windowClass = windowStage.getMainWindowSync();
10. windowClass?.on("windowStatusChange", (windowStatusType: window.WindowStatusType) => {
11. // 应用对于窗口全屏和最大化状态的处理逻辑不同，新增window.WindowStatusType.MAXIMIZE的判断分支
12. if (windowStatusType == window.WindowStatusType.FULL_SCREEN) {
13. // ....
14. } else if (windowStatusType == window.WindowStatusType.MAXIMIZE) {
15. // ...
16. } else {
17. // ...
18. }
19. })
20. } catch (exception) {
21. console.error(`Failed to obtain the main window. Cause code: ${exception.code}, message: ${exception.message}`);
22. }
23. }
24. }
```

API version 14版本不区分最大化状态示例：

```
1. // EntryAbility.ets
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. // ...
6. onWindowStageCreate(windowStage: window.WindowStage) {
7. console.info('onWindowStageCreate');
8. try {
9. let windowClass = windowStage.getMainWindowSync();
10. windowClass?.on("windowStatusChange", (windowStatusType: window.WindowStatusType) => {
11. // 应用对于窗口全屏和最大化状态的处理逻辑相同，直接在判断时新增针对window.WindowStatusType.MAXIMIZE的或条件
12. if (windowStatusType == window.WindowStatusType.FULL_SCREEN ||
13. windowStatusType == window.WindowStatusType.MAXIMIZE) {
14. // ....
15. } else {
16. // ...
17. }
18. })
19. } catch (exception) {
20. console.error(`Failed to obtain the main window. Cause code: ${exception.code}, message: ${exception.message}`);
21. }
22. }
23. }
```

### setWindowLayoutFullScreen、setImmersiveModeEnabledState接口在PC/2in1设备的自由多窗模式上禁用

**变更原因**

因为phone设备上的沉浸式是应用布局全屏且窗口与系统状态栏与导航条交叠，而PC/2in1设备上的沉浸式是应用布局全屏且隐藏系统状态栏和Dock栏，行为与phone设备不一致。所以在PC/2in1设备的自由多窗模式上禁用setWindowLayoutFullScreen、setImmersiveModeEnabledState接口，只能调用maximize接口设置进入/退出沉浸式，在进入最大化时通过maximize接口的入参控制状态栏和Dock栏的隐藏/显示状态。

**变更影响**

变更前：PC/2in1设备的自由多窗模式上调用setWindowLayoutFullScreen、setImmersiveModeEnabledState接口，窗口进入/退出沉浸式。

变更后：PC/2in1设备的自由多窗模式上调用setWindowLayoutFullScreen、setImmersiveModeEnabledState接口不生效。

**起始API Level**

* setWindowLayoutFullScreen：9
* setImmersiveModeEnabledState：12

**变更的接口/组件**

@ohos.window.d.ts

系统能力：SystemCapability.Window.SessionManager

接口：setWindowLayoutFullScreen、setImmersiveModeEnabledState

**适配指导**

PC/2in1设备的自由多窗模式上需要调用[maximize](../harmonyos-references/arkts-apis-window-window.md#maximize12)接口实现窗口沉浸式状态设置。

当调用[setWindowLayoutFullScreen](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)接口时，建议同时调用setWindowLayoutFullScreen和maximize接口。

当调用[setImmersiveModeEnabledState](../harmonyos-references/arkts-apis-window-window.md#setimmersivemodeenabledstate12)接口时，建议同时调用setImmersiveModeEnabledState和maximize接口。

示例：

```
1. // EntryAbility.ets
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. // ...
6. onWindowStageCreate(windowStage: window.WindowStage): void {
7. console.info('onWindowStageCreate');
8. let windowClass: window.Window | undefined = undefined;
9. windowStage.getMainWindow((err: BusinessError, data) => {
10. const errCode: number = err.code;
11. if (errCode) {
12. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
13. return;
14. }
15. windowClass = data;
16. let isLayoutFullScreen = true;
17. try {
18. let promise = windowClass.setWindowLayoutFullScreen(isLayoutFullScreen);
19. promise.then(() => {
20. console.info('Succeeded in setting the window layout to full-screen mode.');
21. }).catch((err: BusinessError) => {
22. console.error(`Failed to set the window layout to full-screen mode. Cause code: ${err.code}, message: ${err.message}`);
23. });
24. } catch (exception) {
25. console.error(`Failed to set the window layout to full-screen mode. Cause code: ${exception.code}, message: ${exception.message}`);
26. }

28. try {
29. let promise = windowClass.maximize(window.MaximizePresentation.ENTER_IMMERSIVE);
30. promise.then(() => {
31. console.info('Succeeded in maximizing the window.');
32. }).catch((err: BusinessError) => {
33. console.error(`Failed to maximize the window. Cause code: ${err.code}, message: ${err.message}`);
34. });
35. } catch (exception) {
36. console.error(`Failed to maximize the window. Cause code: ${exception.code}, message: ${exception.message}`);
37. }
38. });
39. }
40. }
```

```
1. // EntryAbility.ets
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. // ...
6. onWindowStageCreate(windowStage: window.WindowStage): void {
7. console.info('onWindowStageCreate');
8. let windowClass: window.Window | undefined = undefined;
9. windowStage.getMainWindow((err: BusinessError, data) => {
10. const errCode: number = err.code;
11. if (errCode) {
12. console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
13. return;
14. }
15. windowClass = data;
16. try {
17. let enabled = true;
18. windowClass.setImmersiveModeEnabledState(enabled);
19. } catch (exception) {
20. console.error(`Failed to set the window immersive mode enabled status. Cause code: ${exception.code}, message: ${exception.message}`);
21. }

23. try {
24. let promise = windowClass.maximize(window.MaximizePresentation.ENTER_IMMERSIVE);
25. promise.then(() => {
26. console.info('Succeeded in maximizing the window.');
27. }).catch((err: BusinessError) => {
28. console.error(`Failed to maximize the window. Cause code: ${err.code}, message: ${err.message}`);
29. });
30. } catch (exception) {
31. console.error(`Failed to maximize the window. Cause code: ${exception.code}, message: ${exception.message}`);
32. }
33. });
34. }
35. }
```

### setWindowBrightness在PC/2in1设备的行为变更

**变更原因**

PC/2in1设备下，在视频播放页面，通过快捷键调节屏幕亮度不生效，原因是快捷键调节系统亮度，而在视频播放页面屏幕亮度跟随窗口亮度值。

**变更影响**

变更前：PC/2in1设备下，窗口设置屏幕亮度生效时，控制中心和快捷键不可以调整系统屏幕亮度，窗口恢复默认系统亮度之后，控制中心和快捷键可以调整屏幕亮度。

变更后：PC/2in1设备下，窗口设置屏幕亮度生效时，控制中心和快捷键也可以调整系统屏幕亮度。

**起始API Level**

9

**变更的接口/组件**

@ohos.window.d.ts

setWindowBrightness接口

**适配指导**

默认行为变更，无需适配。

## Basic Service Kit

### setAppAccess错误码变更

**变更原因**

为防止资源浪费，禁止应用无限制地通过调用该接口授予三方应用权限，当授权应用数量超过1024个时，返回新增的错误码（12400005）。

**变更影响**

此变更涉及应用适配。

变更前：setAppAccess传入的第三方应用包名未安装时，返回错误码12400001提示应用未找到。

变更后：setAppAccess传入的第三方应用包名未安装时，当已授权的应用列表未超过限制数量时返回成功，当已授权的应用列表超过了限制数量，返回错误码12400005提示授权应用数量超过了上限。

**起始API Level**

9

**变更的接口/组件**

@ohos.account.appAccount.d.ts中如下接口：

* setAppAccess(name: string, bundleName: string, isAccessible: boolean, callback: AsyncCallback<void>): void
* setAppAccess(name: string, bundleName: string, isAccessible: boolean): Promise<void>

**适配指导**

调用setAppAccess接口新增12400005错误码,示例如下:

```
1. import { BusinessError } from '@ohos.base';
2. import account_appAccount from '@ohos.account.appAccount';

4. let appAccountManager: account_appAccount.AppAccountManager = account_appAccount.createAppAccountManager();

6. try {
7. appAccountManager.setAppAccess('ZhangSan', 'com.example.accountjsdemo', true, (err: BusinessError) => {
8. if (err.code === 12400005) {
9. //处理授权应用数量超过上限异常，比如对之前已授权的应用取消授权
10. } else if (err) {
11. console.log('setAppAccess failed: ' + JSON.stringify(err));
12. } else {
13. console.log('setAppAccess successfully');
14. }
15. });
16. } catch (err) {
17. console.log('setAppAccess exception: ' + JSON.stringify(err));
18. }
```

## Call Service Kit

### kit.CallKit.d.ts文件废弃，替换为kit.CallServiceKit.d.ts文件访问级别

**变更原因**

命名优化

**变更影响**

此变更涉及应用适配。

应用导入依赖时，强烈建议使用更名后的kit，即kit.CallServiceKit.d.ts。如继续使用kit.CallKit.d.ts，可能会在后续版本出现错误。

**起始API Level**

4.1.0(11)

**变更的接口/组件**

变更前：kit.CallKit.d.ts文件

变更后：kit.CallServiceKit.d.ts文件

**适配指导**

以导入voipCall为例，导入voipCall时，需要使用新的kit文件，其他代码不需要修改：

变更前：import { voipCall } from '@kit.CallKit';

变更后：import { voipCall } from '@kit.CallServiceKit';

## Core File Kit

### 持久化权限激活接口实现从sandbox\_manager模块切换到UPMS模块

**变更原因**

sandbox\_manager权限清理存在时序问题，需要在临时授权中添加时间戳，所有的临时授权调节到UPMS统一添加时间戳处理。

**变更影响**

此变更涉及应用适配。

变更前：fileShare.activatePermission和OH\_FileShare\_ActivatePermission激活接口调用sandbox\_manager接口能力实现激活功能，应用退出阶段可以进行激活持久化权限。

变更后：fileShare.activatePermission和OH\_FileShare\_ActivatePermission激活接口调用UPMS接口能力实现激活功能，且在应用退出阶段不能进行持久化权限激活操作（退出阶段激活的权限在退出之后也会进行权限回收，这个阶段的激活操作实际没有意义）。

**起始API Level**

11

**变更的接口/组件**

@ohos.fileshare.d.ts的ArkTS API：ohos.fileshare.activatePermission。

oh\_file\_share.h中的C API：OH\_FileShare\_ActivatePermission

**适配指导**

开发者在使用时无需重新适配，接口内部处理流程更新。

如果开发者在应用退出阶段调用了激活接口：

变更前：会激活成功。

变更后：返回13900001错误码，提示不允许操作。

由于该阶段的激活属于无效操作，因此建议开发者删除此阶段的激活操作或者忽略此阶段的激活失败。

## Core Vision Kit

### @hms.ai.vision.objectDetection.d.ts和@hms.ai.vision.skeletonDetection.d.ts方法文件变更

**变更原因**

错误信息表述有误。

**变更影响**

此变更涉及应用适配。

变更前：在多目标识别与骨骼点检测SDK中，错误码1011000001和1011000002错误信息写反。

\* @throws { BusinessError } 1011000001 - The service is abnormal.

\* @throws { BusinessError } 1011000002 - Failed to run, please try again.

变更后：错误码1011000001和1011000002错误信息与实际实现以及资料保持一致。

\* @throws { BusinessError } 1011000001 - Failed to run, please try again.

\* @throws { BusinessError } 1011000002 - The service is abnormal.

**起始API Level**

5.0.0(12)

**变更的接口/组件**

* static create(): Promise<ObjectDetector>
* process(request: visionBase.Request): Promise<ObjectDetectionResponse>
* static create(): Promise<SkeletonDetector>
* process(request: visionBase.Request): Promise<SkeletonDetectionResponse>

**适配指导**

无需特殊适配，实现未进行变更，不影响开发者实际对涉及接口的使用。

## DFX Kit

## Form Kit

### FormLink的router事件允许拉起Ability类型范围变更

**变更原因**

FormLink的router事件当前未对被拉起的Ability类型进行校验，但实际此事件应只允许拉起UIAbility，针对使用router事件拉起非UIAbility的场景，需要做安全加固。

**变更影响**

此变更涉及应用适配。

变更前：通过FormLink接口的router事件，可以拉起所有类型的Ability。

变更后：通过FormLink接口的router事件，仅允许拉起UIAbility。

**起始API Level**

9

**变更的接口/组件**

FormLink

**适配指导**

应用侧使用FormLink接口的router事件拉起Ability时，需确保拉起的目标Ability属于UIAbility。若需要拉起其他类型的Ability，建议通过其他类型的事件，例如message事件，跳转到FormExtensionAbility内处理。

## Image Kit

### image.ImageSource.DecodingOptionsForPicture接口的desiredAuxiliaryPictures属性系统能力变更

**变更原因**

接口DecodingOptionsForPicture与属性desiredAuxiliaryPictures归属的系统能力不一致，会影响对接口支持系统能力情况的判断，需要将desiredAuxiliaryPictures的SystemCapability中的SystemCapability.Multimedia.Image.Core改为SystemCapability.Multimedia.Image.ImageSource。

**变更影响**

此变更涉及应用适配。

对接口中属性的SystemCapability进行调整，对接口本身的使用方式无影响。

变更前：DecodingOptionsForPicture接口的系统能力要求为“SystemCapability.Multimedia.Image.Core”。

变更后：DecodingOptionsForPicture接口的系统能力要求为“SystemCapability.Multimedia.Image.ImageSource”。

**起始API Level**

13

**变更的接口/组件**

@ohos.multimedia.image中涉及修改的属性如下：

| 接口名 | 接口说明 | 属性名 | 属性说明 |
| --- | --- | --- | --- |
| image.ImageSource.DecodingOptionsForPicture | 图像解码设置选项 | desiredAuxiliaryPictures | 设置AuxiliaryPicture类型，默认解码所有AuxiliaryPicture类型。 |

**适配指导**

接口中属性的SystemCapability正常应该与对应接口的SystemCapability一致。但如果代码中涉及调用canIUse()方法对本次变更涉及接口支持情况进行判断，则应修改canIUse()方法传入的SystemCapability，判断设备是否支持图片源解码解析能力需使用canIUse("SystemCapability.Multimedia.Image.ImageSource")。

### image.Component.setAuxiliaryPictureInfo接口行为变更

**变更原因**

通过setAuxiliaryPictureInfo设置辅助图信息时，会将辅助图信息中的size、pixelFormat等信息同步到pixelMap的ImageInfo中，需要对size和pixelFormat信息做合法校验，防止对pixelMap像素数据信息的越界访问。

**变更影响**

此变更涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.0.2(14)时生效。

变更前：setAuxiliaryPictureInfo()接口设置辅助图信息时，对pixelFormat没有校验，都可以设置成功。

变更后：setAuxiliaryPictureInfo()接口设置辅助图信息时，若将存储像素字节数变大，则设置不成功，返回错误码401。例如将pixelFormat从RGBA\_8888设置为RGBA\_F16。

**起始API Level**

13

**变更的接口/组件**

| API类型 | 所在d.ts文件 | 接口名 | 接口起始版本 |
| --- | --- | --- | --- |
| ArkTS API | @ohos.multimedia.image.d.ts | setAuxiliaryPictureInfo(info: AuxiliaryPictureInfo): void | 13 |

**适配指导**

设置辅助图信息时，如果将存储像素字节数变大，则设置不成功，返回错误码401。

```
1. import { image } from '@kit.ImageKit';
2. import { colorSpaceManager } from '@kit.ArkGraphics2D';
3. async function setAuxiliaryPitcutreInfo() {
4. const array: ArrayBuffer = new ArrayBuffer(100);
5. let imageSource: image.ImageSource = image.createImageSource(array);
6. let options: image.DecodingOptionsForPicture = {
7. desiredAuxiliaryPictures: [image.AuxiliaryPictureType.FRAGMENT_MAP]
8. };
9. try {
10. let picture: image.Picture = await imageSource.createPicture(options);
11. let auxiliaryPicture = picture.getAuxiliaryPicture(image.AuxiliaryPictureType.FRAGMENT_MAP);
12. let originInfo = auxiliaryPicture?.getAuxiliaryPictureInfo();
13. console.info("CreatePicture", 'originInfo = ' + JSON.stringify(originInfo));
14. let changedInfo: image.AuxiliaryPictureInfo = {
15. auxiliaryPictureType: image.AuxiliaryPictureType.FRAGMENT_MAP,
16. size: { height: 410, width: 3072 },
17. rowStride: 3072 * 8,
18. pixelFormat: image.PixelMapFormat.RGBA_F16,
19. colorSpace: colorSpaceManager.create(colorSpaceManager.ColorSpace.DCI_P3),
20. };
21. try {
22. auxiliaryPicture?.setAuxiliaryPictureInfo(changedInfo);
23. console.info("CreatePicture", `changedInfo us ${changedInfo}`);
24. } catch (error) {
25. console.error("CreatePicture", `setAuxiliaryPictureInfo, error.code is ${error.code}, error.message is ${error.message}`);
26. }
27. } catch (err) {
28. console.error("CreatePicture", ' decode Picture failed !!!');
29. }
30. }
```

### image.Component.OH\_AuxiliaryPictureNative\_SetInfo()接口行为变更

**变更原因**

通过OH\_AuxiliaryPictureNative\_SetInfo设置辅助图信息时，会将辅助图信息中的size、pixelFormat等信息同步到pixelMap的ImageInfo中，需要对size和pixelFormat信息做合法校验，防止对pixelMap像素数据信息的越界访问。

**变更影响**

此变更涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.0.2(14)时生效。

变更前：OH\_AuxiliaryPictureNative\_SetInfo()接口设置辅助图信息时，对pixelFormat没有校验，都可以设置成功。

变更后：OH\_AuxiliaryPictureNative\_SetInfo()接口设置辅助图信息时，若将存储像素字节数变大，则设置不成功，返回错误码401。例如将pixelFormat从RGBA\_8888设置为RGBA\_F16。

**起始API Level**

13

**变更的接口/组件**

| API类型 | 所在头文件 | 接口名 | 接口起始版本 |
| --- | --- | --- | --- |
| C API | picture\_native.h | Image\_ErrorCode OH\_AuxiliaryPictureNative\_SetInfo(OH\_AuxiliaryPictureNative \*auxiliaryPicture, OH\_AuxiliaryPictureInfo \*info) | 13 |

**适配指导**

设置辅助图信息时，如果将存储像素字节数变大，则设置不成功，返回错误码401。

```
1. #include <hilog/log.h>
2. #include <multimedia/image_framework/image/image_native.h>
3. #include <multimedia/image_framework/image/image_packer_native.h>
4. #include <multimedia/image_framework/image/image_source_native.h>
5. #include <multimedia/image_framework/image/picture_native.h>
6. Image_ErrorCode SetAuxiliaryPictureInfoTest() {
7. size_t filePathSize = 1024;
8. OH_ImageSourceNative* imageSource = nullptr;
9. Image_ErrorCode image_ErrorCode = OH_ImageSourceNative_CreateFromUri("test.jpg", filePathSize, &imageSource);
10. if (image_ErrorCode != Image_ErrorCode::IMAGE_SUCCESS || imageSource == nullptr) {
11. OH_LOG_ERROR(LOG_APP, "OH_ImageSourceNative_CreateFromUri failed.");
12. }
13. OH_DecodingOptionsForPicture *opts = nullptr;
14. OH_DecodingOptionsForPicture_Create(&opts);
15. OH_PictureNative *picture = nullptr;
16. image_ErrorCode = OH_ImageSourceNative_CreatePicture(imageSource, opts, &picture);
17. OH_ImageSourceNative_Release(imageSource);
18. OH_DecodingOptionsForPicture_Release(opts);
19. if (image_ErrorCode != Image_ErrorCode::IMAGE_SUCCESS || picture == nullptr) {
20. OH_LOG_ERROR(LOG_APP, "OH_ImageSourceNative_CreatePicture failed. image_ErrorCode=%{public}d", image_ErrorCode);
21. }
22. OH_AuxiliaryPictureNative *auxiliaryPicture = nullptr;
23. image_ErrorCode = OH_PictureNative_GetAuxiliaryPicture(
24. picture, Image_AuxiliaryPictureType::AUXILIARY_PICTURE_TYPE_FRAGMENT_MAP, &auxiliaryPicture);
25. if (image_ErrorCode != Image_ErrorCode::IMAGE_SUCCESS || auxiliaryPicture == nullptr) {
26. OH_LOG_ERROR(LOG_APP, "OH_PictureNative_GetAuxiliaryPicture failed. image_ErrorCode=%{public}d", image_ErrorCode);
27. }
28. OH_AuxiliaryPictureInfo *auxInfo = nullptr;
29. image_ErrorCode = OH_AuxiliaryPictureNative_GetInfo(auxiliaryPicture, &auxInfo);
30. PIXEL_FORMAT newPixelFormat = PIXEL_FORMAT_RGBA_F16;
31. OH_AuxiliaryPictureInfo_SetPixelFormat(auxInfo, newPixelFormat);
32. image_ErrorCode = OH_AuxiliaryPictureNative_SetInfo(auxiliaryPicture, auxInfo);
33. if (image_ErrorCode != Image_ErrorCode::IMAGE_SUCCESS || auxInfo == nullptr) {
34. OH_LOG_ERROR(LOG_APP, "OH_AuxiliaryPictureNative_SetInfo failed. image_ErrorCode=%{public}d", image_ErrorCode);
35. }
36. OH_AuxiliaryPictureInfo_Release(auxInfo);
37. OH_AuxiliaryPictureNative_Release(auxiliaryPicture);
38. return IMAGE_SUCCESS;
39. }
```

### image接口Heif格式类型变更

**变更原因**

相机Heif编码时，使用图片标准定义image/heic参数编码失败，当前版本Image中的格式参数定义为image/heif，不符合图片标准定义，为提升规范性，将Heif格式图片mimeType变更为image/heic。

**变更影响**

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.0.2(14)时生效。

1. OH\_PackingOptions\_SetMimeType()接口Heif格式参数类型变更，此变更涉及应用适配。

   变更前：设置Heif格式图片mimeType传入参数为image/heif。

   变更后：设置Heif格式图片mimeType传入参数为image/heic。
2. OH\_PackingOptions\_GetMimeType()接口Heif格式返回类型变更，此变更涉及应用适配。

   变更前：获取Heif格式图片mimeType为image/heif。

   变更后：获取Heif格式图片mimeType为image/heic。
3. 调用ImageSource实例提供的supportedFormats接口查询设备支持解码Heif格式返回类型变更，此变更涉及应用适配。

   变更前：查询设备支持的解码类型Heif格式返回值为image/heif。

   变更后：查询设备支持的解码类型Heif格式返回值为image/heic。
4. 调用ImagePacker实例提供的supportedFormats接口查询设备支持编码Heif格式返回类型变更，此变更涉及应用适配。

   变更前：查询设备支持的编码类型Heif格式返回值为image/heif。

   变更后：查询设备支持的编码类型Heif格式返回值为image/heic。
5. image.PackingOption结构体Heif格式编码参数变更，此变更不涉及应用适配。

   变更前：Heif格式图片编码参数的mimeType类型为image/heif。

   变更后：Heif格式图片编码参数的mimeType类型为image/heif或者image/heic。
6. OH\_PackingOptions结构体Heif格式编码参数变更，此变更不涉及应用适配。

   变更前：Heif格式图片编码参数的mimeType类型为image/heif。

   变更后：Heif格式图片编码参数的mimeType类型为image/heif或者image/heic。

**起始API Level**

10-12

**变更的接口/组件**

| API类型 | 所在d.ts/头文件 | 接口名 | 接口起始版本 |
| --- | --- | --- | --- |
| C API | image\_packer\_native.h | Image\_ErrorCode OH\_PackingOptions\_SetMimeType(OH\_PackingOptions \*options, Image\_MimeType \*format) | 12 |
| C API | image\_packer\_native.h | Image\_ErrorCode OH\_PackingOptions\_GetMimeType(OH\_PackingOptions \*options, Image\_MimeType \*format) | 12 |
| ArkTS API | @ohos.multimedia.image.d.ts | imagePacker.supportedFormats: Array<string> | 10 |
| ArkTS API | @ohos.multimedia.image.d.ts | imageSource.supportedFormats: Array<string> | 10 |
| ArkTS API | @ohos.multimedia.image.d.ts | image.PackingOption | 11 |
| C API | image\_packer\_native.h | struct OH\_PackingOptions | 12 |

**适配指导**

1. 调用OH\_PackingOptions\_SetMimeType(OH\_PackingOptions \*options, Image\_MimeType \*format)设置Heif格式图片mimeType时，需要将传入的format参数更新为image/heic。
2. 调用OH\_PackingOptions\_GetMimeType(OH\_PackingOptions \*options, Image\_MimeType \*format)获取Heif格式图片mimeType时，返回的format为image/heic，开发者需检视应用的示例工程，根据实际情况修改。
3. 调用ImageSource实例提供的supportedFormatsImageSource实例提供的查询设备的解码类型时，开发者调用行为不变，如果设备支持Heif类型，返回值将由image/heif变更为image/heic。
4. 调用ImagePacker实例提供的supportedFormatsImageSource实例提供的查询设备的编码类型时，开发者调用行为不变，如果设备支持Heif类型，返回值将由image/heif变更为image/heic。
5. 调用image.PackingOption进行Heif图片编码时，开发者调用参数可以使用变更前的image/heif类型，也可以使用image/heic类型。
6. 调用OH\_PackingOptions进行Heif图片编码时，开发者调用参数可以使用变更前的image/heif类型，也可以使用image/heic类型。

## Media Kit

### AVErrorCode枚举值变更

**变更原因**

播放器当前上报的IO错误码只有一个，为了帮助开发者更好地了解播放失败的原因，本次细化了IO相关错误，提升生态应用友好度。

**变更影响**

此变更涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.0.2(14)时生效。

变更前：应用使用到该接口时，错误码上报规则保持不变，涉及到IO返回错误的接口返回原有的值。

变更后：播放框架返回IO类网络错误时，对应的错误码会细化，涉及到IO返回错误的接口返回值会有变化，用户升级后需要适配新的错误码上报规则。

| 接口声明 | 变更前 | 变更后 |
| --- | --- | --- |
| AVPlayer.on(type: 'error', callback: ErrorCallback) | AVERR\_IO = 5400103 | 网络场景原有错误码废弃，返回细化后的错误码5411001 ~ 5411011，其余场景不变。 |
| void (\*OH\_AVPlayerOnErrorCallback)(OH\_AVPlayer \*player, int32\_t errorCode, const char \*errorMsg) | AV\_ERR\_IO = 4 | 网络场景原有错误码废弃，返回细化后的错误码5411001 ~ 5411011，其余场景不变。 |

**起始API Level**

9

**变更的接口/组件**

1. @ohos.multimedia.media.d.ts中接口：

   AVPlayer.on(type: 'error', callback: ErrorCallback)。
2. avplayer\_base.h中接口：

   void (\*OH\_AVPlayerOnErrorCallback)(OH\_AVPlayer \*player, int32\_t errorCode, const char \*errorMsg)。

**适配指导**

变更后，应用监听IO相关错误时，需新增5411001 ~ 5411011内的错误码监听。

参考Media错误码说明文档。

## Scan Kit

### 自定义界面扫码权限校验错误码变更

**变更原因**

按照错误码规范要求，权限不足时报201错误码。

**变更影响**

此变更涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.0.2(14)时生效。

变更前：在未申请相机权限时调用customScan模块init接口，返回错误码1000500001。customScan模块start接口未作相机权限检验，会检验init接口调用状态，init接口调用失败返回错误码1000500001。

变更后：在未申请相机权限时调用customScan模块init接口和start接口，返回错误码201。

**起始API Level**

4.1.0(11)

**变更的接口/组件**

customScan模块下接口：

* init(options?: scanBarcode.ScanOptions):void;
* start(viewControl: ViewControl, callback: AsyncCallback<Array<scanBarcode.ScanResult>>, frameCallback?: AsyncCallback<ScanFrame>): void;
* start(viewControl: ViewControl): Promise<Array<scanBarcode.ScanResult>>;

**适配指导**

无需特殊适配，如果有根据错误码去申请相机权限的场景，需要将错误码从1000500001变更为201。

### 集成自定义界面扫码应用适配窗口子系统属性变更

**变更原因**

窗口子系统[屏幕Display对象rotation和orientation属性变更](changelogs-for-all-apps-b123sp16.md#屏幕display对象rotation和orientation属性变更)，会导致集成自定义界面扫码的应用相机预览画面和码图位置出现错误，影响用户使用。

**变更影响**

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.0.2(14)时生效。

变更前：手机和平板旋转同样的角度，从屏幕Display对象中的rotation和orientation获取的值不一致，业务方处理相机预览画面和码图位置时，需要针对设备类型做特殊适配。

变更后：手机和平板旋转同样的角度，从屏幕Display对象中的rotation和orientation获取的值保持一致，业务方使用变更前的适配方案会导致平板相机预览画面和码图位置错误，需要统一使用Display对象的rotation属性处理手机和平板设备。

**起始API Level**

4.1.0(11)

**变更的接口/组件**

@ohos.display.d.ts文件中屏幕Display对象的rotation和orientation属性。

**适配指导**

业务方需要获取Display对象并读取其[rotation](../harmonyos-references/js-apis-display.md#display)属性值，根据rotation值、XComponent宽高和位置计算自定义扫码识别结果码图位置，请参考[示例代码](https://gitcode.com/harmonyos_samples/scan-kit_-sample-code_-clientdemo_-arkts)。

## 调试工具

### hdc file recv命令不支持操作媒体库目录

**变更原因**

由于业务演进方向不同，媒体和文档目录需要不同的权限策略，变更后禁止通过hdc file recv命令将媒体库目录内文件从远端设备接收至本地。

**变更影响**

此变更涉及应用适配。

变更前：hdc命令中file recv（接收）命令可以操作媒体库目录内文件从远端设备接收至本地。

变更后：hdc命令中file recv（接收）命令无法操作媒体库目录内文件从远端设备接收至本地。

**起始API Level**

不涉及

**变更的接口/组件**

hdc命令行工具

**适配指导**

媒体库目录包含

/storage/cloud/<USERID>/files/Photo

/storage/media/<USERID>/local/files/Photo

通过如下两步操作可以将媒体库文件接收到本地：

1. 通过mediatool recv命令将指定uri对应的媒体库资源的源文件内容导出到定的设备路径下（/data/local/tmp），具体操作说明可阅读[mediatool参考文档](../harmonyos-guides/mediatool.md#导出命令mediatool-recv)。

   ```
   1. > mediatool recv file://media/Photo/3 /data/local/tmp/out.jpg
   2. Table Name: Photos
   3. /data/local/tmp/out.jpg
   ```
2. 通过hdc file recv命令将媒体文件从远端设备接收文件至本地。

   ```
   1. > hdc file recv /data/local/tmp/out.jpg ./out.jpg
   ```

### hdc的file recv命令及shell读取权限变更

**变更原因**

为了更好的保护终端用户的隐私安全，加强hdc/shell对系统目录文件的权限管控。

**变更影响**

此变更涉及应用适配。

变更前：支持通过hdc/shell对系统目录文件访问，如调试应用数据沙箱等。

变更后：用户所在用户组必须具备访问调试应用沙箱目录的权限，方能通过hdc/shell访问该目录。

**起始API Level**

不涉及

**变更的接口/组件**

hdc命令行工具

**适配指导**

通过hdc访问调试签名的应用的数据沙箱目录文件，需要在目录、文件创建时指定用户组读取权限。

路径如：

/data/app/el1/<USERID>/base/<BUNDLENAME>

/data/app/el1/<USERID>/database/<BUNDLENAME>

/data/app/el2/<USERID>/base/<BUNDLENAME>

/data/app/el2/<USERID>/database/<BUNDLENAME>

### hidumper组件内存输出显示每列后新增一个空格

**变更原因**

解决生态调优测试的显示问题。

**变更影响**

此变更涉及应用适配。

变更前：内存较大时，相邻的两列数据中间无空格

```
1. hidumper --mem `pidof render_service_`
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/k6kprOTVTGqiE0pZcGaqlQ/zh-cn_image_0000002334331997.png?HW-CC-KV=V1&HW-CC-Date=20260427T233543Z&HW-CC-Expire=86400&HW-CC-Sign=653ADD2EA3157B06E4F784003816A587D6FC59F0FB2FCACE0672E8D5EF4AA69D)

变更后：每一列数据后新增一个空格

```
1. hidumper --mem `pidof render_service_`
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/5slBazDaToiOrlwBnnA4Iw/zh-cn_image_0000002334372173.png?HW-CC-KV=V1&HW-CC-Date=20260427T233543Z&HW-CC-Expire=86400&HW-CC-Sign=2399E06E93E86484576A9D4FF111341D07CC02129DA87E5380FB409BCA66E739)

其中hidumper、hidumper --mem、hidumper -c [system]变更效果与hidumper --mem [pid]命令效果一致。

**变更的接口/组件**

hidumper组件

**适配指导**

根据格式变更后进行调整适配

### 安装的应用是已卸载的预置应用时校验签名是否一致

**变更原因**

预置应用被卸载后可以安装一个bundleName相同、签名不同的hap仿冒，有安全风险。

**变更影响**

此变更涉及应用适配。

变更前：预置应用被卸载后安装一个bundleName相同、签名不同的hap会安装成功。

变更后：预置应用被卸载后安装一个bundleName相同、签名不同的hap会安装失败。

**起始API Level**

7

**变更的接口/组件**

[bm工具](../harmonyos-guides/bm-tool.md#安装命令install)安装命令。

**适配指导**

预置应用使用hdc命令安装时，安装hap的签名应该与预置hap的签名一致。
