---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-104
title: 如何在构建任务中执行shell脚本
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何在构建任务中执行shell脚本
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:29+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:46584095488c47a4cf1c29c0b1dcc8f2b9aedea77eccd5be09f9b940eb63ad1a
---

在hvigorfile.ts文件中执行如下示例：

```
1. import { harTasks } from '@ohos/hvigor-ohos-plugin';
2. import { exec } from 'node:child_process';
3. import util from 'node:util';

5. const scriptPath = 'xxxx.bat';

7. export function customPluginFunction1(str?: string) {
8. return {
9. pluginId: 'CustomPluginID1',
10. apply(pluginContext) {
11. pluginContext.registerTask({
12. // Write a custom task
13. name: 'customTask1',
14. run: (taskContext) => {
15. console.log('run into: ');
16. const execPromise = util.promisify(exec)
17. execPromise(scriptPath).then(res => {
18. console.log(res, 'res');
19. }).catch(err => {
20. console.log(err, 'err');
21. })
22. },
23. // Confirm custom task insertion position
24. dependencies: ['default@BuildJS'],
25. postDependencies: ['default@CompileArkTS']
26. })
27. }
28. }
29. }

31. export default {
32. system: harTasks, /* Built-in plugin of Hvigor. It cannot be modified. */
33. plugins: [customPluginFunction1()] /* Custom plugin to extend the functionality of Hvigor. */
34. }
```

[hvigorfile.ts](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CompilingAndBuilding/library3/hvigorfile.ts#L3-L36)
