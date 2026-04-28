---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hp-arkui-use-taskpool-for-web-request
title: @performance/hp-arkui-use-taskpool-for-web-request
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-use-taskpool-for-web-request
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:10+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:4a67907e2bc557af294b8c9867e8719e21b68baa6648cc4302303263675a9763
---

建议网络资源的请求和返回使用taskpool线程池异步处理。

应用内点击完成时延场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-arkui-use-taskpool-for-web-request": "warn",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import { http } from '@kit.NetworkKit';
2. import { BusinessError } from '@ohos.base';
3. import taskpool from '@ohos.taskpool';

5. @Concurrent
6. function processRespTask(err: BusinessError, data: http.HttpResponse) {
7. if (!err) {
8. console.info('Result:' + data.result);
9. console.info('code:' + data.responseCode);
10. console.info('type:' + JSON.stringify(data.resultType));
11. console.info('header:' + JSON.stringify(data.header));
12. console.info('cookies:' + data.cookies);
13. } else {
14. console.info('error:' + JSON.stringify(err));
15. }
16. }

18. let httpRequest = http.createHttp();
19. httpRequest.request("EXAMPLE_URL", async (err: Error, data: http.HttpResponse) => {
20. let task = new taskpool.Task(processRespTask, data);
21. await taskpool.execute(task);
22. });
```

## 反例

```
1. import { http } from '@kit.NetworkKit';

3. let httpRequest = http.createHttp();
4. httpRequest.request("EXAMPLE_URL", (err: Error, data: http.HttpResponse) => {
5. if (!err) {
6. console.info('Result:' + data.result);
7. console.info('code:' + data.responseCode);
8. console.info('type:' + JSON.stringify(data.resultType));
9. console.info('header:' + JSON.stringify(data.header));
10. console.info('cookies:' + data.cookies);
11. } else {
12. console.info('error:' + JSON.stringify(err));
13. }
14. });
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
