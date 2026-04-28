---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-for-all-apps-b035
title: 针对所有应用的变更
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > 接口行为变更说明 > HarmonyOS NEXT Developer Beta3引入的接口行为变更 > 针对所有应用的变更
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:12+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:ee6f479226c8f113a08a30093819e947d416496e0513838eebc48a593fa785f0
---

## Ability Kit

### 入口图标和入口标签规格变动

**变更原因**

[入口图标和名称](../harmonyos-guides/module-configuration-file.md#配置文件标签)（module.json5中abilities配置的icon和label）是应用安装后在桌面上展示的图标和名称，[应用图标和名称](../harmonyos-guides/app-configuration-file.md#配置文件标签)（app.json5中配置的icon和label）是应用安装后在设置的应用列表或者消息通知栏等标识应用处展示的图标和名称。

应用同时配置了应用图标、应用名称和入口图标和入口名称，会导致在桌面和设置中显示的图标和名称存在不同。同一个应用在设备不同地方展示的图标和名称应该保持一致，避免出现恶意应用配置不同的图标。

**变更影响**

当应用存在入口UIAbility且配置了入口图标和入口标签则优先展示，如果不存在入口图标和入口标签，则展示应用图标和应用标签。

变更前

| 展示位置 | 取值 | 说明 |
| --- | --- | --- |
| 桌面展示图标和名称 | 入口图标和名称 | 当应用不存在入口UIAbility时会返回应用图标和名称 |
| 设置中应用列表展示图标和名称 | 应用图标和名称 | 必选字段，创建新工程时会有默认的图标和名称 |

变更后

| 展示位置 | 取值 | 说明 |
| --- | --- | --- |
| 桌面展示图标和名称 | 入口图标和名称 | 当应用不存在入口UIAbility时会返回应用图标和名称 |
| 设置中应用列表展示图标和名称 | 入口图标和名称 | 当应用存在入口UIAbility且配置了图标和名称后，优先返回入口图标和名称；如果不存在入口UIAbility或者没有配置入口图标和名称时，返回应用图标和名称。当存在多个入口UIAbility时，优先返回entry类型HAP的mainElement对应的UIAbility中配置的图标和名称。 |

**起始API Level**

不涉及接口

**变更的接口/组件**

bundleManager模块提供的查询接口返回的icon和label会按照优先级返回。

**适配指导**

建议开发者将应用图标和应用名称、入口图标和入口名称保持一致。

## ArkTS

### TextEncoder.encodeInto()接口变更

**变更原因**

TextEncoder.encodeInto编码字符串，当字符串中每多一个'\0'字符，返回的数组长度会增加2，长度异常。

**变更影响**

此变更涉及应用适配。

```
1. const arr = encoder.encodeInto('\0ab');
2. arr.length;
```

变更前：arr = [0x00, 0x61, 0x62, 0x00], arr.length 为4

变更后：arr = [0x00, 0x61, 0x62], arr.length 为3

**起始API Level**

9

**变更的接口/组件**

TextEncoder.encodeInto

**适配指导**

针对TextEncoder.encodeInto编码字符串时，注意返回的数组长度。

**变更的接口/组件**

| 类名 | 接口 | 变更 |
| --- | --- | --- |
| util.Base64Helper | encodeToStringSync(src: Uint8Array, options?: Type): string; | 参数异常由undefined变更为401。 |
| util.Base64Helper | encode(src: Uint8Array, options?: Type): Promise<Uint8Array>; | 参数异常由undefined变更为401。 |
| util.Base64Helper | encodeSync(src: Uint8Array, options?: Type): Uint8Array; | 参数异常由undefined变更为401。 |
| util.Base64Helper | encodeToString(src: Uint8Array, options?: Type): Promise<string>; | 参数异常由undefined变更为401。 |
| util.Base64Helper | decode(src: Uint8Array | string, options?: Type): Promise<Uint8Array>; | 参数异常由undefined变更为401。 |
| util.StringDecoder | constructor(encoding?: string); | 参数异常由undefined变更为401。 |
| util.StringDecoder | write(chunk: string | Uint8Array): string; | 参数异常由undefined变更为401。 |
| util.StringDecoder | end(chunk?: string | Uint8Array): string; | 参数异常由undefined变更为401。 |

**适配指导**

基于以上变更错误码的接口，开发者若存在对相关接口参数异常的错误码判断为undefined的情况，需要整改为判断401。

## ArkUI

### Search/TextInput/TextArea onchange回调新增可选参数预上屏文本

**变更原因**

在输入过程中，新增预上屏行为，需要将当前已提交上屏的文本和预上屏信息实时返回给开发者。

**变更影响**

此变更涉及应用适配。

变更前：

1.onChange回调在用户全部输入完成，提交正式上屏时触发。

2.onChange唯一参数是已正式提交上屏的文本。

变更后：

1.onChange回调在用户输入过程中，随预上屏内容变更触发。

2.onChange首个参数仍是已正式提交上屏的文本。新增可选参数PreviewText，PreviewText包含预上屏内容的起始位置和文本。

**起始API Level**

7

**变更的接口/组件**

Search/TextInput/TextArea组件的onChange回调事件参数。

**适配指导**

适配前：

默认开启预上屏功能。回调唯一参数为已正式上屏文本；回调时机为输入过程中，每一次预上屏内容变更时触发。

```
1. @Entry
2. @Component
3. struct SearchExample {
4. @State text: string = 'Search支持文本预上屏前...'

6. build() {
7. Column() {
8. Search({
9. value: this.text,
10. placeholder: 'input your word...',
11. })
12. .placeholderFont({ size: 16, weight: 400 })
13. .width(336)
14. .height(56)
15. // onChange回调唯一参数为已正式上屏文本；回调时机为输入过程中，每一次预上屏内容变更时触发
16. .onChange((value: string) => {
17. this.text = value
18. console.log("===get onchange ===")
19. console.log("body text value = " + value)
20. })
21. }
22. .width("90%")
23. .margin("5%")
24. }
25. }
```

适配后：

默认开启预上屏功能，需要适配在输入过程中，回调返回的首个参数为空字符串或者多次回调的首个参数为重复内容的场景；需要适配文本框内所有文本长度变更为含预上屏内容的总长度。

示例代码列举了预上屏状态下，用来适配各问题场景所需要的信息。

```
1. @Entry
2. @Component
3. struct SearchExample {
4. @State text: string = 'Search回调预上屏信息...'

6. build() {
7. Column() {
8. Search({
9. value: this.text,
10. placeholder: 'input your word...',
11. })
12. .placeholderFont({ size: 16, weight: 400 })
13. .width(336)
14. .height(56)
15. // onChange回调首个参数为已经存在的正式上屏文本
16. // 第二个参数为可选参数，返回的是预上屏内容的信息
17. .onChange((value: string, previewText: PreviewText) => {
18. this.text = value
19. console.log("===get onchange and get previewText info===")
20. let bodyTextValue = value
21. console.log("body text value = " + bodyTextValue)
22. let previewTextValue = previewText.value
23. console.log("previewText value = " + previewTextValue)
24. let previewTextStart = previewText.offset
25. let previewTextEnd = previewText.offset + previewTextValue.length
26. console.log("previewText index range in [ " + previewTextStart + ", " + previewTextEnd + " ]")
27. let isPreviewTextWorking = previewTextValue != "";
28. console.log("now is inputing at previewText working= " + isPreviewTextWorking)
29. let wholeTextValue = value + previewTextValue
30. console.log("whole text value = " + wholeTextValue)
31. })
32. }
33. .width("90%")
34. .margin("5%")
35. }
36. }
```

在不需要预上屏功能场景时，可使用enablePreviewText属性关闭预上屏功能。

```
1. @Entry
2. @Component
3. struct SearchExample {
4. @State text: string = 'Search支持关闭文本预上屏...'

6. build() {
7. Column() {
8. Search({
9. value: this.text,
10. placeholder: 'input your word...',
11. })
12. .placeholderFont({ size: 16, weight: 400 })
13. .width(336)
14. .height(56)
15. .enablePreviewText(false) // 使用该属性，可以关闭预上屏功能，使回调内容与回调时机与变更前保持一致
16. .onChange((value: string) => {
17. this.text = value
18. console.log("===get onchange ===")
19. console.log("body text value = " + value)
20. })
21. }
22. .width("90%")
23. .margin("5%")
24. }
25. }
```

## Localization Kit

### 资源匹配逻辑变更

**变更原因**

插入SIM卡时未能获取到正确的mcc目录资源，影响开发者差异化定制资源。

**变更影响**

此变更涉及应用适配。

变更前：应用配置了mcc目录等差异化资源，插sim卡显示的是默认语言目录下资源，未插sim卡显示的是mcc目录下资源。

如：插卡时会显示“Wi-Fi”字串，不插卡时会显示“WLAN”字串。

变更后：插sim卡显示的是mcc目录下资源，未插sim卡显示的是默认语言目录下资源。

如：插卡时会显示“WLAN”字串，不插卡时会显示“Wi-Fi”字串。

**起始API Level**

9

**变更的接口/组件**

SystemCapability.Global.ResourceManager获取资源相关接口。

相关接口查看[接口文档](../harmonyos-references-V5/js-apis-resource-manager-V5.md)

### raw\_file模块头文件变更

**变更原因**

raw\_file模块引用了string头文件，string头文件是C++标准库文件，导致raw\_file模块在C语言环境下无法使用。

**变更影响**

此变更涉及应用适配

变更前：

C++编译环境下开发者使用了raw\_file.h头文件，但开发者没有引用string头文件，调用了"std::string"等string库函数，可以编译成功。

```
1. #include <rawfile/raw_file_manager.h>
2. #include <rawfile/raw_file.h>

4. static napi_value GetRawFileContent(napi_env env, napi_callback_info info) {
5. size_t argc = 2;
6. napi_value argv[2] = {NULL};
7. napi_get_cb_info(env, info, &argc, argv, NULL, NULL);
8. napi_valuetype valueType;
9. napi_typeof(env, argv[0], &valueType);
10. NativeResourceManager *mNativeResMgr = OH_ResourceManager_InitNativeResourceManager(env, argv[0]);
11. size_t strSize;
12. char strBuf[256];
13. napi_get_value_string_utf8(env, argv[1], strBuf, sizeof(strBuf), &strSize);
14. std::string filename(strBuf, strSize);   // 编译通过
15. RawFile *rawFile = OH_ResourceManager_OpenRawFile(mNativeResMgr, filename.c_str());
16. }
```

变更后：

C++编译环境下开发者使用了raw\_file.h头文件，但开发者没有引用string头文件，调用了"std::string"等string库函数，会编译失败。

```
1. #include <rawfile/raw_file_manager.h>
2. #include <rawfile/raw_file.h>

4. static napi_value GetRawFileContent(napi_env env, napi_callback_info info) {
5. size_t argc = 2;
6. napi_value argv[2] = {NULL};
7. napi_get_cb_info(env, info, &argc, argv, NULL, NULL);
8. napi_valuetype valueType;
9. napi_typeof(env, argv[0], &valueType);
10. NativeResourceManager *mNativeResMgr = OH_ResourceManager_InitNativeResourceManager(env, argv[0]);
11. size_t strSize;
12. char strBuf[256];
13. napi_get_value_string_utf8(env, argv[1], strBuf, sizeof(strBuf), &strSize);
14. std::string filename(strBuf, strSize);   // 编译失败
15. RawFile *rawFile = OH_ResourceManager_OpenRawFile(mNativeResMgr, filename.c_str());
16. }
```

**起始API Level**

8

**变更的接口/组件**

| 变更前 | 变更后 |
| --- | --- |
| #include <string> | #include <stddef.h>  #include <stdint.h>  #include <stdbool.h> |

**适配指导**

C++编译环境下开发者使用raw\_file.h头文件，但开发者没有引用string头文件，调用了"std::string"等string库函数，需要进行适配，通过include引入string头文件即可解决。

```
1. #include <rawfile/raw_file_manager.h>
2. #include <rawfile/raw_file.h>
3. #include <string>           // 手动引用string头文件

5. static napi_value GetRawFileContent(napi_env env, napi_callback_info info) {
6. size_t argc = 2;
7. napi_value argv[2] = {NULL};
8. napi_get_cb_info(env, info, &argc, argv, NULL, NULL);
9. napi_valuetype valueType;
10. napi_typeof(env, argv[0], &valueType);
11. NativeResourceManager *mNativeResMgr = OH_ResourceManager_InitNativeResourceManager(env, argv[0]);
12. size_t strSize;
13. char strBuf[256];
14. napi_get_value_string_utf8(env, argv[1], strBuf, sizeof(strBuf), &strSize);
15. std::string filename(strBuf, strSize);   // 编译通过
16. RawFile *rawFile = OH_ResourceManager_OpenRawFile(mNativeResMgr, filename.c_str());
17. }
```

## Network Kit

### webSocket.connect接口新增2302998错误码

**变更原因**

为规范元服务请求域名范围，提升元服务上架审核效率和平台合规经营安全性，当用户使用元服务时，将根据该元服务的域名配置进行域名访问；若是访问未配置域名，则connect接口会返回该错误码。

**变更影响**

此变更涉及应用适配。

API version 11及以下元服务应用访问未配置域名，connect接口不会有任何影响。

API version 12开始，元服务应用访问未配置域名，connect接口抛出该错误码，详情见[接口文档](../harmonyos-references-V5/js-apis-websocket-V5.md)。

**起始API Level**

6

**变更的接口/组件**

@ohos.net.webSocket

**适配指导**

开发者在进行元服务应用开发时，涉及webSocket.connect接口建立连接是，先到[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)

完成服务器域名相关配置，可参考此[指导文档](../atomic-guides-V5/agc-help-harmonyos-server-domain-V5.md)

进行配置。

开发者在进行元服务应用开发时，若遇到webSocket.connect接口失败，请用catch捕获错误；若webSocket.connect接口失败错误码是2302998，可以到[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)完成服务器域名相关配置，可参考此[指导文档](../atomic-guides-V5/agc-help-harmonyos-server-domain-V5.md)
