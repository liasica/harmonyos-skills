---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hp-arkui-use-taskpool-for-web-request
title: "@performance/hp-arkui-use-taskpool-for-web-request"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-use-taskpool-for-web-request
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:439aa163a9fb1e95b14c29835a8f545c1e2a46de651931ea9019b7b213865efe
---

建议网络资源的请求和返回使用taskpool线程池异步处理。

应用内点击完成时延场景下，建议优先修改。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/hp-arkui-use-taskpool-for-web-request": "warn",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
import { http } from '@kit.NetworkKit';
import { BusinessError } from '@ohos.base';
import taskpool from '@ohos.taskpool';

@Concurrent
function processRespTask(err: BusinessError, data: http.HttpResponse) {
  if (!err) {
    console.info('Result:' + data.result);
    console.info('code:' + data.responseCode);
    console.info('type:' + JSON.stringify(data.resultType));
    console.info('header:' + JSON.stringify(data.header));
    console.info('cookies:' + data.cookies);
  } else {
    console.info('error:' + JSON.stringify(err));
  }
}

let httpRequest = http.createHttp();
httpRequest.request("EXAMPLE_URL", async (err: Error, data: http.HttpResponse) => {
  let task = new taskpool.Task(processRespTask, data);
  await taskpool.execute(task);
});
```

## 反例

```screen
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.request("EXAMPLE_URL", (err: Error, data: http.HttpResponse) => {
  if (!err) {
    console.info('Result:' + data.result);
    console.info('code:' + data.responseCode);
    console.info('type:' + JSON.stringify(data.resultType));
    console.info('header:' + JSON.stringify(data.header));
    console.info('cookies:' + data.cookies); 
  } else {
    console.info('error:' + JSON.stringify(err));
  }
});
```

## 规则集

```screen
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
