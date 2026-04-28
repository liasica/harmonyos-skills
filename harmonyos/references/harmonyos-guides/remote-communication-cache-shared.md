---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/remote-communication-cache-shared
title: Session间缓存共享
breadcrumb: 指南 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > 提升HTTP传输性能 > 使用HTTP缓存功能提升资源获取性能 > Session间缓存共享
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:62547e986701a9fa1895e2c8f4de75e136c57f4216720962d99fff3d0a5de71c
---

从6.0.0(20)开始，支持Session间缓存共享。

Session之间数据是隔离的，当业务场景需要实现跨Session访问缓存数据时，可通过以下两种标准方式达成目标：

* 引用相同的HTTP响应缓存实例，不同Session能直接访问同一缓存池中的数据；
* 配置相同的缓存存储路径，使各个Session基于同一存储位置读写缓存，以此实现缓存数据的跨Session共享与交互。

## 约束与限制

Session间缓存共享能力支持Phone、2in1、Tablet、Wearable、TV设备。

## 引用相同HTTP响应缓存实例

创建一个[ResponseCache](../harmonyos-references/remote-communication-rcp.md#responsecache)实例，将其配置到不同Session中，可以在Session间共享缓存数据。

1. 导入模块。

   ```
   1. import { rcp } from '@kit.RemoteCommunicationKit';
   ```
2. 创建[ResponseCache](../harmonyos-references/remote-communication-rcp.md#responsecache)实例。其中，pathToFolder即缓存记录文件路径，”/path/dir”请根据实际情况替换为想要存储HTTP缓存的沙箱路径。

   ```
   1. const responseCache = new rcp.ResponseCache({
   2. persistent: {
   3. kind: 'file-system',
   4. pathToFolder: "/path/dir" // 请根据自身业务选择合适的路径
   5. }
   6. });
   ```
3. 创建SessionA和SessionB。配置responseCache实例到SessionA和SessionB中。

   ```
   1. const sessionA: rcp.Session = rcp.createSession({
   2. requestConfiguration: {
   3. cache: responseCache
   4. }
   5. });
   6. const sessionB: rcp.Session = rcp.createSession({
   7. requestConfiguration: {
   8. cache: responseCache
   9. }
   10. });
   ```
4. 由SessionA发起第一次请求。“https://www.example.com”请根据实际情况替换为支持HTTP缓存协议的URL。本次请求将会从网络服务器获取数据，此时可查看缓存状态信息，此时缓存条数应当为1。

   ```
   1. const responseA = await sessionA.get('https://www.example.com');
   2. console.info(`Request succeeded, message is ${JSON.stringify(responseA)}`);
   3. let cacheState = await responseCache.getState();
   4. console.info(`The current number of cache entries is: ${cacheState.count}`);
   ```
5. 由SessionB发起第二次请求。“https://www.example.com”请根据实际情况替换为支持HTTP缓存协议的URL。本次请求将会直接从缓存中获取响应，此时可查看缓存状态信息，此时缓存命中数应当为1。

   ```
   1. const responseB = await sessionB.get('https://www.example.com');
   2. console.info(`Request succeeded, message is ${JSON.stringify(responseB)}`);
   3. cacheState = await responseCache.getState();
   4. console.info(`The current cache hit count is: ${cacheState.hitCount}`);
   ```

## 配置相同缓存存储路径

创建不同的[ResponseCache](../harmonyos-references/remote-communication-rcp.md#responsecache)实例，但对应缓存存储路径相同，将ResponseCache实例配置到不同Session中，可以在Session间共享缓存数据。

1. 导入模块。

   ```
   1. import { rcp } from '@kit.RemoteCommunicationKit';
   ```
2. 创建ResponseCacheA和ResponseCacheB实例，两者对应缓存存储路径相同。其中，pathToFolder即HTTP缓存响应记录文件路径，”/path/dir”请根据实际情况替换为想要存储HTTP缓存的沙箱路径。

   ```
   1. const responseCacheA = new rcp.ResponseCache({
   2. persistent: {
   3. kind: 'file-system',
   4. pathToFolder: "/path/dir" // 请根据自身业务选择合适的路径
   5. }
   6. });
   7. const responseCacheB = new rcp.ResponseCache({
   8. persistent: {
   9. kind: 'file-system',
   10. pathToFolder: "/path/dir" // 请根据自身业务选择合适的路径
   11. }
   12. });
   ```
3. 创建SessionA和SessionB。配置responseCacheA实例到SessionA，配置responseCacheB实例到SessionB中。

   ```
   1. const sessionA: rcp.Session = rcp.createSession({
   2. requestConfiguration: {
   3. cache: responseCacheA
   4. }
   5. });
   6. const sessionB: rcp.Session = rcp.createSession({
   7. requestConfiguration: {
   8. cache: responseCacheB
   9. }
   10. });
   ```
4. 由SessionA发起第一次请求。“https://www.example.com”请根据实际情况替换为支持HTTP缓存协议的URL。本次请求将会从网络服务器获取数据，此时可查看responseCacheA的缓存状态信息，此时缓存条数应当为1。

   ```
   1. const responseA = await sessionA.get('https://www.example.com');
   2. console.info(`Request succeeded, message is ${JSON.stringify(responseA)}`);
   3. let cacheState = await responseCacheA.getState();
   4. console.info(`The current number of cache entries is: ${cacheState.count}`);
   ```
5. 由SessionB发起第二次请求。“https://www.example.com”请根据实际情况替换为支持HTTP缓存协议的URL。本次请求将会直接从缓存中获取响应，此时可查看responseCacheB的缓存状态信息，此时缓存条数和缓存命中数均应当为1。

   ```
   1. const responseB = await sessionB.get('https://www.example.com');
   2. console.info(`Request succeeded, message is ${JSON.stringify(responseB)}`);
   3. cacheState = await responseCacheB.getState();
   4. console.info(`The current number of cache entries is: ${cacheState.count}`);
   5. console.info(`The current cache hit count is: ${cacheState.hitCount}`);
   ```
