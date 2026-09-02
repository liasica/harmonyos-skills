---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-form-25
title: 如何定位并解决卡片白屏展示的问题
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 卡片开发（Form） > 如何定位并解决卡片白屏展示的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b70c34ef5602c9e28b5182e9a46b62d38f38b10e916992dedab156fd60fe5807
---

## 问题现象

在开发服务卡片功能时，可能会出现卡片白屏显示异常的问题。这可能是因为卡片页面样式配置错误，也可能是因为没有遵循卡片的开发约束。如何通过卡片日志定位并解决问题？异常示例图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/VuOGu6uKQKOwYs77o6fYzw/zh-cn_image_0000002658990875.png "点击放大")

## 背景知识

* [Form Kit（卡片开发服务）](../harmonyos-guides/formkit-overview.md)提供了一种在桌面、锁屏等系统应用上嵌入显示应用信息的开发框架和API，可以将应用内用户关注的重要信息或常用操作抽取到服务卡片（简称“卡片”）上，通过将卡片添加到桌面、锁屏等系统应用上，以达到信息展示、服务直达的便捷体验效果。
* 为确保系统渲染进程的稳定性、各卡片之间的隔离安全性，以及内存功耗等资源考虑，对ArkTS卡片UI可使用的能力做了以下[约束](../harmonyos-guides/arkts-form-overview.md#约束与限制)：
  + 当前仅支持基于ArkUI开发卡片，不支持跨平台开发。
  + 当导入模块时，仅支持导入标识“支持在ArkTS卡片中使用”的模块。若使用了不支持使用的API，卡片加载显示异常。
  + 支持导入HAR静态共享包，不支持导入HSP动态共享包。
  + 不支持使用native语言开发，不支持加载native so。
  + 针对卡片UI页面开发，ArkTS卡片仅支持声明式范式的部分组件、事件、动效、数据管理、状态管理和API能力。对于支持在ArkTS卡片UI页面中使用的接口，会添加“卡片能力”的标记：从API version x开始，该接口支持在ArkTS卡片中使用。
  + 卡片组件内容的事件处理和卡片使用方的事件处理是独立的，为防止手势冲突，卡片内不支持左右滑动的控件。

## 问题定位

**场景一：**

```txt
08-30 23:13:10.652 6421 6421 W A01B01/com.ohos.sceneboard/HOME: FormItemRelativeEvent: event registration completed
08-30 23:13:10.652 6421 6421 I A01C05/com.ohos.sceneboard/FORM: FormComponentEvent: setFormOpacity, opacity: 0.005
```

根据日志信息进行定位，全局搜索关键词setFormOpacity定位，发现卡片透明度被设置为0.005（偏低），因此卡片的内容会呈现空白。

**场景二：**

```txt
[ecmascript] Pending exception before ExecutePendingJob called, in line:5868, exception details as follows:
TypeError: Cannot read property createHttp of undefined
Cannot get SourceMap info, dump raw stack: at anonymous (entry|myhar|1.0.0|src/main/ets/components/MainPage.ts:60:40)
```

出现“Cannot get SourceMap info, dump raw stack”关键字，通常表明开发者的API写法存在错误，或者引入了不支持卡片的模块，从而导致相关模块报错。若错误类型为“TypeError：Cannot read property xxx”，需首先确认该属性是否属于系统模块，并进一步明确当前模块是否支持服务卡片。以调用http模块中createHttp方法为例：根据错误日志，对报错文件中的属性进行检查，发现存在如下定义：

```ts
import { http } from '@kit.NetworkKit';
let httpRequest = http.createHttp();
```

点击函数声明，查询该函数是否支持在卡片中使用。

```ts
/**
  * Creates an HTTP request task.
  * @returns { HttpRequest } the HttpRequest of the createHttp.
  * @syscap SystemCapability.Communication.NetStack
  * @crossplatform
  * @atomicservice
  * @since 11
  */
function createHttp(): HttpRequest;
```

经查询，该函数缺少@form标签，即不支持在卡片中使用。

**场景三：**

```txt
[ecmascript] Pending exception before ExecutePendingJob called, in line:5868, exception details as follows:
TypeError: Cannot read property name of undefined
Cannot get SourceMap info, dump raw stack: at anonymous (entry|entry|1.0.0|src/main/ets/widget/pages/WidgetCard.ts:43:40)
```

出现“Cannot get SourceMap info, dump raw stack”关键字，通常表明代码中API写法存在错误，或者引入了不支持卡片的模块，从而导致相关模块报错。若错误类型为“TypeError：Cannot read property xxx”，需首先确认该属性是否属于业务变量。如果是业务变量，则由业务方自行规避。以访问空数组对象的属性为例：根据错误日志，对报错文件中的属性进行检查，发现存在如下定义：

```ts
interface Person {
  name: string;
  age: number;
}

let persons: Person[] = []
console.info(persons[0].name)
```

**场景四：**

```txt
[form_provider_data.cpp(AddImageData:154)]Get file size failed, errno is 0
```

在服务卡片的数据更新流程中，当通过FormExtensionAbility向卡片管理服务（FormManagerService, FMS）传递图片文件描述符（fd）时，系统底层模块检测到获取图片文件大小失败。此问题通常发生在卡片通过updateForm方法更新数据时，涉及内存图片（memory://fileName）的加载逻辑。根据系统设计，服务卡片在刷新图片时需依赖文件描述符（fd）从内存中读取图片数据并完成渲染。

**场景五：**

```txt
load SharedMemoryImage timeout!
```

在服务卡片的运行过程中，当通过共享内存（Shared Memory）方式加载图片时，系统底层触发了超时异常（load SharedMemoryImage timeout!）。此问题通常发生在卡片一次性请求加载大量网络图片的场景中，其根本原因与卡片对共享内存的资源限制密切相关——系统在处理图片数据时，需将图片加载到共享内存中完成渲染，若图片总量或单张图片大小超出限制，系统将无法及时完成加载，进而触发超时。

## 分析结论

**场景一：**

应用的卡片透明度设置偏低，导致卡片内容呈现空白。

**场景二：**

卡片中调用了不支持的系统模块，调用方式可能为直接调用或者通过引用包间接调用。

**场景三：**

卡片自定义业务中出现了异常，缺乏边界值或空值条件判断。

**场景四：**

异常的核心原因在于传递给卡片管理服务的图片文件描述符（fd）无效或指向的文件已被提前释放。

**场景五：**

从API version 20开始，系统对卡片刷新数据的共享内存总大小限制为10MB，且单次刷新的图片数量上限为20张。在API version 19及之前的版本中，限制更为严格：图片文件数量上限为5张，且每张图片的内存占用不得超过2MB。若开发者在FormExtensionAbility中传递的图片文件描述符（fd）所指向的图片总量或数量超出上述限制，则系统在尝试加载共享内存时会因资源不足而超时，最终导致图片显示异常或卡片渲染失败。

## 修改建议

**场景一：**

在WidgetCard.ets文件中开发UI界面时，将卡片的透明度（即opacity属性）设置为合理可见的值。

**场景二：**

删除不支持卡片的模块。

**场景三：**

在可能出现异常的业务代码中补充判断逻辑。

**场景四：**

1. 确保文件存在：在调用fileio.openSync前，使用fileio.statSync(path)检查目标文件是否存在且可读。
2. 异步加载同步化：对于网络图片（如通过网络下载后保存到内存），需确保图片完全下载并写入文件系统后再调用fileio.openSync获取fd。可通过@ohos.data.fileio模块的异步API（如downloadFile）结合Promise或async/await控制流程，避免因文件未写入完成导致fd无效。

**场景五：**

1. 图片数据优化：通过Image kit相关接口，对图片进行[压缩](https://gitee.com/harmonyos_samples/image-compression)。对于非关键场景（如背景图、低优先级商品图），可采用有损压缩（如JPEG质量参数调整），减少内存占用；对于关键场景（如Logo、核心广告图），优先使用无损压缩（如WebP格式转换）以平衡质量与体积。
2. 刷新策略调整，分批次更新：若业务需刷新多张图片（如超过20张或单张体积较大），应将图片更新请求拆分为多个批次。例如，首次刷新加载首屏关键图片（如轮播图、促销栏），后续通过监听用户交互（如滚动、下拉），逐步加载非首屏图片。

## 总结

| 问题现象 | 关键日志 | 问题根因 | 解决方案 |
| --- | --- | --- | --- |
| 卡片白屏 | setFormOpacity | 卡片透明度被设置较低，导致卡片内容空白 | 将卡片的透明度（即opacity属性）设置为合理可见的值。 |
| Cannot get SourceMap info, dump raw stack | 卡片页面直接/间接引入了不支持卡片的模块 | 在卡片使用带有@form标签的API |
| Cannot get SourceMap info, dump raw stack | 自定义业务逻辑错误 | 根据实际业务修改 |
| Get file size failed, errno is 0 | 图片还未完成加载就打开 | 图片加载完毕后再渲染 |
| load SharedMemoryImage timeout! | 图片大小超过共享内存最大限制 | 图片压缩 |

## 常见FAQ

Q：在卡片开发过程中，很多import方法以及UI能力的使用不支持服务卡片，但只有部分情况会在开发和编译构建时报错提示，体现为卡片显示白屏。如何进行问题定位？

A：当卡片的页面功能复杂时，可能在卡片的实际运行时才崩溃报错，体现为卡片显示白屏。（注意：一个卡片报错后会导致应用的所有卡片渲染全部挂掉成为白屏）出现此类情况时，可以在IDE中查看日志，选择com.ohos.formrenderservice卡片渲染服务查看error日志看具体卡片渲染报错原因。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/5yLJ6qoTT6u1F-X1mCkT_Q/zh-cn_image_0000002628631666.png "点击放大")
