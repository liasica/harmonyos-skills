---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-208
title: Hvigor编译构建实现添加自定义文件至.har产物中
breadcrumb: FAQ > DevEco Studio > 编译构建 > Hvigor编译构建实现添加自定义文件至.har产物中
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b180e265f6a87b77df183616c0c67cfb16933389c1ec0d1adc322db938413260
---

## 问题现象

如何在对模块进行编译时，将自定义的目录文件，例如.ets文件、.log文件等，动态打包进最终的.har产物中。

## 背景知识

[开发Hvigor插件](../harmonyos-guides/ide-hvigor-plugin.md)：Hvigor允许开发者实现自己的插件，开发者可以定义自己的构建逻辑，并与他人共享。Hvigor主要提供了两种方式来开发插件：基于hvigorfile脚本开发插件、基于typescript项目开发。

## 解决方案

目前以以下方式基于Hvigor构建HAR模块时，Hvigor内部会采用白名单模式，只有匹配到的文件，才会被打包进最终的.har产物中，场景需要满足如下条件：

* “Build Mode”为[release模式](../harmonyos-guides/ide-hvigor-build-har.md#section19788284410)，且开启混淆；
* 构建字节码HAR；

在这些场景下，如果您想要将一些其他的文件也打包进去，可以使用自定义插件配合自定义任务进行处理。

比如一个名称为har01的HAR模块，其目录结构如下：

* 模块根目录下新建文件夹interface，interface文件夹中新建文件Index.d.ets、Test.d.ets。
* 模块根目录下新建文件夹logs，logs文件夹下新建文件夹hilogs和hvigor.log文件，hilogs文件夹下新建文件build.log、test.txt。

如果您需要将以下文件打包进最终的.har产物中：

* interface文件夹。
* logs文件夹下的.log文件。

可以编写har01模块的hvigorfile.ts文件如下：

```ts
import { harTasks, OhosHarContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor, getNode } from '@ohos/hvigor';
import path from 'path';
import fs from 'fs';

// 基于hvigor钩子实现添加自定义文件至.har产物中:
function copyFolder(source: string, target: string, excludeExts: string[] = []): void {
  // 检查目标文件夹是否存在，如果不存在则创建
  if (!fs.existsSync(target)) {
    fs.mkdirSync(target, { recursive: true });
  }

  // 读取源文件夹中的文件和文件夹
  const entries = fs.readdirSync(source, { withFileTypes: true });

  for (const entry of entries) {
    const srcPath = path.join(source, entry.name);
    const destPath = path.join(target, entry.name);

    if (entry.isDirectory()) {
      // 如果是文件夹，则递归调用
      copyFolder(srcPath, destPath, excludeExts);
    } else if (entry.isFile() && !excludeExts.includes(path.extname(entry.name))) {
      // 如果是文件，则复制文件
      fs.copyFileSync(srcPath, destPath);
    }
  }
}

hvigor.nodesEvaluated(() => {
  const node = getNode(__filename);
  const context = node.getContext(OhosPluginId.OHOS_HAR_PLUGIN) as OhosHarContext;
  if (!context) {
    return;
  }
  context.targets((target: Target) => {
    const targetName = target.getTargetName();
    const modulePath = context.getModulePath();
    const outputPath = target.getBuildTargetOutputPath();
    const task = node.getTaskByName(`${targetName}@ProcessHarArtifacts`);
    task.afterRun(() => {
      const packageHarDir = path.resolve(outputPath, '../../', 'cache', targetName, `${targetName}@PackageHar`);

      copyFolder(path.join(modulePath, 'interface'), path.join(packageHarDir, 'interface'));
      copyFolder(path.join(modulePath, 'logs'), path.join(packageHarDir, 'logs'), ['.txt']);
    });
  });
});

export default {
  system: harTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```
