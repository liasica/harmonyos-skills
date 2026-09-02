---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-pre-connect
title: 冷启网络预建链最佳实践
breadcrumb: 最佳实践 > 技术创新 > 冷启网络预建链最佳实践
category: best-practices
scraped_at: 2026-09-02T15:03:15+08:00
doc_updated_at: 2026-06-23
content_hash: sha256:9d2d58ad71000a115e64e618fed236ad4ba9bb531bcfa359917f90ef3a4149f3
---

## 概述

应用冷启动时，网络请求需要经历域名解析、TCP连接建立、TLS握手等连接过程，在一次完整的请求中，连接阶段的这些操作会消耗大量时间，从而影响用户首屏加载体验。RCP（Remote Communication Kit）提供预建链技术通过提前建立与目标服务器的网络连接，将请求连接阶段与应用启动、准备请求等操作并行执行，使得在实际数据传输时可直接使用已建立的连接，显著提升首屏加载速度。

以图片列表加载场景为例，应用启动后需要加载多张网络图片。传统方式下，每张图片请求都需要经历完整的建链过程；而使用预建链技术后，可在应用启动阶段提前建立与图片服务器的连接，当用户滑动列表时，图片数据即可通过已建立的连接快速下载。

预建链技术的核心价值体现在三个方面：性能提升、用户体验优化和资源利用率优化。通过将建链过程与业务逻辑并行执行，预建链通常可节省400-700ms的网络延迟，使首屏内容加载更快，减少用户等待时间，提升应用流畅度和响应速度。在网络条件稳定的情况下，提前建立连接还可充分利用网络带宽，避免后续请求的建链等待。

## 实现原理

预建链技术的核心思想是将请求的连接阶段与数据传输阶段分离，通过提前执行DNS解析、TCP连接建立和TLS握手等操作，建立与目标服务器的网络连接。在应用启动阶段，预建链过程与业务逻辑并行执行；当用户实际触发数据请求时，直接使用已建立的连接发送HTTP请求，跳过建链过程。这种机制依赖于RCP能力提供的[Request](../harmonyos-references/remote-communication-rcp.md#request)接口中connectOnly属性，当该属性设置为true时，请求只会执行到连接建立阶段，不会发送HTTP请求体，也不会接收响应数据。预建链请求建立的连接会被会话管理器缓存，系统会自动复用已建立的连接，从而实现连接复用的效果。

从性能优化角度来看，预建链通过并行执行建链过程，将建链时间从请求的执行路径中移除。在传统请求中，建链时间是请求总耗时的主要组成部分，通常占总耗时的40%-60%。而使用预建链后，建链时间被转移到应用启动阶段，与业务逻辑并行执行，实际请求的耗时只包括数据传输时间，可节省200-400ms。同时，预建链充分利用了应用启动阶段的空闲网络带宽，提升了首屏加载速度和用户体验。

使用预建链请求与未使用预建链请求时序对比图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/KsmV1iXpS067TjMRPIUj4Q/zh-cn_image_0000002594079346.png "点击放大") ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/UT7gv8FPQjGmjgDfu3k4Hw/zh-cn_image_0000002624518875.png "点击放大")

## 冷启动网络预热

### 场景描述

在应用冷启动场景中，用户首次打开应用或切换到新页面时，需要加载大量网络资源（如图片、视频、配置数据等）。这些网络请求建立连接的过程会显著影响首屏加载速度，尤其是在移动网络环境下。

典型应用场景包括：

1. 图片列表加载：新闻类、社交类应用启动后，首屏需要加载大量图片，每张图片都需要独立的网络请求。

2. 配置数据拉取：应用启动时需要从服务器拉取配置信息和用户数据等，这些请求的连接建立延迟会影响首屏展示。

3. 视频流媒体：视频应用启动时需要建立与媒体服务器的连接，提前建立连接可以加快视频播放的启动速度。

在这些场景中，如果能在应用启动阶段提前建立与目标服务器的网络连接，当实际数据请求发生时即可直接使用已建立的连接，从而大幅提升首屏加载速度。

