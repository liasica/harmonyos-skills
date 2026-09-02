---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-182
title: 推包调试报错“Error message:cannot find record '&XXX/src/main/ets/YYY&x.y.z', please check the request path.'ZZZ.abc'.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 推包调试报错“Error message:cannot find record '&XXX/src/main/ets/YYY&x.y.z', please check the request path.'ZZZ.abc'.”
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:32e1d01c381fa967a0b66b032af9959dde5c3d41e5e922ca7b515ff937c3d0ef
---

**问题现象**

在使用DevEco Studio推包到设备进行调试时，如果遇到jscrash报错，FaultLog中显示“Error message: cannot find record '&XXX/src/main/ets/YYY&x.y.z'，请检查请求路径 'ZZZ.abc'”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/pZECThcaT4O9S3hAGY29rg/zh-cn_image_0000002654798015.png)

**问题原因**

**场景一**

字节码HAR（H）使用的依赖包XXX未配置在本模块的oh-package.json5的dependencies或dynamicDependencies中（错误地配置在了工程级oh-package.json5中），请参考[字节码HAR约束条件](../harmonyos-guides/ide-hvigor-build-har.md#section38518561610)。

**解决措施**

需要字节码HAR（H）的生产方重新出包，将对XXX包的依赖添加到本模块的oh-package.json5中。

**场景二**

用户在工程级oh-package.json5和模块级oh-package.json5中同时依赖了XXX包的不同版本，请参考[字节码HAR约束条件](../harmonyos-guides/ide-hvigor-build-har.md#section38518561610)。

**解决措施：**

措施1：手工修改工程级或模块级oh-package.json5，将XXX的版本调整一致。

措施2：通过工程级oh-package.json5中的overrides字段，覆盖模块中使用的其他版本。

**场景三**

将HSP包转成HAR包后，未删除"packageType"，导致按字节码进行打包的时候未解析其相关依赖，请参考[HSP转HAR指导](../harmonyos-guides/hsp-to-har.md#hsp转har的操作步骤)。

**解决措施**

参考"HSP转HAR指导"中的第四步，将模块的oh-package.json5文件中"packageType": "InterfaceHar" 配置删除。

**场景四**

使用了不兼容的第三方插件或SDK对代码进行了修改（如混淆、加固类的SDK），导致了代码无法识别。

**解决措施**

联系对应三方插件或SDK进行解决，如升级版本。

**场景****五**

应用依赖了包XXX，该XXX包在构建时使用了[增量构建](../harmonyos-guides/ide-hvigor-incremental-build.md)的方式，且同时修改了模块级oh-package.json5中的version字段，导致了XXX包中部分文件在寻址时还是用老的版本号去寻址，进而导致找不到相关文件。

**解决措施**

措施1：在XXX包对应工程中执行**Build > Clean Project**操作，然后重新构建项目。

措施2：在工程级hvigorfile.ts文件中增加插件来修复。

1）在工程根目录下新增plugin.ts文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/A9SzcNmbTgui9x_yAEc1OA/zh-cn_image_0000002624638566.png)

plugin.ts文件内容：

```typescript
import {OhosPluginId, Target} from '@ohos/hvigor-ohos-plugin';
import {hvigor, HvigorNode, HvigorPlugin} from '@ohos/hvigor';
import path from "path";
import fs from "fs";

function getLoaderJsonPath(target: Target) {
  return path.resolve(target.getBuildTargetOutputPath(), `../../intermediates/loader/${target.getTargetName()}/loader.json`);
}

function getPkgContextInfoPath(target: Target) {
  return path.resolve(target.getBuildTargetOutputPath(), `../../intermediates/loader/${target.getTargetName()}/pkgContextInfo.json`);
}

function deleteLoaderJson(target: Target) {
  const loaderJsonPath = getLoaderJsonPath(target);
  if (fs.existsSync(loaderJsonPath)) {
    fs.rmSync(loaderJsonPath);
  }
}

function deletePkgContextInfo(target: Target) {
  const pkgContextInfoPath = getPkgContextInfoPath(target);
  if (fs.existsSync(pkgContextInfoPath)) {
    fs.rmSync(pkgContextInfoPath);
  }
}

function deleteRollupCache(target: Target, buildMode: string) {
  const arkTSCompileCachePath = path.resolve(target.getBuildTargetOutputPath(),
    `../../cache/${target.getTargetName()}/${target.getTargetName()}@HarCompileArkTS/esmodule/${buildMode}/compiler.cache`);
  if (fs.existsSync(arkTSCompileCachePath)) {
    fs.rmSync(arkTSCompileCachePath, { recursive: true });
  }
}

function updateHapHspAbcVersion(subNode: HvigorNode, target: Target) {
  const task = subNode.getTaskByName(`${target.getTargetName()}@GenerateLoaderJson`);
  if (!task) {
    console.log('GenerateLoaderJson not found.');
    return;
  }
  deleteLoaderJson(target);
  deletePkgContextInfo(target);
  task.afterRun(() => {
    const pkgContextInfoPath = getPkgContextInfoPath(target);
    if (!fs.existsSync(pkgContextInfoPath)) {
      console.log('pkgContextInfo not found.');
      return;
    }
    const pkgContextInfoObj = JSON.parse(fs.readFileSync(pkgContextInfoPath).toString());
    if (!pkgContextInfoObj) {
      console.log('pkgContextInfo parse failed.');
      return;
    }
    const loaderJsonPath = getLoaderJsonPath(target);
    if (!fs.existsSync(loaderJsonPath)) {
      console.log('loaderJson not found.');
      return;
    }
    const loaderJsonObj = JSON.parse(fs.readFileSync(loaderJsonPath).toString());
    if (!loaderJsonObj) {
      console.log('loaderJson parse failed.');
      return;
    }
    for (const [key, value] of Object.entries(pkgContextInfoObj)) {
      if (!value?.version) {
        continue;
      }
      if (!loaderJsonObj.updateVersionInfo[key]) {
        loaderJsonObj.updateVersionInfo[key] = {};
      }
      loaderJsonObj.updateVersionInfo[key][key] = value.version;
    }
    fs.writeFileSync(loaderJsonPath, JSON.stringify(loaderJsonObj));
  });
}

function updateHarAbcVersion(target: Target) {
  deleteLoaderJson(target);
  deleteRollupCache(target, 'debug');
  deleteRollupCache(target, 'release');
}

// The user of bytecode har can use this plugin to correctly modify the version number of ohmurl in abc when integrating bytecode har, ensuring no crashes during runtime
export function updateAbcVersionPlugin(): HvigorPlugin {
  return {
    pluginId: 'updateAbcVersionPlugin',
    apply(node: HvigorNode) {
      hvigor.nodesEvaluated(() => {
        hvigor.getRootNode().subNodes(subNode => {
          let context = subNode.getContext(OhosPluginId.OHOS_HAP_PLUGIN);
          if (!context) {
            context = subNode.getContext(OhosPluginId.OHOS_HSP_PLUGIN);
          }
          if (!context) {
            return;
          }
          context.targets(target => {
            updateHapHspAbcVersion(subNode, target);
          });
        });
      });
    }
  };
}

// The generator of bytecode har uses this plugin to incrementally build ohmurl with the correct bytecode har after modifying the version number
export function updateHarAbcVersionPlugin(): HvigorPlugin {
  return {
    pluginId: 'updateHarAbcVersionPlugin',
    apply(node: HvigorNode) {
      hvigor.nodesEvaluated(() => {
        hvigor.getRootNode().subNodes(subNode => {
          const context = subNode.getContext(OhosPluginId.OHOS_HAR_PLUGIN);
          if (!context) {
            return;
          }
          context.targets(target => {
            updateHarAbcVersion(target);
          });
        });
      });
    }
  };
}
```

2）在工程级hvigorfile.ts文件中增加两个插件，并执行Sync。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/ITGHnD0pQXG-SCPSt1qAjg/zh-cn_image_0000002654837971.png)

hvigorfile.ts文件内容：

```typescript
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { updateAbcVersionPlugin, updateHarAbcVersionPlugin } from './plugin.ts';

export default {
    system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
    plugins:[updateAbcVersionPlugin(), updateHarAbcVersionPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

3) 在Terminal终端执行以下命令后，重新推包运行。

```powershell
hvigorw --stop-daemon
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/onHwOjQDRKue1O5_XD-f1g/zh-cn_image_0000002624478660.png)
