---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/remote-communication-cache-basic
title: HTTP缓存基本功能
breadcrumb: 指南 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > 提升HTTP传输性能 > 使用HTTP缓存功能提升资源获取性能 > HTTP缓存基本功能
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e3fdcf8c77f28409457b06916936ba6ab4e752820ee57c42a20be493a6bb59c5
---

从6.0.0(20)开始，支持HTTP缓存。

HTTP 缓存是一种在客户端存储网络资源副本的机制，当后续请求相同资源时，可直接从缓存中获取，无需再次向服务器发起完整请求。HTTP 缓存适用于静态资源（如图片、CSS）和高访问量内容，能有效提升网络资源获取性能。Remote Communication Kit模块提供HTTP缓存功能，遵循[RFC 9111](https://www.rfc-editor.org/rfc/rfc9111.html)协议，支持独立配置缓存策略与持久化存储路径，实现内存、磁盘双重缓存管理，并提供自定义缓存拦截器能力。

## 约束与限制

HTTP缓存基本功能能力支持Phone、2in1、Tablet、Wearable、TV设备。

## 使用HTTP缓存

在需要频繁获取网络热点数据的场景下，网络请求耗时在总时长中占比较大。开发者可以通过创建[ResponseCache](../harmonyos-references/remote-communication-rcp.md#responsecache)实例，并将其配置到Session中，即可使用HTTP缓存功能，提升资源加载性能。

1. 导入模块。

   ```
   1. import { rcp } from '@kit.RemoteCommunicationKit';
   ```
2. 创建[ResponseCache](../harmonyos-references/remote-communication-rcp.md#responsecache)实例。其中，pathToFolder即HTTP缓存响应记录文件路径，“/path/dir“请根据实际情况替换为想要存储HTTP缓存的沙箱路径。

   ```
   1. const responseCache = new rcp.ResponseCache({
   2. persistent: {
   3. kind: 'file-system',
   4. pathToFolder: "/path/dir" // 请根据自身业务选择合适的路径
   5. }
   6. });
   ```
3. 创建会话。在创建Session时，传入responseCache实例。

   ```
   1. const session: rcp.Session = rcp.createSession({
   2. requestConfiguration: {
   3. cache: responseCache
   4. }
   5. });
   ```
4. 发起第一次请求。“https://www.example.com”请根据实际情况替换为支持HTTP缓存协议的URL。本次请求将会从网络服务器获取数据，此时可查看缓存状态信息，若HTTP缓存成功，此时缓存条数应当为1。

   ```
   1. const responseA = await session.get('https://www.example.com');
   2. console.info(`Request succeeded, message is ${JSON.stringify(responseA)}`);
   3. let cacheState = await responseCache.getState();
   4. console.info(`The current number of cache entries is: ${cacheState.count}`);
   ```
5. 发起第二次请求。由于上次请求将会把响应存储到缓存中，第二次请求将会直接从缓存中获取响应。此时可查看缓存状态信息，此时缓存命中数应当为1。

   ```
   1. const responseB = await session.get('https://www.example.com');
   2. console.info(`Request succeeded, message is ${JSON.stringify(responseB)}`);
   3. cacheState = await responseCache.getState();
   4. console.info(`The current cache hit count is: ${cacheState.hitCount}`);
   ```

## 配置缓存过期策略

Remote Communication Kit提供了丰富的缓存过期策略配置项供开发者使用，包括永不过期、绝对时间、相对时间以及滑动时间过期策略，具体API说明详见[接口文档](../harmonyos-references/remote-communication-rcp.md#expirationpolicy)。开发者可以根据业务特性选择不同的缓存过期策略，灵活调整缓存生命周期。下面以相对时间过期策略配置为例，讲述如何配置缓存过期策略，并体会对应的缓存逻辑。

1. 导入模块。

   ```
   1. import { rcp } from '@kit.RemoteCommunicationKit';
   ```
2. 创建[ResponseCache](../harmonyos-references/remote-communication-rcp.md#responsecache)实例。其中，pathToFolder即HTTP缓存响应记录文件路径，”/path/dir”请根据实际情况替换为想要存储HTTP缓存的沙箱路径。defaultExpirationPolicy即默认过期策略，示例代码中配置了时间间隔3秒的相对时间过期策略，具体API说明详见[RelativeTimeExpirationPolicy](../harmonyos-references/remote-communication-rcp.md#relativetimeexpirationpolicy)。

   ```
   1. const responseCache = new rcp.ResponseCache({
   2. persistent: {
   3. kind: 'file-system',
   4. pathToFolder: "/path/dir" // 请根据自身业务选择合适的路径
   5. },
   6. // 过期策略配置，可根据业务特性进行选择
   7. defaultExpirationPolicy: {
   8. kind: 'relative',
   9. time: {
   10. units: 'seconds',
   11. value: 3,
   12. }
   13. }
   14. });
   ```
3. 创建会话。在创建Session时，传入responseCache实例。

   ```
   1. const session: rcp.Session = rcp.createSession({
   2. requestConfiguration: {
   3. cache: responseCache
   4. }
   5. });
   ```
4. 发起第一次请求。“https://www.example.com”请根据实际情况替换为支持HTTP缓存协议的URL。本次请求将会从网络服务器获取数据，此时可查看缓存状态信息，若HTTP缓存成功，此时缓存条数应当为1。

   ```
   1. const responseA = await session.get('https://www.example.com');
   2. console.info(`Request succeeded, message is ${JSON.stringify(responseA)}`);
   3. let cacheState = await responseCache.getState();
   4. console.info(`The current number of cache entries is: ${cacheState.count}`);
   ```
5. 定义sleep延时函数，并延时4秒。由于配置的缓存过期策略为3秒，此时若延时4秒，步骤4中存储的缓存记录将会过期。

   ```
   1. // 定义sleep函数，入参timeout单位为ms。
   2. type sleepFn = (a: number) => Promise<null>
   3. const sleep: sleepFn = (timeout) => {
   4. return new Promise(resolve => {
   5. setTimeout(() => {
   6. resolve(null)
   7. }, timeout);
   8. });
   9. };
   10. // 延时4秒，使缓存过期。
   11. await sleep(4000);
   ```
6. 发起第二次请求。由于缓存记录已过期，此时本次请求仍然会去访问网络服务器获取数据，此时缓存命中数应为0。

   ```
   1. const responseB = await session.get('https://www.example.com');
   2. console.info(`Request succeeded, message is ${JSON.stringify(responseB)}`);
   3. cacheState = await responseCache.getState();
   4. console.info(`The current cache hit count is: ${cacheState.hitCount}`);
   ```