### 开发步骤

预建链技术关键点在于RCP请求接口[Request](../harmonyos-references/remote-communication-rcp.md#request)的connectOnly属性。当该属性设置为true时，请求仅执行到连接建立阶段，不会发送HTTP请求体，也不会接收响应数据，从而实现快速建链。通过以下步骤配置RCP接口实现网络预热：

1.与目标服务器预建链：创建HTTP请求对象，并将connectOnly属性设置为true，表示仅建立连接而不传输数据，使用[getDefaultSession()](../harmonyos-references/remote-communication-rcp.md#getdefaultsession)执行预建链请求。

```typescript
try {
  const request = new rcp.Request(item.albumUrl, 'GET');
  request.configuration = {tracing: tracingConfig, security: securityConfig};
  request.connectOnly = true;
  let preConnectSession = getPreConnectSession();
  if (preConnectSession !== undefined) {
    preConnectSession.fetch(request).then((preConnectResponse: rcp.Response) => {
      item.preConnectTimeList = getTimeSpend(preConnectResponse);
    }).catch(() => {});
  }
} catch (err) {
  Logger.error(TAG, `preConnect ${item.targetId} error: the code is ${err.code}, the message is ${err.message}`);
}
```

在应用启动时，使用预键链请求与非预键链正常请求对比：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/36CTQAarTU2r9YGwDld_AA/zh-cn_image_0000002594239264.png)

2.连接复用获取数据：当实际数据请求发起时，直接复用预建链阶段已建立的连接，跳过连接建立过程，实现向目标服务器动态预取数据，以优化资源加载。

```typescript
const request = new rcp.Request(item.albumUrl, 'GET');
request.configuration = {tracing: tracingConfig, security: securityConfig};
// ...
  let preConnectSession = getPreConnectSession();
  if (preConnectSession !== undefined) {
    preConnectSession.fetch(request).then(async (preConnectResponse: rcp.Response) => {
      if (preConnectResponse.statusCode !== 200 || !preConnectResponse.body) {
        item.preConnectCachedImage = IMAGE_UNAVAILABLE;
        throw new Error('Bad response');
      } else {
        const preLinkArrayBuffer = preConnectResponse.body as ArrayBuffer;
        item.preConnectCachedImage = await toPixelMap(preLinkArrayBuffer);
        item.preConnectTimeList = getTimeSpend(preConnectResponse);
      }
    }).catch((err: BusinessError) => {
      item.preConnectCachedImage = IMAGE_DEFAULT;
      Logger.error(TAG, `preConnectSession ${item.targetId} request error: the message is ${err.message}`);
    });
  }
```

从应用启动到发起请求获取数据内容，使用预键链技术与正常请求对比：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/KCzhzouqQaSGRgPWARgQCg/zh-cn_image_0000002624638731.gif)

## 常见问题

### 适用场景

**问题现象**

预建链技术是否适用于所有RCP请求场景？

**解决措施**

预建链技术主要适用于冷启动场景或可以提前预测资源URL的场景。对于无法预测URL或资源动态生成的场景，预建链效果有限。建议在应用启动时预建链高频访问的固定资源，如配置服务器、CDN域名等。

### 资源消耗

**问题现象**

预建链技术在一次完整的RCP请求中消耗多少资源？

**解决措施**

预建链仅建立TCP连接，不传输数据，因此消耗的资源较少。每个预建链请求会占用一个TCP连接，建议根据实际需求控制并发数量，避免过多连接占用系统资源。

### 评估预建链效果

**问题现象**

如何量化评估预建链效果？

**解决措施**

可以通过对比预建链前后的首屏加载时间、建链耗时等指标来评估效果。配置RCP的[TracingConfiguration](../harmonyos-references/remote-communication-rcp.md#tracingconfiguration)中耗时采集相关的属性，可以获取详细的网络请求时序信息，包括DNS解析时间、TCP连接时间、TLS握手时间等。

## 示例代码

* [网络预建链](https://gitcode.com/HarmonyOS_Samples/RcpPreconnect)
