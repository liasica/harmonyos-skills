---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-coding-standard-ndk-arkts
title: NDK开发ArkTS侧编码规范
breadcrumb: 最佳实践 > 稳定性 > 稳定性优化 > 稳定性编码规范 > NDK开发ArkTS侧编码规范
category: best-practices
scraped_at: 2026-04-28T08:23:00+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:1b0956116e91603b17c3cbe98e56d235edd61f3fc4ea2835f2322e295dce8cf6
---

ArkTS通过引用编译好的so文件来调用native方法。为避免不规范引用导致的运行时异常和故障排查成本，开发者应按照本文的标准进行引用。

NDK工程创建步骤及目录结构可参考：[创建NDK工程](../harmonyos-guides/create-with-ndk.md)。

## import本模块的so

**配置依赖**：

模块根目录 > oh-package.json5

```
1. {
2. "name": "entry",
3. "version": "1.0.0",
4. "description": "Please describe the basic information.",
5. "main": "",
6. "author": "",
7. "license": "",
8. "dependencies": {
9. // 依赖的so
10. "libentry.so": "file:./src/main/cpp/types/libentry"
11. }
12. }
```

依赖文件中的so名称要与CMakeLists.txt文件中的模块名称一致。

模块根目录 > src > main > cpp > CMakeLists.txt

```
1. # the minimum version of CMake.
2. cmake_minimum_required(VERSION 3.4.1)
3. project(MyApplication14)
4. set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})
5. if(DEFINED PACKAGE_FIND_FILE)
6. include(${PACKAGE_FIND_FILE})
7. endif()
8. include_directories(${NATIVERENDER_ROOT_PATH}
9. ${NATIVERENDER_ROOT_PATH}/include)

11. # 声明一个产物libentry.so，SHARED表示产物为动态库，napi_init.cpp为产物的源代码
12. add_library(entry SHARED napi_init.cpp)

14. # 声明产物entry链接时需要的三方库libace_napi.z.so
15. target_link_libraries(entry PUBLIC libace_napi.z.so)
```

**引用native方法**：

引用的so文件名称必须与oh-package.json5中定义的一致。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. // Reference napi in dependent modules
3. import { testNapi } from 'library';

6. @Entry
7. @Component
8. struct Index {
9. @State message: string = 'Hello World';
10. build() {
11. Row() {
12. Column() {
13. Text(this.message)
14. .fontSize(50)
15. .fontWeight(FontWeight.Bold)
16. .onClick(() => {
17. // Call methods in Napi
18. hilog.info(0x0000, 'testTag', 'Test NAPI 2 + 3 = %{public}d', testNapi.add(1, 2));
19. })
20. }
21. .width('100%')
22. }
23. .height('100%')
24. }
25. }
```

[Index3.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/StabilityCodingSpecification/DevEcoStaticCheck/src/main/ets/pages/Index3.ets#L21-L45)

调用的方法名称必须与.d.ts文件中导出的方法名一致。

模块根目录 > src > main > cpp > types > libentry > index.d.ts

```
1. export const add: (a: number, b: number) => number;
```

[Index.d.ts](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/StabilityCodingSpecification/Ndk1/src/main/cpp/types/libndk1/Index.d.ts#L2-L2)

## import其它模块的so

开发者可以在har/hsp中编写公共的so，供其他模块调用。

### 引用方模块

**本地依赖**：

模块根目录 > oh-package.json5

```
1. {
2. "name": "entry",
3. "version": "1.0.0",
4. "description": "Please describe the basic information.",
5. "main": "",
6. "author": "",
7. "license": "",
8. "dependencies": {
9. // 依赖当前工程下的其它模块
10. "library": "file:../library"
11. }
12. }
```

**远程依赖**：

运行命令

```
1. ohpm install library --registry http://localhost:8088/repos/ohpm
```

工程根目录 > oh-package.json5 中会自动配置依赖。

```
1. {
2. "name": "depend_othermodule_so",
3. "version": "1.0.0",
4. "description": "Please describe the basic information.",
5. "main": "",
6. "author": "",
7. "license": "",
8. "dependencies": {
9. // 名称必须与远程模块名称相同
10. "library": "^2.0.0"
11. },
12. "devDependencies": {
13. "@ohos/hypium": "1.0.17",
14. "@ohos/hamock": "1.0.1-rc2"
15. }
16. }
```

**引用native方法**：

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. // Reference napi in dependent modules
3. import { testNapi } from 'library';

6. @Entry
7. @Component
8. struct Index {
9. @State message: string = 'Hello World';
10. build() {
11. Row() {
12. Column() {
13. Text(this.message)
14. .fontSize(50)
15. .fontWeight(FontWeight.Bold)
16. .onClick(() => {
17. // Call methods in Napi
18. hilog.info(0x0000, 'testTag', 'Test NAPI 2 + 3 = %{public}d', testNapi.add(1, 2));
19. })
20. }
21. .width('100%')
22. }
23. .height('100%')
24. }
25. }
```

[Index3.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/StabilityCodingSpecification/DevEcoStaticCheck/src/main/ets/pages/Index3.ets#L21-L45)

### 导出方模块

通过统一出口将napi导出。

模块根目录 > index.ets

```
1. import testNapi from 'liblibrary.so';
2. export {testNapi}
```

[Index.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/StabilityCodingSpecification/Ndk1/src/main/ets/pages/Index.ets#L19-L20)
