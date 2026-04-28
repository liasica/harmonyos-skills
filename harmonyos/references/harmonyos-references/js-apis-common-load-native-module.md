---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-common-load-native-module
title: loadNativeModule (同步动态加载系统库接口)
breadcrumb: API参考 > 公共基础能力 > ArkTS API > loadNativeModule (同步动态加载系统库接口)
category: harmonyos-references
scraped_at: 2026-04-28T08:19:17+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:7d1822f1ea7b3ecaa2a1cb420d00fce89dfae15b402aebac3cb7444540d2c7b4
---

本模块提供了同步动态加载系统库接口的能力。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## loadNativeModule

PhonePC/2in1TabletTVWearable

loadNativeModule(moduleName: string): Object

loadNativeModule接口用于同步动态加载native模块，目的是按需加载所需要的模块。使用该接口会增加加载so文件的时间，开发者需评估其对功能的影响。

说明

loadNativeModule加载的模块名指的是依赖方oh-package.json5文件的dependencies字段内的名称。

loadNativeModule接口仅支持在UI主线程中加载native模块。

该接口在使用常量字符串或变量表达式作为参数时，都需要配置依赖。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleName | string | 是 | 加载的模块名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | native模块的默认导出。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 10200301 | Loading native module failed. |

**loadNativeModule支持的场景**

| 场景 | 示例 |
| --- | --- |
| 系统库模块 | 加载@ohos.或@system. |
| 应用内native模块 | 加载libNativeLibrary.so |

**示例1**：HAP加载系统库模块

```
1. let hilog: ESObject = loadNativeModule("@ohos.hilog");
2. hilog.info(0, "testTag", "loadNativeModule ohos.hilog success");
```

**示例2**：HAP加载Native库

libentry.so的index.d.ts文件内容如下：

```
1. //index.d.ts
2. export const add: (a: number, b: number) => number;
```

1.在加载本地so库时，配置模块级oh-package.json5文件的dependencies项。配置说明见[模块级oh-package.json5](../harmonyos-guides/ide-oh-package-json5.md#zh-cn_topic_0000001792256137_oh-packagejson5-字段说明)。

```
1. {
2. "dependencies": {
3. "libentry.so": "file:./src/main/cpp/types/libentry"
4. }
5. }
```

2.在模块级build-profile.json5中进行配置。配置说明见[模块级build-profile.json5文件](../harmonyos-guides/ide-hvigor-build-profile.md)。

```
1. {
2. "buildOption": {
3. "arkOptions": {
4. "runtimeOnly": {
5. "packages": [
6. "libentry.so"
7. ]
8. }
9. }
10. }
11. }
```

3.使用loadNativeModule加载libentry.so，调用add函数。

```
1. let module: ESObject = loadNativeModule("libentry.so");
2. let sum: number = module.add(1, 2);
```
