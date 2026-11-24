---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-locate-application-crashes
title: 开发态快速定位应用崩溃
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 开发态稳定性分析 > 应用崩溃类问题分析 > 开发态快速定位应用崩溃
category: best-practices
scraped_at: 2026-11-24T12:47:58+08:00
doc_updated_at: 2026-11-09
content_hash: sha256:fed8e33cea2ff80f140dc519731faccbc17576059bb60fb06a8d48f2d71d68bf
---

## 概述

踩内存是指程序向未分配、已释放或越界的内存地址写入数据，破坏正常内存布局，从而导致程序行为异常、数据错乱甚至崩溃。这类崩溃往往复现困难、定位耗时，属于系统稳定性中的高风险问题。

本文以内存越界访问为典型案例，构建数组越界示例工程，完整演示HWASan（参考：[使用HWASan检测内存错误](bpta-stability-hwasan-detection.md)）与BinXO工具的使用流程，提供踩内存问题的定位范式，为其他高频崩溃场景的排查提供可复用的实践参考。

## 高频崩溃场景

* 内存越界访问：应用程序在读写内存时，超出了它被合法分配的内存区域边界，触发CppCrash日志，最终引发系统异常或应用崩溃。
* 内存未初始化读：应用程序在读取一块内存区域时，该内存之前没有被赋予任何确定的值（例如只分配了空间但没有赋值），最终引发系统异常或应用崩溃。
* 内存释放后访问：应用程序在将一块内存归还给系统（或分配器）之后，仍然通过之前保存的指针去读取、写入或释放该内存，最终引发系统异常或应用崩溃。
* 内存重复释放：应用程序对同一块已经释放过的内存再次调用释放函数（如free或delete），最终引发系统异常或应用崩溃。
* 文件句柄非法关闭：应用程序对一个已经关闭、无效或从未成功打开的文件句柄（或套接字、管道等系统资源句柄）再次执行关闭操作，最终引发系统异常或应用崩溃。
* 内存释放地址异常：应用程序传递给内存释放函数（如free、delete）的指针地址，不是之前由相同分配器（如malloc、new）返回的合法地址，最终引发系统异常或应用崩溃。
* 未定义异常访问：应用程序访问了操作系统未允许其访问的内存地址，从而触发硬件层级的异常（如段错误SIGSEGV），最终引发系统异常或应用崩溃。

## 标准化排查流程

**1、复现与日志获取**

触发数组越界访问，在DevEco Studio底部FaultLog模块中获取CppCrash日志，记录崩溃现场。

**2、分析崩溃日志**

解析CppCrash日志发现：堆栈与业务逻辑无明显关联，呈现随机性且为低概率事件；崩溃类型为“SIGSEGV(SEGV\_MAPERR)”，提示访问无效内存地址。

**3、开启HWASan**

启用HWASan工具重新编译运行，工具立即捕获越界访问并输出详细日志。单击日志中蓝色字体的堆栈行，可直接跳转至越界发生的具体方法源码位置。

**4、开启BinXO**

针对三方库so调用场景，启用BinXO（HWASan增强版）重新运行。工具精准捕获三方库so的数组越界，日志同样支持点击蓝色堆栈快速定位到调用so的具体方法。

**5、修复与验证**

根据定位信息优化越界代码，重新编译并重复上述复现步骤，确认应用不再崩溃，问题闭环。

通过上述流程，HWASan与BinXO可高效定位内存越界等底层崩溃，为复杂崩溃问题的排查提供标准化操作路径，详细流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/OvXmwH6NQZqcWOrQ0D4DXg/zh-cn_image_0000002701362583.png?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=0C0BD632BA9A8910EE04763205C2BEB34B4AE05D7138C9CF26DA5131CD215782)

## 数组越界案例

## 案例背景

通过一个长度为8的数组越界访问的示例工程，完整演示HWASan和BinXO工具使用步骤及日志分析方法，示例工程分为两个场景：

* 场景一：本地代码中数组越界访问（索引大于7）。
* 场景二：三方库so中数组越界访问，本地方法去访问三方库so中的数组越界访问方法（索引小于0）。

## 分析流程

1. 触发场景一和场景二的数组越界访问

   1、设置Build Mode为debug模式打开DevEco Studio，以debug模式运行示例工程，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/SsLIMcBpSFKl3il3QVYY3g/zh-cn_image_0000002671482890.png?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=48D18084B4290753ABCCD535E97D60D33891DDF5906BE2594B72EF8C35FA2416)

   2、运行应用，反复滑动图片触发索引值超出范围，索引值大于7或者小于0的时候会低概率使应用崩溃产生CppCrash日志，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/0JGcLvz0RtWexOMEFMcrow/zh-cn_image_0000002671642752.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=DB51621F0B9B852D8A2C3F3F1D7C8593364CB69D00311CF08AA647D7C23B183D "点击放大")

   3、分析CppCrash日志，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/5sb5jfPfRQuBSpJSQsEKyQ/zh-cn_image_0000002701242495.png?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=0BB339FE5122B3167AB1F5997637DA6E16DF94E64E32B5097DF657012A1226DF "点击放大")

   应用出现“SIGSEGV(SEGV\_MAPERR)”信号，表示访问了无效内存地址。该类崩溃通常由以下内存操作错误引发：

   * 数组越界访问
   * 野指针解引用
   * 重复释放内存
   * 访问已释放内存（Use-After-Free）

   程序实际崩溃点仅为“受害者”——越界写入破坏了堆上关键对象，直到该对象被访问或释放时才触发其他库的安全检查或访问异常。因此，当崩溃堆栈指向系统库且与应用进程无直接关联时，应高度怀疑为踩内存问题。
