---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-jsvm-12
title: napi关联的c层对象无法触发GC
breadcrumb: FAQ > 应用框架开发 > NDK开发 > JSVM > napi关联的c层对象无法触发GC
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:59+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:01d28a13e0102c4e1f471f9756615661d11b47290a79675a17762d230d8d9b68
---

## 问题现象

在ArkTS创建一个对象，通过napi\_wrap将ArkTS对象与Native的C++对象绑定，第一次创建ArkTS对象后触发napi\_wrap的垃圾回收回调，等回收完成后再次创建对象，垃圾回收回调不会触发。

ArkTS侧创建对象：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/q-xm9LTUTky7TvH7JBaQ1w/zh-cn_image_0000002658907827.png "点击放大")

C++侧构造函数和析构函数：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/oF8BJEvYRBWXGszzPoNXqw/zh-cn_image_0000002658787891.png "点击放大")

napi\_wrap绑定ArkTS对象与C++对象：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/qCONgY9sTQiJJ9k5jkAWrw/zh-cn_image_0000002628388616.png "点击放大")

## 背景知识

* GC（全称[Garbage Collection](../harmonyos-guides/gc-introduction.md)），即垃圾回收。在计算机领域，GC是指识别并释放内存中的不再使用的对象，以回收内存空间。
* napi\_wrap可以将ArkTS对象与Native的C++对象绑定，后续操作时再通过napi\_unwrap将ArkTS对象绑定的C++对象取出，并对其进行操作，详见：[Native与ArkTS对象绑定](../harmonyos-guides/use-napi-object-wrap.md)。
* [napi\_wrap\_enhance](../harmonyos-references/napi.md#napi_wrap_enhance)用于在ArkTS对象上绑定一个NAPI模块对象实例并指定实例大小，开发者可以指定绑定的回调函数是否异步执行，如果异步执行，则回调函数必须是线程安全的。

## 问题定位

多次创建对象，析构执行后，再次创建对象不会再执行析构。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/ZpEClTNARCaCBgboaXTD5w/zh-cn_image_0000002628548516.png "点击放大")

## 分析结论

ArkTS侧的变量大小如果没有达到GC触发水位线，此时C++侧内存大小不在触发水位线计算范围内，不会触发GC行为，napi\_wrap绑定的析构处理回调也不会调用。

## 修改建议

将napi\_wrap替换为[napi\_wrap\_enhance](../harmonyos-references/napi.md#napi_wrap_enhance)，napi\_wrap\_enhance会在绑定的时候把Native对象大小传给虚拟机，实现及时回收，示例代码如下：

```cpp
// 通过napi_wrap将ArkTS对象jsThis与C++对象obj绑定
napi_status status = napi_wrap_enhance(env, jsThis, reinterpret_cast<void *>(obj), MyObject::Destructor, false,
                                       nullptr, // finalizeHint
                                       100 * 1024 * 1024, &obj->wrapper_);
```

## 常见FAQ

Q：析构Object时调用了napi\_remove\_wrap，那么对应的FinalizeCallback是否应该被移除？

A：调用[napi\_remove\_wrap](../harmonyos-references/napi.md#napi_remove_wrap)的时候，如果封装中关联有finalize回调，HarmonyOS中该导出接口将在移除封装前调用它。
