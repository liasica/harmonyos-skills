---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/js-apis-load-native-module
title: 同步方式动态加载Native模块
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS运行时 > ArkTS模块化 > 同步方式动态加载Native模块
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:63aff8ceaf8a290c7a5b1cd7aca70cb0a1e2a6400e64b7edc829411021585482
---

[loadNativeModule (同步动态加载系统库接口)](../harmonyos-references/js-apis-common-load-native-module.md)用于同步动态加载Native模块，目的是按需加载所需要的模块。

## 函数说明

```js
loadNativeModule(moduleName: string): Object;
```

| 参数 | 说明 |
| --- | --- |
| moduleName | 加载的模块名。 |

## loadNativeModule支持的场景

| 场景 | 示例 |
| --- | --- |
| 系统库模块 | 加载@ohos.或@system. |
| 应用内Native模块 | 加载libNativeLibrary.so |

## 使用注意事项

* loadNativeModule仅支持在Stage模型的UI主线程中加载native模块。
* 使用该接口会增加so文件的加载时间，使用前需评估其对应用性能和功能的影响。
* 无论moduleName参数使用常量字符串还是变量表达式，都需要在依赖方模块级oh-package.json5文件的dependencies字段中配置依赖。moduleName的值为dependencies字段中声明的依赖名称。
* 加载应用内native模块时，还需要在依赖方模块级build-profile.json5文件的buildOption.arkOptions.runtimeOnly.packages字段中配置模块名称。该名称需与oh-package.json5文件中的依赖名称及loadNativeModule的入参保持一致。
* 接口声明的返回值类型为Object。调用时需使用ESObject类型的变量接收返回值，才能调用native模块导出的方法；使用Object类型接收返回值时，调用其中的方法可能会产生编译错误。

以加载libentry.so为例，需要完成以下配置。

1. 在模块级oh-package.json5文件中配置dependencies字段。

   ```json5
   "dependencies": {
     "libentry.so": "file:./src/main/cpp/types/libentry"
   },
   ```
2. 在模块级build-profile.json5文件中配置runtimeOnly.packages字段。

   ```json5
   "buildOption": {
     "arkOptions": {
       "runtimeOnly": {
         "packages": [
           "libentry.so"
         ]
       }
     },
     // ...
   },
   ```

## 使用示例

**示例1**：HAP加载系统库模块

```typescript
// HAP加载系统库模块
let hilog: ESObject = loadNativeModule('@ohos.hilog');
hilog.info(0, 'testTag', 'loadNativeModule ohos.hilog success');
```

**示例2**：HAP加载Native库

libentry.so的index.d.ts文件如下：

```typescript
export const add: (a: number, b: number) => number;
```

完成[使用注意事项](js-apis-load-native-module.md#使用注意事项)中的依赖配置后，使用loadNativeModule加载libentry.so并调用add函数。

```typescript
//HAP加载Native库
let module: ESObject = loadNativeModule('libentry.so');
let sum: number = module.add(1, 2);
```
