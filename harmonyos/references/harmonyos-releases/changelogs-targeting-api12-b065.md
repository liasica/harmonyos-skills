---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-targeting-api12-b065
title: 针对API 12应用的变更
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > 接口行为变更说明 > HarmonyOS NEXT Beta引入的接口行为变更 > 针对API 12应用的变更
category: harmonyos-releases
scraped_at: 2026-04-29T13:24:09+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:67bdb6154bbf4f18ad73f8ea60431be87dec178f6c3670da4c54502a5fb52b78
---

## Ability

### 禁止BackupExtensionAbility进程拉起启动框架

**变更原因**

BackupExtensionAbility进程用于数据迁移服务，进行数据迁移时，应用还未启动，此时拉起启动框架会影响数据迁移的正常执行。

说明

该变更在9月21日发布的patch版本引入，对应开发工具DevEco Studio版本为5.0.3.810。

**变更影响**

此变更涉及应用适配。

变更前：BackupExtensionAbility进程可以拉起启动框架并执行启动任务。

变更后：BackupExtensionAbility进程无法拉起启动框架。

**起始API Level**

12

**变更的接口/组件**

AppStartup启动框架模块默认行为

**适配指导**

默认行为变更，应注意变更后的行为是否对整体应用逻辑产生影响。

## ArkTS

### StringDecoder中特定场景下解码错误数据行为变更

**变更原因**

StringDecoder对于入参Uint8Array中存在元素0的情况，无法解码出Uint8Array中元素0后数据，在元素0位置截断，导致获取不到完整的解码数据。

**变更影响**

该变更属于问题修复。

变更前：

对于存在元素0的Uint8Array对象进行编码时，数据不完整。对解码出的值进行编码时，无法正常恢复为原始Uint8Array。

变更后：

对存在元素0的Uint8Array对象，正确进行解码，解码数据完整。

**起始API Level**

12

**变更的接口/组件**

util.StringDecoder模块下的两个接口：

write(chunk: string | Uint8Array): string;

end(chunk?: string | Uint8Array): string;

**适配指导**

变更描述：Uint8Array中存在元素0的情况，无需适配，属于问题修复。

```
1. import { util } from '@kit.ArkTS';

3. let decoder = new util.StringDecoder('utf-8');
4. // 0xE4, 0xBD, 0xA0 解码结果：你
5. // 0                解码结果：\u0000(不可见字符，占一个长度)
6. // 0xE5, 0xA5, 0xBD 解码结果：好
7. let input = new Uint8Array([0xE4, 0xBD, 0xA0, 0, 0xE5, 0xA5, 0xBD]);
8. const decoded = decoder.write(input);
9. const decodedend = decoder.end(input);

11. // 变更前:
12. // console.info("decoded:", decoded);// 你
13. // console.info("decoded.length:", decoded.length);// 1
14. // console.info("decodedend:", decodedend);// 你
15. // console.info("decodedend.length:", decodedend.length);// 1

17. // 变更后：
18. console.info("decoded:", decoded);// 你好
19. console.info("decoded.length:", decoded.length);// 3
20. console.info("decodedend:", decodedend);// 你好
21. console.info("decodedend.length:", decodedend.length);// 3
```

## ArkUI

### 状态管理V2版本组件内的@Local,@Param,@Event,@Provider,@Consumer,@BuilderParam,必须声明类型

**变更原因**

V2组件内的@Local,@Param,@Event,@Provider,@Consumer,@BuilderParam装饰器不需要写类型就可以编译成功，而装饰器是有类型限制的，所以这些装饰器需要加上类型校验。

**变更影响**

此变更涉及应用适配。

变更前：V2组件内的@Local,@Param,@Event,@Provider,@Consumer,@BuilderParam修饰的变量没有写类型编译不会报错。

变更后：V2组件内的@Local,@Param,@Event,@Provider,@Consumer,@BuilderParam修饰的变量没有写类型编译报错。

**起始API Level**

12

**变更的接口/组件**

无。

**适配指导**

在V2组件内，每一个被@Local,@Param,@Event,@Provider,@Consumer,@BuilderParam修饰的变量加上类型声明。

```
1. @Builder
2. function testBuilder() {

4. }

6. @Entry
7. @ComponentV2
8. struct V2ComponentMember {
9. @Local localValue: string = 'localValue';
10. @BuilderParam builderParamValue: () => void = testBuilder;
11. @Param paramValue: string = 'paramValue';
12. @Event eventValue: string = 'eventValue';
13. @Provider() providerValue: string = 'providerValue';
14. @Consumer() consumerValue: string = 'consumerValue';
15. build() {

17. }
18. }
```

