---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-coding-standard-ndk-arkts
title: NDK开发ArkTS侧编码规范
breadcrumb: 最佳实践 > 稳定性 > 稳定性优化 > 稳定性编码规范 > NDK开发ArkTS侧编码规范
category: best-practices
scraped_at: 2026-10-29T08:03:28+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:8c47e4b7f9d2f39ed6d1c5409dd77a568085fd5c4e228d334eac4aaf5121e2dd
---

ArkTS通过引用编译好的so文件来调用native方法。为避免不规范引用导致的运行时异常和故障排查成本，开发者应按照本文的标准进行引用。

NDK工程创建步骤及目录结构可参考：[创建NDK工程](../harmonyos-guides/create-with-ndk.md)。

## import本模块的so

**配置依赖**：

模块根目录 > oh-package.json5

```screen
{
  "name": "entry",
  "version": "1.0.0",
  "description": "Please describe the basic information.",
  "main": "",
  "author": "",
  "license": "",
  "dependencies": {
    // Dependent shared libraries
    "libentry.so": "file:./src/main/cpp/types/libentry"
  }
}
```

依赖文件中引用的so名称，要与CMakeLists.txt文件中定义的模块名称保持一致。

模块根目录 > src > main > cpp > CMakeLists.txt

```screen
# the minimum version of CMake.
cmake_minimum_required(VERSION 3.4.1)
project(MyApplication14)
set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})
if(DEFINED PACKAGE_FIND_FILE)
    include(${PACKAGE_FIND_FILE})
endif()
include_directories(${NATIVERENDER_ROOT_PATH}
                    ${NATIVERENDER_ROOT_PATH}/include)

# Declare a shared library artifact named libentry.so, where SHARED indicates that the artifact is a dynamic library, and napi_init.cpp is the source code for the artifact.              
add_library(entry SHARED napi_init.cpp)

# Declare the third-party library libace_napi.z.so required for linking the artifact entry
target_link_libraries(entry PUBLIC libace_napi.z.so)
```

**引用native方法**：

引用的so文件名称必须与oh-package.json5中定义的一致。

```screen
import { hilog } from '@kit.PerformanceAnalysisKit';
// import rely on so
import testNapi from 'libentry.so';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            // call native
            hilog.info(0x0000, 'testTag', 'Test NAPI 2 + 3 = %{public}d', testNapi.add(2, 3));
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

调用的方法名称必须与.d.ts文件中导出的方法名一致。

模块根目录 > src > main > cpp > types > libentry > index.d.ts

```typescript
export const add: (a: number, b: number) => number;
```

## import其它模块的so

开发者可以在har/hsp中编写公共的so，供其他模块调用。

### 引用方模块

**本地依赖**：

模块根目录 > oh-package.json5

```screen
{
  "name": "entry",
  "version": "1.0.0",
  "description": "Please describe the basic information.",
  "main": "",
  "author": "",
  "license": "",
  "dependencies": {
    // Depend on other modules within the current project
    "library": "file:../library"
  }
}
```

**远程依赖**：

运行命令

```screen
ohpm install library --registry http://localhost:8088/repos/ohpm
```

工程根目录 > oh-package.json5 中会自动配置依赖。

```screen
{
  "name": "depend_othermodule_so",
  "version": "1.0.0",
  "description": "Please describe the basic information.",
  "main": "",
  "author": "",
  "license": "",
  "dependencies": {
    // The name must match the remote module name
    "library": "^2.0.0"
  },
  "devDependencies": {
    "@ohos/hypium": "1.0.17",
    "@ohos/hamock": "1.0.1-rc2"
  }
}
```

**引用native方法**：

```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';
// Reference napi in dependent modules
import { testNapi } from 'library';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            // Call methods in Napi
            hilog.info(0x0000, 'testTag', 'Test NAPI 2 + 3 = %{public}d', testNapi.add(1, 2));
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

### 导出方模块

通过统一出口将napi导出。

模块根目录 > index.ets

```typescript
import testNapi from 'liblibrary.so';
export {testNapi}
```
