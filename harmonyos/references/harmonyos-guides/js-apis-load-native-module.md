---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/js-apis-load-native-module
title: 同步方式动态加载Native模块
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS运行时 > ArkTS模块化 > 同步方式动态加载Native模块
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:44+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b0a0bf970e9578244a79b2244ea3b483ffda8c1970a073f2ea581950e4bac199
---

[loadNativeModule接口](../harmonyos-references/js-apis-common-load-native-module.md)用于同步动态加载Native模块，目的是按需加载所需要的模块。使用该接口会增加加载so文件的时间，开发者需评估其对功能的影响。

## 函数说明

```
1. loadNativeModule(moduleName: string): Object;
```

| 参数 | 说明 |
| --- | --- |
| moduleName | 加载的模块名。 |

说明

loadNativeModule加载的模块名是指依赖方oh-package.json5文件的dependencies中的名字。

loadNativeModule必须在UI主线程中调用。

该接口在加载常量字符串或变量表达式作为参数时，需要配置依赖。

## loadNativeModule支持的场景

| 场景 | 示例 |
| --- | --- |
| 系统库模块 | 加载@ohos.或@system. |
| 应用内Native模块 | 加载libNativeLibrary.so |

## 使用示例

* **HAP加载系统库模块**

```
1. let hilog: ESObject = loadNativeModule("@ohos.hilog");
2. hilog.info(0, "testTag", "loadNativeModule ohos.hilog success");
```

* **HAP加载Native库**

libentry.so的index.d.ts文件如下：

```
1. //index.d.ts
2. export const add: (a: number, b: number) => number;
```

1.加载本地so库时，需要在oh-package.json5文件中配置dependencies项。

```
1. {
2. "dependencies": {
3. "libentry.so": "file:./src/main/cpp/types/libentry"
4. }
5. }
```

2.在build-profile.json5中进行配置。

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

3.使用loadNativeModule加载libentry.so，并调用add函数。

```
1. let module: ESObject = loadNativeModule("libentry.so");
2. let sum: number = module.add(1, 2);
```