### 修复C-API场景下NODE\_TIME\_PICKER\_DISAPPEAR\_TEXT\_STYLE的get接口的错误行为

**变更原因**

该接口用于C API中TimePicker组件设置或者获取待消失字体样式。

该变更修复了此处返回值的实现错误。

**变更影响**

此变更涉及应用适配。

变更前：通过该接口返回的值指向的是组件的普通字体样式。

变更后：通过该接口返回的值指向的是组件正确的待消失行字体的样式。

**起始API Level**

12

**变更的接口/组件**

C-API NODE\_TIME\_PICKER\_DISAPPEAR\_TEXT\_STYLE的get接口。

**适配指导**

原先使用该接口的场景，如要保持原效果不变，换用NODE\_TIME\_PICKER\_TEXT\_STYLE接口即可。

即将原先使用 nodeApi->getAttribute(node, NODE\_TIME\_PICKER\_DISAPPEAR\_TEXT\_STYLE) 变更为

nodeApi->getAttribute(node, NODE\_TIME\_PICKER\_TEXT\_STYLE)

### component3d获取资源的路径格式由Resource类型变更到ResourceStr类型

**变更原因**

扩展component3D组件获取系统路径资源能力，目前只支持从应用沙箱路径获取资源。

**变更影响**

此变更涉及应用适配。

变更前：component3D资源获取通过Resource方式，只支持从rawfile路径读取。

变更后：component3D资源获取修改为通过ResourceStr方式，既支持从rawfile路径读取也支持从磁盘路径读取。

涉及场景：

当用户存在指定数据类型赋值场景时，会出现上述情况; 例如：

```
1. const params1: SceneResourceParameters = { name: "name1", uri: $rawfile("default_path") }
2. const test_uri: Resource | undefined = params1.uri;
```

**起始API Level**

12

**变更的接口/组件**

1、 Component3D初始化资源接口SceneOptions中sence变量数据类型由Resource变更为ResourceStr；

2、 Scene中uri变量数据类型由Resource变更为ResourceStr；

3、 SceneResources中uri变量数据类型由Resource变更为ResourceStr；

4、 component3d中environment、customRender、shader和shaderImageTexture接口的入参由Resource类型变更为ResourceStr类型；

5、 Scene中load接口的入参由Resource类型变更为ResourceStr类型；

**适配指导**

```
1. import { Scene, Image, SceneResourceParameters, SceneResourceFactory } from '@kit.ArkGraphics3D'

3. const params1: SceneResourceParameters = { name: "name1", uri: $rawfile("default_path") }
4. // 变更前
5. // const test_uri: Resource | undefined = params1.uri;
6. // 变更后适配为
7. const test_uri: ResourceStr | undefined = params1.uri;

9. @Entry
10. @Component
11. struct node_geometry {
12. scene: Scene | null = null;
13. @State sceneOpt: SceneOptions | null = null;
14. envImg: Image | null = null;

16. onPageShow(): void {
17. this.Init();
18. }

20. onPageHide(): void {
21. if (this.scene) {
22. this.scene.destroy();
23. }
24. }

26. Init(): void {
27. if (this.scene == null) {
28. Scene.load($rawfile("default_path"))
29. .then(async (result: Scene) => {
30. this.scene = result;
31. this.sceneOpt = { scene: this.scene, modelType: ModelType.SURFACE } as SceneOptions;
32. let rf: SceneResourceFactory = this.scene.getResourceFactory();

34. this.envImg = await rf.createImage({ name: "image1", uri: test_uri });
35. });
36. }
37. }

39. build() {
40. Column() {
41. Component3D(this.sceneOpt)
42. .renderWidth('100%')
43. .renderHeight('100%')
44. .width('100%')
45. .height('100%')
46. }
47. }
48. }
```

## ArkWeb

### CustomDialog内嵌Web组件软键盘避让方式由改变Web高度避让软键盘变更为抬升CustomDialog避让软键盘

**变更原因**

CustomDialog内嵌Web组件软键盘避让方式不符合CustomDialog软键盘避让的规范，与其他ArkUI组件避让方式不一致。

**变更影响**

此变更涉及应用适配。

