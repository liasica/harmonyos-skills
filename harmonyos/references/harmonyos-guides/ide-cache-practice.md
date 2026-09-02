---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-cache-practice
title: 性能优化：缓存插件实践
breadcrumb: 指南 > 构建应用 > 提升构建效率 > 实践说明 > 性能优化：缓存插件实践
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:04c7c163cbfdde22d0a30a347d929af568b1cf05f6d887c163741270ee2b8e1a
---

## 概述

在大型应用开发和多团队协作场景中，编译效率是制约开发体验的关键因素：

* 切换代码分支：当开发者切换到其他分支时，往往需要重新编译之前已经编译过的模块，造成时间浪费。
* 多团队协作：同一模块可能由多个团队成员并行开发，已编译过的缓存无法跨成员复用。
* 重复编译：清理工程缓存后，相同代码的重新编译会消耗大量不必要的时间。

针对该问题，Hvigor提供缓存增强插件@ohos/hvigor-cache-booster，采用多级缓存查找机制，按“当前编译模块build目录 -> 本地缓存 -> 远程缓存”的优先级查找编译缓存，显著提升首次编译效率。

## 使用约束

* Node.js版本要求：v18.20.1及以上版本。
* DevEco Studio或Command Line Tools版本要求：6.1.0 Release及以上版本。
* 当前仅支持ArkTS缓存。

## 安装插件

1. @ohos/hvigor-cache-booster插件上架在npm中心仓，需要确保.npmrc中已配置仓库地址。

   ```txt
   @ohos:registry=https://repo.harmonyos.com/npm/
   ```
2. 在工程的hvigor-config.json5文件中配置依赖的插件。

   ```json5
   "dependencies": {
       "@ohos/hvigor-cache-booster": "7.0.0"  
     },
   ```
3. 执行Sync或者Build，DevEco Studio会自动安装依赖。

## 使用示例

在模块的hvigorfile.ts中添加示例代码，按需修改配置后即可使用缓存增强插件，详细使用指导请参考@ohos/hvigor-cache-booster插件的[README.md文件](https://repo.harmonyos.com/npm/@ohos/hvigor-cache-booster/-/@ohos/hvigor-cache-booster-7.0.0.tgz)。

如需启用远程缓存，服务端需按规范实现相应API并提供服务，请参考插件README.md文档了解服务端API的规格要求。

```ts
// entry/hvigorfile.ts
import { hapTasks } from '@ohos/hvigor-ohos-plugin';
import { CacheBooster } from '@ohos/hvigor-cache-booster';
import { arkCacheChainFactory, ArkCacheChainConfig, ChainType } from '@ohos/hvigor-cache-booster';

// 缓存插件配置，可配置本地缓存和远程缓存
const arkChainCfg: ArkCacheChainConfig = {
  local: { enable: true, pushEnable: true, minPushIntervalHours: 0 },
  remote: { enable: true, pushEnable: true }
};

// 缓存链类型，可以为DEFAULT和OHOS_TEST，DEFAULT表示源代码目录，OHOS_TEST表示测试目录
const chain0 = arkCacheChainFactory.createArkCacheChain(ChainType.DEFAULT, arkChainCfg);
const chain1 = arkCacheChainFactory.createArkCacheChain(ChainType.OHOS_TEST, arkChainCfg);

export default {
  system: hapTasks,
  plugins: [new CacheBooster({
    enable: true,
    remoteUrl: 'https://...',   // 远程缓存url，如果启用远程缓存，根据实际环境修改
    strictSSL: false,
    cacheManagerChains: [chain0, chain1]
  })]
}
```
