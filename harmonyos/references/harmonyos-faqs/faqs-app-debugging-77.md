---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-77
title: 如何获取应用打印的日志并写入文件
breadcrumb: FAQ > DevEco Studio > 应用调试 > 如何获取应用打印的日志并写入文件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f17448422d1089c0a8951ea3c13ab51866e6ccec8402167953d76c45462e685e
---

## 问题现象

使用HiLog打印默认是打印在控制台上，如何获取应用打印的日志并写入文件？

## 背景知识

* [使用HiLog打印日志](../harmonyos-guides/hilog-guidelines-ndk.md)：HiLog中定义了DEBUG、INFO、WARN、ERROR、FATAL五种日志级别，并提供了对应的方法输出不同级别的日志，具体说明可查阅[API参考文档](../harmonyos-references/capi-log-h.md)。
* [使用Node-API实现跨语言交互开发流程](../harmonyos-guides/use-napi-process.md)：
  + ArkTS/JS侧：实现C++方法的调用。import一个对应的so库后，即可调用C++方法。
  + Native侧：.cpp文件，实现模块的注册。需要提供注册lib库的名称，并在注册回调方法中定义接口的映射关系，即Native方法及对应的JS/ArkTS接口名称等。
* [OH\_LOG\_SetCallback](../harmonyos-references/capi-log-h.md#oh_log_setcallback)：调用此函数后，用户实现的回调函数可以接收当前进程的所有HiLog日志。回调函数里不允许再调用HiLog接口打印日志会死循环。

## 解决方案

在ArkTS侧将沙箱中的路径传递给Native侧，通过OpenFile方法打开文件，然后调用MyHiLog方法把日志写入到文件中。

* index.ets：在ArkTS侧获取到沙箱路径，调用testNapi.init方法将沙箱中的路径传递给Native侧。

  ```ts
  import { hilog } from '@kit.PerformanceAnalysisKit';
  import { common } from '@kit.AbilityKit';
  import testNapi from 'libentry.so';

  const DOMAIN = 0x0000;

  @Entry
  @Component
  struct Index {

    aboutToAppear(): void {
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      let path: string = context.filesDir;
      testNapi.init(path);
    }

    build() {
      Row() {
        Column() {
          Button('test')
            .fontSize($r('app.float.page_text_font_size'))
            .fontWeight(FontWeight.Bold)
            .onClick(() => {
              hilog.info(DOMAIN, 'testTag', 'Test NAPI 2 + 3 = %{public}d', testNapi.add(2, 3));
            })
        }
        .width('100%')
      }
      .height('100%')
    }
  }
  ```
* Index.d.ts：init接口声明。

  ```ts
  export const add: (a: number, b: number) => number;
  export const init: (path: string) => number;
  ```
* CMakeLists.txt：链接libhilog\_ndk.z.so依赖。

  ```cmake
  # the minimum version of CMake.
  cmake_minimum_required(VERSION 3.5.0)
  project(HilogToFile)
  set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})
  if(DEFINED PACKAGE_FIND_FILE)
      include(${PACKAGE_FIND_FILE})
  endif()
  include_directories(${NATIVERENDER_ROOT_PATH}
                      ${NATIVERENDER_ROOT_PATH}/include)
  add_library(entry SHARED napi_init.cpp)
  target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so )
  ```
* napi\_init.cpp：添加init函数Napi框架。

  ```cpp
  static napi_value Init(napi_env env, napi_value exports)
  {
      napi_property_descriptor desc[] = {
          {"add", nullptr, Add, nullptr, nullptr, nullptr, napi_default, nullptr},
          {"init", nullptr, Init, nullptr, nullptr, nullptr, napi_default, nullptr}};
      napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
      return exports;
  }
  ```
* init函数：Native层从ArkTS层获取到的日志路径存放到static变量g\_path中，作为日志全局的路径。设置g\_openState来防止重复初始化，通过函数OpenFile来打开/创建日志文件。如果正常打开文件则使用OH\_LOG\_SetCallback来注册日志落盘函数。否则返回异常，ArkTS通过返回值来判断是否初始化成功。

  ```cpp
  static napi_value Init(napi_env env, napi_callback_info info)
  {
      size_t argc = 1;
      napi_value args[1] = {nullptr};
      napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
      char path[1024 * 4] = {0};
      size_t pathLen = 0;
      napi_get_value_string_utf8(env, args[0], path, 1024 * 4, &pathLen);
      int ret = 0;
      // 1.设置打印文件路径&日志文件
      std::string tmpPath(path);
      g_path = tmpPath;
      OH_LOG_INFO(LOG_APP, "napi sum Init m_path: %{public}s, %{public}d", g_path.c_str(), g_path.size());
      if (g_openState == UNOPENED && g_path != "" && (g_file = OpenFile("ab"))) {
          g_openState = OPEN;
          // 2.注册回调接口
          OH_LOG_SetCallback(MyHiLog);
      } else {
          ret = -1;
          OH_LOG_INFO(LOG_APP, "napi sum Init m_path fail:%{public}d| %{public}s, %{public}d", g_openState, g_path.c_str(),
                      g_path.size());
      }
      napi_value returnValue;
      napi_create_int32(env, ret, &returnValue);
      return returnValue;
  }
  ```
* OpenFile函数：使用realpath函数来获取文件的绝对路径，并判断路径是否可用，如可用则使用fopen带参数"ab"来打开该文件，并获取到句柄存储到g\_file静态变量中。

  ```cpp
  FILE *OpenFile(const char *pszMode)
  {
      char filePath[PATH_MAX] = {0};
      char *ret = realpath(g_path.c_str(), filePath);
      if (ret == nullptr) {
          OH_LOG_INFO(LOG_APP, "napi sum OpenFile path realpath fail!!, %{public}s, %{public}d", g_path.c_str(),
                      g_path.size());
          return nullptr;
      }
      std::string fullFileName = std::string(filePath) + "/test.log";
      OH_LOG_INFO(LOG_APP, "napi sum OpenFile path is:%{public}s", fullFileName.c_str());
      return std::fopen(fullFileName.c_str(), pszMode);
  }
  ```
* 回调函数MyHiLog：判断文件句柄g\_file是否正常，正常则可以使用fwrite和fflush来写入到文件中。

  ```cpp
  void MyHiLog(const LogType type, const LogLevel level, const unsigned int domain, const char *tag, const char *msg)
  {
      if (g_file != nullptr) {
          std::string tmp(msg);
          tmp += '\n';
          fwrite(tmp.c_str(), sizeof(char), tmp.size(), g_file);
          fflush(g_file);
      }
  }
  ```
* Add函数：ArkTS侧调用Add方法，Add方法内输出日志。

  ```cpp
  static napi_value Add(napi_env env, napi_callback_info info)
  {
      size_t argc = 2;
      napi_value args[2] = {nullptr};
      napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
      napi_valuetype valuetype0;
      napi_typeof(env, args[0], &valuetype0);
      napi_valuetype valuetype1;
      napi_typeof(env, args[1], &valuetype1);
      double value0;
      napi_get_value_double(env, args[0], &value0);
      double value1;
      napi_get_value_double(env, args[1], &value1);
      napi_value sum;
      napi_create_double(env, value0 + value1, &sum);
      OH_LOG_INFO(LOG_APP, "napi sum is:%{public}d.", (int)(value0 + value1));
      
      return sum;
  }
  ```