2. 使用HWASan工具分析

   1、开启HWASan工具，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/JjHBckztTCKJGb1Papr0RA/zh-cn_image_0000002701362591.png?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=B94A59E4FA9A4920F2DF24086CB9D8314EA3113BDA6D9420331AED551C78BBAE)

   2、运行应用，左滑图片超出索引（>7），应用必崩溃（HWASan工具会立即捕获本地代码数组越界访问），触发HWASan日志，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/Br9O9XMvSBWVS6twi8Yuvw/zh-cn_image_0000002671482902.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=E9645F911D5E7979F5CCD56AAB2E6A97F6208BCDF2046F2F6AFB7BDD864DC6C5 "点击放大")

   3、分析HWASan日志，日志中显示堆栈信息，并且蓝色链接单击跳转到具体踩内存的方法中，方便开发者定位修改，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/4pKa-hmKRcG5cLEkFvtYIw/zh-cn_image_0000002671642766.png?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=824116A637677BB8C16F9D43D1C69290E6B68E30A31B015D8C60C84777B69EE8)

   4、重新运行应用，右滑图片超出索引（<0），应用低概率崩溃（HWASan工具不会立即捕获三方库so中的数组越界访问），崩溃产生HWASan日志，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/tYG1wNn4RyqeCbrDuc96Aw/zh-cn_image_0000002701242503.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=DCF26969EDD9CE13CE022B247B2B42860350FDFDD88B69DFD949652505E9DBDB "点击放大")

   5、分析HWASan日志时发现，其输出的堆栈信息无法有效定位到具体的越界访问代码行。原因在于，HWASan工具对第三方动态库（so）中的数组越界错误，往往不能即时捕获；即便捕获到异常，生成的日志也因堆栈信息不完整或缺乏符号解析，难以协助开发者追溯问题源头，具体现象如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/nRZNygTkTw6do8awTP-xDw/zh-cn_image_0000002701362603.png?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=458894D93E64372A38161BC67E85E2C21FE793CE30EECFDCE2E275945E9CA1FB "点击放大")
3. 使用BinXO工具分析

   1、在HWASan基础上打开BinXO开关，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/mGtKM1q1TgO0ahjIQ6Zvbw/zh-cn_image_0000002671482910.png?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=379B3578BA8BAA775BEF5290A5BD51B5E0725B99DD8FCB24BD767B67EC151EB8)

   2、重新运行应用，右滑图片超出索引（<0），应用必崩溃（BinXO工具会立即捕获三方库so中数组越界访问），触发HWASan日志，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/ckGLXk4FR7eWR5y4LC0HiA/zh-cn_image_0000002671642770.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=619038883608A1C23FBC2D4FBB662748BD4FE85D613F202734851DD64DE69166 "点击放大")

   3、分析HWASan日志，日志中显示堆栈信息，并且蓝色链接单击跳转到具体踩内存的方法中，方便开发者定位修改，堆栈第0帧是调用的三方库so信息，第1帧蓝色链接单击跳转到具体踩内存的方法，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/qC1lKS_dS1y1oJ6vh8JsJQ/zh-cn_image_0000002701242505.png?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=B5E0ABF82C9F16E6EA3367E6BB653660E50417059E0BC961A5F5713F91E1728A)

## 代码分析与优化

场景一：本地代码实现数组越界访问，imageAccessTime[index]未做边界检查，索引大于7会触发数组越界访问问题。需要在imageAccessTime[index]之前做索引index检查（如下注释代码），防止越界。

```cpp
static napi_value GetImageNameNotFromSo(napi_env env, napi_callback_info info)
{
    std::int64_t *imageAccessTime = new std::int64_t[8]{0};

    size_t argc = 1;
    napi_value args[1] = {nullptr};
    napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

    int index;
    napi_get_value_int32(env, args[0], &index);
    
    /*
     if (index < 0 || index >= g_count) {
         napi_throw_error(env, "", G_WARN_IMAGE);
         return nullptr;
     }
    */
    
    imageAccessTime[index] = std::time(nullptr);

    if (index < 0 || index >= g_count) {
        napi_throw_error(env, "", G_WARN_IMAGE);
        return nullptr;
    }

    napi_value imageName;
    napi_create_string_utf8(env, G_IMAGE_NAMES[index], strlen(G_IMAGE_NAMES[index]), &imageName);

    delete[] imageAccessTime;
    return imageName;
}
```

场景二：引入三方库so实现数组越界访问，GetImageName()函数入参index未做边界检查，索引小于0会触发数组越界访问问题。需要在GetImageName()之前做索引index检查（如下注释代码），防止越界。

```cpp
extern "C" const char *GetImageName(int index);

static napi_value GetImageNameFromSo(napi_env env, napi_callback_info info)
{
    size_t argc = 1;
    napi_value args[1] = {nullptr};
    napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

    int index;
    napi_get_value_int32(env, args[0], &index);
    
    /*
     if (index < 0 || index >= g_count) {
         napi_throw_error(env, "", G_WARN_IMAGE);
         return nullptr;
     }
    */
    
    const char *imageNameStr = GetImageName(index);

    if (index < 0 || index >= g_count) {
        napi_throw_error(env, "", G_WARN_IMAGE);
        return nullptr;
    }
    napi_value imageName;
    napi_create_string_utf8(env, imageNameStr, strlen(imageNameStr), &imageName);

    return imageName;
}
```

## 示例代码

* [踩内存问题分析用例](https://gitcode.com/HarmonyOS_Codelabs/memory-corruption-arkts/tree/dev)
