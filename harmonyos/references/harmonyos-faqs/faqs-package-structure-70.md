---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-70
title: 如何通过代码获取Hap包的打包时间
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 如何通过代码获取Hap包的打包时间
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:39+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:b4779290087c018168f664504cd4c4cd97e5c1e83764da98ac49d66a33883d89
---

通过hvigor构建脚本实现，打包时将时间写入到一个Json文件，保存到rawfile目录下，然后在APP中直接读取这个文件的内容即可。hvigorfile.ts文件内容：

```
1. import { appTasks } from '@ohos/hvigor-ohos-plugin';
2. import { hvigor } from '@ohos/hvigor';
3. import * as fileIo from 'fs';
4. import * as path from 'path';

6. // Callback function after node evaluation
7. hvigor.afterNodeEvaluate((hvigorNode) => {
8. // Ensure this directory exists
9. const resourcesDir = path.join(__dirname, 'entry/src/main/resources/rawfile');
10. if (!fileIo.existsSync(resourcesDir)) {
11. fileIo.mkdirSync(resourcesDir, { recursive: true });
12. }

14. // Write the build time into the JSON file
15. const now = new Date();
16. const buildTime = now.getFullYear() + '-'
17. + String(now.getMonth() + 1).padStart(2, '0') + '-'
18. + String(now.getDate()).padStart(2, '0') + ' '
19. + String(now.getHours()).padStart(2, '0') + ':'
20. + String(now.getMinutes()).padStart(2, '0') + ':'
21. + String(now.getSeconds()).padStart(2, '0');
22. const buildInfo = { 'buildTime': buildTime };
23. fileIo.writeFileSync(
24. path.join(resourcesDir, 'build_info.json'),
25. JSON.stringify(buildInfo, null, 2)
26. );
27. })

29. export default {
30. system: appTasks, /* Built-in plugin of Hvigor. It cannot be modified. */
31. plugins: [] /* Custom plugin to extend the functionality of Hvigor. */
32. }
```

[hvigorfile.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/PackageStructureKit/hvigorfile.ts#L17-L48)
