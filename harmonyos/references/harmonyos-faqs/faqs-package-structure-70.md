---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-70
title: 如何通过代码获取Hap包的打包时间
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 如何通过代码获取Hap包的打包时间
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:bf2994460a7943a1e2158d4f1900adfe046120c9814b56a966a5cf2a7e3ec8fb
---

通过hvigor构建脚本实现，打包时将时间写入到一个Json文件，保存到rawfile目录下，然后在APP中直接读取这个文件的内容即可。hvigorfile.ts文件内容：

```ts
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { hvigor } from '@ohos/hvigor';
import * as fileIo from 'fs';
import * as path from 'path';

// Callback function after node evaluation
hvigor.afterNodeEvaluate((hvigorNode) => {
  // Ensure this directory exists
  const resourcesDir = path.join(__dirname, 'entry/src/main/resources/rawfile');
  if (!fileIo.existsSync(resourcesDir)) {
    fileIo.mkdirSync(resourcesDir, { recursive: true });
  }

  // Write the build time into the JSON file
  const now = new Date();
  const buildTime = now.getFullYear() + '-'
    + String(now.getMonth() + 1).padStart(2, '0') + '-'
    + String(now.getDate()).padStart(2, '0') + ' '
    + String(now.getHours()).padStart(2, '0') + ':'
    + String(now.getMinutes()).padStart(2, '0') + ':'
    + String(now.getSeconds()).padStart(2, '0');
  const buildInfo = { 'buildTime': buildTime };
  fileIo.writeFileSync(
    path.join(resourcesDir, 'build_info.json'),
    JSON.stringify(buildInfo, null, 2)
  );
})

export default {
  system: appTasks, /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins: [] /* Custom plugin to extend the functionality of Hvigor. */
}
```