变更前：CustomDialog内嵌Web组件，在Web组件内点击输入框弹出软键盘时，会默认通过改变Web的高度来避让软键盘。

变更后：CustomDialog内嵌Web组件，在Web组件内点击输入框弹出软键盘时，会默认通过抬升CustomDialog来避让软键盘。

下表为变更前后CustomDialog嵌套Web场景软键盘避让效果对比：

| 变更前 | 变更后 |
| --- | --- |
|  |  |

**起始API Level**

12

**变更的接口/组件**

CustomDialog内嵌Web组件软键盘避让场景。

**适配指导**

[CustomDialog](../harmonyos-references-V5/ts-methods-custom-dialog-box-V5.md)弹窗避让软键盘时，会将弹窗整个抬升，并且与软键盘之间存在一定的安全间距。如果应用不期望弹窗被抬升或存在安全间距，应当合理配置[CustomDialog](../harmonyos-references-V5/ts-methods-custom-dialog-box-V5.md)的属性或改用其他组件替代。

## Crypto Architecture Kit

### 通用密钥库SystemCapability变更

**变更原因**

通用密钥库为了满足未来mini平台算法能力扩展诉求，将加解密算法相关TAG的SystemCapability由SystemCapability.Security.Huks.Extension调整为SystemCapability.Security.Huks.Core。且由于mini平台算法能力较弱，部分算法当前返回不支持，待后续扩展。

说明

该变更在9月12日发布的patch版本引入，对应开发工具DevEco Studio版本为5.0.3.806。

**变更影响**

此变更涉及应用适配。

对接口所属的SystemCapability进行调整，对接口本身的使用方式无影响。

变更前：

相关接口的系统能力要求为“SystemCapability.Security.Huks.Extension”。判断设备是否支持本次变更涉及算法需使用canIUse("SystemCapability.Security.Huks.Extension")。

变更后：

相关接口的系统能力要求为“SystemCapability.Security.Huks.Core”。判断设备是否支持本次变更涉及算法需改为使用canIUse("SystemCapability.Security.Huks.Core")。

**起始API Level**

12

**变更的接口/组件**

@ohos.security.huks模块中的加解密算法相关接口。详细接口如下：

| 序号 | 接口名 | 接口说明 |
| --- | --- | --- |
| 1 | huks.importKeyItem | 导入明文密钥 |
| 2 | huks.importWrappedKeyItem | 导入加密密钥 |
| 3 | huks.exportKeyItem | 导出密钥 |
| 4 | huks.getKeyItemProperties | 获取密钥属性 |
| 5 | huks.deleteKey | 删除密钥 |

@ohos.security.huks模块中的相关枚举类型。详细如下：

| 序号 | 枚举名 | 枚举说明 |
| --- | --- | --- |
| 1 | HuksKeyPurpose | 表示密钥用途 |
| 2 | HuksKeyDigest | 表示摘要算法 |
| 3 | HuksKeyPadding | 表示补齐算法 |
| 4 | HuksCipherMode | 表示加密模式 |
| 5 | HuksKeySize | 表示密钥长度 |
| 6 | HuksKeyAlg | 表示密钥使用的算法 |
| 7 | HuksUnwrapSuite | 表示导入加密密钥的算法套件 |
| 8 | HuksKeyStorageType | 表示密钥存储方式 |
| 9 | HuksImportKeyType | 表示导入密钥的密钥类型 |
| 10 | HuksRsaPssSaltLenType | 表示Rsa在签名验签、padding为pss时需指定的salt\_len类型 |
| 11 | HuksAuthStorageLevel | 表示生成或导入密钥时，指定该密钥的存储安全等级 |
| 12 | HuksSendType | 表示发送Tag的方式 |
| 13 | HuksTagType | 表示Tag的数据类型 |

HuksTag中的枚举值。详细如下：

