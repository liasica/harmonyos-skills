---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-prefetch-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 预加载 > 概述
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:15+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:54772a2cce584f8b6e303b670a70ec2b8dca9e997deb3fab0ea1d5a24fe6701e
---

从5.0.3(15)版本开始，新增支持安装预加载和周期性预加载功能；从6.1.0(23)版本开始，新增支持跳链安装预加载功能。

预加载是Cloud Foundation Kit提供的一种可提前加载所需资源的服务。通过预加载，可以将页面所需的文本、图片、音频、视频等资源数据提前加载到本地进行缓存，以提升应用页面加载速度。预加载仅以字符串数据形式进行缓存，应用使用预加载时不需要修改原有数据格式，获取缓存后可直接进行解析，并且可以对隐私、敏感数据进行加密。

当前支持如下三种预加载类型：

* **安装预加载**：适用于安装应用后首次打开，应用首页加载提速场景。在应用安装时下载云侧应用数据进行缓存，应用打开时直接获取本地首开页面缓存数据呈现内容。
* **周期性预加载**：适用于任意页面加载提速的场景，可与安装预加载结合使用。系统每隔12h拉取一次指定页面（不局限首开页面）的云侧数据并将其缓存到本地，并可将静态资源放置到云端，减少包体大小。比较适合节日主题资源、H5离线包等场景。
* **跳链安装预加载**：适用于被分享用户安装应用后首次打开，应用详情页加载提速场景，可与安装预加载、周期性预加载结合使用。在应用安装过程中，预加载结合App Linking Kit的延迟链接功能，可提前将用户之前点击的详情页数据缓存到本地。当用户首次打开应用时，即可直接跳转到相应的详情页，并即时加载本地缓存的数据呈现内容。

  **说明** 

  跳链安装预加载仅支持在HarmonyOS应用中调用。

同时还支持**H5预加载组件FastWeb**，它是基于Open Harmony基础组件开发的高性能Web容器，具有预启动、预渲染、预编译JavaScript生成字节码缓存、离线资源免拦截注入等能力，可为应用中Web页面的加载进行提速。H5预加载组件FastWeb无需使用Cloud Foundation Kit能力，详细使用方法可参考[Web容器FastWeb](https://developer.huawei.com/consumer/cn/market/prod-detail/686766c4728d43cc9741728552a560bf/2adce9bbd4cb42d58a87e6add45594b3)。

## 工作原理

1. 预加载服务根据配置的数据预加载策略从应用后台获取数据。
2. 预加载服务将获取的数据在本地进行缓存。
3. 应用使用获取的缓存数据，进行页面渲染。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/Pn_9AdiSQvqucO6e2uxlgw/zh-cn_image_0000002788307990.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004632Z&HW-CC-Expire=31536000000&HW-CC-Sign=9881AA3FCFE6086435D940D5B07433A0B645DD79D42B24044E943E3C50D2D531)

## 典型应用场景

### 提升应用首开速度

在应用启动前或初始化阶段，为避免出现首页内容加载慢、白屏等情况，开发者可以使用预加载将一些必要的资源，例如图片、音频、视频或数据文件，提前加载到本地进行缓存。用户首次访问应用时，可直接从缓存中获取数据，这样就减少了从服务器重新下载资源的时间，提升了应用首开速度，从而提高用户留存率。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/L7vsOf37QN2lSgmjqB2QlQ/zh-cn_image_0000002817427353.png?HW-CC-KV=V1&HW-CC-Date=20261114T004632Z&HW-CC-Expire=31536000000&HW-CC-Sign=8F6130BDEB3C53896DB7D16997992F3126595F47038F34075104987C73F316B7)

### 实现节日主题即发即现

很多应用会在节日更换特定主题内容进行活动营销，用户打开应用时需要从服务器上获取相关资源来呈现内容，可能会造成页面加载速度较慢而导致用户体验不佳。开发者可以使用预加载，在节日活动开始前通过周期性的数据拉取提前将主题资源获取到本地，活动开始用户访问时直接从本地获取即可，减少了网络请求的时间和带宽消耗，从而能够更快地展示节日主题，实现即发即现的效果，提升用户体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/7X9sy-KsTluz4DTNfmZJpA/zh-cn_image_0000002788467934.png?HW-CC-KV=V1&HW-CC-Date=20261114T004632Z&HW-CC-Expire=31536000000&HW-CC-Sign=4E3E4B84EBF44DC1CA34EBB1AF495401F95C097C14DBEEB608F4511EA04BC6F0)

## 约束与限制

### 设备限制

支持Phone、Tablet设备。并且从6.1.0(23)版本开始，新增支持PC/2in1设备。

### 数据限制

| 限制项 | 说明 |
| --- | --- |
| 数据类型 | 仅支持缓存文本、图片、音频、视频等静态资源数据，不支持代码、脚本等动态资源数据。 |

### 配额限制

| 配额类型 | 配额 |
| --- | --- |
| 安装预加载缓存大小 | 2MB |
| 周期性预加载缓存大小 | 3MB |
| 跳链安装预加载缓存大小 | 3MB |
