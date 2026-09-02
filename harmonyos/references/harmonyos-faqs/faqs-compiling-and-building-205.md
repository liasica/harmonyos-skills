---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-205
title: 基于hvigorfile.ts自定义打包文件名，如何删除同文件夹存在的安装包
breadcrumb: FAQ > DevEco Studio > 编译构建 > 基于hvigorfile.ts自定义打包文件名，如何删除同文件夹存在的安装包
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:206d36620a137bfe2572bb653957a5383e1c13b798bcc468b18d2cde1c6513e5
---

## 问题现象

目前使用如下代码在打包时自定义包名，但是由于每次打包的包名都不一样，导致老的包一直存在打包路径下，请问如何能做到删除旧的构建产物？

## 背景知识

Hvigor支持灵活定制编译，用户可以在hvigorfile.ts文件中开发[自定义任务](../harmonyos-guides/ide-hvigor-task.md)和[自定义插件](../harmonyos-guides/ide-hvigor-plugin.md)。

## 解决方案

可以参考如下代码中的deleteOldApp()方法，在构建之前遍历目标文件夹，删除旧的目标产物。

```ts
import { appTasks , OhosPluginId} from '@ohos/hvigor-ohos-plugin';
import { hvigor } from '@ohos/hvigor'
import * as fs from 'fs';
import * as path from 'path';

// 定义要删除的文件路径和文件格式
const dir = 'D:/Program/HarmonyProject/XXXXXX'; // 替换为你的目标路径
const ext = '.app'; // 要删除的文件格式
hvigor.afterNodeEvaluate((hvigorNode)=>{
    const context = hvigorNode.getContext(OhosPluginId.OHOS_APP_PLUGIN)
    if (context && context.getBuildProfileOpt) {
        const buildProfile = context.getBuildProfileOpt();
        const products = buildProfile.app.products;
        deleteOldApp(dir, ext)
        for (const product of products) {
            if (product.name === context.getCurrentProduct().productBuildOpt.name) {
                product.output={
                    "artifactName": "app-v1.0.3-" + getTime()
                }
            }
        }
        context.setBuildProfileOpt(buildProfile);
    }
})

function deleteOldApp(dir: string, ext: string): void {
    if (!fs.existsSync(dir)) {
        console.error(`Directory does not exist: ${dir}`);
        return;
    }
    fs.readdir(dir, { withFileTypes: true }, (err, files) => {
        if (err) {
            console.error(`Error occurred while reading directory ${dir}:`, err);
            return;
        }
        files.forEach(file => {
            console.info(file.name)
            const filePath = path.join(dir, file.name);
            if (file.name.endsWith(ext)) {
                // 如果是目标文件，删除
                fs.unlink(filePath, err => {
                    if (err) {
                        console.error(`Error occurred while deleting file ${filePath}:`, err);
                    } else {
                        console.info(`Deleted file: ${filePath}`);
                    }
                });
            }
        });
    });
}

function getTime(): string {
    let date = new Date()
    let year = date.getFullYear()
    let month = (date.getMonth() + 1).toString().padStart(2, '0')
    let day = date.getDate().toString().padStart(2, '0')
    let hours = date.getHours().toString().padStart(2, '0')
    let minutes = date.getMinutes().toString().padStart(2, '0')
    return `${year}-${month}-${day}_${hours}_${minutes}`
}

export default {
    system: appTasks, /* Built-in plugin of Hvigor. It cannot be modified. */
    plugins:[] /* Custom plugin to extend the functionality of Hvigor. */
}
```