| 序号 | 枚举值 | 枚举值说明 |
| --- | --- | --- |
| 1 | HUKS\_TAG\_DIGEST | 表示摘要算法的Tag |
| 2 | HUKS\_TAG\_SALT | 表示密钥派生时的盐值 |
| 3 | HUKS\_TAG\_ITERATION | 表示密钥派生时的迭代次数 |
| 4 | HUKS\_TAG\_AGREE\_ALG | 表示密钥协商时的算法类型 |
| 5 | HUKS\_TAG\_AGREE\_PUBLIC\_KEY\_IS\_KEY\_ALIAS | 表示密钥协商时的公钥别名 |
| 6 | HUKS\_TAG\_AGREE\_PRIVATE\_KEY\_ALIAS | 表示密钥协商时的私钥别名 |
| 7 | HUKS\_TAG\_AGREE\_PUBLIC\_KEY | 表示密钥协商时的公钥 |
| 8 | HUKS\_TAG\_DERIVE\_KEY\_SIZE | 表示派生密钥的大小 |
| 9 | HUKS\_TAG\_IMPORT\_KEY\_TYPE | 表示导入的密钥类型 |
| 10 | HUKS\_TAG\_UNWRAP\_ALGORITHM\_SUITE | 表示导入加密密钥的套件 |
| 11 | HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG | 表示派生密钥/协商密钥的存储类型 |
| 12 | HUKS\_TAG\_RSA\_PSS\_SALT\_LEN\_TYPE | 表示rsa\_pss\_salt\_length的类型 |
| 13 | HUKS\_TAG\_ALL\_USERS | 预留 |
| 14 | HUKS\_TAG\_USER\_ID | 表示当前密钥属于哪个userID |
| 15 | HUKS\_TAG\_NO\_AUTH\_REQUIRED | 预留 |
| 16 | HUKS\_TAG\_IS\_ALLOWED\_WRAP | 预留 |
| 17 | HUKS\_TAG\_KEY\_WRAP\_TYPE | 预留 |
| 18 | HUKS\_TAG\_KEY\_ROLE | 预留 |
| 19 | HUKS\_TAG\_IS\_ASYNCHRONIZED | 预留 |
| 20 | HUKS\_TAG\_ASYMMETRIC\_PUBLIC\_KEY\_DATA | 预留 |
| 21 | HUKS\_TAG\_ASYMMETRIC\_PRIVATE\_KEY\_DATA | 预留 |

**适配指导**

SystemCapability.Security.Huks.Core为必选基础能力，SystemCapability.Security.Huks.Extension为可选扩展能力。当前SDK默认定义的device-define都包含SystemCapability.Security.Huks.Core必选能力，因此涉及Universal Keystore组件的功能代码原则上无需适配。但如果代码中涉及调用canIUse()方法对本次变更涉及算法支持情况进行判断，则应修改canIUse()方法传入的SystemCapability，同时参考资料，结合API level判断。

### @ohos.security.cryptoFramework 接口SysCap变更

**变更原因**

加解密算法库框架为了灵活适配不同平台，按照算法类型对接口重新划分SysCap。

说明

该变更在9月12日发布的patch版本引入，对应开发工具DevEco Studio版本为5.0.3.806。

**变更影响**

此变更涉及应用适配。

变更前：

加解密算法库框架所有接口的SysCap均是SystemCapability.Security.CryptoFramework。

（1）可以使用canIUse("SystemCapability.Security.CryptoFramework")判断设备是否支持加解密算法库能力。

（2）若自定义设备支持加解密算法库能力能力，只需在设备的能力集配置中配置SystemCapability.Security.CryptoFramework。

变更后：

加解密算法库框架按照算法类型对接口重新划分SysCap，如随机数相关接口SysCap变更为SystemCapability.Security.CryptoFramework.Rand。

（1）应该使用具体的Syscap判断设备的加解密算法库是否支持对应算法，如使用canIUse("SystemCapability.Security.CryptoFramework.Rand")判断设备的加解密算法库能力是否支持随机数能力。

（2）若自定义设备原本就支持加解密算法库能力，则需在设备的能力集配置中添加加解密算法库框架的所有SysCap，具体SysCap名见“变更的接口/组件”。

**起始API Level**

12

**变更的接口/组件**

@ohos.security.cryptoFramework按照算法类型对接口重新划分SysCap，具体划分如下，其中序号为2到11的10个SysCap是新增的：

| 序号 | SysCap名 | SysCap描述 |
| --- | --- | --- |
| 1 | SystemCapability.Security.CryptoFramework | 原有的SysCap，变更后不包含任何算法能力，仅包含公共能力 |
| 2 | SystemCapability.Security.CryptoFramework.Key | 密钥基础类型 |
| 3 | SystemCapability.Security.CryptoFramework.Key.SymKey | 对称密钥 |
| 4 | SystemCapability.Security.CryptoFramework.Key.AsymKey | 非对称密钥 |
| 5 | SystemCapability.Security.CryptoFramework.Signature | 签名验签 |
| 6 | SystemCapability.Security.CryptoFramework.Cipher | 对称、非对称加解密 |
| 7 | SystemCapability.Security.CryptoFramework.KeyAgreement | 密钥协商 |
| 8 | SystemCapability.Security.CryptoFramework.MessageDigest | 消息摘要 |
| 9 | SystemCapability.Security.CryptoFramework.Mac | 消息验证码 |
| 10 | SystemCapability.Security.CryptoFramework.Kdf | 密钥派生 |
| 11 | SystemCapability.Security.CryptoFramework.Rand | 随机数 |

**适配指导**

（1）判断设备是否支持加解密算法库框架的随机数能力需使用canIUse("SystemCapability.Security.CryptoFramework.Rand")，其他算法类型类似。

（2）若自定义设备的能力集配置文件中包含了SystemCapability.Security.CryptoFramework，则需要添加此次变更新增的10个SysCap。

## IME Kit

### 系统增加对基础访问模式输入法的管控

**变更原因**

为保护用户个人数据安全，系统增加对基础模式输入法的安全管控，用于提升输入法的安全性。

**变更影响**

此变更涉及应用适配。

新增的系统管控可能会导致输入法应用原先在基础模式下使用的部分功能出现不可用的情况。

当输入法以安全模式[SecurityMode](../harmonyos-references-V5/js-apis-inputmethodengine-V5.md#securitymode11)为基础访问模式（即BASIC）运行，系统增加了对其功能的管控。主要体现为：系统禁止基础模式下的输入法调用，涉及访问或泄漏用户隐私数据的系统能力。

变更前：

1. 输入法Extension进程与应用的主入口的进程共用同一个应用沙箱，两个进程对该沙箱均可读可写。
2. 输入法Extension进程可以拉起其他Extension应用或其他应用的UIAbility。
3. 输入法Extension进程可以使用涉及访问或泄漏用户个人数据的接口，可以将数据传出进程。

变更后：

1. 输入法Extension进程使用独立沙箱，与应用的主入口进程不可互相访问对方独立沙箱。
2. 新增输入法Extension与应用的主入口的共享沙箱，基础访问模式下输入法Extension对共享沙箱只读，完整访问模式下可读可写；应用的主入口对共享沙箱保持可读可写。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/Si1lYA2lRH6RcP4NNKMS4w/zh-cn_image_0000002117367217.png?HW-CC-KV=V1&HW-CC-Date=20260429T052408Z&HW-CC-Expire=86400&HW-CC-Sign=ABEE48BC6F8234AAA2BB1B9326A5F4797FCBD901C4255FE19B79D64E2BE1275F)
3. 基础访问模式下，输入法应用Extension进程无法拉起其他Extension应用进程以及其他UIAbility。
4. 基础访问模式下，输入法Extension进程会受到系统管控，不能使用涉及访问或泄漏用户个人数据的各种接口，同时无法将数据传递出进程。管控功能包括但不限于：网络、短信、电话、麦克风、定位、相机、蓝牙、壁纸、支付、日历、游戏、扬声器、Wi-Fi、剪切板、多媒体、联系人、公共事件、系统账号、健康数据、地图服务、推送服务、融合搜索、共享内存、分布式特性、广告设备标识等。
5. 基础访问模式下，输入法Extension可以使用基础输入功能相关的必要系统能力，例如，IME Kit、ArkUI、窗口、图形、屏幕管理等。

**起始API Level**

12

**变更的接口/组件**

不涉及

**适配指导**

为确保输入法应用在运行期间功能正常，建议输入法应用在应用初始化流程：[onCreate](../harmonyos-references-V5/js-apis-inputmethod-extension-ability-V5.md#inputmethodextensionabilityoncreate)回调中，通过调用接口[getSecurityMode](../harmonyos-references-V5/js-apis-inputmethodengine-V5.md#getsecuritymode11)查询当前模式：

1. 若当前处于基础模式，开发者可以调整内部功能呈现情况，防止出现功能不可用。
2. 若当前处于完整模式，开发者可以使用涉及访问用户数据的接口，但是，对于这些接口的访问仅限于提升输入法体验。

为保证输入法功能稳定，请开发者确保在基础模式下仅使用与基础输入功能相关的能力，不能试图通过绕过系统机制将数据传递到输入法Extension进程和沙箱外。
